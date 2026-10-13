"""Coleta da SQ1 no Scopus pela API Elsevier (emenda v1.1): identificação.

A string é a tradução Scopus de `ferramentas/scopus_wos.md` (bloco "### Scopus"), lida
do arquivo, sem redigitação. Scopus Search com `cursor=*`; guarda EID, DOI, título,
periódico, ano e tipo. Fora do IP institucional a API dá a visão reduzida (STANDARD),
sem resumo: o resumo vem da exportação pela CAPES ou é hidratado por DOI na Etapa 3.

Credenciais: `ELSEVIER_API_KEY` (obrigatória) e `ELSEVIER_INSTTOKEN` (opcional), enviadas
nos cabeçalhos `X-ELS-APIKey`/`X-ELS-Insttoken`. Com 401/403, para sem gravar e diz a
causa provável.

Rodar de docs/revisao-sistematica:

    python3 ferramentas/coleta_scopus.py --plano      # mostra a string, sem rede
    python3 ferramentas/coleta_scopus.py --conferir   # só a contagem e a visão
    python3 ferramentas/coleta_scopus.py              # coleta

Saídas: `registros/scopus-api-sq1.csv` e uma linha em `registros/coletas.jsonl`.
"""
import argparse
import csv
import datetime as dt
import os
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coleta_openalex import BASE, REG, loga  # noqa: E402

API = "https://api.elsevier.com/content/search/scopus"
POR_PAGINA = 25
PAUSA = 0.2
CAMPOS_API = "eid,doi,dc:title,prism:publicationName,prism:coverDate,subtype,subtypeDescription,prism:aggregationType"
CAMPOS = ["fonte", "bloco", "linha", "posicao", "eid", "doi", "titulo", "ano", "periodico", "tipo", "tipo_fonte"]


def string_scopus():
    """Bloco ```text logo depois de '### Scopus' em scopus_wos.md, com as linhas unidas por espaço."""
    linhas = open(os.path.join(BASE, "ferramentas", "scopus_wos.md"), encoding="utf-8").read().splitlines()
    i = next(k for k, l in enumerate(linhas) if l.startswith("### Scopus"))
    ini = next(k for k in range(i, len(linhas)) if linhas[k].startswith("```text")) + 1
    fim = next(k for k in range(ini, len(linhas)) if linhas[k].startswith("```"))
    q = " ".join(l.strip() for l in linhas[ini:fim] if l.strip())
    assert q.startswith("TITLE-ABS-KEY") and q.count("(") == q.count(")"), q[:80]
    return q


def cabecalhos():
    chave = os.environ.get("ELSEVIER_API_KEY")
    if not chave:
        sys.exit("ELSEVIER_API_KEY ausente no ambiente; nada foi feito.")
    h = {"X-ELS-APIKey": chave, "Accept": "application/json"}
    if os.environ.get("ELSEVIER_INSTTOKEN"):
        h["X-ELS-Insttoken"] = os.environ["ELSEVIER_INSTTOKEN"]
    return h


def causa(r):
    t = r.text[:300]
    if r.status_code == 401:
        return f"HTTP 401: chave inválida ou não reconhecida ({t})"
    return (f"HTTP 403: a chave é válida, mas sem direito a este recurso/visão; fora do IP institucional "
            f"e sem insttoken, a Elsevier só libera a visão STANDARD ({t})")


def get(params, tentativas=5):
    h = cabecalhos()
    for k in range(tentativas):
        time.sleep(PAUSA)
        try:
            r = requests.get(API, params=params, headers=h, timeout=120)
        except requests.RequestException as e:
            print(f"  tentativa {k + 1}: {e!r}", file=sys.stderr)
            time.sleep(2 ** (k + 1))
            continue
        if r.status_code == 200:
            return r.json()["search-results"], r.headers
        if r.status_code in (400, 401, 403):
            raise PermissionError(causa(r)) if r.status_code != 400 else ValueError(f"HTTP 400: {r.text[:500]}")
        print(f"  tentativa {k + 1}: HTTP {r.status_code} {r.text[:200]}", file=sys.stderr)
        time.sleep(2 ** (k + 1))
    raise RuntimeError(f"{tentativas} tentativas falharam")


