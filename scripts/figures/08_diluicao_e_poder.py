"""F08 — Diluição e poder: o que um coeficiente pequeno implica, e o que o desenho enxerga.

Toda a conta vem de `scripts/estimate/12_erro_de_classificacao.py` — esta figura
só desenha as funções e constantes de lá (`limite_corolario1`,
`poder_aproximado`, `sinal_esperado`, `CENARIOS_VPP`, `COEFICIENTES_PAPER`,
`MDE_G`). Mudou lá, muda aqui.

- **(a) Corolário 1 de Denteh & Kédagni: `ATT = θ / VPP`.** Sob tendências
  paralelas no tratamento observado e sem falso negativo, o coeficiente θ é o
  ATT atenuado pelo VPP. A faixa são os coeficientes já reportados na §6; as
  verticais, os cenários de VPP do script 12.
- **(b) Curva de poder do desenho.** Poder de um teste z bilateral contra um
  efeito verdadeiro θ, com o erro-padrão implícito no MDE. As faixas marcam o θ
  ESPERADO (`VPP · f · δ`) sob o VPP do Censo e sob "dose é tratamento".

⚠️ CALIBRAÇÃO, NÃO CORREÇÃO
----------------------------

- O painel (a) **não** estima o ATT: diz o que cada θ implicaria SE o VPP fosse
  aquele. O VPP é de 2006 e pode não valer em 2018 (flag 7).
- Os coeficientes da faixa **não são achados** — nenhum é confirmatório (§6 da
  pré-especificação) e todos ficam abaixo do MDE.
- `δ` = 80–150 g vem do RESUMO de Calzada, Gisbert & Moscoso (2023); `f` é
  grade, não estimativa.
- O poder é aproximação de ordem de grandeza: a inferência do paper é por
  Conley–Taber / wild bootstrap.

Uso:
    python scripts/figures/08_diluicao_e_poder.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _estilo as E  # noqa: E402

ROTULOS_VPP = {
    "censo2006": "Censo 2006\n(2 de 17)",
    "teto_geografico": "teto geográfico\n(6 de 17)",
    "dose_e_tratamento": "dose é\ntratamento",
}


def desenha(e12):
    plt = E.aplica_estilo()
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(11.2, 5.0))
    coefs = [abs(v) for v in e12.COEFICIENTES_PAPER.values()]
    th_min, th_max = min(coefs), max(coefs)
    d_min, d_max = e12.EFEITOS_INDIVIDUAIS_G

    # ---------------- (a) ATT = θ / VPP ----------------
    vpp = np.linspace(0.05, 1, 400)
    att_min = np.array([abs(e12.limite_corolario1(-th_min, v)[0]) for v in vpp])
    att_max = np.array([abs(e12.limite_corolario1(-th_max, v)[0]) for v in vpp])
    ax_a.fill_between(vpp, att_min, att_max, color=E.AZUL_CLARO, alpha=0.55, linewidth=0)
    ax_a.plot(vpp, att_min, color=E.AZUL, linewidth=1.2)
    ax_a.plot(vpp, att_max, color=E.AZUL, linewidth=1.2)
    ax_a.axhspan(d_min, d_max, color="#f3e3cc", zorder=0)
    ax_a.text(0.985, (d_min * d_max) ** 0.5, f"δ: {d_min:.0f}–{d_max:.0f} g, efeito individual\n"
              "sob exposição alta (Calzada et al. 2023)", ha="right", va="center",
              fontsize=7.5, color="#8a5a12")
    for nome, rot in ROTULOS_VPP.items():
        v = e12.CENARIOS_VPP[nome]
        ax_a.axvline(v, color=E.NEUTRO, linewidth=0.8, linestyle=(0, (3, 2)))
        ax_a.text(v + 0.012, 9.2, rot, fontsize=7.5, color=E.CINZA, va="bottom")
        for th in (th_min, th_max):
            ax_a.scatter([v], [th / v], s=22, color=E.AZUL, zorder=4)
        ax_a.text(v + 0.012, th_max / v * 1.06, f"{th_min / v:.0f}–{th_max / v:.0f} g",
                  fontsize=8, fontweight="bold", va="bottom")
    ax_a.set_yscale("log")
    ax_a.set_ylim(8, 900)
    ax_a.set_xlim(0.05, 1.19)
    ax_a.set_yticks([10, 30, 100, 300], ["10", "30", "100", "300"])
    ax_a.set_xticks([0.1, 0.25, 0.5, 0.75, 1.0], ["10%", "25%", "50%", "75%", "100%"])
    ax_a.set_xlabel("VPP: fração dos \"tratados\" que tinha pulverização aérea")
    ax_a.set_ylabel("|ATT| implicado nos genuinamente tratados (g, log)")
    ax_a.set_title("(a) O que o coeficiente implica: ATT = θ / VPP")
    ax_a.text(0.985, 0.97, f"Faixa: |θ| de {th_min:.0f} a {th_max:.0f} g\n"
              "(coeficientes da §6; nenhum confirmatório)".replace(".", ","),
              transform=ax_a.transAxes, ha="right", va="top", fontsize=7.5)

    # ---------------- (b) curva de poder ----------------
    mde = e12.MDE_G
    theta = np.linspace(0, 2 * mde, 300)
    poder = np.array([e12.poder_aproximado(t) for t in theta])
    f_min, f_max = min(e12.FRACOES_EXPOSTAS), max(e12.FRACOES_EXPOSTAS)
    faixas = (
        # a faixa larga primeiro: a estreita é desenhada por cima
        ("dose_e_tratamento", "θ esperado se dose\nfosse tratamento", E.AZUL, "#e3edf7"),
        ("censo2006", "θ esperado com o\nVPP do Censo 2006", E.LARANJA, "#f8e2c4"),
    )
    for nome, rot, cor, fundo in faixas:
        v = e12.CENARIOS_VPP[nome]
        lo = e12.sinal_esperado(v, f_min, d_min)
        hi = min(e12.sinal_esperado(v, f_max, d_max), 2 * mde)
        ax_b.axvspan(lo, hi, color=fundo, zorder=0)
        ax_b.text((lo + hi) / 2 if nome != "censo2006" else hi + 0.8,
                  0.60 if nome == "censo2006" else 0.30, rot, fontsize=7.5, color=cor,
                  ha="center" if nome != "censo2006" else "left", va="center")
        if nome == "censo2006":
            p_hi = e12.poder_aproximado(hi)
            ax_b.scatter([hi], [p_hi], s=30, color=E.LARANJA, zorder=5)
            ax_b.annotate(f"no máximo {hi:.1f} g → poder {p_hi:.0%}".replace(".", ","),
                          (hi, p_hi), xytext=(10, 14), textcoords="offset points",
                          fontsize=8, fontweight="bold",
                          arrowprops=dict(arrowstyle="-", color=E.NEUTRO, linewidth=0.5))
    ax_b.plot(theta, poder, color=E.TINTA, linewidth=2)
    ax_b.scatter([mde], [e12.PODER_NO_MDE], s=30, color=E.TINTA, zorder=5)
    ax_b.annotate(f"MDE = {mde:.1f} g\n(poder {e12.PODER_NO_MDE:.0%})".replace(".", ","),
                  (mde, e12.PODER_NO_MDE), xytext=(8, -22), textcoords="offset points",
                  fontsize=8)
    ax_b.axhline(e12.ALFA, color=E.NEUTRO, linewidth=0.6, linestyle=(0, (3, 2)))
    ax_b.text(2 * mde, e12.ALFA + 0.012, f"α = {e12.ALFA:.0%}", ha="right", fontsize=7,
              color=E.CINZA)
    ax_b.set_xlim(0, 2 * mde)
    ax_b.set_ylim(0, 1.02)
    ax_b.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ["0%", "20%", "40%", "60%", "80%", "100%"])
    ax_b.grid(axis="y")
    ax_b.set_axisbelow(True)
    ax_b.set_xlabel("Efeito verdadeiro sobre o peso ao nascer, |θ| (g)")
    ax_b.set_ylabel("Poder (teste bilateral, α = 5%)")
    ax_b.set_title("(b) O que o desenho enxerga: curva de poder")

    fig.text(0.01, 0.008, "CALIBRAÇÃO, NÃO ESTIMATIVA — o VPP é de 2006; δ vem de um "
             "análogo; f (fração exposta) é grade de 10% a 50%.", fontsize=7,
             color=E.VERMELHO)
    fig.text(0.99, 0.008, "Conta: scripts/estimate/12_erro_de_classificacao.py "
             "(Denteh & Kédagni, arXiv:2207.11890, Corolário 1).", ha="right",
             fontsize=6, color=E.CINZA)
    fig.tight_layout(rect=(0, 0.03, 1, 1), w_pad=2.5)
    return fig


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out-dir", type=Path, default=E.FIG_DIR)
    args = p.parse_args(argv)
    e12 = E.carrega_script("estimate/12_erro_de_classificacao.py")
    E.grava(desenha(e12), "diluicao_e_poder", args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
