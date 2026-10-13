"""Coleta da SQ1 nas APIs VuFind do OASISBR (IBICT) e da LA Referencia (emendas v1.1 e v1.2).

Consulta: blocos congelados SQ1-AL #1 (exposição) AND #2 (desfecho), lidos de
`calibracao/sq1-america-latina-final.json` por `blocos_al()` + `carrega()` de
`coleta_openalex.py`, sem redigitação. Sem o #3 (geografia): as duas fontes já são
brasileira e latino-americana (emenda v1.1).

Fatiamento. Como (E1 OR E2) AND (O1 OR O2) = U_ij (Ei AND Oj), os termos de #1 e #2
são repartidos em fatias, e os registros das fatias são unidos por `id`. O `--plano`
confere, sem rede, que as fatias cobrem exatamente os termos dos blocos.
- LA Referencia: fatias com URL < LIMITE_URL. A API aceita a consulta inteira, e a
  união das fatias tem de bater com a chamada única; se não bater, para sem gravar.
- OASISBR (emenda v1.2): a API recusa consulta booleana com ~10 termos ou mais (HTTP
  403, regra de firewall) e depois bloqueia o IP. Fatias de no máximo MAX_TERMOS
  termos de cada lado, pausa de PAUSA["oasisbr"] s e parada no primeiro 403. A coleta
  é retomável: cada fatia concluída vai para `data/raw/.../oasisbr-progresso.jsonl`,
  e uma nova execução pula as já feitas. Sem chamada única possível, a conferência é
  a cobertura: todo registro brasileiro (`BR_`) da LA Referencia, que é subconjunto
  do OASISBR, tem de reaparecer na união (mínimo COBERTURA_MIN, por título normalizado).

Rodar de docs/revisao-sistematica:

    python3 ferramentas/coleta_vufind.py --plano      # fatias e tamanhos de URL, sem rede
    python3 ferramentas/coleta_vufind.py --conferir --amostra 3   # só contagens, sem gravar
    python3 ferramentas/coleta_vufind.py              # coleta as duas fontes
    python3 ferramentas/coleta_vufind.py --fontes oasisbr   # só o OASISBR; a LA Referencia
                                                            # entra no Apêndice pelo CSV versionado
    python3 ferramentas/coleta_vufind.py --reidratar  # refaz o JSONL a partir dos IDs versionados

Saídas: `registros/vufind-<fonte>-sq1.csv` (metadados + SHA-256 do resumo), resumo em
`data/raw/revisao-sistematica/`, log em `registros/coletas.jsonl` (uma linha por
fatia e uma de resumo por fonte) e `ferramentas/vufind.md` (linhas congeladas do
Apêndice A, com contagens e recall dos itens conhecidos).
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import unicodedata
from urllib.parse import urlencode, urlsplit

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coleta_openalex import BASE, BRUTO, REG, blocos_al, carrega, loga, sha  # noqa: E402

FONTES = {
    "oasisbr": "https://oasisbr.ibict.br/vufind/api/v1/search",
    "lareferencia": "https://buscador.lareferencia.info/api/v1/search",
}
NOME_FONTE = {"oasisbr": "OASISBR", "lareferencia": "LA Referencia"}
CAMPOS_API = ["id", "title", "formats", "languages", "publicationDates", "summary", "primaryAuthors", "urls"]
LIMITE_URL = 1800
POR_PAGINA = 100
PAUSA = {"oasisbr": 3.0, "lareferencia": 0.5}
TENTATIVAS = {"oasisbr": 2, "lareferencia": 5}
# Teste de 2026-10-13, de IP residencial: a API do OASISBR devolve 403 a consultas booleanas com
# ~10 termos ou mais, mesmo com URL de 459 caracteres (5 termos de cada lado passam), e depois
# recusa conexões do IP por um tempo. É regra de firewall, não limite de URL (emenda v1.2).
MAX_TERMOS = {"oasisbr": 5}
COBERTURA_MIN = 0.95
BLOCO, LINHA = "sq1-america-latina", "VuFind #1 AND #2"
OASISBR_BLOQUEIO = ("A API recusa consulta booleana com ~10 termos ou mais (HTTP 403, regra de firewall, não "
                    "tamanho de URL) e depois bloqueia o IP por um tempo; 5 termos de cada lado passam.")
PROGRESSO = os.path.join(BRUTO, "oasisbr-progresso.jsonl")


class Bloqueio(RuntimeError):
    """403 ou conexão recusada no OASISBR: parar, guardar o progresso e retomar mais tarde."""

# O ID VuFind ("ES_<32 hex>") vai em duas colunas: inteiro, o ID de registro espanhol tem o
# formato da chave secreta do hCaptcha, e o push protection do GitHub bloqueia o CSV. `id_vufind()`
# remonta o ID.
CAMPOS = ["fonte", "bloco", "linha", "posicao", "vufind_pais", "vufind_hash", "doi", "titulo", "ano", "formato",
          "idioma", "primeiro_autor", "fatias", "url", "tem_resumo", "n_car_resumo", "sha256_resumo"]


def termos(bloco):
    """'a OR "b c" OR d' -> ['a', '"b c"', 'd']; o bloco é uma lista plana de OR."""
    assert "(" not in bloco and ")" not in bloco, "bloco com parênteses: o fatiamento supõe OR plano"
    ts = bloco.split(" OR ")
    assert all(t and t == t.strip() for t in ts), "termo vazio ou com espaço sobrando"
    assert all(t.count('"') in (0, 2) for t in ts), "aspas desbalanceadas"
    return ts


def consulta(e, o):
    return f"({' OR '.join(e)}) AND ({' OR '.join(o)})"


def params(lookfor, pagina=1, limite=POR_PAGINA):
    return [("lookfor", lookfor), ("type", "AllFields"), ("limit", limite), ("page", pagina)] + \
           [("field[]", c) for c in CAMPOS_API]


def tamanho_url(api, e, o):
    return len(api + "?" + urlencode(params(consulta(e, o), pagina=99)))


def empacota(ts, cabe):
    """Fatias contíguas, gulosas, de termos que cabem; falha se um termo sozinho não couber."""
    out, cur = [], []
    for t in ts:
        if cur and not cabe(cur + [t]):
            out.append(cur)
            cur = []
        assert cabe(cur + [t]), f"termo {t!r} não cabe sozinho"
        cur.append(t)
    return out + [cur] if cur else out


def fatias(fonte, e, o):
    """OASISBR: fatias de no máximo MAX_TERMOS termos de cada lado. Demais fontes: as fatias de
    #1 e #2 que minimizam o número de chamadas com URL < LIMITE_URL."""
    api = FONTES[fonte]
    if fonte in MAX_TERMOS:
        n = MAX_TERMOS[fonte]
        fe, fo = empacota(e, lambda c: len(c) <= n), empacota(o, lambda c: len(c) <= n)
        assert all(tamanho_url(api, a, b) < LIMITE_URL for a in fe for b in fo), "fatia acima do limite de URL"
        return [{"rotulo": f"E{i + 1}xO{j + 1}", "e": a, "o": b} for i, a in enumerate(fe) for j, b in enumerate(fo)]
    melhor = None
    for corte in range(1, len(e) + 1):
        fe = empacota(e, lambda c: len(c) <= corte)
        maior_e = max(fe, key=lambda c: tamanho_url(api, c, []))
        try:
            fo = empacota(o, lambda c: tamanho_url(api, maior_e, c) < LIMITE_URL)
        except AssertionError:
            continue
        if any(tamanho_url(api, a, b) >= LIMITE_URL for a in fe for b in fo):
            continue
        n = len(fe) * len(fo)
        if melhor is None or n < melhor[0]:
            melhor = (n, fe, fo)
    assert melhor, "nenhum fatiamento cabe no limite de URL"
    _, fe, fo = melhor
    return [{"rotulo": f"E{i + 1}xO{j + 1}", "e": a, "o": b} for i, a in enumerate(fe) for j, b in enumerate(fo)]


