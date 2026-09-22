"""Testes das funções de limpeza dos scripts numerados de data_prep.

Os scripts começam com dígito (01_, 02_) e não são importáveis por `import`;
carregamos por caminho. Cada teste cobre uma decisão de limpeza que, se mudar
sem querer, muda o desfecho estimado — não é teste de trivialidade.

Rodar: pytest -q
"""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

RAIZ = Path(__file__).resolve().parents[1]


def _carrega(nome: str, sub: str = "data_prep"):
    caminho = RAIZ / "scripts" / sub / nome
    spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


dose = _carrega("01_check_dose_variation.py")
nasc = _carrega("02_clean_births.py")
fetal = _carrega("03_clean_fetal_deaths.py")
intox = _carrega("04_clean_poisoning.py")
painel = _carrega("05_build_panel.py", sub="build_panel")
robust = _carrega("04_robustness.py", sub="estimate")
gaez = _carrega("06_build_gaez.py")
gate = _carrega("14_gate_fronteira.py")


def _medias_e_painel(n_muni: int = 20, sd_ruido: float = 30.0, seed: int = 7):
    """Fixture compartilhada: dose de uma cultura + painel de nascimentos.

    Um município com dose alta (500 ha), nove com dose baixa, dez com zero.
    """
    medias = pd.DataFrame(
        {
            "cod_ibge": [f"239{i:03d}0" for i in range(n_muni)],
            "cod_ibge6": [f"239{i:03d}" for i in range(n_muni)],
            "cultura": ["Melão"] * n_muni,
            "area_ha_media": [500.0] + [10.0] * 9 + [0.0] * (n_muni - 10),
        }
    )
    rng = np.random.default_rng(seed)
    linhas = [
        {
            "cod_ibge6": cod,
            "ano": ano,
            "mes": 6,
            "n_nascimentos": 200,
            "peso_medio": 3200 + rng.normal(0, sd_ruido),
        }
        for cod in medias["cod_ibge6"]
        for ano in (2015, 2016, 2017, 2018)
    ]
    return medias, pd.DataFrame(linhas)


# --------------------------------------------------------------------------
# 01 — variação de dose
# --------------------------------------------------------------------------

def test_normaliza_tira_acento_e_asterisco_do_sidra():
    assert dose.normaliza("Abacaxi*") == "abacaxi"
    assert dose.normaliza("Algodão herbáceo (em caroço)") == "algodao herbaceo (em caroco)"


def test_filtra_candidatas_casa_rotulo_completo_do_pam():
    df = pd.DataFrame(
        {
            "cultura": ["Algodão herbáceo (em caroço)", "Melão", "Soja (em grão)"],
            "cod_ibge": ["2390011", "2390011", "2390011"],
            "ano": [2015, 2015, 2015],
            "area_ha": [10.0, 20.0, 30.0],
        }
    )
    saida = dose.filtra_candidatas(df)
    assert set(saida["cultura"]) == {"Algodão herbáceo (em caroço)", "Melão"}


def test_valor_sidra_traco_e_zero_mas_sigilo_e_ausente():
    serie = pd.Series(["-", "..", "...", "X", "123", "1,5"])
    saida = dose._valor_sidra_para_float(serie)
    assert saida.iloc[0] == 0.0          # "-" = zero absoluto
    assert saida.iloc[1:4].isna().all()  # ".." / "..." / "X" = ausente, não zero
    assert saida.iloc[4] == 123.0
    assert saida.iloc[5] == 1.5


def test_media_por_municipio_trata_ausencia_de_linha_como_zero():
    df = pd.DataFrame(
        {
            "cod_ibge": ["2390011", "2390011", "2390022"],
            "ano": [2015, 2016, 2015],
            "cultura": ["Melão", "Melão", "Banana (cacho)"],
            "area_ha": [100.0, 200.0, 50.0],
        }
    )
    medias = dose.media_por_municipio(df, anos=(2015, 2016))
    assert len(medias) == 4  # grade cheia: 2 municípios × 2 culturas
    melao_11 = medias.query("cod_ibge == '2390011' and cultura == 'Melão'")["area_ha_media"]
    assert melao_11.iloc[0] == pytest.approx(150.0)
    banana_11 = medias.query("cod_ibge == '2390011' and cultura == 'Banana (cacho)'")
    assert banana_11["area_ha_media"].iloc[0] == 0.0
    assert medias["cod_ibge6"].iloc[0] == "239001"  # chave de join com o SINASC


def test_dispersao_separa_cv_com_e_sem_zeros():
    medias = pd.DataFrame(
        {
            "cod_ibge": [f"239{i:03d}0" for i in range(10)],
            "cultura": ["Melão"] * 10,
            "area_ha_media": [100.0, 100.0] + [0.0] * 8,
        }
    )
    linha = dose.dispersao_por_cultura(medias).iloc[0]
    assert linha["n_muni_positivo"] == 2
    assert linha["cv_positivos"] == 0.0   # entre quem planta, não há dispersão
    assert linha["cv_todos"] > 1.0        # com zeros, dispersão é grande
    assert np.isnan(linha["p90_p10_positivos"])  # <10 positivos: percentil não diz nada


def test_escada_de_especificacao_cobre_os_tres_degraus():
    """A recomendação vem do suporte, não de limiar de área ou de concentração."""
    tabela = pd.DataFrame(
        {
            "cultura": ["espalhada", "media", "fina", "rala"],
            "n_muni_positivo": [60, 25, 13, 8],
            "n_dose_distintas": [60, 25, 13, 8],
            "n_muni_decil_superior": [6, 3, 2, 1],
        }
    )
    saida = dose.recomenda_especificacao(tabela)
    assert "curva não-paramétrica" in saida["especificacao"].iloc[0]
    assert "faixas discretas" in saida["especificacao"].iloc[1]
    assert "SUPORTE FINO" not in saida["especificacao"].iloc[1]
    # 12 a 14: faixas ainda saem, mas marcadas — refinamento do pesquisador
    assert "SUPORTE FINO" in saida["especificacao"].iloc[2]
    assert "binário" in saida["especificacao"].iloc[3]
    assert "curva abandonada" in saida["especificacao"].iloc[3]


def test_muitos_municipios_com_dose_empatada_nao_sustenta_a_curva():
    """O caso patológico que a contagem de municípios sozinha não pega.

    80 municípios positivos parecem suporte de sobra — mas se quase todos estão
    empilhados na mesma dose, o sieve não tem onde avaliar a curva.
    """
    tabela = pd.DataFrame(
        {
            "cultura": ["empatada"],
            "n_muni_positivo": [80],
            "n_dose_distintas": [4],
            "n_muni_decil_superior": [8],
        }
    )
    saida = dose.recomenda_especificacao(tabela)
    assert "faixas discretas" in saida["especificacao"].iloc[0]
    assert "valores distintos" in saida["motivo"].iloc[0]


def test_cauda_superior_vazia_derruba_a_curva():
    """Suporte no corpo da distribuição não substitui suporte no topo.

    É no topo que a hipótese de limiar põe o efeito; sem municípios lá, a
    inclinação que interessa não é estimável.
    """
    tabela = pd.DataFrame(
        {
            "cultura": ["sem topo"],
            "n_muni_positivo": [55],
            "n_dose_distintas": [55],
            "n_muni_decil_superior": [2],
        }
    )
    saida = dose.recomenda_especificacao(tabela)
    assert "faixas discretas" in saida["especificacao"].iloc[0]
    assert "decil superior" in saida["motivo"].iloc[0]


def test_colunas_de_suporte_medem_o_que_prometem():
    medias = pd.DataFrame(
        {
            "cod_ibge": [f"239{i:03d}0" for i in range(10)],
            "cultura": ["Melão"] * 10,
            # 4 positivos, dois deles empatados; o maior isolado no topo
            "area_ha_media": [100.0, 100.0, 250.0, 900.0] + [0.0] * 6,
        }
    )
    linha = dose.dispersao_por_cultura(medias).iloc[0]
    assert linha["n_muni_positivo"] == 4
    assert linha["n_muni_zero"] == 6
    assert linha["n_dose_distintas"] == 3        # o empate em 100 conta uma vez
    assert linha["n_muni_acima_mediana"] == 2    # 250 e 900 acima da mediana (175)
    assert linha["n_muni_decil_superior"] == 1   # só o 900
    assert 0.0 < linha["gini_dose"] < 1.0


def test_mde_agrupado_e_maior_que_o_ingenuo():
    """A conta que conta municípios tem que ser mais dura que a que conta bebês.

    É o argumento inteiro para Conley–Taber: se o agrupado saísse menor, a
    inferência com poucos clusters seria um detalhe, e não é.
    """
    medias, painel = _medias_e_painel()
    tabela = dose.recomenda_especificacao(dose.dispersao_por_cultura(medias))
    saida = dose.acrescenta_mde(tabela, medias, painel)
    ingenuo = saida["mde_ingenuo_g"].iloc[0]
    agrupado = saida["mde_agrupado_g"].iloc[0]
    assert ingenuo > 0 and agrupado > 0
    assert agrupado > ingenuo
    assert saida["n_nascimentos_dose_alta"].iloc[0] > 0
    assert saida["n_muni_dose_alta"].iloc[0] > 0


def test_meia_largura_do_ic_e_a_razao_dos_z_vezes_o_mde_agrupado():
    """A meia-largura sai de Z_IC/Z_PODER, nunca de um 0,70 hard-codado.

    Se alguém mexer no poder e a constante ficar para trás, esta conta acusa —
    é o ponto do docs/ars/07-*.md §Pergunta 2 virando código.
    """
    medias, painel = _medias_e_painel()
    tabela = dose.recomenda_especificacao(dose.dispersao_por_cultura(medias))
    saida = dose.acrescenta_mde(tabela, medias, painel)

    esperado = (dose.Z_IC / dose.Z_PODER) * saida["mde_agrupado_g"].iloc[0]
    assert saida["ic_meia_largura_g"].iloc[0] == pytest.approx(esperado)
    assert dose.Z_IC / dose.Z_PODER == pytest.approx(0.70, abs=0.01)


def test_falsifica_vira_quando_o_piso_cruza_a_meia_largura():
    """A coluna tem de responder ao piso — e o piso é do pesquisador.

    Com o piso logo ABAIXO da meia-largura, um nulo é ilegível (False); logo
    ACIMA, é legível (True). Se não virasse, a coluna estaria medindo outra
    coisa.
    """
    medias, painel = _medias_e_painel()
    tabela = dose.recomenda_especificacao(dose.dispersao_por_cultura(medias))
    base = dose.acrescenta_mde(tabela, medias, painel)
    meia = float(base["ic_meia_largura_g"].iloc[0])

    apertado = dose.acrescenta_mde(tabela, medias, painel, efeito_esperado_g=meia - 1)
    folgado = dose.acrescenta_mde(tabela, medias, painel, efeito_esperado_g=meia + 1)
    assert not bool(apertado["falsifica"].iloc[0])
    assert bool(folgado["falsifica"].iloc[0])
    assert folgado.attrs["efeito_esperado_g"] == pytest.approx(meia + 1)


def test_sem_mde_agrupado_o_veredito_e_ausente_e_nao_falso():
    """NaN propaga. False leria como 'não falsifica', que é afirmação — e sem
    DP das tendências não se sabe. Ausente é a única resposta honesta."""
    medias, painel = _medias_e_painel()
    painel = painel[painel["ano"] == 2015]  # sem segunda metade: DP indefinida
    tabela = dose.recomenda_especificacao(dose.dispersao_por_cultura(medias))
    saida = dose.acrescenta_mde(tabela, medias, painel)

    assert saida["mde_agrupado_g"].isna().all()
    assert saida["ic_meia_largura_g"].isna().all()
    assert saida["falsifica"].isna().all()


# --------------------------------------------------------------------------
# 02 — nascimentos
# --------------------------------------------------------------------------

def test_extrai_ano_mes_aguenta_zero_a_esquerda_perdido():
    serie = pd.Series(["01032017", "1032017", "31122019", "99999999", None])
    saida = nasc.extrai_ano_mes(serie)
    assert saida["ano"].iloc[0] == 2017 and saida["mes"].iloc[0] == 3
    assert saida["ano"].iloc[1] == 2017 and saida["mes"].iloc[1] == 3  # 7 chars
    assert saida["mes"].iloc[2] == 12
    assert pd.isna(saida["ano"].iloc[3]) and pd.isna(saida["ano"].iloc[4])


def test_limpa_peso_descarta_codigo_de_ausencia_e_implausivel():
    serie = pd.Series(["3200", "0000", "9999", "2499", ""])
    saida = nasc.limpa_peso(serie)
    assert saida.iloc[0] == 3200
    assert pd.isna(saida.iloc[1])  # "0000" = ignorado, não bebê de 0 g
    assert pd.isna(saida.iloc[2])  # acima de 8000 g
    assert saida.iloc[3] == 2499
    assert pd.isna(saida.iloc[4])


def test_limpa_semanas_descarta_99():
    saida = nasc.limpa_semanas(pd.Series([39, 99, 36, 12]))
    assert saida.iloc[0] == 39
    assert pd.isna(saida.iloc[1])
    assert saida.iloc[2] == 36
    assert pd.isna(saida.iloc[3])


def test_prematuridade_usa_gestacao_so_quando_semagestac_falta():
    semanas = pd.Series([36.0, 39.0, np.nan, np.nan, np.nan])
    gestacao = pd.Series([5, 1, 4, 5, 9])  # 1–4 = <37 sem; 5–6 = termo; 9 = ignorado
    saida = nasc.deriva_prematuridade(semanas, gestacao)
    # SEMAGESTAC manda quando existe, mesmo discordando da faixa
    assert saida["prematuro"].iloc[0] == 1.0
    assert saida["prematuro"].iloc[1] == 0.0
    assert saida["prematuro_por_faixa"].iloc[0] == 0.0
    # fallback entra só nas ausentes
    assert saida["prematuro"].iloc[2] == 1.0
    assert saida["prematuro"].iloc[3] == 0.0
    assert saida["prematuro_por_faixa"].iloc[2] == 1.0
    # categoria 9 (ignorado) não vira zero
    assert pd.isna(saida["prematuro"].iloc[4])


def test_filtra_ceara_mantem_so_uf_23():
    df = pd.DataFrame({"CODMUNRES": ["230440", "230000", "355030", "239001", "292740"]})
    saida = nasc.filtra_ceara(nasc.padroniza_colunas(df))
    assert list(saida["cod_ibge6"]) == ["230440", "239001"]


def test_padroniza_colunas_aceita_saida_datazoom_sinasc():
    bruto = pd.DataFrame({
        "codmunres": ["230440"],
        "data_nascimento_recemnascido": ["2017-03-01"],
        "peso": [3200],
        "semanas_gestacao": [39],
        "gestacao": [5],
        "idade_mae": [25],
        "escolaridade_mae": [4],
        "consultas_prenatal_agrupadas": [4],
    })
    saida = nasc.prepara_nascimentos(bruto)
    assert saida.iloc[0]["ano"] == 2017
    assert saida.iloc[0]["mes"] == 3
    assert saida.iloc[0]["IDADEMAE"] == 25


