"""Varre o acervo das câmaras municipais atrás de bans anteriores a 2019.

Consome o CSV de alvos que `08_alvos_legislativos.py` semeia e preenche as
colunas de achado. **Mescla, nunca sobrescreve**: linha já resolvida não é
tocada, porque varredura é trabalho caro e não se reproduz sozinha.

⚠️ **O ponto inteiro deste script é a coluna `confianca`.** Ausência de lei no
site de uma câmara NÃO é prova de ausência de lei. Ele só grava
`ausente_conferido` quando **todos** os termos de busca voltaram resposta
válida; se qualquer consulta falhou, ou se a plataforma não é conhecida, grava
`inconclusivo`. Colapsar os dois transformaria buraco de fonte em zero — que é
exatamente a falha silenciosa que a varredura existe para evitar.

## As plataformas, mapeadas em 2026-09-21

As câmaras cearenses respondem em `www.camara<slug>.ce.gov.br` e usam **duas**
plataformas distintas, mais um resto sem site nesse padrão:

| Plataforma | Marca no HTML | Busca | Estado |
|---|---|---|---|
| **A** | `leis.php` | `GET /leis.php?descr=<termo>` — renderizada no servidor | ✅ |
| **B** | `atividade-legislativa` | `GET /institucional/legislacao/export/?format=json&pagina=2` — **acervo inteiro em JSON** | ✅ |

E o host tem **dois prefixos**, não um: `camara<slug>.ce.gov.br` para a maioria,
`cm<slug>.ce.gov.br` para uma minoria (Itapajé, Pacoti, Palmácia, Guaraciaba do
Norte). Testar só o primeiro faz 4 municípios parecerem "sem site".

⚠️ **Três armadilhas achadas rodando, e nenhuma se enxerga lendo o HTML:**

1. **A busca casa palavra inteira, não substring.** `?descr=pulveriza` devolve
   zero; `?descr=AERONAVES` devolve a lei. A ementa de Limoeiro diz
   "pulverizações", e o prefixo não casa. Daí a lista `TERMOS` ser redundante
   de propósito — variações com e sem acento, singular e plural.
2. **A paginação de `/leis.php` é JS.** `?pagina=N` é aceito e **ignorado**:
   páginas 5 a 13 devolvem o mesmo conteúdo. Varrer por paginação não funciona;
   por isso este script busca por termo, não lista tudo.
3. **A API da plataforma B devolve 400 para todo nome de parâmetro testado**
   (`q`, `termo`, `busca`, e sem parâmetro). O nome vive no JS do portal.

## Limites — o que este script NÃO resolve

- **Portal que não é A nem B** fica `inconclusivo`. Resolver exige inspeção
  manual do site.
- **Acervo incompleto.** Câmara que não publica lei de 2009 devolve vazio
  legitimamente. `ausente_conferido` significa "o acervo publicado não tem",
  não "o município não legislou". A §8 da pré-especificação recebe isso como
  ameaça declarada.
- ⚠️ **Lei achada não é lei vigente.** Quando acha mais de uma lei, o script
  grava a **primeira** (a mais antiga) — e nunca procura a que a revoga. Foi
  assim que a Lei 1.478/2009 de Limoeiro ficou registrada como ban vigente,
  quando fontes secundárias (CPT 2014; MST 2019) dizem que ela foi **revogada
  em 20/05/2010**. A revogadora dificilmente tem "aeronave" na ementa ("Revoga
  a Lei nº ..."), então os `TERMOS` não a pegam. Todo `confirmado` exige
  conferência manual de revogação, registrada em `data_revogacao` /
  `fonte_revogacao` (colunas do script 08). Ver `docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md` §5.

Rodar:

    python scripts/data_prep/09_varre_camaras.py --prioridade 1
    python scripts/data_prep/09_varre_camaras.py --revogacao            # só relata
    python scripts/data_prep/09_varre_camaras.py --revogacao --gravar-revogacao

O modo `--revogacao` procura, para cada `confirmado`, as leis POSTERIORES que
citam o número da lei achada ou que revogam algo do tema. Só grava a candidata
inequívoca — a que cita o número E fala em revogar — e troca a fonte de
"secundaria" para "primaria". O resto sai no relatório para conferência à mão.
"""

