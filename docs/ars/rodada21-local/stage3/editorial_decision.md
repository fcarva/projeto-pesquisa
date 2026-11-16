# Editorial Decision

## Manuscript Information
- **Title**: Proibição da pulverização aérea de agrotóxicos no Ceará: efeitos sobre o peso ao nascer
- **Manuscript ID**: não há; arquivo lido: `manuscript.txt` (SHA-256 `c0200ab9dc9344c5497bce1147c9c9b1fdde7230c47ef713100bd13fa353fb80`)
- **Natureza**: projeto de pesquisa de mestrado em economia, sem estimativa própria
- **Decision Date**: 2026-11-16
- **Review Round**: Round 1 (Estágio 3, modo `full`, contrato `reviewer/reviewer_full/v2`)
- **Veículo**: não confirmado. Chamada não vinculada (`criteria_binding_unavailable`), declarada pelos cinco assentos na Fase 1. Esta carta não faz alegação de alinhamento a critérios de veículo algum; o assento `eic` usou como referência uma banca de programa de pós-graduação em economia.

## Calibration Resolution

`calibration_status: NOT_CALIBRATED`

Nenhum perfil de calibração foi medido para este painel. Os cinco pareceres declaram o mesmo estado.

## Review Panel Provenance (#540/#740)

- **Typed artifact**: não fornecido à síntese (estado `invalid`, razão `absent`)
- **Artifact SHA-256**: unknown
- **Panel ID**: unknown
- **Normalized manifest SHA-256**: unknown
- **Execution topology SHA-256**: unknown
- **Fresh-context scope**: `within_panel_attempt_only`

| Provenance axis | Status (`true` / `false` / `unknown`) |
|---|---|
| Role-separated | unknown |
| Within-panel invocation-context separation | unknown |
| Blind to peer outputs | unknown |
| Model-family distinct | unknown |
| Provider distinct | unknown |
| Human-reviewer distinct | unknown |

- **Binary independence claim**: Not computed. Os cinco assentos têm papéis separados no contrato; isso não é alegação de independência de erro.
- **Correlated-error disclosure**: requerida, razão `model_family_unknown`. O artefato `review-panel-provenance/1.0` é da sessão que despacha e não estava na pasta; por isso todos os eixos saem `unknown`, e nada aqui foi inferido de persona ou de configuração. Falha de artefato de proveniência registrada.

---

## Decision *

### Major Revision

Decisão do motor mecânico do contrato, sem matriz qualitativa. Todos os bloqueios são `repairable`; nenhum é `fatal`.

dimension_verdicts: [D1=block, D2=warn, D3=block, D4=warn, D5=warn, D6=block]
fired_conditions: [F2, F3, F5]
da_critical_adjudications: [C1=VALIDATED]
editorial_decision=major_revision

---

## Mechanical Decision Engine (a conta)

**Step 1 — matriz por papel.** Só entram notas de assentos elegíveis que avaliaram a dimensão. Notas `not_assessed` de assentos não elegíveis ficam fora do numerador e do denominador.

| Dimensão | Prioridade | Assentos elegíveis | Notas avaliadas | Gatilho declarado pelo assento | Veredito (pior nota) |
|---|---|---|---|---|---|
| D1 methodology_rigor | mandatory | methodology | methodology = block (repairable) | "a fronteira entre análise confirmatória e exploratória não pode ser verificada" | block |
| D2 domain_accuracy | mandatory | domain | domain = warn | "as ressalvas de transferência de um resultado externo estão listadas mas não são levadas às consequências no uso que o texto faz dele" | warn |
| D3 argumentative_coherence | mandatory | da, methodology | da = block (repairable); methodology = warn | da: "depende de uma premissa não declarada e não sustentada"; methodology: "ressalvas declaradas em um trecho e ignoradas em outro" | block |
| D4 cross_disciplinary_relevance | high | perspective | perspective = warn | "ressalva conhecida do campo adjacente omitida" | warn |
| D5 writing_and_structure | normal | eic | eic = warn | "há termos, siglas ou notação usados antes de definidos ou de forma não uniforme" | warn |
| D6 venue_fit_and_contribution | mandatory | eic | eic = block (repairable) | "o que é entregue não é sustentado como suficiente para o requisito do veículo" | block |

Em D3 as duas notas elegíveis diferem (da block, methodology warn). Não há média: o veredito de auditoria é a pior nota avaliada.

**Step 2 — condições de falha.**

| Condição | Severidade | Quantificador entre assentos | Expressão (padrão do §9) | Avaliação dimensão a dimensão | Disparou? |
|---|---|---|---|---|---|
| F1 | 95 | any | algum bloqueio fatal em dimensão mandatory (padrão 6) | D1, D3 e D6 em block, todos repairable; D2 warn. Nenhum fatal. | não |
| F2 | 90 | any | alguma dimensão mandatory com nota block (padrão 1) | D1: methodology block, sim. D3: da block, sim. D6: eic block, sim. D2: não. | **sim** |
| F3 | 70 | majority | duas ou mais dimensões mandatory com warn ou pior (padrão 2) | D1 (n=1, o dono): sim. D2 (n=1): sim. D3 (n=2, exige os dois): da block e methodology warn, sim. D6 (n=1): sim. Quatro de quatro. | **sim** |
| F4 | 60 | any | alguma dimensão high com nota block (padrão 1) | D4: warn. | não |
| F5 | 40 | any | alguma dimensão com warn ou pior (padrão 7) | as seis. | **sim** |
| F0 | 10 | all | todas as dimensões com pass (padrão 9) | nenhuma. | não |

Todas as expressões foram reconhecidas no vocabulário fechado.

**Step 3 — precedência.** Entre F2 (90), F3 (70) e F5 (40), vence F2. Ação de F2: revisão substancial (`major_revision`). A ação não foi abrandada nem endurecida. F3 levaria à mesma ação; F5, sozinha, levaria a revisão menor.

**O que mudaria a conta.** Para sair de revisão substancial seria preciso que D1, D3 e D6 deixassem de estar em block e que no máximo uma dimensão mandatory ficasse em warn. Isso é matéria do Estágio 3', não desta carta.

---

## DA-CRITICAL Adjudication

**C1 — a premissa de que os voos voltariam depois da seca.**

*O argumento do assento `da`.* O coeficiente confirmatório compara 2007 a 2011 com 2020 em diante. Ele só equivale ao efeito da lei se, sem ela, os voos voltassem ao padrão da referência quando a chuva voltou. Essa premissa não está entre as hipóteses de identificação. O texto trata "não voar desde antes" como mais uma versão do tratamento; mas, para esses municípios, o estimador atribui à lei toda a variação ocorrida desde a referência. A regra de decisão declara o desenho confirmatório com voo em um único ano da referência e não tem linha para a prática ter cessado antes de 2019.

*Conferência no manuscrito.*

1. As duas frases citadas existem e dizem o que o assento afirma: "ou não voar desde antes, por causa da seca. O parâmetro, de intenção de tratar, é a média sobre essas versões." (Cap. 5, Interferência e versões do tratamento) e "Contam-se como documentados os voos registrados em ao menos um ano do período de referência." (Cap. 5, Regra de decisão).
2. A premissa não está declarada como hipótese. O quadro que liga o diagrama às hipóteses lista tendências paralelas, ausência de antecipação, ausência de interferência e versão única do tratamento; o retorno dos voos não aparece. O texto conhece o cenário e o descreve como leitura: "a lei teria impedido a sua volta, e não interrompido uma prática em curso" (Cap. 7), "precisava haver voos a suspender ou a impedir de voltar" (Cap. 5, cadeia causal).
3. A regra de decisão não tem linha para cessação anterior à lei. A linha 1 depende só de voos documentados por município e mês e de poder.
4. O intervalo de 2013 a 2018 não funciona como teste: o coeficiente do período de seca é declarado descritivo e o fechamento do hiato é a própria H2.
5. O manuscrito relata causas de cessação que não são a chuva: a notícia de proibição e a ação civil pública de 2011, a regulação municipal de 2010 com distâncias mínimas, a possível retração da lavoura. Só a seca entra na lista de versões.

*O que não se sustenta.* A sub-afirmação de que a premissa "não tem evidência prevista" é mais forte do que o texto permite. O projeto pede os relatórios mensais de 2008 a 2024 do Ceará e do Rio Grande do Norte, lista "relatórios mensais" como resposta à ameaça "voos suspensos pela seca antes da lei" no quadro de ameaças, registra o relato de um produtor que voou até 2018 e prevê H3 (efeito maior nos anos chuvosos). A evidência está prevista; o que falta é dar a ela papel de teste da premissa e consequência na regra. O próprio assento reconhece isso na sua narrativa (item 3 das explicações alternativas).

*Corroboração por outros assentos.* Nenhum dos quatro assentos sem o `da` levantou a premissa como tal. Três tocam o mesmo fato: `methodology` W5 (a divergência entre 2012 e 2019 "não é testável porque o período pode já estar tratado pela suspensão dos voos"), `methodology` W2 (intenção de tratar "sobre versões que incluem municípios onde já não se voava") e `eic` W4 ("onde a prática existia" convive com a hipótese de voos suspensos desde 2012).

*Adjudicação.* **Parcialmente validado: validado no núcleo, com uma sub-afirmação não sustentada.** O núcleo (premissa não declarada como hipótese de identificação; nenhuma linha da regra para cessação anterior à lei; um coeficiente positivo não distingue "a lei funcionou" de "a prática acabou antes") confere com o manuscrito e é o que carrega a gravidade. A gramática de auditoria só admite três valores; como o núcleo está confirmado, o valor registrado é `VALIDATED`. A sub-afirmação sobre ausência de evidência prevista fica registrada como não sustentada e reduz o tamanho do reparo: é texto e regra, sem dado novo, como o próprio assento diz.

*Efeito sobre a decisão.* Nenhum sobre a conta: a decisão já é revisão substancial por F2, e D3 já está em block. Um CRITICAL validado impediria a aceitação se a conta desse aceitação; não é o caso.

*Resposta exigida do autor.* REV-32 (`must_fix`).

---

## Blocking Issues * (0–3, immutable source order)

Os três são os gatilhos declarados dos três bloqueios (D6, D1, D3). Os outros seis itens `must_fix` estão na seção Required Revisions.

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---------------|----------------|--------------------|-----------------|------------------------|
| R1 | O texto não sustenta que a entrega das linhas 2 a 5 da regra de decisão basta como ensaio de dissertação (gatilho de D6) | eic W1 | absence: secoes/08-cronograma.tex (Resultados esperados) e secoes/05-metodologia.tex (Seção sec:regra) — expected argumento de suficiência das linhas 2 a 5; checked resumo, Cap. 1, Cap. 4, Cap. 5 (sec:regra), Cap. 8 e os quatro apêndices | REV-01 |
| R6 | O estatuto confirmatório não é verificável depois das rodadas exploratórias declaradas (gatilho de D1) | methodology W1; da M1; methodology W12; eic W6, W9; perspective W9 | text: secoes/05-metodologia.tex, Inferência, poder e plano de análise "a exposição sazonal já foi cruzada com o desfecho do pós-lei" | REV-07 |
| R9 | A premissa de retorno dos voos não é hipótese declarada e a regra não cobre a cessação anterior à lei (gatilho de D3; DA C1) | da C1 | text: secoes/05-metodologia.tex, seções Interferência e versões do tratamento e Regra de decisão "ou não voar desde antes, por causa da seca. O parâmetro, de intenção de tratar, é a média sobre essas versões." | REV-32 |

---

## Reviewer Summary

