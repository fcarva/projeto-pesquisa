# Academic Integrity Verification Report

*ARS v3.24.2 · `integrity_verification_agent` · Estágio 2.5 · **projeto_v2, rodada 2** (reverificação da rodada 1 de correções) · concluída em 2026-11-15T22:59Z (UTC).
Manuscrito no commit `0d44888` (`git diff HEAD~1 HEAD -- paper/`): alterados `02-contexto`, `03-referencial`, `04-objetivos`, `05-metodologia`, `07-ameacas` e `referencias-projeto.bib`. PDF `paper/projeto/projeto.pdf`: 21 páginas, 15 textuais.
Relatório anterior desta versão: `stage2.5_integrity_report_v2_round1.md`, não alterado. Este agente não editou o manuscrito nem os `.bib`. Arquivos gravados: este relatório e a atualização de `evidence/`.*

## Verification Mode

Initial Verification (Mode 1, pre-review), reverificação dos itens corrigidos. Não refeito: o que não mudou desde a rodada 1 da v2.

## Verdict

**PASS WITH NOTES**

Zero SERIOUS, zero MEDIUM, zero MAJOR_DISTORTION, zero UNVERIFIABLE. Restam 3 MINOR e notas. As duas issues que davam FAIL foram resolvidas no texto. Nenhum modo de falha bloqueia.

Duas ressalvas que acompanham o PASS: o que o projeto diz de Calzada et al. confere com o manuscrito de março de 2023, e a versão publicada continua sem ser lida (9 afirmações em UNVERIFIABLE_ACCESS, 6 delas por isso); e no Estágio 4.5 as issues MINOR também bloqueiam.

## Verification Summary

| Category | Total | Passed | Issues |
|----------|-------|--------|--------|
| Reference Existence | 45 (44 da rodada 1 + `globorural2021bananais`) | 45 | 0 |
| Bibliographic Accuracy | 45 | 45 nos campos presentes | 2 MINOR de completude |
| Ghost Citations | -- | -- | 0 órfãs na lista impressa / 0 pendentes (45 chaves, 45 itens no `projeto.bbl`, nenhuma referência indefinida) |
| Citation Context Accuracy | 9 contextos novos ou alterados | 8 | 1 MINOR (`skevas2012`) |
| Statistical Data Accuracy | 2 afirmações corrigidas (150 metros; Censo de 2006 fora dos polos) | 2 | 0 |
| Internal Consistency | -- | Pass | 0 |
| Originality Check (D1) | não refeita (rodada 1 da v2: 9 de 27 parágrafos novos, 33%) | -- | -- |
| Self-Plagiarism (D2) | não refeita | -- | -- |
| Claim Verification (E) | 62 de 66 registradas (Mode 1: HIGH-IMPACT: 48, RANDOM: 0, TOP-UP: 14; NOT-SELECTED: 4, só no E5; semantic extraction coverage: not_machine_detectable; candidate gaps: 1, falso positivo já inspecionado) | 52 | 0 MAJOR_DISTORTION / 0 UNVERIFIABLE (1 MINOR_DISTORTION; 9 UNVERIFIABLE_ACCESS) |

Restrições do autor:

| Restrição | Resultado |
|---|---|
| Nenhum número de estimativa | Nenhum. As correções só trocaram "poucas centenas de metros" por "150 metros", que é da literatura. |
| No máximo 15 páginas textuais | 15 (numeração impressa 3 a 17; referências a partir da 18). No limite. |
| Só o Ensaio 1 | Sem mudança. |

O PDF é posterior aos fontes (22:57:43 contra 22:57:40) e contém o texto corrigido. Não o recompilei.

## Status das issues da rodada 1 da v2