from __future__ import annotations

import argparse
import gzip
import re
import sys
import time
import unicodedata
import urllib.parse
import json
import urllib.request
from datetime import date
from pathlib import Path

import pandas as pd

DESTINO = Path("docs/legislacao/bans-municipais-ce.csv")
ANO_BAN_ESTADUAL = 2019
UA = "Mozilla/5.0 (pesquisa academica; dissertacao PPGEco/UFES)"

# ⚠️ Redundante DE PROPÓSITO: a busca casa palavra inteira. "pulveriza" não
# encontra "pulverizações". Cada variação custa uma requisição e evita um falso
# negativo — e falso negativo aqui vira "não há lei", que é o erro caro.
TERMOS = (
    "AERONAVES", "AERONAVE", "AVIAO", "AVIÃO", "AVIÕES",
    "PULVERIZACAO", "PULVERIZAÇÃO", "PULVERIZAÇÕES", "PULVERIZAR",
    "AGROTOXICO", "AGROTÓXICO", "AGROTÓXICOS", "AEREA", "AÉREA", "FUMIGACAO",
)

# Slug do portal por código IBGE6. Conferido um a um em 2026-09-21: o padrão
# `camara<slug>.ce.gov.br` resolve para a maioria, mas não para todos, e o slug
# nem sempre é o nome sem acento (por isso a tabela, e não uma regra).
SLUGS = {
    "230640": "itapipoca", "230760": "limoeirodonorte", "230840": "missaovelha",
    "230910": "mulungu", "230210": "baturite", "230290": "capistrano",
    "231380": "uruburetama", "231160": "redencao", "230140": "aratuba",
    "231180": "russas", "231150": "quixere", "231340": "tiangua",
    "231395": "varjota", "230630": "itapaje", "230980": "pacoti",
    "231010": "palmacia", "230500": "guaraciabadonorte",
}


