"""E17 — Auditoria do canal-água: o que exatamente quebra na série do SISAGUA

POR QUE ESTE SCRIPT EXISTE
--------------------------

`docs/lacunas-de-dados.md` §1-ter suspendeu o canal-água com um alerta correto e
uma explicação incompleta. O alerta: as detecções de agrotóxico no Ceará caem a
**zero exato** a partir de 2020, com mais amostras que antes, e um DiD sobre
"agrotóxico detectado" acharia que o ban eliminou 100% das detecções. A
explicação oferecida — "mudança de prática laboratorial cearense, no ano
seguinte ao ban" — **não sobrevive ao dado**, e este script mostra por quê.

O QUE A AUDITORIA ENCONTRA (rodada de 2026-09-22)
--------------------------------------------------

**1. A sensibilidade analítica NÃO mudou em 2020.** LD e LQ medianos ficam em
0,10 e 0,30 µg/L de 2019 a 2023, atravessando a quebra sem se mexer. Logo o
sumiço dos numéricos **não pode ser perda de sensibilidade** — que era a
hipótese natural, e é a que o §1-ter não testou.

**2. As detecções do pré-período eram legítimas.** Das 123 detecções numéricas
de 2015–2019, apenas **2%** ficam abaixo do próprio LQ do registro; a mediana é
0,37 µg/L e o máximo 10,25. E **56% delas continuariam quantificáveis** sob o LQ
de 0,30 que vigorou depois. Se a mesma água tivesse a mesma contaminação em
2020–2023, mais da metade daquelas detecções teria de reaparecer. Não
reapareceu nenhuma.

**3. São QUATRO anos, não três — e os numéricos VOLTAM.** O §1-ter para em 2022.
2023 também é zero (4.957 amostras, 100% `MENOR_LD`). E 2024–2026 voltam a ter
numéricos, no mesmo ano em que o LQ mediano **cai ~30×** (0,30 → 0,0101): método
mais sensível entrando, e o numérico reaparece com ele.

**4. ⚠️ E o Ceará SEMPRE foi anômalo — a quebra de 2020 é menor do que parece.**
Percentual de resultados numéricos:

| ano | Ceará | resto do Brasil |
|---|---|---|
| 2015–2019 | **0,11 – 0,64%** | 7 – 55% |
| 2020–2023 | 0,00% | 57 → 6% |

O Ceará reportava ~0,3% de numéricos **antes** do ban. A queda de 0,6% para 0,0%
é mudança dentro de um regime que já era quase-todo censurado, não a perda de
uma série informativa. E **zerar o numérico é comum**: 5 a 9 de ~20 UFs zeram em
qualquer ano dado; Paraíba e Tocantins zeram em quase todos. O resto do Brasil
também desaba, de 57% em 2020 para 5% em 2022.

> **A conclusão muda de forma.** O problema do canal-água no Ceará não é uma
> quebra em 2020: é que a série **nunca teve variância para explorar**. São 123
> detecções em ~31 mil amostras de 2015–2019 — 0,4%. O §1-ter diz que "o
> pré-período 2015–2018 é usável"; é essa frase que não sobrevive, mais do que
> a do pós.

⚠️ O QUE ESTE SCRIPT NÃO FAZ
-----------------------------

- **Não decide o destino do canal.** As três saídas do §1-ter (descritivo de
  pré-período, LAI de microdado à SESA/CE, ou fora do escopo) continuam abertas,
  e a escolha é do pesquisador com o orientador.
- **Não estima nada.** Mede a fonte, não o efeito.
- **Não julga os laboratórios.** "Mudança de convenção de reporte" é a leitura
  que o dado sustenta; por que ela ocorreu, o dado não diz.

Uso:
    python scripts/data_prep/17_audita_sisagua.py
    python scripts/data_prep/17_audita_sisagua.py --uf CE --refazer-cache

Saídas (gitignored):
    data/processed/sisagua_auditoria_composicao.csv
    data/processed/sisagua_auditoria_limites.csv
    data/processed/sisagua_auditoria_censura.csv
"""

