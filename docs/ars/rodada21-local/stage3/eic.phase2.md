contract_role: eic
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: warn
trigger: "há termos, siglas ou notação usados antes de definidos ou de forma não uniforme"

### D6: venue_fit_and_contribution
score: block
trigger: "o que é entregue não é sustentado como suficiente para o requisito do veículo"
block_class: repairable

## Review Body

### Reviewer Identity
Journal-Fit Reviewer (assento `eic`), configurado pelo Cartão #1 como professor titular de economia aplicada com experiência em bancas de qualificação e defesa e como editor associado. Leitura de quem preside a banca: isto é uma dissertação, cabe no tempo, e o que sai dela em cada desfecho.

Nota de escopo: a chamada é não vinculada (`criteria_binding_unavailable`). Não há veículo confirmado; o veículo usado é o do cartão (banca de programa de pós-graduação em economia). Nada abaixo é alegação de alinhamento a critérios de um veículo confirmado.

### Overall Recommendation
Major Revision (sinal deste assento para a síntese; não é decisão).

### Confidence Score
4. Dentro da minha competência no que toca a adequação, contribuição, cronograma e contrato de entrega. Confiança menor (3) no único achado que desce à relação entre o parâmetro e a equação.

### Calibration Status
`NOT_CALIBRATED`

### Summary Assessment
O manuscrito é um projeto de pesquisa de mestrado, sem estimativa própria, que propõe avaliar o efeito da proibição cearense da pulverização aérea sobre o peso ao nascer por uma diferença tripla de calendário gestacional, com período de referência anterior à seca e uma regra que liga a medição dos voos e o poder ao que será entregue. O objeto é original e oportuno, a delimitação frente à literatura é precisa, e o texto é incomumente franco sobre o que não sabe e sobre o que já olhou nos dados. O ponto forte é o contrato de entrega condicional. O ponto fraco está no mesmo lugar: em quatro das cinco linhas da regra não há teste confirmatório, e o texto não argumenta que o que resta basta como ensaio de dissertação; as condições que escolhem a linha não estão fixadas nem são exaustivas; o segundo ensaio, que completa a dissertação, tem uma frase e uma célula do cronograma; e a pergunta do título e da introdução é mais ampla que o contraste que o desenho estima. Nenhum desses problemas exige dado novo. Todos se reparam por reescrita do contrato de entrega e do cronograma, mas a banca precisa ver a versão reparada antes de assinar. Por isso o bloqueio em D6 é reparável e o sinal é de revisão substancial.

### S1: Entrega condicional fixada antes dos resultados
O projeto não promete um efeito; promete o que entrega em cada estado da medição e do poder, e declara que nenhum critério usa o desfecho do pós-lei. Para uma banca, isso transforma o projeto em algo cujo cumprimento se pode cobrar.
**Evidence Anchor**: `table: Quadro qua:regra (secoes/05-metodologia.tex) — coluna O que o ensaio entrega, cinco linhas`
**Confidence**: 4 — competência central: avaliação de projetos em banca

### S2: Uma única hipótese confirmatória, com estatuto declarado para o resto
A separação entre confirmatório, exploratório e descritivo é dita no Cap. 4, repetida no Cap. 5 e tabulada análise por análise no apêndice de especificações. Um leitor de fora da área sabe qual resultado conta.
**Evidence Anchor**: `text: secoes/05-metodologia.tex, seção de inferência "Há uma única hipótese confirmatória, sobre o peso ao nascer; os demais desfechos e contrastes são exploratórios."`
**Confidence**: 4 — competência central

### S3: Franqueza sobre o que já foi olhado
O texto informa que duas rodadas exploratórias já cruzaram a exposição com o desfecho do pós-lei e tira a consequência (tratados e estação fixados pela medição, análise refeita das bases originais). É a informação que uma banca mais precisa e menos costuma receber.
**Evidence Anchor**: `text: secoes/05-metodologia.tex, seção de inferência "a exposição sazonal já foi cruzada com o desfecho do pós-lei"`
**Confidence**: 4 — competência central

