#!/usr/bin/env python3
"""Tarefa 7 — A DP das tendências municipais é ruído amostral ou heterogeneidade real?

POR QUE ESTE SCRIPT EXISTE
--------------------------
O gate E1.5 (`docs/ars/04-roteiro-qualificacao.md`) declara que o parâmetro que
decide a detectabilidade do Ensaio 1 **não** é a dispersão de dose no PAM, e sim
o **desvio-padrão das tendências municipais do desfecho no pré-período**. O
script 01 já o reporta como `sd_tendencia_g` e o usa para o MDE agrupado.

⚠️ **Mas o número que o 01 calcula é NÃO PONDERADO entre municípios**, e o Ceará
tem 184 municípios cuja mediana é de ~283 nascimentos/ano. Um município de 30
nascimentos/mês tem média mensal ruidosa por amostragem pura, e entra na conta
com o mesmo peso de Fortaleza. Então `sd_tendencia_g` mistura duas coisas que
têm consequências opostas para o desenho:

  • **ruído amostral** — encolhe com ponderação por nascimento e com corte de
    porte; é artefato de medida, não propriedade do mundo;
  • **heterogeneidade real** — não encolhe com nada disso, e é ela que governa
    o MDE de verdade.

Se o MDE for calculado sobre a soma das duas, o desenho é declarado inviável por
uma razão que em parte não existe. Se for calculado ignorando o ruído, a precisão
é exagerada. Este script separa as duas e mostra o que cada hipótese implica.

⚠️ **O QUE ESTE SCRIPT NÃO FAZ.** Não escolhe a ponderação, não escolhe corte de
porte e não declara o gate aprovado. Ele mede; a decisão é do pesquisador, e o
roteiro pede que ela seja registrada com data antes de qualquer estimação.

MÉTODO
------
Parte a janela pré-ban ao meio (2015–2016 vs. 2017–2018) e mede, por município,
a variação do peso médio. No pré-período não há tratamento: essa variação é
placebo. Para cada município i, a variância da diferença de médias tem uma parte
que é aritmética de amostragem, conhecida sem suposição nenhuma:

    Var_amostral(i) = s_i² · (1/n_i,ini + 1/n_i,fim)

com s_i² a variância individual do peso dentro do município. A média dessas
variâncias é o piso de ruído; o que sobra da variância observada é o sinal:

    Var_real = Var_observada − média(Var_amostral)

Uso:
    python scripts/data_prep/07_diagnose_trend_sd.py                  # usa o cache do pysus
    python scripts/data_prep/07_diagnose_trend_sd.py --caminho data/raw/sinasc_ce_*.csv.gz
    python scripts/data_prep/07_diagnose_trend_sd.py --efeito-esperado-g 20

Saída: data/processed/diagnostico_dp_tendencias.csv (gitignored).
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

ANOS_PRE = (2015, 2016, 2017, 2018)
UF_CEARA = "23"
CODMUNRES_DESCONHECIDO = "230000"
PESO_MIN_G, PESO_MAX_G = 200, 8000
OUT_DIR = Path("data/processed")
Z_PODER = 2.8  # 1,96 (tamanho) + 0,84 (poder de 80%), igual ao script 01
EFEITO_ESPERADO_G = 15.0

# Estratos de porte. O piso de 800/ano é o do cálculo do roteiro; os demais
# existem para mostrar como o ruído escala, não porque tenham significado.
ESTRATOS = ((0, 150), (150, 300), (300, 800), (800, 10**9))


def carrega_microdado_pysus(anos=ANOS_PRE) -> pd.DataFrame:
    """Peso individual do SINASC/CE. Usa o cache local do pysus quando já baixado.

    ⚠️ `Parquet.load()` é corotina em pysus 2.10.0 — ver a nota em
    `02_clean_births.py`. Este script repete o padrão de propósito, para não
    depender da ordem em que os scripts são rodados.
    """
    from pysus.api import PySUSClient

    pedacos = []
    with PySUSClient() as client:
        ftp = client.get_ftp()
        base = next(d for d in client._run_async(ftp.datasets()) if d.name == "SINASC")
        for ano in anos:
            for arquivo in client._run_async(base.search(state="CE", year=ano)):
                parquet = client.download_to_parquet(arquivo)
                bloco = client._run_async(parquet.load())
                bloco = bloco[["CODMUNRES", "PESO"]].copy()
                bloco["ano"] = ano
                pedacos.append(bloco)
    if not pedacos:
        raise RuntimeError("pysus não devolveu arquivos SINASC para CE.")
    return pd.concat(pedacos, ignore_index=True)


def carrega_microdado_arquivos(caminhos: list[str]) -> pd.DataFrame:
    pedacos = []
    for padrao in caminhos:
        for caminho in sorted(Path().glob(padrao)) or [Path(padrao)]:
            if caminho.suffix == ".parquet":
                bloco = pd.read_parquet(caminho)
            else:
                bloco = pd.read_csv(caminho, low_memory=False)
            colunas = {c.upper(): c for c in bloco.columns}
            bloco = bloco.rename(columns={colunas.get("CODMUNRES", ""): "CODMUNRES",
                                          colunas.get("PESO", ""): "PESO"})
            if "ano" not in bloco.columns:
                dtnasc = colunas.get("DTNASC")
                if dtnasc is None:
                    raise ValueError(f"{caminho}: sem coluna de ano nem DTNASC.")
                bloco["ano"] = bloco[dtnasc].astype(str).str[-4:].astype(int)
            pedacos.append(bloco[["CODMUNRES", "PESO", "ano"]])
    if not pedacos:
        raise FileNotFoundError(f"Nenhum arquivo casou com {caminhos}.")
    return pd.concat(pedacos, ignore_index=True)


def limpa(bruto: pd.DataFrame, anos=ANOS_PRE) -> pd.DataFrame:
    d = bruto.copy()
    d["PESO"] = pd.to_numeric(d["PESO"], errors="coerce")
    d["cod_ibge6"] = d["CODMUNRES"].astype(str).str.strip().str.zfill(6)
    d = d[d["ano"].isin(anos)]
    d = d[(d["PESO"] >= PESO_MIN_G) & (d["PESO"] <= PESO_MAX_G)]
    d = d[d["cod_ibge6"].str.startswith(UF_CEARA)]
    d = d[d["cod_ibge6"] != CODMUNRES_DESCONHECIDO]
    return d[["cod_ibge6", "ano", "PESO"]]


def decompoe(d: pd.DataFrame, anos=ANOS_PRE) -> tuple[pd.DataFrame, dict]:
    """Separa a variância das tendências em ruído amostral e heterogeneidade real."""
    metade = min(anos) + (max(anos) - min(anos)) // 2
    d = d.assign(half=np.where(d["ano"] <= metade, "ini", "fim"))
    g = d.groupby(["cod_ibge6", "half"])["PESO"].agg(["mean", "var", "count"]).unstack("half")
    g = g.dropna()

    n_ini, n_fim = g[("count", "ini")], g[("count", "fim")]
    # Variância individual agrupada entre as duas metades do município.
    s2 = ((n_ini - 1) * g[("var", "ini")] + (n_fim - 1) * g[("var", "fim")]) / (n_ini + n_fim - 2)
    var_amostral_i = s2 * (1 / n_ini + 1 / n_fim)
    diferenca = g[("mean", "fim")] - g[("mean", "ini")]

    var_obs = float(diferenca.var(ddof=1))
    var_ruido = float(var_amostral_i.mean())
    var_real = max(var_obs - var_ruido, 0.0)

    por_muni = pd.DataFrame({
        "cod_ibge6": diferenca.index,
        "nascimentos_ano": ((n_ini + n_fim) / len(anos)).values,
        "variacao_peso_g": diferenca.values,
        "ruido_esperado_g": np.sqrt(var_amostral_i).values,
    })
    resumo = {
        "dp_observada_g": np.sqrt(var_obs),
        "dp_ruido_g": np.sqrt(var_ruido),
        "dp_real_g": np.sqrt(var_real),
        "fracao_variancia_ruido": var_ruido / var_obs if var_obs else np.nan,
        "n_municipios": int(len(diferenca)),
    }
    return por_muni, resumo


def mde(dp_g: float, n_tratados: int, n_controles: int) -> float:
    if n_tratados <= 0 or n_controles <= 0 or not np.isfinite(dp_g):
        return float("nan")
    return Z_PODER * dp_g * np.sqrt(1 / n_tratados + 1 / n_controles)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--fonte", choices=("pysus", "arquivos"), default="pysus")
    p.add_argument("--caminho", nargs="*", default=None)
    p.add_argument("--efeito-esperado-g", type=float, default=EFEITO_ESPERADO_G)
    p.add_argument("--dose", default="data/processed/pam_ce_muni_cultura_media__sidra.parquet",
                   help="painel município×cultura do script 01, para o perfil de porte do grupo tratado")
    args = p.parse_args()

    if args.fonte == "arquivos":
        if not args.caminho:
            print("[erro] --fonte arquivos exige --caminho.", file=sys.stderr)
            return 2
        bruto = carrega_microdado_arquivos(args.caminho)
    else:
        bruto = carrega_microdado_pysus()

    d = limpa(bruto)
    por_muni, r = decompoe(d)

    barra = "=" * 92
    print(barra)
    print("DP DAS TENDÊNCIAS MUNICIPAIS — ruído amostral contra heterogeneidade real")
    print(f"pré-ban {min(ANOS_PRE)}–{max(ANOS_PRE)} | {len(d):,} nascimentos | "
          f"{r['n_municipios']} municípios".replace(",", "."))
    print(barra)
    print(f"  DP observada das variações       : {r['dp_observada_g']:7.1f} g")
    print(f"    componente de RUÍDO AMOSTRAL   : {r['dp_ruido_g']:7.1f} g")
    print(f"    componente de HETEROGENEIDADE  : {r['dp_real_g']:7.1f} g   <- é esta que governa o MDE")
    print(f"    fração da variância que é ruído: {r['fracao_variancia_ruido']:7.1%}")
    print()
    print("  Por porte do município (nascimentos/ano no pré-ban):")
    print(f"    {'estrato':>12}  {'n':>4}  {'DP obs':>8}  {'ruído':>8}")
    for lo, hi in ESTRATOS:
        m = (por_muni["nascimentos_ano"] >= lo) & (por_muni["nascimentos_ano"] < hi)
        if m.sum() > 2:
            rot = f"{lo}-{hi}" if hi < 10**9 else f">={lo}"
            print(f"    {rot:>12}  {m.sum():4d}  {por_muni.loc[m,'variacao_peso_g'].std(ddof=1):7.1f}g  "
                  f"{np.sqrt((por_muni.loc[m,'ruido_esperado_g']**2).mean()):7.1f}g")

    # --- o que cada hipótese de DP implica para o MDE -----------------------
    caminho_dose = Path(args.dose)
    if caminho_dose.exists():
        pam = pd.read_parquet(caminho_dose)
        pam["cod_ibge6"] = pam["cod_ibge6"].astype(str).str.zfill(6)
        porte = por_muni.set_index("cod_ibge6")["nascimentos_ano"]
        linhas = []
        print()
        print(barra)
        print("O QUE A ESCOLHA DE DP FAZ COM O MDE, por cultura (decil superior = tratados)")
        print(f"efeito esperado de referência: {args.efeito_esperado_g:.0f} g "
              "| meia-largura do IC = 0,70 × MDE")
        print(barra)
        print(f"  {'cultura':<30} {'trat':>4} {'nasc/ano':>9} {'MDE(obs)':>9} {'MDE(real)':>10}  falsifica?")
        for cultura, bloco in pam.groupby("cultura"):
            b = bloco[bloco["area_ha_media"] > 0].sort_values("area_ha_media", ascending=False)
            if b.empty:
                continue
            k = max(1, int(np.ceil(len(b) * 0.10)))
            tratados = b.head(k)["cod_ibge6"]
            controles = len(por_muni) - k
            sz = porte.reindex(tratados).dropna()
            mde_obs = mde(r["dp_observada_g"], k, controles)
            mde_real = mde(r["dp_real_g"], k, controles)
            falsifica = "sim" if 0.70 * mde_real <= args.efeito_esperado_g else "nao"
            linhas.append({"cultura": cultura, "n_tratados": k,
                           "mediana_nascimentos_ano": sz.median() if len(sz) else np.nan,
                           "mde_dp_observada_g": mde_obs, "mde_dp_real_g": mde_real,
                           "falsifica_com_dp_real": falsifica})
            print(f"  {cultura:<30} {k:4d} {sz.median() if len(sz) else float('nan'):9.0f} "
                  f"{mde_obs:8.1f}g {mde_real:9.1f}g  {falsifica:>10}")

        saida = pd.DataFrame(linhas).sort_values("mde_dp_real_g")
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        destino = OUT_DIR / "diagnostico_dp_tendencias.csv"
        with open(destino, "w", encoding="utf-8", newline="") as fh:
            fh.write(f"# gerado em {date.today().isoformat()} por 07_diagnose_trend_sd.py\n")
            fh.write(f"# dp_observada_g={r['dp_observada_g']:.2f} dp_ruido_g={r['dp_ruido_g']:.2f} "
                     f"dp_real_g={r['dp_real_g']:.2f}\n")
            fh.write("# 'falsifica_com_dp_real' supõe que o ruído amostral seja neutralizado "
                     "(ponderação por nascimento ou corte de porte). NÃO é resultado; é conta de desenho.\n")
            saida.to_csv(fh, index=False)
        print(f"\n[ok] -> {destino}")
    else:
        print(f"\n[aviso] {caminho_dose} não existe; rode o script 01 antes para a parte por cultura.")

    print()
    print(barra)
    print("COMO LER — e o que este script NÃO diz")
    print(barra)
    print("  • A coluna MDE(real) supõe que o ruído amostral seja NEUTRALIZADO. Isso não")
    print("    acontece sozinho: exige ponderar por nascimento, ou cortar por porte, ou")
    print("    ambos. Sem uma dessas, o MDE que vale é o MDE(obs).")
    print("  • ⚠️ Cortar por porte NÃO é neutro: se os municípios de dose alta forem os")
    print("    pequenos, o corte remove o próprio grupo tratado. A coluna 'nasc/ano' ao")
    print("    lado existe para essa checagem, e ela é por cultura.")
    print("  • Ponderar por nascimento MUDA O ESTIMANDO: passa a ser efeito por criança,")
    print("    não por município. É defensável — e talvez preferível para bem-estar —,")
    print("    mas é mudança de alvo, e o texto tem de dizer isso.")
    print("  • Nada aqui é resultado do ban. É tudo pré-período: placebo, por construção.")
    print(barra)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