from __future__ import annotations

import argparse
import zipfile
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
OUT_DIR = RAIZ / "data" / "processed"
ZIP_PADRAO = RAIZ / "data" / "raw" / "sisagua_vigilancia_demais_parametros_csv.zip"
CACHE = RAIZ / "data" / "raw" / "sisagua_agrotoxicos.parquet"

UF_ALVO = "CE"
# ⚠️ O ban vigora em 09/01/2019. A "quebra" começa em 2020 — um ano DEPOIS —, e
# essa defasagem é parte do que torna a leitura causal tentadora e errada.
ANOS_PRE = (2015, 2016, 2017, 2018, 2019)
ANOS_QUEBRA = (2020, 2021, 2022, 2023)

COLUNAS = ["UF", "Código IBGE", "Município", "Ano", "Grupo de parâmetros",
           "Parâmetro (demais parâmetros)", "Procedência da Coleta",
           "LD", "LQ", "Resultado"]


def _num(serie: pd.Series) -> pd.Series:
    """Texto do SISAGUA para float. Vírgula decimal; não-número vira NaN."""
    return pd.to_numeric(
        serie.astype(str).str.strip().str.replace(",", ".", regex=False),
        errors="coerce",
    )


def carrega_agrotoxicos(caminho_zip: Path = ZIP_PADRAO, cache: Path = CACHE,
                        refazer: bool = False, tamanho_bloco: int = 400_000) -> pd.DataFrame:
    """Lê o CSV de 905 MB em blocos e guarda só o grupo Agrotóxicos.

    ⚠️ O cache não é conveniência: sem ele cada pergunta da auditoria releria
    905 MB, e auditoria que custa caro é auditoria que se roda uma vez só.
    """
    if cache.exists() and not refazer:
        return pd.read_parquet(cache)
    if not caminho_zip.exists():
        raise FileNotFoundError(
            f"{caminho_zip} não existe. O CSV vem de "
            "s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SISAGUA/ (aberto)."
        )
    pedacos = []
    with zipfile.ZipFile(caminho_zip) as z:
        interno = z.namelist()[0]
        with z.open(interno) as fh:
            for bloco in pd.read_csv(fh, sep=";", encoding="latin-1", usecols=COLUNAS,
                                     dtype=str, chunksize=tamanho_bloco,
                                     on_bad_lines="skip"):
                bloco = bloco[bloco["Grupo de parâmetros"].str.contains(
                    "grotóxic", case=False, na=False)]
                if len(bloco):
                    pedacos.append(bloco)
    if not pedacos:
        raise RuntimeError("Nenhuma linha do grupo 'Agrotóxicos' no arquivo.")
    df = pd.concat(pedacos, ignore_index=True)
    df = prepara(df)
    cache.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(cache, index=False)
    return df


def prepara(df: pd.DataFrame) -> pd.DataFrame:
    """Tipa e classifica o resultado nas três categorias que o SISAGUA usa.

    ⚠️ São TRÊS, não duas: `MENOR_LD`, `MENOR_LQ` e o numérico. O §1-ter só
    menciona `MENOR_LQ`, e `MENOR_LD` é a maior de todas — 280 mil dos 476 mil
    registros do país. Tratar as duas como uma só apaga justamente a distinção
    que a auditoria precisa.
    """
    saida = df.copy()
    saida["ano"] = _num(saida["Ano"]).astype("Int64")
    saida["resultado_num"] = _num(saida["Resultado"])
    saida["ld"] = _num(saida["LD"])
    saida["lq"] = _num(saida["LQ"])
    saida["categoria"] = np.where(
        saida["resultado_num"].notna(), "numerico",
        saida["Resultado"].astype(str).str.strip(),
    )
    saida["molecula"] = (saida["Parâmetro (demais parâmetros)"]
                         .str.split(" - VMP").str[0].str.strip())
    return saida


