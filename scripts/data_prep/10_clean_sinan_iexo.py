"""Canal SPT pelo SINAN/IEXO — a notificação compulsória de intoxicação exógena.

Substitui (ou acompanha) o SIH como fonte do canal de intoxicação. A razão é de
ordem de grandeza, e está em `docs/gates-resultados-dados-reais.md` §7-bis:

| fonte | eventos no Ceará |
|---|---|
| SIH, **8 anos** (2015–2022) | **50** — dos quais **1** acidental |
| SINAN/IEXO, **1 ano** (2015) | **2.914** — dos quais **266** de agrotóxico agrícola |

O SIH mede **internação faturada**, e intoxicação aguda por agrotóxico costuma
ser atendida em emergência sem internar. Com 1 evento acidental e 1
autoprovocado em oito anos, o placebo do canal — o contraste entre intenções —
simplesmente não existe. No SINAN existe, e é campo do formulário.

## Os códigos, conferidos contra fonte oficial

⚠️ **Nenhum destes é suposição.** O gates doc §7-bis.3 condicionava escrever
este ingestor a conferir os dois dicionários antes; foi feito.

`AGENTE_TOX` — Nota Técnica nº 5/2026-CGVAM/DVSAT/SVSA/MS, §3.5:

| código | significado | papel |
|---|---|---|
| **02** | Agrotóxico de uso **agrícola** | **é o canal A5** |
| 03 | Agrotóxico de uso doméstico | contraste: não passa por avião |
| **04** | Agrotóxico de uso em **saúde pública** | ⚠️ **é a flag 5** — o controle vetorial do §2º do art. 28-B, que contamina o grupo `d = 0`. Aqui ele deixa de ser hipótese e vira **mensurável** |

`CIRCUNSTAN` — Dicionário de Dados da Intoxicação Exógena, campo 55
(`tp_contaminacao`), conferido em 2026-09-21:

| grupo | códigos | papel |
|---|---|---|
| **não intencional** | 01 uso habitual, 02 acidental, **03 ambiental** | o canal de substituição aéreo→terrestre |
| **intencional** | 10 tentativa de suicídio, 11 tentativa de aborto, 12 violência | **o placebo** |

⚠️ **`03 Ambiental` não estava previsto** na leitura suposta do gates doc, que
falava em "02 acidental contra 10 suicídio". Para deriva de pulverização a
circunstância ambiental é provavelmente a **mais aderente** — descreve quem é
atingido sem manusear o produto. Recortar só em `02` encolheria o numerador sem
razão, e o encolhimento passaria despercebido.

## Três armadilhas achadas RODANDO

1. ⚠️ **`search(disease="IEXO")` e `search(agravo="IEXO")` são aceitos e
   devolvem lista VAZIA, em silêncio.** Conferido em 2026-09-21 contra o
   `pysus` 2.10.0. É a mesma armadilha do `group="DO"` no SIM (§7-bis.1). Este
   script usa `search(year=...)` e filtra pelo **nome do arquivo**, que é
   verificável.
2. **O arquivo é NACIONAL: `IEXOBR<AA>.dbc`**, não por UF. O recorte do Ceará
   tem de ser feito por `ID_MUNICIP` depois de baixar — não há atalho por
   nome de arquivo como no SIH (`RDCE<AAMM>`).
3. ⚠️ **`ID_MUNICIP` tem 7 dígitos, com dígito verificador**, contra os 6 de
   `cod_ibge6`. A truncagem é obrigatória, e é o mesmo tipo de armadilha que o
   `add_dv` do `pysus` quase criou no SINASC.

## O que este script NÃO faz

Não decide se o SINAN substitui o SIH como fonte primária do canal A5. Grava seu
próprio painel, com nome próprio; a escolha é declarada na pré-especificação,
com *vintage* registrada em `docs/fontes-e-vintages.md`. O SIH mede **caso grave
internado**, que é outro estimando — não um pior.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

UF_CEARA = "23"
CODMUNIC_DESCONHECIDO = "230000"   # "município ignorado" — sem denominador possível
ANOS_PADRAO = (2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)
OUT_DIR = Path("data/processed")
NOME_SAIDA = "sinan_iexo_ce_muni_mes"
SEED = 20190613          # mesma dos scripts 01–04; semente, não data do ban
PREFIXO_ARQUIVO = "IEXOBR"
CELULA_PEQUENA = 5

# Conferidos contra a Nota Técnica nº 5/2026-CGVAM (§3.5). Ver o docstring.
AGENTE_AGRICOLA = "02"
AGENTE_SAUDE_PUBLICA = "04"        # ⚠️ a flag 5, agora mensurável
AGENTE_DOMESTICO = "03"

# Conferidos contra o Dicionário de Dados, campo 55. Ver o docstring.
CIRCUNSTANCIAS_NAO_INTENCIONAIS = ("01", "02", "03")
CIRCUNSTANCIAS_INTENCIONAIS = ("10", "11", "12")

# Colunas que o desenho usa. O preflight exige as essenciais e avisa sobre o
# resto: coluna que some vira filtro que não filtra, e filtro que não filtra
# devolve painel plausível e errado.
COLUNAS_ESSENCIAIS = ("ID_MUNICIP", "DT_NOTIFIC")
COLUNAS_DESEJADAS = ("AGENTE_TOX", "CIRCUNSTAN", "ID_OCUPA_N", "ZONA",
                     "SG_UF_NOT", "NU_ANO")


def _saida_utf8() -> None:
    """Força UTF-8 na saída antes de qualquer print.

    Mesmo guarda dos scripts 01–09: no Windows o pipe usa a codepage da locale
    (cp1252), que não encoda ─ ⚠ ✔ ✘, e o script morreria DEPOIS de ter feito o
    trabalho — aqui, depois de baixar o SINAN inteiro.
    """
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def preflight(bloco: pd.DataFrame) -> tuple[bool, list[str]]:
    """As colunas do desenho existem na fonte real?

    ⚠️ Existe pela mesma razão que o preflight do SIDRA no script 01: **filtro
    contra coluna ausente não dá erro — dá vazio.** Um `AGENTE_TOX` que sumisse
    do layout produziria "nenhuma intoxicação por agrotóxico no Ceará", que é
    conclusão substantiva saindo de defeito de leitura.
    """
    faltando = [c for c in COLUNAS_ESSENCIAIS if c not in bloco.columns]
    avisos = [c for c in COLUNAS_DESEJADAS if c not in bloco.columns]
    return (not faltando), (faltando + [f"(opcional) {c}" for c in avisos])


def carrega_de_pysus(anos=ANOS_PADRAO) -> pd.DataFrame:
    """Baixa `IEXOBR<AA>.dbc` do SINAN, ano a ano.

    ⚠️ **NÃO usa `search(disease=...)` nem `search(agravo=...)`.** Os dois são
    aceitos e devolvem lista vazia em silêncio — conferido rodando contra o
    `pysus` 2.10.0 em 2026-09-21. O agravo é garantido pelo NOME do arquivo.
    """
    try:
        from pysus.api import PySUSClient
    except ImportError as erro:
        raise RuntimeError(
            f"pysus indisponível ({erro}). requirements.txt pina pysus==2.10.0."
        ) from erro

    pedacos = []
    with PySUSClient() as client:
        ftp = client.get_ftp()
        base = next(d for d in client._run_async(ftp.datasets()) if d.name == "SINAN")
        for ano in anos:
            arquivos = [a for a in client._run_async(base.search(year=ano))
                        if a.basename.upper().startswith(PREFIXO_ARQUIVO)]
            if not arquivos:
                print(f"  ⚠️ SINAN {ano}: nenhum {PREFIXO_ARQUIVO}*.dbc — ano pulado.")
                continue
            for arquivo in arquivos:
                parquet = client.download_to_parquet(arquivo)
                # `load()` é corotina — mesma armadilha dos scripts 02, 03 e 04.
                bloco = client._run_async(parquet.load())
                ok, notas = preflight(bloco)
                if not ok:
                    raise RuntimeError(
                        f"{arquivo.basename}: colunas essenciais ausentes: {notas}")
                presentes = [c for c in COLUNAS_ESSENCIAIS + COLUNAS_DESEJADAS
                             if c in bloco.columns]
                pedacos.append(bloco[presentes].astype(str))
                print(f"  SINAN/IEXO {ano}: {len(bloco):>8} notificações (BR)")
    if not pedacos:
        raise RuntimeError("pysus não devolveu arquivo IEXO algum.")
    return pd.concat(pedacos, ignore_index=True)


def filtra_ceara(df: pd.DataFrame) -> pd.DataFrame:
    """Recorta o Ceará e trunca o dígito verificador.

    ⚠️ `ID_MUNICIP` vem com **7 dígitos**; `cod_ibge6` tem 6. Sem a truncagem o
    join com o painel de nascimentos não casa — e não casa em SILÊNCIO, virando
    painel vazio ou meio vazio.

    ⚠️ `230000` ("município ignorado") é descartado, como nos scripts 02 e 03:
    é unidade sem denominador possível, e taxa com numerador que o denominador
    não cobre não é taxa.
    """
    saida = df.copy()
    saida["cod_ibge6"] = saida["ID_MUNICIP"].astype(str).str.strip().str[:6]
    saida = saida[saida["cod_ibge6"].str.startswith(UF_CEARA)]
    return saida[saida["cod_ibge6"] != CODMUNIC_DESCONHECIDO]


def classifica(df: pd.DataFrame) -> pd.DataFrame:
    """Marca agente e intenção com os códigos oficiais."""
    saida = df.copy()
    agente = saida.get("AGENTE_TOX", pd.Series("", index=saida.index))
    agente = agente.astype(str).str.strip().str.zfill(2)
    circ = saida.get("CIRCUNSTAN", pd.Series("", index=saida.index))
    circ = circ.astype(str).str.strip().str.zfill(2)

    saida["agrotoxico_agricola"] = (agente == AGENTE_AGRICOLA)
    saida["agrotoxico_saude_publica"] = (agente == AGENTE_SAUDE_PUBLICA)
    saida["agrotoxico_domestico"] = (agente == AGENTE_DOMESTICO)
    saida["nao_intencional"] = circ.isin(CIRCUNSTANCIAS_NAO_INTENCIONAIS)
    saida["intencional"] = circ.isin(CIRCUNSTANCIAS_INTENCIONAIS)
    saida["circunstancia_ignorada"] = ~(saida["nao_intencional"] | saida["intencional"])
    return saida


def extrai_ano_mes(df: pd.DataFrame) -> pd.DataFrame:
    """`DT_NOTIFIC` -> ano/mês. Formatos variam; tenta os do DATASUS."""
    saida = df.copy()
    bruto = saida["DT_NOTIFIC"].astype(str).str.strip()
    data = pd.to_datetime(bruto, format="%Y%m%d", errors="coerce")
    for formato in ("%d/%m/%Y", "%Y-%m-%d", "%d%m%Y"):
        falta = data.isna()
        if not falta.any():
            break
        data = data.fillna(pd.to_datetime(bruto[falta], format=formato, errors="coerce"))
    saida["data_notificacao"] = data
    saida = saida[saida["data_notificacao"].notna()]
    saida["ano"] = saida["data_notificacao"].dt.year
    saida["mes"] = saida["data_notificacao"].dt.month
    return saida


def colapsa_muni_mes(individual: pd.DataFrame) -> pd.DataFrame:
    """Contagens por município × ano-mês, por agente e por intenção."""
    g = individual.groupby(["cod_ibge6", "ano", "mes"], as_index=False)
    painel = g.agg(
        n_notificacoes=("cod_ibge6", "size"),
        n_agricola=("agrotoxico_agricola", "sum"),
        n_saude_publica=("agrotoxico_saude_publica", "sum"),
        n_domestico=("agrotoxico_domestico", "sum"),
        n_nao_intencional=("nao_intencional", "sum"),
        n_intencional=("intencional", "sum"),
        n_circunstancia_ignorada=("circunstancia_ignorada", "sum"),
    )
    # o cruzamento que o canal pede: agrícola × intenção
    cruz = (individual[individual["agrotoxico_agricola"]]
            .groupby(["cod_ibge6", "ano", "mes"], as_index=False)
            .agg(n_agricola_nao_intencional=("nao_intencional", "sum"),
                 n_agricola_intencional=("intencional", "sum")))
    painel = painel.merge(cruz, on=["cod_ibge6", "ano", "mes"], how="left")
    for coluna in ("n_agricola_nao_intencional", "n_agricola_intencional"):
        painel[coluna] = painel[coluna].fillna(0).astype(int)
    return painel.sort_values(["cod_ibge6", "ano", "mes"]).reset_index(drop=True)


def simula_sinan(anos=ANOS_PADRAO, seed: int = SEED, n_por_muni_ano: int = 4):
    """Dado sintético para validar a fiação sem tocar a rede.

    ⚠️ Não é evidência sobre nada. Serve para o pipeline rodar e para os testes.
    """
    rng = np.random.default_rng(seed)
    linhas = []
    for i in range(184):
        cod6 = f"23{i:04d}"
        for ano in anos:
            for _ in range(rng.poisson(n_por_muni_ano)):
                linhas.append({
                    "ID_MUNICIP": cod6 + str(rng.integers(0, 10)),
                    "DT_NOTIFIC": f"{ano}{rng.integers(1,13):02d}{rng.integers(1,29):02d}",
                    "AGENTE_TOX": rng.choice(["02", "03", "04", "05"], p=[.4, .2, .2, .2]),
                    "CIRCUNSTAN": rng.choice(["01", "02", "03", "10", "12", "99"],
                                             p=[.15, .25, .15, .25, .1, .1]),
                    "SG_UF_NOT": "23",
                })
    return pd.DataFrame(linhas).astype(str)


def _mil(n: int) -> str:
    """Separador de milhar brasileiro.

    ⚠️ Existe porque `f"{n:,}".replace(",", ".")` aplicado à linha INTEIRA come
    vírgulas literais: "01,02,03" virava "01.02.03" e "CE, pós-limpeza" virava
    "CE. pós-limpeza". O replace tem de ver só o número.
    """
    return f"{int(n):,}".replace(",", ".")


def imprime_resumo(individual: pd.DataFrame, painel: pd.DataFrame, fonte: str) -> None:
    barra = "=" * 88
    print(barra)
    print(f"SINAN/IEXO — CANAL SPT | fonte: {fonte}")
    print(barra)
    n = len(individual)
    print(f"  notificações (CE, pós-limpeza)   : {_mil(n):>8}")
    print(f"  municípios                       : {individual['cod_ibge6'].nunique():>8}")
    print(f"  células município-mês            : {_mil(len(painel)):>8}")
    print()
    print("  por agente (Nota Técnica nº 5/2026, §3.5):")
    print(f"    02 agrotóxico AGRÍCOLA  (canal A5) : "
          f"{_mil(individual['agrotoxico_agricola'].sum()):>7}")
    print(f"    04 agrotóxico SAÚDE PÚBLICA (flag 5): "
          f"{_mil(individual['agrotoxico_saude_publica'].sum()):>7}")
    print(f"    03 agrotóxico doméstico            : "
          f"{_mil(individual['agrotoxico_domestico'].sum()):>7}")
    print()
    print("  por circunstância (Dicionário de Dados, campo 55):")
    print(f"    não intencional (01,02,03)  : "
          f"{_mil(individual['nao_intencional'].sum()):>7}")
    print(f"    intencional (10,11,12)      : "
          f"{_mil(individual['intencional'].sum()):>7}")
    ign = int(individual["circunstancia_ignorada"].sum())
    print(f"    ⚠️ ignorada/não preenchida  : {_mil(ign):>7}"
          f"  ({ign / max(n, 1):.1%})")

    pequenas = (painel["n_notificacoes"] < CELULA_PEQUENA).mean()
    print()
    print(f"  ⚠️ células com < {CELULA_PEQUENA} notificações: {pequenas:.1%}")
    print()
    print(barra)
    print("COMO LER — e o que este script NÃO diz")
    print(barra)
    print("  • Nada aqui é resultado do ban. É construção de painel.")
    print("  • ⚠️ O placebo do canal é 'não intencional' contra 'intencional'. Se a")
    print("    fração IGNORADA for alta, o contraste enfraquece — e a fraqueza fica")
    print("    invisível no resultado. Olhe a linha de ignorada antes de estimar.")
    print("  • ⚠️ O agente 04 (saúde pública) NÃO é ruído: é o controle vetorial do")
    print("    §2º do art. 28-B, a flag 5. Aqui ele é mensurável pela primeira vez.")
    print("  • Este painel NÃO substitui o do SIH por decreto. O SIH mede caso")
    print("    grave internado — outro estimando. A escolha é da pré-especificação.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--fonte", choices=("auto", "pysus", "simulado"), default="auto")
    p.add_argument("--anos", type=int, nargs="*", default=list(ANOS_PADRAO))
    p.add_argument("--seed", type=int, default=SEED)
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    if args.fonte == "simulado":
        bruto, fonte = simula_sinan(tuple(args.anos), args.seed), "simulado"
    else:
        try:
            bruto, fonte = carrega_de_pysus(tuple(args.anos)), "pysus"
        except Exception as erro:
            if args.fonte == "pysus":
                print(f"  ✘ SINAN via pysus falhou: {erro}")
                return 1
            print(f"  ⚠️ pysus indisponível ({erro}); caindo no simulado.")
            bruto, fonte = simula_sinan(tuple(args.anos), args.seed), "simulado"

    individual = extrai_ano_mes(classifica(filtra_ceara(bruto)))
    if individual.empty:
        print("  ✘ Nenhuma notificação do Ceará sobrou. Confira:")
        print("     1. ID_MUNICIP começa em 23 e tem 7 dígitos?")
        print("     2. DT_NOTIFIC está em AAAAMMDD?")
        print("     3. O arquivo baixado é IEXOBR<AA>.dbc mesmo?")
        return 1

    painel = colapsa_muni_mes(individual)
    painel["fonte"] = fonte
    imprime_resumo(individual, painel, fonte)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    sufixo = "" if fonte != "simulado" else "__simulado"
    destino = args.out_dir / f"{NOME_SAIDA}{sufixo}.parquet"
    painel.to_parquet(destino, index=False)
    print(f"\n[ok] painel -> {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
