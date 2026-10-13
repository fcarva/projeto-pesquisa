"""Fluxograma PRISMA 2020 de cada SQ, a partir das contagens da deduplicação e das decisões (Etapa 4).

Entradas:
- `registros/contagens-prisma.json` (de `deduplica.py`): identificação e remoção antes da triagem;
- opcional, `registros/decisoes-<sq>.csv`, uma linha por registro triado, com as colunas
  `id_unico`, `titulo_resumo` (incluir/excluir), `texto_obtido` (sim/nao),
  `texto_completo` (incluir/excluir), `motivo` (da lista fechada) e `estudo` (ID do estudo:
  relatos do mesmo estudo têm o mesmo `estudo`). Na SQ2/SQ3, um registro sem linha aqui é
  "não triado pela regra de parada";
- opcional, `registros/outros-metodos-<sq>.csv`, com as mesmas colunas mais `origem`
  (citacao/site/organizacao): a coluna "outros métodos" do fluxograma.
Sem decisões, as caixas de triagem em diante saem como "pendente".

Mapeamento para o PRISMA 2020 (Page et al. 2021, BMJ 372:n71):
- "Registros identificados" por base = registros distintos na base (`distintos_na_fonte`);
- "Duplicatas removidas" = `duplicatas_por_chave` (IDs diferentes, mesmo DOI/PMID/título + ano);
  a sobreposição entre linhas de uma mesma base já está fora dos distintos e vai na nota;
- "Marcados como inelegíveis por ferramenta automática" = exclusões por regra de metadado
  (período, idioma, paratext, retratado), aplicadas por script e listadas na caixa.
O script falha se uma identidade não fechar.

Saídas: `paper/overleaf/prisma-<sq>.tex` (TikZ, classe standalone: compila sozinho no Overleaf
ou entra com `\\includestandalone`), `docs/revisao-sistematica/prisma-fluxo.md` e
`registros/prisma-fluxo.json`.

    python3 ferramentas/prisma.py
"""
import csv
import json
import os
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
REG = os.path.join(BASE, "registros")
RAIZ = os.path.dirname(os.path.dirname(BASE))
OVERLEAF = os.path.join(RAIZ, "paper", "overleaf")

TITULO = {"sq1": "SQ1: agrotóxicos agrícolas e desfechos ao nascer (revisão sistemática)",
          "sq2": "SQ2: método (revisão estruturada complementar)",
          "sq3": "SQ3: escolha de instrumento (revisão estruturada complementar)"}
NOME_BASE = {"Scopus (API)": "Scopus (API, visão reduzida)", "OASISBR": "OASISBR (IBICT)"}
MOTIVO_AUTO = {"periodo": "anterior a 1990", "idioma": "idioma fora de en/pt/es", "paratext": "paratexto",
               "retratado": "retratado"}
PENDENTE = None


def le(caminho):
    return list(csv.DictReader(open(caminho, encoding="utf-8"))) if os.path.exists(caminho) else None


def fluxo(sq, c):
    """Números de cada caixa; None = pendente."""
    bases = {NOME_BASE.get(f, f): v["distintos_na_fonte"] for f, v in c["identificados_por_fonte"].items()}
    auto = c["excluidos_por_metadado"]
    f = {"bases": bases, "registros_de_registro": 0,
         "duplicatas": c["duplicatas_por_chave"], "sobreposicao_entre_linhas": c["sobreposicao_entre_linhas"],
         "automacao": sum(auto.values()), "automacao_motivos": auto, "outros_removidos": 0,
         "triados": c["a_triar"]}
    assert sum(bases.values()) - f["duplicatas"] - f["automacao"] - f["outros_removidos"] == f["triados"], \
        f"{sq}: identificação não fecha"
    dec = le(os.path.join(REG, f"decisoes-{sq}.csv"))
    for k in ("nao_triados_regra_parada", "excluidos_titulo_resumo", "buscados", "nao_obtidos", "avaliados",
              "excluidos_texto", "estudos_incluidos", "relatos_incluidos"):
        f[k] = PENDENTE
    f["excluidos_texto_motivos"] = {}
    if dec is not None:
        triados = [d for d in dec if d.get("titulo_resumo")]
        if sq != "sq1":
            f["nao_triados_regra_parada"] = f["triados"] - len(triados)
            f["triados"] = len(triados)
        f["excluidos_titulo_resumo"] = sum(1 for d in triados if d["titulo_resumo"] == "excluir")
        buscados = [d for d in triados if d["titulo_resumo"] == "incluir"]
        f["buscados"] = len(buscados)
        f["nao_obtidos"] = sum(1 for d in buscados if d.get("texto_obtido") == "nao")
        avaliados = [d for d in buscados if d.get("texto_obtido") == "sim" and d.get("texto_completo")]
        f["avaliados"] = len(avaliados)
        exc = [d for d in avaliados if d["texto_completo"] == "excluir"]
        f["excluidos_texto"] = len(exc)
        f["excluidos_texto_motivos"] = dict(Counter(d.get("motivo") or "sem motivo" for d in exc))
        inc = [d for d in avaliados if d["texto_completo"] == "incluir"]
        f["relatos_incluidos"] = len(inc)
        f["estudos_incluidos"] = len({d.get("estudo") or d["id_unico"] for d in inc})
        assert f["triados"] - f["excluidos_titulo_resumo"] == f["buscados"], f"{sq}: triagem não fecha"
        assert f["buscados"] - f["nao_obtidos"] >= f["avaliados"], f"{sq}: busca de texto não fecha"
        assert f["avaliados"] - f["excluidos_texto"] == f["relatos_incluidos"], f"{sq}: elegibilidade não fecha"
    outros = le(os.path.join(REG, f"outros-metodos-{sq}.csv"))
    f["outros_metodos"] = None if outros is None else dict(Counter(o.get("origem") or "outro" for o in outros))
    return f


