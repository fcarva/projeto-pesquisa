# Relatório de verificação de integridade — Estágio 4.5 (final), rodada 21

Data da execução: 2026-11-16. Agente: `integrity_verification_agent` (ARS v3.24.2), Mode 2 (final-check). Passada nova, do zero; os relatórios do 2.5 e da re-revisão serviram só de pista.

Objeto: `paper/projeto/` na versão projeto_v12 (`projeto.tex`, `secoes/01` a `08`, `secoes/apendices.tex`, `referencias-projeto.bib`, `../referencias.bib`; `projeto.pdf`, `.toc`, `.bbl`, `.log` de 16/11/2026, 02h22, posteriores a todos os `.tex`).

## Modo de verificação

Final Verification (Estágio 4.5).

## Veredito

**FAIL.**

Zero SERIOUS. **1 MEDIUM** e **11 MINOR**; no Estágio 4.5 qualquer MINOR também reprova. Nenhuma referência fabricada, nenhuma distorção grave de fonte, nenhum número de estimativa própria no texto. Todas as correções cabem em troca de palavras ou em apêndice.

À parte da contagem por gravidade, há dois bloqueios de regra que pedem resposta do pesquisador, não correção de texto:

- **C4, condição 4 do anti-skip (D7): FAIL formal.** O passport declara `no_experiments_declared` ("Não reporta"), e o texto reporta, em primeira pessoa, o sentido de um resultado próprio (`05-metodologia.tex:280-283`; `apendices.tex:417-426`).
- **Checklist dos 7 modos:** Modos 3 e 6 SUSPECTED; Modo 1 INSUFFICIENT EVIDENCE. Ver a seção própria.

## Resumo da verificação

| Categoria | Total | Passou | Problemas |
|---|---|---|---|
| Existência das referências | 58 citadas (chaves do `.bbl`) | 58 | 0 |
| Exatidão bibliográfica | 58 | 53 | 5 entradas com problema menor: F-MINOR-8, 9, 10 e as duas de F-MINOR-11; 2 campos não conferidos (ver "Não conferido") |
| Citações fantasma | — | — | 0 órfãs, 0 penduradas |
| Contexto de citação (B) | 87 comandos de citação; 58 chaves | 44 chaves conferidas contra texto ou resumo da fonte; 14 só contra título e metadados (lista na Fase B) | 2 MINOR (F-MINOR-3, 4) |
| Dados de terceiros (C1) | 14 superfícies numéricas | 14 | 0 |
| Consistência interna (C2) | — | Falha em 4 pontos menores | F-MINOR-5, 6, 7 e F-MINOR-2 |
| Número de estimativa própria | corpo, resumo, quadros, apêndices | nenhum valor | 0 (uma nota: N-1) |
| Fidelidade à rodada exploratória | 14 afirmações | 11 | 1 MEDIUM (F-MEDIUM-1), 2 MINOR (F-MINOR-1, 2) |
| Originalidade (D1) | 7 blocos novos que resumem literatura, de cerca de 70 parágrafos (≈10%) | 7 | 0 CLOSE_MATCH, 0 VERBATIM |
| Autoplágio (D2) | não executado | — | — |
| Afirmações (E) | 42 com fonte externa citada, registradas à mão (ver ressalva) | 39 VERIFIED; 2 MINOR_DISTORTION; 1 UNVERIFIABLE_ACCESS | 0 MAJOR_DISTORTION, 0 UNVERIFIABLE |
| Formais | `??`, `\ref`, páginas, Overfull | passou | "MEJíA" na lista (F-MINOR-8) |

Ressalva de método, sem atenuação: **não rodei** `claim_registry_coverage.py`, `evidence_rows.py` nem o contrato do E6. O registro de afirmações é uma tabela escrita à mão, não um artefato `claim-registry/1.0`; estado `E1-COVERAGE-UNRESOLVED`, cobertura semântica `not_machine_detectable`. A Fase D ficou abaixo dos 50% do protocolo por causa da regra de não enviar trechos a buscadores.

## Fase A — referências (58 de 58)

Todas as 58 chaves citadas foram conferidas por mim nesta passada. Não houve amostragem: o Crossref respondeu às 31 consultas espaçadas de 2,5 s, de modo que a "amostra" das já conferidas no 2.5 foi de 100%.

| Grupo | n | Como | Resultado |
|---|---|---|---|
| Artigos e relatório com DOI | 31 | `api.crossref.org/works/<doi>`, campo a campo | 31 conferem em autores, título, periódico, volume, número, páginas e ano. Böcker et al.: o Crossref não traz volume nem páginas; conferidos na página da OUP (v. 47, n. 2, p. 371–402, 2020). |
| arXiv | 2 | `arxiv.org/abs/…` | `denteh2022misclassification`: v3 de 30/04/2026 (confere com "versão 3, de 2026"). `ortiz2025triple`: v3 de 18/07/2025 (confere). |
| Documentos, leis, notícias | 25 | página ou PDF aberto, ou API do IBGE | 25 existem; ver problemas abaixo. |

As doze que entraram ou mudaram desde a v7:

