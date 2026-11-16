"""Testes do script 18 — Censo Agro, familiar × não familiar. Sem rede."""

import importlib.util
import math
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[1]


def _carrega(nome: str, sub: str = "data_prep"):
    caminho = RAIZ / "scripts" / sub / nome
    spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


censo = _carrega("18_censo_agro_familiar.py")


def _linha_2069(cod, eq, fam, v, nome="Município - CE"):
    return {"D1C": cod, "D1N": nome, "D5C": eq, "D9C": fam, "V": v}


def _linha_6851(cod, tip, uso, v, nome="Município - CE"):
    return {"D1C": cod, "D1N": nome, "D4C": tip, "D5C": uso, "V": v}


def test_traco_e_zero_e_inibido_e_ausencia():
    assert censo.valor("-") == 0.0
    assert math.isnan(censo.valor("X"))
    assert math.isnan(censo.valor("..."))
    assert censo.valor("18") == 18.0


def test_arruma_2069_preserva_inibido_como_nan():
    linhas = [
        _linha_2069("2307601", "113450", "0", "18"),
        _linha_2069("2307601", "113450", "8864", "14"),
        _linha_2069("2307601", "113450", "8865", "X"),
        _linha_2069("2311504", "113450", "0", "-"),
    ]
    tb = censo.arruma_2069(linhas).set_index("cod_ibge7")
    assert tb.loc["2307601", "eq_aeronave_tot_2006"] == 18
    assert tb.loc["2307601", "eq_aeronave_naofam_2006"] == 14
    assert math.isnan(tb.loc["2307601", "eq_aeronave_fam_2006"])
    assert tb.loc["2311504", "eq_aeronave_tot_2006"] == 0


def test_chave_repetida_levanta():
    linhas = [_linha_2069("2307601", "113450", "0", "18")] * 2
    with pytest.raises(ValueError):
        censo.arruma_2069(linhas)


def test_uf_ausente_levanta():
    tb = censo.arruma_2069([_linha_2069("2307601", "113450", "0", "18")])
    with pytest.raises(RuntimeError):
        censo.confere_ufs(tb, ["23", "24"])


def test_razao_sobre_zero_fica_ausente():
    t06 = censo.arruma_2069([_linha_2069("2400000", "113450", "0", "-")])
    t17 = censo.arruma_6851([
        _linha_6851("2400000", "46302", "46556", "-"),
        _linha_6851("2400000", "46303", "46556", "-"),
        _linha_6851("2400000", "46304", "46556", "-"),
        _linha_6851("2400000", "46303", "111611", "-"),
        _linha_6851("2400000", "46304", "111611", "-"),
    ])
    tb = censo.deriva(t06.merge(t17.drop(columns="municipio"), on="cod_ibge7"))
    assert math.isnan(tb.loc[0, "share_naofam_estab_2017"])
    assert not tb.loc[0, "tinha_aeronave_2006"]
