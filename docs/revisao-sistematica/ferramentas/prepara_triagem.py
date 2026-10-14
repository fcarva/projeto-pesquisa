"""Prepara os lotes de triagem por título e resumo (Etapa 5).

Para cada registro a triar de `registros/deduplicado-<sq>.csv`, monta o texto que o triador vê:
título, ano, tipo, periódico e o resumo da melhor fonte disponível, nesta ordem: PubMed, OpenAlex,
OASISBR/LA Referencia (JSONL em `data/raw/revisao-sistematica/`, reconstruídos com `--reidratar`)
e, por fim, o resumo hidratado por DOI (`resumos-hidratados.jsonl`). Registro sem resumo vai com
`resumo = null`, e o prompt manda decidir pelo título.

Modos:
- `--piloto`: amostra de 50 registros da SQ1, com semente fixa e estratificada por camada (30 da
  camada 1, 15 da 2 e 5 da 3). A camada 1 é sobreamostrada para o piloto ter casos de fronteira
  bastantes para calibrar a redação dos critérios. O κ do piloto é de calibração, não estimativa
  da concordância na triagem completa;
- `--completo`: todos os registros a triar, na ordem do `deduplicado` (camadas e segmentos).

Saídas:
- `data/raw/revisao-sistematica/triagem/<sq>-<modo>-lote-NNN.json`, com o texto (fora do git);
- `registros/triagem/<sq>-<modo>-manifesto.csv` (versionado): ID curto do lote → `id_unico`,
  camada, fonte e SHA-256 do resumo. O SHA-256 prova qual texto foi triado.

O resumo do OpenAlex que faltar localmente é buscado só para os registros do lote (filtro
`openalex:`), com `OPENALEX_API_KEY` ou a cota do IP.

    python3 ferramentas/prepara_triagem.py --piloto
    python3 ferramentas/prepara_triagem.py --completo --sq sq1 --tamanho 25
"""
import argparse
import csv
import glob
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coleta_openalex import BRUTO, REG, SemCredito, sha  # noqa: E402
from coleta_openalex import get as oa_get  # noqa: E402
from coleta_openalex import resumo as de_indice_invertido  # noqa: E402

SEMENTE = 20261013
PILOTO = {"1": 30, "2": 15, "3": 5}
MAX_RESUMO = 5000
DIR_LOTES = os.path.join(BRUTO, "triagem")
DIR_MANIF = os.path.join(REG, "triagem")
AVULSOS = os.path.join(BRUTO, "openalex-resumos-avulsos.jsonl")
ORDEM_FONTES = ["PubMed", "OpenAlex", "OASISBR", "LA Referencia"]


def id_api(fonte, i):
    """O deduplicado grava o ID VuFind como PAÍS/hash; o JSONL usa PAÍS_hash."""
    return i.replace("/", "_", 1) if fonte in ("OASISBR", "LA Referencia") else i


def indice_resumos():
    """(fonte, id) -> resumo, a partir dos JSONL locais."""
    idx = {}
    for caminho in glob.glob(os.path.join(BRUTO, "*.jsonl")):
        nome = os.path.basename(caminho)
        if nome.startswith(("pubmed-", "openalex-", "vufind-")):
            for l in open(caminho, encoding="utf-8"):
                r = json.loads(l)
                if not r.get("resumo"):
                    continue
                if nome.startswith("pubmed-"):
                    idx[("PubMed", r["pmid"])] = r["resumo"]
                elif nome.startswith("openalex-"):
                    idx[("OpenAlex", r["openalex_id"])] = r["resumo"]
                else:
                    idx[(r["fonte"], r["vufind_id"])] = r["resumo"]
    hid = os.path.join(BRUTO, "resumos-hidratados.jsonl")
    if os.path.exists(hid):
        for l in open(hid, encoding="utf-8"):
            r = json.loads(l)
            if r["status"] == "ok":
                idx.setdefault(("hidratado", r["doi"]), r["resumo"])
    return idx


def fontes_do_registro(u):
    """[(fonte, id)] em ordem de preferência, a partir de `resumo_em` e `resumo_hidratado`."""
    pares = []
    for item in filter(None, u["resumo_em"].split("|")):
        fonte, i = item.split(":", 1)
        pares.append((fonte, id_api(fonte, i)))
    pares.sort(key=lambda p: ORDEM_FONTES.index(p[0]) if p[0] in ORDEM_FONTES else 99)
    if u.get("resumo_hidratado") and u["doi"]:
        pares.append(("hidratado", u["doi"]))
    return pares


def busca_openalex(ids):
    """Resumos do OpenAlex para IDs que faltam localmente; grava em AVULSOS."""
    achados = {}
    for i in range(0, len(ids), 100):
        lote = ids[i:i + 100]
        res = oa_get({"filter": "openalex:" + "|".join(lote), "per-page": 100,
                      "select": "id,abstract_inverted_index"})["results"]
        for w in res:
            wid = w["id"].rsplit("/", 1)[-1]
            achados[wid] = de_indice_invertido(w.get("abstract_inverted_index"))
    os.makedirs(BRUTO, exist_ok=True)
    with open(AVULSOS, "a", encoding="utf-8") as f:
        for wid, txt in achados.items():
            f.write(json.dumps({"openalex_id": wid, "resumo": txt}, ensure_ascii=False) + "\n")
    return achados


