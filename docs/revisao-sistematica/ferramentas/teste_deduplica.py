"""Testes da deduplicação e do importador, com casos sintéticos. Sem rede e sem gravar nada.

    python3 ferramentas/teste_deduplica.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deduplica as d  # noqa: E402
import importa_exportacoes as imp  # noqa: E402


def reg(fonte, i, **kw):
    r = {"arquivo": f"{fonte.lower()}-teste.csv", "fonte": fonte, "bloco": "sq1-internacional", "linha": "#6",
         "posicao": i, "doi": "", "pmid": "", "openalex_id": "", "eid": "", "vufind_id": "", "titulo": "",
         "ano": 2020, "idiomas": {"en"}, "tipo": "article", "periodico": "", "primeiro_autor": "",
         "retratado": False, "relevancia": None, "camada_pubmed": "", "tem_resumo": True, "sha256_resumo": "x",
         "marca8": False}
    r.update(kw)
    r["doi"] = d.norm_doi(r["doi"])
    r["id_fonte"] = r["pmid"] if fonte == "PubMed" else (r["openalex_id"] or r["eid"] or r["vufind_id"]
                                                         or f"{r['arquivo']}:{i}")
    r["rotulo_linha"] = f"{fonte} {r['linha']}"
    return r


def por_titulo(unicos, trecho):
    return [u for u in unicos if d.norm_titulo(trecho) in d.norm_titulo(u["titulo"])]


def teste_chaves():
    T = "Pesticide exposure and birth weight in a Brazilian cohort"
    regs = [
        # 1. mesmo DOI com caixa e prefixo diferentes
        reg("OpenAlex", 1, openalex_id="W1", doi="https://doi.org/10.1000/ABC.1", titulo="Caso um, título A qualquer longo"),
        reg("Scopus (API)", 2, eid="2-s2.0-1", doi="10.1000/abc.1", titulo="Caso um, título B diferente e longo"),
        # 2. PMID sem DOI no PubMed, com PMID no OpenAlex
        reg("PubMed", 3, pmid="111", titulo="Caso dois no PubMed com um título bem longo"),
        reg("OpenAlex", 4, openalex_id="W2", pmid="111", titulo="Caso dois no OpenAlex, título diferente longo"),
        # 3. título com e sem acento, mesmo ano, sem IDs em comum
        reg("OASISBR", 5, vufind_id="BR_a", titulo="Exposição a agrotóxicos e malformações congênitas no Ceará"),
        reg("LA Referencia", 6, vufind_id="BR_b", titulo="EXPOSICAO A AGROTOXICOS E MALFORMACOES CONGENITAS NO CEARA"),
        # 4. mesmo título, ano diferente: não funde, marca possível duplicata
        reg("OpenAlex", 7, openalex_id="W3", titulo=T, ano=2019),
        reg("OpenAlex", 8, openalex_id="W4", titulo=T, ano=2021),
        # 5. tese e artigo com o mesmo título e ano: não funde, vira par
        reg("OASISBR", 9, vufind_id="BR_c", titulo="Agrotóxicos e desfechos ao nascer em Mato Grosso", tipo="masterThesis",
            primeiro_autor="Silva, Ana Maria"),
        reg("OpenAlex", 10, openalex_id="W5", titulo="Agrotóxicos e desfechos ao nascer em Mato Grosso",
            primeiro_autor="Ana Maria Silva"),
        # 6. título curto genérico, mesmo ano: não funde
        reg("OpenAlex", 11, openalex_id="W6", titulo="Editorial"),
        reg("OpenAlex", 12, openalex_id="W7", titulo="Editorial"),
    ]
    u = d.deduplica_pool("sq1", regs)
    assert len([x for x in u if x["n_membros"] == 2 and "10.1000/abc.1" == x["doi"]]) == 1, "1: DOI"
    assert len([x for x in u if x["pmid"] == "111"]) == 1 and [x for x in u if x["pmid"] == "111"][0]["n_membros"] == 2, "2: PMID"
    assert len(por_titulo(u, "malformac")) == 1, "3: acento"
    t4 = por_titulo(u, "brazilian cohort")
    assert len(t4) == 2 and all(x["possivel_duplicata_de"] for x in t4), "4: ano diferente"
    t5 = por_titulo(u, "mato grosso")
    assert len(t5) == 2 and {x["tese"] for x in t5} == {0, 1}, "5: tese × artigo não funde"
    pares = d.pares_tese_artigo(u)
    assert len(pares) == 1 and pares[0]["sobrenome"] == "silva", "5: par tese-artigo"
    assert len(por_titulo(u, "editorial")) == 2, "6: título curto"
    c = d.contagens("sq1", regs, u)
    assert c["unicos"] == len(u) == 9 and c["total_bruto"] == 12 and c["duplicatas_total"] == 3


def teste_exclusoes_e_representante():
    regs = [
        reg("PubMed", 1, pmid="1", titulo="Old study of pesticide spraying and stillbirth rates", ano=1985),
        reg("OpenAlex", 2, openalex_id="W1", titulo="Étude française sur les pesticides et la naissance", idiomas={"fr"}),
        reg("Scopus (API)", 3, eid="2-s2.0-9", titulo="Record without any language metadata at all", idiomas=set()),
        # versão preprint e publicada: o representante é o artigo
        reg("OpenAlex", 4, openalex_id="W8", doi="10.2139/ssrn.1", tipo="preprint",
            titulo="Aerial spraying and infant health: evidence from Ecuador", posicao=1),
        reg("OpenAlex", 5, openalex_id="W9", doi="10.1086/725349", tipo="article",
            titulo="Aerial spraying and infant health: evidence from Ecuador", posicao=2),
    ]
    u = d.deduplica_pool("sq1", regs)
    exc = {d.norm_titulo(x["titulo"])[:10]: x["exclusao_auto"] for x in u}
    assert exc["old study "] == "periodo" and exc["etude fran"] == "idioma" and exc["record wit"] == "", exc
    pub = por_titulo(u, "ecuador")[0]
    assert pub["doi"] == "10.1086/725349" and pub["id_unico"] == "doi:10.1086/725349", "vale o publicado"
    sq3 = d.deduplica_pool("sq3", [reg("OpenAlex", 1, openalex_id="W1", bloco="sq3-instrumento", linha="#5a",
                                       tipo="paratext", titulo="Front matter of a journal issue on pesticides")])
    assert sq3[0]["exclusao_auto"] == "paratext"


def teste_ordem_sq2():
    regs = [reg("OpenAlex", 1, openalex_id="WA", bloco="sq2-metodo", linha="#5", titulo="Estimador A de diferenças"),
            reg("OpenAlex", 1, openalex_id="WB", bloco="sq2-metodo", linha="#12", titulo="Item conhecido B do método"),
            reg("OpenAlex", 2, openalex_id="WA", bloco="sq2-metodo", linha="#9", titulo="Estimador A de diferenças")]
    u = d.deduplica_pool("sq2", regs)
    assert [x["openalex_id"] for x in u] == ["WB", "WA"] and [x["segmento"] for x in u] == [1, 2], "SQ2: ordem"


def teste_importador():
    ris = ("TY  - JOUR\nTI  - Pesticides and newborns in Bahia\nPY  - 2019\nDO  - https://doi.org/10.1590/X.Y\n"
           "AB  - Resumo do artigo.\nLA  - English\nAU  - Souza, A.\nT2  - Cad Saude Publica\n"
           "UR  - https://www.scopus.com/inward/record.uri?eid=2-s2.0-8506&partnerID=40\nER  - \n"
           "TY  - THES\nT1  - Dissertação sem DOI\nY1  - 2021/03/01\nER  - \n")
    rs = [imp.de_ris(r) for r in imp.le_ris(ris)]
    assert len(rs) == 2
    assert rs[0]["doi"] == "10.1590/x.y" and rs[0]["eid"] == "2-s2.0-8506" and rs[0]["ano"] == "2019"
    assert rs[0]["primeiro_autor"] == "Souza" and rs[0]["resumo"] == "Resumo do artigo."
    assert rs[1]["tipo"] == "THES" and rs[1]["ano"] == "2021" and rs[1]["doi"] == ""
    linha = {"Authors": "Silva J.; Costa M.", "Title": "A title", "Year": "2020", "DOI": "10.1/Z", "EID": "2-s2.0-5",
             "Abstract": "[No abstract available]", "Language of Original Document": "Portuguese; English"}
    c = imp.de_csv_scopus(linha)
    assert c["doi"] == "10.1/z" and c["resumo"] == "" and c["idioma"] == "Portuguese|English"
    assert d.idiomas(c["idioma"]) == {"pt", "en"}
    assert imp.PADRAO.match("scielo-sq1-S2b-2026-10-20.ris").group(3) == "S2b"
    assert imp.PADRAO.match("scopus-sq1-2026-10-20.csv").group(3) is None


if __name__ == "__main__":
    for nome, f in list(globals().items()):
        if nome.startswith("teste_") and callable(f):
            f()
            print(f"ok  {nome}")