| ID (rodada 1 da v2) | Status | Onde está agora | Observação |
|---|---|---|---|
| IL-SERIOUS-1 (banana familiar "não tem o avião") | **Resolvida** | `05-metodologia.tex:108-114`; `04-objetivos.tex:16-18` | Passou a hipótese ("por hipótese, não têm o avião"), com verificação declarada nos relatórios do MAPA e no Censo de 2006 e regra de exclusão: "município com qualquer registro de aeronave é excluído do grupo de comparação". A frase "que registra aplicação aérea também fora dos polos irrigados" confere com a tabela SIDRA 1008 |
| IL-MEDIUM-1 (terceiro trimestre) | **Resolvida** | `03-referencial.tex:49-50`; `05-metodologia.tex:104-106`; `04-objetivos.tex:29-32`; `07-ameacas.tex:26` | "Estimativa sem significância estatística no terceiro" e "contraste de efeito menor" conferem com o manuscrito de março de 2023. O terceiro trimestre saiu das respostas de falsificação do Quadro 4 e a hipótese correspondente passou de "ausente" a "menor" |
| IL-MINOR-1 (relato da seca) | **Resolvida** | `02-contexto.tex:88-91` | O relato é atribuído a "uma moradora de comunidade da Chapada", com a pouca chuva como causa, como na fonte; a umidade aparece como raciocínio do projeto ("o que é coerente com") |
| IL-MINOR-2 (declarações do setor) | **Resolvida** | `02-contexto.tex:91-93` | "Um produtor do Cariri [...] declarou ter feito aplicações aéreas em seu bananal até 2018", com citação. A reportagem traz a declaração: "até 2018, fazia duas aplicações aéreas anuais no seu bananal". Saíram a Chapada e "em anos chuvosos" |
| IL-MINOR-3 (Skevas e "dimensão distributiva") | **Parcialmente resolvida** | `03-referencial.tex:16-19` | Skevas et al. saiu da frase distributiva, mas foi parar junto de Weitzman, numa frase sobre inclinações relativas de benefício e custo marginais, de que também não trata. IL-MINOR-1 desta rodada |
| IL-MINOR-4 (heterocedasticidade) | **Resolvida** | `05-metodologia.tex:240-241` | "este último com heterocedasticidade por tamanho de município" |
| IL-MINOR-5 ("poucas centenas de metros") | **Resolvida** | `07-ameacas.tex:58-59` | "a até 150 metros do bananal", igual a `03-referencial.tex:32` |
| IL-MINOR-6 (ordem do Quadro 1) | **Resolvida** | `02-contexto.tex:39-42` | 2012-2017, 24/02/2015, 03/2018, 18/12/2018, em ordem |
| IL-MINOR-7 (três entradas novas) | **Parcialmente resolvida** | `referencias-projeto.bib` | `ceara2018nascer` agora tem o hospital como autor. `agenciabrasil2016ceara` segue sem a repórter. `ibge2017censoagro` ficou sem número de tabela: deixou de apontar tabelas que não serviam, mas também não aponta as que servem. IL-MINOR-2 desta rodada |
| IL-MINOR-8 (completude das entradas normativas; vem da v1) | **Não resolvida** | `referencias-projeto.bib` | IL-MINOR-3 desta rodada |
| IL-MINOR-9 (troca de desenho depois da rodada exploratória) | **Resolvida** | `05-metodologia.tex:259-261` | "o desenho de calendário foi adotado como principal depois dela, sem que a exposição sazonal tenha sido cruzada com os desfechos". As duas metades conferem com o repositório (abaixo). A frase "Antes de qualquer contato com os desfechos do pós-lei" (`:133`) continua igual, mas agora o mesmo capítulo diz o que já foi feito |

## Phase A: Reference Verification Results

Entrada nova:

| Chave | Existência | Campo a campo | Fonte |
|---|---|---|---|
| globorural2021bananais | VERIFIED | Título confere com o da página ("Pulverização aérea de bananais no CE é alvo de ação no STF"). Data confere: a página traz "09 Abr 2021". O endereço responde (HTTP 200). A entrada não traz autoria da reportagem nem data de acesso | Página da Globo Rural, baixada na rodada 1 da v2 |

Entradas alteradas: `ceara2018nascer` (autor "Hospital Geral Dr. César Cals") confere com o sítio; `ibge2017censoagro` sem tabelas, sem campo errado.

## Phase B: Citation Context Verification Results

| Chave | Local | O que o texto atribui | Resultado |
|---|---|---|---|
| agenciabrasil2016ceara | `02-contexto.tex:88-90` | moradora relata, em 2016, que não havia aplicações desde 2012, pela pouca chuva | Confere |
| globorural2021bananais | `02-contexto.tex:91-93` | produtor do Cariri declara aplicações aéreas até 2018 | Confere |
| weitzman1974, skevas2012 | `03-referencial.tex:16-18` | a escolha do instrumento "depende das inclinações relativas do benefício e do custo marginais" | Weitzman: texto não lido (nota). Skevas et al. não trata disso. IL-MINOR-1 |
| lichtenberg1988, helfand1995 | `03-referencial.tex:18-19` | dimensão distributiva | Confere |
| calzada2023bananas | `03-referencial.tex:49-50`; `05-metodologia.tex:104-106` | terceiro trimestre sem significância estatística | Confere no manuscrito |
| calzada2023bananas (implícita) | `07-ameacas.tex:58-59` | efeito a até 150 metros | Confere no manuscrito |
| conley2011, ferman2019inference | `05-metodologia.tex:240-241` | heterocedasticidade só em Ferman e Pinto | Confere |
| ibge2017censoagro | `05-metodologia.tex:108-110` | classificação pela agricultura familiar | Confere (a fonte tem a tipologia) |
| (sem chave) | `05-metodologia.tex:112-113` | o Censo de 2006 registra aplicação aérea fora dos polos irrigados | Confere em fonte primária |

