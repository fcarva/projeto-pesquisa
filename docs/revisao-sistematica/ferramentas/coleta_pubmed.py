"""Coleta definitiva do PubMed (E-utilities) para as linhas congeladas do Apêndice A.

As strings vêm dos `calibracao/*-final.json`, sem redigitação. Linhas coletadas:

- SQ1 internacional, PubMed #5 (conjunto de triagem), com a marca de camada
  calculada no history server: camada 1 = #5 AND #6 (#7 congelada), camada 2 = o resto (#8);
- SQ3, PubMed P1 (linha suplementar de vocabulário controlado).

Saídas (rodar de docs/revisao-sistematica):
- `registros/pubmed-<bloco>-<linha>.csv`: metadados versionados (sem resumo) + SHA-256 do resumo;
- `data/raw/revisao-sistematica/pubmed-<bloco>-<linha>.jsonl` na raiz do repositório:
  registro completo, com resumo. Fica fora do git (repositório público; o resumo
  tem direito autoral do editor) e é reconstruível com `--reidratar`;
- `registros/coletas.jsonl`: uma linha de log por consulta (data UTC, contagem
  congelada × de hoje, querytranslation).

    python3 ferramentas/coleta_pubmed.py              # coleta
    python3 ferramentas/coleta_pubmed.py --reidratar  # refaz o JSONL a partir dos PMIDs versionados
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import sys
import time
import xml.etree.ElementTree as ET

import requests

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
# Mesmo identificador de contato da calibração; não é endereço pessoal.
TOOL, EMAIL = "projeto-pesquisa-revisao-sistematica", "revisao.sistematica.ufes@example.org"
PAUSA = 0.4  # sem chave NCBI: no máximo 3 requisições por segundo
LOTE = 200

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)  # docs/revisao-sistematica
RAIZ = os.path.dirname(os.path.dirname(BASE))
REG = os.path.join(BASE, "registros")
BRUTO = os.path.join(RAIZ, "data", "raw", "revisao-sistematica")

# (bloco, arquivo final, linha do conjunto, linha da marca de camada ou None)
COLETAS = [
    ("sq1-internacional", "#5", "#6"),
    ("sq3-instrumento", "P1", None),
]

CAMPOS = ["fonte", "bloco", "linha", "pmid", "doi", "pmcid", "titulo", "ano", "periodico",
          "primeiro_autor", "idiomas", "tipos_publicacao", "camada", "tem_resumo",
          "n_car_resumo", "sha256_resumo"]


def linha_congelada(bloco, linha):
    fin = json.load(open(os.path.join(BASE, "calibracao", f"{bloco}-final.json")))
    for ln in fin["numbered_lines"]:
        if ln["line"] == linha and ln["database"].startswith("PubMed"):
            return ln
    sys.exit(f"linha {linha} do PubMed não encontrada em {bloco}-final.json")


def post(util, dados, tentativas=5):
    dados = {**dados, "tool": TOOL, "email": EMAIL}
    for k in range(tentativas):
        time.sleep(PAUSA)
        try:
            r = requests.post(EUTILS + util, data=dados, timeout=120)
            if r.status_code == 200:
                return r
            erro = f"HTTP {r.status_code}: {r.text[:200]}"
        except requests.RequestException as e:
            erro = repr(e)
        print(f"  {util}: tentativa {k + 1} falhou ({erro})", file=sys.stderr)
        time.sleep(2 ** (k + 1))
    sys.exit(f"{util} falhou {tentativas} vezes; nada foi gravado para esta linha")


def esearch(term, webenv=None):
    dados = {"db": "pubmed", "term": term, "usehistory": "y", "retmax": 10000, "retmode": "json"}
    if webenv:
        dados["WebEnv"] = webenv
    res = post("esearch.fcgi", dados).json()["esearchresult"]
    if res.get("errorlist") and any(res["errorlist"].values()):
        sys.exit(f"esearch devolveu erro: {res['errorlist']}")
    n = int(res["count"])
    if n > 9999:
        sys.exit(f"{n} registros: acima do teto de 9.999 do esearch; paginar com retstart")
    return res


def texto(el):
    return " ".join("".join(el.itertext()).split()) if el is not None else ""


def parse_artigo(art):
    """Um <PubmedArticle> ou <PubmedBookArticle> -> dict."""
    cit = art.find("MedlineCitation")
    livro = cit is None
    raiz = art.find("BookDocument") if livro else cit
    pmid = raiz.findtext("PMID")
    a = raiz if livro else cit.find("Article")
    titulo = texto(a.find("ArticleTitle")) or texto(a.find("Book/BookTitle"))
    partes = []
    for t in a.findall("Abstract/AbstractText"):
        rot = t.get("Label")
        partes.append(f"{rot}: {texto(t)}" if rot else texto(t))
    resumo = " ".join(p for p in partes if p)
    if livro:
        ano = raiz.findtext("Book/PubDate/Year") or ""
        periodico = texto(raiz.find("Book/BookTitle"))
    else:
        pd = a.find("Journal/JournalIssue/PubDate")
        ano = (pd.findtext("Year") if pd is not None else None) or ""
        if not ano and pd is not None and pd.findtext("MedlineDate"):
            ano = pd.findtext("MedlineDate")[:4]
        if not ano:
            ano = a.findtext("ArticleDate/Year") or ""
        periodico = texto(a.find("Journal/Title"))
    autor = (a.find("AuthorList/Author") if not livro else raiz.find("AuthorList/Author"))
    primeiro = ""
    if autor is not None:
        primeiro = autor.findtext("LastName") or autor.findtext("CollectiveName") or ""
    ids = {i.get("IdType"): (i.text or "").strip() for i in art.findall("PubmedData/ArticleIdList/ArticleId")}
    doi = ids.get("doi") or ""
    if not doi:
        for e in a.findall("ELocationID"):
            if e.get("EIdType") == "doi":
                doi = (e.text or "").strip()
    return {
        "pmid": pmid,
        "doi": doi.lower(),
        "pmcid": ids.get("pmc", ""),
        "titulo": titulo,
        "ano": ano,
        "periodico": periodico,
        "primeiro_autor": primeiro,
        "idiomas": "|".join(l.text for l in a.findall("Language") if l.text),
        "tipos_publicacao": "|".join(texto(p) for p in a.findall("PublicationTypeList/PublicationType")),
        "resumo": resumo,
    }


def efetch(pmids):
    out = {}
    for i in range(0, len(pmids), LOTE):
        lote = pmids[i:i + LOTE]
        r = post("efetch.fcgi", {"db": "pubmed", "id": ",".join(lote), "retmode": "xml"})
        raiz = ET.fromstring(r.content)
        for art in list(raiz):
            if art.tag in ("PubmedArticle", "PubmedBookArticle"):
                d = parse_artigo(art)
                out[d["pmid"]] = d
        print(f"  efetch {min(i + LOTE, len(pmids))}/{len(pmids)}", file=sys.stderr)
    faltam = [p for p in pmids if p not in out]
    if faltam:
        sys.exit(f"efetch não devolveu {len(faltam)} PMIDs (ex.: {faltam[:5]}); nada gravado")
    return out


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest() if s else ""


def nome(bloco, linha):
    return f"pubmed-{bloco}-{linha.strip('#').lower()}"


def grava(bloco, linha, registros, camada_de):
    os.makedirs(REG, exist_ok=True)
    os.makedirs(BRUTO, exist_ok=True)
    base = nome(bloco, linha)
    with open(os.path.join(REG, base + ".csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for d in registros:
            w.writerow({"fonte": "PubMed", "bloco": bloco, "linha": linha,
                        **{k: d[k] for k in CAMPOS if k in d and k != "resumo"},
                        "camada": camada_de(d["pmid"]),
                        "tem_resumo": int(bool(d["resumo"])),
                        "n_car_resumo": len(d["resumo"]),
                        "sha256_resumo": sha(d["resumo"])})
    with open(os.path.join(BRUTO, base + ".jsonl"), "w", encoding="utf-8") as f:
        for d in registros:
            f.write(json.dumps({"fonte": "PubMed", "bloco": bloco, "linha": linha,
                                "camada": camada_de(d["pmid"]), **d}, ensure_ascii=False) + "\n")


def loga(entrada):
    with open(os.path.join(REG, "coletas.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(entrada, ensure_ascii=False) + "\n")


def coleta():
    agora = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for bloco, linha, linha_flag in COLETAS:
        ln = linha_congelada(bloco, linha)
        print(f"{bloco} {linha}: esearch", file=sys.stderr)
        res = esearch(ln["query"])
        pmids = res["idlist"]
        assert len(pmids) == int(res["count"]), "idlist incompleta"
        camada1 = None
        if linha_flag:
            flag = linha_congelada(bloco, linha_flag)
            res1 = esearch(f"#{res['querykey']} AND {flag['query']}", webenv=res["webenv"])
            camada1 = set(res1["idlist"])
            assert camada1 <= set(pmids), "camada 1 fora do conjunto de triagem"
        regs = efetch(pmids)
        ordenados = [regs[p] for p in pmids]  # ordem do esearch (mais recente primeiro)
        camada_de = (lambda p: "") if camada1 is None else (lambda p: 1 if p in camada1 else 2)
        grava(bloco, linha, ordenados, camada_de)
        entrada = {
            "data_utc": agora, "fonte": "PubMed", "bloco": bloco, "linha": linha,
            "contagem_congelada": ln.get("count"), "data_congelamento": ln.get("run_date"),
            "contagem_hoje": int(res["count"]), "baixados": len(ordenados),
            "com_resumo": sum(1 for d in ordenados if d["resumo"]),
            "querytranslation": res.get("querytranslation", ""),
            "arquivo": f"registros/{nome(bloco, linha)}.csv",
        }
        if camada1 is not None:
            entrada.update({"linha_marca": linha_flag, "camada1_hoje": len(camada1),
                            "camada2_hoje": len(pmids) - len(camada1)})
        loga(entrada)
        print(json.dumps({k: v for k, v in entrada.items() if k != "querytranslation"},
                         ensure_ascii=False), file=sys.stderr)


def reidratar():
    """Refaz os JSONL (com resumo) a partir dos PMIDs versionados e confere o SHA-256."""
    for bloco, linha, _ in COLETAS:
        base = nome(bloco, linha)
        linhas = list(csv.DictReader(open(os.path.join(REG, base + ".csv"), encoding="utf-8")))
        regs = efetch([l["pmid"] for l in linhas])
        mudou = [l["pmid"] for l in linhas if sha(regs[l["pmid"]]["resumo"]) != l["sha256_resumo"]]
        os.makedirs(BRUTO, exist_ok=True)
        with open(os.path.join(BRUTO, base + ".jsonl"), "w", encoding="utf-8") as f:
            for l in linhas:
                f.write(json.dumps({"fonte": "PubMed", "bloco": bloco, "linha": linha,
                                    "camada": l["camada"], **regs[l["pmid"]]}, ensure_ascii=False) + "\n")
        print(f"{base}: {len(linhas)} reidratados; {len(mudou)} resumos mudaram desde a coleta"
              + (f" (ex.: {mudou[:5]})" if mudou else ""), file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reidratar", action="store_true")
    args = ap.parse_args()
    reidratar() if args.reidratar else coleta()
