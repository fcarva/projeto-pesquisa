"""Confere as referências devolvidas por um assistente de IA (p. ex. LeapSpace) antes de usá-las.

Lê um Markdown de `registros/importados/` com uma tabela `| n | referência | doi |`. Para cada DOI:
1. **existe?** Crossref `/works/{doi}`: título, ano e periódico registrados;
2. **é a mesma obra?** O título do Crossref é comparado ao título informado (palavras em comum);
3. **já está no conjunto?** Procura o DOI (e, na falta, o título normalizado) nos
   `registros/deduplicado-sq{1,2,3}.csv`, com `id_unico`, exclusão automática e fontes.

Saída: `registros/<nome do arquivo>-conferencia.csv` e um resumo no terminal. Nada entra na
deduplicação por aqui: uma referência nova e verificada só vira registro depois da emenda que
autoriza o método (PRISMA 2020, "outros métodos").

    python3 ferramentas/confere_referencias_ia.py registros/importados/leapspace-sq1-2026-10-13.md
"""
import csv
import os
import re
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deduplica import REG, norm_doi, norm_titulo  # noqa: E402

MAILTO = "revisao.sistematica.ufes@example.org"
VAZIAS = set("a an the of and in on for to with by at from de da do e em na no para".split())


def le_tabela(caminho):
    out = []
    for l in open(caminho, encoding="utf-8"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 3 and c[0].isdigit():
            out.append({"n": int(c[0]), "referencia": c[1], "doi": norm_doi(c[2])})
    return out


def palavras(t):
    return {w for w in norm_titulo(t).split() if w not in VAZIAS and len(w) > 2}


def crossref(doi):
    for k in range(4):
        try:
            r = requests.get(f"https://api.crossref.org/works/{doi}", params={"mailto": MAILTO}, timeout=60)
        except requests.RequestException:
            time.sleep(2 ** (k + 1))
            continue
        if r.status_code == 404:
            return None
        if r.status_code == 200:
            m = r.json()["message"]
            ano = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
            return {"titulo": " ".join(((m.get("title") or [""])[0]).split()), "ano": ano,
                    "periodico": (m.get("container-title") or [""])[0], "tipo": m.get("type", "")}
        time.sleep(2 ** (k + 1))
    raise RuntimeError(f"Crossref não respondeu para {doi}")


def indice_pool():
    por_doi, por_tit = {}, {}
    for p in ("sq1", "sq2", "sq3"):
        caminho = os.path.join(REG, f"deduplicado-{p}.csv")
        for r in csv.DictReader(open(caminho, encoding="utf-8")):
            info = {"sq": p, "id_unico": r["id_unico"], "exclusao_auto": r["exclusao_auto"], "fontes": r["fontes"],
                    "camada": r.get("camada") or r.get("segmento", "")}
            if r["doi"]:
                por_doi.setdefault(r["doi"], []).append(info)
            t = norm_titulo(r["titulo"])
            if len(t) >= 30:
                por_tit.setdefault(t, []).append(info)
    return por_doi, por_tit


def roda(caminho):
    refs = le_tabela(caminho)
    por_doi, por_tit = indice_pool()
    linhas = []
    for r in refs:
        cr = crossref(r["doi"]) if r["doi"] else None
        time.sleep(0.2)
        informado = re.sub(r"^.*?\(\d{4}\)\s*", "", r["referencia"])
        comum = palavras(informado) & palavras(cr["titulo"]) if cr else set()
        confere = bool(cr) and len(comum) >= 0.6 * max(1, len(palavras(cr["titulo"])))
        achados = por_doi.get(r["doi"], []) or (por_tit.get(norm_titulo(cr["titulo"]), []) if cr else [])
        linhas.append({
            "n": r["n"], "doi": r["doi"], "crossref_existe": int(bool(cr)), "titulo_confere": int(confere),
            "titulo_crossref": cr["titulo"] if cr else "", "ano_crossref": cr["ano"] if cr else "",
            "periodico_crossref": cr["periodico"] if cr else "", "tipo_crossref": cr["tipo"] if cr else "",
            "no_conjunto": "|".join(sorted({a["sq"] for a in achados})),
            "id_unico": "|".join(a["id_unico"] for a in achados),
            "exclusao_auto": "|".join(a["exclusao_auto"] for a in achados if a["exclusao_auto"]),
            "fontes": "|".join(sorted({a["fontes"] for a in achados})),
            "referencia_informada": r["referencia"],
        })
    saida = os.path.join(REG, os.path.splitext(os.path.basename(caminho))[0] + "-conferencia.csv")
    with open(saida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)
    for l in linhas:
        status = ("NÃO EXISTE" if not l["crossref_existe"] else "título diverge" if not l["titulo_confere"]
                  else "ok")
        onde = l["no_conjunto"] or "NOVO"
        print(f"{l['n']:>2} {status:<15} {onde:<10} {l['exclusao_auto']:<8} {l['ano_crossref']} "
              f"{l['titulo_crossref'][:70]}")
    print(f"\n{len(linhas)} referências; {sum(l['crossref_existe'] for l in linhas)} existem no Crossref; "
          f"{sum(l['titulo_confere'] for l in linhas)} com título conferido; "
          f"{sum(1 for l in linhas if l['no_conjunto'])} já no conjunto; "
          f"{sum(1 for l in linhas if not l['no_conjunto'] and l['titulo_confere'])} novas e verificadas.\n"
          f"Arquivo: {os.path.relpath(saida, os.path.dirname(REG))}")


if __name__ == "__main__":
    roda(sys.argv[1])