def _saida_utf8() -> None:
    """Força UTF-8 na saída antes de qualquer print.

    Mesmo guarda dos scripts 01–08: no Windows o pipe usa a codepage da locale
    (cp1252), que não encoda ─ ⚠ ✔ ✘, e o script morreria DEPOIS de ter feito o
    trabalho — aqui, depois de gastar dezenas de requisições de rede.
    """
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def sem_acento(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn").lower()


def busca_http(url: str, timeout: int = 35) -> str | None:
    """GET que devolve texto, ou None se a rede falhar.

    ⚠️ Descomprime gzip à mão: vários portais públicos brasileiros respondem
    comprimido **mesmo sem `Accept-Encoding: gzip`**, e o `urllib` não
    descomprime sozinho. Sem isto o `.decode` morre em `0x8b` com uma mensagem
    que parece erro de codificação de texto e não é. Mesmo achado da API de
    localidades do IBGE no script 08.
    """
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as resposta:
            corpo = resposta.read()
    except Exception:
        return None
    if corpo[:2] == b"\x1f\x8b":
        corpo = gzip.decompress(corpo)
    return corpo.decode("utf-8", errors="replace")


# ⚠️ DOIS prefixos de host, não um. Conferido em 2026-09-21: a maioria responde
# em `camara<slug>`, mas Itapajé, Pacoti, Palmácia e Guaraciaba do Norte só
# respondem em `cm<slug>`. Testar só o primeiro fazia quatro municípios
# parecerem "sem site" — e "sem site" vira `inconclusivo`, isto é, trabalho que
# nunca seria feito porque parecia impossível.
# ⚠️ E o terceiro não é prefixo de câmara: é a PREFEITURA. Itapajé responde em
# `cmitapaje.ce.gov.br` com um stub de 3 KB — parece site, não é acervo — e o
# acervo de leis mora em `itapaje.ce.gov.br`, o portal do executivo. Testar só
# os dois primeiros deixava o município `inconclusivo` para sempre, e um
# "inconclusivo" é trabalho que nunca será feito porque parece impossível.
#
# A ordem importa: prefeitura POR ÚLTIMO, porque onde a câmara publica o acervo
# ela é a fonte melhor (é o órgão que aprova a lei).
PREFIXOS_HOST = ("camara", "cm", "")


def detecta_plataforma(slug: str) -> tuple[str, str]:
    """('A' | 'B' | 'desconhecida' | 'sem_site', url_base)."""
    ultimo = None
    for prefixo in PREFIXOS_HOST:
        base = f"https://www.{prefixo}{slug}.ce.gov.br"
        html = busca_http(base + "/", timeout=30)
        if html is None:
            continue
        ultimo = base
        if "leis.php" in html:
            return "A", base
        if "atividade-legislativa" in html:
            return "B", base
        # ⚠️ NÃO devolve "desconhecida" aqui: um host pode responder com stub e
        # o acervo estar no próximo da lista. Só desiste depois de testar todos.
    if ultimo:
        return "desconhecida", ultimo
    return "sem_site", f"https://www.camara{slug}.ce.gov.br"


def varre_plataforma_b(base: str, timeout: int = 300) -> dict:
    """Baixa o acervo inteiro em JSON e filtra localmente.

    ⚠️ O `&pagina=2` não é para ir à página 2. É um parâmetro **não
    reconhecido** pelo endpoint, e passá-lo desliga o filtro de paginação:
    sem ele vêm 3 registros do ano corrente; com ele, o acervo completo. Sem
    esse truque a varredura concluiria "acervo minúsculo, nada aqui".
    """
    acervo, erros, url = _acervo_plataforma_b(base, timeout)
    if erros:
        return {"leis": [], "erros": 1, "termos": 1, "n_acervo": 0, "url": url}
    leis = [lei for lei in acervo
            if lei["ano"] < ANO_BAN_ESTADUAL and _e_do_tema(lei["ementa"])]
    return {"leis": leis, "erros": 0, "termos": 1, "n_acervo": len(acervo), "url": url}


def _acervo_plataforma_b(base: str, timeout: int = 300) -> tuple[list[dict], int, str]:
    """O acervo INTEIRO da plataforma B, sem filtro — (leis, erros, url).

    Separado da varredura porque a busca de revogação precisa do que a
    varredura descarta: as leis de depois de 2009 e as que não são do tema
    ("Revoga a Lei nº 1.478" não fala em aeronave).
    """
    url = f"{base}/institucional/legislacao/export/?format=json&pagina=2"
    texto = busca_http(url, timeout=timeout)
    if texto is None:
        return [], 1, url
    try:
        bruto = json.loads(texto)
    except json.JSONDecodeError:
        return [], 1, url
    itens = bruto if isinstance(bruto, list) else bruto.get("results", [])
    leis = []
    for item in itens:
        ano = str(item.get("Ano", "")).strip()
        if not ano.isdigit():
            continue
        leis.append({
            "numero_lei": f"{item.get('Número', '?')}/{ano}",
            "ano": int(ano),
            "data_lei": str(item.get("Data", ""))[:10],
            "ementa": str(item.get("Ementa", ""))[:200],
            "url_fonte": url,
        })
    return leis, 0, url


def extrai_leis(html: str) -> list[dict]:
    """Lê a lista de leis da página de resultado da plataforma A."""
    texto = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))
    achados = []
    for m in re.finditer(
        r"Lei Municipal - ([\d.]+)/(\d{4})\s+(\d{2}/\d{2}/\d{4})\s+(.{10,260}?)\s+Acessar",
        texto,
    ):
        numero, ano, data_br, ementa = m.groups()
        ementa = re.sub(r"^-+>\s*", "", ementa).strip()
        achados.append({
            "numero_lei": f"{numero}/{ano}",
            "ano": int(ano),
            "data_lei": "-".join(reversed(data_br.split("/"))),
            "ementa": ementa[:200],
        })
    return achados


