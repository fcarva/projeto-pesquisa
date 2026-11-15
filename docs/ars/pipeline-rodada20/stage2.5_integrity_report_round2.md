# Academic Integrity Verification Report

*ARS v3.24.2 · `integrity_verification_agent` · Estágio 2.5 · reverificação da rodada 1 de correções · concluída em 2026-11-15T22:01Z (UTC).
Manuscrito no commit `048d9fc` (`paper/projeto/secoes/01…08`, `paper/referencias.bib`, `paper/projeto/referencias-projeto.bib`). PDF `paper/projeto/projeto.pdf`: 21 páginas, 15 textuais.
Relatório da rodada 1: `stage2.5_integrity_report.md` (não alterado). Este agente não editou o manuscrito nem os `.bib`. Arquivos gravados: este relatório e a pasta `evidence/`.*

## Verification Mode

Initial Verification (Mode 1, pre-review), reverificação após correções (rodada 1 do laço de FAIL). Escopo, conforme o "Correction Process on FAIL": os itens corrigidos, as 9 referências novas, a consistência interna inteira (C2) e a Fase E refeita sobre o texto atual.

## Verdict

**FAIL**

Restam 2 issues MEDIUM e nenhuma SERIOUS. As duas SERIOUS da rodada 1 foram resolvidas no que tinham de erro factual. Uma das MEDIUM é efeito direto da decisão (b) do pesquisador e pode ser encerrada por decisão registrada dele; a outra é um campo de bibliografia sem base, de correção imediata. Nenhum modo de falha bloqueia. O `E1-COVERAGE-UNRESOLVED` da rodada 1 está fechado.

## Verification Summary

| Category | Total | Passed | Issues |
|----------|-------|--------|--------|
| Reference Existence | 37 (28 da rodada 1 + 9 novas) | 37 | 0 |
| Bibliographic Accuracy | 37 | 34 | 1 MEDIUM (`ibgepam`), 2 MINOR (`mapa2008in2`, `ibge2006censoagro`); mais 1 MINOR geral de completude das entradas novas |
| Ghost Citations | -- | -- | 0 órfãs na lista impressa / 0 pendentes (37 chaves citadas, 37 itens no `projeto.bbl`; 27 entradas dos `.bib` seguem sem citação e não são impressas) |
| Citation Context Accuracy | 37 de 37 chaves | 34 | 0; 3 chaves com acesso limitado (calzada2023bananas, weitzman1974, coase1960), como notas |
| Statistical Data Accuracy | 13 afirmações novas ou alteradas (tabela C1) | 11 | 2 MINOR (mês do projeto de lei de 2011; janela "posterior à primeira proposição") |
| Internal Consistency | -- | Fail | 1 inconsistência (MEDIUM): tempo verbal do texto contra o registro do repositório |
| Originality Check (D1) | não refeita nesta rodada (rodada 1: 17 de 51, 33%) | -- | -- |
| Self-Plagiarism (D2) | não refeita | -- | -- |
| Claim Verification (E) | 51 de 55 registradas (Mode 1: HIGH-IMPACT: 38, RANDOM: 0, TOP-UP: 13; NOT-SELECTED: 4, tratadas só no E5; semantic extraction coverage: not_machine_detectable; candidate gaps: 1, inspecionado, falso positivo) | 40 | 0 MAJOR_DISTORTION / 0 UNVERIFIABLE (3 MINOR_DISTORTION; 8 UNVERIFIABLE_ACCESS) |

Restrições do autor:

| Restrição | Resultado |
|---|---|
| Nenhum número de estimativa | Nenhum. Os únicos valores de efeito são da literatura (23 a 32 g; 80 a 150 g). A frase da rodada 1 sobre "o nível estimado" saiu. |
| No máximo 15 páginas textuais | 15 páginas textuais (numeração impressa 3 a 17; referências a partir da 18). No limite, sem folga: qualquer acréscimo passa de 15. |
| Só o Ensaio 1 | Sem mudança: o Ensaio 2 aparece como remissão (`03-referencial.tex:26-29`; `08-cronograma.tex:15-18`) e como linha do cronograma (`08-cronograma.tex:40`). |

O PDF não foi recompilado por mim. Ele é posterior aos fontes (21:52:57 contra 21:52:53), tem 37 itens bibliográficos resolvidos e contém o texto novo ("proposição semelhante em 2011").

## Status das issues da rodada 1