| Reviewer | Role | Recommendation | Confidence |
|----------|------|---------------|------------|
| Journal-Fit Reviewer (`eic`) | Professor titular de economia aplicada; bancas de qualificação e defesa | Major Revision (sinal do assento) | 4 (3 no achado W4) |
| Reviewer 1 (`methodology`) | Econometrista aplicado: diferença tripla, poucos tratados, planos pré-especificados, poder | Major Revision | 4 |
| Reviewer 2 (`domain`) | Economista ambiental e da saúde: agrotóxicos e desfechos ao nascer, semiárido, instrumentos | Minor Revision | 3 |
| Reviewer 3 (`perspective`) | Saúde coletiva e vigilância em saúde ambiental; epidemiologia perinatal | Minor Revision | 4 |
| Devil's Advocate (`da`) | Assento adversarial fixo | N/A — findings only | N/A — per-finding only |

A confiança é declaração de incerteza e de escopo de cada assento. Ela não foi somada, ponderada nem usada para resolver divergência.

---

## Consensus Analysis *

O consenso é contado sobre os quatro assentos sem o `da`, por sub-afirmação. Silêncio não é concordância.

### Points of Agreement (Consensus)

**[CONSENSUS-4]**: nenhum achado de fraqueza foi levantado pelos quatro. Há um ponto forte reconhecido pelos quatro, e também pelo `da`: a franqueza do texto sobre os próprios limites e a separação entre método e cultura, entre relato e registro, entre confirmatório e exploratório (`eic` S1 a S3; `methodology` S1, S4, S5; `domain` S1 a S3; `perspective` S1 a S3, S6, S7; `da`, "O que o projeto faz bem").

**[CONSENSUS-3]** (três de quatro, o quarto em silêncio):

1. **A regra de decisão não cobre registros parciais** (SC-04a; REV-04). `eic` W3 ("as linhas não cobrem casos que o próprio texto torna prováveis"), `methodology` W6 ("falta o cenário que o texto trata como provável: registros obtidos em parte"), `perspective` W1 ("não o caso mais provável em arquivo administrativo: entrega parcial"). Em silêncio: `domain`.
2. **A grade de frações expostas que decide se há teste não está fixada nem tem fonte** (SC-03a; REV-03). `eic` W3, `methodology` W2, `domain` W1 ("A grade prevista varia só a fração exposta, não a magnitude") e pergunta 2 do mesmo assento. Em silêncio: `perspective`. O `da` soma-se em M2 ("A porta é, na prática, um parâmetro livre").

**Achados corroborados por dois assentos (abaixo do limiar de consenso):**

- O efeito plausível de 80 gramas estima outro contraste e entra sem desconto (SC-03b): `methodology` W2, `domain` W1; `da` M2.
- O parâmetro formal não é o que o coeficiente recupera (SC-05; REV-05): `eic` W4, `methodology` W3.
- "Pico sazonal" sem critério (SC-04b): `eic` W3, `methodology` W6.
- Regra de classificação de A_m em aberto ("ao menos um ano") (SC-04c): `methodology` W6, `perspective` W1.
- Silêncio do registro lido como ausência de voo (SC-04e): `perspective` W1, `methodology` W6.
- O perfil químico vem de análises de água (SC-18; REV-18): `domain` W3, `perspective` W4.
- Falta registro público datado do plano (SC-07b): `methodology` W1, `perspective` W9, e `eic` W6 quanto ao depósito junto à banca. A gravidade é disputada; ver a Disagreement 2.

Os demais achados são de um só assento. Eles foram mantidos e avaliados contra a própria âncora, sem rótulo de consenso.

### Points of Disagreement

As divergências ficam visíveis. Nenhuma foi resolvida por média.

**Disagreement 1: recomendação geral**
- **`eic` e `methodology`**: Major Revision. `eic`: "a banca precisa ver a versão reparada antes de assinar". `methodology`: "O problema que impede aceitar o desenho como está é o estatuto confirmatório".
- **`domain` e `perspective`**: Minor Revision. `domain`: "o achado principal se resolve reescrevendo a regra de decisão e o cálculo de poder, sem dado novo". `perspective`: "A revisão pedida é textual e delimitada".
- **Disagreement type**: Perspective difference. Os quatro concordam que o reparo é de texto e de regra; divergem em se a banca precisa ver a versão reparada.
- **Editor's Resolution**: a decisão não sai desta contagem. Sob contrato, decide o motor: F2 disparou com D1, D3 e D6 em block.
- **Resolution Rationale**: `editorial_decision_standards.md` §0. A divergência fica registrada e não foi convertida em voto.

**Disagreement 2: gravidade das rodadas exploratórias (REV-07) — SPLIT de severidade**
- **`methodology` W1 (Major, gatilho do bloqueio em D1)**: as escolhas dadas como fixadas foram fixadas depois de o desfecho do pós-lei ter sido cruzado com a exposição, e o leitor não distingue o caso limpo do contaminado. `da` M1 (Major) diz o mesmo.
- **`eic`**: conta a revelação como ponto forte (S3) e levanta só a sua visibilidade (W9, Minor) e a posição da qualificação (W6, Minor). **`perspective`** W9 (Minor): o plano só o autor pode datar.
- **Em silêncio**: `domain`.
- **Disagreement type**: Severity disagreement.
- **Editor's Resolution**: o item fica `must_fix` com a severidade Major transportada do achado condutor (`methodology` W1).
- **Resolution Rationale**: evidência e competência. O manuscrito dá a cronologia que sustenta o achado ("Ele não é escolhido pelos dados." e, adiante, "a exposição sazonal já foi cruzada com o desfecho do pós-lei"), e o estatuto confirmatório é matéria do assento de metodologia. O ponto forte que `eic` aponta não é negado: a franqueza é o que torna o reparo possível.

**Disagreement 3: o que fazer com um diagnóstico de identificação desfavorável (REV-12)**
- **`da` M3**: a regra de decisão deve declarar a consequência quando a identificação falha (pré-tendência, tratamento falso); hoje um resultado pode ser rotulado confirmatório apesar disso.
- **`methodology` W7**: concorda que não há consequência prevista, mas recomenda relato conjunto e não portão ("condicionar o teste principal a um pré-teste tem custos próprios, e por isso sugiro relato conjunto em vez de portão"; conhecimento do parecerista, não conferido).
- **Disagreement type**: Direction disagreement (remédios incompatíveis para o mesmo problema).
- **Editor's Resolution**: não resolvida no mérito. O autor deve pré-especificar uma das duas formas e justificar a escolha.
- **Resolution Rationale**: autonomia do autor. Os dois assentos concordam na existência do problema; a escolha entre portão e relato conjunto é decisão de método do pesquisador com o orientador. Para a chuva por grupo os dois convergem (REV-11).

**Disagreement 4: direção do viés do efeito plausível (REV-03)**
- **`domain` W1**: as ressalvas puxam em sentidos opostos (o contraste voo contra nenhum voo é mais amplo que intensivo contra habitual; a menor frequência de ciclos e o desconto do efeito tardio reduzem), "e o texto não diz qual domina".
- **`da` M2**: "Tudo empurra o beta plausível para baixo de 80 vezes a fração". **`methodology` W2**: lista só descontos e alerta para efeito plausível superestimado.
- **Disagreement type**: Existence disagreement sobre uma sub-afirmação (a direção); os três concordam que o valor único não serve.
- **Editor's Resolution**: prevalece a leitura de `domain`: a direção é indeterminada no texto.
- **Resolution Rationale**: evidência. O próprio manuscrito diz que os 80 gramas comparam fumigação intensiva "em comparação com a fumigação habitual" e que "o contraste da lei, entre voo e ausência de voo, não é o do artigo"; essa ressalva não empurra para baixo. O remédio (faixa de magnitude, e regra para quando os cenários discordam) cobre os dois sentidos.

**Disagreement 5: o reparo exige análise nova? (REV-33)**
- **`da` M4**: o projeto deveria trazer já o efeito mínimo detectável calculado com dados anteriores à lei.
- **`eic`, `methodology`, `domain`, `perspective`**: o reparo é de reescrita, "sem dado novo" (`eic`, Summary; `methodology`, Summary; `domain`, Summary; `perspective`, Overall Recommendation). `methodology` W2 pede a definição do efeito detectável, não o número.
- **Disagreement type**: Direction disagreement.
- **Editor's Resolution**: o número fica `should_fix`, marcado como o único item que exige análise nova. A definição do efeito detectável é `must_fix` em REV-03.
- **Resolution Rationale**: nenhum bloqueio depende de M4 (o próprio `da` diz que D3 recebe block "por C1 isoladamente" e que M1 a M4 "não herdam a banda de C1"). O autor decide na triagem; a recusa fica visível.

**Observação sem conflito.** `methodology` W7 diz que o exame de pré-tendência "cobre só o intervalo anterior à referência"; `da` m1 precisa que, com 2011 como base e 2007 a 2010 dentro da referência, o exame fora dela se reduz a 2005 e 2006. As duas leituras são compatíveis com o texto ("2011 como base, de modo que os anos de 2005 a 2010 testam a pré-tendência"); a do `da` é a mais exata.

---

## Decision Rationale *

A decisão é revisão substancial porque três dimensões obrigatórias estão em bloqueio reparável, cada uma por um assento elegível e com gatilho declarado: D1 (`methodology`: a fronteira entre confirmatório e exploratório não é verificável), D3 (`da`: a tese depende de uma premissa não declarada) e D6 (`eic`: a suficiência do que se entrega não é sustentada fora da primeira linha da regra). A condição F2 do contrato dispara e leva a essa ação; nada foi abrandado.

Os nove itens obrigatórios se agrupam em quatro problemas. Primeiro, o rótulo "confirmatório": o texto revela que o desenho já foi rodado com o desfecho do pós-lei e, ao mesmo tempo, afirma independência em relação aos dados (REV-07). Segundo, o que o coeficiente identifica: a premissa de retorno dos voos (REV-32), a separação entre lei e chuva (REV-11), a distância entre parâmetro e coeficiente (REV-05) e a inferência com tratados contíguos (REV-10). Terceiro, a regra de decisão, que é o ponto forte do projeto e o lugar onde ele ainda está aberto: o portão de poder (REV-03) e os casos sem linha (REV-04). Quarto, o contrato com a banca: suficiência por cenário (REV-01) e escopo do documento (REV-06).

Por que não revisão menor, como sinalizam `domain` e `perspective`: porque a conta do contrato não é voto, e porque três bloqueios foram declarados por assentos elegíveis com âncora conferida. Por que não rejeição: nenhum bloqueio é fatal, e os cinco assentos dizem que o reparo é de texto e de regra, sem dado novo. As divergências entre assentos foram arbitradas por evidência do manuscrito ou deixadas, declaradamente, à escolha do autor.

A decisão é sobre um projeto. Nenhum item obrigatório pede estimativa, e o único item que pede análise nova (REV-33) não é obrigatório.

---

## Synthesizer Check of Quoted Passages (CRITICAL and MAJOR findings)

Conferência feita pela síntese contra o `manuscript.txt`: o trecho citado existe e diz o que o parecerista afirma? Esta seção não é o anexo #1002, que a sessão que despacha acrescenta depois.