def test_colapso_calcula_taxa_sobre_o_denominador_observado():
    bruto = pd.DataFrame(
        {
            "CODMUNRES": ["230440"] * 4,
            "DTNASC": ["01032017", "15032017", "20032017", "02042017"],
            "PESO": ["2400", "3300", "0000", "3100"],  # um peso ignorado
            "SEMAGESTAC": [35, 39, 40, 99],
            "GESTACAO": [4, 5, 5, 9],
            "IDADEMAE": [25, 30, 22, 28],
            "ESCMAE": [3, 4, 3, 4],
            "CONSULTAS": [4, 4, 3, 4],
        }
    )
    painel = nasc.colapsa_muni_mes(nasc.prepara_nascimentos(bruto))
    marco = painel.query("mes == 3").iloc[0]
    assert marco["n_nascimentos"] == 3
    assert marco["n_peso_valido"] == 2          # o "0000" não entra
    assert marco["taxa_baixo_peso"] == pytest.approx(0.5)   # 1 de 2 observados
    assert marco["peso_medio"] == pytest.approx(2850.0)
    assert marco["taxa_prematuridade"] == pytest.approx(1 / 3)
    abril = painel.query("mes == 4").iloc[0]
    assert abril["n_gest_valido"] == 0          # SEMAGESTAC 99 + GESTACAO 9
    assert pd.isna(abril["taxa_prematuridade"])
    assert bool(abril["celula_pequena"]) is True


def test_simulacao_bate_os_alvos_do_enunciado():
    """~9% baixo peso, ~11% prematuridade — a fixture precisa valer como fixture."""
    bruto = nasc.simula_sinasc(anos=(2018,), seed=1, n_por_muni_mes=12)
    individual = nasc.prepara_nascimentos(bruto)
    assert individual["baixo_peso"].mean() == pytest.approx(0.09, abs=0.015)
    assert individual["prematuro"].mean() == pytest.approx(0.11, abs=0.015)
    assert individual["cod_ibge6"].str.startswith("23").all()  # filtro de UF pegou tudo


# --------------------------------------------------------------------------
# 03 — óbito fetal (SIM)
# --------------------------------------------------------------------------

def _do_bruto(**over) -> pd.DataFrame:
    """DO com uma linha fetal e uma não fetal, ambas no Ceará."""
    base = {
        "TIPOBITO": [1, 2],
        "DTOBITO": ["15032017", "15032017"],
        "CODMUNRES": ["230440", "230440"],
        "PESO": ["1200", "3100"],
        "SEMAGESTAC": [30, 39],
        "GESTACAO": [3, 5],
        "OBITOPARTO": [1, 3],
        "IDADEMAE": [28, 31],
    }
    base.update(over)
    return pd.DataFrame(base)


def test_tipobito_nao_fetal_e_descartado():
    """O filtro que define a série. Deixar TIPOBITO==2 entrar misturaria óbito
    infantil com óbito fetal — populações e desfechos diferentes."""
    individual = fetal.prepara_obitos(_do_bruto())
    assert len(individual) == 1
    assert pd.to_numeric(individual["TIPOBITO"]).iloc[0] == fetal.TIPOBITO_FETAL

    # TIPOBITO ausente também sai: é campo obrigatório na DO, NaN é erro de leitura
    assert fetal.prepara_obitos(_do_bruto(TIPOBITO=[np.nan, 2])).empty


def test_limiar_de_notificacao_e_OU_e_nao_E():
    """≥ 22 semanas OU ≥ 500 g. Tratar como 'e' descartaria registro válido.

    Linha 1: 20 semanas, 520 g -> entra pelo peso.
    Linha 2: 23 semanas, 400 g -> entra pelas semanas.
    Linha 3: 20 semanas, 300 g -> fica de fora.
    Linha 4: nada conhecido    -> AUSENTE, não 'fora'.
    """
    saida = fetal.deriva_acima_limiar(
        pd.Series([20.0, 23.0, 20.0, np.nan]),
        pd.Series([np.nan, np.nan, np.nan, 9]),
        pd.Series([520.0, 400.0, 300.0, np.nan]),
    )
    assert saida["acima_limiar"].tolist()[:3] == [1.0, 1.0, 0.0]
    assert pd.isna(saida["acima_limiar"].iloc[3])


def test_limiar_usa_gestacao_so_quando_semagestac_falta():
    """Fallback categórico, como no script 02 — e marcado, para que um salto de
    cobertura em torno de 2019 apareça como ameaça de mensuração."""
    saida = fetal.deriva_acima_limiar(
        pd.Series([np.nan, 30.0]),
        pd.Series([2, 1]),          # 2 = 22–27 sem (acima); 1 = <22 (abaixo)
        pd.Series([np.nan, np.nan]),
    )
    assert saida["acima_limiar"].tolist() == [1.0, 1.0]   # a 2ª vem de SEMAGESTAC
    assert saida["limiar_por_faixa"].tolist() == [1.0, 0.0]


def test_serie_restrita_nunca_excede_o_total():
    """n_obito_fetal_22sem <= n_obito_fetal, sempre. A restrita é subconjunto."""
    bruto = fetal.simula_sim(anos=(2018,), seed=3, n_por_muni_mes=12)
    painel = fetal.colapsa_muni_mes(fetal.prepara_obitos(bruto))
    assert (painel["n_obito_fetal_22sem"] <= painel["n_obito_fetal"]).all()
    assert (painel["n_limiar_valido"] <= painel["n_obito_fetal"]).all()
    assert painel["n_obito_fetal_22sem"].sum() > 0   # a fixture tem o que contar


def test_denominador_inclui_os_obitos_fetais():
    """Dividir só por nascidos vivos poria a própria seleção no denominador.

    2 óbitos fetais e 98 nascidos vivos dão taxa de 2/100, não 2/98.
    """
    painel_fetal = pd.DataFrame(
        {
            "cod_ibge6": ["230440"], "ano": [2017], "mes": [3],
            "n_obito_fetal": [2], "n_obito_fetal_22sem": [2], "n_limiar_valido": [2],
            "n_peso_valido": [2], "peso_medio_fetal": [1200.0],
            "n_gest_valido": [2], "semanas_media": [30.0],
            "share_gest_por_faixa": [0.0], "idade_mae_media": [28.0],
            "celula_pequena": [True],
        }
    )
    painel_nasc = pd.DataFrame(
        {"cod_ibge6": ["230440"], "ano": [2017], "mes": [3], "n_nascimentos": [98]}
    )
    junto = fetal.junta_denominador(painel_fetal, painel_nasc)
    assert junto["coorte_registrada"].iloc[0] == 100
    assert junto["taxa_obito_fetal"].iloc[0] == pytest.approx(0.02)
    assert junto["taxa_obito_fetal"].iloc[0] != pytest.approx(2 / 98)


def test_juncao_preserva_toda_a_chave_do_painel_de_nascimentos():
    """Município-mês com nascimento e sem óbito fetal é taxa ZERO, não ausência.

    Uma junção interna o perderia — e perder as células de taxa zero enviesaria
    o teste de seleção exatamente onde ele precisa de contraste.
    """
    bruto_nasc = nasc.simula_sinasc(anos=(2018,), seed=5, n_por_muni_mes=10)
    painel_nasc = nasc.colapsa_muni_mes(nasc.prepara_nascimentos(bruto_nasc))
    bruto_fetal = fetal.simula_sim(anos=(2018,), seed=5, n_por_muni_mes=10)
    painel_fetal = fetal.colapsa_muni_mes(fetal.prepara_obitos(bruto_fetal))

    junto = fetal.junta_denominador(painel_fetal, painel_nasc)
    chave = ["cod_ibge6", "ano", "mes"]
    assert painel_nasc.set_index(chave).index.isin(junto.set_index(chave).index).all()
    assert len(junto) >= len(painel_nasc)
    # células só de nascimento sobrevivem com contagem zero, não NaN
    so_nasc = junto[junto["n_obito_fetal"] == 0]
    assert len(so_nasc) > 0
    assert (so_nasc["taxa_obito_fetal"] == 0).all()


# --------------------------------------------------------------------------
# 01 — aquisição SIDRA: preflight de metadados e diagnóstico de rede
# --------------------------------------------------------------------------

# Resposta de metadados no formato da API v3 do servicodados. ⚠️ Gravada a
# partir da documentação, NÃO de uma chamada real — a rede estava fechada
# quando isto foi escrito. Serve para travar o parser, não para provar que os
# códigos estão certos; quem prova isso é `--verificar-codigos` com rede.
_METADADOS_1612 = {
    "id": "1612",
    "nome": "Área plantada, área colhida, quantidade produzida...",
    "variaveis": [
        {"id": 109, "nome": "Área plantada", "unidade": "Hectares"},
        {"id": 216, "nome": "Área colhida", "unidade": "Hectares"},
    ],
    "classificacoes": [
        {"id": 81, "nome": "Produto das lavouras temporárias", "categorias": []},
    ],
}


def test_extrai_codigos_normaliza_id_para_texto():
    """O SIDRA aceita id como texto e o script os guarda como texto. Comparar
    int com str daria 'código não existe' para um código que existe."""
    variaveis = dose._extrai_codigos(_METADADOS_1612, "variaveis")
    assert variaveis == {"109": "Área plantada", "216": "Área colhida"}
    assert dose._extrai_codigos(_METADADOS_1612, "classificacoes") == {
        "81": "Produto das lavouras temporárias"
    }
    # chave ausente ou formato inesperado não estoura: devolve vazio
    assert dose._extrai_codigos({}, "variaveis") == {}
    assert dose._extrai_codigos({"variaveis": "nao é lista"}, "variaveis") == {}


def test_preflight_aprova_codigo_existente_e_reprova_inventado(monkeypatch):
    """O preflight é o que impede a queda silenciosa: código errado devolve
    VAZIO no SIDRA, não erro, e vazio virava 'simulado' sem ninguém notar."""
    monkeypatch.setattr(dose, "busca_metadados_sidra", lambda t, timeout=30: _METADADOS_1612)

    bom = [{"tabela": "1612", "variavel": "109", "classificacao": "81", "grupo": "t"}]
    assert dose.imprime_verificacao(dose.verifica_codigos_sidra(bom)) is True

    ruim = [{"tabela": "1612", "variavel": "999", "classificacao": "81", "grupo": "t"}]
    relatorio = dose.verifica_codigos_sidra(ruim)
    assert not relatorio["variavel_ok"].iloc[0]
    assert relatorio["classificacao_ok"].iloc[0]
    assert dose.imprime_verificacao(relatorio) is False
    # e o relatório carrega o que EXISTE, para a correção não virar adivinhação
    assert "109" in relatorio["variaveis_disponiveis"].iloc[0]


def test_403_do_proxy_e_bloqueio_de_rede_e_nao_erro_do_ibge():
    """As duas causas pedem ações diferentes: liberar domínio contra mexer na
    consulta. Confundi-las custou tempo numa sessão anterior."""
    proxy = OSError("Tunnel connection failed: 403 Forbidden")
    assert dose._diagnostica_erro_rede(proxy) is not None
    assert "POLÍTICA DE REDE" in dose._diagnostica_erro_rede(proxy)
    assert "apisidra.ibge.gov.br" in dose._diagnostica_erro_rede(proxy)

    # erro do lado do IBGE não pode ser reclassificado como bloqueio
    assert dose._diagnostica_erro_rede(ValueError("500 Server Error")) is None
    assert dose._diagnostica_erro_rede(KeyError("variavel")) is None


def test_bloqueio_de_rede_nao_vira_simulado_calado(monkeypatch, capsys):
    """Em --fonte auto o fallback é legítimo, mas tem de anunciar QUAL motivo."""
    def falha(*a, **k):
        raise dose.BloqueioDeRede(dose._diagnostica_erro_rede(
            OSError("Tunnel connection failed: 403 Forbidden")
        ))

    monkeypatch.setattr(dose, "carrega_pam_sidra", falha)
    _, fonte = dose.carrega_pam("auto", anos=(2015, 2016), seed=1)
    saida = capsys.readouterr().out
    assert fonte == "simulado"
    assert "NÃO é o IBGE" in saida
    assert "SIMULADOS" in saida


def _cabecalho_sidra(**extra) -> dict:
    """Cabeçalho como o SIDRA devolve: par (código, nome) por dimensão, código
    PRIMEIRO. Vale para os dois transportes — o `/values` do apisidra usa a mesma
    convenção do sidrapy, e é por isso que os dois compartilham o parser."""
    base = {
        "D1C": "Município (Código)", "D1N": "Município",
        "D2C": "Ano (Código)", "D2N": "Ano",
        "D4C": "Produto das lavouras temporárias (Código)",
        "D4N": "Produto das lavouras temporárias",
        "V": "Valor",
    }
    base.update(extra)
    return base


def test_parser_pega_o_NOME_da_cultura_e_nao_o_codigo():
    """O bug que abortaria a primeira rodada real do Gate 1.

    Casar "produto" e parar no primeiro resultado pega D4C (código) porque o
    SIDRA devolve o código antes do nome. Aí `cultura` vira "40099",
    `filtra_candidatas` não casa nada, e o script morre em "Nenhuma cultura
    candidata casou com os rótulos do PAM" — sem indicar que a causa é o parser.
    """
    bruto = pd.DataFrame([
        _cabecalho_sidra(),
        {"D1C": "2307304", "D1N": "Limoeiro do Norte", "D2C": "2015", "D2N": "2015",
         "D4C": "40099", "D4N": "Melão", "V": "1200"},
    ])
    longo = dose._sidra_para_longo(bruto, "temporária")

    assert longo["cultura"].iloc[0] == "Melão"       # o nome, não "40099"
    assert longo["cod_ibge"].iloc[0] == "2307304"    # aqui o CÓDIGO é o certo
    assert longo["ano"].iloc[0] == 2015
    assert longo["area_ha"].iloc[0] == pytest.approx(1200.0)
    # e o resultado sobrevive ao filtro de culturas, que é o ponto
    assert not dose.filtra_candidatas(longo).empty


def test_parser_serve_aos_dois_transportes():
    """`_pam_via_rest` passa a resposta do apisidra direto para o mesmo parser.
    Nenhum teste cobria esse caminho — uma correção pensada só para a forma do
    sidrapy passaria verde e quebraria o fallback em silêncio."""
    linhas = [
        _cabecalho_sidra(),
        {"D1C": "2307304", "D1N": "Limoeiro do Norte", "D2C": "2016", "D2N": "2016",
         "D4C": "40099", "D4N": "Melão", "V": "800"},
    ]
    via_rest = dose._sidra_para_longo(pd.DataFrame(linhas), "temporária")     # lista de dicts
    via_pacote = dose._sidra_para_longo(pd.DataFrame(linhas), "temporária")   # DataFrame
    assert via_rest["cultura"].iloc[0] == via_pacote["cultura"].iloc[0] == "Melão"


def test_rotulo_ausente_falha_dizendo_o_que_viu():
    """Este script existe para falhar alto. Se só vier a coluna de código, o erro
    tem de nomear o que faltou e listar os rótulos — não um StopIteration mudo."""
    so_codigo = pd.DataFrame([
        {k: v for k, v in _cabecalho_sidra().items() if k != "D4N"},
        {"D1C": "2307304", "D1N": "Limoeiro do Norte", "D2C": "2015", "D2N": "2015",
         "D4C": "40099", "V": "1200"},
    ])
    with pytest.raises(KeyError) as erro:
        dose._sidra_para_longo(so_codigo, "temporária")
    mensagem = str(erro.value)
    assert "excluindo colunas de código" in mensagem   # diz o que foi descartado
    assert "Produto das lavouras" in mensagem   # e lista os rótulos que viu


# --------------------------------------------------------------------------
# 01 — o caminho manual (--fonte arquivo), a saída de emergência sem rede
# --------------------------------------------------------------------------

_CABECALHO_CSV = (
    '"Município (Código)","Município","Ano (Código)","Ano",'
    '"Produto das lavouras temporárias (Código)","Produto das lavouras temporárias","Valor"\n'
)
_LINHA_CSV = '"2307304","Limoeiro do Norte","2015","2015","40099","Melão","1200"\n'


