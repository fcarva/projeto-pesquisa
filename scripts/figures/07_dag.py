"""F07 — DAG da identificação: o caminho causal, o que a dose mede e as ameaças.

Figura **conceitual**, no idioma de Cunningham (*Mixtape*, cap. 3): nós são
variáveis, setas são efeitos diretos supostos. Não é resultado — é o mapa do
que o desenho precisa supor, com cada ameaça ancorada numa flag do `CLAUDE.md`.

Como ler:
- **Caminho de interesse (azul):** ban × pós → pulverização aérea → exposição
  materna → desfecho ao nascer.
- **O que se observa no lugar do método (laranja):** a dose é ÁREA da cultura,
  um proxy do método aéreo — a seta dose → pulverização é o VPP (flag 7).
- **Ameaças (tracejado):** antecipação morde a dose (PL 2015); substituição
  aéreo → terrestre devolve exposição (canal SIH/SINAN); confundidores de onde
  se planta; seleção para nascimento vivo (flag 6) — condicionar em "nasceu
  vivo" abre caminho entre exposição e saúde fetal latente.
- **Instrumento (verde):** aptidão FAO-GAEZ desloca onde se planta.

⚠️ Um DAG é hipótese desenhada. Seta ausente é suposição tão forte quanto seta
presente — em particular, a exclusão do GAEZ (sem seta direta até o desfecho).

Uso:
    python scripts/figures/07_dag.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _estilo as E  # noqa: E402

VERDE = "#2e7d4f"

# nome → (x, y, rótulo, cor da borda, estilo)
NOS = {
    "gaez": (0.8, 3.0, "Aptidão\nFAO-GAEZ", VERDE, "obs"),
    "dose": (3.3, 3.0, "Dose: área da\ncultura (PAM\n2015–2018)", E.LARANJA, "obs"),
    "aereo": (5.9, 3.0, "Pulverização\naérea\n(método)", E.AZUL, "latente"),
    "expo": (8.5, 3.0, "Exposição\nmaterna", E.AZUL, "latente"),
    "y": (11.1, 3.0, "Desfecho ao\nnascer (SINASC)", E.AZUL, "obs"),
    "ban": (5.9, 5.0, "Ban × pós-2019\n(Lei 16.820)", E.VERMELHO, "obs"),
    "pl": (3.3, 5.0, "Notícia do PL\n(24/02/2015)", E.CINZA, "obs"),
    "terra": (8.5, 5.0, "Aplicação\nterrestre", E.CINZA, "latente"),
    "u": (3.3, 0.9, "Confundidores:\nrenda, irrigação,\nserviços de saúde", E.CINZA, "latente"),
    "fetal": (8.5, 0.9, "Óbito fetal\n(SIM)", E.CINZA, "obs"),
    "vivo": (11.1, 0.9, "Nasceu vivo\n(condição de\nentrar no SINASC)", E.TINTA, "condicionado"),
    "saude": (13.2, 1.95, "Saúde fetal\nlatente", E.CINZA, "latente"),
}
# (origem, destino, cor, tracejado, rótulo, curvatura)
SETAS = (
    ("ban", "aereo", E.AZUL, False, "", 0),
    ("aereo", "expo", E.AZUL, False, "", 0),
    ("expo", "y", E.AZUL, False, "", 0),
    ("dose", "aereo", E.LARANJA, False, "VPP\n(flag 7)", 0),
    ("gaez", "dose", VERDE, False, "1º estágio", 0),
    ("pl", "dose", E.CINZA, True, "antecipação", 0),
    ("ban", "terra", E.CINZA, True, "substituição", 0),
    ("terra", "expo", E.CINZA, True, "", 0),
    ("u", "dose", E.CINZA, True, "", 0),
    ("u", "y", E.CINZA, True, "", 0),
    ("expo", "fetal", E.CINZA, True, "", 0),
    ("fetal", "vivo", E.CINZA, True, "seleção\n(flag 6)", 0),
    ("saude", "vivo", E.CINZA, True, "", 0),
    ("saude", "y", E.CINZA, True, "", 0),
)
LARG, ALT = 1.6, 0.95


def desenha():
    plt = E.aplica_estilo()
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

    fig, ax = plt.subplots(figsize=(11.2, 5.4))
    caixas = {}
    for nome, (x, y, rot, cor, estilo) in NOS.items():
        caixa = FancyBboxPatch(
            (x - LARG / 2, y - ALT / 2), LARG, ALT,
            boxstyle="round,pad=0.02,rounding_size=0.12" if estilo != "condicionado"
            else "square,pad=0.02",
            facecolor="white" if estilo != "condicionado" else "#f1f1f1",
            edgecolor=cor, linewidth=1.5 if estilo != "latente" else 1.1,
            linestyle="-" if estilo != "latente" else (0, (3, 2)), zorder=3)
        ax.add_patch(caixa)
        caixas[nome] = caixa
        ax.text(x, y, rot, ha="center", va="center", fontsize=8, color=E.TINTA, zorder=4)
    for a, b, cor, tracejado, rot, curva in SETAS:
        seta = FancyArrowPatch(
            NOS[a][:2], NOS[b][:2], patchA=caixas[a], patchB=caixas[b],
            arrowstyle="-|>", mutation_scale=11, color=cor,
            linewidth=1.8 if not tracejado else 1.0,
            linestyle="-" if not tracejado else (0, (4, 2.5)),
            connectionstyle=f"arc3,rad={curva}", shrinkA=2, shrinkB=2, zorder=2)
        ax.add_patch(seta)
        if rot:
            (xa, ya), (xb, yb) = NOS[a][:2], NOS[b][:2]
            vertical = abs(xa - xb) < 0.1
            ax.text((xa + xb) / 2 + (0.1 if vertical else 0),
                    (ya + yb) / 2 + (0 if vertical else 0.1), rot, fontsize=7,
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.6, alpha=0.9),
                    color=cor if cor != E.CINZA else E.CINZA,
                    ha="left" if vertical else "center",
                    va="center" if vertical else "bottom", zorder=4)

    legenda = [
        ("-", E.AZUL, 1.8, "caminho de interesse"),
        ("-", E.LARANJA, 1.8, "proxy observado do tratamento"),
        ("-", VERDE, 1.8, "instrumento"),
        ((0, (4, 2.5)), E.CINZA, 1.0, "ameaça à identificação"),
    ]
    from matplotlib.lines import Line2D

    itens = [Line2D([], [], color=c, linewidth=w, linestyle=ls, label=r)
             for ls, c, w, r in legenda]
    itens.append(FancyBboxPatch((0, 0), 1, 1, facecolor="white", edgecolor=E.CINZA,
                                linestyle=(0, (3, 2)), label="variável não observada"))
    itens.append(FancyBboxPatch((0, 0), 1, 1, facecolor="#f1f1f1", edgecolor=E.TINTA,
                                label="condicionada pela amostra"))
    ax.legend(handles=itens, loc="upper right", bbox_to_anchor=(1.0, 1.0), fontsize=7.5,
              ncol=1)
    ax.set_xlim(-0.2, 14.2)
    ax.set_ylim(0.1, 5.8)
    ax.axis("off")
    ax.set_title("O que o desenho supõe: caminho causal, medida do tratamento e ameaças",
                 loc="left")
    fig.text(0.01, 0.01, "ESQUEMA CONCEITUAL — hipóteses do desenho, não resultado.",
             fontsize=7, color=E.VERMELHO)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    return fig


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out-dir", type=Path, default=E.FIG_DIR)
    args = p.parse_args(argv)
    E.grava(desenha(), "dag_identificacao", args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
