# Academic Integrity Verification Report

*ARS v3.24.2 · `integrity_verification_agent` · Estágio 2.5 · quarta verificação (após a rodada 3 de correções) · concluída em 2026-11-15T22:25Z (UTC).
Manuscrito no commit `ed66940` (`git diff HEAD~1 HEAD -- paper/`). PDF `paper/projeto/projeto.pdf`: 21 páginas, 15 textuais.
Relatórios anteriores (`stage2.5_integrity_report.md`, `_round2.md`, `_round3.md`) não alterados. Este agente não editou o manuscrito nem os `.bib`. Arquivos gravados: este relatório e a atualização de `evidence/`.*

## Verification Mode

Initial Verification (Mode 1, pre-review), reverificação dos itens corrigidos na rodada 3. Não refeito: tudo o que não mudou desde a rodada 3.

## Verdict

**PASS WITH NOTES**

Zero SERIOUS, zero MEDIUM, zero MAJOR_DISTORTION, zero UNVERIFIABLE; 3 MINOR e notas. A IL-MEDIUM-1 foi resolvida pela divulgação.

**O checkpoint, porém, fica fechado pelo checklist de modos de falha.** A divulgação fez o rascunho voltar a descrever análises como feitas pelo autor, enquanto a declaração de intake segue `no_experiments_declared`. Pela regra, escrita como está, os Modos 3 e 6 ficam SUSPECTED e o Modo 1 fica INSUFFICIENT EVIDENCE; os três bloqueiam. Pelo meu protocolo, esse bloqueio não é issue das Fases A a E e não altera o veredito, mas o pipeline não avança até o pesquisador responder. A saída é uma decisão dele sobre a declaração, descrita na seção do checklist.

## Verification Summary

| Category | Total | Passed | Issues |
|----------|-------|--------|--------|
| Reference Existence | 39 | 39 | 0 |
| Bibliographic Accuracy | 39 | 39 nos campos presentes | 2 MINOR de completude, os mesmos da rodada 3, um deles reduzido |
| Ghost Citations | -- | -- | 0 órfãs na lista impressa / 0 pendentes (39 chaves citadas, 39 itens no `projeto.bbl`, nenhuma referência indefinida) |
| Citation Context Accuracy | 0 contextos novos | -- | 0 (nenhuma citação foi acrescentada ou alterada no texto) |
| Statistical Data Accuracy | 0 números novos | -- | 0 |
| Internal Consistency | 5 frases novas de divulgação conferidas contra o repositório | 4 | 1 MINOR ("essa especificação") |
| Originality Check (D1) | não refeita (rodada 1: 17 de 51, 33%) | -- | -- |
| Self-Plagiarism (D2) | não refeita | -- | -- |
| Claim Verification (E) | 54 de 58 registradas (Mode 1: HIGH-IMPACT: 39, RANDOM: 0, TOP-UP: 15; NOT-SELECTED: 4, só no E5; semantic extraction coverage: not_machine_detectable; candidate gaps: 1, falso positivo já inspecionado) | 45 | 0 MAJOR_DISTORTION / 0 UNVERIFIABLE (1 MINOR_DISTORTION; 8 UNVERIFIABLE_ACCESS) |

Restrições do autor:

| Restrição | Resultado |
|---|---|
| Nenhum número de estimativa | Nenhum. A divulgação é qualitativa: diz que houve diagnóstico, cálculo e rodada exploratória, e não reporta valor algum. "Setembro de 2026" é o único dado novo. |
| No máximo 15 páginas textuais | 15 (numeração impressa 3 a 17; referências a partir da 18). No limite. O encurtamento do último parágrafo da Introdução absorveu o texto acrescentado. |
| Só o Ensaio 1 | Sem mudança. |

O PDF é posterior aos fontes (22:23:48 contra 22:23:47) e contém o texto novo ("rodada exploratória"). Não o recompilei.