def n(x):
    return "pendente" if x is None else f"{x:,}".replace(",", ".")


# ---------------------------------------------------------------- TikZ

def tex(s):
    return (str(s).replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%")
            .replace("#", r"\#").replace("_", r"\_"))


def nn(x):
    """(n = x) sem quebra de linha no meio."""
    return rf"\mbox{{(\textit{{n}} = {n(x)})}}"


def tikz(sq, f):
    bases = r" \\ ".join(f"{tex(b)} {nn(v)}" for b, v in sorted(f["bases"].items(), key=lambda kv: -kv[1]))
    motivos = "; ".join(f"{MOTIVO_AUTO.get(k, k)}: {n(v)}" for k, v in f["automacao_motivos"].items()) or "nenhum"
    exc_texto = (r" \\ ".join(f"{tex(k)} {nn(v)}" for k, v in f["excluidos_texto_motivos"].items())
                 if f["excluidos_texto_motivos"] else "motivos: pendente")
    parada = (rf" \\ Não triados pela regra de parada {nn(f['nao_triados_regra_parada'])}" if sq != "sq1" else "")
    if f["outros_metodos"] is None:
        outros = rf"Busca de citações e sites de literatura cinzenta {nn(None)}"
    else:
        outros = r" \\ ".join(f"{tex(k)} {nn(v)}" for k, v in f["outros_metodos"].items())
    return rf"""% Gerado por docs/revisao-sistematica/ferramentas/prisma.py: não editar à mão.
% PRISMA 2020 (Page et al. 2021, BMJ 372:n71). {tex(TITULO[sq])}
\documentclass[tikz,border=6pt]{{standalone}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage[brazil]{{babel}}
\usetikzlibrary{{positioning,arrows.meta,calc}}
\begin{{document}}
\begin{{tikzpicture}}[
  caixa/.style={{draw, rectangle, align=left, text width=6.4cm, font=\footnotesize, inner sep=4pt}},
  lado/.style={{caixa, text width=5.4cm}},
  cab/.style={{draw, fill=gray!30, font=\footnotesize\bfseries, align=center}},
  seta/.style={{-{{Stealth}}, thick}}, node distance=0.55cm and 0.6cm]
\node[caixa, minimum height=2.6cm] (id) {{\textbf{{Registros identificados em bases}}: \\ {bases} \\ Registros de ensaios {nn(f['registros_de_registro'])}}};
\node[lado, right=of id.north east, anchor=north west] (rem) {{\textbf{{Registros removidos antes da triagem}}: \\ Duplicatas removidas {nn(f['duplicatas'])} \\ Marcados como inelegíveis por regra automática de metadado {nn(f['automacao'])}: {tex(motivos)} \\ Removidos por outros motivos {nn(f['outros_removidos'])}}};
\node[caixa, below=1.0cm of id.south |- rem.south, anchor=north] (tri) {{Registros triados por título e resumo {nn(f['triados'])}{parada}}};
\node[lado, right=of tri] (exc1) {{Registros excluídos {nn(f['excluidos_titulo_resumo'])}}};
\node[caixa, below=of tri] (busc) {{Relatos buscados para leitura do texto completo {nn(f['buscados'])}}};
\node[lado, right=of busc] (nobt) {{Relatos não obtidos {nn(f['nao_obtidos'])}}};
\node[caixa, below=of busc] (aval) {{Relatos avaliados quanto à elegibilidade {nn(f['avaliados'])}}};
\node[lado, right=of aval] (exc2) {{\textbf{{Relatos excluídos}} {nn(f['excluidos_texto'])}: \\ {exc_texto}}};
\node[caixa, minimum height=2.0cm, below=1.0cm of aval] (inc) {{\textbf{{Estudos incluídos na revisão}} {nn(f['estudos_incluidos'])} \\ Relatos dos estudos incluídos {nn(f['relatos_incluidos'])}}};
\node[lado, text width=4.4cm, right=1.0cm of rem.north east, anchor=north west] (out) {{\textbf{{Registros identificados por outros métodos}}: \\ {outros}}};
\node[cab, above=0.4cm of id.north west, anchor=south west, minimum width=12.6cm] {{Identificação via bases de dados e registros}};
\node[cab, above=0.4cm of out.north west, anchor=south west, minimum width=4.6cm, text width=4.4cm] {{Identificação via outros métodos}};
\draw[seta] (id) -- (rem); \draw[seta] (id) -- (tri); \draw[seta] (tri) -- (exc1);
\draw[seta] (tri) -- (busc); \draw[seta] (busc) -- (nobt); \draw[seta] (busc) -- (aval);
\draw[seta] (aval) -- (exc2); \draw[seta] (aval) -- (inc);
\draw[seta] (out.south) |- (inc.east);
\foreach \ini/\fim/\rot in {{id/id/Identificação, tri/aval/Triagem, inc/inc/Inclusão}} {{
  \draw[fill=gray!15, rounded corners] ($(\ini.north west)+(-0.85cm,0)$) rectangle ($(\fim.south west)+(-0.3cm,0)$);
  \node[rotate=90, font=\footnotesize\bfseries] at ($($(\ini.north west)!0.5!(\fim.south west)$)+(-0.575cm,0)$) {{\rot}};
}}
\end{{tikzpicture}}
\end{{document}}
"""