def test_arquivo_do_portal_com_preambulo_e_lido(tmp_path):
    """O caso que quebrava, e que é o formato mais provável de entrada.

    O export do portal do SIDRA traz título, variável e linha em branco antes do
    cabeçalho. Lendo com `header=0` isso estourava num ParserError do pandas
    ("Expected 1 fields in line 4, saw 7") — mensagem que não diz nada sobre
    preâmbulo, no caminho que o pesquisador usa justamente quando a rede falhou.
    """
    arq = tmp_path / "tabela1612.csv"
    arq.write_text(
        '"Tabela 1612 - Área plantada, área colhida, quantidade produzida"\n'
        '"Variável - Área plantada (Hectares)"\n'
        '""\n' + _CABECALHO_CSV + _LINHA_CSV,
        encoding="utf-8",
    )
    saida = dose.carrega_pam_arquivo([arq])
    assert len(saida) == 1
    assert saida["cultura"].iloc[0] == "Melão"        # nome, não "40099"
    assert saida["cod_ibge"].iloc[0] == "2307304"
    assert saida["ano"].iloc[0] == 2015
    assert saida["area_ha"].iloc[0] == pytest.approx(1200.0)


def test_arquivo_no_formato_sidrapy_continua_funcionando(tmp_path):
    """Sem preâmbulo, rótulos na linha 0 — a convenção do pacote. A detecção não
    pode quebrar o caso que já funcionava."""
    arq = tmp_path / "1612.csv"
    arq.write_text(_CABECALHO_CSV + _LINHA_CSV, encoding="utf-8")
    assert dose.carrega_pam_arquivo([arq])["cultura"].iloc[0] == "Melão"


def test_grupo_sai_do_nome_do_arquivo(tmp_path):
    """1612 = temporária, 1613 = permanente. Não vem no arquivo; é inferido."""
    def grava(nome):
        arq = tmp_path / nome
        arq.write_text(_CABECALHO_CSV + _LINHA_CSV, encoding="utf-8")
        return dose.carrega_pam_arquivo([arq])["grupo"].iloc[0]

    assert grava("tabela1612.csv") == "temporária"
    assert grava("export_1613_ce.csv") == "permanente"
    assert grava("sem_numero.csv") == "desconhecido"


def test_arquivo_sem_cabecalho_nomeia_o_preambulo_como_causa(tmp_path):
    """Falhar alto é o princípio do script; falhar alto DIZENDO A CAUSA é o
    ponto. 'Expected 1 fields in line 4' não ajuda ninguém."""
    arq = tmp_path / "1612.csv"
    arq.write_text("lixo\noutra coisa qualquer\n", encoding="utf-8")
    with pytest.raises(ValueError) as erro:
        dose.carrega_pam_arquivo([arq])
    mensagem = str(erro.value)
    assert "preâmbulo" in mensagem                 # nomeia a causa provável
    assert "Município" in mensagem                 # e o que procurava
    assert "lixo" in mensagem                      # e o que viu


def test_caminho_vazio_e_extensao_ruim_falham_claro(tmp_path):
    with pytest.raises(ValueError, match="--caminho"):
        dose.carrega_pam_arquivo([])
    pdf = tmp_path / "1612.pdf"
    pdf.write_bytes(b"%PDF-1.4")
    with pytest.raises(ValueError, match="Extensão não suportada"):
        dose.carrega_pam_arquivo([pdf])


# --------------------------------------------------------------------------
# 02/03 — portabilidade de fonte: datas e recombinação de painéis
# --------------------------------------------------------------------------

@pytest.mark.parametrize("modulo", ["nasc", "fetal"], ids=["sinasc", "sim"])
@pytest.mark.parametrize(
    "texto,ano,mes",
    [
        ("15032017", 2017, 3),     # DATASUS: DDMMAAAA
        ("1032017", 2017, 3),      # DATASUS com zero à esquerda perdido
        ("2017-03-01", 2017, 3),   # ISO: datazoom / BigQuery
        ("01/02/2017", 2017, 2),   # barra brasileira: dia 1 de FEVEREIRO
        ("31/12/2019", 2019, 12),
    ],
)
def test_data_nao_troca_dia_por_mes_em_nenhuma_fonte(modulo, texto, ano, mes):
    """`format="mixed"` lia "01/02/2017" como JANEIRO — mês errado no painel.

    Num desenho mensal cujo tratamento entra em 09/01/2019, mês trocado é
    contaminação silenciosa da janela do evento. E `dayfirst=True` não é a
    correção: conserta a barra e quebra o ISO. Por isso a lista de formatos é
    fechada, tentada em ordem, sem inferência nenhuma.
    """
    m = {"nasc": nasc, "fetal": fetal}[modulo]
    saida = m.extrai_ano_mes(pd.Series([texto]))
    assert saida["ano"].iloc[0] == ano
    assert saida["mes"].iloc[0] == mes


def test_data_ilegivel_vira_ausente_e_nao_data_errada():
    """Melhor perder a linha (o pipeline conta e descarta) que gravar mês errado."""
    saida = nasc.extrai_ano_mes(pd.Series(["99999999", "não é data", None]))
    assert saida["ano"].isna().all()


def test_alias_datazoom_nao_confunde_idade_do_falecido_com_a_da_mae():
    """Na DO do SIM, IDADE é a idade do FALECIDO em código composto (401 = 1
    ano), não a da mãe — que já tem campo próprio, IDADEMAE. O alias punha 401
    dentro de `idade_mae_media`."""
    bruto = pd.DataFrame({
        "TIPOBITO": [1], "DTOBITO": ["15032017"], "CODMUNRES": ["230440"],
        "PESO": ["1200"], "SEMAGESTAC": [30], "GESTACAO": [3],
        "OBITOPARTO": [1], "IDADE": [401],
    })
    saida = fetal.padroniza_colunas(bruto)
    assert pd.isna(saida["IDADEMAE"].iloc[0])   # ausente, não 401


def test_recombina_soma_celula_que_aparece_em_dois_arquivos():
    """Registro tardio: um nascimento de dez/2015 pode vir no arquivo de 2016.

    Colapsando arquivo a arquivo e concatenando, a mesma célula sai em DUAS
    linhas — o painel perde a chave única, uma junção em build_panel
    multiplicaria linhas, e média de médias sem peso daria o desfecho errado.
    """
    def um(dia, peso):
        bruto = pd.DataFrame({"CODMUNRES": ["230440"], "DTNASC": [dia],
                              "PESO": [peso], "SEMAGESTAC": [39], "GESTACAO": [5]})
        return nasc.colapsa_muni_mes(nasc.prepara_nascimentos(bruto))

    recombinado = nasc.recombina_paineis([um("15122015", "3000"), um("20122015", "3400")])
    juntos = nasc.colapsa_muni_mes(nasc.prepara_nascimentos(pd.DataFrame({
        "CODMUNRES": ["230440", "230440"], "DTNASC": ["15122015", "20122015"],
        "PESO": ["3000", "3400"], "SEMAGESTAC": [39, 39], "GESTACAO": [5, 5],
    })))

    assert len(recombinado) == 1                                  # chave única
    assert recombinado["n_nascimentos"].iloc[0] == 2
    # e bate com o colapso feito de uma vez só — média PONDERADA, não de médias
    assert recombinado["peso_medio"].iloc[0] == pytest.approx(juntos["peso_medio"].iloc[0])
    assert recombinado["peso_medio"].iloc[0] == pytest.approx(3200.0)


def test_recombina_pondera_pelo_denominador_certo():
    """Célula grande e célula pequena não podem entrar com peso igual."""
    def celula(n, peso):
        bruto = pd.DataFrame({"CODMUNRES": ["230440"] * n, "DTNASC": ["15122015"] * n,
                              "PESO": [peso] * n, "SEMAGESTAC": [39] * n, "GESTACAO": [5] * n})
        return nasc.colapsa_muni_mes(nasc.prepara_nascimentos(bruto))

    saida = nasc.recombina_paineis([celula(9, "3000"), celula(1, "4000")])
    assert saida["n_nascimentos"].iloc[0] == 10
    assert saida["peso_medio"].iloc[0] == pytest.approx(3100.0)   # não 3500


# --------------------------------------------------------------------------
# 02/03 — aliases do datazoom.saude, conferidos contra R/dictionary.R
# --------------------------------------------------------------------------

def test_datazoom_sinasc_em_ingles_o_padrao_do_pacote():
    """⚠️ O `language` do datazoom.saude tem PADRÃO "eng", não "pt".

    Cobrindo só o português, a rodada padrão do pacote não casa nenhuma coluna:
    tudo vira NaN, toda linha é descartada por data inválida, e o script morre em
    "Nada sobrou após filtrar Ceará" — apontando para a causa errada.
    """
    bruto = pd.DataFrame({
        "codmunres": ["230440"],
        "newborn_birth_date": ["2017-03-01"],
        "weight": [3200],
        "gestational_weeks": [39],
        "grouped_gestational_weeks": [5],
        "mother_age": [25],
    })
    saida = nasc.prepara_nascimentos(bruto)
    assert len(saida) == 1
    assert saida.iloc[0]["ano"] == 2017 and saida.iloc[0]["mes"] == 3
    assert saida.iloc[0]["peso_g"] == 3200          # WEIGHT -> PESO
    assert saida.iloc[0]["semanas"] == 39
    assert saida.iloc[0]["IDADEMAE"] == 25


def test_datazoom_sinasc_gestacao_agrupada_alimenta_o_fallback():
    """`GESTACAO` vem de `semanas_gestacao_agrupado`, que nenhum alias cobria.

    É o fallback da prematuridade quando SEMAGESTAC falta. Sem o alias, a coluna
    ficava NaN e o fallback morria em silêncio — a taxa saía só de quem tinha
    semana exata, sem nada indicando a perda.
    """
    bruto = pd.DataFrame({
        "codmunres": ["230440"],
        "data_nascimento_recemnascido": ["01/03/2017"],
        "peso": [3200],
        "semanas_gestacao": [99],                 # ignorado -> força o fallback
        "semanas_gestacao_agrupado": [4],         # faixa 32–36 = prematuro
    })
    saida = nasc.prepara_nascimentos(bruto)
    assert bool(saida.iloc[0]["prematuro"]) is True
    assert saida.iloc[0]["prematuro_por_faixa"] == 1.0   # veio do fallback


def test_semanas_gestacao_e_agrupado_nao_se_confundem():
    """Campos DIFERENTES com nomes vizinhos: contagem contra faixa categórica.
    Trocá-los inverteria desfecho com fallback."""
    assert nasc.ALIASES_DATAZOOM["SEMANAS_GESTACAO"] == "SEMAGESTAC"
    assert nasc.ALIASES_DATAZOOM["SEMANAS_GESTACAO_AGRUPADO"] == "GESTACAO"


@pytest.mark.parametrize(
    "colunas",
    [
        {"peso_nascimento": "1200", "duracao_gestacao": 3},        # pt
        {"birth_weight": "1200", "gestational_duration": 3},       # eng (padrão)
    ],
    ids=["pt", "eng"],
)
def test_datazoom_sim_traz_peso_e_gestacao_com_outros_nomes(colunas):
    """No SIM o pacote renomeia PESO e GESTACAO — nenhum dos dois era coberto.

    São exatamente os campos de que o limiar de notificação depende (≥22 semanas
    OU ≥500 g). Sem eles, `acima_limiar` fica ausente e `n_obito_fetal_22sem`
    sai zero para tudo: o diagnóstico de subnotificação devolveria zeros sem
    nada indicando que a causa é coluna faltando.
    """
    bruto = pd.DataFrame({
        "tipobito": [1], "dtobito": ["15032017"], "codmunres": ["230440"],
        "obitoparto": [1], "idademae": [28], **{k: [v] for k, v in colunas.items()},
    })
    individual = fetal.prepara_obitos(bruto)
    assert len(individual) == 1
    assert individual.iloc[0]["peso_g"] == 1200
    assert individual.iloc[0]["acima_limiar"] == 1.0   # 28–31 sem e 1200 g
    painel = fetal.colapsa_muni_mes(individual)
    assert painel["n_obito_fetal_22sem"].iloc[0] == 1


def test_idade_do_falecido_continua_fora_de_idademae():
    """No dicionário do SIM, `idade` e `idademae` são campos separados."""
    assert "IDADE" not in fetal.ALIASES_DATAZOOM


def test_dofet_sem_tipobito_nao_zera_a_serie(capsys):
    """⚠️ Zero silencioso é o pior desfecho possível aqui.

    O SIM entrega óbito fetal de duas formas: dentro do DO geral (com TIPOBITO
    separando) ou num DOFET dedicado, que `datazoom.saude` expõe como
    `load_mortality(dataset = "fetal")` e que não precisa trazer TIPOBITO. Sem
    detecção, o filtro descartava tudo — e um painel vazio de óbito fetal
    *parece* o resultado benigno do teste de seleção ("não se move com a dose").
    """
    dofet = pd.DataFrame({
        "dtobito": ["15032017"], "codmunres": ["230440"],
        "peso_nascimento": ["1200"], "duracao_gestacao": [3], "idademae": [28],
    })
    saida = fetal.prepara_obitos(dofet)
    assert len(saida) == 1
    # e a decisão é ANUNCIADA, nunca tomada em silêncio
    assert "DOFET" in capsys.readouterr().out


def test_do_geral_continua_exigindo_o_filtro_tipobito():
    """A detecção não pode afrouxar o filtro quando TIPOBITO existe."""
    do_geral = pd.DataFrame({
        "TIPOBITO": [1, 2], "DTOBITO": ["15032017", "15032017"],
        "CODMUNRES": ["230440", "230440"], "PESO": ["1200", "3100"],
        "SEMAGESTAC": [30, 39], "GESTACAO": [3, 5], "OBITOPARTO": [1, 3],
        "IDADEMAE": [28, 31],
    })
    assert len(fetal.prepara_obitos(do_geral)) == 1          # só o fetal
    assert len(fetal.prepara_obitos(do_geral, ja_fetal=False)) == 1


def test_ja_fetal_forcado_nao_engole_do_geral_por_engano():
    """`--ja-fetal` num DO geral é erro do usuário, e o resultado tem de mostrar
    isso: os não fetais entram, e a contagem denuncia."""
    do_geral = pd.DataFrame({
        "TIPOBITO": [1, 2], "DTOBITO": ["15032017", "15032017"],
        "CODMUNRES": ["230440", "230440"], "PESO": ["1200", "3100"],
        "SEMAGESTAC": [30, 39], "GESTACAO": [3, 5], "OBITOPARTO": [1, 3],
        "IDADEMAE": [28, 31],
    })
    assert len(fetal.prepara_obitos(do_geral, ja_fetal=True)) == 2


# --------------------------------------------------------------------------
# 04 — intoxicação por agrotóxico (SIH), o canal de substituição
# --------------------------------------------------------------------------

def _aih(principal, secundario="", muni="230440", data="20170315", idade=30, morte=0):
    return {"DIAG_PRINC": principal, "DIAG_SECUN": secundario, "MUNIC_RES": muni,
            "DT_INTER": data, "MORTE": morte, "IDADE": idade, "SEXO": 1}


def test_familias_de_intencao_nunca_sao_somadas():
    """A separação É o desenho, não organização.

    X48 (acidental) responde a COMO se aplica — o canal de substituição. X68
    (autoprovocada) responde à DISPONIBILIDADE da molécula, que o ban não muda,
    e por isso serve de placebo. Somar as duas mistura mecanismos e destrói o
    placebo que vem de graça dentro do mesmo dado.
    """
    bruto = pd.DataFrame([_aih("X48"), _aih("X68"), _aih("X68"), _aih("Y18")])
    painel = intox.colapsa_muni_mes(intox.prepara_internacoes(bruto))
    linha = painel.iloc[0]
    assert linha["n_acidental"] == 1
    assert linha["n_autoprovocada"] == 2
    assert linha["n_indeterminada"] == 1
    # não existe coluna que some as intenções
    assert "n_intoxicacao_total" not in painel.columns