### S4: Originalidade delimitada com precisão
A contribuição de objeto é enunciada contra os antecedentes certos: os estudos de método avaliam a introdução ou a vigência da prática, e o projeto avalia a sua retirada. A alegação de ineditismo vem qualificada ("na literatura consultada"), como deve.
**Evidence Anchor**: `text: secoes/01-introducao.tex, Antecedentes "Nos estudos de método, a pulverização aérea é introduzida ou está em curso; no Ceará ela é retirada"`
**Confidence**: 3 — campo adjacente: não conferi a literatura por fora, só a delimitação que o texto faz

### S5: Relevância prática atual e bem situada
A justificativa liga a pergunta a decisões em curso (constitucionalidade assentada, flexibilização de 2024, nova contestação) e admite que um resultado de não mensurabilidade também informa.
**Evidence Anchor**: `text: secoes/01-introducao.tex, Justificativa "informa os estados que consideram adotar a medida e a decisão de mantê-la"`
**Confidence**: 4 — competência central

### W1: A suficiência como dissertação não é argumentada fora da primeira linha da regra
**Problem**: O Cap. 8 lista o que se entrega (i a iv) e o Quadro de regra de decisão diz o que cada cenário aciona, mas em nenhum lugar o texto sustenta que a entrega das linhas 2 a 5 basta como ensaio de dissertação. Na linha 2 há desenho "reportado como limite, sem teste"; nas linhas 3 e 4, medida e forma reduzida descritiva, "sem estimativa de efeito da pulverização"; na linha 5, o desenho com a classificação de 2006, declarado exploratório, mais o cálculo de poder. A linha 5 é, pelo próprio texto, provável (não se sabe se os relatórios anteriores a 2021 foram preservados) e o seu conteúdo é próximo do que a rodada exploratória de novembro já fez.
**Evidence Anchor**: `absence: secoes/08-cronograma.tex (Resultados esperados) e secoes/05-metodologia.tex (Seção sec:regra) — expected argumento de que a entrega das linhas 2 a 5 do Quadro de regra de decisão basta como ensaio de dissertação de mestrado; checked resumo, Cap. 1 (Contribuição), Cap. 4, Cap. 5 (sec:regra), Cap. 8 e os quatro apêndices`
**Why it matters**: É a pergunta de quem preside a banca. Um projeto que só é dissertação em um de cinco cenários, sem dizer por que os outros quatro também o são, deixa a aprovação dependente de um documento cuja existência o texto declara incerta.
**Suggestion**: Acrescentar ao Cap. 8, linha a linha, o produto mínimo e o argumento de suficiência: o que a medida do alcance da lei acrescenta ao conhecimento por si, o que o diagnóstico de poder ensina a quem vier depois, e o que, na linha 5, vai além do que as rodadas exploratórias já produziram. Se alguma linha não basta sozinha, dizê-lo e indicar o que a completa (por exemplo, peso maior do segundo ensaio).
**Severity**: Major
**Confidence**: 4 — competência central: exigência de bancas de mestrado em economia

### W2: O Cap. 8 e a linha 5 do Quadro não dizem a mesma coisa
**Problem**: O Cap. 8 afirma que, fora do cenário com voos documentados e poder, o ensaio se entrega como medida do alcance da lei e diagnóstico de poder. Na linha 5 do Quadro (registros não obtidos) não há medida alguma: há o desenho com o Censo de 2006, exploratório, e o cálculo de poder. O item (iii) do mesmo capítulo confirma que a medida depende dos registros.
**Evidence Anchor**: `text: secoes/08-cronograma.tex, parágrafo Resultados esperados "Nos demais cenários, o ensaio se entrega como medida do alcance da lei e diagnóstico de poder."`
**Why it matters**: O contrato de entrega tem duas redações, e elas divergem justamente no cenário em que a entrega é menor.
**Suggestion**: Reescrever a frase final do parágrafo para remeter ao Quadro linha a linha, ou repetir no Cap. 8 a coluna de entrega.
**Severity**: Minor
**Confidence**: 5 — conferência direta entre dois trechos

