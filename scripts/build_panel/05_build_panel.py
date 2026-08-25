#!/usr/bin/env python3
"""E5 — junta dose e desfechos num painel município × ano-mês.

Encontro das duas trilhas do roteiro. Lê o que os scripts 01–04 gravaram e
entrega o painel que `scripts/estimate/03_contdid.R` vai consumir.

────────────────────────────────────────────────────────────────────────────
O PONTO SUBSTANTIVO: **quando o tratamento pega cada coorte**
────────────────────────────────────────────────────────────────────────────
O ban entra em 09/01/2019. A tentação é marcar tratado todo nascimento a partir
dali. Isso está **errado**, e o erro tem direção conhecida.

Um bebê nascido em **março de 2019** foi gestado de junho/2018 a março/2019 —
dois terços da gestação **antes** do ban. Chamá-lo de tratado dilui o efeito com
gestação não exposta. O tratamento não liga de vez em jan/2019: ele **sobe ao
longo de ~9 meses**, e só a coorte de out/2019 em diante teve gestação
inteiramente pós-ban.

Por isso o painel emite `share_gestacao_pos_ban` — a fração da janela
gestacional que caiu depois do ban — e, ao lado, `pos_ban_nascimento`, a versão
ingênua. As duas saem juntas de propósito: a distância entre elas é o tamanho da
atenuação que a marcação ingênua embute.

⚠️ **E a janela gestacional é FIXA, não a observada.** Usar `SEMAGESTAC` de cada
célula para retroprojetar seria endógeno: **prematuridade é um dos desfechos**.
Se o ban encurta a gestação, a janela de exposição encolheria junto com o
tratamento, e o desenho passaria a condicionar numa variável afetada pelo
tratamento — viés de má condicionamento, na direção que ninguém sabe. A janela é
fixa em {JANELA} meses. A gestação observada entra como desfecho, nunca como
definidor de exposição.

**Por trimestre.** Larsen et al. (2017) acham efeito concentrado na cauda de
exposição, e a literatura perinatal costuma separar por trimestre. O painel emite
`share_tri1/2/3_pos_ban` para que a janela crítica seja questão empírica em vez
de suposição. Qual trimestre é o desfecho continua decisão sua.

⚠️ **Intoxicação não retroprojeta.** Intoxicação aguda é contemporânea à
exposição — não há gestação entre causa e efeito. O canal do script 04 usa
`pos_ban_nascimento` (isto é, o mês da internação) direto. Retroprojetar ali
seria inventar defasagem que não existe.

────────────────────────────────────────────────────────────────────────────
O QUE ESTE SCRIPT NÃO FAZ
────────────────────────────────────────────────────────────────────────────
  • **Não escolhe a cultura-âncora.** `--cultura` é obrigatório; sem ele o script
    lista as disponíveis e sai. É a flag 1 do CLAUDE.md, e o script 01 também se
    recusa a escolher.
  • **Não binariza a dose nem corta em faixas.** A dose sai contínua, como o CGS
    pede; a escada de especificação é recomendação do script 01, ratificada por
    você em E3.
  • **Não estima nada.** Grava parquet; o R lê.

Uso:
    python scripts/build_panel/05_build_panel.py --cultura "Melão"
    python scripts/build_panel/05_build_panel.py --cultura "Banana (cacho)" --fonte simulado

Saída: data/processed/painel_ensaio1[__simulado].parquet (gitignored).
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

IN_DIR = OUT_DIR = Path("data/processed")
NOME_SAIDA = "painel_ensaio1"

# Marcos, de `docs/legislacao/README.md`. Três, não um — ver
# docs/ars/06-quimico-e-antecipacao.md §1.
BAN_ANO, BAN_MES = 2019, 1          # vigência: 09/01/2019
NOTICIA_ANO, NOTICIA_MES = 2015, 2  # PL 18/2015 apresentado em 24/02/2015
CERTEZA_ANO, CERTEZA_MES = 2018, 12 # aprovação unânime na ALECE, 18/12/2018
FIM_ANO, FIM_MES = 2024, 12         # Lei 19.135/2024 (drones), 19/12/2024

# Janela gestacional FIXA, em meses. 40 semanas ≈ 9,2 meses; 9 é o arredondamento
# que a literatura perinatal usa. ⚠️ Fixa de propósito — ver a nota no topo.
JANELA_GESTACIONAL_MESES = 9

INICIO_PADRAO = (2015, 1)


def _t(ano, mes) -> int:
    """Índice contínuo de mês. Faz a aritmética de janela virar subtração."""
    return int(ano) * 12 + int(mes) - 1


T_BAN = _t(BAN_ANO, BAN_MES)
T_NOTICIA = _t(NOTICIA_ANO, NOTICIA_MES)
T_CERTEZA = _t(CERTEZA_ANO, CERTEZA_MES)


# --------------------------------------------------------------------------
# Exposição
# --------------------------------------------------------------------------

def share_pos_ban(t_nascimento: pd.Series, inicio: float, fim: float) -> pd.Series:
    """Fração de um intervalo da gestação que caiu depois do ban.

    `inicio` e `fim` são deslocamentos em meses **relativos ao nascimento**, e
    negativos: a gestação inteira é (-9, 0); o primeiro trimestre é (-9, -6).

    A conta é a sobreposição de [t+inicio, t+fim] com [T_BAN, ∞), dividida pela
    largura do intervalo. Sai em [0, 1]: 0 = intervalo inteiro antes do ban,
    1 = inteiro depois, fração = a coorte atravessa o ban no meio.
    """
    largura = fim - inicio
    if largura <= 0:
        raise ValueError(f"Intervalo vazio: ({inicio}, {fim}).")
    a = t_nascimento + inicio
    b = t_nascimento + fim
    sobreposicao = (b - np.maximum(a, T_BAN)).clip(lower=0, upper=largura)
    return sobreposicao / largura


def acrescenta_exposicao(painel: pd.DataFrame) -> pd.DataFrame:
    """Marca cada célula com as construções de exposição, todas lado a lado."""
    df = painel.copy()
    df["t"] = df["ano"] * 12 + df["mes"] - 1

    j = JANELA_GESTACIONAL_MESES
    # gestação inteira
    df["share_gestacao_pos_ban"] = share_pos_ban(df["t"], -j, 0)
    # por trimestre: 1 é o mais distante do parto
    for k in (1, 2, 3):
        inicio = -j + (k - 1) * j / 3
        df[f"share_tri{k}_pos_ban"] = share_pos_ban(df["t"], inicio, inicio + j / 3)

    # A versão INGÊNUA, guardada de propósito: a distância entre ela e
    # `share_gestacao_pos_ban` é a atenuação que marcar por data de nascimento
    # embute. Serve à intoxicação (que é contemporânea) e à comparação.
    df["pos_ban_nascimento"] = (df["t"] >= T_BAN).astype(int)

    # Tempo de evento em meses, para os leads/lags do event study. Os leads
    # precisam alcançar 2018 — ver docs/ars/04-roteiro-qualificacao.md.
    df["evento_meses"] = df["t"] - T_BAN
    df["pos_noticia"] = (df["t"] >= T_NOTICIA).astype(int)
    df["pos_certeza"] = (df["t"] >= T_CERTEZA).astype(int)
    return df


# --------------------------------------------------------------------------
# Dose
# --------------------------------------------------------------------------

def extrai_dose(pam: pd.DataFrame, cultura: str) -> pd.DataFrame:
    """Dose contínua por município, para a cultura escolhida pelo pesquisador."""
    disponiveis = sorted(pam["cultura"].unique())
    if cultura not in disponiveis:
        raise KeyError(
            f"Cultura {cultura!r} não está no PAM carregado.\n"
            f"  Disponíveis: {disponiveis}"
        )
    dose = (
        pam[pam["cultura"] == cultura][["cod_ibge6", "area_ha_media"]]
        .rename(columns={"area_ha_media": "dose_ha"})
        .drop_duplicates(subset="cod_ibge6")
        .reset_index(drop=True)
    )
    dose["cod_ibge6"] = dose["cod_ibge6"].astype(str)
    # Dose relativa, para a curva não depender da unidade. O CGS trabalha bem
    # com dose em [0,1]; a bruta fica ao lado para leitura.
    maximo = dose["dose_ha"].max()
    dose["dose"] = dose["dose_ha"] / maximo if maximo > 0 else 0.0
    dose["dose_zero"] = dose["dose_ha"] <= 0
    return dose


# --------------------------------------------------------------------------
# Montagem
# --------------------------------------------------------------------------

def grade_completa(municipios, inicio: tuple[int, int], fim: tuple[int, int]) -> pd.DataFrame:
    """Grade balanceada município × mês.

    Balanceada de propósito: um município-mês sem nascimento registrado é
    informação (zero), não ausência, e uma grade furada faria o estimador
    trabalhar com painel desbalanceado sem ninguém ter decidido isso.
    """
    meses = pd.period_range(
        start=f"{inicio[0]}-{inicio[1]:02d}", end=f"{fim[0]}-{fim[1]:02d}", freq="M"
    )
    grade = pd.MultiIndex.from_product(
        [sorted(set(municipios)), meses], names=["cod_ibge6", "periodo"]
    ).to_frame(index=False)
    grade["ano"] = grade["periodo"].dt.year
    grade["mes"] = grade["periodo"].dt.month
    return grade.drop(columns="periodo")


def junta_desfechos(grade: pd.DataFrame, fontes: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Left-join de cada painel de desfecho sobre a grade balanceada."""
    chave = ["cod_ibge6", "ano", "mes"]
    painel = grade.copy()
    for nome, df in fontes.items():
        if df is None:
            print(f"[aviso] {nome} ausente — painel sai sem essas colunas.")
            continue
        bloco = df.copy()
        bloco["cod_ibge6"] = bloco["cod_ibge6"].astype(str)
        bloco = bloco.drop(columns=[c for c in ("fonte",) if c in bloco.columns])
        # sufixo evita colisão silenciosa: 02 e 03 têm n_peso_valido, por exemplo
        colisoes = set(bloco.columns) & set(painel.columns) - set(chave)
        if colisoes:
            bloco = bloco.rename(columns={c: f"{c}_{nome}" for c in colisoes})
        painel = painel.merge(bloco, on=chave, how="left")
    return painel


