"""E19 — Inventário local: o que já foi baixado de SINASC e SIM, e o que falta.

POR QUE ESTE SCRIPT EXISTE
--------------------------

Os microdados não são versionados (`data/` está no .gitignore) e a sessão em
nuvem não os enxerga. Antes de montar o painel do desenho de fronteira é preciso
saber, **na máquina do pesquisador**, se os arquivos estão todos lá.

O desenho novo (docs/pre-especificacao-v2.md) pede:

- **SINASC**, declarações de nascido vivo: `DN{UF}{AAAA}.dbc` para Ceará (CE) e
  Rio Grande do Norte (RN), de 2005 a 2024.
- **SIM, óbito fetal**: `DOFET{AA}.dbc`, de 2005 a 2024. O arquivo é NACIONAL
  (não há `DOFETCE`); o recorte por UF é feito depois, pela residência.

O script não lê o conteúdo dos arquivos nem depende de pandas: só nomes,
tamanhos e datas. Roda com o Python do sistema.

    python scripts/data_prep/19_inventario_local.py
    python scripts/data_prep/19_inventario_local.py --conferir-ftp
    python scripts/data_prep/19_inventario_local.py --conferir-ftp --salvar
    python scripts/data_prep/19_inventario_local.py --pasta "D:/datasus" --pasta ~/Downloads

`--conferir-ftp` lista os diretórios do DATASUS (porta 21) e compara o tamanho
de cada arquivo local com o do servidor: arquivo menor que o do servidor é
download interrompido. `--salvar` grava o relatório em
`docs/inventario-local.md`, que só tem nomes e tamanhos e pode ser commitado
para a sessão em nuvem ler.

Código de saída: 0 se nada falta; 1 se falta algo ou há arquivo suspeito.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
FTP_HOST = "ftp.datasus.gov.br"
FTP_SINASC = "/dissemin/publicos/SINASC/1996_/Dados/DNRES"
FTP_DOFET = "/dissemin/publicos/SIM/CID10/DOFET"

UFS_PADRAO = ("CE", "RN")
ANOS_PADRAO = tuple(range(2005, 2025))
EXTENSOES = (".dbc", ".dbf", ".parquet", ".csv", ".csv.gz")

RE_SINASC = re.compile(r"^DN([A-Z]{2})(\d{4})$")
RE_DOFET = re.compile(r"^DOFET(\d{2})$")
RE_DO_UF = re.compile(r"^DO([A-Z]{2})(\d{4})$")


def _radical(nome: str) -> tuple[str, str]:
    """Separa 'DNCE2019.dbc' em ('DNCE2019', '.dbc'). Trata '.csv.gz' e '.parte'."""
    parte = nome.lower().endswith(".parte")
    if parte:  # download interrompido: 'DNRN2019.dbc.parte'
        nome = nome[: -len(".parte")]
    baixo = nome.lower()
    for ext in (".csv.gz",) + tuple(e for e in EXTENSOES if e != ".csv.gz"):
        if baixo.endswith(ext):
            return nome[: -len(ext)].upper(), ".parte" if parte else ext
    return nome.upper(), ".parte" if parte else ""


def classifica(nome: str) -> tuple[str, str, int] | None:
    """Devolve (base, uf, ano) para arquivo reconhecido, ou None.

    base: 'sinasc', 'dofet' ou 'do_uf' (o DO estadual NÃO traz óbito fetal).
    """
    radical, _ = _radical(nome)
    radical = radical.split("__")[0]
    m = RE_SINASC.match(radical)
    if m:
        return "sinasc", m.group(1), int(m.group(2))
    m = RE_DOFET.match(radical)
    if m:
        aa = int(m.group(1))
        return "dofet", "BR", 2000 + aa if aa < 80 else 1900 + aa
    m = RE_DO_UF.match(radical)
    if m:
        return "do_uf", m.group(1), int(m.group(2))
    return None


def varre(pastas: list[Path]) -> list[dict]:
    achados = []
    for pasta in pastas:
        if not pasta.exists():
            continue
        for caminho in sorted(pasta.rglob("*")):
            if not caminho.is_file():
                continue
            chave = classifica(caminho.name)
            if chave is None:
                continue
            st = caminho.stat()
            _, ext = _radical(caminho.name)
            achados.append({
                "base": chave[0], "uf": chave[1], "ano": chave[2],
                "caminho": caminho, "ext": ext, "bytes": st.st_size,
                "modificado": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d"),
                "incompleto": ext == ".parte" or st.st_size == 0,
            })
    return achados


def lista_ftp(diretorio: str, timeout: int = 60) -> dict[str, int]:
    """Nome em maiúsculas -> tamanho em bytes, para um diretório do DATASUS."""
    from ftplib import FTP

    tamanhos: dict[str, int] = {}
    with FTP(FTP_HOST, timeout=timeout) as ftp:
        ftp.login()
        ftp.cwd(diretorio)
        linhas: list[str] = []
        ftp.retrlines("LIST", linhas.append)
    for linha in linhas:
        partes = linha.split()
        if len(partes) < 4:
            continue
        nome = partes[-1]
        if linha[:1] in "-dl" and len(partes) >= 9:
            # Formato Unix: permissões, links, dono, grupo, TAMANHO, data..., nome.
            if partes[4].isdigit():
                tamanhos[nome.upper()] = int(partes[4])
            continue
        # Formato DOS, que é o do DATASUS: data, hora, tamanho, nome.
        numeros = [p for p in partes[:-1] if p.isdigit()]
        if numeros:
            tamanhos[nome.upper()] = int(numeros[-1])
    return tamanhos


def esperado(ufs, anos) -> list[tuple[str, str, int, str]]:
    """(base, uf, ano, nome no FTP) de tudo o que o desenho pede."""
    itens = [("sinasc", uf, ano, f"DN{uf}{ano}.DBC") for uf in ufs for ano in anos]
    itens += [("dofet", "BR", ano, f"DOFET{ano % 100:02d}.DBC") for ano in anos]
    return itens


def confronta(achados, ufs, anos, ftp_sinasc=None, ftp_dofet=None) -> list[dict]:
    indice: dict[tuple, list[dict]] = {}
    for a in achados:
        indice.setdefault((a["base"], a["uf"], a["ano"]), []).append(a)
    linhas = []
    for base, uf, ano, nome_ftp in esperado(ufs, anos):
        locais = indice.get((base, uf, ano), [])
        bons = [a for a in locais if not a["incompleto"]]
        ftp = ftp_sinasc if base == "sinasc" else ftp_dofet
        no_ftp = None if ftp is None else ftp.get(nome_ftp)
        if not locais:
            situacao = "FALTA"
            if ftp is not None and no_ftp is None:
                situacao = "NAO EXISTE NO FTP"
        elif not bons:
            situacao = "INCOMPLETO"
        else:
            situacao = "ok"
            dbc = [a for a in bons if a["ext"] == ".dbc"]
            if no_ftp is not None and dbc and all(a["bytes"] != no_ftp for a in dbc):
                situacao = "TAMANHO DIFERE DO FTP"
        linhas.append({"base": base, "uf": uf, "ano": ano, "nome": nome_ftp,
                       "situacao": situacao, "locais": locais, "bytes_ftp": no_ftp})
    return linhas


def _mb(b: int | None) -> str:
    return "—" if b is None else f"{b / 1e6:.1f}"


def _onde(caminho: Path) -> str:
    """Caminho relativo ao repositório; fora dele, só o nome da pasta e do arquivo.

    O relatório pode ser commitado: não deve carregar o caminho completo de uma
    pasta pessoal.
    """
    if caminho.is_relative_to(RAIZ):
        return str(caminho.relative_to(RAIZ))
    return f"(fora do repositório) {caminho.parent.name}/{caminho.name}"


def relatorio(linhas, achados, pastas, usou_ftp: bool) -> str:
    out = [f"# Inventário local de SINASC e SIM — {datetime.now():%Y-%m-%d %H:%M}", ""]
    out.append("Pastas varridas: " + ", ".join(
        f"`{p.relative_to(RAIZ)}`" if p.is_relative_to(RAIZ) else f"`(externa) {p.name}`"
        for p in pastas))
    out.append(f"Conferência com o FTP do DATASUS: {'sim' if usou_ftp else 'não'}")
    out.append("")
    for base, titulo in (("sinasc", "SINASC (nascidos vivos)"), ("dofet", "SIM, óbito fetal (DOFET, nacional)")):
        sel = [l for l in linhas if l["base"] == base]
        ok = sum(l["situacao"] == "ok" for l in sel)
        out.append(f"## {titulo}: {ok} de {len(sel)} arquivos em ordem")
        out.append("")
        out.append("| arquivo | situação | local (MB) | FTP (MB) | onde está |")
        out.append("|---|---|---|---|---|")
        for l in sel:
            locais = l["locais"]
            tam = ", ".join(_mb(a["bytes"]) for a in locais) or "—"
            onde = ", ".join(f"`{_onde(a['caminho'])}`" for a in locais) or "—"
            out.append(f"| {l['nome']} | {l['situacao']} | {tam} | {_mb(l['bytes_ftp'])} | {onde} |")
        out.append("")
    extras = [a for a in achados if a["base"] == "do_uf"]
    if extras:
        out.append(f"## DO estadual encontrado ({len(extras)} arquivos)")
        out.append("")
        out.append("⚠️ O `DO{UF}{ano}` é o registro geral de óbitos e **não traz óbito "
                   "fetal** (TIPOBITO = 2 em todas as linhas). Para o desfecho de perda "
                   "fetal o arquivo é o `DOFET{AA}`, nacional.")
        out.append("")
    return "\n".join(out)


def comandos(linhas) -> list[str]:
    """Comandos para baixar o que falta, agrupados por base."""
    cmds = []
    ruins = [l for l in linhas if l["situacao"] in {"FALTA", "INCOMPLETO", "TAMANHO DIFERE DO FTP"}]
    anos_sinasc = sorted({l["ano"] for l in ruins if l["base"] == "sinasc"})
    ufs_sinasc = sorted({l["uf"] for l in ruins if l["base"] == "sinasc"})
    cod = {"CE": "23", "RN": "24", "PI": "22", "PB": "25", "PE": "26"}
    if anos_sinasc:
        cmds.append("python scripts/data_prep/02_clean_births.py --fonte ftp --ufs "
                    + " ".join(cod.get(u, u) for u in ufs_sinasc)
                    + " --anos " + " ".join(map(str, anos_sinasc)))
    anos_dofet = sorted({l["ano"] for l in ruins if l["base"] == "dofet"})
    if anos_dofet:
        cmds.append("python scripts/data_prep/03_clean_fetal_deaths.py --fonte dofet --anos "
                    + " ".join(map(str, anos_dofet)))
    return cmds


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pasta", type=Path, action="append", default=[],
                    help="Pasta adicional a varrer (pode repetir). Padrão: data/raw e data/processed.")
    ap.add_argument("--ufs", nargs="+", default=list(UFS_PADRAO))
    ap.add_argument("--anos", type=int, nargs=2, metavar=("DE", "ATE"),
                    default=[ANOS_PADRAO[0], ANOS_PADRAO[-1]])
    ap.add_argument("--conferir-ftp", action="store_true",
                    help="Compara com o FTP do DATASUS (porta 21).")
    ap.add_argument("--salvar", action="store_true",
                    help="Grava docs/inventario-local.md (só nomes e tamanhos).")
    a = ap.parse_args(argv)

    pastas = [RAIZ / "data" / "raw", RAIZ / "data" / "processed"] + [p.expanduser() for p in a.pasta]
    anos = range(a.anos[0], a.anos[1] + 1)
    achados = varre(pastas)

    ftp_sinasc = ftp_dofet = None
    if a.conferir_ftp:
        try:
            ftp_sinasc, ftp_dofet = lista_ftp(FTP_SINASC), lista_ftp(FTP_DOFET)
        except Exception as erro:  # noqa: BLE001
            print(f"[aviso] não consegui listar o FTP ({type(erro).__name__}: {erro}). "
                  "Sigo só com o inventário local.", file=sys.stderr)

    linhas = confronta(achados, [u.upper() for u in a.ufs], anos, ftp_sinasc, ftp_dofet)
    texto = relatorio(linhas, achados, pastas, ftp_sinasc is not None)
    print(texto)

    cmds = comandos(linhas)
    if cmds:
        print("## Para baixar o que falta\n")
        for c in cmds:
            print("    " + c)
        print("\n⚠️ O script 03 recorta hoje só o Ceará. O arquivo DOFET é nacional: "
              "baixe-o agora e o recorte do RN entra quando o script for estendido.")
    else:
        print("Nada falta para o desenho de fronteira (CE e RN, "
              f"{anos[0]}–{anos[-1]}).")

    if a.salvar:
        destino = RAIZ / "docs" / "inventario-local.md"
        extra = ("\n## Para baixar o que falta\n\n" + "\n".join(f"    {c}" for c in cmds) + "\n") if cmds else ""
        destino.write_text(texto + extra, encoding="utf-8")
        print(f"\ngravado: {destino.relative_to(RAIZ)}")
    return 1 if cmds else 0


if __name__ == "__main__":
    sys.exit(main())
