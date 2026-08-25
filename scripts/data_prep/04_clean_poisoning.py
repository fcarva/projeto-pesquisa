#!/usr/bin/env python3
"""Internação por intoxicação com agrotóxico (SIH) — o canal de substituição.

**A hipótese.** Proibido o avião, a aplicação migra para trator e pulverizador
costal. Isso *afasta* o veneno da população — menos deriva — e *aproxima* o
veneno do aplicador. Então o ban pode **reduzir** exposição perinatal e ao mesmo
tempo **aumentar** intoxicação aguda ocupacional. Sinal oposto ao do desfecho
principal, e por isso vale medir separado: é o item A5 do roteiro.

**Por que isso ataca a flag 3 do CLAUDE.md.** A lacuna de *enforcement* — o ban
foi fiscalizado? — hoje depende de um pedido LAI que ainda não voltou. Se a série
de intoxicação se move com a dose, isso é evidência **independente** de que o ban
mudou comportamento no campo. Não substitui o dado administrativo; chega por
outro caminho.

────────────────────────────────────────────────────────────────────────────
A DECISÃO DE MEDIDA QUE ESTE SCRIPT **NÃO** TOMA
────────────────────────────────────────────────────────────────────────────
O CID-10 separa intoxicação por agrotóxico **por intenção**, e as famílias não
respondem ao ban da mesma maneira:

  X48  acidental / exposição       → responde a COMO se aplica
  X68  autoprovocada (suicídio)    → responde à DISPONIBILIDADE da molécula
  X87  agressão
  Y18  intenção indeterminada

No Brasil rural o agrotóxico é meio comum de suicídio, então X68 costuma ser
parcela grande das internações. **Somar X68 com X48 mistura dois mecanismos.**

⚠️ E há um ganho de desenho escondido aí. A flag 3 do CLAUDE.md registra que
*proibir método ≠ proibir molécula*: o ban não muda a disponibilidade do
produto. Logo a hipótese de substituição prevê movimento em **X48** e prevê
**nenhum movimento em X68** — o que faz de X68 um **placebo dentro do mesmo
dado**, com a mesma população, o mesmo sistema de registro e os mesmos
municípios. Se as duas séries se moverem juntas, a explicação não é
substituição de método; é algo que move internação em geral.

Por isso este script **emite cada família em coluna própria e nunca as soma**.
Qual delas é o desfecho, e qual é placebo, é decisão sua.

Mesma lógica nas moléculas, e aqui a ligação é com a flag 2:

  T60.0  organofosforados e CARBAMATOS  ← carbaril 23/23, carbofurano 18/23,
                                           fenitrotiona 16/23 (Dossiê ABRASCO)
  T60.3  herbicidas e FUNGICIDAS        ← procimidona 23/23; fungicida em
                                           banana, por avião
  T60.x  demais subtipos

────────────────────────────────────────────────────────────────────────────
LIMITES DA FONTE, QUE PRECISAM ESTAR NO TEXTO
────────────────────────────────────────────────────────────────────────────
  • **SIH é internação, não incidência.** Só entra o caso grave o bastante para
    internar, na rede SUS. Intoxicação leve, atendimento ambulatorial e rede
    privada ficam de fora. O nível é subestimado; o que se estima é efeito sobre
    caso grave internado.
  • **SIH é dado de faturamento.** `diag_princ` é o diagnóstico principal da
    AIH, e a codificação responde a incentivo de pagamento. Por isso o script
    varre também `diag_secun` e **marca em qual campo casou** — principal e
    secundário não significam a mesma coisa.
  • **Sem denominador aqui.** Saem contagens; população municipal vem do IBGE
    (bloqueado nesta sessão) e entra em `scripts/build_panel/`.
  • **Data de internação, não de exposição.** Mesmo problema dos scripts 02 e 03.

Uso:
    python scripts/data_prep/04_clean_poisoning.py --fonte simulado
    python scripts/data_prep/04_clean_poisoning.py --caminho data/raw/sih_rd_ce_*.csv.gz

A fonte real vem de `scripts/data_prep/00_export_datazoom.R --bases sih`.
Saída: data/processed/intoxicacao_ce_muni_mes[__simulado].parquet (gitignored).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# Parâmetros
# --------------------------------------------------------------------------

UF_CEARA = "23"
ANOS_PADRAO = (2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)
OUT_DIR = Path("data/processed")
NOME_SAIDA = "intoxicacao_ce_muni_mes"
SEED = 20190613  # mesma seed dos scripts 01, 02 e 03

COLUNAS_SIH = (
    "DIAG_PRINC",   # CID-10 do diagnóstico principal
    "DIAG_SECUN",   # CID-10 do diagnóstico secundário
    "MUNIC_RES",    # município de residência (código IBGE)
    "DT_INTER",     # data da internação
    "MORTE",        # indicador de óbito na internação
    "IDADE",        # idade do paciente
    "SEXO",
)

# --- datazoom.saude (R) -----------------------------------------------------
# Conferido contra R/dictionary.R do repositório datazoompuc/datazoom.saude,
# seção `datasus_sih`. Duas convenções pelo `language`; o padrão do pacote é
# "eng", então as duas entram — mesma armadilha dos scripts 02 e 03.
ALIASES_DATAZOOM = {
    # português (language = "pt")
    "CID_DIAGNOSTICO_PRINCIPAL": "DIAG_PRINC",
    "CID_DIAGNOSTICO_SECUNDARIO": "DIAG_SECUN",
    "MUNICIPIO_RESIDENCIA": "MUNIC_RES",
    "CODIGO_IBGE_MUNICIPIO_RESIDENCIA": "MUNIC_RES",
    "DATA_INTERNACAO": "DT_INTER",
    "INDICADOR_OBITO": "MORTE",
    "IDADE_PACIENTE": "IDADE",
    "SEXO_PACIENTE": "SEXO",
    # inglês (language = "eng", o PADRÃO do pacote)
    "MAIN_DIAGNOSIS_CID": "DIAG_PRINC",
    "SECONDARY_DIAGNOSIS_CID": "DIAG_SECUN",
    "RESIDENCE_MUNICIPALITY": "MUNIC_RES",
    "IBGE_CODE_RESIDENCE_MUNICIPALITY": "MUNIC_RES",
    "DATE_ADMISSION": "DT_INTER",
    "DEATH_INDICATOR": "MORTE",
    "PATIENT_AGE": "IDADE",
    "PATIENT_GENDER": "SEXO",
}

# --- Famílias de CID --------------------------------------------------------
# O SIH grava o CID sem ponto: T60.0 vira "T600", X48 fica "X48". O casamento
# abaixo é por PREFIXO sobre o código normalizado.
#
# ⚠️ Cada família vira uma coluna, e elas NUNCA são somadas aqui. Ver a nota de
# medida no topo do arquivo: a escolha de desfecho e de placebo é do pesquisador.
FAMILIAS_INTENCAO = {
    "acidental": ("X48",),        # acidental / exposição — o canal de substituição
    "autoprovocada": ("X68",),    # suicídio — candidato a PLACEBO
    "agressao": ("X87",),
    "indeterminada": ("Y18",),
}

FAMILIAS_MOLECULA = {
    # T60.0 casa a química que o Dossiê ABRASCO achou na Chapada do Apodi
    "t60_organofosforado_carbamato": ("T600",),
    # T60.3 casa a história da banana: fungicida por avião
    "t60_herbicida_fungicida": ("T603",),
    "t60_outros": ("T601", "T602", "T604", "T605", "T606", "T607", "T608", "T609"),
}

# Todo T60 e todo código de intenção, para a linha de referência. É a única
# coluna agregada, e existe para conferência de cobertura — não como desfecho.
PREFIXO_T60 = "T60"

# Faixa etária de trabalho: proxy grosseiro de exposição ocupacional. Intoxicação
# em criança tende a ser doméstica, não ocupacional, e o canal de substituição
# fala do aplicador.
IDADE_TRABALHO_MIN, IDADE_TRABALHO_MAX = 15, 64

CELULA_PEQUENA = 5


# --------------------------------------------------------------------------
# Limpeza
# --------------------------------------------------------------------------

FORMATOS_DATA = ("%Y%m%d", "%d%m%Y", "%Y-%m-%d", "%d/%m/%Y")


def _para_data(bruto: pd.Series) -> pd.Series:
    """Converte para data tentando os formatos conhecidos, sem inferir.

    ⚠️ `DT_INTER` do SIH vem em **AAAAMMDD**, não DDMMAAAA como o SINASC — o
    próprio dicionário do datazoom diz "no formato aaaammdd" para `dt_saida`.
    Por isso `%Y%m%d` vem primeiro. Inverter a ordem faria "20170301" virar
    dia 20 de… nada, mas "20150102" parsearia nas duas e daria data errada.
    Inferência aqui troca dia por mês em silêncio; a lista é fechada.
    """
    texto = bruto.astype("string").str.strip().str.replace(r"\.0$", "", regex=True)
    so_digitos = texto.str.fullmatch(r"\d+").fillna(False)
    texto = texto.mask(so_digitos, texto.str.zfill(8))

    data = pd.Series(pd.NaT, index=bruto.index, dtype="datetime64[ns]")
    for formato in FORMATOS_DATA:
        falta = data.isna()
        if not falta.any():
            break
        data.loc[falta] = pd.to_datetime(texto[falta], format=formato, errors="coerce")
    return data


def padroniza_colunas(df: pd.DataFrame) -> pd.DataFrame:
    """Nomes em maiúscula, aliases do datazoom, colunas esperadas garantidas."""
    saida = df.copy()
    saida.columns = [str(c).strip().upper() for c in saida.columns]
    saida = saida.rename(columns=ALIASES_DATAZOOM)
    saida = saida.loc[:, ~saida.columns.duplicated()]
    faltando = [c for c in COLUNAS_SIH if c not in saida.columns]
    for col in faltando:
        saida[col] = np.nan
    if faltando:
        print(f"[aviso] colunas ausentes na fonte, preenchidas com NaN: {faltando}")
    return saida[list(COLUNAS_SIH)]


def normaliza_cid(serie: pd.Series) -> pd.Series:
    """CID em maiúscula, sem ponto e sem espaço. 'T60.0' e 't600' viram 'T600'."""
    return (
        serie.astype("string").str.upper()
        .str.replace(r"[^A-Z0-9]", "", regex=True)
        .fillna("")
    )


def classifica_cid(principal: pd.Series, secundario: pd.Series) -> pd.DataFrame:
    """Marca cada internação por família de CID, em colunas separadas.

    Varre **os dois** campos de diagnóstico, porque SIH é dado de faturamento e
    a escolha entre principal e secundário responde a incentivo de pagamento,
    não só a clínica. `casou_principal` registra onde casou: uma família que só
    aparece no secundário significa outra coisa, e o painel precisa deixar isso
    à vista em vez de fundir os dois.
    """
    p, s = normaliza_cid(principal), normaliza_cid(secundario)

    def casa(prefixos: tuple[str, ...]) -> tuple[pd.Series, pd.Series]:
        em_p = pd.Series(False, index=p.index)
        em_s = pd.Series(False, index=s.index)
        for pref in prefixos:
            em_p |= p.str.startswith(pref)
            em_s |= s.str.startswith(pref)
        return em_p, em_s

    saida = pd.DataFrame(index=principal.index)
    for nome, prefixos in {**FAMILIAS_INTENCAO, **FAMILIAS_MOLECULA}.items():
        em_p, em_s = casa(prefixos)
        saida[f"fam_{nome}"] = em_p | em_s
        saida[f"fam_{nome}_principal"] = em_p

    em_p, em_s = casa((PREFIXO_T60,))
    saida["fam_t60_qualquer"] = em_p | em_s
    saida["fam_t60_qualquer_principal"] = em_p
    return saida


def filtra_ceara(df: pd.DataFrame) -> pd.DataFrame:
    """Mantém residentes no Ceará. Aceita código IBGE de 6 ou 7 dígitos.

    O SIH tem os dois: `munic_res` histórico com 6 dígitos e `codibge` com 7.
    Truncar para 6 é a chave do projeto — a mesma de `cod_ibge6` nos scripts 02
    e 03, que é o que permite a junção.
    """
    cod = (
        df["MUNIC_RES"].astype("string").str.strip()
        .str.replace(r"\.0$", "", regex=True)
        .str.replace(r"\D", "", regex=True)
    )
    cod = cod.where(cod.str.len() != 7, cod.str[:6]).str.zfill(6)
    saida = df.copy()
    saida["cod_ibge6"] = cod
    return saida[cod.str.startswith(UF_CEARA).fillna(False)].copy()


def prepara_internacoes(bruto: pd.DataFrame, anos=None) -> pd.DataFrame:
    """Pipeline no nível da internação, antes do colapso."""
    df = filtra_ceara(padroniza_colunas(bruto))
    df = pd.concat([df, classifica_cid(df["DIAG_PRINC"], df["DIAG_SECUN"])], axis=1)

    # Só internações que casam ALGUMA família — o resto do SIH não interessa aqui.
    colunas_fam = [c for c in df.columns if c.startswith("fam_") and not c.endswith("_principal")]
    df = df[df[colunas_fam].any(axis=1)].copy()

    data = _para_data(df["DT_INTER"])
    df["ano"] = data.dt.year.astype("Int64")
    df["mes"] = data.dt.month.astype("Int64")
    df["idade_anos"] = pd.to_numeric(df["IDADE"], errors="coerce")
    df["idade_trabalho"] = df["idade_anos"].between(IDADE_TRABALHO_MIN, IDADE_TRABALHO_MAX)
    df["obito"] = pd.to_numeric(df["MORTE"], errors="coerce").fillna(0) == 1

    df = df[df["ano"].notna() & df["mes"].notna()]
    if anos is not None:
        df = df[df["ano"].isin(list(anos))]
    return df.reset_index(drop=True)


def colapsa_muni_mes(individual: pd.DataFrame) -> pd.DataFrame:
    """Colapsa a `cod_ibge6` × ano × mês — a MESMA chave dos scripts 02 e 03.

    Cada família vira sua própria contagem. **Nada é somado entre famílias**:
    acidental e autoprovocada respondem a mecanismos diferentes, e a coluna
    `n_t60_qualquer` existe só como referência de cobertura, não como desfecho.
    """
    nomes = list(FAMILIAS_INTENCAO) + list(FAMILIAS_MOLECULA) + ["t60_qualquer"]

    df = individual.copy()
    agregados = {"n_internacoes_com_cid": ("cod_ibge6", "size")}
    for nome in nomes:
        agregados[f"n_{nome}"] = (f"fam_{nome}", "sum")
        agregados[f"n_{nome}_principal"] = (f"fam_{nome}_principal", "sum")

    # Recortes do canal ocupacional, só para a família acidental — que é a que a
    # hipótese de substituição fala. Fazer isso para todas seria ruído.
    df["_acid_trab"] = df["fam_acidental"] & df["idade_trabalho"]
    df["_acid_obito"] = df["fam_acidental"] & df["obito"]
    agregados["n_acidental_idade_trabalho"] = ("_acid_trab", "sum")
    agregados["n_acidental_obito"] = ("_acid_obito", "sum")

    painel = df.groupby(["cod_ibge6", "ano", "mes"], dropna=True).agg(**agregados).reset_index()
    painel["ano"] = painel["ano"].astype(int)
    painel["mes"] = painel["mes"].astype(int)
    for coluna in painel.columns:
        if coluna.startswith("n_"):
            painel[coluna] = painel[coluna].astype(int)
    painel["celula_pequena"] = painel["n_internacoes_com_cid"] < CELULA_PEQUENA
    return painel.sort_values(["cod_ibge6", "ano", "mes"]).reset_index(drop=True)


# --------------------------------------------------------------------------
# Fontes
# --------------------------------------------------------------------------

def carrega_de_arquivos(caminhos: list[Path]) -> pd.DataFrame:
    """Lê SIH já exportado (.csv.gz do 00_export_datazoom.R, .csv ou .parquet)."""
    if not caminhos:
        raise ValueError("Nenhum caminho informado (use --caminho).")
    pedacos = []
    for caminho in caminhos:
        if caminho.suffix == ".parquet":
            pedacos.append(pd.read_parquet(caminho))
        elif caminho.suffix in (".csv", ".gz"):
            pedacos.append(pd.read_csv(caminho, dtype=str, low_memory=False))
        else:
            raise ValueError(f"Extensão não suportada: {caminho}")
    return pd.concat(pedacos, ignore_index=True)


def simula_sih(anos=ANOS_PADRAO, seed: int = SEED, n_por_muni_ano: int = 3) -> pd.DataFrame:
    """Microdado simulado com o esquema e os códigos reais do SIH.

    ⚠️ **A simulação não embute relação nenhuma entre dose e intoxicação**, nem
    quebra em 2019. Rodar o teste do canal contra ela devolve nulo por
    construção, e esse nulo não diz nada sobre o Ceará. É fixture de código.

    Calibrada só na ordem de grandeza e na composição por intenção que a
    literatura brasileira descreve — parcela grande de autoprovocada —, para que
    o script tenha o que separar.
    """
    rng = np.random.default_rng(seed)
    municipios = [f"{239000 + i:06d}" for i in range(1, 185)]

    # composição por intenção; autoprovocada pesa porque é assim no Brasil rural
    intencoes = ["X48", "X68", "X87", "Y18"]
    pesos_intencao = [0.34, 0.52, 0.02, 0.12]
    t60 = ["T600", "T603", "T601", "T602", "T609"]
    pesos_t60 = [0.45, 0.25, 0.10, 0.10, 0.10]

    linhas = []
    for cod in municipios:
        for ano in anos:
            n = int(rng.poisson(n_por_muni_ano))
            if n == 0:
                continue
            mes = rng.integers(1, 13, n)
            dia = rng.integers(1, 29, n)
            # metade das AIH traz o T60 como principal e o X como secundário;
            # a outra metade inverte — é assim que faturamento se comporta
            inverte = rng.random(n) < 0.5
            causa = rng.choice(intencoes, n, p=pesos_intencao)
            efeito = rng.choice(t60, n, p=pesos_t60)
            linhas.append(
                pd.DataFrame(
                    {
                        "DIAG_PRINC": np.where(inverte, efeito, causa),
                        "DIAG_SECUN": np.where(inverte, causa, efeito),
                        "MUNIC_RES": cod,
                        "DT_INTER": [f"{ano}{m:02d}{d:02d}" for m, d in zip(mes, dia)],
                        "MORTE": rng.choice([0, 1], n, p=[0.94, 0.06]),
                        "IDADE": rng.integers(5, 80, n),
                        "SEXO": rng.choice([1, 3], n),
                    }
                )
            )

    df = pd.concat(linhas, ignore_index=True)
    # ruído: internações sem CID de agrotóxico, que o filtro tem de descartar
    outras = df.sample(int(0.6 * len(df)), random_state=seed).copy()
    outras["DIAG_PRINC"] = "J189"   # pneumonia
    outras["DIAG_SECUN"] = ""
    # e residentes de fora do Ceará
    fora = df.sample(int(0.05 * len(df)), random_state=seed + 1).copy()
    fora["MUNIC_RES"] = rng.choice(["350010", "292740"], size=len(fora))
    return pd.concat([df, outras, fora], ignore_index=True).sample(
        frac=1, random_state=seed
    ).reset_index(drop=True)


def carrega_internacoes(
    fonte: str = "auto", caminhos: list[Path] | None = None, anos=ANOS_PADRAO, seed: int = SEED
) -> tuple[pd.DataFrame, str]:
    """Dispatcher: 'arquivos' | 'simulado' | 'auto'.

    Não há caminho de download aqui de propósito: a fonte real vem do
    `00_export_datazoom.R`, que é R, e a fronteira entre as linguagens é arquivo.
    """
    if fonte == "simulado":
        return simula_sih(anos, seed), "simulado"
    if fonte == "arquivos":
        return carrega_de_arquivos(caminhos or []), "arquivos"
    if caminhos:
        try:
            return carrega_de_arquivos(caminhos), "arquivos"
        except Exception as erro:  # noqa: BLE001
            print(f"[aviso] leitura dos arquivos falhou ({type(erro).__name__}: {erro}).")
    print("[aviso] Sem arquivo do SIH. Rode scripts/data_prep/00_export_datazoom.R")
    print("[aviso] --bases sih na sua máquina. Caindo para SIMULADO — não é evidência.")
    return simula_sih(anos, seed), "simulado"


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

def imprime_resumo(individual: pd.DataFrame, painel: pd.DataFrame, fonte: str) -> None:
    barra = "=" * 84
    print(barra)
    print(f"INTOXICAÇÃO POR AGROTÓXICO — CEARÁ, município × ano-mês (SIH) | fonte: {fonte.upper()}")
    if fonte == "simulado":
        print("!! DADOS SIMULADOS. A simulação NÃO embute relação dose–intoxicação")
        print("!! nem quebra em 2019: um nulo aqui é construção, não achado.")
    print(barra)
    print(f"internações com CID de agrotóxico : {len(individual):,}")
    print(f"municípios                        : {painel['cod_ibge6'].nunique()}")
    print(f"células município-mês             : {len(painel):,}")
    print(f"período                           : {painel['ano'].min()}–{painel['ano'].max()}")
    print("-" * 84)

    print("POR INTENÇÃO — não somar; são mecanismos diferentes")
    total = max(int(painel["n_internacoes_com_cid"].sum()), 1)
    for nome in FAMILIAS_INTENCAO:
        n = int(painel[f"n_{nome}"].sum())
        n_p = int(painel[f"n_{nome}_principal"].sum())
        marca = "  ← canal de substituição" if nome == "acidental" else (
                "  ← candidato a PLACEBO" if nome == "autoprovocada" else "")
        print(f"  {nome:<16} {n:>7,}  ({n/total:>5.1%})   como principal: {n_p:>7,}{marca}")

    print("\nPOR MOLÉCULA (T60)")
    for nome in FAMILIAS_MOLECULA:
        n = int(painel[f"n_{nome}"].sum())
        print(f"  {nome:<32} {n:>7,}  ({n/total:>5.1%})")

    print("\nRECORTES DA FAMÍLIA ACIDENTAL")
    n_acid = max(int(painel["n_acidental"].sum()), 1)
    print(f"  em idade de trabalho ({IDADE_TRABALHO_MIN}–{IDADE_TRABALHO_MAX}) : "
          f"{int(painel['n_acidental_idade_trabalho'].sum()):>7,}  "
          f"({painel['n_acidental_idade_trabalho'].sum()/n_acid:>5.1%})")
    print(f"  com óbito na internação            : "
          f"{int(painel['n_acidental_obito'].sum()):>7,}  "
          f"({painel['n_acidental_obito'].sum()/n_acid:>5.1%})")

    pequenas = painel["celula_pequena"].mean()
    print("-" * 84)
    print(f"células com <{CELULA_PEQUENA} internações        : {pequenas:.1%}")
    if pequenas > 0.90:
        print(f"  ⚠️ {pequenas:.0%} das células são finas. Intoxicação internada é evento raro:")
        print("     o teste vai precisar de agregação mais grossa (município×ano, ou")
        print("     faixas de dose empilhadas). Propriedade do desfecho, não defeito.")
    print(barra)
    print("Como usar:")
    print("  • Rode a série ACIDENTAL contra a dose — é a que o canal de")
    print("    substituição prevê que se move, e no sentido OPOSTO ao perinatal.")
    print("  • Rode AUTOPROVOCADA como placebo: o ban proíbe método, não molécula,")
    print("    então ela NÃO deveria se mover. Se as duas se moverem juntas, a")
    print("    explicação não é substituição — é algo que move internação em geral.")
    print("  • ⚠️ SIH é internação, não incidência: só o caso grave, só rede SUS.")
    print("    O nível é subestimado; o estimando é efeito sobre caso internado.")
    print("  • ⚠️ SIH é faturamento: 'principal' e 'secundário' não são a mesma")
    print("    coisa. As duas contagens saem lado a lado de propósito.")
    print("  • Qual família é o desfecho é decisão sua. O script separa, não escolhe.")
    print(barra)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--fonte", choices=("auto", "arquivos", "simulado"), default="auto")
    parser.add_argument("--caminho", type=Path, nargs="*", default=[],
                        help="SIH exportado pelo 00_export_datazoom.R (.csv.gz/.parquet).")
    parser.add_argument("--anos", type=int, nargs="*", default=list(ANOS_PADRAO))
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    bruto, fonte = carrega_internacoes(args.fonte, args.caminho, tuple(args.anos), args.seed)
    individual = prepara_internacoes(bruto, args.anos)
    if individual.empty:
        print("[erro] Nenhuma internação com CID de agrotóxico sobrou. Confira:")
        print("       1. DIAG_PRINC/DIAG_SECUN trazem CID-10 (T60*, X48, X68, X87, Y18)?")
        print("       2. MUNIC_RES tem código IBGE começando em 23?")
        print("       3. DT_INTER está em AAAAMMDD (o formato do SIH)?")
        return 1

    painel = colapsa_muni_mes(individual)
    painel["fonte"] = fonte
    imprime_resumo(individual, painel, fonte)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    sufixo = "" if fonte != "simulado" else "__simulado"
    destino = args.out_dir / f"{NOME_SAIDA}{sufixo}.parquet"
    painel.to_parquet(destino, index=False)
    print(f"[ok] painel -> {destino}")
    print("[nota] data/processed/ é gitignored: microdado não vai para o repositório.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
