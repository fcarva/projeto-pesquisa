"""E16 — Censo Demográfico 2022 via censobr: comparabilidade estrutural CE × vizinho.

POR QUE ESTE SCRIPT EXISTE
--------------------------

O gate da Rota 1 (`14_gate_fronteira.py`) tem um G3 que compara **peso ao
nascer** entre as UFs — e peso exige SINASC. Antes de qualquer desfecho, porém,
há uma pergunta mais barata e anterior: **os municípios dos dois lados da linha
são o mesmo tipo de lugar?** Água, esgoto, dependência de poço. Se não forem,
nenhum paralelismo de tendência vai parecer plausível na banca.

O Censo responde isso, e o **censobr** (IPEA) o entrega por setor censitário em
parquet, hospedado em **GitHub Releases**. Isso importa operacionalmente: é uma
rota de dados que passou pelo proxy da sessão remota quando SIDRA, DATASUS e
servicodados estavam todos bloqueados (conferido em 2026-09-22: HTTP 200, 115 MB,
Parquet válido). Na máquina local a rede do IBGE funciona — ver
`docs/fontes-e-vintages.md` —, mas o censobr continua sendo a via mais curta
para o Censo por setor.

> Pereira, R. H. M. & Barbosa, R. J. (2023). *censobr: Download Data from
> Brazil's Population Census.* Pacote R, IPEA. doi:10.32614/CRAN.package.censobr
> (citação oficial do `inst/CITATION`). Dados: `github.com/ipea/censobr_prep_data`,
> release `v1.0.0`.

OS GRUPOS SÃO DEFINIDOS DE FORA
-------------------------------

Nenhum grupo aqui foi escolhido olhando dado. Todos vêm de delimitação externa,
anterior e independente do desfecho:

- **CE — Região Geográfica Imediata Russas–Limoeiro do Norte** (IBGE, 230007).
  Contém Limoeiro do Norte e Quixeré, os dois municípios que concentram 27 das
  36 aeronaves do Censo Agro 2006.
- **RN — Região Geográfica Imediata de Mossoró** (IBGE, 240009).
- **RN — RIDE da Chapada do Apodi** (PLP 98/07, Câmara dos Deputados): os 21
  municípios potiguares nomeados no projeto. ⚠️ É PLP aprovado em comissão, não
  RIDE instituída — delimitação documentada, não entidade jurídica. Os 9
  municípios cearenses da mesma RIDE **não** estão listados na fonte obtida.

⚠️ O QUE ESTE SCRIPT NÃO FAZ
-----------------------------

- **Não testa paralelismo.** Compara NÍVEIS. Diferença de nível é absorvida pelo
  efeito fixo de município; o que invalidaria o DiD é diferença de TENDÊNCIA, e
  um corte transversal não a mede. Isto é triagem, e dizer aqui impede que um
  "comparável" vire licença.
- **Não é pré-período.** O Censo é de **2022**, três anos depois do ban.
  Infraestrutura de água e esgoto dificilmente responde a uma proibição de
  pulverização aérea em três anos, mas o Censo 2010 é que seria o corte limpo —
  pendente, porque os códigos de variável de 2010 são outros e o dicionário de
  2010 é PDF.
- **Não mexe no painel do Ensaio 1.** Grava artefato próprio, com sufixo de UF.

Uso:
    python scripts/data_prep/15_censo_demografico.py                  # CE x RN
    python scripts/data_prep/15_censo_demografico.py --ufs 23 22      # CE x PI
    python scripts/data_prep/15_censo_demografico.py --verificar-dicionario

Saídas (gitignored):
    data/raw/censobr/2022_tracts_domicilio_v1.0.0.parquet           (cache, ~115 MB)
    data/processed/censo2022_domicilios_muni__uf23-24.parquet
    data/processed/censo2022_comparabilidade__uf23-24.csv
"""

from __future__ import annotations

import argparse
import sys
import urllib.request as urlreq
from datetime import date
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
RAW_DIR = RAIZ / "data" / "raw" / "censobr"
OUT_DIR = RAIZ / "data" / "processed"

URL_BASE = "https://github.com/ipea/censobr_prep_data/releases/download"
RELEASE = "v1.0.0"
UFS_PADRAO = ("23", "24")

