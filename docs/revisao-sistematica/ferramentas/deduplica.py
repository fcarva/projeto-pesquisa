"""Deduplicação dos registros coletados, por SQ, com as contagens do PRISMA (Etapa 3).

Entradas: todos os `registros/*.csv` dos coletores (`pubmed-*`, `openalex-*`, `scopus-api-*`,
`vufind-*`) e do importador (`importado-*`), mais `openalex-sq1-internacional-8-ids.csv` (marca de
camada). *Pools* separados: SQ1 (internacional + América Latina + fontes brasileiras +
importados `sq1`), SQ2 e SQ3. A pertença cruzada entre *pools* é registrada, não fundida.

Regra (protocolo, "Deduplicação"): chaves em ordem DOI normalizado → PMID → ID OpenAlex / EID /
ID VuFind → título normalizado + ano, unidas por *union-find*. Duas salvaguardas:
- o título só serve de chave com >= 30 caracteres normalizados (evita "Editorial", "Pesticides");
- tese/dissertação/TCC e artigo com o mesmo título **não** se fundem: o par vai para
  `pares-tese-artigo-sq1.csv`, para conferência (regra "vale o publicado", emendas v1.1 e v1.2).
O mesmo título com ano diferente também não se funde (o protocolo pede título + ano): fica em
`possivel_duplicata_de`, para o triador.

Exclusões automáticas por metadado (contadas à parte no PRISMA, nunca apagadas):
- SQ1: todos os anos conhecidos < 1990 ("periodo"); idiomas conhecidos, nenhum en/pt/es ("idioma");
- SQ3: OpenAlex `paratext` ("paratext") ou retratado ("retratado").

Ordem de triagem: as `screening_priority_rule` dos `calibracao/*-final.json`. SQ1: camada
informativa (tudo é triado). SQ2: segmentos 1 (#12), 2 (#9-#11), 3 (#7), 4 (#5, por relevância;
a regra de parada vale só aqui). SQ3: camadas 1 (#5a, #7a-c, #8, #9, #10, #12), 2 (#5b, #6, #11)
e 3 (#5c, depois PubMed P1); a regra de parada vale dentro de cada camada. O registro fica na
primeira ocorrência (camada mais alta) e, dentro dela, na ordem da linha e da posição de relevância.

Contagens (por pool): `total_bruto` (soma das linhas) − `sobreposicao_entre_linhas` (o mesmo ID
em mais de uma linha da mesma fonte) − `duplicatas_por_chave` (IDs diferentes com o mesmo DOI,
PMID ou título + ano, entre fontes ou dentro de uma, como obras duplicadas no OpenAlex) =
`unicos`; `unicos` − `excluidos_por_metadado` = `a_triar`. No PRISMA, "duplicatas removidas" =
`duplicatas_total` = as duas primeiras parcelas.

Resumo: `tem_resumo` diz se alguma fonte coletada trouxe o resumo; `resumo_hidratado` diz de
onde veio o resumo buscado depois por DOI (`hidrata_resumos.py` -> `registros/resumos-hidratados.csv`).

Saídas: `registros/deduplicado-sq{1,2,3}.csv`, `registros/pares-tese-artigo-sq1.csv` e
`registros/contagens-prisma.json`, cujas identidades o script confere. Nas saídas, o ID VuFind
`PAÍS_<32 hex>` é gravado como `PAÍS/<32 hex>`: o *push protection* do GitHub confunde
`ES_<32 hex>` com a chave secreta do hCaptcha (ver `coleta_vufind.py`). Para voltar ao ID da
API, trocar a primeira `/` por `_`.

    python3 ferramentas/deduplica.py
"""
import csv
import glob
import hashlib
import json
import math
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(os.path.dirname(AQUI), "registros")

POOLS = {"sq1": ("sq1-internacional", "sq1-america-latina", "sq1"),
         "sq2": ("sq2-metodo", "sq2"),
         "sq3": ("sq3-instrumento", "sq3")}
# Prioridade de fonte para os metadados do representante.
PRIORIDADE = ["PubMed", "OpenAlex", "Scopus (exportação)", "Scopus (API)", "SciELO", "LILACS", "OASISBR",
              "LA Referencia"]
IDIOMA = {"en": "en", "eng": "en", "english": "en", "inglês": "en", "ingles": "en",
          "pt": "pt", "por": "pt", "portuguese": "pt", "português": "pt", "portugues": "pt",
          "es": "es", "spa": "es", "spanish": "es", "espanhol": "es", "español": "es"}
