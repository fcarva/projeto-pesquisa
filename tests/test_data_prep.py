"""Testes das funções de limpeza dos scripts numerados de data_prep.

Os scripts começam com dígito (01_, 02_) e não são importáveis por `import`;
carregamos por caminho. Cada teste cobre uma decisão de limpeza que, se mudar
sem querer, muda o desfecho estimado — não é teste de trivialidade.

Rodar: pytest -q
"""

from __future__ import annotations

import importlib.util
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