# ⚠️ Códigos decodificados do dicionário OFICIAL do censobr
# (`censo_docs/2022_dictionary_tracts.xlsx`, aba `Domicilios`), em 2026-09-22.
# O valor é um trecho que TEM de aparecer na descrição — é o que
# `verifica_dicionario` confere. Um código errado aqui não dá erro: dá uma
# coluna de outra coisa com nome certo, que é a pior forma de erro.
VARIAVEIS_2022 = {
    "domicilio01_V00001": ("dppo", "Domicílios Particulares Permanentes Ocupados"),
    # abastecimento de água — forma principal
    "domicilio02_V00111": ("agua_rede_geral", "rede geral de distribuição"),
    "domicilio02_V00112": ("agua_poco_profundo", "poço profundo ou artesiano"),
    "domicilio02_V00113": ("agua_poco_raso", "poço raso, freático ou cacimba"),
    "domicilio02_V00114": ("agua_fonte", "fonte, nascente ou mina"),
    "domicilio02_V00115": ("agua_carro_pipa", "carro-pipa"),
    "domicilio02_V00116": ("agua_chuva", "água da chuva armazenada"),
    "domicilio02_V00117": ("agua_rio_acude", "rios, açudes"),
    "domicilio02_V00118": ("agua_outra", "outra forma de abastecimento de água"),
    # destinação do esgoto
    "domicilio02_V00309": ("esg_rede", "rede geral ou pluvial"),
    "domicilio02_V00310": ("esg_fossa_ligada", "fossa séptica ou fossa filtro ligada à rede"),
    "domicilio02_V00311": ("esg_fossa_nao_ligada", "não ligada à rede"),
    "domicilio02_V00312": ("esg_fossa_rudimentar", "fossa rudimentar ou buraco"),
    "domicilio02_V00313": ("esg_vala", "vala"),
    "domicilio02_V00314": ("esg_rio_lago", "rio, lago, córrego ou mar"),
    "domicilio02_V00315": ("esg_outra", "outra forma"),
    "domicilio02_V00316": ("esg_sem_banheiro", "não tinham banheiro nem sanitário"),
}
AGUA = [v[0] for k, v in VARIAVEIS_2022.items() if v[0].startswith("agua_")]
ESGOTO = [v[0] for k, v in VARIAVEIS_2022.items() if v[0].startswith("esg_")]
GEO = ["code_state", "code_muni", "name_muni", "code_immediate", "name_immediate"]

# Grupos de comparação — delimitação EXTERNA. Ver docstring.
RI_RUSSAS_LIMOEIRO = 230007
RI_MOSSORO = 240009
RIDE_CHAPADA_RN = frozenset({
    2400307, 2400703, 2401008, 2401107, 2400208, 2401453, 2402303,
    2402501, 2403707, 2404101, 2404309, 2404408, 2404507, 2404705,
    2407203, 2408003, 2409902, 2410256, 2413359, 2411056, 2414605,
})
MUNICIPIOS_AERONAVE_CE = frozenset({2307601, 2311504})  # Limoeiro do Norte, Quixeré

# Abaixo disto a soma das categorias não fecha no total de domicílios, e a
# fração calculada deixa de significar o que o nome diz.
FECHAMENTO_MINIMO = 0.97


def url_setores(ano: int, dataset: str, release: str = RELEASE) -> str:
    """URL do parquet por setor no censobr — a mesma que `read_tracts()` monta."""
    return f"{URL_BASE}/{release}/{ano}_tracts_{dataset.lower()}_{release}.parquet"


def url_dicionario(ano: int) -> str:
    extensao = "xlsx" if ano == 2022 else "pdf"
    return f"{URL_BASE}/censo_docs/{ano}_dictionary_tracts.{extensao}"


def baixa(url: str, destino: Path, timeout: int = 600) -> Path:
    """Baixa para `destino` se ainda não existir. Falha ALTO, nunca devolve vazio.

    ⚠️ Arquivo parcial de download interrompido é o risco real aqui: 115 MB por
    proxy. Grava em `.parte` e só renomeia quando termina, para que um cache
    truncado nunca seja lido como se estivesse completo.
    """
    if destino.exists() and destino.stat().st_size > 0:
        return destino
    destino.parent.mkdir(parents=True, exist_ok=True)
    parte = destino.with_suffix(destino.suffix + ".parte")
    requisicao = urlreq.Request(url, headers={"User-Agent": "projeto-pesquisa/1.0"})
    with urlreq.urlopen(requisicao, timeout=timeout) as resposta, open(parte, "wb") as fh:
        while True:
            bloco = resposta.read(1 << 20)
            if not bloco:
                break
            fh.write(bloco)
    parte.rename(destino)
    return destino