| Achado | Severidade | Trecho ou ausência citada | Confere? | Ressalva |
|---|---|---|---|---|
| eic W1 | Major | ausência de argumento de suficiência das linhas 2 a 5 | Sim | O parecer diz que a linha 5 é "pelo próprio texto, provável". O texto diz apenas "Não se sabe se os relatórios anteriores ao envio eletrônico foram preservados". "Provável" é inferência do assento. |
| eic W3 | Major | "para uma grade de frações fixada no plano de análise; decide o valor central da grade" | Sim | Nenhuma. |
| eic W4 | Major | "O coeficiente compara, portanto, exposição no início da gestação com exposição no fim" | Sim | Nenhuma. |
| eic W5 | Major | "Essa escolha é objeto de um segundo ensaio da dissertação." | Sim | Nenhuma. O cronograma tem seis bimestres e a célula "Início do segundo ensaio (escolha de instrumento)". |
| methodology W1 | Major | "a exposição sazonal já foi cruzada com o desfecho do pós-lei" | Sim | Nenhuma. A lista de parâmetros que a ratificação ainda pode alterar confere. |
| methodology W2 | Major | "fixada no plano de análise; decide o valor central da grade" | Sim | Nenhuma. |
| methodology W3 | Major | primeira equação (definição de τ) | Sim | O parecer diz que o referencial cita estimativa "imprecisa, não nula" para o terceiro trimestre; o texto diz só "estimativa imprecisa no terceiro". |
| methodology W4 | Major | "Há poucos municípios tratados, contíguos" | Sim | O porquê do achado usa conhecimento externo sobre os procedimentos citados, declarado pelo assento como não conferido. O problema em si (o texto não diz como o procedimento se aplica nem como trata a contiguidade) confere. |
| methodology W5 | Major | "tiver efeito sazonal diferente em municípios irrigados e de sequeiro" | Sim | Nenhuma. |
| methodology W6 | Major | Quadro de regra de decisão, linhas 3 e 5 | Sim | "Cenário que o texto trata como provável" para registros parciais é inferência: o texto fala em preservação incerta e em envio eletrônico só a partir de 2021. |
| domain W1 | Major | "O efeito plausível é o da especificação principal do análogo equatoriano, cerca de 80 gramas, multiplicado pela fração de nascimentos exposta" | Sim | Nenhuma. As três ressalvas (a), (b) e (c) estão no manuscrito. |
| perspective W1 | Major | "Registros mostram ausência de voos no período de referência"; "Contam-se como documentados os voos registrados em ao menos um ano do período de referência" | Sim | Duas. (i) O parecer diz que a exclusão do grupo de comparação "também depende de haver registro"; o texto prevê verificação "nos registros e no Censo de 2006", de modo que a exclusão não depende só dos relatórios. (ii) As afirmações sobre operador privado e arquivamento por superintendência são conhecimento externo declarado e não conferido. |
| da C1 | Critical | "ou não voar desde antes, por causa da seca. O parâmetro, de intenção de tratar, é a média sobre essas versões."; "Contam-se como documentados os voos registrados em ao menos um ano do período de referência." | Sim | "Nem tem evidência prevista" não se sustenta por inteiro; ver a adjudicação. |
| da M1 | Major | "Ele não é escolhido pelos dados."; "a exposição sazonal já foi cruzada com o desfecho do pós-lei" | Sim | O texto oferece também refazer a análise a partir das bases originais, que o achado não menciona; isso não muda o achado. |
| da M2 | Major | "mas a intensidade não foi convertida, e o contraste da lei, entre voo e ausência de voo, não é o do artigo"; "decide o valor central da grade" | Sim | "Tudo empurra para baixo" não se sustenta por inteiro; ver a Disagreement 4. |
| da M3 | Major | "mas não separa por completo a lei do retorno das chuvas"; "Nenhum critério usa o desfecho do pós-lei." | Sim | Nenhuma. |
| da M4 | Major | ausência de valor numérico do efeito mínimo detectável | Sim | O juízo sobre qual ramo da regra é provável é inferência declarada pelo assento (confiança 3). |

**Resultado.** Os dezessete trechos ou ausências conferem. Nenhum achado CRITICAL ou MAJOR cita texto inexistente ou lhe atribui sentido que ele não tem. Seis trazem ressalva de alcance, anotada acima.

**Informação que não está no manuscrito.**

- **Não declarada.** `methodology`, Detailed Comments, Sampling Strategy: "O grupo tratado [...] pode ter de dois a sete municípios; o texto é franco quanto a isso." O manuscrito dá apenas o limite de sete (36 estabelecimentos em 7 dos 184 municípios, Censo de 2006). O "dois" não tem origem no texto, e o texto não é "franco" quanto a um intervalo que não enuncia. Pode ser inferência ou informação de fora do manuscrito. Está em comentário, não em achado com severidade, e não entrou em nenhum item do roteiro.
- **Declarada pelos próprios assentos como conhecimento externo não conferido.** `perspective`: operador privado e arquivamento dos relatórios (W1), mudança da notificação por volta de 2010 e 2011 (W3), produtos usuais contra a sigatoka (W4), cisternas e açudes (W5), completude do campo de idade gestacional no SIM (W6), lei federal de 2016 sobre dispersão aérea (W7), prática de pedidos de acesso à informação (Detailed Comments). `domain`: Diretiva 2009/128/CE e portaria de Davao (W2), ativos típicos da sigatoka (W3), peso fetal no fim da gestação (W4), deposição a distâncias maiores (W6), resultado de Camacho e Mejía e conteúdo de Helfand e House (Detailed Comments). `methodology`: propriedades dos procedimentos de inferência (W4) e custo do pré-teste (W7). Nenhum achado com severidade depende só dessas afirmações; nos itens REV-17, REV-21, REV-25 e REV-26 a parte que depende delas está marcada como opcional ou não verificada.
- **Conta do parecerista.** `methodology` W8 calcula que, sob a estação provisória de fevereiro a maio e janela de nove meses, as coortes de exposição alta nascem de agosto a dezembro e as de referência de março a maio. A conta foi refeita pela síntese sob a mesma convenção e confere.

---

## Reviewer-Suggested References — NOT VERIFIED, not recommended

O assento `domain` sugeriu quatro referências, todas de memória, sem DOI e declaradas "a verificar". Elas **não** são recomendação desta carta, não entram em nenhum critério de aceitação e não devem ser citadas sem conferência. A checagem #1001 é da sessão que despacha.

| Referência como o assento a deu | DOI | Estado |
|---|---|---|
| Pignati, Machado e Cabral (2007), "Acidente rural ampliado: o caso das chuvas de agrotóxicos sobre a cidade de Lucas do Rio Verde - MT" | não informado | não verificada |
| Gunnell e coautores (2007), "The impact of pesticide regulations on suicide in Sri Lanka" | não informado | não verificada |
| Frank (2024), "The economic impacts of ecosystem disruptions: Costs from substituting biological pest control" | não informado | não verificada |
| Skidmore, Sims e Gibbs (2023), "Agricultural intensification and childhood cancer in Brazil" | não informado | não verificada |

O assento `perspective` não sugeriu obra alguma (lista vazia) e deu apenas pistas de busca marcadas `[UNVERIFIED]`.

---

## Required Revisions * (Must Fix)

Nota de leitura: nesta carta, `R1`…`R9` são referências de transporte dos itens obrigatórios (ordem imutável de origem, não ordem de trabalho); os pareceristas são sempre nomeados pelo assento (`eic`, `methodology`, `domain`, `perspective`, `da`). O ID estável de cada item é `REV-nn`.

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source Reviewer | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| R1 (REV-01) | Suficiência como ensaio de dissertação nas linhas 2 a 5 da regra | SC-01 | major | absence: secoes/08-cronograma.tex (Resultados esperados) e secoes/05-metodologia.tex (Seção sec:regra) — expected argumento de que a entrega das linhas 2 a 5 do Quadro de regra de decisão basta como ensaio de dissertação de mestrado; checked resumo, Cap. 1 (Contribuição), Cap. 4, Cap. 5 (sec:regra), Cap. 8 e os quatro apêndices | 4 — competência central: exigência de bancas de mestrado em economia | eic W1 | must_fix | section: Cap. 8, parágrafo Resultados esperados | acceptance_criterion_unmet → section: Cap. 8 — Resultados esperados; Quadro qua:regra |
| R2 (REV-03) | Portão de poder: efeito plausível, grade de frações e efeito mínimo detectável | SC-03a, SC-03b, SC-03c | major | text: secoes/05-metodologia.tex, Seção sec:regra "para uma grade de frações fixada no plano de análise; decide o valor central da grade" | 4 — competência central; o assento não avaliou se o cálculo de poder em si está bem especificado | eic W3 (parte 1); methodology W2; domain W1; da M2 | must_fix | section: Cap. 5, Seção sec:regra e parágrafo de poder da seção de inferência | method_reproducibility_unresolved → section: Cap. 5, Seção sec:regra |
| R3 (REV-04) | Regra de decisão: casos sem linha e critérios não definidos | SC-04a, SC-04b, SC-04c, SC-04d, SC-04e | major | text: secoes/05-metodologia.tex, Seção sec:regra "para uma grade de frações fixada no plano de análise; decide o valor central da grade" | 4 — competência central (eic W3); o assento não avaliou o cálculo de poder | eic W3 (parte 2); eic W7; methodology W6; perspective W1 | must_fix | section: Cap. 5, Seção sec:regra e Quadro qua:regra; Cap. 8, parágrafo Cronograma | acceptance_criterion_unmet → table: Quadro qua:regra |
| R4 (REV-05) | O parâmetro, a pergunta e o objetivo não nomeiam o contraste que o coeficiente identifica | SC-05 | major | text: secoes/05-metodologia.tex, Seção sec:calendario "O coeficiente compara, portanto, exposição no início da gestação com exposição no fim" | 3 — campo adjacente: leitura de coerência, sem descer à derivação (eic W4) | eic W4; methodology W3 | must_fix | section: Cap. 5, primeira seção (definição de τ); Cap. 1 (pergunta); Cap. 4 (objetivo geral); resumo | claim_scope_unsupported → claim: efeito em nível sobre as coortes de exposição alta (τ, pergunta e objetivo geral) |
| R5 (REV-06) | Escopo do documento: segundo ensaio e prazo da dissertação | SC-06 | major | text: secoes/03-referencial.tex, primeira seção "Essa escolha é objeto de um segundo ensaio da dissertação." | 4 — competência central; o assento desconhece o regimento do programa | eic W5 | must_fix | sentence: preâmbulo; Cap. 1; Cap. 3, primeira seção; nota do Quadro qua:cronograma | editorial_conformance_unmet → manuscript: escopo declarado do documento |
| R6 (REV-07) | O estatuto confirmatório depois das rodadas exploratórias declaradas | SC-07a, SC-07b, SC-07c | major [achado condutor: methodology W1; a primeira origem na ordem de assentos (eic W6) é Minor] | text: secoes/05-metodologia.tex, Inferência, poder e plano de análise "a exposição sazonal já foi cruzada com o desfecho do pós-lei" | 5 — núcleo de competência: planos de análise pré-especificados (methodology W1, achado condutor) | eic W6; eic W9; methodology W1; methodology W12; perspective W9 (parte 1); da M1 | must_fix | section: Cap. 5, seção Inferência, poder e plano de análise, e parágrafo Período de referência; uma linha no Cap. 1 | acceptance_criterion_unmet → claim: estatuto confirmatório de H1 |
| R7 (REV-10) | Inferência principal: estatística da interação tripla e contiguidade dos tratados | SC-10 | major | text: secoes/05-metodologia.tex, Inferência, poder e plano de análise "Há poucos municípios tratados, contíguos" | 4 — núcleo de competência: inferência com poucos grupos tratados; o assento não releu os artigos citados | methodology W4 | must_fix | section: Cap. 5, seção Inferência, poder e plano de análise, primeiro parágrafo | method_reproducibility_unresolved → section: Cap. 5, Inferência, poder e plano de análise |
| R8 (REV-11) | Separação entre a lei e o retorno das chuvas: qual especificação decide | SC-11 | major | text: secoes/07-ameacas.tex, A seca "tiver efeito sazonal diferente em municípios irrigados e de sequeiro" | 4 — núcleo de competência: identificação em diferença tripla com confundidor variante no tempo; hidrologia do semiárido fora do assento | methodology W5; da M3 (parte 1) | must_fix | section: Cap. 5, parágrafo Chuva e Seção sec:regra; Cap. 7, parágrafo A seca | interpretive_ambiguity_remains → claim: leitura de β como efeito da lei e não do retorno das chuvas |
| R9 (REV-32) | DA C1: a premissa de que os voos voltariam depois da seca | — | critical | text: secoes/05-metodologia.tex, seções Interferência e versões do tratamento e Regra de decisão "ou não voar desde antes, por causa da seca. O parâmetro, de intenção de tratar, é a média sobre essas versões." | 4 — leitura direta da equação, do quadro de decisão e das ameaças declaradas | da C1 | must_fix | section: Cap. 5, seções Parâmetro-alvo, Interferência e versões do tratamento e sec:regra; Apêndice do diagrama | claim_scope_unsupported → claim: β como efeito da lei de 2019 quando os voos cessaram antes dela |