def plano():
    b = blocos_al(carrega(BLOCO))
    e, o = termos(b["#1"]), termos(b["#2"])
    out = {}
    for fonte in FONTES:
        fs = fatias(fonte, e, o)
        # A união dos termos das fatias é exatamente o bloco, na mesma ordem e sem repetição.
        for lado, ts in (("e", e), ("o", o)):
            vistos = []
            for f in fs:
                if f[lado] not in vistos:
                    vistos.append(f[lado])
            assert [t for c in vistos for t in c] == ts, f"{fonte}: fatias de {lado} ≠ bloco"
        assert {(tuple(f["e"]), tuple(f["o"])) for f in fs} == \
               {(tuple(a["e"]), tuple(c["o"])) for a in fs for c in fs}, f"{fonte}: produto incompleto"
        out[fonte] = fs
    return e, o, out


def fonte_de(api):
    host = urlsplit(api).netloc
    return next(f for f, u in FONTES.items() if urlsplit(u).netloc == host)


def get(api, ps):
    fonte = fonte_de(api)
    tentativas = TENTATIVAS[fonte]
    for k in range(tentativas):
        time.sleep(PAUSA[fonte])
        try:
            r = requests.get(api, params=ps, timeout=120)
        except requests.RequestException as ex:
            print(f"  tentativa {k + 1}: {ex!r}", file=sys.stderr)
            if fonte == "oasisbr" and k + 1 == tentativas:
                raise Bloqueio(f"OASISBR: conexão recusada ({ex!r})")
            time.sleep(2 ** (k + 1))
            continue
        if r.status_code == 403 and fonte == "oasisbr":
            raise Bloqueio(f"OASISBR: HTTP 403 (URL de {len(r.url)} car.)")
        if r.status_code == 200:
            d = r.json()
            if d.get("status") != "OK":
                raise RuntimeError(f"status {d.get('status')}: {str(d)[:300]}")
            return d
        if r.status_code in (400, 403, 414):
            raise RuntimeError(f"HTTP {r.status_code} (URL de {len(r.url)} car.): {r.text[:300]}")
        print(f"  tentativa {k + 1}: HTTP {r.status_code} {r.text[:200]}", file=sys.stderr)
        time.sleep(2 ** (k + 1))
    raise RuntimeError(f"{tentativas} tentativas falharam")


