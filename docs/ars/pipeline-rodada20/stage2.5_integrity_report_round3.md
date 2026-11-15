# Academic Integrity Verification Report

*ARS v3.24.2 · `integrity_verification_agent` · Estágio 2.5 · terceira passada (reverificação da rodada 2 de correções) · concluída em 2026-11-15T22:09Z (UTC).
Manuscrito no commit `e0a89d2`; as correções estão em `3ee75c1` (`git diff 7e34946 3ee75c1 -- paper/`; o commit `e0a89d2` só altera o ledger). PDF `paper/projeto/projeto.pdf`: 21 páginas, 15 textuais.
Relatórios anteriores: `stage2.5_integrity_report.md` e `stage2.5_integrity_report_round2.md`, não alterados. Este agente não editou o manuscrito nem os `.bib`. Arquivos gravados: este relatório e a atualização de `evidence/`.*

## Verification Mode

Initial Verification (Mode 1, pre-review), reverificação dos itens corrigidos na rodada 2. Não refeito: tudo o que não mudou desde a rodada 2.

## Verdict

**FAIL**, por uma única issue MEDIUM, que é uma decisão registrada do autor.

Pelos critérios do meu protocolo, qualquer issue MEDIUM aberta dá FAIL, e eu não posso rebaixá-la nem retirá-la. O mesmo protocolo prevê a saída: a entrada no Estágio 3 exige PASS **ou**, esgotado o laço de três rodadas de correção, uma decisão explícita e registrada do usuário sobre os itens não resolvidos. A decisão existe e está no ledger. O contador do ledger marca `integrity_fix_round: 2`. Cabe ao orquestrador, pela máquina de estados do pipeline, dizer se a decisão registrada basta agora ou se o laço precisa ser formalmente encerrado; não há terceira correção a fazer, porque o único item restante é o que o autor decidiu manter.

Tirando esse item, o estado é o de PASS WITH NOTES: zero SERIOUS, zero outra MEDIUM, 2 MINOR e notas.

## Verification Summary

| Category | Total | Passed | Issues |
|----------|-------|--------|--------|
| Reference Existence | 39 (37 da rodada 2 + 2 novas) | 39 | 0 |
| Bibliographic Accuracy | 39 | 39 nos campos presentes | 2 MINOR de completude (campos ausentes, nenhum errado) |
| Ghost Citations | -- | -- | 0 órfãs na lista impressa / 0 pendentes (39 chaves citadas, 39 itens no `projeto.bbl`, nenhuma referência indefinida no log) |
| Citation Context Accuracy | 5 contextos novos ou alterados | 5 | 0 |
| Statistical Data Accuracy | 2 afirmações corrigidas | 2 | 0 |
| Internal Consistency | -- | 1 inconsistência mantida por decisão do autor | 1 MEDIUM (IL-MEDIUM-1 da rodada 2) |
| Originality Check (D1) | não refeita (rodada 1: 17 de 51, 33%) | -- | -- |
| Self-Plagiarism (D2) | não refeita | -- | -- |
| Claim Verification (E) | 51 de 55 registradas (Mode 1: HIGH-IMPACT: 38, RANDOM: 0, TOP-UP: 13; NOT-SELECTED: 4, só no E5; semantic extraction coverage: not_machine_detectable; candidate gaps: 1, falso positivo já inspecionado) | 42 | 0 MAJOR_DISTORTION / 0 UNVERIFIABLE (1 MINOR_DISTORTION; 8 UNVERIFIABLE_ACCESS) |

Restrições do autor:

| Restrição | Resultado |
|---|---|
| Nenhum número de estimativa | Nenhum. As correções da rodada 2 não acrescentaram número algum além de "PL nº 134". |
| No máximo 15 páginas textuais | 15 (numeração impressa 3 a 17; referências a partir da 18). Continua no limite, sem folga. |
| Só o Ensaio 1 | Sem mudança. |

O PDF é posterior aos fontes (22:06:08 contra 22:06:05) e contém o texto corrigido ("PL nº 134"). Não o recompilei.

## Decisão registrada do autor sobre a IL-MEDIUM-1 da rodada 2

