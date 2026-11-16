"""Rodada 21 — diferença tripla de calendário sobre DADO REAL. EXPLORATÓRIO.

⚠️ NÃO é a análise confirmatória do projeto. Autorizada pelo pesquisador em
2026-11-15 ("vamos rodar novas com dados reais"), contra a regra do projeto de
não cruzar a exposição sazonal com o desfecho antes do plano ratificado.
Consequência declarada: depois desta rodada, o desenho de calendário já foi
visto contra o desfecho; nenhum número daqui entra em `paper/projeto/`.

O que é PROVISÓRIO aqui (e não medido):
  - A_m       : estabelecimento com aplicação por aeronave no Censo Agro 2006
                (SIDRA 1008) — 7 municípios; variante "Chapada" = Limoeiro + Quixeré.
  - estação   : quadra chuvosa, fev–mai (hipótese; os relatórios do MAPA não vieram).
  - comparação: banana (>= N estab., Censo 2017, SIDRA 6955) sem aeronave em 2006
                e fração familiar de ESTABELECIMENTOS >= limiar. A fração por
                área tem sigilo (X) em ~metade dos municípios.
  - chuva     : AUSENTE. A eq. do projeto tem theta_k (k x chuva da quadra); sem
                série municipal de chuva, esses termos ficam fora. Lacuna.

Especificação (05-metodologia.tex, eq. ddd, sem os termos de chuva):
  Y_mt = a_{m,mes} + mu_{m,ano} + g_t
         + sum_{k in I,H} [ bS_k A_m k_t Seca_t + b_k A_m k_t Pos_t ] + e
  ponderada por nascimentos com peso válido; 2012 e 2019 excluídos.

Uso:
  python scripts/exploratorio/21_calendario_exploratorio.py \
      --dados projeto-pesquisa/data/processed/rodada21 [--perm 999]
"""
from __future__ import annotations

import argparse
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
SEED = 20261115
ESTACAO = (2, 3, 4, 5)          # quadra chuvosa — HIPÓTESE
REF, SECA, POS = (2007, 2011), (2013, 2018), (2020, 2024)
CHAPADA = {"230760", "231150"}  # Limoeiro do Norte (2307601), Quixeré (2311504)


def exposicao(mes: int, estacao=ESTACAO) -> float:
    """Fração dos meses t-9..t-4 (dois primeiros trimestres) dentro da estação."""
    janela = [((mes - k - 1) % 12) + 1 for k in range(4, 10)]
    return float(np.mean([m in estacao for m in janela]))