def composicao_por_ano(df: pd.DataFrame, uf: str = UF_ALVO) -> pd.DataFrame:
    """Como o resultado é reportado, por ano, na UF contra o resto do país."""
    base = df[df["ano"].notna()].copy()
    base["grupo"] = np.where(base["UF"] == uf, uf, "resto do BR")
    tab = base.pivot_table(index="ano", columns=["grupo", "categoria"],
                           values="Resultado", aggfunc="count").fillna(0)
    linhas = []
    for grupo in [uf, "resto do BR"]:
        if grupo not in tab.columns.get_level_values(0):
            continue
        sub = tab[grupo]
        total = sub.sum(axis=1)

        def coluna(nome):
            """Categoria ausente é coluna de ZEROS, não o escalar 0.

            ⚠️ `sub.get(nome, 0)` devolve um int quando a categoria não
            aparece — e um recorte em que todo mundo reportou numérico não tem
            coluna MENOR_LD. Indexar o int por ano quebra.
            """
            if nome in sub.columns:
                return sub[nome]
            return pd.Series(0.0, index=sub.index)

        for ano in sub.index:
            if total.loc[ano] == 0:
                continue
            linhas.append({
                "ano": int(ano), "grupo": grupo, "n_amostras": int(total.loc[ano]),
                "pct_numerico": round(100 * coluna("numerico").loc[ano] / total.loc[ano], 2),
                "pct_menor_lq": round(100 * coluna("MENOR_LQ").loc[ano] / total.loc[ano], 2),
                "pct_menor_ld": round(100 * coluna("MENOR_LD").loc[ano] / total.loc[ano], 2),
            })
    return pd.DataFrame(linhas).sort_values(["grupo", "ano"])


def limites_por_ano(df: pd.DataFrame, uf: str = UF_ALVO) -> pd.DataFrame:
    """LD e LQ por ano — o teste que decide se a quebra é de sensibilidade.

    Se o LQ subisse em 2020, o sumiço dos numéricos teria explicação analítica.
    Ele não sobe: fica em 0,30 µg/L de 2019 a 2023. A explicação tem de ser
    outra.
    """
    base = df[(df["UF"] == uf) & (df["ano"].notna())]
    return (base.groupby("ano")
            .agg(n=("Resultado", "size"),
                 ld_mediana=("ld", "median"), ld_distintos=("ld", "nunique"),
                 lq_mediana=("lq", "median"), lq_distintos=("lq", "nunique"))
            .round(4).reset_index())


def teste_censura(df: pd.DataFrame, uf: str = UF_ALVO) -> dict:
    """As detecções do pré-período sobreviveriam ao LQ do regime seguinte?

    É a pergunta decisiva, e o §1-ter não a fez. Se as detecções antigas fossem
    quase todas abaixo do LQ que passou a vigorar, o zero posterior seria
    censura — artefato de limite, não de reporte. Não é o caso.
    """
    base = df[(df["UF"] == uf) & (df["ano"].notna())]
    det = base[(base["resultado_num"].notna()) & (base["resultado_num"] > 0)
               & (base["ano"].isin(ANOS_PRE))]
    if det.empty:
        raise ValueError(f"nenhuma detecção numérica em {uf} no pré-período")
    lq_regime = float(base[base["ano"].isin(ANOS_QUEBRA)]["lq"].median())
    ld_regime = float(base[base["ano"].isin(ANOS_QUEBRA)]["ld"].median())
    return {
        "uf": uf,
        "n_deteccoes_pre": int(len(det)),
        "mediana_ugL": round(float(det["resultado_num"].median()), 4),
        "maximo_ugL": round(float(det["resultado_num"].max()), 4),
        "pct_abaixo_do_proprio_lq": round(100 * float(
            (det["resultado_num"] < det["lq"]).mean()), 1),
        "lq_mediano_regime_quebra": round(lq_regime, 4),
        "ld_mediano_regime_quebra": round(ld_regime, 4),
        "pct_sobreviveria_ao_lq": round(100 * float(
            (det["resultado_num"] >= lq_regime).mean()), 1),
        "pct_sobreviveria_ao_ld": round(100 * float(
            (det["resultado_num"] >= ld_regime).mean()), 1),
    }