### W3: As condições que escolhem a linha da regra não estão fixadas nem são exaustivas
**Problem**: A fronteira entre a linha 1 (teste confirmatório) e a linha 2 (sem teste) é decidida pelo valor central de uma grade de frações expostas que só será fixada no plano de análise; o projeto não dá a grade nem a fonte da fração (a aproximação pelo Censo de 2022 fica "como extensão"). O texto informa, além disso, que a rodada de novembro já calculou efeito detectável com o período inteiro, de modo que a grade será escolhida por quem já conhece a ordem de grandeza do poder. "Sem pico sazonal" (linha 3) não tem critério. E as linhas não cobrem casos que o próprio texto torna prováveis: registros obtidos só de 2021 em diante (envio eletrônico), registros por município e ano mas não por mês, registros que chegam depois da data-limite.
**Evidence Anchor**: `text: secoes/05-metodologia.tex, Seção sec:regra "para uma grade de frações fixada no plano de análise; decide o valor central da grade"`
**Why it matters**: A regra é o que permite à banca dizer, ao fim, se o projeto foi cumprido. Com a condição decisiva em aberto e casos sem linha, ela ainda não cumpre essa função.
**Suggestion**: Fixar já no projeto a grade e o seu valor central, com a justificativa; definir pico sazonal por um critério numérico sobre os relatórios; acrescentar linhas (ou uma regra de enquadramento) para registros parciais e tardios; declarar que a ratificação com o orientador não altera a grade.
**Severity**: Major
**Confidence**: 4 — competência central; não avaliei se o cálculo de poder em si está bem especificado

### W4: A pergunta anunciada é mais ampla que o contraste estimado
**Problem**: Título, pergunta do Cap. 1 e objetivo geral falam do efeito da proibição sobre o peso ao nascer das coortes com início de gestação na estação, nos municípios onde a prática existia. O parâmetro do Cap. 5 é um efeito em nível sobre essas coortes. O coeficiente que o desenho entrega é a mudança da diferença entre essas coortes e as de referência, que também atravessam a estação, no terceiro trimestre. O corpo reconhece a distância (o coeficiente subestima se a exposição tardia causar dano), mas o reconhecimento não sobe ao parâmetro, ao objetivo, à pergunta nem ao título. Soma-se que "onde a prática existia" convive com a hipótese, tratada como séria, de que os voos estavam suspensos desde 2012.
**Evidence Anchor**: `text: secoes/05-metodologia.tex, Seção sec:calendario "O coeficiente compara, portanto, exposição no início da gestação com exposição no fim"`
**Why it matters**: As quatro formulações (pergunta, objetivo, hipótese, parâmetro) deveriam nomear a mesma população e o mesmo contraste. Só a hipótese confirmatória nomeia o contraste que de fato se estima. Um membro de banca que leia título e objetivo cobrará um efeito que o desenho não promete.
**Suggestion**: Reescrever o parâmetro como o contraste que o coeficiente identifica (efeito diferencial da lei entre exposição no início e no fim da gestação) e alinhar a ele a pergunta e o objetivo geral; ou manter o parâmetro em nível e declarar a hipótese adicional que o liga ao coeficiente. Trocar "onde a prática existia" pela formulação datada que o Cap. 5 usa. Fica para o assento de metodologia julgar a identificação; aqui o achado é de coerência entre as formulações.
**Severity**: Major
**Confidence**: 3 — campo adjacente: leitura de coerência, sem descer à derivação

### W5: O segundo ensaio e o prazo da dissertação não aparecem no plano
**Problem**: O documento é apresentado como requisito do mestrado e trata o trabalho como primeiro de dois ensaios, mas o segundo tem uma frase no Cap. 3 e uma célula no sexto bimestre ("Início do segundo ensaio"). O cronograma termina em doze meses sem defesa, sem a execução do segundo ensaio e sem o prazo do curso. Não se diz se este é o projeto da dissertação ou só do primeiro ensaio, nem o que o segundo ensaio recebe do primeiro nas linhas 3 a 5 da regra, em que não há estimativa de efeito para servir de "insumo parcial".
**Evidence Anchor**: `text: secoes/03-referencial.tex, primeira seção "Essa escolha é objeto de um segundo ensaio da dissertação."`
**Why it matters**: A banca aprova um plano de dissertação. Sem o segundo ensaio e sem o prazo final, não há como julgar se o conjunto cabe no tempo, nem se a dependência entre os ensaios sobrevive aos cenários sem estimativa.
**Suggestion**: Declarar o escopo do documento. Se for o projeto da dissertação, acrescentar meia página sobre o segundo ensaio (pergunta, método, o que usa do primeiro em cada linha da regra) e estender o cronograma até a defesa. Se for só do primeiro ensaio, dizê-lo no preâmbulo e na introdução e indicar onde o segundo será apresentado.
**Severity**: Major
**Confidence**: 4 — competência central; desconheço o regimento do programa, o que limita a confiança