def conta(api, lookfor):
    return get(api, params(lookfor, limite=0))["resultCount"]


DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s\"<>|&\\]+)", re.I)


def doi_de(urls):
    for u in urls or []:
        u = u.get("url", "") if isinstance(u, dict) else str(u)
        m = re.search(r"doi\.org/(10\.[^\s?#]+)", u, re.I)
        if m:
            return m.group(1).rstrip(".,;)").lower()
    return ""


def achata(rec):
    def um(c):
        v = rec.get(c) or []
        return v[0] if isinstance(v, list) and v else (v if isinstance(v, str) else "")
    urls = rec.get("urls") or []
    autores = rec.get("primaryAuthors") or []
    return {
        "vufind_id": rec["id"],
        "doi": doi_de(urls),
        "titulo": " ".join((rec.get("title") or "").split()),
        "ano": um("publicationDates"),
        "formato": "|".join(rec.get("formats") or []),
        "idioma": "|".join(rec.get("languages") or []),
        "primeiro_autor": autores[0] if autores else "",
        "url": (urls[0].get("url", "") if isinstance(urls[0], dict) else str(urls[0])) if urls else "",
        "resumo": " ".join(" ".join(rec.get("summary") or []).split()),
    }


def baixa_fatia(api, f):
    q = consulta(f["e"], f["o"])
    regs, pagina, total = {}, 1, None
    while True:
        d = get(api, params(q, pagina))
        total = d["resultCount"]
        recs = d.get("records") or []
        for r in recs:
            regs.setdefault(r["id"], r)
        if not recs or pagina * POR_PAGINA >= total:
            break
        pagina += 1
    if len(regs) != total:
        raise RuntimeError(f"fatia {f['rotulo']}: {len(regs)} ids distintos para {total} resultados")
    return regs, total


def agora_utc():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def progresso_feito(fs):
    """Fatias do OASISBR já baixadas numa execução anterior, se a consulta não mudou."""
    if not os.path.exists(PROGRESSO):
        return {}
    por_rotulo = {f["rotulo"]: consulta(f["e"], f["o"]) for f in fs}
    feito = {}
    for l in open(PROGRESSO, encoding="utf-8"):
        p = json.loads(l)
        if por_rotulo.get(p["fatia"]) == p["lookfor"]:
            feito[p["fatia"]] = p
    return feito


