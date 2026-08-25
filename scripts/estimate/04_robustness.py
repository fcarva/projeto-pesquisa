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

3. **Inferência por aleatorização** sobre a dose. Permuta o vetor de dose entre
   municípios e reconstrói a distribuição nula do estimador. Não depende de
   assintótico nenhum: sob o nulo agudo de que a dose não importa, a
   permutação é exata. É o mais conservador dos três, e o mais difícil de
   contestar.

   ⚠️ **Isto não é Conley–Taber literal.** CT (2011) tratam o caso de tratamento
   **binário** com poucas mudanças de política, usando os resíduos do grupo de
   controle como distribuição de referência. Aqui o tratamento é **contínuo**, e
   a adaptação fiel é permutar a dose. Chamar de "Conley–Taber" seria citar
   errado; a lógica é a mesma — não confiar no assintótico —, o procedimento não.

────────────────────────────────────────────────────────────────────────────
O GATE DO E7
────────────────────────────────────────────────────────────────────────────
**O efeito estimado supera o MDE do próprio desenho?** Se não, o resultado é um
**limite superior informativo**, e é assim que tem de ser escrito. Reportar
coeficiente abaixo do próprio MDE como achado é o erro que a banca pega.

⚠️ **E a sensibilidade ao grupo `d = 0` não é opcional.** O sieve do `contdid`
centra a curva em `mean(dy[dose == 0])` — contaminação do zero **desloca o nível
inteiro**, não acrescenta ruído. Este script roda o estimador sob cada definição
de zero que você passar e reporta a **dispersão entre elas**, que É a incerteza
sobre o nível.

Uso:
    python scripts/estimate/04_robustness.py --painel data/processed/painel_ensaio1__simulado.parquet
    python scripts/estimate/04_robustness.py --desfecho taxa_baixo_peso --mde 33
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


def inferencia_aleatorizacao(dados: pd.DataFrame, n_perm: int = N_BOOT,
                             seed: int = SEED) -> dict:
    """Permuta a dose entre municípios: distribuição nula exata.

    Sob o nulo agudo de que a dose não afeta o desfecho, qual município recebeu
    qual dose é arbitrário — então permutar reconstrói a distribuição do
    estimador **sem assintótico nenhum**. É o mais conservador dos três, e o mais
    difícil de contestar com poucos tratados.

    ⚠️ Não é Conley–Taber literal: CT tratam tratamento binário com poucas
    mudanças de política, usando resíduos do controle como referência. Com
    tratamento contínuo, a adaptação fiel é esta.
    """
    rng = np.random.default_rng(seed)
    beta = estima(dados)
    if np.isnan(beta):
        return {"p": np.nan, "ic_baixo": np.nan, "ic_alto": np.nan}

    nulos = np.empty(n_perm)
    base = dados[["dose", "dy"]].copy()
    for k in range(n_perm):
        embaralhado = base.copy()
        embaralhado["dose"] = rng.permutation(base["dose"].to_numpy())
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
               "estimativa": estima(dados)}]
    for nome, excluir in definicoes.items():
        recorte = dados[~(dados["cod_ibge6"].isin(excluir) & (dados["dose"] <= 0))]
        linhas.append({
            "definicao": nome,
            "n_zero": int((recorte["dose"] <= 0).sum()),
            "estimativa": estima(recorte),
        })
    tabela = pd.DataFrame(linhas)
    tabela["desloc_vs_base"] = tabela["estimativa"] - tabela["estimativa"].iloc[0]
    return tabela


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