IDIOMAS_OK = {"en", "pt", "es"}
TESE_TIPOS = {"dissertation", "masterthesis", "doctoralthesis", "bachelorthesis", "thes", "thesis"}
MIN_TITULO = 30
ANO_MIN_SQ1 = 1990

# SQ1-AL: linhas de efeito (camada 1), rede de idioma (camada 2) e de contexto (camada 3).
AL_EFEITO = {"OA #4", "OA #6", "S1'", "S3", "L1'"}
AL_IDIOMA = {"OA #5"}
AL_CONTEXTO = {"OA #7a", "OA #7b", "OA #8", "OA #9", "S2'", "S2b", "L2''", "L2b"}
# SQ2 e SQ3: segmentos/camadas e ordem das linhas dentro deles.
SQ2_SEGMENTOS = [["#12"], ["#9", "#10", "#11"], ["#7"], ["#5"]]
SQ3_CAMADAS = [["#5a", "#7a", "#7b", "#7c", "#8", "#9", "#10", "#12"], ["#5b", "#6", "#11"], ["#5c", "P1"]]


# ---------------------------------------------------------------- normalização

def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", d)
    return d.rstrip(".,;)") if d.startswith("10.") else ""


def norm_titulo(t):
    t = re.sub(r"<[^>]+>", " ", t or "")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())


def ano_int(a):
    m = re.search(r"\d{4}", str(a or ""))
    return int(m.group(0)) if m else None


def idiomas(s):
    out = set()
    for x in re.split(r"[|;,]", s or ""):
        x = x.strip().lower()
        if x:
            out.add(IDIOMA.get(x, x))
    return out


def sobrenome(nome):
    nome = (nome or "").strip()
    if not nome:
        return ""
    s = nome.split(",")[0] if "," in nome else nome.split()[-1]
    return norm_titulo(s)


def eh_tese(tipo):
    return any(t.strip().lower() in TESE_TIPOS for t in (tipo or "").split("|"))


# ---------------------------------------------------------------- leitura

def le_csv(caminho):
    return list(csv.DictReader(open(caminho, encoding="utf-8")))


def carrega():
    """Todos os registros, num esquema comum. Cada um sabe a fonte, a linha e o arquivo."""
    marca8 = set()
    p8 = os.path.join(REG, "openalex-sq1-internacional-8-ids.csv")
    if os.path.exists(p8):
        marca8 = {l["openalex_id"] for l in le_csv(p8)}
    regs = []
    for caminho in sorted(glob.glob(os.path.join(REG, "*.csv"))):
        nome = os.path.basename(caminho)
        if nome.startswith(("deduplicado-", "pares-")) or nome.endswith("-ids.csv"):
            continue
        for l in le_csv(caminho):
            fonte = l.get("fonte", "")
            r = {
                "arquivo": nome, "fonte": fonte, "bloco": l.get("bloco", ""), "linha": l.get("linha", ""),
                "posicao": int(l["posicao"]) if l.get("posicao", "").isdigit() else None,
                "doi": norm_doi(l.get("doi")), "pmid": (l.get("pmid") or "").strip(),
                "openalex_id": (l.get("openalex_id") or "").strip(), "eid": (l.get("eid") or "").strip(),
                "vufind_id": "", "titulo": " ".join((l.get("titulo") or "").split()),
                "ano": ano_int(l.get("ano")), "idiomas": idiomas(l.get("idioma") or l.get("idiomas")),
                "tipo": l.get("tipo") or l.get("formato") or l.get("tipos_publicacao") or "",
                "periodico": l.get("periodico", ""), "primeiro_autor": l.get("primeiro_autor", ""),
                "retratado": l.get("retratado") == "1" or "Retracted Publication" in l.get("tipos_publicacao", ""),
                "relevancia": float(l["relevance_score"]) if l.get("relevance_score") else None,
                "camada_pubmed": l.get("camada", ""), "tem_resumo": l.get("tem_resumo") == "1",
                "sha256_resumo": l.get("sha256_resumo", ""),
            }
            if nome.startswith("vufind-"):
                pais, h = l.get("vufind_pais", ""), l.get("vufind_hash", "")
                r["vufind_id"] = f"{pais}_{h}" if pais else h
            r["marca8"] = r["openalex_id"] in marca8 and r["bloco"] == "sq1-internacional"
            r["id_fonte"] = r["pmid"] if fonte == "PubMed" else (
                r["openalex_id"] or r["eid"] or r["vufind_id"] or r["doi"] or f"{nome}:{r['posicao']}")
            r["rotulo_linha"] = f"{fonte} {r['linha']}".strip()
            regs.append(r)
    return regs


