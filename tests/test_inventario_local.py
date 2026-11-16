"""Testes do script 19 — inventário local de SINASC e SIM. Sem rede."""

import importlib.util
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "inventario", RAIZ / "scripts" / "data_prep" / "19_inventario_local.py")
inv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(inv)


def test_classifica_nomes_do_datasus():
    assert inv.classifica("DNCE2019.dbc") == ("sinasc", "CE", 2019)
    assert inv.classifica("dnrn2005.DBC") == ("sinasc", "RN", 2005)
    assert inv.classifica("DOFET19.dbc") == ("dofet", "BR", 2019)
    assert inv.classifica("DOFET05.parquet") == ("dofet", "BR", 2005)
    assert inv.classifica("DOCE2019.dbc") == ("do_uf", "CE", 2019)
    assert inv.classifica("DNRN2019.dbc.parte") == ("sinasc", "RN", 2019)
    assert inv.classifica("leia-me.txt") is None


def _cria(pasta, nome, n=10):
    (pasta / nome).write_bytes(b"x" * n)


def test_falta_incompleto_e_ok(tmp_path):
    _cria(tmp_path, "DNCE2019.dbc")
    _cria(tmp_path, "DNRN2019.dbc.parte")
    _cria(tmp_path, "DOFET19.dbc", n=0)
    linhas = inv.confronta(inv.varre([tmp_path]), ["CE", "RN"], range(2019, 2021))
    sit = {l["nome"]: l["situacao"] for l in linhas}
    assert sit["DNCE2019.DBC"] == "ok"
    assert sit["DNRN2019.DBC"] == "INCOMPLETO"
    assert sit["DOFET19.DBC"] == "INCOMPLETO"
    assert sit["DNCE2020.DBC"] == "FALTA"


def test_tamanho_diferente_do_ftp_e_ausente_no_ftp(tmp_path):
    _cria(tmp_path, "DNCE2019.dbc", n=10)
    ftp = {"DNCE2019.DBC": 99}
    linhas = inv.confronta(inv.varre([tmp_path]), ["CE"], range(2019, 2021), ftp, {})
    sit = {l["nome"]: l["situacao"] for l in linhas}
    assert sit["DNCE2019.DBC"] == "TAMANHO DIFERE DO FTP"
    assert sit["DNCE2020.DBC"] == "NAO EXISTE NO FTP"


def test_comandos_so_para_o_que_falta(tmp_path):
    _cria(tmp_path, "DNCE2019.dbc")
    linhas = inv.confronta(inv.varre([tmp_path]), ["CE", "RN"], range(2019, 2020))
    cmds = inv.comandos(linhas)
    assert any("--ufs 24 --anos 2019" in c for c in cmds)
    assert any("03_clean_fetal_deaths.py" in c and "2019" in c for c in cmds)


def test_relatorio_nao_expoe_caminho_externo(tmp_path):
    _cria(tmp_path, "DNCE2019.dbc")
    achados = inv.varre([tmp_path])
    linhas = inv.confronta(achados, ["CE"], range(2019, 2020))
    texto = inv.relatorio(linhas, achados, [tmp_path], False)
    assert str(tmp_path.parent) not in texto