## Phase C: Data Verification Results

**C1.** "A até 150 metros" confere com o manuscrito de março de 2023. "O Censo de 2006 [...] registra aplicação aérea também fora dos polos irrigados" confere com a tabela SIDRA 1008: Aiuaba 5, Jaguaruana 1, Mauriti 1, Quiterianópolis 1, Quixeramobim 1, além de Limoeiro do Norte 18 e Quixeré 9.

**C2.** As três inconsistências da rodada 1 da v2 foram desfeitas (distância; ordem do Quadro 1; troca de desenho). Reli as passagens que dependem das correções: hipóteses H3 e H4 (`04-objetivos.tex:28-32`), contraste do terceiro trimestre (`05-metodologia.tex:104-106`) e Quadro 4 (`07-ameacas.tex:24-26`) estão coerentes entre si. Nenhuma inconsistência nova.

A frase nova sobre a troca de desenho, contra o repositório:

| Trecho | Evidência |
|---|---|
| "o desenho de calendário foi adotado como principal depois dela" | Documento de 10/11, §7, item 1 ("Vocês trocaram de desenho depois de ver um resultado ruim. Verdade."); `docs/ars/20` registra a decisão |
| "sem que a exposição sazonal tenha sido cruzada com os desfechos" | `docs/ars/19`, linhas 29 a 33: o cálculo de poder do calendário rodou "em dado sintético"; documento de 10/11, §5.2: `14_mde_calendario.py` "nunca rodou com dado real" |

Conferência contra documentos do repositório, não contra logs.

**C3.** Sem mudança: Figura 1 e cinco quadros sem entrada de rastreio (nota *trace-unavailable*).

**C4.** "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS." D7 sem mudança: declaração presente, sem `experiment_provenance[]`; condição 4 limítrofe e, pela letra, não acionada.

## Phase D: Originality Verification Results

Não refeita. As correções alteraram frases, não parágrafos inteiros.

| Grade | Paragraph Count | Proportion |
|-------|----------------|-----------|
| ORIGINAL | -- | não refeita |
| COMMON_KNOWLEDGE | -- | -- |
| PARAPHRASE | -- | -- |
| CLOSE_MATCH | -- | -- |
| VERBATIM | -- | -- |

## Phase E: Claim Verification Results

