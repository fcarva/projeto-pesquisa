# Academic Integrity Verification Report

**Manuscrito:** projeto_v5, commit `23f0753` ("Projeto: duas entradas de bibliografia"). Diff conferido: `git diff HEAD~1 HEAD -- paper/`.
**Data:** 2026-11-16
**Agente:** integrity_verification_agent (ARS v3.24.2), Estágio 4.5, rodada 3

## Verification Mode

**Mode 2: Final check (final-check)**, terceira passada, restrita às duas entradas alteradas. O restante vale como nos relatórios das rodadas 1 e 2.

## Verdict

**PASS WITH NOTES**

Zero issues abertas: SERIOUS 0; MEDIUM 0; MINOR 0. As notas abaixo não bloqueiam.

## Verification Summary

| Item | Resultado |
|---|---|
| Diff | 3 linhas em `paper/projeto/referencias-projeto.bib`; nenhum `.tex` alterado; árvore de `paper/` limpa |
| `brasil2002decreto4074` | Nota com "Diário Oficial da União, Brasília, 8 jan. 2002, Seção 1, p. 1". Confere com o valor que confirmei em três fontes oficiais na rodada 2. IL-MINOR-1 da rodada 2 resolvida |
| `brasil2011sinasc` | `year = {2013}` e nota com a data do arquivo. Confere com o metadado do PDF (02/06/2013). A citação em `06-dados.tex:17` sai como (Brasil. Ministério da Saúde, 2013). IL-MINOR-2 da rodada 2 resolvida |
| Compilação | PDF de 28 páginas, posterior ao `.bib`; 48 entradas no `.bbl` para 48 chaves citadas; nenhuma referência indefinida no log; BibTeX sem aviso |
| Páginas textuais | 15, impressas 5 a 19; referências a partir da 20 |
| Restrições | Sem número de estimativa do autor; só Ensaio 1: cumpridas, sem mudança |
| Artefatos da Fase E | Seguem válidos: os `.tex` não mudaram (o SHA-256 de `06-dados.tex` é igual ao gravado no registro). Não foram refeitos |

## Phase A: Reference Verification Results

48 de 48 referências existem (rodadas 1 e 2). As duas entradas alteradas conferem nos campos corrigidos.

## Phase B: Citation Context Verification Results

Sem mudança: 66 comandos de citação, todos adequados.

## Phase C: Data Verification Results

Sem mudança. C4/D7: This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

## Phase D: Originality Verification Results

Sem mudança: 54 de 54 parágrafos de prosa sondados na rodada 1, sem coincidência literal.

## Phase E: Claim Verification Results

Sem mudança: 94 afirmações registradas; 92 com veredito, 84 VERIFIED e 8 UNVERIFIABLE_ACCESS; 2 no E5.

## Issue List (Sorted by Severity)

### SERIOUS (Must Fix)

Nenhuma.

### MEDIUM (Must Fix)

Nenhuma.

### MINOR (Recommended Fix at Stage 2.5; Must Fix at Stage 4.5)

Nenhuma.

## Notas que seguem abertas, sem bloquear

- **8 UNVERIFIABLE_ACCESS.** C06, C08, C15, C18, H14: Calzada, Gisbert e Moscoso (2023) conferido só no manuscrito de março de 2023, não na versão do JAERE. C07, C11: Weitzman (1974) não lido. C10: Coase (1960) não lido.
- **3 ADV-E5** (primazia, sem busca documentada): `01-introducao.tex:22-23`; `01-introducao.tex:75`; `03-referencial.tex:44-46`.
- **Alcance da leitura.** A maioria dos artigos foi conferida só no resumo; Pereira e Cuellar e a Portaria 298/2021, por trechos.
- **Fontes secundárias** para os eventos de 2010, 2011, 2012–2017 e a votação de 18/12/2018, como o Apêndice D declara.
- **URLs do SIDRA** não abertas (403 a esta sessão); contagens recalculadas de respostas guardadas em 15/11.
- **Decisão registrada do pesquisador:** REV-44 (contrafactual de volta dos voos) mantida como recomendação, "Manter como recomendação" (ledger, `stage3prime-decision`).
- **Override dos Modos 1, 3 e 6**, a relatar no Estágio 6.
- **Falha minha da rodada 1:** uma consulta de busca enviou o nome do autor a um buscador.

## AI Research Failure Mode Checklist

Declaração `no_experiments_declared`; override dos Modos 1, 3 e 6 registrado, com as palavras do pesquisador: "como é um projeto de pesquisa essa parte vai ser feita ao longo do ano, então é só o que eu vou fazer".

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | INSUFFICIENT EVIDENCE, coberto pelo override registrado | Nenhum código nem resultado apresentado | no |
| 2. Hallucinated citation | CLEAR | 48 de 48 referências existem | no |
| 3. Hallucinated experimental result | SUSPECTED pela regra da declaração, resolvido por override com justificativa | Nenhum resultado próprio no texto | no |
| 4. Shortcut reliance | CLEAR | Sem resultado que dependa de atalho | no |
| 5. Implementation bug reframed as novel insight | NOT APPLICABLE | Sem resultado | no |
| 6. Methodology fabrication | SUSPECTED pela regra da declaração, resolvido por override com justificativa | Métodos descritos como plano; divulgações conferem com o repositório | no |
| 7. Frame-lock at early pipeline stage | CLEAR | Premissas sem registro tratadas como hipóteses, com saída na regra de decisão | no |

**Resultado do checklist:** nenhum bloqueio. Modo 4 não está SUSPECTED; os modos SUSPECTED no 2.5 estão resolvidos por override do usuário com justificativa.

## Tool Limitation Disclaimer

Valem as limitações das rodadas 1 e 2. Nesta rodada só o diff, o PDF, o log e as duas entradas foram conferidos. O mérito do desenho não é objeto desta verificação.

## Verification Audit Trail

- `git diff HEAD~1 HEAD -- paper/` (3 linhas, só o `.bib`); `git status` de `paper/` limpo.
- `pdfinfo`, `pdftotext`, `projeto.log`, `projeto.blg`, `projeto.bbl`.
- Comparação do SHA-256 de `06-dados.tex` com o registro em `evidence/claim_registry__06-dados.json`.
- Nenhum arquivo do manuscrito, `.bib` ou artefato de evidência foi alterado nesta rodada. Nada foi commitado.
