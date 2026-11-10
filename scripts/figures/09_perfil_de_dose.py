"""F09 — Perfil de dose: a variação do desfecho, antes → depois, por faixa de dose.

O gráfico de "médias por faixa" que os artigos aplicados mostram antes da
regressão: para cada faixa de dose (zero e tercis dos positivos), a variação
média do desfecho entre o pré e o pós-ban, com intervalo de 95%. Se o ban tem
efeito crescente na dose, os pontos sobem (ou descem) da esquerda para a
direita; `d = 0` é a referência.

A figura **não calcula nada**: lê `robustez_perfil_dose.csv`, gravado por
`scripts/estimate/04_robustness.py`, e a proveniência em
`robustez_inferencia.csv` (coluna `fonte`).

⚠️ O QUE A FIGURA NÃO É
------------------------

- **Não é a curva dose-resposta de CGS** — é média bruta por faixa, e a
  inclinação entre faixas só é causal sob *strong parallel trends* (F06).
- **O intervalo é ingênuo** (erro-padrão da média por faixa): a inferência do
  paper é por Conley–Taber / wild bootstrap.
- **SIMULADO NUNCA VAI PARA O PAPER**: com `fonte` simulada ou ausente, a figura
  sai com marca d'água em `data/processed/figuras_simulado/`.

Uso:
    python scripts/figures/09_perfil_de_dose.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _estilo as E  # noqa: E402

ROTULO_DESFECHO = {
    "peso_medio": "peso médio ao nascer (g)",
    "taxa_baixo_peso": "taxa de baixo peso",
    "taxa_prematuridade": "taxa de prematuridade",
}


def e_simulado(inferencia: Path) -> bool:
    """Real só com prova: sem o arquivo de proveniência, trata como simulado."""
    if not inferencia.exists():
        return True
    fontes = set(pd.read_csv(inferencia)["fonte"].astype(str).str.lower())
    return not fontes or any("simul" in f or f in ("nan", "") for f in fontes)


def desenha(perfil: pd.DataFrame, simulado: bool):
    plt = E.aplica_estilo()
    desfecho = str(perfil["desfecho"].iloc[0])
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    x = range(len(perfil))
    cores = [E.NEUTRO if "= 0" in f else E.AZUL for f in perfil["faixa"]]
    if simulado:
        ax.text(0.5, 0.5, "SIMULADO", transform=ax.transAxes, ha="center", va="center",
                fontsize=44, color="#dedede", rotation=20, zorder=0)
    ax.axhline(0, color=E.NEUTRO, linewidth=0.7)
    for xi, (_, r), cor in zip(x, perfil.iterrows(), cores):
        ax.errorbar(xi, r["dy_medio"], yerr=1.96 * r["ep"], color=cor, marker="o",
                    markersize=7, linewidth=1.6, capsize=4, zorder=3)
        ax.annotate(f"{r['dy_medio']:+.1f}".replace(".", ","), (xi, r["dy_medio"]),
                    xytext=(9, 0), textcoords="offset points", va="center", fontsize=8)
    ax.set_xticks(list(x), [f"{f}\n(n = {int(n)})" for f, n in
                            zip(perfil["faixa"], perfil["n"])], fontsize=8)
    ax.set_xlim(-0.5, len(perfil) - 0.4)
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.set_ylabel(f"Variação pré → pós-ban: {ROTULO_DESFECHO.get(desfecho, desfecho)}")
    ax.set_title("Variação do desfecho por faixa de dose (média e IC de 95%)")
    fig.text(0.99, 0.008, "Fonte: robustez_perfil_dose.csv (scripts/estimate/04_robustness.py). "
             "Médias brutas por município; IC ingênuo.", ha="right", fontsize=6,
             color=E.CINZA)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    return fig


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--perfil", type=Path, default=E.PROCESSED / "robustez_perfil_dose.csv")
    p.add_argument("--inferencia", type=Path,
                   default=E.PROCESSED / "robustez_inferencia.csv",
                   help="De onde sai a proveniência (coluna `fonte`).")
    p.add_argument("--out-dir", type=Path, default=None)
    args = p.parse_args(argv)
    if not args.perfil.exists():
        print(f"[erro] {args.perfil} não existe: rode scripts/estimate/04_robustness.py")
        return 1
    perfil = pd.read_csv(args.perfil)
    simulado = e_simulado(args.inferencia)
    out = args.out_dir or (E.PROCESSED / "figuras_simulado" if simulado else E.FIG_DIR)
    if simulado:
        print("⚠️ perfil SIMULADO (ou sem proveniência): marca d'água, fora de paper/figures/.")
        if out.resolve() == E.FIG_DIR.resolve():
            print("[erro] figura simulada não é gravada em paper/figures/.")
            return 1
    for desfecho, bloco in perfil.groupby("desfecho", sort=False):
        E.grava(desenha(bloco.reset_index(drop=True), simulado),
                f"perfil_de_dose__{E.slug(str(desfecho))}", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
