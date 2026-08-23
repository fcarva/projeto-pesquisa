#!/usr/bin/env python3
"""Tarefa 2 — Limpa microdado de nascimentos (SINASC) e colapsa a município × ano-mês.

Desfechos do Ensaio 1 (ver CLAUDE.md): peso ao nascer, baixo peso (<2500 g) e
prematuridade (<37 semanas), agregados por município de residência × ano-mês.

Notas de interpretação que o código carrega junto (flags de auditoria):

  • Descasamento tratamento/molécula. A Lei 16.820/2019 proíbe o *método aéreo*,
    não princípios ativos. Quem continua pulverizando por trator não é tratado
    pela lei, e glifosato — o químico mais estudado em saúde perinatal — é em
    boa medida terrestre. O efeito detectável tende a se restringir a culturas e
    moléculas de aplicação aérea, e a medida de exposição por área plantada
    (script 01) atenua ainda mais. Esperar efeito pequeno é parte do desenho,
    não sinal de falha.

  • Timing gestacional. O SINASC dá o mês de *nascimento*, não o de exposição.
    Como o desfecho é intrauterino, a exposição relevante ocorre 0–9 meses
    antes, e a janela precisa ser retroprojetada a partir de SEMAGESTAC ao
    montar o painel (scripts/build_panel/). Colapsar por mês, e não por ano,
    existe justamente para deixar essa retroprojeção possível — um painel anual
    já teria jogado fora a informação.

  • Denominadores pequenos. Município × mês em municípios pequenos gera células
    com pouquíssimos nascimentos: taxas de desfecho raro viram ruído. Daí as
    colunas de contagem irem para o parquet — a estimação deve ponderar por
    nascimentos e a inferência usar Conley–Taber / wild bootstrap.

Uso:
    python scripts/data_prep/02_clean_births.py                          # tenta real, cai p/ simulado
    python scripts/data_prep/02_clean_births.py --caminho data/raw/*.parquet
    python scripts/data_prep/02_clean_births.py --fonte simulado --anos 2015 2022

Saída: data/processed/nascimentos_ce_muni_mes.parquet (gitignored). Rodadas
simuladas gravam com sufixo "__simulado" para que dado falso nunca ocupe o
nome canônico que os scripts seguintes vão ler.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# Parâmetros
# --------------------------------------------------------------------------

UF_CEARA = "23"
ANOS_PADRAO = (2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)  # pré e pós-ban (jun/2019)
OUT_DIR = Path("data/processed")
NOME_SAIDA = "nascimentos_ce_muni_mes"
SEED = 20190613

# Colunas do DATASUS/SINASC usadas aqui (nomes reais do dicionário).
COLUNAS_SINASC = (
    "CODMUNRES",   # município de residência, código IBGE de 6 dígitos
    "DTNASC",      # data de nascimento, DDMMAAAA
    "PESO",        # peso ao nascer, em gramas
    "SEMAGESTAC",  # semanas de gestação (numérico; 99 = ignorado)
    "GESTACAO",    # faixa de gestação (categórica) — fallback de SEMAGESTAC
    "IDADEMAE",
    "ESCMAE",
    "CONSULTAS",
)

# Faixas plausíveis. Fora delas é erro de digitação/código de ausência, não
# observação extrema: PESO vem com zeros à esquerda e "0000" para ignorado.
PESO_MIN_G, PESO_MAX_G = 200, 8000
SEMANAS_MIN, SEMANAS_MAX = 20, 45
LIMIAR_BAIXO_PESO_G = 2500
LIMIAR_PREMATURO_SEM = 37

# GESTACAO (SINASC): faixas, usadas quando SEMAGESTAC falta.
#   1 = menos de 22 semanas   2 = 22 a 27   3 = 28 a 31
#   4 = 32 a 36               5 = 37 a 41   6 = 42 e mais   9 = ignorado
# Categorias 1–4 são inteiramente < 37 semanas; 5 e 6, inteiramente >= 37.
# Nenhuma faixa cruza o limiar, então o fallback não introduz erro de
# classificação — só perde precisão sobre *quanto* prematuro.
GESTACAO_PREMATURO = {1: True, 2: True, 3: True, 4: True, 5: False, 6: False, 9: None}

CELULA_PEQUENA = 5  # nascimentos por município-mês abaixo disso: taxa é ruído


# --------------------------------------------------------------------------
# Limpeza — funções pequenas, testáveis uma a uma
# --------------------------------------------------------------------------

def padroniza_colunas(df: pd.DataFrame) -> pd.DataFrame:
    """Nomes em maiúscula e garante que as colunas esperadas existam (NaN se não)."""
    saida = df.copy()
    saida.columns = [str(c).strip().upper() for c in saida.columns]
    faltando = [c for c in COLUNAS_SINASC if c not in saida.columns]
    for col in faltando:
        saida[col] = np.nan
    if faltando:
        print(f"[aviso] colunas ausentes na fonte, preenchidas com NaN: {faltando}")
    return saida[list(COLUNAS_SINASC)]


def extrai_ano_mes(dtnasc: pd.Series) -> pd.DataFrame:
    """DTNASC (DDMMAAAA) -> ano e mês.

    O campo costuma chegar como string; quando passa por leitor que o trata
    como número, o zero à esquerda do dia some e sobram 7 caracteres — daí o
    zfill antes do parse. Data inválida vira NaT, e a linha cai depois.
    """
    texto = dtnasc.astype("string").str.strip().str.replace(r"\.0$", "", regex=True)
    texto = texto.str.zfill(8)
    data = pd.to_datetime(texto, format="%d%m%Y", errors="coerce")
    return pd.DataFrame(
        {
            "ano": data.dt.year.astype("Int64"),
            "mes": data.dt.month.astype("Int64"),
        },
        index=dtnasc.index,
    )


def limpa_peso(peso: pd.Series) -> pd.Series:
    """Peso em gramas dentro da faixa plausível; fora dela, ausente."""
    valores = pd.to_numeric(peso, errors="coerce")
    return valores.where(valores.between(PESO_MIN_G, PESO_MAX_G))


def limpa_semanas(semagestac: pd.Series) -> pd.Series:
    """Semanas de gestação; 99 (ignorado) e valores implausíveis viram ausente."""
    valores = pd.to_numeric(semagestac, errors="coerce")
    return valores.where(valores.between(SEMANAS_MIN, SEMANAS_MAX))


def deriva_baixo_peso(peso_limpo: pd.Series) -> pd.Series:
    """Baixo peso ao nascer. Ausente onde o peso é ausente — nunca imputado."""
    return pd.Series(
        np.where(peso_limpo.isna(), np.nan, (peso_limpo < LIMIAR_BAIXO_PESO_G).astype(float)),
        index=peso_limpo.index,
        dtype="float64",
    )


def deriva_prematuridade(semanas_limpas: pd.Series, gestacao: pd.Series) -> pd.DataFrame:
    """Prematuridade (<37 semanas), com GESTACAO como fallback de SEMAGESTAC.

    Devolve também `prematuro_por_faixa`: 1 quando o valor veio do fallback
    categórico. A cobertura de SEMAGESTAC muda ao longo dos anos, então essa
    proporção precisa entrar como checagem — se ela salta justamente em torno
    de jun/2019, a mudança de mensuração vira ameaça à identificação, não
    detalhe de limpeza.
    """
    por_semanas = pd.Series(
        np.where(semanas_limpas.isna(), np.nan, (semanas_limpas < LIMIAR_PREMATURO_SEM).astype(float)),
        index=semanas_limpas.index,
        dtype="float64",
    )
    faixa = pd.to_numeric(gestacao, errors="coerce").map(GESTACAO_PREMATURO)
    por_faixa = pd.Series(
        [np.nan if v is None or pd.isna(v) else float(v) for v in faixa],
        index=gestacao.index,
        dtype="float64",
    )
    usou_fallback = por_semanas.isna() & por_faixa.notna()
    return pd.DataFrame(
        {
            "prematuro": por_semanas.fillna(por_faixa),
            "prematuro_por_faixa": usou_fallback.astype(float),
        }
    )


def filtra_ceara(df: pd.DataFrame) -> pd.DataFrame:
    """Mantém só residentes no Ceará (CODMUNRES começando em 23)."""
    cod = df["CODMUNRES"].astype("string").str.strip().str.replace(r"\.0$", "", regex=True)
    cod = cod.str.zfill(6)
    saida = df.copy()
    saida["cod_ibge6"] = cod
    return saida[cod.str.startswith(UF_CEARA).fillna(False)].copy()


def prepara_nascimentos(bruto: pd.DataFrame, anos=None) -> pd.DataFrame:
    """Pipeline de limpeza no nível do indivíduo, antes do colapso."""
    df = filtra_ceara(padroniza_colunas(bruto))
    df = pd.concat([df, extrai_ano_mes(df["DTNASC"])], axis=1)
    df["peso_g"] = limpa_peso(df["PESO"])
    df["semanas"] = limpa_semanas(df["SEMAGESTAC"])
    df["baixo_peso"] = deriva_baixo_peso(df["peso_g"])
    df = pd.concat([df, deriva_prematuridade(df["semanas"], df["GESTACAO"])], axis=1)
    df = df[df["ano"].notna() & df["mes"].notna()]
    if anos is not None:
        df = df[df["ano"].isin(list(anos))]
    return df.reset_index(drop=True)


def colapsa_muni_mes(individual: pd.DataFrame) -> pd.DataFrame:
    """Colapsa a CODMUNRES × ano × mês (aqui, `cod_ibge6` × ano × mês).

    Taxas são médias sobre os *não ausentes*: um município-mês com metade dos
    pesos ignorados devolve a taxa da metade observada, e `n_peso_valido` diz
    isso na cara. Imputar aqui esconderia problema de cobertura dentro do
    desfecho.
    """
    agrupado = individual.groupby(["cod_ibge6", "ano", "mes"], dropna=True)
    painel = agrupado.agg(
        n_nascimentos=("cod_ibge6", "size"),
        n_peso_valido=("peso_g", "count"),
        peso_medio=("peso_g", "mean"),
        n_baixo_peso=("baixo_peso", "sum"),
        taxa_baixo_peso=("baixo_peso", "mean"),
        n_gest_valido=("prematuro", "count"),
        n_prematuro=("prematuro", "sum"),
        taxa_prematuridade=("prematuro", "mean"),
        share_gest_por_faixa=("prematuro_por_faixa", "mean"),
        idade_mae_media=("IDADEMAE", "mean"),
    ).reset_index()

    painel["ano"] = painel["ano"].astype(int)
    painel["mes"] = painel["mes"].astype(int)
    painel["celula_pequena"] = painel["n_nascimentos"] < CELULA_PEQUENA
    return painel.sort_values(["cod_ibge6", "ano", "mes"]).reset_index(drop=True)


# --------------------------------------------------------------------------
# Fontes
# --------------------------------------------------------------------------

def carrega_de_arquivos(caminhos: list[Path]) -> pd.DataFrame:
    """Lê arquivos SINASC já baixados (.parquet / .csv / .csv.gz).

    Caminho mais robusto para a fonte real: baixe uma vez do DATASUS e aponte
    para cá. `.dbc` precisa ser convertido antes (pysus/read.dbc) — o formato
    é comprimido proprietário e pandas não lê.
    """
    if not caminhos:
        raise ValueError("Nenhum caminho informado.")
    pedacos = []
    for caminho in caminhos:
        if caminho.suffix == ".parquet":
            pedacos.append(pd.read_parquet(caminho))
        elif caminho.suffix in (".csv", ".gz"):
            pedacos.append(pd.read_csv(caminho, dtype=str, low_memory=False))
        else:
            raise ValueError(f"Extensão não suportada: {caminho} (converta .dbc antes).")
    return pd.concat(pedacos, ignore_index=True)


def carrega_de_pysus(anos=ANOS_PADRAO) -> pd.DataFrame:
    """Baixa SINASC/CE via pysus. A API do pysus mudou entre versões maiores,
    então tentamos a atual e caímos para a antiga."""
    try:  # pysus >= 0.10
        from pysus.ftp.databases.sinasc import SINASC

        base = SINASC().load()
        pedacos = []
        for ano in anos:
            arquivos = base.get_files(uf="CE", year=ano)
            for parquet in base.download(arquivos):
                pedacos.append(parquet.to_dataframe())
        if not pedacos:
            raise RuntimeError("pysus não devolveu arquivos para CE.")
        return pd.concat(pedacos, ignore_index=True)
    except ImportError:
        pass

    from pysus.online_data.SINASC import download  # API antiga

    return pd.concat([download("CE", ano) for ano in anos], ignore_index=True)


def simula_sinasc(anos=ANOS_PADRAO, seed: int = SEED, n_por_muni_mes: int = 18) -> pd.DataFrame:
    """Microdado simulado com as colunas e os tipos reais do SINASC.

    Alvos calibrados no enunciado da tarefa: ~9% de baixo peso e ~11% de
    prematuridade. Duas escolhas de desenho valem nota:

    1. Peso é sorteado *condicional* à prematuridade, não independente dela.
       Um N(3200, 500) puro dá 8,1% abaixo de 2500 g e produz prematuros com
       peso normal — o que quebraria qualquer checagem de consistência entre os
       dois desfechos. Aqui P(baixo peso | prematuro) = 0,50 e
       P(baixo peso | termo) = 0,04, o que recompõe ~9% no agregado.
    2. A simulação injeta de propósito o que a limpeza precisa aguentar:
       SEMAGESTAC ignorado (99) em ~3% dos casos, com GESTACAO disponível para
       o fallback; pesos "0000"; e ~5% de linhas de fora do Ceará.

    Nada disso é evidência sobre o Ceará — é fixture para o código.
    """
    rng = np.random.default_rng(seed)
    municipios = [f"{239000 + i:06d}" for i in range(1, 185)]  # mesma convenção do script 01
    tamanho = rng.lognormal(mean=np.log(n_por_muni_mes), sigma=0.9, size=len(municipios))

    linhas = []
    for cod, escala in zip(municipios, tamanho):
        for ano in anos:
            for mes in range(1, 13):
                n = int(rng.poisson(max(escala, 0.5)))
                if n == 0:
                    continue
                prematuro = rng.random(n) < 0.11
                p_baixo = np.where(prematuro, 0.50, 0.04)
                baixo = rng.random(n) < p_baixo
                peso = np.where(
                    baixo,
                    rng.normal(2050, 320, n).clip(600, LIMIAR_BAIXO_PESO_G - 1),
                    rng.normal(3340, 420, n).clip(LIMIAR_BAIXO_PESO_G, 5200),
                )
                semanas = np.where(
                    prematuro, rng.integers(26, 37, n), rng.integers(37, 43, n)
                ).astype(float)
                dia = rng.integers(1, 29, n)

                # ~3% com SEMAGESTAC ignorado: exercita o fallback por GESTACAO
                sem_semana = rng.random(n) < 0.03
                semagestac = np.where(sem_semana, 99, semanas).astype(int)
                gestacao = np.select(
                    [semanas < 22, semanas < 28, semanas < 32, semanas < 37, semanas < 42],
                    [1, 2, 3, 4, 5],
                    default=6,
                )
                # ~1% com peso ignorado, codificado como no DATASUS
                peso_txt = pd.Series(np.round(peso).astype(int).astype(str)).str.zfill(4)
                peso_txt = peso_txt.mask(pd.Series(rng.random(n) < 0.01), "0000")

                linhas.append(
                    pd.DataFrame(
                        {
                            "CODMUNRES": cod,
                            "DTNASC": [f"{d:02d}{mes:02d}{ano}" for d in dia],
                            "PESO": peso_txt.to_numpy(),
                            "SEMAGESTAC": semagestac,
                            "GESTACAO": gestacao,
                            "IDADEMAE": rng.integers(14, 45, n),
                            "ESCMAE": rng.integers(1, 6, n),
                            "CONSULTAS": rng.integers(1, 5, n),
                        }
                    )
                )

    df = pd.concat(linhas, ignore_index=True)

    # ~5% de residentes fora do Ceará, para que o filtro de UF tenha o que filtrar
    n_fora = int(0.05 * len(df))
    fora = df.sample(n_fora, random_state=seed).copy()
    fora["CODMUNRES"] = rng.choice(["350010", "292740", "150140"], size=n_fora)
    return pd.concat([df, fora], ignore_index=True).sample(frac=1, random_state=seed).reset_index(drop=True)


def carrega_nascimentos(
    fonte: str = "auto", caminhos: list[Path] | None = None, anos=ANOS_PADRAO, seed: int = SEED
) -> tuple[pd.DataFrame, str]:
    """Dispatcher: 'arquivos' | 'pysus' | 'simulado' | 'auto'.

    'auto' = arquivos (se houver) -> pysus -> simulado. Trocar para a fonte real
    é uma linha: `--caminho data/raw/SINASC_CE_*.parquet` ou `--fonte pysus`.
    """
    if fonte == "simulado":
        return simula_sinasc(anos, seed), "simulado"
    if fonte == "arquivos":
        return carrega_de_arquivos(caminhos or []), "arquivos"
    if fonte == "pysus":
        return carrega_de_pysus(anos), "pysus"

    if caminhos:
        try:
            return carrega_de_arquivos(caminhos), "arquivos"
        except Exception as erro:  # noqa: BLE001
            print(f"[aviso] leitura dos arquivos falhou ({type(erro).__name__}: {erro}).")
    try:
        return carrega_de_pysus(anos), "pysus"
    except Exception as erro:  # noqa: BLE001
        print(f"[aviso] acesso via pysus indisponível ({type(erro).__name__}: {erro}).")
        print("[aviso] Caindo para microdado SIMULADO. Nada abaixo é evidência empírica.")
        return simula_sinasc(anos, seed), "simulado"


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

def imprime_resumo(individual: pd.DataFrame, painel: pd.DataFrame, fonte: str) -> None:
    barra = "=" * 84
    print(barra)
    print(f"NASCIMENTOS — CEARÁ, município de residência × ano-mês (SINASC) | fonte: {fonte.upper()}")
    if fonte == "simulado":
        print("!! DADOS SIMULADOS — números inventados, servem só para validar o código. !!")
    print(barra)
    print(f"nascimentos (CE, após limpeza) : {len(individual):,}")
    print(f"municípios                     : {painel['cod_ibge6'].nunique()}")
    print(f"células município-mês          : {len(painel):,}")
    print(f"período                        : {painel['ano'].min()}–{painel['ano'].max()}")
    print("-" * 84)
    peso_medio = np.average(
        painel["peso_medio"].fillna(0), weights=painel["n_peso_valido"].clip(lower=0)
    )
    taxa_bp = painel["n_baixo_peso"].sum() / max(painel["n_peso_valido"].sum(), 1)
    taxa_pre = painel["n_prematuro"].sum() / max(painel["n_gest_valido"].sum(), 1)
    print(f"peso médio ao nascer           : {peso_medio:,.0f} g")
    print(f"taxa de baixo peso (<2500 g)   : {taxa_bp:.2%}")
    print(f"taxa de prematuridade (<37 sem): {taxa_pre:.2%}")
    print("-" * 84)
    falta_peso = 1 - painel["n_peso_valido"].sum() / painel["n_nascimentos"].sum()
    falta_gest = 1 - painel["n_gest_valido"].sum() / painel["n_nascimentos"].sum()
    fallback = np.average(
        painel["share_gest_por_faixa"].fillna(0), weights=painel["n_nascimentos"]
    )
    pequenas = painel["celula_pequena"].mean()
    print(f"peso ausente                   : {falta_peso:.2%}")
    print(f"gestação ausente               : {falta_gest:.2%}")
    print(f"prematuridade vinda de GESTACAO: {fallback:.2%}  (checar salto em torno de jun/2019)")
    print(f"células com <{CELULA_PEQUENA} nascimentos      : {pequenas:.1%}  (taxa é ruído; ponderar por n)")
    print(barra)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--fonte", choices=("auto", "arquivos", "pysus", "simulado"), default="auto"
    )
    parser.add_argument("--caminho", type=Path, nargs="*", default=[],
                        help="Arquivos SINASC já baixados (.parquet/.csv/.csv.gz).")
    parser.add_argument("--anos", type=int, nargs="*", default=list(ANOS_PADRAO))
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    bruto, fonte = carrega_nascimentos(args.fonte, args.caminho, tuple(args.anos), args.seed)
    individual = prepara_nascimentos(bruto, args.anos)
    if individual.empty:
        print("[erro] Nada sobrou após filtrar Ceará e datas válidas. Confira CODMUNRES/DTNASC.")
        return 1

    painel = colapsa_muni_mes(individual)
    painel["fonte"] = fonte  # a proveniência viaja junto com o dado
    imprime_resumo(individual, painel, fonte)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    sufixo = "" if fonte != "simulado" else "__simulado"
    destino = args.out_dir / f"{NOME_SAIDA}{sufixo}.parquet"
    painel.to_parquet(destino, index=False)
    print(f"[ok] painel -> {destino}")
    print("[nota] data/processed/ é gitignored: microdado e derivados não vão para o repositório.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
