# Integridade — projeto_v7 (reescrita da seção 3.3 e Apêndice E)

Data: 2026-11-16. Objeto: commit da reescrita da seção 3.3 com Sant'Anna como
referência de diferença em diferenças, estimador duplamente robusto como
sensibilidade, Apêndice E (DAG → hipóteses) e cortes de texto em 01, 05–08.
Verificador: agente independente, sem acesso de escrita.

**Veredito do verificador: PASS WITH NOTES** (1 SERIOUS, 7 MINOR, notas).

## Cobertura da verificação
- Lidos na fonte: Ortiz-Villavicencio e Sant'Anna (arXiv 2505.09942, resumo e
  trechos da v3, não o texto integral); Olden e Møen (resumo e seções 5 e 8);
  Callaway, Goodman-Bacon e Sant'Anna 2024 (só o resumo); Baker et al. (resumo).
- **Só metadados (Crossref):** Callaway e Sant'Anna 2021, Goodman-Bacon 2021,
  de Chaisemartin e D'Haultfœuille 2020, Sant'Anna e Zhao 2020. O conteúdo
  atribuído a eles não foi conferido na fonte nesta rodada.

## Achados e destino
| nº | gravidade | achado | destino |
|---|---|---|---|
| 1 | SERIOUS | Chuva do ano usada como covariável do estimador duplamente robusto, que admite covariáveis anteriores ao tratamento | Corrigido: covariáveis municipais anteriores à lei (chuva média de 2007–2011); chuva do ano fica só na regressão |
| 2 | MINOR | Sant'Anna e Zhao citado como estimador de diferença tripla | Corrigido: citação retirada da frase |
| 3 | nota | Viabilidade do duplamente robusto com poucos tratados | Corrigido: "se o número de tratados permitir" no Apêndice C |
| 4 | nota | de Chaisemartin e D'Haultfœuille: frase só morde no caso contínuo | Mantido, aceito pelo verificador |
| 5 | nota | Resultado de CGS aplicado a exposição entre coortes é analogia | Corrigido: "por analogia com" |
| 6 | MINOR | Iniciais de Sant'Anna inconsistentes | Corrigido: "Pedro H. C." |
| 7 | MINOR | NBER WP sem número na lista | Corrigido: campo `note` |
| 9 | MINOR | Hipótese da chuva enunciada de dois modos | Corrigido no Apêndice E |
| 10 | MINOR | Antecipação mais forte no Apêndice E que no B | Corrigido: mesma redação |
| 11 | MINOR | Três listas de testes de seleção | Corrigido: lista do Apêndice C nos três |
| 12 | MINOR | Composição materna dada por cancelada | Corrigido no Apêndice E |
| 13 | nota | Apêndice E não lista versão única do tratamento nem o canal de renda | **Aberto**, sem espaço na página; não contradiz o texto |
| 14 | — | Cortes não removeram ressalva substantiva | Sem ação |

Preexistente, não corrigido: a seção 7 diz "sai atenuado" e o Apêndice B,
"atenuado ou invertido".

Após as correções: compila, zero citação indefinida, 15 páginas textuais.
As correções não passaram por nova verificação independente.