def verifica_dicionario(linhas_domicilios) -> list[str]:
    """Confere cada código de `VARIAVEIS_2022` contra a descrição oficial.

    Recebe as linhas da aba `Domicilios` (qualquer iterável de tuplas em que a
    posição 3 é o código original e a 5 é a descrição). Devolve a lista de
    divergências — vazia quando tudo confere.
    """
    descricao = {}
    for linha in linhas_domicilios:
        if len(linha) > 5 and linha[3]:
            descricao[str(linha[3]).strip()] = str(linha[5])
    problemas = []
    for coluna, (_, trecho) in VARIAVEIS_2022.items():
        codigo = coluna.split("_", 1)[1]
        if codigo not in descricao:
            problemas.append(f"{codigo}: ausente do dicionário")
        elif trecho.lower() not in descricao[codigo].lower():
            problemas.append(f"{codigo}: esperava '{trecho}', dicionário diz "
                             f"'{descricao[codigo][:90]}'")
    return problemas


def le_setores(caminho: Path, ufs) -> pd.DataFrame:
    """Lê só as colunas e UFs necessárias — o arquivo nacional tem 699 colunas."""
    import pyarrow.parquet as pq

    colunas = GEO + list(VARIAVEIS_2022)
    tabela = pq.read_table(caminho, columns=colunas,
                           filters=[("code_state", "in", [int(u) for u in ufs])])
    df = tabela.to_pandas().rename(columns={k: v[0] for k, v in VARIAVEIS_2022.items()})
    return df


def agrega_municipio(setores: pd.DataFrame) -> pd.DataFrame:
    """Soma setores em municípios. Valor ausente no setor vira zero.

    ⚠️ O IBGE suprime células pequenas por sigilo; zero aqui significa "não
    informado no setor", não "nenhum domicílio". É por isso que o fechamento é
    conferido depois, e não suposto.
    """
    numericas = ["dppo"] + AGUA + ESGOTO
    df = setores.copy()
    df[numericas] = df[numericas].apply(pd.to_numeric, errors="coerce").fillna(0)
    chaves = ["code_state", "code_muni", "name_muni", "code_immediate", "name_immediate"]
    municipios = df.groupby(chaves, as_index=False)[numericas].sum()
    for chave in ("code_state", "code_muni", "code_immediate"):
        municipios[chave] = municipios[chave].astype("int64")
    return municipios


def fechamento(municipios: pd.DataFrame) -> dict[str, float]:
    """Que fração do total de domicílios as categorias cobrem, por bloco."""
    total = municipios["dppo"].sum()
    return {
        "agua": float(municipios[AGUA].sum(axis=1).sum() / total),
        "esgoto": float(municipios[ESGOTO].sum(axis=1).sum() / total),
    }


def indicadores(grupo: pd.DataFrame) -> dict[str, float]:
    """Frações do grupo — ponderadas por domicílio E média municipal simples.

    As duas entram de propósito. A ponderada descreve onde as pessoas moram; a
    média municipal descreve a UNIDADE DO DiD, que é o município. Num grupo com
    uma cidade grande (Mossoró), as duas divergem, e a divergência é informação.
    """
    total = grupo["dppo"].sum()
    poco = grupo["agua_poco_profundo"] + grupo["agua_poco_raso"]
    adequado = grupo["esg_rede"] + grupo["esg_fossa_ligada"]
    return {
        "n_municipios": float(len(grupo)),
        "domicilios": float(total),
        "rede_geral": grupo["agua_rede_geral"].sum() / total,
        "poco": poco.sum() / total,
        "poco_media_municipal": (poco / grupo["dppo"]).mean(),
        "carro_pipa": grupo["agua_carro_pipa"].sum() / total,
        "esgoto_adequado": adequado.sum() / total,
        "fossa_rudimentar": grupo["esg_fossa_rudimentar"].sum() / total,
        "sem_banheiro": grupo["esg_sem_banheiro"].sum() / total,
    }


def grupos_de_comparacao(municipios: pd.DataFrame) -> dict[str, pd.Series]:
    m = municipios
    return {
        "CE estado": m["code_state"] == 23,
        "RN estado": m["code_state"] == 24,
        "CE: RI Russas–Limoeiro": m["code_immediate"] == RI_RUSSAS_LIMOEIRO,
        "RN: RI Mossoró": m["code_immediate"] == RI_MOSSORO,
        "RN: RIDE Chapada (PLP 98/07)": m["code_muni"].isin(RIDE_CHAPADA_RN),
        "CE: Limoeiro + Quixeré": m["code_muni"].isin(MUNICIPIOS_AERONAVE_CE),
    }