### W6: A qualificação vem depois da análise confirmatória
**Problem**: No cronograma, o plano de análise é ratificado só com o orientador no segundo bimestre, o desenho principal roda nos bimestres 3 e 4, e a qualificação aparece nos bimestres 4 e 5. O texto informa que não há pré-registro público. Se a qualificação é o momento em que a banca examina o desenho, ela o fará com o resultado já conhecido, e qualquer mudança pedida será posterior ao desfecho.
**Evidence Anchor**: `table: Quadro qua:cronograma (secoes/08-cronograma.tex) — linha Redação do ensaio e qualificação marcada nos bimestres 4 e 5, depois da linha Desenho principal nos bimestres 3 e 4`
**Why it matters**: O valor do plano fixado de antemão depende de alguém de fora tê-lo visto antes. A banca seria a testemunha natural.
**Suggestion**: Dizer qual é o papel desta apresentação do projeto em relação à qualificação; depositar o plano de análise com data junto à banca ou à coordenação antes do terceiro bimestre; declarar que pedidos da banca posteriores à análise entram como exploratórios.
**Severity**: Minor
**Confidence**: 3 — depende do calendário do programa, que o texto não informa

### W7: A data-limite dos registros não tem folga e o caso de chegada tardia fica ambíguo
**Problem**: A data-limite dos registros é o fim do terceiro bimestre, e o desenho principal começa no mesmo bimestre; todas as análises (principal, três secundárias, mais de uma dúzia de especificações, quatro procedimentos de inferência) cabem nos bimestres 3 e 4. Se os registros chegarem no fim do prazo, classificação, verificação do pico, adendo ao plano e estimação ficam em um bimestre. Se chegarem depois, o texto diz que entram por adendo, mas não diz se o ensaio passa da linha 5 para a linha 1 depois de já ter rodado o desenho de modo exploratório com o desfecho do pós-lei.
**Evidence Anchor**: `text: secoes/08-cronograma.tex, parágrafo Cronograma "e o que for medido depois entra por adendo datado"`
**Why it matters**: A dependência externa que o texto aponta como incerta é a que tem menos margem no calendário, e a regra não diz o que vale quando ela falha por atraso e não por ausência.
**Suggestion**: Separar no cronograma a espera dos registros da estimação; dizer o estatuto (confirmatório ou exploratório) de uma análise com registros recebidos após a data-limite.
**Severity**: Minor
**Confidence**: 4 — competência central: exequibilidade de cronogramas

### W8: Conceitos centrais usados antes de definidos, e a estação só aparece em nota de apêndice
**Problem**: "Estação de pulverização" organiza a pergunta, o objetivo e a hipótese, mas não é definida no corpo: a única indicação concreta está na nota de fonte do quadro de especificações, e em caráter provisório. "Período de referência" aparece no resumo e no Cap. 4 e só é definido no Cap. 5. "Forma reduzida estadual" entra no objetivo específico (d) antes de ser explicada. "Quadra chuvosa" é usada desde o Cap. 2 sem definição. Siglas de bases (SINASC, SIM, SINAN, PAM) e ATT não são expandidas.
**Evidence Anchor**: `text: secoes/apendices.tex, nota do Quadro qua:espec "A quadra chuvosa é tomada, provisoriamente, como fevereiro a maio"`
**Why it matters**: Um membro de banca de fora da área não reconstrói a hipótese confirmatória sem saber o que é a estação e o período de referência; hoje precisa ir ao apêndice e voltar.
**Suggestion**: Um parágrafo de definições ao fim do Cap. 1 ou no início do Cap. 4 (estação provisória, período de referência, coortes, grupos), e expansão das siglas na primeira ocorrência.
**Severity**: Minor
**Confidence**: 4 — competência central

