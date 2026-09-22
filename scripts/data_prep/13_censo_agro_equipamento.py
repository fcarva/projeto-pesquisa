"""E12 — Quem de fato pulverizava por avião: Censo Agropecuário, equipamento.

POR QUE ESTE SCRIPT EXISTE
--------------------------

Saiu de uma busca pelo lado do CUSTO do Ensaio 2 (a heterogeneidade do custo de
conversão, que decide `c = C''` na regra de Weitzman) e acabou encontrando coisa
que morde o Ensaio 1 muito mais fundo.

A tabela 1008 do SIDRA traz **"Número de estabelecimentos agropecuários com uso
de agrotóxicos por tipo de equipamento utilizado na aplicação"**, com a categoria
**"Por aeronave"** separada de "Equipamento de tração mecânica e/ou animal", e
desce a município.

⚠️ E O QUE ELA MOSTRA NO CEARÁ
-------------------------------

No estado inteiro, **36 estabelecimentos** usavam aeronave, contra 105.624 com
pulverizador costal — 95,8% do total. Os 36 estão em **sete** municípios, e dois
deles concentram 75%: Limoeiro do Norte (18) e Quixeré (9).

Isso põe três coisas em cima da mesa, e nenhuma é sobre custo:

1. ✅ **Nenhum município com aeronave tem dose zero.** O grupo de comparação não
   está contaminado por usuários de aeronave — é verificação direta da flag 5,
   e ela passa aqui.

2. ⚠️ **Diluição do tratamento.** Dos 19 municípios do decil superior da banana,
   **17 não tinham aeronave alguma**. O `d` alto está sendo atribuído a
   municípios onde o tratamento — remover a pulverização aérea — não tinha o que
   remover. Isso atenua o ATT por construção, e é problema de DEFINIÇÃO de
   tratamento, não de poder estatístico.

3. ⚠️ **E compõe com a flag 0.** Das 27 aeronaves dentro do decil superior, 18
   são de Limoeiro do Norte, que proibiu a pulverização aérea em 2009. Sobram
   **9 aeronaves em Quixeré** como tratamento genuinamente novo em 2019.

⚠️ AS RESSALVAS, QUE SÃO SÉRIAS
--------------------------------

- **O dado é de 2006**, treze anos antes do ban. A aviação agrícola brasileira
  cresceu no período. ⚠️ O Censo 2017 **não publicou** esse corte no SIDRA —
  conferido: as oito tabelas com "equipamento" + "aplicação" são todas de 2006.
- **Conta estabelecimentos, não área nem voos.** Trinta e seis estabelecimentos
  podem cobrir área grande.
- Declaração do informante, com subdeclaração provável em prática regulada.

Nada aqui substitui a variável de dose. O que isto faz é dar uma **medida
direta** do que a dose tenta aproximar, e a distância entre as duas é
informação.

Saída: `data/processed/censo_agro_equipamento_ce.csv`
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
import time
import urllib.request as urlreq
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimate"))
from importlib import import_module

_saida_utf8 = import_module("04_robustness")._saida_utf8

RAIZ = Path(__file__).resolve().parents[2]
OUT_DIR = RAIZ / "data" / "processed"
PAINEL = OUT_DIR / "painel_ensaio1.parquet"

UA = {"User-Agent": "projeto-pesquisa/1.0 (pesquisa academica)"}
TABELA, PERIODO, VARIAVEL = 1008, "2006", "2020"

EQUIPAMENTOS = {
    "118149": "total",
    "113447": "costal",
    "113449": "tracao_mecanica",
    "113450": "aeronave",
    "118150": "outro",
}


def _get(url: str, timeout: int = 300):
    """⚠️ O IBGE devolve gzip mesmo sem pedir. Cheque o magic byte, não o header:
    o header mente, e o sintoma é UnicodeDecodeError em 0x8b."""
    b = urlreq.urlopen(urlreq.Request(url, headers=UA), timeout=timeout).read()
    if b[:2] == b"\x1f\x8b":
        b = gzip.decompress(b)
    return json.loads(b.decode("utf-8"))


def municipios_ce() -> list[str]:
    """Códigos de SETE dígitos. ⚠️ Com seis a API devolve HTTP 500, não vazio."""
    ms = _get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/23/municipios")
    return [str(m["id"]) for m in ms]


def baixa(ids: list[str], chunk: int = 25, pausa: float = 0.3) -> pd.DataFrame:
    cats = ",".join(EQUIPAMENTOS)
    linhas: dict[tuple[str, str], float] = {}
    nomes: dict[str, str] = {}
    falhas = 0
    for k in range(0, len(ids), chunk):
        loc = ",".join(ids[k:k + chunk])
        url = (f"https://servicodados.ibge.gov.br/api/v3/agregados/{TABELA}"
               f"/periodos/{PERIODO}/variaveis/{VARIAVEL}"
               f"?localidades=N6[{loc}]&classificacao=12596[{cats}]")
        try:
            d = _get(url)
        except Exception:
            falhas += 1
            continue
        if not d or not d[0].get("resultados"):
            continue
        for r in d[0]["resultados"]:
            cid = next(iter(r["classificacoes"][0]["categoria"]))
            rot = EQUIPAMENTOS.get(cid, cid)
            for s in r["series"]:
                mid = str(s["localidade"]["id"])
                nomes[mid] = s["localidade"]["nome"]
                try:
                    linhas[(mid, rot)] = float(s["serie"].get(PERIODO))
                except (TypeError, ValueError):
                    linhas[(mid, rot)] = 0.0
        time.sleep(pausa)

    if falhas:
        print(f"  ⚠️ {falhas} blocos falharam — a soma abaixo é PARCIAL.")
    if not linhas:
        return pd.DataFrame()

    tb = (pd.Series(linhas).unstack(fill_value=0.0)
          .rename_axis("cod_ibge7").reset_index())
    tb["municipio"] = tb["cod_ibge7"].map(nomes)
    tb["cod_ibge6"] = tb["cod_ibge7"].str[:6]
    for c in EQUIPAMENTOS.values():
        if c not in tb.columns:
            tb[c] = 0.0
    return tb


def confronta(tb: pd.DataFrame, painel: Path) -> pd.DataFrame | None:
    if not painel.exists():
        print("  ⚠️ painel ausente — pulando o confronto com a dose.")
        return None
    pn = pd.read_parquet(painel)
    d = (pn.groupby("cod_ibge6")
           .agg(dose=("dose", "first"), dose_ha=("dose_ha", "first"))
           .reset_index())
    d["cod_ibge6"] = d["cod_ibge6"].astype(str)
    m = d.merge(tb[["cod_ibge6", "municipio", "aeronave", "tracao_mecanica",
                    "costal", "total"]], on="cod_ibge6", how="left")
    for c in ("aeronave", "tracao_mecanica", "costal", "total"):
        m[c] = m[c].fillna(0.0)
    m["rank_dose"] = m["dose"].rank(ascending=False, method="min").astype(int)
    m["decil_superior"] = m["dose"] >= m["dose"].quantile(0.9)
    return m


def relata(tb: pd.DataFrame, m: pd.DataFrame | None) -> None:
    barra = "=" * 84
    print(barra)
    print(f"E12 — EQUIPAMENTO DE APLICAÇÃO, CENSO AGROPECUÁRIO {PERIODO} (CE)")
    print(barra)
    tot = {c: tb[c].sum() for c in EQUIPAMENTOS.values()}
    print(f"  estabelecimentos com uso de agrotóxico : {tot['total']:>10,.0f}")
    for c, rot in [("costal", "pulverizador costal"),
                   ("tracao_mecanica", "tração mecânica/animal"),
                   ("aeronave", "POR AERONAVE")]:
        pct = 100 * tot[c] / tot["total"] if tot["total"] else 0
        print(f"  {rot:<38} {tot[c]:>10,.0f}   ({pct:5.2f}%)")
    print()
    av = tb[tb["aeronave"] > 0].sort_values("aeronave", ascending=False)
    print(f"  ⚠️ A aeronave está em {len(av)} de {len(tb)} municípios.")
    for _, r in av.iterrows():
        print(f"     {r['municipio'][:32]:<32} {r['aeronave']:>4.0f}")
    if len(av) >= 2:
        top2 = av["aeronave"].head(2).sum()
        print(f"     os dois maiores concentram {top2:.0f} de {tot['aeronave']:.0f} "
              f"({100*top2/tot['aeronave']:.0f}%)")
    print("-" * 84)

    if m is None:
        print(barra)
        return

    print("O CONFRONTO COM A DOSE — e é aqui que o achado morde o Ensaio 1")
    print()
    print(f"  {'município':<24} {'aero':>5} {'dose':>9} {'ha':>7} {'rank':>6}  decil")
    print("  " + "-" * 62)
    for _, r in m[m["aeronave"] > 0].sort_values("aeronave", ascending=False).iterrows():
        nome = (r["municipio"] or r["cod_ibge6"])[:24]
        print(f"  {nome:<24} {r['aeronave']:>5.0f} {r['dose']:>9.5f} "
              f"{r['dose_ha']:>7.0f} {r['rank_dose']:>4}/{len(m)}"
              f"  {'SIM' if r['decil_superior'] else ''}")
    print()

    zero_com_aero = int(((m["dose"] == 0) & (m["aeronave"] > 0)).sum())
    dec = m[m["decil_superior"]]
    sem_aero = int((dec["aeronave"] == 0).sum())
    cap = dec["aeronave"].sum()
    tot_a = m["aeronave"].sum()

    if zero_com_aero == 0:
        print("  ✅ NENHUM município de dose zero tinha aeronave.")
        print("     O grupo de comparação não está contaminado por usuário de")
        print("     aeronave. É verificação direta da flag 5, e ela passa aqui.")
    else:
        print(f"  ⚠️ {zero_com_aero} município(s) de dose ZERO tinham aeronave —")
        print("     o grupo de comparação está contaminado. Flag 5 confirmada.")
    print()
    print(f"  ⚠️ DILUIÇÃO DO TRATAMENTO: {sem_aero} dos {len(dec)} municípios do")
    print("     decil superior da banana NÃO tinham aeronave alguma.")
    print(f"     O decil captura {cap:.0f} de {tot_a:.0f} aeronaves "
          f"({100*cap/tot_a if tot_a else 0:.0f}%), mas o faz atribuindo dose alta")
    print("     a municípios onde não havia pulverização aérea a remover.")
    print()
    print("     Isso atenua o ATT POR CONSTRUÇÃO, e é problema de DEFINIÇÃO de")
    print("     tratamento — não de poder estatístico. A leitura da §6 do paper")
    print("     muda: parte do que se lia como 'desenho sem poder' pode ser")
    print("     'tratamento medido no lugar errado'.")
    print()
    corr = m[m["dose"] > 0][["dose", "aeronave"]].corr().iloc[0, 1]
    print(f"  correlação dose × aeronaves (entre os de dose > 0): {corr:.3f}")
    print("-" * 84)
    print("⚠️ RESSALVAS — e elas são sérias")
    print(f"  1. O dado é de {PERIODO}, treze anos antes do ban. O Censo 2017 NÃO")
    print("     publicou esse corte: as oito tabelas de equipamento são de 2006.")
    print("  2. Conta ESTABELECIMENTOS, não área nem número de voos.")
    print("  3. É declaração do informante, em prática regulada.")
    print()
    print("  Isto NÃO substitui a variável de dose. Dá uma medida DIRETA do que a")
    print("  dose aproxima, e a distância entre as duas é que é o achado.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--painel", type=Path, default=PAINEL)
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    p.add_argument("--chunk", type=int, default=25)
    args = p.parse_args(argv)

    print(f"  baixando SIDRA {TABELA}/{PERIODO} para os municípios do CE...")
    try:
        ids = municipios_ce()
    except Exception as e:
        print(f"✘ não foi possível listar os municípios: {type(e).__name__}")
        return 1
    tb = baixa(ids, chunk=args.chunk)
    if tb.empty:
        print("✘ nenhum dado retornado.")
        return 1

    relata(tb, confronta(tb, args.painel))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / "censo_agro_equipamento_ce.csv"
    tb.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}  ({len(tb)} municípios)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
