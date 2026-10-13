# Checklist PRISMA-S (relato da busca)

*Rethlefsen et al. 2021, Syst Rev 10:39. Estado em 2026-10-13, depois da coleta e da deduplicação.*

| # | item | estado | onde |
|---|---|---|---|
| 1 | Nome de cada base buscada | feito | `protocolo.md`, "Fontes de informação": OpenAlex, PubMed (MEDLINE), Scopus (API), OASISBR, LA Referencia; SciELO, LILACS e Scopus completo por exportação (pendentes) |
| 2 | Busca em várias bases ao mesmo tempo (plataforma) | feito | cada base buscada isoladamente, pela própria API (`ferramentas/coleta_*.py`) |
| 3 | Registros de estudos (*trial registries*) | feito | não buscados: estudos observacionais e quase-experimentais (declarar) |
| 4 | Recursos *online* e navegação (sites, literatura cinzenta) | pendente | `protocolo.md` prevê NBER, IZA, SSRN, RePEc, AgEcon, Banco Mundial, BID, IPEA, ANPEC; a busca ainda não foi rodada |
| 5 | Busca de citações | pendente | `protocolo.md`: retrospectiva e prospectiva (OpenAlex `cites:`/`referenced_works`) dos incluídos |
| 6 | Contato com autores ou especialistas | feito | não haverá contato, por viabilidade (`protocolo.md`, "Coleta de dados") |
| 7 | Outros métodos | feito | linhas de contexto (SQ1-AL #7a–#9) e itens conhecidos (SQ2 #12, SQ3 #12), no Apêndice A |
| 8 | Estratégia completa de cada base, como rodada | feito | `apendice-a-estrategias.md` (strings exatas, geradas por script); Scopus em `ferramentas/scopus_wos.md`; OASISBR e LA Referencia em `ferramentas/vufind.md` (string e fatias); filtros resolvidos em `registros/coletas.jsonl` (`filtro`, `querytranslation`, `lookfor`) |
| 9 | Limites e restrições (data, idioma, tipo) e justificativa | feito | sem limite na busca; período (≥ 1990) e idioma (en/pt/es) aplicados depois, por regra de metadado (`ferramentas/deduplica.py`), e contados no fluxograma |
| 10 | Filtros de busca publicados ou validados | feito | nenhum filtro validado; o bloco "animal" e o de mosquiteiro são próprios (Apêndice A, PRESS) |
| 11 | Trabalho prévio reaproveitado | feito | strings desenvolvidas na calibração de 2026-10-11 (`calibracao/`), com a revisão PRESS |
| 12 | Atualizações da busca | pendente | registrar se houver nova rodada antes da síntese |
| 13 | Data da busca em cada base | feito | `registros/coletas.jsonl` (`data_utc` por linha); PubMed 2026-10-12, LA Referencia, OASISBR, Scopus API e OpenAlex 2026-10-13 |
| 14 | Revisão por pares da estratégia (PRESS) | feito | PRESS 2015 feita por agente de IA independente, **não** por bibliotecário (declarar); `calibracao/*-press.json` |
| 15 | Total de registros por base | feito | `registros/contagens-prisma.json` e `prisma-fluxo.md` |
| 16 | Método de deduplicação | feito | `ferramentas/deduplica.py` (docstring): DOI → PMID → ID OpenAlex/EID/VuFind → título normalizado + ano, por *union-find*; tese × artigo não se fundem; testes em `ferramentas/teste_deduplica.py` |