| Chave | Fonte aberta | Resultado |
|---|---|---|
| `carneiro2015dossie` | PDF do ICICT/Fiocruz (629 p.), folha de rosto e ficha catalográfica | Organizadores, título, cidades, editoras e ano conferem. p. 69 e 152 impressas = p. 71 e 154 do PDF; os dois trechos estão lá. |
| `sindag2021plataforma` | sindag.org.br | Título e data (17/06/2021) conferem; plataforma lançada em 16/06/2021, no Sipeagro. |
| `stf2025adi7794` | noticias.stf.jus.br | Título, data (12/03/2025), ADI 7794, relator Luiz Fux, Lei 19.135/2024: conferem. |
| `mpt2011apodi` | prt7.mpt.mp.br | Título e data (07/07/2011) conferem. Ação civil pública de MPF, MPT e MP estadual, 15ª Vara Federal, Limoeiro do Norte. A página não dá número do processo nem data de ajuizamento, como o texto diz. |
| `rebello2018seca` | UOL (acesso direto recusado; lido por serviço de extração) | Título, autor (Aiuri Rebello) e data (03/03/2018) conferem. |
| `limoeiro2009lei1478` | camaralimoeirodonorte.ce.gov.br/leis/549 | Lei 1478/2009, de 20/11/2009; ementa confere palavra por palavra. |
| `rambachan2023credible` | Crossref; resumo no RePEc | Confere (ReStud 90(5), 2555–2591). |
| `callaway2024continuous` | NBER w32117; página "Forthcoming" da AER | NBER WP 32117, fev. 2024: confere. "No prelo na American Economic Review": **confere** (listado em aeaweb.org/journals/aer/forthcoming). |
| `ortiz2025triple` | arXiv | Confere. |
| `denteh2022misclassification` | arXiv, PDF da v3 lido | Confere. |
| `ibge2006censoagro` | API do IBGE, tabela 1008 | Tabela existe; dado refeito (ver C1). Ano de publicação "2012" não conferido. |
| `ceara2018nascer` | hgcc.ce.gov.br | Título e data (26/03/2018) conferem; programa Nascer no Ceará. |

## Fase B — contexto de citação

Conferidas contra o texto ou o resumo da fonte (44 chaves): todas as doze acima; `calzada2023bananas`, `reynier2025glyphosate`, `rigotto2013trends`, `larsen2017agricultural`, `jones2020invasive`, `brainerd2014seasonal`, `buckles2013season`, `currie2013within`, `rocha2015water`, `olden2022triple`, `ferman2019inference`, `hagemann2025single`, `mackinnon2018wild`, `canay2021wild`, `bocker2020glyphosate`, `pereira2015conflitos`, `agenciabrasil2016ceara`, `globorural2021bananais`, `lavor2019antes`, `limoeiro2010lei1511`, `ceara2019lei16820`, `ceara1993lei12228`, `ceara2024lei19135`, `ceara2015pl18`, `ceara2011pl134`, `mapa2008in2`, `mapa2021portaria298`, `brasil2002decreto4074`, `cns2016res510`, `brasil2011sinasc`, `stf2023adi6137`, `ibgepam`.

Conferidas só contra título e metadados (14), porque o texto lhes atribui apenas o tema ou um resultado de manual: `coase1960`, `weitzman1974`, `lichtenberg1988`, `helfand1995`, `camacho2017health`, `dias2023down`, `baker2026practitioner`, `callaway2021multiple`, `goodmanbacon2021`, `dechaisemartin2020`, `arkhangelsky2021sdid`, `chernozhukov2021conformal`, `conley2011`, `ibge2017censoagro`.

O que o texto novo afirma sobre a literatura de inferência e de identificação, e o que a fonte diz:

| Afirmação do texto | Fonte | Veredito |
|---|---|---|
| Ferman e Pinto "admite heterocedasticidade por tamanho de município" (`05:264-265`) | Resumo: método para poucos tratados e muitos controles sob heterocedasticidade, com o exemplo da variação no tamanho dos grupos | VERIFIED |
| "Ele supõe municípios independentes" (`05:267`; `ap:456`) | Versão de trabalho (MPRA 73683), Assumption 1 (Independence): independência entre grupos | VERIFIED (na versão de trabalho) |
| MacKinnon e Webb: o *wild cluster bootstrap* não é defensável com tão poucos tratados (`05:261-263`) | Resumo: a inferência com *t* ou com o *wild cluster bootstrap* "is known to fail when the number of treated clusters is very small" | VERIFIED |
| Hagemann: procedimento para um único agregado tratado (`05:268-270`) | Resumo: número finito de clusters heterogêneos com um único tratado | VERIFIED |
| Conley e Taber; Canay et al. como sensibilidade (`05:270-272`) | Nenhuma propriedade é atribuída; títulos e, em Canay et al., resumo conferem | VERIFIED |
| Rambachan e Roth: intervalo de sensibilidade a desvios "do tamanho observado antes da lei" (`05:128-131`; `ap:470-473`) | Resumo: restrições sobre quão diferentes as violações pós-tratamento podem ser das pré-tendências; análise de sensibilidade | VERIFIED |
| Olden e Møen: a diferença tripla exige uma única hipótese de tendências paralelas (`03:81-82`; `05:120-123`) | Resumo: "requires only one parallel trend assumption to hold" | VERIFIED |
| Ortiz-Villavicencio e Sant'Anna: com covariáveis, a regressão de efeitos fixos e a diferença de dois DiD deixam, em geral, de ser válidas; estimador duplamente robusto (`03:83-86`; `05:131-133`; `ap:165`) | Resumo no arXiv: mesmas duas implementações "generally invalid when identification requires conditioning on covariates"; propõe RA, IPW e DR | VERIFIED |
| Denteh e Kédagni: falsos positivos atenuam (`05:204-206`) | Corolário 1 da v3: sem falso negativo, θ = P(ε=0 \| D=1)·ATT, "attenuation bias" | VERIFIED |
| Callaway, Goodman-Bacon e Sant'Anna: nível sob tendências paralelas usuais, curva sob hipótese mais forte (`03:78-80`) | Resumo do NBER | VERIFIED |

Calzada et al. (lido o manuscrito de março de 2023, 41 p.):