def varre_plataforma_a(base: str, termos=TERMOS, pausa: float = 0.3) -> dict:
    """Busca cada termo e devolve achados anteriores ao ban estadual.

    ⚠️ `erros` não é diagnóstico secundário: é o que separa `ausente_conferido`
    de `inconclusivo`. Um termo que falhou por rede é um termo não conferido, e
    um único desses já impede afirmar que não há lei.
    """
    leis, erros = {}, 0
    for termo in termos:
        url = f"{base}/leis.php?descr={urllib.parse.quote(termo)}"
        html = busca_http(url)
        if html is None:
            erros += 1
            continue
        for lei in extrai_leis(html):
            if lei["ano"] < ANO_BAN_ESTADUAL and _e_do_tema(lei["ementa"]):
                lei["url_fonte"] = url
                leis[lei["numero_lei"]] = lei
        time.sleep(pausa)
    return {"leis": list(leis.values()), "erros": erros, "termos": len(termos)}


def _e_do_tema(ementa: str) -> bool:
    """Filtra falso positivo: o termo pode casar por outro motivo.

    "aérea" casa com "área aérea de lazer"; "avião" com homenagem a aviador.
    Exige co-ocorrência de um termo de **método aéreo** com um de **veneno ou
    lavoura** — que é a estrutura da ementa de Limoeiro.
    """
    e = sem_acento(ementa)
    metodo = any(t in e for t in ("aeronave", "aviao", "aviões", "aereo", "aerea",
                                  "pulveriza", "fumiga"))
    alvo = any(t in e for t in ("agrotoxic", "defensivo", "veneno", "lavoura",
                                "pulveriza", "praga", "agricol"))
    return metodo and alvo


def classifica(resultado: dict) -> tuple[str, str]:
    """(confianca, tem_lei) a partir do que a varredura de fato conseguiu."""
    if resultado["leis"]:
        return "confirmado", "sim"
    if resultado["erros"] > 0:
        return "inconclusivo", ""          # ⚠️ NÃO é "não há"
    return "ausente_conferido", "nao"


# --------------------------------------------------------------------------
# Revogação — lei achada não é lei vigente
# --------------------------------------------------------------------------
# Acrescentado em 2026-09-22, depois que fontes secundárias mostraram que a Lei
# 1.478/2009 de Limoeiro foi revogada em 20/05/2010 — e a varredura, que parava
# na primeira lei achada, não tinha como saber. Ver
# docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md §5.

TERMOS_REVOGACAO = ("REVOGA", "REVOGADA", "REVOGAÇÃO", "REVOGACAO")


def variantes_do_numero(numero_lei: str) -> set[str]:
    """'1478/2009' ou '1.478/2009' → {'1478', '1.478'}: as câmaras escrevem dos dois jeitos."""
    num = numero_lei.split("/")[0].replace(".", "").strip()
    if not num.isdigit():
        return {num}
    return {num, f"{int(num):,}".replace(",", ".")}


def cita_a_lei(ementa: str, numero_lei: str) -> bool:
    """A ementa cita o número? Casa '1.478' e '1478', mas não '11.478' nem '1.4789'."""
    e = sem_acento(ementa)
    return any(re.search(rf"(?<![\d.]){re.escape(v)}(?![\d])", e)
               for v in variantes_do_numero(numero_lei))


def _data_iso(texto: str) -> str:
    """'20/05/2010' → '2010-05-20'; ISO passa como está. A plataforma B não
    garante o formato, e comparar datas como texto em formatos diferentes
    ordena errado sem avisar."""
    texto = str(texto).strip()[:10]
    m = re.fullmatch(r"(\d{2})/(\d{2})/(\d{4})", texto)
    return f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else texto