### Required Item Details

**R1: Suficiência como ensaio de dissertação nas linhas 2 a 5 da regra** (REV-01)
- **Problem**: Suficiência como ensaio de dissertação nas linhas 2 a 5 da regra. Âncora do achado condutor: absence: secoes/08-cronograma.tex (Resultados esperados) e secoes/05-metodologia.tex (Seção sec:regra) — expected argumento de que a entrega das linhas 2 a 5 do Quadro de regra de decisão basta como ensaio de dissertação de mestrado; checked resumo, Cap. 1 (Contribuição), Cap. 4, Cap. 5 (sec:regra), Cap. 8 e os quatro apêndices
- **Source**: eic W1. Consenso: achado de um assento (1/4).
- **Requirement**: Acrescentar, linha a linha do Quadro de regra de decisão, o produto mínimo e a razão pela qual ele basta como ensaio; se alguma linha não basta sozinha, dizê-lo e indicar o que a completa; na linha 5, dizer o que vai além do que as rodadas exploratórias já produziram.
- **Acceptance criteria**: Para cada uma das linhas 2 a 5 do Quadro de regra de decisão, o texto nomeia o produto mínimo e dá ao menos uma razão de suficiência, ou declara que a linha não basta sozinha e diz o que a completa; para a linha 5, diz o que excede as rodadas exploratórias já feitas.
- **Seção do manuscrito**: Cap. 8 (Resultados esperados); Quadro qua:regra (Cap. 5)
- **Exige dado ou análise nova?** Não. Só reescrita.

**R2: Portão de poder: efeito plausível, grade de frações e efeito mínimo detectável** (REV-03)
- **Problem**: Portão de poder: efeito plausível, grade de frações e efeito mínimo detectável. Âncora do achado condutor: text: secoes/05-metodologia.tex, Seção sec:regra "para uma grade de frações fixada no plano de análise; decide o valor central da grade"
- **Source**: eic W3 (parte 1); methodology W2; domain W1; da M2. Consenso: CONSENSUS-3 em SC-03a (eic, methodology, domain; perspective em silêncio); SC-03b corroborado 2/4; SC-03c 1/4; DA M2 soma-se.
- **Requirement**: Fixar no projeto, por regra que não use o desfecho: (a) a grade de frações expostas e o valor que decide, com fonte ou justificativa; (b) a faixa de magnitude individual tomada como efeito plausível, levando à regra as ressalvas que o Cap. 3 já lista (contraste intensivo contra habitual, frequência de ciclos, contraste início contra fim da gestação, intenção de tratar), e o que decide quando os cenários de magnitude discordam; (c) a definição do efeito mínimo detectável: nível, poder alvo, lateralidade e procedimento de inferência sob o qual é calculado.
- **Acceptance criteria**: O texto do projeto traz a grade e o valor decisório com justificativa independente do desfecho; a regra usa faixa de magnitude, ou justifica o valor único de 80 gramas diante das ressalvas do Cap. 3; o efeito mínimo detectável tem nível, poder, lateralidade e procedimento declarados.
- **Seção do manuscrito**: Cap. 5, Seção sec:regra (Regra de decisão) e seção Inferência, poder e plano de análise; Cap. 3 (magnitudes do análogo)
- **Exige dado ou análise nova?** Não. Fixar grade, faixa e definição é reescrita; nenhum número de estimativa própria é pedido aqui (o valor numérico do efeito detectável é REV-33).

**R3: Regra de decisão: casos sem linha e critérios não definidos** (REV-04)
- **Problem**: Regra de decisão: casos sem linha e critérios não definidos. Âncora do achado condutor: text: secoes/05-metodologia.tex, Seção sec:regra "para uma grade de frações fixada no plano de análise; decide o valor central da grade"
- **Source**: eic W3 (parte 2); eic W7; methodology W6; perspective W1. Consenso: CONSENSUS-3 em SC-04a (eic, methodology, perspective; domain em silêncio); SC-04b, SC-04c e SC-04e corroborados 2/4; SC-04d 1/4.
- **Requirement**: Acrescentar linha ou regra de enquadramento para registros parciais, com critério de completude por operador e por ano, e para registros que chegam depois da data-limite, com o estatuto da análise nesse caso; definir pico sazonal por critério numérico sobre os relatórios; escrever a regra de classificação de A_m (cultura, área mínima, número de anos, e a conciliação entre registros que começam em 2008 e o parâmetro de 2007 a 2011); reservar a expressão ausência de voos para série comprovadamente completa e declarar a validação cruzada mínima com regra de discordância.
- **Acceptance criteria**: O Quadro ou regra anexa atribui linha e entrega a registros parciais e a registros tardios; pico sazonal e série completa têm critério verificável nos relatórios, fixado antes de abri-los; a regra de classificação de A_m está escrita; ausência de voos não é usada para série incompleta.
- **Seção do manuscrito**: Cap. 5, Seção sec:regra e Quadro qua:regra; Seção sec:medicao; Cap. 8 (Cronograma)
- **Exige dado ou análise nova?** Não. Só reescrita. Opcional (perspective W1, item ii): pedir no mesmo requerimento a relação de operadores registrados; é ato de coleta, não análise.

**R4: O parâmetro, a pergunta e o objetivo não nomeiam o contraste que o coeficiente identifica** (REV-05)
- **Problem**: O parâmetro, a pergunta e o objetivo não nomeiam o contraste que o coeficiente identifica. Âncora do achado condutor: text: secoes/05-metodologia.tex, Seção sec:calendario "O coeficiente compara, portanto, exposição no início da gestação com exposição no fim"
- **Source**: eic W4; methodology W3. Consenso: corroborado 2/4 (eic, methodology); domain W1(c) e da M2 apoiam o fato de base.
- **Requirement**: Redefinir o estimando como o contraste entre exposição no início e exposição apenas no fim da gestação, ou manter o efeito em nível e declarar a hipótese adicional que o liga ao coeficiente; enunciar como hipótese mantida, não testável, o sinal do efeito da exposição tardia; alinhar pergunta, objetivo geral, resumo e regra de poder a essa definição; trocar onde a prática existia pela formulação datada do Cap. 5.
- **Acceptance criteria**: A definição formal do parâmetro, a pergunta do Cap. 1, o objetivo geral e H1 nomeiam a mesma população e o mesmo contraste; a hipótese sobre a exposição tardia que liga o contraste ao efeito em nível está enunciada como mantida; onde a prática existia não aparece sem data.
- **Seção do manuscrito**: Cap. 5, Parâmetro-alvo e cadeia causal (equação de τ); Cap. 1 (pergunta); Cap. 4 (objetivo geral); resumo; título (opcional)
- **Exige dado ou análise nova?** Não. Só reescrita.

**R5: Escopo do documento: segundo ensaio e prazo da dissertação** (REV-06)
- **Problem**: Escopo do documento: segundo ensaio e prazo da dissertação. Âncora do achado condutor: text: secoes/03-referencial.tex, primeira seção "Essa escolha é objeto de um segundo ensaio da dissertação."
- **Source**: eic W5. Consenso: achado de um assento (1/4).
- **Requirement**: Declarar o escopo do documento. Como ele cobre só o primeiro ensaio, dizê-lo no preâmbulo e na introdução, indicar onde o segundo será apresentado, dizer em uma frase o que o segundo recebe do primeiro nos cenários sem estimativa de efeito, e situar o cronograma em relação ao prazo do curso.
- **Acceptance criteria**: O texto diz se é o projeto da dissertação ou só do primeiro ensaio; sendo só do primeiro, preâmbulo e introdução o dizem e indicam onde o segundo será apresentado; o cronograma situa o prazo do curso ou declara que cobre apenas o primeiro ensaio.
- **Seção do manuscrito**: Preâmbulo; Cap. 1; Cap. 3 (primeira seção); Cap. 8 (Quadro qua:cronograma)
- **Exige dado ou análise nova?** Não. Só reescrita. O caminho alternativo do assento (meia página sobre o segundo ensaio) não se aplica à restrição declarada pelo pesquisador.

**R6: O estatuto confirmatório depois das rodadas exploratórias declaradas** (REV-07)
- **Problem**: O estatuto confirmatório depois das rodadas exploratórias declaradas. Âncora do achado condutor: text: secoes/05-metodologia.tex, Inferência, poder e plano de análise "a exposição sazonal já foi cruzada com o desfecho do pós-lei"
- **Source**: eic W6; eic W9; methodology W1; methodology W12; perspective W9 (parte 1); da M1. Consenso: SPLIT de severidade, arbitrado: methodology Major (gatilho do bloqueio em D1), eic e perspective Minor; domain em silêncio; da M1 Major.
- **Requirement**: Trocar as afirmações de independência (Ele não é escolhido pelos dados; Nenhum critério usa o desfecho do pós-lei) por descrição verificável: o que foi decidido, quando, com que informação à vista, e quais escolhas (período de referência, limiar de exposição alta, exclusão de 2012 e 2019, início do pós-lei, conceito do grupo de comparação) antecederam a rodada de novembro; listar as variantes estimadas nas duas rodadas e, não sendo mostradas as estimativas, dizê-lo e depositar o material com data verificável por terceiro; comprometer o depósito datado do plano antes da estimação confirmatória; fechar por regra que não use o desfecho os parâmetros ainda abertos ou dizer quais já foram variados; pré-especificar como o resultado é rotulado se a classificação medida coincidir com a provisória; dar à informação subseção própria e uma linha no Cap. 1.
- **Acceptance criteria**: O texto lista as variantes já estimadas e separa as escolhas anteriores e posteriores à rodada de novembro; as afirmações de independência em relação aos dados foram trocadas por descrição datada; há compromisso de depósito do plano e do material exploratório com data verificável por terceiro antes da estimação confirmatória; o texto diz como o resultado é rotulado se a classificação medida coincidir com a provisória.
- **Seção do manuscrito**: Cap. 5, Inferência, poder e plano de análise (último parágrafo) e Período de referência; Seção sec:regra; Cap. 1; Cap. 8 (Cronograma)
- **Exige dado ou análise nova?** Não. Reescrita mais um ato de depósito. Nenhuma estimativa precisa entrar no texto: o próprio achado condutor admite a lista de variantes com depósito datado no lugar das estimativas.

**R7: Inferência principal: estatística da interação tripla e contiguidade dos tratados** (REV-10)
- **Problem**: Inferência principal: estatística da interação tripla e contiguidade dos tratados. Âncora do achado condutor: text: secoes/05-metodologia.tex, Inferência, poder e plano de análise "Há poucos municípios tratados, contíguos"
- **Source**: methodology W4. Consenso: achado de um assento (1/4).
- **Requirement**: Descrever a estatística por município à qual o procedimento principal se aplica no teste do coeficiente da interação tripla e como ele trata choques comuns a tratados contíguos; pré-especificar a leitura da conclusão confirmatória se o procedimento principal e a análise de agregado único divergirem; dizer sob qual procedimento o efeito mínimo detectável é calculado. Promover a análise de agregado único a co-principal, usar blocos regionais ou permutação são opções do assento, não exigência.
- **Acceptance criteria**: O texto descreve a estatística por município usada no procedimento principal para o coeficiente da interação tripla, diz como trata a contiguidade dos tratados e pré-especifica a leitura em caso de divergência entre o procedimento principal e o de agregado único.
- **Seção do manuscrito**: Cap. 5, Inferência, poder e plano de análise
- **Exige dado ou análise nova?** Não. Só reescrita. Trocar o procedimento principal é decisão do pesquisador com o orientador e não é pedida.