| Afirmação do texto | Fonte | Veredito |
|---|---|---|
| "cerca de 80 gramas na especificação principal (Tabela 3, coluna 2…)" (`03:31-33`) | Tabela 3, coluna (2): Banana Exposure × Intensive Fumigation = −80,02 (30,81) | VERIFIED no manuscrito de 2023 |
| "até 150 conforme a exposição" | Resumo e conclusão: "between 80 and 150 grams, with an impact that depends on the number of months of exposure" | VERIFIED |
| até 150 metros do perímetro; três meses ou mais de fumigação intensiva | Seções 1 e 4 | VERIFIED |
| além de 150 metros, sem diferença entre gestados dentro e fora dos períodos | Figura 3 e texto: gradientes "quite similar" entre 150 e 2.500 m | VERIFIED |
| "vinte ou mais ciclos por ano" (`03:37-38`) | "from 20 applications (cycles) per year per plantation to almost one application per week" | VERIFIED |
| efeito nos dois primeiros trimestres, estimativa imprecisa no terceiro (`03:55-57`) | Colunas (3) a (6): 1º e 2º significativos; 3º não significativo | VERIFIED |
| fumigação o ano inteiro, mais intensa na estação chuvosa (`02:37-38`) | Seção 1 | VERIFIED |
| a doença combatida não é a mesma (`01:55-56`) | Sigatoka Negra no Equador; sigatoka-amarela no Dossiê (p. 152) e nas reportagens | VERIFIED |
| Localizador "versão de trabalho de 2023, não conferida contra a publicada" | A declaração é honesta. O repositório da Universidade de Barcelona (hdl 2445/213742) deposita, como "versão publicada" do artigo do JAERE, o mesmo arquivo de março de 2023 (comparei byte a byte com a cópia da NBER). A versão diagramada pela revista não foi aberta | UNVERIFIABLE_ACCESS para a numeração de tabela na versão diagramada (nota N-2) |

Magnitudes e grade (`05:223-228`; `ap:402-415`; Quadro da grade):

- 80 e 150 gramas têm fonte (acima). 40 gramas, o desconto de metade, a grade de frações de 0,05 a 0,50 e a fração 0,25 **não têm fonte**, e o texto o diz em cada caso ("o desconto de metade não tem fonte"; "A fração exposta também não tem fonte neste projeto"). Honesto.
- Aritmética da grade: os doze produtos conferem (2, 4, 10, 20; 4, 8, 20, 40; 7,5, 15, 37,5, 75).
- A faixa de 23 a 32 gramas de Reynier e Rubin (`03:29-31`) está na Discussão do artigo ("reduced average birthweight by 23 to 32 g at the average level of glyphosate exposure"). VERIFIED.

Leis municipais de Limoeiro do Norte: Lei 1.478, de 20/11/2009 (página da Câmara); Lei 1.511, assinada em 26/05/2010, art. 212 revoga a 1.478 e art. 214 fixa 1.000 e 500 metros (PDF oficial em `docs/legislacao/`, p. 65–67, lido por mim). VERIFIED.

Dossiê Abrasco: p. 69, "de seis a oito vezes por ano"; p. 152, "eram realizadas no mínimo seis pulverizações durante a quadra chuvosa", com remissão a Marinho, Carneiro e Almeida (2011). "Relato de 2011 e no pretérito" (`07:24-25`): VERIFIED.

## Fase C — dados e consistência

### C1. Dados de terceiros

| Dado no texto | Conferência | Resultado |
|---|---|---|
| 36 estabelecimentos com aplicação por aeronave, em 7 dos 184 municípios (`02:59`) | API do IBGE, tabela 1008, categoria "Por aeronave", Ceará: Limoeiro do Norte 18, Quixeré 9, Aiuaba 5, Jaguaruana 1, Mauriti 1, Quiterianópolis 1, Quixeramobim 1 | confere |
| A banana está presente na maior parte do estado (`02:61-62`) | API do IBGE, tabela 1613, banana, 2015–2018: 169 de 184 municípios com área colhida | confere |
| 23 pontos; procimidona e carbaril em todos; carbofurano 18; fenitrotiona 16; glifosato 4 (`02:46-48`) | Justificativa do PL 18/2015 | confere |
| Datas das leis estaduais, do PL 134/2011 (31/05/2011) e do PL 18/2015 (24/02/2015) | páginas da Assembleia | conferem |
| Texto do caput e do § 2º do art. 28-B | Lei 16.820 | confere |
| Relatório mensal com município, cultura, área e produto (`05:162-164`) | IN 2/2008, art. 14, I, alíneas c, e, f, g | confere |
| Receituário registra a modalidade de aplicação | Decreto 4.074/2002, art. 66, IV, d | confere |
| Lei 12.228: municípios legislam supletivamente (`06:33-34`) | art. 29 | confere |
| ADI 6137: maio de 2023, caput e § 1º | resumo de jurisprudência (julgamento em 26/05/2023; constitucionalidade do § 1º e do caput) | confere |
| Troca do formulário de nascido vivo em 2011 altera a idade gestacional | documento do Ministério da Saúde | confere |

### C2. Nenhum número de estimativa própria

Li corpo, resumo, quadros e apêndices procurando número com cara de estimativa. **Nenhum valor de coeficiente, de erro-padrão, de p-valor ou de efeito mínimo detectável.** Os números presentes são de desenho (contagens de municípios, janelas, limiares, produtos da grade), da literatura, do Censo ou de datas e horários. O Quadro da grade diz na fonte que os valores "são produtos de desenho, e não estimativas".

Uma nota, N-1, que não conto como problema e que o pesquisador deve decidir: a frase "o efeito detectável ficou acima do efeito plausível dessa célula, tanto com os sete municípios … quanto só com os dois" (`ap:420-422`), lida com a célula em negrito do Quadro da grade (20 gramas), dá um **limite inferior numérico** para o efeito detectável exploratório nos dois recortes. Não é um valor, mas é uma desigualdade sobre um número próprio. A resposta aos resíduos reconhece o cuidado (limitou a frase a "fração menor" para não dar limite pela grade inteira); a célula que decide já o dá.

### C2. Aritmética de desenho

