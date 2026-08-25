#!/usr/bin/env python3
"""Óbito fetal (SIM) colapsado a município × ano-mês — o teste de seleção.

**Por que este script existe.** O desfecho principal do Ensaio 1 é peso ao
nascer entre **nascidos vivos**. Se o ban reduziu óbito fetal, fetos que antes
morriam passam a nascer vivos — e entram na amostra pela cauda de baixo peso,
puxando a média para baixo, na direção *oposta* ao efeito esperado e competindo
pelo mesmo espaço de magnitude. É a flag 6 do CLAUDE.md: seleção para nascimento
vivo. Um efeito estimado de zero pode ser um efeito real cancelado por
recomposição da amostra.

Antes de escolher qualquer correção, é preciso saber se o problema existe. O
teste barato (docs/ars/07-layer4-perguntas-abertas.md §Pergunta 1): **rodar a
série de óbito fetal contra a dose, com o mesmo desenho.** Se óbito fetal não se
move com a dose, a seleção é problema teórico e não atual, e a discussão acaba
num parágrafo de limitações — com o teste como evidência. Se se move, aí a
escolha difícil se torna necessária, e só aí.

**O que este script NÃO faz.** Não roda o teste — ele prepara a série. E não
escolhe entre as três rotas conhecidas de correção (reporte conjunto, desfecho
composto, limites de seleção amostral). Aquilo é decisão do pesquisador, e
continua registrada como aberta.

Notas de fonte que o código carrega junto:

  • **Óbito fetal não é arquivo separado.** No SIM moderno vem dentro do DO
    (`DO<UF><ano>`), identificado por TIPOBITO: 1 = fetal, 2 = não fetal. O
    filtro por TIPOBITO é a primeira coisa que este script faz e é o que ele
    mais precisa acertar — errar aqui contamina a série com óbitos infantis, que
    são outro desfecho.

  • **Subnotificação é a ameaça central, e ela é heterogênea.** A notificação
    compulsória alcança perdas de ≥ 22 semanas OU ≥ 500 g; abaixo disso o
    registro é irregular e varia por município e por ano. Como a variação
    espúria entre municípios é justamente o que o desenho usa como identificação,
    subnotificação diferencial não é ruído: é confundidor. Daí a coluna
    `n_obito_fetal_22sem` sair ao lado do total — se as duas séries divergirem,
    a restrita é a comparável, e a divergência em si é diagnóstico.

  • **Denominador.** A taxa relevante é sobre o total de gestações que chegaram
    ao registro, isto é, nascidos vivos + óbitos fetais. Usar só nascidos vivos
    no denominador embute a própria seleção que se quer medir.

  • **Data de óbito, não de exposição.** Mesmo problema do script 02: DTOBITO é
    quando terminou, não quando expôs. A retroprojeção por semanas de gestação
    fica em scripts/build_panel/, e colapsar por mês existe para deixá-la
    possível.

Uso:
    python scripts/data_prep/03_clean_fetal_deaths.py
    python scripts/data_prep/03_clean_fetal_deaths.py --caminho data/raw/DOCE*.parquet
    python scripts/data_prep/03_clean_fetal_deaths.py --fonte simulado \\
        --nascimentos data/processed/nascimentos_ce_muni_mes__simulado.parquet

Saída: data/processed/obitos_fetais_ce_muni_mes.parquet (gitignored). Rodadas
simuladas gravam com sufixo "__simulado", como nos scripts 01 e 02.
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
ANOS_PADRAO = (2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)  # espelha o script 02
OUT_DIR = Path("data/processed")
NOME_SAIDA = "obitos_fetais_ce_muni_mes"
SEED = 20190613  # mesma seed dos scripts 01 e 02

# Colunas do DATASUS/SIM (DO) usadas aqui.
COLUNAS_SIM = (
    "TIPOBITO",    # 1 = fetal, 2 = não fetal — o filtro que define a série
    "DTOBITO",     # data do óbito, DDMMAAAA (mesmo formato de DTNASC)
    "CODMUNRES",   # município de residência, código IBGE de 6 dígitos
    "PESO",        # peso, em gramas
    "SEMAGESTAC",  # semanas de gestação (99 = ignorado)
    "GESTACAO",    # faixa de gestação (categórica) — fallback de SEMAGESTAC
    "OBITOPARTO",  # 1 = antes, 2 = durante, 3 = depois do parto
    "IDADEMAE",
)

TIPOBITO_FETAL = 1

# Mesmas faixas plausíveis do script 02, com uma diferença: o piso de peso desce.
# Perdas fetais precoces pesam muito menos que qualquer nascido vivo viável, e
# cortar em 200 g jogaria fora exatamente a cauda que a seleção move.
PESO_MIN_G, PESO_MAX_G = 100, 8000
SEMANAS_MIN, SEMANAS_MAX = 20, 45

# Limiar de notificação compulsória. Vale ≥ 22 semanas OU ≥ 500 g — é "ou", não
# "e": uma perda de 20 semanas com 520 g é de registro obrigatório, e uma de 23
# semanas com 400 g também. Tratar como "e" descartaria registros válidos.
LIMIAR_REGISTRO_SEM = 22
LIMIAR_REGISTRO_G = 500

# GESTACAO (SIM, mesma codificação do SINASC):
#   1 = menos de 22 semanas   2 = 22 a 27   3 = 28 a 31
#   4 = 32 a 36               5 = 37 a 41   6 = 42 e mais   9 = ignorado
# Para o limiar de 22 semanas só a categoria 1 é inteiramente abaixo; as demais
# (2–6) são inteiramente >= 22. Nenhuma faixa cruza o corte, então o fallback
# categórico não erra a classificação.
GESTACAO_ACIMA_22 = {1: False, 2: True, 3: True, 4: True, 5: True, 6: True, 9: None}

CELULA_PEQUENA = 5  # óbitos fetais por município-mês abaixo disso: taxa é ruído


# --------------------------------------------------------------------------
# Limpeza
# --------------------------------------------------------------------------

# --- datazoom.saude (R) -----------------------------------------------------
# Conferido contra R/dictionary.R do repositório datazoompuc/datazoom.saude,
# seção `datasus_sim`. Duas convenções pelo parâmetro `language`; **o padrão do
# pacote é "eng"**, então as duas entram.
#
# ⚠️ `IDADE` NÃO é alias de IDADEMAE. No dicionário do SIM os dois são campos
# separados: `idade` é a idade do FALECIDO, em código composto (1º dígito =
# unidade: 1=horas, 2=dias, 3=meses, 4=anos), que num óbito fetal é a do feto;
# `idademae` é a da mãe e o pacote mantém o nome. Mapear um no outro punha 401
# dentro de `idade_mae_media`.
#
# ⚠️ O dicionário do SIM **não tem `semagestac`** — a duração gestacional só vem
# na forma agrupada (`duracao_gestacao`). Com fonte datazoom, o fallback
# categórico de `deriva_acima_limiar` deixa de ser fallback e vira o único
# caminho, e `share_gest_por_faixa` sai 100%. Isso não é defeito: é o que a
# fonte oferece, e a coluna existe justamente para deixar visível.
ALIASES_DATAZOOM = {
    # português (language = "pt")
    "PESO_NASCIMENTO": "PESO",          # faltava: sem isto o peso fetal vira NaN
    "DURACAO_GESTACAO": "GESTACAO",     # faltava: e com ele o limiar de 22 semanas
    # inglês (language = "eng", o PADRÃO do pacote)
    "BIRTH_WEIGHT": "PESO",
    "GESTATIONAL_DURATION": "GESTACAO",
}
# `tipobito`, `dtobito`, `codmunres`, `idademae` e `obitoparto` o pacote mantém
# iguais nas duas línguas — não precisam de alias.

def padroniza_colunas(df: pd.DataFrame) -> pd.DataFrame:
    """Nomes em maiúscula e garante que as colunas esperadas existam (NaN se não)."""
    saida = df.copy()
    saida.columns = [str(c).strip().upper() for c in saida.columns]
    saida = saida.rename(columns=ALIASES_DATAZOOM)
    faltando = [c for c in COLUNAS_SIM if c not in saida.columns]
    for col in faltando:
        saida[col] = np.nan
    if faltando:
        print(f"[aviso] colunas ausentes na fonte, preenchidas com NaN: {faltando}")
    return saida[list(COLUNAS_SIM)]


def filtra_fetal(df: pd.DataFrame) -> pd.DataFrame:
    """Mantém só óbito fetal (TIPOBITO == 1).

    O filtro mais importante do script. TIPOBITO == 2 é óbito não fetal — outro
    desfecho, outra população, e deixá-lo entrar transformaria a série num
    agregado sem sentido. Ausente também sai: TIPOBITO é campo obrigatório na
    DO, então NaN aqui é erro de leitura, não categoria.
    """
    tipo = pd.to_numeric(df["TIPOBITO"], errors="coerce")
    return df[tipo == TIPOBITO_FETAL].copy()


# Formatos de data aceitos, tentados NESTA ORDEM. Explícitos de propósito:
# `format="mixed"` infere por elemento e, num campo brasileiro, lê "01/02/2017"
# como janeiro — troca dia por mês e joga o nascimento na célula errada do painel
# mensal. Num desenho cujo tratamento entra em janeiro de 2019, mês errado é
# contaminação da janela do evento, e silenciosa. Já `dayfirst=True` conserta a
# barra e quebra o ISO ("2017-03-01" vira janeiro). Nenhuma inferência serve:
# a lista abaixo é fechada e determinística.
FORMATOS_DATA = ("%d%m%Y", "%Y-%m-%d", "%d/%m/%Y")


def _para_data(bruto: pd.Series) -> pd.Series:
    """Converte para data tentando os formatos conhecidos, sem inferir."""
    texto = bruto.astype("string").str.strip().str.replace(r"\.0$", "", regex=True)
    so_digitos = texto.str.fullmatch(r"\d+").fillna(False)
    texto = texto.mask(so_digitos, texto.str.zfill(8))

    data = pd.Series(pd.NaT, index=bruto.index, dtype="datetime64[ns]")
    for formato in FORMATOS_DATA:
        se_falta = data.isna()
        if not se_falta.any():
            break
        data.loc[se_falta] = pd.to_datetime(
            texto[se_falta], format=formato, errors="coerce"
        )
    return data


def extrai_ano_mes(dtobito: pd.Series) -> pd.DataFrame:
    """DTOBITO (DDMMAAAA) -> ano e mês. Mesma lógica do DTNASC no script 02:
    o zero à esquerda do dia some quando o campo passa por leitor numérico."""
    data = _para_data(dtobito)
    return pd.DataFrame(
        {
            "ano": data.dt.year.astype("Int64"),
            "mes": data.dt.month.astype("Int64"),
        },
        index=dtobito.index,
    )


def limpa_peso(peso: pd.Series) -> pd.Series:
    """Peso em gramas dentro da faixa plausível; fora dela, ausente."""
    valores = pd.to_numeric(peso, errors="coerce")
    return valores.where(valores.between(PESO_MIN_G, PESO_MAX_G))


def limpa_semanas(semagestac: pd.Series) -> pd.Series:
    """Semanas de gestação; 99 (ignorado) e implausíveis viram ausente."""
    valores = pd.to_numeric(semagestac, errors="coerce")
    return valores.where(valores.between(SEMANAS_MIN, SEMANAS_MAX))


def deriva_acima_limiar(
    semanas_limpas: pd.Series, gestacao: pd.Series, peso_limpo: pd.Series
) -> pd.DataFrame:
    """Marca os óbitos de notificação compulsória (≥ 22 semanas OU ≥ 500 g).

    Devolve `acima_limiar` e `limiar_por_faixa` (1 quando a classificação veio
    do fallback categórico GESTACAO, porque SEMAGESTAC faltava).

    Regra de ausência: se nem semanas nem peso são conhecidos, o registro fica
    **ausente**, não False. Chamar de "abaixo do limiar" o que só é
    desconhecido inventaria justamente o padrão de subnotificação que a coluna
    deveria medir.
    """
    por_semanas = pd.Series(
        np.where(semanas_limpas.isna(), np.nan, (semanas_limpas >= LIMIAR_REGISTRO_SEM).astype(float)),
        index=semanas_limpas.index,
        dtype="float64",
    )
    faixa = pd.to_numeric(gestacao, errors="coerce").map(GESTACAO_ACIMA_22)
    por_faixa = pd.Series(
        [np.nan if v is None or pd.isna(v) else float(v) for v in faixa],
        index=gestacao.index,
        dtype="float64",
    )
    usou_fallback = por_semanas.isna() & por_faixa.notna()
    gestacional = por_semanas.fillna(por_faixa)

    por_peso = pd.Series(
        np.where(peso_limpo.isna(), np.nan, (peso_limpo >= LIMIAR_REGISTRO_G).astype(float)),
        index=peso_limpo.index,
        dtype="float64",
    )

    # "OU" com ausentes: um lado True basta, mesmo com o outro desconhecido.
    # Só é False quando algum critério é conhecido e nenhum conhecido é True;
    # com ambos ausentes, ausente.
    algum_true = (gestacional == 1) | (por_peso == 1)
    algum_conhecido = gestacional.notna() | por_peso.notna()
    acima = pd.Series(
        np.where(algum_true, 1.0, np.where(algum_conhecido, 0.0, np.nan)),
        index=gestacional.index,
        dtype="float64",
    )
    return pd.DataFrame({"acima_limiar": acima, "limiar_por_faixa": usou_fallback.astype(float)})


def filtra_ceara(df: pd.DataFrame) -> pd.DataFrame:
    """Mantém só residentes no Ceará (CODMUNRES começando em 23)."""
    cod = df["CODMUNRES"].astype("string").str.strip().str.replace(r"\.0$", "", regex=True)
    cod = cod.str.zfill(6)
    saida = df.copy()
    saida["cod_ibge6"] = cod
    return saida[cod.str.startswith(UF_CEARA).fillna(False)].copy()


def prepara_obitos(bruto: pd.DataFrame, anos=None) -> pd.DataFrame:
    """Pipeline de limpeza no nível do indivíduo, antes do colapso.

    Ordem deliberada: TIPOBITO primeiro. Filtrar Ceará antes de filtrar fetal
    daria o mesmo resultado, mas o filtro que define a série vem na frente para
    que qualquer inspeção do meio do caminho já esteja olhando óbito fetal.
    """
    df = filtra_ceara(padroniza_colunas(bruto))
    df = filtra_fetal(df)
    df = pd.concat([df, extrai_ano_mes(df["DTOBITO"])], axis=1)
    df["peso_g"] = limpa_peso(df["PESO"])
    df["semanas"] = limpa_semanas(df["SEMAGESTAC"])
    df = pd.concat([df, deriva_acima_limiar(df["semanas"], df["GESTACAO"], df["peso_g"])], axis=1)
    df = df[df["ano"].notna() & df["mes"].notna()]
    if anos is not None:
        df = df[df["ano"].isin(list(anos))]
    return df.reset_index(drop=True)


def colapsa_muni_mes(individual: pd.DataFrame) -> pd.DataFrame:
    """Colapsa a `cod_ibge6` × ano × mês — a MESMA chave do script 02.

    Isso não é coincidência de estilo: é a condição para o teste de seleção
    existir. Sem chave idêntica não há junção com o painel de nascidos vivos, e
    sem junção não há denominador nem comparação.

    `n_obito_fetal_22sem` soma `acima_limiar` ignorando ausentes, então um óbito
    com semanas e peso desconhecidos **não** entra no numerador. É a direção
    conservadora, e `n_limiar_valido` denuncia quanto disso houve: quando ele
    fica bem abaixo de `n_obito_fetal`, a série restrita está subcontando por
    falta de informação, não por ausência de perdas.
    """
    agrupado = individual.groupby(["cod_ibge6", "ano", "mes"], dropna=True)
    painel = agrupado.agg(
        n_obito_fetal=("cod_ibge6", "size"),
        n_obito_fetal_22sem=("acima_limiar", "sum"),
        n_limiar_valido=("acima_limiar", "count"),
        n_peso_valido=("peso_g", "count"),
        peso_medio_fetal=("peso_g", "mean"),
        n_gest_valido=("semanas", "count"),
        semanas_media=("semanas", "mean"),
        share_gest_por_faixa=("limiar_por_faixa", "mean"),
        idade_mae_media=("IDADEMAE", "mean"),
    ).reset_index()

    painel["ano"] = painel["ano"].astype(int)
    painel["mes"] = painel["mes"].astype(int)
    painel["n_obito_fetal_22sem"] = painel["n_obito_fetal_22sem"].astype(int)
    painel["celula_pequena"] = painel["n_obito_fetal"] < CELULA_PEQUENA
    return painel.sort_values(["cod_ibge6", "ano", "mes"]).reset_index(drop=True)


def junta_denominador(painel_fetal: pd.DataFrame, painel_nasc: pd.DataFrame) -> pd.DataFrame:
    """Acrescenta a taxa de óbito fetal usando o painel de nascidos vivos.

    Denominador = nascidos vivos + óbitos fetais, não só nascidos vivos. A
    diferença é o ponto inteiro do teste: o denominador é a coorte de gestações
    que chegaram ao registro, e o desfecho é qual fração dela terminou em óbito.
    Dividir só por nascidos vivos faria a própria seleção entrar no denominador.

    A junção é `outer`: município-mês com nascimento e sem óbito fetal é
    informação (taxa zero), não ausência, e some numa junção interna. O
    contrário — óbito sem nascimento registrado — não deveria acontecer e sai
    marcado em `sem_denominador` para inspeção.
    """
    nasc = painel_nasc[["cod_ibge6", "ano", "mes", "n_nascimentos"]].copy()
    nasc["cod_ibge6"] = nasc["cod_ibge6"].astype(str)
    fetal = painel_fetal.copy()
    fetal["cod_ibge6"] = fetal["cod_ibge6"].astype(str)

    junto = fetal.merge(nasc, on=["cod_ibge6", "ano", "mes"], how="outer")
    contagens = ["n_obito_fetal", "n_obito_fetal_22sem", "n_limiar_valido",
                 "n_peso_valido", "n_gest_valido"]
    for col in contagens:
        junto[col] = junto[col].fillna(0).astype(int)
    junto["celula_pequena"] = junto["n_obito_fetal"] < CELULA_PEQUENA

    junto["sem_denominador"] = junto["n_nascimentos"].isna() & (junto["n_obito_fetal"] > 0)
    nascidos = junto["n_nascimentos"].fillna(0)
    coorte = nascidos + junto["n_obito_fetal"]
    junto["n_nascimentos"] = nascidos.astype(int)
    junto["coorte_registrada"] = coorte.astype(int)
    junto["taxa_obito_fetal"] = np.where(coorte > 0, junto["n_obito_fetal"] / coorte, np.nan)
    junto["taxa_obito_fetal_22sem"] = np.where(
        coorte > 0, junto["n_obito_fetal_22sem"] / coorte, np.nan
    )
    return junto.sort_values(["cod_ibge6", "ano", "mes"]).reset_index(drop=True)


# --------------------------------------------------------------------------
# Fontes
# --------------------------------------------------------------------------

def carrega_de_arquivos(caminhos: list[Path]) -> pd.DataFrame:
    """Lê arquivos SIM já baixados (.parquet / .csv / .csv.gz).

    Caminho mais robusto para a fonte real: baixe o DO uma vez do DATASUS e
    aponte para cá. `.dbc` precisa ser convertido antes (pysus/read.dbc).
    """
    if not caminhos:
        raise ValueError("Nenhum caminho informado.")
    pedacos = []
    for caminho in caminhos:
        if caminho.suffix == ".parquet":
            pedacos.append(pd.read_parquet(caminho))
        elif caminho.suffix in (".csv", ".gz"):
            pedacos.append(pd.read_csv(caminho, dtype=str, low_memory=False))
        else:
            raise ValueError(f"Extensão não suportada: {caminho} (converta .dbc antes).")
    return pd.concat(pedacos, ignore_index=True)


def carrega_de_pysus(anos=ANOS_PADRAO) -> pd.DataFrame:
    """Baixa SIM/CE via pysus, grupo CID10 (arquivos DO<UF><ano>).

    A API do pysus mudou entre versões maiores; tentamos a atual e caímos para a
    ⚠️ Usa `client._run_async`, método PRIVADO. Verificado que existe em 2.10.0,
    mas nome privado não tem contrato de estabilidade: é o pin de versão em
    requirements.txt que torna isso seguro, não a API. Ao subir o pysus, conferir
    este ponto primeiro.
    """
    try:
        from pysus.api import PySUSClient

        pedacos = []
        with PySUSClient() as client:
            ftp = client.get_ftp()
            datasets = client._run_async(ftp.datasets())
            base = next(dataset for dataset in datasets if dataset.name == "SIM")
            for ano in anos:
                arquivos = client._run_async(base.search(group="DO", state="CE", year=ano))
                for arquivo in arquivos:
                    parquet = client.download_to_parquet(arquivo)
                    pedacos.append(parquet.to_dataframe())
        if not pedacos:
            raise RuntimeError("pysus não devolveu arquivos SIM para CE.")
        return pd.concat(pedacos, ignore_index=True)
    except ImportError as erro:
        # Sem fallback para `pysus.online_data` / `pysus.ftp`: verificado contra
        # o pacote instalado que os DOIS somem em 2.10.0 (ModuleNotFoundError).
        # Um fallback para módulo inexistente não é rede de segurança — é uma
        # mensagem de erro apontando para o lugar errado.
        raise RuntimeError(
            f"pysus indisponível ou incompatível ({type(erro).__name__}: {erro}).\n"
            "  requirements.txt pina pysus==2.10.0, cuja API é `pysus.api.PySUSClient`.\n"
            "  ⚠️ Se o erro for 'No module named yaml': pysus 2.10.0 IMPORTA yaml mas\n"
            "     não o declara como dependência. Instale `pyyaml` (já está no\n"
            "     requirements.txt deste repositório por causa disso).\n"
            "  Sem pysus, use --fonte arquivos --caminho com o DBC baixado à mão."
        ) from erro


def simula_sim(anos=ANOS_PADRAO, seed: int = SEED, n_por_muni_mes: int = 18) -> pd.DataFrame:
    """Microdado simulado com as colunas e os tipos reais do SIM.

    Calibrado na ordem de grandeza brasileira: taxa de mortalidade fetal em
    torno de 1% das gestações registradas. Como no script 02, a simulação injeta
    de propósito o que a limpeza precisa aguentar:

      • **TIPOBITO == 2 em maioria.** Óbitos não fetais entram na base porque é
        assim que o DO chega — se o filtro por TIPOBITO quebrar, a série
        explode, e é bom que o teste veja isso.
      • SEMAGESTAC ignorado (99) em ~8% dos casos (cobertura pior que no SINASC,
        que é o realista), com GESTACAO disponível para o fallback.
      • Perdas abaixo do limiar de notificação, para a coluna `_22sem` ter o que
        distinguir.
      • ~5% de linhas de fora do Ceará.

    Nada disso é evidência sobre o Ceará — é fixture para o código. Em
    particular, **a simulação não embute relação nenhuma entre dose e óbito
    fetal**: rodar o teste de seleção contra ela devolve um nulo por construção,
    e esse nulo não diz nada sobre o Ceará.
    """
    rng = np.random.default_rng(seed)
    municipios = [f"{239000 + i:06d}" for i in range(1, 185)]  # convenção dos scripts 01 e 02
    tamanho = rng.lognormal(mean=np.log(n_por_muni_mes), sigma=0.9, size=len(municipios))

    linhas = []
    for cod, escala in zip(municipios, tamanho):
        for ano in anos:
            for mes in range(1, 13):
                nascimentos = max(escala, 0.5)
                n_fetal = int(rng.poisson(nascimentos * 0.01))     # ~1% de óbito fetal
                n_outros = int(rng.poisson(nascimentos * 0.05))    # óbitos não fetais no DO
                n = n_fetal + n_outros
                if n == 0:
                    continue

                tipobito = np.concatenate([np.full(n_fetal, 1), np.full(n_outros, 2)])

                # ~20% das perdas fetais abaixo do limiar de notificação
                precoce = rng.random(n) < 0.20
                semanas = np.where(
                    precoce, rng.integers(20, 22, n), rng.integers(22, 41, n)
                ).astype(float)
                peso = np.where(
                    precoce,
                    rng.normal(380, 90, n).clip(PESO_MIN_G, 640),
                    rng.normal(1900, 700, n).clip(400, 4200),
                )
                dia = rng.integers(1, 29, n)

                # ~8% com SEMAGESTAC ignorado: exercita o fallback por GESTACAO
                sem_semana = rng.random(n) < 0.08
                semagestac = np.where(sem_semana, 99, semanas).astype(int)
                gestacao = np.select(
                    [semanas < 22, semanas < 28, semanas < 32, semanas < 37, semanas < 42],
                    [1, 2, 3, 4, 5],
                    default=6,
                )
                # ~2% com peso ignorado, codificado como no DATASUS
                peso_txt = pd.Series(np.round(peso).astype(int).astype(str)).str.zfill(4)
                peso_txt = peso_txt.mask(pd.Series(rng.random(n) < 0.02), "0000")

                linhas.append(
                    pd.DataFrame(
                        {
                            "TIPOBITO": tipobito,
                            "DTOBITO": [f"{d:02d}{mes:02d}{ano}" for d in dia],
                            "CODMUNRES": cod,
                            "PESO": peso_txt.to_numpy(),
                            "SEMAGESTAC": semagestac,
                            "GESTACAO": gestacao,
                            "OBITOPARTO": rng.integers(1, 4, n),
                            "IDADEMAE": rng.integers(14, 45, n),
                        }
                    )
                )

    df = pd.concat(linhas, ignore_index=True)

    # ~5% de residentes fora do Ceará, para que o filtro de UF tenha o que filtrar
    n_fora = int(0.05 * len(df))
    fora = df.sample(n_fora, random_state=seed).copy()
    fora["CODMUNRES"] = rng.choice(["350010", "292740", "150140"], size=n_fora)
    return pd.concat([df, fora], ignore_index=True).sample(frac=1, random_state=seed).reset_index(drop=True)


def carrega_obitos(
    fonte: str = "auto", caminhos: list[Path] | None = None, anos=ANOS_PADRAO, seed: int = SEED
) -> tuple[pd.DataFrame, str]:
    """Dispatcher: 'arquivos' | 'pysus' | 'simulado' | 'auto'.

    'auto' = arquivos (se houver) -> pysus -> simulado, como no script 02.
    """
    if fonte == "simulado":
        return simula_sim(anos, seed), "simulado"
    if fonte == "arquivos":
        return carrega_de_arquivos(caminhos or []), "arquivos"
    if fonte == "pysus":
        return carrega_de_pysus(anos), "pysus"

    if caminhos:
        try:
            return carrega_de_arquivos(caminhos), "arquivos"
        except Exception as erro:  # noqa: BLE001
            print(f"[aviso] leitura dos arquivos falhou ({type(erro).__name__}: {erro}).")
    try:
        return carrega_de_pysus(anos), "pysus"
    except Exception as erro:  # noqa: BLE001
        print(f"[aviso] acesso via pysus indisponível ({type(erro).__name__}: {erro}).")
        print("[aviso] Caindo para microdado SIMULADO. Nada abaixo é evidência empírica.")
        return simula_sim(anos, seed), "simulado"


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

def imprime_resumo(
    individual: pd.DataFrame, painel: pd.DataFrame, fonte: str, tem_denominador: bool
) -> None:
    barra = "=" * 84
    print(barra)
    print(f"ÓBITO FETAL — CEARÁ, município de residência × ano-mês (SIM) | fonte: {fonte.upper()}")
    if fonte == "simulado":
        print("!! DADOS SIMULADOS — números inventados, servem só para validar o código.")
        print("!! A simulação NÃO embute relação dose–óbito fetal: um nulo aqui é")
        print("!! construção, não achado.")
    print(barra)
    print(f"óbitos fetais (CE, após limpeza): {len(individual):,}")
    print(f"municípios                      : {painel['cod_ibge6'].nunique()}")
    print(f"células município-mês           : {len(painel):,}")
    print(f"período                         : {painel['ano'].min()}–{painel['ano'].max()}")
    print("-" * 84)

    total = painel["n_obito_fetal"].sum()
    acima = painel["n_obito_fetal_22sem"].sum()
    share_acima = acima / max(total, 1)
    print(f"acima do limiar de notificação  : {acima:,} de {total:,}  ({share_acima:.1%})")
    print(f"  (>= {LIMIAR_REGISTRO_SEM} semanas OU >= {LIMIAR_REGISTRO_G} g — notificação compulsória)")
    if tem_denominador:
        coorte = painel["coorte_registrada"].sum()
        print(f"taxa de óbito fetal (agregada)  : {total / max(coorte, 1):.2%}")
        print(f"  denominador = nascidos vivos + óbitos fetais = {coorte:,}")
        orfaos = int(painel["sem_denominador"].sum())
        if orfaos:
            print(f"⚠️  {orfaos} células com óbito fetal e SEM nascimento registrado — inspecionar.")
    else:
        print("taxa não calculada. Rode com --nascimentos <painel do script 02>.")
    print("-" * 84)

    falta_peso = 1 - painel["n_peso_valido"].sum() / max(total, 1)
    falta_gest = 1 - painel["n_gest_valido"].sum() / max(total, 1)
    fallback = np.average(
        painel["share_gest_por_faixa"].fillna(0),
        weights=painel["n_obito_fetal"].clip(lower=0),
    ) if total else 0.0
    pequenas = painel["celula_pequena"].mean()
    print(f"peso ausente                    : {falta_peso:.2%}")
    print(f"gestação ausente                : {falta_gest:.2%}")
    print(f"limiar vindo de GESTACAO        : {fallback:.2%}  (checar salto em torno de 2019)")
    print(f"células com <{CELULA_PEQUENA} óbitos          : {pequenas:.1%}  (taxa é ruído; ponderar por n)")
    print(barra)
    print("Como usar (ver docs/ars/07-layer4-perguntas-abertas.md §Pergunta 1):")
    if pequenas > 0.90:
        print(f"  ⚠️  {pequenas:.0%} das células têm menos de {CELULA_PEQUENA} óbitos. Óbito fetal é evento raro:")
        print("     no nível município×mês a taxa quase não existe. O teste precisa de")
        print("     agregação mais grossa (município×ano, ou faixas de dose empilhadas)")
        print("     — não de mais limpeza. Isto é propriedade do desfecho, não defeito.")
    print("  • Este painel é o INSUMO do teste de seleção, não o teste. Rode a série")
    print("    contra a dose com o mesmo desenho do desfecho principal.")
    print("  • Se óbito fetal NÃO se move com a dose: a seleção é problema teórico,")
    print("    vira parágrafo de limitações com o teste como evidência.")
    print("  • Se SE MOVE: a escolha entre reporte conjunto, desfecho composto e")
    print("    limites de seleção passa a ser necessária — e é sua, não do script.")
    print("  • Rode o teste nas DUAS séries (total e >= limiar). Se elas divergirem,")
    print("    a divergência é subnotificação diferencial, que é confundidor, não ruído.")
    print(barra)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--fonte", choices=("auto", "arquivos", "pysus", "simulado"), default="auto"
    )
    parser.add_argument("--caminho", type=Path, nargs="*", default=[],
                        help="Arquivos SIM já baixados (.parquet/.csv/.csv.gz).")
    parser.add_argument("--nascimentos", type=Path, default=None,
                        help="Painel do script 02 (parquet). Sem ele a taxa não é calculada.")
    parser.add_argument("--anos", type=int, nargs="*", default=list(ANOS_PADRAO))
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    bruto, fonte = carrega_obitos(args.fonte, args.caminho, tuple(args.anos), args.seed)
    individual = prepara_obitos(bruto, args.anos)
    if individual.empty:
        print("[erro] Nada sobrou após filtrar TIPOBITO==1, Ceará e datas válidas.")
        print("       Confira TIPOBITO/CODMUNRES/DTOBITO na fonte.")
        return 1

    painel = colapsa_muni_mes(individual)

    tem_denominador = False
    if args.nascimentos is not None:
        try:
            painel = junta_denominador(painel, pd.read_parquet(args.nascimentos))
            tem_denominador = True
        except Exception as erro:  # noqa: BLE001
            print(f"[aviso] taxa não calculada ({type(erro).__name__}: {erro}).")

    painel["fonte"] = fonte  # a proveniência viaja junto com o dado
    imprime_resumo(individual, painel, fonte, tem_denominador)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    sufixo = "" if fonte != "simulado" else "__simulado"
    destino = args.out_dir / f"{NOME_SAIDA}{sufixo}.parquet"
    painel.to_parquet(destino, index=False)
    print(f"[ok] painel -> {destino}")
    print("[nota] data/processed/ é gitignored: microdado e derivados não vão para o repositório.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