def candidatas_revogacao(leis: list[dict], numero_lei: str, data_lei: str) -> list[dict]:
    """Leis POSTERIORES à achada que citam o número dela, ou que revogam algo do tema.

    ⚠️ Não decide. "Altera a Lei nº 1.478" cita o número e não revoga; "Revoga
    as Leis nº ..." pode não repetir o tema. Por isso cada candidata sai com as
    duas marcas, `cita_o_numero` e `fala_em_revogar`, e só a coincidência das
    duas autoriza gravar sem olho humano (`--gravar-revogacao`).
    """
    vistas, saida, limite = set(), [], _data_iso(data_lei)
    for lei in leis:
        data = _data_iso(lei["data_lei"])
        if lei["numero_lei"] in vistas or not data or data <= limite:
            continue
        vistas.add(lei["numero_lei"])
        lei = {**lei, "data_lei": data}
        e = sem_acento(lei["ementa"])
        cita = cita_a_lei(lei["ementa"], numero_lei)
        revoga = "revog" in e
        if cita or (revoga and _e_do_tema(lei["ementa"])):
            saida.append({**lei, "cita_o_numero": cita, "fala_em_revogar": revoga})
    return sorted(saida, key=lambda x: x["data_lei"])


def busca_revogacao(plataforma: str, base: str, numero_lei: str, data_lei: str,
                    pausa: float = 0.3) -> dict:
    """Candidatas a revogadora, pela plataforma do portal. `erros` tem o mesmo
    papel da varredura: um termo que falhou é um termo não conferido."""
    if plataforma == "B":
        acervo, erros, _ = _acervo_plataforma_b(base)
        return {"candidatas": candidatas_revogacao(acervo, numero_lei, data_lei),
                "erros": erros, "termos": 1}
    termos = TERMOS_REVOGACAO + tuple(sorted(variantes_do_numero(numero_lei)))
    leis, erros = [], 0
    for termo in termos:
        url = f"{base}/leis.php?descr={urllib.parse.quote(termo)}"
        html = busca_http(url)
        if html is None:
            erros += 1
            continue
        for lei in extrai_leis(html):
            leis.append({**lei, "url_fonte": url})
        time.sleep(pausa)
    return {"candidatas": candidatas_revogacao(leis, numero_lei, data_lei),
            "erros": erros, "termos": len(termos)}


def revogadora_inequivoca(candidatas: list[dict]) -> dict | None:
    """A única candidata que cita o número E fala em revogar — ou nenhuma."""
    fortes = [c for c in candidatas if c["cita_o_numero"] and c["fala_em_revogar"]]
    return fortes[0] if len(fortes) == 1 else None


