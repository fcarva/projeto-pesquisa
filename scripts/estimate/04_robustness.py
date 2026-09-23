#!/usr/bin/env python3
"""E7 — inferência honesta com poucos municípios tratados, e o gate do MDE.

**Por que este script existe.** O `contdid` faz bootstrap multiplicador
(`bstrap = TRUE`), que é assintótico no número de clusters. Com 3 a 10
municípios de dose alta — que é o cenário que o Gate 1 provavelmente entrega —
esse intervalo é **estreito demais**, e reportá-lo como se fosse a incerteza real
é o erro que a banca pega. O `CLAUDE.md` já manda: *"Inferência com poucos
clusters tratados e desfechos raros: Conley–Taber (2011) / wild-cluster
bootstrap. Não superestimar precisão."* Este script é essa exigência virando
código.

**O achado não é nenhum dos três números — é a distância entre eles.** Se o
agrupado ingênuo dá p = 0,01 e a inferência de aleatorização dá p = 0,31, o
resultado não é "significante"; é "o desenho não distingue". A saída põe os três
lado a lado de propósito.

────────────────────────────────────────────────────────────────────────────
OS TRÊS PROCEDIMENTOS, E O QUE CADA UM SUPÕE
────────────────────────────────────────────────────────────────────────────
1. **Cluster-robusto ingênuo.** Assintótico no nº de clusters. Entra como
   *linha de base a ser desmentida*, não como resultado.

2. **Wild cluster bootstrap** (Cameron, Gelbach & Miller 2008), pesos de
   Rademacher, com o nulo imposto. ⚠️ Canay, Santos & Shaikh (2021) mostram que
   ele **sub-rejeita** quando os clusters tratados são poucos — então um p alto
   aqui é informativo, mas um p baixo não absolve.

3. **Análise de permutação** sobre a dose. Permuta o vetor de dose entre
   municípios e reconstrói uma distribuição de referência do estimador, sem
   assintótico. ⚠️ **Não é inferência exata** (parecer de 2026-09-22,
   comentário 3). Seria exata se a dose tivesse sido atribuída de forma
   intercambiável entre municípios. Não foi: a dose é área de banana, e segue
   aptidão e geografia. A validade exige uma hipótese sobre essa atribuição
   (Canay, Romano & Shaikh 2017), e a hipótese tem de ser dita. Com
   `--estratos-aptidao K`, a permutação corre dentro de K faixas de aptidão
   GAEZ, e a hipótese passa a ser intercambiabilidade *condicional* à aptidão.
   É mais fraca, mas continua sendo hipótese.

   ⚠️ **Isto não é Conley–Taber literal.** CT (2011) tratam o caso de tratamento
   **binário** com poucas mudanças de política, usando os resíduos do grupo de
   controle como distribuição de referência. Aqui o tratamento é **contínuo**, e
   a adaptação fiel é permutar a dose. Chamar de "Conley–Taber" seria citar
   errado; a lógica é a mesma — não confiar no assintótico —, o procedimento não.

────────────────────────────────────────────────────────────────────────────
O MDE NÃO É RÉGUA DO RESULTADO (corrigido em 2026-09-23)
────────────────────────────────────────────────────────────────────────────
Até 2026-09-23 este script classificava a estimativa pelo MDE: abaixo dele,
"não é achado, é limite superior informativo". A auditoria de 2026-09-23
(`docs/revisao/auditoria-2026-09-23/`) mostrou que a regra é falsa. O MDE é
propriedade de PLANEJAMENTO: com 80% de poder e 5% bilateral, MDE ≈ 2,8·EP,
e a significância começa em 1,96·EP. Uma estimativa de 2,2·EP fica abaixo do
MDE e rejeita o zero. Limite superior sai de intervalo ou de teste
direcional, nunca da desigualdade |β̂| < MDE. O MDE passado por `--mde` vem
do script 01, que é do contraste decil × resto (17×167), e não se compara
nem com a inclinação daqui (g por unidade de dose) nem com o nível (169 ×
controles). O relatório o imprime como informação de desenho, e só.

O piso de 15 g da §5 da pré-especificação também era lido pela largura do
IC. Largura não testa efeito mínimo: IC [20; 30] tem meia-largura 5 e não
exclui +15. O teste certo está em `teste_piso`: o benefício de 15 g ou mais
é rejeitado quando o limite superior do IC de 95% fica abaixo de +15, e a
equivalência a ±15 g é o TOST.

⚠️ **E a sensibilidade ao grupo `d = 0` não é opcional.** O sieve do `contdid`
centra a curva em `mean(dy[dose == 0])` — contaminação do zero **desloca o nível
inteiro**, não acrescenta ruído. Este script roda o estimador sob cada definição
de zero que você passar e reporta a **dispersão entre elas**, que É a incerteza
sobre o nível.

Uso:
    python scripts/estimate/04_robustness.py --painel data/processed/painel_ensaio1__simulado.parquet
    python scripts/estimate/04_robustness.py --painel data/processed/painel_ensaio1.parquet --d-zero 4

Saída: `robustez_inferencia__<desfecho>__d0-<def>.csv` e
`robustez_perfil_dose__<desfecho>__d0-<def>.csv`, no padrão de nome do
03_contdid.R. Até 2026-09-23 os nomes eram fixos, e rodar o fetal depois do
peso apagava o peso.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20190613
N_BOOT = 2000
ALPHA = 0.05
OUT_DIR = Path("data/processed")
# Piso de efeito da §5 da pré-especificação, em gramas de PESO. Não vale para
# taxa: aplicado a `taxa_obito_fetal`, qualquer IC "passaria".
PISO_G = 15.0
DESFECHOS_EM_GRAMAS = ("peso_medio",)


# --------------------------------------------------------------------------
# Estimador
# --------------------------------------------------------------------------

def primeira_diferenca(painel: pd.DataFrame, desfecho: str,
                       t_pre: int, t_pos: int) -> pd.DataFrame:
    """Colapsa a município: variação do desfecho entre pré e pós, contra a dose.

    Esta é a MESMA forma reduzida em que o sieve do `contdid` trabalha —
    `dy <- get_first_difference(...)` seguido de regressão em dose. Fazer aqui
    o mesmo objeto é o que permite comparar as inferências de igual para igual:
    o que muda entre os três procedimentos é só como se calcula a incerteza,
    nunca o que está sendo estimado.
    """
    df = painel.copy()
    df["t"] = df["ano"] * 12 + df["mes"] - 1
    df = df[df[desfecho].notna()]

    pre = df[df["t"] <= t_pre].groupby("cod_ibge6")[desfecho].mean()
    pos = df[df["t"] >= t_pos].groupby("cod_ibge6")[desfecho].mean()
    dose = df.groupby("cod_ibge6")["dose"].first()

    saida = pd.DataFrame({"pre": pre, "pos": pos, "dose": dose}).dropna()
    saida["dy"] = saida["pos"] - saida["pre"]
    return saida.reset_index()


def estima(dados: pd.DataFrame) -> float:
    """Inclinação de `dy` sobre a dose — o ACR na forma reduzida.

    Centrada no grupo de dose zero quando ele existe, replicando o que o sieve
    faz (`m0 <- mean(dy[dose == 0]); dy_centered <- dy - m0`).
    """
    d, y = dados["dose"].to_numpy(float), dados["dy"].to_numpy(float)
    zeros = d <= 0
    if zeros.any():
        y = y - y[zeros].mean()
    dc = d - d.mean()
    var = (dc**2).sum()
    return float((dc * y).sum() / var) if var > 0 else np.nan


# --------------------------------------------------------------------------
# Inferência
# --------------------------------------------------------------------------

def erro_padrao_ingenuo(dados: pd.DataFrame) -> float:
    """EP assintótico da inclinação. Linha de base a ser desmentida."""
    d, y = dados["dose"].to_numpy(float), dados["dy"].to_numpy(float)
    n = len(d)
    if n <= 2:
        return np.nan
    dc = d - d.mean()
    var = (dc**2).sum()
    if var <= 0:
        return np.nan
    beta = estima(dados)
    resid = (y - y.mean()) - beta * dc
    # HC1, com o município como unidade — cada um é seu próprio cluster aqui,
    # porque a primeira diferença já colapsou o tempo.
    return float(np.sqrt(((dc**2) * (resid**2)).sum() / var**2 * n / (n - 2)))


def wild_cluster_bootstrap(dados: pd.DataFrame, n_boot: int = N_BOOT,
                           seed: int = SEED) -> dict:
    """Wild bootstrap com pesos de Rademacher e o nulo imposto.

    ⚠️ Canay, Santos & Shaikh (2021): sub-rejeita quando os clusters tratados
    são poucos. Um p ALTO aqui é informativo; um p baixo não absolve.
    """
    rng = np.random.default_rng(seed)
    d, y = dados["dose"].to_numpy(float), dados["dy"].to_numpy(float)
    n = len(d)
    dc = d - d.mean()
    var = (dc**2).sum()
    if var <= 0 or n <= 2:
        return {"p": np.nan, "ep": np.nan}

    beta = estima(dados)
    ep = erro_padrao_ingenuo(dados)
    # nulo imposto: resíduos do modelo restrito (inclinação zero)
    resid_nulo = y - y.mean()

    t_boot = np.empty(n_boot)
    for b in range(n_boot):
        pesos = rng.choice([-1.0, 1.0], size=n)
        y_b = y.mean() + resid_nulo * pesos
        d_b = pd.DataFrame({"dose": d, "dy": y_b})
        beta_b = estima(d_b)
        ep_b = erro_padrao_ingenuo(d_b)
        t_boot[b] = beta_b / ep_b if ep_b and ep_b > 0 else np.nan

    t_obs = beta / ep if ep and ep > 0 else np.nan
    validos = t_boot[~np.isnan(t_boot)]
    p = float((np.abs(validos) >= abs(t_obs)).mean()) if len(validos) else np.nan
    return {"p": p, "ep": ep, "n_boot_validos": len(validos)}


def _permuta(rng: np.random.Generator, valores: np.ndarray,
             estratos: np.ndarray | None) -> np.ndarray:
    """Permutação global ou dentro de cada estrato.

    Sem estratos, é exatamente `rng.permutation(valores)`: a mesma sequência de
    sorteios de antes, e portanto os mesmos números já reportados."""
    if estratos is None:
        return rng.permutation(valores)
    saida = valores.copy()
    for e in pd.unique(estratos):
        idx = np.flatnonzero(estratos == e)
        saida[idx] = valores[idx][rng.permutation(len(idx))]
    return saida


def _estratos(dados: pd.DataFrame, coluna: str | None) -> np.ndarray | None:
    if coluna is None:
        return None
    if coluna not in dados.columns:
        raise KeyError(f"coluna de estrato ausente: {coluna!r}")
    return dados[coluna].astype(str).to_numpy()


def inferencia_aleatorizacao(dados: pd.DataFrame, n_perm: int = N_BOOT,
                             seed: int = SEED, estratos: str | None = None) -> dict:
    """Permuta a dose entre municípios: ANÁLISE de permutação da inclinação.

    Sob o nulo agudo de que a dose não afeta o desfecho, e SE a dose tivesse
    sido atribuída de forma intercambiável, permutar reconstruiria a
    distribuição exata do estimador. A primeira condição é o nulo. A segunda é
    hipótese, e aqui é falsa: a dose é área de banana, que segue aptidão e
    geografia (comentário 3 do parecer de 2026-09-22). Por isso o resultado é
    análise de permutação, não inferência exata. `estratos` (nome de coluna)
    restringe a permutação a dentro de cada estrato, e a hipótese passa a ser
    intercambiabilidade condicional.

    ⚠️ Não é Conley–Taber literal: CT tratam tratamento binário com poucas
    mudanças de política, usando resíduos do controle como referência.

    ⚠️ `ic_baixo`/`ic_alto` são o ATALHO de sempre (β̂ menos os quantis da
    distribuição nula), mantido para reproduzir o número já reportado. A
    inversão feita de verdade está em `ic_inversao`.
    """
    rng = np.random.default_rng(seed)
    beta = estima(dados)
    if np.isnan(beta):
        return {"p": np.nan, "ic_baixo": np.nan, "ic_alto": np.nan}

    nulos = np.empty(n_perm)
    base = dados[["dose", "dy"]].copy()
    grupos = _estratos(dados, estratos)
    for k in range(n_perm):
        embaralhado = base.copy()
        embaralhado["dose"] = _permuta(rng, base["dose"].to_numpy(), grupos)
        nulos[k] = estima(embaralhado)

    validos = nulos[~np.isnan(nulos)]
    p = float((np.abs(validos) >= abs(beta)).mean()) if len(validos) else np.nan
    # IC por inversão: beta menos os quantis da distribuição nula centrada
    q_baixo, q_alto = np.quantile(validos, [ALPHA / 2, 1 - ALPHA / 2])
    return {
        "p": p,
        "ic_baixo": float(beta - q_alto),
        "ic_alto": float(beta - q_baixo),
        "n_perm_validas": len(validos),
    }


def ic_inversao(dados: pd.DataFrame, n_perm: int = N_BOOT, seed: int = SEED,
                alfa: float = ALPHA, estratos: str | None = None,
                n_grade: int = 801) -> dict:
    """IC da inclinação pela inversão do teste de permutação, feita de fato.

    Para cada β0, o nulo agudo "dy_i = dy_i(0) + β0·dose_i para todo município"
    torna `dy − β0·dose` invariante à atribuição. p(β0) compara a inclinação
    observada de `dy − β0·dose` sobre a dose, que é β̂ − β0, com as inclinações
    sobre as doses permutadas. O IC é o conjunto dos β0 com p(β0) > α (aqui, a
    envoltória desse conjunto).

    Como a inclinação é linear em y, slope(dy − β0·d, d_π) = a_π − β0·b_π, com
    a_π = slope(dy, d_π) e b_π = slope(d, d_π). As permutações são sorteadas
    uma vez, com a mesma semente e a mesma sequência de `inferencia_aleatorizacao`,
    e reaproveitadas na grade inteira.

    ⚠️ O atalho (β̂ menos os quantis da distribuição nula) supõe b_π = 0, isto
    é, dose permutada sem correlação com a verdadeira. Em amostra finita há
    correlação, e o atalho só aproxima a inversão. A validade continua
    dependendo da hipótese de intercambiabilidade da docstring acima.
    """
    rng = np.random.default_rng(seed)
    d = dados["dose"].to_numpy(float)
    y = dados["dy"].to_numpy(float)
    dc = d - d.mean()
    var = (dc**2).sum()
    if var <= 0 or len(d) < 3:
        return {"ic_baixo": np.nan, "ic_alto": np.nan, "p_zero": np.nan}
    beta = float((dc * y).sum() / var)
    grupos = _estratos(dados, estratos)

    a = np.empty(n_perm)
    b = np.empty(n_perm)
    for k in range(n_perm):
        dpc = _permuta(rng, d, grupos) - d.mean()
        a[k] = (dpc * y).sum() / var
        b[k] = (dpc * d).sum() / var

    def p_de(beta0: np.ndarray) -> np.ndarray:
        nulos = a[None, :] - beta0[:, None] * b[None, :]
        obs = np.abs(beta - beta0)[:, None]
        return (np.abs(nulos) >= obs - 1e-12).mean(axis=1)

    meia = 6 * a.std() if a.std() > 0 else 1.0
    grade = np.linspace(beta - meia, beta + meia, n_grade)
    aceitos = grade[p_de(grade) > alfa]
    if len(aceitos) == 0:
        return {"ic_baixo": np.nan, "ic_alto": np.nan,
                "p_zero": float(p_de(np.array([0.0]))[0])}
    borda = aceitos.min() == grade[0] or aceitos.max() == grade[-1]
    return {
        "ic_baixo": float(aceitos.min()),
        "ic_alto": float(aceitos.max()),
        "p_zero": float(p_de(np.array([0.0]))[0]),
        "toca_a_borda_da_grade": bool(borda),
    }


# --------------------------------------------------------------------------
# O nível — o ATT(d|d) agregado, no mesmo estimando
# --------------------------------------------------------------------------
# Acrescentado em 2026-09-23 pelo comentário 4 do parecer de 2026-09-22
# (docs/revisao/feedback-2026-09-22.md). A §6.2 reporta o ATT(d|d) agregado,
# −36,19 g com IC do multiplicador que exclui o zero, e a Tabela 8 faz a
# inferência robusta sobre OUTRO objeto, a inclinação de +6,81. O parecer pede
# inferência robusta sobre o próprio ATT(d|d).
#
# Sob PT, ATT(d|d) = E[ΔY|D=d] − E[ΔY|D=0], e a média disso entre os tratados
# é E[ΔY|D>0] − E[ΔY|D=0]: o DiD binarizado. CONFERIDO NO CÓDIGO fixado no
# renv.lock: com o sieve, o `overall_att` do contdid (5cfec81, R/cont_did.R,
# l. 289–317) sai de `ptetools::pte_default`; o `pte_attgt` (ptetools bda4aa5)
# toma ΔY e roda `DRDID::drdid_panel` só com intercepto e pesos iguais, que é
# a diferença de médias; e o 03_contdid.R põe g = 2 se dose > 0. O agregado É
# esta diferença de médias, sem reponderação, e a inferência sobre ele pode ser
# feita aqui, sobre a mesma primeira diferença.
#
# ⚠️ O lado escasso é o de CONTROLE. São 15 municípios de área nula (14 pela
# definição 4) contra 169 com área positiva. A variância do nível é dominada
# pela média dos 15, e as especificações binárias da §6 (decil × zero)
# reutilizam os mesmos 15. Variam o tratado e o estimando, não o controle:
# concordância de sinal entre elas não é independência.

def nivel(dados: pd.DataFrame) -> float:
    """ATT(d|d) agregado da primeira diferença: média de dy entre os de dose > 0
    menos a média entre os de dose = 0."""
    d, y = dados["dose"].to_numpy(float), dados["dy"].to_numpy(float)
    trat, ctrl = d > 0, d <= 0
    if not trat.any() or not ctrl.any():
        return np.nan
    return float(y[trat].mean() - y[ctrl].mean())


def zeros_suspeitos(painel: pd.DataFrame, aptidao_p: float = 0.75) -> set:
    """Definição 4 da §5.3: zeros de área com aptidão GAEZ acima do percentil.

    A mesma regra do 03_contdid.R: o corte é o quantil `aptidao_p` da aptidão
    sobre todos os municípios, e sai do grupo de comparação o município de
    área nula com aptidão acima dele. Com o painel real, sai 1 dos 15 (230523),
    e ficam os 14 do agregado de −36,19 g.

    ⚠️ Zero sem aptidão é ERRO, não controle (auditoria de 2026-09-23). Antes,
    o R mantinha esse município, porque `NA > corte` não é verdadeiro, e o
    07/08 o descartava, porque `NA <= corte` também não. As duas rotas diziam
    "definição 4" com amostras diferentes.
    """
    if "aptidao_gaez" not in painel.columns:
        raise ValueError("a definição 4 exige `aptidao_gaez` no painel. Rode antes: make gaez")
    por_muni = painel.drop_duplicates("cod_ibge6")[["cod_ibge6", "dose", "aptidao_gaez"]]
    zeros = por_muni[por_muni["dose"] <= 0]
    sem = zeros.loc[zeros["aptidao_gaez"].isna(), "cod_ibge6"].tolist()
    if sem:
        raise ValueError(f"município(s) de dose zero sem aptidão GAEZ: {sem}. "
                         "A definição 4 não decide o lado deles.")
    corte = por_muni["aptidao_gaez"].quantile(aptidao_p)
    return set(zeros.loc[zeros["aptidao_gaez"] > corte, "cod_ibge6"])


def aplica_d_zero(dados: pd.DataFrame, suspeitos: set) -> pd.DataFrame:
    """Tira do grupo de comparação os zeros suspeitos. Os tratados não mudam."""
    fora = dados["cod_ibge6"].isin(suspeitos) & (dados["dose"] <= 0)
    return dados[~fora].reset_index(drop=True)


def _ep_welch(y_t: np.ndarray, y_c: np.ndarray) -> float:
    if len(y_t) < 2 or len(y_c) < 2:
        return np.nan
    return float(np.sqrt(y_t.var(ddof=1) / len(y_t) + y_c.var(ddof=1) / len(y_c)))


def _gl_welch(y_t: np.ndarray, y_c: np.ndarray) -> float:
    """Graus de liberdade de Welch–Satterthwaite.

    Com 14 controles e 169 tratados ficam perto de 14, porque quase toda a
    variância vem da média dos controles: a cauda é a de uma t com ~14 gl, e
    não a normal que o `p_welch` usava até 2026-09-23.
    """
    if len(y_t) < 2 or len(y_c) < 2:
        return np.nan
    v_t = y_t.var(ddof=1) / len(y_t)
    v_c = y_c.var(ddof=1) / len(y_c)
    den = v_t**2 / (len(y_t) - 1) + v_c**2 / (len(y_c) - 1)
    return float((v_t + v_c) ** 2 / den) if den > 0 else np.nan


def teste_piso(est: float, ep: float, gl: float, piso: float = PISO_G,
               alfa: float = ALPHA) -> dict:
    """O piso de 15 g da §5, testado como teste, e não pela largura do IC.

    - **Benefício ≥ piso rejeitado** quando o limite superior do IC de 95% fica
      abaixo de `+piso`. É o teste unilateral de H0: θ ≥ piso, a 2,5%, e usa o
      mesmo IC de 95% com que a §5 foi escrita. `p_beneficio_piso` é o p dele.
    - **Equivalência a ±piso** pelo TOST: os dois testes unilaterais a `alfa`,
      que é o mesmo que o IC de 90% caber dentro de (−piso; +piso).

    A regra antiga, `1,96·EP ≤ piso`, ignora o centro: IC [20; 30] passaria e
    IC [−66,5; −5,9] não, embora o segundo exclua +15 e o primeiro não.
    """
    from scipy.stats import t as dist_t
    if not (np.isfinite(est) and np.isfinite(ep) and ep > 0 and np.isfinite(gl)):
        return {"ic_baixo": np.nan, "ic_alto": np.nan, "p_beneficio_piso": np.nan,
                "rejeita_beneficio_piso": False, "p_equivalencia": np.nan,
                "equivalente_piso": False}
    q = dist_t.ppf(1 - alfa / 2, gl)
    ic_baixo, ic_alto = est - q * ep, est + q * ep
    p_sup = float(dist_t.cdf((est - piso) / ep, gl))       # H0: θ ≥ +piso
    p_inf = float(dist_t.sf((est + piso) / ep, gl))        # H0: θ ≤ −piso
    p_equiv = max(p_sup, p_inf)
    return {"ic_baixo": float(ic_baixo), "ic_alto": float(ic_alto),
            "p_beneficio_piso": p_sup,
            "rejeita_beneficio_piso": bool(ic_alto < piso),
            "p_equivalencia": p_equiv, "equivalente_piso": bool(p_equiv < alfa)}


def _t_nivel(d: np.ndarray, y: np.ndarray) -> float:
    trat, ctrl = d > 0, d <= 0
    ep = _ep_welch(y[trat], y[ctrl])
    return float((y[trat].mean() - y[ctrl].mean()) / ep) if ep and ep > 0 else np.nan


def inferencia_nivel(dados: pd.DataFrame, n_boot: int = N_BOOT, seed: int = SEED,
                     estratos: str | None = None, piso: float | None = None) -> dict:
    """O nível e quatro leituras da incerteza dele. Nenhuma vale sozinha.

    1. **Welch**, heterocedástico. `p_welch` e o IC usam a t com graus de
       liberdade de Welch–Satterthwaite (`gl_welch`); `p_normal` é a cauda
       normal que este campo usava até 2026-09-23, mantida para comparação.
       Com 14 ou 15 controles, a diferença entre as duas não é detalhe.
    2. **Wild bootstrap** com o nulo imposto: pesos de Rademacher sobre os
       resíduos em torno da média comum, estatística t de Welch. ⚠️ Com poucos
       clusters num dos grupos ele pode errar (Canay, Santos & Shaikh 2021
       tratam o caso de poucos tratados; aqui são poucos controles).
    3. **Permutação do rótulo** produtor/não produtor, com a estatística
       studentizada. É análise, não inferência exata, pela mesma razão da
       inclinação: ser produtor de banana não é intercambiável entre
       municípios. `estratos` restringe a permutação a dentro de cada estrato.
    4. **Jackknife dos controles**: o nível sem cada um dos controles. Com 15,
       um só pode mover tudo. É a pergunta "quem está fazendo o número?".

    Com `piso` (gramas), acrescenta o teste do piso da §5 (`teste_piso`).
    """
    from scipy.stats import t as dist_t
    d = dados["dose"].to_numpy(float)
    y = dados["dy"].to_numpy(float)
    trat, ctrl = d > 0, d <= 0
    n_t, n_c = int(trat.sum()), int(ctrl.sum())
    vazio = {"nivel": np.nan, "ep_welch": np.nan, "gl_welch": np.nan,
             "p_welch": np.nan, "p_normal": np.nan, "ic_baixo": np.nan,
             "ic_alto": np.nan, "p_wcb": np.nan, "p_perm": np.nan,
             "jack_min": np.nan, "jack_max": np.nan, "jack_cod_min": "",
             "jack_cod_max": "", "n_tratados": n_t, "n_controles": n_c}
    if piso is not None:
        vazio.update({"p_beneficio_piso": np.nan, "rejeita_beneficio_piso": False,
                      "p_equivalencia": np.nan, "equivalente_piso": False})
    if n_t < 2 or n_c < 2:
        return vazio

    from math import erfc, sqrt
    est = float(y[trat].mean() - y[ctrl].mean())
    ep = _ep_welch(y[trat], y[ctrl])
    gl = _gl_welch(y[trat], y[ctrl])
    t_obs = est / ep if ep > 0 else np.nan
    p_normal = erfc(abs(t_obs) / sqrt(2)) if not np.isnan(t_obs) else np.nan
    p_welch = (float(2 * dist_t.sf(abs(t_obs), gl))
               if np.isfinite(t_obs) and np.isfinite(gl) else np.nan)
    q = dist_t.ppf(1 - ALPHA / 2, gl) if np.isfinite(gl) else np.nan

    rng = np.random.default_rng(seed)
    resid = y - y.mean()
    t_wcb = np.array([_t_nivel(d, y.mean() + resid * rng.choice([-1.0, 1.0], size=len(y)))
                      for _ in range(n_boot)])
    t_wcb = t_wcb[~np.isnan(t_wcb)]
    p_wcb = float((np.abs(t_wcb) >= abs(t_obs)).mean()) if len(t_wcb) else np.nan

    rng = np.random.default_rng(seed)
    grupos = _estratos(dados, estratos)
    t_perm = np.array([_t_nivel(_permuta(rng, d, grupos), y) for _ in range(n_boot)])
    t_perm = t_perm[~np.isnan(t_perm)]
    p_perm = float((np.abs(t_perm) >= abs(t_obs)).mean()) if len(t_perm) else np.nan

    cods = dados["cod_ibge6"].astype(str).to_numpy() if "cod_ibge6" in dados else \
        np.array([str(i) for i in range(len(d))])
    jack = {}
    for i in np.flatnonzero(ctrl):
        manter = np.ones(len(d), bool)
        manter[i] = False
        jack[cods[i]] = float(y[manter & trat].mean() - y[manter & ctrl].mean())
    cod_min = min(jack, key=jack.get)
    cod_max = max(jack, key=jack.get)
    saida = {"nivel": est, "ep_welch": ep, "gl_welch": gl, "p_welch": p_welch,
             "p_normal": p_normal, "ic_baixo": est - q * ep, "ic_alto": est + q * ep,
             "p_wcb": p_wcb, "p_perm": p_perm, "jack_min": jack[cod_min],
             "jack_max": jack[cod_max], "jack_cod_min": cod_min,
             "jack_cod_max": cod_max, "n_tratados": n_t, "n_controles": n_c}
    if piso is not None:
        tp = teste_piso(est, ep, gl, piso)
        saida.update({k: tp[k] for k in ("p_beneficio_piso", "rejeita_beneficio_piso",
                                         "p_equivalencia", "equivalente_piso")})
    return saida


def perfil_por_faixa(dados: pd.DataFrame, n_faixas: int = 3) -> pd.DataFrame:
    """Média de dy no grupo de dose zero e em cada faixa (quantil) da dose positiva.

    É a olhada não paramétrica que o nível e a inclinação resumem. Se o nível
    for grande e as faixas positivas forem planas entre si, o número vem da
    comparação produtor × não produtor (a margem extensiva), e não da dose. É
    a assinatura de tendência diferencial entre os dois grupos, não de efeito
    do ban, que cresceria com a exposição.
    """
    d, y = dados["dose"].to_numpy(float), dados["dy"].to_numpy(float)
    linhas = []

    def linha(rotulo, m):
        n = int(m.sum())
        ep = float(y[m].std(ddof=1) / np.sqrt(n)) if n > 1 else np.nan
        linhas.append({"faixa": rotulo, "n": n,
                       "dose_media": float(d[m].mean()) if n else np.nan,
                       "dy_medio": float(y[m].mean()) if n else np.nan, "ep": ep})

    linha("dose = 0", d <= 0)
    pos = d > 0
    if pos.sum() >= n_faixas:
        faixas = pd.qcut(pd.Series(d[pos]).rank(method="first"), n_faixas, labels=False).to_numpy()
        idx_pos = np.flatnonzero(pos)
        for k in range(n_faixas):
            m = np.zeros(len(d), bool)
            m[idx_pos[faixas == k]] = True
            linha(f"dose > 0, faixa {k + 1}/{n_faixas}", m)
    return pd.DataFrame(linhas)


# --------------------------------------------------------------------------
# Sensibilidade ao grupo d = 0
# --------------------------------------------------------------------------

def sensibilidade_zero(dados: pd.DataFrame,
                       definicoes: dict[str, set[str]]) -> pd.DataFrame:
    """Reestima sob cada definição de `d = 0`. A dispersão É a incerteza.

    ⚠️ Não é robustez decorativa. O sieve do `contdid` centra a curva inteira em
    `mean(dy[dose == 0])`: trocar quem está no zero **desloca o nível**, não
    acrescenta ruído. As quatro construções da §5.3 de
    `03-modelagem-ensaio1.md` têm de ser rodadas, e o intervalo entre elas é o
    que se reporta.

    `definicoes` mapeia nome → conjunto de `cod_ibge6` que **saem** do grupo zero
    (por exemplo, os municípios com controle vetorial aéreo, pelo §2º do
    art. 28-B).
    """
    linhas = [{"definicao": "base (PAM, área nula)", "n_zero": int((dados["dose"] <= 0).sum()),
               "estimativa": estima(dados), "nivel": nivel(dados)}]
    for nome, excluir in definicoes.items():
        recorte = aplica_d_zero(dados, excluir)
        linhas.append({
            "definicao": nome,
            "n_zero": int((recorte["dose"] <= 0).sum()),
            "estimativa": estima(recorte),
            # o nível também: até 2026-09-23 a tabela só trazia a inclinação,
            # e o rótulo falava do nível (auditoria de 2026-09-23)
            "nivel": nivel(recorte),
        })
    tabela = pd.DataFrame(linhas)
    tabela["desloc_vs_base"] = tabela["estimativa"] - tabela["estimativa"].iloc[0]
    tabela["desloc_nivel"] = tabela["nivel"] - tabela["nivel"].iloc[0]
    return tabela


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

def imprime_relatorio(dados: pd.DataFrame, desfecho: str, mde: float | None,
                      resultados: dict, sens: pd.DataFrame | None) -> None:
    barra = "=" * 84
    beta = resultados["estimativa"]
    print(barra)
    print(f"E7 — INFERÊNCIA NO MESMO ESTIMANDO | desfecho: {desfecho}")
    print(barra)
    n_pos = int((dados["dose"] > 0).sum())
    print(f"municípios: {len(dados)}  (dose > 0: {n_pos} | dose = 0: {len(dados) - n_pos})"
          f"  | d = 0 pela {resultados.get('rotulo_d_zero', 'definição 1')}")
    print(f"estimativa (inclinação dy ~ dose): {beta:+.3f}")
    print("-" * 84)

    print("OS TRÊS PROCEDIMENTOS — o achado é a DISTÂNCIA entre eles")
    ing = resultados["ingenuo"]
    print(f"  cluster-robusto ingênuo   EP {ing['ep']:.3f}   p = {ing['p']:.3f}"
          "   ← linha de base a desmentir")
    wcb = resultados["wcb"]
    print(f"  wild cluster bootstrap                  p = {wcb['p']:.3f}"
          "   ← sub-rejeita com poucos tratados")
    rnd = resultados["aleatorizacao"]
    print(f"  análise de permutação da dose           p = {rnd['p']:.3f}"
          "   ← sem assintótico; exige intercambiabilidade")
    print(f"     IC 95%, atalho (β̂ − quantis do nulo): [{rnd['ic_baixo']:+.3f}, {rnd['ic_alto']:+.3f}]")
    inv = resultados.get("inversao")
    if inv is not None:
        print(f"     IC 95%, inversão do teste:          [{inv['ic_baixo']:+.3f}, {inv['ic_alto']:+.3f}]"
              + ("   ⚠️ toca a borda da grade" if inv.get("toca_a_borda_da_grade") else ""))
    if resultados.get("estratos"):
        print(f"     permutação dentro de estratos: {resultados['estratos']}")
    else:
        print("     ⚠️ permutação global: supõe dose intercambiável entre TODOS os")
        print("        municípios, o que a aptidão desmente. É análise de permutação,")
        print("        não inferência exata (parecer de 2026-09-22, comentário 3).")

    razao = rnd["p"] / ing["p"] if ing["p"] and ing["p"] > 0 else np.nan
    if not np.isnan(razao) and razao > 3:
        print(f"\n  ⚠️ A aleatorização dá p {razao:.0f}× MAIOR que o ingênuo.")
        print("     Isso não é ruído de método: é o assintótico falhando com")
        print("     poucos tratados. Reporte o conservador, não o conveniente.")

    niv = resultados.get("nivel")
    if niv is not None and not np.isnan(niv["nivel"]):
        print("-" * 84)
        print("O NÍVEL — o ATT(d|d) agregado, com a inferência no MESMO estimando")
        print(f"  média(dy | dose>0) − média(dy | dose=0) = {niv['nivel']:+.3f}"
              f"   ({niv['n_tratados']} tratados × {niv['n_controles']} controles)")
        print(f"  Welch: EP {niv['ep_welch']:.3f}, {niv['gl_welch']:.1f} gl   "
              f"IC 95% [{niv['ic_baixo']:+.3f}; {niv['ic_alto']:+.3f}]   p = {niv['p_welch']:.3f}")
        print(f"     (cauda normal, a leitura de antes: p = {niv['p_normal']:.3f} — otimista"
              " com poucos controles)")
        print(f"  wild bootstrap (nulo imposto)   p = {niv['p_wcb']:.3f}")
        print(f"  permutação do rótulo            p = {niv['p_perm']:.3f}"
              "   ← análise, não exata")
        print(f"  jackknife dos controles: [{niv['jack_min']:+.3f}, {niv['jack_max']:+.3f}]"
              f"   (sem {niv['jack_cod_min']} / sem {niv['jack_cod_max']})")
        if niv["n_controles"] < 30:
            print(f"  ⚠️ {niv['n_controles']} controles. O lado escasso do nível é o de")
            print("     CONTROLE, não o de tratados. As especificações binárias da §6")
            print("     reutilizam o mesmo grupo: concordarem não é independência.")
        if "p_beneficio_piso" in niv:
            print(f"  PISO DE {PISO_G:.0f} g DA §5 — testado, não pela largura do IC:")
            if niv["rejeita_beneficio_piso"]:
                print(f"    benefício ≥ {PISO_G:.0f} g: REJEITADO (o IC fica abaixo de "
                      f"+{PISO_G:.0f}; p unilateral = {niv['p_beneficio_piso']:.4f})")
            else:
                print(f"    benefício ≥ {PISO_G:.0f} g: não rejeitado "
                      f"(p unilateral = {niv['p_beneficio_piso']:.4f})")
            print(f"    equivalência a ±{PISO_G:.0f} g (TOST): "
                  + ("SIM" if niv["equivalente_piso"] else "não")
                  + f"  (p = {niv['p_equivalencia']:.4f})")
            print("    ⚠️ Sob PT e com a inferência de Welch valendo. E é o estimando")
            print("       diluído: rejeitar +15 g aqui não diz nada sobre o efeito")
            print("       onde havia avião (VPP ≈ 7/169 em 2006).")
        perfil = resultados.get("perfil")
        if perfil is not None and len(perfil) > 1:
            print("  dy médio por faixa — o nível cresce com a dose, ou é só o zero?")
            for _, r in perfil.iterrows():
                print(f"    {r['faixa']:<24} n={r['n']:>4}  dose média {r['dose_media']:.3f}"
                      f"  dy {r['dy_medio']:+9.3f}  (EP {r['ep']:.3f})")

    print("-" * 84)
    print("MDE — informação de PLANEJAMENTO, não régua do resultado")
    if mde is None:
        print("  MDE não informado. Para o MDE de cada contraste: make mde-desenhos.")
    else:
        print(f"  MDE informado: {mde:.1f} g (80% de poder, 5% bilateral, aprox. normal).")
        print("  ⚠️ A estimativa NÃO se classifica por ele: MDE ≈ 2,8·EP e a")
        print("     significância começa em 1,96·EP, então uma estimativa abaixo do")
        print("     MDE pode rejeitar o zero. O que se reporta é o IC. E o MDE do")
        print("     script 01 é do decil × resto (17×167): nem a inclinação (g por")
        print("     unidade de dose) nem o nível (169 × controles) são esse contraste.")

    if sens is not None and len(sens) > 1:
        print("-" * 84)
        print("SENSIBILIDADE AO GRUPO d = 0 — a dispersão É a incerteza sobre o nível")
        print("  (o sieve centra a curva em mean(dy[dose==0]); trocar o zero desloca tudo)")
        for _, r in sens.iterrows():
            print(f"  {r['definicao']:<34} n_zero={r['n_zero']:>4}  "
                  f"β={r['estimativa']:+.3f}  nível={r['nivel']:+.3f}  "
                  f"Δnível={r['desloc_nivel']:+.3f}")
        print(f"  amplitude do nível entre definições: "
              f"{sens['nivel'].max() - sens['nivel'].min():.3f}")
    print(barra)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

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
    parser.add_argument("--painel", type=Path,
                        default=OUT_DIR / "painel_ensaio1__simulado.parquet")
    parser.add_argument("--desfecho", default="peso_medio")
    parser.add_argument("--corte-pre", default="2018-12")
    parser.add_argument("--corte-pos", default="2019-10")
    parser.add_argument("--mde", type=float, default=None,
                        help="MDE do desenho, só como informação (não classifica a "
                             "estimativa). O de cada contraste: make mde-desenhos.")
    parser.add_argument("--d-zero", choices=("1", "4"), default="1",
                        help="construção do d = 0 da inferência principal: 1 = área "
                             "nula; 4 = área nula e aptidão GAEZ <= p75, a ratificada, "
                             "que o `make real` passa (D_ZERO). A tabela de "
                             "sensibilidade traz as duas de qualquer forma.")
    parser.add_argument("--piso", type=float, default=PISO_G,
                        help="piso da §5 em gramas; só para desfecho em gramas.")
    parser.add_argument("--aptidao-p", type=float, default=0.75,
                        help="percentil de aptidão GAEZ acima do qual o zero é "
                             "SUSPEITO (definição 4 da §5.3). ⚠️ p75 deixa 14 de "
                             "15 controles; p25 deixa 5 — cortes apertados "
                             "destroem o grupo de comparação.")
    parser.add_argument("--estratos-aptidao", type=int, default=0,
                        help="permutar dentro de K faixas (quantis) de aptidão GAEZ; "
                             "0 = permutação global, a de sempre. Troca a hipótese de "
                             "intercambiabilidade global pela condicional à aptidão.")
    parser.add_argument("--n-boot", type=int, default=N_BOOT)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    if not args.painel.exists():
        print(f"[erro] Painel não encontrado: {args.painel}")
        print("       Rode antes: python scripts/build_panel/05_build_panel.py --cultura ...")
        return 1

    painel = pd.read_parquet(args.painel)
    if args.desfecho not in painel.columns:
        print(f"[erro] Desfecho {args.desfecho!r} não está no painel.")
        print(f"       Disponíveis: {[c for c in painel.columns if c.startswith(('peso','taxa','n_'))][:12]}")
        return 1

    def t_de(txt):
        a, m = (int(x) for x in txt.split("-"))
        return a * 12 + m - 1

    dados = primeira_diferenca(painel, args.desfecho, t_de(args.corte_pre), t_de(args.corte_pos))
    if len(dados) < 5:
        print(f"[erro] Só {len(dados)} municípios com pré e pós. Nada a inferir.")
        return 1

    # A tabela de sensibilidade usa `todos`; a inferência, a definição pedida.
    todos = dados
    suspeitos: set = set()
    if args.d_zero == "4":
        try:
            suspeitos = zeros_suspeitos(painel, args.aptidao_p)
        except ValueError as erro:
            print(f"[erro] {erro}")
            return 1
        dados = aplica_d_zero(todos, suspeitos)
    rotulo_d_zero = (f"definição 4 (aptidão GAEZ <= p{int(args.aptidao_p * 100)}; "
                     f"{len(suspeitos)} zero(s) fora)" if args.d_zero == "4"
                     else "definição 1 (área nula)")
    piso = args.piso if args.desfecho in DESFECHOS_EM_GRAMAS else None

    beta = estima(dados)
    ep = erro_padrao_ingenuo(dados)
    from math import erfc, sqrt
    p_ing = erfc(abs(beta / ep) / sqrt(2)) if ep and ep > 0 else np.nan

    estratos, rotulo_estratos = None, ""
    if args.estratos_aptidao > 1:
        if "aptidao_gaez" not in painel.columns:
            print("[erro] --estratos-aptidao exige `aptidao_gaez` no painel. Rode antes: make gaez")
            return 1
        apt = (painel.drop_duplicates("cod_ibge6").set_index("cod_ibge6")["aptidao_gaez"])
        faixas = pd.qcut(apt.rank(method="first"), args.estratos_aptidao, labels=False)
        dados["estrato"] = dados["cod_ibge6"].map(faixas).fillna(-1).astype(int).astype(str)
        estratos = "estrato"
        rotulo_estratos = f"{args.estratos_aptidao} faixas de aptidão GAEZ"

    resultados = {
        "estimativa": beta,
        "ingenuo": {"ep": ep, "p": p_ing},
        "wcb": wild_cluster_bootstrap(dados, args.n_boot, args.seed),
        "aleatorizacao": inferencia_aleatorizacao(dados, args.n_boot, args.seed,
                                                  estratos=estratos),
        "inversao": ic_inversao(dados, args.n_boot, args.seed, estratos=estratos),
        "nivel": inferencia_nivel(dados, args.n_boot, args.seed, estratos=estratos,
                                  piso=piso),
        "perfil": perfil_por_faixa(dados),
        "estratos": rotulo_estratos,
        "rotulo_d_zero": rotulo_d_zero,
    }
    # ⚠️ ATUALIZADO 2026-09-21: o FAO-GAEZ FOI adquirido, e a definição 4 da §5.3
    # passa a rodar. A mensagem anterior — "dependem de GAEZ, ainda não
    # adquiridos" — virou falsa e dizia ao leitor que a banda era impossível
    # quando ela já era calculável.
    definicoes = {}
    if "aptidao_gaez" in painel.columns:
        try:
            definicoes[f"def. 4 — aptidão GAEZ > p{int(args.aptidao_p*100)}"] = \
                zeros_suspeitos(painel, args.aptidao_p)
        except ValueError as erro:
            print(f"[aviso] definição 4 fora da tabela de sensibilidade: {erro}")

    sens = sensibilidade_zero(todos, definicoes)

    imprime_relatorio(dados, args.desfecho, args.mde, resultados, sens)
    if definicoes:
        print("✅ Sensibilidade ao zero inclui a DEFINIÇÃO 4 (aptidão FAO-GAEZ),")
        print("   ratificada na pré-especificação de 2026-09-21.")
        print("   ⚠️ A definição 3 (cadastro aeroagrícola) segue impossível: o")
        print("      SIPEAGRO não tem profundidade histórica, e a LAI à SEMACE é")
        print("      a única rota para o pré-ban. Ver lacunas-de-dados.md §1-bis.")
    else:
        print("⚠️ Sem `aptidao_gaez` no painel, só a definição base roda.")
        print("   Rode antes: make gaez")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    linha = {"desfecho": args.desfecho, "estimativa": beta,
             "ep_ingenuo": ep, "p_ingenuo": p_ing,
             "p_wcb": resultados["wcb"]["p"],
             "p_aleatorizacao": resultados["aleatorizacao"]["p"],
             "ic_baixo": resultados["aleatorizacao"]["ic_baixo"],
             "ic_alto": resultados["aleatorizacao"]["ic_alto"],
             "ic_inv_baixo": resultados["inversao"]["ic_baixo"],
             "ic_inv_alto": resultados["inversao"]["ic_alto"],
             "estratos": rotulo_estratos or "global",
             **{f"nivel_{k}" if k != "nivel" else "nivel": v
                for k, v in resultados["nivel"].items()},
             "mde": args.mde, "n_municipios": len(dados), "d_zero": args.d_zero,
             "piso_g": piso if piso is not None else np.nan,
             "corte_pre": args.corte_pre, "corte_pos": args.corte_pos,
             "seed": args.seed, "n_boot": args.n_boot,
             "fonte": painel["fonte"].iloc[0] if "fonte" in painel else "?"}
    sufixo = f"__{args.desfecho}__d0-{args.d_zero}"
    destino = args.out_dir / f"robustez_inferencia{sufixo}.csv"
    pd.DataFrame([linha]).to_csv(destino, index=False)
    print(f"[ok] {destino}")
    destino_perfil = args.out_dir / f"robustez_perfil_dose{sufixo}.csv"
    resultados["perfil"].assign(desfecho=args.desfecho, d_zero=args.d_zero).to_csv(
        destino_perfil, index=False)
    print(f"[ok] {destino_perfil}")
    destino_sens = args.out_dir / f"robustez_sensibilidade_zero{sufixo}.csv"
    sens.assign(desfecho=args.desfecho).to_csv(destino_sens, index=False)
    print(f"[ok] {destino_sens}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
