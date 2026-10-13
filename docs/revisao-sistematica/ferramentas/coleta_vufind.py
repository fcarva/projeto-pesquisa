"""Coleta da SQ1 nas APIs VuFind do OASISBR (IBICT) e da LA Referencia (emenda v1.1).

Consulta: blocos congelados SQ1-AL #1 (exposição) AND #2 (desfecho), lidos de
`calibracao/sq1-america-latina-final.json` por `blocos_al()` + `carrega()` de
`coleta_openalex.py`, sem redigitação. Sem o #3 (geografia): as duas fontes já são
brasileira e latino-americana (emenda v1.1).

Fatiamento: o OASISBR responde 403 a URL longa (~3.200 caracteres). Como
(E1 OR E2) AND (O1 OR O2) = U_ij (Ei AND Oj), os termos de #1 e #2 são repartidos
em fatias com URL < LIMITE_URL, e os registros das fatias são unidos por `id`. O
`--plano` confere, sem rede, que as fatias cobrem exatamente os termos dos blocos.
Na LA Referencia, que aceita a URL inteira, a união das fatias tem de bater com a
contagem da chamada única; se não bater, o script para sem gravar.

Rodar de docs/revisao-sistematica:

    python3 ferramentas/coleta_vufind.py --plano      # fatias e tamanhos de URL, sem rede
    python3 ferramentas/coleta_vufind.py --conferir   # só contagens, sem gravar
    python3 ferramentas/coleta_vufind.py              # coleta as duas fontes
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
from urllib.parse import urlencode

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
PAUSA = 0.5
BLOCO, LINHA = "sq1-america-latina", "VuFind #1 AND #2"
# Teste de 2026-10-13, de IP residencial: o 403 do OASISBR não é de tamanho de URL.
OASISBR_BLOQUEIO = ("Teste de 2026-10-13: a API devolve HTTP 403 a consultas booleanas com ~10 termos ou mais, "
                    "mesmo com URL de 459 caracteres (5 termos de cada lado passam), e em seguida recusa "
                    "conexões do IP por um tempo. Parece regra de firewall, não limite de URL. O nó brasileiro "
                    "da LA Referencia é o próprio IBICT/OASISBR, então os registros brasileiros chegam por ela.")

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


def fatias(api, e, o):
    """Escolhe as fatias de #1 e #2 que minimizam o número de chamadas com URL < LIMITE_URL."""
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
    for fonte, api in FONTES.items():
        fs = fatias(api, e, o)
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


def get(api, ps, tentativas=5):
    for k in range(tentativas):
        time.sleep(PAUSA)
        try:
            r = requests.get(api, params=ps, timeout=120)
        except requests.RequestException as ex:
            print(f"  tentativa {k + 1}: {ex!r}", file=sys.stderr)
            time.sleep(2 ** (k + 1))
            continue
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


def coleta(fonte, fs):
    """Baixa todas as fatias e confere; não grava nada (quem grava é o __main__, depois do recall)."""
    api = FONTES[fonte]
    agora = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    uniao, de_fatia, logs = {}, {}, []
    for f in fs:
        regs, total = baixa_fatia(api, f)
        print(f"  {fonte} {f['rotulo']}: {total}", file=sys.stderr)
        for i, r in regs.items():
            uniao.setdefault(i, r)
            de_fatia.setdefault(i, []).append(f["rotulo"])
        logs.append({"data_utc": agora, "fonte": NOME_FONTE[fonte], "bloco": BLOCO, "linha": LINHA,
                     "papel": "fatia", "fatia": f["rotulo"], "contagem_hoje": total,
                     "n_termos_e": len(f["e"]), "n_termos_o": len(f["o"]),
                     "lookfor": consulta(f["e"], f["o"])})
    unica = None
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
              "uniao": len(uniao), "chamada_unica": unica, "com_resumo": sum(1 for r in regs if r["resumo"]),
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
    pais, hash_ = i.split("_", 1)
    assert pais and hash_ and f"{pais}_{hash_}" == i, i
    return {"vufind_pais": pais, "vufind_hash": hash_}


def id_vufind(linha):
    return f"{linha['vufind_pais']}_{linha['vufind_hash']}"


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
    w.append("## SQ1 — OASISBR e LA Referencia (emenda v1.1)\n")
    w.append(f"*Gerado por `ferramentas/coleta_vufind.py` em {hoje}. Consulta = blocos SQ1-AL #1 "
             f"(exposição, {len(e)} termos) AND #2 (desfecho, {len(o)} termos) da seção \"SQ1 — braço "
             "América Latina\", lidos dos JSON congelados, **sem o #3 (geografia)**, porque as fontes já "
             "são brasileira e latino-americana. API VuFind, `type=AllFields`. Teses e dissertações "
             "entram (emenda v1.1).*\n")
    w.append("| linha | base | contagem | descrição |")
    w.append("|---|---|---:|---|")
    for fonte, res in resumos.items():
        fs = fs_por_fonte[fonte]
        nome = NOME_FONTE[fonte]
        w.append(f"| {nome} #1 | {nome} (API VuFind) | {res['uniao']:,} | #1 AND #2, em {len(fs)} fatias "
                 f"(soma bruta {res['soma_fatias']:,}; união por `id`). "
                 + (f"Chamada única: {res['chamada_unica']:,}, igual à união. " if res["chamada_unica"] else
                    "Sem chamada única: a API responde 403 a URL longa. ")
                 + f"Com resumo: {res['com_resumo']:,}; com DOI: {res['com_doi']:,}. "
                 + "Formatos: " + ", ".join(f"{k} {v}" for k, v in res["formatos"].items()) + ". |")
    if "oasisbr" not in resumos:
        w.append(f"| OASISBR #1 | OASISBR (API VuFind) | — | **Não coletado.** {OASISBR_BLOQUEIO} |")
    w.append("")
    w.append(f"**String exata** ({hoje}; a mesma em todas as fontes VuFind):\n")
    w.append("```text\n" + consulta(e, o) + "\n```")
    for fonte, fs in fs_por_fonte.items():
        w.append(f"\n**Fatias, {NOME_FONTE[fonte]}** (URL < {LIMITE_URL} caracteres; `--plano` reproduz e "
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
             "destas fontes é trazer teses, dissertações e periódicos brasileiros que as bases indexadas não "
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
            for f in fs:
                print(f"{fonte} {f['rotulo']}: {conta(api, consulta(f['e'], f['o']))}", file=sys.stderr)
            if fonte == "lareferencia":
                print(f"{fonte} chamada única: {conta(api, consulta(e, o))}", file=sys.stderr)
        sys.exit(0)
    resumos, todos, logs = {}, {}, {}
    for fonte, fs in fs_por_fonte.items():
        # Baixa e confere as duas fontes antes de gravar qualquer uma.
        todos[fonte], resumos[fonte], logs[fonte] = coleta(fonte, fs)
    itens = itens_conhecidos()
    recs = {f: recall(itens, regs, FONTES[f]) for f, regs in todos.items()}
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
    apendice(e, o, fs_por_fonte, resumos, recs)