**R8: Separação entre a lei e o retorno das chuvas: qual especificação decide** (REV-11)
- **Problem**: Separação entre a lei e o retorno das chuvas: qual especificação decide. Âncora do achado condutor: text: secoes/07-ameacas.tex, A seca "tiver efeito sazonal diferente em municípios irrigados e de sequeiro"
- **Source**: methodology W5; da M3 (parte 1). Consenso: achado de um assento entre os quatro (methodology), com da M3 no mesmo ponto.
- **Requirement**: Pré-especificar qual especificação sustenta a conclusão quando a principal (efeito da chuva comum aos grupos) e a de chuva por grupo divergirem, tornando principal a de chuva por grupo ou exigindo concordância em sinal e ordem de grandeza, e declarar o estatuto do resultado nesse caso; dizer o que se conclui se a chuva do pós-lei e a da referência não forem comparáveis. Volume de reservatório, forma não linear e placebo em irrigados sem aeronave são opções do assento.
- **Acceptance criteria**: O texto diz qual das duas especificações de chuva decide a conclusão confirmatória, ou exige a concordância das duas, e declara o estatuto do resultado quando elas divergem.
- **Seção do manuscrito**: Cap. 5 (parágrafo Chuva; Seção sec:regra); Cap. 7 (A seca); Apêndice de especificações (linha Chuva por grupo)
- **Exige dado ou análise nova?** Não no núcleo (só reescrita). As opções do assento (volume de reservatório, placebo em irrigados) exigiriam dado novo e não são pedidas.

**R9: DA C1: a premissa de que os voos voltariam depois da seca** (REV-32)
- **Problem**: DA C1: a premissa de que os voos voltariam depois da seca. Âncora do achado condutor: text: secoes/05-metodologia.tex, seções Interferência e versões do tratamento e Regra de decisão "ou não voar desde antes, por causa da seca. O parâmetro, de intenção de tratar, é a média sobre essas versões."
- **Source**: da C1. Consenso: DA-CRITICAL, VALIDATED no núcleo; nenhum dos quatro assentos levantou a premissa como tal; methodology W5 e eic W4 tocam o mesmo fato.
- **Requirement**: Declarar como hipótese de identificação que, sem a lei, os voos voltariam ao padrão da referência depois da seca, e dizer que evidência a sustentaria (os relatórios pedidos de 2008 a 2024 do Ceará e do Rio Grande do Norte, a que o texto hoje dá papel de cumprimento e de interferência); rever a afirmação de que não voar desde antes é uma versão do tratamento absorvida pela intenção de tratar; acrescentar à regra de decisão o caso voo na referência, nenhum voo nos anos chuvosos imediatamente anteriores à lei, com entrega própria.
- **Acceptance criteria**: A premissa de retorno dos voos consta entre as hipóteses de identificação com a evidência que a sustentaria; a regra de decisão tem linha ou enquadramento para cessação anterior à lei, com entrega declarada; o texto diz que, nesse caso, um coeficiente positivo não distingue o efeito da lei do fim da prática por outra causa.
- **Seção do manuscrito**: Cap. 5 (Parâmetro-alvo; Interferência e versões do tratamento; Seção sec:regra e Quadro qua:regra); Apêndice Do diagrama causal às hipóteses; Cap. 7 (A seca)
- **Exige dado ou análise nova?** Não. Reparo de texto e de regra, como o próprio assento declara.

---

## Suggested Revisions (Should Fix)

Inclui os itens `should_fix` e `consider`. Nenhum deles condiciona a decisão.

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source Reviewer | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| S1 (REV-02) | Coerência do contrato de entrega entre resumo, Cap. 1, Cap. 8 e a linha 5 | SC-02 | minor | text: secoes/08-cronograma.tex, parágrafo Resultados esperados "Nos demais cenários, o ensaio se entrega como medida do alcance da lei e diagnóstico de poder." | 5 — conferência direta entre dois trechos | eic W2; eic W10; eic W11 | should_fix | sentence: Cap. 8 (frase final de Resultados esperados); resumo; Cap. 1 (Contribuição); linha 5 do Quadro qua:regra | interpretive_ambiguity_remains → section: Cap. 8 e Quadro qua:regra, linha 5 |
| S2 (REV-08) | Conceitos centrais usados antes de definidos; siglas não expandidas | SC-08 | minor | text: secoes/apendices.tex, nota do Quadro qua:espec "A quadra chuvosa é tomada, provisoriamente, como fevereiro a maio" | 4 — competência central | eic W8 | should_fix | sentence: fim do Cap. 1 ou início do Cap. 4 | reader_traceability_reduced → manuscript: definições de estação de pulverização, período de referência e forma reduzida estadual |
| S3 (REV-09) | Listas de Minor Issues dos quatro pareceres com lista | — | — | — | — | eic Minor Issues; methodology Minor Issues; domain Minor Issues; perspective Minor Issues | consider | sentence: pontos de forma listados na seção Minor Issues de eic, methodology, domain e perspective | reader_traceability_reduced → manuscript: pontos de forma |
| S4 (REV-12) | Alcance e consequência dos diagnósticos de identificação | SC-12 | minor | text: secoes/05-metodologia.tex, Grupo de comparação "testam a pré-tendência" | 4 — núcleo de competência: diagnósticos de tendências paralelas | methodology W7; da M3 (parte 2); da m1; da m5 | should_fix | sentence: Cap. 5, parágrafo Grupo de comparação e Seção sec:diagnostico | interpretive_ambiguity_remains → section: Cap. 5, Grupo de comparação |
| S5 (REV-13) | Definições que faltam para a equação principal ser única | SC-13 | minor | equation: Eq. eq:ddd (secoes/05-metodologia.tex) — termos k_t × C_{m,a(t)} e a definição de P_t que os alimenta | 4 — núcleo de competência: especificação de efeitos fixos; a conta dos meses é do assento | methodology W8 | should_fix | section: Cap. 5, Seção sec:calendario, ou Apêndice de especificações | method_reproducibility_unresolved → section: Eq. eq:ddd e definição de P_t |
| S6 (REV-14) | Critério de concordância entre análises | SC-14 | minor | text: secoes/05-metodologia.tex, Análises secundárias e triangulação "sinais coincidem e os intervalos se sobrepõem" | 4 — núcleo de competência: triangulação de estimadores | methodology W9; da m2 | should_fix | sentence: Cap. 5, última frase da seção Análises secundárias e triangulação | interpretive_ambiguity_remains → claim: concordância entre a análise principal e as secundárias |
| S7 (REV-15) | Sensibilidade duplamente robusta: hipótese e critério de acionamento | SC-15 | minor | table: Quadro qua:espec (Especificações do desenho de calendário) — linha Duplamente robusto | 3 — campo adjacente: o assento conhece o resultado citado em linhas gerais, não o releu | methodology W10 | consider | sentence: Quadro qua:espec, linha Duplamente robusto; Cap. 5, Grupo de comparação | interpretive_ambiguity_remains → table: Quadro qua:espec, linha Duplamente robusto |
| S8 (REV-16) | Ponderação por nascimentos e definição do estimando | SC-16 | minor | text: secoes/05-metodologia.tex, Desenho principal "Estima-se, com ponderação pelo número de nascimentos" | 4 — núcleo de competência: agregação e ponderação em painéis municipais | methodology W11 | should_fix | sentence: Cap. 5, definição do parâmetro; Apêndice de especificações | interpretive_ambiguity_remains → claim: média por nascimento ou por município no parâmetro |
| S9 (REV-17) | Alegação de lacuna: alcance da busca não descrito | SC-17 | minor | text: secoes/01-introducao.tex "não se localizou, na literatura consultada, avaliação causal dos efeitos dessa resposta" | 3 — o assento conhece a literatura econômica próxima; não atesta a inexistência de avaliação anterior | domain W2 | should_fix | sentence: Cap. 1, segundo parágrafo e Antecedentes | claim_scope_unsupported → claim: ineditismo da avaliação de uma proibição de método |
| S10 (REV-18) | O perfil químico vem de análises de água, não do que o avião aplicava | SC-18 | minor | text: secoes/02-contexto.tex "registra 23 pontos de coleta na Chapada em 2009" | 3 — a leitura do que uma amostra de água identifica é segura; a observação agronômica é de memória do assento | domain W3; perspective W4 | should_fix | sentence: Cap. 2, segundo parágrafo da seção A Chapada do Apodi, a cultura e o químico | claim_scope_unsupported → claim: identificação do produto aplicado por aeronave a partir de análises de água |
| S11 (REV-19) | Janela dos dois primeiros trimestres ancorada em um único estudo | SC-19 | minor | text: secoes/03-referencial.tex "encontram efeito nos dois primeiros trimestres e estimativa imprecisa no terceiro" | 3 — domínio próximo; a caracterização do terceiro trimestre no artigo de origem é a do manuscrito | domain W4 | should_fix | sentence: Cap. 3, terceira regularidade; Cap. 5, limites declarados da Seção sec:calendario | evidence_gap_remains → claim: terceiro trimestre como referência de menor sensibilidade |
| S12 (REV-20) | Peso médio como desfecho confirmatório sem justificativa | SC-20 | minor | absence: secoes/06-dados.tex, parágrafo Desfechos — expected justificativa da escolha do peso médio como desfecho confirmatório diante da concentração na cauda destacada no Capítulo 3; checked Cap. 3 (segunda regularidade), Cap. 4, Cap. 5 (inferência, poder e plano de análise), Cap. 6 e Cap. 7 | 4 — ponto de coerência entre a literatura citada e a escolha de desfecho | domain W5 | should_fix | sentence: Cap. 6, parágrafo Desfechos | interpretive_ambiguity_remains → claim: escolha do peso médio como desfecho confirmatório |
| S13 (REV-21) | Escala da deriva afirmada sem fonte | SC-21 | minor | absence: secoes/01-introducao.tex e secoes/05-metodologia.tex (seção Interferência e versões do tratamento) — expected referência técnica sobre distância e determinantes da deriva em aplicação aérea; checked Cap. 1, Cap. 2, Cap. 3, Cap. 5 e a lista de referências | 3 — área adjacente (agronomia de aplicação) | domain W6 | should_fix | sentence: Cap. 5, seção Interferência e versões do tratamento; Cap. 1, segundo parágrafo | evidence_gap_remains → claim: a deriva opera em escala de centenas de metros |
| S14 (REV-22) | Magnitudes do análogo citadas sem localizador | SC-22 | minor | text: secoes/03-referencial.tex "80 gramas na especificação principal, e de até 150 conforme a exposição" | 4 — prática de citação de magnitudes; o assento não teve acesso à fonte | domain W7 | should_fix | sentence: Cap. 3, primeira regularidade | reader_traceability_reduced → claim: magnitudes de 80 e 150 gramas e de 23 a 32 gramas |
| S15 (REV-23) | Documentação prévia da exposição à deriva afirmada sem citação | SC-23 | minor | text: secoes/02-contexto.tex "onde a exposição da população à deriva foi documentada antes da proibição" | 4 — verificação direta no texto | domain W8 | should_fix | sentence: Cap. 2, primeiro parágrafo da seção A Chapada do Apodi; Cap. 1, primeiro parágrafo | evidence_gap_remains → claim: exposição da população à deriva documentada antes da proibição |
| S16 (REV-24) | Proibição municipal de Limoeiro do Norte dentro do período de referência | SC-24 | minor | text: secoes/06-dados.tex "um levantamento preliminar encontrou uma proibição, em Limoeiro do Norte, de 2009, revogada em 2010" | 4 — leitura da cadeia de datas do próprio manuscrito | perspective W2 | should_fix | sentence: Cap. 5, parágrafo Período de referência | interpretive_ambiguity_remains → section: Cap. 5, Período de referência |
| S17 (REV-25) | Notificações de intoxicação medem também o esforço de notificar | SC-25 | minor | text: secoes/apendices.tex, Quadro Especificações do desenho de calendário, linha Substituição "Notificações de intoxicação ocupacional por agrotóxico agrícola, por município e ano, antes e depois da lei" | 4 — uso rotineiro do sistema de notificação; a data da mudança de norma não foi conferida pelo assento | perspective W3 | should_fix | sentence: Apêndice de fontes, linha SINAN; Apêndice de especificações, linha Substituição | interpretive_ambiguity_remains → table: Quadro qua:espec, linha Substituição (H5) |
| S18 (REV-26) | A exposição pode não acompanhar o mês do voo (água armazenada, resíduo doméstico) | SC-26 | minor | text: secoes/06-dados.tex "O canal hídrico, que exigiria medições de agrotóxicos na água de consumo com localização dos pontos de coleta, não integra a análise confirmatória" | 3 — vigilância da qualidade da água para consumo; magnitude desconhecida para a região | perspective W5 | consider | sentence: Cap. 5, limites declarados da Seção sec:calendario | interpretive_ambiguity_remains → claim: a exposição gestacional concentra-se nos meses de aplicação |
| S19 (REV-27) | Desfecho composto: regra de alocação do óbito fetal à coorte | SC-27 | minor | text: secoes/06-dados.tex "a proporção de gestações registradas que terminam em nascido vivo com 2.500 gramas ou mais" | 4 — epidemiologia perinatal com SIM e SINASC | perspective W6 | consider | sentence: Cap. 6, parágrafo Desfechos | method_reproducibility_unresolved → claim: alocação do óbito fetal à coorte no desfecho composto |
| S20 (REV-28) | O § 2º (controle vetorial por aeronave) aparece no contexto e some do desenho | SC-28 | minor | absence: secoes/05-metodologia.tex e secoes/06-dados.tex — expected delimitação do alcance do § 2º do art. 28-B (controle vetorial por aeronave) no escopo ou nas versões do tratamento; checked Cap. 2, Cap. 5, Cap. 6 (parágrafo Escopo), Cap. 7 e os apêndices de fontes, ameaças, especificações, cronologia e diagrama | 3 — a pergunta é do campo do assento; a resposta factual não foi verificada | perspective W7 | should_fix | sentence: Cap. 6, parágrafo Escopo | claim_scope_unsupported → claim: definição de município tratado diante do § 2º do art. 28-B |
| S21 (REV-29) | Sigilo: identificação indireta de operador pela medida municipal e mensal | SC-29 | minor | text: secoes/06-dados.tex "nenhum resultado será divulgado com identificação de empresa ou pessoa" | 4 — prática de pesquisa com registros de fiscalização; o assento declara não ser jurista | perspective W8 | should_fix | sentence: Cap. 6, parágrafos Reprodutibilidade e sigilo e Aspectos éticos | reporting_requirement_unmet → section: Cap. 6, Aspectos éticos |
| S22 (REV-30) | Alcance do que o ensaio informa à decisão pública | SC-30 | minor | text: secoes/05-metodologia.tex "Os planos são versionados em repositório, sem pré-registro público" | 3 — comunicação de evidência em vigilância | perspective W9 (parte 2); da m3 | should_fix | sentence: Cap. 1, Justificativa | claim_scope_unsupported → claim: o resultado informa a decisão de manter, relaxar ou substituir a lei |
| S23 (REV-31) | Fontes primárias disponíveis substituídas por secundárias; lei de 2009 sem referência | SC-31 | minor | absence: lista de referências (projeto.bbl) — expected entrada para a Lei municipal nº 1.478/2009 de Limoeiro do Norte; checked todas as entradas da lista e as citações do Cap. 2, do Cap. 6 e do Apêndice de cronologia | 4 — conferência direta da lista de referências do manuscrito | perspective W10 | should_fix | sentence: lista de referências; Apêndice de cronologia | reader_traceability_reduced → manuscript: lista de referências e Quadro qua:cronologia |
| S24 (REV-33) | DA M4: a viabilidade do ramo confirmatório não tem número | — | major | absence: secoes/05-metodologia.tex, seção Inferência, poder e plano de análise — expected valor numérico do efeito mínimo detectável com dados anteriores à lei e a grade de frações expostas; checked resumo, capítulos 1 a 8, quadro de decisão e apêndices | 3 — a ausência é verificável; o juízo sobre qual ramo é provável é inferência do assento a partir das premissas do texto | da M4 | should_fix | re_analysis: efeito mínimo detectável com dados anteriores à lei (Cap. 5, parágrafo de poder) | evidence_gap_remains → claim: viabilidade do ramo confirmatório da regra de decisão |
| S25 (REV-34) | Equação da atenuação apresentada e declarada inaplicável | — | minor [achado menor narrativo do assento da; âncora tipada montada pela síntese a partir do objeto que o achado nomeia] | equation: Eq. eq:atenuacao (secoes/05-metodologia.tex, Análises secundárias e triangulação) | 3 — o assento não conferiu o resultado citado | da m4 | consider | sentence: Cap. 5, Análises secundárias e triangulação, Eq. eq:atenuacao | interpretive_ambiguity_remains → claim: papel da equação θ = VPP × ATT no argumento |