def monta_painel(
    pam: pd.DataFrame,
    cultura: str,
    nascimentos: pd.DataFrame | None,
    fetais: pd.DataFrame | None = None,
    intoxicacao: pd.DataFrame | None = None,
    inicio: tuple[int, int] = INICIO_PADRAO,
    fim: tuple[int, int] | None = None,
) -> pd.DataFrame:
    """Painel município × ano-mês com dose, exposição e desfechos."""
    dose = extrai_dose(pam, cultura)

    if fim is None:
        anos = [d["ano"].max() for d in (nascimentos, fetais, intoxicacao) if d is not None]
        ano_fim = min(max(anos), FIM_ANO) if anos else FIM_ANO
        fim = (int(ano_fim), 12)

    grade = grade_completa(dose["cod_ibge6"], inicio, fim)
    painel = junta_desfechos(
        grade,
        {"nasc": nascimentos, "fetal": fetais, "intox": intoxicacao},
    )
    painel = painel.merge(dose, on="cod_ibge6", how="left")
    painel = acrescenta_exposicao(painel)
    painel["cultura_ancora"] = cultura
    return painel.sort_values(["cod_ibge6", "ano", "mes"]).reset_index(drop=True)


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

def imprime_resumo(painel: pd.DataFrame, cultura: str, fonte: str) -> None:
    barra = "=" * 88
    print(barra)
    print(f"E5 — PAINEL DO ENSAIO 1 | cultura-âncora: {cultura} | fonte: {fonte.upper()}")
    if fonte == "simulado":
        print("!! DADOS SIMULADOS em ao menos uma fonte. Não é evidência sobre o Ceará.")
    print(barra)
    print(f"municípios          : {painel['cod_ibge6'].nunique()}")
    print(f"meses               : {painel[['ano','mes']].drop_duplicates().shape[0]}")
    print(f"células (balanceado): {len(painel):,}")
    print(f"período             : {painel['ano'].min()}-{painel['ano'].max()}")
    print("-" * 88)

    positivos = int((~painel.drop_duplicates('cod_ibge6')["dose_zero"]).sum())
    zeros = int(painel.drop_duplicates('cod_ibge6')["dose_zero"].sum())
    print(f"dose > 0 em {positivos} municípios; dose = 0 em {zeros}")
    print("⚠️ 'dose = 0' é zero de PROXY (área nula da cultura), não zero de")
    print("   tratamento. Quatro construções de zero em 03-modelagem-ensaio1.md §5.3.")
    print("-" * 88)

    print("EXPOSIÇÃO — o tratamento sobe ao longo da gestação, não liga de vez")
    print(f"(janela FIXA de {JANELA_GESTACIONAL_MESES} meses; a observada seria endógena)")
    amostra = (
        painel[["ano", "mes", "share_gestacao_pos_ban", "pos_ban_nascimento"]]
        .drop_duplicates(subset=["ano", "mes"])
        .query("ano == 2018 or ano == 2019")
        .sort_values(["ano", "mes"])
    )
    print(f"  {'coorte':<10}{'gestação pós-ban':>18}{'ingênuo':>10}   diferença")
    for _, r in amostra.iterrows():
        s, p = r["share_gestacao_pos_ban"], r["pos_ban_nascimento"]
        marca = "  <-- ingênuo diz tratado, gestação diz o contrário" if p == 1 and s < 0.5 else ""
        print(f"  {int(r['ano'])}-{int(r['mes']):02d}{s:>18.2f}{p:>10.0f}{marca}")
    print(barra)
    print("Como usar:")
    print("  • `share_gestacao_pos_ban` é a exposição do desfecho perinatal.")
    print("    `pos_ban_nascimento` fica ao lado para você medir a atenuação que")
    print("    a marcação ingênua embutiria — não para ser o tratamento.")
    print("  • `share_tri1/2/3_pos_ban`: qual trimestre importa é empírico, não")
    print("    suposição. A escolha do desfecho é sua.")
    print("  • ⚠️ Intoxicação (script 04) é CONTEMPORÂNEA: use `pos_ban_nascimento`,")
    print("    que ali é o mês da internação. Retroprojetar inventaria defasagem.")
    print("  • Os leads do event study precisam alcançar 2018: `evento_meses` e")
    print("    `pos_certeza` (18/12/2018) estão no painel para isso.")
    print(barra)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _le(caminho: Path):
    return pd.read_parquet(caminho) if caminho.exists() else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--cultura", default=None,
                        help="Cultura-âncora. OBRIGATÓRIO — o script não escolhe (flag 1).")
    parser.add_argument("--fonte", choices=("auto", "simulado", "real"), default="auto")
    parser.add_argument("--in-dir", type=Path, default=IN_DIR)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    sufixo = "__simulado" if args.fonte == "simulado" else ""
    pam_caminho = args.in_dir / f"pam_ce_muni_cultura_media{sufixo}.parquet"
    if args.fonte == "auto" and not pam_caminho.exists():
        pam_caminho = args.in_dir / "pam_ce_muni_cultura_media__simulado.parquet"
        sufixo = "__simulado"
    pam = _le(pam_caminho)
    if pam is None:
        print(f"[erro] PAM não encontrado em {pam_caminho}.")
        print("       Rode antes: python scripts/data_prep/01_check_dose_variation.py")
        return 1

    if not args.cultura:
        print("[erro] --cultura é obrigatório. Este script NÃO escolhe a cultura-âncora:")
        print("       é a flag 1 do CLAUDE.md, e a decisão é do pesquisador.")
        print("       Rode o script 01 para ver a dispersão de dose de cada uma.")
        print(f"\n       Disponíveis no PAM carregado:\n         "
              + "\n         ".join(sorted(pam["cultura"].unique())))
        return 1

    fontes = {
        "nascimentos": _le(args.in_dir / f"nascimentos_ce_muni_mes{sufixo}.parquet"),
        "fetais": _le(args.in_dir / f"obitos_fetais_ce_muni_mes{sufixo}.parquet"),
        "intoxicacao": _le(args.in_dir / f"intoxicacao_ce_muni_mes{sufixo}.parquet"),
    }
    if fontes["nascimentos"] is None:
        print("[erro] Painel de nascimentos ausente — é o desfecho principal.")
        print("       Rode antes: python scripts/data_prep/02_clean_births.py")
        return 1

    try:
        painel = monta_painel(pam, args.cultura, **fontes)
    except KeyError as erro:
        print(f"[erro] {erro}")
        return 1

    fonte_rotulo = "simulado" if sufixo else "real"
    painel["fonte"] = fonte_rotulo
    imprime_resumo(painel, args.cultura, fonte_rotulo)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / f"{NOME_SAIDA}{sufixo}.parquet"
    painel.to_parquet(destino, index=False)
    print(f"[ok] painel -> {destino}")
    print("[nota] data/processed/ é gitignored. Próximo: scripts/estimate/03_contdid.R")
    return 0


if __name__ == "__main__":
    sys.exit(main())
