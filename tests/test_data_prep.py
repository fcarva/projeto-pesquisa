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


def test_sinaliza_massa_reprova_cultura_fina_e_concentrada():
    tabela = pd.DataFrame(
        {
            "cultura": ["fina", "boa"],
            "n_muni_positivo": [3, 60],
            "area_total_estado_ha": [200.0, 50_000.0],
            "share_top5_muni": [0.95, 0.25],
        }
    )
    sinal = dose.sinaliza_massa(tabela)["sinal"]
    assert "poucos municípios" in sinal.iloc[0]
    assert "área fina" in sinal.iloc[0]
    assert "concentrada" in sinal.iloc[0]
    assert sinal.iloc[1] == "OK — candidata a dose"


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
