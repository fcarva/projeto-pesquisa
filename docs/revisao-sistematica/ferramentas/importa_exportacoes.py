"""Importa as exportações do pesquisador (Scopus pela CAPES, SciELO, LILACS) para o esquema comum.

Lê `registros/importados/<fonte>-<sq>[-<linha>]-<AAAA-MM-DD>.<ris|csv|txt>`, por exemplo
`scopus-sq1-2026-10-20.ris`, `scielo-sq1-S2b-2026-10-20.ris` ou `lilacs-sq1-2026-10-20.ris`.
O token de linha é opcional: com ele, a deduplicação sabe a camada (SciELO S1'/S3 e LILACS L1'
são de efeito; S2', S2b, L2'' e L2b são de contexto). Formatos: RIS (todas as fontes) e o CSV
do Scopus.

Saídas, no padrão dos coletores:
- `registros/importado-<nome do arquivo sem extensão>.csv`: metadados + SHA-256 do resumo;
- `data/raw/revisao-sistematica/importado-<…>.jsonl`: com o resumo (fora do git);
- uma linha por arquivo em `registros/coletas.jsonl`. Se `registros/importados/LEIAME.md` tiver
  uma linha de tabela `| <arquivo> | <contagem> | <data> |`, a contagem declarada é conferida.

    python3 ferramentas/importa_exportacoes.py
"""
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coleta_openalex import BRUTO, REG, loga, sha  # noqa: E402

PASTA = os.path.join(REG, "importados")
NOME_FONTE = {"scopus": "Scopus (exportação)", "scielo": "SciELO", "lilacs": "LILACS"}
PADRAO = re.compile(r"^(scopus|scielo|lilacs)-(sq[123])(?:-([^-]+))?-(\d{4}-\d{2}-\d{2})\.(ris|csv|txt)$", re.I)
CAMPOS = ["fonte", "bloco", "linha", "posicao", "eid", "pmid", "doi", "titulo", "ano", "periodico", "tipo",
          "idioma", "primeiro_autor", "tem_resumo", "n_car_resumo", "sha256_resumo"]


def doi_limpo(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", d)
    return d.rstrip(".,;)")


def le_ris(texto):
    """RIS -> lista de dicts (tag -> lista de valores)."""
    recs, cur = [], {}
    for linha in texto.splitlines():
        m = re.match(r"^([A-Z][A-Z0-9])  -\s?(.*)$", linha)
        if not m:
            continue
        tag, val = m.group(1), m.group(2).strip()
        if tag == "ER":
            if cur:
                recs.append(cur)
            cur = {}
            continue
        cur.setdefault(tag, []).append(val)
    if cur:
        recs.append(cur)
    return recs


def de_ris(r):
    def um(*tags):
        for t in tags:
            if r.get(t):
                return r[t][0]
        return ""
    url = " ".join(r.get("UR", []))
    eid = re.search(r"eid=(2-s2\.0-\d+)", url)
    ano = re.search(r"\d{4}", um("PY", "Y1", "DA") or "")
    autor = um("AU", "A1")
    doi_url = re.search(r"doi\.org/(10\.\S+)", url)
    return {
        "eid": eid.group(1) if eid else "",
        "pmid": "",
        "doi": doi_limpo(um("DO") or (doi_url.group(1) if doi_url else "")),
        "titulo": " ".join(um("TI", "T1").split()),
        "ano": ano.group(0) if ano else "",
        "periodico": um("T2", "JO", "JF", "JA"),
        "tipo": um("TY"),
        "idioma": "|".join(r.get("LA", [])),
        "primeiro_autor": autor.split(",")[0].strip() if autor else "",
        "resumo": " ".join(" ".join(r.get("AB", []) or r.get("N2", [])).split()),
    }


def de_csv_scopus(linha):
    g = lambda *ks: next((linha[k] for k in ks if linha.get(k)), "")  # noqa: E731
    autor = g("Authors", "Author full names")
    return {
        "eid": g("EID"),
        "pmid": g("PubMed ID"),
        "doi": doi_limpo(g("DOI")),
        "titulo": " ".join(g("Title").split()),
        "ano": g("Year"),
        "periodico": g("Source title"),
        "tipo": g("Document Type"),
        "idioma": g("Language of Original Document").replace("; ", "|"),
        "primeiro_autor": autor.split(",")[0].split(";")[0].strip() if autor else "",
        "resumo": "" if g("Abstract") == "[No abstract available]" else " ".join(g("Abstract").split()),
    }


def declarados():
    caminho = os.path.join(PASTA, "LEIAME.md")
    out = {}
    if os.path.exists(caminho):
        for l in open(caminho, encoding="utf-8"):
            c = [x.strip().strip("`") for x in l.strip().strip("|").split("|")]
            if len(c) >= 2 and PADRAO.match(c[0]) and c[1].replace(".", "").isdigit():
                out[c[0]] = int(c[1].replace(".", ""))
    return out


def importa(caminho):
    nome = os.path.basename(caminho)
    m = PADRAO.match(nome)
    if not m:
        print(f"ignorado (nome fora do padrão): {nome}", file=sys.stderr)
        return None
    fonte, sq, linha, data, ext = m.groups()
    texto = open(caminho, encoding="utf-8-sig", errors="replace").read()
    if ext.lower() == "csv":
        regs = [de_csv_scopus(l) for l in csv.DictReader(texto.splitlines())]
    else:
        regs = [de_ris(r) for r in le_ris(texto)]
    base = "importado-" + os.path.splitext(nome)[0]
    meta = {"fonte": NOME_FONTE[fonte.lower()], "bloco": sq.lower(), "linha": linha or "exportação"}
    with open(os.path.join(REG, base + ".csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for k, r in enumerate(regs, 1):
            w.writerow({**meta, "posicao": k, **{c: r[c] for c in CAMPOS if c in r},
                        "tem_resumo": int(bool(r["resumo"])), "n_car_resumo": len(r["resumo"]),
                        "sha256_resumo": sha(r["resumo"])})
    os.makedirs(BRUTO, exist_ok=True)
    with open(os.path.join(BRUTO, base + ".jsonl"), "w", encoding="utf-8") as f:
        for k, r in enumerate(regs, 1):
            f.write(json.dumps({**meta, "posicao": k, **r}, ensure_ascii=False) + "\n")
    declarado = declarados().get(nome)
    entrada = {"data_utc": data + "T00:00:00Z", "fonte": meta["fonte"], "bloco": meta["bloco"],
               "linha": meta["linha"], "papel": "importacao", "arquivo_origem": f"registros/importados/{nome}",
               "contagem_declarada": declarado, "importados": len(regs),
               "com_resumo": sum(1 for r in regs if r["resumo"]), "com_doi": sum(1 for r in regs if r["doi"]),
               "arquivo": f"registros/{base}.csv"}
    loga(entrada)
    if declarado is not None and declarado != len(regs):
        print(f"⚠️ {nome}: {len(regs)} registros lidos, {declarado} declarados no LEIAME", file=sys.stderr)
    print(json.dumps(entrada, ensure_ascii=False), file=sys.stderr)
    return entrada


if __name__ == "__main__":
    if not os.path.isdir(PASTA):
        sys.exit(f"sem a pasta {PASTA}: nada a importar")
    feitos = [importa(os.path.join(PASTA, n)) for n in sorted(os.listdir(PASTA))
              if n.lower().endswith((".ris", ".csv", ".txt"))]
    print(f"{sum(1 for f in feitos if f)} arquivo(s) importado(s)", file=sys.stderr)