| ID (rodada 1) | Status | Onde está agora | Observação |
|---|---|---|---|
| IL-SERIOUS-1 (169 e 15 na janela errada) | **Resolvida** | `02-contexto.tex:73-77`; `05-metodologia.tex:53-60`; `05-metodologia.tex:82-84` | A dose principal voltou a 2015-2018 e as contagens saíram do texto. As frases que ficaram conferem com a fonte primária: banana em 169 de 184 municípios; 162 desses 169 sem registro de aeronave; a janela 2010-2014 reduz os municípios sem a cultura de 15 para 6. |
| IL-SERIOUS-2 ("plano registrado"; estágio 1 como não estimado) | **Parcialmente resolvida** | `05-metodologia.tex:215-219` | Saíram "registrado" e a frase sobre o nível estimado; o texto agora diz "não de pré-registro público"; a dose do projeto voltou a coincidir com a do plano versionado, e `docs/ars/20` §4 registra a reversão. O que resta é a omissão da rodada anterior, agora com verbos no futuro: IL-MEDIUM-1 desta rodada. |
| IL-MEDIUM-1 (leads e início do painel) | **Resolvida** | `05-metodologia.tex:93-97` | O texto promete só o marco de certeza e diz por que os de notícia não podem ser examinados. |
| IL-MINOR-1 (Calzada, primeiro trimestre) | **Parcialmente resolvida** | `01-introducao.tex:53-55`; `03-referencial.tex:53-54`; `04-objetivos.tex:27`; `05-metodologia.tex:132-134` | A redação deixou de afirmar "mais forte no primeiro trimestre" e o estágio 3 ganhou o segundo trimestre como sensibilidade. "Início da gestação" continua sem conferência no texto publicado. Fica como nota (UNVERIFIABLE_ACCESS), não como issue. |
| IL-MINOR-2 (Skevas) | **Resolvida** | `03-referencial.tex:25` | "comparação, por simulação". |
| IL-MINOR-3 (estimadores escalonados) | **Resolvida** | `03-referencial.tex:62-64` | "os estimadores e as decomposições". |
| IL-MINOR-4 (banana "de variação mais ampla") | **Resolvida** | `05-metodologia.tex:47-50` | A afirmação saiu. A frase nova põe o diagnóstico no futuro; ver IL-MEDIUM-1. |
| IL-MINOR-5 (fonte do Quadro 1) | **Resolvida** | `02-contexto.tex:46` | A fonte declara que 2009 a 2011 vêm de fontes secundárias. |
| IL-MINOR-6 ("obtidas, inspecionadas") | **Resolvida** | `06-dados.tex:59-66` | O parágrafo foi substituído por "Escopo". A avaliação das três fontes está no futuro; ver IL-MEDIUM-1. |
| IL-MINOR-7 (`bocker2020glyphosate`) | **Resolvida** | `paper/referencias.bib` | 2020, v. 47, n. 2, p. 371-402; confere com o RePEc. |
| IL-MINOR-8 (`larsen2017agricultural`) | **Resolvida** | `paper/referencias.bib` | `pages = {302}`; confere com Crossref e OpenAlex. |
| IL-MINOR-9 (`reynier2025glyphosate`) | **Resolvida** | `paper/referencias.bib` | `pages = {e2413013121}`. |
| IL-MINOR-10 (`weitzman1974`) | **Resolvida** | `paper/referencias.bib` | 477-491; confirmado nesta rodada na página do RePEc do próprio artigo. |
| IL-MINOR-11 (`denteh2022misclassification`) | **Resolvida** | `paper/projeto/referencias-projeto.bib` | "arXiv:2207.11890, versão 3". Com a versão fixada, a afirmação C23 passa a VERIFIED. |
| IL-MINOR-12 (fontes sem entrada) | **Parcialmente resolvida** | 9 entradas novas, todas citadas | Faltam: ADI 6137 (`01-introducao.tex:84`; `02-contexto.tex:42`); o projeto de lei de 2011, agora mencionado; `\cite{ibgepam}` na frase sobre a presença da bananicultura (`02-contexto.tex:76`); `\cite{ceara1993lei12228}` em `05-metodologia.tex:117-118`. Ver IL-MINOR-5 desta rodada. |
| IL-MINOR-13 (projeto de lei de 2011) | **Parcialmente resolvida** | `02-contexto.tex:19-20`; `02-contexto.tex:38`; `05-metodologia.tex:55-60`; `07-ameacas.tex:23` | O texto passou a tratar 2011 como primeira proposição e reconhece que 2010-2014 não a antecede. O mês no Quadro 1 está errado: ver IL-MINOR-1 desta rodada. |

## Phase A: Reference Verification Results

As 28 entradas da rodada 1 não foram reverificadas do zero; só os cinco campos corrigidos, que conferem (tabela acima). As 9 entradas novas:

| Chave | Existência | Campo a campo | Fonte da conferência |
|---|---|---|---|
| ceara2019lei16820 | VERIFIED | Número e data (8 de janeiro de 2019) corretos. "Diário Oficial do Estado, 9 jan. 2019" correto. Ementa resumida corretamente. | Texto da ALECE, cópia em `docs/legislacao/lei-16820-2019.md`: "LEI N.º 16.820, DE 08.01.19 (D.O. 09.01.19)" |
| ceara1993lei12228 | VERIFIED | Número e data (9 de dezembro de 1993) corretos. Ementa truncada, mas fiel. Sem data de publicação (o `README` de `docs/legislacao/` registra D.O. de 14/12/1993; não conferi). | `docs/legislacao/lei-12228-1993-consolidada.md` |
| ceara2024lei19135 | VERIFIED | Número e data (19 de dezembro de 2024) corretos. A nota "Altera o art. 28-B" é paráfrase correta da ementa. Sem data de publicação (D.O. de 19/12/2024). | Página da ALECE, baixada nesta rodada: "LEI N.° 19.135, DE 19.12.24 (D.O. 19.12.24)" |
| ceara2015pl18 | VERIFIED | Número e data de apresentação (24 de fevereiro de 2015) corretos. Sem endereço eletrônico. | `docs/legislacao/pl-18-2015.md` (cópia do texto da ALECE) |
| brasil2002decreto4074 | VERIFIED | Número e data (4 de janeiro de 2002) corretos. "Lei nº 7.802, de 11 de julho de 1989": a data da lei confere em documento da ALECE; a ementa do decreto não foi lida no original nesta rodada. | Título no portal da Câmara dos Deputados (rodada 1); art. 66 no Planalto (rodada 1) |
| mapa2008in2 | VERIFIED | **Título incompleto**: a entrada diz "Instrução Normativa nº 2, de 2008". O correto é Instrução Normativa nº 2, de 3 de janeiro de 2008, publicada no DOU de 8 de janeiro de 2008, Seção 1. A nota "Normas de trabalho da aviação agrícola" confere com o art. 1º. IL-MINOR-3. | PDF no gov.br (rodada 1: "DE 3 DE JANEIRO DE 2008"; "D.O.U., 08/01/2008 - Seção 1"); reprodução baixada nesta rodada ("Publicado no DO em 08 jan 2008") |
| cns2016res510 | VERIFIED | Número e data (7 de abril de 2016) corretos. Sem data de publicação (DOU de 24/05/2016). | PDF da página do Conselho Nacional de Saúde, baixado nesta rodada |
| ibge2006censoagro | VERIFIED | A tabela SIDRA 1008 existe e é do Censo Agropecuário 2006. `year = {2006}` é o ano de referência do censo, não o de publicação nem o de consulta; o ano de publicação não foi conferido (o catálogo do IBGE recusou o acesso). IL-MINOR-4. | Resposta da API do SIDRA para a tabela 1008 |
| ibgepam | VERIFIED | **`year = {2024}` não tem base.** A PAM é uma pesquisa anual contínua; o texto usa as edições de 2010 a 2018, e o repositório registra extração em 25/08/2026 das tabelas 1612 e 1613 (`docs/fontes-e-vintages.md`). 2024 não é nem o ano dos dados nem o da consulta. A entrada também não identifica a tabela. IL-MEDIUM-2. | API do SIDRA (tabela 5457 nesta verificação); `docs/fontes-e-vintages.md` |

