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


CAMINHO_BANS = Path("docs/legislacao/bans-municipais-ce.csv")
NOME_POPULACAO = "populacao_ce_muni_ano"
NOME_GAEZ = "gaez_aptidao_muni"


def carrega_gaez(in_dir: Path) -> pd.DataFrame:
    """Aptidão agroclimática FAO-GAEZ, do script 06. Invariante no tempo.

    ⚠️ **Três papéis, e dois são mecânicos** — não interpretativos. O sieve do
    `contdid` faz `m0 <- mean(dy[dose == 0])`: a curva inteira é centrada no
    grupo de dose zero. Então quem está no zero **desloca o nível do
    resultado**, e o GAEZ é o que permite construir e testar esse grupo:

    1. instrumento da exposição endógena (§5.2 da modelagem);
    2. **definição 4 de `d = 0`** — baixa aptidão é zero que não depende de
       registro administrativo estar completo;
    3. **teste de contaminação do zero** — dentro do `d = 0`, quebrar por
       aptidão: se os de alta aptidão com área zero se comportam como os de
       baixa, o zero é real; se divergem, o zero é medida, e a divergência
       estima a contaminação.

    Sem isto o nível da curva fica **sem banda**, que é o que a matriz de
    degradação da `lacunas-de-dados.md` §2 chama de "indefensável".
    """
    for sufixo in ("", "__irrigada", "__sequeiro"):
        caminho = in_dir / f"{NOME_GAEZ}{sufixo}.parquet"
        if caminho.exists():
            g = pd.read_parquet(caminho)
            g["cod_ibge6"] = g["cod_ibge6"].astype(str)
            colunas = ["cod_ibge6"] + [c for c in g.columns
                                       if c.startswith(("aptidao", "percentil"))]
            return g[colunas].drop_duplicates("cod_ibge6")
    return pd.DataFrame(columns=["cod_ibge6", "aptidao_gaez"])


def carrega_populacao(in_dir: Path, fonte: str = "auto") -> pd.DataFrame:
    """Denominador do canal de intoxicação, do script 11.

    ⚠️ Anual, não mensal — repetir população mês a mês inventaria variação que
    não existe. A junção é por (`cod_ibge6`, `ano`).

    ⚠️ **Traz a coluna `origem` junto, e não é enfeite.** Até 2021 o número é
    estimativa intercensitária; em 2022 é contagem do Censo. No Ceará isso é
    uma queda de 9.240.580 para 8.794.957 — **4,8% no estado inteiro**, de um
    ano para o outro, sem que nada tenha acontecido no mundo. Uma taxa que
    cruze esse corte sem marcar a origem atribui à política o que é mudança de
    metodologia.
    """
    for sufixo in (["__sidra", ""] if fonte != "simulado" else ["__simulado"]):
        caminho = in_dir / f"{NOME_POPULACAO}{sufixo}.parquet"
        if caminho.exists():
            pop = pd.read_parquet(caminho)
            pop["cod_ibge6"] = pop["cod_ibge6"].astype(str)
            colunas = ["cod_ibge6", "ano", "populacao"]
            if "origem" in pop.columns:
                colunas.append("origem")
            saida = pop[colunas].rename(columns={"origem": "populacao_origem"})
            return saida
    return pd.DataFrame(columns=["cod_ibge6", "ano", "populacao", "populacao_origem"])


