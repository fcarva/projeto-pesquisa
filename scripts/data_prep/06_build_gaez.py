#!/usr/bin/env python3
"""Aptidão agroclimática FAO-GAEZ → índice municipal. A lacuna mais cara.

**Por que esta é a fonte prioritária, acima de SISAGUA, ANA e MapBiomas.** O
GAEZ tem **três papéis**, e o E6 promoveu dois deles de interpretativo para
mecânico:

| Papel | Onde | Status |
|---|---|---|
| Instrumento da exposição endógena | §5.2 da modelagem | como sempre foi |
| **Definição 4 de `d = 0`** | §5.3, construção 4 | ⚠️ **mecânico** |
| **Teste de contaminação do zero** | §5.3, teste | ⚠️ **mecânico** |

O motivo: o sieve do `contdid` faz `m0 <- mean(dy[dose == 0])` — **a curva
inteira é centrada no grupo de dose zero**. Trocar quem está no zero não
acrescenta ruído: **desloca o nível**. Sem GAEZ, três das quatro construções de
zero ficam impossíveis (a 3 depende de ANAC/SEMACE, também não adquirido), e o
**nível da curva fica sem banda de incerteza**.

Isto não é canal. É o resultado principal.

────────────────────────────────────────────────────────────────────────────
A RECEITA, E OS TRÊS JEITOS DE ERRÁ-LA EM SILÊNCIO
────────────────────────────────────────────────────────────────────────────
De Reynier & Rubin (2025), transcrita em `03-modelagem-ensaio1.md` §5.2:

1. **Diferença** de rendimento atingível entre os cenários de **alto e baixo
   insumo** — ⚠️ **não** o rendimento puro. O rendimento alto mede fertilidade;
   a *diferença* mede o quanto a terra responde a insumo, que é o que prediz
   adoção de cultivo intensivo. Usar o nível no lugar da diferença troca o
   instrumento por outra coisa, e nada acusa.
2. **Percentil nacional** da diferença — não do Ceará. O percentil define a
   posição relativa da terra no país, que é o que a receita original faz.
3. **Máximo entre as culturas** relevantes — e **depois** do percentil, não
   antes. Máximo de rendimentos brutos em unidades diferentes (t/ha de banana
   contra t/ha de milho) não significa nada; máximo de percentis, sim.
4. Reescala e normaliza em [0, 1].

Os três erros acima passam verdes: produzem um número plausível no intervalo
certo. Por isso a receita está separada da E/S e **testada sem raster nenhum**.

⚠️ **A ressalva que não pode sumir.** A receita do Reynier & Rubin é construída
sobre culturas **GM** — milho, soja, algodão. **Banana não é GM**, e é a
candidata a cultura-âncora aqui (flag 2 do `CLAUDE.md`). Então a transferência é
de *método*, não de *lista de culturas*: `--culturas` é obrigatório e sem padrão,
como a cultura-âncora no script 05. O script não escolhe.

────────────────────────────────────────────────────────────────────────────
DEPENDÊNCIAS
────────────────────────────────────────────────────────────────────────────
A E/S exige `requirements-geo.txt` (rasterio, geopandas, rasterstats) — **nada
disso está instalado por padrão**, e sem isso nenhuma fonte espacial é legível.
A receita não exige nada além de numpy/pandas, de propósito.

Uso:
    pip install -r requirements-geo.txt
    python scripts/data_prep/06_build_gaez.py \\
        --raster data/geo/gaez_alto.tif data/geo/gaez_baixo.tif \\
        --culturas banana melao \\
        --municipios data/geo/municipios_br.gpkg

Saída: data/processed/gaez_aptidao_muni.parquet (gitignored).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

OUT_DIR = Path("data/processed")
NOME_SAIDA = "gaez_aptidao_muni"

# Percentil calculado sobre o BRASIL, não sobre o Ceará. A receita original põe
# a terra na distribuição nacional; restringir ao estado mudaria o significado
# do índice sem mudar sua aparência.
ESCOPO_PERCENTIL = "nacional"


# --------------------------------------------------------------------------
# A receita — numpy puro, testável sem raster
# --------------------------------------------------------------------------

def diferenca_insumo(alto: np.ndarray, baixo: np.ndarray) -> np.ndarray:
    """Rendimento atingível sob alto insumo MENOS sob baixo insumo.

    ⚠️ É a diferença, não o nível. O nível mede fertilidade; a diferença mede
    **o quanto a terra responde a insumo**, que é o que prediz adoção de cultivo
    intensivo — e é isso que o instrumento precisa predizer.

    Negativos são possíveis em terra onde insumo não ajuda; ficam como estão,
    porque zerá-los inventaria um piso que a fonte não tem.
    """
    a = np.asarray(alto, dtype="float64")
    b = np.asarray(baixo, dtype="float64")
    if a.shape != b.shape:
        raise ValueError(f"Formas diferentes: alto {a.shape} vs baixo {b.shape}.")
    return a - b


def percentil_nacional(valores: np.ndarray) -> np.ndarray:
    """Posição de cada unidade na distribuição nacional, em [0, 1].

    Ausentes ficam ausentes — não entram no ranking e não recebem percentil.
    Imputá-los pela mediana poria terra desconhecida no meio da distribuição,
    que é uma afirmação, não um dado.
    """
    v = np.asarray(valores, dtype="float64")
    saida = np.full(v.shape, np.nan)
    observados = ~np.isnan(v)
    n = int(observados.sum())
    if n == 0:
        return saida
    if n == 1:
        saida[observados] = 0.5   # único ponto: o meio é a única resposta neutra
        return saida
    ordem = v[observados].argsort().argsort()
    saida[observados] = ordem / (n - 1)
    return saida


def combina_culturas(percentis_por_cultura: dict[str, np.ndarray]) -> np.ndarray:
    """Máximo entre culturas — **depois** do percentil, nunca antes.

    ⚠️ Máximo de rendimentos brutos não significa nada: t/ha de banana e t/ha de
    milho não são comparáveis, e o máximo seria decidido pela cultura de maior
    tonelagem, não pela de maior aptidão relativa. Máximo de **percentis** é
    comparável por construção.

    A unidade é apta se for apta para ALGUMA das culturas — daí o máximo, e não
    a média.
    """
    if not percentis_por_cultura:
        raise ValueError("Nenhuma cultura informada.")
    pilha = np.vstack([np.asarray(v, dtype="float64").ravel()
                       for v in percentis_por_cultura.values()])
    for nome, v in percentis_por_cultura.items():
        if np.asarray(v).ravel().shape != pilha[0].shape:
            raise ValueError(f"Cultura {nome!r} tem forma diferente das demais.")
    # nanmax: uma cultura ausente não derruba a unidade se outra tem valor
    with np.errstate(all="ignore"):
        return np.where(np.all(np.isnan(pilha), axis=0), np.nan, np.nanmax(pilha, axis=0))


def normaliza_aptidao(valores: np.ndarray) -> np.ndarray:
    """Reescala para [0, 1] pelo mínimo e máximo observados.

    Segunda reescala da receita: o máximo entre percentis não ocupa
    necessariamente [0, 1] inteiro, e o índice final tem de ocupar, para que
    `dose = 0` e `dose = 1` signifiquem os extremos da amostra.
    """
    v = np.asarray(valores, dtype="float64")
    observados = ~np.isnan(v)
    if not observados.any():
        return v
    lo, hi = np.nanmin(v), np.nanmax(v)
    if hi == lo:
        saida = np.full(v.shape, np.nan)
        saida[observados] = 0.5   # tudo igual: nenhum extremo é defensável
        return saida
    return (v - lo) / (hi - lo)


def aptidao_municipal(
    por_cultura: dict[str, tuple[np.ndarray, np.ndarray]],
) -> pd.DataFrame:
    """A receita inteira, dos rendimentos brutos ao índice em [0, 1].

    `por_cultura` mapeia cultura -> (rendimento alto insumo, rendimento baixo),
    ambos já agregados por município. A ordem das quatro etapas é o que importa:
    diferença → percentil nacional → máximo entre culturas → normalização.
    """
    percentis = {
        nome: percentil_nacional(diferenca_insumo(alto, baixo))
        for nome, (alto, baixo) in por_cultura.items()
    }
    combinado = combina_culturas(percentis)
    indice = normaliza_aptidao(combinado)

    tabela = pd.DataFrame({"aptidao_gaez": indice})
    for nome, p in percentis.items():
        tabela[f"percentil_{nome}"] = p
    return tabela


# --------------------------------------------------------------------------
# E/S — fina, isolada, e falha nomeando o requirements
# --------------------------------------------------------------------------

def _exige_geo():
    """Importa o stack espacial, ou falha dizendo exatamente o que instalar."""
    try:
        import rasterio  # noqa: F401
        import geopandas  # noqa: F401
        from rasterstats import zonal_stats  # noqa: F401
    except ImportError as erro:
        raise RuntimeError(
            f"Stack espacial ausente ({erro}).\n"
            "  Nenhuma fonte geo é legível sem ele — GAEZ, ottobacias da ANA,\n"
            "  polígonos do MapBiomas.\n"
            "  Instale:  pip install -r requirements-geo.txt\n"
            "  ⚠️ Ele é separado do requirements.txt de propósito: GDAL/PROJ/GEOS\n"
            "     são pesados e brigam, e o pipeline 01–05 não precisa deles."
        ) from erro
    import rasterio
    import geopandas as gpd
    from rasterstats import zonal_stats
    return rasterio, gpd, zonal_stats


def le_raster_por_municipio(
    caminho_raster: Path, municipios, campo_id: str = "CD_MUN"
) -> pd.DataFrame:
    """Média zonal do raster dentro de cada polígono municipal.

    ⚠️ **Não verificado contra um raster real do GAEZ** — nenhum foi baixado, e
    `gaez.fao.org` está bloqueado nesta sessão. O que está aqui é a chamada
    padrão de estatística zonal; na primeira rodada conferir CRS (o GAEZ vem em
    WGS84; a malha do IBGE também, mas conferir é barato e o erro é silencioso —
    reprojeção errada dá média sobre a área errada, não erro).
    """
    _, gpd, zonal_stats = _exige_geo()
    malha = municipios if hasattr(municipios, "geometry") else gpd.read_file(municipios)
    estat = zonal_stats(malha, str(caminho_raster), stats=["mean"], all_touched=False)
    return pd.DataFrame(
        {
            "cod_ibge7": malha[campo_id].astype(str).values,
            "valor": [e["mean"] if e and e["mean"] is not None else np.nan for e in estat],
        }
    )


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--culturas", nargs="+", default=None,
                        help="OBRIGATÓRIO. O script não escolhe (flag 2 do CLAUDE.md).")
    parser.add_argument("--raster-alto", type=Path, nargs="+", default=[],
                        help="GeoTIFF de rendimento atingível, ALTO insumo — um por cultura.")
    parser.add_argument("--raster-baixo", type=Path, nargs="+", default=[],
                        help="GeoTIFF de rendimento atingível, BAIXO insumo — um por cultura.")
    parser.add_argument("--municipios", type=Path, default=None,
                        help="Malha municipal do IBGE (.gpkg/.shp), com CD_MUN.")
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    if not args.culturas:
        print("[erro] --culturas é obrigatório. Este script NÃO escolhe as culturas.")
        print()
        print("       ⚠️ A receita do Reynier & Rubin é construída sobre culturas GM")
        print("          (milho, soja, algodão). BANANA NÃO É GM — e é a candidata a")
        print("          cultura-âncora aqui (flag 2 do CLAUDE.md). A transferência é")
        print("          de MÉTODO, não de lista de culturas.")
        print()
        print("       Antes de escolher, confira o catálogo do GAEZ: ele cobre banana")
        print("       e melão? Isso é a 'prioridade zero' registrada na Layer 3.")
        return 1

    n = len(args.culturas)
    if len(args.raster_alto) != n or len(args.raster_baixo) != n:
        print(f"[erro] {n} culturas exigem {n} rasters de alto insumo e {n} de baixo.")
        print(f"       Recebi {len(args.raster_alto)} e {len(args.raster_baixo)}.")
        print("       A receita é a DIFERENÇA entre os cenários — o nível não serve.")
        return 1

    if args.municipios is None:
        print("[erro] --municipios é obrigatório (malha do IBGE, .gpkg/.shp).")
        print("       Sem polígono não há como levar o raster a município.")
        return 1

    try:
        blocos = {}
        for cultura, r_alto, r_baixo in zip(args.culturas, args.raster_alto, args.raster_baixo):
            alto = le_raster_por_municipio(r_alto, args.municipios)
            baixo = le_raster_por_municipio(r_baixo, args.municipios)
            juntos = alto.merge(baixo, on="cod_ibge7", suffixes=("_alto", "_baixo"))
            blocos[cultura] = (juntos["valor_alto"].to_numpy(), juntos["valor_baixo"].to_numpy())
            codigos = juntos["cod_ibge7"]
    except RuntimeError as erro:
        print(f"[erro] {erro}")
        return 2
    except Exception as erro:  # noqa: BLE001
        print(f"[erro] Falha lendo os rasters ({type(erro).__name__}: {erro}).")
        print("       Confira o CRS: GAEZ vem em WGS84 e a malha do IBGE também,")
        print("       mas reprojeção errada dá média sobre a área errada SEM erro.")
        return 1

    tabela = aptidao_municipal(blocos)
    tabela.insert(0, "cod_ibge7", codigos.values)
    tabela["cod_ibge6"] = tabela["cod_ibge7"].str[:6]   # a chave do projeto

    barra = "=" * 84
    print(barra)
    print(f"APTIDÃO FAO-GAEZ | culturas: {', '.join(args.culturas)}")
    print(barra)
    print(f"municípios com índice : {tabela['aptidao_gaez'].notna().sum()} de {len(tabela)}")
    print(f"índice em [0,1]       : {tabela['aptidao_gaez'].min():.3f}"
          f" a {tabela['aptidao_gaez'].max():.3f}")
    print(barra)
    print("Como usar — TRÊS papéis, e dois deles são mecânicos:")
    print("  1. Instrumento da exposição endógena (§5.2).")
    print("  2. ⚠️ Definição 4 de d = 0: baixa aptidão = zero que não depende de")
    print("     registro administrativo estar completo.")
    print("  3. ⚠️ Teste de contaminação do zero: dentro do grupo d = 0, quebrar")
    print("     por aptidão. Se os de ALTA aptidão com área zero se comportam como")
    print("     os de BAIXA, o zero é real. Se divergem, o zero é medida — e a")
    print("     divergência estima a contaminação.")
    print("  ⚠️ 2 e 3 movem o NÍVEL da curva, não a interpretação: o sieve centra")
    print("     tudo em mean(dy[dose==0]). Ver docs/lacunas-de-dados.md.")
    print(barra)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / f"{NOME_SAIDA}.parquet"
    tabela.to_parquet(destino, index=False)
    print(f"[ok] {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