- Estação provisória de fevereiro a maio, janela de t−9 a t−4: exposição alta para nascidos de agosto a dezembro (P = 3/6, 4/6, 4/6, 4/6, 3/6); intermediária para janeiro, fevereiro, junho e julho (2/6, 1/6, 1/6, 2/6); referência para março a maio (0). **Confere** com `ap:124-126`: 5, 4 e 3 meses.
- "Toda gestação a termo a atravessa em algum trimestre" (`05:95`): nove meses de doze sempre tocam uma estação de quatro. Confere. As de referência têm só o terceiro trimestre na estação (1, 2 e 3 meses). Confere.
- Chuva: quadra do ano de nascimento, salvo janeiro e fevereiro (ano anterior). Refiz para as nove coortes com P > 0. Confere.
- Pico sazonal: "sob distribuição uniforme concentrariam um terço" (4/12). Confere.
- Data-limite: bimestre 1 = dezembro de 2026 e janeiro de 2027; o terceiro termina em 31/05/2027. Confere.
- Coortes de Limoeiro "com início de gestação na estação de 2010": nascidas de junho de 2010 a fevereiro de 2011. A conta confere com a definição. A definição deixa de fora coortes afetadas: ver F-MINOR-7.
- `Seca_t` (nascidas de 2013 a 2018) e a seca de 2012–2017: ver F-MINOR-6.

### C2. Consistência entre resumo, corpo, Quadro da regra e Apêndices B, C, E, F

Conferem entre si: referência 2007–2011 (resumo, `01`, `04`, `05`, Apêndices B, C, E, F); classificação com 2008–2011 e hipótese declarada sobre 2007; seca 2012–2017; `Seca_t` 2013–2018; pós-lei a partir de 2020; 2012 e 2019 excluídas; 2005 e 2006 só no estudo de evento; fim da janela em 19/12/2024; H1 a H5 (Capítulo 4 e Apêndice C); numeração das seis linhas da regra em todas as remissões (linha 2 em `05:283` e `ap:423`; linha 5 em `05:40`, Apêndices B, E e F; linha 6 nos casos intermediários); precedência (4 sobre 5, 5 sobre 1 a 3); as quatro condições da conclusão confirmatória (`ap:474-480`) contra o corpo (`05:139-143`, `05:268-270`, `05:298-300`); o que a ratificação não altera (período de referência e Quadro da regra, em `05:295-298` e `ap:314-317`); data-limite (`05:229-231` e cronograma). Divergências: F-MINOR-5, 6 e 7.

### C4. Proveniência de experimentos

"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

D7: declaração presente (`no_experiments_declared`, `declared_by: scholar`, `declared_at`), `experiment_provenance[]` ausente: condições 1, 2, 3 e 5 passam. **Condição 4: FAIL formal.** O texto traz frase de resultado próprio, em primeira pessoa, sem marcador de referência: "A rodada exploratória de novembro, com classificação e estação provisórias, indicou efeito detectável acima do plausível na célula que decide" (`05:280-283`). Saídas possíveis, todas do pesquisador: trocar a declaração para `experiments_declared` e registrar a proveniência das duas rodadas; retirar a frase; ou registrar justificativa. Nenhuma linha de `experiment_alignment_results[]` foi emitida, porque não há manifesto de afirmações com `planned_experiment_ids`.

## Fidelidade do texto à rodada exploratória

Conferido contra `mapa-de-lacunas-e-exploratorio.md`, os quatro roteiros em `scripts/exploratorio/` (lidos, não executados), `RETOMAR.md`, `docs/pre-especificacao.md` e o histórico do git. Não abri `data/` nem `projeto-pesquisa/data/`.

| Afirmação do texto | Registro | Resultado |
|---|---|---|
| "indicou efeito detectável acima do plausível na célula que decide" (`05:280-283`; `ap:420-424`) | O mapa registra o efeito detectável por permutação nos dois recortes; ambos ficam acima do valor da célula | **fiel** |
| "tanto com os sete municípios do Censo de 2006 quanto só com os dois da Chapada do Apodi" | idem | fiel |
| "A escolha de 0,25, e não de fração menor, não muda o lado" | verdadeiro; e é correto não estender a frase à grade inteira, porque ela não vale para todas as células | fiel |
| "calculado por permutação, com o período inteiro e com a classificação e a estação provisórias" | roteiro 21, função `permuta`, amostra com referência, seca e pós | fiel |
| Novembro: sem plano e sem a chuva; fevereiro a maio; limiar de metade; 2007–2011; 2012 e 2019 fora | roteiro 21 (`REF`, `SECA`, `POS`; `P >= 0.5`) | fiel |
| Três grupos tratados (7, 2, 5); referência 2008–2010; pós sem 2020–2021; tratamento falso; estudo de evento com base 2011 | roteiro 21 e mapa | fiel |
| Cinco grupos de comparação potiguares | mapa, seção 4 (cinco linhas) | fiel |
| "o limiar de exposição alta e a exclusão de 2012 e 2019 não foram variados" | roteiros 21 e 22 | fiel |
| Setembro: plano fechado em 21 de setembro; alvo revisto no dia seguinte, da curva para o nível | `docs/pre-especificacao.md` (fechada em 21/09; linha de desvio de 22/09); commit de fechamento às 23h05, estimações depois | fiel |
| Roteiros de novembro fora do repositório; gravação entre 23h23 e 23h45 | não rastreados no git; datas de arquivo 23:23:27 a 23:45:36 | fiel |
| "três definições do grupo de comparação" | roteiro 21: a principal (0,5; ≥ 10) e três alternativas (0,75; ≥ 10), (0,5; ≥ 50), (0,0; ≥ 10) | **F-MINOR-1** |
| "Um roteiro de estudo de evento com bases em 2014 e 2018 e com a idade da mãe como desfecho foi escrito na mesma rodada" | `RETOMAR.md:28`: "só 1 de 6 rodadas terminou; o processo foi morto por falta de memória" | **F-MEDIUM-1** |
| Escolhas em versões "entre 18h16 e 22h12" | commits: 19h45, 20h58, 21h19, 22h12; o de 18h16 não traz nenhuma delas | **F-MINOR-2** |
| "Só as escolhas têm, portanto, registro verificável" | os commits estão no remoto (`origin/claude/gifted-maxwell-ryr7yk`) | fiel |

## Formais