**Claim Registry coverage sidecar (#737)**

Mudaram os bytes de 02, 03, 04, 05 e 07. Só os registros e relatórios desses cinco foram alterados; os de 01, 06 e 08 têm os mesmos SHA-256 da rodada 1 da v2 (conferido antes e depois).

- Status: `completed` (replay PASS nos cinco refeitos)
- Registry: `claim-registry/1.0`
- Candidate scope: citation-bearing + quantitative sentences only
- Candidate-unregistered count: 1 (o mesmo falso positivo, `05-metodologia.tex:87`)
- Semantic extraction coverage: `not_machine_detectable`

| Arquivo | Afirmações | Não registrados | SHA-256 do rascunho | SHA-256 do registro | SHA-256 da cobertura |
|---|---|---|---|---|---|
| 02-contexto | 19 | 0 | 7609ce97e8a77a08d4ad3357ebd38e832eff21aa6b94274ca1e10125780078fc | 24a392f98bd23e976aef83c5e6a4330d8f4231e59d18ee1417e60044265ce396 | c4636ef4fa2368ea2451e67e05ec790c43f32f7bd22fa693471a3dcf09d25058 |
| 03-referencial | 14 | 0 | 34b66ace3aab3daaf80198dc09930cb0a18031594bf45f588ef8937c66bd15ca | e33e58ec8ea20c0666ed6d85bca05a9fc48b4a284858c401f5975b05dbefb61d | 53a0a8567a8de4fa0327f011ba06568101aee9ae9449f2e43a29796cdec14cf5 |
| 04-objetivos | 0 | 0 | 78f0bbb6a14d66f7bdb259670ae398bc0f3d33cc04523b9b15faf52af570c41b | cb53668db20c4f378d9c8e28a153e2a3fcc21a9d5b5430e0c7907df8c7587875 | 9940ca12cdcc5b2f722428ab3ca91011e7594a26df95c60d449075c5dba526a7 |
| 05-metodologia | 13 | 1 | 8472c7b10c9d8361499b6b95b522cdbdd8d4dd2d933f09d2ce55ec7cb6a332c2 | b24c6b3a795b3ff026b8e42adcae5dec9e138152aeb85de19513ec380d720a17 | c0c4ab44c30a9a285069fb7d488db20be01ff3067ffede707181bd9b3dc7a9ca |
| 07-ameacas | 1 | 0 | 4cbdb68425f18fe1a01bcf365d9401d24888bd526a9e933a0a0f3c53b385a168 | 30e794cdea7fc3176e40bf73944ea0b088403d070ee5b6ea15b7dfddedf790c7 | d9e4c255d604e25b0527b9d7813e70e8484d050d3d2593e568601af431b54498 |
| 01, 06, 08 | 14, 4, 1 | 0 | inalterados | inalterados (ver relatório da rodada 1 da v2) | inalterados |

| Verdict | Claim Count | Proportion |
|---------|------------|-----------|
| VERIFIED | 52 | 84% |
| MINOR_DISTORTION | 1 | 2% |
| MAJOR_DISTORTION | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| UNVERIFIABLE_ACCESS | 9 | 15% |

Mudanças em relação à rodada 1 da v2:

| Afirmação | Rodada 1 | Rodada 2 | Motivo |
|---|---|---|---|
| H07 (avião na banana familiar) | UNVERIFIABLE | VERIFIED | A afirmação virou hipótese; o fato que resta no texto (Censo de 2006 fora dos polos) confere |
| H03 (relato da seca), H04 (produtor do Cariri), C12 (dimensão distributiva), H10 (heterocedasticidade) | MINOR_DISTORTION | VERIFIED | redação corrigida |
| H14 (150 metros) | MINOR_DISTORTION | UNVERIFIABLE_ACCESS | o número agora confere com o manuscrito; a versão publicada não foi lida |
| C11 (Weitzman, agora com Skevas) | UNVERIFIABLE_ACCESS | MINOR_DISTORTION | Skevas et al. não sustenta a frase |
| F23 (troca de desenho depois da rodada exploratória) | -- | VERIFIED | nova; fonte interna |

UNVERIFIABLE_ACCESS, nove: C06, C08, C15, C18, H08 e H14 (Calzada et al.: conferem no manuscrito de março de 2023; versão publicada não lida; em C06, "mesma classe de produto", o manuscrito lista um inseticida ao lado de dois grupos de fungicidas); C07 (Weitzman) e C10 (Coase), texto não lido; H12 (Canay et al. na diferença tripla), o resumo não basta.

**Persisted Phase E evidence rows (#656)**

- `docs/ars/pipeline-rodada20/evidence/evidence_rows.json`, refeito (SHA-256 `eaa45eb9f3b04f3f841496e6b0f412e1567dd1614d5324ad2d493ca5b5974d0a`), com `checked: 62` e `verified: 52`.
- 77 linhas: 56 `agent_extracted`, 5 `access_failed`, 16 `anchorless`. `evidence_rows.py validate evidence_rows.json --source-dir sources`: "PASS: 77 evidence row(s)".
- `phases.E_claims.evidence_source_dir`: `docs/ars/pipeline-rodada20/evidence/sources`, com 39 arquivos. Entrou `globorural2021bananais.txt`; saiu `ibge2017censoagro.txt`, que eu havia gravado e que nenhuma linha referencia mais.
- `sources_manifest.json` atualizado (SHA-256 `ef49a2663bb133ea39a583a430867dc7118e5218a74eeec8cfc3bfb318b2e41b`). Continuam valendo os avisos da rodada 1: a fonte de `calzada2023bananas` é o manuscrito de março de 2023; a de `limoeiro2010lei1511` é transcrição parcial minha; a pasta contém texto integral de terceiros, com direitos de redistribuição não avaliados.

**Scope-conformance advisory (#547)**: `[E4-SKIPPED: no scope context]`

| ID | Claim location | Effective scope | Drafted scope | Broadened axis |
|----|---------------|-----------------|---------------|----------------|
| -- | -- | -- | -- | -- |

**Novelty-claim classification (#548)** — advisory-only. As cinco linhas da rodada 1 da v2 seguem abertas e inalteradas (ADV-E5-1 a ADV-E5-5: `01-introducao.tex:14-15`; `:23-24` e `:58-59`; `:86-87`; `08-cronograma.tex:9-11`; `03-referencial.tex:41-42`), todas UNRESOLVED.

| ID | Claim location | Claim wording | Classification | Nearest prior work / recommended bounded rewording |
|----|---------------|--------------|----------------|---------------------------------------------------|
| ADV-E5-1 a 5 | ver relatório da rodada 1 da v2 | inalteradas | UNRESOLVED | inalteradas |

**Cache staleness advisory (#541)**: nenhuma linha servida de cache.

**Claim-strength drift review (#569)**: `[E6-SKIPPED: no revision evidence]`. Sem bundle de revisão. As mudanças de força desta rodada estão na tabela acima: todas enfraquecem afirmações (de fato para hipótese; de "nenhum efeito" para "sem significância") e todas correspondem a itens da lista de correção.

**Token-conservation advisory (#570)**: não executado.

## Issue List (Sorted by Severity)

IDs novos, deste relatório.

### SERIOUS (Must Fix)

| ID | # | Category | Location | Issue Description | Correct Information | Source |
|----|---|----------|----------|------------------|--------------------|----|
| -- | -- | -- | -- | Nenhuma | -- | -- |

### MEDIUM (Must Fix)

| ID | # | Category | Location | Issue Description | Correct Information | Source |
|----|---|----------|----------|------------------|--------------------|----|
| -- | -- | -- | -- | Nenhuma | -- | -- |

### MINOR (Recommended Fix at Stage 2.5; Must Fix at Stage 4.5)

| ID | # | Category | Location | Issue Description | Suggestion |
|----|---|----------|----------|------------------|----|
| IL-MINOR-1 | 1 | Citation context (C11) | `paper/projeto/secoes/03-referencial.tex:16-18` | `skevas2012` foi posto ao lado de `weitzman1974` na frase "depende das inclinações relativas do benefício e do custo marginais". Skevas et al. é uma comparação de instrumentos por simulação e não trata disso | Deixar só Weitzman nessa frase e dar a Skevas uma oração própria, como na v1: "e há comparação, por simulação, entre cotas e taxas \cite{skevas2012}". Se a página não comportar, retirar a citação |
| IL-MINOR-2 | 2 | Reference | `paper/projeto/referencias-projeto.bib`: `ibge2017censoagro`, `agenciabrasil2016ceara`, `globorural2021bananais` | `ibge2017censoagro` não identifica tabela; as que cruzam produtos da lavoura permanente com tipologia são a 6955 e a 6956. `agenciabrasil2016ceara` sem a autoria da reportagem (Edwirges Nogueira). As três sem data de acesso | Acrescentar "tabelas 6955 e 6956" (e conferir, ao baixar os dados, que servem à classificação pretendida); autoria na notícia; "Acesso em" nas três |
| IL-MINOR-3 | 3 | Reference format (vem da v1) | `paper/projeto/referencias-projeto.bib` | Dez entradas normativas e estatísticas sem endereço eletrônico e data de acesso; três sem data de publicação oficial; ano de publicação do Censo Agropecuário 2006 não conferido | Como nos relatórios das rodadas 3 e 4 da v1 |

## AI Research Failure Mode Checklist

Declaração no passport: `no_experiments_declared`. Override dos Modos 1, 3 e 6 registrado na rodada 4 da v1, com as palavras do pesquisador: "como é um projeto de pesquisa essa parte vai ser feita ao longo do ano, então é só o que eu vou fazer". As correções desta rodada não acrescentaram análise própria ao texto; a frase nova (`05-metodologia.tex:259-261`) diz quando o desenho foi escolhido e o que não foi feito.

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | INSUFFICIENT EVIDENCE, coberto pelo override registrado | Sem mudança desde a rodada 1 da v2 | no |
| 2. Hallucinated citation | CLEAR | 45 de 45 referências existem; a entrada nova confere em título, data e conteúdo | no |
| 3. Hallucinated experimental result | SUSPECTED pela regra, coberto pelo override registrado | Sem mudança; nenhum resultado próprio no texto | no |
| 4. Shortcut reliance | CLEAR (flag-only neste estágio) | Sem mudança | no |
| 5. Implementation bug reframed as novel insight | CLEAR | Sem mudança | no |
| 6. Methodology fabrication | SUSPECTED pela regra, coberto pelo override registrado | Sem mudança no enquadramento. No mérito, a frase nova sobre a troca de desenho confere com o repositório | no |
| 7. Frame-lock at early pipeline stage | CLEAR | Na rodada 1 da v2 ficou INSUFFICIENT EVIDENCE por três premissas não confirmadas. Duas deixaram de ser premissas: a ausência de avião na banana familiar virou hipótese com verificação e regra de exclusão; o terceiro trimestre deixou de ser falsificação. A terceira, a existência de estação de pulverização no bananal irrigado, já era tratada como hipótese, com verificação antes da estimação e saída prevista na regra de decisão (`05-metodologia.tex:210-229`; `07-ameacas.tex:67-71`). O texto agora também diz que o desenho foi trocado depois da rodada exploratória | no |

**Resultado do checklist:** nenhum bloqueio. O override dos Modos 1, 3 e 6 segue em vigor e deve ser reavaliado no Estágio 4.5 e relatado no Estágio 6.

Fica para os pareceristas do Estágio 3, não como pendência de integridade: o documento de 10/11 desaconselha a agricultura familiar como controle direto (§6), e o projeto a usa como grupo de comparação dentro da diferença tripla, com justificativa.

## Tool Limitation Disclaimer

> This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 33% dos parágrafos novos da v2 (rodada 1; não refeita nesta rodada), and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.

Continuam valendo as limitações da rodada 1 da v2. Em resumo:

1. O artigo publicado de Calzada et al. e seu apêndice online não foram lidos; o que o projeto diz dele foi conferido no manuscrito de março de 2023.
2. Weitzman (1974) e Coase (1960) não lidos; de Canay et al., Hagemann, Jones e MacKinnon e Webb, só o resumo.
3. Lei 1.511/2010: só as páginas 1, 65 e 66; alterações posteriores não verificadas.
4. Censo de 2017: não baixei dados municipais; não sei quais municípios caem no grupo de comparação nem quantos sobram depois da regra de exclusão.
5. A frase sobre a troca de desenho foi conferida contra documentos do repositório, não contra logs.
6. Nenhuma consulta nova à web nesta rodada; usei o que foi baixado na rodada 1 da v2.
7. Fases D e D2 não refeitas; 29 entradas não citadas dos `.bib` sem verificação; E4 e E6 pulados; sem verificação cruzada entre modelos; PDF não recompilado; `content_hash_v2` não conferido.

## Verification Audit Trail

Projeto_v2, rodada 2, 2026-11-15, concluída às 22:59Z.

- Diferença examinada: `git diff HEAD~1 HEAD -- paper/` em `0d44888` (cinco `.tex`; três entradas de `.bib`, uma nova).
- `globorural2021bananais`: página baixada na rodada 1 da v2 (`globorural.globo.com/.../pulverizacao-aerea-de-bananais-no-ce-e-alvo-de-acao-no-stf.html`, HTTP 200); título no elemento `title`; "09 Abr 2021" e carimbos de 2021-04-09 no HTML; trecho "Regis conta que, até 2018, fazia duas aplicações aéreas anuais no seu bananal".
- Relato da moradora: página da Agência Brasil baixada na rodada 1 da v2 ("A partir de 2012, segundo a agricultura, não houve novas aplicações devido à baixa intensidade das chuvas nas últimas quadras invernosas").
- Terceiro trimestre e 150 metros: manuscrito de março de 2023 de Calzada et al., seção 5 e introdução (rodada 1 da v2).
- Censo de 2006 fora dos polos: resposta do SIDRA para a tabela 1008 (v1).
- Troca de desenho: `docs/ars/19-medida-e-desenho-fase2-investigacao.md`, linhas 29 a 33; documento de 10/11, §5.2 e §7.
- Páginas e citações: `pdfinfo` (21); `projeto.toc` (capítulo 1 na página 3; capítulo 8 na 17; referências na 18); 45 chaves; 45 `\bibitem`; log sem "undefined".
- Artefatos: SHA-256 dos registros e coberturas de 01, 06 e 08 comparados antes e depois (idênticos); `claim_registry_coverage.py --validate-report` nos cinco refeitos (PASS); `evidence_rows.py validate --source-dir sources` (PASS, 77 linhas); 62 `claim_id` distintos, igual a `checked`; 52 VERIFIED, igual a `verified`.
