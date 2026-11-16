"""E18 — Avião por tipo de agricultura: Censo Agropecuário, familiar × não familiar.

POR QUE ESTE SCRIPT EXISTE
--------------------------

O caminho-alvo do Ensaio 1 é `lei → menos avião → menos deriva → melhor
nascimento` (docs/dag-identificacao.md). O primeiro elo precisa de uma linha de
base: onde havia avião, e de quem era. A tabela 1008 (script 13) conta os
estabelecimentos com aplicação por aeronave; a **2069** abre a mesma contagem
por **agricultura familiar × não familiar** (Lei 11.326), por município. A
**6851** dá, para 2017, o uso de agrotóxico pela mesma tipologia.

Servem a três coisas:

1. **Heterogeneidade** (framework §4.3): a previsão é que o efeito da lei se
   concentre onde a agricultura não familiar aplicava por avião.
2. **O "resto do estado" da diferença tripla** (dag §5.2): municípios sem
   nenhum estabelecimento com aplicação por aeronave em 2006.
3. **Covariável de linha de base** do estimador de Callaway & Sant'Anna.

Tudo aqui é anterior à lei (2019), ao PL (2015) e à seca (2012). Não é desfecho.

⚠️ RESSALVAS, AS MESMAS DO SCRIPT 13
------------------------------------

- A 2069 é de **2006**. O Censo 2017 não repetiu a pergunta sobre equipamento.
- Conta **estabelecimentos**, não área nem voos.
- Um estabelecimento pode declarar mais de um equipamento: as categorias de
  equipamento não somam o total de quem usou agrotóxico.

CONVENÇÃO DE AUSÊNCIA
---------------------

O SIDRA devolve "-" para zero absoluto, "X" para valor inibido (sigilo) e "..."
para não disponível. "-" vira 0; "X" e "..." viram NaN, e o relatório conta
quantos são. Inibido não é zero.

Uso:
    python scripts/data_prep/18_censo_agro_familiar.py            # CE e RN
    python scripts/data_prep/18_censo_agro_familiar.py --ufs 23 24 22
    make censo-agro-familiar

Saída (gitignored): `data/processed/censo_agro_familiar__uf23-24.csv`
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request as urlreq
from datetime import date
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
SAIDA = RAIZ / "data" / "processed"
API = "https://apisidra.ibge.gov.br/values"

# Tabela 2069, Censo Agropecuário 2006. Demais classificações no total.
EQUIPAMENTO = {
    "0": "eq_total",
    "113447": "eq_costal",
    "113448": "eq_estacionario",
    "113449": "eq_tracao",
    "113450": "eq_aeronave",
    "113451": "eq_outro",
    "113452": "eq_nenhum",
}
FAMILIAR_2006 = {"0": "tot", "8864": "naofam", "8865": "fam"}
URL_2069 = (
    "{api}/t/2069/n6/in%20n3%20{ufs}/v/183/p/2006"
    "/c12521/111611"            # usou agrotóxico
    "/c12596/all"               # tipo de equipamento
    "/c12592/113604/c12590/0/c12591/0"
    "/c12896/all"               # agricultura familiar
)

# Tabela 6851, Censo Agropecuário 2017.
TIPOLOGIA_2017 = {"46302": "tot", "46303": "naofam", "46304": "fam"}
USO_2017 = {"46556": "estab", "111611": "usa"}
URL_6851 = (
    "{api}/t/6851/n6/in%20n3%20{ufs}/v/183/p/2017"
    "/c829/46302,46303,46304"
    "/c12521/46556,111611"
    "/c12564/41145/c218/46502/c800/41147/c12598/41141"
)


def valor(v: str) -> float:
    """Converte o campo V do SIDRA. '-' é zero; 'X' e '...' são ausência."""
    v = (v or "").strip()
    if v == "-":
        return 0.0
    if v in {"X", "...", ".."}:
        return float("nan")
    return float(v)


def _get(url: str, timeout: int = 300) -> list[dict]:
    req = urlreq.Request(url, headers={"User-Agent": "python-urllib"})
    with urlreq.urlopen(req, timeout=timeout) as r:
        linhas = json.loads(r.read().decode("utf-8"))
    return linhas[1:]  # a primeira linha é o cabeçalho


def arruma_2069(linhas: list[dict]) -> pd.DataFrame:
    """Uma linha por município: aeronave, costal etc., por tipo de agricultura."""
    reg = []
    for r in linhas:
        eq, fam = EQUIPAMENTO.get(r["D5C"]), FAMILIAR_2006.get(r["D9C"])
        if eq is None or fam is None:
            continue
        reg.append({"cod_ibge7": r["D1C"], "municipio": r["D1N"],
                    "col": f"{eq}_{fam}_2006", "v": valor(r["V"])})
    return _larga(reg)


def arruma_6851(linhas: list[dict]) -> pd.DataFrame:
    reg = []
    for r in linhas:
        tip, uso = TIPOLOGIA_2017.get(r["D4C"]), USO_2017.get(r["D5C"])
        if tip is None or uso is None:
            continue
        reg.append({"cod_ibge7": r["D1C"], "municipio": r["D1N"],
                    "col": f"{uso}_{tip}_2017", "v": valor(r["V"])})
    return _larga(reg)


def _larga(reg: list[dict]) -> pd.DataFrame:
    if not reg:
        raise ValueError("o SIDRA não devolveu nenhuma linha reconhecida")
    longo = pd.DataFrame(reg)
    if longo.duplicated(["cod_ibge7", "col"]).any():
        raise ValueError("município × coluna repetido: a consulta não fixou "
                         "alguma classificação no total")
    # `pivot`, não `pivot_table`: preserva NaN de valor inibido e falha se a
    # chave não for única, em vez de agregar em silêncio.
    larga = longo.pivot(index="cod_ibge7", columns="col", values="v")
    larga.columns.name = None
    nomes = longo.drop_duplicates("cod_ibge7").set_index("cod_ibge7")["municipio"]
    larga.insert(0, "municipio", nomes)
    return larga.reset_index()


def deriva(tb: pd.DataFrame) -> pd.DataFrame:
    """Indicadores de linha de base. Razão sobre denominador zero fica NaN."""
    tb = tb.copy()
    tb["cod_ibge6"] = tb["cod_ibge7"].str[:6]
    tb["uf"] = tb["cod_ibge7"].str[:2]
    tb["tinha_aeronave_2006"] = tb["eq_aeronave_tot_2006"] > 0
    den = tb["estab_tot_2017"].where(tb["estab_tot_2017"] > 0)
    tb["share_naofam_estab_2017"] = tb["estab_naofam_2017"] / den
    for g in ("fam", "naofam"):
        d = tb[f"estab_{g}_2017"].where(tb[f"estab_{g}_2017"] > 0)
        tb[f"share_usa_{g}_2017"] = tb[f"usa_{g}_2017"] / d
    return tb


def confere_ufs(tb: pd.DataFrame, ufs: list[str]) -> None:
    """Faltar UMA das UFs pedidas é erro, não tabela menor (doc 15 §4.1)."""
    veio = set(tb["cod_ibge7"].str[:2])
    falta = [u for u in ufs if u not in veio]
    if falta:
        raise RuntimeError(f"UF(s) pedida(s) e ausente(s) na resposta: {falta}")


def monta(ufs: list[str]) -> pd.DataFrame:
    lista = ",".join(ufs)
    t06 = arruma_2069(_get(URL_2069.format(api=API, ufs=lista)))
    t17 = arruma_6851(_get(URL_6851.format(api=API, ufs=lista)))
    confere_ufs(t06, ufs)
    confere_ufs(t17, ufs)
    tb = t06.merge(t17.drop(columns="municipio"), on="cod_ibge7",
                   how="outer", validate="one_to_one")
    return deriva(tb)


def relata(tb: pd.DataFrame) -> None:
    barra = "=" * 78
    print(barra)
    print("AVIÃO POR TIPO DE AGRICULTURA — Censo Agro 2006 (2069) e 2017 (6851)")
    print(barra)
    for uf, g in tb.groupby("uf"):
        aero = g[g["tinha_aeronave_2006"]]
        print(f"\nUF {uf}: {len(g)} municípios; {len(aero)} com aplicação por aeronave em 2006")
        print(f"  estabelecimentos com aeronave: total {g['eq_aeronave_tot_2006'].sum():.0f}"
              f" | não familiar {g['eq_aeronave_naofam_2006'].sum(skipna=True):.0f}"
              f" | familiar {g['eq_aeronave_fam_2006'].sum(skipna=True):.0f}")
        inib = int(g[["eq_aeronave_naofam_2006", "eq_aeronave_fam_2006"]].isna().any(axis=1).sum())
        if inib:
            print(f"  ⚠️ {inib} município(s) com a abertura familiar/não familiar inibida ou ausente")
        cols = ["municipio", "eq_aeronave_tot_2006", "eq_aeronave_naofam_2006",
                "eq_aeronave_fam_2006", "eq_costal_tot_2006", "share_naofam_estab_2017"]
        if len(aero):
            print(aero.sort_values("eq_aeronave_tot_2006", ascending=False)[cols]
                  .to_string(index=False, float_format=lambda x: f"{x:.3g}"))
    print(f"\nExtraído em {date.today().isoformat()} de {API}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ufs", nargs="+", default=["23", "24"])
    ap.add_argument("--saida", type=Path, default=None)
    a = ap.parse_args(argv)
    ufs = sorted(a.ufs)
    tb = monta(ufs)
    destino = a.saida or SAIDA / f"censo_agro_familiar__uf{'-'.join(ufs)}.csv"
    destino.parent.mkdir(parents=True, exist_ok=True)
    tb.to_csv(destino, index=False)
    relata(tb)
    print(f"gravado: {destino.relative_to(RAIZ) if destino.is_relative_to(RAIZ) else destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