def pool_de(r):
    for p, blocos in POOLS.items():
        if r["bloco"] in blocos:
            return p
    raise ValueError(f"bloco desconhecido: {r['bloco']} ({r['arquivo']})")


# ---------------------------------------------------------------- agrupamento

class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def acha(self, i):
        while self.p[i] != i:
            self.p[i] = self.p[self.p[i]]
            i = self.p[i]
        return i

    def une(self, a, b):
        a, b = self.acha(a), self.acha(b)
        if a != b:
            self.p[max(a, b)] = min(a, b)


def chaves(r):
    ks = []
    if r["doi"]:
        ks.append(("doi", r["doi"]))
    if r["pmid"]:
        ks.append(("pmid", r["pmid"]))
    if r["openalex_id"]:
        ks.append(("oa", r["openalex_id"]))
    if r["eid"]:
        ks.append(("eid", r["eid"]))
    if r["vufind_id"]:
        ks.append(("vf", r["vufind_id"]))
    t = norm_titulo(r["titulo"])
    if len(t) >= MIN_TITULO and r["ano"]:
        ks.append(("tit", t, r["ano"], "tese" if eh_tese(r["tipo"]) else "outro"))
    return ks


def agrupa(regs):
    """Componentes de registros que compartilham alguma chave."""
    uf = UF(len(regs))
    dono = {}
    for i, r in enumerate(regs):
        for k in chaves(r):
            if k in dono:
                uf.une(i, dono[k])
            else:
                dono[k] = i
    comps = defaultdict(list)
    for i in range(len(regs)):
        comps[uf.acha(i)].append(regs[i])
    return list(comps.values())


PUBLICADO = ("article", "journal article", "review", "letter")


def prioridade(r):
    """Fonte (PRIORIDADE) e, dentro dela, a versão publicada antes de preprint, relatório, dataset ou
    resumo de congresso: o representante segue a regra "vale o publicado"."""
    tipo = (r["tipo"] or "").split("|")[0].strip().lower()
    return (PRIORIDADE.index(r["fonte"]) if r["fonte"] in PRIORIDADE else 99,
            0 if tipo in PUBLICADO else 1, r["posicao"] or 10 ** 9)


def representante(membros):
    return min(membros, key=prioridade)


def primeiro(membros, campo):
    for r in sorted(membros, key=prioridade):
        if r[campo]:
            return r[campo]
    return ""


def id_unico(membros):
    for campo, pre in (("doi", "doi"), ("pmid", "pmid"), ("openalex_id", "oa"), ("eid", "eid"), ("vufind_id", "vf")):
        v = primeiro(membros, campo)
        if v:
            return f"{pre}:{v}"
    r = representante(membros)
    return "tit:" + hashlib.sha1(f"{norm_titulo(r['titulo'])}|{r['ano']}".encode()).hexdigest()[:12]


# ---------------------------------------------------------------- regras por pool

def exclusao_auto(pool, membros):
    if pool == "sq1":
        anos = [r["ano"] for r in membros if r["ano"]]
        if anos and max(anos) < ANO_MIN_SQ1:
            return "periodo"
        langs = set().union(*(r["idiomas"] for r in membros))
        if langs and not langs & IDIOMAS_OK:
            return "idioma"
    if pool == "sq3":
        if any(r["fonte"] == "OpenAlex" and r["tipo"] == "paratext" for r in membros):
            return "paratext"
        if any(r["retratado"] for r in membros):
            return "retratado"
    return ""