## Status das issues da rodada 3

| ID (rodada 3) | Status | Onde está agora | Observação |
|---|---|---|---|
| IL-MEDIUM-1 (etapas do estágio 1 no futuro; decisão anterior de manter) | **Resolvida** | `05-metodologia.tex:48-50`, `:209-210`, `:216-221`; `06-dados.tex:54-57`, `:62-65` | A decisão "Manter o texto como está" (ledger `seq: 8`) foi substituída por "Resolver a pendência antes" (ledger `seq: 11`, 22:24:11Z). Os cinco trechos agora dizem que a etapa foi feita em caráter preliminar e será refeita. Resta uma imprecisão de redação: IL-MINOR-1 desta rodada |
| IL-MINOR-1 (completude das entradas normativas) | **Parcialmente resolvida** | `referencias-projeto.bib` | `stf2023adi6137` completada e correta. As outras dez seguem sem endereço eletrônico e data de acesso (salvo `ibgepam`); três sem data de publicação oficial |
| IL-MINOR-2 (`ibge2006censoagro`, ano de publicação) | **Não resolvida** | `referencias-projeto.bib` | Sem mudança |

## Phase A: Reference Verification Results

Única entrada alterada: `stf2023adi6137`.

| Campo | Valor na entrada | Conferência |
|---|---|---|
| Título | "Ação Direta de Inconstitucionalidade nº 6137/CE" | Confere (ficha de jurisprudência do STF: "ADI 6137 / CE - CEARÁ") |
| Relatora | Min. Cármen Lúcia | Confere |
| Órgão e julgamento | "Tribunal Pleno, julgamento em sessão virtual de 19 a 26 maio 2023" | Confere ("Plenário, Sessão Virtual de 19.5.2023 a 26.5.2023"; o acórdão é datado de 29/05/2023) |
| Publicação | "Diário da Justiça Eletrônico, Brasília, 14 jun. 2023" | Confere ("DIVULG 13-06-2023 PUBLIC 14-06-2023") |

Fonte: ficha e inteiro teor lidos na rodada 1; notícia oficial baixada na rodada 2.

## Phase B: Citation Context Verification Results

Nenhuma citação nova ou alterada no texto. Sem mudança em relação à rodada 3.

## Phase C: Data Verification Results

### C1/C2. As frases novas, uma a uma, contra o repositório

