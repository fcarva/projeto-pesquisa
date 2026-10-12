"""Coleta definitiva do OpenAlex para as linhas congeladas do Apêndice A.

As strings vêm dos `calibracao/*-final.json`, sem redigitação. Algumas linhas
congeladas usam marcadores no lugar da string expandida; o `plano()` os resolve
a partir dos mesmos JSON e falha se sobrar algum:

- SQ1-AL: `(#1)`, `(#2)`, `(#3)` -> corpo dos blocos OA #1-#3; `#n-v0` -> o mesmo
  corpo sem a cauda pós-validação (6, 9 e 18 termos, conforme as descrições);
- SQ2 #7: `<the #5 search string, verbatim>` -> o valor de busca da SQ2 #5.

Rodar de docs/revisao-sistematica:

    python3 ferramentas/coleta_openalex.py --plano          # resolve e valida, sem rede
    python3 ferramentas/coleta_openalex.py --conferir       # só contagens (1 chamada por linha)
    python3 ferramentas/coleta_openalex.py                  # coleta tudo
    python3 ferramentas/coleta_openalex.py --linhas sq1-internacional:#6
    python3 ferramentas/coleta_openalex.py --reidratar      # refaz o JSONL a partir dos IDs versionados

Chave: `OPENALEX_API_KEY` no ambiente vai como `api_key=`. Sem ela, o script
confia no proxy para injetar a credencial; se a resposta for 401/429, ele para
sem gravar nada.

Saídas: como em `coleta_pubmed.py` (metadados versionados em `registros/`, resumo
em `data/raw/revisao-sistematica/`, log em `registros/coletas.jsonl`).
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time

import requests

API = "https://api.openalex.org/works"
MAILTO = "revisao.sistematica.ufes@example.org"
POR_PAGINA = 200
PAUSA = 0.15
SELECT = ("id,doi,title,publication_year,type,language,primary_location,ids,"
          "abstract_inverted_index,authorships,relevance_score,is_retracted")

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
RAIZ = os.path.dirname(os.path.dirname(BASE))
REG = os.path.join(BASE, "registros")
BRUTO = os.path.join(RAIZ, "data", "raw", "revisao-sistematica")

# (bloco, linha, papel). papel: "conjunto" = registros a triar; "marca" = só IDs,
# para a camada; "conferencia" = só contagem, para validar o resolvedor.
LINHAS = [
    ("sq1-internacional", "#6", "conjunto"),
    ("sq1-internacional", "#8", "marca"),
    ("sq1-america-latina", "OA #4", "conjunto"),
    ("sq1-america-latina", "OA #5", "conjunto"),
    ("sq1-america-latina", "OA #6", "conjunto"),
    ("sq1-america-latina", "OA #7a", "conjunto"),
    ("sq1-america-latina", "OA #7b", "conjunto"),
    ("sq1-america-latina", "OA #8", "conjunto"),
    ("sq1-america-latina", "OA #9", "conjunto"),
    ("sq1-america-latina", "OA #4-v0", "conferencia"),
    ("sq2-metodo", "#5", "conjunto"),
    ("sq2-metodo", "#7", "conjunto"),
    ("sq2-metodo", "#9", "conjunto"),
    ("sq2-metodo", "#10", "conjunto"),
    ("sq2-metodo", "#11", "conjunto"),
    ("sq2-metodo", "#12", "conjunto"),
] + [("sq3-instrumento", l, "conjunto") for l in
     ("#5a", "#5b", "#5c", "#6", "#7a", "#7b", "#7c", "#8", "#9", "#10", "#11", "#12")]

# Caudas pós-validação da SQ1-AL (descrições de OA #1, #2 e #3 no -final.json).
CAUDAS = {
    "OA #1": ('DDE OR DDT OR organochlorine OR organochlorines OR organoclorados OR '
              'dichlorodiphenyldichloroethylene', 6),
    "OA #2": ('"congenital abnormalities" OR "orofacial clefts" OR "cleft lip" OR "cleft palate" OR '
              'neonates OR neonate OR "birth length" OR "head circumference" OR "birth size"', 9),
    "OA #3": ('Ceara OR Parana OR Goias OR "Sao Paulo" OR "Rio Grande do Norte" OR Piauí OR Piaui OR '
              'Maranhão OR Maranhao OR Tocantins OR "Espírito Santo" OR "América del Sur" OR '
              '"América do Sul" OR Sudamérica OR Latinoamérica OR Latinoamerica OR "Sul do Brasil" OR '
              '"Sur de Brasil"', 18),
}

CAMPOS = ["fonte", "bloco", "linha", "posicao", "openalex_id", "doi", "pmid", "titulo", "ano",
          "tipo", "idioma", "periodico", "primeiro_autor", "retratado", "relevance_score",
          "tem_resumo", "n_car_resumo", "sha256_resumo"]


def carrega(bloco):
    return {l["line"]: l for l in json.load(open(os.path.join(BASE, "calibracao", f"{bloco}-final.json")))["numbered_lines"]
            if l["database"].startswith("OpenAlex")}


def filtro_cru(q):
    """URL completa ou 'filter=...' -> valor do parâmetro filter."""
    if q.startswith("http"):
        q = q.split("?", 1)[1]
        partes = [p for p in q.split("&") if p.startswith("filter=")]
        assert len(partes) == 1, q[:120]
        q = partes[0]
    assert q.startswith("filter="), q[:120]
    q = q[len("filter="):]
    return re.sub(r"\s+\[.*\]\s*$", "", q)  # comentário entre colchetes no fim (SQ1-AL #4-v0)


def corpo(clausula):
    """'title_and_abstract.search:(X)' -> 'X'."""
    m = re.fullmatch(r"title_and_abstract\.search:\((.*)\)", clausula, re.S)
    assert m, clausula[:120]
    return m.group(1)


def blocos_al(linhas):
    out = {}
    for k in ("OA #1", "OA #2", "OA #3"):
        c = corpo(linhas[k]["query"])
        cauda, n = CAUDAS[k]
        assert c.endswith(" OR " + cauda), f"{k}: a cauda pós-validação não está no fim da string"
        assert len(cauda.split(" OR ")) == n, f"{k}: cauda com {len(cauda.split(' OR '))} termos, esperado {n}"
        out["#" + k[-1]] = c
        out["#" + k[-1] + "-v0"] = c[: -len(" OR " + cauda)]
    return out


def plano():
    cache = {}
    itens = []
    for bloco, linha, papel in LINHAS:
        if bloco not in cache:
            cache[bloco] = carrega(bloco)
        ln = cache[bloco][linha]
        f = filtro_cru(ln["query"])
        if bloco == "sq1-america-latina":
            subs = blocos_al(cache[bloco])
            for k in sorted(subs, key=len, reverse=True):  # "#1-v0" antes de "#1"
                f = f.replace(f"({k})", f"({subs[k]})")
        if bloco == "sq2-metodo" and "<the #5 search string, verbatim>" in f:
            f5 = filtro_cru(cache[bloco]["#5"]["query"])
            valor = f5.split("title_and_abstract.search:", 1)[1]
            f = f.replace("<the #5 search string, verbatim>", valor)
        sobra = re.findall(r"\(#\d|<[^>]*>|#\d+[a-z]?(?:-v0)?\b", f)
        assert not sobra, f"{bloco} {linha}: marcador não resolvido {sobra}"
        assert f.count("(") == f.count(")"), f"{bloco} {linha}: parênteses desbalanceados"
        busca = ".search:" in f
        itens.append({"bloco": bloco, "linha": linha, "papel": papel, "filtro": f,
                      "ordenar": busca, "contagem_congelada": ln.get("count"),
                      "data_congelamento": ln.get("run_date")})
    return itens


class SemCredito(Exception):
    pass


def get(params, tentativas=5):
    params = {**params, "mailto": MAILTO}
    chave = os.environ.get("OPENALEX_API_KEY")
    if chave:
        params["api_key"] = chave
    for k in range(tentativas):
        time.sleep(PAUSA)
        try:
            r = requests.get(API, params=params, timeout=120)
        except requests.RequestException as e:
            print(f"  tentativa {k + 1}: {e!r}", file=sys.stderr)
            time.sleep(2 ** (k + 1))
            continue
        if r.status_code == 200:
            return r.json()
        if r.status_code in (401, 403) or (r.status_code == 429 and "budget" in r.text.lower()):
            raise SemCredito(f"HTTP {r.status_code}: {r.text[:300]}")
        if r.status_code == 400:
            raise ValueError(f"HTTP 400: {r.text[:500]}")
        print(f"  tentativa {k + 1}: HTTP {r.status_code} {r.text[:200]}", file=sys.stderr)
        time.sleep(2 ** (k + 1))
    raise RuntimeError(f"{tentativas} tentativas falharam")


def resumo(inv):
    if not inv:
        return ""
    pos = sorted((p, w) for w, ps in inv.items() for p in ps)
    return " ".join(w for _, w in pos)


def achata(w, posicao):
    loc = w.get("primary_location") or {}
    fonte = (loc.get("source") or {}).get("display_name") or ""
    autores = w.get("authorships") or []
    primeiro = ((autores[0].get("author") or {}).get("display_name") or "") if autores else ""
    pmid = ((w.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1]
    doi = (w.get("doi") or "").lower().replace("https://doi.org/", "")
    return {
        "posicao": posicao,
        "openalex_id": (w.get("id") or "").rsplit("/", 1)[-1],
        "doi": doi,
        "pmid": pmid,
        "titulo": " ".join((w.get("title") or "").split()),
        "ano": w.get("publication_year") or "",
        "tipo": w.get("type") or "",
        "idioma": w.get("language") or "",
        "periodico": fonte,
        "primeiro_autor": primeiro,
        "retratado": int(bool(w.get("is_retracted"))),
        "relevance_score": w.get("relevance_score") if w.get("relevance_score") is not None else "",
        "resumo": resumo(w.get("abstract_inverted_index")),
    }


def baixa(item, so_ids=False):
    params = {"filter": item["filtro"], "per-page": POR_PAGINA, "cursor": "*",
              "select": "id" if so_ids else SELECT}
    if item["ordenar"] and not so_ids:
        params["sort"] = "relevance_score:desc"
    regs, total = [], None
    while True:
        try:
            dados = get(params)
        except ValueError as e:
            if "relevance_score" in params["select"] and "select" in str(e).lower():
                print("  select recusou relevance_score; sigo sem ele e registro no log", file=sys.stderr)
                params["select"] = SELECT.replace(",relevance_score", "")
                item["sem_relevance_score"] = True
                continue
            raise
        total = dados["meta"]["count"]
        for w in dados["results"]:
            regs.append(achata(w, len(regs) + 1) if not so_ids else {"openalex_id": w["id"].rsplit("/", 1)[-1]})
        cur = dados["meta"].get("next_cursor")
        print(f"  {item['bloco']} {item['linha']}: {len(regs)}/{total}", file=sys.stderr)
        if not cur or not dados["results"]:
            break
        params["cursor"] = cur
    if len(regs) != total:
        raise RuntimeError(f"{item['bloco']} {item['linha']}: baixados {len(regs)} de {total}")
    return regs, total


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest() if s else ""


def nome(bloco, linha):
    return "openalex-" + bloco + "-" + re.sub(r"[^0-9a-z]+", "", linha.lower().replace("oa ", ""))


def grava(item, regs):
    os.makedirs(REG, exist_ok=True)
    os.makedirs(BRUTO, exist_ok=True)
    base = nome(item["bloco"], item["linha"])
    if item["papel"] == "marca":
        with open(os.path.join(REG, base + "-ids.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["openalex_id"])
            w.writerows([[r["openalex_id"]] for r in regs])
        return
    with open(os.path.join(REG, base + ".csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for r in regs:
            w.writerow({"fonte": "OpenAlex", "bloco": item["bloco"], "linha": item["linha"],
                        **{k: r[k] for k in CAMPOS if k in r},
                        "tem_resumo": int(bool(r["resumo"])), "n_car_resumo": len(r["resumo"]),
                        "sha256_resumo": sha(r["resumo"])})
    with open(os.path.join(BRUTO, base + ".jsonl"), "w", encoding="utf-8") as f:
        for r in regs:
            f.write(json.dumps({"fonte": "OpenAlex", "bloco": item["bloco"], "linha": item["linha"], **r},
                               ensure_ascii=False) + "\n")


def loga(entrada):
    os.makedirs(REG, exist_ok=True)
    with open(os.path.join(REG, "coletas.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(entrada, ensure_ascii=False) + "\n")


def roda(itens, so_contar):
    agora = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for it in itens:
        if so_contar or it["papel"] == "conferencia":
            n = get({"filter": it["filtro"], "per-page": 1, "select": "id"})["meta"]["count"]
            print(f"{it['bloco']} {it['linha']}: hoje {n}, congelada {it['contagem_congelada']}", file=sys.stderr)
            if not so_contar:
                loga({"data_utc": agora, "fonte": "OpenAlex", "bloco": it["bloco"], "linha": it["linha"],
                      "papel": it["papel"], "contagem_congelada": it["contagem_congelada"],
                      "contagem_hoje": n, "filtro": it["filtro"]})
            continue
        regs, total = baixa(it, so_ids=it["papel"] == "marca")
        grava(it, regs)
        entrada = {"data_utc": agora, "fonte": "OpenAlex", "bloco": it["bloco"], "linha": it["linha"],
                   "papel": it["papel"], "contagem_congelada": it["contagem_congelada"],
                   "data_congelamento": it["data_congelamento"], "contagem_hoje": total,
                   "baixados": len(regs), "filtro": it["filtro"],
                   "ordenacao": "relevance_score:desc" if it["ordenar"] and it["papel"] != "marca" else "padrão"}
        if it["papel"] == "conjunto":
            entrada["com_resumo"] = sum(1 for r in regs if r["resumo"])
        if it.get("sem_relevance_score"):
            entrada["aviso"] = "relevance_score recusado no select; a ordem do arquivo é a da API"
        loga(entrada)


def reidratar():
    """Refaz os JSONL (com resumo) a partir dos IDs versionados e confere o SHA-256."""
    for it in plano():
        if it["papel"] != "conjunto":
            continue
        base = nome(it["bloco"], it["linha"])
        caminho = os.path.join(REG, base + ".csv")
        if not os.path.exists(caminho):
            continue
        linhas = list(csv.DictReader(open(caminho, encoding="utf-8")))
        regs = {}
        for i in range(0, len(linhas), 100):
            ids = "|".join(l["openalex_id"] for l in linhas[i:i + 100])
            for w in get({"filter": f"openalex:{ids}", "per-page": 100, "select": SELECT})["results"]:
                r = achata(w, 0)
                regs[r["openalex_id"]] = r
        mudou = [l["openalex_id"] for l in linhas if sha(regs.get(l["openalex_id"], {}).get("resumo", "")) != l["sha256_resumo"]]
        with open(os.path.join(BRUTO, base + ".jsonl"), "w", encoding="utf-8") as f:
            for l in linhas:
                r = {**regs.get(l["openalex_id"], {}), "posicao": int(l["posicao"])}
                f.write(json.dumps({"fonte": "OpenAlex", "bloco": it["bloco"], "linha": it["linha"], **r},
                                   ensure_ascii=False) + "\n")
        print(f"{base}: {len(linhas)} reidratados; {len(mudou)} resumos diferentes da coleta", file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plano", action="store_true", help="resolve e valida as linhas, sem rede")
    ap.add_argument("--conferir", action="store_true", help="só as contagens de hoje, sem gravar")
    ap.add_argument("--reidratar", action="store_true")
    ap.add_argument("--linhas", nargs="*", help="bloco:linha, p. ex. sq1-internacional:#6")
    a = ap.parse_args()
    itens = plano()
    if a.linhas:
        itens = [i for i in itens if f"{i['bloco']}:{i['linha']}" in a.linhas]
    if a.plano:
        for i in itens:
            print(f"{i['bloco']:<20} {i['linha']:<9} {i['papel']:<11} congelada={i['contagem_congelada']!s:<6} "
                  f"ordena={i['ordenar']!s:<5} filtro={len(i['filtro'])} car.")
        sys.exit(0)
    try:
        reidratar() if a.reidratar else roda(itens, a.conferir)
    except SemCredito as e:
        sys.exit(f"OpenAlex recusou a credencial ou a cota acabou; nada desta linha foi gravado.\n{e}")