def cobertura_lareferencia(uniao):
    """Fração dos registros BR_ da LA Referencia (subconjunto do OASISBR) que reaparecem na união
    do OASISBR, por título normalizado (igual, ou um contido no outro com >= 40 caracteres)."""
    caminho = os.path.join(REG, "vufind-lareferencia-sq1.csv")
    br = [l for l in csv.DictReader(open(caminho, encoding="utf-8")) if l["vufind_pais"] == "BR"]
    tits = {norm(r.get("title")) for r in uniao.values() if r.get("title")}
    prefixos = {t[:40] for t in tits if len(t) >= 40}
    faltam = [l for l in br if norm(l["titulo"]) not in tits and norm(l["titulo"])[:40] not in prefixos]
    return len(br) - len(faltam), len(br), faltam


def coleta(fonte, fs):
    """Baixa todas as fatias e confere; não grava nada (quem grava é o __main__, depois do recall).
    No OASISBR, cada fatia concluída vai para PROGRESSO, e um Bloqueio interrompe a execução."""
    api = FONTES[fonte]
    agora = agora_utc()
    uniao, de_fatia, logs = {}, {}, []
    feito = progresso_feito(fs) if fonte == "oasisbr" else {}
    if feito:
        print(f"  {fonte}: retomando; {len(feito)}/{len(fs)} fatias já baixadas", file=sys.stderr)
    for k, f in enumerate(fs, 1):
        q = consulta(f["e"], f["o"])
        if f["rotulo"] in feito:
            p = feito[f["rotulo"]]
            regs, total, quando = p["registros"], p["total"], p["data_utc"]
        else:
            try:
                regs, total = baixa_fatia(api, f)
            except Bloqueio as ex:
                raise Bloqueio(f"{ex}. Parado na fatia {f['rotulo']} ({k}/{len(fs)}); "
                               f"{k - 1} fatias guardadas em {PROGRESSO}. Esperar e rodar de novo.") from ex
            quando = agora_utc()
            if fonte == "oasisbr":
                os.makedirs(BRUTO, exist_ok=True)
                with open(PROGRESSO, "a", encoding="utf-8") as pf:
                    pf.write(json.dumps({"fatia": f["rotulo"], "lookfor": q, "total": total,
                                         "data_utc": quando, "registros": regs}, ensure_ascii=False) + "\n")
        print(f"  {fonte} {f['rotulo']} ({k}/{len(fs)}): {total}", file=sys.stderr)
        for i, r in regs.items():
            uniao.setdefault(i, r)
            de_fatia.setdefault(i, []).append(f["rotulo"])
        logs.append({"data_utc": quando, "fonte": NOME_FONTE[fonte], "bloco": BLOCO, "linha": LINHA,
                     "papel": "fatia", "fatia": f["rotulo"], "contagem_hoje": total,
                     "n_termos_e": len(f["e"]), "n_termos_o": len(f["o"]), "lookfor": q})
    unica, cobertura = None, None
    if fonte == "oasisbr":
        ok, n, faltam = cobertura_lareferencia(uniao)
        cobertura = f"{ok}/{n}"
        print(f"  cobertura dos BR_ da LA Referencia: {cobertura} ({ok / n:.1%})", file=sys.stderr)
        for l in faltam[:15]:
            print(f"    falta: {l['ano']} {l['formato']} {l['titulo'][:90]}", file=sys.stderr)
        if ok / n < COBERTURA_MIN:
            raise RuntimeError(f"OASISBR: cobertura dos BR_ da LA Referencia {cobertura} abaixo de "
                               f"{COBERTURA_MIN:.0%}. Nada gravado; o progresso fica em {PROGRESSO}.")
    if fonte == "lareferencia":
        b = blocos_al(carrega(BLOCO))
        unica = conta(api, f"({b['#1']}) AND ({b['#2']})")
        if unica != len(uniao):
            raise RuntimeError(f"LA Referencia: união das fatias = {len(uniao)}, chamada única = {unica}. "
                               "Nada gravado; registrar e investigar antes de seguir.")
    regs = [{**achata(r), "fatias": "|".join(de_fatia[i])} for i, r in uniao.items()]
    regs.sort(key=lambda r: r["vufind_id"])
    for k, r in enumerate(regs, 1):
        r["posicao"] = k
    resumo = {"data_utc": agora, "fonte": NOME_FONTE[fonte], "bloco": BLOCO, "linha": LINHA,
              "papel": "conjunto", "n_fatias": len(fs), "soma_fatias": sum(l["contagem_hoje"] for l in logs),
              "uniao": len(uniao), "chamada_unica": unica, "cobertura_lareferencia_br": cobertura,
              "com_resumo": sum(1 for r in regs if r["resumo"]),
              "com_doi": sum(1 for r in regs if r["doi"]),
              "formatos": dict(sorted(_conta(r["formato"] for r in regs).items(), key=lambda kv: -kv[1])),
              "arquivo": f"registros/vufind-{fonte}-sq1.csv"}
    return regs, resumo, logs


