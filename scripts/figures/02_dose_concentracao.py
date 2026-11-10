"""F02 — Por que esta cultura, e o que a dose mede: concentração e aeronave.

- **(a) Triagem das culturas candidatas (Gate 1).** Municípios do Ceará com área
  positiva na média 2015–2018, por cultura, com o Gini da dose anotado. A conta
  é a do script 01 (`dispersao_por_cultura`) — a figura não recalcula nada.
- **(b) A dose ordenada, e onde havia avião (flag 7).** Cada ponto é um
  município produtor da cultura-âncora, do maior para o menor (escala log). A
  faixa marca o decil superior; os anéis, os municípios com estabelecimento que
  aplicava agrotóxico por aeronave no Censo Agro 2006 (SIDRA 1008).

⚠️ O painel (b) é o desenho da ameaça de **diluição**: a dose mede a cultura, não
o método. O VPP anotado (tratados com aeronave / tratados) é de **2006** e conta
estabelecimentos, não voos — pode não valer em 2018 (CLAUDE.md, flag 7).

Uso:
    python scripts/figures/02_dose_concentracao.py --cultura "Banana (cacho)"
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _estilo as E  # noqa: E402


def triagem(pam_ce: pd.DataFrame) -> pd.DataFrame:
    s01 = E.carrega_script("data_prep/01_check_dose_variation.py")
    tab = s01.dispersao_por_cultura(pam_ce)
    tab = tab[tab["n_muni_positivo"] > 0]  # sem produtor não há dispersão a medir
    return tab[["cultura", "n_muni_positivo", "gini_dose"]].sort_values("n_muni_positivo")


def dose_ordenada(pam_ce: pd.DataFrame, rotulo: str, aeronave: pd.DataFrame) -> pd.DataFrame:
    """Produtores da âncora em ordem decrescente, com decil e aeronave marcados."""
    d = pam_ce[(pam_ce["cultura"] == rotulo) & (pam_ce["area_ha_media"] > 0)]
    d = d.sort_values("area_ha_media", ascending=False).reset_index(drop=True)
    d["posicao"] = d.index + 1
    d["tratado"] = d["cod_ibge"].astype(str).isin(E.decil_superior(pam_ce, rotulo))
    voo = dict(zip(aeronave["cod_ibge7"].astype(str), aeronave["aeronave"]))
    d["aeronave"] = d["cod_ibge"].astype(str).map(voo).fillna(0)
    return d


def desenha(tab: pd.DataFrame, d: pd.DataFrame, rotulo: str, n_muni: int):
    plt = E.aplica_estilo()
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(11.2, 5.6),
                                     gridspec_kw={"width_ratios": [1, 1.25]})

    cores = [E.AZUL if c == rotulo else E.AZUL_CLARO for c in tab["cultura"]]
    ax_a.barh(tab["cultura"].str.replace("*", "", regex=False), tab["n_muni_positivo"],
              color=cores, height=0.72)
    for y, (n, g) in enumerate(zip(tab["n_muni_positivo"], tab["gini_dose"])):
        ax_a.text(n + 2, y, f"{int(n)}  ·  Gini {g:.2f}".replace(".", ","),
                  va="center", fontsize=7, color=E.CINZA)
    ax_a.axvline(n_muni, color=E.NEUTRO, linewidth=0.6, linestyle=(0, (3, 2)))
    ax_a.text(n_muni + 2, -0.75, f"todos os {n_muni}\nmunicípios", va="center",
              fontsize=7, color=E.CINZA)
    ax_a.set_xlim(0, n_muni * 1.33)
    ax_a.set_xlabel("Municípios do Ceará com área positiva (média 2015–2018)")
    ax_a.tick_params(axis="y", length=0, labelsize=7.5, labelcolor=E.TINTA)
    ax_a.set_title("(a) Triagem das culturas candidatas")

    k = int(d["tratado"].sum())
    ax_b.axvspan(0.3, k + 0.5, color="#eef3f9", zorder=0)
    ax_b.scatter(d["posicao"], d["area_ha_media"], s=14,
                 c=d["tratado"].map({True: E.AZUL, False: E.AZUL_CLARO}),
                 linewidths=0, zorder=3)
    voo = d[d["aeronave"] > 0]
    ax_b.scatter(voo["posicao"], voo["area_ha_media"], s=90, facecolor="none",
                 edgecolor=E.LARANJA, linewidth=1.5, zorder=4)
    nomes = E.nomes_municipios()
    for i, (_, m) in enumerate(voo.iterrows()):
        nome = nomes.get(str(m["cod_ibge"]), str(m["cod_ibge"]))
        esquerda = m["posicao"] > 0.8 * len(d)  # perto da borda: rótulo para dentro
        ax_b.annotate(f"{nome} ({int(m['aeronave'])})", (m["posicao"], m["area_ha_media"]),
                      xytext=(-9 if esquerda else 9, 9 if i % 2 == 0 else -13),
                      textcoords="offset points", ha="right" if esquerda else "left",
                      fontsize=7.5, color=E.TINTA)
    ax_b.set_yscale("log")
    ax_b.set_xlim(0.3, len(d) + 2)
    ax_b.grid(axis="y")
    ax_b.set_axisbelow(True)
    ax_b.set_xlabel(f"Posição entre os {len(d)} municípios produtores (1 = maior área)")
    ax_b.set_ylabel(f"{rotulo}: área média 2015–2018 (ha, log)")
    com_voo = int((d["tratado"] & (d["aeronave"] > 0)).sum())
    ax_b.text(k / 2 + 0.4, d["area_ha_media"].min() * 1.15,
              f"decil\nsuperior\n({k})", ha="center", va="bottom", fontsize=7.5,
              color=E.AZUL)
    topo_area = d.loc[d["tratado"], "area_ha_media"].sum() / d["area_ha_media"].sum()
    ax_b.text(0.98, 0.97,
              f"Tratados com aeronave em 2006: {com_voo} de {k}\n"
              f"O decil concentra {topo_area:.0%} da área".replace(".", ","),
              transform=ax_b.transAxes, ha="right", va="top", fontsize=8.5)
    ax_b.set_title("(b) A dose ordenada, e onde havia aplicação aérea")
    ax_b.scatter([], [], s=90, facecolor="none", edgecolor=E.LARANJA, linewidth=1.5,
                 label="Aplicação por aeronave, Censo Agro 2006 (nº de estabelecimentos)")
    ax_b.legend(loc="lower left", bbox_to_anchor=(0.12, 0.0), fontsize=7.5)

    fig.text(0.99, 0.005, "Fontes: PAM/IBGE (SIDRA 1612 e 1613), média 2015–2018; "
             "Censo Agropecuário 2006 (SIDRA 1008).", ha="right", fontsize=6, color=E.CINZA)
    fig.tight_layout(rect=(0, 0.02, 1, 1), w_pad=3)
    return fig


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--cultura", required=True, help="Cultura-âncora (sem default).")
    p.add_argument("--pam", type=Path, default=None)
    p.add_argument("--censo", type=Path,
                   default=E.PROCESSED / "censo_agro_equipamento_ce.csv")
    p.add_argument("--out-dir", type=Path, default=E.FIG_DIR)
    args = p.parse_args(argv)
    try:
        pam_ce = E.so_ceara(pd.read_parquet(E.pam_real(args.pam)))
    except FileNotFoundError as erro:
        print(f"[erro] {erro}")
        return 1
    if not args.censo.exists():
        print(f"[erro] sem {args.censo}: rode scripts/data_prep/13_censo_agro_equipamento.py")
        return 1
    rotulo = E.rotulo_unico(pam_ce["cultura"].unique(), args.cultura)
    aeronave = pd.read_csv(args.censo, dtype={"cod_ibge7": str})
    d = dose_ordenada(pam_ce, rotulo, aeronave)
    fig = desenha(triagem(pam_ce), d, rotulo, pam_ce["cod_ibge"].nunique())
    E.grava(fig, f"dose_concentracao__{E.slug(rotulo)}", args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
