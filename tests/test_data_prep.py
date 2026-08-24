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


def _carrega(nome: str):
    caminho = RAIZ / "scripts" / "data_prep" / nome
    spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


dose = _carrega("01_check_dose_variation.py")
nasc = _carrega("02_clean_births.py")
fetal = _carrega("03_clean_fetal_deaths.py")


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
    df = pd.DataFrame({"CODMUNRES": ["230440", "355030", "239001", "292740"]})
    saida = nasc.filtra_ceara(nasc.padroniza_colunas(df))
    assert list(saida["cod_ibge6"]) == ["230440", "239001"]


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