| # | Frase | Local | Resultado | Evidência no repositório |
|---|---|---|---|---|
| 1 | "O plano de análise do primeiro estágio foi escrito e versionado em setembro de 2026" | `05-metodologia.tex:216-217` | Confere | `docs/pre-especificacao.md`: "Status: FECHADA · Data de fechamento: 2026-09-21"; commit `c386514`, de 2026-09-21 |
| 2 | "uma rodada exploratória com essa especificação já foi executada, não é reportada aqui e será refeita a partir das bases originais" | `05-metodologia.tex:217-219` | Confere quanto à rodada; **impreciso em "essa especificação"** | A §8 do plano registra que a família confirmatória foi estimada. Mas o plano fechado em 21/09 tinha a curva como alvo primário (§4: "Parâmetro-alvo primário: `slope`") e o nível como sensibilidade. O nível passou a alvo primário em 22/09, **depois** da rodada, com o motivo registrado na §8. O projeto descreve o nível como alvo e a curva como diagnóstico (`05-metodologia.tex:71-80`), isto é, a versão revista. IL-MINOR-1 |
| 3 | "um diagnóstico preliminar da dispersão da dose entre as culturas candidatas, entre elas o melão, apontou-a [a banana], e será refeito antes da estimação" | `05-metodologia.tex:48-50` | Confere | `docs/gates-resultados-dados-reais.md` §4 ("a variação de dose existe, e a cultura-âncora não é o melão": banana com área em 169 municípios e dispersão utilizável; melão em 10, algodão em 28); `docs/pre-especificacao.md` §3 ("Melão e algodão estão empiricamente encerrados [...] o dado a descartou"). Ressalva: o diagnóstico descartou melão e algodão e deixou a banana como a candidata viável ligada à prática aérea; caju, coco e manga também passaram no critério de dispersão. "Apontou-a" é leitura aceitável, não literal |
| 4 | "o cálculo preliminar já feito para o primeiro estágio será refeito com as bases congeladas" | `05-metodologia.tex:209-210` | Confere | `docs/gates-resultados-dados-reais.md` §5 e §6 (efeito mínimo detectável por cultura, com dados do pré-período) |
| 5 | "um levantamento preliminar encontrou uma, em Limoeiro do Norte, de 2009, dada como revogada em 2010. O levantamento será refeito no segundo estágio, com conferência de vigência." | `06-dados.tex:54-57` | Confere | `docs/legislacao/README.md`: 17 municípios do decil superior varridos, 1 com lei (Lei 1.478/2009), revogação pela Lei 1.511/2010 por fonte secundária, texto integral a conferir |
| 6 | "Uma avaliação preliminar do monitoramento da qualidade da água, dos registros meteorológicos e do mapeamento de uso da terra por satélite indicou limitações para esses fins" | `06-dados.tex:62-65` | Confere | `docs/lacunas-de-dados.md` §1-ter (água: três dos quatro princípios ativos predominantes sem medição, 95% de água tratada, quebra de registro a partir de 2020); vento com coerência de 0,96 entre estações; satélite com banana em classe genérica |
| 7 | "Este documento descreve um desenho, não um resultado: seguem o contexto institucional, [...]" | `01-introducao.tex:96-98` | Coerente com o restante | O texto não reporta resultado; a rodada exploratória é mencionada como não reportada |

Essas conferências são contra documentos do próprio repositório (fonte secundária interna). As análises em si não foram refeitas.

Consistência entre capítulos: sem contradição nova. A frase "o efeito mínimo detectável é calculado apenas com dados do pré-período, antes da estimação" (`05-metodologia.tex:206-208`) agora convive com a menção ao cálculo preliminar e à rodada exploratória; lida junto com "será refeito com as bases congeladas", descreve o procedimento a seguir na nova rodada.

### C3

Sem mudança (cinco quadros avulsos; nota *trace-unavailable*).

### C4. Experiment Provenance & Claim Alignment

"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

D7, com a declaração `no_experiments_declared` e sem `experiment_provenance[]`:

| Condição | Resultado |
|---|---|
| 1, 2, 3, 5 | Não acionadas, como nas rodadas 2 e 3 |
| 4. Sem experimentos declarados, mas o manuscrito mostra afirmações de experimento próprio | **Limítrofe; pela letra, não acionada.** O sinal mínimo que a regra define é (a) afirmação de manifesto com `planned_experiment_ids`, que não existe, ou (b) frase de seção de Resultados que relate um desfecho experimental em primeira pessoa (métrica, ablação ou rodada própria). O projeto não tem seção de Resultados e diz expressamente que a rodada exploratória "não é reportada aqui". As frases 3, 5 e 6 da tabela acima relatam, em Metodologia e Dados, o que três verificações preliminares indicaram, sem métrica |

Na rodada 1 marquei esta condição como acionada com ressalva, porque havia uma frase sobre o comportamento de uma estimativa; ela saiu na rodada 1 de correções. A mesma contradição entre declaração e rascunho é capturada, sem ambiguidade, pela regra do checklist de modos de falha, que é escrita de forma mais ampla. Se o pesquisador mudar a declaração (opção A abaixo), a D7 passa a exigir `experiment_provenance[]` (condição 2).

Nenhuma linha de `experiment_alignment_results[]`.

## Phase D: Originality Verification Results

Não refeita. A rodada 3 de correções alterou seis frases.

