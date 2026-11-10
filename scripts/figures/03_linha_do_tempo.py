"""F03 — Linha do tempo: marcos legais, antecipação e janelas do desenho.

Uma figura só de datas: o que aconteceu, quando, e como as janelas do desenho
(dose 2015–2018; estimação 2015 → 19/12/2024) se posicionam em relação aos três
marcos de antecipação — notícia, certeza e obrigação.

⚠️ Toda data aqui vem do `CLAUDE.md` e de `docs/legislacao/`; a coluna `fonte`
de `MARCOS` diz de onde. Data sem fonte primária conferida está marcada:
- a revogação de Limoeiro (Lei 1.511/2010) tem fonte **secundária** (texto
  integral a conferir);
- a notícia da SEDH de 11/03/2011 e a ação de jul/2011 têm **desfecho
  desconhecido** (flag 7) — aparecem como interrogação, não como fato.

Uso:
    python scripts/figures/03_linha_do_tempo.py
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _estilo as E  # noqa: E402

# (data, rótulo, faixa, incerto, fonte)
MARCOS = (
    (date(2009, 11, 20), "Limoeiro do Norte proíbe\n(Lei mun. 1.478)", "municipal", False,
     "camaralimoeirodonorte.ce.gov.br/leis/549"),
    (date(2010, 5, 26), "Revogada\n(Lei mun. 1.511)", "municipal", True,
     "secundária: Diário do Nordeste abr/2010; G1 31/10/2024 — texto a conferir"),
    (date(2011, 3, 11), "SEDH noticia proibição\nna Chapada; ação do MP\n(jul/2011) — desfecho?", "municipal", True,
     "docs/ars/19 §2.3 — desfecho desconhecido"),
    (date(2015, 2, 24), "PL 18/2015\napresentado\n(notícia)", "estadual", False,
     "docs/ars/06-quimico-e-antecipacao.md"),
    (date(2018, 12, 18), "Aprovado por\nunanimidade\n(certeza)", "estadual", False,
     "docs/ars/06-quimico-e-antecipacao.md"),
    (date(2019, 1, 9), "Lei 16.820\nem vigor\n(obrigação)", "estadual", False,
     "docs/legislacao/ — texto oficial"),
    (date(2024, 12, 19), "Lei 19.135:\nexceção de\ndrones", "estadual", False,
     "docs/legislacao/"),
)
JANELAS = (
    ("Dose: PAM, média 2015–2018", date(2015, 1, 1), date(2018, 12, 31), E.AZUL_CLARO),
    ("Pré-ban", date(2015, 1, 1), date(2019, 1, 8), "#d5d5d5"),
    ("Pós-ban com cota zero (até a exceção de drones)", date(2019, 1, 9),
     date(2024, 12, 19), "#f0c9c5"),
)


def desenha():
    plt = E.aplica_estilo()
    import matplotlib.dates as mdates

    fig, ax = plt.subplots(figsize=(11.2, 4.4))
    y_eixo = {"municipal": 1.0, "estadual": 0.0}
    for nome, y in y_eixo.items():
        ax.axhline(y, color=E.NEUTRO, linewidth=0.8, zorder=1)
        ax.text(date(2008, 9, 1), y, {"municipal": "Chapada do Apodi\n(município / MP)",
                                      "estadual": "Ceará\n(lei estadual)"}[nome],
                ha="right", va="center", fontsize=8, color=E.CINZA)

    # janelas, empilhadas abaixo do eixo estadual
    for i, (rot, ini, fim, cor) in enumerate(JANELAS):
        y = -0.62 - 0.2 * (0 if i == 0 else 1)
        ax.barh(y, (fim - ini).days, left=ini, height=0.14, color=cor, zorder=2)
        ax.text(ini if i < 2 else fim, y + (0.1 if i == 0 else -0.1), rot, fontsize=7.5,
                va="bottom" if i == 0 else "top", ha="left" if i < 2 else "right",
                color=E.TINTA)

    acima = {"estadual": (0.16, "bottom"), "municipal": (0.16, "bottom")}
    # (dias, altura) — só o RÓTULO se desloca; o marcador fica na data.
    desloca = {date(2009, 11, 20): (-300, 0.16), date(2010, 5, 26): (0, 0.52),
               date(2011, 3, 11): (520, 0.16),
               date(2018, 12, 18): (-420, 0.16), date(2019, 1, 9): (420, 0.16)}
    for quando, rot, faixa, incerto, _ in MARCOS:
        y = y_eixo[faixa]
        cor = E.VERMELHO if quando == date(2019, 1, 9) else E.TINTA
        ax.scatter([quando], [y], s=46, zorder=4, linewidth=1.3, edgecolor=cor,
                   facecolor="white" if incerto else cor)
        _, va = acima[faixa]
        dias, dy = desloca.get(quando, (0, 0.16))
        x_txt = quando + timedelta(days=dias)
        ax.annotate(f"{quando:%d/%m/%Y}\n{rot}", (quando, y), xytext=(x_txt, y + dy),
                    ha="center", va=va, fontsize=7.5, color=cor, linespacing=1.25,
                    arrowprops=dict(arrowstyle="-", color=E.NEUTRO, linewidth=0.5))

    ax.scatter([], [], s=46, facecolor="white", edgecolor=E.TINTA, linewidth=1.3,
               label="Fonte secundária ou desfecho desconhecido")
    ax.legend(loc="lower left", bbox_to_anchor=(0.0, -0.02), fontsize=7.5)
    ax.set_ylim(-1.25, 2.0)
    ax.set_xlim(date(2008, 9, 1), date(2025, 9, 1))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_title("Marcos legais e janelas do desenho: a dose é medida depois da notícia do PL")
    fig.text(0.99, 0.008, "Fontes: Leis 16.820/2019 e 19.135/2024 (docs/legislacao/); "
             "Câmara de Limoeiro do Norte; docs/ars/06 e 19.", ha="right", fontsize=6,
             color=E.CINZA)
    fig.tight_layout(rect=(0.09, 0.02, 1, 1))
    return fig


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out-dir", type=Path, default=E.FIG_DIR)
    args = p.parse_args(argv)
    E.grava(desenha(), "linha_do_tempo", args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