def carrega_bans_municipais(caminho: Path = CAMINHO_BANS) -> pd.DataFrame:
    """Bans municipais anteriores a 2019, do levantamento legislativo.

    Flag 0 do `CLAUDE.md`: Limoeiro do Norte proibiu a pulverização aérea pela
    Lei 1.478 de 20/11/2009, e está no decil superior da banana. ⚠️ **E a lei
    foi revogada pela Lei 1.511, de 26/05/2010** (política ambiental; a
    revogação está no corpo, não na ementa). Por isso a TERCEIRA coluna: sem a data de
    revogação, "ban em 2009" lia-se como "tratado desde 2009", e no pré-período
    de 2015–2018 Limoeiro pulverizava como qualquer vizinho.

    ⚠️ **Devolve a data E a confiança, e a confiança não é decorativa.** Se o painel
    levasse só a data, `inconclusivo` (ninguém conseguiu conferir) e
    `ausente_conferido` (conferido, não há lei) virariam ambos `NaT` — e a
    distinção que o CSV inteiro existe para preservar morreria na fronteira
    entre os dois arquivos. Um município não conferido entraria na estimação
    como se fosse comprovadamente não tratado antes de 2019. É a mesma classe
    de falha silenciosa que a varredura foi feita para evitar.

    Fonte gitignored? Não: `docs/legislacao/`, de propósito. `data/` não chega
    às sessões remotas.
    """
    if not caminho.exists():
        return pd.DataFrame(columns=["cod_ibge6", "ban_municipal_data",
                                     "ban_municipal_revogado_em",
                                     "ban_municipal_confianca"])
    bruto = pd.read_csv(caminho, dtype=str, comment="#").fillna("")
    # CSV anterior a 2026-09-22 não tem a coluna: vira NaT, não erro.
    revogacao = bruto.get("data_revogacao", pd.Series("", index=bruto.index))
    saida = pd.DataFrame({
        "cod_ibge6": bruto["cod_ibge6"].astype(str),
        "ban_municipal_data": pd.to_datetime(bruto["data_lei"], errors="coerce"),
        "ban_municipal_revogado_em": pd.to_datetime(revogacao, errors="coerce"),
        "ban_municipal_confianca": bruto["confianca"],
    })
    return saida


def ban_vigente_em(bans: pd.DataFrame, data: str | pd.Timestamp) -> pd.Series:
    """Quem estava sob ban municipal VIGENTE na data — não quem teve lei um dia.

    ⚠️ É a pergunta que importa para o pré-período: Limoeiro teve lei em 2009 e
    não tinha ban em 2015. Recebe o que `carrega_bans_municipais` devolve (ou o
    painel) e tolera a ausência da coluna de revogação.
    """
    data = pd.Timestamp(data)
    inicio = pd.to_datetime(bans["ban_municipal_data"], errors="coerce")
    fim = pd.to_datetime(bans.get("ban_municipal_revogado_em",
                                  pd.Series(pd.NaT, index=bans.index)),
                         errors="coerce")
    return (inicio <= data) & (fim.isna() | (fim > data))


