## Volume esperado para triagem (bruto, antes da deduplicação)

| bloco | linhas | registros | fonte da contagem |
|---|---|---:|---|
| SQ1 internacional | OpenAlex #6 (camadas 1 e 2) | 3.730 | finalização, 2026-10-12 |
| SQ1 internacional | PubMed #5 | 2.054 | finalização, 2026-10-12 (grande sobreposição com o OpenAlex; ~150–350 só no PubMed) |
| SQ1 América Latina | OpenAlex #11 | 1.591–1.740 | finalização, 2026-10-12 |
| SQ1 América Latina | SciELO #5 + LILACS #4 | 458 + 567 (brutos) | finalização; o SciELO repete o artigo entre coleções |
| SQ1 Scopus | — | ⬜ | exportação do pesquisador |
| **SQ1, únicos estimados** | | **~5.000–5.500** | estimativa; o braço AL sobrepõe pouco ao internacional fora dos estudos em inglês |
| SQ2 método | OpenAlex #13 | ≤ 4.265 (≈3.400–3.800 após versões) | finalização, 2026-10-12 |
| SQ3 instrumento | OpenAlex #13 (+ PubMed P1, 578, triado por último) | ≤ ~5.650 únicos (5.837 brutos) | finalização, 2026-10-12 |

⚠️ **Recall em validação independente (finalização):**
- **SQ1 internacional: 5/7 (71%; IC 95% de Wilson 0,36–0,92).** As duas perdas são estudos argentinos que reportam "parâmetros neonatais/antropométricos". Os registros não têm resumo no OpenAlex, e o resumo no PubMed não traz nenhuma frase do bloco de desfecho. Um remendo amplo traria 2.223 registros de ruído e não foi adotado. **Mitigação prevista no protocolo:** busca de citações a partir das revisões relevantes. As duas perdas estão na lista de referências da revisão de escopo da EHP 2024 (10.1289/JHP1043), e o braço América Latina emendado recupera uma delas.
- **SQ1 América Latina: 7/10** na estratégia PRESS; a emenda pós-validação (#4) fecha as quatro perdas, mas essa emenda não foi validada de forma independente.
- **SQ2:** a validação foi emulada fora do OpenAlex, em títulos e resumos do arXiv, depois que as ferramentas esgotaram. Não é teste de recuperação.
- **SQ3: 5/9 só pela busca (IC exato 21–86%); 7/9 com a busca de citações do protocolo.** A causa estrutural é exigir o conceito "agrotóxico" no **título**, escolha que mantém o volume triável. O conjunto V4 veio só do Wiley e foi julgado por um único revisor (IA). Nenhuma string foi mudada depois do V4, para que ele siga como estimativa independente.

**Total geral:** ~5.000–5.500 (SQ1) + ~3.400–3.800 (SQ2) + ~5.650 (SQ3) ≈ **14.000–15.000 registros únicos** antes da triagem.