- **O item.** `paper/projeto/secoes/05-metodologia.tex:48-50`, `:206-208`, `:215-219`; `paper/projeto/secoes/06-dados.tex:55-57`, `:62-66`. O texto põe no futuro, e como anteriores à estimação, etapas do estágio 1 que o repositório registra como feitas entre agosto e setembro de 2026 (diagnóstico de dose, efeito mínimo detectável, plano de análise, levantamento de leis municipais, avaliação das bases de água, vento e satélite), e não menciona a rodada exploratória com a mesma especificação.
- **A decisão.** Ledger `passport_run_ledger.yaml`, entrada `seq: 8`, `kind: checkpoint_closed`, `checkpoint_id: stage2.5-round2`, `at: 2026-11-15T22:08:53Z`. `answer`: "manter o texto e registrar a decisão". `user_words`: "[resposta dada por seleção de opção] "Manter o texto como está"".
- **O que o orquestrador informa.** Que o pesquisador foi avisado de que o repositório registra o plano de setembro e a rodada exploratória, e de que a pendência fica listada como exceção consciente. Eu não presenciei o checkpoint; registro o que o ledger e o despacho dizem.
- **Como fica.** A issue permanece aberta, com a severidade da rodada 2, marcada como decisão do autor. A afirmação F22 segue com veredito MINOR_DISTORTION nas linhas de evidência, com a decisão anotada no detalhe. O item deve seguir listado no Estágio 3, no 4.5 e no resumo de processo do Estágio 6.

## Status das issues da rodada 2

| ID (rodada 2) | Status | Onde está agora | Observação |
|---|---|---|---|
| IL-MEDIUM-1 (etapas do estágio 1 no futuro) | **Mantida por decisão registrada do autor** | ver seção acima | Texto inalterado nesses trechos |
| IL-MEDIUM-2 (`ibgepam`, ano sem base) | **Resolvida** | `paper/projeto/referencias-projeto.bib`, `ibgepam` | `year = {2026}`; tabelas 1612 e 1613; "Acesso em: 25 ago. 2026". Confere com `docs/fontes-e-vintages.md` |
| IL-MINOR-1 (projeto de lei de 2011, "julho") | **Resolvida** | `02-contexto.tex:38` | "projeto de lei estadual com a mesma vedação (PL nº 134, maio); ação civil pública do Ministério Público (julho)". Confere com a página da ALECE (31/05/2011) |
| IL-MINOR-2 (janela "posterior à primeira proposição") | **Resolvida** | `05-metodologia.tex:59-60` | "é em sua maior parte posterior" |
| IL-MINOR-3 (`mapa2008in2`, data) | **Resolvida** | `referencias-projeto.bib` | "de 3 de janeiro de 2008"; "Diário Oficial da União, Brasília, 8 jan. 2008, Seção 1". Confere com o PDF oficial e com a reprodução baixada na rodada 2 |
| IL-MINOR-4 (`ibge2006censoagro`, ano) | **Parcialmente resolvida** | `referencias-projeto.bib` | A nota "Ano de referência 2006" desfaz a ambiguidade. O ano de publicação segue sem conferência; ver IL-MINOR-2 desta rodada |
| IL-MINOR-5 (fontes sem referência) | **Resolvida** | `01-introducao.tex:84` (`\cite{stf2023adi6137}`); `02-contexto.tex:20` (`\cite{ceara2011pl134}`); `02-contexto.tex:76-77` (`\cite{ibgepam}`); `05-metodologia.tex:117-118` (`\cite{ceara1993lei12228}`) | A linha do Quadro 1 sobre a ADI (`02-contexto.tex:42`) segue sem `\cite`, o que é aceitável em quadro cuja fonte é declarada |
| IL-MINOR-6 (endereço, data de acesso e data de publicação nas entradas normativas) | **Não resolvida** | `referencias-projeto.bib` | Só `ibgepam` ganhou data de acesso. Ver IL-MINOR-1 desta rodada |

## Phase A: Reference Verification Results

Duas entradas novas:

| Chave | Existência | Campo a campo | Fonte da conferência |
|---|---|---|---|
| ceara2011pl134 | VERIFIED | Autor institucional, número (134/2011) e data ("Apresentado em 31 de maio de 2011") conferem com a página da ALECE: "Sala das Sessões da Assembleia Legislativa do Estado do Ceará, em 31 de maio de 2011. Deputado HEITOR FÉRRER". Ressalva da rodada 2 mantida: o cabeçalho da página traz "EMENDA MODIFICATIVA / PROJETO DE LEI Nº 134/2011", e não conferi se o texto é o original ou uma versão emendada; 31/05/2011 é a data que consta do documento | `www2.al.ce.gov.br/legislativo/tramit2011/pl134_11.htm`, baixada na rodada 2 |
| stf2023adi6137 | VERIFIED | "Relatora: Min. Cármen Lúcia" confere. "Julgamento em maio de 2023" confere: sessão virtual de 19 a 26/05/2023, acórdão datado de 29/05/2023, publicado no DJe de 14/06/2023, decisão unânime. A entrada não traz a unidade da federação (ADI 6137/CE), o órgão julgador (Tribunal Pleno) nem a data de publicação | Notícia oficial do STF de 30/05/2023; ficha de jurisprudência e inteiro teor lidos na rodada 1 |

Campos corrigidos em entradas existentes (`ibgepam`, `mapa2008in2`, `ibge2006censoagro`): conferem, como na tabela de status.

## Phase B: Citation Context Verification Results

| Chave | Local | O que o texto atribui | Resultado |
|---|---|---|---|
| stf2023adi6137 | `01-introducao.tex:83-85` | o STF julgou constitucional, em 2023, a proibição de método | Confere. O Tribunal conheceu da ação quanto ao caput e ao § 1º do art. 28-B |
| ceara2011pl134 | `02-contexto.tex:19-20` | proposição semelhante em 2011, anterior ao projeto de 2015 | Confere: o art. 4º cria um art. 28-B com a mesma redação |
| ibgepam | `02-contexto.tex:76-77` | bananicultura presente na maior parte do estado | Confere: 169 de 184 municípios na média 2015-2018 |
| ceara1993lei12228 | `05-metodologia.tex:117-118` | cadastro estadual de prestadores, no órgão ambiental | Confere: art. 8º (registro na SEMACE) |
| (sem chave) | `02-contexto.tex:38` | PL nº 134, maio de 2011, "com a mesma vedação" | Confere |

## Phase C: Data Verification Results

**C1.** As duas afirmações corrigidas (mês do projeto de lei de 2011; janela "em sua maior parte posterior") conferem com a fonte primária.

**C2.** Reli as passagens alteradas e as que dependem delas. A cronologia está coerente entre `02-contexto.tex:19-21`, `:38-41`, `05-metodologia.tex:55-60` e `07-ameacas.tex:23`: proposições em maio de 2011 e fevereiro de 2015, certeza em dezembro de 2018, vigência em janeiro de 2019. Única inconsistência: a IL-MEDIUM-1 da rodada 2, mantida por decisão do autor.

**C3.** Sem mudança (cinco quadros avulsos; nota *trace-unavailable*).

**C4.** "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS." D7 sem mudança em relação à rodada 2: declaração presente, sem `experiment_provenance[]`, nenhuma das cinco condições de FAIL acionada. As correções da rodada 2 não introduziram frase de resultado próprio.

## Phase D: Originality Verification Results

Não refeita. As correções da rodada 2 alteraram cinco frases e nenhum parágrafo inteiro.

| Grade | Paragraph Count | Proportion |
|-------|----------------|-----------|
| ORIGINAL | -- | não refeita |
| COMMON_KNOWLEDGE | -- | -- |
| PARAPHRASE | -- | -- |
| CLOSE_MATCH | -- | -- |
| VERBATIM | -- | -- |

## Phase E: Claim Verification Results