def test_cid_casa_com_e_sem_ponto():
    """O SIH grava sem ponto ('T600'); a documentação usa 'T60.0'."""
    bruto = pd.DataFrame([_aih("T60.0"), _aih("t600"), _aih("T603")])
    painel = intox.colapsa_muni_mes(intox.prepara_internacoes(bruto))
    assert painel["n_t60_organofosforado_carbamato"].iloc[0] == 2
    assert painel["n_t60_herbicida_fungicida"].iloc[0] == 1


def test_diagnostico_secundario_conta_mas_fica_marcado():
    """SIH é faturamento: a escolha entre principal e secundário responde a
    incentivo de pagamento, não só a clínica. Ignorar o secundário perde casos;
    fundir os dois esconde o que a contagem significa."""
    bruto = pd.DataFrame([_aih("T600", "X48"), _aih("X48", "T600")])
    painel = intox.colapsa_muni_mes(intox.prepara_internacoes(bruto))
    assert painel["n_acidental"].iloc[0] == 2             # os dois casam
    assert painel["n_acidental_principal"].iloc[0] == 1   # só um no principal


def test_internacao_sem_cid_de_agrotoxico_e_descartada():
    """O SIH inteiro entra; só o que casa família fica."""
    bruto = pd.DataFrame([_aih("J189"), _aih("I219"), _aih("X48")])
    assert len(intox.prepara_internacoes(bruto)) == 1


def test_data_do_sih_e_AAAAMMDD_e_nao_DDMMAAAA():
    """⚠️ Formato DIFERENTE do SINASC. '20170315' é 15/03/2017; lido como
    DDMMAAAA daria lixo, e num painel mensal mês errado é contaminação da
    janela do evento."""
    bruto = pd.DataFrame([_aih("X48", data="20170315")])
    saida = intox.prepara_internacoes(bruto)
    assert saida.iloc[0]["ano"] == 2017 and saida.iloc[0]["mes"] == 3


def test_codigo_ibge_de_7_digitos_vira_a_chave_de_6():
    """O SIH tem os dois: munic_res com 6 e codibge com 7. Sem truncar, a
    junção com os painéis dos scripts 02 e 03 não acontece."""
    bruto = pd.DataFrame([_aih("X48", muni="2304400"), _aih("X48", muni="230440")])
    saida = intox.prepara_internacoes(bruto)
    assert list(saida["cod_ibge6"].unique()) == ["230440"]


def test_chave_casa_com_os_paineis_dos_scripts_02_e_03():
    """Sem chave idêntica não há canal: o teste roda contra a mesma dose."""
    b_intox = intox.simula_sih(anos=(2018,), seed=4)
    p_intox = intox.colapsa_muni_mes(intox.prepara_internacoes(b_intox))
    p_nasc = nasc.colapsa_muni_mes(
        nasc.prepara_nascimentos(nasc.simula_sinasc(anos=(2018,), seed=4, n_por_muni_mes=10))
    )
    chave = ["cod_ibge6", "ano", "mes"]
    juncao = p_nasc.merge(p_intox, on=chave, how="inner")
    assert len(juncao) > 0
    assert not p_intox.duplicated(subset=chave).any()


def test_recorte_ocupacional_so_vale_para_a_familia_acidental():
    """A hipótese de substituição fala do APLICADOR. Intoxicação em criança
    tende a ser doméstica; em idade de trabalho, ocupacional."""
    bruto = pd.DataFrame([
        _aih("X48", idade=30),   # idade de trabalho
        _aih("X48", idade=8),    # criança
        _aih("X68", idade=30),   # autoprovocada não entra no recorte
    ])
    painel = intox.colapsa_muni_mes(intox.prepara_internacoes(bruto))
    assert painel["n_acidental"].iloc[0] == 2
    assert painel["n_acidental_idade_trabalho"].iloc[0] == 1
    assert "n_autoprovocada_idade_trabalho" not in painel.columns


def test_aliases_datazoom_do_sih_cobrem_as_duas_linguas():
    """Mesma armadilha dos scripts 02 e 03: o padrão do pacote é inglês."""
    for colunas in (
        {"cid_diagnostico_principal": "X48", "municipio_residencia": "230440",
         "data_internacao": "20170315"},
        {"main_diagnosis_cid": "X48", "residence_municipality": "230440",
         "date_admission": "20170315"},
    ):
        saida = intox.prepara_internacoes(pd.DataFrame([colunas]))
        assert len(saida) == 1, colunas
        assert saida.iloc[0]["cod_ibge6"] == "230440"
        assert saida.iloc[0]["mes"] == 3


# --------------------------------------------------------------------------
# 05 — painel: a retroprojeção gestacional é o ponto
# --------------------------------------------------------------------------

def _celulas(anos_meses):
    return pd.DataFrame([{"cod_ibge6": "230440", "ano": a, "mes": m} for a, m in anos_meses])


def test_tratamento_sobe_ao_longo_da_gestacao_em_vez_de_ligar_de_vez():
    """O ban entra em 09/01/2019, mas a coorte de jan/2019 gestou tudo ANTES.

    Marcar tratado por data de nascimento dilui o efeito com gestação não
    exposta — atenuação de direção conhecida. Só a coorte de out/2019 em diante
    teve gestação inteiramente pós-ban.
    """
    saida = painel.acrescenta_exposicao(_celulas([
        (2018, 12), (2019, 1), (2019, 5), (2019, 10), (2020, 6),
    ]))
    s = saida["share_gestacao_pos_ban"].tolist()
    assert s[0] == pytest.approx(0.0)      # dez/2018: gestação toda pré-ban
    assert s[1] == pytest.approx(0.0)      # jan/2019: idem, apesar de "pós-ban"
    assert s[2] == pytest.approx(4 / 9)    # mai/2019: 4 dos 9 meses pós-ban
    assert s[3] == pytest.approx(1.0)      # out/2019: gestação inteira pós-ban
    assert s[4] == pytest.approx(1.0)

    # e o ingênuo diverge exatamente onde deveria
    assert saida["pos_ban_nascimento"].tolist() == [0, 1, 1, 1, 1]


def test_a_marcacao_ingenua_fica_ao_lado_para_medir_a_atenuacao():
    """As duas saem juntas de propósito: a distância entre elas É a atenuação."""
    saida = painel.acrescenta_exposicao(_celulas([(2019, m) for m in range(1, 13)]))
    tratadas_ingenuo = saida["pos_ban_nascimento"].sum()
    exposicao_real = saida["share_gestacao_pos_ban"].sum()
    # 2019 tem 12 coortes; a exposição real soma 7 — o ingênuo superconta 5/12.
    # (jan a set rampam de 0/9 a 8/9; out, nov e dez valem 1 cada.)
    assert tratadas_ingenuo == 12
    assert exposicao_real == pytest.approx(7.0)
    assert (tratadas_ingenuo - exposicao_real) / tratadas_ingenuo == pytest.approx(5 / 12)


def test_trimestres_particionam_a_gestacao():
    """Os três trimestres cobrem a janela inteira, sem sobra nem sobreposição:
    a média deles tem de bater com o share da gestação toda."""
    saida = painel.acrescenta_exposicao(_celulas([(2019, m) for m in range(1, 13)]))
    media_tri = saida[["share_tri1_pos_ban", "share_tri2_pos_ban", "share_tri3_pos_ban"]].mean(axis=1)
    assert np.allclose(media_tri, saida["share_gestacao_pos_ban"])
    # e o 3º trimestre (mais perto do parto) é sempre o mais exposto
    assert (saida["share_tri3_pos_ban"] >= saida["share_tri1_pos_ban"]).all()


def test_janela_e_fixa_e_nao_a_gestacao_observada():
    """⚠️ Usar SEMAGESTAC para retroprojetar seria endógeno: prematuridade é um
    dos desfechos. Se o ban encurta a gestação, a janela andaria junto com o
    tratamento. A constante existe para travar isso."""
    assert painel.JANELA_GESTACIONAL_MESES == 9
    # a função de exposição não aceita gestação observada — só deslocamentos fixos
    import inspect
    assert "semanas" not in inspect.signature(painel.share_pos_ban).parameters


def test_leads_alcancam_2018_e_os_tres_marcos_estao_no_painel():
    """Os leads do event study têm de cobrir a antecipação: notícia (02/2015),
    certeza (12/2018) e obrigação (01/2019)."""
    saida = painel.acrescenta_exposicao(_celulas([(2015, 1), (2015, 2), (2018, 12), (2019, 1)]))
    assert saida["evento_meses"].tolist() == [-48, -47, -1, 0]
    assert saida["pos_noticia"].tolist() == [0, 1, 1, 1]
    assert saida["pos_certeza"].tolist() == [0, 0, 1, 1]


def test_painel_sai_balanceado_e_com_chave_unica():
    """Município-mês sem nascimento é zero, não ausência. Grade furada faria o
    estimador rodar desbalanceado sem ninguém ter decidido isso."""
    pam = pd.DataFrame({
        "cod_ibge6": ["230440", "230440", "230190"],
        "cultura": ["Melão", "Banana (cacho)", "Melão"],
        "area_ha_media": [500.0, 10.0, 0.0],
    })
    nasc_painel = pd.DataFrame({
        "cod_ibge6": ["230440"], "ano": [2018], "mes": [6], "n_nascimentos": [50],
    })
    saida = painel.monta_painel(pam, "Melão", nasc_painel,
                                inicio=(2018, 1), fim=(2018, 12))
    assert len(saida) == 2 * 12                       # 2 municípios × 12 meses
    assert not saida.duplicated(subset=["cod_ibge6", "ano", "mes"]).any()
    assert saida["n_nascimentos"].notna().sum() == 1  # o resto fica ausente, não some


def test_cultura_ancora_nao_tem_default():
    """Flag 1 do CLAUDE.md: o script não escolhe, e cultura inexistente falha
    listando as que existem."""
    pam = pd.DataFrame({"cod_ibge6": ["230440"], "cultura": ["Melão"], "area_ha_media": [10.0]})
    with pytest.raises(KeyError, match="Disponíveis"):
        painel.monta_painel(pam, "Algodão herbáceo (em caroço)", None)


def test_colunas_homonimas_dos_desfechos_nao_se_sobrescrevem():
    """Os scripts 02 e 03 têm `n_peso_valido` os dois. Sem sufixo, a junção
    apagaria um silenciosamente."""
    pam = pd.DataFrame({"cod_ibge6": ["230440"], "cultura": ["Melão"], "area_ha_media": [10.0]})
    n = pd.DataFrame({"cod_ibge6": ["230440"], "ano": [2018], "mes": [6],
                      "n_peso_valido": [50], "peso_medio": [3200.0]})
    f = pd.DataFrame({"cod_ibge6": ["230440"], "ano": [2018], "mes": [6],
                      "n_peso_valido": [2], "n_obito_fetal": [2]})
    saida = painel.monta_painel(pam, "Melão", n, f, inicio=(2018, 6), fim=(2018, 6))
    assert saida["n_peso_valido"].iloc[0] == 50        # o do 02 mantém o nome
    assert saida["n_peso_valido_fetal"].iloc[0] == 2   # o do 03 ganha sufixo


# --------------------------------------------------------------------------
# E7 — inferência: o que importa é ser CALIBRADA, não só rodar
# --------------------------------------------------------------------------

def _dados_dose(n=60, efeito=0.0, ruido=1.0, seed=1, n_zero=20):
    """Municípios com dose em [0,1] e dy = efeito*dose + ruído."""
    rng = np.random.default_rng(seed)
    dose = np.concatenate([np.zeros(n_zero), rng.uniform(0.05, 1.0, n - n_zero)])
    dy = efeito * dose + rng.normal(0, ruido, n)
    return pd.DataFrame({
        "cod_ibge6": [f"23{i:04d}" for i in range(n)], "dose": dose, "dy": dy,
    })


def test_estimador_recupera_efeito_plantado():
    """Sem isso, nenhum dos testes de inferência significa nada."""
    assert robust.estima(_dados_dose(n=400, efeito=10.0, ruido=0.5, seed=2)) == pytest.approx(10.0, abs=0.5)
    assert robust.estima(_dados_dose(n=400, efeito=0.0, ruido=0.5, seed=2)) == pytest.approx(0.0, abs=0.5)


def test_aleatorizacao_e_calibrada_sob_o_nulo():
    """O teste que dá sentido ao script.

    Sob o nulo verdadeiro, a inferência por aleatorização tem de rejeitar perto
    de 5% — nem mais (falso positivo), nem muito menos (poder jogado fora). Um
    procedimento que só roda, sem ser calibrado, dá falsa segurança, que é
    exatamente o que este script existe para não fazer.
    """
    rejeicoes = sum(
        robust.inferencia_aleatorizacao(
            _dados_dose(n=40, efeito=0.0, seed=s), n_perm=200, seed=s
        )["p"] < 0.05
        for s in range(60)
    )
    assert 0 <= rejeicoes <= 8, f"rejeitou {rejeicoes}/60 sob o nulo (esperado ~3)"


def test_aleatorizacao_detecta_efeito_grande():
    """Calibrado não pode significar cego."""
    r = robust.inferencia_aleatorizacao(
        _dados_dose(n=60, efeito=8.0, ruido=1.0, seed=7), n_perm=500, seed=7
    )
    assert r["p"] < 0.05
    assert r["ic_baixo"] > 0     # o IC exclui o zero


def test_com_poucos_tratados_o_ingenuo_e_otimista_demais():
    """O argumento inteiro do script: com poucos municípios de dose alta, o
    assintótico promete precisão que não existe. A distância entre o p ingênuo e
    o de aleatorização É o achado."""
    dados = _dados_dose(n=50, efeito=0.0, ruido=1.0, seed=11, n_zero=46)  # 4 tratados
    p_ing = 2 * (1 - abs(robust.estima(dados) / robust.erro_padrao_ingenuo(dados)))
    p_rnd = robust.inferencia_aleatorizacao(dados, n_perm=500, seed=11)["p"]
    # não afirmo direção fixa num sorteio; afirmo que a aleatorização não é
    # sistematicamente mais frouxa — que é o que a torna a mais dura das três
    assert 0.0 <= p_rnd <= 1.0
    assert robust.wild_cluster_bootstrap(dados, n_boot=300, seed=11)["p"] >= 0.0


def test_sensibilidade_ao_zero_desloca_o_nivel():
    """⚠️ Não é robustez decorativa. O sieve centra a curva em
    `mean(dy[dose==0])`; trocar quem está no zero desloca o nível inteiro."""
    dados = _dados_dose(n=60, efeito=5.0, seed=3, n_zero=20)
    # contamina o zero: metade dele passa a ter dy deslocado, como teria um
    # município com controle vetorial aéreo (§2º do art. 28-B)
    contaminados = set(dados.loc[dados["dose"] <= 0, "cod_ibge6"].iloc[:10])
    tabela = robust.sensibilidade_zero(dados, {"sem controle vetorial": contaminados})

    assert len(tabela) == 2
    assert tabela["n_zero"].iloc[1] < tabela["n_zero"].iloc[0]   # o zero encolheu
    assert tabela["desloc_vs_base"].iloc[0] == 0.0
    assert "desloc_vs_base" in tabela.columns