Observação comum às entradas normativas e estatísticas: nenhuma traz endereço eletrônico nem data de acesso, que a ABNT pede para documento consultado em meio eletrônico (IL-MINOR-6).

**A0.** O Semantic Scholar não cobre legislação nem tabelas estatísticas; não se aplica às 9 novas.

## Phase B: Citation Context Verification Results

Contextos das 9 chaves novas:

| Chave | Local | O que o texto atribui | Resultado |
|---|---|---|---|
| ceara2019lei16820 | `02-contexto.tex:9-13` | sanção, vigência, art. 28-B, caput, § 2º | Confere |
| ceara1993lei12228 | `02-contexto.tex:10-11` | norma alterada | Confere |
| ceara2024lei19135 | `02-contexto.tex:21-23` | nova redação; exceção para aeronaves remotamente pilotadas | Confere |
| ceara2015pl18 | `02-contexto.tex:61-65` | tabela reproduzida na justificativa, atribuída ao Dossiê ABRASCO | Confere (recontagem da rodada 1) |
| ibge2006censoagro | `02-contexto.tex:73-75` | 36 estabelecimentos em 7 dos 184 municípios | Confere |
| ibgepam | `05-metodologia.tex:45-47` | fonte da área plantada | Confere |
| mapa2008in2 | `05-metodologia.tex:111-113` | relatório mensal com município, cultura, área e produto | Confere (art. 14) |
| brasil2002decreto4074 | `05-metodologia.tex:114-115` | receita registra a modalidade de aplicação | Confere (art. 66, IV, d) |
| cns2016res510 | `06-dados.tex:76-78` | dispensa de submissão ao CEP/CONEP | Confere (art. 1º, parágrafo único) |

Nas 28 antigas, as três imprecisões da rodada 1 foram corrigidas. `cameron2008wild` passou de "acesso limitado" a "confere" (resumo obtido pelo OpenAlex). Continuam com acesso limitado: `calzada2023bananas` (texto publicado), `weitzman1974` e `coase1960` (sem resumo; texto não lido).

## Phase C: Data Verification Results

### C1. Afirmações novas ou alteradas pela correção

| # | Afirmação | Local | Resultado | Fonte e tipo |
|---|---|---|---|---|
| 1 | "precedida de proposição semelhante em 2011" | `02-contexto.tex:19-20` | Confere | **primária, obtida nesta rodada**: página da ALECE do Projeto de Lei nº 134/2011 (dep. Heitor Férrer), Sala das Sessões em 31/05/2011. O art. 4º cria um art. 28-B com a mesma redação que a lei de 2019 adotou |
| 2 | "projeto de lei estadual com o mesmo objeto (julho)" | `02-contexto.tex:38` | **Mês errado** | idem. O projeto é de 31 de maio de 2011; julho é a data da reportagem que o noticiou. O projeto é mais amplo: também proíbe onze princípios ativos e altera o cadastro de produtos. IL-MINOR-1 |
| 3 | "a proibição foi proposta em projetos de lei de 2011 e de 2015" | `05-metodologia.tex:56-57` | Confere | primária (ALECE: PL 134/2011 e PL 18/2015) |
| 4 | a janela 2010-2014 "também é posterior à primeira proposição" | `05-metodologia.tex:59-60` | Confere em parte | 2010 e os cinco primeiros meses de 2011 são anteriores a 31/05/2011. IL-MINOR-2 |
| 5 | a janela 2010-2014 "reduz o número de municípios sem a cultura" | `05-metodologia.tex:60` | Confere | primária: PAM/SIDRA, 15 municípios sem área em 2015-2018 e 6 em 2010-2014 (consulta da rodada 1) |
| 6 | "36 estabelecimentos, em 7 dos 184 municípios" | `02-contexto.tex:74-75` | Confere | primária (SIDRA 1008) |
| 7 | "a bananicultura está presente na maior parte do estado" | `02-contexto.tex:76`; `05-metodologia.tex:82-83` | Confere | primária: 169 de 184 municípios (média 2015-2018). Sem citação na frase |
| 8 | "a maioria dos municípios com a cultura não tinha registro de avião" | `02-contexto.tex:76-77` | Confere | primária: 162 de 169 |
| 9 | "o estimador centra o nível do efeito na variação desse grupo" | `05-metodologia.tex:83-84` | Confere | NBER WP 32117: o nível na dose d é a variação do desfecho nessa dose menos a variação na dose zero |
| 10 | "a lei estadual de 1993 autoriza os municípios a legislar supletivamente" | `06-dados.tex:52-53` | Confere | primária (cópia no repositório): art. 29 da Lei 12.228 |
| 11 | "há registro de uma, em Limoeiro do Norte, de 2009, dada como revogada em 2010" | `06-dados.tex:54-55` | Confere | secundária externa (G1; Estudos Sociedade e Agricultura). A redação já é cautelosa |
| 12 | Parágrafo "Escopo" | `06-dados.tex:59-66` | Sem afirmação factual verificável; são condições e compromissos. Ver C2 | -- |
| 13 | Quadro de fontes, coluna "Acesso" | `06-dados.tex:21-32` | Confere com o que se sabe das bases (públicas; pedidos de acesso; consulta processual) | -- |