def avulsos():
    out = {}
    if os.path.exists(AVULSOS):
        for l in open(AVULSOS, encoding="utf-8"):
            r = json.loads(l)
            if r["resumo"]:
                out[("OpenAlex", r["openalex_id"])] = r["resumo"]
    return out


def monta(registros):
    idx = {**indice_resumos(), **avulsos()}
    faltam = [i for u in registros for f, i in fontes_do_registro(u)
              if f == "OpenAlex" and (f, i) not in idx
              and not any(p in idx for p in fontes_do_registro(u))]
    faltam = sorted(set(faltam))
    if faltam:
        try:
            for wid, txt in busca_openalex(faltam).items():
                if txt:
                    idx[("OpenAlex", wid)] = txt
        except SemCredito as e:
            print(f"⚠️ OpenAlex indisponível para {len(faltam)} resumos ({str(e)[:100]})", file=sys.stderr)
    itens = []
    for u in registros:
        txt, fonte = None, ""
        for p in fontes_do_registro(u):
            if p in idx:
                txt, fonte = idx[p], p[0]
                break
        esperava = bool(u["resumo_em"] or u.get("resumo_hidratado"))
        itens.append({"u": u, "resumo": (txt or "")[:MAX_RESUMO] or None, "fonte_resumo": fonte,
                      "resumo_faltando_localmente": esperava and txt is None})
    return itens


def amostra_piloto(registros):
    rng = random.Random(SEMENTE)
    por_camada = {}
    for u in registros:
        por_camada.setdefault(u["camada"], []).append(u)
    escolha = []
    for camada, n in PILOTO.items():
        grupo = sorted(por_camada.get(camada, []), key=lambda u: u["id_unico"])
        escolha += rng.sample(grupo, n)
    rng.shuffle(escolha)
    return escolha


def grava(sq, modo, itens, tamanho):
    os.makedirs(DIR_LOTES, exist_ok=True)
    os.makedirs(DIR_MANIF, exist_ok=True)
    manifesto = []
    for k in range(0, len(itens), tamanho):
        lote, n_lote = itens[k:k + tamanho], k // tamanho + 1
        registros = []
        for j, it in enumerate(lote, k + 1):
            u, rid = it["u"], f"R{j:04d}"
            registros.append({"id": rid, "titulo": u["titulo"], "ano": u["ano"], "tipo": u["tipo"],
                              "periodico": u["periodico"], "resumo": it["resumo"]})
            manifesto.append({"id_lote": rid, "lote": n_lote, "id_unico": u["id_unico"],
                              "camada": u.get("camada") or u.get("segmento", ""), "fonte_resumo": it["fonte_resumo"],
                              "n_car_resumo": len(it["resumo"] or ""), "sha256_resumo": sha(it["resumo"] or ""),
                              "resumo_faltando_localmente": int(it["resumo_faltando_localmente"])})
        json.dump(registros, open(os.path.join(DIR_LOTES, f"{sq}-{modo}-lote-{n_lote:03d}.json"), "w",
                                  encoding="utf-8"), ensure_ascii=False, indent=1)
    with open(os.path.join(DIR_MANIF, f"{sq}-{modo}-manifesto.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(manifesto[0]))
        w.writeheader()
        w.writerows(manifesto)
    return manifesto


def roda(sq, modo, tamanho):
    caminho = os.path.join(REG, f"deduplicado-{sq}.csv")
    registros = [u for u in csv.DictReader(open(caminho, encoding="utf-8")) if not u["exclusao_auto"]]
    if modo == "piloto":
        registros = amostra_piloto(registros)
    itens = monta(registros)
    man = grava(sq, modo, itens, tamanho)
    com = sum(1 for m in man if m["n_car_resumo"])
    falt = sum(m["resumo_faltando_localmente"] for m in man)
    car = sum(m["n_car_resumo"] for m in man)
    print(f"{sq} {modo}: {len(man)} registros em {len({m['lote'] for m in man})} lote(s); "
          f"{com} com resumo; {falt} com resumo faltando localmente; {car:,} caracteres de resumo",
          file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--piloto", action="store_true")
    g.add_argument("--completo", action="store_true")
    ap.add_argument("--sq", default="sq1", choices=["sq1", "sq2", "sq3"])
    ap.add_argument("--tamanho", type=int, default=25, help="registros por lote")
    a = ap.parse_args()
    if a.piloto and a.sq != "sq1":
        sys.exit("o piloto é só da SQ1 (protocolo)")
    roda(a.sq, "piloto" if a.piloto else "completo", 50 if a.piloto else a.tamanho)
