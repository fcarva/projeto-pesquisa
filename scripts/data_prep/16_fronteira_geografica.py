"""E16 — A pergunta que o gate do script 14 não faz: os tratados estão NA fronteira?

POR QUE ESTE SCRIPT EXISTE
--------------------------

O gate do script 14 responde se o vizinho **tinha pulverização aérea** (G1), se
o **melão fecha suporte** (G2) e se o **registro é comparável** (G3). Nenhuma das
três olha para o mapa — e um desenho de fronteira é, antes de tudo, uma
afirmação geométrica: as unidades tratadas têm de estar *na linha* que separa os
dois regimes. Um vizinho pode passar nos três portões e ainda assim não servir,
porque o grupo tratado está a 300 km da divisa.

⚠️ E foi exatamente o que aconteceu. Rodado em 2026-09-22 (ver
`docs/ars/15-gate-rota1-resultado.md` §7):

- **Pernambuco passou o G1 com folga** — 40 estabelecimentos com aeronave em 12
  municípios, mais que os 36 do próprio Ceará — e **nenhum** dos 17 municípios
  do decil superior da banana toca a divisa com ele. O mais próximo, Missão
  Velha, está a 19 km e não tinha aeronave. Distância média dos 17: **323 km**.
- **Os dois únicos tratados COM aeronave** — Limoeiro do Norte (18) e Quixeré
  (9), que somam as 27 aeronaves do decil — **tocam a divisa do Rio Grande do
  Norte**. A Chapada do Apodi está em cima da linha potiguar.

Isto não reabilita o RN no G1 nem reprova o PE no seu: é **outra dimensão**, e
ela entra na decisão junto com as outras, não no lugar delas.

FONTE
-----

Malha municipal do IBGE via **geobr** (IPEA), `read_municipality(year=...)`.

> Pereira, R. H. M. & Gonçalves, C. N. (2019). *geobr: Loads Shapefiles of
> Official Spatial Data Sets of Brazil.* IPEA. github.com/ipeaGIT/geobr

⚠️ **Duas ressalvas de proveniência, e a segunda é séria:**

1. A malha é de **2022**; os limites municipais do Ceará não mudaram no período
   do desenho, mas o ano é do arquivo, não do dado do ban.
2. O `geobr` baixa com **verificação TLS desativada** (`InsecureRequestWarning`
   em `github.com` e `release-assets.githubusercontent.com`). O conteúdo vem do
   GitHub Releases do IPEA, mas a cadeia não é verificada. Anotado aqui porque
   este repositório exige proveniência por fonte, e "veio do geobr" não é o
   mesmo que "veio verificado".

⚠️ O QUE ESTE SCRIPT NÃO FAZ
-----------------------------

- **Não decide o vizinho, nem monta painel, nem estima.** Trocar o grupo de
  comparação é mudança de identificação e passa pelo orientador (CLAUDE.md).
- **Não substitui o gate.** Ele mede geometria; o script 14 mede método,
  suporte e registro. Um vizinho precisa dos dois.
- **Não mede distância de exposição.** "Tocar a divisa" é adjacência de
  polígono, não alcance de deriva de pulverização.

Uso:
    python scripts/data_prep/16_fronteira_geografica.py
    python scripts/data_prep/16_fronteira_geografica.py --vizinhos 24 22 26
    python scripts/data_prep/16_fronteira_geografica.py --simplificado

Saída: `data/processed/fronteira_geografica__uf23.csv` (gitignored).
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
OUT_DIR = RAIZ / "data" / "processed"

UF_CEARA = "23"
SIGLA_POR_UF = {"23": "CE", "24": "RN", "22": "PI", "25": "PB", "26": "PE"}
VIZINHOS_PADRAO = ("24", "22", "26")
ANO_MALHA = 2022

# ⚠️ SIRGAS 2000 / Brasil Polyconic. A malha do geobr vem em EPSG:4674, que é
# GEOGRÁFICO: distância ali sai em GRAUS, e um grau não é um quilômetro. Medir
# sem reprojetar daria números plausíveis e errados — a classe de erro que este
# repositório mais persegue.
CRS_METRICO = 5880

# Área positiva da cultura-âncora define o denominador do decil, como no
# script 12: 169 municípios na banana, decil = 17. Ver docs/ars/15 §5.
CULTURA_PADRAO = "banana"


def carrega_malha(siglas, ano: int = ANO_MALHA, simplificado: bool = False):
    """Malha municipal por UF, reprojetada para o CRS métrico.

    `simplificado=False` de propósito: o padrão do geobr é a geometria
    simplificada, e adjacência de fronteira é justamente onde simplificar pode
    mentir. Rodado dos dois jeitos em 2026-09-22, o resultado bateu — mas o
    padrão aqui é o caro, e quem quiser o barato pede.
    """
    import geobr

    return {sigla: geobr.read_municipality(code_muni=sigla, year=ano,
                                           simplified=simplificado).to_crs(CRS_METRICO)
            for sigla in siglas}


def decil_superior(pam: pd.DataFrame, cultura: str = CULTURA_PADRAO) -> set[str]:
    """Municípios do decil superior de área da cultura — o grupo tratado.

    Mesma convenção do Gate 1 e do script 12: o decil sai sobre os municípios
    com área POSITIVA (169 na banana → 17), não sobre os 184 do estado. Foi
    essa distinção que gerou a divergência 17 × 19 do repositório.
    """
    col = "area_ha_media" if "area_ha_media" in pam.columns else "area_ha"
    bloco = pam[pam["cultura"].str.contains(cultura, case=False, na=False)]
    bloco = bloco[bloco[col] > 0]
    if bloco.empty:
        raise ValueError(f"nenhum município com área positiva de {cultura!r}")
    k = max(1, round(bloco["cod_ibge"].nunique() / 10))
    return set(bloco.nlargest(k, col)["cod_ibge"].astype(str))


def adjacencia(ce, vizinho, tratados: set[str]) -> dict:
    """Quantos municípios do CE — e quantos TRATADOS — tocam a UF vizinha."""
    borda = vizinho.union_all()
    tocam = ce[ce.geometry.intersects(borda)]
    trat = ce[ce["cod7"].isin(tratados)]
    trat_na_borda = trat[trat.geometry.intersects(borda)]
    distancias = trat.geometry.distance(borda) / 1000.0
    return {
        "municipios_ce_na_fronteira": int(len(tocam)),
        "tratados_na_fronteira": int(len(trat_na_borda)),
        "tratados_total": int(len(trat)),
        "dist_media_tratados_km": float(distancias.mean()),
        "dist_minima_tratados_km": float(distancias.min()),
        "nomes_tratados_na_fronteira": ", ".join(sorted(trat_na_borda["name_muni"])),
    }


def tabela_por_tratado(ce, malhas: dict, tratados: set[str],
                       com_aeronave: set[str]) -> pd.DataFrame:
    """Uma linha por município tratado, com a distância a cada divisa."""
    trat = ce[ce["cod7"].isin(tratados)]
    bordas = {s: g.union_all() for s, g in malhas.items() if s != "CE"}
    linhas = []
    for _, mun in trat.iterrows():
        linha = {"municipio": mun["name_muni"], "cod_ibge7": mun["cod7"],
                 "tem_aeronave_2006": mun["cod7"] in com_aeronave}
        for sigla, borda in bordas.items():
            linha[f"dist_{sigla}_km"] = round(mun.geometry.distance(borda) / 1000.0)
        cols = [c for c in linha if c.startswith("dist_")]
        linha["fronteira_mais_proxima"] = min(cols, key=lambda c: linha[c])[5:-3]
        linhas.append(linha)
    return pd.DataFrame(linhas).sort_values("municipio")


def imprime(resumo: pd.DataFrame, detalhe: pd.DataFrame) -> None:
    larg = 84
    print("=" * larg)
    print("FRONTEIRA GEOGRÁFICA — os tratados estão NA linha?")
    print("=" * larg)
    print(resumo.to_string(index=False))
    print()
    print("Por município tratado (distância em km à divisa de cada UF):")
    print(detalhe.to_string(index=False))
    print("=" * larg)
    print("  ⚠️ Isto NÃO decide o vizinho: é uma dimensão a mais, ao lado do")
    print("     método (G1), do suporte (G2) e do registro (G3) do script 14.")
    print("  ⚠️ 'Tocar a divisa' é adjacência de polígono — não é alcance de")
    print("     deriva de pulverização, que é outra pergunta e outro dado.")
    print("=" * larg)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--vizinhos", nargs="+", default=list(VIZINHOS_PADRAO),
                   metavar="COD", help="Códigos IBGE das UFs vizinhas (24 22 26).")
    p.add_argument("--pam", type=Path,
                   default=OUT_DIR / "pam_ce_muni_cultura_media__sidra.parquet",
                   help="PAM município×cultura do Ceará (script 01).")
    p.add_argument("--censo", type=Path,
                   default=OUT_DIR / "censo_agro_equipamento_ce.csv",
                   help="Equipamento por município (script 13). Opcional.")
    p.add_argument("--cultura", default=CULTURA_PADRAO)
    p.add_argument("--ano-malha", type=int, default=ANO_MALHA)
    p.add_argument("--simplificado", action="store_true",
                   help="Usa a geometria simplificada do geobr (mais rápida).")
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    if UF_CEARA in args.vizinhos:
        print("[erro] 23 não é vizinho: o Ceará é o grupo tratado.")
        return 1
    desconhecidas = [u for u in args.vizinhos if u not in SIGLA_POR_UF]
    if desconhecidas:
        print(f"[erro] UF sem sigla em SIGLA_POR_UF: {desconhecidas}")
        return 1
    if not args.pam.exists():
        print(f"[erro] PAM não encontrado: {args.pam}")
        print("       Rode antes: scripts/data_prep/01_check_dose_variation.py --fonte sidra")
        return 1

    tratados = decil_superior(pd.read_parquet(args.pam), args.cultura)
    print(f"[ok] decil superior de {args.cultura!r}: {len(tratados)} municípios")

    com_aeronave: set[str] = set()
    if args.censo.exists():
        censo = pd.read_csv(args.censo, dtype={"cod_ibge7": str})
        com_aeronave = set(censo.loc[censo["aeronave"] > 0, "cod_ibge7"].astype(str))
    else:
        print(f"[aviso] sem {args.censo.name}: a coluna de aeronave sai vazia.")

    siglas = ["CE"] + [SIGLA_POR_UF[u] for u in args.vizinhos]
    malhas = carrega_malha(siglas, args.ano_malha, args.simplificado)
    ce = malhas["CE"].copy()
    ce["cod7"] = ce["code_muni"].astype("int64").astype(str)

    linhas = []
    for uf in args.vizinhos:
        sigla = SIGLA_POR_UF[uf]
        linhas.append({"vizinho_uf": uf, "vizinho": sigla,
                       **adjacencia(ce, malhas[sigla], tratados)})
    resumo = pd.DataFrame(linhas)
    detalhe = tabela_por_tratado(ce, malhas, tratados, com_aeronave)
    imprime(resumo, detalhe)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    # Proveniência viaja DENTRO do arquivo, não só no nome.
    resumo["cultura"] = args.cultura
    resumo["ano_malha"] = args.ano_malha
    resumo["geometria"] = "simplificada" if args.simplificado else "completa"
    resumo["extraido_em"] = date.today().isoformat()
    destino = args.out_dir / f"fronteira_geografica__uf{UF_CEARA}.csv"
    resumo.to_csv(destino, index=False, encoding="utf-8")
    detalhe.to_csv(args.out_dir / f"fronteira_geografica_tratados__uf{UF_CEARA}.csv",
                   index=False, encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
