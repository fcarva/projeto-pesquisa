# Academic Integrity Verification Report

**Manuscrito:** projeto_v5, commit `b121c65` ("Projeto v5: correções da integridade final"). Diff conferido: `git diff HEAD~1 HEAD -- paper/`.
**Data:** 2026-11-16
**Agente:** integrity_verification_agent (ARS v3.24.2), Estágio 4.5, rodada 2

## Verification Mode

**Mode 2: Final check (final-check)**, reverificação restrita ao que mudou na rodada 1 de correções e ao que dependia das seis issues. O restante vale como está no relatório da rodada 1 (`stage4.5_final_integrity_report.md`).

## Verdict

**FAIL**

Das seis MINOR da rodada 1, cinco estão resolvidas e uma está resolvida em parte. Restam **2 MINOR**, as duas em `referencias-projeto.bib`, cada uma de uma linha, e as duas agora com valor confirmado. Pela regra do 4.5, MINOR bloqueia e não há decisão registrada do pesquisador sobre elas. SERIOUS 0; MEDIUM 0.

## Verification Summary

| Item | Verificado | Resultado |
|---|---|---|
| Correções da rodada 1 | 6 issues, 17 pontos de edição | 5 resolvidas; IL-MINOR-4 com um resíduo |
| Referências novas ou alteradas | 2 novas, 15 alteradas | todas existem; 2 reparos de campo |
| Contextos de citação novos | 3 | adequados |
| Afirmações (Fase E) | 92 com veredito de 94 registradas | 84 VERIFIED; 8 UNVERIFIABLE_ACCESS (as mesmas); 2 no E5 |
| Modos de falha | 7 | nenhum bloqueio; sem mudança |

Restrições do autor: sem número de estimativa do autor (cumprida; as correções não introduziram número); **15 páginas textuais, impressas 5 a 19** (confere com a conta do coordenador: PDF de 28 páginas, capítulo 1 na impressa 5, capítulo 8 termina na 19, referências a partir da 20; PDF posterior aos fontes; log e BibTeX sem aviso); só Ensaio 1 (cumprida).

## Status das issues da rodada 1

| Issue | Estado | Conferência |
|---|---|---|
| IL-MINOR-1 | Resolvida | `02-contexto.tex:37-38`: "um produtor do Cariri relata duas aplicações aéreas por ano \cite{globorural2021bananais}" |
| IL-MINOR-2 | Resolvida | `03-referencial.tex:35-36` diz "o único relato disponível" e remete ao capítulo 2; `01-introducao.tex:56-58` e `07-ameacas.tex:35` ajustados |
| IL-MINOR-3 (a) a (d) | Resolvida | "coortes nascidas de 2013 a 2018" em `04-objetivos.tex` e `05-metodologia.tex`; H2 descritiva em 04, 05 e Apêndice C; linha "Sem 2020--2021" no Apêndice C, coerente com o Apêndice B; "Três ameaças" |
| IL-MINOR-4 | Resolvida em parte | URL, data de acesso e datas de DOE/DOU entraram; resta `brasil2002decreto4074` (IL-MINOR-1 desta rodada) |
| IL-MINOR-5 | Resolvida | `ibge2006censoagro`: "segunda apuração", 2012, URL da tabela 1008. A citação sai como (IBGE, 2012) ao lado de "Censo Agropecuário de 2006" no texto, o que está correto |
| IL-MINOR-6 (a) a (d) | Resolvida no texto | `mapa2021portaria298` citada em `05-metodologia.tex:182`; `brasil2011sinasc` citada em `06-dados.tex:17`; Apêndice A com "segundo o setor"; remissão à seção em `05-metodologia.tex:126`. O ano da entrada do SINASC é a IL-MINOR-2 desta rodada |
| ADV-E5-2 | Atenuada | "não se conhece estimativa causal do que a proibição de fato produziu": o capítulo descritivo de 2023 que achei deixa de contradizer a frase. Segue como linha aberta só porque não há busca documentada |

**Autoria de `agenciabrasil2016ceara`:** a página traz a assinatura "Edwirges Nogueira – Repórter da Agência Brasil". Autoria individual confere; (NOGUEIRA, 2016) está correto.

**`ibge2017censoagro` sem número de tabela:** aceito. O texto só nomeia a fonte de um recorte que ainda será feito. A URL nova não pôde ser aberta (o SIDRA devolve 403 a esta sessão).

## Phase A: Reference Verification Results

48 chaves citadas, 48 entradas no `.bbl`. Conferidas nesta rodada só as duas novas e as alteradas.

- `mapa2021portaria298`: existe. Portaria MAPA nº 298, de 22/09/2021, DOU de 24/09/2021, edição 182, Seção 1, p. 14. Campos conferem.
- `brasil2011sinasc`: existe. PDF aberto e lido (24 p.), título confere. Ano: ver IL-MINOR-2.
- `brasil2002decreto4074`: data do DOU agora confirmada em três fontes oficiais (Câmara dos Deputados, LexML, Planalto): 8 jan. 2002, Seção 1, p. 1. Ver IL-MINOR-1.
- Demais alterações: valores iguais aos que confirmei na rodada 1.

## Phase B: Citation Context Verification Results

Três contextos novos, todos adequados: Globo Rural para o relato do produtor; Portaria 298/2021 para os relatórios de drones (arts. 11 e 19, I); consolidação do SINASC para a troca do formulário ("a idade gestacional foi um dos campos que teve a forma de captação do dado alterada").

## Phase C: Data Verification Results

Nenhum dado novo. Consistência interna: os quatro desencontros da rodada 1 estão fechados; não achei desencontro novo nas linhas alteradas. C4/D7: This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS. Sem mudança.

