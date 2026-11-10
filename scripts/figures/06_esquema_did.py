"""F06 — Esquema da identificação: o DiD 2×2 e o que muda com dose contínua.

Figura **conceitual**, no idioma dos manuais (Angrist & Pischke, *Mostly
Harmless*, cap. 5; Cunningham, *Mixtape*, cap. 9) e de Callaway, Goodman-Bacon &
Sant'Anna (2024). Nenhum ponto é dado: as curvas são desenhadas à mão para
mostrar a LÓGICA, e a figura diz isso nela mesma.

- **(a) O DiD 2×2.** Alta dose contra `d = 0`, antes e depois do ban. O
  contrafactual tracejado é a hipótese de tendências paralelas; a distância até
  o observado é o `ATT(d|d)` — o resultado principal desde 2026-09-22.
- **(b) Por que a curva custa mais caro que o nível.** Cada grupo de dose tem a
  SUA curva de resposta. Sob tendências paralelas tradicionais identifica-se um
  ponto de cada curva, `ATT(d|d)`. Comparar esses pontos entre doses mistura o
  efeito causal de mais dose com **seleção nos ganhos** (as curvas diferem); só
  o *strong parallel trends* (uma curva só) faz da inclinação um efeito causal.

Uso:
    python scripts/figures/06_esquema_did.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _estilo as E  # noqa: E402


def desenha():
    plt = E.aplica_estilo()
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(11.2, 4.9))

    # ---------------- (a) DiD 2×2 ----------------
    t = np.array([0.0, 1.0, 2.0])  # pré, ban, pós
    controle = 2.0 + 0.55 * t
    tratado_cf = 3.3 + 0.55 * t
    tratado = tratado_cf.copy()
    tratado[2] += 0.95
    ax_a.plot(t, controle, color=E.NEUTRO, linewidth=2.2, marker="o")
    ax_a.plot(t[:2], tratado[:2], color=E.AZUL, linewidth=2.2, marker="o")
    ax_a.plot(t[1:], tratado[1:], color=E.AZUL, linewidth=2.2, marker="o")
    ax_a.plot(t[1:], tratado_cf[1:], color=E.AZUL, linewidth=1.6, linestyle=(0, (4, 3)))
    ax_a.scatter([t[2]], [tratado_cf[2]], s=40, facecolor="white", edgecolor=E.AZUL,
                 linewidth=1.4, zorder=4)
    ax_a.axvline(1, color=E.VERMELHO, linewidth=0.9, linestyle=(0, (4, 2)))
    ax_a.text(1.03, 5.75, "ban\n(09/01/2019)", color=E.VERMELHO, fontsize=8, va="top")
    ax_a.annotate("", (2.07, tratado[2]), (2.07, tratado_cf[2]),
                  arrowprops=dict(arrowstyle="<->", color=E.TINTA, linewidth=1))
    ax_a.text(2.12, (tratado[2] + tratado_cf[2]) / 2, "ATT(d | d)", va="center",
              fontsize=9.5, fontweight="bold")
    ax_a.text(2.0, tratado[2] + 0.14, "dose alta,\nobservado", color=E.AZUL, fontsize=8,
              ha="center", va="bottom")
    ax_a.text(1.55, tratado_cf[1] + 0.02, "contrafactual:\ntendência do d = 0",
              color=E.AZUL, fontsize=8, ha="center", va="top", rotation=0)
    ax_a.text(2.0, controle[2] - 0.38, "d = 0 (comparação)", color=E.CINZA, fontsize=8,
              ha="center", va="top")
    ax_a.text(0.5, (tratado[0] + controle[0]) / 2 + 0.3,
              "tendências paralelas:\nmesma inclinação\nsem o ban", fontsize=8,
              color=E.CINZA, ha="center", va="center")
    ax_a.set_xticks(t, ["pré-ban\n(2015–2018)", "", "pós-ban\n(2019–2024)"])
    ax_a.set_yticks([])
    ax_a.set_ylabel("Desfecho médio (ex.: peso ao nascer)")
    ax_a.set_xlim(-0.15, 2.75)
    ax_a.set_ylim(1.5, 5.9)
    ax_a.set_title("(a) O nível: DiD de alta dose contra d = 0")

    # ---------------- (b) dose contínua ----------------
    d = np.linspace(0, 1, 200)
    baixa = 2.2 * (1 - np.exp(-1.6 * d))      # resposta do grupo de dose baixa
    alta = 3.9 * (1 - np.exp(-2.4 * d))       # resposta do grupo de dose alta
    dl, dh = 0.3, 0.8
    f_b = lambda x: 2.2 * (1 - np.exp(-1.6 * x))  # noqa: E731
    f_a = lambda x: 3.9 * (1 - np.exp(-2.4 * x))  # noqa: E731
    ax_b.plot(d, baixa, color=E.AZUL_CLARO, linewidth=2.2)
    ax_b.plot(d, alta, color=E.AZUL, linewidth=2.2)
    ax_b.text(1.01, baixa[-1], "resposta do grupo\nde dose baixa", color="#5b93c4",
              fontsize=8, va="center")
    ax_b.text(1.01, alta[-1], "resposta do grupo\nde dose alta", color=E.AZUL, fontsize=8,
              va="center")
    ax_b.scatter([dl, dh], [f_b(dl), f_a(dh)], s=55, color=E.TINTA, zorder=5)
    ax_b.scatter([dl], [f_a(dl)], s=55, facecolor="white", edgecolor=E.TINTA,
                 linewidth=1.3, zorder=5)
    ax_b.annotate("ATT(dᴮ | dᴮ)", (dl, f_b(dl)), xytext=(8, -14),
                  textcoords="offset points", ha="left", fontsize=9, fontweight="bold")
    ax_b.annotate("ATT(dᴬ | dᴬ)", (dh, f_a(dh)), xytext=(-8, 8),
                  textcoords="offset points", ha="right", fontsize=9, fontweight="bold")
    for x in (dl, dh):
        ax_b.plot([x, x], [0, f_a(x) if x == dh else f_b(x)], color=E.GRADE,
                  linewidth=0.8, zorder=0)
    # Decomposição de CGS: ATT(dᴬ|dᴬ) − ATT(dᴮ|dᴮ) =
    #   [ATT(dᴬ|dᴬ) − ATT(dᴮ|dᴬ)]  efeito causal de mais dose, no grupo de dose alta
    # + [ATT(dᴮ|dᴬ) − ATT(dᴮ|dᴮ)]  seleção nos ganhos, avaliada em dᴮ
    xs = dh + 0.035
    ax_b.annotate("", (xs, f_a(dh)), (xs, f_a(dl)),
                  arrowprops=dict(arrowstyle="<->", color=E.TINTA, linewidth=0.9))
    ax_b.plot([dl, xs + 0.01], [f_a(dl)] * 2, color=E.NEUTRO, linewidth=0.6,
              linestyle=(0, (2, 2)))
    ax_b.text(xs + 0.015, (f_a(dh) + f_a(dl)) / 2,
              "efeito causal\nde mais dose\n(grupo de dose alta)", fontsize=7.5,
              va="center")
    ax_b.annotate("", (dl - 0.025, f_a(dl)), (dl - 0.025, f_b(dl)),
                  arrowprops=dict(arrowstyle="<->", color=E.VERMELHO, linewidth=0.9))
    ax_b.text(dl - 0.045, (f_a(dl) + f_b(dl)) / 2, "seleção\nnos ganhos",
              fontsize=7.5, va="center", ha="right", color=E.VERMELHO)
    ax_b.annotate("ATT(dᴮ | dᴬ)", (dl, f_a(dl)), xytext=(-8, 8),
                  textcoords="offset points", ha="right", fontsize=8, color=E.CINZA)
    ax_b.text(0.02, 0.97,
              "Tendências paralelas: identifica só os pontos cheios.\n"
              "Strong parallel trends: as duas curvas são uma só —\n"
              "só então a diferença entre eles é causal.",
              transform=ax_b.transAxes, va="top", fontsize=8, color=E.TINTA)
    ax_b.set_xticks([0, dl, dh], ["0", "dᴮ", "dᴬ"])
    ax_b.set_yticks([0], ["0"])
    ax_b.set_xlim(0, 1.32)
    ax_b.set_ylim(0, 4.9)
    ax_b.set_xlabel("Dose: intensidade pré-ban de exposição")
    ax_b.set_ylabel("Efeito do ban sobre o desfecho")
    ax_b.set_title("(b) A curva: por que comparar doses exige mais")

    fig.text(0.01, 0.008, "ESQUEMA CONCEITUAL — curvas ilustrativas, não são dados nem "
             "estimativas.", fontsize=7, color=E.VERMELHO)
    fig.text(0.99, 0.008, "Adaptado de Angrist & Pischke (2009, cap. 5) e Callaway, "
             "Goodman-Bacon & Sant'Anna (2024).", ha="right", fontsize=6, color=E.CINZA)
    fig.tight_layout(rect=(0, 0.03, 1, 1), w_pad=2.5)
    return fig


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out-dir", type=Path, default=E.FIG_DIR)
    args = p.parse_args(argv)
    E.grava(desenha(), "esquema_did", args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