def _conta(xs):
    out = {}
    for x in xs:
        out[x or "?"] = out.get(x or "?", 0) + 1
    return out


def separa_id(i):
    if "_" not in i:  # sem prefixo de país/coleção
        return {"vufind_pais": "", "vufind_hash": i}
    pais, hash_ = i.split("_", 1)
    assert pais and hash_ and f"{pais}_{hash_}" == i, i
    return {"vufind_pais": pais, "vufind_hash": hash_}


def id_vufind(linha):
    return f"{linha['vufind_pais']}_{linha['vufind_hash']}" if linha["vufind_pais"] else linha["vufind_hash"]


def carrega_coletada(fonte):
    """Fonte coletada numa execução anterior: registros do CSV versionado (sem resumo) e o
    resumo da coleta do log. Serve ao Apêndice A quando só a outra fonte é coletada agora."""
    caminho = os.path.join(REG, f"vufind-{fonte}-sq1.csv")
    if not os.path.exists(caminho):
        return None, None
    regs = [{**l, "vufind_id": id_vufind(l)} for l in csv.DictReader(open(caminho, encoding="utf-8"))]
    resumo = None
    for l in open(os.path.join(REG, "coletas.jsonl"), encoding="utf-8"):
        d = json.loads(l)
        if d.get("fonte") == NOME_FONTE[fonte] and d.get("papel") == "conjunto":
            resumo = d
    return regs, resumo