def visao(q):
    """COMPLETE se a rede/insttoken permitir; senão STANDARD (reduzida)."""
    try:
        get({"query": q, "count": 1, "view": "COMPLETE"})
        return "COMPLETE"
    except PermissionError:
        return "STANDARD"


def achata(e, pos):
    return {"posicao": pos, "eid": e.get("eid", ""), "doi": (e.get("prism:doi") or "").lower(),
            "titulo": " ".join((e.get("dc:title") or "").split()), "ano": (e.get("prism:coverDate") or "")[:4],
            "periodico": e.get("prism:publicationName") or "", "tipo": e.get("subtypeDescription") or "",
            "tipo_fonte": e.get("prism:aggregationType") or ""}


TETO_START = 5000  # sem assinatura, o `cursor` é recusado (ENTITLEMENTS_ERROR) e o `start` vai até 5.000


def coleta(q, gravar=True):
    v = visao(q)
    paginacao = "cursor"
    # Ordem explícita: a padrão (relevância) muda entre páginas e repete/perde registros no `start`
    # (teste de 2026-10-13: -coverDate deu 4.945/4.945 distintos numa passada).
    params = {"query": q, "count": POR_PAGINA, "cursor": "*", "view": "STANDARD", "field": CAMPOS_API,
              "sort": "-coverDate"}
    regs, total, cota = [], None, None
    while True:
        try:
            res, h = get(params)
        except PermissionError as e:
            if paginacao != "cursor" or "cursor" not in str(e):
                raise
            print("  cursor recusado sem assinatura; sigo com start/count (teto de 5.000)", file=sys.stderr)
            paginacao = "start"
            params.pop("cursor")
            params["start"] = 0
            continue
        total = int(res["opensearch:totalResults"])
        if paginacao == "start" and total > TETO_START:
            raise RuntimeError(f"{total} registros passam do teto de {TETO_START} do start; nada gravado")
        cota = h.get("X-RateLimit-Remaining")
        ents = [e for e in res.get("entry") or [] if "error" not in e]
        regs += [achata(e, len(regs) + 1) for e in ents]
        print(f"  Scopus: {len(regs)}/{total}", file=sys.stderr)
        if not ents or len(regs) >= total or not gravar:
            break
        if paginacao == "cursor":
            prox = (res.get("cursor") or {}).get("@next")
            if not prox:
                break
            params["cursor"] = prox
        else:
            params["start"] = len(regs)
    if gravar and len(regs) != total:
        raise RuntimeError(f"baixados {len(regs)} de {total}; nada gravado")
    if gravar and len({r["eid"] for r in regs}) != total:
        raise RuntimeError("EID repetido entre páginas (a ordem mudou durante a coleta); nada gravado")
    return regs, total, v, cota, paginacao


def grava(regs):
    with open(os.path.join(REG, "scopus-api-sq1.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for r in regs:
            w.writerow({"fonte": "Scopus (API)", "bloco": "sq1-internacional", "linha": "Scopus SQ1", **r})


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plano", action="store_true")
    ap.add_argument("--conferir", action="store_true")
    a = ap.parse_args()
    q = string_scopus()
    if a.plano:
        print(f"{len(q)} caracteres\n{q}")
        sys.exit(0)
    agora = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        regs, total, v, cota, paginacao = coleta(q, gravar=not a.conferir)
    except PermissionError as e:
        sys.exit(f"Scopus recusou a credencial; nada gravado.\n{e}")
    if a.conferir:
        print(f"Scopus SQ1: {total} registros; visão disponível: {v}; cota semanal restante: {cota}", file=sys.stderr)
        sys.exit(0)
    grava(regs)
    loga({"data_utc": agora, "fonte": "Scopus (API)", "bloco": "sq1-internacional", "linha": "Scopus SQ1",
          "papel": "identificacao", "contagem_hoje": total, "baixados": len(regs),
          "com_doi": sum(1 for r in regs if r["doi"]), "visao_disponivel": v,
          "visao_usada": "STANDARD", "paginacao": paginacao, "cota_restante": cota, "resumo": "não (hidratar por DOI na Etapa 3; exportação CAPES)",
          "query": q, "arquivo": "registros/scopus-api-sq1.csv"})
    print(f"Scopus SQ1: {len(regs)} gravados; visão disponível: {v}", file=sys.stderr)
