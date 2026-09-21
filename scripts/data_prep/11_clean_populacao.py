"""População residente municipal — o denominador que falta ao canal A5.

`docs/lacunas-de-dados.md` lista, na Classe B: *"População municipal (IBGE) —
denominador do canal de intoxicação | ingestor existe? ❌"*. Sem ela o canal de
intoxicação entrega **contagem**, não taxa, e a matriz de degradação da §2 diz o
que se perde: *"taxas; a comparação entre municípios de porte diferente"*.

⚠️ **E o porte não é detalhe neste desenho.** O script 07 mostrou que a DP das
tendências municipais é governada por porte — 68,2 g nos municípios de menos de
150 nascimentos/ano contra 17,9 g nos de 800 ou mais. Comparar contagem de
intoxicação entre municípios de porte diferente mistura exposição com tamanho,
exatamente como a DP não ponderada misturava heterogeneidade com ruído.

Fonte: **SIDRA tabela 6579** — "População residente estimada", variável 9324,
nível N6 (municípios), 2001–2026. Cobre a janela inteira com folga.

⚠️ **O que esta série é, e o que não é.** São **estimativas** do IBGE entre
censos, não contagem. Para 2015–2022 isso significa projeção a partir do Censo
2010 até 2021, e a partir do Censo 2022 depois — há uma descontinuidade
metodológica no meio da janela. Ela não invalida o denominador, mas o texto tem
de dizer que taxas de antes e depois de 2022 não são estritamente comparáveis.

Saída anual, de propósito: o painel é mensal, e repetir população mensal
inventaria variação que não existe. O `05_build_panel.py` junta por
(`cod_ibge6`, `ano`).
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

TABELA = "6579"
VARIAVEL = "9324"

# ⚠️ ANO CENSITÁRIO NÃO TEM ESTIMATIVA. Conferido rodando em 2026-09-21: a
# tabela 6579 devolve **zero registros** para 2022 — o IBGE não estima no ano em
# que conta. Sem o recurso abaixo, o último ano do painel sairia com denominador
# NaN, e a taxa de intoxicação de 2022 sumiria em silêncio.
#
# O Censo 2022 está na tabela 4709, variável 93 ("População residente").
TABELA_CENSO = "4709"
VARIAVEL_CENSO = "93"
ANOS_CENSITARIOS = {2022: (TABELA_CENSO, VARIAVEL_CENSO)}
UF_CEARA_N3 = "23"
ANOS_PADRAO = (2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)
OUT_DIR = Path("data/processed")
NOME_SAIDA = "populacao_ce_muni_ano"
SEED = 20190613
N_MUNICIPIOS_CE = 184

API_VALORES = "https://apisidra.ibge.gov.br/values"
API_METADADOS = "https://servicodados.ibge.gov.br/api/v3/agregados/{t}/metadados"


def _saida_utf8() -> None:
    """Força UTF-8 na saída antes de qualquer print.

    Mesmo guarda dos scripts 01–10: no Windows o pipe usa a codepage da locale
    (cp1252), que não encoda ─ ⚠ ✔ ✘, e o script morreria DEPOIS do trabalho.
    """
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def _http(url: str, timeout: int = 120) -> str:
    """GET com descompressão manual de gzip.

    ⚠️ As APIs do IBGE respondem **gzip mesmo sem `Accept-Encoding: gzip`**, e
    o `urllib` não descomprime sozinho. Sem isto o `.decode` morre em `0x8b` —
    o segundo byte do número mágico — com mensagem que parece erro de
    codificação de texto e não é. Mesmo achado dos scripts 08 e 09.
    """
    req = urllib.request.Request(url, headers={"User-Agent": "pesquisa-academica"})
    with urllib.request.urlopen(req, timeout=timeout) as resposta:
        corpo = resposta.read()
    if corpo[:2] == b"\x1f\x8b":
        corpo = gzip.decompress(corpo)
    return corpo.decode("utf-8", errors="replace")


def verifica_codigos(timeout: int = 60) -> dict:
    """Preflight: a tabela, a variável e o nível territorial existem?

    ⚠️ Pela mesma razão do preflight do script 01: **código errado no SIDRA
    devolve vazio, não erro.** Um `v/9324` que mudasse de número produziria
    "nenhuma população encontrada", e o painel sairia sem denominador — com o
    canal de intoxicação virando contagem outra vez, em silêncio.
    """
    meta = json.loads(_http(API_METADADOS.format(t=TABELA), timeout))
    variaveis = {str(v["id"]): v["nome"] for v in meta.get("variaveis", [])}
    niveis = meta.get("nivelTerritorial", {}).get("Administrativo", [])
    periodo = meta.get("periodicidade", {})
    return {
        "tabela_nome": meta.get("nome", "?"),
        "variavel_ok": VARIAVEL in variaveis,
        "variavel_nome": variaveis.get(VARIAVEL, "(não encontrada)"),
        "n6_ok": "N6" in niveis,
        "inicio": periodo.get("inicio"),
        "fim": periodo.get("fim"),
    }


def imprime_preflight(rel: dict) -> bool:
    barra = "=" * 84
    print(barra)
    print("PREFLIGHT — os códigos da tabela de população existem no IBGE?")
    print(barra)
    print(f"tabela {TABELA} — {rel['tabela_nome'][:70]}")
    marca = "✔" if rel["variavel_ok"] else "✘"
    print(f"  {marca} variável {VARIAVEL}: {rel['variavel_nome']}")
    marca = "✔" if rel["n6_ok"] else "✘"
    print(f"  {marca} nível N6 (municípios)")
    print(f"  ⓘ período coberto: {rel['inicio']} – {rel['fim']}")
    ok = rel["variavel_ok"] and rel["n6_ok"]
    print(barra)
    print("Todos os códigos conferem." if ok else
          "⚠️ CÓDIGO NÃO CONFERE — não baixe: o resultado viria vazio, não com erro.")
    print(barra)
    return ok


def _consulta(tabela: str, variavel: str, anos, timeout: int) -> list[dict]:
    """`n6/in n3 23` = todos os municípios da UF 23. Devolve [] se vier vazio."""
    periodo = ",".join(str(a) for a in anos)
    caminho = (f"/t/{tabela}/n6/{urllib.parse.quote(f'in n3 {UF_CEARA_N3}')}"
               f"/v/{variavel}/p/{periodo}")
    bruto = json.loads(_http(API_VALORES + caminho, timeout))
    return bruto[1:] if len(bruto) > 1 else []


def carrega_sidra(anos=ANOS_PADRAO, timeout: int = 180) -> pd.DataFrame:
    """População por ano, tirando cada ano da tabela que de fato o tem.

    ⚠️ **Duas fontes, e a distinção viaja NA TABELA, não só na documentação.**
    A coluna `origem` separa `estimativa` de `censo` porque a descontinuidade é
    grande — Abaiara sai de 11.483 estimados em 2016 para 10.038 contados em
    2022, ~13% — e uma taxa que cruze o corte sem saber disso atribui à política
    o que é mudança de metodologia. Guardar a origem só no docstring seria
    repetir o erro do `ban_municipal_confianca`: perder a distinção na fronteira
    entre arquivos.
    """
    anos_censo = [a for a in anos if a in ANOS_CENSITARIOS]
    anos_est = [a for a in anos if a not in ANOS_CENSITARIOS]

    pedacos = []
    if anos_est:
        registros = _consulta(TABELA, VARIAVEL, anos_est, timeout)
        if not registros:
            raise RuntimeError(
                "SIDRA devolveu só o cabeçalho para as estimativas. "
                "Confira os códigos com --verificar-codigos.")
        bloco = _sidra_para_longo(registros)
        bloco["origem"] = "estimativa"
        pedacos.append(bloco)

    for ano in anos_censo:
        tabela, variavel = ANOS_CENSITARIOS[ano]
        registros = _consulta(tabela, variavel, [ano], timeout)
        if not registros:
            print(f"  ⚠️ {ano} é ano censitário e a tabela {tabela} também veio "
                  f"vazia — o ano fica SEM denominador.")
            continue
        bloco = _sidra_para_longo(registros)
        bloco["origem"] = "censo"
        pedacos.append(bloco)
        print(f"  ⓘ {ano}: sem estimativa (ano censitário) — usado o Censo "
              f"(tabela {tabela}).")

    if not pedacos:
        raise RuntimeError("nenhuma das tabelas devolveu dado.")
    return (pd.concat(pedacos, ignore_index=True)
            .sort_values(["cod_ibge6", "ano"]).reset_index(drop=True))


def _sidra_para_longo(registros: list[dict]) -> pd.DataFrame:
    """Converte a resposta do SIDRA no formato do painel.

    ⚠️ `D1C` traz o código IBGE de **7 dígitos**; `cod_ibge6` tem 6. Mesma
    truncagem obrigatória do `ID_MUNICIP` no script 10 e do `add_dv` no SINASC.
    """
    linhas = []
    for r in registros:
        valor = str(r.get("V", "")).strip()
        if valor in ("", "-", "..", "...", "X"):   # códigos de ausência do SIDRA
            continue
        cod7 = str(r.get("D1C", "")).strip()
        linhas.append({
            "cod_ibge": cod7,
            "cod_ibge6": cod7[:6],
            "ano": int(str(r.get("D3N", "")).strip()),
            "populacao": int(float(valor)),
        })
    return pd.DataFrame(linhas).sort_values(["cod_ibge6", "ano"]).reset_index(drop=True)


def simula_populacao(anos=ANOS_PADRAO, seed: int = SEED) -> pd.DataFrame:
    """Dado sintético para validar a fiação sem tocar a rede.

    ⚠️ Não é evidência sobre nada. A distribuição imita a do Ceará — mediana
    baixa, cauda longa — só para que o código exercite os mesmos caminhos.
    """
    rng = np.random.default_rng(seed)
    base = rng.lognormal(mean=9.6, sigma=0.9, size=N_MUNICIPIOS_CE).astype(int) + 2000
    linhas = []
    for i, pop0 in enumerate(base):
        for k, ano in enumerate(anos):
            linhas.append({"cod_ibge": f"23{i:04d}0", "cod_ibge6": f"23{i:04d}",
                           "ano": ano, "populacao": int(pop0 * (1.008 ** k)),
                           "origem": "censo" if ano in ANOS_CENSITARIOS
                                     else "estimativa"})
    return pd.DataFrame(linhas)


def imprime_resumo(pop: pd.DataFrame, fonte: str) -> None:
    barra = "=" * 84
    print(barra)
    print(f"POPULAÇÃO MUNICIPAL — CE | fonte: {fonte}")
    print(barra)
    n_muni = pop["cod_ibge6"].nunique()
    anos = sorted(pop["ano"].unique())
    print(f"  municípios         : {n_muni:>6}"
          + ("" if n_muni == N_MUNICIPIOS_CE else f"  ⚠️ esperado {N_MUNICIPIOS_CE}"))
    print(f"  anos               : {anos[0]}–{anos[-1]} ({len(anos)})")
    print(f"  células            : {len(pop):>6}")

    faltas = [a for a in anos if pop[pop["ano"] == a]["cod_ibge6"].nunique() < n_muni]
    if faltas:
        print(f"  ⚠️ anos com município faltando: {faltas}")

    if "origem" in pop.columns:
        print()
        print("  origem do número, por ano:")
        for ano in anos:
            origens = sorted(pop[pop["ano"] == ano]["origem"].unique())
            marca = "⚠️" if "censo" in origens else "  "
            print(f"    {marca} {ano}: {', '.join(origens)}")

    ultimo = pop[pop["ano"] == anos[-1]]
    print()
    print(f"  em {anos[-1]}:")
    print(f"    população total  : {int(ultimo['populacao'].sum()):>10,}".replace(",", "."))
    print(f"    mediana municipal: {int(ultimo['populacao'].median()):>10,}".replace(",", "."))
    print(f"    menor / maior    : {int(ultimo['populacao'].min()):,}".replace(",", ".")
          + f" / {int(ultimo['populacao'].max()):,}".replace(",", "."))
    print()
    print(barra)
    print("COMO LER — e o que este script NÃO diz")
    print(barra)
    print("  • São ESTIMATIVAS intercensitárias, não contagem.")
    print("  • ⚠️ Há descontinuidade metodológica: até 2021 a projeção parte do")
    print("    Censo 2010; de 2022 em diante, do Censo 2022. Taxas de antes e")
    print("    depois não são estritamente comparáveis, e o texto tem de dizer.")
    print("  • Série ANUAL de propósito. Repetir mês a mês inventaria variação")
    print("    que não existe; o painel junta por (cod_ibge6, ano).")
    print("  • Nada aqui é resultado do ban. É denominador.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--fonte", choices=("auto", "sidra", "simulado"), default="auto")
    p.add_argument("--anos", type=int, nargs="*", default=list(ANOS_PADRAO))
    p.add_argument("--verificar-codigos", action="store_true",
                   help="só confere os códigos contra a API de metadados; não baixa")
    p.add_argument("--seed", type=int, default=SEED)
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    if args.verificar_codigos:
        return 0 if imprime_preflight(verifica_codigos()) else 1

    if args.fonte == "simulado":
        pop, fonte = simula_populacao(tuple(args.anos), args.seed), "simulado"
    else:
        try:
            if not imprime_preflight(verifica_codigos()):
                return 1
            pop, fonte = carrega_sidra(tuple(args.anos)), "sidra"
        except Exception as erro:
            if args.fonte == "sidra":
                print(f"  ✘ SIDRA falhou: {erro}")
                return 1
            print(f"  ⚠️ SIDRA indisponível ({erro}); caindo no simulado.")
            pop, fonte = simula_populacao(tuple(args.anos), args.seed), "simulado"

    if pop.empty:
        print("  ✘ Nenhuma linha de população. O resultado do SIDRA veio vazio —")
        print("    confira os códigos com --verificar-codigos.")
        return 1

    pop["fonte"] = fonte
    imprime_resumo(pop, fonte)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    sufixo = "" if fonte != "simulado" else "__simulado"
    destino = args.out_dir / f"{NOME_SAIDA}{sufixo}.parquet"
    pop.to_parquet(destino, index=False)
    print(f"\n[ok] população -> {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
