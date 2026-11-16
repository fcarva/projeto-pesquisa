"""Rodada 21 — banana por tipologia (agricultura familiar), Censo Agro 2017.

Fonte: SIDRA, tabela 6955, classificação 829 (tipologia) × 227 = Banana (4930),
municípios do Ceará, 2017. Variáveis: 9504 (estabelecimentos com 50 pés e
mais), 10078 (área colhida, ha), 9506 (quantidade produzida).

Serve ao grupo de comparação do desenho de calendário ("banana predominantemente
familiar"). ⚠️ O IBGE desidentifica (X) células pequenas: a fração familiar por
ÁREA some em cerca de metade dos municípios; a fração por ESTABELECIMENTO é a
que sobrevive. O limiar é decisão do plano de análise, não deste script.

Junta a contagem de aeronave do Censo 2006 (script 13) se o arquivo existir.
"""
from __future__ import annotations

import argparse
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

API = "https://servicodados.ibge.gov.br/api/v3/agregados/6955"
VARS = {9504: "estab", 10078: "area_colhida_ha", 9506: "qtd_t"}
TIP = {"46302": "total", "46304": "fam", "46303": "nfam"}


def baixa(uf: str) -> pd.DataFrame:
    import requests
    linhas = []
    for var, nome in VARS.items():
        url = (f"{API}/periodos/2017/variaveis/{var}?localidades=N6[N3[{uf}]]"
               f"&classificacao=829[{','.join(TIP)}]|227[4930]|218[46502]|12517[113601]")
        r = requests.get(url, timeout=180)
        r.raise_for_status()
        for res in r.json()[0]["resultados"]:
            cid = next(list(c["categoria"])[0] for c in res["classificacoes"] if c["id"] == "829")
            for s in res["series"]:
                linhas.append((s["localidade"]["id"], s["localidade"]["nome"],
                               f"{nome}__{TIP[cid]}", s["serie"]["2017"]))
    return pd.DataFrame(linhas, columns=["cod_ibge7", "municipio", "k", "valor"])


def main(argv=None) -> int:
    warnings.filterwarnings("ignore")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--uf", default="23")
    a = ap.parse_args(argv)

    r = baixa(a.uf)
    sigilo = int((r["valor"] == "X").sum())
    # "-" é zero; "X" (desidentificado) e "..." ficam ausentes — não são zero.
    r["v"] = pd.to_numeric(r["valor"].replace({"-": "0", "X": np.nan, "...": np.nan}), errors="coerce")
    nomes = r.drop_duplicates("cod_ibge7").set_index("cod_ibge7")["municipio"]
    w = r.pivot(index="cod_ibge7", columns="k", values="v").reset_index()
    w.insert(1, "municipio", w["cod_ibge7"].map(nomes))
    w["share_fam_estab"] = w["estab__fam"] / w["estab__total"]
    w["share_fam_area"] = w["area_colhida_ha__fam"] / w["area_colhida_ha__total"]
    aer = a.out_dir / "censo_agro_equipamento_ce.csv"
    if aer.exists():
        w = w.merge(pd.read_csv(aer, dtype={"cod_ibge7": str})[["cod_ibge7", "aeronave"]],
                    on="cod_ibge7", how="left")
    a.out_dir.mkdir(parents=True, exist_ok=True)
    destino = a.out_dir / "censo2017_banana_familiar_ce.csv"
    w.to_csv(destino, index=False)
    b = w[w["estab__total"] > 0]
    print(f"municípios: {len(w)} | com banana: {len(b)} | células sob sigilo (X): {sigilo}")
    print(f"fração familiar por área ausente: {int(b['share_fam_area'].isna().sum())} de {len(b)}")
    print(f"[ok] {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
