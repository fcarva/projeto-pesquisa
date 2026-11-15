# Academic Integrity Verification Report

*ARS v3.24.2 · `integrity_verification_agent` · Estágio 2.5 · execução em 2026-11-15T21:43Z (UTC).
Manuscrito: `paper/projeto/projeto.tex` + `paper/projeto/secoes/01…08` (PDF compilado às 21:16Z, 19 páginas, 14 textuais).
Bibliografia: `paper/referencias.bib` + `paper/projeto/referencias-projeto.bib`.
Este agente não editou o manuscrito, os `.bib` nem qualquer outro arquivo do repositório; este relatório é o único arquivo gravado.*

## Verification Mode

Initial Verification (Mode 1, pre-review)

## Verdict

**FAIL**

Motivo: 2 issues SERIOUS (3 afirmações com veredito MAJOR_DISTORTION) e 1 issue MEDIUM. À parte do veredito, o checklist de modos de falha tem três resultados que fecham o checkpoint (Modos 1, 3 e 6) e a verificação C4/D7 tem uma condição heurística acionada. As 28 referências citadas existem e conferem; nenhum número de estimativa foi encontrado no texto.

## Verification Summary

| Category | Total | Passed | Issues |
|----------|-------|--------|--------|
| Reference Existence | 28 (população registrada = chaves citadas nos `.tex`) | 28 | 0 |
| Bibliographic Accuracy | 28 | 23 | 5 MINOR (registro incompleto ou versão não fixada) |
| Ghost Citations | -- | -- | 0 órfãs na lista impressa / 0 pendentes (27 entradas dos `.bib` não são citadas e por isso não são impressas) |
| Citation Context Accuracy | 28 de 28 chaves (48 ocorrências; 100%, acima dos 30% exigidos) | 19 | 3 MINOR (afetam 5 chaves); outras 4 chaves com acesso limitado (notas) |
| Statistical Data Accuracy | 13 superfícies numéricas ou factuais | 11 | 1 SERIOUS (duas contagens, mesma causa) |
| Internal Consistency | -- | Fail | 3 inconsistências (2 SERIOUS, 1 MEDIUM) |
| Originality Check (D1) | 17 de 51 parágrafos (33%) | 17 | 0 (CLOSE_MATCH / VERBATIM) |
| Self-Plagiarism (D2) | 1 comparação interna (rascunho de qualificação do próprio autor); busca externa pelo nome do autor não executada | 1 | 0 |
| Claim Verification (E) | 46 de 50 registradas (Mode 1: HIGH-IMPACT: 34, RANDOM: 0, TOP-UP: 12; NOT-SELECTED: 4, tratadas só no E5; semantic extraction coverage: not_machine_detectable; candidate gaps: não medido, ver E1-COVERAGE-UNRESOLVED) | 30 | 3 MAJOR_DISTORTION / 0 UNVERIFIABLE (mais 3 MINOR_DISTORTION e 10 UNVERIFIABLE_ACCESS) |

Restrições do autor, conferidas:

| Restrição | Resultado |
|---|---|
| Nenhum número de estimativa (efeito estimado pelo autor, IC, p-valor) | Nenhum encontrado. Os únicos valores de efeito são da literatura (23 a 32 g; 80 a 150 g). Há, porém, uma frase que relata o comportamento de uma estimativa já feita (`05-metodologia.tex:79-80`), tratada em IL-SERIOUS-2. |
| No máximo 15 páginas textuais | 14 páginas textuais (numeração impressa 3 a 16; referências a partir da 17). |
| Só o Ensaio 1 | O Ensaio 2 aparece como remissão em `03-referencial.tex:26-29` e `08-cronograma.tex:15-18`, e como linha do cronograma em `08-cronograma.tex:40`. Nenhum conteúdo do Ensaio 2 é desenvolvido. |

## Phase A: Reference Verification Results

População registrada: 28 chaves citadas com `\cite{}` ou `\citeonline{}` (20 em `referencias.bib`, 8 em `referencias-projeto.bib`). A lista impressa (`projeto.bbl`) tem 28 itens, igual à população.

**A0 (Semantic Scholar, lote único):** a API respondeu (HTTP 200). 22 `S2_VERIFIED`, 6 `S2_NOT_FOUND` (arkhangelsky2021sdid, callaway2021multiple, callaway2024continuous, rambachan2023credible, buckles2013season, olden2022triple), 0 `DOI_MISMATCH`. As 6 não encontradas no S2 seguiram para A1.

**A1/A2 (Crossref `api.crossref.org/works/<doi>` para os 27 DOIs; `export.arxiv.org` para o arXiv):** os 27 DOIs resolvem para a obra citada, com autores, título, periódico, volume, número e páginas iguais aos do `.bib`, salvo os cinco registros abaixo.

| Chave | Veredito A1 | Observação A2 |
|---|---|---|
| arkhangelsky2021sdid, callaway2021multiple, calzada2023bananas, camacho2017health, cameron2008wild, coase1960, conley2011, dechaisemartin2020, dias2023down, goodmanbacon2021, helfand1995, lichtenberg1988, rambachan2023credible, roth2023trending, skevas2012, brainerd2014seasonal, currie2013within, buckles2013season, olden2022triple, ferman2019inference, chernozhukov2021conformal, mackinnon2018wild | VERIFIED | Todos os campos conferem com o Crossref. |
| callaway2024continuous | VERIFIED | NBER WP 32117, DOI 10.3386/w32117. Existe versão posterior do mesmo trabalho (arXiv:2107.02637v5; versão dos autores de dez/2025) com notação alterada; o `.bib` fixa a do NBER, que foi a versão lida. |
| bocker2020glyphosate | VERIFIED | Ano no `.bib`: 2019 (publicação online, igual ao Crossref). Volume, número e páginas ausentes. O RePEc lista ERAE v. 47, n. 2, p. 371-402, 2020. A chave diz 2020 e o campo diz 2019. IL-MINOR-7. |
| larsen2017agricultural | VERIFIED | Falta o número do artigo (Crossref: 302). IL-MINOR-8. |
| reynier2025glyphosate | VERIFIED | Falta o número do artigo (Crossref: e2413013121). IL-MINOR-9. |
| weitzman1974 | VERIFIED | `pages = {477}` (igual ao depósito do Crossref, que só traz a primeira página). O intervalo 477-491 aparece em fonte secundária; conferir no JSTOR. IL-MINOR-10. |
| denteh2022misclassification | VERIFIED | arXiv:2207.11890 existe; autores e título conferem. O `.bib` não fixa a versão. A versão corrente é a v3, de 30/04/2026; o Corolário 1 usado no projeto foi lido nela. IL-MINOR-11. |

**A3 (citações fantasma):** 0 citações pendentes. 27 entradas dos `.bib` não são citadas no projeto e não foram verificadas a fundo: baker2026practitioner, borusyak2022shiftshare, borusyak2024, borusyak2025formula, bravoureta2020psmdid, bustos2016agricultural, callaway2024eventstudy, canay2021wild, chatzimichael2021pesticide, fernandezcornejo1998, finger2024europe, frank2024ecosystem, frank2024vultures, goldsmithpinkham2020bartik, greenstone2014india, henningsen2025causal, keiser2018cwa, neginegi2025misclassified, rocha2017chapada, roth2002engineer, rull2003misclassification, santanna2020drdid, sasaki2024extreme, shirangi2010living, sorensen2025birth, sunabraham2021, voica2021trading. Como o BibTeX só imprime o que é citado, elas não geram órfãs no PDF.