- Citações e `\ref` indefinidas: **zero**. Nenhum `??` no PDF nem no `.log`; nenhum aviso de referência ou citação indefinida.
- Páginas: PDF de 40 páginas; parte textual da p. 5 à p. 19, **15 páginas**; Referências começam na **p. 20** (`projeto.toc` e PDF conferem).
- `Overfull`: nenhum no `.log`.
- BibTeX: zero avisos.
- Lista de referências: uma entrada com caixa quebrada (F-MINOR-8) e duas com campo de acesso fora do padrão (F-MINOR-11).

## Fase D — originalidade

Não enviei trecho do projeto nem o nome do pesquisador a buscador algum. A comparação foi feita lendo os parágrafos novos contra as fontes que abri.

| Bloco novo | Fontes comparadas | Grau |
|---|---|---|
| `03` §3.2, primeira regularidade (Reynier e Rubin; Calzada et al.; Rigotto et al.) | PNAS; manuscrito de 2023; SciELO | ORIGINAL (fatos com citação) |
| `03` §3.2, concentração (Larsen et al.; Jones) | resumos | ORIGINAL |
| `03` §3.2, calendário (Brainerd e Menon; Buckles e Hungerman; Currie e Schwandt; Rocha e Soares) | resumos; PNAS | ORIGINAL |
| `03` §3.3 (Olden e Møen; Ortiz-Villavicencio e Sant'Anna; Callaway et al.) | resumos | PARAPHRASE com citação em duas frases (a de Olden e Møen e a de Ortiz-Villavicencio e Sant'Anna seguem de perto o resumo, em tradução) |
| `02` §2.2, frequência das aplicações | Dossiê p. 69 e 152; Globo Rural | ORIGINAL |
| `05` §5.7, primeiro parágrafo (inferência) | resumos | ORIGINAL |
| `ap` F.3, magnitudes | manuscrito de 2023 | ORIGINAL |

| Grau | Blocos | Proporção |
|---|---|---|
| ORIGINAL | 6 | 86% |
| COMMON_KNOWLEDGE | 0 | 0% |
| PARAPHRASE (com citação) | 1 | 14% |
| CLOSE_MATCH | 0 | 0% |
| VERBATIM | 0 | 0% |

Cobertura real: 7 blocos de cerca de 70 parágrafos, perto de 10%, todos os que resumem literatura no texto novo; nenhum parágrafo foi buscado na web. Abaixo dos 50% do protocolo. D2 não executado.

> Esta verificação de originalidade é comparação heurística contra as fontes abertas, não um detector de plágio profissional (Turnitin, iThenticate). Cobertura de cerca de 10%, restrita às fontes citadas; há risco de não detecção. Recomenda-se ferramenta profissional antes da submissão formal.

## Fase E — afirmações

Registro à mão, 42 afirmações factuais ou quantitativas com fonte externa citada (as das tabelas das Fases B e C1, mais as sete das fontes documentais novas e as duas dos achados abaixo). 39 VERIFIED; 2 MINOR_DISTORTION (F-MINOR-3 e F-MINOR-4); 1 UNVERIFIABLE_ACCESS (N-2). Zero MAJOR_DISTORTION, zero UNVERIFIABLE. As 14 afirmações sobre a rodada exploratória foram conferidas contra o repositório e estão na seção de fidelidade, fora desta contagem.

