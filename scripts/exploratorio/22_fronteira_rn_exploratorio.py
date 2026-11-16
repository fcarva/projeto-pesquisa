"""Rodada 21 — Chapada do Apodi: CE (sob a lei) x RN (sem a lei). EXPLORATÓRIO.

⚠️ Mesmas ressalvas do script 21: dado real, autorizado pelo pesquisador em
2026-11-15, nenhum número entra em `paper/projeto/`; sem controle de chuva;
estação = fev–mai por hipótese.

Lógica de avaliação de política: o grupo de comparação ideal é o que teria a
mesma trajetória na ausência da lei. Os vizinhos potiguares partilham aquífero,
clima, seca, mercado de fruta e empresas; não partilham a lei. Em diferença
simples isso não basta — tudo que é estadual muda junto na divisa. Na diferença
TRIPLA de calendário, os efeitos fixos de município × ano absorvem qualquer
choque estadual comum às coortes de um ano; resta supor que o HIATO SAZONAL
teria evoluído igual nos dois lados.

⚠️ O que o RN não é: grupo "com avião e sem lei". O Censo Agro 2006 registra
aeronave no RN só em Januário Cicco e São Miguel — nenhum na Chapada potiguar.
Se o lado potiguar não voava, a comparação mede "lei onde havia avião" contra
"vizinho parecido sem avião", que é o contraste do projeto, e não um placebo.
E vazamento (migração do serviço aéreo para o RN após 2019) enviesaria para
cima — SUTVA é hipótese aqui, não fato.

Grupos de comparação (por nome, no Censo 2017):
  chapada_rn : polo contíguo de fruticultura (Baraúna, Apodi, Mossoró, Upanema,
               Felipe Guerra, Governador Dix-Sept Rosado, Tibau)
  acu_rn     : banana irrigada do Vale do Açu (Ipanguaçu, Assú, Alto do
               Rodrigues, Carnaubais) — mesma cultura, outra bacia
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
spec = importlib.util.spec_from_file_location("cal21", AQUI / "21_calendario_exploratorio.py")
cal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cal)

GRUPOS = {
    "chapada_rn": ["Baraúna", "Apodi", "Mossoró", "Upanema", "Felipe Guerra",
                   "Governador Dix-Sept Rosado", "Tibau"],
    "acu_rn": ["Ipanguaçu", "Assú", "Alto do Rodrigues", "Carnaubais"],
}


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dados", type=Path, required=True)
    ap.add_argument("--dados-rn", type=Path, required=True)
    ap.add_argument("--perm", type=int, default=999)
    a = ap.parse_args(argv)
    rng = np.random.default_rng(cal.SEED)

    n = pd.read_parquet(a.dados / "nascimentos_ce_muni_mes__uf23-24.parquet")
    n["cod_ibge6"] = n["cod_ibge6"].astype(str).str[:6]
    n = n[n["n_peso_valido"] > 0].copy()
    rn = pd.read_csv(a.dados_rn / "censo2017_banana_familiar_ce.csv", dtype={"cod_ibge7": str})
    rn["nome"] = rn["municipio"].str.replace(" - RN", "", regex=False)
    rn["cod_ibge6"] = rn["cod_ibge7"].str[:6]

    n["P"] = n["mes"].map(cal.exposicao)
    n["H"] = (n["P"] >= 0.5).astype(int)
    n["I"] = ((n["P"] > 0) & (n["P"] < 0.5)).astype(int)
    n["Ref"] = n["ano"].between(*cal.REF).astype(int)
    n["Seca"] = n["ano"].between(*cal.SECA).astype(int)
    n["Pos"] = n["ano"].between(*cal.POS).astype(int)
    n["t"] = n["ano"] * 12 + n["mes"]
    n = n[(n["Ref"] + n["Seca"] + n["Pos"]) == 1]
    n["A"] = n["cod_ibge6"].isin(cal.CHAPADA).astype(int)

    print("=" * 88)
    print("RODADA 21 — FRONTEIRA CE x RN, DIFERENÇA TRIPLA DE CALENDÁRIO — EXPLORATÓRIO")
    print("=" * 88)
    linhas = []
    todos_rn = set()
    for g, nomes in GRUPOS.items():
        ids = set(rn.loc[rn["nome"].isin(nomes), "cod_ibge6"])
        faltou = sorted(set(nomes) - set(rn.loc[rn["nome"].isin(nomes), "nome"]))
        if faltou:
            print(f"[aviso] {g}: não achei {faltou}")
        todos_rn |= ids
        s = n[(n["A"] == 1) | n["cod_ibge6"].isin(ids)].copy()
        f = cal.estima(s)
        r = cal.linha(f"Limoeiro+Quixeré x {g}", f, s)
        r["nasc_mes_comp"] = s.loc[s["A"] == 0].groupby(["ano", "mes"])["n_peso_valido"].sum().mean()
        linhas.append(r)
    s = n[(n["A"] == 1) | n["cod_ibge6"].isin(todos_rn)].copy()
    linhas.append(cal.linha("Limoeiro+Quixeré x os dois grupos do RN", cal.estima(s), s))
    s_sem = s[s["cod_ibge6"] != rn.loc[rn["nome"] == "Mossoró", "cod_ibge6"].iloc[0]]
    linhas.append(cal.linha("idem, sem Mossoró", cal.estima(s_sem), s_sem))

    # todo o RN como reservatório de placebos: o hiato sazonal de 2 municípios
    # potiguares sorteados reage "à lei cearense"?
    rn_all = n[n["cod_ibge6"].str.startswith("24")].copy()
    porte = rn_all.groupby("cod_ibge6")["n_peso_valido"].sum()
    rn_all = rn_all[rn_all["cod_ibge6"].isin(porte[porte >= porte.quantile(0.5)].index)]
    s_rn = pd.concat([n[n["A"] == 1], rn_all])
    f_rn = cal.estima(s_rn)
    linhas.append(cal.linha("Limoeiro+Quixeré x RN (metade maior)", f_rn, s_rn))
    dist = cal.permuta(s_rn, 2, a.perm, rng)
    b = f_rn.coef()["TH_pos"]
    p = (1 + np.sum(np.abs(dist) >= abs(b))) / (1 + len(dist))

    tab = pd.DataFrame(linhas)
    pd.set_option("display.width", 250)
    print(tab.round(2).to_string(index=False))
    q = np.quantile(dist, [0.025, 0.975])
    print(f"\nPERMUTAÇÃO no RN (2 tratados falsos entre municípios potiguares): beta={b:.2f}  "
          f"p_perm={p:.3f}  placebo 95%: [{q[0]:.1f}, {q[1]:.1f}]  dp={dist.std():.1f}  "
          f"=> MDE(80%, 5%) ~ {2.8 * dist.std():.0f} g")
    tab.to_csv(a.dados / "expl_fronteira_rn.csv", index=False)
    print(f"[ok] {a.dados / 'expl_fronteira_rn.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
