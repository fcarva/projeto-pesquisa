"""F01 — Mapa do desenho: a dose no Ceará e a Chapada do Apodi na divisa com o RN.

O QUE A FIGURA MOSTRA
---------------------

Dois painéis, e cada um responde a uma pergunta de quem lê o DiD pela primeira vez:

- **(a) Ceará — quem é tratado, e com que dose.** Coroplético da área média
  pré-ban (PAM, 2015–2018) da cultura-âncora, em escala log (a dose é muito
  concentrada). Contorno grosso = decil superior entre os produtores (o grupo
  tratado das especificações binárias, mesma conta dos estimadores 07/08 e do
  script 16). Hachura = `d = 0` na definição base (área nula na PAM). Círculos =
  estabelecimentos com aplicação por aeronave no Censo Agropecuário 2006
  (tabela SIDRA 1008).
- **(b) Chapada do Apodi — a divisa CE × RN.** Zoom na região onde os dois
  únicos tratados com aeronave (Limoeiro do Norte e Quixeré) tocam a linha
  potiguar, com os municípios do lado do RN nomeados no PLP 98/07 (RIDE da
  Chapada, delimitação externa do script 15).

⚠️ O QUE A FIGURA NÃO AFIRMA
-----------------------------

- **Não desenha a "Chapada do Apodi" como polígono.** Não há limite oficial da
  chapada na malha do IBGE; o painel (b) é um recorte por municípios, e o rótulo
  é de região, não de fronteira geomorfológica.
- **Não decide o grupo de comparação.** O lado potiguar aparece como a
  comparação *candidata* da Rota 1; trocar o grupo de controle é mudança de
  identificação e passa pelo orientador (CLAUDE.md).
- **O `d = 0` hachurado é a definição base** (área nula na PAM), não a
  definição 4 (baixa aptidão GAEZ) ratificada como primária na pré-especificação.
- **Aeronave é dado de 2006** e conta estabelecimentos, não voos (flag 7).

FONTES
------

- Malha municipal 2022: IBGE via geobr/IPEA (`geobr_prep_data`, release v2.0.0,
  geometria simplificada — suficiente para figura; adjacência se mede no script
  16, com a geometria completa). Baixada do GitHub Releases **com verificação
  TLS** e guardada em `data/geo/` (gitignored).
- Dose: `pam_ce_muni_cultura_media__sidra*.parquet` (script 01).
- Aeronave: `censo_agro_equipamento_{ce,uf24}.csv` (script 13). Opcional.

Uso:
    python scripts/figures/01_mapa_desenho.py --cultura "Banana (cacho)"

Saída: `paper/figures/mapa_desenho__<cultura>.{pdf,png}` — agregado municipal de
dado público, seguro para versionar.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import unicodedata
from datetime import date
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
PROCESSED = RAIZ / "data" / "processed"
GEO_DIR = RAIZ / "data" / "geo"
FIG_DIR = RAIZ / "paper" / "figures"

ANO_MALHA = 2022
ARQUIVO_MALHA = f"municipalities_{ANO_MALHA}_simplified.parquet"
URL_MALHA = ("https://github.com/ipea/geobr_prep_data/releases/download/v2.0.0/"
             + ARQUIVO_MALHA)

UF_CE, UF_RN = 23, 24
VIZINHOS_CONTEXTO = {22: "PI", 24: "RN", 25: "PB", 26: "PE"}
CRS_METRICO = 5880  # SIRGAS 2000 / Brasil Polyconic — só para o buffer da divisa

# Rótulos do painel (b). Escolha editorial de legibilidade, não de desenho.
ROTULOS_ZOOM = (
    "Limoeiro do Norte", "Quixeré", "Russas", "Jaguaruana", "Tabuleiro do Norte",
    "Baraúna", "Mossoró", "Apodi", "Governador Dix-Sept Rosado", "Felipe Guerra",
)

# Paleta: um matiz sequencial para a magnitude (dose); tinta neutra para o resto.
# Deslocamento (em pontos) dos rótulos que cairiam sobre o círculo de aeronave.
DESLOCA_ROTULO = {"Limoeiro do Norte": (-14, -20), "Quixeré": (0, 15),
                  "Jaguaruana": (0, 12)}
# Posição dos rótulos de UF no painel (a): editorial, dentro da moldura.
ROTULOS_UF = {"PI": (-41.45, -7.3), "PE": (-40.3, -7.95), "PB": (-38.2, -7.1),
              "RN": (-37.0, -6.3)}

COR_DIVISA = "#b3261e"
COR_TINTA = "#1a1a1a"
COR_CONTEXTO = "#ececec"
COR_RIDE = "#d9d2c3"


def _carrega_script(relativo: str):
    """Scripts numerados não são importáveis por nome; mesmo padrão dos testes."""
    caminho = RAIZ / "scripts" / relativo
    spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def slug(texto: str) -> str:
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", sem_acento.lower()).strip("-")


def carrega_malha(caminho: Path = GEO_DIR / ARQUIVO_MALHA):
    """Malha municipal do Brasil (geobr v2), com cache em `data/geo/`."""
    import geopandas as gpd

    if not caminho.exists():
        import requests

        print(f"[rede] baixando a malha: {URL_MALHA}")
        resposta = requests.get(URL_MALHA, timeout=300)  # TLS verificado (padrão)
        resposta.raise_for_status()
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_bytes(resposta.content)
    malha = gpd.read_parquet(caminho)
    malha["cod7"] = malha["code_muni"].astype("int64").astype(str)
    malha["uf"] = malha["code_state"].astype(int)
    return malha


def escolhe_pam(explicito: Path | None) -> Path:
    """Prefere o recorte CE+RN; o do Ceará sozinho basta para o painel (a)."""
    if explicito is not None:
        return explicito
    for nome in ("pam_ce_muni_cultura_media__sidra__uf23-24.parquet",
                 "pam_ce_muni_cultura_media__sidra.parquet"):
        if (PROCESSED / nome).exists():
            return PROCESSED / nome
    raise FileNotFoundError(
        "PAM real não encontrado em data/processed/. Rode antes:\n"
        "  python scripts/data_prep/01_check_dose_variation.py --fonte sidra --ufs 23 24")


def dose_do_ceara(pam: pd.DataFrame, cultura: str) -> pd.DataFrame:
    """Dose por município do CE. Falha alto se a cultura não casar com um rótulo só."""
    rotulos = sorted({c for c in pam["cultura"].unique()
                      if cultura.lower() in c.lower()})
    if len(rotulos) != 1:
        raise ValueError(f"--cultura {cultura!r} casa com {rotulos or 'nenhum rótulo'}; "
                         f"disponíveis: {sorted(pam['cultura'].unique())}")
    bloco = pam[(pam["cultura"] == rotulos[0])
                & pam["cod_ibge"].astype(str).str.startswith(str(UF_CE))]
    dose = bloco[["cod_ibge", "area_ha_media"]].rename(
        columns={"cod_ibge": "cod7", "area_ha_media": "dose"})
    dose["cod7"] = dose["cod7"].astype(str)
    dose.attrs["rotulo"] = rotulos[0]
    return dose


def carrega_aeronaves() -> pd.DataFrame:
    """Estabelecimentos com aplicação por aeronave (Censo Agro 2006). Opcional."""
    pedacos = []
    for nome in ("censo_agro_equipamento_ce.csv", "censo_agro_equipamento_uf24.csv"):
        arq = PROCESSED / nome
        if arq.exists():
            pedacos.append(pd.read_csv(arq, dtype={"cod_ibge7": str}))
        else:
            print(f"[aviso] sem {nome}: aeronaves dessa UF não entram no mapa.")
    if not pedacos:
        return pd.DataFrame(columns=["cod_ibge7", "aeronave"])
    tudo = pd.concat(pedacos, ignore_index=True)
    return tudo.loc[tudo["aeronave"] > 0, ["cod_ibge7", "aeronave"]]


def linha_da_divisa(ce, rn):
    """Trecho do contorno do CE que encosta no RN.

    A geometria simplificada não garante vértices coincidentes entre UFs: o
    buffer de 1 km (em CRS métrico) é tolerância de DESENHO, não medida.
    """
    borda_ce = ce.to_crs(CRS_METRICO).union_all().boundary
    faixa_rn = rn.to_crs(CRS_METRICO).union_all().buffer(1000)
    import geopandas as gpd

    return gpd.GeoSeries([borda_ce.intersection(faixa_rn)], crs=CRS_METRICO).to_crs(ce.crs)


def desenha(malha, dose: pd.DataFrame, tratados: set[str], aeronaves: pd.DataFrame,
            ride_rn: set[str], cultura_rotulo: str, fonte_pam: str):
    import matplotlib.pyplot as plt
    from matplotlib import colormaps
    from matplotlib.colors import LinearSegmentedColormap, LogNorm
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch, Rectangle

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8,
                         "hatch.linewidth": 0.4, "hatch.color": "#8a8a8a"})

    ce = malha[malha["uf"] == UF_CE].merge(dose, on="cod7", how="left")
    if ce["dose"].isna().any():
        raise ValueError(f"{int(ce['dose'].isna().sum())} municípios do CE sem dose na PAM")
    rn = malha[malha["uf"] == UF_RN]
    contexto = malha[malha["uf"].isin(VIZINHOS_CONTEXTO)].dissolve("uf")
    # A malha simplificada deixa frestas entre municípios; fechar e reabrir
    # (~1 km) apaga os riscos internos sem mover o contorno. Só desenho.
    contexto["geometry"] = contexto.geometry.buffer(0.01).buffer(-0.01)
    positivos, zeros = ce[ce["dose"] > 0], ce[ce["dose"] == 0]
    trat = ce[ce["cod7"].isin(tratados)]
    ride = rn[rn["cod7"].isin(ride_rn)]
    divisa = linha_da_divisa(ce, rn)

    base = colormaps["Blues"]
    cmap = LinearSegmentedColormap.from_list(
        "dose", [base(x) for x in (0.10, 0.35, 0.60, 0.80, 0.98)])
    norm = LogNorm(vmin=max(1.0, positivos["dose"].min()), vmax=positivos["dose"].max())

    pontos = malha[malha["cod7"].isin(aeronaves["cod_ibge7"])].merge(
        aeronaves, left_on="cod7", right_on="cod_ibge7")
    centros = pontos.geometry.representative_point()
    escala = 14.0  # pt² por estabelecimento

    def camadas(ax, rotulo_uf: bool):
        contexto.plot(ax=ax, color=COR_CONTEXTO, edgecolor="#b5b5b5", linewidth=0.5)
        rn.plot(ax=ax, color=COR_CONTEXTO, edgecolor="#cfcfcf", linewidth=0.25)
        ride.plot(ax=ax, color=COR_RIDE, edgecolor="#a79f8d", linewidth=0.35)
        positivos.plot(ax=ax, column="dose", cmap=cmap, norm=norm,
                       edgecolor="white", linewidth=0.25)
        zeros.plot(ax=ax, facecolor="white", edgecolor="#8a8a8a", linewidth=0.3,
                   hatch="//////")
        trat.boundary.plot(ax=ax, color=COR_TINTA, linewidth=1.1)
        divisa.plot(ax=ax, color=COR_DIVISA, linewidth=2.0)
        if len(pontos):
            ax.scatter(centros.x, centros.y, s=pontos["aeronave"] * escala,
                       facecolor="none", edgecolor="#e07b00", linewidth=1.4, zorder=5)
        if rotulo_uf:
            for sigla, (x, y) in ROTULOS_UF.items():
                ax.annotate(sigla, (x, y), ha="center", color="#6b6b6b", fontsize=9)
        ax.set_xticks([]), ax.set_yticks([])
        ax.set_xlabel(""), ax.set_ylabel("")
        for lado in ax.spines.values():
            lado.set_edgecolor("#9a9a9a"), lado.set_linewidth(0.6)

    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(11.2, 6.6),
                                     gridspec_kw={"width_ratios": [1.05, 1]})

    # --- (a) Ceará -----------------------------------------------------------
    camadas(ax_a, rotulo_uf=True)
    x0, y0, x1, y1 = ce.total_bounds
    ax_a.set_xlim(x0 - 0.35, x1 + 1.45), ax_a.set_ylim(y0 - 0.25, y1 + 0.25)
    ax_a.set_title("(a) Ceará: dose pré-ban e grupo tratado", loc="left",
                   fontsize=10, color=COR_TINTA)

    # --- (b) Chapada do Apodi ------------------------------------------------
    camadas(ax_b, rotulo_uf=False)
    # Enquadra os municípios rotulados; a RIDE potiguar segue para leste, fora
    # do quadro — o painel (a) a mostra inteira.
    ambos = pd.concat([ce, rn])
    zx0, zy0, zx1, zy1 = ambos[ambos["name_muni"].isin(ROTULOS_ZOOM)].total_bounds
    m = 0.08
    ax_b.set_xlim(zx0 - m, zx1 + m), ax_b.set_ylim(zy0 - m, zy1 + m)
    ax_b.set_title("(b) Chapada do Apodi: a divisa CE × RN", loc="left",
                   fontsize=10, color=COR_TINTA)
    halo = dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none", alpha=0.75)
    for _, mun in ambos.iterrows():
        if mun["name_muni"] in ROTULOS_ZOOM:
            p = mun.geometry.representative_point()
            peso = "bold" if mun["cod7"] in tratados else "normal"
            ax_b.annotate(mun["name_muni"].replace("Governador", "Gov."), (p.x, p.y),
                          xytext=DESLOCA_ROTULO.get(mun["name_muni"], (0, 0)),
                          textcoords="offset points", ha="center", va="center", fontsize=7, fontweight=peso,
                          color=COR_TINTA, bbox=halo, zorder=6)
    ax_b.text(0.03, 0.04, "CEARÁ\nban desde 09/01/2019", transform=ax_b.transAxes,
              fontsize=8.5, color=COR_TINTA, va="bottom", bbox=halo)
    ax_b.text(0.97, 0.04, "RIO GRANDE DO NORTE\nsem ban", transform=ax_b.transAxes,
              fontsize=8.5, color=COR_TINTA, va="bottom", ha="right", bbox=halo)

    ax_a.add_patch(Rectangle((zx0 - m, zy0 - m), zx1 - zx0 + 2 * m, zy1 - zy0 + 2 * m,
                             fill=False, edgecolor=COR_TINTA, linewidth=0.8,
                             linestyle=(0, (4, 2)), zorder=7))
    ax_a.annotate("painel (b)", (zx0 - m, zy1 + m), xytext=(0, 3),
                  textcoords="offset points", fontsize=7, color=COR_TINTA)

    # --- legenda e barra de cor ---------------------------------------------
    n_trat, n_pos, n_zero = len(trat), len(positivos), len(zeros)
    itens = [
        Line2D([], [], color=COR_TINTA, linewidth=1.1,
               label=f"Decil superior da dose ({n_trat} de {n_pos} produtores)"),
        Patch(facecolor="white", edgecolor="#8a8a8a", hatch="//////",
              label=f"d = 0: área nula na PAM ({n_zero} municípios)"),
        Line2D([], [], color=COR_DIVISA, linewidth=2.0, label="Divisa CE × RN"),
        Patch(facecolor=COR_RIDE, edgecolor="#a79f8d",
              label="RN: municípios da RIDE da Chapada (PLP 98/07)"),
    ]
    if len(pontos):
        for n in (1, int(pontos["aeronave"].max())):
            itens.append(Line2D([], [], linestyle="none", marker="o",
                                markerfacecolor="none", markeredgecolor="#e07b00",
                                markeredgewidth=1.4, markersize=(n * escala) ** 0.5,
                                label=f"Aplicação por aeronave, Censo Agro 2006: "
                                      f"{n} estabelecimento{'s' if n > 1 else ''}"))
    fig.legend(handles=itens, loc="lower left", bbox_to_anchor=(0.05, 0.015), ncol=2,
               frameon=False, fontsize=7.5, labelspacing=0.9, handlelength=2.4)

    cax = fig.add_axes([0.71, 0.10, 0.24, 0.018])
    from matplotlib.cm import ScalarMappable

    barra = fig.colorbar(ScalarMappable(norm=norm, cmap=cmap), cax=cax,
                         orientation="horizontal")
    barra.outline.set_visible(False)
    barra.ax.tick_params(labelsize=7, length=2, color="#9a9a9a")
    barra.set_label(f"Dose — {cultura_rotulo}:\nárea média 2015–2018 (ha, escala log)",
                    fontsize=7.5)

    fig.text(0.05, 0.965, "Desenho do DiD: banimento estadual da pulverização aérea "
             "(Lei 16.820/2019) e intensidade pré-ban de exposição",
             fontsize=11.5, color=COR_TINTA, fontweight="bold")
    fig.text(0.95, 0.002,
             f"Fontes: PAM/IBGE ({fonte_pam}); Censo Agropecuário 2006 (SIDRA 1008); "
             f"malha municipal IBGE {ANO_MALHA} via geobr/IPEA. Gerado em "
             f"{date.today().isoformat()}.", fontsize=6, color="#6b6b6b", ha="right",
             va="bottom")
    fig.subplots_adjust(left=0.05, right=0.95, top=0.92, bottom=0.17, wspace=0.05)
    return fig


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--cultura", required=True,
                   help='Cultura-âncora da dose, ex.: "Banana (cacho)". Sem default: '
                        "o CLAUDE.md proíbe hard-codar a âncora.")
    p.add_argument("--pam", type=Path, default=None,
                   help="PAM município×cultura (script 01). Padrão: o recorte real "
                        "em data/processed/.")
    p.add_argument("--out-dir", type=Path, default=FIG_DIR)
    p.add_argument("--dpi", type=int, default=300)
    args = p.parse_args(argv)

    try:
        caminho_pam = escolhe_pam(args.pam)
    except FileNotFoundError as erro:
        print(f"[erro] {erro}")
        return 1
    if "simulado" in caminho_pam.name:
        print("[erro] mapa com dose SIMULADA não vai para paper/figures/.")
        return 1

    pam = pd.read_parquet(caminho_pam)
    dose = dose_do_ceara(pam, args.cultura)
    rotulo = dose.attrs["rotulo"]

    fronteira = _carrega_script("data_prep/16_fronteira_geografica.py")
    censo15 = _carrega_script("data_prep/15_censo_demografico.py")
    pam_ce = pam[pam["cod_ibge"].astype(str).str.startswith(str(UF_CE))]
    tratados = fronteira.decil_superior(pam_ce, re.escape(rotulo))  # o 16 usa regex
    print(f"[ok] {rotulo}: {int((dose['dose'] > 0).sum())} produtores, "
          f"{len(tratados)} no decil superior, {int((dose['dose'] == 0).sum())} com d = 0")

    import matplotlib

    matplotlib.use("Agg")
    fig = desenha(carrega_malha(), dose, tratados, carrega_aeronaves(),
                  {str(c) for c in censo15.RIDE_CHAPADA_RN}, rotulo, caminho_pam.name)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "png"):
        destino = args.out_dir / f"mapa_desenho__{slug(rotulo)}.{ext}"
        fig.savefig(destino, dpi=args.dpi)
        print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