### W9: A informação sobre as rodadas exploratórias está no meio de um parágrafo de inferência
**Problem**: A declaração de que o desenho já foi rodado sobre o período inteiro, com o desfecho do pós-lei, está no último parágrafo da seção de inferência, sem título próprio e sem menção no resumo, na introdução ou nas ameaças.
**Evidence Anchor**: `text: secoes/05-metodologia.tex, seção de inferência "Duas rodadas exploratórias antecedem o plano, e nenhuma é reportada aqui."`
**Why it matters**: É uma informação que condiciona a leitura de tudo o que o projeto chama de confirmatório; o leitor que não chega ao fim do Cap. 5 não a vê.
**Suggestion**: Dar-lhe subseção própria ("O que já foi feito") e uma linha no Cap. 1.
**Severity**: Minor
**Confidence**: 4 — competência central

### W10: O texto não diz o que resta de cada camada de contribuição em cada cenário
**Problem**: A contribuição é apresentada em três camadas (objeto, medida, identificação), e a seção termina afirmando que o projeto diz o que entrega em todos os cenários. O Quadro diz o que é entregue, mas não o que resta de cada camada: a de medida desaparece na linha 5; a de objeto, como avaliação de efeito, só existe plenamente na linha 1; a de identificação fica sem aplicação na linha 3. Além disso, resumo e Cap. 1 descrevem os cenários adversos como "não haver efeito detectável", quando quatro das cinco linhas são de teste não realizado, e não de efeito nulo.
**Evidence Anchor**: `text: secoes/01-introducao.tex, Contribuição "Em todos os cenários previstos, inclusive o de não haver efeito detectável, o projeto diz o que entrega"`
**Why it matters**: A contribuição anunciada na introdução é incondicional na forma e condicional no conteúdo; o leitor só descobre a condição no Cap. 5.
**Suggestion**: Acrescentar ao Quadro uma coluna, ou ao Cap. 1 uma frase por camada, dizendo de que cada uma depende; distinguir "efeito não detectável" de "teste não realizado".
**Severity**: Minor
**Confidence**: 4 — competência central

### W11: A população do parâmetro muda na linha 5 sem que o texto o diga
**Problem**: O parâmetro condiciona em municípios com aplicação documentada entre 2007 e 2011, e a regra conta como documentados os voos registrados em ao menos um ano do período de referência. Na linha 5 a classificação vem do Censo de 2006, que é anterior a essa janela e não distingue cultura. A população do contraste deixa de ser a do parâmetro.
**Evidence Anchor**: `text: secoes/05-metodologia.tex, primeira seção "município com aplicação aérea documentada entre 2007 e 2011"`
**Why it matters**: O objetivo geral fala em "aplicação aérea documentada"; na linha 5 a análise responde a outra população, e isso deveria constar da descrição da entrega.
**Suggestion**: Dizer, na linha 5 e no Cap. 8, que a população é a dos municípios com registro de aeronave em 2006, e que o parâmetro do Cap. 5 não é o alvo nesse cenário.
**Severity**: Minor
**Confidence**: 4 — conferência direta entre trechos

### Criterion-Bound Judgements
Calibration status: `NOT_CALIBRATED`. Fonte dos critérios: contrato `reviewer/reviewer_full/v2` (D5, D6) e Cartão #1. Sem pontos, pesos ou médias.

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| Adequação ao veículo configurado (D6) | Contrato D6; Cartão, foco 3 | PARTLY_MEETS | W1, W5 | É projeto de dissertação em economia aplicada, com escopo próprio de ensaio; falta sustentar a suficiência fora da linha 1 e situar o segundo ensaio | Veículo não confirmado; regimento do programa não informado | Sim: sustenta o bloqueio reparável |
| Originalidade (D6) | Contrato D6; Cartão, foco 2 | MEETS | S4, W10 | Objeto novo e delimitado; a dependência de cada camada não está dita por cenário | Não conferi a literatura por fora | Não |
| Relevância e interesse (D6) | Contrato D6 | MEETS | S5 | Decisões em curso dependem da pergunta | nenhuma identificada | Não |
| Pergunta anunciada e pergunta respondível (D6) | Cartão, foco 1 | PARTLY_MEETS | W4, W11 | O contraste estimado é mais estreito que a pergunta do título e do objetivo; o corpo reconhece, as formulações não | Não desci à derivação | Sim |
| Contrato de entrega e verificabilidade (D6) | Cartão, focos 3 e 4 | PARTLY_MEETS | S1, W2, W3, W7 | A regra existe e é boa na forma; a condição decisiva está em aberto e há casos sem linha | nenhuma identificada | Sim |
| Exequibilidade do cronograma (D6) | Cartão, foco 4 | PARTLY_MEETS | W5, W6, W7 | Sequência coerente para o primeiro ensaio, sem folga na dependência externa e sem o fim da dissertação | Calendário do programa não informado | Sim |
| Organização e clareza (D5) | Contrato D5; Cartão, foco 5 | PARTLY_MEETS | S2, W8, W9 | Estrutura limpa e estatutos declarados; conceitos centrais definidos tarde ou só em apêndice | nenhuma identificada | Não: aviso |
| Quadros, figura e proporção corpo/apêndice (D5) | Contrato D5 | MEETS | S1 | Quadros legíveis sozinhos; o diagrama declara o que omite; apêndices proporcionais | nenhuma identificada | Não |