### C2. Consistência interna (refeita por inteiro)

As três inconsistências da rodada 1 não existem mais. Datas, janelas e contagens batem entre os capítulos: dose principal 2015-2018 (`05:53`), sensibilidade 2010-2014 (`05:58`; `07:25`), painel de janeiro de 2015 a 19/12/2024 (`06:8`; `02:25`; `08:34`), marcos de 2011, 2015 e 2018 (`02:19-21`; `02:38-40`; `07:23`).

Resta uma, de outra natureza (IL-MEDIUM-1): o texto descreve no futuro, e como anteriores à estimação, etapas do estágio 1 que o repositório registra como já feitas.

| Trecho | O que diz | O que o repositório registra |
|---|---|---|
| `05-metodologia.tex:48-50` | a escolha da cultura "será confirmada, antes da estimação, por um diagnóstico da dispersão" | diagnóstico rodado em 25/08/2026 (`docs/gates-resultados-dados-reais.md` §4) |
| `05-metodologia.tex:206-208` | o efeito mínimo detectável "é calculado apenas com dados do pré-período, antes da estimação" | calculado em agosto de 2026 (mesmo documento, §5 e §6) |
| `05-metodologia.tex:215-217` | "O plano de análise de cada estágio será escrito e versionado antes da respectiva estimação" | plano do estágio 1 fechado em 21/09/2026; depois dele, estimação com esta mesma especificação: dose 2015-2018, banana, nível (`docs/pre-especificacao.md` §0 e §8; `docs/ars/17` §1) |
| `06-dados.tex:55-57` | o levantamento das leis municipais "integra o segundo estágio" | 17 municípios de dose alta já levantados (`docs/legislacao/README.md`) |
| `06-dados.tex:62-66` | a adequação das bases de água, vento e satélite "será avaliada" | avaliada em setembro de 2026 (`docs/lacunas-de-dados.md`) |

Isto decorre da decisão (b) do checkpoint ("Retirar tudo que soa a análise feita"). A decisão resolve a discordância entre a declaração e o rascunho, que é o que o checklist de modos de falha mede. Ela não torna verdadeiras as frases acima: com a dose de volta a 2015-2018, o estágio 1 do projeto é a especificação que já foi estimada. Na resposta de intake, o próprio pesquisador diz que rodou "um primeiro projeto utilizando o pipeline".

### C3. Figure/Table Caption Fidelity

Sem figuras; cinco quadros avulsos sem entrada de rastreio. Nota *trace-unavailable*, sem mudança.

### C4. Experiment Provenance & Claim Alignment

"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

D7: declaração presente (`no_experiments_declared`, `declared_by`, `declared_at`); sem `experiment_provenance[]`. A condição 4, acionada com ressalva na rodada 1, **não é mais acionada**: o texto não tem seção de Resultados nem frase que relate resultado de análise própria. As frases descritivas que restam (`02-contexto.tex:76`; `05-metodologia.tex:60`) são leituras de tabelas públicas e conferem com a fonte primária. Nenhuma das cinco condições de FAIL está presente. Nenhuma linha de `experiment_alignment_results[]`.

## Phase D: Originality Verification Results

Não refeita. A rodada 1 sondou 17 de 51 parágrafos, sem ocorrência. Os parágrafos reescritos nesta correção ("Janela da dose", "Grupo de comparação", "Exposição", "Escopo") são redação nova do próprio projeto e não foram sondados na web.

| Grade | Paragraph Count | Proportion |
|-------|----------------|-----------|
| ORIGINAL | -- | não refeita |
| COMMON_KNOWLEDGE | -- | -- |
| PARAPHRASE | -- | -- |
| CLOSE_MATCH | -- | -- |
| VERBATIM | -- | -- |

## Phase E: Claim Verification Results

