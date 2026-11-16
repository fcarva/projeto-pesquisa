# Academic Integrity Verification Report

**Manuscrito:** projeto_v6, commit `1e71a72` ("Projeto v6: exposição em grupos e menção às proibições municipais"). Diff conferido: `git diff 23f0753 HEAD -- paper/` (5 arquivos: `03-referencial.tex`, `04-objetivos.tex`, `05-metodologia.tex`, `apendices.tex`, `referencias-projeto.bib`).
**Data:** 2026-11-16
**Agente:** integrity_verification_agent (ARS v3.24.2), regras do Estágio 4.5

## Verification Mode

**Mode 2: Final check (final-check)**, restrita ao que mudou depois do PASS WITH NOTES da v5 e ao que dependia disso.

## Verdict

**FAIL**

SERIOUS 0; MEDIUM 0; **MINOR 3**. Pela regra do 4.5, MINOR bloqueia. Duas das três estão em texto novo da v6; a terceira é a frase que o coordenador pediu para avaliar, e sobre ela não há decisão registrada do pesquisador (ele não selecionou a reescrita, mas também não decidiu mantê-la depois de saber que é issue).

## Verification Summary

| Item | Resultado |
|---|---|
| Referência nova (`lavor2019antes`) | Existe; autoria, título e data conferem |
| Contextos de citação novos | 2 (Lavor; Callaway, Goodman-Bacon e Sant'Anna no capítulo 5): 1 adequado, 1 com excesso (IL-MINOR-2) |
| Álgebra da Eq. (2) | Absorção confere; nenhum grupo vazio com estação de quatro meses |
| Consistência interna | 2 resíduos do desenho anterior (IL-MINOR-3) |
| Fase E | 96 afirmações registradas; 94 com veredito: 84 VERIFIED, 8 UNVERIFIABLE_ACCESS, 2 MINOR_DISTORTION |
| Compilação | PDF de 28 páginas, posterior aos fontes; 49 entradas para 49 chaves; nenhuma referência indefinida; BibTeX sem aviso |
| Restrições | 15 páginas textuais, impressas 5 a 19 (confere com a conta do coordenador); nenhum número de estimativa; só Ensaio 1 |

## Phase A: Reference Verification Results

`lavor2019antes`: a página da Agência Pública (cópia que baixei em 15/11) traz o título "Antes do Ceará, 8 municípios já haviam proibido fumigação aérea de agrotóxicos", a assinatura "Thays Lavor, Agência Pública/Repórter Brasil" e a data de 15 de fevereiro de 2019 (metadado `2019-02-15`). Todos os campos conferem. Não reabri a URL hoje.

## Phase B: Citation Context Verification Results

**A frase de `03-referencial.tex:65-68` (veredito independente).** Li os resumos das três versões publicadas.

- Callaway e Sant'Anna (2021): "(ii) variation in treatment timing" e "staggered DiD setups". A descrição "para adoção escalonada" confere.
- Goodman-Bacon (2021): "units that receive treatment at different times". Confere.
- de Chaisemartin e D'Haultfœuille (2020): "Linear regressions with period and group fixed effects […] estimate weighted sums of the average treatment effects (ATE) in each group and period, with weights that may be negative." O resumo não restringe o resultado à adoção escalonada; é um resultado geral sobre regressões de efeitos fixos com efeitos heterogêneos.

Concordo com a avaliação do coordenador em parte. Para os dois primeiros a frase é defensável: sem variação de data não há o que esses métodos explorem (em Callaway e Sant'Anna o caso de data única é um caso particular, e "não se aplicam" é forte, mas a leitura "nada acrescentam" cabe). Para o terceiro a caracterização está errada, e "não se aplica" contradiz o próprio capítulo 5, que agora evita o regressor contínuo por um argumento da mesma família. É **MINOR_DISTORTION**: IL-MINOR-1.

Registro de responsabilidade: nas rodadas anteriores dei VERIFIED a essa frase com o resumo de de Chaisemartin e D'Haultfœuille e só o título de Callaway e Sant'Anna. Revejo o veredito.

**Lavor (2019)** (`03-referencial.tex:68-70`): a reportagem sustenta "proibições e restrições municipais em outros estados" (8 cidades proibiram, 3 vetaram em áreas de proteção, 3 impuseram restrições; todas no Centro-Oeste, Sul e Sudeste). Não sustenta, no texto que li, "em datas diferentes": o corpo da reportagem não dá as datas das leis. Se elas existem, estão no mapa interativo, que não é texto e não foi lido. IL-MINOR-2.

**Callaway, Goodman-Bacon e Sant'Anna (2024)** (`05-metodologia.tex:121-125`): confere com o NBER WP 32117. O resumo diz que os estimadores de efeitos fixos "typically fail to have appealing causal interpretations, even when weights are non-negative", e o texto mostra a decomposição em média ponderada e a exigência de tendências paralelas fortes para a curva. Ressalva de alcance, não issue: o artigo trata de diferenças-em-diferenças com dose; aplicá-lo à tripla de calendário é analogia do projeto, e a frase ("numa regressão de efeitos fixos") é genérica o bastante para comportá-la.

## Phase C: Data Verification Results

**Álgebra da Eq. (2), conferida à mão.** Com janela gestacional fixa e coortes por mês de nascimento, `k_t` é função só do mês do ano.

- `A_m × k_t` é absorvido por `α_{m,s(t)}`; `k_t × Seca_t` e `k_t × Pos_t`, por `γ_t`; `A_m × Seca_t` e `A_m × Pos_t`, por `μ_{m,a(t)}`, porque os dois indicadores são definidos pelo ano de nascimento. O efeito principal da chuva também cai em `μ_{m,a(t)}`. A exclusão de 2012 e 2019 não é o que produz a absorção; ela só garante que a comparação seja contra 2007–2011.
- `β^H` é identificado pela interação tripla: dentro do município e do ano, a diferença entre as coortes de exposição alta e as de referência; a variação dessa diferença do período de referência para o pós-lei; e o contraste disso entre municípios com avião e de comparação.
- Com estação de quatro meses e janela de seis meses (dois trimestres), a sobreposição vai de 0 a 4 meses, e `P_t` assume 0, 1/6, 1/3, 1/2 e 2/3. Meses de nascimento por valor: 3, 2, 2, 2 e 3. Logo: referência (`P_t = 0`), 3 meses; intermediária, 4; alta (`P_t ≥ 1/2`), 5. **Nenhum grupo fica vazio.** O perfil saturado tem quatro indicadores, com 2 ou 3 meses cada.
- As três coortes de referência têm 3, 2 e 1 mês do terceiro trimestre na estação, o que confere com "as que têm apenas o terceiro trimestre na estação".
- A conta vale para a quadra provisória de fevereiro a maio. O texto diz que a estação é fixada no plano de análise; com estação de sete meses ou mais o grupo de referência some. Nota, não issue.

**Consistência.** Eq. (1) com `H_t = 1`, Eq. (2), H1 (`04-objetivos.tex:27-31`) e as linhas "Principal", "Período de seca", "Perfil saturado", "Linear em P_t", "Chuva por grupo", "Efeito por chuva" e "Terceiro trimestre" do Apêndice C são coerentes entre si. O resumo ("compara coortes com início de gestação dentro e fora da estação") continua compatível. Quadro da regra de decisão, H2 a H5 e cronograma não dependem da forma do regressor. Não há resto de "por unidade de `P_t`"; `P_t` só aparece na definição dos grupos e nas duas linhas de sensibilidade. Dois resíduos do desenho anterior: IL-MINOR-3.

**Apêndice C.** A linha em branco dentro do `tabular` (`apendices.tex:99`) já existia na v5 e não quebra o quadro: o PDF traz as 14 linhas, incluídas as duas novas, e o log não tem erro.

**C4/D7.** This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS. Nada de análise executada foi acrescentado.

## Phase D: Originality Verification Results

Não refeita. O texto novo é especificação do próprio projeto e uma frase sobre a reportagem.

## Phase E: Claim Verification Results

Registros, coberturas e linhas de evidência refeitos para `03-referencial.tex`, `04-objetivos.tex`, `05-metodologia.tex` e `apendices.tex` (119 linhas, validação PASS; replay de cobertura PASS; 46 arquivos em `evidence/sources/`). Entraram duas afirmações (C37, Lavor; C38, a atribuição nova ao WP 32117) e mudou um veredito (C20).

| ID | Local | Veredito |
|---|---|---|
| C20 | `03-referencial.tex:65-67` | MINOR_DISTORTION |
| C37 | `03-referencial.tex:68-70` | MINOR_DISTORTION |
| C38 | `05-metodologia.tex:121-125` | VERIFIED |

As 8 UNVERIFIABLE_ACCESS e as 3 linhas ADV-E5 da v5 seguem como estavam.

## Issue List (Sorted by Severity)

### SERIOUS (Must Fix)

Nenhuma.

### MEDIUM (Must Fix)

Nenhuma.

### MINOR (Recommended Fix at Stage 2.5; Must Fix at Stage 4.5)

**IL-MINOR-1.** `paper/projeto/secoes/03-referencial.tex:65-68`. A frase classifica de Chaisemartin e D'Haultfœuille (2020) como estimador "para adoção escalonada" que "não se aplica"; o resumo do artigo descreve um resultado geral sobre regressões de efeitos fixos.
Correção, uma frase no lugar da atual (até "variação de \emph{timing}."):
`Como a lei vale para todo o estado desde a mesma data, os estimadores e as decomposições de diferenças-em-diferenças que exploram variação na data de adoção \cite{callaway2021multiple,goodmanbacon2021} não têm aqui o que explorar, embora a advertência de que regressões de efeitos fixos misturam efeitos heterogêneos \cite{dechaisemartin2020} continue valendo: dentro do Ceará, não há variação de \emph{timing}.`
Se o pesquisador preferir manter a frase atual, é decisão dele e precisa ir ao ledger com as palavras dele.

**IL-MINOR-2.** `paper/projeto/secoes/03-referencial.tex:68-70`. "em datas diferentes" não tem apoio no texto da reportagem citada.
Correção: `Há registro de proibições e restrições municipais em outros estados \cite{lavor2019antes}; se as datas de adoção diferirem, um desenho de adoção escalonada entre municípios brasileiros é extensão possível, fora do escopo deste projeto, e essas leis não foram conferidas.`

**IL-MINOR-3.** Dois resíduos do regressor único.
(a) `paper/projeto/secoes/05-metodologia.tex:43-44`: "as coortes com início de gestação na estação de pulverização com as demais". Com três grupos, a comparação que define o hiato é com a referência, como H1 já diz. Correção: `as coortes de exposição alta à estação de pulverização no início da gestação com as expostas apenas no fim`.
(b) `paper/projeto/secoes/apendices.tex:98`, linha "Estudo de evento": "Um coeficiente de $A_m \times H_t$ por ano". Só com `H_t`, as coortes intermediárias entram na base de comparação, o que difere da Eq. (2). Correção: `Um coeficiente de $A_m \times k_t$ por ano, $k \in \{I,H\}$, com 2011 como base; reporta-se o de $H_t$`.

## AI Research Failure Mode Checklist

Declaração `no_experiments_declared`; override dos Modos 1, 3 e 6 registrado, com as palavras do pesquisador: "como é um projeto de pesquisa essa parte vai ser feita ao longo do ano, então é só o que eu vou fazer". A v6 muda a especificação planejada e não acrescenta análise executada nem resultado.

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | INSUFFICIENT EVIDENCE, coberto pelo override registrado | Sem código nem resultado | no |
| 2. Hallucinated citation | CLEAR | 49 de 49 referências existem; a nova confere | no |
| 3. Hallucinated experimental result | SUSPECTED pela regra da declaração, resolvido por override com justificativa | Sem resultado próprio | no |
| 4. Shortcut reliance | CLEAR | Sem resultado; os grupos e o limiar são fixados antes do desfecho, com perfil saturado reportado | no |
| 5. Implementation bug reframed as novel insight | NOT APPLICABLE | Sem resultado | no |
| 6. Methodology fabrication | SUSPECTED pela regra da declaração, resolvido por override com justificativa | Métodos descritos como plano | no |
| 7. Frame-lock at early pipeline stage | CLEAR | O desenho foi reaberto a pedido do pesquisador depois da entrega | no |

Decisões registradas do pesquisador, reportadas como tais: "Tratar a exposição contínua" e "Mencionar as proibições municipais" (origem da v6); REV-44 mantida como recomendação.

## Tool Limitation Disclaimer

- Mapa interativo da reportagem de Lavor (2019) não lido; a página não foi reaberta hoje.
- de Chaisemartin e D'Haultfœuille (2020), Callaway e Sant'Anna (2021) e Goodman-Bacon (2021): só os resumos.
- A álgebra foi conferida à mão, para a quadra provisória de quatro meses e gestação de nove meses com coortes mensais; não rodei verificação numérica de posto. O mérito da escolha do limiar e da referência não é objeto desta verificação.
- Fases A, C1 e D não refeitas fora do que mudou. Valem as limitações dos relatórios anteriores.

## Verification Audit Trail

- `git diff 23f0753 HEAD -- paper/` lido por inteiro.
- Resumos: RePEc/IDEAS (Callaway e Sant'Anna, hoje); Semantic Scholar (Goodman-Bacon; de Chaisemartin e D'Haultfœuille, guardados). NBER WP 32117 em `evidence/sources/`. Página da Agência Pública guardada em 15/11.
- `pdfinfo`, `pdftotext`, `projeto.log`, `projeto.blg`, `projeto.bbl`.
- Artefatos atualizados em `docs/ars/pipeline-rodada20/evidence/`. Nenhum arquivo do manuscrito nem `.bib` foi alterado. Nada foi commitado.
