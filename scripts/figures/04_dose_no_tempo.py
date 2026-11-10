"""F04 — A dose no tempo: a área da cultura-âncora antes e depois da notícia do PL.

A dose do desenho é a média 2015–2018 da PAM — e essa janela começa **depois**
da apresentação do PL 18/2015 (24/02/2015). Se os produtores reagiram à
expectativa do ban, a própria variável de tratamento já carrega resposta
(CLAUDE.md; `docs/ars/06-quimico-e-antecipacao.md`). Esta figura é o descritivo
que essa preocupação pede: a área anual da cultura, por grupo, indexada à média
da janela da dose (= 100).

Grupos — todos definidos pela dose 2015–2018 e pelo Censo Agro 2006, nunca por
desfecho:
- decil superior **com** aplicação por aeronave em 2006;
- decil superior **sem** aeronave;
- demais produtores.

⚠️ O QUE A FIGURA NÃO É
------------------------

- **Não é teste de antecipação.** É série descritiva de três agregados, sem
  contrafactual. Queda ou alta depois de 2015 tem muitas explicações (a seca de
  2012–2017 atravessa a janela inteira).
- **Os grupos são classificados pela janela 2015–2018**: fora dela há regressão
  à média por construção — quem está no topo em 2015–2018 tende a estar abaixo
  antes e depois.
- **PAM é área destinada à colheita**, não aplicação de agrotóxico.

Uso:
    python scripts/figures/04_dose_no_tempo.py --cultura "Banana (cacho)"
    python scripts/figures/04_dose_no_tempo.py --cultura "Banana (cacho)" --sem-preflight

Cache: `data/processed/pam_ce_muni_cultura_ano__sidra.parquet` (gitignored).
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _estilo as E  # noqa: E402

ANOS = tuple(range(2008, 2024))
JANELA_DOSE = (2015, 2016, 2017, 2018)
BLOCO = 6  # anos por consulta: o SIDRA recusa pedidos acima de 100 mil valores
CACHE = E.PROCESSED / "pam_ce_muni_cultura_ano__sidra.parquet"


def pam_anual(anos=ANOS, preflight: bool = True, cache: Path = CACHE) -> pd.DataFrame:
    """PAM município×cultura×ano do Ceará, via as funções do script 01."""
    if cache.exists():
        df = pd.read_parquet(cache)
        if set(anos) <= set(df["ano"].unique()):
            return df
    s01 = E.carrega_script("data_prep/01_check_dose_variation.py")
    pedacos = []
    for i in range(0, len(anos), BLOCO):
        bloco = tuple(anos[i:i + BLOCO])
        print(f"[rede] SIDRA/PAM {bloco[0]}–{bloco[-1]}")
        # O preflight de códigos roda uma vez; os blocos seguintes o reaproveitam.
        pedacos.append(s01.carrega_pam_sidra(bloco, verificar=preflight and i == 0))
    df = pd.concat(pedacos, ignore_index=True)
    df["extraido_em"] = date.today().isoformat()
    cache.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(cache, index=False)
    return df


def series_por_grupo(anual: pd.DataFrame, rotulo: str, tratados: set[str],
                     com_aeronave: set[str]) -> pd.DataFrame:
    """Área total por ano e grupo, indexada à média da janela da dose (= 100)."""
    d = anual[anual["cultura"] == rotulo].copy()
    cod = d["cod_ibge"].astype(str)
    d["grupo"] = "demais"
    d.loc[cod.isin(tratados), "grupo"] = "decil_sem_aeronave"
    d.loc[cod.isin(tratados & com_aeronave), "grupo"] = "decil_com_aeronave"
    tot = d.groupby(["grupo", "ano"], as_index=False)["area_ha"].sum()
    base = (tot[tot["ano"].isin(JANELA_DOSE)].groupby("grupo")["area_ha"].mean()
            .rename("base"))
    tot = tot.merge(base, on="grupo")
    tot["indice"] = 100 * tot["area_ha"] / tot["base"]
    tot["n_muni"] = tot["grupo"].map(d.groupby("grupo")["cod_ibge"].nunique())
    return tot


def desenha(tot: pd.DataFrame, rotulo: str):
    plt = E.aplica_estilo()
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    estilo = {
        "decil_com_aeronave": ("Decil superior, com aeronave em 2006", E.LARANJA),
        "decil_sem_aeronave": ("Decil superior, sem aeronave", E.AZUL),
        "demais": ("Demais produtores", E.NEUTRO),
    }
    ax.axvspan(JANELA_DOSE[0] - 0.5, JANELA_DOSE[-1] + 0.5, color="#f1f1f1", zorder=0)
    ax.text(sum(JANELA_DOSE) / 4, 0.02, "janela da dose\n(média = 100)", ha="center",
            va="bottom", fontsize=7.5, color=E.CINZA,
            transform=ax.get_xaxis_transform())
    ax.axhline(100, color=E.NEUTRO, linewidth=0.6)
    for x, txt, cor in ((2015 + 54 / 365, "PL 18/2015\n(24/02/2015)", E.TINTA),
                        (2019 + 8 / 365, "ban em vigor\n(09/01/2019)", E.VERMELHO)):
        ax.axvline(x, color=cor, linewidth=0.9, linestyle=(0, (4, 2)))
        ax.text(x + 0.08, 0.985, txt, transform=ax.get_xaxis_transform(), va="top",
                fontsize=7.5, color=cor)
    for grupo, (nome, cor) in estilo.items():
        g = tot[tot["grupo"] == grupo].sort_values("ano")
        if g.empty:
            continue
        ax.plot(g["ano"], g["indice"], color=cor, linewidth=2, marker="o", markersize=3.5,
                label=f"{nome} ({int(g['n_muni'].iloc[0])} mun.; "
                      + f"{g['base'].iloc[0]:,.0f} ha)".replace(",", "."))
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.set_xticks(sorted(tot["ano"].unique())[::2])
    ax.set_ylabel(f"{rotulo}: área total do grupo (média 2015–2018 = 100)")
    ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.84), fontsize=7.5, title="Grupo (municípios; área-base)",
              title_fontsize=7.5, alignment="left")
    ax.set_title("A área da cultura-âncora antes e depois da notícia do PL")
    fig.text(0.99, 0.008, "Fonte: PAM/IBGE (SIDRA 1613), área destinada à colheita; "
             "Censo Agropecuário 2006 (SIDRA 1008). Série descritiva, sem contrafactual.",
             ha="right", fontsize=6, color=E.CINZA)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    return fig


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--cultura", required=True, help="Cultura-âncora (sem default).")
    p.add_argument("--pam", type=Path, default=None, help="PAM média 2015–2018 (script 01).")
    p.add_argument("--censo", type=Path,
                   default=E.PROCESSED / "censo_agro_equipamento_ce.csv")
    p.add_argument("--sem-preflight", action="store_true",
                   help="Pula a conferência de códigos na API de metadados do IBGE "
                        "(use só se servicodados.ibge.gov.br estiver inalcançável).")
    p.add_argument("--out-dir", type=Path, default=E.FIG_DIR)
    args = p.parse_args(argv)
    try:
        pam_ce = E.so_ceara(pd.read_parquet(E.pam_real(args.pam)))
    except FileNotFoundError as erro:
        print(f"[erro] {erro}")
        return 1
    rotulo = E.rotulo_unico(pam_ce["cultura"].unique(), args.cultura)
    tratados = E.decil_superior(pam_ce, rotulo)
    com_aeronave: set[str] = set()
    if args.censo.exists():
        censo = pd.read_csv(args.censo, dtype={"cod_ibge7": str})
        com_aeronave = set(censo.loc[censo["aeronave"] > 0, "cod_ibge7"])
    else:
        print(f"[aviso] sem {args.censo.name}: o decil sai sem a divisão por aeronave.")
    anual = pam_anual(preflight=not args.sem_preflight)
    tot = series_por_grupo(anual, rotulo, tratados, com_aeronave)
    print(tot.pivot(index="ano", columns="grupo", values="indice").round(1).to_string())
    E.grava(desenha(tot, rotulo), f"dose_no_tempo__{E.slug(rotulo)}", args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