def camadas_sq1(membros):
    intl = [r for r in membros if r["bloco"] == "sq1-internacional" and r["fonte"] in ("OpenAlex", "PubMed")]
    if not intl:
        c_intl = ""
    elif any(r["marca8"] or r["camada_pubmed"] == "1" for r in intl):
        c_intl = 1
    else:
        c_intl = 2
    linhas_al = {r["linha"] for r in membros if r["bloco"] in ("sq1-america-latina", "sq1")}
    vufind = any(r["fonte"] in ("OASISBR", "LA Referencia") for r in membros)
    if linhas_al & AL_EFEITO or vufind:
        c_al = 1
    elif linhas_al & AL_IDIOMA:
        c_al = 2
    elif linhas_al & AL_CONTEXTO:
        c_al = 3
    else:
        c_al = ""
    flags = []
    if linhas_al & AL_CONTEXTO:
        flags.append("contexto")
    if "OA #9" in linhas_al:
        flags.append("ensaio2")
    if c_al == 2:
        flags.append("rede_idioma")
    conhecidas = [c for c in (c_intl, c_al) if c != ""]
    # Só no Scopus (string SQ1 sem bloco de contexto): sem marca; triado depois da camada 1.
    return c_intl, c_al, (min(conhecidas) if conhecidas else 2), flags


def segmento(pool, membros):
    """(segmento, índice da linha no segmento, posição na linha) da primeira ocorrência."""
    grade = SQ2_SEGMENTOS if pool == "sq2" else SQ3_CAMADAS
    melhor = None
    for r in membros:
        for s, linhas in enumerate(grade, 1):
            if r["linha"] in linhas:
                k = (s, linhas.index(r["linha"]), r["posicao"] or 10 ** 9)
                melhor = k if melhor is None or k < melhor else melhor
    return melhor or (len(grade) + 1, 0, 10 ** 9)


# ---------------------------------------------------------------- pares tese ↔ artigo

PALAVRAS_VAZIAS = set("a o as os de da do das dos e em no na nos nas para por com sem um uma the of and in on for "
                      "to with by an at from la el los las del y en".split())


def tokens(t):
    return {w for w in norm_titulo(t).split() if w not in PALAVRAS_VAZIAS and len(w) > 2}


def pares_tese_artigo(unicos):
    teses = [u for u in unicos if u["tese"]]
    artigos = [u for u in unicos if not u["tese"]]
    por_sobrenome = defaultdict(list)
    for a in artigos:
        if a["sobrenome"]:
            por_sobrenome[a["sobrenome"]].append(a)
    pares = []
    for t in teses:
        tt = tokens(t["titulo"])
        for a in por_sobrenome.get(t["sobrenome"], []):
            if t["ano"] and a["ano"] and a["ano"] < t["ano"]:
                continue
            ta = tokens(a["titulo"])
            jac = len(tt & ta) / len(tt | ta) if tt | ta else 0
            if jac >= 0.4 or norm_titulo(t["titulo"]) == norm_titulo(a["titulo"]):
                pares.append({"id_tese": t["id_unico"], "id_artigo": a["id_unico"], "sobrenome": t["sobrenome"],
                              "similaridade_titulo": round(jac, 2), "ano_tese": t["ano"], "ano_artigo": a["ano"],
                              "tipo_tese": t["tipo"], "titulo_tese": t["titulo"], "titulo_artigo": a["titulo"]})
    return pares


# ---------------------------------------------------------------- pipeline

def hidratados():
    """DOI -> fonte do resumo hidratado (`hidrata_resumos.py`), se houver."""
    caminho = os.path.join(REG, "resumos-hidratados.csv")
    if not os.path.exists(caminho):
        return {}
    return {l["doi"]: l["fonte_resumo"] for l in le_csv(caminho) if l["fonte_resumo"]}


