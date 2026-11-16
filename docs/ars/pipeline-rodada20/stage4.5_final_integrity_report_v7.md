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

## Reverificação independente das correções (2026-11-16)

Segundo verificador, sem acesso de escrita e sem ver a rodada anterior.
**Veredito: PASS WITH NOTES** — 0 SERIOUS, 8 MINOR, 4 notas. Todos os
"Corrigido" acima foram confirmados no texto; nenhuma correção introduziu erro
factual; compilação limpa; 15 páginas textuais; nenhum número de estimativa.

Conteúdo da seção 3.3 conferido por resumo (não por texto integral) para
Baker et al., Callaway e Sant'Anna 2021, Goodman-Bacon 2021 e de Chaisemartin
e D'Haultfœuille 2020: todas as afirmações sustentadas.

| nº | achado da reverificação | destino |
|---|---|---|
| 1 | Condição "se o número de tratados permitir" só no Apêndice C | Corrigido: levada ao corpo |
| 2 | Mapeamento do duplamente robusto para o desenho de coortes não declarado | Corrigido no Apêndice C: unidade município × mês do ano; dois períodos; sem chuva do ano; inferência do desenho principal |
| 3 | Frase do duplamente robusto no parágrafo da chuva | Corrigido: movida para o parágrafo do grupo de comparação |
| 4 | Figura 1 ainda listava composição materna como absorvida | Corrigido no nó da figura |
| 5 | Seção 7 sem o desfecho composto na lista de testes de seleção | Corrigido |
| 6 | "atenuado" × "atenuado ou invertido" | Corrigido: seção 7 passa a "atenuado ou, se a seleção for forte, invertido" |
| 7 | Apêndice E sem linha para o duplamente robusto | Corrigido |
| 8 | Caixa alta quebrada em nomes acentuados na lista | Corrigido no `.bib` |

Ressalvas que ficam, do verificador: a sensibilidade duplamente robusta não
responde à ameaça da chuva do ano, e sim a tendências do hiato que variem com
características de base; com poucos tratados, a sobreposição do escore de
propensão é frágil; cinco anos de chuva média é climatologia ruidosa (uma
normal mais longa serviria melhor). Achado 13 da primeira rodada segue aberto.

Estas últimas oito correções são de redação e metadados e não passaram por
terceira verificação.

## Fechamento do achado 13 (2026-11-16)

A pedido do pesquisador, o Apêndice E ganhou duas linhas: versões do
tratamento (a hipótese de versão única não se sustenta; o parâmetro é a média
sobre as versões) e emprego e renda da fruticultura. A redação segue a seção
5.5 e o Apêndice B. Não passou por verificação independente.