**Claim Registry coverage sidecar (#737)**

O rascunho é multiarquivo. Há um registro e um relatório de cobertura por arquivo `.tex`, cada um vinculado aos bytes exatos do arquivo. Pasta: `docs/ars/pipeline-rodada20/evidence/`.

- Status: `completed` (8 de 8 relatórios construídos e validados por replay: "claim-registry coverage replay: PASS")
- Registry: `claim-registry/1.0`
- Candidate scope: citation-bearing + quantitative sentences only
- Candidate-unregistered count: 1
- Semantic extraction coverage: `not_machine_detectable`

| Arquivo | Afirmações | Candidatos | Não registrados | SHA-256 do rascunho | SHA-256 do registro (`claim_registry__<arquivo>.json`) | SHA-256 da cobertura (`coverage__<arquivo>.json`) |
|---|---|---|---|---|---|---|
| 01-introducao | 14 | 0 | 0 | b5ac6c2939e59739646032841dce024195c13a2f9fae270ac4e76720787ba473 | 9af7686d30b236fd93fc1757f50fa87defd54e6898c28bd0c8ef62e547abb85e | bf5d970c4202c02c80eff196b99152bbda1d025f72720ef2dd91664a4c8ab72d |
| 02-contexto | 14 | 0 | 0 | f7635ac7deb8b871fcc7effab1c5a0e19fbfaac376bbb6ba667ab0d5c393912e | 837a3233995dc98add9815153be28476a9fb9ade6e7b80aa4208aba818083dcf | 06059dbdebe0a0c17ae3b22d2ffba0979852a84b8499fc6980d4c1f7ad041591 |
| 03-referencial | 14 | 0 | 0 | 604b6b4b691699110fa38877e0b8946bc80624b453c01336c028a9d61bf0744c | 88897db9cee8ac3a9ae9cde5ece576c6b658f007fab39d6fd4d8f4a0d41e29ba | 76b3aafe4019891f3eb6f9a97d9cebc2b6bda8ab8402be8487bf4f5335fc6783 |
| 04-objetivos | 0 | 0 | 0 | c445f6ed5c7cbe1daf3917fddc207b895fdc59b01c9ba43cbf661329c0a99d3e | 5824a020aefa475b638a08c2cfc5b74bbbd8bdef6dc15a5d1d27c43bb29c8c80 | c173a81ae7052f48cd61fdc49e49d9d07d39732e6adad117bd50746c8653d54b |
| 05-metodologia | 9 | 1 | 1 | ec4d152335544b4b446711297845dd052f9824ea46355734210264feb240574f | ab69d26ac231dabedcb36c0dd13fc04eb2663a82cbfc9556cbbcb71bc7ee6c96 | 38b4a7a65d47c3214adb9b75b767ac0c44e960c4c2cbe6203974cc6ddd63ef9f |
| 06-dados | 3 | 0 | 0 | d6cb31c7483c419fce2bb8c452ea23e50a36e5856b8393b8f90c2e61ae11bbd7 | 0a0cd2e00fe70e288786b42ca3728fe605c93c08d5f3e6e9aa7df57b2a33d180 | c4aceb55ba02d31d2377a41136fa51e0311d37682a68e93382279d8d203509d0 |
| 07-ameacas | 0 | 0 | 0 | 38d35f22350537f3c75a47c45456757e956086556cfbdfedaab7f6b210c4b1b0 | 5e5cab6c742206e7858110b218aa2878249531c87cb52fc172539b0b2d16eac5 | aa04a2e7f05561274edf7380f9deefecf917f398c144360baa0a8c81cf440252 |
| 08-cronograma | 1 | 0 | 0 | 713491f0ea59b92acf8c3e677408f0506da8a9cc6489319954a2add61dbb76e3 | e8b7ab15a6147d0e33264b7a094d09e35fa300bf6ef33e0cab0ea66e1c1ce6b5 | 6064fdf45ba6e56abb13685d4f51bb5ecfb160eb2aff10b287750bf40b00a4f5 |

O único candidato não registrado (`05-metodologia.tex:136`, "Seja $P_t \in [0,1]$ a fração do primeiro") foi inspecionado: o detector leu o intervalo `[0,1]` como citação numérica. É definição de variável, não afirmação. Não há omissão a devolver ao E1.

**Limite do detector neste rascunho.** A gramática lexical do script reconhece citações em Markdown, autor-ano e Pandoc e unidades em inglês; não reconhece `\cite{}` do LaTeX nem unidades em português, e segmenta por linha. Por isso encontrou um candidato em oito arquivos. O status `completed` diz que a ferramenta rodou e foi validada, não que a extração esteja completa. A extração das 55 afirmações é semântica e feita por modelo.

`E1-COVERAGE-UNRESOLVED` da rodada 1: **fechado** nos termos do protocolo (relatórios persistidos, vinculados e validados por replay; candidato inspecionado).

| Verdict | Claim Count | Proportion |
|---------|------------|-----------|
| VERIFIED | 40 | 78% |
| MINOR_DISTORTION | 3 | 6% |
| MAJOR_DISTORTION | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| UNVERIFIABLE_ACCESS | 8 | 16% |

Mesmo critério da rodada 1: VERIFIED quando o resumo da versão citada contém a afirmação (a coluna de detalhe das linhas diz "só o resumo"); UNVERIFIABLE_ACCESS quando a afirmação não está no resumo e o texto completo da versão citada não pôde ser lido.

Mudanças de veredito em relação à rodada 1:

| Afirmação | Rodada 1 | Rodada 2 | Motivo |
|---|---|---|---|
| F14, F15 (169 e 15) | MAJOR_DISTORTION | retiradas do texto | dose principal de volta a 2015-2018 |
| F22 (plano) | MAJOR_DISTORTION | MINOR_DISTORTION | "registrado" saiu; resta a omissão (IL-MEDIUM-1) |
| F16 (banana "mais ampla") | MINOR_DISTORTION | retirada do texto | -- |
| C13 (Skevas), C20 (escalonados) | MINOR_DISTORTION | VERIFIED | redação corrigida |
| C23 (Denteh e Kédagni) | UNVERIFIABLE_ACCESS | VERIFIED | versão fixada na entrada |
| C24 (poucos grupos) | UNVERIFIABLE_ACCESS | VERIFIED | resumo de Cameron et al. obtido |
| G02 (projeto de lei de 2011, "julho") | -- | MINOR_DISTORTION | nova; mês errado |
| G06 (janela "posterior à primeira proposição") | -- | MINOR_DISTORTION | nova; só em parte |

UNVERIFIABLE_ACCESS que permanecem: C05, C06, C08, C16 e C18 (Calzada et al., texto publicado); C07 e C11 (Weitzman); C10 (Coase).

**Persisted Phase E evidence rows (#656)**

- Arquivo: `docs/ars/pipeline-rodada20/evidence/evidence_rows.json` (SHA-256 `1c80f3f10b26f814dd94a2472ebe54bce06e8a8ed18810179ed689b39b659c3f`), no formato `phases.E_claims` com `checked: 51`, `verified: 40` e `evidence_rows[]`.
- `phases.E_claims.evidence_source_dir`: `docs/ars/pipeline-rodada20/evidence/sources` (30 arquivos, um por fonte, com os nomes dados por `source_file_name(ref_slug)`).
- 66 linhas, construídas e validadas com `scripts/evidence_rows.py`: 37 `agent_extracted` (trecho de até 25 palavras, presente no texto-fonte guardado), 9 `access_failed`, 20 `anchorless` (afirmações factuais sem chave de bibliografia, conferidas em fonte primária ou secundária descrita no detalhe da linha).
- Validação por replay contra a pasta de fontes: `evidence_rows.py validate evidence_rows.json --source-dir sources` devolveu "PASS: 66 evidence row(s)".
- Renderização: `evidence_rows.py render evidence_rows.json --format markdown --source-dir sources --page N` (25 linhas por página, 3 páginas). A tabela não é reproduzida aqui.
- Proveniência de cada texto-fonte: `evidence/sources_manifest.json` (SHA-256 `e07fd544687b2e87b13bbf6334fca9956fd2c6db47e09431009cab251b2e2bb6`). Cinco fontes são parciais e estão marcadas assim: resumos de três APIs; só o título de Callaway e Sant'Anna (2021); uma alínea transcrita do Decreto 4.074; reprodução não oficial da IN MAPA 2/2008.
- A pasta `sources/` contém texto de terceiros (texto integral do NBER WP 32117, do arXiv 2207.11890v3 e do artigo de Reynier e Rubin; resumos). As linhas estão marcadas `session_only / not_assessed`: não avaliei direitos de redistribuição. Decidir antes de publicar o repositório.

**Scope-conformance advisory (#547)** — advisory-only, not counted in verdicts or the gate decision:

`[E4-SKIPPED: no scope context]`

| ID | Claim location | Effective scope | Drafted scope | Broadened axis |
|----|---------------|-----------------|---------------|----------------|
| -- | -- | -- | -- | -- |

**Novelty-claim classification (#548)** — advisory-only, not counted in verdicts or the gate decision. Nenhuma das quatro foi alterada pela correção.

| ID | Claim location | Claim wording | Classification | Nearest prior work / recommended bounded rewording |
|----|---------------|--------------|----------------|---------------------------------------------------|
| ADV-E5-1 | `01-introducao.tex:14-15` | "na primeira proibição estadual do gênero no Brasil" | UNRESOLVED | Citar a fonte, ou "apontada como a primeira" |
| ADV-E5-2 | `01-introducao.tex:23-24`; `:58-59` | "praticamente não há evidência causal no país"; "O que nenhum desses trabalhos oferece" | UNRESOLVED | "entre os trabalhos revisados" |
| ADV-E5-3 | `01-introducao.tex:88-89` | "registros administrativos nunca explorados para esse fim" | UNRESOLVED | "que não localizamos em uso para esse fim" |
| ADV-E5-4 | `08-cronograma.tex:9-10` | "a primeira medida municipal da aplicação aérea de agrotóxicos no Ceará antes da proibição" | UNRESOLVED; o projeto usa o Censo de 2006, que é medida municipal anterior | "a primeira medida municipal para 2015-2018" |

**Cache staleness advisory (#541)**: nenhuma linha servida de cache.

| ID | Citation key | Cache age (days) | Threshold | Re-verified live? |
|----|-------------|------------------|-----------|-------------------|
| -- | -- | -- | -- | -- |

**Claim-strength drift review (#569, revision rounds)**: `[E6-SKIPPED: no revision evidence]`. Não há Revision-Evidence Bundle nem artefato `claim-strength-drift-findings/1.0` da rodada anterior para vincular, e o rascunho não é ancorado por blocos. As mudanças de força que observei estão na tabela "Mudanças de veredito" acima; todas correspondem a itens da lista de correção da rodada 1.

**Token-conservation advisory (#570, revision rounds)**: não executado (`scripts/check_revision_token_conservation.py` não foi rodado pelo orquestrador nem por mim).

## Issue List (Sorted by Severity)

IDs novos, desta rodada. Não reutilize os da rodada 1.

### SERIOUS (Must Fix)

| ID | # | Category | Location | Issue Description | Correct Information | Source |
|----|---|----------|----------|------------------|--------------------|----|
| -- | -- | -- | -- | Nenhuma | -- | -- |

### MEDIUM (Must Fix)

| ID | # | Category | Location | Issue Description | Correct Information | Source |
|----|---|----------|----------|------------------|--------------------|----|
| IL-MEDIUM-1 | 1 | Internal consistency / disclosure | `paper/projeto/secoes/05-metodologia.tex:48-50`, `:206-208`, `:215-219`; `paper/projeto/secoes/06-dados.tex:55-57`, `:62-66` | O texto põe no futuro, e como anteriores à estimação, o diagnóstico de dose, o cálculo do efeito mínimo detectável, o plano de análise do estágio 1, o levantamento de leis municipais e a avaliação das bases de água, vento e satélite. O repositório registra todos como feitos entre agosto e setembro de 2026, e registra uma estimação com a mesma especificação que o estágio 1 agora descreve. É consequência da decisão (b) do checkpoint | Duas saídas. (1) Uma frase de divulgação, sem número: por exemplo, em `05-metodologia.tex:215`, "O plano de análise do primeiro estágio foi escrito e versionado em setembro de 2026; uma rodada exploratória com essa especificação já foi executada, não é reportada aqui e será refeita a partir das bases originais." Com isso os futuros dos outros trechos passam a ser lidos como "refazer". Custo: a contagem está em 15 páginas, sem folga. (2) O pesquisador mantém o texto e registra a decisão no checkpoint, ciente de que as frases descrevem como futuro o que já ocorreu | `docs/pre-especificacao.md` §0 e §8; `docs/gates-resultados-dados-reais.md` §4 a §6; `docs/ars/17` §1; `docs/lacunas-de-dados.md`; `docs/legislacao/README.md`; `passport.yaml` (`scholar_answer`) |
| IL-MEDIUM-2 | 2 | Reference | `paper/projeto/referencias-projeto.bib`, entrada `ibgepam` | `year = {2024}` não corresponde a nada: nem aos anos dos dados usados (2010 a 2018) nem à data da consulta. A entrada não identifica a tabela | Ano da consulta (2026) com data de acesso, e a tabela: o repositório registra extração em 25/08/2026 das tabelas SIDRA 1612 e 1613; a tabela 5457 traz a mesma variável. Exemplo de nota: "Tabelas 1612 e 1613. Disponível em: https://sidra.ibge.gov.br. Acesso em: 25 ago. 2026" | `docs/fontes-e-vintages.md`; API do SIDRA |

### MINOR (Recommended Fix at Stage 2.5; Must Fix at Stage 4.5)

| ID | # | Category | Location | Issue Description | Suggestion |
|----|---|----------|----------|------------------|----|
| IL-MINOR-1 | 1 | Data (G02) | `paper/projeto/secoes/02-contexto.tex:38` | O Quadro 1 data de julho de 2011 o projeto de lei estadual. O PL 134/2011 é de 31 de maio de 2011; e não tem "o mesmo objeto" apenas, pois também proíbe onze princípios ativos | "ação civil pública do Ministério Público (julho); projeto de lei estadual com a mesma vedação (PL nº 134, maio)". A fonte agora é primária: `www2.al.ce.gov.br/legislativo/tramit2011/pl134_11.htm`. Falta conferir o desfecho da tramitação |
| IL-MINOR-2 | 2 | Claim precision (G06) | `paper/projeto/secoes/05-metodologia.tex:59-60` | A janela 2010-2014 não é toda posterior à primeira proposição (31/05/2011) | "porque é, em sua maior parte, posterior à primeira proposição" |
| IL-MINOR-3 | 3 | Reference | `paper/projeto/referencias-projeto.bib`, `mapa2008in2` | Título sem dia e mês | "Instrução Normativa nº 2, de 3 de janeiro de 2008"; nota: "Diário Oficial da União, Brasília, 8 jan. 2008, Seção 1" |
| IL-MINOR-4 | 4 | Reference | `paper/projeto/referencias-projeto.bib`, `ibge2006censoagro` | `year = {2006}` é o ano de referência do censo; o ano de publicação não foi conferido | Conferir no catálogo do IBGE o ano de publicação dos resultados e acrescentar data de acesso à tabela 1008 |
| IL-MINOR-5 | 5 | Format / traceability | `01-introducao.tex:84`; `02-contexto.tex:19-20`, `:38`, `:42`, `:76`; `05-metodologia.tex:117-118` | Seguem sem referência: ADI 6137; o PL 134/2011; a frase sobre a presença da bananicultura (falta `\cite{ibgepam}`); a Lei 12.228 no item do cadastro (a entrada existe, falta o `\cite`) | Acrescentar duas entradas (ADI 6137; PL 134/2011) e os dois `\cite` |
| IL-MINOR-6 | 6 | Reference format | `paper/projeto/referencias-projeto.bib`, as 9 entradas novas | Sem endereço eletrônico e data de acesso; `ceara1993lei12228`, `ceara2024lei19135` e `cns2016res510` sem data de publicação oficial | Acrescentar "Disponível em" e "Acesso em"; datas de publicação: Lei 19.135, D.O. de 19/12/2024; Resolução 510, DOU de 24/05/2016; Lei 12.228, conferir o D.O. de 14/12/1993 |

## AI Research Failure Mode Checklist

Declaração no passport: `no_experiments_declared`, com a resposta do pesquisador: "É, Considere que eu rodei um primeiro projeto utilizando o pipeline, mas ainda o projeto eu considero que não, nenhuma estimativa ainda precisa ser consolidada. É um projeto para que eu vá realizar isso, certo? Então, o que eu fiz foi só apenas pegar os dados e tudo mais. [segunda resposta] Vamos começar do zero [...] vamos considerar que a gente vai rodar tudo do zero."

Na rodada 1 a regra NOT APPLICABLE não pôde ser aplicada porque o rascunho apresentava análises como feitas pelo autor. O texto atual não as apresenta mais, e a referência prevê esse caminho de resolução. A regra se aplica.

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | NOT APPLICABLE | Declaração acima; o rascunho não apresenta mais análise própria. Os números que ficaram (184; 36 em 7; contagens da tabela do PL) foram refeitos de fonte primária e conferem | no |
| 2. Hallucinated citation | CLEAR | 37 de 37 referências existem; as cinco correções da rodada 1 conferem; nas 9 novas, um ano sem base (`ibgepam`) e uma data incompleta (`mapa2008in2`), que são erros de campo, não de existência | no |
| 3. Hallucinated experimental result | NOT APPLICABLE | Declaração acima. Rodada 1: SUSPECTED; o pesquisador confirmou o apontamento e pediu a revisão. Não há mais resultado próprio no texto | no |
| 4. Shortcut reliance | CLEAR (flag-only neste estágio) | Sem mudança: o texto trata a medida pela cultura como ameaça central | no |
| 5. Implementation bug reframed as novel insight | NOT APPLICABLE | Declaração acima. Não há linguagem de surpresa | no |
| 6. Methodology fabrication | NOT APPLICABLE | Declaração acima. Rodada 1: SUSPECTED; confirmado e revisado. O que resta é o tempo verbal de etapas já feitas, tratado fora do checklist, em IL-MEDIUM-1 | no |
| 7. Frame-lock at early pipeline stage | CLEAR | A janela da dose foi revista neste checkpoint, com registro em `docs/ars/20` §4; o desenho em estágios tem regra de decisão que permite recuar; o estágio 3 passou a ter o segundo trimestre como sensibilidade. Pendente só a leitura do texto publicado de Calzada et al. | no |

**Resultado do checklist:** nenhum modo bloqueia.

Registro de honestidade, fora do checklist: a regra NOT APPLICABLE compara a declaração com o rascunho, e os dois agora concordam. Ela não compara nenhum dos dois com o repositório, que registra as rodadas de agosto e setembro de 2026. Essa diferença está em IL-MEDIUM-1 e é o pesquisador quem decide.

## Tool Limitation Disclaimer

> This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 33% (rodada 1; não refeita nesta rodada), and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.

Limitações específicas desta rodada:

1. **Não lidos.** Texto publicado de Calzada et al. (JAERE); Weitzman (1974) e Coase (1960), só metadados; Brainerd e Menon não pôde ser baixado de novo (conferido na rodada 1 por trechos da busca).
2. **Fontes primárias não acessadas.** Dossiê ABRASCO; texto das leis municipais 1.478 e 1.511; autos da ação civil pública de 2011; desfecho da tramitação do PL 134/2011; Diário Oficial do Estado; ementa do Decreto 4.074 no original; catálogo do IBGE (ano de publicação do Censo Agropecuário 2006).
3. **Acesso por `curl` recusado nesta rodada:** `gov.br/agricultura` (PDF da IN), `planalto.gov.br`, `bvsms.saude.gov.br`, `people.brandeis.edu`, `diposit.ub.edu`, `biblioteca.ibge.gov.br`. Por isso a fonte guardada da IN é uma reprodução e a do decreto é uma alínea transcrita.
4. **Fase D e D2** não refeitas; parágrafos reescritos não sondados.
5. **28 referências antigas** não reverificadas do zero (só os campos corrigidos). As 27 entradas não citadas seguem sem verificação.
6. **Detector de cobertura** quase cego a LaTeX e a português (ver Fase E).
7. **PDF** não recompilado por mim; contagem de páginas feita no PDF existente.
8. **Verificação cruzada entre modelos** não habilitada; modelo verificador da mesma família do que escreveu e corrigiu o rascunho.
9. **`content_hash` do passport** não conferido.

## Verification Audit Trail

Rodada 2, 2026-11-15, concluída às 22:01Z.

**Diferença examinada.** `git diff 048d9fc~1 048d9fc -- paper/ docs/`; leitura integral das oito seções no estado atual.

**Fase A (9 entradas novas).**
- Lei 16.820, Lei 12.228, PL 18/2015: `docs/legislacao/*.md` (cabeçalhos e artigos).
- Lei 19.135: `GET https://www2.al.ce.gov.br/legislativo/legislacao5/leis2024/19135.htm`, HTTP 200; cabeçalho "LEI N.° 19.135, DE 19.12.24 (D.O. 19.12.24)".
- IN MAPA 2/2008: `GET https://www.normasbrasil.com.br/norma/instrucao-normativa-2-2008_76999.html`, HTTP 200 ("Instrução Normativa MAPA nº 2 de 03/01/2008 [...] Publicado no DO em 08 jan 2008"); PDF oficial lido na rodada 1.
- Resolução CNS 510: PDF em `gov.br/conselho-nacional-de-saude/.../resolucao-no-510-de-07-de-abril-de-2016`, HTTP 200, convertido com `pdftotext`.
- Decreto 4.074: sem acesso direto nesta rodada (Planalto e Câmara recusaram); título e art. 66 da rodada 1. Data da Lei 7.802 ("de 11/07/89") lida no texto do PL 134/2011.
- Censo Agropecuário e PAM: API do SIDRA (rodada 1); `docs/fontes-e-vintages.md` linha 9 (tabelas 1612 e 1613, extração em 2026-08-25).
- Campos corrigidos: Böcker, RePEc `RePEc:oup:erevae:v:47:y:2020:i:2:p:371-402` (rodada 1); Weitzman, `GET https://ideas.repec.org/a/oup/restud/v41y1974i4p477-491..html`, HTTP 200, "477-491"; Larsen e Reynier, OpenAlex (`first_page` 302 e e2413013121).

**Fase C (afirmações novas).**
- PL 134/2011: `GET https://www2.al.ce.gov.br/legislativo/tramit2011/pl134_11.htm`, HTTP 200. Lido: ementa; arts. 1º a 4º; "Sala das Sessões da Assembleia Legislativa do Estado do Ceará, em 31 de maio de 2011. Deputado HEITOR FÉRRER". O cabeçalho da página traz "EMENDA MODIFICATIVA / PROJETO DE LEI Nº 134/2011"; não conferi se é o texto original ou uma versão emendada.
- Art. 29 da Lei 12.228: `docs/legislacao/lei-12228-1993-consolidada.md`, linha 167.
- Contagens de banana e de aeronaves: consultas ao SIDRA da rodada 1 (tabelas 5457 e 1008).
- Expressão de identificação do nível: `pdftotext` do PDF `https://www.nber.org/system/files/working_papers/w32117/w32117.pdf`.
- Páginas: `pdfinfo` (21 páginas); `projeto.toc` (capítulo 1 na página 3; referências na 18); `pdftotext` página a página.
- Citações: 37 chaves distintas nos `.tex`; 37 `\bibitem` em `projeto.bbl`; `projeto.log` sem referência indefinida.

**Fase E (artefatos).**
- Fontes baixadas e guardadas: arXiv `2207.11890v3` (PDF, `pdftotext -layout`); NBER w32117 (PDF, `pdftotext`); Europe PMC `PMC11761964/fullTextXML`; resumos do Semantic Scholar e do Crossref (respostas da rodada 1); resumos do OpenAlex (`api.openalex.org/works/doi:<doi>`, índice invertido reconstruído) para Buckles e Hungerman, Conley e Taber e Cameron et al.; textos legais como na Fase A; JSON do SIDRA (tabela 1008).
- Construção: registro por arquivo com spans de bytes calculados por marcadores de início e fim; `scripts/claim_registry_coverage.py --draft --registry --output`, seguido de `--validate-report` (8 de 8 PASS); linhas com `evidence_rows.build(...)` e validação `evidence_rows.py validate evidence_rows.json --source-dir sources` (PASS, 66 linhas).
- Conferências exigidas pelo protocolo: 51 `claim_id` distintos nas linhas, igual a `checked`; 40 com veredito VERIFIED, igual a `verified`; linhas da mesma afirmação com o mesmo veredito; nenhuma linha para as 4 NOT-SELECTED.