def grava(fonte, regs):
    os.makedirs(REG, exist_ok=True)
    os.makedirs(BRUTO, exist_ok=True)
    base = f"vufind-{fonte}-sq1"
    with open(os.path.join(REG, base + ".csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for r in regs:
            w.writerow({"fonte": NOME_FONTE[fonte], "bloco": BLOCO, "linha": LINHA,
                        **{k: r[k] for k in CAMPOS if k in r}, **separa_id(r["vufind_id"]),
                        "tem_resumo": int(bool(r["resumo"])), "n_car_resumo": len(r["resumo"]),
                        "sha256_resumo": sha(r["resumo"])})
    with open(os.path.join(BRUTO, base + ".jsonl"), "w", encoding="utf-8") as f:
        for r in regs:
            f.write(json.dumps({"fonte": NOME_FONTE[fonte], "bloco": BLOCO, "linha": LINHA, **r},
                               ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- recall dos itens conhecidos

def norm(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())


def itens_conhecidos():
    """DOIs dos itens conhecidos da calibração SQ1-AL (sementes, V, X, incidentais, desenvolvimento
    e validação independente), com título e país dos autores pelo OpenAlex."""
    textos = []
    for nome in ("sq1-america-latina", "sq1-america-latina-final"):
        textos.append(json.dumps(json.load(open(os.path.join(BASE, "calibracao", nome + ".json"),
                                                encoding="utf-8")), ensure_ascii=False))
    dois = []
    for d in DOI_RE.findall(" ".join(textos)):
        d = d.rstrip(".,;:)'\\").lower()
        if d not in dois:
            dois.append(d)
    from coleta_openalex import get as oa_get
    meta = {}
    for i in range(0, len(dois), 50):
        lote = dois[i:i + 50]
        res = oa_get({"filter": "doi:" + "|".join(lote), "per-page": 50,
                      "select": "doi,title,publication_year,authorships"})["results"]
        for w in res:
            d = (w.get("doi") or "").lower().replace("https://doi.org/", "")
            paises = {c for a in w.get("authorships") or [] for c in a.get("countries") or []}
            meta[d] = {"titulo": w.get("title") or "", "ano": w.get("publication_year"),
                       "br": "BR" in paises}
    return [{"doi": d, **meta.get(d, {"titulo": "", "ano": None, "br": None})} for d in dois]


def indexado(api, titulo):
    """O item está na fonte? Busca pelas 8 primeiras palavras do título (campo Title) e compara
    os 40 primeiros caracteres normalizados. Separa 'fora da fonte' de 'perdido pela string'."""
    d = get(api, [("lookfor", " ".join(norm(titulo).split()[:8])), ("type", "Title"), ("limit", 5),
                  ("field[]", "id"), ("field[]", "title")])
    return any(norm(r.get("title"))[:40] == norm(titulo)[:40] for r in d.get("records") or [])


def recall(itens, regs, api):
    por_doi = {r["doi"]: r for r in regs if r["doi"]}
    por_tit = {norm(r["titulo"]): r for r in regs if r["titulo"]}
    out = []
    for it in itens:
        hit = por_doi.get(it["doi"])
        como = "doi" if hit else ""
        t = norm(it["titulo"])
        if not hit and len(t) >= 25:
            hit = por_tit.get(t) or next((r for k, r in por_tit.items() if len(k) >= 25 and (t in k or k in t)), None)
            como = "titulo" if hit else ""
        idx = True if hit else (indexado(api, it["titulo"]) if len(t) >= 25 else None)
        out.append({**it, "achado": bool(hit), "como": como, "indexado": idx,
                    "vufind_id": hit["vufind_id"] if hit else ""})
    return out


# ---------------------------------------------------------------- Apêndice A

def apendice(e, o, fs_por_fonte, resumos, recs):
    hoje = dt.date.today().isoformat()
    w = []
    w.append("## SQ1 — OASISBR e LA Referencia (emendas v1.1 e v1.2)\n")
    w.append(f"*Gerado por `ferramentas/coleta_vufind.py` em {hoje}. Consulta = blocos SQ1-AL #1 "
             f"(exposição, {len(e)} termos) AND #2 (desfecho, {len(o)} termos) da seção \"SQ1 — braço "
             "América Latina\", lidos dos JSON congelados, **sem o #3 (geografia)**, porque as fontes já "
             "são brasileira e latino-americana. API VuFind, `type=AllFields`. Teses e dissertações "
             "(emenda v1.1) e TCCs de graduação (emenda v1.2) entram.*\n")
    w.append("| linha | base | contagem | descrição |")
    w.append("|---|---|---:|---|")
    for fonte, res in resumos.items():
        fs = fs_por_fonte[fonte]
        nome = NOME_FONTE[fonte]
        w.append(f"| {nome} #1 | {nome} (API VuFind) | {res['uniao']:,} | #1 AND #2, em {len(fs)} fatias "
                 f"(soma bruta {res['soma_fatias']:,}; união por `id`). "
                 + (f"Chamada única: {res['chamada_unica']:,}, igual à união. " if res.get("chamada_unica") else
                    f"Sem chamada única possível ({OASISBR_BLOQUEIO}). Conferência: dos registros brasileiros "
                    f"(`BR_`) da LA Referencia, que é subconjunto do OASISBR, {res.get('cobertura_lareferencia_br')} "
                    "reaparecem na união, por título normalizado. ")
                 + f"Com resumo: {res['com_resumo']:,}; com DOI: {res['com_doi']:,}. "
                 + "Formatos: " + ", ".join(f"{k} {v}" for k, v in res["formatos"].items()) + ". |")
    if "oasisbr" not in resumos:
        w.append(f"| OASISBR #1 | OASISBR (API VuFind) | — | **Não coletado.** {OASISBR_BLOQUEIO} |")
    w.append("")
    w.append(f"**String exata** ({hoje}; a mesma em todas as fontes VuFind):\n")
    w.append("```text\n" + consulta(e, o) + "\n```")
    for fonte, fs in fs_por_fonte.items():
        regra = (f"no máximo {MAX_TERMOS[fonte]} termos de cada lado, pausa de {PAUSA[fonte]:.0f} s"
                 if fonte in MAX_TERMOS else f"URL < {LIMITE_URL} caracteres")
        w.append(f"\n**Fatias, {NOME_FONTE[fonte]}** ({len(fs)} chamadas; {regra}; `--plano` reproduz e "
                 "confere que cobrem exatamente os blocos):\n")
        es, os_ = [], []
        for f in fs:
            if f["e"] not in es:
                es.append(f["e"])
            if f["o"] not in os_:
                os_.append(f["o"])
        for i, c in enumerate(es, 1):
            w.append(f"- E{i}: termos de #1 de `{c[0]}` a `{c[-1]}` ({len(c)})")
        for j, c in enumerate(os_, 1):
            w.append(f"- O{j}: termos de #2 de `{c[0]}` a `{c[-1]}` ({len(c)})")
    w.append("\n**Recall dos itens conhecidos** (DOIs da calibração SQ1-AL; conferência por DOI e, na "
             "falta, por título normalizado; \"BR\" = algum autor com afiliação brasileira no OpenAlex):\n")
    w.append("| DOI | ano | BR | " + " | ".join(NOME_FONTE[f] for f in recs) + " | título |")
    w.append("|---|---|---|" + "---|" * len(recs) + "---|")
    primeiro = next(iter(recs.values()))
    for k, it in enumerate(primeiro):
        marcas = []
        for f in recs:
            r = recs[f][k]
            marcas.append(("✓ " + r["como"]) if r["achado"] else
                          {True: "✗ indexado, não recuperado", False: "fora da fonte", None: "?"}[r["indexado"]])
        br = {True: "sim", False: "não", None: "?"}[it["br"]]
        w.append(f"| {it['doi']} | {it['ano'] or ''} | {br} | " + " | ".join(marcas)
                 + f" | {(it['titulo'] or '')[:90].replace('|', '/')} |")
    for f, rs in recs.items():
        idx = [r for r in rs if r["indexado"]]
        perdidos = [r for r in idx if not r["achado"]]
        w.append(f"\n- {NOME_FONTE[f]}: {len(idx)}/{len(rs)} itens conhecidos estão na fonte; a string "
                 f"recupera {sum(r['achado'] for r in idx)}/{len(idx)} deles."
                 + (" Perdidos, mas indexados: " + "; ".join(f"`{r['doi']}`" for r in perdidos) + "." if perdidos else ""))
    w.append("\nO recall que conta é o **sobre os itens indexados**: os itens conhecidos são, na maioria, "
             "artigos em periódicos internacionais, que repositórios institucionais não precisam ter. O papel "
             "destas fontes é trazer teses, dissertações, TCCs e periódicos brasileiros que as bases indexadas não "
             "cobrem. \"Fora da fonte\" = a busca pelo título (8 primeiras palavras, campo Title) não achou o "
             "item; um título traduzido pode dar falso \"fora da fonte\". Os itens de **contexto** (sem termo "
             "de desfecho ao nascer: Rocha 2017, Dossiê ABRASCO, textos jurídicos) não são alvo de #1 AND #2: "
             "na calibração, só os braços de contexto os recuperam.")
    open(os.path.join(BASE, "ferramentas", "vufind.md"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(w) + "\n")


def reidratar():
    """Refaz os JSONL a partir dos IDs versionados e confere o SHA-256 do resumo."""
    for fonte, api in FONTES.items():
        caminho = os.path.join(REG, f"vufind-{fonte}-sq1.csv")
        if not os.path.exists(caminho):
            continue
        linhas = list(csv.DictReader(open(caminho, encoding="utf-8")))
        regs = {}
        rec_api = api.replace("/search", "/record")
        for i in range(0, len(linhas), 50):
            ps = [("id[]", id_vufind(l)) for l in linhas[i:i + 50]] + [("field[]", c) for c in CAMPOS_API]
            for r in get(rec_api, ps).get("records") or []:
                regs[r["id"]] = achata(r)
        mudou = [id_vufind(l) for l in linhas if sha(regs.get(id_vufind(l), {}).get("resumo", "")) != l["sha256_resumo"]]
        with open(os.path.join(BRUTO, f"vufind-{fonte}-sq1.jsonl"), "w", encoding="utf-8") as f:
            for l in linhas:
                r = {**regs.get(id_vufind(l), {}), "posicao": int(l["posicao"]), "fatias": l["fatias"]}
                f.write(json.dumps({"fonte": NOME_FONTE[fonte], "bloco": BLOCO, "linha": LINHA, **r},
                                   ensure_ascii=False) + "\n")
        print(f"{fonte}: {len(linhas)} reidratados; {len(mudou)} resumos diferentes da coleta", file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plano", action="store_true", help="fatias e tamanhos de URL, sem rede")
    ap.add_argument("--conferir", action="store_true", help="só contagens, sem gravar")
    ap.add_argument("--reidratar", action="store_true")
    ap.add_argument("--amostra", type=int, help="com --conferir: só as N primeiras fatias de cada fonte")
    ap.add_argument("--fontes", nargs="*", default=list(FONTES), choices=list(FONTES))
    a = ap.parse_args()
    e, o, fs_por_fonte = plano()
    fs_por_fonte = {f: fs_por_fonte[f] for f in a.fontes}
    if a.plano:
        print(f"#1: {len(e)} termos; #2: {len(o)} termos")
        for fonte, fs in fs_por_fonte.items():
            print(f"{fonte}: {len(fs)} fatias; URL máx. "
                  f"{max(tamanho_url(FONTES[fonte], f['e'], f['o']) for f in fs)} car. (limite {LIMITE_URL})")
            for f in fs:
                print(f"  {f['rotulo']}: {len(f['e'])} × {len(f['o'])} termos, "
                      f"URL {tamanho_url(FONTES[fonte], f['e'], f['o'])} car.")
        sys.exit(0)
    if a.reidratar:
        reidratar()
        sys.exit(0)
    if a.conferir:
        for fonte, fs in fs_por_fonte.items():
            api = FONTES[fonte]
            for f in fs[:a.amostra] if a.amostra else fs:
                print(f"{fonte} {f['rotulo']}: {conta(api, consulta(f['e'], f['o']))}", file=sys.stderr)
            if fonte == "lareferencia":
                print(f"{fonte} chamada única: {conta(api, consulta(e, o))}", file=sys.stderr)
        sys.exit(0)
    resumos, todos, logs = {}, {}, {}
    for fonte, fs in fs_por_fonte.items():
        # Baixa e confere as fontes pedidas antes de gravar qualquer uma.
        try:
            todos[fonte], resumos[fonte], logs[fonte] = coleta(fonte, fs)
        except Bloqueio as ex:
            sys.exit(f"Interrompido, nada gravado em registros/: {ex}")
    # Fonte não pedida agora, mas já coletada: entra no Apêndice A pelo CSV versionado.
    _, _, fs_todas = plano()
    reusadas = {}
    for fonte in FONTES:
        if fonte not in todos:
            regs, res = carrega_coletada(fonte)
            if regs is not None and res is not None:
                reusadas[fonte] = (regs, res)
    itens = itens_conhecidos()
    ordem = [f for f in FONTES if f in todos or f in reusadas]
    recs = {f: recall(itens, todos[f] if f in todos else reusadas[f][0], FONTES[f]) for f in ordem}
    for fonte in fs_por_fonte:
        grava(fonte, todos[fonte])
        for l in logs[fonte]:
            loga(l)
        rs = recs[fonte]
        idx = [r for r in rs if r["indexado"]]
        loga({**resumos[fonte], "itens_conhecidos": len(rs), "itens_indexados": len(idx),
              "recall_sobre_indexados": f"{sum(r['achado'] for r in idx)}/{len(idx)}",
              "indexados_perdidos": [r["doi"] for r in idx if not r["achado"]]})
        print(json.dumps(resumos[fonte], ensure_ascii=False), file=sys.stderr)
    apendice(e, o, {f: fs_todas[f] for f in ordem},
             {f: resumos[f] if f in resumos else reusadas[f][1] for f in ordem}, recs)