def tabela_comparacao(municipios: pd.DataFrame) -> pd.DataFrame:
    linhas = {}
    for rotulo, mascara in grupos_de_comparacao(municipios).items():
        grupo = municipios[mascara]
        if grupo.empty:
            continue  # UF fora do recorte pedido: o grupo simplesmente não existe
        linhas[rotulo] = indicadores(grupo)
    return pd.DataFrame(linhas).T


def sufixo_das_ufs(ufs) -> str:
    return "__uf" + "-".join(sorted(ufs))


def imprime(tabela: pd.DataFrame, fecha: dict[str, float]) -> None:
    barra = "=" * 96
    print(barra)
    print("CENSO 2022 (censobr) — comparabilidade ESTRUTURAL, níveis, não tendências")
    print(barra)
    print(f"  fechamento: água {fecha['agua']:.1%} | esgoto {fecha['esgoto']:.1%} "
          f"(mínimo {FECHAMENTO_MINIMO:.0%})")
    print()
    cabecalho = (f"  {'grupo':<30}{'mun':>5}{'rede':>8}{'poço':>8}{'poço/mun':>10}"
                 f"{'pipa':>7}{'esg.ok':>8}{'rudim.':>8}")
    print(cabecalho)
    for rotulo, r in tabela.iterrows():
        print(f"  {rotulo:<30}{int(r['n_municipios']):>5}{r['rede_geral']:>8.1%}"
              f"{r['poco']:>8.1%}{r['poco_media_municipal']:>10.1%}"
              f"{r['carro_pipa']:>7.1%}{r['esgoto_adequado']:>8.1%}"
              f"{r['fossa_rudimentar']:>8.1%}")
    print(barra)
    print("  ⚠️ Níveis, não tendências: o efeito fixo de município absorve diferença")
    print("     de nível. Isto é triagem de plausibilidade, não teste de paralelismo.")
    print("  ⚠️ 2022 é pós-ban. O corte limpo seria o Censo 2010 (pendente).")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--ufs", nargs="+", default=list(UFS_PADRAO), metavar="COD")
    p.add_argument("--cache", type=Path, default=RAW_DIR)
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    p.add_argument("--setores", type=Path, default=None,
                   help="Parquet já baixado (pula o download).")
    p.add_argument("--verificar-dicionario", action="store_true",
                   help="Baixa o dicionário oficial e confere os códigos (exige openpyxl).")
    args = p.parse_args(argv)
    ufs = tuple(str(u).strip() for u in args.ufs)

    if args.verificar_dicionario:
        try:
            import openpyxl
        except ImportError:
            print("[erro] --verificar-dicionario exige openpyxl (pip install openpyxl).")
            return 1
        caminho = baixa(url_dicionario(2022), args.cache / "2022_dictionary_tracts.xlsx")
        planilha = openpyxl.load_workbook(caminho, read_only=True)["Domicilios"]
        problemas = verifica_dicionario(planilha.iter_rows(values_only=True))
        if problemas:
            print("✘ CÓDIGOS DIVERGEM DO DICIONÁRIO — nada foi calculado:")
            for problema in problemas:
                print("   ", problema)
            return 1
        print(f"✔ {len(VARIAVEIS_2022)} códigos conferidos contra o dicionário oficial.")

    try:
        setores_pq = args.setores or baixa(
            url_setores(2022, "domicilio"),
            args.cache / f"2022_tracts_domicilio_{RELEASE}.parquet",
        )
    except Exception as erro:  # noqa: BLE001
        print(f"✘ download do censobr falhou: {type(erro).__name__}: {erro}")
        print("  A rota é github.com/ipea/censobr_prep_data/releases — confira a rede.")
        return 2

    municipios = agrega_municipio(le_setores(setores_pq, ufs))
    fecha = fechamento(municipios)
    if min(fecha.values()) < FECHAMENTO_MINIMO:
        print(f"✘ fechamento abaixo de {FECHAMENTO_MINIMO:.0%}: {fecha}. As frações "
              "não significariam o que o nome diz — nada foi gravado.")
        return 1

    tabela = tabela_comparacao(municipios)
    imprime(tabela, fecha)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    sufixo = sufixo_das_ufs(ufs)
    municipios = municipios.assign(fonte=f"censobr {RELEASE}",
                                   extraido_em=date.today().isoformat())
    municipios.to_parquet(args.out_dir / f"censo2022_domicilios_muni{sufixo}.parquet",
                          index=False)
    saida = tabela.reset_index(names="grupo").assign(
        fonte=f"censobr {RELEASE}", extraido_em=date.today().isoformat())
    destino = args.out_dir / f"censo2022_comparabilidade{sufixo}.csv"
    saida.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
