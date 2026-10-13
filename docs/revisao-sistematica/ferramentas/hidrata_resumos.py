"""Hidrata o resumo dos registros a triar que não têm resumo em nenhuma fonte (Etapa 3).

Para cada DOI de `registros/deduplicado-sq{1,2,3}.csv` com `tem_resumo == 0` e sem exclusão
automática, tenta, nesta ordem (protocolo, "Seleção"): OpenAlex (`abstract_inverted_index`, em
lotes de 50 DOIs) e, na falta, Crossref (`/works/{doi}`, campo `abstract`, JATS sem as tags).
Se o OpenAlex estiver sem cota ou sem chave, o script segue só com o Crossref e registra isso;
uma execução posterior, com o OpenAlex disponível, tenta nele os DOIs que ficaram sem resumo.

Retomável: cada tentativa vai para `data/raw/revisao-sistematica/resumos-hidratados.jsonl` (com
o texto; fora do git). Um DOI com resumo, ou já tentado sem sucesso numa fonte, não é refeito
naquela fonte. Erro de rede não conta como tentativa.

Saída versionada: `registros/resumos-hidratados.csv` (DOI, fonte do resumo, SHA-256, tentativas),
que o `deduplica.py` lê para marcar `tem_resumo`.

    python3 ferramentas/hidrata_resumos.py
"""
import csv
import datetime as dt
import html
import json
import os
import re
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coleta_openalex import BRUTO, REG, SemCredito, resumo as de_indice_invertido, sha  # noqa: E402
from coleta_openalex import get as oa_get  # noqa: E402

CROSSREF = "https://api.crossref.org/works/"
MAILTO = "revisao.sistematica.ufes@example.org"
BRUTO_JSONL = os.path.join(BRUTO, "resumos-hidratados.jsonl")
SAIDA = os.path.join(REG, "resumos-hidratados.csv")
FONTES = ("OpenAlex", "Crossref")


def agora():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def alvos():
    dois = []
    for p in ("sq1", "sq2", "sq3"):
        for r in csv.DictReader(open(os.path.join(REG, f"deduplicado-{p}.csv"), encoding="utf-8")):
            if r["tem_resumo"] == "0" and not r["exclusao_auto"] and r["doi"] and r["doi"] not in dois:
                dois.append(r["doi"])
    return dois


def historico():
    """doi -> {fonte: (status, resumo, data)} das execuções anteriores."""
    h = {}
    if os.path.exists(BRUTO_JSONL):
        for l in open(BRUTO_JSONL, encoding="utf-8"):
            t = json.loads(l)
            h.setdefault(t["doi"], {})[t["fonte"]] = (t["status"], t.get("resumo", ""), t["data_utc"])
    return h


def registra(doi, fonte, status, resumo=""):
    os.makedirs(BRUTO, exist_ok=True)
    with open(BRUTO_JSONL, "a", encoding="utf-8") as f:
        f.write(json.dumps({"doi": doi, "fonte": fonte, "status": status, "resumo": resumo, "data_utc": agora()},
                           ensure_ascii=False) + "\n")


def limpa_jats(t):
    t = re.sub(r"<[^>]+>", " ", t or "")
    t = html.unescape(" ".join(t.split()))
    return re.sub(r"^(abstract|resumo|resumen)\s*[:.]?\s+", "", t, flags=re.I)


def via_openalex(dois):
    """Lotes de 50 DOIs. Devolve {doi: resumo ou ''}; levanta SemCredito sem cota/chave."""
    out = {}
    for i in range(0, len(dois), 50):
        lote = dois[i:i + 50]
        res = oa_get({"filter": "doi:" + "|".join(lote), "per-page": 50, "select": "doi,abstract_inverted_index"})
        achados = {(w.get("doi") or "").lower().replace("https://doi.org/", ""):
                   de_indice_invertido(w.get("abstract_inverted_index")) for w in res["results"]}
        for d in lote:
            out[d] = achados.get(d, "")
        print(f"  OpenAlex {min(i + 50, len(dois))}/{len(dois)}", file=sys.stderr)
    return out


def via_crossref(sessao, doi):
    for k in range(4):
        try:
            r = sessao.get(CROSSREF + doi, params={"mailto": MAILTO}, timeout=60)
        except requests.RequestException:
            time.sleep(2 ** (k + 1))
            continue
        if r.status_code == 404:
            return ""
        if r.status_code == 200:
            return limpa_jats(r.json()["message"].get("abstract", ""))
        time.sleep(2 ** (k + 1))
    return None  # erro de rede: não conta como tentativa


def roda():
    dois = alvos()
    h = historico()
    pendentes = [d for d in dois if not any(s == "ok" for s, _, _ in h.get(d, {}).values())]
    print(f"{len(dois)} DOIs sem resumo; {len(pendentes)} pendentes", file=sys.stderr)
    oa = [d for d in pendentes if "OpenAlex" not in h.get(d, {})]
    openalex_disponivel = True
    try:
        for d, txt in via_openalex(oa).items():
            registra(d, "OpenAlex", "ok" if txt else "sem_resumo", txt)
    except SemCredito as e:
        openalex_disponivel = False
        print(f"  OpenAlex indisponível ({str(e)[:120]}); sigo só com o Crossref", file=sys.stderr)
    h = historico()
    cr = [d for d in pendentes if not any(s == "ok" for s, _, _ in h.get(d, {}).values())
          and "Crossref" not in h.get(d, {})]
    sessao = requests.Session()
    for k, d in enumerate(cr, 1):
        txt = via_crossref(sessao, d)
        if txt is not None:
            registra(d, "Crossref", "ok" if txt else "sem_resumo", txt)
        time.sleep(0.1)
        if k % 250 == 0:
            print(f"  Crossref {k}/{len(cr)}", file=sys.stderr)
    grava(dois, openalex_disponivel)


def grava(dois, openalex_disponivel):
    h = historico()
    linhas = []
    for d in dois:
        tent = h.get(d, {})
        ok = [(f, tent[f]) for f in FONTES if f in tent and tent[f][0] == "ok"]
        fonte, (st, txt, quando) = ok[0] if ok else ("", ("", "", ""))
        linhas.append({"doi": d, "fonte_resumo": fonte, "n_car_resumo": len(txt), "sha256_resumo": sha(txt),
                       "tentativas": "|".join(f"{f}:{tent[f][0]}" for f in FONTES if f in tent),
                       "data_utc": quando})
    with open(SAIDA, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)
    por_fonte = {f: sum(1 for l in linhas if l["fonte_resumo"] == f) for f in FONTES}
    resumo = {"data_utc": agora(), "fonte": "OpenAlex/Crossref", "papel": "hidratacao_resumo",
              "dois_sem_resumo": len(dois), "hidratados": por_fonte, "sem_resumo_em_nenhuma": sum(
                  1 for l in linhas if not l["fonte_resumo"]),
              "openalex_disponivel": openalex_disponivel, "arquivo": "registros/resumos-hidratados.csv"}
    with open(os.path.join(REG, "coletas.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(resumo, ensure_ascii=False) + "\n")
    print(json.dumps(resumo, ensure_ascii=False), file=sys.stderr)


if __name__ == "__main__":
    roda()