- Artefato `claim-registry/1.0`: não gerado. Relatório de cobertura (#737): `not_run` → **E1-COVERAGE-UNRESOLVED**. Linhas de evidência (#656): não persistidas; `evidence_source_dir`: o despacho não nomeou pasta.
- E4 (escopo): `[E4-SKIPPED: no scope context]`.
- E5 (novidade), consultivo: ADV-E5-1, `01:22-23` "não se localizou, na literatura consultada, avaliação causal"; ADV-E5-2, `01:60-61` "Entre os trabalhos localizados, nenhum avalia uma proibição de método". Redação limitada à busca, mas sem protocolo nem data de busca: `UNRESOLVED` (é a pendência REV-17 dentro de RES-17).
- E6 (deriva de força): contrato não executado (revisão por edição direta, sem pacote de evidência). Uma mudança de força observada à mão: ADV-E6-1, `05:279-284`, de "não se sabe ainda qual linha é a provável" para "indicou efeito detectável acima do plausível … linha 2"; item do roteiro que a autoriza: RES-01, marcado "provisório, a ratificar pelo autor". Sem a disposição do autor o checkpoint fica fechado.

## Lista de achados (por gravidade)

### SERIOUS

Nenhum.

### MEDIUM

| ID | Local | O que o texto diz | O que o registro diz | Fonte | Correção de uma linha |
|---|---|---|---|---|---|
| F-MEDIUM-1 | `apendices.tex:534-535` (F.6) | "Um roteiro de estudo de evento com bases em 2014 e 2018 e com a idade da mãe como desfecho foi escrito na mesma rodada." Fica fora de "Foram estimados". | O roteiro `23_leads_lags_exploratorio.py` foi executado em parte: "só 1 de 6 rodadas terminou; o processo foi morto por falta de memória". A primeira das seis é a dos sete municípios com base 2018. A data do `__pycache__` (23:45:46, dez segundos depois da gravação do roteiro) é coerente com a execução. Não abri a saída. | `docs/ars/rodada21-local/RETOMAR.md:28`; `scripts/exploratorio/23_leads_lags_exploratorio.py:172-177` | Trocar "foi escrito na mesma rodada" por "foi escrito na mesma rodada, e só a primeira de suas seis estimações terminou" (o pesquisador confirma qual). |

### MINOR

| ID | Local | O que o texto diz | O que a fonte ou o registro diz | Fonte | Correção de uma linha |
|---|---|---|---|---|---|
| F-MINOR-1 | `apendices.tex:529-531` | "três definições do grupo de comparação" | São quatro: a principal e três alternativas; uma delas com limiar familiar zero, isto é, sem exigir predominância familiar. | `scripts/exploratorio/21_calendario_exploratorio.py:132,169` | "quatro definições do grupo de comparação (a principal e três alternativas, uma delas sem o critério familiar)". |
| F-MINOR-2 | `apendices.tex:541-542` | escolhas em versões "entre 18h16 e 22h12" | O commit de 18h16 (`df25151`) não traz nenhuma das escolhas listadas. Elas entram às 19h45 (comparação familiar, `5c6cac4`), 20h58 (referência, `b46e878`), 21h19 (2012 e 2019; pós-lei em 2020, `96dc402`) e 22h12 (limiar de metade, `1e71a72`). A ordem em relação aos roteiros (23h23) não muda. | `git log` de `paper/projeto/secoes/05-metodologia.tex` | Trocar "18h16" por "19h45". |
| F-MINOR-3 | `02-contexto.tex:20-21` | "(aprovação unânime, em dezembro de 2018 \cite{lavor2019antes})" | A reportagem diz "sem nenhum voto contrário" e não dá a data. A data (18/12/2018) é verdadeira, por outra fonte. | https://apublica.org/2019/02/antes-do-ceara-8-municipios-ja-haviam-proibido-fumigacao-aerea-de-agrotoxicos/ ; https://www.brasildefato.com.br/2018/12/19/assembleia-legislativa-proibe-pulverizacao-aerea-de-agrotoxicos-no-ceara-entenda/ | "(aprovação sem voto contrário \cite{lavor2019antes}, em dezembro de 2018)". |
| F-MINOR-4 | `07-ameacas.tex:13-14` | "Ela restringiu a água de irrigação no Baixo Jaguaribe \cite{pereira2015conflitos}" | O artigo diz que, de início, a seca não impediu a expansão da agricultura irrigada e que os perímetros aumentaram a produção; o racionamento começa em meados de 2014 (50% no arroz e 8,5% nas frutas, em Tabuleiro de Russas). | https://periodicos.usp.br/eav/article/download/104951/103740/184424 | "Ela levou, a partir de 2014, ao racionamento da água de irrigação no Baixo Jaguaribe". |
| F-MINOR-5 | `08-cronograma.tex:15-16` | "na 6 não há medida dos voos" | Quadro da regra, linha 6: "medida parcial dos voos, se houver"; `ap:504`: cadastro, autos de infração e autos da ação "como medida parcial". | `05-metodologia.tex:251`; `apendices.tex:504` | "na 6 a medida dos voos é, no máximo, parcial". |
| F-MINOR-6 | `05-metodologia.tex:64-65` | `Seca_t`: coortes nascidas de 2013 a 2018, "cujo início de gestação cai nos anos de seca" | Para as de exposição alta nascidas de agosto a dezembro de 2018, o início da gestação cai na quadra de 2018, depois da seca de 2012–2017; o Apêndice F o diz (`ap:355-359`), o corpo não. | `apendices.tex:355-359` | Inserir "em geral": "cujo início de gestação cai, em geral, nos anos de seca". |
| F-MINOR-7 | `apendices.tex:151`; `05-metodologia.tex:110-111` | O corpo promete "a exclusão das coortes de Limoeiro afetadas"; o Apêndice C exclui as "com início de gestação na estação de 2010 (nascidas de junho de 2010 a fevereiro de 2011)". | As coortes de referência nascidas de março a maio de 2010 tiveram o terceiro trimestre na estação de 2010, sob a proibição municipal (20/11/2009 a 26/05/2010), e ficam na amostra; pelo próprio desenho, a exposição delas também mudou. | conta sobre `apendices.tex:120-126` | No Apêndice C: "Exclui, em Limoeiro do Norte, as coortes com algum trimestre na estação de 2010 (nascidas de março de 2010 a fevereiro de 2011…)"; ou manter e declarar que as de referência de março a maio de 2010 permanecem. Decisão do pesquisador. |
| F-MINOR-8 | `../referencias.bib:47`; lista, p. 21 | "CAMACHO, A.; MEJíA, D." | Caixa quebrada: o "í" entra como caractere direto e o estilo não o põe em maiúscula. | `projeto.bbl:142-143` | `author = {Camacho, Adriana and Mej{\'i}a, Daniel}`. |
| F-MINOR-9 | `referencias-projeto.bib:256-263` | autor "Globo Rural" | A reportagem é assinada por Eliane Silva (09/04/2021). Título e data conferem. | https://globorural.globo.com/Noticias/Agricultura/noticia/2021/04/pulverizacao-aerea-de-bananais-no-ce-e-alvo-de-acao-no-stf.html | `author = {Silva, Eliane}` e `note = {Globo Rural, S{\~a}o Paulo, 9 abr. 2021}`. |
| F-MINOR-10 | `referencias-projeto.bib:296` | "o documento não traz data de publicação" | O documento termina com "Brasília, 28 de maio de 2013". | http://tabnet.datasus.gov.br/cgi/sinasc/Consolida_Sinasc_2011.pdf | `note = {Bras{\'i}lia, 28 maio 2013}`. |
| F-MINOR-11 | `referencias-projeto.bib:156-162` e `10-16` | `ibgepam`: "Acesso em: 25 ago. 2026" dentro da nota, antes de "Disponível em"; `denteh2022misclassification`: URL sem data de acesso | Fora do padrão das demais entradas (campo `urlaccessdate`). | `projeto.bbl:327-332` e `264-269` | Mover a data para `urlaccessdate` em `ibgepam`; acrescentar `urlaccessdate = {16 nov. 2026}` em `denteh2022misclassification`. |

### Notas (não são problemas)

| ID | Local | Nota |
|---|---|---|
| N-1 | `apendices.tex:420-424` com o Quadro da grade | A divulgação qualitativa, lida com a célula em negrito, dá limite inferior numérico ao efeito detectável exploratório. Decisão do pesquisador sobre a restrição "nenhum número de estimativa". |
| N-2 | `03-referencial.tex:32-33` | Tabela 3, coluna 2, conferida no manuscrito de março de 2023, que o repositório da Universidade de Barcelona deposita como versão do artigo. A versão diagramada do JAERE não foi aberta; a ressalva do texto continua exata. |
| N-3 | `apendices.tex:195` | "Há registro, em reprodução que não se conseguiu reabrir, de nota oficial de março": afirmação sem fonte, declarada como pista. Mantida fora dos achados porque o texto não a apresenta como fato. |
| N-4 | `04-objetivos.tex`, `05-metodologia.tex:104-106` | "A escolha foi registrada em 15 de novembro de 2026 … antes da de novembro": confere com os commits (20h58 contra 23h23). O intervalo é de horas, e o texto o diz. |

## Itens congelados da re-revisão

| Item | Estado no texto atual |
|---|---|
| RES-13 (em parte) | **Quase fechado por esta verificação.** Localizador dos 80 g conferido no manuscrito de 2023 (N-2). Os 150 g estão no resumo, na introdução e na conclusão do mesmo manuscrito; os 23 a 32 g, na Discussão de Reynier e Rubin. O texto segue sem localizador para esses dois; não é erro. Falta só a versão diagramada do JAERE. |
| RES-17 | **Pendência do autor, mantida.** Protocolo e data da busca: ausentes (ADV-E5-1 e 2). Página do Dossiê: há página para a frequência dos voos (p. 69 e 152); a tabela de água segue citada pela justificativa do PL, com atribuição ("atribuída ao Dossiê"). Estimativas por trimestre: não entraram; conferi que existem na Tabela 3. Dispersão contra vetores: limitação declarada (`06:43-46`). Supressão e guarda: remetidas ao plano (`06:58-60`). Tramitação de 2018: a data confere por fonte secundária, mas a citação não a sustenta (F-MINOR-3). Série de chuva: só reportagem. Número da ação: não localizado; a página do MPT não o traz. |
| RES-18 | **Pendência do autor, mantida.** Sem mudança de texto; chuva pela quadra de exposição e vizinhos fora da comparação seguem em `ap:126-130`, à espera de confirmação. |
| NEW-1 | Resolvido no texto (`05:279-284`; `ap:417-428`). Gera a divulgação nova: ver C4, N-1 e Modos 1, 3 e 6. |
| NEW-2 | Resolvido (`05:226-227`). |
| NEW-3 | Resolvido no apêndice (`ap:355-359`). Resta o corpo: F-MINOR-6. |
| NEW-4 | Resolvido: precedência na nota do Quadro (`05:254`); quatro condições em `ap:474-480`. A linha 1 do Quadro segue sem remissão própria; a nota remete ao apêndice. |
| NEW-5 | Resolvido (`05:250`). |
| NEW-6 | Resolvido (`ap:348-353`). Provisório, a ratificar. |
| NEW-7 | Resolvido na redação (`ap:543-548`). Resíduo: F-MINOR-2. |
| NEW-8 | Resolvido (`ap:535-537`). |
| NEW-9 | Resolvido (`08:15`; `ap:500-502`). Resíduo novo ao lado: F-MINOR-5. |
| NEW-10 | Resolvido (`05:295-298`; `ap:314-317`). |
| NEW-11 | Resolvido (`05:283-284`). |
| NEW-12 | Resolvido (`ap:343-345`). |
| NEW-13 | Resolvido (`ap:470-473`). |
| NEW-14 | Declarado no texto; conferido no manuscrito de 2023 (N-2). |
| NEW-15 | Aberto: é RES-18. |

## Checklist dos 7 modos (regra do Estágio 4.5)

A declaração é `no_experiments_declared`, com `scholar_answer` "Não reporta". O texto apresenta análises próprias como feitas ("estimou a forma reduzida estadual"; "estimou o desenho de calendário"; "indicou efeito detectável acima do plausível"). Pela regra, declaração e texto discordam: nenhum dos Modos 1, 3, 5 e 6 é NOT APPLICABLE, e os Modos 3 e 6 ficam SUSPECTED.

| Modo | Resultado | Evidência | Bloqueia? |
|---|---|---|---|
| 1. Erro de implementação que passa pela autorrevisão | **INSUFFICIENT EVIDENCE** | No 2.5 o texto não afirmava resultado algum. Agora afirma o sentido de um (efeito detectável acima da célula que decide). Li o roteiro 21, não o executei e não vi registro de execução nem a saída. A margem registrada no mapa é larga nos dois recortes, o que torna improvável que um erro inverta o lado; não é prova. | **sim** |
| 2. Citação alucinada | CLEAR | 58 de 58 existem; nenhum DOI desviado; três imprecisões menores de metadado. | não |
| 3. Resultado experimental alucinado | **SUSPECTED** (regra formal; no mérito, sem contradição) | O único resultado afirmado confere com `mapa-de-lacunas-e-exploratorio.md`. Não conferi contra a saída bruta. | **sim** |
| 4. Atalho | CLEAR | Não há afirmação de efeito nem de desempenho; o confundidor mais óbvio (chuva) é declarado e a regra exige concordância. | não |
| 5. Erro reenquadrado como achado | CLEAR | Nenhuma narrativa de surpresa; o resultado divulgado é desfavorável ao teste e não é apresentado como descoberta. | não |
| 6. Fabricação de metodologia | **SUSPECTED** (regra formal e, em pequena medida, mérito) | A descrição do que foi rodado diverge do registro em dois pontos: uma estimação do roteiro 23 terminou e o texto diz só "foi escrito" (F-MEDIUM-1); quatro definições de comparação, e não três (F-MINOR-1). O restante confere. | **sim** |
| 7. Travamento de enquadramento | INSUFFICIENT EVIDENCE | O texto diz que, sob as escolhas provisórias, a indicação é a linha 2 (sem teste), e mantém o desenho de calendário como principal, com saídas declaradas. Seguem abertos o grupo tratado (sete ou dois), o limiar familiar e a comparação potiguar. Pergunta ao pesquisador: sabendo da indicação, o desenho principal continua o mesmo? | não (aviso) |

**A justificativa do pesquisador ainda cobre?** Em parte, e não basta repeti-la.

- A justificativa era: "Projeto, não resultado: É um projeto de pesquisa: descreve o que será feito. As duas rodadas exploratórias estão declaradas no texto, sem número, e serão refeitas a partir das bases originais."
- **Modo 6:** continua válida para a metodologia futura. Não cobre a lista de variantes do Apêndice F, que é relato do que foi feito e tem uma omissão (F-MEDIUM-1). Corrigida a omissão, a justificativa volta a cobrir.
- **Modo 3: a divulgação nova muda o mérito.** "Descreve o que será feito" já não é toda a verdade: o texto relata o sentido de um resultado exploratório e o usa para explicar por que a célula que decide não é pré-especificada. "Sem número" continua verdadeiro na letra; com a célula em negrito, há um limite numérico implícito (N-1). A justificativa precisa ser registrada de novo e dizer isto expressamente: que o texto divulga, de propósito e sem valor, o lado em que o portão cai na rodada de novembro; que o resultado confere com o registro; e que será recalculado como o Apêndice F descreve. No mérito não encontrei nada que contradiga o registro.
- **Modo 1:** não estava em causa no 2.5 e a justificativa antiga não o cobre. Pede resposta própria: o pesquisador tem a saída da permutação gravada e a execução terminou sem erro?

## Não conferido

| Item | Motivo |
|---|---|
| Versão diagramada de Calzada et al. no JAERE (numeração da Tabela 3) | Acesso pago; o depósito aberto é o manuscrito de março de 2023. |
| Data do DJe da ADI 6137 ("14 jun. 2023", `referencias-projeto.bib:175`) | Não abri o acórdão; um resumo de jurisprudência dá "Publicação: 02/06/2023". Relatora, mês do julgamento e dispositivos conferem. |
| Ano "2012" de `ibge2006censoagro` | A API do IBGE não informa a data de publicação da tabela 1008. O dado confere. |
| Página do SIDRA de `ibge2017censoagro` | HTTP 403. Existência conferida pela API (tabela 6955, Censo Agropecuário 2017) e pela data de divulgação dos resultados definitivos (25/10/2019). |
| Texto integral de Conley e Taber, Canay et al., Baker et al., Goodman-Bacon, de Chaisemartin e D'Haultfœuille, Callaway e Sant'Anna (2021), Arkhangelsky et al., Chernozhukov et al., Camacho e Mejía, Dias et al., Coase, Weitzman, Lichtenberg et al., Helfand e House | Só metadados e, quando havia, resumo. O texto lhes atribui o tema ou resultado de manual. |
| Ferman e Pinto, versão publicada | A hipótese de independência foi lida na versão de trabalho (MPRA 73683). |
| Saídas das rodadas exploratórias (`data/`, `projeto-pesquisa/data/`) | Fora do escopo por instrução. A fidelidade foi conferida contra o mapa, os roteiros e o `RETOMAR.md`. |
| Execução parcial do roteiro 23 | Apoiada em `RETOMAR.md:28` e na data do `__pycache__`; não vi a saída. O pesquisador confirma. |
| Ausência de lei municipal de Limoeiro posterior a 2010 ("legal e regulada até a lei estadual", `02:67-68`) | Não refiz o levantamento; o texto diz que ele será refeito. |
| Nota oficial de março de 2011 (Apêndice D) | O texto a declara como pista não reaberta; não tentei localizá-la. |
| Artefatos do protocolo: registro de afirmações, cobertura (#737), linhas de evidência (#656), E6, verificação entre modelos | Não executados. `ARS_CROSS_MODEL` não foi usado. |

## Trilha de auditoria (resumo)

- Crossref: 31 DOIs, um por chamada, 2,5 s de intervalo, sem erro 429. Saída: autores, título, periódico, volume, número, páginas, datas.
- arXiv: 2207.11890 (v1 a v3; PDF da v3 lido), 2505.09942 (v1 a v3), 2107.02637 (v1 a v8).
- NBER w32117; aeaweb.org/journals/aer/forthcoming (artigo listado).
- Calzada et al.: conference.nber.org/conf_papers/f181409/f181409.pdf e diposit.ub.edu, hdl 2445/213742 (arquivos idênticos).
- Dossiê Abrasco: icict.fiocruz.br/sites/www.icict.fiocruz.br/files/DossieAbrasco_2015_web.pdf (texto extraído; busca por "seis a oito vezes", "seis pulverizações").
- IBGE: servicodados.ibge.gov.br/api/v3/agregados/1008, 1613 e 6955.
- Assembleia do Ceará: leis 12.228, 16.820, 19.135; PL 134/2011; PL 18/2015.
- Câmara de Limoeiro do Norte: /leis/549; PDF local da Lei 1.511 (p. 65–68).
- MAPA: IN 2/2008 (PDF, art. 14); Portaria 298/2021 (DOU de 24/09/2021, Seção 1, p. 14, por busca).
- Planalto: Decreto 4.074/2002, art. 66.
- STF: noticias.stf.jus.br (ADI 7794); portal.stf.jus.br (ADI 6137, relatora); informativos.trilhante.com.br (julgamento e dispositivos).
- Notícias: Agência Brasil (16/07/2016), Globo Rural (09/04/2021), Agência Pública (15/02/2019), UOL (03/03/2018), MPT-CE (07/07/2011), SINDAG (17/06/2021), HGCC (26/03/2018), Brasil de Fato (19/12/2018, só para a data da votação).
- Resumos: RePEc (Ferman e Pinto; Rambachan e Roth; Canay et al.; Rocha e Soares; Brainerd e Menon), OUP (Olden e Møen; MacKinnon e Webb; Hagemann; Böcker et al.), PNAS (Reynier e Rubin; Currie e Schwandt), Land Economics (Jones), SciELO (Rigotto et al.), USP (Pereira e Cuellar, texto integral), MPRA 73683 (Ferman e Pinto).
- Repositório: `git log` e `git show` das versões de `05-metodologia.tex` de 15/11/2026; leitura dos roteiros `scripts/exploratorio/20` a `23`; `projeto.log`, `.blg`, `.toc`, `.bbl`; texto extraído do PDF.