def roda_revogacao(tabela: pd.DataFrame, gravar: bool) -> tuple[pd.DataFrame, list[str]]:
    """Para cada `confirmado`, procura a revogadora. Devolve a tabela e o relatório."""
    relatorio, t = [], tabela.copy()
    for coluna in ("data_revogacao", "fonte_revogacao"):
        if coluna not in t.columns:
            t[coluna] = ""
    for idx, linha in t[t["confianca"] == "confirmado"].iterrows():
        cod = linha["cod_ibge6"]
        if cod not in SLUGS:
            relatorio.append(f"  ?? {linha['municipio']}: sem slug conhecido")
            continue
        plataforma, base = detecta_plataforma(SLUGS[cod])
        if plataforma not in ("A", "B"):
            relatorio.append(f"  ?? {linha['municipio']}: plataforma {plataforma} — à mão")
            continue
        r = busca_revogacao(plataforma, base, linha["numero_lei"], linha["data_lei"])
        relatorio.append(f"  {linha['municipio']} — Lei {linha['numero_lei']} "
                         f"({linha['data_lei']}), plataforma {plataforma}, "
                         f"{r['termos'] - r['erros']}/{r['termos']} buscas ok")
        for c in r["candidatas"]:
            marcas = ("cita o número" if c["cita_o_numero"] else "") + \
                     (" + revoga" if c["fala_em_revogar"] else "")
            relatorio.append(f"     >>> Lei {c['numero_lei']}  {c['data_lei']}  [{marcas.strip(' +')}]")
            relatorio.append(f"         {c['ementa'][:110]}")
        if not r["candidatas"]:
            relatorio.append("     nenhuma candidata"
                             + (" — ⚠️ com busca falhando, isto NÃO é 'não revogada'"
                                if r["erros"] else ""))
        achada = revogadora_inequivoca(r["candidatas"])
        if gravar and achada:
            t.loc[idx, "data_revogacao"] = achada["data_lei"]
            t.loc[idx, "fonte_revogacao"] = (
                f"primaria: Lei {achada['numero_lei']} de {achada['data_lei']} — "
                f"{achada['ementa'][:90]} ({achada.get('url_fonte', base)})")
            relatorio.append(f"     ✔ gravada: Lei {achada['numero_lei']} "
                             f"(antes: {linha.get('data_revogacao', '') or 'vazio'})")
        elif gravar:
            relatorio.append("     ✘ não gravada: nenhuma candidata inequívoca — conferir à mão")
    return t, relatorio