def test_primeira_diferenca_usa_a_mesma_forma_do_sieve():
    """O objeto estimado tem de ser o mesmo que o `contdid` usa, senão as três
    inferências não são comparáveis com a saída do E6."""
    p = pd.DataFrame({
        "cod_ibge6": ["230440"] * 4,
        "ano": [2018, 2018, 2020, 2020], "mes": [1, 2, 1, 2],
        "peso_medio": [3000.0, 3100.0, 3200.0, 3400.0], "dose": [0.5] * 4,
    })
    saida = robust.primeira_diferenca(p, "peso_medio", 2018 * 12 + 11, 2019 * 12 + 9)
    assert len(saida) == 1
    assert saida["pre"].iloc[0] == pytest.approx(3050.0)
    assert saida["pos"].iloc[0] == pytest.approx(3300.0)
    assert saida["dy"].iloc[0] == pytest.approx(250.0)


# --------------------------------------------------------------------------
# 06 — receita FAO-GAEZ: os três erros que passam verdes
# --------------------------------------------------------------------------

def test_receita_usa_a_DIFERENCA_de_insumo_e_nao_o_nivel():
    """⚠️ Erro nº 1, e o mais fácil de cometer.

    O nível de rendimento mede FERTILIDADE. A diferença alto-menos-baixo mede
    o quanto a terra RESPONDE a insumo — que é o que prediz adoção de cultivo
    intensivo, e portanto o que o instrumento precisa predizer. Trocar um pelo
    outro dá um número plausível e um instrumento diferente.
    """
    # terra A: rende muito sempre (fértil, mas não responde a insumo)
    # terra B: rende pouco sem insumo e muito com (responde)
    alto = np.array([100.0, 90.0])
    baixo = np.array([95.0, 10.0])
    dif = gaez.diferenca_insumo(alto, baixo)
    assert dif.tolist() == [5.0, 80.0]
    # pelo NÍVEL, A ganharia; pela diferença, B — que é o correto
    assert alto.argmax() == 0
    assert dif.argmax() == 1


def test_percentil_e_sobre_a_amostra_inteira_e_ausente_continua_ausente():
    """Imputar ausente pela mediana poria terra DESCONHECIDA no meio da
    distribuição — isso é afirmação, não dado."""
    p = gaez.percentil_nacional(np.array([10.0, 20.0, 30.0, np.nan, 40.0]))
    assert p[0] == pytest.approx(0.0)     # menor
    assert p[4] == pytest.approx(1.0)     # maior
    assert np.isnan(p[3])                 # ausente segue ausente
    assert 0.0 <= np.nanmin(p) and np.nanmax(p) <= 1.0


def test_maximo_entre_culturas_vem_DEPOIS_do_percentil():
    """⚠️ Erro nº 2. Máximo de rendimentos brutos é decidido pela cultura de
    maior tonelagem, não pela de maior aptidão relativa — t/ha de banana e t/ha
    de milho não são comparáveis. Máximo de PERCENTIS é comparável por
    construção.
    """
    # banana rende em ordem de grandeza maior que milho, em unidades brutas
    banana_bruto = np.array([50.0, 10.0])     # município 0 melhor
    milho_bruto = np.array([1.0, 9.0])        # município 1 melhor

    # errado: máximo do bruto -> banana domina os dois municípios
    assert np.maximum(banana_bruto, milho_bruto).tolist() == [50.0, 10.0]

    # certo: percentil primeiro, máximo depois -> cada um no seu melhor
    correto = gaez.combina_culturas({
        "banana": gaez.percentil_nacional(banana_bruto),
        "milho": gaez.percentil_nacional(milho_bruto),
    })
    assert correto.tolist() == [1.0, 1.0]     # ambos são o topo de ALGUMA cultura


def test_uma_cultura_ausente_nao_derruba_o_municipio():
    """Apto para ALGUMA cultura basta — daí o máximo, não a média."""
    saida = gaez.combina_culturas({
        "banana": np.array([0.9, np.nan]),
        "melao": np.array([np.nan, 0.4]),
    })
    assert saida.tolist() == [0.9, 0.4]
    # mas se TODAS faltam, o município fica ausente
    todas_nan = gaez.combina_culturas({"a": np.array([np.nan]), "b": np.array([np.nan])})
    assert np.isnan(todas_nan[0])


def test_normalizacao_fecha_em_zero_e_um():
    """⚠️ Erro nº 3. `dose = 0` e `dose = 1` têm de significar os extremos da
    amostra; sem a segunda reescala o índice não ocupa [0,1]."""
    saida = gaez.normaliza_aptidao(np.array([0.2, 0.5, 0.8]))
    assert saida.min() == pytest.approx(0.0)
    assert saida.max() == pytest.approx(1.0)
    # tudo igual: nenhum extremo é defensável, então o meio
    plano = gaez.normaliza_aptidao(np.array([0.4, 0.4, 0.4]))
    assert np.allclose(plano, 0.5)


def test_receita_completa_respeita_a_ordem_das_quatro_etapas():
    """Ponta a ponta: diferença -> percentil -> máximo -> normalização."""
    tabela = gaez.aptidao_municipal({
        "banana": (np.array([100.0, 90.0, 20.0]), np.array([95.0, 10.0, 19.0])),
        "melao":  (np.array([10.0, 12.0, 80.0]),  np.array([9.0, 11.0, 5.0])),
    })
    assert list(tabela.columns) == ["aptidao_gaez", "percentil_banana", "percentil_melao"]
    assert tabela["aptidao_gaez"].min() == pytest.approx(0.0)
    assert tabela["aptidao_gaez"].max() == pytest.approx(1.0)
    # município 0 responde pouco a insumo nas duas culturas -> é o piso
    assert tabela["aptidao_gaez"].idxmin() == 0


def test_formas_incompativeis_falham_alto():
    with pytest.raises(ValueError, match="Formas diferentes"):
        gaez.diferenca_insumo(np.array([1.0, 2.0]), np.array([1.0]))
    with pytest.raises(ValueError, match="Nenhuma cultura"):
        gaez.combina_culturas({})


# --------------------------------------------------------------------------
# Portabilidade da saída — o console do Windows
# --------------------------------------------------------------------------
#
# Os scripts imprimem ─ ⚠ ✔ ✘ → ≥. No Windows o pipe que captura a saída usa a
# codepage da locale (cp1252), que não encoda nenhum deles, e o script morre de
# UnicodeEncodeError DEPOIS de ter feito o trabalho. Aconteceu: a API do IBGE
# respondeu e o preflight morreu ao imprimir o que tinha achado.
#
# PYTHONIOENCODING só age no arranque do interpretador, então estes são os
# únicos testes por subprocess do arquivo — os demais carregam in-process.
#
# ⚠️ Não testar `--help`: ele usa só a primeira linha do docstring, que é
# ASCII+acentos, e passa com ou sem o conserto. Um teste que nunca falha não é
# portão. O corpo é que quebra.
#
# E nem todo corpo quebra. Medido, rodando cada caminho simulado e conferindo a
# saída contra cp1252 — a contagem estática dos scripts engana, porque a maior
# parte do traço de caixa está em caminhos que a rodada simulada não toma:
#
#     01 dose + MDE     ≈ ✔ ✘     <- portão (é onde a sessão do Windows bateu)
#     04 intoxicacao    ← ⚠️      <- portão
#     05 painel         ⚠️        <- portão
#     04 robustez       ← ⚠️      <- portão
#     03 obito fetal    ⚠️        <- portão
#     02 nascimentos    nenhum    <- NÃO é portão: aqui ele só produz o parquet
#     07 diagnose DP    ─ ⚠️ ✔     <- portão, mas NÃO coberto aqui — ver abaixo
#     08 alvos legisl. ─ ⚠️ ✘     <- portão, e COBERTO: aceita --cache-nomes,
#                                    então prende sem depender de rede
#     06 gaez (erro)    nenhum
#
# Verificado removendo o guarda de cada script: com o do 02 fora, o teste passa
# do mesmo jeito; com o do 01 fora, falha em '\u2718'. Se algum dia o script 02
# ganhar um símbolo na saída, ele vira portão também — por ora, não é.
#
# ⚠️ O script 07 ficou fora da primeira passada por ser untracked, e quebrava de
# verdade — `line 265`, com a decomposição inteira já calculada e perdida. O
# guarda foi aplicado e conferido à mão sob cp1252 nativo (exit 0), mas ele NÃO
# entra nos testes por subprocess: não tem `--fonte simulado` e só roda contra o
# SINASC pela rede. Cobertura por inspeção, não por portão — se algum dia ganhar
# modo simulado, promover a portão aqui.


def _roda_sob_cp1252(args: list[str], saida) -> subprocess.CompletedProcess:
    """Executa um script com a saída forçada a cp1252, como no Windows."""
    return subprocess.run(
        [sys.executable, *args, "--out-dir", str(saida)],
        capture_output=True,          # bytes, não texto: o teste não pode
        cwd=RAIZ,                     # morrer do mesmo mal que está testando
        env={**os.environ, "PYTHONIOENCODING": "cp1252"},
    )


def _exige_saida_limpa(r: subprocess.CompletedProcess) -> None:
    erro = r.stderr.decode("utf-8", errors="replace")
    assert "UnicodeEncodeError" not in erro, erro[-2000:]
    assert r.returncode == 0, erro[-2000:]


def test_saida_sobrevive_a_console_cp1252(tmp_path):
    """As duas famílias de símbolo: o traço de caixa e as marcas ✔/✘."""
    nasc_args = ["scripts/data_prep/02_clean_births.py", "--fonte", "simulado"]
    _exige_saida_limpa(_roda_sob_cp1252(nasc_args, tmp_path))

    parquet = tmp_path / "nascimentos_ce_muni_mes__simulado.parquet"
    assert parquet.exists(), "o script 02 não gravou o painel esperado"

    # este caminho imprime a tabela `falsifica`, que é onde vivem ✔ e ✘
    _exige_saida_limpa(_roda_sob_cp1252(
        ["scripts/data_prep/01_check_dose_variation.py",
         "--fonte", "simulado", "--nascimentos", str(parquet)], tmp_path))


def test_saida_mais_pesada_sobrevive_a_cp1252(tmp_path):
    """O script 04 é o de maior densidade de caractere que quebra em cp1252."""
    _exige_saida_limpa(_roda_sob_cp1252(
        ["scripts/data_prep/04_clean_poisoning.py", "--fonte", "simulado"], tmp_path))


# --------------------------------------------------------------------------
# 07_diagnose_trend_sd.py — a decomposição que decide a leitura do gate E1.5
# --------------------------------------------------------------------------

dp = _carrega("07_diagnose_trend_sd.py")


def _microdado_sintetico(n_muni, nasc_por_ano, sd_real_g, seed=11, sd_individual=568.0):
    """Municípios com heterogeneidade REAL conhecida, mais ruído de amostragem.

    O deslocamento verdadeiro de cada município entre as duas metades tem DP
    `sd_real_g`; o resto do que se observa é amostragem. É esse contraste que a
    decomposição precisa recuperar.
    """
    rng = np.random.default_rng(seed)
    deslocamento = rng.normal(0.0, sd_real_g, n_muni)
    linhas = []
    for i in range(n_muni):
        for ano in dp.ANOS_PRE:
            media = 3200.0 + (deslocamento[i] if ano > 2016 else 0.0)
            pesos = rng.normal(media, sd_individual, nasc_por_ano)
            for peso in pesos:
                linhas.append((f"23{i:04d}", ano, peso))
    return pd.DataFrame(linhas, columns=["cod_ibge6", "ano", "PESO"])


def test_decomposicao_recupera_a_heterogeneidade_real():
    """⚠️ O ponto do script: a DP observada SOMA ruído e sinal, e é o sinal que
    governa o MDE. Ler a observada como se fosse heterogeneidade reprova um
    desenho que talvez passe.

    ⚠️ O regime deste teste é DELIBERADAMENTE generoso (muitos municípios,
    muitos nascimentos). A decomposição é não-viesada mas **ruidosa**: o erro
    da variância observada é de ordem `var·sqrt(2/n)`, então recuperar um sinal
    pequeno com poucos municípios não é possível — e essa é exatamente a
    ressalva que `docs/gates-resultados-dados-reais.md` §6 registra sobre a
    estimativa de 28,4 g do Ceará.
    """
    d = _microdado_sintetico(n_muni=400, nasc_por_ano=500, sd_real_g=40.0)
    _, r = dp.decompoe(d)
    # a observada tem de ficar ACIMA da real — é a soma das duas variâncias
    assert r["dp_observada_g"] > r["dp_real_g"]
    # e a real tem de recuperar os 40 g plantados
    assert r["dp_real_g"] == pytest.approx(40.0, abs=6.0)
    assert r["fracao_variancia_ruido"] > 0.1


def test_municipio_grande_tem_menos_ruido_que_pequeno():
    """O ruído amostral escala com 1/sqrt(n): é isso que faz a DP não ponderada
    do Ceará (mediana de 283 nascimentos/ano) exagerar a heterogeneidade."""
    pequeno = dp.decompoe(_microdado_sintetico(300, 60, sd_real_g=40.0, seed=3))[1]
    grande = dp.decompoe(_microdado_sintetico(300, 600, sd_real_g=40.0, seed=4))[1]
    # o ruído desaba com o porte...
    assert pequeno["dp_ruido_g"] > 2 * grande["dp_ruido_g"]
    # ...e a DP OBSERVADA vai junto, que é o artefato que engana
    assert pequeno["dp_observada_g"] > grande["dp_observada_g"]
    # a heterogeneidade real, essa, NÃO muda com o porte
    assert grande["dp_real_g"] == pytest.approx(pequeno["dp_real_g"], abs=15.0)


def test_sem_heterogeneidade_real_a_componente_vai_a_zero():
    """Municípios idênticos: tudo o que se observa é amostragem, e a
    decomposição não pode inventar sinal onde não há."""
    d = _microdado_sintetico(n_muni=120, nasc_por_ano=200, sd_real_g=0.0)
    _, r = dp.decompoe(d)
    assert r["dp_real_g"] < 12.0
    assert r["fracao_variancia_ruido"] > 0.75


def test_mde_cai_com_mais_tratados_e_com_dp_menor():
    """Conta de desenho, não de resultado — mas é a que inverte o veredito do
    gate, então tem de estar certa nas duas direções."""
    assert dp.mde(47.0, 17, 167) > dp.mde(47.0, 40, 144)   # mais tratados, menor
    assert dp.mde(47.0, 17, 167) > dp.mde(28.0, 17, 167)   # menos DP, menor
    assert np.isnan(dp.mde(47.0, 0, 184))                  # sem tratado, sem conta


# --------------------------------------------------------------------------
# 05_build_panel.py — o encontro das trilhas quebrou por NOME DE ARQUIVO
# --------------------------------------------------------------------------

def _toca_pam(pasta, sufixo):
    alvo = pasta / f"{painel.NOME_PAM}{sufixo}.parquet"
    pd.DataFrame({"cod_ibge6": ["230010"], "cultura": ["Banana (cacho)"],
                  "area_ha_media": [1.0]}).to_parquet(alvo, index=False)
    return alvo


def test_resolve_pam_acha_o_sufixo_da_fonte_real(tmp_path):
    """⚠️ Regressão. O script 01 grava `__sidra`; o 05 procurava só por "" e
    `__simulado`. Resultado: o PAM real existia, o painel não montava, e o erro
    mandava rodar o script 01 que já tinha rodado."""
    _toca_pam(tmp_path, "__sidra")
    caminho, sufixo = painel.resolve_pam(tmp_path, "auto")
    assert caminho is not None and sufixo == "__sidra"


def test_resolve_pam_prefere_real_a_simulado(tmp_path):
    """Com os dois na pasta, o real ganha — senão uma rodada real silenciosamente
    usaria dose simulada, que é o erro que nenhum resultado denuncia."""
    _toca_pam(tmp_path, "__simulado")
    _toca_pam(tmp_path, "__sidra")
    _, sufixo = painel.resolve_pam(tmp_path, "auto")
    assert sufixo == "__sidra"