# ---------------------------------------------------------------- Markdown

def markdown(fluxos):
    w = ["# Fluxogramas PRISMA 2020", "",
         "*Gerado por `ferramentas/prisma.py` a partir de `registros/contagens-prisma.json` e, quando "
         "existirem, das decisões de triagem. Não editar à mão. Versões TikZ para o Overleaf em "
         "`paper/overleaf/prisma-<sq>.tex`.*", ""]
    for sq, f in fluxos.items():
        w += [f"## {TITULO[sq]}", "", "**Identificação**", ""]
        for b, v in sorted(f["bases"].items(), key=lambda kv: -kv[1]):
            w.append(f"- {b}: {n(v)}")
        w += [f"- Registros de ensaios: {n(f['registros_de_registro'])}",
              f"- Outros métodos (citações, sites): "
              + ("pendente" if f["outros_metodos"] is None else
                 "; ".join(f"{k}: {n(v)}" for k, v in f["outros_metodos"].items())),
              "", "**Removidos antes da triagem**", "",
              f"- Duplicatas: {n(f['duplicatas'])} (além de {n(f['sobreposicao_entre_linhas'])} sobreposições "
              "entre linhas de uma mesma base, já fora dos distintos)",
              f"- Regra automática de metadado: {n(f['automacao'])} ("
              + ("; ".join(f"{MOTIVO_AUTO.get(k, k)} {n(v)}" for k, v in f["automacao_motivos"].items()) or "nenhum")
              + ")", "", "**Triagem e inclusão**", "",
              f"- Triados por título e resumo: {n(f['triados'])}"
              + (f" (não triados pela regra de parada: {n(f['nao_triados_regra_parada'])})" if sq != "sq1" else ""),
              f"- Excluídos na triagem: {n(f['excluidos_titulo_resumo'])}",
              f"- Buscados para texto completo: {n(f['buscados'])}; não obtidos: {n(f['nao_obtidos'])}",
              f"- Avaliados: {n(f['avaliados'])}; excluídos: {n(f['excluidos_texto'])}"
              + ("" if not f["excluidos_texto_motivos"] else
                 " (" + "; ".join(f"{k} {n(v)}" for k, v in f["excluidos_texto_motivos"].items()) + ")"),
              f"- **Estudos incluídos: {n(f['estudos_incluidos'])}** (relatos: {n(f['relatos_incluidos'])})", ""]
    return "\n".join(w)


def roda():
    c = json.load(open(os.path.join(REG, "contagens-prisma.json"), encoding="utf-8"))
    fluxos = {sq: fluxo(sq, c[sq]) for sq in ("sq1", "sq2", "sq3")}
    os.makedirs(OVERLEAF, exist_ok=True)
    for sq, f in fluxos.items():
        open(os.path.join(OVERLEAF, f"prisma-{sq}.tex"), "w", encoding="utf-8").write(tikz(sq, f))
    open(os.path.join(BASE, "prisma-fluxo.md"), "w", encoding="utf-8").write(markdown(fluxos))
    json.dump(fluxos, open(os.path.join(REG, "prisma-fluxo.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    for sq, f in fluxos.items():
        print(f"{sq}: bases {sum(f['bases'].values())} − duplicatas {f['duplicatas']} − automação "
              f"{f['automacao']} = triados {f['triados']}")


if __name__ == "__main__":
    roda()