**Claim Registry coverage sidecar (#737)**

Mudaram os bytes de três arquivos `.tex` (01, 02 e 05). Só os registros e relatórios desses três foram alterados; os dos outros cinco têm os mesmos SHA-256 da rodada 2 (conferido antes e depois).

- Status: `completed` (replay PASS nos três refeitos; os cinco restantes inalterados)
- Registry: `claim-registry/1.0`
- Candidate scope: citation-bearing + quantitative sentences only
- Candidate-unregistered count: 1 (o mesmo falso positivo da rodada 2, `05-metodologia.tex:136`, intervalo `[0,1]` lido como citação)
- Semantic extraction coverage: `not_machine_detectable`

| Arquivo | Afirmações | Não registrados | SHA-256 do rascunho | SHA-256 do registro | SHA-256 da cobertura |
|---|---|---|---|---|---|
| 01-introducao | 14 | 0 | 150c36939e53cafca1bdef5b58adb8b22d8d1f060a368a07fb3c28524bd7a9c0 | 4bb6bcce2d55aa1eb90701cbb041daacb1db3f211ec968e717b50d896821bacb | 9d3819d584f06a4f99b5feeb81bb7bc76fc98c9047c72ece609770faf602d821 |
| 02-contexto | 14 | 0 | abcbcf387b46033da922fe8479d02e2a3bd62815d56c2e4dc42da941b86c9d50 | c78120092f9684b8fbc9b10d50a8b87cb9fab855eed6f7eacd6ec3e438d7f370 | 3765f839e76f45bffd3009bc3bc10f423b1725c16f802b124eaed716d4a50509 |
| 05-metodologia | 9 | 1 | 9a76c443cc5050e79779d922f130aa0e19e2349277deb5128fe47500c1b5a23a | f3db929ce947ae1e25e14454fec1d58ebc815655bd5eeac5907f80a6c3e6f227 | 3188580a170e4e7cddb450c1dcb38bf9d2aaa8ce0013611c06299efa78e7cd11 |
| 03, 04, 06, 07, 08 | 14, 0, 3, 0, 1 | 0 | inalterados | inalterados (ver relatório da rodada 2) | inalterados |

O limite do detector descrito na rodada 2 continua valendo: ele não reconhece `\cite{}` nem unidades em português.

| Verdict | Claim Count | Proportion |
|---------|------------|-----------|
| VERIFIED | 42 | 82% |
| MINOR_DISTORTION | 1 | 2% |
| MAJOR_DISTORTION | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| UNVERIFIABLE_ACCESS | 8 | 16% |

Mudanças em relação à rodada 2:

| Afirmação | Rodada 2 | Rodada 3 | Motivo |
|---|---|---|---|
| G02 (projeto de lei de 2011) | MINOR_DISTORTION | VERIFIED | mês corrigido |
| G06 (janela e primeira proposição) | MINOR_DISTORTION | VERIFIED | redação corrigida |
| F04 (ADI 6137), G01 (proposição de 2011), G03 (bananicultura) | VERIFIED, sem fonte vinculada | VERIFIED, com fonte vinculada | passaram a ter `\cite`; ganharam linha de evidência com trecho |
| F22 (plano de análise) | MINOR_DISTORTION | MINOR_DISTORTION | texto mantido por decisão do autor |

UNVERIFIABLE_ACCESS, os mesmos oito: C05, C06, C08, C16 e C18 (Calzada et al., texto publicado); C07 e C11 (Weitzman); C10 (Coase).

**Persisted Phase E evidence rows (#656)**

- `docs/ars/pipeline-rodada20/evidence/evidence_rows.json`, refeito (SHA-256 `a621c2c52d014521b4573320e8a07e344c2bea3bb834518fb73043106a524633`), com `checked: 51` e `verified: 42`.
- 66 linhas: 40 `agent_extracted`, 9 `access_failed`, 17 `anchorless`. `evidence_rows.py validate evidence_rows.json --source-dir sources` devolveu "PASS: 66 evidence row(s)".
- `phases.E_claims.evidence_source_dir`: `docs/ars/pipeline-rodada20/evidence/sources`, agora com 33 arquivos. Três novos: `stf2023adi6137.txt` (notícia oficial do STF, não o acórdão), `ceara2011pl134.txt` (página da ALECE) e `ibgepam.txt` (resposta da API do SIDRA para a tabela 5457; o projeto cita as tabelas 1612 e 1613, que trazem a mesma variável).
- `sources_manifest.json` atualizado (SHA-256 `c5fcc066d896dcabffe6b91d5a97c850cd99f9c0ad516a328fba46eaa8c625d5`).
- O `git status` não lista a pasta `sources/` como não rastreada, o que indica que ela está fora do versionamento. Se for assim, o replay das linhas vinculadas a fonte só funciona onde a pasta existir.

**Scope-conformance advisory (#547)**: `[E4-SKIPPED: no scope context]`

| ID | Claim location | Effective scope | Drafted scope | Broadened axis |
|----|---------------|-----------------|---------------|----------------|
| -- | -- | -- | -- | -- |

**Novelty-claim classification (#548)** — advisory-only. As quatro linhas da rodada 2 seguem abertas e inalteradas (ADV-E5-1 a ADV-E5-4: `01-introducao.tex:14-15`; `:23-24` e `:58-59`; `:88-89`; `08-cronograma.tex:9-10`), todas UNRESOLVED.

| ID | Claim location | Claim wording | Classification | Nearest prior work / recommended bounded rewording |
|----|---------------|--------------|----------------|---------------------------------------------------|
| ADV-E5-1 a 4 | ver relatório da rodada 2 | inalteradas | UNRESOLVED | inalteradas |

**Cache staleness advisory (#541)**: nenhuma linha servida de cache.

**Claim-strength drift review (#569)**: `[E6-SKIPPED: no revision evidence]`, pelo mesmo motivo da rodada 2.

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
| IL-MEDIUM-1 | 1 | Internal consistency / disclosure. **Decisão registrada do autor: manter o texto** | `paper/projeto/secoes/05-metodologia.tex:48-50`, `:206-208`, `:215-219`; `paper/projeto/secoes/06-dados.tex:55-57`, `:62-66` | A mesma IL-MEDIUM-1 da rodada 2: etapas do estágio 1 descritas no futuro e como anteriores à estimação, contra o que o repositório registra | A correção possível segue sendo uma frase de divulgação sem número (texto sugerido no relatório da rodada 2). O autor decidiu não aplicá-la | `passport_run_ledger.yaml`, `seq: 8`; `docs/pre-especificacao.md` §0 e §8; `docs/ars/17` §1 |

### MINOR (Recommended Fix at Stage 2.5; Must Fix at Stage 4.5)

| ID | # | Category | Location | Issue Description | Suggestion |
|----|---|----------|----------|------------------|----|
| IL-MINOR-1 | 1 | Reference format | `paper/projeto/referencias-projeto.bib`: as 9 entradas normativas e estatísticas da rodada 1 de correções e as 2 desta | Nenhum campo errado; faltam campos. Sem endereço eletrônico e data de acesso em todas, salvo `ibgepam`. Sem data de publicação oficial em `ceara1993lei12228`, `ceara2024lei19135`, `cns2016res510` e `stf2023adi6137`. `stf2023adi6137` também sem a unidade da federação e o órgão julgador | "Disponível em" e "Acesso em" em cada uma. Datas: Lei 19.135, D.O. de 19/12/2024; Resolução 510, DOU de 24/05/2016; ADI 6137/CE, Tribunal Pleno, julgamento em 29/05/2023, DJe de 14/06/2023; Lei 12.228, conferir o D.O. de 14/12/1993 |
| IL-MINOR-2 | 2 | Reference | `paper/projeto/referencias-projeto.bib`, `ibge2006censoagro` | `year = {2006}` com a nota "Ano de referência 2006" é defensável, mas o ano de publicação dos resultados não foi conferido | Conferir no catálogo do IBGE e, se for outro, usar o ano de publicação, mantendo a nota |

## AI Research Failure Mode Checklist

Declaração no passport: `no_experiments_declared`, com a resposta do pesquisador citada nos relatórios das rodadas 1 e 2 ("É, Considere que eu rodei um primeiro projeto utilizando o pipeline, mas ainda o projeto eu considero que não, nenhuma estimativa ainda precisa ser consolidada. [...] vamos considerar que a gente vai rodar tudo do zero."). O texto corrigido continua sem apresentar análise como feita pelo autor; a regra NOT APPLICABLE se aplica.

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | NOT APPLICABLE | Declaração acima; sem mudança desde a rodada 2 | no |
| 2. Hallucinated citation | CLEAR | 39 de 39 referências existem; as duas novas e os três campos corrigidos conferem com fonte primária | no |
| 3. Hallucinated experimental result | NOT APPLICABLE | Declaração acima; nenhum resultado próprio no texto | no |
| 4. Shortcut reliance | CLEAR (flag-only neste estágio) | Sem mudança | no |
| 5. Implementation bug reframed as novel insight | NOT APPLICABLE | Declaração acima | no |
| 6. Methodology fabrication | NOT APPLICABLE | Declaração acima. O tempo verbal das etapas já feitas é tratado fora do checklist, na IL-MEDIUM-1, agora com decisão registrada do autor | no |
| 7. Frame-lock at early pipeline stage | CLEAR | Sem mudança desde a rodada 2 | no |

**Resultado do checklist:** nenhum modo bloqueia.

## Tool Limitation Disclaimer

> This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 33% (rodada 1; não refeita nas rodadas 2 e 3), and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.

Continuam valendo as limitações das rodadas 1 e 2. Em resumo:

1. Não lidos: texto publicado de Calzada et al.; Weitzman (1974) e Coase (1960).
2. Fontes primárias não acessadas: Dossiê ABRASCO; leis municipais 1.478 e 1.511; autos da ação civil pública de 2011; tramitação e desfecho do PL 134/2011; Diário Oficial do Estado; catálogo do IBGE.
3. O acórdão da ADI 6137 foi lido na rodada 1 pela ferramenta de busca; a fonte guardada na pasta de evidências é a notícia oficial do STF.
4. Nesta passada não fiz nenhuma consulta nova à web: usei o que foi baixado nas rodadas 1 e 2.
5. Fases D e D2 não refeitas; as 27 entradas não citadas dos `.bib` seguem sem verificação; as 28 referências originais não foram reverificadas do zero.
6. E4 e E6 pulados; conservação de tokens não rodada; sem verificação cruzada entre modelos; `content_hash` do passport não conferido.
7. Não presenciei o checkpoint em que a decisão foi tomada; reporto o que o ledger registra.

## Verification Audit Trail

Rodada 3, 2026-11-15, concluída às 22:09Z.

- Diferença examinada: `git diff 7e34946 3ee75c1 -- paper/` (5 frases em 3 arquivos `.tex`; 3 entradas corrigidas e 2 novas em `referencias-projeto.bib`). `git show e0a89d2`: só o ledger.
- Decisão do autor: `git show e0a89d2 -- docs/ars/pipeline-rodada20/passport_run_ledger.yaml`, entradas `seq: 8` e `seq: 9`.
- `ceara2011pl134`: texto da página da ALECE baixada na rodada 2 (`pl134_11.htm`), fecho "em 31 de maio de 2011. Deputado HEITOR FÉRRER" e art. 4º.
- `stf2023adi6137`: notícia do STF baixada na rodada 2 ("Por unanimidade, o Plenário do Supremo Tribunal Federal (STF) manteve a validade de dispositivo de lei do Ceará que proíbe a pulverização aérea de agrotóxicos no estado. A decisão se deu na sessão virtual finalizada em 26/5"); ficha de jurisprudência e acórdão da rodada 1 (relatora, 29/05/2023, DJe 14/06/2023).
- `ibgepam`: `docs/fontes-e-vintages.md`, linha 9 (tabelas 1612 e 1613; 2026-08-25).
- `mapa2008in2`: PDF oficial (rodada 1) e reprodução (rodada 2).
- Páginas e citações: `pdfinfo` (21); `projeto.toc` (capítulo 1 na página 3; referências na 18); 39 chaves distintas nos `.tex`; 39 `\bibitem`; `projeto.log` sem "undefined".
- Artefatos: SHA-256 dos registros e coberturas de 03, 04, 06, 07 e 08 comparados antes e depois da reconstrução (idênticos); `claim_registry_coverage.py --validate-report` nos três refeitos (PASS); `evidence_rows.py validate --source-dir sources` (PASS, 66 linhas).