---

## Revision Roadmap *

Total: 34 itens — `must_fix` 9, `should_fix` 20, `consider` 5. Ordem imutável de origem (assento `eic`, `methodology`, `domain`, `perspective`, `da`; depois o número do achado). A ordem não é ordem de trabalho. Itens duplicados entre assentos foram fundidos num só, com todas as origens listadas. Forma de máquina: `revision_roadmap.unbound.json` (mesmos IDs).

| ID | Ref. | Origem (assento e achado) | Severidade transportada | Obrigação | Seção do manuscrito | O que se pede | Dado ou análise nova? |
|---|---|---|---|---|---|---|---|
| REV-01 | R1 | eic W1 | major | must_fix | Cap. 8 (Resultados esperados); Quadro qua:regra (Cap. 5) | Acrescentar, linha a linha do Quadro de regra de decisão, o produto mínimo e a razão pela qual ele basta como ensaio; se alguma linha não basta sozinha, dizê-lo e indicar o que a completa; na linha 5, dizer o que vai além do que as rodadas exploratórias já produziram. | Não. Só reescrita. |
| REV-02 | S1 | eic W2; eic W10; eic W11 | minor | should_fix | Resumo; Cap. 1 (Contribuição); Cap. 8; Quadro qua:regra, linha 5 | Reescrever a frase final de Resultados esperados para remeter ao Quadro linha a linha (na linha 5 não há medida dos voos); dizer de que depende cada camada de contribuição e distinguir efeito não detectável de teste não realizado; dizer, na linha 5, que a população é a dos municípios com aeronave no Censo de 2006 e que o parâmetro do Cap. 5 não é o alvo nesse cenário. | Não. Só reescrita. |
| REV-03 | R2 | eic W3 (parte 1); methodology W2; domain W1; da M2 | major | must_fix | Cap. 5, Seção sec:regra (Regra de decisão) e seção Inferência, poder e plano de análise; Cap. 3 (magnitudes do análogo) | Fixar no projeto, por regra que não use o desfecho: (a) a grade de frações expostas e o valor que decide, com fonte ou justificativa; (b) a faixa de magnitude individual tomada como efeito plausível, levando à regra as ressalvas que o Cap. 3 já lista (contraste intensivo contra habitual, frequência de ciclos, contraste início contra fim da gestação, intenção de tratar), e o que decide quando os cenários de magnitude discordam; (c) a definição do efeito mínimo detectável: nível, poder alvo, lateralidade e procedimento de inferência sob o qual é calculado. | Não. Fixar grade, faixa e definição é reescrita; nenhum número de estimativa própria é pedido aqui (o valor numérico do efeito detectável é REV-33). |
| REV-04 | R3 | eic W3 (parte 2); eic W7; methodology W6; perspective W1 | major | must_fix | Cap. 5, Seção sec:regra e Quadro qua:regra; Seção sec:medicao; Cap. 8 (Cronograma) | Acrescentar linha ou regra de enquadramento para registros parciais, com critério de completude por operador e por ano, e para registros que chegam depois da data-limite, com o estatuto da análise nesse caso; definir pico sazonal por critério numérico sobre os relatórios; escrever a regra de classificação de A_m (cultura, área mínima, número de anos, e a conciliação entre registros que começam em 2008 e o parâmetro de 2007 a 2011); reservar a expressão ausência de voos para série comprovadamente completa e declarar a validação cruzada mínima com regra de discordância. | Não. Só reescrita. Opcional (perspective W1, item ii): pedir no mesmo requerimento a relação de operadores registrados; é ato de coleta, não análise. |
| REV-05 | R4 | eic W4; methodology W3 | major | must_fix | Cap. 5, Parâmetro-alvo e cadeia causal (equação de τ); Cap. 1 (pergunta); Cap. 4 (objetivo geral); resumo; título (opcional) | Redefinir o estimando como o contraste entre exposição no início e exposição apenas no fim da gestação, ou manter o efeito em nível e declarar a hipótese adicional que o liga ao coeficiente; enunciar como hipótese mantida, não testável, o sinal do efeito da exposição tardia; alinhar pergunta, objetivo geral, resumo e regra de poder a essa definição; trocar onde a prática existia pela formulação datada do Cap. 5. | Não. Só reescrita. |
| REV-06 | R5 | eic W5 | major | must_fix | Preâmbulo; Cap. 1; Cap. 3 (primeira seção); Cap. 8 (Quadro qua:cronograma) | Declarar o escopo do documento. Como ele cobre só o primeiro ensaio, dizê-lo no preâmbulo e na introdução, indicar onde o segundo será apresentado, dizer em uma frase o que o segundo recebe do primeiro nos cenários sem estimativa de efeito, e situar o cronograma em relação ao prazo do curso. | Não. Só reescrita. O caminho alternativo do assento (meia página sobre o segundo ensaio) não se aplica à restrição declarada pelo pesquisador. |
| REV-07 | R6 | eic W6; eic W9; methodology W1; methodology W12; perspective W9 (parte 1); da M1 | major | must_fix | Cap. 5, Inferência, poder e plano de análise (último parágrafo) e Período de referência; Seção sec:regra; Cap. 1; Cap. 8 (Cronograma) | Trocar as afirmações de independência (Ele não é escolhido pelos dados; Nenhum critério usa o desfecho do pós-lei) por descrição verificável: o que foi decidido, quando, com que informação à vista, e quais escolhas (período de referência, limiar de exposição alta, exclusão de 2012 e 2019, início do pós-lei, conceito do grupo de comparação) antecederam a rodada de novembro; listar as variantes estimadas nas duas rodadas e, não sendo mostradas as estimativas, dizê-lo e depositar o material com data verificável por terceiro; comprometer o depósito datado do plano antes da estimação confirmatória; fechar por regra que não use o desfecho os parâmetros ainda abertos ou dizer quais já foram variados; pré-especificar como o resultado é rotulado se a classificação medida coincidir com a provisória; dar à informação subseção própria e uma linha no Cap. 1. | Não. Reescrita mais um ato de depósito. Nenhuma estimativa precisa entrar no texto: o próprio achado condutor admite a lista de variantes com depósito datado no lugar das estimativas. |
| REV-08 | S2 | eic W8 | minor | should_fix | Cap. 1 ou Cap. 4; resumo; primeira ocorrência de cada sigla | Um parágrafo de definições (estação provisória, período de referência, coortes, grupos) e expansão das siglas na primeira ocorrência. | Não. Só reescrita. |
| REV-09 | S3 | eic Minor Issues; methodology Minor Issues; domain Minor Issues; perspective Minor Issues | — | consider | Vários (ver seção Minor Issues de cada parecer) | Percorrer as quatro listas de Minor Issues e decidir item a item; entre eles: duração da janela gestacional fixa, mês truncado de dezembro de 2024, data de calendário da data-limite, papel das notificações de arboviroses, linha em branco no Quadro de especificações. | Não. |
| REV-10 | R7 | methodology W4 | major | must_fix | Cap. 5, Inferência, poder e plano de análise | Descrever a estatística por município à qual o procedimento principal se aplica no teste do coeficiente da interação tripla e como ele trata choques comuns a tratados contíguos; pré-especificar a leitura da conclusão confirmatória se o procedimento principal e a análise de agregado único divergirem; dizer sob qual procedimento o efeito mínimo detectável é calculado. Promover a análise de agregado único a co-principal, usar blocos regionais ou permutação são opções do assento, não exigência. | Não. Só reescrita. Trocar o procedimento principal é decisão do pesquisador com o orientador e não é pedida. |
| REV-11 | R8 | methodology W5; da M3 (parte 1) | major | must_fix | Cap. 5 (parágrafo Chuva; Seção sec:regra); Cap. 7 (A seca); Apêndice de especificações (linha Chuva por grupo) | Pré-especificar qual especificação sustenta a conclusão quando a principal (efeito da chuva comum aos grupos) e a de chuva por grupo divergirem, tornando principal a de chuva por grupo ou exigindo concordância em sinal e ordem de grandeza, e declarar o estatuto do resultado nesse caso; dizer o que se conclui se a chuva do pós-lei e a da referência não forem comparáveis. Volume de reservatório, forma não linear e placebo em irrigados sem aeronave são opções do assento. | Não no núcleo (só reescrita). As opções do assento (volume de reservatório, placebo em irrigados) exigiriam dado novo e não são pedidas. |
| REV-12 | S4 | methodology W7; da M3 (parte 2); da m1; da m5 | minor | should_fix | Cap. 5 (Grupo de comparação; Seção sec:diagnostico; Seção sec:regra); Apêndice de especificações | Reformular testam como examinam e dizer o alcance (com 2011 como base, o exame fora da referência cobre 2005 e 2006); dizer o que o tratamento falso mostra e o que não mostra; pré-especificar como um estudo de evento ou tratamento falso desfavorável entra no relato (intervalo de sensibilidade junto ao coeficiente) ou na regra (mudança de estatuto). A forma é escolha do autor; uma das duas deve estar escrita. | Não. Só reescrita. |
| REV-13 | S5 | methodology W8 | minor | should_fix | Cap. 5, Seção sec:calendario; Apêndice de especificações (pode ir em apêndice) | Dar a fórmula de P_t com a duração da janela e uma tabela mês de nascimento por grupo sob a estação provisória; indexar a chuva pela quadra a que a coorte foi exposta; declarar que a estação é única ou reescrever a equação com os termos adicionais; dizer onde ficam os vizinhos imediatos e o mês truncado de dezembro de 2024. | Não. Só reescrita; cabe em apêndice. |
| REV-14 | S6 | methodology W9; da m2 | minor | should_fix | Cap. 5, Análises secundárias e triangulação | Tratar a comparação como descritiva, sem rótulo de concordância, dizendo o valor esperado de cada análise secundária sob o efeito principal; ou adotar critério de equivalência com margem declarada. | Não. Só reescrita. |
| REV-15 | S7 | methodology W10 | minor | consider | Apêndice de especificações; Cap. 5 (Grupo de comparação) | Fixar o número mínimo de tratados que aciona o estimador, declarar a hipótese condicional de cada versão e dizer por que a ressalva citada no Cap. 3 não atinge a especificação principal, ou em que medida atinge. | Não. |
| REV-16 | S8 | methodology W11 | minor | should_fix | Cap. 5 (parâmetro; Desenho principal); Apêndice de especificações | Declarar o estimando como média por nascimento; prever no quadro de especificações a versão sem pesos e a exclusão de um tratado por vez; usar pesos do período de referência. | Não. Só reescrita (as versões adicionais são linhas do plano, não análise agora). |
| REV-17 | S9 | domain W2 | minor | should_fix | Cap. 1 (abertura; Antecedentes; Justificativa) | Acrescentar uma frase com o protocolo e a data da busca e uniformizar as formulações mais fortes (O que nenhum desses trabalhos oferece; não se conhece estimativa causal) com a forma cautelosa. O parágrafo sobre precedentes regulatórios em outros países é opcional, e as pistas do assento são declaradas não conferidas [FIELD-NORM UNVERIFIED]. | Não. Uma frase. Nenhuma das pistas do assento deve entrar sem conferência. |
| REV-18 | S10 | domain W3; perspective W4 | minor | should_fix | Cap. 2, seção A Chapada do Apodi, a cultura e o químico | Redigir a tabela como evidência de contaminação da água na região, e não da calda aérea; citar a fonte primária com página; remeter a identificação do produto aéreo ao campo produto dos relatórios mensais. | Não. Reescrita e conferência de uma fonte já citada. |
| REV-19 | S11 | domain W4 | minor | should_fix | Cap. 3 (terceira regularidade); Cap. 5 (Seção sec:calendario) | Dizer que a janela vem do análogo e não de mecanismo estabelecido para os produtos em questão; reportar do artigo de origem as estimativas por trimestre com intervalo (número da literatura, não estimativa própria), ou declarar que não se encontrou referência sobre período sensível. | Não. Reescrita e consulta ao artigo já citado. |
| REV-20 | S12 | domain W5 | minor | should_fix | Cap. 6, parágrafo Desfechos | Duas frases que justifiquem a média como desfecho confirmatório e digam como a concentração na cauda será lida nos exploratórios. O desfecho de cauda construído no nível individual é opção do assento. | Não. Só reescrita. |
| REV-21 | S13 | domain W6 | minor | should_fix | Cap. 1; Cap. 5 (Interferência e versões do tratamento) | Citar fonte técnica ou regulatória para a escala da deriva, ou enfraquecer a frase. | Não. |
| REV-22 | S14 | domain W7 | minor | should_fix | Cap. 3 (primeira regularidade) | Indicar tabela e coluna da versão publicada para cada número do análogo equatoriano e para a faixa de 23 a 32 gramas. | Não. Conferência de fonte já citada. |
| REV-23 | S15 | domain W8 | minor | should_fix | Cap. 2; Cap. 1 (abertura) | Citar a fonte com página e dizer o que foi documentado (resíduo em água, relato de moradores, medição de deposição, biomonitoramento). | Não. |
| REV-24 | S16 | perspective W2 | minor | should_fix | Cap. 5 (Período de referência); Cap. 6 (Exposição) | Dizer no Cap. 5 como entram as coortes com início de gestação na estação de 2010 naquele município (excluídas, ou mantidas com sensibilidade) e prever o uso dos relatórios de 2009 e 2010, se vierem, como verificação do cumprimento da lei municipal. | Não. Só reescrita. |
| REV-25 | S17 | perspective W3 | minor | should_fix | Apêndice de fontes (linha SINAN); Apêndice de especificações (linha Substituição); Cap. 5 (cadeia causal) | Declarar a limitação (subnotificação e dependência do esforço local) no quadro de fontes e na linha da especificação, e dizer quais elos da cadeia ficam sem medida. Internações e receituário pós-lei como indicadores paralelos são opção do assento. | Não no núcleo. Os indicadores paralelos sugeridos seriam dado novo e não são pedidos. |
| REV-26 | S18 | perspective W5 | minor | consider | Cap. 5 (Seção sec:calendario, limites declarados) | Acrescentar a defasagem da exposição por água armazenada e resíduo doméstico à lista de limites do contraste, com o sinal do viés (atenuação). | Não. A heterogeneidade por cobertura de cisternas sugerida pelo assento seria dado novo e não é pedida. |
| REV-27 | S19 | perspective W6 | minor | consider | Cap. 6 (Desfechos) | Declarar a regra de alocação do óbito fetal à coorte (pela idade gestacional registrada quando houver, com sensibilidade para os registros sem o campo). | Não. |
| REV-28 | S20 | perspective W7 | minor | should_fix | Cap. 6 (Escopo) | Uma frase no parágrafo de escopo, com a fonte consultada, dizendo se houve ou não dispersão aérea para controle de vetores no Ceará antes de 2019, e o papel exato das notificações de arboviroses na análise. | Não é análise; exige uma consulta factual a fonte oficial. |
| REV-29 | S21 | perspective W8 | minor | should_fix | Cap. 6 (Reprodutibilidade e sigilo; Aspectos éticos); Cap. 8 (entrega iii) | Fixar limiar de supressão e nível de agregação em que a medida de voos será divulgada; descrever guarda, acesso e descarte dos documentos recebidos; dizer se o enquadramento ético foi conferido também para os registros identificados. | Não. |
| REV-30 | S22 | perspective W9 (parte 2); da m3 | minor | should_fix | Cap. 1 (Justificativa); Cap. 5 (Seção sec:regra) | Acrescentar à Justificativa uma frase de alcance: o ensaio informa um desfecho, por uma via, em nível municipal, e não mede os demais danos alegados. | Não. |
| REV-31 | S23 | perspective W10 | minor | should_fix | Lista de referências; Apêndice de cronologia; Cap. 2 | Incluir a lei municipal de 2009 na lista; citar a tramitação oficial para a votação de 2018; apoiar a datação da seca nas séries de precipitação; localizar e registrar o número da ação de 2011. | Não é análise; exige localizar fontes. |
| REV-32 | R9 | da C1 | critical | must_fix | Cap. 5 (Parâmetro-alvo; Interferência e versões do tratamento; Seção sec:regra e Quadro qua:regra); Apêndice Do diagrama causal às hipóteses; Cap. 7 (A seca) | Declarar como hipótese de identificação que, sem a lei, os voos voltariam ao padrão da referência depois da seca, e dizer que evidência a sustentaria (os relatórios pedidos de 2008 a 2024 do Ceará e do Rio Grande do Norte, a que o texto hoje dá papel de cumprimento e de interferência); rever a afirmação de que não voar desde antes é uma versão do tratamento absorvida pela intenção de tratar; acrescentar à regra de decisão o caso voo na referência, nenhum voo nos anos chuvosos imediatamente anteriores à lei, com entrega própria. | Não. Reparo de texto e de regra, como o próprio assento declara. |
| REV-33 | S24 | da M4 | major | should_fix | Cap. 5, Inferência, poder e plano de análise | Reportar o efeito mínimo detectável calculado só com dados anteriores à lei, ao lado da grade de frações expostas. A parte da grade já está em REV-03. | SIM: exige análise nova e põe um número calculado no texto, o que contraria a restrição declarada pelo pesquisador. Decisão do autor na triagem. |
| REV-34 | S25 | da m4 | minor | consider | Cap. 5, Análises secundárias e triangulação | Dar função à equação no argumento ou retirá-la. | Não. Retirar a equação libera espaço. |