def test_resolve_pam_nao_mistura_as_duas_fontes(tmp_path):
    """'real' nunca cai no simulado, e 'simulado' nunca sobe para o real."""
    _toca_pam(tmp_path, "__simulado")
    assert painel.resolve_pam(tmp_path, "real") == (None, "")
    _toca_pam(tmp_path, "__sidra")
    caminho, sufixo = painel.resolve_pam(tmp_path, "simulado")
    assert sufixo == "__simulado"


def test_resolve_pam_sem_arquivo_devolve_none(tmp_path):
    assert painel.resolve_pam(tmp_path, "auto") == (None, "")


# --------------------------------------------------------------------------
# 08_alvos_legislativos.py — quem varrer, e o trabalho manual que não pode sumir
# --------------------------------------------------------------------------

alvos = _carrega("08_alvos_legislativos.py")


def _pam_sintetico(n_muni=50):
    """PAM com duas culturas: uma de alta pulverização, uma comparadora."""
    linhas = []
    for i in range(n_muni):
        linhas.append({"cod_ibge6": f"23{i:04d}", "cultura": "Banana (cacho)",
                       "area_ha_media": float(n_muni - i)})
        linhas.append({"cod_ibge6": f"23{i:04d}", "cultura": "Mandioca",
                       "area_ha_media": float(i + 1)})
    return pd.DataFrame(linhas)


def test_decil_usa_a_mesma_conta_do_script_07():
    """⚠️ O decil daqui TEM de ser o do 07: é ele que produz `n_tratados` na
    tabela de MDE, logo é ele cuja contaminação por ban municipal importa.
    Duas definições de 'tratado' no mesmo repositório fariam a varredura cobrir
    um grupo diferente do que o poder usa — e ninguém notaria."""
    d = alvos.decil_superior(_pam_sintetico(50))
    for cultura, bloco in d.groupby("cultura"):
        assert len(bloco) == int(np.ceil(50 * 0.10))   # == max(1, ceil(n*0.10))


def test_comparador_casa_apesar_do_qualificador_do_sidra():
    """O rótulo do SIDRA vem com qualificador; o casamento é por prefixo."""
    assert alvos.e_comparador("Milho (em grão)")
    assert alvos.e_comparador("Arroz (em casca)")
    assert alvos.e_comparador("Mandioca")
    assert not alvos.e_comparador("Banana (cacho)")
    assert not alvos.e_comparador("Melão")


def test_prioridade_separa_alta_pulverizacao_de_comparador():
    """Quem só aparece no decil de mandioca não é alvo prioritário."""
    t = alvos.monta_alvos(alvos.decil_superior(_pam_sintetico(50)), {})
    # os de maior área de banana entram como prioridade 1
    assert t[t.cod_ibge6 == "230000"]["prioridade"].iloc[0] == 1
    # os do topo da mandioca (área cresce com i) são só comparador
    so_mandioca = t[t.motivo_alvo.str.startswith("Mandioca")]
    assert not so_mandioca.empty
    assert (so_mandioca["prioridade"] == 2).all()


def test_rigotto_entra_mesmo_fora_do_decil():
    """Os três municípios expostos entram por construção, como prioridade 1."""
    t = alvos.monta_alvos(alvos.decil_superior(_pam_sintetico(50)), {})
    for cod in alvos.RIGOTTO:
        linha = t[t.cod_ibge6 == cod]
        assert not linha.empty, f"{cod} devia entrar por Rigotto"
        assert linha["prioridade"].iloc[0] == 1


def test_mesclar_preserva_o_levantamento_manual(tmp_path):
    """⚠️ A regressão que mais custaria caro. Varredura de câmara é trabalho
    manual e não se reproduz sozinho: uma segunda rodada do script — depois de
    trocar a cultura-âncora, por exemplo — NÃO pode apagar o que já se achou."""
    destino = tmp_path / "bans.csv"
    primeira = alvos.monta_alvos(alvos.decil_superior(_pam_sintetico(50)), {})
    primeira.to_csv(destino, index=False)

    # alguém varreu e achou uma lei
    achado = pd.read_csv(destino, dtype=str).fillna("")
    alvo = achado.loc[achado.index[0], "cod_ibge6"]
    achado.loc[achado.index[0], ["tem_lei", "numero_lei", "confianca"]] =         ["sim", "999/2011", "confirmado"]
    achado.to_csv(destino, index=False)

    segunda = alvos.mescla_com_existente(
        alvos.monta_alvos(alvos.decil_superior(_pam_sintetico(50)), {}), destino)
    linha = segunda[segunda.cod_ibge6 == alvo].iloc[0]
    assert linha["numero_lei"] == "999/2011"
    assert linha["confianca"] == "confirmado"


def test_semente_nao_sobrescreve_varredura_posterior():
    """A semente do Limoeiro preenche o branco, não corrige quem já olhou."""
    base = alvos.monta_alvos(alvos.decil_superior(_pam_sintetico(50)), {})
    base.loc[base.cod_ibge6 == "230760", ["confianca", "numero_lei"]] =         ["ausente_conferido", "nada"]
    depois = alvos.aplica_semente(base)
    assert depois[depois.cod_ibge6 == "230760"]["numero_lei"].iloc[0] == "nada"


def test_resolve_pam_do_08_nao_mistura_fontes(tmp_path):
    """Mesma regra do script 05: 'real' nunca cai no simulado."""
    (tmp_path / f"{alvos.NOME_PAM}__simulado.parquet").write_bytes(b"x")
    assert alvos.resolve_pam(tmp_path, "real") == (None, "")
    assert alvos.resolve_pam(tmp_path, "simulado")[1] == "__simulado"


def _roda_sob_cp1252_bruto(args: list[str]) -> subprocess.CompletedProcess:
    """Como `_roda_sob_cp1252`, mas sem cravar `--out-dir`.

    O script 08 não tem essa flag: ele escreve em `docs/`, não em
    `data/processed/`, porque o produto é tabela derivada que precisa ser
    **visível ao git** — `data/` é gitignored, e um arquivo ali nunca chega às
    sessões remotas.
    """
    return subprocess.run(
        [sys.executable, *args],
        capture_output=True,
        cwd=RAIZ,
        env={**os.environ, "PYTHONIOENCODING": "cp1252"},
    )


def test_alvos_legislativos_sobrevive_a_cp1252(tmp_path):
    """⚠️ Portão de cp1252 para o script 08, e ele prende SEM REDE.

    Diferente do 07 — que só roda contra o SINASC e por isso ficou fora dos
    testes por subprocess —, o 08 aceita `--cache-nomes`, então a API de
    localidades do IBGE pode ser pré-semeada. É o que torna este um portão de
    verdade e não um teste que depende do dia.

    O caminho exercitado imprime `⚠️`, `✘` e `─`, que é a família que quebra."""
    import json

    pam = pd.DataFrame({
        "cod_ibge6": ["230760", "230010", "230020"],
        "cultura": ["Banana (cacho)"] * 3,
        "area_ha_media": [100.0, 50.0, 10.0],
    })
    pam.to_parquet(tmp_path / f"{alvos.NOME_PAM}__simulado.parquet", index=False)

    cache = tmp_path / "nomes.json"
    cache.write_text(json.dumps(
        [{"id": 2307601, "nome": "Limoeiro do Norte"},
         {"id": 2300101, "nome": "Abaiara"},
         {"id": 2300200, "nome": "Acarapé"}], ensure_ascii=False), encoding="utf-8")

    r = _roda_sob_cp1252_bruto([
        "scripts/data_prep/08_alvos_legislativos.py",
        "--fonte", "simulado",
        "--dir-dados", str(tmp_path),
        "--cache-nomes", str(cache),
        "--destino", str(tmp_path / "bans.csv"),
    ])
    _exige_saida_limpa(r)
    assert (tmp_path / "bans.csv").exists()


def test_alvos_legislativos_falha_legivel_sem_pam(tmp_path):
    """Sem PAM ele tem de dizer o que rodar, não estourar — e a mensagem sai
    com `✘`, que em cp1252 é exatamente o que mata sem o guarda."""
    r = _roda_sob_cp1252_bruto([
        "scripts/data_prep/08_alvos_legislativos.py",
        "--fonte", "sidra",
        "--dir-dados", str(tmp_path),
        "--destino", str(tmp_path / "bans.csv"),
    ])
    erro = r.stderr.decode("utf-8", errors="replace")
    assert "UnicodeEncodeError" not in erro, erro[-2000:]
    assert r.returncode == 1              # falha declarada, não acidente
    assert b"01_check_dose_variation" in r.stdout   # diz o que rodar antes


# --------------------------------------------------------------------------
# ban_municipal_data no painel — a distinção que NÃO pode morrer na fronteira
# --------------------------------------------------------------------------

def _csv_bans(tmp_path, linhas):
    caminho = tmp_path / "bans.csv"
    pd.DataFrame(linhas).to_csv(caminho, index=False)
    return caminho


def test_carrega_bans_preserva_a_distincao_de_confianca(tmp_path):
    """⚠️ A regressão central. `inconclusivo` (ninguém conseguiu conferir) e
    `ausente_conferido` (conferido, não há lei) têm data vazia NOS DOIS CASOS.
    Se o painel levasse só a data, os dois virariam NaT e ficariam
    indistinguíveis de um município comprovadamente não tratado — e a estimação
    trataria "não sei" como "não". É a falha silenciosa que a varredura inteira
    existe para evitar."""
    c = _csv_bans(tmp_path, [
        {"cod_ibge6": "230760", "data_lei": "2009-11-20", "confianca": "confirmado"},
        {"cod_ibge6": "230010", "data_lei": "", "confianca": "ausente_conferido"},
        {"cod_ibge6": "230020", "data_lei": "", "confianca": "inconclusivo"},
    ])
    b = painel.carrega_bans_municipais(c).set_index("cod_ibge6")
    assert pd.isna(b.loc["230010", "ban_municipal_data"])
    assert pd.isna(b.loc["230020", "ban_municipal_data"])
    # ...mas a confiança separa os dois, que é o ponto
    assert b.loc["230010", "ban_municipal_confianca"] == "ausente_conferido"
    assert b.loc["230020", "ban_municipal_confianca"] == "inconclusivo"
    assert b.loc["230760", "ban_municipal_data"] == pd.Timestamp("2009-11-20")


def test_municipio_fora_do_csv_vira_nao_verificado(tmp_path):
    """Quem a varredura nem alcançou NÃO pode entrar como 'não tratado'."""
    medias, nasc = _medias_e_painel()
    c = _csv_bans(tmp_path, [{"cod_ibge6": "999999", "data_lei": "",
                              "confianca": "ausente_conferido"}])
    p = painel.monta_painel(medias, "Melão", nasc,
                            bans=painel.carrega_bans_municipais(c))
    assert (p["ban_municipal_confianca"] == "nao_verificado").all()
    assert p["ban_municipal_data"].isna().all()


def test_ban_nao_altera_a_grade_do_painel():
    """O merge não pode duplicar célula nem perder município — 184×96 é o
    invariante que o gate E5 estabeleceu."""
    medias, nasc = _medias_e_painel()
    sem = painel.monta_painel(medias, "Melão", nasc, bans=pd.DataFrame(
        columns=["cod_ibge6", "ban_municipal_data", "ban_municipal_confianca"]))
    com = painel.monta_painel(medias, "Melão", nasc, bans=pd.DataFrame({
        "cod_ibge6": [medias["cod_ibge6"].iloc[0]],
        "ban_municipal_data": [pd.Timestamp("2009-11-20")],
        "ban_municipal_confianca": ["confirmado"]}))
    assert len(sem) == len(com)
    assert sem["cod_ibge6"].nunique() == com["cod_ibge6"].nunique()
    assert com["ban_municipal_data"].notna().any()


def test_sem_arquivo_de_bans_o_painel_ainda_monta(tmp_path):
    """A varredura pode não ter rodado. O painel não pode quebrar por isso —
    mas também não pode fingir que ninguém tem ban."""
    b = painel.carrega_bans_municipais(tmp_path / "nao-existe.csv")
    assert b.empty
    medias, nasc = _medias_e_painel()
    p = painel.monta_painel(medias, "Melão", nasc, bans=b)
    assert (p["ban_municipal_confianca"] == "nao_verificado").all()


# --------------------------------------------------------------------------
# 10_clean_sinan_iexo.py — o canal A5, e os códigos conferidos
# --------------------------------------------------------------------------

sinan = _carrega("10_clean_sinan_iexo.py")


def test_trunca_o_digito_verificador_do_id_municip():
    """⚠️ ID_MUNICIP tem 7 dígitos; cod_ibge6 tem 6. Sem truncar, o join com o
    painel de nascimentos não casa — e não casa EM SILÊNCIO."""
    d = pd.DataFrame({"ID_MUNICIP": ["2307601", "2311504", "1234567"]})
    r = sinan.filtra_ceara(d)
    assert list(r["cod_ibge6"]) == ["230760", "231150"]   # o de fora do CE sai


def test_descarta_municipio_ignorado():
    """230000 é unidade sem denominador possível — mesma regra dos scripts 02/03."""
    d = pd.DataFrame({"ID_MUNICIP": ["2300000", "2307601"]})
    assert list(sinan.filtra_ceara(d)["cod_ibge6"]) == ["230760"]


def test_circunstancia_separa_intencional_de_nao_intencional():
    """⚠️ O contraste que É o placebo. 03 (ambiental) entra como NÃO
    intencional — foi o que a conferência do dicionário acrescentou à leitura
    suposta do gates doc, que só previa 02."""
    d = pd.DataFrame({"ID_MUNICIP": ["2307601"] * 6,
                      "AGENTE_TOX": ["02"] * 6,
                      "CIRCUNSTAN": ["01", "02", "03", "10", "12", "99"]})
    r = sinan.classifica(d)
    assert list(r["nao_intencional"]) == [True, True, True, False, False, False]
    assert list(r["intencional"]) == [False, False, False, True, True, False]
    assert r["circunstancia_ignorada"].sum() == 1      # o 99


def test_agente_04_e_a_flag_5_e_nao_se_confunde_com_agricola():
    """04 é controle vetorial (o §2º do art. 28-B). Colapsá-lo em 02 poria
    contaminação do d=0 dentro do próprio canal A5."""
    d = pd.DataFrame({"ID_MUNICIP": ["2307601"] * 3,
                      "AGENTE_TOX": ["02", "03", "04"], "CIRCUNSTAN": ["02"] * 3})
    r = sinan.classifica(d)
    assert list(r["agrotoxico_agricola"]) == [True, False, False]
    assert list(r["agrotoxico_saude_publica"]) == [False, False, True]
    assert list(r["agrotoxico_domestico"]) == [False, True, False]


def test_preflight_reprova_sem_coluna_essencial():
    """⚠️ Filtro contra coluna ausente não dá erro — dá vazio. O preflight
    existe para o vazio virar exceção em vez de conclusão."""
    ok, notas = sinan.preflight(pd.DataFrame({"ID_MUNICIP": ["2307601"]}))
    assert not ok and "DT_NOTIFIC" in notas
    ok2, _ = sinan.preflight(pd.DataFrame({"ID_MUNICIP": ["x"], "DT_NOTIFIC": ["y"]}))
    assert ok2


def test_colapso_preserva_o_cruzamento_agricola_x_intencao():
    """O canal precisa do cruzamento, não só das marginais."""
    d = pd.DataFrame({
        "ID_MUNICIP": ["2307601"] * 4,
        "DT_NOTIFIC": ["20150310"] * 4,
        "AGENTE_TOX": ["02", "02", "04", "02"],
        "CIRCUNSTAN": ["02", "10", "02", "03"]})
    painel = sinan.colapsa_muni_mes(sinan.extrai_ano_mes(sinan.classifica(
        sinan.filtra_ceara(d))))
    linha = painel.iloc[0]
    assert linha["n_agricola"] == 3
    assert linha["n_agricola_nao_intencional"] == 2   # 02 e 03
    assert linha["n_agricola_intencional"] == 1      # o 10