def monta(dados: Path, limiar: float, n_min: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    nasc = pd.read_parquet(dados / "nascimentos_ce_muni_mes.parquet")
    nasc["cod_ibge6"] = nasc["cod_ibge6"].astype(str).str[:6]
    mun = pd.read_csv(dados / "censo2017_banana_familiar_ce.csv", dtype={"cod_ibge7": str})
    mun["cod_ibge6"] = mun["cod_ibge7"].str[:6]
    mun["A"] = (mun["aeronave"] > 0).astype(int)
    banana = mun["estab__total"].fillna(0)
    mun["comp"] = ((mun["A"] == 0) & (banana >= n_min)
                   & (mun["share_fam_estab"] >= limiar)).astype(int)
    mun["sem_banana"] = ((mun["A"] == 0) & (banana == 0)).astype(int)
    d = nasc.merge(mun[["cod_ibge6", "municipio", "A", "comp", "sem_banana"]], on="cod_ibge6")
    d = d[d["n_peso_valido"] > 0].copy()
    d["P"] = d["mes"].map(exposicao)
    d["H"] = (d["P"] >= 0.5).astype(int)
    d["I"] = ((d["P"] > 0) & (d["P"] < 0.5)).astype(int)
    d["Ref"] = d["ano"].between(*REF).astype(int)
    d["Seca"] = d["ano"].between(*SECA).astype(int)
    d["Pos"] = d["ano"].between(*POS).astype(int)
    d["t"] = d["ano"] * 12 + d["mes"]
    return d, mun


def estima(d: pd.DataFrame, trat: str = "A", cluster: bool = True):
    import pyfixest as pf
    x = d.copy()
    for k in ("H", "I"):
        x[f"T{k}_seca"] = x[trat] * x[k] * x["Seca"]
        x[f"T{k}_pos"] = x[trat] * x[k] * x["Pos"]
    x["mun_mes"] = x["cod_ibge6"] + "_" + x["mes"].astype(str)
    x["mun_ano"] = x["cod_ibge6"] + "_" + x["ano"].astype(str)
    fit = pf.feols("peso_medio ~ TH_pos + TH_seca + TI_pos + TI_seca | mun_mes + mun_ano + t",
                   data=x, weights="n_peso_valido",
                   vcov={"CRV1": "cod_ibge6"} if cluster else "iid")
    return fit


def amostra(d: pd.DataFrame, trat_ids: set[str] | None = None) -> pd.DataFrame:
    s = d[(d["Ref"] + d["Seca"] + d["Pos"]) == 1]
    s = s[(s["A"] == 1) | (s["comp"] == 1)]
    if trat_ids is not None:
        s = s[(s["A"] == 0) | s["cod_ibge6"].isin(trat_ids)]
    return s.copy()


def permuta(s: pd.DataFrame, n_trat: int, reps: int, rng) -> np.ndarray:
    """Placebo: sorteia n_trat municípios de COMPARAÇÃO como tratados falsos."""
    comp = s[s["A"] == 0]
    ids = comp["cod_ibge6"].unique()
    out = []
    for _ in range(reps):
        falso = set(rng.choice(ids, size=n_trat, replace=False))
        c = comp.copy()
        c["Af"] = c["cod_ibge6"].isin(falso).astype(int)
        try:
            out.append(estima(c, "Af", cluster=False).coef()["TH_pos"])
        except Exception:
            continue
    return np.array(out)


def linha(nome, fit, s, trat="A"):
    co, se = fit.coef(), fit.se()
    return {
        "especificacao": nome,
        "n_trat": s.loc[s[trat] == 1, "cod_ibge6"].nunique(),
        "n_comp": s.loc[s[trat] == 0, "cod_ibge6"].nunique(),
        "celulas": len(s),
        "nasc_trat_pos_H": int(s.loc[(s[trat] == 1) & (s["Pos"] == 1) & (s["H"] == 1), "n_peso_valido"].sum()),
        "beta_H_pos": co["TH_pos"], "ep_cluster": se["TH_pos"],
        "beta_H_seca": co["TH_seca"], "ep_seca": se["TH_seca"],
        "beta_I_pos": co["TI_pos"], "ep_I": se["TI_pos"],
    }


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dados", type=Path, required=True)
    ap.add_argument("--limiar", type=float, default=0.5)
    ap.add_argument("--n-min", type=int, default=10)
    ap.add_argument("--perm", type=int, default=999)
    a = ap.parse_args(argv)
    rng = np.random.default_rng(SEED)

    d, mun = monta(a.dados, a.limiar, a.n_min)
    print("=" * 88)
    print("RODADA 21 — DIFERENÇA TRIPLA DE CALENDÁRIO, DADO REAL — EXPLORATÓRIO, SEM CHUVA")
    print("=" * 88)
    print(f"anos no painel: {d['ano'].min()}–{d['ano'].max()} | municípios: {d['cod_ibge6'].nunique()}")
    print(f"A_m (Censo 2006): {sorted(mun.loc[mun['A'] == 1, 'municipio'])}")
    print(f"comparação (banana >= {a.n_min} estab., sem aeronave, familiar >= {a.limiar}): "
          f"{int(mun['comp'].sum())} | sem banana: {int(mun['sem_banana'].sum())}")
    print("coortes por mês de nascimento (P = fração de t-9..t-4 em fev–mai):")
    print("  " + "  ".join(f"{m}:{exposicao(m):.2f}" for m in range(1, 13)))

    linhas = []
    s = amostra(d)
    f = estima(s)
    linhas.append(linha("principal: 7 municípios do Censo 2006", f, s))
    s2 = amostra(d, CHAPADA)
    f2 = estima(s2)
    linhas.append(linha("Chapada: Limoeiro + Quixeré", f2, s2))
    s3 = amostra(d, set(mun.loc[mun["A"] == 1, "cod_ibge6"]) - CHAPADA)
    linhas.append(linha("aeronave fora da Chapada (5)", estima(s3), s3))
    s4 = s[~s["ano"].isin([2007, 2011])]
    linhas.append(linha("referência 2008–2010", estima(s4), s4))
    s5 = s[~s["ano"].isin([2020, 2021])]
    linhas.append(linha("pós sem 2020–2021 (pandemia)", estima(s5), s5))

    # tratamento falso: banana familiar x sem banana
    pl = d[((d["Ref"] + d["Seca"] + d["Pos"]) == 1) & ((d["comp"] == 1) | (d["sem_banana"] == 1))].copy()
    if pl["sem_banana"].sum() > 0 and pl["comp"].sum() > 0:
        linhas.append(linha("FALSO: banana familiar x sem banana", estima(pl, "comp"), pl, "comp"))

    # sensibilidade ao limiar
    for lim, nmin in ((0.75, 10), (0.5, 50), (0.0, 10)):
        dd, _ = monta(a.dados, lim, nmin)
        ss = amostra(dd)
        linhas.append(linha(f"limiar familiar {lim}, >= {nmin} estab.", estima(ss), ss))

    tab = pd.DataFrame(linhas)
    pd.set_option("display.width", 250)
    print("\n" + tab.round(2).to_string(index=False))

    # inferência por permutação (placebo entre os de comparação)
    print("\nPERMUTAÇÃO (tratados falsos sorteados entre os de comparação; estatística: beta_H_pos)")
    res = []
    for nome, ss, ff in (("principal", s, f), ("Chapada", s2, f2)):
        nt = ss.loc[ss["A"] == 1, "cod_ibge6"].nunique()
        dist = permuta(ss, nt, a.perm, rng)
        assert nt == (7 if nome == "principal" else 2), f"{nome}: {nt} tratados"
        b = ff.coef()["TH_pos"]
        p = (1 + np.sum(np.abs(dist) >= abs(b))) / (1 + len(dist))
        q = np.quantile(dist, [0.025, 0.975])
        res.append({"amostra": nome, "n_trat": nt, "beta": b, "p_perm": p, "placebo_2.5%": q[0],
                    "placebo_97.5%": q[1], "dp_placebo": dist.std(), "reps": len(dist)})
        print(f"  {nome:10s} beta={b:8.2f}  p_perm={p:.3f}  placebo 95%: [{q[0]:.1f}, {q[1]:.1f}]  "
              f"dp={dist.std():.1f}  => MDE(80%, 5%) ~ {2.8 * dist.std():.0f} g")
    perm = pd.DataFrame(res)

    # estudo de evento: A x H x ano, base 2011 (inclui 2005–2006, 2012, 2019)
    import pyfixest as pf
    e = d[(d["A"] == 1) | (d["comp"] == 1)].copy()
    e["mun_mes"] = e["cod_ibge6"] + "_" + e["mes"].astype(str)
    e["mun_ano"] = e["cod_ibge6"] + "_" + e["ano"].astype(str)
    anos = [y for y in sorted(e["ano"].unique()) if y != 2011]
    for y in anos:
        e[f"ev{y}"] = e["A"] * e["H"] * (e["ano"] == y)
        e[f"iv{y}"] = e["A"] * e["I"] * (e["ano"] == y)
    rhs = " + ".join([f"ev{y}" for y in anos] + [f"iv{y}" for y in anos])
    fe = pf.feols(f"peso_medio ~ {rhs} | mun_mes + mun_ano + t", data=e,
                  weights="n_peso_valido", vcov={"CRV1": "cod_ibge6"})
    ev = pd.DataFrame({"ano": anos, "coef": [fe.coef()[f"ev{y}"] for y in anos],
                       "ep_cluster": [fe.se()[f"ev{y}"] for y in anos]})
    print("\nESTUDO DE EVENTO (A x H x ano; base 2011; erro-padrão agrupado, otimista)")
    print(ev.round(1).to_string(index=False))

    out = a.dados
    tab.to_csv(out / "expl_calendario_especificacoes.csv", index=False)
    perm.to_csv(out / "expl_calendario_permutacao.csv", index=False)
    ev.to_csv(out / "expl_calendario_evento.csv", index=False)
    print(f"\n[ok] gravado em {out} (expl_calendario_*.csv)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
