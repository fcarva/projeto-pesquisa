"""Valida as saídas dos triadores, mede a concordância e consolida as decisões (Etapa 5).

Entradas (em `registros/triagem/`):
- `<sq>-<modo>-manifesto.csv` (de `prepara_triagem.py`);
- `<sq>-<modo>-triador-1.json` e `-triador-2.json` (piloto), ou um par por lote,
  `<sq>-<modo>-lote-NNN-triador-{1,2}.json` (triagem completa). Com lotes, entram só os que
  já têm os dois triadores; os demais são listados como pendentes;
- opcional, `<sq>-<modo>-adjudicacao.json`: a resposta do adjudicador às divergências.

Faz:
1. **validação do esquema** (PRISMA-trAIce M5): todo ID do manifesto aparece uma vez; `decisao` em
   incluir/excluir; `motivo` nulo se e só se incluir, e da lista fechada;
2. **citação literal**: confere se `citacao` aparece no título ou no resumo do lote (espaços e caixa
   normalizados) e reporta a taxa. Uma citação que não está no texto é sinal de paráfrase ou invenção;
3. **concordância**: tabela 2 × 2, concordância observada e κ de Cohen;
4. **divergências**: grava o lote para o adjudicador em `data/raw/.../triagem/<sq>-<modo>-divergencias.json`
   (com o texto; fora do git);
5. com a adjudicação: `registros/triagem/<sq>-<modo>-decisoes.csv` (decisão final por registro) e,
   na triagem completa, o `registros/decisoes-<sq>.csv` que o `prisma.py` lê.

    python3 ferramentas/concordancia.py --sq sq1 --modo piloto
"""
import argparse
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coleta_openalex import BRUTO, REG  # noqa: E402

MOTIVOS = {"fora_do_tema", "exposicao", "desfecho", "desenho", "animal_ou_in_vitro", "revisao", "tipo_documento"}
DIR = os.path.join(REG, "triagem")
DIR_LOTES = os.path.join(BRUTO, "triagem")


def norm(t):
    return " ".join(re.sub(r"[^\w]+", " ", (t or "").lower()).split())


def le_json(caminho):
    texto = open(caminho, encoding="utf-8").read().strip()
    texto = re.sub(r"^```(?:json)?\s*|\s*```$", "", texto)
    return json.loads(texto)