def imprime_relatorio(linhas: list[dict]) -> None:
    barra = "=" * 92
    print(barra)
    print("VARREDURA DAS CÂMARAS — bans municipais anteriores a 2019")
    print(barra)
    for r in linhas:
        marca = {"confirmado": "⚠️ ACHOU", "ausente_conferido": "  nada",
                 "inconclusivo": "?? incon"}.get(r["confianca"], "   ?")
        print(f"  {marca:<10} {r['municipio']:<24} [{r['plataforma']}] {r['nota']}")
        for lei in r.get("achados", []):
            print(f"       >>> Lei {lei['numero_lei']}  {lei['data_lei']}")
            print(f"           {lei['ementa'][:110]}")
        if r.get("achados"):
            print("       ⚠️ achada ≠ vigente: conferir revogação à mão "
                  "(?descr=REVOGA e o número da lei) e gravar data_revogacao.")
    print()
    print(barra)
    print("COMO LER")
    print(barra)
    print("  • 'nada' = ausente_conferido: o acervo PUBLICADO não tem lei do tema.")
    print("    ⚠️ Não é 'o município não legislou' — câmara pode não publicar 2009.")
    print("  • '?? incon' = inconclusivo: plataforma não automatizada, site fora,")
    print("    ou algum termo falhou. É trabalho por fazer, NÃO ausência de lei.")
    print("  • Nada aqui é resultado do ban. É saneamento de pré-período.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--csv", type=Path, default=DESTINO)
    p.add_argument("--prioridade", type=int, default=1,
                   help="varrer só alvos até esta prioridade (1 = alta pulverização)")
    p.add_argument("--limite", type=int, default=None,
                   help="máximo de municípios nesta rodada")
    p.add_argument("--refazer", action="store_true",
                   help="revisita linhas já resolvidas (padrão: não)")
    p.add_argument("--revogacao", action="store_true",
                   help="em vez de varrer, procura a revogadora de cada lei 'confirmado'")
    p.add_argument("--gravar-revogacao", action="store_true",
                   help="com --revogacao: grava só a candidata inequívoca "
                        "(cita o número E fala em revogar)")
    args = p.parse_args(argv)

    if not args.csv.exists():
        print(f"  ✘ {args.csv} não existe. Rode antes:")
        print("    python scripts/data_prep/08_alvos_legislativos.py")
        return 1

    tabela = pd.read_csv(args.csv, dtype=str, comment="#").fillna("")

    if args.revogacao:
        nova, relatorio = roda_revogacao(tabela, gravar=args.gravar_revogacao)
        print("=" * 92)
        print("REVOGAÇÃO — lei achada não é lei vigente")
        print("=" * 92)
        print("\n".join(relatorio) if relatorio else "  nenhum 'confirmado' no registro")
        if args.gravar_revogacao and not nova.equals(tabela):
            cabecalho = [l for l in args.csv.read_text(encoding="utf-8").split("\n")
                         if l.startswith("#")]
            with open(args.csv, "w", encoding="utf-8", newline="") as fh:
                for l in cabecalho:
                    fh.write(l + "\n")
                fh.write(f"# revogação conferida: {date.today().isoformat()} "
                         "por 09_varre_camaras.py --revogacao\n")
                nova.to_csv(fh, index=False)
            print(f"gravado: {args.csv}")
        return 0
    alvo = tabela[tabela["prioridade"].astype(int) <= args.prioridade]
    if not args.refazer:
        alvo = alvo[alvo["confianca"] == "nao_verificado"]
    alvo = alvo[alvo["cod_ibge6"].isin(SLUGS)]
    if args.limite:
        alvo = alvo.head(args.limite)

    if alvo.empty:
        print("  Nada a varrer — todos os alvos com slug conhecido já foram "
              "resolvidos. Use --refazer para revisitar.")
        return 0

    hoje = date.today().isoformat()
    linhas_rel, indexado = [], tabela.set_index("cod_ibge6")
    for _, linha in alvo.iterrows():
        cod = linha["cod_ibge6"]
        slug = SLUGS[cod]
        plataforma, base = detecta_plataforma(slug)

        if plataforma in ("sem_site", "desconhecida"):
            nota = {"sem_site": f"nem camara{slug} nem cm{slug} respondem",
                    "desconhecida": "portal não é plataforma A nem B"}[plataforma]
            indexado.loc[cod, ["confianca", "data_consulta", "url_fonte"]] =                 ["inconclusivo", hoje, base + "/"]
            linhas_rel.append({"municipio": linha["municipio"],
                               "plataforma": plataforma,
                               "confianca": "inconclusivo", "nota": nota})
            continue

        if plataforma == "A":
            resultado = varre_plataforma_a(base)
            nota = (f"{resultado['termos'] - resultado['erros']}/"
                    f"{resultado['termos']} termos conferidos")
        else:
            resultado = varre_plataforma_b(base)
            nota = (f"acervo de {resultado['n_acervo']} leis lido"
                    if not resultado["erros"] else "export não respondeu")
        confianca, tem_lei = classifica(resultado)
        campos = {"confianca": confianca, "tem_lei": tem_lei, "data_consulta": hoje}
        if resultado["leis"]:
            primeira = sorted(resultado["leis"], key=lambda x: x["data_lei"])[0]
            campos |= {"numero_lei": primeira["numero_lei"],
                       "data_lei": primeira["data_lei"],
                       "ementa": primeira["ementa"],
                       "url_fonte": primeira["url_fonte"], "escopo": "total"}
        else:
            campos["url_fonte"] = resultado.get("url", base + "/")
        for coluna, valor in campos.items():
            indexado.loc[cod, coluna] = valor
        linhas_rel.append({"municipio": linha["municipio"], "plataforma": plataforma,
                       "confianca": confianca, "nota": nota,
                       "achados": resultado["leis"]})

    final = indexado.reset_index()[tabela.columns.tolist()]
    cabecalho = [l for l in args.csv.read_text(encoding="utf-8").split("\n")
                 if l.startswith("#")]
    with open(args.csv, "w", encoding="utf-8", newline="") as fh:
        for l in cabecalho:
            fh.write(l + "\n")
        fh.write(f"# varredura de câmaras: {hoje} por 09_varre_camaras.py\n")
        final.to_csv(fh, index=False)

    imprime_relatorio(linhas_rel)
    print(f"\n[ok] -> {args.csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