### Source-traceability checklist

- [ ] R1 (REV-01) — obligation `must_fix`: Suficiência como ensaio de dissertação nas linhas 2 a 5 da regra
- [ ] S1 (REV-02) — obligation `should_fix`: Coerência do contrato de entrega entre resumo, Cap. 1, Cap. 8 e a linha 5
- [ ] R2 (REV-03) — obligation `must_fix`: Portão de poder: efeito plausível, grade de frações e efeito mínimo detectável
- [ ] R3 (REV-04) — obligation `must_fix`: Regra de decisão: casos sem linha e critérios não definidos
- [ ] R4 (REV-05) — obligation `must_fix`: O parâmetro, a pergunta e o objetivo não nomeiam o contraste que o coeficiente identifica
- [ ] R5 (REV-06) — obligation `must_fix`: Escopo do documento: segundo ensaio e prazo da dissertação
- [ ] R6 (REV-07) — obligation `must_fix`: O estatuto confirmatório depois das rodadas exploratórias declaradas
- [ ] S2 (REV-08) — obligation `should_fix`: Conceitos centrais usados antes de definidos; siglas não expandidas
- [ ] S3 (REV-09) — obligation `consider`: Listas de Minor Issues dos quatro pareceres com lista
- [ ] R7 (REV-10) — obligation `must_fix`: Inferência principal: estatística da interação tripla e contiguidade dos tratados
- [ ] R8 (REV-11) — obligation `must_fix`: Separação entre a lei e o retorno das chuvas: qual especificação decide
- [ ] S4 (REV-12) — obligation `should_fix`: Alcance e consequência dos diagnósticos de identificação
- [ ] S5 (REV-13) — obligation `should_fix`: Definições que faltam para a equação principal ser única
- [ ] S6 (REV-14) — obligation `should_fix`: Critério de concordância entre análises
- [ ] S7 (REV-15) — obligation `consider`: Sensibilidade duplamente robusta: hipótese e critério de acionamento
- [ ] S8 (REV-16) — obligation `should_fix`: Ponderação por nascimentos e definição do estimando
- [ ] S9 (REV-17) — obligation `should_fix`: Alegação de lacuna: alcance da busca não descrito
- [ ] S10 (REV-18) — obligation `should_fix`: O perfil químico vem de análises de água, não do que o avião aplicava
- [ ] S11 (REV-19) — obligation `should_fix`: Janela dos dois primeiros trimestres ancorada em um único estudo
- [ ] S12 (REV-20) — obligation `should_fix`: Peso médio como desfecho confirmatório sem justificativa
- [ ] S13 (REV-21) — obligation `should_fix`: Escala da deriva afirmada sem fonte
- [ ] S14 (REV-22) — obligation `should_fix`: Magnitudes do análogo citadas sem localizador
- [ ] S15 (REV-23) — obligation `should_fix`: Documentação prévia da exposição à deriva afirmada sem citação
- [ ] S16 (REV-24) — obligation `should_fix`: Proibição municipal de Limoeiro do Norte dentro do período de referência
- [ ] S17 (REV-25) — obligation `should_fix`: Notificações de intoxicação medem também o esforço de notificar
- [ ] S18 (REV-26) — obligation `consider`: A exposição pode não acompanhar o mês do voo (água armazenada, resíduo doméstico)
- [ ] S19 (REV-27) — obligation `consider`: Desfecho composto: regra de alocação do óbito fetal à coorte
- [ ] S20 (REV-28) — obligation `should_fix`: O § 2º (controle vetorial por aeronave) aparece no contexto e some do desenho
- [ ] S21 (REV-29) — obligation `should_fix`: Sigilo: identificação indireta de operador pela medida municipal e mensal
- [ ] S22 (REV-30) — obligation `should_fix`: Alcance do que o ensaio informa à decisão pública
- [ ] S23 (REV-31) — obligation `should_fix`: Fontes primárias disponíveis substituídas por secundárias; lei de 2009 sem referência
- [ ] R9 (REV-32) — obligation `must_fix`: DA C1: a premissa de que os voos voltariam depois da seca
- [ ] S24 (REV-33) — obligation `should_fix`: DA M4: a viabilidade do ramo confirmatório não tem número
- [ ] S25 (REV-34) — obligation `consider`: Equação da atenuação apresentada e declarada inaplicável