def valida(decs, ids, nome, textos):
    erros, literais = [], 0
    vistos = [d.get("id") for d in decs]
    if sorted(vistos) != sorted(ids):
        erros.append(f"{nome}: IDs diferentes do lote (faltam {sorted(set(ids) - set(vistos))[:5]}, "
                     f"sobram {sorted(set(vistos) - set(ids))[:5]}, repetidos {len(vistos) - len(set(vistos))})")
    for d in decs:
        if d.get("decisao") not in ("incluir", "excluir"):
            erros.append(f"{nome} {d.get('id')}: decisao inválida {d.get('decisao')!r}")
        if (d.get("decisao") == "incluir") != (d.get("motivo") is None):
            erros.append(f"{nome} {d.get('id')}: motivo {d.get('motivo')!r} incoerente com {d.get('decisao')}")
        if d.get("motivo") is not None and d["motivo"] not in MOTIVOS:
            erros.append(f"{nome} {d.get('id')}: motivo fora da lista {d['motivo']!r}")
        if norm(d.get("citacao")) and norm(d.get("citacao")) in textos.get(d.get("id"), ""):
            literais += 1
    return erros, literais


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(x == "incluir" for x in a) / n, sum(x == "incluir" for x in b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return po, (po - pe) / (1 - pe) if pe < 1 else 1.0


def roda(sq, modo):
    base = f"{sq}-{modo}"
    man = {m["id_lote"]: m for m in csv.DictReader(open(os.path.join(DIR, f"{base}-manifesto.csv"), encoding="utf-8"))}
    lote = {}
    for caminho in sorted(glob.glob(os.path.join(DIR_LOTES, f"{base}-lote-*.json"))):
        for r in json.load(open(caminho, encoding="utf-8")):
            lote[r["id"]] = r
    textos = {i: norm(f"{r['titulo']} {r.get('resumo') or ''}") for i, r in lote.items()}
    unico = os.path.join(DIR, f"{base}-triador-1.json")
    if os.path.exists(unico):
        t = [{d["id"]: d for d in le_json(os.path.join(DIR, f"{base}-triador-{k}.json"))} for k in (1, 2)]
        ids = sorted(man)
        lotes_pendentes = []
    else:
        t, lotes_ok, lotes_pendentes = [{}, {}], [], []
        for n in sorted({m["lote"] for m in man.values()}, key=int):
            caminhos = [os.path.join(DIR, f"{base}-lote-{int(n):03d}-triador-{k}.json") for k in (1, 2)]
            if all(os.path.exists(c) for c in caminhos):
                for k, c in enumerate(caminhos):
                    t[k].update({d["id"]: d for d in le_json(c)})
                lotes_ok.append(n)
            else:
                lotes_pendentes.append(n)
        ids = sorted(i for i, m in man.items() if m["lote"] in lotes_ok)
        if not ids:
            sys.exit(f"nenhum lote com os dois triadores; pendentes: {lotes_pendentes}")
    erros, lits = [], []
    for k in (0, 1):
        e, l = valida(list(t[k].values()), ids, f"triador-{k + 1}", textos)
        erros += e
        lits.append(l)
    if erros:
        sys.exit("Saída fora do esquema; nada consolidado:\n  " + "\n  ".join(erros[:20]))
    a = [t[0][i]["decisao"] for i in ids]
    b = [t[1][i]["decisao"] for i in ids]
    po, k = kappa(a, b)
    tab = {f"{x}/{y}": sum(1 for p, q in zip(a, b) if (p, q) == (x, y))
           for x in ("incluir", "excluir") for y in ("incluir", "excluir")}
    div = [i for i in ids if t[0][i]["decisao"] != t[1][i]["decisao"]]
    ambos_exc = [i for i in ids if a[ids.index(i)] == b[ids.index(i)] == "excluir"]
    motivo_igual = sum(1 for i in ambos_exc if t[0][i]["motivo"] == t[1][i]["motivo"])
    resumo = {"sq": sq, "modo": modo, "registros": len(ids), "lotes_pendentes": lotes_pendentes,
              "tabela_t1_t2": tab,
              "concordancia_observada": round(po, 3), "kappa_cohen": round(k, 3),
              "divergencias": len(div), "citacao_literal": {"triador-1": f"{lits[0]}/{len(ids)}",
                                                            "triador-2": f"{lits[1]}/{len(ids)}"},
              "ambos_excluem_mesmo_motivo": f"{motivo_igual}/{len(ambos_exc)}"}
    lote_div = [{**lote[i], "triador_1": {c: t[0][i].get(c) for c in ("decisao", "motivo", "citacao")},
                 "triador_2": {c: t[1][i].get(c) for c in ("decisao", "motivo", "citacao")}} for i in div]
    json.dump(lote_div, open(os.path.join(DIR_LOTES, f"{base}-divergencias.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    adj_caminho = os.path.join(DIR, f"{base}-adjudicacao.json")
    adj = {}
    if os.path.exists(adj_caminho):
        adj = {d["id"]: d for d in le_json(adj_caminho)}
        e, _ = valida(list(adj.values()), div, "adjudicador", textos)
        if e:
            sys.exit("Adjudicação fora do esquema:\n  " + "\n  ".join(e[:20]))
    linhas = []
    for i in ids:
        x, y = t[0][i], t[1][i]
        # (registros de lotes pendentes não entram aqui)
        if x["decisao"] == y["decisao"]:
            final, motivo, origem = x["decisao"], x["motivo"] if x["motivo"] == y["motivo"] else (x["motivo"] or y["motivo"]), "consenso"
        elif i in adj:
            final, motivo, origem = adj[i]["decisao"], adj[i]["motivo"], "adjudicacao"
        else:
            final, motivo, origem = "", "", "pendente"
        linhas.append({"id_lote": i, "id_unico": man[i]["id_unico"], "camada": man[i]["camada"],
                       "triador_1": x["decisao"], "motivo_1": x["motivo"] or "",
                       "triador_2": y["decisao"], "motivo_2": y["motivo"] or "",
                       "adjudicacao": adj.get(i, {}).get("decisao", ""), "decisao_final": final,
                       "motivo_final": motivo or "", "origem": origem,
                       "para_citacoes": int(bool(x.get("para_citacoes") or y.get("para_citacoes")
                                                 or adj.get(i, {}).get("para_citacoes")))})
    with open(os.path.join(DIR, f"{base}-decisoes.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)
    resumo["finais"] = {o: sum(1 for l in linhas if l["decisao_final"] == o) for o in ("incluir", "excluir", "")}
    resumo["adjudicadas"] = sum(1 for l in linhas if l["origem"] == "adjudicacao")
    json.dump(resumo, open(os.path.join(DIR, f"{base}-resumo.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(json.dumps(resumo, ensure_ascii=False, indent=1))
    if modo == "completo" and all(l["decisao_final"] for l in linhas):
        with open(os.path.join(REG, f"decisoes-{sq}.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["id_unico", "titulo_resumo", "texto_obtido", "texto_completo",
                                              "motivo", "estudo"])
            w.writeheader()
            for l in linhas:
                w.writerow({"id_unico": l["id_unico"], "titulo_resumo": l["decisao_final"], "texto_obtido": "",
                            "texto_completo": "", "motivo": "", "estudo": ""})


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sq", default="sq1")
    ap.add_argument("--modo", default="piloto")
    a = ap.parse_args()
    roda(a.sq, a.modo)