def deduplica_pool(pool, regs, hidr=None):
    hidr = hidr or {}
    comps = agrupa(regs)
    unicos = []
    for membros in comps:
        rep = representante(membros)
        u = {
            "id_unico": id_unico(membros),
            "doi": primeiro(membros, "doi"), "pmid": primeiro(membros, "pmid"),
            "openalex_id": primeiro(membros, "openalex_id"), "eid": primeiro(membros, "eid"),
            "vufind_ids": "|".join(sorted({r["vufind_id"] for r in membros if r["vufind_id"]})),
            "titulo": rep["titulo"] or primeiro(membros, "titulo"), "ano": rep["ano"] or primeiro(membros, "ano"),
            "idiomas": "|".join(sorted(set().union(*(r["idiomas"] for r in membros)))),
            "tipo": rep["tipo"] or primeiro(membros, "tipo"),
            "tese": int(any(eh_tese(r["tipo"]) for r in membros)),
            "primeiro_autor": primeiro(membros, "primeiro_autor"),
            "periodico": primeiro(membros, "periodico"),
            "fontes": "|".join(sorted({r["fonte"] for r in membros})),
            "linhas": "|".join(sorted({r["rotulo_linha"] for r in membros})),
            "n_membros": len(membros),
            "tem_resumo": int(any(r["tem_resumo"] for r in membros)),
            "resumo_em": "|".join(sorted({f"{r['fonte']}:{r['id_fonte']}" for r in membros if r["tem_resumo"]})),
            "resumo_hidratado": "",
            "retratado": int(any(r["retratado"] for r in membros)),
            "exclusao_auto": exclusao_auto(pool, membros),
            "membros": "|".join(sorted({f"{r['arquivo']}:{r['id_fonte']}" for r in membros})),
        }
        if not u["tem_resumo"] and u["doi"] in hidr:
            u["resumo_hidratado"] = hidr[u["doi"]]
        u["sobrenome"] = sobrenome(u["primeiro_autor"])
        if pool == "sq1":
            u["camada_intl"], u["camada_al"], u["camada"], flags = camadas_sq1(membros)
            u["flags"] = "|".join(flags)
            pos6 = min((r["posicao"] for r in membros if r["linha"] == "#6" and r["fonte"] == "OpenAlex"
                        and r["posicao"]), default=10 ** 9)
            u["_ordem"] = (u["camada"], pos6, -(u["ano"] or 0), u["id_unico"])
        else:
            s, li, pos = segmento(pool, membros)
            u["segmento"] = s
            flags = []
            if pool == "sq3" and any(r["linha"] in ("#7b", "#9") for r in membros):
                flags.append("marcar_sq1")  # nota (c) do -final.json da SQ3
            u["flags"] = "|".join(flags)
            u["_ordem"] = (s, li, pos, u["id_unico"])
        u["_membros"] = membros
        unicos.append(u)
    unicos.sort(key=lambda u: u["_ordem"])
    for k, u in enumerate(unicos, 1):
        u["ordem"] = k
    # Mesmo título (>= MIN_TITULO) em componentes diferentes: ano diferente ou tese × artigo.
    por_tit = defaultdict(list)
    for u in unicos:
        t = norm_titulo(u["titulo"])
        if len(t) >= MIN_TITULO:
            por_tit[t].append(u["id_unico"])
    for u in unicos:
        outros = [i for i in por_tit.get(norm_titulo(u["titulo"]), []) if i != u["id_unico"]]
        u["possivel_duplicata_de"] = "|".join(outros)
    assert len({u["id_unico"] for u in unicos}) == len(unicos), f"{pool}: id_unico repetido"
    return unicos


def contagens(pool, regs, unicos):
    por_fonte = {}
    for f in sorted({r["fonte"] for r in regs}):
        rf = [r for r in regs if r["fonte"] == f]
        por_fonte[f] = {"linhas": dict(sorted(Counter(r["linha"] for r in rf).items())),
                        "bruto": len(rf), "distintos_na_fonte": len({r["id_fonte"] for r in rf})}
    bruto = sum(v["bruto"] for v in por_fonte.values())
    distintos = sum(v["distintos_na_fonte"] for v in por_fonte.values())
    excl = Counter(u["exclusao_auto"] for u in unicos if u["exclusao_auto"])
    c = {
        "identificados_por_fonte": por_fonte,
        "total_bruto": bruto,
        "sobreposicao_entre_linhas": bruto - distintos,
        "total_distintos_por_fonte": distintos,
        "duplicatas_por_chave": distintos - len(unicos),
        "duplicatas_total": bruto - len(unicos),
        "unicos": len(unicos),
        "excluidos_por_metadado": dict(excl),
        "a_triar": len(unicos) - sum(excl.values()),
        "teses_dissertacoes_tccs": sum(u["tese"] for u in unicos),
        "com_resumo": sum(u["tem_resumo"] for u in unicos),
        "com_resumo_hidratado": sum(1 for u in unicos if u["resumo_hidratado"]),
        "possiveis_duplicatas": sum(1 for u in unicos if u["possivel_duplicata_de"]),
        "exclusivos_por_fonte_a_triar": dict(sorted(Counter(
            u["fontes"] for u in unicos if "|" not in u["fontes"] and not u["exclusao_auto"]).items())),
        "sem_resumo_a_triar": sum(1 for u in unicos if not u["tem_resumo"] and not u["resumo_hidratado"]
                                  and not u["exclusao_auto"]),
        "sem_resumo_a_triar_por_fonte": dict(sorted(Counter(
            u["fontes"] for u in unicos if not u["tem_resumo"] and not u["resumo_hidratado"]
            and not u["exclusao_auto"]).items(), key=lambda kv: -kv[1])[:8]),
    }
    # Identidades do fluxograma.
    assert c["total_bruto"] - c["sobreposicao_entre_linhas"] - c["duplicatas_por_chave"] == c["unicos"]
    assert c["duplicatas_total"] == c["sobreposicao_entre_linhas"] + c["duplicatas_por_chave"]
    assert c["unicos"] - sum(excl.values()) == c["a_triar"]
    a_triar = [u for u in unicos if not u["exclusao_auto"]]
    if pool == "sq1":
        c["por_camada"] = dict(sorted(Counter(u["camada"] for u in a_triar).items()))
    else:
        tam = Counter(u["segmento"] for u in a_triar)
        c["por_segmento"] = {str(s): {"registros": n, "piso_30pct": math.ceil(0.3 * n)}
                             for s, n in sorted(tam.items())}
    return c


