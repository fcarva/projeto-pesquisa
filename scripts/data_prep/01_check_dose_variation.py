#!/usr/bin/env python3
"""Tarefa 1 — Existe variação de dose utilizável entre municípios do Ceará?

Diagnóstico, não decisão. O desenho do Ensaio 1 é DiD de tratamento contínuo
(Callaway, Goodman-Bacon & Sant'Anna 2024): o ban da pulverização aérea é
estadual e simultâneo (jun/2019), então a identificação vem da variação de
*dose* entre municípios, não de variação de *timing*. Se não houver dispersão
entre municípios na intensidade agrícola pré-ban, o desenho inteiro cai — por
isso esta checagem vem antes de qualquer outra coisa.

O que este script NÃO faz (ver CLAUDE.md, "Flags de auditoria"):

  1. Não escolhe a cultura-âncora. A saída é uma tabela ordenada por dispersão
     com sinalização de massa; a escolha é do pesquisador. Em particular, não
     assume "algodão" (área possivelmente fina no pós-bicudo) nem "fruticultura"
     (Chapada do Apodi) antes de olhar o dado.
  2. Não resolve o descasamento tratamento/molécula. Área plantada em PAM é
     proxy de *intensidade agrícola*, não de pulverização aérea efetiva: a lei
     proíbe o método aéreo, não moléculas, e culturas diferem em quanto de fato
     recebem aplicação aérea. Qualquer dose construída daqui herda esse viés de
     medida — em geral atenuante, e vale dizer isso na seção de identificação.
  3. Não trata a área plantada como exógena. O passo seguinte é instrumentar a
     exposição com aptidão agroclimática FAO-GAEZ (Reynier & Rubin 2025;
     Dias, Rocha & Soares 2023).

Uso:
    python scripts/data_prep/01_check_dose_variation.py                 # tenta SIDRA, cai p/ simulado
    python scripts/data_prep/01_check_dose_variation.py --fonte sidra   # exige SIDRA (falha alto)
    python scripts/data_prep/01_check_dose_variation.py --fonte simulado

Saídas em data/processed/ (nunca commitadas — ver .gitignore). O nome do
arquivo carrega a fonte ("sidra" ou "simulado") justamente para que um
diagnóstico simulado nunca seja lido como se fosse real.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# Parâmetros
# --------------------------------------------------------------------------

ANOS_PRE_BAN = (2015, 2016, 2017, 2018)  # janela pré-ban (lei entra em jun/2019)
UF_CEARA = "23"
OUT_DIR = Path("data/processed")
SEED = 20190613  # data de sanção da Lei 16.820/2019; seed fixa, ver CLAUDE.md

# --- SIDRA / PAM ----------------------------------------------------------
# Tabelas da Produção Agrícola Municipal:
#   1612 = lavouras temporárias (algodão, melão, melancia, milho, feijão, ...)
#   1613 = lavouras permanentes (banana, mamão, castanha de caju, uva, ...)
# Variável: usamos área *plantada* (temporárias) / *destinada à colheita*
# (permanentes), e não área colhida, de propósito: 2012–2017 foi seca severa no
# semiárido cearense e a área colhida responde à quebra de safra — ou seja, é
# endógena ao clima, que é exatamente o canal que o instrumento GAEZ tenta
# isolar depois. Área plantada mede intenção de plantio.
# Se o SIDRA devolver erro ou vazio, confira os códigos em
# https://sidra.ibge.gov.br/tabela/1612 e /1613 — a API muda de tempos em tempos.
SIDRA_TABELAS = (
    {"tabela": "1612", "variavel": "109", "classificacao": "81", "grupo": "temporária"},
    {"tabela": "1613", "variavel": "2313", "classificacao": "82", "grupo": "permanente"},
)
# "in n3 23" = todos os municípios (n6) dentro da UF 23. Se a sua versão do
# sidrapy não repassar essa sintaxe, troque por uma lista explícita de códigos.
SIDRA_TERRITORIO = "in n3 23"

# Culturas candidatas a dose — HIPÓTESES, não escolhas. Alta pulverização
# e/ou peso no agronegócio cearense; os comparadores de baixa pulverização
# ficam junto de propósito, para dar contraste na tabela.
CULTURAS_CANDIDATAS = (
    "algodão herbáceo",   # flag 1 do CLAUDE.md: área pode ser fina no pós-bicudo
    "melão",              # Chapada do Apodi / baixo Jaguaribe, irrigado
    "melancia",
    "abacaxi",
    "banana",
    "mamão",
    "manga",
    "goiaba",
    "uva",
    "tomate",
    "cana-de-açúcar",
    "castanha de caju",   # peso no CE, mas sequeiro/extensivo
    "coco-da-baía",
    "milho",              # comparadores de baixa pulverização aérea
    "feijão",
    "arroz",
    "sorgo",
    "mandioca",
)

# --- Escada de especificação ------------------------------------------------
# Estes cortes NÃO são preferência estética: saem do que cada estimador precisa.
# A curva não-paramétrica de CGS usa um sieve (Chen, Christensen & Kankanala) e
# exige suporte espalhado — valores de dose distintos, não municípios empilhados
# no mesmo ponto. Quando o suporte encolhe, o próprio CGS aponta o degrau
# seguinte: dose discreta com indicadores múltiplos ("when the treatment is
# discrete, this is as simple as running a linear regression with multiple
# treatment indicators"). O último degrau é binarizar sob Assumption 4-Agg,
# abandonando a curva.
#
# Quem ratifica os cortes é o pesquisador — estão aqui em cima exatamente para
# isso, e a versão anterior deste arquivo usava limiares que eram palpite meu
# travestido de critério (ver docs/ars/02-research-plan-summary.md, nota de poder).
MIN_MUNI_CURVA = 40            # abaixo disso o sieve não-paramétrico não se defende
MIN_MUNI_FAIXAS = 15           # abaixo disso nem faixas discretas — só binário
MIN_DOSE_DISTINTAS_CURVA = 20  # empate em massa mata o sieve mesmo com muitos municípios
MIN_MUNI_DECIL_SUPERIOR = 5    # suporte no topo, onde a hipótese de limiar põe o efeito

# --- Poder ------------------------------------------------------------------
SD_PESO_G = 500.0  # DP individual do peso ao nascer; trocar pela do SINASC real
Z_PODER = 2.8      # 80% de poder, 5% bilateral (1.96 + 0.84)


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def normaliza(texto: str) -> str:
    """Minúscula, sem acento, sem asterisco de nota de rodapé do SIDRA."""
    if not isinstance(texto, str):
        return ""
    sem_acento = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join(c for c in sem_acento if not unicodedata.combining(c))
    return sem_acento.lower().replace("*", "").strip()


def filtra_candidatas(df: pd.DataFrame, candidatas=CULTURAS_CANDIDATAS) -> pd.DataFrame:
    """Casa rótulos do PAM ("Algodão herbáceo (em caroço)") com a lista candidata.

    Casamento por substring normalizada — o rótulo oficial muda de vintage para
    vintage e não vale a pena hard-codar a string inteira.
    """
    alvo = [normaliza(c) for c in candidatas]
    rotulo_norm = df["cultura"].map(normaliza)
    mascara = pd.Series(False, index=df.index)
    for termo in alvo:
        mascara |= rotulo_norm.str.contains(termo, regex=False, na=False)
    return df.loc[mascara].copy()


def municipios_ce_sinteticos(n: int = 184) -> list[str]:
    """Códigos IBGE de 6 dígitos *sintéticos* para o Ceará (239001..239184).

    O Ceará tem 184 municípios. Os códigos reais vão de 2300101 a 2314102, então
    a faixa 239xxx é reconhecidamente falsa — de propósito: dado simulado não
    deve casar por acidente com dado real. O script 02 (SINASC) usa a mesma
    convenção, de modo que uma rodada simulada ponta a ponta ainda junta.
    """
    return [f"{239000 + i:06d}" for i in range(1, n + 1)]


def _digito_falso(cod6: str) -> str:
    """7º dígito sintético (o real é dígito verificador do IBGE)."""
    return str(sum(int(d) for d in cod6) % 10)


# --------------------------------------------------------------------------
# Fonte real: SIDRA / PAM
# --------------------------------------------------------------------------

def _sidra_para_longo(bruto: pd.DataFrame, grupo: str) -> pd.DataFrame:
    """Converte o retorno cru do sidrapy no esquema longo do projeto.

    O sidrapy devolve a primeira linha como cabeçalho descritivo e as colunas
    com códigos ("D1C", "V", ...). Em vez de hard-codar qual código é qual —
    a ordem varia entre tabelas — lemos os rótulos dessa primeira linha.
    """
    rotulos = bruto.iloc[0]
    corpo = bruto.iloc[1:].copy()

    def coluna_por_rotulo(*termos: str) -> str:
        for codigo, rotulo in rotulos.items():
            if any(t in normaliza(str(rotulo)) for t in termos):
                return str(codigo)
        raise KeyError(
            f"Coluna com rótulo {termos!r} não encontrada no retorno do SIDRA. "
            f"Rótulos vistos: {list(rotulos.values)}"
        )

    col_muni = coluna_por_rotulo("municipio (codigo)", "codigo do municipio")
    col_ano = coluna_por_rotulo("ano (codigo)", "ano")
    col_cultura = coluna_por_rotulo("lavoura", "produto")
    col_valor = coluna_por_rotulo("valor")

    longo = pd.DataFrame(
        {
            "cod_ibge": corpo[col_muni].astype(str).str.strip(),
            "ano": pd.to_numeric(corpo[col_ano], errors="coerce").astype("Int64"),
            "cultura": corpo[col_cultura].astype(str).str.strip(),
            "area_ha": _valor_sidra_para_float(corpo[col_valor]),
        }
    )
    longo["grupo"] = grupo
    return longo


def _valor_sidra_para_float(serie: pd.Series) -> pd.Series:
    """SIDRA codifica ausência com símbolos, não com vazio.

    "-"   = zero absoluto (a cultura não é plantada ali)  -> 0.0
    ".."  = não se aplica          -> NaN
    "..." = dado não disponível    -> NaN
    "X"   = omitido por sigilo     -> NaN  (importante: sigilo != zero)
    """
    limpo = serie.astype(str).str.strip()
    resultado = pd.to_numeric(limpo.str.replace(",", ".", regex=False), errors="coerce")
    return resultado.mask(limpo.isin(["..", "...", "X", "x"])).fillna(
        pd.Series(np.where(limpo == "-", 0.0, np.nan), index=serie.index)
    )


def carrega_pam_sidra(anos=ANOS_PRE_BAN) -> pd.DataFrame:
    """Baixa área plantada por cultura × município do Ceará via SIDRA (PAM/IBGE).

    Levanta exceção se o acesso não estiver disponível — quem chama decide se
    cai para o simulado.
    """
    import sidrapy  # import local: o simulado não deve exigir a dependência

    periodo = f"{min(anos)}-{max(anos)}"
    pedacos = []
    for spec in SIDRA_TABELAS:
        bruto = sidrapy.get_table(
            table_code=spec["tabela"],
            territorial_level="6",
            ibge_territorial_code=SIDRA_TERRITORIO,
            variable=spec["variavel"],
            classification=spec["classificacao"],
            categories="all",
            period=periodo,
            header="y",
        )
        if bruto is None or len(bruto) <= 1:
            raise RuntimeError(f"SIDRA devolveu vazio para a tabela {spec['tabela']}.")
        pedacos.append(_sidra_para_longo(bruto, spec["grupo"]))

    df = pd.concat(pedacos, ignore_index=True)
    df = df[df["cod_ibge"].str.startswith(UF_CEARA)]
    df = df[df["ano"].isin(anos)]
    if df.empty:
        raise RuntimeError("SIDRA respondeu, mas nada sobrou após o filtro CE/anos.")
    return df.reset_index(drop=True)


# --------------------------------------------------------------------------
# Fonte simulada (mesmo esquema; troca de uma linha para a real)
# --------------------------------------------------------------------------

def simula_pam(anos=ANOS_PRE_BAN, seed: int = SEED) -> pd.DataFrame:
    """DataFrame simulado com o esquema de `carrega_pam_sidra`.

    Serve só para exercitar o código: as magnitudes são inventadas e NÃO devem
    ser lidas como evidência sobre o Ceará. O desenho da simulação embute a
    própria pergunta do diagnóstico — algumas culturas concentradas em poucos
    municípios (dose com pouco suporte), outras espalhadas (dose utilizável) —
    para que a tabela de saída tenha o que discriminar.
    """
    rng = np.random.default_rng(seed)
    municipios = municipios_ce_sinteticos()
    codigos7 = [c + _digito_falso(c) for c in municipios]

    # (prevalência entre municípios, escala de área em ha, grupo)
    perfil = {
        "Algodão herbáceo (em caroço)": (0.08, 60, "temporária"),
        "Melão": (0.15, 900, "temporária"),
        "Melancia": (0.30, 250, "temporária"),
        "Abacaxi": (0.10, 300, "temporária"),
        "Banana (cacho)": (0.55, 400, "permanente"),
        "Mamão": (0.12, 150, "permanente"),
        "Manga": (0.20, 200, "permanente"),
        "Goiaba": (0.14, 90, "permanente"),
        "Uva": (0.03, 120, "permanente"),
        "Tomate": (0.18, 70, "temporária"),
        "Cana-de-açúcar": (0.12, 350, "temporária"),
        "Castanha de caju": (0.70, 1200, "permanente"),
        "Coco-da-baía": (0.45, 300, "permanente"),
        "Milho (em grão)": (0.98, 2500, "temporária"),
        "Feijão (em grão)": (0.98, 2000, "temporária"),
        "Arroz (em casca)": (0.25, 300, "temporária"),
        "Sorgo (em grão)": (0.22, 400, "temporária"),
        "Mandioca": (0.85, 700, "temporária"),
    }

    linhas = []
    for cultura, (prevalencia, escala, grupo) in perfil.items():
        planta = rng.random(len(municipios)) < prevalencia
        # lognormal: área agrícola é fortemente assimétrica à direita
        nivel = rng.lognormal(mean=np.log(escala), sigma=1.1, size=len(municipios))
        nivel = np.where(planta, nivel, 0.0)
        for ano in anos:
            choque = rng.normal(1.0, 0.15, size=len(municipios)).clip(0.4, 1.8)
            linhas.append(
                pd.DataFrame(
                    {
                        "cod_ibge": codigos7,
                        "ano": ano,
                        "cultura": cultura,
                        "area_ha": np.round(nivel * choque, 1),
                        "grupo": grupo,
                    }
                )
            )
    return pd.concat(linhas, ignore_index=True)


def carrega_pam(fonte: str = "auto", anos=ANOS_PRE_BAN, seed: int = SEED) -> tuple[pd.DataFrame, str]:
    """Dispatcher: 'sidra' | 'simulado' | 'auto' (tenta SIDRA, cai para simulado)."""
    if fonte == "simulado":
        return simula_pam(anos, seed), "simulado"
    if fonte == "sidra":
        return carrega_pam_sidra(anos), "sidra"
    try:
        return carrega_pam_sidra(anos), "sidra"
    except Exception as erro:  # noqa: BLE001 — qualquer falha vira fallback avisado
        print(f"[aviso] Acesso ao SIDRA indisponível ({type(erro).__name__}: {erro}).")
        print("[aviso] Caindo para dados SIMULADOS. Nada abaixo é evidência empírica.")
        return simula_pam(anos, seed), "simulado"


# --------------------------------------------------------------------------
# Diagnóstico
# --------------------------------------------------------------------------

def media_por_municipio(df: pd.DataFrame, anos=ANOS_PRE_BAN) -> pd.DataFrame:
    """Média da área 2015–2018 por município × cultura (o candidato a dose).

    Município sem linha para uma cultura conta como zero: no PAM, ausência de
    registro é ausência de plantio, e zero é dose válida (grupo de controle).
    Sigilo (NaN) é diferente de zero e continua NaN — a média ignora o ano
    omitido em vez de fingir que foi zero.
    """
    janela = df[df["ano"].isin(anos)]
    medias = (
        janela.groupby(["cod_ibge", "cultura"], as_index=False)["area_ha"]
        .mean()
        .rename(columns={"area_ha": "area_ha_media"})
    )
    grade = pd.MultiIndex.from_product(
        [sorted(janela["cod_ibge"].unique()), sorted(janela["cultura"].unique())],
        names=["cod_ibge", "cultura"],
    )
    medias = (
        medias.set_index(["cod_ibge", "cultura"])
        .reindex(grade)
        .reset_index()
    )
    medias["area_ha_media"] = medias["area_ha_media"].fillna(0.0)
    medias["cod_ibge6"] = medias["cod_ibge"].str[:6]  # chave de join com SINASC
    return medias


def dispersao_por_cultura(medias: pd.DataFrame) -> pd.DataFrame:
    """Uma linha por cultura com o que decide a especificação, não só descrição.

    Duas versões do CV de propósito:
      - cv_todos:     inclui municípios com área zero. É o CV da variável de
                      tratamento como ela entraria na regressão (zero é dose).
      - cv_positivos: só entre quem planta. Separa "dose varia entre produtores"
                      de "quase ninguém planta".

    As colunas de suporte (`n_dose_distintas`, `n_muni_acima_mediana`,
    `n_muni_decil_superior`) existem porque contagem de municípios sozinha não
    pega dois casos patológicos: muitos municípios empilhados na mesma dose, e
    cauda superior vazia — que é justamente onde a hipótese de limiar põe o
    efeito.
    """
    registros = []
    n_muni_total = medias["cod_ibge"].nunique()

    for cultura, bloco in medias.groupby("cultura"):
        area = bloco["area_ha_media"].to_numpy(dtype=float)
        positivos = area[area > 0]
        area_total = float(area.sum())

        if positivos.size:
            mediana_pos = float(np.median(positivos))
            corte_decil = float(np.percentile(positivos, 90))
            no_decil = positivos[positivos >= corte_decil]
            # Área é contínua: contar valores distintos só informa depois de
            # arredondar. 0,1 ha é a precisão em que o PAM reporta.
            n_distintas = int(np.unique(np.round(positivos, 1)).size)
        else:
            mediana_pos, no_decil, n_distintas = 0.0, np.array([]), 0

        registros.append(
            {
                "cultura": cultura,
                "n_muni_positivo": int(positivos.size),
                "n_muni_zero": int(n_muni_total - positivos.size),
                "share_muni_positivo": positivos.size / n_muni_total if n_muni_total else np.nan,
                "area_total_estado_ha": area_total,
                "area_media_positivos_ha": float(positivos.mean()) if positivos.size else 0.0,
                "mediana_positivos_ha": mediana_pos,
                "n_dose_distintas": n_distintas,
                "n_muni_acima_mediana": int((positivos > mediana_pos).sum()),
                "n_muni_decil_superior": int(no_decil.size),
                "share_area_decil_superior": (
                    float(no_decil.sum() / area_total) if area_total > 0 else np.nan
                ),
                "gini_dose": _gini(area),
                "cv_todos": float(area.std(ddof=1) / area.mean()) if area.mean() > 0 else np.nan,
                "cv_positivos": (
                    float(positivos.std(ddof=1) / positivos.mean())
                    if positivos.size > 1 and positivos.mean() > 0
                    else np.nan
                ),
                "p90_p10_positivos": _razao_p90_p10(positivos),
            }
        )

    tabela = pd.DataFrame(registros)
    return tabela.sort_values("n_muni_positivo", ascending=False).reset_index(drop=True)


def _razao_p90_p10(positivos: np.ndarray) -> float:
    if positivos.size < 10:
        return np.nan  # percentil com menos de 10 pontos não diz nada
    p10 = float(np.percentile(positivos, 10))
    p90 = float(np.percentile(positivos, 90))
    return p90 / p10 if p10 > 0 else np.nan


def _gini(valores: np.ndarray) -> float:
    """Gini da dose como ela entra na regressão — com os zeros dentro."""
    x = np.sort(np.asarray(valores, dtype=float))
    n = x.size
    if n == 0 or x.sum() <= 0:
        return np.nan
    cum = np.cumsum(x)
    return float((n + 1 - 2 * cum.sum() / cum[-1]) / n)


def recomenda_especificacao(tabela: pd.DataFrame) -> pd.DataFrame:
    """Aplica a escada do CGS. **Recomenda; não decide.**

    Substitui a coluna `sinal` da versão anterior, que dava "OK — candidata a
    dose" com base em limiares arbitrários — e aprovava, por exemplo, cultura
    com 25 municípios e três quartos da área em cinco deles.
    """
    def avalia(linha: pd.Series) -> tuple[str, str]:
        n = int(linha["n_muni_positivo"])
        if n < MIN_MUNI_FAIXAS:
            return (
                "binário (Assumption 4-Agg) — curva abandonada",
                f"{n} municípios com dose > 0, abaixo de {MIN_MUNI_FAIXAS}",
            )
        if n < MIN_MUNI_CURVA:
            return (
                "faixas discretas (indicadores múltiplos)",
                f"{n} municípios, abaixo dos {MIN_MUNI_CURVA} que o sieve pede",
            )
        motivos = []
        if linha["n_dose_distintas"] < MIN_DOSE_DISTINTAS_CURVA:
            motivos.append(f"só {int(linha['n_dose_distintas'])} valores distintos de dose")
        if linha["n_muni_decil_superior"] < MIN_MUNI_DECIL_SUPERIOR:
            motivos.append(
                f"{int(linha['n_muni_decil_superior'])} municípios no decil superior"
            )
        if motivos:
            return ("faixas discretas (indicadores múltiplos)", "; ".join(motivos))
        return ("curva não-paramétrica (sieve)", f"{n} municípios, suporte espalhado")

    saida = tabela.copy()
    avaliado = saida.apply(avalia, axis=1, result_type="expand")
    saida["especificacao"] = avaliado[0]
    saida["motivo"] = avaliado[1]
    return saida


# --------------------------------------------------------------------------
# Poder — o número que decide se vale estimar
# --------------------------------------------------------------------------

def acrescenta_mde(
    tabela: pd.DataFrame, medias: pd.DataFrame, painel: pd.DataFrame, anos_pre=ANOS_PRE_BAN
) -> pd.DataFrame:
    """Efeito mínimo detectável para peso ao nascer, nas duas contabilidades.

    A ingênua conta **bebês** — é o que uma regressão sem cluster reporta, e é
    otimista por uma ordem de grandeza. A honesta conta **municípios**, porque
    com poucos clusters tratados quem manda é a dispersão das tendências
    municipais, não o tamanho da amostra individual. A distância entre as duas é
    o argumento inteiro para Conley–Taber e wild bootstrap.

    A DP das tendências é estimada dentro do pré-período: parte-se a janela ao
    meio e mede-se, por município, a variação do peso médio. É um placebo — no
    pré-período não há tratamento, então essa variação é ruído puro.
    """
    nasc = painel.copy()
    nasc["cod_ibge6"] = nasc["cod_ibge6"].astype(str)
    total_nasc = nasc.groupby("cod_ibge6")["n_nascimentos"].sum()

    metade = min(anos_pre) + (max(anos_pre) - min(anos_pre)) // 2
    pre = nasc[nasc["ano"].isin(anos_pre)]
    inicio = pre[pre["ano"] <= metade].groupby("cod_ibge6")["peso_medio"].mean()
    fim = pre[pre["ano"] > metade].groupby("cod_ibge6")["peso_medio"].mean()
    variacao = (fim - inicio).dropna()
    sd_tendencia = float(variacao.std(ddof=1)) if variacao.size > 1 else np.nan

    linhas = []
    for cultura in tabela["cultura"]:
        bloco = medias[medias["cultura"] == cultura]
        dose = bloco.set_index("cod_ibge6")["area_ha_media"]
        positivos = dose[dose > 0]
        if positivos.empty:
            linhas.append((0, np.nan, np.nan))
            continue
        corte = float(np.percentile(positivos, 90))
        altos = dose.index[dose >= corte]
        g1 = len(altos)
        g0 = int(dose.size - g1)
        n1 = int(total_nasc.reindex(altos).fillna(0).sum())
        n0 = int(total_nasc.sum() - n1)

        ingenuo = (
            Z_PODER * SD_PESO_G * np.sqrt(1 / n1 + 1 / n0) if n1 > 0 and n0 > 0 else np.nan
        )
        agrupado = (
            Z_PODER * sd_tendencia * np.sqrt(1 / g1 + 1 / g0)
            if g1 > 0 and g0 > 0 and not np.isnan(sd_tendencia)
            else np.nan
        )
        linhas.append((n1, ingenuo, agrupado))

    saida = tabela.copy()
    saida[["n_nascimentos_dose_alta", "mde_ingenuo_g", "mde_agrupado_g"]] = pd.DataFrame(
        linhas, index=saida.index
    )
    saida.attrs["sd_tendencia_g"] = sd_tendencia
    return saida


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

def imprime_relatorio(tabela: pd.DataFrame, fonte: str, anos=ANOS_PRE_BAN) -> None:
    faixa = f"{min(anos)}–{max(anos)}"
    barra = "=" * 108
    print(barra)
    print(f"GATE 1 — VARIAÇÃO DE DOSE ENTRE MUNICÍPIOS DO CEARÁ, área média {faixa} (PAM/IBGE)")
    print(f"fonte dos dados: {fonte.upper()}")
    if fonte == "simulado":
        print("!! DADOS SIMULADOS — números inventados a partir dos próprios flags de")
        print("!! auditoria. A tabela CONFIRMA os flags por circularidade. Não é evidência.")
    print(barra)

    colunas = [
        "cultura", "n_muni_positivo", "n_dose_distintas", "n_muni_decil_superior",
        "share_area_decil_superior", "gini_dose", "cv_todos", "especificacao",
    ]
    tem_mde = "mde_agrupado_g" in tabela.columns
    if tem_mde:
        colunas = colunas[:-1] + ["mde_ingenuo_g", "mde_agrupado_g", "especificacao"]

    exibe = tabela[colunas].copy()
    exibe["share_area_decil_superior"] = exibe["share_area_decil_superior"].map(
        lambda v: "—" if pd.isna(v) else f"{v:.0%}"
    )
    for col in ("gini_dose", "cv_todos"):
        exibe[col] = exibe[col].map(lambda v: "—" if pd.isna(v) else f"{v:.2f}")
    if tem_mde:
        for col in ("mde_ingenuo_g", "mde_agrupado_g"):
            exibe[col] = exibe[col].map(lambda v: "—" if pd.isna(v) else f"{v:.1f}")
    print(exibe.to_string(index=False))
    print(barra)
    print("Como ler (ordenado por nº de municípios com dose > 0):")
    print("  • 'especificacao' é RECOMENDAÇÃO, não decisão. Vem da escada do CGS:")
    print(f"    >= {MIN_MUNI_CURVA} municípios com suporte espalhado -> curva não-paramétrica;")
    print(f"    {MIN_MUNI_FAIXAS} a {MIN_MUNI_CURVA - 1} -> faixas discretas; abaixo de {MIN_MUNI_FAIXAS} -> binário.")
    print("  • Municípios no decil superior é onde a hipótese de limiar põe o efeito —")
    print("    e é onde o suporte é mais fino. Quanto mais certa a hipótese sobre o")
    print("    formato, menos municípios carregam o efeito e maior o MDE.")
    if tem_mde:
        sd = tabela.attrs.get("sd_tendencia_g")
        print(f"  • MDE ingênuo conta bebês; MDE agrupado conta municípios (DP das")
        print(f"    tendências municipais no pré-período = {sd:.1f} g). A distância entre")
        print("    os dois é o argumento para Conley–Taber. Compare o efeito esperado")
        print("    com o AGRUPADO, nunca com o ingênuo.")
    else:
        print("  • MDE não calculado. Rode com --nascimentos <painel do script 02>.")
    print("  • Área plantada é proxy de intensidade agrícola, não de pulverização")
    print("    AÉREA. O ban proíbe o método, não a molécula.")
    print("  • Este script não escolhe a cultura-âncora. A decisão é sua.")
    print(barra)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--fonte", choices=("auto", "sidra", "simulado"), default="auto",
        help="auto (padrão): tenta SIDRA e cai para simulado se não houver acesso.",
    )
    parser.add_argument(
        "--nascimentos", type=Path, default=None,
        help="Painel do script 02 (parquet). Sem ele o MDE não é calculado.",
    )
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    bruto, fonte = carrega_pam(args.fonte, ANOS_PRE_BAN, args.seed)
    candidatas = filtra_candidatas(bruto)
    if candidatas.empty:
        print("[erro] Nenhuma cultura candidata casou com os rótulos do PAM.")
        print(f"       Rótulos disponíveis: {sorted(bruto['cultura'].unique())[:40]}")
        return 1

    medias = media_por_municipio(candidatas)
    tabela = recomenda_especificacao(dispersao_por_cultura(medias))

    if args.nascimentos is not None:
        try:
            painel = pd.read_parquet(args.nascimentos)
            tabela = acrescenta_mde(tabela, medias, painel)
        except Exception as erro:  # noqa: BLE001
            print(f"[aviso] MDE não calculado ({type(erro).__name__}: {erro}).")

    imprime_relatorio(tabela, fonte)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    # Sufixo com a fonte: diagnóstico simulado nunca deve passar por real.
    caminho_tabela = args.out_dir / f"dose_variacao_diagnostico__{fonte}.csv"
    caminho_painel = args.out_dir / f"pam_ce_muni_cultura_media__{fonte}.parquet"

    # Proveniência viaja DENTRO do arquivo, não só no nome. Um CSV desgarrado do
    # nome já foi lido como se fosse real uma vez; não de novo.
    saida = tabela.copy()
    saida.insert(0, "fonte", fonte)
    with caminho_tabela.open("w", encoding="utf-8") as fh:
        fh.write(f"# fonte={fonte} seed={args.seed} extraido_em={date.today().isoformat()}\n")
        if fonte == "simulado":
            fh.write("# ATENCAO: DADOS SIMULADOS - nao é evidência sobre o Ceará\n")
        saida.to_csv(fh, index=False)

    medias.to_parquet(caminho_painel, index=False)
    print(f"[ok] tabela diagnóstica -> {caminho_tabela}")
    print(f"[ok] painel município×cultura -> {caminho_painel}")
    print("[nota] data/processed/ é gitignored: nada disso vai para o repositório.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