| Grade | Paragraph Count | Proportion |
|-------|----------------|-----------|
| ORIGINAL | -- | não refeita |
| COMMON_KNOWLEDGE | -- | -- |
| PARAPHRASE | -- | -- |
| CLOSE_MATCH | -- | -- |
| VERBATIM | -- | -- |

## Phase E: Claim Verification Results

**Claim Registry coverage sidecar (#737)**

Mudaram os bytes de 01, 05 e 06. Só os registros e relatórios desses três foram alterados; os de 02, 03, 04, 07 e 08 têm os mesmos SHA-256 da rodada 3 (conferido antes e depois).

- Status: `completed` (replay PASS nos três refeitos)
- Registry: `claim-registry/1.0`
- Candidate scope: citation-bearing + quantitative sentences only
- Candidate-unregistered count: 1 (o mesmo falso positivo: `05-metodologia.tex:136`, intervalo `[0,1]`)
- Semantic extraction coverage: `not_machine_detectable`

| Arquivo | Afirmações | Não registrados | SHA-256 do rascunho | SHA-256 do registro | SHA-256 da cobertura |
|---|---|---|---|---|---|
| 01-introducao | 14 | 0 | 1438c1d8a158e7807626c4a60866fa8c2293022e35d301c863fadaebb93178b0 | f5f56396b3d07b735ee24f04272f7d7b25f55fec04d95a225c2498a9205ab927 | feb0562b436795341e0d130db2b61f61974d8fe1f8c731cf7365aefa1fc0a9cd |
| 05-metodologia | 11 | 1 | 6ec897d7d90f6783a14c5f5c8157fb82a21cd09420da3051011c63df65a46107 | 404f1f693554f9985453290b6093ca66a5e1dcdc55a82a32a81a9f9f7e6ef7a1 | d690bd5513844ad03130d55c28ca26bb0dc5d998ae8bb4e3a8ed9f9f975aee8b |
| 06-dados | 4 | 0 | feae2d572620db436495c41f9838d8a9301159f646bba1a641053bdba465864a | 428abf8794d189d80ece114c77440d1d3aa11776d406aba30558440b1cf491da | 7de3cb7f468acc74c5434015d6a2830969a9a2284f005f9fccc07dde0c1ee1ea |
| 02, 03, 04, 07, 08 | 14, 14, 0, 0, 1 | 0 | inalterados | inalterados (ver relatórios das rodadas 2 e 3) | inalterados |

O limite do detector descrito na rodada 2 continua valendo.

| Verdict | Claim Count | Proportion |
|---------|------------|-----------|
| VERIFIED | 45 | 83% |
| MINOR_DISTORTION | 1 | 2% |
| MAJOR_DISTORTION | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| UNVERIFIABLE_ACCESS | 8 | 15% |

Mudanças em relação à rodada 3:

| Afirmação | Rodada 3 | Rodada 4 | Motivo |
|---|---|---|---|
| F22 (plano de análise) | MINOR_DISTORTION (texto no futuro) | MINOR_DISTORTION (texto novo) | A frase agora divulga plano e rodada; resta "essa especificação" |
| G09 (lei de Limoeiro do Norte) | VERIFIED | VERIFIED | span atualizado para a redação nova |
| G10 (diagnóstico de dose "apontou-a") | -- | VERIFIED | nova; fonte interna |
| G11 (cálculo preliminar do efeito mínimo detectável) | -- | VERIFIED | nova; fonte interna |
| G12 (avaliação preliminar "indicou limitações") | -- | VERIFIED | nova; fonte interna |

UNVERIFIABLE_ACCESS, os mesmos oito: C05, C06, C08, C16 e C18 (Calzada et al., texto publicado); C07 e C11 (Weitzman); C10 (Coase).

**Persisted Phase E evidence rows (#656)**

- `docs/ars/pipeline-rodada20/evidence/evidence_rows.json`, refeito (SHA-256 `a66a5e33863793f161c3200533ce4d44bc881f33b448f6acd0b1d05736cc3a43`), com `checked: 54` e `verified: 45`.
- 69 linhas: 40 `agent_extracted`, 9 `access_failed`, 20 `anchorless`. `evidence_rows.py validate evidence_rows.json --source-dir sources`: "PASS: 69 evidence row(s)".
- `phases.E_claims.evidence_source_dir`: `docs/ars/pipeline-rodada20/evidence/sources` (33 arquivos, sem mudança). As três afirmações novas e a F22 são conferidas contra documentos do repositório e têm linha `anchorless`, com a fonte descrita no detalhe.

**Scope-conformance advisory (#547)**: `[E4-SKIPPED: no scope context]`

| ID | Claim location | Effective scope | Drafted scope | Broadened axis |
|----|---------------|-----------------|---------------|----------------|
| -- | -- | -- | -- | -- |

**Novelty-claim classification (#548)** — advisory-only. As quatro linhas seguem abertas e inalteradas (ADV-E5-1 a ADV-E5-4; redação e sugestões no relatório da rodada 2).

| ID | Claim location | Claim wording | Classification | Nearest prior work / recommended bounded rewording |
|----|---------------|--------------|----------------|---------------------------------------------------|
| ADV-E5-1 a 4 | `01-introducao.tex:14-15`; `:23-24` e `:58-59`; `:88-89`; `08-cronograma.tex:9-10` | inalteradas | UNRESOLVED | inalteradas |

**Cache staleness advisory (#541)**: nenhuma linha servida de cache.

**Claim-strength drift review (#569)**: `[E6-SKIPPED: no revision evidence]`.

**Token-conservation advisory (#570)**: não executado.

## Issue List (Sorted by Severity)

IDs novos, desta rodada.

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
| IL-MINOR-1 | 1 | Claim precision (F22) | `paper/projeto/secoes/05-metodologia.tex:216-219` | "uma rodada exploratória com essa especificação já foi executada": o plano de setembro tinha a curva dose-resposta como alvo primário; o nível passou a alvo depois da rodada, com o motivo registrado na tabela de desvios do plano. A especificação que o projeto descreve é a revista | Acrescentar uma oração, sem número: "[...] já foi executada; depois dela o alvo principal passou da curva ao nível, com o motivo registrado na tabela de desvios do plano; a rodada não é reportada aqui e será refeita [...]". Custo: a contagem está em 15 páginas, sem folga |
| IL-MINOR-2 | 2 | Reference format | `paper/projeto/referencias-projeto.bib`: dez entradas normativas e estatísticas | Nenhum campo errado. Faltam endereço eletrônico e data de acesso (salvo em `ibgepam`), e data de publicação oficial em `ceara1993lei12228`, `ceara2024lei19135` e `cns2016res510` | "Disponível em" e "Acesso em" em cada uma. Datas: Lei 19.135, D.O. de 19/12/2024; Resolução 510, DOU de 24/05/2016; Lei 12.228, conferir o D.O. de 14/12/1993 |
| IL-MINOR-3 | 3 | Reference | `paper/projeto/referencias-projeto.bib`, `ibge2006censoagro` | Ano de publicação dos resultados do Censo Agropecuário 2006 não conferido | Conferir no catálogo do IBGE; se for outro, usar o ano de publicação e manter a nota "Ano de referência 2006" |

## AI Research Failure Mode Checklist

**A regra, como está escrita** (`academic-pipeline/references/ai_research_failure_modes.md`): os Modos 1, 3, 5 e 6 são NOT APPLICABLE quando a declaração é `no_experiments_declared`. Mas, se o rascunho mesmo assim apresenta experimentos ou análises de dados como feitos pelo autor (seus resultados, as configurações da rodada ou texto de método que os descreva como feitos), declaração e rascunho discordam: nenhum dos quatro é NOT APPLICABLE, os Modos 3 e 6 são SUSPECTED, e o usuário vê as duas coisas.

**As duas coisas.**
- A declaração (`passport.yaml`): `status: no_experiments_declared`, com a resposta do pesquisador: "É, Considere que eu rodei um primeiro projeto utilizando o pipeline, mas ainda o projeto eu considero que não, nenhuma estimativa ainda precisa ser consolidada. É um projeto para que eu vá realizar isso, certo? Então, o que eu fiz foi só apenas pegar os dados e tudo mais. [segunda resposta] Vamos começar do zero [...] vamos considerar que a gente vai rodar tudo do zero."
- O rascunho, agora: `05-metodologia.tex:48-50` (diagnóstico preliminar que "apontou" a banana), `:209-210` (cálculo preliminar "já feito"), `:216-219` (plano escrito e "rodada exploratória [...] já foi executada"), `06-dados.tex:54-56` (levantamento preliminar que "encontrou" uma lei) e `:62-64` (avaliação preliminar que "indicou limitações").

O texto de método descreve análises como feitas. A condição da regra está satisfeita. A divulgação que resolveu a IL-MEDIUM-1 é o que a reativa.

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | INSUFFICIENT EVIDENCE | A regra retira o NOT APPLICABLE. No mérito: o texto não reporta número algum saído dessas análises, e os números que reporta (184; 36 em 7; contagens da tabela do PL) foram refeitos de fonte primária nas rodadas 1 e 2. Não tenho os logs do diagnóstico de dose, do cálculo de efeito mínimo detectável nem da rodada exploratória (`data/processed` está vazio nesta sessão) | yes |
| 2. Hallucinated citation | CLEAR | 39 de 39 referências existem; a entrada do STF foi completada e confere | no |
| 3. Hallucinated experimental result | SUSPECTED (pela regra da declaração) | Declaração e rascunho discordam. No mérito, a evidência é favorável: nenhum resultado é reportado, e cada uma das cinco menções confere com documento versionado do repositório (tabela C1/C2) | yes |
| 4. Shortcut reliance | CLEAR (flag-only neste estágio) | Sem mudança | no |
| 5. Implementation bug reframed as novel insight | CLEAR | A regra retira o NOT APPLICABLE; avaliado no mérito. Nenhuma linguagem de surpresa; nenhum achado anunciado | no |
| 6. Methodology fabrication | SUSPECTED (pela regra da declaração) | Declaração e rascunho discordam. No mérito, o texto de método está mais fiel ao repositório do que em qualquer rodada anterior; resta a imprecisão "essa especificação" (IL-MINOR-1) | yes |
| 7. Frame-lock at early pipeline stage | CLEAR | Sem mudança. A divulgação torna visível que o alvo foi revisto depois da rodada exploratória, o que pesa contra travamento | no |

**Resultado do checklist:** bloqueio pelos Modos 1, 3 e 6, até o pesquisador responder.

**O que o pesquisador precisa decidir.** A discordância agora está do lado da declaração, não do texto. Três caminhos:

- **A. Corrigir a declaração.** Passar `experiment_intake_declaration.status` a `experiments_declared` e registrar no passport um `experiment_provenance[]` com as atividades preliminares que o texto menciona: diagnóstico de dose, cálculo de efeito mínimo detectável, rodada exploratória do estágio 1, levantamento de leis municipais, avaliação das bases de água, vento e satélite. Cada entrada pede `experiment_id`, `title`, `repro_lock` (ou nulo com motivo), `planned_vs_executed`, `negative_results` e `known_limitations`. Com isso a regra da declaração deixa de se aplicar, os modos passam a ser julgados pela evidência, e a C4 passa a produzir linhas de alinhamento para as afirmações F22, G09, G10, G11 e G12. Para o Modo 1 ele ainda teria de apontar os logs ou dizer que não os tem. É o caminho que alinha passport, texto e repositório; a própria resposta de intake já diz que ele rodou um primeiro projeto.
- **B. Anular com justificativa** (override), modo a modo, registrada para o Estágio 6. Justificativa disponível: nenhum resultado é reportado; as menções são de trabalho preliminar a refazer e conferem com documentos versionados. A declaração fica como está e a discordância fica registrada.
- **C. Voltar ao texto sem divulgação.** Devolve os modos a NOT APPLICABLE e reabre a IL-MEDIUM-1.

A declaração é do pesquisador (`declared_by: scholar`); não cabe ao orquestrador nem a mim alterá-la. A nota acrescentada ao `passport.yaml` nesta rodada já prevê que a decisão volte a ele.

## Tool Limitation Disclaimer

> This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 33% (rodada 1; não refeita desde então), and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.

Limitações, em resumo (as das rodadas 1 a 3 continuam valendo):

1. As frases de divulgação foram conferidas contra documentos do repositório, não contra logs nem saídas de execução. Não refiz o diagnóstico de dose, o cálculo de efeito mínimo detectável nem a rodada exploratória.
2. Não lidos: texto publicado de Calzada et al.; Weitzman (1974) e Coase (1960).
3. Fontes primárias não acessadas: Dossiê ABRASCO; leis municipais 1.478 e 1.511; autos da ação civil pública de 2011; tramitação do PL 134/2011; catálogo do IBGE.
4. Nenhuma consulta nova à web nesta rodada.
5. Fases D e D2 não refeitas; 27 entradas não citadas dos `.bib` sem verificação; E4 e E6 pulados; conservação de tokens não rodada; sem verificação cruzada entre modelos; `content_hash` do passport não conferido.
6. Não presenciei os checkpoints; as decisões são reportadas como o ledger as registra.

## Verification Audit Trail

Rodada 4, 2026-11-15, concluída às 22:25Z.

- Diferença examinada: `git diff HEAD~1 HEAD` em `ed66940` (três `.tex`, uma entrada de `.bib`, `passport.yaml`, ledger).
- Decisão do autor: `passport_run_ledger.yaml`, `seq: 11` (`checkpoint_closed`, `stage2.5-exit`, "resolver a pendência antes"), `seq: 12` (`integrity_fix_round: 3`).
- Frase 1: `docs/pre-especificacao.md`, linhas 3 a 20; `git log -- docs/pre-especificacao.md` (commit `c386514`, 2026-09-21).
- Frase 2: `docs/pre-especificacao.md` §4 (alvo primário `slope`) e §8 (linhas de 2026-09-22: troca do alvo; Holm; "a família confirmatória foi estimada").
- Frase 3: `docs/gates-resultados-dados-reais.md` §4 (tabela por cultura); `docs/pre-especificacao.md` §3 (linhas 96 a 99).
- Frase 4: `docs/gates-resultados-dados-reais.md` §5 e §6 (lidos nas rodadas 1 e 2).
- Frase 5: `docs/legislacao/README.md` (varredura dos 17 municípios).
- Frase 6: `docs/lacunas-de-dados.md` §1-ter e tabela de estado.
- `stf2023adi6137`: ficha `jurisprudencia.stf.jus.br/pages/search/sjur481679/false` e inteiro teor (rodada 1).
- Páginas e citações: `pdfinfo` (21); `projeto.toc` (capítulo 1 na página 3; referências na 18); 39 chaves; 39 `\bibitem`; log sem "undefined"; busca por padrões numéricos nos três `.tex` alterados (só o limiar de 2.500 gramas, que é definição de desfecho).
- Artefatos: SHA-256 dos registros e coberturas de 02, 03, 04, 07 e 08 comparados antes e depois (idênticos); `claim_registry_coverage.py --validate-report` nos três refeitos (PASS); `evidence_rows.py validate --source-dir sources` (PASS, 69 linhas).