O cabeçalho de `referencias-projeto.bib` diz que `referencias.bib` tem "47 entradas, verificadas no Crossref". Esta execução verificou só as 20 citadas; as outras 27 ficam fora do denominador.

## Phase B: Citation Context Verification Results

Todas as 28 chaves tiveram o contexto conferido contra o resumo da versão citada ou contra texto completo, como indicado.

| Chave | Local | O que o texto atribui | Resultado | Base |
|---|---|---|---|---|
| dias2023down | 01:38-40 | soja transgênica, fluxo d'água, piora a jusante | Confere | resumo (Crossref) |
| reynier2025glyphosate | 01:40-43; 03:37-39; 03:46-48; 05:86-87 | aptidão como fonte de variação; 23 a 32 g; cauda inferior | Confere | texto completo (PMC11761964, Discussão) |
| larsen2017agricultural | 01:44-47; 03:46 | efeito só no topo da exposição | Confere | resumo |
| camacho2017health | 01:50-51 | aspersão aérea de herbicida, Colômbia | Confere | resumo |
| calzada2023bananas | 01:52-56; 02:55-57; 02:67-68; 03:40-43; 03:53-54; 01:93 | 80 a 150 g com exposição alta; primeiro trimestre; estação chuvosa | Parcial: 80 a 150 g confere no resumo publicado. Primeiro trimestre e estação chuvosa não estão no resumo, e o texto completo da versão publicada não pôde ser lido | resumo publicado; ver IL-MINOR-1 |
| weitzman1974 | 01:60; 03:22 | preço e quantidade sob incerteza de custos; inclinações relativas | Acesso limitado | só metadados; conteúdo descrito de forma concordante em fontes secundárias |
| lichtenberg1988, helfand1995 | 01:60; 03:25 | dimensão distributiva na regulação de agrotóxicos | Confere | resumos |
| bocker2020glyphosate | 01:61 | simulação do banimento de molécula | Confere | resumo (S2) |
| callaway2024continuous | 01:92; 03:69-75; 05:68 | `ATT(d\|d)` sob tendências paralelas; curva exige hipótese forte | Confere | PDF do NBER WP 32117 (trechos) |
| brainerd2014seasonal | 01:93; 03:54-55 | mês da concepção e estação de aplicação de agroquímicos, Índia | Confere | versão final dos autores do JDE (trechos) |
| coase1960 | 03:14 | direitos definidos e custos de transação baixos | Acesso limitado | só metadados |
| skevas2012 | 03:26 | "comparação empírica entre cotas e taxas" | Imprecisão: é modelo de simulação de política. IL-MINOR-2 | resumo |
| buckles2013season, currie2013within | 03:58 | composição sazonal das mães | Confere | resumos (PMC; Crossref) |
| callaway2021multiple, goodmanbacon2021, dechaisemartin2020 | 03:64 | "estimadores para adoção escalonada" | Imprecisão de rótulo. IL-MINOR-3 | resumos |
| olden2022triple | 03:77; 05:143 | uma única hipótese de tendências paralelas | Confere | resumo |
| denteh2022misclassification | 03:80-84; 05:37 | atenuação pelo VPP, sem falso negativo | O Corolário 1 da v3 diz exatamente isso; a entrada não fixa a versão | arXiv v3 (PDF) |
| conley2011 | 03:86; 05:189 | distribuição de referência tirada do grupo numeroso | Confere | resumo (NBER/RePEc) |
| ferman2019inference | 03:86; 05:189-191 | heterocedasticidade por tamanho de grupo | Confere | resumo |
| chernozhukov2021conformal | 03:87; 05:192 | inferência conformal para contrafactuais | Confere | resumo |
| cameron2008wild | 03:89 | wild cluster bootstrap | Acesso limitado | só metadados |
| mackinnon2018wild | 03:89 | restrições do wild bootstrap com poucos tratados | Confere | resumo |
| roth2023trending | 05:92 | teste de pré-tendência pode não ter poder | Confere | texto (ScienceDirect, introdução; arXiv, seção 4.4) |
| rambachan2023credible | 05:95 | intervalos robustos a violações limitadas | Confere | resumo |
| arkhangelsky2021sdid | 05:155 | diferenças-em-diferenças sintético | Confere | resumo |

**B2 (formato):** abntex2cite no sistema autor-data, usado de modo uniforme. Fontes normativas e de dados são mencionadas no texto sem entrada na lista de referências (IL-MINOR-12).

## Phase C: Data Verification Results

### C1. Números e fatos, um a um

Legenda da fonte: **primária** = documento ou base original consultada nesta execução; **primária (cópia no repositório)** = transcrição do documento oficial guardada em `docs/legislacao/`; **secundária externa** = imprensa, artigo ou portal que relata o fato; **secundária interna** = documento do próprio repositório, não refeito aqui.