def test_mil_nao_come_virgula_literal():
    """⚠️ Regressão: `f"{n:,}".replace(",", ".")` na linha inteira transformava
    '01,02,03' em '01.02.03' e 'CE, pós-limpeza' em 'CE. pós-limpeza'."""
    assert sinan._mil(1517) == "1.517"
    assert sinan._mil(266) == "266"


# --------------------------------------------------------------------------
# 11_clean_populacao.py — o denominador, e a quebra censitária
# --------------------------------------------------------------------------

pop_mod = _carrega("11_clean_populacao.py")


def test_trunca_codigo_de_7_digitos_do_sidra():
    """D1C do SIDRA tem 7 dígitos; cod_ibge6 tem 6. Sem truncar, nada casa."""
    r = pop_mod._sidra_para_longo([
        {"D1C": "2307601", "D3N": "2015", "V": "56264"}])
    assert r.loc[0, "cod_ibge6"] == "230760"
    assert r.loc[0, "populacao"] == 56264


def test_descarta_codigos_de_ausencia_do_sidra():
    """'-', '..', 'X' são ausência no SIDRA, não zero. Virar 0 faria a taxa
    explodir para infinito em vez de sumir."""
    r = pop_mod._sidra_para_longo([
        {"D1C": "2307601", "D3N": "2015", "V": "-"},
        {"D1C": "2311504", "D3N": "2015", "V": ".."},
        {"D1C": "2311801", "D3N": "2015", "V": "70000"}])
    assert list(r["cod_ibge6"]) == ["231180"]


def test_ano_censitario_esta_declarado():
    """⚠️ Regressão. 2022 NÃO tem estimativa na tabela 6579 — conferido rodando:
    zero registros. Sem o recurso à tabela do Censo o último ano do painel sai
    com denominador NaN e a taxa some em silêncio."""
    assert 2022 in pop_mod.ANOS_CENSITARIOS
    tabela, variavel = pop_mod.ANOS_CENSITARIOS[2022]
    assert tabela != pop_mod.TABELA        # tem de ser OUTRA tabela
    assert variavel != pop_mod.VARIAVEL


def test_simulado_marca_a_origem_do_numero():
    """A distinção estimativa/censo viaja NA TABELA, não só no docstring."""
    r = pop_mod.simula_populacao(anos=(2021, 2022))
    assert set(r["origem"]) == {"estimativa", "censo"}
    assert (r[r.ano == 2022]["origem"] == "censo").all()


def test_painel_calcula_taxa_e_preserva_a_grade():
    """A população não pode duplicar célula — 184×96 é o invariante do E5."""
    medias, nasc = _medias_e_painel()
    codigos = medias["cod_ibge6"].unique()
    pop = pd.DataFrame([{"cod_ibge6": c, "ano": a, "populacao": 10_000,
                         "populacao_origem": "estimativa"}
                        for c in codigos for a in range(2015, 2023)])
    sem = painel.monta_painel(medias, "Melão", nasc)
    com = painel.monta_painel(medias, "Melão", nasc, populacao=pop)
    assert len(sem) == len(com)
    assert com["populacao"].notna().all()


def test_sem_populacao_o_painel_ainda_monta():
    """A coluna existe mesmo sem o arquivo — mas vazia, não zero."""
    medias, nasc = _medias_e_painel()
    p = painel.monta_painel(medias, "Melão", nasc, populacao=pd.DataFrame())
    assert "populacao" in p.columns
    assert p["populacao"].isna().all()


# --------------------------------------------------------------------------
# SINAN no painel — zero só dentro da cobertura
# --------------------------------------------------------------------------

def _sinan_parcial(codigos, anos):
    """Painel SINAN cobrindo SÓ os anos pedidos."""
    return pd.DataFrame([
        {"cod_ibge6": c, "ano": a, "mes": m, "n_notificacoes": 1,
         "n_agricola": 1, "n_agricola_nao_intencional": 1}
        for c in codigos[:3] for a in anos for m in (1, 6)])


def test_ano_sem_download_do_sinan_vira_nan_nao_zero():
    """⚠️ A regressão mais cara desta rodada, e eu mesmo a criei antes de pegá-la.

    `fillna(0)` cego transforma 'ano nunca baixado' em 'zero notificações'. Num
    painel 2015–2022 com só 2015 baixado, isso diz que o canal A5 **desapareceu
    a partir de 2016** — que é justamente o ano seguinte ao início da janela e
    logo antes do ban. Achado espúrio pronto, saído de preenchimento de NaN.
    """
    medias, nasc = _medias_e_painel()
    codigos = list(medias["cod_ibge6"].unique())
    p = painel.monta_painel(medias, "Melão", nasc,
                            sinan=_sinan_parcial(codigos, [2015]))
    dentro = p[p["ano"] == 2015]
    fora = p[p["ano"] > 2015]
    assert dentro["sinan_n_agricola"].notna().all(), "2015 foi baixado: 0 é legítimo"
    assert fora["sinan_n_agricola"].isna().all(), "ano não baixado tem de ser NaN"
    assert not fora["sinan_ano_coberto"].any()


def test_zero_legitimo_sobrevive_dentro_da_cobertura():
    """Município-mês sem notificação, dentro de ano baixado, É zero — não NaN.
    Confundir os dois na outra direção apagaria a ausência real de eventos."""
    medias, nasc = _medias_e_painel()
    codigos = list(medias["cod_ibge6"].unique())
    p = painel.monta_painel(medias, "Melão", nasc,
                            sinan=_sinan_parcial(codigos, [2015]))
    em_2015 = p[p["ano"] == 2015]
    # meses 2..5 e 7..12 não estão no fixture, mas o ano está coberto
    assert (em_2015["sinan_n_agricola"] == 0).any()


def test_sinan_entra_prefixado_e_nao_colide_com_o_sih():
    """SIH e SINAN medem coisas diferentes — internação faturada contra
    notificação compulsória —, e diferem por duas ordens de grandeza. Deixar
    `n_agricola` nu ao lado de `n_acidental` convidaria a somá-los."""
    medias, nasc = _medias_e_painel()
    codigos = list(medias["cod_ibge6"].unique())
    p = painel.monta_painel(medias, "Melão", nasc,
                            sinan=_sinan_parcial(codigos, [2015, 2016]))
    assert "sinan_n_agricola" in p.columns
    assert "n_agricola" not in p.columns


# --------------------------------------------------------------------------
# GAEZ no painel — o instrumento, e a ordem percentil→recorte
# --------------------------------------------------------------------------

