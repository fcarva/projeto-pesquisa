"""Deriva o conjunto-alvo da varredura de bans municipais anteriores a 2019.

A flag 0 do `CLAUDE.md` deixou de ser hipótese em 2026-09-21: Limoeiro do Norte
proibiu a pulverização aérea pela **Lei Municipal 1.478, de 20/11/2009** — nove
anos antes da lei estadual —, e ele **está no decil superior da banana**, o
grupo tratado da cultura-âncora candidata. Ver `docs/legislacao/README.md` §1.

Isto é um defeito de painel, não uma ressalva de texto: para essa unidade a dose
medida em 2015–2018 já vem suprimida pelo próprio ban municipal, e 2015–2018
deixa de ser pré-tratamento. A pergunta que sobra é **quantos mais**.

⚠️ **Por que o alvo NÃO são os 184 municípios.** Um ban municipal num município
de dose **zero** quase não enviesa: ele já entra como não tratado, e continua
não tratado. O que morde o desenho é ban em município de dose **alta**, porque
aí o contraste pré/pós que identifica o efeito já foi parcialmente consumido
antes da janela. Varrer os 184 gasta a maior parte do esforço onde não muda
nada. A fase 1 cobre exatamente onde o viés existe; a fase 2 (os 184) é
verificação de completude e não bloqueia nada.

O conjunto-alvo é a **união do decil superior entre as culturas do PAM**, mais
os três municípios expostos de Rigotto et al. (2013). A definição de decil é a
mesma de `07_diagnose_trend_sd.py` — `ceil(n * 0,10)` sobre os de área positiva,
ordenados por área — de propósito: é ela que define `n_tratados` na tabela de
MDE, então é ela cuja contaminação importa.

⚠️ **Este script não raspa nada.** Ele só diz onde olhar. A varredura em si é
`/scrape` + `WebFetch` contra o acervo de cada câmara, e o resultado volta para
o mesmo CSV que este script semeia.

Saída: `docs/legislacao/bans-municipais-ce.csv` — **no repositório, não em
`data/`**. É tabela derivada pequena e segura, que o `CLAUDE.md` autoriza
commitar; e `data/` é gitignored, então um arquivo ali nunca chega às sessões
remotas. Essa invisibilidade já custou duas rodadas de retrabalho nesta
linhagem, e é o mesmo mecanismo que fez o script 07 ficar sem o guarda de
encoding.

O script **mescla, não sobrescreve**: linhas já preenchidas pela varredura
sobrevivem a uma nova rodada. Rodar de novo depois de mudar a cultura-âncora
acrescenta alvos sem perder trabalho feito.
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
import urllib.request
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

DIR_DADOS = Path("data/processed")
DESTINO = Path("docs/legislacao/bans-municipais-ce.csv")
NOME_PAM = "pam_ce_muni_cultura_media"
API_LOCALIDADES = (
    "https://servicodados.ibge.gov.br/api/v1/localidades/estados/23/municipios"
)

# Fração do topo que conta como "tratado". Igual à do script 07 de propósito:
# é essa definição que produz `n_tratados` na tabela de MDE, então é essa cuja
# contaminação por ban municipal importa. Mudar aqui sem mudar lá faria o
# levantamento cobrir um grupo diferente do que o poder usa.
FRACAO_DECIL = 0.10

# ⚠️ Classificação REUSADA de `01_check_dose_variation.py`, não inventada aqui:
# lá a lista `CULTURAS_CANDIDATAS` marca, em comentário, onde começam os
# "comparadores de baixa pulverização aérea". Eles entram no PAM para dar
# contraste na tabela de dispersão — não são candidatos a âncora. Um município
# que só aparece no decil de mandioca não é alvo prioritário de varredura.
#
# Isto NÃO hard-coda a cultura-âncora (o `CLAUDE.md` proíbe): não elege nenhuma,
# só ordena o trabalho. Todo município continua no CSV; a coluna `prioridade`
# diz por onde começar quando o tempo apertar.
COMPARADORES_BAIXA_PULV = ("milho", "feijão", "arroz", "sorgo", "mandioca")

# Rigotto et al. (2013) comparam três municípios expostos da Chapada do Apodi.
# Entram por construção mesmo que o decil não os pegue: são o antecedente
# epidemiológico do qual o projeto herda a hipótese, e Limoeiro já se confirmou.
RIGOTTO = {
    "230760": "Limoeiro do Norte",
    "231150": "Quixeré",
    "231180": "Russas",
}

# Vocabulário de `confianca`. ⚠️ A distinção entre as duas últimas é o ponto
# inteiro da coluna: ausência de lei no site de uma câmara NÃO é prova de
# ausência de lei — muitas não publicam acervo histórico. Colapsar as duas em
# "não há" transforma um buraco de fonte em um zero, silenciosamente.
CONFIANCA = (
    "nao_verificado",     # semeado por este script; ninguém olhou ainda
    "confirmado",         # lei achada, com número e data, em fonte primária
    "ausente_conferido",  # acervo do município conferido, e não há lei
    "inconclusivo",       # ⚠️ site fora do ar, sem acervo histórico, busca falhou
)

COLUNAS = [
    "cod_ibge6", "municipio", "prioridade", "tem_lei", "numero_lei", "data_lei",
    "ementa", "url_fonte", "data_consulta", "escopo", "confianca",
    "motivo_alvo", "area_max_ha", "rank_melhor",
    # ⚠️ Acrescentadas em 2026-09-22. Lei achada não é lei vigente: a de
    # Limoeiro (1.478/2009) foi revogada em 20/05/2010, e o registro só dizia
    # quando ela nasceu. Sem estas colunas, "confirmado" lia-se como "tratado
    # desde 2009" — e a varredura (script 09) guarda só a PRIMEIRA lei achada,
    # nunca a que a revoga.
    "data_revogacao", "fonte_revogacao",
]

# Colunas que a varredura preenche e que uma nova rodada do 08 NÃO pode apagar.
COLUNAS_DE_ACHADO = (
    "tem_lei", "numero_lei", "data_lei", "ementa", "url_fonte",
    "data_consulta", "escopo", "confianca", "data_revogacao", "fonte_revogacao",
)

# O único achado já confirmado, em fonte primária. Semeia o CSV para que a
# varredura comece com um exemplo do formato preenchido, e não de uma tabela
# vazia que não diz o que "bom" parece.
SEMENTE_CONFIRMADA = {
    "230760": {
        "tem_lei": "sim",
        "numero_lei": "1478/2009",
        "data_lei": "2009-11-20",
        "ementa": ("Dispõe sobre a proibição do uso de aeronaves nas "
                   "pulverizações de lavouras no município de Limoeiro do Norte"),
        "url_fonte": "https://www.camaralimoeirodonorte.ce.gov.br/leis/549",
        "data_consulta": "2026-09-21",
        "escopo": "total",
        "confianca": "confirmado",
        # ⚠️ Fonte SECUNDÁRIA, e dita como tal: nota da CPT (2014), reproduzida
        # pela Terra de Direitos, e o MST (2019). A lei revogadora ainda não
        # foi localizada no acervo da Câmara — ver docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md §5.
        "data_revogacao": "2010-05-20",
        "fonte_revogacao": ("secundaria: CPT 2014 (terradedireitos.org.br) e "
                            "MST 2019; lei revogadora nao localizada"),
    }
}


def _saida_utf8() -> None:
    """Força UTF-8 na saída antes de qualquer print.

    Mesmo guarda dos scripts 01–07: no Windows o pipe que captura a saída usa a
    codepage da locale (cp1252 em pt-BR), que não encoda ─ ⚠ ✔ ✘ → ≥, e o script
    morre de UnicodeEncodeError DEPOIS de ter feito o trabalho.
    """
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def resolve_pam(pasta: Path, fonte: str) -> tuple[Path | None, str]:
    """Acha o PAM pelo sufixo da fonte, como `05_build_panel.resolve_pam`.

    ⚠️ Regressão conhecida: o script 01 grava `__sidra`, e um consumidor que
    procure só por "" e `__simulado` não acha o arquivo real — o painel não
    monta e o erro manda rodar o script que já rodou. Ver os quatro testes de
    regressão de `resolve_pam` em `tests/test_data_prep.py`.

    E `real` nunca cai no simulado: diagnóstico simulado ocupando o lugar do
    real é o erro que nenhum resultado denuncia.
    """
    reais = ["__sidra", "__arquivo", ""]
    ordem = {
        "real": reais,
        "sidra": ["__sidra"],
        "simulado": ["__simulado"],
        "auto": reais + ["__simulado"],
    }[fonte]
    for sufixo in ordem:
        caminho = pasta / f"{NOME_PAM}{sufixo}.parquet"
        if caminho.exists():
            return caminho, sufixo
    return None, ""


def nomes_municipios(cache: Path, timeout: int = 30) -> dict[str, str]:
    """Nomes dos 184 municípios do Ceará, da API de localidades do IBGE.

    O parquet do PAM traz só código — e um CSV de alvos sem nome é inútil para
    quem vai procurar o acervo de cada câmara. O cache existe para a varredura
    não depender da rede a cada rodada.
    """
    if cache.exists():
        bruto = json.loads(cache.read_text(encoding="utf-8"))
    else:
        with urllib.request.urlopen(API_LOCALIDADES, timeout=timeout) as resposta:
            corpo = resposta.read()
        # ⚠️ Achado rodando: a API do IBGE responde **gzip mesmo sem
        # `Accept-Encoding: gzip`**, e o `urllib` não descomprime sozinho (o
        # `requests` descomprimiria, daí o erro não aparecer em quem testa com
        # ele). Sem isto, `.decode("utf-8")` morre em `0x8b` — o segundo byte
        # do número mágico do gzip — com uma mensagem que parece problema de
        # codificação de texto e não é.
        if corpo[:2] == b"\x1f\x8b":
            corpo = gzip.decompress(corpo)
        bruto = json.loads(corpo.decode("utf-8"))
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(bruto, ensure_ascii=False), encoding="utf-8")
    return {str(m["id"])[:6]: m["nome"] for m in bruto}


def decil_superior(pam: pd.DataFrame, fracao: float = FRACAO_DECIL) -> pd.DataFrame:
    """Para cada cultura, os municípios do topo da distribuição de área.

    Devolve uma linha por (cultura, município) com a posição, para que o CSV de
    alvos diga **por que** cada município entrou — um alvo sem justificativa é
    um alvo que ninguém sabe se pode cortar quando o tempo apertar.
    """
    linhas = []
    for cultura, bloco in pam.groupby("cultura"):
        positivos = (bloco[bloco["area_ha_media"] > 0]
                     .sort_values("area_ha_media", ascending=False))
        if positivos.empty:
            continue
        k = max(1, int(np.ceil(len(positivos) * fracao)))
        topo = positivos.head(k)
        for posicao, (_, linha) in enumerate(topo.iterrows(), start=1):
            linhas.append({
                "cod_ibge6": str(linha["cod_ibge6"]),
                "cultura": cultura,
                "area_ha_media": float(linha["area_ha_media"]),
                "rank": posicao,
                "n_positivos": len(positivos),
            })
    return pd.DataFrame(linhas)


def e_comparador(cultura: str) -> bool:
    """A cultura é um comparador de baixa pulverização, e não candidata a âncora?

    Casamento por prefixo normalizado porque o rótulo do SIDRA vem com
    qualificador — "Milho (em grão)", "Feijão (em grão)", "Arroz (em casca)".
    """
    base = cultura.lower()
    return any(base.startswith(c) for c in COMPARADORES_BAIXA_PULV)


def monta_alvos(decis: pd.DataFrame, nomes: dict[str, str]) -> pd.DataFrame:
    """Colapsa (cultura, município) em uma linha por município."""
    alvos = []
    for cod, bloco in decis.groupby("cod_ibge6"):
        b = bloco.sort_values("rank")
        motivo = "; ".join(f"{r.cultura} ({r['rank']}º/{r.n_positivos})"
                           for _, r in b.iterrows())
        alta_pulv = [r for _, r in b.iterrows() if not e_comparador(r.cultura)]
        alvos.append({
            "cod_ibge6": cod,
            "municipio": nomes.get(cod, "?"),
            # 1 = está no decil de alguma cultura de alta pulverização, que é
            # onde a âncora pode cair. 2 = só aparece em comparador.
            "prioridade": 1 if alta_pulv else 2,
            "motivo_alvo": motivo,
            "area_max_ha": float(b["area_ha_media"].max()),
            "rank_melhor": int(min(r["rank"] for r in alta_pulv) if alta_pulv
                               else b["rank"].min()),
        })

    for cod, nome in RIGOTTO.items():
        if not any(a["cod_ibge6"] == cod for a in alvos):
            alvos.append({
                "cod_ibge6": cod, "municipio": nome, "prioridade": 1,
                "motivo_alvo": "Rigotto et al. (2013) — município exposto",
                "area_max_ha": np.nan, "rank_melhor": np.nan,
            })
        else:
            for a in alvos:
                if a["cod_ibge6"] == cod:
                    a["motivo_alvo"] += "; Rigotto et al. (2013)"
                    a["prioridade"] = 1   # antecedente epidemiológico manda

    saida = pd.DataFrame(alvos)
    for coluna in COLUNAS_DE_ACHADO:
        saida[coluna] = ""
    saida["confianca"] = "nao_verificado"
    return (saida[COLUNAS]
            .sort_values(["prioridade", "rank_melhor", "cod_ibge6"])
            .reset_index(drop=True))


def mescla_com_existente(novos: pd.DataFrame, destino: Path) -> pd.DataFrame:
    """Preserva o que a varredura já preencheu.

    ⚠️ Sem isto, rodar o script de novo — depois de trocar a cultura-âncora, por
    exemplo — apagaria em silêncio o levantamento feito à mão. Trabalho de
    varredura é caro e não se reproduz sozinho.
    """
    if not destino.exists():
        return novos
    antigo = pd.read_csv(destino, dtype=str, comment="#").fillna("")
    preenchidos = antigo[antigo["confianca"] != "nao_verificado"]
    resultado = novos.set_index("cod_ibge6")
    for _, linha in preenchidos.iterrows():
        cod = str(linha["cod_ibge6"])
        if cod not in resultado.index:            # alvo saiu do decil, mas o
            continue                              # achado não deixa de valer
        # `.get`: um CSV anterior a 2026-09-22 não tem as colunas de revogação,
        # e ler um arquivo velho não pode quebrar.
        for coluna in COLUNAS_DE_ACHADO:
            resultado.loc[cod, coluna] = linha.get(coluna, "")
    return resultado.reset_index()[COLUNAS]


def aplica_semente(tabela: pd.DataFrame) -> pd.DataFrame:
    """Preenche o único achado já confirmado, se ainda estiver em branco."""
    t = tabela.set_index("cod_ibge6")
    for cod, campos in SEMENTE_CONFIRMADA.items():
        if cod in t.index and t.loc[cod, "confianca"] == "nao_verificado":
            for coluna, valor in campos.items():
                t.loc[cod, coluna] = valor
    return t.reset_index()[COLUNAS]


def imprime_relatorio(tabela: pd.DataFrame, decis: pd.DataFrame, sufixo: str) -> None:
    barra = "=" * 92
    print(barra)
    print("ALVOS DA VARREDURA DE BANS MUNICIPAIS < 2019 — fase 1")
    print(f"fonte do PAM: {NOME_PAM}{sufixo}.parquet")
    print(barra)

    n_cult = decis["cultura"].nunique()
    n_p1 = int((tabela["prioridade"] == 1).sum())
    n_p2 = int((tabela["prioridade"] == 2).sum())
    print(f"  culturas no PAM                : {n_cult}")
    print(f"  união dos decis superiores     : {tabela.shape[0]} municípios "
          f"(de 184 — {tabela.shape[0] / 184:.0%} do estado)")
    print()
    print("  ordem de trabalho (a coluna `prioridade`):")
    print(f"    1 — no decil de cultura de ALTA pulverização : {n_p1:3d}  <- comece aqui")
    print(f"    2 — só aparece em comparador de baixa pulv.  : {n_p2:3d}")
    print("    ⚠️ Os dois ficam no CSV. A prioridade ordena o trabalho; não elege")
    print("       cultura-âncora, que o CLAUDE.md proíbe hard-codar.")

    contagem = tabela["confianca"].value_counts()
    print()
    print("  estado da varredura:")
    for chave in CONFIANCA:
        print(f"    {chave:<20} {int(contagem.get(chave, 0)):3d}")

    confirmados = tabela[tabela["confianca"] == "confirmado"]
    if not confirmados.empty:
        print()
        print("  ⚠️ JÁ TRATADOS ANTES DE 2019 (dentro do grupo de dose alta):")
        for _, linha in confirmados.iterrows():
            print(f"    {linha['municipio']} ({linha['cod_ibge6']}) — "
                  f"lei {linha['numero_lei']} de {linha['data_lei']}")
            print(f"      {linha['motivo_alvo']}")

    print()
    print(barra)
    print("COMO LER — e o que este script NÃO diz")
    print(barra)
    print("  • Ele diz ONDE olhar, não o que foi achado. Toda linha com")
    print("    confianca=nao_verificado é trabalho por fazer, não ausência de lei.")
    print("  • ⚠️ 'ausente_conferido' e 'inconclusivo' NÃO são a mesma coisa. Site")
    print("    de câmara sem acervo histórico devolve vazio, e tratar esse vazio")
    print("    como 'não há lei' converte buraco de fonte em zero — que é")
    print("    exatamente a falha silenciosa que esta varredura existe para evitar.")
    print("  • Prioridade 2 não é 'não importa': se a âncora acabar sendo milho ou")
    print("    feijão, ela vira prioridade 1. É ordem de trabalho sob tempo escasso.")
    print("  • A fase 2 (os 184) é verificação de completude e não bloqueia nada.")
    print("  • Nada aqui é resultado do ban. É saneamento de pré-período.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--fonte", choices=("auto", "real", "sidra", "simulado"),
                   default="auto")
    p.add_argument("--dir-dados", type=Path, default=DIR_DADOS)
    p.add_argument("--destino", type=Path, default=DESTINO)
    p.add_argument("--fracao-decil", type=float, default=FRACAO_DECIL)
    p.add_argument("--cache-nomes", type=Path,
                   default=DIR_DADOS / "municipios_ce_nomes.json")
    args = p.parse_args(argv)

    caminho, sufixo = resolve_pam(args.dir_dados, args.fonte)
    if caminho is None:
        print(f"  ✘ PAM não encontrado em {args.dir_dados} para --fonte {args.fonte}.")
        print("    Rode antes: python scripts/data_prep/01_check_dose_variation.py "
              "--fonte sidra")
        return 1

    pam = pd.read_parquet(caminho)
    pam["cod_ibge6"] = pam["cod_ibge6"].astype(str)

    try:
        nomes = nomes_municipios(args.cache_nomes)
    except OSError as erro:
        print(f"  ⚠️ API de localidades do IBGE indisponível ({erro}).")
        print("    Seguindo sem nomes — o CSV sai com '?' na coluna municipio.")
        nomes = {}

    decis = decil_superior(pam, args.fracao_decil)
    if decis.empty:
        print("  ✘ nenhuma cultura com área positiva no PAM. Nada a fazer.")
        return 1

    tabela = aplica_semente(mescla_com_existente(monta_alvos(decis, nomes),
                                                 args.destino))

    args.destino.parent.mkdir(parents=True, exist_ok=True)
    with open(args.destino, "w", encoding="utf-8", newline="") as fh:
        fh.write(f"# gerado em {date.today().isoformat()} por "
                 "08_alvos_legislativos.py\n")
        fh.write(f"# fonte do PAM: {NOME_PAM}{sufixo}.parquet | "
                 f"decil = topo {args.fracao_decil:.0%} por área\n")
        fh.write("# confianca: nao_verificado | confirmado | ausente_conferido | "
                 "inconclusivo\n")
        fh.write("# ⚠️ 'inconclusivo' NÃO é 'ausente_conferido' — ver o docstring "
                 "do script e docs/legislacao/README.md §1\n")
        tabela.to_csv(fh, index=False)

    imprime_relatorio(tabela, decis, sufixo)
    print(f"\n[ok] -> {args.destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
