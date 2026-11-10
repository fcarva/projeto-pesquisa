"""F05 — Tendências brutas dos desfechos por grupo de dose (lê o painel).

Média anual, ponderada por nascimentos, de cada desfecho do SINASC em três
grupos definidos pela dose pré-ban: decil superior entre os produtores, demais
produtores e `d = 0`. É o gráfico que se olha **antes** de qualquer estimador:
os grupos andavam juntos no pré-período?

⚠️ O QUE A FIGURA NÃO É
------------------------

- **Não é estimativa.** São médias brutas, sem efeito fixo, sem inferência. O
  resultado do desenho sai de `scripts/estimate/`, não daqui.
- **Paralelismo visual não valida o SPT** (CLAUDE.md): a implicação pré-período
  é comum ao PT e ao SPT.
- **O `d = 0` é o da coluna `dose_zero` do painel** — a construção escolhida no
  `D_ZERO` do build (definição 4, GAEZ, é a primária).
- **Nascimento é datado pelo mês do parto**: o ano de 2019 mistura gestações
  expostas antes e depois do ban.

⚠️ SIMULADO NUNCA VAI PARA O PAPER. Com painel simulado a figura sai com marca
d'água em `data/processed/figuras_simulado/` (gitignored), só para validar o
código. Para `paper/figures/` é preciso o painel real (`make real`).

Uso:
    python scripts/figures/05_desfechos_tendencias.py
    python scripts/figures/05_desfechos_tendencias.py --painel data/processed/painel_ensaio1__simulado.parquet
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _estilo as E  # noqa: E402

# desfecho → (rótulo, coluna de peso, fator de escala)
DESFECHOS = {
    "peso_medio": ("Peso médio ao nascer (g)", "n_peso_valido", 1.0),
    "taxa_baixo_peso": ("Baixo peso, < 2.500 g (%)", "n_peso_valido", 100.0),
    "taxa_prematuridade": ("Prematuridade, < 37 semanas (%)", "n_gest_valido", 100.0),
}
GRUPOS = {
    "decil": ("Decil superior da dose", E.AZUL),
    "demais": ("Demais produtores", E.AZUL_CLARO),
    "zero": ("d = 0", E.NEUTRO),
}


def classifica(painel: pd.DataFrame) -> pd.Series:
    """Grupo por município: mesma conta do decil dos estimadores (ceil de 10%)."""
    muni = painel.groupby("cod_ibge6").agg(dose=("dose_ha", "first"),
                                           zero=("dose_zero", "first"))
    produtores = muni[(muni["dose"] > 0) & ~muni["zero"]]
    k = max(1, math.ceil(len(produtores) * 0.10))
    grupo = pd.Series("demais", index=muni.index)
    grupo[muni["zero"]] = "zero"
    grupo[produtores.nlargest(k, "dose").index] = "decil"
    return grupo


def medias_anuais(painel: pd.DataFrame) -> pd.DataFrame:
    """Média ponderada por ano × grupo, em formato longo."""
    p = painel.assign(grupo=painel["cod_ibge6"].map(classifica(painel)))
    linhas = []
    for col, (_, peso, fator) in DESFECHOS.items():
        if col not in p.columns:
            continue
        v = p.dropna(subset=[col, peso])
        v = v.assign(_num=v[col] * v[peso])
        g = v.groupby(["grupo", "ano"]).agg(num=("_num", "sum"), den=(peso, "sum"),
                                            n_muni=("cod_ibge6", "nunique")).reset_index()
        g["valor"] = fator * g["num"] / g["den"]
        g["desfecho"] = col
        linhas.append(g[["desfecho", "grupo", "ano", "valor", "den", "n_muni"]])
    return pd.concat(linhas, ignore_index=True)


def desenha(med: pd.DataFrame, cultura: str, simulado: bool):
    plt = E.aplica_estilo()
    cols = [c for c in DESFECHOS if c in set(med["desfecho"])]
    fig, eixos = plt.subplots(1, len(cols), figsize=(3.9 * len(cols), 4.3), squeeze=False)
    for ax, col in zip(eixos[0], cols):
        bloco = med[med["desfecho"] == col]
        for grupo, (nome, cor) in GRUPOS.items():
            g = bloco[bloco["grupo"] == grupo].sort_values("ano")
            if g.empty:
                continue
            ax.plot(g["ano"], g["valor"], color=cor, linewidth=2, marker="o",
                    markersize=3.5, label=f"{nome} ({int(g['n_muni'].max())} mun.)")
        ax.axvline(2019 + 8 / 365, color=E.VERMELHO, linewidth=0.9, linestyle=(0, (4, 2)))
        ax.grid(axis="y")
        ax.set_axisbelow(True)
        ax.set_xticks(sorted(bloco["ano"].unique())[::2])
        ax.set_title(DESFECHOS[col][0], fontsize=9)
        if simulado:
            ax.text(0.5, 0.5, "SIMULADO", transform=ax.transAxes, ha="center",
                    va="center", fontsize=30, color="#d9d9d9", rotation=25, zorder=0)
    eixos[0][0].text(2019.15, 0.03, "ban", transform=eixos[0][0].get_xaxis_transform(),
                     fontsize=7.5, color=E.VERMELHO)
    alcas, rotulos = eixos[0][0].get_legend_handles_labels()
    fig.legend(alcas, rotulos, loc="lower left", bbox_to_anchor=(0.03, 0.02), ncol=3,
               fontsize=8)
    fig.suptitle(f"Desfechos de nascimento por grupo de dose ({cultura}) — médias anuais "
                 "brutas, ponderadas por nascimentos", x=0.01, ha="left", fontsize=10.5)
    fig.text(0.99, 0.008, "Fonte: SINASC/DATASUS e PAM/IBGE, via painel do Ensaio 1. "
             "Médias brutas, sem contrafactual.", ha="right", fontsize=6, color=E.CINZA)
    fig.tight_layout(rect=(0, 0.09, 1, 0.94))
    return fig


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--painel", type=Path, default=E.PROCESSED / "painel_ensaio1.parquet")
    p.add_argument("--out-dir", type=Path, default=None,
                   help="Padrão: paper/figures/ (real) ou "
                        "data/processed/figuras_simulado/ (simulado).")
    args = p.parse_args(argv)
    if not args.painel.exists():
        print(f"[erro] painel não encontrado: {args.painel}\n"
              "       Rode `make real CULTURA=...` (ou passe --painel com o simulado).")
        return 1
    painel = pd.read_parquet(args.painel)
    # A proveniência é a coluna `fonte` DENTRO do arquivo, não o nome dele.
    fontes = set(painel["fonte"].astype(str).unique()) if "fonte" in painel else {"?"}
    simulado = fontes != {"real"} and any("simul" in f or f == "?" for f in fontes)
    cultura = str(painel["cultura_ancora"].iloc[0])
    med = medias_anuais(painel)
    out = args.out_dir or (E.PROCESSED / "figuras_simulado" if simulado else E.FIG_DIR)
    if simulado:
        print("⚠️ painel SIMULADO: figura com marca d'água, fora de paper/figures/.")
        if out.resolve() == E.FIG_DIR.resolve():
            print("[erro] figura simulada não é gravada em paper/figures/.")
            return 1
    E.grava(desenha(med, cultura, simulado),
            f"desfechos_tendencias__{E.slug(cultura)}", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