| # | Afirmação | Local | Resultado | Fonte e tipo |
|---|---|---|---|---|
| 1 | 184 municípios no Ceará | 02:16; 06:7-8 | Confere | primária: SIDRA devolve 184 municípios para a UF 23 |
| 2 | Censo Agropecuário 2006: 36 estabelecimentos com aplicação por aeronave, em 7 municípios | 02:73-75 | Confere | primária: SIDRA, tabela 1008, variável 2020, categoria "Por aeronave", consultada hoje. Aiuaba 5, Jaguaruana 1, Limoeiro do Norte 18, Mauriti 1, Quiterianópolis 1, Quixeramobim 1, Quixeré 9; soma 36 |
| 3 | Os 7 são produtores de banana; nenhum município sem banana tinha aplicação aérea | 02:75-76; 05:28-29 | Confere nas duas janelas de dose | primária: SIDRA 1008 cruzada com PAM (tabela 5457, área plantada, banana) |
| 4 | "169 municípios com área de banana" | 02:77 | **Não confere com a janela que o texto declara principal** | primária: PAM/SIDRA. Média 2015-2018: 169 com área e 15 sem. Média 2010-2014: 178 com área e 6 sem. IL-SERIOUS-1 |
| 5 | "15 municípios sem área de banana" | 05:79 | **Idem** | idem. Os 6 de área nula em 2010-2014: Arneiroz, Fortim, Horizonte, Ibicuitinga, Palhano, Potiretama |
| 6 | Tabela do Dossiê ABRASCO no PL 18/2015: 23 pontos, 2009; procimidona e carbaril em todos; carbofurano 18; fenitrotiona 16; glifosato 4 | 02:61-65 | Confere com o texto do PL | primária (cópia no repositório) para o PL: recontagem linha a linha de `docs/legislacao/pl-18-2015.md` deu 23 linhas e 23/23/18/16/4. O Dossiê ABRASCO original não foi consultado. O PL fala em "24 amostras" no corpo e lista 23 pontos na tabela; o projeto usa a contagem da tabela |
| 7 | Reynier e Rubin: 23 a 32 g | 03:37-39 | Confere | primária: texto completo no PMC, Discussão ("reduced average birthweight by 23 to 32 g at the average level of glyphosate exposure") |
| 8 | Calzada et al.: 80 a 150 g com exposição alta | 03:40-42 | Confere | primária: resumo da versão publicada (JAERE). Só o resumo |
| 9 | Lei 16.820: sanção em 08/01/2019, vigência no dia seguinte; art. 28-B; redação do caput; § 2º sobre controle vetorial | 02:9-13 | Confere | primária (cópia no repositório): `lei-16820-2019.md` ("DE 08.01.19 (D.O. 09.01.19)"; art. 2º) |
| 10 | Lei 12.228 de 09/12/1993 | 02:35 | Confere | primária (cópia no repositório) |
| 11 | PL 18/2015 apresentado em 24/02/2015 | 02:39 | Confere | primária (cópia no repositório): data da Sala das Sessões |
| 12 | Aprovação unânime em 18/12/2018 | 02:40 | Confere | secundária externa: Brasil de Fato, 19/12/2018 ("nesta terça-feira (18)"); revista Estudos Sociedade e Agricultura ("unanimidade parlamentar") |
| 13 | STF julga a lei constitucional em maio de 2023 (ADI 6137) | 01:68-70; 01:84; 02:42 | Confere | primária: STF, sessão virtual de 19 a 26/05/2023, acórdão de 29/05/2023, relatora min. Cármen Lúcia, unânime. O Tribunal conheceu da ação quanto ao caput e ao § 1º |
| 14 | Lei 19.135, de 19/12/2024, exceção para drones; nova redação questionada no STF | 01:70-72; 02:21-25; 02:43 | Confere | primária: texto da lei na ALECE ("DE 19.12.24 (D.O. 19.12.24)"); notícia do STF sobre a ADI 7794, de 12/03/2025 |
| 15 | Ceará: primeira proibição estadual | 01:13-15 | Confere | secundária externa: Agência Pública (15/02/2019), Abrasco (04/02/2019), G1 (31/10/2024). Ver ADV-E5-1 |
| 16 | Assassinato de Zé Maria do Tomé em abril de 2010 | 01:8-9; 02:37 | Confere | secundária externa: G1 e Repórter Brasil (21/04/2010) |
| 17 | Limoeiro do Norte, Lei 1.478, de 20/11/2009 | 02:36 | Confere quanto a número e mês | secundária externa (G1: novembro de 2009, lei 1.478). O dia 20 vem de `docs/legislacao/README.md` (secundária interna, que cita o acervo da Câmara); o acervo não foi acessado nesta execução |
| 18 | Revogação em maio de 2010 pela Lei 1.511 | 02:37; 06:51-54 | Confere | secundária externa: G1 (31/10/2024) e revista Estudos Sociedade e Agricultura (revogação em 26/05/2010). O texto integral da Lei 1.511 não foi lido por ninguém, segundo o próprio repositório. IL-MINOR-5 |
| 19 | Março de 2011: notícia de proibição na Chapada; julho de 2011: ação civil pública do Ministério Público, na Justiça Federal | 02:38; 02:80-84; 05:113-114 | Confere, com a ressalva que o texto já faz | secundária externa: Mapa de Conflitos da Fiocruz (SDH/PR, março de 2011; MPF, MPT e MPCE, 15ª Vara Federal de Limoeiro do Norte, julho de 2011); Revista de Direito Sanitário (2015) |
| 20 | IN MAPA 2/2008: relatório mensal com município, cultura, área e produto | 05:105-107 | Confere | primária: texto da IN no gov.br, art. 14 (UF, município, tipo de serviço, cultura, área em hectares, nomes comerciais dos produtos, prefixo das aeronaves). O relatório lista nomes comerciais, sem dose nem quantidade |
| 21 | Decreto 4.074/2002: a receita registra a modalidade de aplicação | 05:108-110 | Confere | primária: Planalto, art. 66, IV, d |
| 22 | Lei 12.228/1993: cadastro estadual de prestadores, no órgão ambiental | 05:111-112 | Confere | primária (cópia no repositório): art. 8º (registro na SEMACE) |
| 23 | Seca de 2012 a 2017 | 05:50 | Confere | secundária externa: Ipea (2020); UOL com dados do Inmet (03/03/2018) |
| 24 | Resolução CNS 510/2016: pesquisa com dados públicos não passa pelo CEP/CONEP | 06:71-75 | Confere | primária: art. 1º, parágrafo único, II e V (DOU; página do CNS). O Ofício Circular 17/2022 da Conep inclui dados obtidos pela Lei de Acesso à Informação, desde que não sigilosos |
| 25 | SINASC e SIM "adquiridos até 2022" | 06:20-21 | Confere | secundária interna: `docs/fontes-e-vintages.md` |
| 26 | SISAGUA: quebra de registro no Ceará a partir de 2020; não monitora os princípios ativos predominantes | 06:58-60 | Confere com o repositório | secundária interna: `docs/lacunas-de-dados.md` §1-ter (procimidona, carbaril e fenitrotiona com zero medições). Análise do autor, não refeita aqui |
| 27 | Vento sem variação espacial de direção | 06:60-62 | Confere com o repositório | secundária interna: coerência circular de 0,96 entre estações. Não refeita aqui |
| 28 | Satélite não separa banana de outras perenes | 06:62-63 | Confere com o repositório | secundária interna: legenda do MapBiomas (classe 48). Ver IL-MINOR-6 |

As 13 "superfícies" do resumo agrupam estas 28 linhas (por exemplo, todas as datas legais contam como uma).

### C2. Consistência interna

1. **Contagens e janela da dose (IL-SERIOUS-1).** `05-metodologia.tex:55-57` fixa a dose principal na média de 2010 a 2014. Os números 169 (`02-contexto.tex:77`) e 15 (`05-metodologia.tex:79`) valem para a média de 2015 a 2018, que o mesmo texto rebaixa a sensibilidade. Na janela principal o grupo de dose nula tem 6 municípios.
2. **Plano "registrado" e desenho descrito (IL-SERIOUS-2).** `05-metodologia.tex:208-210` afirma que o plano de análise do primeiro estágio está registrado e versionado. O plano versionado (`docs/pre-especificacao.md`) fixa a dose em 2015-2018; a troca para 2010-2014 está descrita em `docs/ars/20` e no `CLAUDE.md` como desvio ainda não ratificado nem registrado.
3. **Leads e início do painel (IL-MEDIUM-1).** `05-metodologia.tex:89-91` promete leads que tornem visível o marco de notícia. O painel de desfechos começa em janeiro de 2015 (`06-dados.tex:7-8`) e o marco de notícia é 24/02/2015 (`02-contexto.tex:39`): há um mês de observação antes dele.

O projeto não tem resumo; a verificação resumo-corpo não se aplica.

### C3. Figure/Table Caption Fidelity

Não há figuras nem Figure Package. Os cinco quadros (cronologia, regra de decisão, fontes, ameaças, cronograma de atividades) são tabelas avulsas sem entrada de rastreio: nota *trace-unavailable* (consultiva, não bloqueia).

### C4. Experiment Provenance & Claim Alignment

"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