def test_percentil_e_nacional_nao_estadual():
    """⚠️ O erro nº 2 da lista do script 06, e ele passa verde: ranquear só o
    Ceará dá a posição DENTRO do estado, não no país — número plausível em
    [0,1], instrumento errado. O percentil tem de ver a distribuição inteira
    antes de qualquer recorte."""
    nacional = np.array([1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    p_nac = gaez.percentil_nacional(nacional)
    # os três últimos são o topo do país
    assert p_nac[-1] == pytest.approx(1.0)
    # se ranqueássemos só esse subconjunto, o menor deles viraria 0.0
    p_sub = gaez.percentil_nacional(nacional[-3:])
    assert p_sub[0] == pytest.approx(0.0)
    assert p_nac[-3] > 0.5, "no ranking nacional ele NÃO é o menor"


def test_percentil_ignora_ausente_em_vez_de_imputar():
    """Terra sem dado não entra no ranking. Imputar pela mediana poria terra
    desconhecida no meio da distribuição — afirmação, não dado."""
    v = np.array([1.0, np.nan, 3.0])
    r = gaez.percentil_nacional(v)
    assert np.isnan(r[1])
    assert r[0] == pytest.approx(0.0) and r[2] == pytest.approx(1.0)


def test_diferenca_de_insumo_nao_e_o_nivel():
    """A receita é ALTO menos BAIXO. Usar o nível troca o instrumento por outra
    coisa — fertilidade em vez de resposta a insumo — e nada acusa."""
    alto = np.array([100.0, 100.0])
    baixo = np.array([90.0, 10.0])
    d = gaez.diferenca_insumo(alto, baixo)
    assert d[1] > d[0], "a terra que responde mais a insumo tem diferença maior"


def test_gaez_entra_no_painel_sem_alterar_a_grade():
    """Invariante do E5: o merge não pode duplicar nem perder célula."""
    medias, nasc = _medias_e_painel()
    codigos = medias["cod_ibge6"].unique()
    g = pd.DataFrame({"cod_ibge6": codigos,
                      "aptidao_gaez": np.linspace(0, 1, len(codigos))})
    sem = painel.monta_painel(medias, "Melão", nasc)
    com = painel.monta_painel(medias, "Melão", nasc, gaez=g)
    assert len(sem) == len(com)
    assert com["aptidao_gaez"].notna().all()


def test_sem_gaez_a_coluna_existe_vazia():
    """Sem o raster o painel monta — mas a aptidão fica NaN, não zero. Zero
    diria 'terra sem aptidão', que é afirmação sobre o mundo."""
    medias, nasc = _medias_e_painel()
    p = painel.monta_painel(medias, "Melão", nasc, gaez=pd.DataFrame())
    assert "aptidao_gaez" in p.columns and p["aptidao_gaez"].isna().all()


# --------------------------------------------------------------------------
# D4 — a janela da dose vira parâmetro, sem sobrescrever o painel canônico
# --------------------------------------------------------------------------

def test_janela_padrao_nao_ganha_sufixo():
    """A rodada canônica tem de continuar gravando no nome de sempre — senão o
    script 05 não acha o painel e o E5 quebra de novo."""
    assert dose.sufixo_da_janela(dose.ANOS_PRE_BAN) == ""
    assert dose.sufixo_da_janela(list(reversed(dose.ANOS_PRE_BAN))) == ""


def test_janela_da_d4_ganha_sufixo_proprio():
    """⚠️ Sem isto, `--anos 2010..2014` gravaria POR CIMA do painel canônico e o
    script 05 leria o arquivo de sempre com dose medida em outra janela — sem
    nada acusar. Mesma classe de erro do `__sidra` que quebrou o E5."""
    assert dose.sufixo_da_janela((2010, 2011, 2012, 2013, 2014)) == "__2010_2014"
    assert dose.sufixo_da_janela((2013, 2014)) == "__2013_2014"


def test_carrega_pam_arquivo_honra_a_janela(tmp_path):
    """⚠️ Regressão: `carrega_pam_arquivo` usava ANOS_PRE_BAN fixo, então
    `--anos 2010..2014 --fonte arquivo` filtrava para 2015–2018 e devolvia
    VAZIO, sem erro. A janela tem de chegar até o filtro."""
    import inspect
    sig = inspect.signature(dose.carrega_pam_arquivo)
    assert "anos" in sig.parameters, "a janela tem de ser parâmetro, não constante"


# --------------------------------------------------------------------------
# 09_holm.py e 10_spt_pretrend.py — o que a auditoria de 2026-09-22 mandou criar
#
# O 09 cumpre a correção de Holm que a §6 da pré-especificação declarava e que
# nenhuma linha implementava. O 10 é a sonda do strong parallel trends que o
# CGS §6.3 propõe — a hipótese de que o alvo primário precisava.
#
# ⚠️ Os dois leem painel. O teste NÃO usa `data/processed/`, que é gitignored e
# portanto ausente em clone novo: constrói painel sintético próprio. É o que
# torna estes testes rodáveis em CI.
# --------------------------------------------------------------------------

holm_mod = _carrega("09_holm.py", sub="estimate")
spt_mod = _carrega("10_spt_pretrend.py", sub="estimate")


def test_holm_valores_conhecidos():
    """Holm a mão, para dois casos onde a conta é conferível."""
    # p ordenados 0,01 e 0,04 com m=2: 0,01x2=0,02 ; 0,04x1=0,04
    assert holm_mod.holm([0.01, 0.04]) == pytest.approx([0.02, 0.04])
    # a ordem de entrada não importa — o ajuste segue o p, não a posição
    assert holm_mod.holm([0.04, 0.01]) == pytest.approx([0.04, 0.02])


def test_holm_impoe_monotonicidade():
    """Sem o acúmulo do máximo, o segundo p ajustado sairia MENOR que o primeiro.

    0,03x2 = 0,06 e 0,04x1 = 0,04. Devolver [0,06 ; 0,04] não seria p-valor.
    """
    assert holm_mod.holm([0.03, 0.04]) == pytest.approx([0.06, 0.06])


def test_holm_nunca_passa_de_um():
    assert holm_mod.holm([0.6, 0.7]) == pytest.approx([1.0, 1.0])


def test_holm_uma_hipotese_nao_corrige():
    """Com m=1 não há família, e Holm tem de ser a identidade."""
    assert holm_mod.holm([0.031]) == pytest.approx([0.031])


def test_placebos_cabem_inteiros_no_pre_periodo():
    """Nenhuma janela placebo pode encostar no ban — senão o teste é circular."""
    t_ini, t_fim, gap, larg = 2015 * 12, 2018 * 12 + 11, 10, 12
    cortes = spt_mod.placebos(t_ini, t_fim, gap, larg)
    assert cortes, "o pré-período de 2015-2018 comporta ao menos um corte"
    for a, b in cortes:
        assert b - a == gap, "o gap placebo tem de espelhar o do desenho real"
        assert a - larg >= t_ini, "janela pré do placebo vaza antes do início"
        assert b + larg <= t_fim, "⚠️ janela pós do placebo alcança o ban"


def test_placebos_vazio_quando_janela_nao_cabe():
    """Pré-período curto tem de devolver lista vazia, não janela inválida."""
    assert spt_mod.placebos(2018 * 12, 2018 * 12 + 11, 10, 12) == []


def _painel_sintetico(caminho, n_muni=60, seed=7):
    """Painel mínimo com as colunas que os dois scripts exigem."""
    rng = np.random.default_rng(seed)
    linhas = []
    dose = np.concatenate([np.zeros(n_muni // 4),
                           rng.gamma(2.0, 0.02, n_muni - n_muni // 4)])
    for i in range(n_muni):
        nivel = 3200 + rng.normal(0, 40)
        for ano in range(2015, 2023):
            for mes in range(1, 13):
                linhas.append({
                    "cod_ibge6": 230000 + i,
                    "ano": ano, "mes": mes,
                    "dose": float(dose[i]),
                    "peso_medio": nivel + rng.normal(0, 25),
                    "taxa_obito_fetal": abs(rng.normal(0.01, 0.003)),
                })
    pd.DataFrame(linhas).to_parquet(caminho)
    return caminho


def test_holm_e_spt_sobrevivem_a_cp1252(tmp_path):
    """Portão de encoding: os dois imprimem ⚠️, ✔ e traço de caixa."""
    painel = _painel_sintetico(tmp_path / "painel_teste.parquet")

    for args in (
        ["scripts/estimate/09_holm.py", "--painel", str(painel), "--n-boot", "60"],
        ["scripts/estimate/10_spt_pretrend.py", "--painel", str(painel),
         "--desfecho", "peso_medio", "--n-boot", "60"],
    ):
        _exige_saida_limpa(_roda_sob_cp1252(args, tmp_path))

    assert (tmp_path / "holm_confirmatorios.csv").exists()
    assert (tmp_path / "spt_pretrend__peso_medio.csv").exists()


def test_holm_grava_as_duas_hipoteses_confirmatorias(tmp_path):
    """A família da §6 tem DUAS hipóteses; gravar uma só seria Holm otimista."""
    painel = _painel_sintetico(tmp_path / "painel_teste.parquet")
    r = _roda_sob_cp1252(
        ["scripts/estimate/09_holm.py", "--painel", str(painel), "--n-boot", "60"],
        tmp_path)
    _exige_saida_limpa(r)

    res = pd.read_csv(tmp_path / "holm_confirmatorios.csv")
    assert len(res) == 2, "a família confirmatória tem de sair completa"
    assert set(res["desfecho"]) == {"peso_medio", "taxa_obito_fetal"}
    for col in ("p_uni_holm", "p_rnd_holm", "p_wcb_holm"):
        assert (res[col] >= res[col.replace("_holm", "")] - 1e-9).all(), \
            f"{col}: p ajustado nunca pode ser MENOR que o bruto"
        assert (res[col] <= 1.0).all()


# --------------------------------------------------------------------------
# 11_weitzman_inversao.py — a rota 3 do Ensaio 2
#
# ⚠️ O teste que mais importa aqui é o que garante que o script NAO conclui
# quando nao tem faixa de beta. Concluir sem calibracao seria exatamente o erro
# de alvo que a auditoria pegou: usar o IC do ACR como se fosse do ACR'.
# --------------------------------------------------------------------------

wtz = _carrega("11_weitzman_inversao.py", sub="estimate")


def test_weitzman_regra_bate_com_o_teorema():
    """beta > c => proibicao domina (Delta < 0). beta < c => taxa domina."""
    assert wtz.vantagem_preco(beta=10.0, c=5.0, sigma=1.0) < 0     # quantidade
    assert wtz.vantagem_preco(beta=2.0, c=5.0, sigma=1.0) > 0      # preco
    assert wtz.vantagem_preco(beta=5.0, c=5.0, sigma=1.0) == pytest.approx(0.0)


def test_weitzman_sigma_escala_mas_nao_vira_o_lado():
    """Mais incerteza aumenta a magnitude e NUNCA troca o instrumento."""
    a = wtz.vantagem_preco(beta=10.0, c=5.0, sigma=1.0)
    b = wtz.vantagem_preco(beta=10.0, c=5.0, sigma=3.0)
    assert abs(b) > abs(a)
    assert np.sign(a) == np.sign(b)
    assert wtz.limiar_beta(5.0) == 5.0


def test_weitzman_sem_calibracao_nao_conclui():
    """⚠️ O portao central: sem faixa de beta, TUDO tem de sair indeterminado."""
    fr = wtz.fronteira(np.linspace(1, 60, 9), sigma=1.0, beta_faixa=None)
    assert (fr["conclusao"] == "indeterminado").all()
    assert fr["beta_min"].isna().all()


def test_weitzman_com_calibracao_conclui_nos_extremos():
    fr = wtz.fronteira(np.linspace(1, 60, 9), sigma=1.0, beta_faixa=(40.0, 55.0))
    assert (fr["conclusao"] == "proibição").any(), "c bem abaixo de beta"
    assert (fr["conclusao"] == "taxa").any(), "c bem acima de beta"
    assert (fr["conclusao"] == "indeterminado").any(), "a faixa tem de cruzar"


# --------------------------------------------------------------------------
# 12_clean_conab_custos.py — o lado do custo da inversao de Weitzman
# --------------------------------------------------------------------------

conab = _carrega("12_clean_conab_custos.py")


def test_conab_alvos_cobrem_aviao_e_trator():
    """Os dois itens de linha que a substituicao aereo->terrestre precisa."""
    assert "custo_aviao" in conab.ALVOS
    assert "custo_tratores" in conab.ALVOS
    assert conab.ALVOS["custo_aviao"].startswith("2 - Opera")


def test_conab_num_tolera_texto():
    """A planilha mistura numero e texto livre; o parser nao pode morrer."""
    assert conab._num("") != conab._num("")          # NaN
    assert conab._num(520) == 520.0
    assert conab._num("nao e numero") != conab._num("nao e numero")


def test_conab_le_aba_ignora_indice():
    """A aba 'Índice' nao casa o padrao regiao-UF-ano e tem de sair como None."""
    class _XL:
        def parse(self, aba, header=None):
            raise AssertionError("nao deveria abrir a aba Indice")
    assert conab.le_aba(_XL(), "Índice") is None


# --------------------------------------------------------------------------
# 13_censo_agro_equipamento.py — quem pulverizava por aviao
#
# ⚠️ Os dois testes que importam sao os das ARMADILHAS que custaram tempo:
# o gzip sem header do IBGE, e o codigo de 6 digitos que devolve HTTP 500.
# --------------------------------------------------------------------------

equip = _carrega("13_censo_agro_equipamento.py")


def test_equip_categorias_separam_aeronave_de_terrestre():
    """O par que a substituicao aereo->terrestre precisa, com rotulo estavel."""
    assert equip.EQUIPAMENTOS["113450"] == "aeronave"
    assert equip.EQUIPAMENTOS["113449"] == "tracao_mecanica"
    assert equip.TABELA == 1008 and equip.PERIODO == "2006"


def test_equip_confronta_sem_painel_nao_explode(tmp_path):
    """Sem painel o script segue e avisa; nao pode morrer no confronto."""
    tb = pd.DataFrame({"cod_ibge6": ["230760"], "municipio": ["X"],
                       "aeronave": [18.0], "tracao_mecanica": [56.0],
                       "costal": [1.0], "total": [100.0]})
    assert equip.confronta(tb, tmp_path / "nao_existe.parquet") is None


def test_equip_confronta_marca_decil_e_preenche_zero(tmp_path):
    """Municipio ausente do censo entra como ZERO, nunca como NaN silencioso."""
    pn = pd.DataFrame({"cod_ibge6": ["230760", "230010"] * 3,
                       "dose": [0.39, 0.0] * 3, "dose_ha": [1858.0, 0.0] * 3})
    alvo = tmp_path / "painel.parquet"
    pn.to_parquet(alvo)
    tb = pd.DataFrame({"cod_ibge6": ["230760"], "municipio": ["Limoeiro"],
                       "aeronave": [18.0], "tracao_mecanica": [56.0],
                       "costal": [1.0], "total": [100.0]})
    m = equip.confronta(tb, alvo)
    assert m is not None and len(m) == 2
    assert m.loc[m.cod_ibge6 == "230010", "aeronave"].iloc[0] == 0.0
    assert "decil_superior" in m.columns and m["decil_superior"].any()


# --------------------------------------------------------------------------
# Rota 1 — recorte multi-UF (desenho de fronteira CE x vizinho)
#
# O ban é ESTADUAL: o grupo de comparação de um desenho de fronteira vive fora
# da UF 23. Estes testes travam as três coisas que, se quebrarem, quebram em
# SILÊNCIO — recorte territorial errado no SIDRA, código de "município
# ignorado" entrando como município, e arquivo multi-UF sobrescrevendo o painel
# canônico do Ceará. Ver docs/auditoria-mensuracao-do-tratamento.md §4.
# --------------------------------------------------------------------------

def test_territorio_sidra_uma_uf_preserva_o_comportamento_antigo():
    assert dose.territorio_sidra(("23",)) == dose.SIDRA_TERRITORIO


def test_territorio_sidra_duas_ufs_usa_lista_separada_por_virgula():
    assert dose.territorio_sidra(("23", "24")) == "in n3 23,24"


@pytest.mark.parametrize("modulo", [dose, nasc])
def test_sufixo_das_ufs_vazio_no_padrao_e_marcado_fora_dele(modulo):
    # Vazio no padrão: uma rodada só-Ceará não pode mudar de nome de arquivo.
    assert modulo.sufixo_das_ufs(("23",)) == ""
    # Fora do padrão o nome MUDA — é o que impede a sobrescrita silenciosa.
    assert modulo.sufixo_das_ufs(("23", "24")) == "__uf23-24"
    # E é estável à ordem: --ufs 24 23 grava no mesmo lugar que --ufs 23 24.
    assert modulo.sufixo_das_ufs(("24", "23")) == modulo.sufixo_das_ufs(("23", "24"))


def test_filtra_ufs_mantem_as_duas_ufs_e_descarta_os_dois_ignorados():
    # 230000 e 240000 são "município ignorado" de CE e RN. Descartar só o do
    # Ceará deixaria o do RN entrar como se fosse município — e ele tem
    # nascimentos, então o painel ganharia uma unidade fantasma.
    df = pd.DataFrame({"CODMUNRES": [
        "230440",  # Limoeiro do Norte (CE)
        "240810",  # Mossoró (RN)
        "230000",  # ignorado CE
        "240000",  # ignorado RN
        "355030",  # São Paulo, fora das duas
    ]})
    saida = nasc.filtra_ufs(nasc.padroniza_colunas(df), ("23", "24"))
    assert list(saida["cod_ibge6"]) == ["230440", "240810"]


def test_filtra_ceara_continua_sendo_o_caso_de_uma_uf():
    # A função antiga vira caso particular da nova — se isso quebrar, todo o
    # pipeline canônico do Ceará muda sem ninguém pedir.
    df = pd.DataFrame({"CODMUNRES": ["230440", "240810", "230000"]})
    padronizado = nasc.padroniza_colunas(df)
    assert (list(nasc.filtra_ceara(padronizado)["cod_ibge6"])
            == list(nasc.filtra_ufs(padronizado, ("23",))["cod_ibge6"])
            == ["230440"])


def test_sigla_da_uf_falha_alto_em_codigo_desconhecido():
    # O pysus aceita qualquer string e devolve lista vazia: sem esta guarda,
    # um código errado viraria "UF sem nascimentos", não "você digitou errado".
    assert nasc._sigla_da_uf("24") == "RN"
    with pytest.raises(ValueError, match="SIGLA_POR_UF"):
        nasc._sigla_da_uf("99")


def test_finaliza_pam_filtra_pelo_conjunto_de_ufs_pedido():
    pedacos = [pd.DataFrame({
        "cod_ibge": ["230440", "240810", "355030"],
        "ano": [2017, 2017, 2017],
        "cultura": ["banana"] * 3,
        "area_ha": [100.0, 200.0, 300.0],
    })]
    so_ce = dose._finaliza_pam(pedacos, (2017,), ("23",))
    assert list(so_ce["cod_ibge"]) == ["230440"]
    fronteira = dose._finaliza_pam(pedacos, (2017,), ("23", "24"))
    assert list(fronteira["cod_ibge"]) == ["230440", "240810"]


def test_finaliza_pam_nomeia_as_ufs_quando_o_filtro_esvazia():
    # A mensagem antiga dizia "filtro CE/anos" mesmo num recorte de duas UFs.
    pedacos = [pd.DataFrame({
        "cod_ibge": ["355030"], "ano": [2017],
        "cultura": ["banana"], "area_ha": [1.0],
    })]
    with pytest.raises(RuntimeError, match="23,24"):
        dose._finaliza_pam(pedacos, (2017,), ("23", "24"))


# --------------------------------------------------------------------------
# Gate da Rota 1 (script 14)
#
# A regra que estes testes existem para travar: **'ausente' não é '✘'**.
# Bloqueio de rede tem de produzir "não verificado", nunca "verificado e
# reprovado" — as duas coisas pedem ações opostas, e confundi-las já produziu
# conclusão substantiva errada neste repositório (a truncagem do bucket GAEZ).
# --------------------------------------------------------------------------

def test_veredito_ausente_em_G1_domina_mesmo_com_o_resto_aprovado():
    # G2 e G3 ✔ com G1 ausente NÃO é aprovação: é ignorância sobre a única
    # coisa que estava em dúvida.
    r = [{"gate": "G1_aeronave", "veredito": "ausente"},
         {"gate": "G2_melao", "veredito": "✔"},
         {"gate": "G3_registro", "veredito": "✔"}]
    assert gate.veredito_agregado(r) == "ausente"


def test_veredito_reprova_a_rota_quando_o_vizinho_nao_tinha_aeronave():
    r = [{"gate": "G1_aeronave", "veredito": "✘"},
         {"gate": "G2_melao", "veredito": "✔"},
         {"gate": "G3_registro", "veredito": "✔"}]
    assert gate.veredito_agregado(r).startswith("✘")


def test_veredito_aprova_so_com_os_tres_verdes():
    r = [{"gate": "G1_aeronave", "veredito": "✔"},
         {"gate": "G2_melao", "veredito": "✔"},
         {"gate": "G3_registro", "veredito": "✔"}]
    assert gate.veredito_agregado(r) == "✔"
    r[1]["veredito"] = "✘"
    assert gate.veredito_agregado(r) == "⚠ com ressalva"
    r[1]["veredito"] = "ausente"
    assert gate.veredito_agregado(r) == "⚠ parcial"


def test_suporte_por_cultura_separa_as_ufs_e_ignora_area_zero():
    medias = pd.DataFrame({
        "cod_ibge": ["230440", "230970", "240810", "241170", "355030"],
        "cultura": ["melão"] * 5,
        "area_ha": [10.0, 0.0, 50.0, 30.0, 999.0],  # zero não conta; SP fica fora
    })
    t = gate.suporte_por_cultura(medias, ("23", "24"))
    assert t.loc["melão", "23"] == 1      # só Limoeiro tem área > 0
    assert t.loc["melão", "24"] == 2
    assert t.loc["melão", "total"] == 3


def test_gate_melao_vira_verde_quando_a_ampliacao_fecha_o_suporte():
    # O encerramento do melão no Gate 1 foi condicional à amostra só-Ceará.
    # Com poucos municípios continua ✘; com muitos, o suporte fecha.
    poucos = pd.DataFrame({
        "cod_ibge": ["230440", "240810"], "cultura": ["melão"] * 2,
        "area_ha": [10.0, 20.0],
    })
    assert gate.gate_melao(poucos, "24")["veredito"] == "✘"

    muitos = pd.DataFrame({
        "cod_ibge": [f"23{i:04d}" for i in range(20)] + [f"24{i:04d}" for i in range(20)],
        "cultura": ["melão"] * 40, "area_ha": [10.0] * 40,
    })
    saida = gate.gate_melao(muitos, "24")
    assert saida["veredito"] == "✔"
    assert saida["municipios_melao_ce"] == 20
    assert saida["municipios_melao_total"] == 40


def test_gate_melao_sem_pam_devolve_ausente_e_nao_reprovacao():
    assert gate.gate_melao(None, "24")["veredito"] == "ausente"
    assert gate.gate_melao(pd.DataFrame(), "24")["veredito"] == "ausente"


def test_gate_registro_compara_peso_medio_entre_ufs():
    painel = pd.DataFrame({
        "cod_ibge6": ["230440", "230440", "240810", "240810"],
        "n_nascimentos": [100, 100, 100, 100],
        "peso_medio": [3200.0, 3200.0, 3210.0, 3210.0],
    })
    saida = gate.gate_registro(painel, "24")
    assert saida["veredito"] == "✔"
    assert saida["delta_peso_g"] == pytest.approx(-10.0)

    # Diferença grande de nível reprova a TRIAGEM (não a identificação).
    painel.loc[painel["cod_ibge6"] == "240810", "peso_medio"] = 3000.0
    assert gate.gate_registro(painel, "24")["veredito"] == "✘"


def test_gate_registro_exige_as_duas_ufs_no_painel():
    # Painel só-Ceará não reprova o vizinho: ele não o observou.
    painel = pd.DataFrame({
        "cod_ibge6": ["230440"], "n_nascimentos": [100], "peso_medio": [3200.0],
    })
    saida = gate.gate_registro(painel, "24")
    assert saida["veredito"] == "ausente"
    assert "não tem as duas UFs" in saida["detalhe"]


def test_gate_recusa_o_ceara_como_vizinho():
    # --vizinho 23 compararia o Ceará consigo mesmo e devolveria zero por
    # construção, sem nada acusar.
    assert gate.main(["--vizinho", "23"]) == 1