def imprime_relatorio(dados: pd.DataFrame, desfecho: str, mde: float | None,
                      resultados: dict, sens: pd.DataFrame | None) -> None:
    barra = "=" * 84
    beta = resultados["estimativa"]
    print(barra)
    print(f"E7 — INFERÊNCIA E GATE DO MDE | desfecho: {desfecho}")
    print(barra)
    n_pos = int((dados["dose"] > 0).sum())
    print(f"municípios: {len(dados)}  (dose > 0: {n_pos} | dose = 0: {len(dados) - n_pos})")
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
    print(f"  inferência por aleatorização            p = {rnd['p']:.3f}"
          "   ← sem assintótico; o mais duro")
    print(f"     IC 95% por inversão: [{rnd['ic_baixo']:+.3f}, {rnd['ic_alto']:+.3f}]")

    razao = rnd["p"] / ing["p"] if ing["p"] and ing["p"] > 0 else np.nan
    if not np.isnan(razao) and razao > 3:
        print(f"\n  ⚠️ A aleatorização dá p {razao:.0f}× MAIOR que o ingênuo.")
        print("     Isso não é ruído de método: é o assintótico falhando com")
        print("     poucos tratados. Reporte o conservador, não o conveniente.")

    print("-" * 84)
    print("GATE DO E7 — o efeito supera o MDE do próprio desenho?")
    if mde is None:
        print("  MDE não informado. Rode o script 01 com --nascimentos e passe --mde.")
    elif abs(beta) >= mde:
        print(f"  |{beta:+.3f}| >= MDE {mde:.3f}  ✔ o efeito é maior que o piso detectável.")
    else:
        print(f"  |{beta:+.3f}| <  MDE {mde:.3f}  ✘")
        print("  ⚠️ O coeficiente está ABAIXO do mínimo que o desenho detecta.")
        print("     Ele NÃO é um achado — é um limite superior informativo, e é")
        print("     assim que tem de ser escrito. Reportar como achado é o erro")
        print("     que a banca pega.")

    if sens is not None and len(sens) > 1:
        print("-" * 84)
        print("SENSIBILIDADE AO GRUPO d = 0 — a dispersão É a incerteza sobre o nível")
        print("  (o sieve centra a curva em mean(dy[dose==0]); trocar o zero desloca tudo)")
        for _, r in sens.iterrows():
            print(f"  {r['definicao']:<34} n_zero={r['n_zero']:>4}  "
                  f"β={r['estimativa']:+.3f}  Δ={r['desloc_vs_base']:+.3f}")
        amplitude = sens["estimativa"].max() - sens["estimativa"].min()
        print(f"  amplitude entre definições: {amplitude:.3f}")
        if mde and amplitude > mde:
            print("  ⚠️ A amplitude entre as definições de zero SUPERA o MDE.")
            print("     A escolha do zero move mais que o efeito que se quer medir.")
    print(barra)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--painel", type=Path,
                        default=OUT_DIR / "painel_ensaio1__simulado.parquet")
    parser.add_argument("--desfecho", default="peso_medio")
    parser.add_argument("--corte-pre", default="2018-12")
    parser.add_argument("--corte-pos", default="2019-10")
    parser.add_argument("--mde", type=float, default=None,
                        help="MDE do desenho, do script 01 (mde_agrupado_g).")
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

    beta = estima(dados)
    ep = erro_padrao_ingenuo(dados)
    from math import erfc, sqrt
    p_ing = erfc(abs(beta / ep) / sqrt(2)) if ep and ep > 0 else np.nan

    resultados = {
        "estimativa": beta,
        "ingenuo": {"ep": ep, "p": p_ing},
        "wcb": wild_cluster_bootstrap(dados, args.n_boot, args.seed),
        "aleatorizacao": inferencia_aleatorizacao(dados, args.n_boot, args.seed),
    }
    # sem as definições alternativas de zero (dependem de GAEZ/ANAC, ainda não
    # adquiridos), a tabela sai só com a base — e diz que sai
    sens = sensibilidade_zero(dados, {})

    imprime_relatorio(dados, args.desfecho, args.mde, resultados, sens)
    print("⚠️ Sensibilidade ao zero rodou só com a definição base: as outras três")
    print("   da §5.3 dependem de FAO-GAEZ e do cadastro aeroagrícola/SEMACE,")
    print("   ainda não adquiridos. Sem elas, o nível da curva está SEM banda.")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    linha = {"desfecho": args.desfecho, "estimativa": beta,
             "ep_ingenuo": ep, "p_ingenuo": p_ing,
             "p_wcb": resultados["wcb"]["p"],
             "p_aleatorizacao": resultados["aleatorizacao"]["p"],
             "ic_baixo": resultados["aleatorizacao"]["ic_baixo"],
             "ic_alto": resultados["aleatorizacao"]["ic_alto"],
             "mde": args.mde, "n_municipios": len(dados),
             "fonte": painel["fonte"].iloc[0] if "fonte" in painel else "?"}
    destino = args.out_dir / "robustez_inferencia.csv"
    pd.DataFrame([linha]).to_csv(destino, index=False)
    print(f"[ok] {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