def monta_painel(
    pam: pd.DataFrame,
    cultura: str,
    nascimentos: pd.DataFrame | None,
    fetais: pd.DataFrame | None = None,
    intoxicacao: pd.DataFrame | None = None,
    inicio: tuple[int, int] = INICIO_PADRAO,
    fim: tuple[int, int] | None = None,
    bans: pd.DataFrame | None = None,
    populacao: pd.DataFrame | None = None,
    sinan: pd.DataFrame | None = None,
    gaez: pd.DataFrame | None = None,
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
    # ⚠️ SINAN entra com PREFIXO, e não é preciosismo de nome. Ele e o SIH
    # medem coisas diferentes — notificação compulsória contra internação
    # faturada — e as contagens diferem por duas ordens de grandeza (266
    # agrícolas em 1 ano contra 1 acidental em 8). Deixar `n_agricola` nu ao
    # lado de `n_acidental` convidaria a somar ou comparar os dois como se
    # fossem a mesma série. Ver gates-resultados-dados-reais.md §7-bis.
    if sinan is not None and not sinan.empty:
        bloco = sinan.copy()
        bloco["cod_ibge6"] = bloco["cod_ibge6"].astype(str)
        bloco = bloco.drop(columns=[c for c in ("fonte",) if c in bloco.columns])
        chave = ["cod_ibge6", "ano", "mes"]
        bloco = bloco.rename(columns={c: f"sinan_{c}" for c in bloco.columns
                                      if c not in chave})
        painel = painel.merge(bloco, on=chave, how="left")

        # ⚠️ ZERO SÓ DENTRO DA COBERTURA. Município-mês sem notificação dentro
        # de um ano baixado é zero legítimo; ano que nunca foi baixado é
        # AUSÊNCIA, e preencher com zero inventaria "nenhuma intoxicação em
        # 2016–2022" a partir de um download incompleto. O painel diria que o
        # canal A5 desapareceu depois do ban — achado espúrio pronto, saído de
        # `fillna(0)`.
        anos_cobertos = set(bloco["ano"].unique())
        dentro = painel["ano"].isin(anos_cobertos)
        painel["sinan_ano_coberto"] = dentro
        for coluna in [c for c in painel.columns if c.startswith("sinan_n_")]:
            painel[coluna] = painel[coluna].where(~dentro,
                                                  painel[coluna].fillna(0))
            painel.loc[~dentro, coluna] = np.nan

    painel = painel.merge(dose, on="cod_ibge6", how="left")
    painel = acrescenta_exposicao(painel)
    painel["cultura_ancora"] = cultura

    # ⚠️ INSTRUMENTA, não decide. O script marca quem já estava banido antes de
    # 2019; QUAL especificação primária faz com esses municípios — excluir,
    # sensibilidade, grupo próprio — é decisão de E3/L3 e vai para a
    # pré-especificação, não para cá. O CLAUDE.md proíbe o script escolher.
    if populacao is not None and not populacao.empty:
        painel = painel.merge(populacao, on=["cod_ibge6", "ano"], how="left")
        # Taxas por 100 mil — a unidade em que o canal A5 é comparável entre
        # municípios de porte diferente. ⚠️ Contagem não é; ver o script 07.
        # ⚠️ Nomes conferidos contra o painel montado, não supostos: o SIH
        # grava `n_acidental`/`n_t60_qualquer` e o SINAN entra prefixado. Uma
        # versão anterior procurava `n_intoxicacao`, que não existe — e o
        # resultado não era erro, era ausência silenciosa da taxa.
        for coluna, nome in (("n_acidental", "taxa_sih_acidental_100k"),
                             ("n_t60_qualquer", "taxa_sih_t60_100k"),
                             ("sinan_n_agricola", "taxa_sinan_agricola_100k"),
                             ("sinan_n_agricola_nao_intencional",
                              "taxa_sinan_agricola_nao_intencional_100k")):
            if coluna in painel.columns:
                painel[nome] = np.where(
                    painel["populacao"].to_numpy(dtype=float) > 0,
                    painel[coluna].to_numpy(dtype=float)
                    / painel["populacao"].to_numpy(dtype=float) * 100_000,
                    np.nan)
    else:
        painel["populacao"] = np.nan
        painel["populacao_origem"] = ""

    if gaez is not None and not gaez.empty:
        painel = painel.merge(gaez, on="cod_ibge6", how="left")
    else:
        painel["aptidao_gaez"] = np.nan

    if bans is None:
        bans = carrega_bans_municipais()
    if not bans.empty:
        painel = painel.merge(bans, on="cod_ibge6", how="left")
    else:
        painel["ban_municipal_data"] = pd.NaT
        painel["ban_municipal_confianca"] = "nao_verificado"
    if "ban_municipal_revogado_em" not in painel.columns:
        painel["ban_municipal_revogado_em"] = pd.NaT
    painel["ban_municipal_confianca"] = (
        painel["ban_municipal_confianca"].fillna("nao_verificado"))

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

    if "aptidao_gaez" in painel.columns:
        por_muni = painel.drop_duplicates("cod_ibge6")
        cob = por_muni["aptidao_gaez"].notna().mean()
        print()
        print(f"  APTIDÃO FAO-GAEZ: cobertura {cob:.1%} dos municípios")
        if cob > 0:
            zero = por_muni[por_muni["dose"] == 0]
            if len(zero):
                print(f"    no grupo d = 0 ({len(zero)} municípios): aptidão mediana "
                      f"{zero['aptidao_gaez'].median():.3f}")
                print("    ⚠️ Quebrar o d = 0 por aptidão é o teste de contaminação")
                print("       da §5.3 — e ele move o NÍVEL da curva, não a leitura.")
        else:
            print("    ⚠️ SEM GAEZ o nível da curva fica sem banda. Rode:")
            print("       python scripts/data_prep/06_build_gaez.py --culturas ...")

    if "sinan_ano_coberto" in painel.columns:
        anos_ok = sorted(int(a) for a in
                         painel[painel["sinan_ano_coberto"]]["ano"].unique())
        todos = sorted(int(a) for a in painel["ano"].unique())
        faltam = [a for a in todos if a not in anos_ok]
        print()
        print(f"  SINAN/IEXO (canal A5): anos baixados {anos_ok}")
        if faltam:
            print(f"    ⚠️ SEM DADO em {faltam} — as colunas sinan_* ficam NaN,")
            print("       não zero. Zero ali diria que o canal sumiu após o ban.")
            print("       Rode: python scripts/data_prep/10_clean_sinan_iexo.py "
                  "--fonte pysus")

    if "populacao" in painel.columns:
        cob = painel["populacao"].notna().mean()
        print()
        print(f"  DENOMINADOR POPULACIONAL: cobertura {cob:.1%}")
        if cob < 1.0:
            faltando = sorted(painel[painel["populacao"].isna()]["ano"].unique())
            print(f"    ⚠️ anos sem população: {faltando} — a taxa some nesses anos")
        origens = painel.get("populacao_origem")
        if origens is not None and origens.notna().any():
            por_ano = (painel.dropna(subset=["populacao"])
                       .groupby("ano")["populacao_origem"].first())
            censo = [a for a, o in por_ano.items() if o == "censo"]
            if censo:
                print(f"    ⚠️ anos de CENSO (não estimativa): {censo}")
                print("       A quebra metodológica é de ~4,8% no estado. Taxa que")
                print("       cruze esse corte mostra salto que não é do mundo.")

    if "ban_municipal_confianca" in painel.columns:
        por_muni = painel.drop_duplicates("cod_ibge6")
        contagem = por_muni["ban_municipal_confianca"].value_counts()
        banidos = por_muni[por_muni["ban_municipal_data"].notna()]
        print()
        print("  ⚠️ BANS MUNICIPAIS ANTERIORES A 2019 (flag 0):")
        print(f"    confirmados (lei achada no acervo): {len(banidos):3d}")
        for _, linha in banidos.iterrows():
            revogado = linha.get("ban_municipal_revogado_em", pd.NaT)
            fim = (f", REVOGADO em {revogado.date()}" if pd.notna(revogado)
                   else " (sem revogação registrada — conferir)")
            print(f"      {linha['cod_ibge6']}  desde "
                  f"{linha['ban_municipal_data'].date()}{fim}")
        vigentes = int(ban_vigente_em(por_muni, "2015-01-01").sum())
        print(f"    vigentes no início do pré-período (2015-01-01): {vigentes:3d}"
              "  ← é este número que contamina o pré-período")
        for chave in ("ausente_conferido", "inconclusivo", "nao_verificado"):
            print(f"    {chave:<20} {int(contagem.get(chave, 0)):3d}")
        print("    ⚠️ 'inconclusivo' e 'nao_verificado' NÃO são 'não tratado'. Para")
        print("       eles não se sabe, e a §8 da pré-especificação recebe isso")
        print("       como ameaça declarada — não como zero.")
    print(barra)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

# ⚠️ O PAM não segue a convenção de nome dos painéis de desfecho, e a diferença
# já quebrou o encontro das trilhas (E5). Os scripts 02/03/04 gravam **nome nu**
# quando a fonte é real e `__simulado` quando não é; o script 01 grava SEMPRE o
# nome da fonte — `__sidra`, `__arquivo` ou `__simulado` —, de propósito, para
# que um diagnóstico simulado nunca ocupe o nome canônico.
#
# Procurar só por "" e "__simulado", como este script fazia, não acha o PAM real
# e faz a mensagem de erro mandar rodar o script 01 que **já rodou**.
SUFIXOS_PAM_REAIS = ("__sidra", "__arquivo", "")
SUFIXO_SIMULADO = "__simulado"
NOME_PAM = "pam_ce_muni_cultura_media"


def resolve_pam(in_dir: Path, fonte: str = "auto") -> tuple[Path | None, str]:
    """Acha o PAM na pasta e devolve (caminho, sufixo). (None, "") se não houver.

    'real' nunca cai no simulado, e 'simulado' nunca sobe para o real: misturar
    as duas fontes num painel é o tipo de erro que não se vê no resultado.
    """
    if fonte == "simulado":
        candidatos = (SUFIXO_SIMULADO,)
    elif fonte == "real":
        candidatos = SUFIXOS_PAM_REAIS
    else:
        candidatos = SUFIXOS_PAM_REAIS + (SUFIXO_SIMULADO,)
    for suf in candidatos:
        caminho = in_dir / f"{NOME_PAM}{suf}.parquet"
        if caminho.exists():
            return caminho, suf
    return None, ""


def _le(caminho: Path):
    return pd.read_parquet(caminho) if caminho.exists() else None


def _saida_utf8() -> None:
    """Força UTF-8 na saída antes de qualquer print.

    No Windows o console — e, sobretudo, o *pipe* que captura a saída — usa a
    codepage da locale (cp1252 em pt-BR), que não encoda ─ ⚠ ✔ ✘ → ≥. Sem isto o
    script morre de UnicodeEncodeError DEPOIS de ter feito o trabalho: a rodada
    inteira se perde na impressão do resultado. Foi o que aconteceu — a API do
    IBGE respondeu e o preflight morreu ao imprimir o que tinha encontrado.

    Os acentos do português passam em cp1252; o que quebra é a decoração.
    Reproduzível em qualquer plataforma com PYTHONIOENCODING=cp1252, e é assim
    que o teste de regressão o prende.
    """
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--cultura", default=None,
                        help="Cultura-âncora. OBRIGATÓRIO — o script não escolhe (flag 1).")
    parser.add_argument("--fonte", choices=("auto", "simulado", "real"), default="auto")
    parser.add_argument("--in-dir", type=Path, default=IN_DIR)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    pam_caminho, pam_sufixo = resolve_pam(args.in_dir, args.fonte)
    # Os painéis de desfecho seguem a OUTRA convenção: nome nu quando reais.
    sufixo = SUFIXO_SIMULADO if pam_sufixo == SUFIXO_SIMULADO else ""

    pam = _le(pam_caminho) if pam_caminho else None
    if pam is None:
        procurados = ", ".join(
            f"{NOME_PAM}{s}.parquet" for s in (SUFIXOS_PAM_REAIS + (SUFIXO_SIMULADO,))
        )
        print(f"[erro] PAM não encontrado em {args.in_dir}. Procurados: {procurados}")
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
    sinan = _le(args.in_dir / f"sinan_iexo_ce_muni_mes{sufixo}.parquet")
    if fontes["nascimentos"] is None:
        print("[erro] Painel de nascimentos ausente — é o desfecho principal.")
        print("       Rode antes: python scripts/data_prep/02_clean_births.py")
        return 1

    try:
        painel = monta_painel(
            pam, args.cultura, **fontes,
            populacao=carrega_populacao(args.in_dir, args.fonte),
            sinan=sinan, gaez=carrega_gaez(args.in_dir))
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