### Sub-claim inventory (itens com mais de uma sub-afirmação ou mais de um assento)

Posições: `raised`, `corroborated`, `not-mentioned`, `disputed`. Severidade e confiança são as do parecer, sem reavaliação. Nos itens de um só achado, o sub-claim é o próprio achado (`SC-nn` do item `REV-nn`).

| sub_claim_id | Sub-afirmação | eic | methodology | domain | perspective | da (fora da contagem) | Disposição |
|---|---|---|---|---|---|---|---|
| SC-03a | Grade de frações e valor decisório não fixados nem com fonte | raised (W3, Major, 4) | raised (W2, Major, 4) | raised (W1, Major, 4) | not-mentioned | M2 (Major, 4) | CONSENSUS-3 |
| SC-03b | Os 80 gramas estimam outro contraste e entram sem desconto | not-mentioned | raised (W2) | raised (W1) | not-mentioned | M2 | corroborado 2/4; direção do viés em disputa (Disagreement 4) |
| SC-03c | Efeito mínimo detectável sem nível, poder, lateralidade e procedimento | not-mentioned | raised (W2) | not-mentioned | not-mentioned | — | 1/4 |
| SC-04a | Sem linha para registros parciais; sem critério de completude | raised (W3, Major, 4) | raised (W6, Major, 4) | not-mentioned | raised (W1, Major, 4) | — | CONSENSUS-3 |
| SC-04b | "Pico sazonal" sem critério | raised (W3) | raised (W6) | not-mentioned | not-mentioned | — | corroborado 2/4 |
| SC-04c | Regra de classificação de A_m em aberto | not-mentioned | raised (W6) | not-mentioned | raised (W1) | C1 toca ("um único ano") | corroborado 2/4 |
| SC-04d | Estatuto da análise com registros que chegam depois da data-limite | raised (W3, W7 Minor, 4) | not-mentioned | not-mentioned | not-mentioned | — | 1/4 |
| SC-04e | Silêncio do registro lido como ausência de voo | not-mentioned | raised (W6) | not-mentioned | raised (W1) | — | corroborado 2/4 |
| SC-05 | Parâmetro, pergunta e objetivo não nomeiam o contraste que β identifica | raised (W4, Major, 3) | raised (W3, Major, 5) | not-mentioned (W1c usa o mesmo fato) | not-mentioned | M2 usa o mesmo fato | corroborado 2/4 |
| SC-07a | Estatuto confirmatório não verificável; afirmações de independência contraditas pela cronologia | not-mentioned (S3 conta a revelação como ponto forte) | raised (W1 Major, 5; W12 Minor, 5) | not-mentioned | not-mentioned | M1 (Major, 4) | 1/4 mais da M1 |
| SC-07b | Sem registro público datado do plano | raised (W6, Minor, 3) | raised (W1, Major, 5) | not-mentioned | raised (W9, Minor, 3) | M1 | SPLIT de severidade (Disagreement 2) |
| SC-07c | A informação sobre as rodadas está enterrada num parágrafo de inferência | raised (W9, Minor, 4) | not-mentioned | not-mentioned | not-mentioned | — | 1/4 |
| SC-11 | Lei e retorno das chuvas: sem regra para quando as especificações divergem | not-mentioned | raised (W5, Major, 4) | not-mentioned | not-mentioned | M3 (Major, 4) | 1/4 mais da M3 |
| SC-12 | Diagnósticos sem consequência prevista | not-mentioned | raised (W7, Minor, 4) | not-mentioned | not-mentioned | M3, m1, m5 | 1/4 mais da; remédio em disputa (Disagreement 3) |
| SC-14 | Critério de concordância não discrimina | not-mentioned | raised (W9, Minor, 4) | not-mentioned | not-mentioned | m2 | 1/4 mais da m2 |
| SC-18 | Perfil químico inferido de análises de água | not-mentioned | not-mentioned | raised (W3, Minor, 3) | raised (W4, Minor, 3) | — | corroborado 2/4 |
| SC-30 | Alcance do que um desfecho informa à decisão pública | not-mentioned | not-mentioned | not-mentioned | raised (W9, Minor, 3) | m3 | 1/4 mais da m3 |

Os itens REV-32, REV-33 e REV-34 vêm só do assento `da` e não têm sub-claim (`—`). REV-09 reúne as listas de Minor Issues.

### Criterion-bound judgements (escala do contrato, transportada sem conversão)

`judgement_scale: sprint_contract`. Nenhuma nota foi traduzida para outra escala.

| Dimensão | Fonte do critério | eic | methodology | domain | perspective | da |
|---|---|---|---|---|---|---|
| D1 methodology_rigor | contrato, D1 | not_assessed | block (repairable) | not_assessed | not_assessed | not_assessed |
| D2 domain_accuracy | contrato, D2 | not_assessed | not_assessed | warn | not_assessed | not_assessed |
| D3 argumentative_coherence | contrato, D3 | not_assessed | warn | not_assessed | not_assessed | block (repairable) |
| D4 cross_disciplinary_relevance | contrato, D4 | not_assessed | not_assessed | not_assessed | warn | not_assessed |
| D5 writing_and_structure | contrato, D5 | warn | not_assessed | not_assessed | not_assessed | not_assessed |
| D6 venue_fit_and_contribution | contrato, D6 | block (repairable) | not_assessed | not_assessed | not_assessed | not_assessed |

---

## Journal-Supplied Deadline (Optional Transport)

- **Exact deadline from source letter**: NOT PROVIDED
- Nenhum prazo, duração ou estimativa de trabalho foi inferido.

---

## Response Letter Instructions

Responda item a item, pelo ID `REV-nn`, no formato de `templates/revision_response_template.md`.

1. Para cada um dos nove itens `must_fix`: o que mudou e onde (capítulo, seção, quadro).
2. Para cada item `should_fix`: adotado, ou a razão de não adotar. Recusar é permitido e fica visível; não é tratado como falta.
3. Itens `consider`: resposta facultativa.
4. Marque as alterações no texto revisado e dê a correspondência entre trechos antigos e novos.

Três limites que esta carta respeita e que a resposta pode invocar: o documento cobre só o primeiro ensaio; o corpo tem teto de páginas e está sem folga; o texto não traz número de estimativa própria. Nenhum item `must_fix` colide com esses limites. O único item que colide é REV-33 (`should_fix`).

---

## Closing

O painel reconhece, nos cinco pareceres, a qualidade incomum do projeto: o tratamento definido pelo método, a regra de decisão fixada de antemão e a franqueza sobre o que já foi olhado. A revisão pedida não muda o desenho. Ela leva as admissões que o texto já faz até o parâmetro, as hipóteses e a regra de decisão. A versão revisada passa por nova rodada de verificação (Estágio 3'), item a item, contra os critérios de aceitação desta carta.

---

## Appendix: Reviewer Report Summary

Os cinco pareceres completos estão nesta pasta, inalterados: `eic.phase2.md`, `methodology.phase2.md`, `domain.phase2.md`, `perspective.phase2.md`, `da.phase2.md`. As perguntas aos autores e as listas de Minor Issues de cada parecer continuam valendo como leitura do autor; as listas estão reunidas em REV-09.

### Journal-Fit Review Report Summary (`eic`)
- Recommendation: Major Revision | Confidence: 4
- Key Point: o contrato de entrega condicional é o ponto forte e o ponto fraco: fora da primeira linha da regra, a suficiência como dissertação não é argumentada, e a condição que escolhe a linha está em aberto.

### Reviewer 1 (Methodology) Summary
- Recommendation: Major Revision | Confidence: 4
- Key Point: o desenho é cuidadoso, mas o estatuto confirmatório não é verificável depois das rodadas exploratórias declaradas; somam-se o portão de poder, o estimando, a inferência, a chuva e a regra incompleta.

### Reviewer 2 (Domain) Summary
- Recommendation: Minor Revision | Confidence: 3
- Key Point: a disciplina de fonte é rara; a fragilidade é usar um valor único do análogo equatoriano na regra de decisão sem levar a ela as ressalvas de transferência que o próprio texto lista.

### Reviewer 3 (Perspective) Summary
- Recommendation: Minor Revision | Confidence: 4
- Key Point: a regra de decisão lê o silêncio de um registro administrativo de preservação incerta como ausência de voo, sem critério de completude nem validação cruzada.

### Devil's Advocate Summary
- Recommendation: N/A — findings only
- Key Challenge: o coeficiente só é o efeito da lei se os voos fossem voltar depois da seca; essa premissa não é hipótese declarada, e a regra não cobre a cessação anterior à lei (C1, validado no núcleo).