O sinal de revisão substancial vem dos critérios de D6 marcados como decisivos: suficiência por cenário (W1), operacionalidade da regra (W3), coerência pergunta e contraste (W4) e escopo da dissertação (W5). Todos são reparáveis por reescrita, sem dado ou análise nova. Nenhum deles é, sozinho, razão de recusa; o bloqueio decorre do efeito conjunto sobre a possibilidade de a banca julgar o cumprimento. Os pontos fortes em originalidade e franqueza não compensam essa lacuna, e ela não os diminui.

### Detailed Comments

#### Journal Fit
O trabalho é, na forma e no conteúdo, um projeto de avaliação de política em economia aplicada, do tipo que uma banca de mestrado examina. O desajuste não é de tema nem de nível: é que o documento se apresenta como requisito do curso e descreve metade da dissertação.

#### Originality
A retirada de um método de aplicação, avaliada depois do fato, é objeto novo frente aos antecedentes que o texto cita. A camada de medida (distância entre cultura e método) pode ser a contribuição mais durável, e é a que depende inteiramente dos registros.

#### Significance
Alta para o debate estadual e federal. O texto acerta ao dizer que um resultado de não mensurabilidade também informa, mas esse argumento precisa ser desenvolvido como argumento de suficiência (W1).

#### Structural Coherence
Resumo, introdução e Cap. 8 dizem a mesma coisa sobre a entrega condicional, com a divergência pontual de W2. A cadeia pergunta, objetivo, hipótese e parâmetro tem a folga descrita em W4 e W11.

#### Title & Abstract
O título promete "efeitos sobre o peso ao nascer" sem qualificação; o resumo é mais honesto que o título e já anuncia a entrega por cenário. "O período de referência é fixado antes da seca" é opaco para quem ainda não leu o Cap. 5.

#### Conclusion
Não há conclusão, o que é próprio de um projeto. O Cap. 8 faz esse papel e é onde a revisão deve se concentrar.

### Questions for Authors
1. Este documento é o projeto da dissertação ou do primeiro ensaio? Qual é o prazo de defesa, e o que o segundo ensaio usa do primeiro nas linhas 3 a 5 da regra?
2. Qual é o valor central da grade de frações expostas e em que se apoia, dado que a rodada de novembro já calculou efeito detectável com o período inteiro?
3. Em que linha da regra cai o caso de registros obtidos só de 2021 em diante, ou obtidos depois da data-limite?
4. A qualificação dos bimestres 4 e 5 examina este projeto ou o ensaio pronto? Quem, além do orientador, vê o plano de análise antes da estimação?

### Minor Issues
- secoes/apendices.tex, Quadro de especificações: linha em branco solta depois da linha "Estudo de evento".
- secoes/01-introducao.tex: a frase que começa em "Mais precisamente" está colada à seguinte na mesma linha de fonte, sem quebra; conferir o parágrafo.
- A data-limite é dada em bimestres no Cap. 5 antes de o cronograma dizer que o primeiro bimestre é dezembro de 2026 e janeiro de 2027; dar a data de calendário.
- A chave `brasil2011sinasc` sai na lista como publicação de 2013, enquanto o texto fala da troca de formulário em 2011; uma nota evita a dúvida do leitor.
- Metadado `pdftitle` genérico ("Projeto de pesquisa").