def ufs_que_zeram(df: pd.DataFrame) -> pd.DataFrame:
    """Quantas UFs reportam 0% de numérico em cada ano.

    ⚠️ Desfaz o "não é fenômeno nacional" do §1-ter: zerar é comum, e o Ceará
    não é exceção quando zera — é exceção por reportar tão pouco o tempo todo.
    """
    base = df[df["ano"].notna()]
    p = base.pivot_table(index="ano", columns="UF", values="categoria",
                         aggfunc=lambda s: float((s == "numerico").mean()))
    linhas = []
    for ano in p.index:
        linha = p.loc[ano].dropna()
        if linha.empty:
            continue
        zeradas = sorted(linha[linha == 0].index)
        linhas.append({"ano": int(ano), "ufs_com_dado": int(len(linha)),
                       "ufs_com_zero_numerico": len(zeradas),
                       "quais": ", ".join(zeradas)})
    return pd.DataFrame(linhas)


def imprime(comp: pd.DataFrame, lim: pd.DataFrame, cens: dict,
            zeram: pd.DataFrame, uf: str) -> None:
    larg = 84
    print("=" * larg)
    print(f"AUDITORIA DO CANAL-ÁGUA — SISAGUA, grupo Agrotóxicos, {uf} contra o país")
    print("=" * larg)
    print("1. Como o resultado é reportado (% das amostras do ano)")
    piv = comp.pivot(index="ano", columns="grupo",
                     values="pct_numerico").round(2)
    piv.columns = [f"%numerico {c}" for c in piv.columns]
    print(piv.to_string())
    print()
    print(f"2. Sensibilidade analítica em {uf} — o teste da quebra")
    print(lim.to_string(index=False))
    print("   ⚠️ LD e LQ medianos atravessam 2020 SEM se mexer. A quebra não é")
    print("      de sensibilidade; é de convenção de reporte.")
    print()
    print("3. As detecções do pré-período sobreviveriam ao regime seguinte?")
    for k, v in cens.items():
        print(f"   {k:32} {v}")
    print(f"   ⚠️ {cens['pct_sobreviveria_ao_lq']}% das detecções de "
          f"{ANOS_PRE[0]}–{ANOS_PRE[-1]} continuariam quantificáveis sob o LQ")
    print("      vigente na quebra. Nenhuma reapareceu.")
    print()
    print("4. Zerar o numérico é fenômeno nacional?")
    print(zeram.to_string(index=False))
    print("=" * larg)
    print("  ⚠️ NÃO estima nada, e NÃO decide o destino do canal: as três saídas")
    print("     do §1-ter de docs/lacunas-de-dados.md seguem abertas.")
    print("=" * larg)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--zip", type=Path, default=ZIP_PADRAO)
    p.add_argument("--cache", type=Path, default=CACHE)
    p.add_argument("--refazer-cache", action="store_true")
    p.add_argument("--uf", default=UF_ALVO)
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    try:
        df = carrega_agrotoxicos(args.zip, args.cache, args.refazer_cache)
    except FileNotFoundError as erro:
        print(f"[erro] {erro}")
        return 1
    print(f"[ok] {len(df):,} medições de agrotóxico no país; "
          f"{(df['UF'] == args.uf).sum():,} em {args.uf}".replace(",", "."))

    comp = composicao_por_ano(df, args.uf)
    lim = limites_por_ano(df, args.uf)
    cens = teste_censura(df, args.uf)
    zeram = ufs_que_zeram(df)
    imprime(comp, lim, cens, zeram, args.uf)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    hoje = date.today().isoformat()
    for nome, tabela in [("composicao", comp), ("limites", lim),
                         ("censura", pd.DataFrame([cens])), ("ufs_zeram", zeram)]:
        tabela = tabela.copy()
        tabela["extraido_em"] = hoje
        destino = args.out_dir / f"sisagua_auditoria_{nome}.csv"
        tabela.to_csv(destino, index=False, encoding="utf-8")
        print(f"gravado: {destino.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