## Phase D: Originality Verification Results

Não refeita. As edições são correções pontuais pedidas por este verificador, de poucas palavras cada uma.

## Phase E: Claim Verification Results

Registros, coberturas e linhas de evidência refeitos para os oito arquivos alterados (01 a 07 e apêndices); `projeto.tex` e `08-cronograma.tex` não mudaram. 94 afirmações registradas; 92 com veredito: 84 VERIFIED e 8 UNVERIFIABLE_ACCESS (as mesmas da rodada 1: C06, C07, C08, C10, C11, C15, C18, H14). 115 linhas de evidência, validação PASS; replay de cobertura PASS; 45 arquivos em `evidence/sources/` (entraram a Portaria 298, por trechos, e o PDF do SINASC).

Novelty-claim classification (#548), advisory-only: ADV-E5-1 (`01-introducao.tex:22-23`), ADV-E5-2 (`01-introducao.tex:75`, agora com redação limitada) e ADV-E5-3 (`03-referencial.tex:44-46`) seguem UNRESOLVED por falta de busca documentada. Não bloqueiam.

## Issue List (Sorted by Severity)

### SERIOUS (Must Fix)

Nenhuma.

### MEDIUM (Must Fix)

Nenhuma.

### MINOR (Recommended Fix at Stage 2.5; Must Fix at Stage 4.5)

**IL-MINOR-1 (resíduo da IL-MINOR-4 da rodada 1).** `paper/projeto/referencias-projeto.bib`, entrada `brasil2002decreto4074`: falta a data do DOU, agora confirmada.
Correção: `note = {Regulamenta a Lei n{\textordmasculine} 7.802, de 11 de julho de 1989. Di{\'a}rio Oficial da Uni{\~a}o, Bras{\'i}lia, 8 jan. 2002, Se{\c c}{\~a}o 1, p. 1},`

**IL-MINOR-2 (introduzida na correção).** `paper/projeto/referencias-projeto.bib`, entrada `brasil2011sinasc`: `year = {2011}` é o ano dos dados, e o documento não pode ser de 2011, porque descreve a base de 2011 já consolidada. O arquivo foi criado em 2 de junho de 2013 (metadado do PDF). A citação sai como (BRASIL, 2011) em `06-dados.tex:17`. É o mesmo tipo de erro que a IL-MINOR-5 da rodada 1 corrigiu no Censo.
Correção, sem colchetes no campo de ano: `year = {2013},` e `note = {Bras{\'i}lia. Data do arquivo eletr{\^o}nico: jun. 2013; o documento n{\~a}o traz data de publica{\c c}{\~a}o},`
Se o pesquisador preferir manter 2011, isso é decisão dele e deve ir ao ledger.

## AI Research Failure Mode Checklist

Declaração `no_experiments_declared`; override dos Modos 1, 3 e 6 registrado, com as palavras do pesquisador: "como é um projeto de pesquisa essa parte vai ser feita ao longo do ano, então é só o que eu vou fazer". As correções não acrescentaram análise nem resultado.

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | INSUFFICIENT EVIDENCE, coberto pelo override registrado | Sem mudança | no |
| 2. Hallucinated citation | CLEAR | 48 de 48 existem; as duas novas foram abertas | no |
| 3. Hallucinated experimental result | SUSPECTED pela regra da declaração, resolvido por override com justificativa | Sem mudança | no |
| 4. Shortcut reliance | CLEAR | Sem mudança | no |
| 5. Implementation bug reframed as novel insight | NOT APPLICABLE | Sem resultado | no |
| 6. Methodology fabrication | SUSPECTED pela regra da declaração, resolvido por override com justificativa | Sem mudança | no |
| 7. Frame-lock at early pipeline stage | CLEAR | Sem mudança | no |

**Decisão registrada do pesquisador, reportada como tal:** a recomendação da re-revisão sobre o contrafactual de volta dos voos (REV-44) foi mantida como recomendação e não entrou no texto, por seleção de opção, "Manter como recomendação" (ledger, fechamento de `stage3prime-decision`). Não é issue de integridade e não altera o veredito.

## Tool Limitation Disclaimer

- Valem todas as limitações da rodada 1 (versão publicada de Calzada et al. não lida; Weitzman e Coase só por metadados; maioria dos artigos só pelo resumo; fontes secundárias para 2010, 2011, 2012–2017 e 18/12/2018).
- Portaria 298/2021: lida por trechos da publicação no DOU, não na íntegra.
- URLs novas do SIDRA (`ibge2017censoagro`, `ibge2006censoagro`, `ibgepam`): não abertas; o serviço devolve 403 a esta sessão. A URL de `cns2016res510` não foi acrescentada pelo autor nem conferida por mim.
- Data de publicação do documento do SINASC: só o metadado do arquivo (2013); o documento não traz data.
- Fases C1 e D não refeitas; Fase A só nas entradas novas ou alteradas.
- O ano de `denteh2022misclassification` (2022, com a versão 3 de 2026) segue como estava; aceito desde o 2.5.

## Verification Audit Trail

- `git diff HEAD~1 HEAD -- paper/` lido por inteiro (texto e `.bib`).
- `pdfinfo` e `pdftotext` sobre `projeto.pdf`; `projeto.log` e `projeto.blg`.
- PDF do SINASC baixado e lido; Decreto 4.074 conferido em camara.leg.br, lexml.gov.br e planalto.gov.br (por trechos de busca).
- Artefatos atualizados em `docs/ars/pipeline-rodada20/evidence/`: registros e coberturas de 01 a 07 e apêndices, `evidence_rows.json`, `sources_manifest.json`, `sources/`.
- Nenhum arquivo do manuscrito nem `.bib` foi alterado. Nada foi commitado.