Verificação D7 no passport (`repro_lock: null`, logo tratado como posterior ao #260):

| Condição | Resultado |
|---|---|
| 1. Declaração ausente | Não acionada. `experiment_intake_declaration` presente, com `status: no_experiments_declared`, `declared_by: scholar`, `declared_at: 2026-11-15T21:29:42Z` |
| 2. Experimentos declarados sem proveniência | Não se aplica |
| 3. Sem experimentos declarados, mas com `experiment_provenance[]` | Não acionada (bloco ausente) |
| 4. Sem experimentos declarados, mas o manuscrito mostra resultados de análise própria | **Acionada (heurística), com ressalva.** Não há manifesto de afirmações nem seção de Resultados, que é onde a regra define o sinal mínimo. Mas o texto relata, como feitas pelo autor, análises de dados e seus resultados: `05:47-49` (diagnóstico de dispersão entre culturas), `05:79-80` (a composição do grupo de dose nula "desloca o nível estimado"), `06:56-63` (três fontes obtidas e inspecionadas, com o defeito de cada uma), `02:73-78` (cruzamento Censo × PAM). Como a regra fala em seção de Resultados, registro o enquadramento como limítrofe e deixo a decisão ao pesquisador |
| 5. `legacy_unknown` em passport novo | Não acionada |

Nenhuma linha de `experiment_alignment_results[]` foi produzida: não há `experiment_provenance[]` nem manifesto com `planned_experiment_ids`.

Evidência do repositório relevante para a condição 4 e para os Modos 1, 3 e 6: `docs/pre-especificacao.md` §8 registra que "a família confirmatória foi estimada" e que "nenhuma hipótese rejeita a 5%"; `docs/ars/17` discute uma estimativa de nível obtida com a dose 2015-2018; o `git log` de `scripts/estimate/` vai de 25/08 a 23/09/2026. A declaração do pesquisador reconhece isso ("rodei um primeiro projeto utilizando o pipeline") e pede para tratar a rodada como começo do zero.

## Phase D: Originality Verification Results

51 parágrafos de prosa com 35 palavras ou mais. 17 sondados (33%), com pelo menos um por capítulo, por busca de frase exata entre aspas (8 a 14 palavras).

| Grade | Paragraph Count | Proportion |
|-------|----------------|-----------|
| ORIGINAL | 14 | 82% |
| COMMON_KNOWLEDGE | 3 | 18% |
| PARAPHRASE | 0 | 0% |
| CLOSE_MATCH | 0 | 0% |
| VERBATIM | 0 | 0% |

Os três COMMON_KNOWLEDGE são definições de manual (externalidade negativa; resultado de Weitzman; uma única hipótese na diferença tripla), com redação própria e citação.

**D2.** A busca externa pelas publicações do autor não foi feita: ela exigiria enviar o nome do autor a um serviço externo, o que as regras desta sessão vedam sem pedido expresso. Foi feita a comparação interna por sequências de 12 palavras contra `paper/secoes/*.tex`, `docs/**/*.md` e `CLAUDE.md`. Oito parágrafos compartilham sequências com o rascunho de qualificação do próprio autor (máximo de 23 sequências num parágrafo, em `01-introducao.tex`, contra `paper/secoes/01-introducao.tex`). É reaproveitamento de texto próprio e não publicado, declarado nos comentários de cabeçalho das seções ("Condensada de ..."). Sem ocorrência.

## Phase E: Claim Verification Results

**Claim Registry coverage sidecar (#737)**

- Status: `not_run`
- Registry: não persistido como artefato `claim-registry/1.0`. A tabela abaixo é só uma vista renderizada.
- Coverage report: inexistente
- Draft binding: o rascunho é multiarquivo (9 `.tex`); SHA-256 por arquivo (16 primeiros dígitos): `projeto.tex` 808d8be8fa05ab17; `01` e8e20cf64f98e53c; `02` 38e10530ea9cc353; `03` b92117002e850d43; `04` 18458a28d072bfc7; `05` a25131f4e1424a4b; `06` 80a5c088551eb7c8; `07` 2ce7f6530718e76c; `08` b811e01668df8de9
- Candidate scope: citation-bearing + quantitative sentences only
- Candidate-unregistered count: não disponível
- Semantic extraction coverage: `not_machine_detectable`

**`E1-COVERAGE-UNRESOLVED`.** O despacho limita a saída deste agente a um arquivo e não nomeia pasta de fontes de evidência; por isso não foram gravados o registro com spans de bytes, o relatório de cobertura (`scripts/claim_registry_coverage.py`) nem as linhas de evidência (`scripts/evidence_rows.py`). O checkpoint não consegue renderizar linhas vinculadas a fonte. Isto não equivale a zero lacunas de extração e, pelo protocolo, mantém o checkpoint fechado até que E1/E1.1 rodem.

| Verdict | Claim Count | Proportion |
|---------|------------|-----------|
| VERIFIED | 30 | 65% |
| MINOR_DISTORTION | 3 | 7% |
| MAJOR_DISTORTION | 3 | 7% |
| UNVERIFIABLE | 0 | 0% |
| UNVERIFIABLE_ACCESS | 10 | 22% |

Critério usado, declarado como interpretação: quando o resumo da versão citada contém a afirmação de forma explícita, o veredito é VERIFIED e a coluna "base" diz "resumo". Quando a afirmação não está no resumo e o texto completo da versão citada não pôde ser lido, o veredito é UNVERIFIABLE_ACCESS, mesmo havendo outra versão legível.

**Registro (vista renderizada).** HI = HIGH-IMPACT; TU = TOP-UP.

| ID | Tier | Local | Afirmação (resumida) | Fonte citada | Veredito | Base |
|---|---|---|---|---|---|---|
| C01 | HI | 01:38-40 | Dias et al.: piora dos desfechos a jusante | dias2023down | VERIFIED | resumo |
| C02 | HI | 01:40-43 | Reynier e Rubin: aptidão; peso e gestação; cauda inferior | reynier2025glyphosate | VERIFIED | texto completo |
| C03 | HI | 01:44-47 | Larsen et al.: só no topo da exposição | larsen2017agricultural | VERIFIED | resumo |
| C04 | HI | 01:50-51 | Camacho e Mejía: aspersão aérea, Colômbia | camacho2017health | VERIFIED | resumo |
| C05 | HI | 01:52-55 | Calzada et al.: déficit mais forte quando o primeiro trimestre coincide com fumigação intensa | calzada2023bananas | UNVERIFIABLE_ACCESS | texto publicado ilegível (assinatura; PDF do repositório da UB recusou a conexão) |
| C06 | TU | 01:55-56 | mesma cultura, método e classe de produto | calzada2023bananas | UNVERIFIABLE_ACCESS | cultura e método estão no resumo; classe de produto não |
| C07 | TU | 01:59-62 | proibir e taxar: comparação antiga; simulações de banimento | weitzman1974, lichtenberg1988, helfand1995, bocker2020glyphosate | UNVERIFIABLE_ACCESS | Weitzman não lido; os demais conferem no resumo |
| C08 | TU | 02:55-57 | fumigação se intensifica na estação chuvosa | calzada2023bananas | UNVERIFIABLE_ACCESS | não está no resumo publicado |
| C09 | HI | 02:61-65 | contagens da tabela ABRASCO no PL 18/2015 | (sem entrada na bibliografia) | VERIFIED | texto do PL (cópia no repositório) |
| C10 | TU | 03:14-17 | Coase: direitos definidos e custos de transação baixos | coase1960 | UNVERIFIABLE_ACCESS | só metadados |
| C11 | TU | 03:19-22 | Weitzman: inclinações relativas | weitzman1974 | UNVERIFIABLE_ACCESS | só metadados |
| C12 | TU | 03:23-25 | dimensão distributiva | lichtenberg1988, helfand1995 | VERIFIED | resumos |
| C13 | TU | 03:25-26 | "comparação empírica entre cotas e taxas" | skevas2012 | MINOR_DISTORTION | resumo: modelo de simulação com quatro instrumentos |
| C14 | HI | 03:37-39 | 23 a 32 g | reynier2025glyphosate | VERIFIED | texto completo |
| C15 | HI | 03:40-42 | 80 a 150 g, exposição alta | calzada2023bananas | VERIFIED | resumo |
| C16 | TU | 03:42-43 | "vizinhança imediata da plantação" | calzada2023bananas | UNVERIFIABLE_ACCESS | não está no resumo |
| C17 | HI | 03:45-48 | concentração no topo da exposição e na cauda inferior | larsen2017agricultural, reynier2025glyphosate | VERIFIED | resumos |
| C18 | HI | 03:51-55 | Calzada: primeiro trimestre; Brainerd e Menon: mês da concepção | calzada2023bananas, brainerd2014seasonal | UNVERIFIABLE_ACCESS | Brainerd e Menon conferem; Calzada como em C05 |
| C19 | TU | 03:55-58 | composição sazonal das mães | buckles2013season, currie2013within | VERIFIED | resumos |
| C20 | TU | 03:62-65 | "estimadores para adoção escalonada" não se aplicam | callaway2021multiple, goodmanbacon2021, dechaisemartin2020 | MINOR_DISTORTION | Goodman-Bacon é teorema de decomposição; de Chaisemartin e D'Haultfœuille tratam de efeitos heterogêneos em geral |
| C21 | HI | 03:69-75 | parâmetros sob cada hipótese | callaway2024continuous | VERIFIED | PDF do NBER (trechos) |
| C22 | HI | 03:75-77; 05:143 | uma única hipótese na diferença tripla | olden2022triple | VERIFIED | resumo |
| C23 | HI | 03:79-84; 05:26-37 | `θ = VPP × ATT`, sem inversão de sinal | denteh2022misclassification | UNVERIFIABLE_ACCESS | VERSION_INCONSISTENT_CITATION: a entrada não diz a versão. Na v3, o Corolário 1 diz `θ_DID = P(ε=0\|D=1)·ATT` sob tendências paralelas no tratamento observado e sem falso negativo |
| C24 | HI | 03:84-89; 05:186-194 | inferência com poucos grupos | conley2011, ferman2019inference, chernozhukov2021conformal, cameron2008wild, mackinnon2018wild | UNVERIFIABLE_ACCESS | quatro conferem no resumo; Cameron et al. só por metadados |
| F01 | HI | 01:8-9 | assassinato em abril de 2010 | -- | VERIFIED | secundária externa |
| F02 | HI | 01:13-16 | primeira proibição estadual; Lei 16.820/2019 | -- | VERIFIED | lei: primária; primazia: secundária externa |
| F03 | HI | 01:68-72 | STF; drones em 2024; nova contestação | -- | VERIFIED | primária |
| F04 | HI | 01:84 | constitucional em 2023 (ADI 6137) | -- | VERIFIED | primária |
| F05 | HI | 02:9-13 | texto e datas da Lei 16.820 | -- | VERIFIED | primária (cópia no repositório) |
| F06 | HI | 02:16 | 184 municípios | -- | VERIFIED | primária |
| F07 | HI | 02:19-21 | marcos de 2015 e 2018 | -- | VERIFIED | primária e secundária externa |
| F08 | HI | 02:21-25 | Lei 19.135, 19/12/2024 | -- | VERIFIED | primária |
| F09 | HI | 02:35 | Lei 12.228, 09/12/1993 | -- | VERIFIED | primária (cópia no repositório) |
| F10 | HI | 02:36 | Lei municipal 1.478, 20/11/2009 | -- | VERIFIED | secundária externa e interna |
| F11 | HI | 02:37; 06:51-54 | revogação em maio de 2010, Lei 1.511 | -- | VERIFIED | secundária externa |
| F12 | HI | 02:38; 02:80-84 | fatos de 2011 | -- | VERIFIED | secundária externa |
| F13 | HI | 02:73-76 | 36 estabelecimentos, 7 municípios, todos com banana | -- | VERIFIED | primária |
| F14 | HI | 02:77 | 169 municípios com área de banana | -- | MAJOR_DISTORTION | primária: 178 na janela principal declarada |
| F15 | HI | 05:79 | 15 municípios sem área de banana | -- | MAJOR_DISTORTION | primária: 6 na janela principal declarada |
| F16 | HI | 05:47-49 | banana "a de variação mais ampla" | -- | MINOR_DISTORTION | secundária interna (`docs/gates-resultados-dados-reais.md` §4): coco-da-baía, algodão e melão têm Gini maior; a banana foi a escolhida por juntar dispersão e número de municípios |
| F17 | TU | 05:49-50 | seca de 2012 a 2017 | -- | VERIFIED | secundária externa |
| F18 | HI | 05:105-107 | IN MAPA 2/2008 | -- | VERIFIED | primária |
| F19 | HI | 05:108-110 | Decreto 4.074/2002 | -- | VERIFIED | primária |
| F20 | HI | 05:111-112 | cadastro da Lei 12.228 | -- | VERIFIED | primária (cópia no repositório) |
| F21 | TU | 05:113-114 | ação de 2011 na Justiça Federal | -- | VERIFIED | secundária externa |
| F22 | HI | 05:208-210 | plano do primeiro estágio "registrado e versionado" | -- | MAJOR_DISTORTION | secundária interna: `docs/pre-especificacao.md` §0 e §8 |
| N01-N04 | NOT-SELECTED | ver E5 | afirmações de primazia ou ausência | -- | (só E5) | -- |

**Persisted Phase E evidence rows (#656):** não persistidas. Ver `E1-COVERAGE-UNRESOLVED`.

**Scope-conformance advisory (#547)** — advisory-only, not counted in verdicts or the gate decision:

`[E4-SKIPPED: no scope context]` (o despacho não trouxe o `scope` do RQ Brief).

| ID | Claim location | Effective scope | Drafted scope | Broadened axis |
|----|---------------|-----------------|---------------|----------------|
| -- | -- | -- | -- | -- |

**Novelty-claim classification (#548)** — advisory-only, not counted in verdicts or the gate decision:

| ID | Claim location | Claim wording | Classification | Nearest prior work / recommended bounded rewording |
|----|---------------|--------------|----------------|---------------------------------------------------|
| ADV-E5-1 | 01-introducao.tex:13-15 | "na primeira proibição estadual do gênero no Brasil" | UNRESOLVED (sem estratégia de busca documentada; apoiada por três fontes secundárias) | Citar a fonte, ou "apontada como a primeira proibição estadual" |
| ADV-E5-2 | 01-introducao.tex:23-24; 58-59 | "praticamente não há evidência causal no país"; "O que nenhum desses trabalhos oferece" | UNRESOLVED | Limitar ao conjunto revisado: "entre os trabalhos revisados" |
| ADV-E5-3 | 01-introducao.tex:88-89 | "registros administrativos nunca explorados para esse fim" | UNRESOLVED | "que não localizamos em uso para esse fim" |
| ADV-E5-4 | 08-cronograma.tex:9-10 | "a primeira medida municipal da aplicação aérea de agrotóxicos no Ceará antes da proibição" | UNRESOLVED; além disso, o próprio projeto usa o Censo Agropecuário de 2006, que é uma medida municipal anterior | "a primeira medida municipal para 2015-2018" |

**Cache staleness advisory (#541)** — advisory-only, not counted in verdicts or the gate decision:

| ID | Citation key | Cache age (days) | Threshold | Re-verified live? |
|----|-------------|------------------|-----------|-------------------|
| -- | nenhuma linha servida de cache; todas as consultas foram ao vivo | -- | -- | -- |

**Claim-strength drift review (#569, revision rounds)**: `[E6-SKIPPED: no revision evidence]` (primeira passagem).

**Token-conservation advisory (#570, revision rounds)**: vazio (primeira passagem).

## Issue List (Sorted by Severity)

### SERIOUS (Must Fix)

| ID | # | Category | Location | Issue Description | Correct Information | Source |
|----|---|----------|----------|------------------|--------------------|----|
| IL-SERIOUS-1 | 1 | Data / Claim (F14, F15) | `paper/projeto/secoes/02-contexto.tex:77`; `paper/projeto/secoes/05-metodologia.tex:79-80` (e a leitura de `05-metodologia.tex:186` e `07-ameacas.tex:26-28`, que dependem do tamanho do grupo) | As contagens "169 municípios com área de banana" e "15 municípios sem área de banana" valem para a média de 2015-2018. O texto declara a média de 2010-2014 como dose principal (`05-metodologia.tex:55-57`). Nessa janela o grupo de dose nula tem 6 municípios, não 15 | PAM, área plantada de banana: média 2010-2014, 178 com área e 6 sem (Arneiroz, Fortim, Horizonte, Ibicuitinga, Palhano, Potiretama); média 2015-2018, 169 e 15. Correção sugerida: dar as duas contagens com a janela ao lado de cada uma, e rever o que o texto diz sobre o grupo de comparação com o número da janela principal | `https://apisidra.ibge.gov.br/values/t/5457/n6/in n3 23/v/8331/p/2010,...,2018/c782/40136`, consulta de 2026-11-15 |
| IL-SERIOUS-2 | 2 | Claim (F22) / Methods disclosure | `paper/projeto/secoes/05-metodologia.tex:208-210`; frases correlatas em `05-metodologia.tex:79-80`, `05-metodologia.tex:199-201` e `01-introducao.tex:96` | "O plano de análise do primeiro estágio está registrado e versionado." (a) O documento versionado se declara "plano pré-estimação, não pré-registro". (b) Ele fixa a dose principal em 2015-2018; o projeto usa 2010-2014, desvio que `docs/ars/20` §4 e o `CLAUDE.md` dão como não ratificado e não registrado. (c) O repositório documenta que uma estimação do tipo do estágio 1 já foi rodada com a dose antiga, e `05:79-80` relata o comportamento de uma estimativa. O texto apresenta o estágio 1 como ainda não estimado e não informa a rodada anterior nem a troca de janela feita depois dela | Sem número de estimativa, o texto pode dizer: que existe um plano de análise versionado, anterior à estimação, que não é pré-registro em repositório público; que uma rodada exploratória com a dose 2015-2018 já foi executada; e que a dose 2010-2014 é desvio desse plano, com data e motivo na tabela de desvios. Antes disso, registrar o desvio em `docs/pre-especificacao.md` §8. Alternativa: retirar "registrado" e a frase sobre o nível estimado | `docs/pre-especificacao.md` §0 e §8; `docs/ars/20-projeto-de-pesquisa-desenho.md` §4; `docs/ars/17-resposta-ao-feedback-2026-09-22.md` §1; `git log -- scripts/estimate` |

### MEDIUM (Must Fix)

| ID | # | Category | Location | Issue Description | Correct Information | Source |
|----|---|----------|----------|------------------|--------------------|----|
| IL-MEDIUM-1 | 1 | Internal consistency | `paper/projeto/secoes/05-metodologia.tex:89-91`; `06-dados.tex:7-8`; `02-contexto.tex:39`; `07-ameacas.tex:25` | O estudo de eventos promete leads que tornem visível o marco de notícia (24/02/2015), mas o painel de desfechos começa em janeiro de 2015. Só há um mês antes do marco | Ou o painel de desfechos recua para antes de 2015 (o `docs/fontes-e-vintages.md` registra SINASC definitivo desde 2013), ou a frase passa a prometer só o marco de certeza (dezembro de 2018) | os três trechos do próprio manuscrito |

### MINOR (Recommended Fix at Stage 2.5; Must Fix at Stage 4.5)

| ID | # | Category | Location | Issue Description | Suggestion |
|----|---|----------|----------|------------------|----|
| IL-MINOR-1 | 1 | Citation context | `01-introducao.tex:53-55`; `03-referencial.tex:53-54`; reflete em `04-objetivos.tex:27-28` | Atribui a Calzada et al. efeito "mais forte" no primeiro trimestre. O texto publicado não pôde ser lido. As versões legíveis do mesmo trabalho (texto para discussão de 2021 e slides do NBER Summer Institute de 2023) relatam efeito no primeiro **e** no segundo trimestres | Ler o PDF da versão publicada (JAERE 10(6)) e ajustar: provavelmente "primeiro e segundo trimestres". Se confirmar, rever a redação de H3 |
| IL-MINOR-2 | 2 | Citation context (C13) | `03-referencial.tex:25-26` | Skevas et al. é simulação de política com dados de produtores holandeses, não comparação empírica ex post | "a comparação, por simulação, entre taxas, penalidades, subsídios e cotas" |
| IL-MINOR-3 | 3 | Citation context (C20) | `03-referencial.tex:62-64` | Chama os três trabalhos de "estimadores para adoção escalonada". Goodman-Bacon (2021) é uma decomposição | "a literatura de diferenças-em-diferenças com variação de timing" |
| IL-MINOR-4 | 4 | Claim (F16) | `05-metodologia.tex:47-49` | "a banana se mostrou a de variação mais ampla": no diagnóstico do repositório, coco-da-baía, algodão e melão têm concentração maior. E o diagnóstico usou 2015-2018 | Dizer o critério real: dispersão alta combinada com presença em muitos municípios e ligação com a prática aérea; informar a janela do diagnóstico |
| IL-MINOR-5 | 5 | Source attribution | `02-contexto.tex:36-38` e `:46` | A fonte do Quadro 1 diz "a partir dos textos legais", mas a Lei municipal 1.511 não teve o texto lido e os fatos de 2011 vêm de imprensa e de portal | "a partir dos textos legais, da tramitação e, para 2010 e 2011, de fontes secundárias" |
| IL-MINOR-6 | 6 | Claim precision | `06-dados.tex:56-58` | "Três fontes [...] foram obtidas, inspecionadas": para o mapeamento por satélite o repositório registra a conferência da legenda de classes, sem ingestão do dado | "avaliadas" no lugar de "obtidas, inspecionadas", ou separar os casos |
| IL-MINOR-7 | 7 | Reference | `paper/referencias.bib`, entrada `bocker2020glyphosate` | Ano 2019 (online) com chave 2020; sem volume, número e páginas | Conferir na página da editora; o RePEc lista v. 47, n. 2, p. 371-402, 2020 |
| IL-MINOR-8 | 8 | Reference | `paper/referencias.bib`, `larsen2017agricultural` | Sem número do artigo | Acrescentar `pages = {302}` ou campo equivalente |
| IL-MINOR-9 | 9 | Reference | `paper/referencias.bib`, `reynier2025glyphosate` | Sem número do artigo | Acrescentar e2413013121 |
| IL-MINOR-10 | 10 | Reference | `paper/referencias.bib`, `weitzman1974` | `pages = {477}` | Conferir o intervalo no JSTOR (fonte secundária indica 477-491) |
| IL-MINOR-11 | 11 | Reference | `paper/projeto/referencias-projeto.bib`, `denteh2022misclassification` | Não fixa a versão do arXiv; o resultado usado está na v3 (30/04/2026) | Acrescentar "v3" e a data da versão em `howpublished` ou `note` |
| IL-MINOR-12 | 12 | Format / traceability | `02-contexto.tex` (leis, PL 18/2015, Dossiê ABRASCO, Censo); `05-metodologia.tex:105-112`; `06-dados.tex:74` | Leis, o PL, o Dossiê ABRASCO, o Censo Agropecuário (tabela SIDRA 1008), a PAM, a IN MAPA 2/2008, o Decreto 4.074, a ADI 6137 e a Resolução CNS 510 são usados no texto sem entrada na lista de referências | Criar as entradas (a ABNT prevê referência de legislação, jurisprudência e bases de dados) |
| IL-MINOR-13 | 13 | Factual completeness | `02-contexto.tex:19-21`; `05-metodologia.tex:52-57` | O texto data a "notícia" em 2015 e trata 2010-2014 como janela anterior a ela. Reportagem do Diário do Nordeste de 14/07/2011 registra o PL 134/2011 (dep. Heitor Férrer), que já propunha proibir a pulverização aérea no estado; documento do SINDAG o lista entre projetos rejeitados ou arquivados | Conferir a tramitação do PL 134/2011 na ALECE e mencioná-lo na cronologia; rever a frase que dá 2010-2014 como "fixada antes que a política pudesse alterá-la" |

**Bloqueio fora da numeração IL:** condição 4 da verificação D7 (Fase C4), acionada por heurística e com ressalva; ver a seção C4.

## AI Research Failure Mode Checklist

Base da regra NOT APPLICABLE: o passport traz `experiment_intake_declaration.status: no_experiments_declared`, com a resposta do pesquisador: "É, Considere que eu rodei um primeiro projeto utilizando o pipeline, mas ainda o projeto eu considero que não, nenhuma estimativa ainda precisa ser consolidada. É um projeto para que eu vá realizar isso, certo? Então, o que eu fiz foi só apenas pegar os dados e tudo mais. [segunda resposta] Vamos começar do zero [...] vamos considerar que a gente vai rodar tudo do zero."

A regra diz que, se o rascunho mesmo assim apresenta análises de dados como feitas pelo autor (resultados, ou texto de método que as descreve como feitas), declaração e rascunho discordam: nenhum dos quatro modos fica NOT APPLICABLE, e os Modos 3 e 6 ficam SUSPECTED. O rascunho apresenta essas análises em `05-metodologia.tex:47-49`, `05-metodologia.tex:79-80`, `06-dados.tex:51-63` e `02-contexto.tex:73-78`. Aplico a regra como escrita. O pesquisador vê as duas coisas: a declaração acima e os trechos citados.

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | INSUFFICIENT EVIDENCE | Refiz de fonte primária quatro conjuntos de números do texto (184; 36 em 7; 169 e 15; contagens da tabela do PL). Três reproduzem. O quarto reproduz só na janela 2015-2018, que não é a declarada (IL-SERIOUS-1); os documentos do repositório usam 169 e 15 para essa janela antiga. Não auditei os logs das demais análises relatadas (dispersão de dose, quebra do SISAGUA, coerência do vento) | yes |
| 2. Hallucinated citation | CLEAR | 28 de 28 referências existem; 27 DOIs resolvem para a obra citada e o arXiv confere; nenhum `DOI_MISMATCH`; cinco registros incompletos (MINOR) | no |
| 3. Hallucinated experimental result | SUSPECTED (pela regra da declaração) | Declaração e rascunho discordam. No conteúdo: o texto não traz número de estimativa; os números descritivos conferem com fonte primária, salvo 169 e 15, que estão na janela errada; `05:79-80` relata o comportamento de uma estimativa que o texto não apresenta | yes |
| 4. Shortcut reliance | CLEAR (flag-only neste estágio) | O atalho óbvio do desenho, medir o tratamento pela cultura e não pelo método, é tratado pelo próprio texto como ameaça central (`05-metodologia.tex:26-41`; `07-ameacas.tex:49-57`) | no |
| 5. Implementation bug reframed as novel insight | CLEAR | Nenhuma ocorrência de "surpreendente", "inesperado", "contraintuitivo" ou equivalentes; o texto não anuncia achado | no |
| 6. Methodology fabrication | SUSPECTED (pela regra da declaração) | Declaração e rascunho discordam. No conteúdo: o texto de método diz que o plano do estágio 1 está "registrado" e descreve o estágio como futuro, enquanto o plano versionado tem outra janela de dose e uma rodada já foi executada (IL-SERIOUS-2) | yes |
| 7. Frame-lock at early pipeline stage | INSUFFICIENT EVIDENCE | O desenho em estágios com regra de decisão permite recuar, o que pesa contra o travamento. Três pontos pedem resposta do pesquisador: a janela 2010-2014 contém os eventos de 2011 e um projeto de lei estadual de 2011 (IL-MINOR-13); a hipótese do primeiro trimestre vem de uma leitura de Calzada et al. ainda não conferida no texto publicado (IL-MINOR-1); a troca da janela de dose veio depois de uma rodada com a janela antiga | no (segue com aviso; reavaliar no 4.5) |

**Resultado do checklist:** o pipeline fica bloqueado pelos Modos 1, 3 e 6 até o pesquisador responder. Opções previstas na referência: confirmar o apontamento e voltar ao Estágio 2; anular com justificativa registrada; ou revisar os trechos e rodar de novo a verificação. Este bloqueio não entra na contagem de issues nem altera o veredito.

## Tool Limitation Disclaimer

> This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 33%, and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.

Limitações específicas desta execução:

1. **Texto completo não lido.** Calzada et al. (JAERE, assinatura; o PDF no repositório da Universidade de Barcelona recusou a conexão), Weitzman (1974), Coase (1960) e Cameron et al. (2008) foram conferidos só por metadados; a maior parte das demais referências, só pelo resumo. Texto completo ou trechos longos foram lidos para Reynier e Rubin (PMC), Denteh e Kédagni (arXiv v3), Callaway et al. (NBER), Brainerd e Menon (versão final dos autores), Buckles e Hungerman (PMC) e Roth et al.
2. **Fontes primárias não acessadas.** O Dossiê ABRASCO (2012); o acervo da Câmara de Limoeiro do Norte (leis 1.478 e 1.511), que não tentei acessar e que o repositório registra como bloqueado pelo proxy; os autos da ação civil pública de 2011; o Diário Oficial do Estado.
3. **APIs.** O Semantic Scholar respondeu normalmente. `servicodados.ibge.gov.br` recusou a conexão; a consulta foi feita por `apisidra.ibge.gov.br`, que respondeu. O serviço Parallel Search atingiu o limite gratuito na última rodada (uma consulta falhou e foi refeita pelo WebSearch).
4. **Dados do autor.** `data/processed` está vazio nesta sessão. As análises descritas em `docs/gates-resultados-dados-reais.md` e `docs/lacunas-de-dados.md` não foram refeitas, salvo as contagens da PAM e do Censo, obtidas de novo na fonte.
5. **Autoplágio.** Sem busca externa pelo nome do autor (regra de privacidade da sessão).
6. **Artefatos da Fase E.** Registro de afirmações, relatório de cobertura e linhas de evidência não foram persistidos (`E1-COVERAGE-UNRESOLVED`).
7. **Verificação cruzada entre modelos.** `ARS_CROSS_MODEL` não está definido; verificação por um único modelo, da mesma família do que escreveu o rascunho.
8. **Passport.** Não conferi o `content_hash` do passport (o método de composição do hash não está descrito no arquivo).

## Verification Audit Trail

Execução em 2026-11-15, concluída às 21:43Z.

**Fase A.**
- Extração das chaves: expressão regular sobre `\cite{}` e `\citeonline{}` nos nove `.tex`; 28 chaves, 48 ocorrências. Diferença de conjuntos contra as 55 chaves dos dois `.bib`: 27 não citadas, 0 pendentes. `projeto.bbl`: 28 `\bibitem`.
- A0: `POST https://api.semanticscholar.org/graph/v1/paper/batch` com 27 DOIs e `ARXIV:2207.11890`. Resultado: 22 encontrados com título, autores e DOI iguais; 6 nulos.
- A1/A2: `GET https://api.crossref.org/works/<doi>` para cada um dos 27 DOIs (27 respostas HTTP 200). Comparação campo a campo de autores, título, periódico, volume, número, páginas e ano. Diferenças: as cinco listadas na Fase A.
- arXiv: `GET https://export.arxiv.org/api/query?id_list=2207.11890`. Resultado: `2207.11890v3`, publicado em 2022-07-25, atualizado em 2026-04-30, Augustine Denteh e Désiré Kédagni.
- Böcker et al.: Crossref sem volume; OpenAlex sem volume; busca "Böcker Britz Möhring Finger ... European Review of Agricultural Economics volume 47" devolveu `econpapers.repec.org/RePEc:oup:erevae:v:47:y:2020:i:2:p:371-402`.
- Weitzman: OpenAlex traz primeira e última página iguais (477); busca devolveu 477-491 em lista de referências de terceiros.

**Fases B e E (fontes de conteúdo).**
- Resumos: campos `abstract` do Crossref e do Semantic Scholar nas mesmas respostas da Fase A.
- Reynier e Rubin: `https://pmc.ncbi.nlm.nih.gov/articles/PMC11761964`, seção "Broader Considerations".
- Calzada et al.: resumo em `https://www.journals.uchicago.edu/doi/10.1086/725349`; outras versões, não usadas para veredito de apoio: `https://conference.nber.org/conf_papers/f181409.slides.pdf` (primeiro e segundo trimestres), texto para discussão E21/405 da UB, e a nota dos autores no VoxDev (estação chuvosa; 150 metros). Tentativa de baixar `https://diposit.ub.edu/bitstream/2445/213742/1/846255.pdf`: conexão recusada.
- Denteh e Kédagni: `https://arxiv.org/pdf/2207.11890v3`, Corolário 1 e sua prova (A.3).
- Callaway, Goodman-Bacon e Sant'Anna: `https://www.nber.org/system/files/working_papers/w32117/w32117.pdf`, resumo, introdução e quadro de parâmetros identificados.
- Roth et al.: `https://www.sciencedirect.com/science/article/pii/S0304407623001318` e `https://arxiv.org/html/2201.01194`, seção 4.4.
- Brainerd e Menon: `https://people.brandeis.edu/~nmenon/JDE_final.pdf`. Buckles e Hungerman: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3777829`. Conley e Taber: resumo em `https://www.nber.org/papers/t0312` e RePEc.

**Fase C (fatos e números).**
- SIDRA, Censo Agropecuário 2006: `https://apisidra.ibge.gov.br/values/t/1008/n6/in n3 23/v/2020/p/2006/c12596/113450`. 184 linhas; 7 com valor positivo, soma 36; 177 com "-".
- SIDRA, PAM: tabela 5457, variável 8331 (área plantada ou destinada à colheita), `c782/40136` (banana, cacho), anos 2010 a 2014 e 2015 a 2018, todos os municípios da UF 23. "-" tratado como zero. Médias por município e contagem de positivos e nulos em cada janela.
- Tabela do PL 18/2015: leitura programática de `docs/legislacao/pl-18-2015.md`, 23 linhas de ponto de coleta, contagem por princípio ativo.
- Lei 16.820 e Lei 12.228: `docs/legislacao/lei-16820-2019.md` e `lei-12228-1993-consolidada.md` (arts. 4º e 8º).
- ADI 6137: `https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=508087`; inteiro teor em `portal.stf.jus.br/processos/downloadPeca.asp?id=15358834376`; ficha em `jurisprudencia.stf.jus.br/pages/search/sjur481679/false`. ADI 7794: `https://noticias.stf.jus.br/postsnoticias/partido-questiona-lei-do-ceara-que-autoriza-pulverizacao-de-agrotoxicos-por-drones/`.
- Lei 19.135: `https://www2.al.ce.gov.br/legislativo/legislacao5/leis2024/19135.htm` (pelo índice de busca).
- IN MAPA 2/2008: `https://www.gov.br/agricultura/pt-br/assuntos/insumos-agropecuarios/insumos-agricolas/agrotoxicos/arquivos/in2.pdf`, arts. 9º e 14 e Anexo V.
- Decreto 4.074/2002: `https://www.planalto.gov.br/ccivil_03/decreto/2002/D4074.htm`, art. 66.
- Resolução CNS 510/2016: `https://www.in.gov.br/web/dou/-/resolucao-n-510-de-7-%20de-%20abril-de-2016-%2022917558` e página do CNS; Ofício Circular 17/2022 da Conep.
- 2011: `https://mapadeconflitos.ensp.fiocruz.br/conflito/ce-uso-indiscriminado-de-agrotoxicos-contamina-recursos-hidricos-e-e-a-provavel-razao-da-forte-incidencia-de-cancer-em-populacoes-trabalhadoras-e-moradoras-do-vale-do-jaguaribe`; `https://revistas.usp.br/rdisan/pt_BR/article/download/97324/96336`; `https://mst.org.br/2011/07/14/projeto-de-lei-quer-fim-da-pulverizacao-aerea-de-agrotoxicos-no-ceara/` (reprodução do Diário do Nordeste; PL 134/2011); apresentação do SINDAG no gov.br (projeto de Heitor Férrer entre os rejeitados ou arquivados).
- Aprovação de 18/12/2018: `https://www.brasildefato.com.br/2018/12/19/assembleia-legislativa-proibe-pulverizacao-aerea-de-agrotoxicos-no-ceara-entenda/`; `revistaesa.com` (artigo sobre a Lei Zé Maria do Tomé).
- Zé Maria do Tomé e Limoeiro do Norte: `https://g1.globo.com/ce/ceara/noticia/2024/10/31/ze-maria-do-tome-o-ambientalista-cearense-assassinado-por-combater-o-uso-de-agrotoxicos-no-ceara.ghtml`; `https://reporterbrasil.org.br/2024/10/assassinato-ativista-anti-agrotoxicos-ce-julgamento`; `https://apublica.org/2019/02/antes-do-ceara-8-municipios-ja-haviam-proibido-fumigacao-aerea-de-agrotoxicos/`.
- Seca: `https://repositorio.ipea.gov.br/server/api/core/bitstreams/42514baf-e7ee-4713-95e5-6921ccff9d4a/content`; UOL, 03/03/2018.
- Documentos internos lidos: `docs/legislacao/README.md`, `docs/ars/06`, `docs/ars/17` (trechos), `docs/ars/20`, `docs/pre-especificacao.md` (§0 e §8), `docs/fontes-e-vintages.md`, `docs/lacunas-de-dados.md` (§1-ter e tabela de estado), `docs/gates-resultados-dados-reais.md` (§4), `CLAUDE.md`, `passport.yaml`, `passport_run_ledger.yaml`.
- Páginas e números de estimativa: `pdfinfo` e `pdftotext` sobre `paper/projeto/projeto.pdf`; busca por padrões numéricos e por termos de inferência nos `.tex`.

**Fase D.** 17 buscas de frase exata (WebSearch), uma por parágrafo sondado: 01 (4 parágrafos), 02 (2), 03 (5), 04 (1), 05 (2), 06 (1), 07 (1), 08 (1). Nenhuma devolveu o trecho. Comparação interna: sequências de 12 palavras entre cada parágrafo e os arquivos `paper/secoes/*.tex`, `paper/main.tex`, `docs/**/*.md` e `CLAUDE.md`.
