"""Rodada 21 — leads e lags (estudo de evento) da diferença tripla. EXPLORATÓRIO.

⚠️ Dado real; autorizado pelo pesquisador em 2026-11-15; nada entra em
`paper/projeto/`. Sem controle de chuva. Estação fev–mai e A_m do Censo 2006
são hipóteses provisórias.

Fundamento (Cunningham, cap. 9 "Difference-in-Differences", seções "Event
Studies", "Falsifications", "Inference" e "Medicaid and Mortality" — lido em
mixtape.scunning.com em 2026-11-15):
  - regressão com q leads e m lags do tratamento, omitido o período t = -1
    ("we want to impose no anticipation");
  - cada LEAD mede a tendência diferencial de Y(0) entre os grupos antes da
    política — evidência indireta: "the parallel trends assumption cannot be
    tested because it involves a non-existent counterfactual";
  - cada LAG estima o efeito naquela data, se houver tendências paralelas a
    partir da base e não houver antecipação;
  - falsificações: "same outcome, alternative group" e "same group,
    alternative outcome";
  - com poucos tratados, o agrupamento falha; inferência por aleatorização
    (Buchmueller, DiNardo e Valletta, 2011).

Aqui o "tratamento" do estudo de evento é A_m × H_t (município com avião ×
coorte de exposição alta); os coeficientes são A × H × ano. Duas bases:
  2018 — t = -1 da lei (vigência 09/01/2019): a convenção do livro;
  2014 — último ano antes da NOTÍCIA (PL 18/2015, 24/02/2015): se houve
         antecipação, 2015–2018 já são "lags" e 2018 é base contaminada.
(O projeto usa 2011 por causa da seca; ver 21_calendario_exploratorio.py.)

Inferência: bandas e testes por permutação — tratados falsos sorteados entre
os municípios de comparação. Teste conjunto dos leads: soma dos quadrados dos
coeficientes pré contra a distribuição placebo.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
AQUI = Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location("cal21", AQUI / "21_calendario_exploratorio.py")
cal = importlib.util.module_from_spec(_s)
_s.loader.exec_module(cal)
_s2 = importlib.util.spec_from_file_location("fr22", AQUI / "22_fronteira_rn_exploratorio.py")
fr = importlib.util.module_from_spec(_s2)
_s2.loader.exec_module(fr)


def evento(d: pd.DataFrame, base: int, y: str = "peso_medio", w: str = "n_peso_valido",
           trat: str = "A") -> pd.Series:
    """Coeficientes A × H × ano (base omitida), com A × I × ano como controle."""
    import pyfixest as pf
    x = d.copy()
    anos = [a for a in sorted(x["ano"].unique()) if a != base]
    for a in anos:
        x[f"ev{a}"] = x[trat] * x["H"] * (x["ano"] == a)
        x[f"iv{a}"] = x[trat] * x["I"] * (x["ano"] == a)
    x["mun_mes"] = x["cod_ibge6"] + "_" + x["mes"].astype(str)
    x["mun_ano"] = x["cod_ibge6"] + "_" + x["ano"].astype(str)
    rhs = " + ".join([f"ev{a}" for a in anos] + [f"iv{a}" for a in anos])
    f = pf.feols(f"{y} ~ {rhs} | mun_mes + mun_ano + t", data=x, weights=w, vcov="iid")
    c = f.coef()
    return pd.Series({a: c[f"ev{a}"] for a in anos})


def roda(nome: str, d: pd.DataFrame, base: int, reps: int, rng, y="peso_medio",
         w="n_peso_valido") -> pd.DataFrame:
    d = d[d[w] > 0].dropna(subset=[y])
    real = evento(d, base, y, w)
    comp = d[d["A"] == 0]
    ids = comp["cod_ibge6"].unique()
    nt = d.loc[d["A"] == 1, "cod_ibge6"].nunique()
    plc = []
    for _ in range(reps):
        falso = set(rng.choice(ids, size=nt, replace=False))
        c = comp.assign(Af=comp["cod_ibge6"].isin(falso).astype(int))
        try:
            plc.append(evento(c, base, y, w, "Af"))
        except Exception:
            continue
    P = pd.DataFrame(plc)
    out = pd.DataFrame({"ano": real.index, "coef": real.values})
    out["tempo_evento"] = out["ano"] - 2019
    out["tipo"] = np.where(out["ano"] < 2019, "lead", "lag")
    out["plc_2.5"] = P.quantile(0.025).values
    out["plc_97.5"] = P.quantile(0.975).values
    out["p_perm"] = [(1 + (P[a].abs() >= abs(real[a])).sum()) / (1 + len(P)) for a in real.index]
    leads = [a for a in real.index if a < 2019]
    lags = [a for a in real.index if a >= 2020]
    def conj(cols):
        est = float((real[cols] ** 2).sum())
        return (1 + ((P[cols] ** 2).sum(axis=1) >= est).sum()) / (1 + len(P))
    def media(cols):
        est = float(real[cols].mean())
        return est, (1 + (P[cols].mean(axis=1).abs() >= abs(est)).sum()) / (1 + len(P))
    m_lag, p_lag = media(lags)
    m_lead, p_lead = media(leads)
    out.attrs = {"nome": nome, "base": base, "desfecho": y, "n_trat": nt, "n_comp": len(ids),
                 "reps": len(P), "p_leads_conjunto": conj(leads), "p_lags_conjunto": conj(lags),
                 "media_leads": m_lead, "p_media_leads": p_lead,
                 "media_lags": m_lag, "p_media_lags": p_lag}
    return out


def figura(res: list[pd.DataFrame], destino: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(len(res), 1, figsize=(8.5, 3.1 * len(res)), sharex=True)
    for ax, r in zip(np.atleast_1d(axs), res):
        a = r.attrs
        ax.axhline(0, color="0.4", lw=0.8)
        ax.axvline(2018.5, color="0.4", lw=0.8, ls="--")
        ax.axvspan(2011.5, 2018.5, color="0.92", zorder=0)
        # hastes desconectadas: faixa placebo de 95% em torno de zero + ponto
        ax.vlines(r["ano"], r["plc_2.5"], r["plc_97.5"], color="0.65", lw=5, alpha=0.7)
        ax.plot(r["ano"], r["coef"], "o", color="black", ms=4.5)
        ax.plot([a["base"]], [0], "o", mfc="white", mec="black", ms=5)
        ax.set_title(f"{a['nome']} — base {a['base']}; {a['n_trat']} tratados; "
                     f"leads p={a['p_leads_conjunto']:.2f}, lags p={a['p_lags_conjunto']:.2f}",
                     fontsize=9, loc="left")
        ax.set_ylabel("g")
    np.atleast_1d(axs)[-1].set_xlabel("ano de nascimento (cinza: seca 2012–2018; tracejado: lei)")
    np.atleast_1d(axs)[-1].set_xticks(range(2005, 2025, 2))
    fig.suptitle("EXPLORATÓRIO — A × H × ano; barras: placebos (95%), não IC", fontsize=10)
    fig.tight_layout()
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, dpi=150)


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dados", type=Path, required=True)
    ap.add_argument("--dados-rn", type=Path, required=True)
    ap.add_argument("--perm", type=int, default=499)
    ap.add_argument("--fig", type=Path, default=Path("docs/ars/rodada21-local/fig/leads_lags_exploratorio.png"))
    a = ap.parse_args(argv)
    rng = np.random.default_rng(cal.SEED)

    # --- amostras (todos os anos 2005–2024: leads e lags precisam de 2012 e 2019)
    d, mun = cal.monta(a.dados, 0.5, 10)
    ce = d[(d["A"] == 1) | (d["comp"] == 1)].copy()
    ce_chap = ce[(ce["A"] == 0) | ce["cod_ibge6"].isin(cal.CHAPADA)].copy()

    n = pd.read_parquet(a.dados / "nascimentos_ce_muni_mes__uf23-24.parquet")
    n["cod_ibge6"] = n["cod_ibge6"].astype(str).str[:6]
    n = n.groupby(["cod_ibge6", "ano", "mes"], as_index=False).first()
    rn = pd.read_csv(a.dados_rn / "censo2017_banana_familiar_ce.csv", dtype={"cod_ibge7": str})
    rn["nome"] = rn["municipio"].str.replace(" - RN", "", regex=False)
    ids_rn = set(rn.loc[rn["nome"].isin(sum(fr.GRUPOS.values(), [])), "cod_ibge7"].str[:6])
    n["P"] = n["mes"].map(cal.exposicao)
    n["H"] = (n["P"] >= 0.5).astype(int)
    n["I"] = ((n["P"] > 0) & (n["P"] < 0.5)).astype(int)
    n["t"] = n["ano"] * 12 + n["mes"]
    n["A"] = n["cod_ibge6"].isin(cal.CHAPADA).astype(int)
    front = n[(n["A"] == 1) | n["cod_ibge6"].isin(ids_rn)].copy()
    # reservatório de placebos da fronteira: metade maior do RN
    rn_all = n[n["cod_ibge6"].str.startswith("24")]
    porte = rn_all.groupby("cod_ibge6")["n_peso_valido"].sum()
    front_rn = pd.concat([n[n["A"] == 1], rn_all[rn_all["cod_ibge6"].isin(porte[porte >= porte.median()].index)]])

    rodadas = [
        ("CE: 7 do Censo 2006 x banana familiar", ce, 2018, "peso_medio", "n_peso_valido"),
        ("CE: Chapada x banana familiar", ce_chap, 2018, "peso_medio", "n_peso_valido"),
        ("Fronteira: Chapada x RN (metade maior)", front_rn, 2018, "peso_medio", "n_peso_valido"),
        ("CE: Chapada x banana familiar", ce_chap, 2014, "peso_medio", "n_peso_valido"),
        ("Fronteira: Chapada x RN (metade maior)", front_rn, 2014, "peso_medio", "n_peso_valido"),
        ("FALSIFICAÇÃO (outro desfecho: idade da mãe) CE: Chapada", ce_chap, 2018, "idade_mae_media", "n_idade_valido"),
    ]
    res, resumo = [], []
    print("=" * 92)
    print("RODADA 21 — LEADS E LAGS DA DIFERENÇA TRIPLA (A × H × ano) — EXPLORATÓRIO, SEM CHUVA")
    print("=" * 92)
    for nome, dd, base, y, w in rodadas:
        r = roda(nome, dd, base, a.perm, rng, y, w)
        res.append(r)
        at = r.attrs
        resumo.append(at)
        print(f"\n{nome} | base {base} | desfecho {y} | {at['n_trat']} tratados x {at['n_comp']} | {at['reps']} permutações")
        print(r[["ano", "tempo_evento", "tipo", "coef", "plc_2.5", "plc_97.5", "p_perm"]].round(2).to_string(index=False))
        print(f"  leads: média {at['media_leads']:.1f} (p={at['p_media_leads']:.2f}); teste conjunto p={at['p_leads_conjunto']:.2f}")
        print(f"  lags 2020–2024: média {at['media_lags']:.1f} (p={at['p_media_lags']:.2f}); teste conjunto p={at['p_lags_conjunto']:.2f}")
        r.assign(especificacao=nome, base=base, desfecho=y).to_csv(
            a.dados / f"expl_leads_lags__{len(res)}.csv", index=False)
    pd.DataFrame(resumo).to_csv(a.dados / "expl_leads_lags_resumo.csv", index=False)
    figura(res[:3], a.fig)
    print(f"\n[ok] figura: {a.fig}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