VUFIND_ID = re.compile(r"\b([A-Za-z0-9-]+)_([0-9a-f]{32})\b")


def seguro(v):
    """ID VuFind PAÍS_<hash> -> PAÍS/<hash> nas saídas (falso positivo do push protection)."""
    return VUFIND_ID.sub(r"\1/\2", v) if isinstance(v, str) else v


COLUNAS = ["ordem", "id_unico", "exclusao_auto", "camada", "camada_intl", "camada_al", "segmento", "flags",
           "titulo", "ano", "tipo", "tese", "idiomas", "primeiro_autor", "periodico", "doi", "pmid", "openalex_id",
           "eid", "vufind_ids", "fontes", "linhas", "n_membros", "tem_resumo", "resumo_em", "resumo_hidratado", "retratado",
           "tambem_em", "possivel_duplicata_de", "membros"]


def grava(pool, unicos):
    cols = [c for c in COLUNAS if not (pool == "sq1" and c == "segmento")
            and not (pool != "sq1" and c in ("camada", "camada_intl", "camada_al"))]
    with open(os.path.join(REG, f"deduplicado-{pool}.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for u in unicos:
            w.writerow({k: seguro(v) for k, v in u.items() if k in cols})


def roda():
    regs = carrega()
    por_pool = defaultdict(list)
    for r in regs:
        por_pool[pool_de(r)].append(r)
    resultado, todos = {}, {}
    hidr = hidratados()
    for pool in POOLS:
        todos[pool] = deduplica_pool(pool, por_pool[pool], hidr)
        resultado[pool] = contagens(pool, por_pool[pool], todos[pool])
    # Pertença cruzada: chaves de cada pool.
    chaves_pool = {p: {k for u in us for r in u["_membros"] for k in chaves(r)} for p, us in todos.items()}
    for p, us in todos.items():
        for u in us:
            ks = {k for r in u["_membros"] for k in chaves(r)}
            u["tambem_em"] = "|".join(q for q in POOLS if q != p and ks & chaves_pool[q])
        resultado[p]["tambem_em_outro_pool"] = sum(1 for u in us if u["tambem_em"])
    for p, us in todos.items():
        grava(p, us)
    pares = pares_tese_artigo(todos["sq1"])
    with open(os.path.join(REG, "pares-tese-artigo-sq1.csv"), "w", newline="", encoding="utf-8") as f:
        cols = ["id_tese", "id_artigo", "sobrenome", "similaridade_titulo", "ano_tese", "ano_artigo", "tipo_tese",
                "titulo_tese", "titulo_artigo"]
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows({k: seguro(v) for k, v in p.items()} for p in sorted(pares, key=lambda p: -p["similaridade_titulo"]))
    resultado["sq1"]["pares_tese_artigo"] = len(pares)
    json.dump(resultado, open(os.path.join(REG, "contagens-prisma.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    for p, c in resultado.items():
        print(f"{p}: bruto {c['total_bruto']}, únicos {c['unicos']}, excluídos {c['excluidos_por_metadado']}, "
              f"a triar {c['a_triar']}", file=sys.stderr)
    return resultado


if __name__ == "__main__":
    roda()
