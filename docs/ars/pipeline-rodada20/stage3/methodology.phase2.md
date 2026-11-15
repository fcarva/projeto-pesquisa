contract_role: methodology

## Dimension Scores

### D1: methodology_rigor

score: warn
trigger: "Um problema corrigível sem alterar o desenho, como verificação de robustez mencionada mas não especificada"

O parâmetro-alvo, a hipótese de identificação única da diferença tripla, a janela gestacional fixa, a seleção para o nascimento vivo, o poder e a inferência com poucos tratados estão todos enunciados, o que afasta os gatilhos de bloqueio do meu plano. O que falta é técnico e se resolve na redação: a Eq. (2) não contém o efeito fixo que o texto e a Figura 1 dizem absorver os choques município-ano (W1); o `β` da Eq. (2) não é o `ATT` da Eq. (1) sem hipóteses que o texto não escreve (W2); a interação por chuva, o contraste de terceiro trimestre, `H2` e `H4` não têm especificação (W3); o diagnóstico de abertura condiciona a análise confirmatória no desfecho do pré-período (W4); não há verificação dinâmica planejada da hipótese de identificação (W6); e o procedimento de inferência primário não está designado (W8). Nenhum desses pontos exige redesenho. Em conjunto justificam `warn`, não `block`.

### D2: domain_accuracy

score: not_assessed

### D3: argumentative_coherence

score: warn
trigger: "regra de decisão incompleta para algum resultado plausível"

A cadeia pergunta, parâmetro, estimador e interpretação é em geral contínua, e a linguagem causal é contida: o capítulo 8 condiciona a entrega da estimativa à medição e ao diagnóstico, e admite o ensaio como diagnóstico de medida e de poder. Os descompassos são localizados: o Quadro 2 não cobre o resultado que o próprio texto torna mais provável (W5); o tratamento é definido de três modos em seções diferentes (W9); o critério de concordância da triangulação não é operacional (W10); e o elo entre `β` e o parâmetro-alvo fica implícito (W2).

### D4: cross_disciplinary_relevance

score: not_assessed

### D5: writing_and_structure

score: not_assessed

### D6: venue_fit_and_contribution

score: not_assessed

## Review Body

Parecer do assento de metodologia sobre um projeto de pesquisa de mestrado, sem resultados. Não há critérios de veículo vinculados (`criteria_binding_unavailable`), e não faço afirmação de adequação a periódico ou a norma do programa. Dois critérios de `review_criteria_framework.md` §2.1 foram aplicados ao que o texto promete, e não a resultados: completude do relato estatístico (avaliada sobre §5.8: efeito mínimo detectável, correção de Holm, procedimentos para poucos grupos; sem estatística reportada a conferir) e conservadorismo das conclusões (avaliado sobre o capítulo 8, que atende). A ausência de números de estimativa é regra declarada do documento e não foi tratada como defeito. Não encontrei no manuscrito tentativa de instruir o parecerista.

Conferi a álgebra da Eq. (2) à mão e por posto de matriz num painel simulado (município por mês de nascimento, janela gestacional fixa de nove meses, estação de fevereiro a maio como hipótese minha para a quadra chuvosa, coortes de transição de 2019 excluídas). Resultado: `A_m × P_t` e `P_t × Pos_t` são absorvidos por `α_{m,s(t)}` e `γ_t` quando `P_t` depende só do mês do ano. `A_m × Pos_t` não é absorvido e está corretamente incluído como `λ`. `β` é identificado. Nenhum termo da equação absorve choques de município por ano. Os achados W1 e W2 decorrem dessa conferência.

As afirmações que o manuscrito não permite conferir (existência e data do plano versionado, conteúdo da rodada exploratória, ausência de cruzamento da exposição sazonal com os desfechos) foram tratadas como declarações. W11 diz o que seria preciso ver.

Distingo, em cada fraqueza, a correção necessária da sugestão opcional. As correções necessárias cabem em cerca de uma página adicional: uma equação reescrita, um quadro de especificações e três ou quatro frases.

### S1: Parâmetro-alvo definido antes do estimador e sobre coortes

A Eq. (1) define o efeito sobre coortes expostas em municípios com aplicação aérea, e a §5.1 lista os elos da cadeia causal que podem falhar separadamente, com a população tratada encolhendo a cada elo. Isso permite ler um nulo como falha de implementação ou de mecanismo, e não só como ausência de efeito.

**Evidence Anchor**: text: §5.1 "É um efeito sobre coortes expostas, e não sobre municípios"

### S2: Janela gestacional fixa

A exposição é definida por janela fixa, e não pela duração observada da gestação. Evita-se condicionar em variável afetada pelo tratamento, erro comum em desenhos de calendário gestacional.

**Evidence Anchor**: text: §5.2 "a duração observada da gestação é desfecho, e usá-la para definir a exposição condicionaria em variável afetada pelo tratamento"

### S3: Hipótese de identificação única, enunciada, com a comparação em nível descartada

O texto diz que a comparação em nível entre municípios empresariais e familiares seria inválida e reduz a exigência a uma hipótese só: evolução igual do hiato sazonal na ausência da lei. A hipótese é refutável em princípio (ver W6 sobre como).

**Evidence Anchor**: text: §5.2, Grupo de comparação "Em nível, essa comparação não seria válida"

### S4: Regra operacional entre teste e limite

O efeito mínimo detectável é calculado só com o pré-período e comparado a magnitudes da literatura para diferentes frações expostas. Análise sem poder é reportada como limite. É a resposta correta a poucos tratados com diluição intramunicipal.

**Evidence Anchor**: text: §5.8 "análise cujo efeito mínimo detectável supere o efeito plausível é reportada como limite, e não como teste"

### S5: Seleção para o nascimento vivo tratada como desfecho confirmatório

O óbito fetal entra como segundo desfecho confirmatório e como teste de seleção, com o sentido do viés sobre o peso médio declarado de antemão.

**Evidence Anchor**: text: cap. 6, Desfechos "O óbito fetal tem função dupla: é desfecho de saúde e é teste de seleção"

### S6: Ordem dos fatos declarada

O texto revela que uma rodada exploratória da forma reduzida já foi executada, que ela mudou o alvo e que o desenho de calendário foi adotado depois. Essa declaração afasta o gatilho fatal do meu plano (especificação condicionada ao resultado apresentada como pré-especificada).

**Evidence Anchor**: text: §5.8 "uma rodada exploratória dessa análise já foi executada e levou a rever seu alvo, da curva para o nível"

### W1: A Eq. (2) não contém o efeito fixo que o texto e a Figura 1 dizem absorver os choques município-ano

**O que está errado e onde.** A §5.2 afirma que os efeitos fixos absorvem "os choques comuns a todas as coortes de um município num dado ano", e a Figura 1 repete "choques município-ano" no nó de efeitos fixos. A Eq. (2) tem `α_{m,s(t)}` (município por mês do ano) e `γ_t` (coorte, comum a todos os municípios). Nenhum dos dois varia por município e ano. `γ_t` remove o que é comum ao estado em cada coorte. `λ(A_m × Pos_t)` remove um único degrau de nível entre os grupos, constante em todo o pós-lei. Um choque próprio de um município num ano (seca local, programa municipal, 2020 e 2021 com intensidade desigual) fica no erro.

**Por que importa.** Num painel balanceado e sem pesos, esse choque é ortogonal ao contraste sazonal dentro do ano e não enviesa `β`. Mas ele não é absorvido: aumenta a variância do erro justamente onde há poucos tratados, e a ortogonalidade deixa de ser exata com pesos por número de nascimentos ou com anos incompletos (em 2019 só as coortes de outubro a dezembro são pós-lei). A linha "Políticas estaduais de saúde materna" do Quadro 4 apoia-se na mesma frase. Também é mais forte do que a equação permite dizer que os efeitos fixos absorvem "a composição das mães por mês de concepção": só a parte invariante no tempo é absorvida. A mudança de composição sazonal própria dos municípios com avião no pós-lei é a hipótese de identificação, não algo removido.

**Correção proposta (necessária).** Ou acrescentar o efeito fixo de município por ano de nascimento à Eq. (2), caso em que `λ(A_m × Pos_t)` fica colinear e sai da equação (conferido: com as coortes de transição excluídas, `A_m × Pos_t` é constante dentro de cada município-ano), ou manter a Eq. (2) e corrigir a frase, a Figura 1 e o Quadro 4 para dizer o que de fato é absorvido. A primeira opção é a que implementa o desenho descrito. Se a estação medida variar de ano para ano, `P_t` deixa de ser função do mês do ano e `A_m × P_t` precisa entrar explicitamente.

**Severity**: Major
**Evidence Anchor**: equation: Eq. (2), termos alpha_{m,s(t)} e gamma_t, sem efeito fixo de município por ano
**Confidence**: 5 — especialidade central (diferença tripla com efeitos fixos); conferido por posto de matriz

### W2: O `β` da Eq. (2) não é o `ATT` da Eq. (1) sem hipóteses que o texto não escreve

**O que está errado e onde.** Três descompassos entre a Eq. (1) e a Eq. (2).

Primeiro, a Eq. (1) condiciona em `S_t = 1`, definido como "coorte cuja gestação atravessa a estação de pulverização". Com gestação de nove meses e estação de quatro (a quadra chuvosa, que o texto adota na falta de calendário medido), toda gestação a termo atravessa a estação: os oito meses restantes do ano não comportam nove meses de gestação. `S_t` vale 1 para todas as coortes e não define subpopulação.

Segundo, a Eq. (2) usa `P_t`, a fração dos dois primeiros trimestres na estação. Sob a mesma hipótese de quatro meses, as coortes com `P_t = 0` são exatamente as que têm o terceiro trimestre na estação, e o valor máximo de `P_t` é dois terços. O grupo de referência do contraste é, portanto, exposto no terceiro trimestre, e `β` mede a mudança da diferença entre exposição precoce e exposição tardia, extrapolada linearmente para `P_t = 1`, valor fora do suporte.

Terceiro, `β` só iguala o efeito da lei sobre as coortes de estação se a lei não tiver efeito sobre as coortes de referência. Qualquer benefício fora da estação ou no terceiro trimestre vai para `λ`, que não tem leitura causal, e `β` subestima o efeito. O contraste por trimestre apoia-se numa estimativa do análogo equatoriano descrita como "sem significância estatística", que o texto trata, com cuidado, como "efeito menor" e não como zero. Falta dizer que a identificação do `ATT` depende disso.

**Por que importa.** O texto interpreta `β` corretamente como mudança do hiato sazonal, mas o objetivo geral e a Eq. (1) prometem um `ATT`. A leitura de teste ou limite (§5.8) e a comparação com magnitudes da literatura dependem de qual dos dois se estima.

**Correção proposta (necessária).** Redefinir `S_t` na Eq. (1) pelos dois primeiros trimestres, ou reescrever o alvo como diferença de efeitos entre exposição precoce e tardia. Declarar em uma frase a hipótese de exclusão (efeito nulo ou menor nas coortes de referência) e o sentido do viés se ela falhar. Informar o suporte de `P_t` sob a estação adotada e reportar o efeito na escala observada. Opcional: versão com `P_t` em categorias, que dispensa a linearidade.

**Severity**: Major
**Evidence Anchor**: equation: Eq. (1), condicionamento em S_t = 1, frente a P_t em [0,1] na Eq. (2)
**Confidence**: 4 — especialidade central em desenhos de calendário; a contagem de meses supõe estação de quatro meses, que o manuscrito não fixa

### W3: Componentes do desenho principal descritos no texto e ausentes da especificação

**O que está errado e onde.** A Eq. (2) é a única especificação escrita, e quatro elementos do desenho confirmatório ou da regra de decisão não aparecem nela.

A interação por chuva (§5.2, `H3`, terceira linha do Quadro 2): não há variável, corte nem termos. Como a chuva modula o voo também antes da lei, a interação quádrupla exige `A_m × P_t × Chuva` no pré-período e `A_m × Chuva × Pos_t`. Sem eles, o coeficiente de interesse absorve a relação pré-existente entre chuva e hiato sazonal.

O contraste de terceiro trimestre (`H3`): não há variável correspondente a `P_t` para o terceiro trimestre.

A amostra: a Eq. (2) tem `A_m` binário, mas a §5.5 cria três grupos e o teste de `H4` usa municípios sem banana. Não se diz quais municípios entram na estimação de `β`, onde ficam os vizinhos expostos e os municípios com banana que não são nem tratados nem predominantemente familiares.

`H2`, que é confirmatória: não há especificação para a taxa de óbito fetal (denominador, tratamento de células município-mês com zero evento, modelo linear ou de contagem). O "desfecho composto que soma nascidos vivos e óbitos fetais" é uma contagem, e não fica claro que quantidade de saúde ele mede. Também não se diz se as células são ponderadas por nascimentos.

**Por que importa.** Na terceira linha do Quadro 2 a interação por chuva passa a ser o desenho principal, e ela é a parte menos especificada. `H2` entra na correção de Holm sem equação.

**Correção proposta (necessária, proporcional).** Um quadro de meia página com uma linha por hipótese (`H1` a `H5`): desfecho, amostra, coeficiente testado, ponderação, estatuto confirmatório ou exploratório. E a Eq. (2) estendida com os termos de chuva. Cortes numéricos (limiar de chuva, meses da estação) podem ficar para o plano de análise, como o texto já prevê.

**Severity**: Major
**Evidence Anchor**: absence: §5.2 e cap. 4 — expected especificação (variável, termos de ordem inferior, amostra e ponderação) para a interação por chuva, o terceiro trimestre, H2 e H4; checked §5.2, §5.3, §5.5, §5.8, cap. 4, cap. 6 e Quadro 2
**Confidence**: 4 — especialidade central; reconheço o risco de pedir a um projeto o detalhe de um plano de pré-análise, e por isso limito a correção a um quadro

### W4: O diagnóstico de abertura condiciona a análise confirmatória no desfecho do pré-período

**O que está errado e onde.** A §5.3 afirma que o diagnóstico "não consome graus de liberdade da análise confirmatória". A afirmação não se sustenta como escrita. O diagnóstico estima, com o mesmo desfecho, os mesmos municípios e o mesmo contraste sazonal, o hiato do pré-período, e seu resultado decide duas coisas: se o desenho principal é executado (Quadro 2) e "qual pré-período serve de referência à Equação" (2). Ora, `β` é a diferença entre o hiato do pós-lei e o hiato do pré-período de referência. Escolher como referência o subperíodo em que o hiato aparece negativo, com poucos municípios tratados e hiato ruidoso, seleciona em parte o ruído. Sob efeito nulo, o hiato do pós-lei regride à média e `β` sai positivo, na direção de `H1`. É o problema conhecido de estimar depois de um pré-teste (ver Roth, 2022, AER: Insights, a conferir pelo autor).

Há dois problemas menores no mesmo passo. Os dois subperíodos diferem pela seca, que altera a sazonalidade de renda, alimentação e doença por vias alheias ao voo, de modo que "gradiente presente no primeiro e ausente no segundo" não isola a pulverização. E o subperíodo "em que há registro de voos" é anterior a 2012, enquanto os relatórios pedidos ao Ministério cobrem 2012 a 2018: para ele, o único registro é o Censo de 2006.

**Por que importa.** É o passo que o projeto apresenta como garantia de que o pós-lei é usado uma só vez. Sem correção, a taxa de erro do teste confirmatório não é a nominal.

**Correção proposta (necessária).** Escolher uma das saídas e escrevê-la: (a) fixar o pré-período de referência por critério que não use o desfecho (registros de voo, ou anos definidos de antemão); (b) separar as amostras, com o diagnóstico em um trecho do pré-período e a referência em outro; ou (c) manter o condicionamento e obter a distribuição de referência aplicando o procedimento inteiro, diagnóstico seguido de estimação, a conjuntos placebo de municípios. Em qualquer caso, definir o que conta como "gradiente" (sinal, limiar em relação ao efeito mínimo detectável) e retirar a frase sobre graus de liberdade. Opcional: estender o pedido ao Ministério para antes de 2012, se os relatórios existirem.

**Severity**: Major
**Evidence Anchor**: text: §5.3 "não consome graus de liberdade da análise confirmatória"
**Confidence**: 4 — especialidade central (inferência após pré-teste em diferenças-em-diferenças)

### W5: O Quadro 2 não cobre o resultado que o próprio texto torna mais provável

**O que está errado e onde.** As quatro linhas não são exaustivas nem mutuamente exclusivas frente às combinações de medição e diagnóstico. Faltam pelo menos: voos documentados às vésperas da lei e nenhum gradiente sazonal no pré-período (o caso que o capítulo 7 torna mais provável, dada a diluição intramunicipal); gradiente presente sem registro de voo (pedidos de acesso sem resposta); e voos documentados com calendário sem pico sazonal, situação em que o texto diz que o desenho "mede zero por construção". As três primeiras linhas são definidas só pela medição, e a quarta, pela medição e pelo diagnóstico. A terceira linha muda o estimando para "impedir a volta dos voos" sem dizer qual é o contrafactual. Os critérios de cada linha não são observáveis como escritos: não se diz o que é "documentado" nem o que é "gradiente".

**Por que importa.** A regra de decisão é o dispositivo de pré-compromisso do projeto. Uma regra que não cobre o caso mais provável deixa a decisão para depois do dado.

**Correção proposta (necessária).** Reescrever o quadro como cruzamento de duas entradas (medição: voos com calendário, voos sem calendário, voos suspensos, sem registro, sem resposta; diagnóstico: gradiente, sem gradiente), com uma ação por célula, e definir os critérios em uma linha cada. Para a célula de voos documentados sem gradiente, dizer se o desenho principal roda como teste ou é reportado como limite segundo a regra de poder da §5.8.

**Severity**: Major
**Evidence Anchor**: table: Quadro 2 — quatro linhas, sem a combinação de voos documentados com ausência de gradiente sazonal no pré-período
**Confidence**: 5 — leitura direta do quadro contra as combinações possíveis

### W6: Não há verificação dinâmica planejada da hipótese de identificação da diferença tripla

**O que está errado e onde.** A hipótese é que, sem a lei, o hiato sazonal teria evoluído do mesmo modo nos dois grupos. As verificações previstas não a testam. O diagnóstico da §5.3 estima o nível do hiato em dois subperíodos, não sua trajetória relativa. O tratamento falso (`H4`) compara banana familiar com municípios sem banana: pode mostrar que o grupo de comparação não reage à lei, mas nada diz sobre uma mudança de sazonalidade própria dos municípios com avião, que é a ameaça à qual o Quadro 4 o atribui. A exclusão de 2020 e 2021 é sensibilidade, não teste.

Há um agravante que o próprio texto fornece: se a seca suspendeu os voos de 2012 a 2017, o hiato sazonal dos tratados muda dentro do pré-período por causa do tratamento. A estabilidade pré-lei do hiato relativo é então esperada falhar, e o contrafactual do pós-lei depende da chuva de cada ano.

**Por que importa.** Sem verificação dinâmica, a hipótese central fica enunciada mas com teste só indireto. Meu plano da Fase 1 trataria como bloqueio a ausência total de verificação possível. Não é o caso, porque a verificação é viável com os dados previstos, mas ela precisa ser prometida.

**Correção proposta (necessária).** Prometer o estudo de evento da diferença tripla: `β` por ano, com ano de referência fixado, coeficientes do pré-período reportados com a mesma inferência do efeito principal. E dizer de antemão como os anos de seca entram: ou a especificação condicional à chuva de W3, em que a relação pré-lei entre chuva e hiato sazonal fornece o contrafactual, ou a restrição do pré-período de referência conforme W4. Opcional: placebo no tempo com uma data de lei falsa no pré-período.

**Severity**: Major
**Evidence Anchor**: absence: §5.2, §5.3 e Quadro 4 — expected estudo de evento ou placebo no tempo para a evolução do hiato sazonal relativo no pré-período; checked §5.2, §5.3, §5.6, §5.8, Quadro 2 e Quadro 4
**Confidence**: 4 — especialidade central; a força do agravante depende de a seca ter de fato suspendido os voos, que o texto trata como hipótese

### W7: Definição operacional do grupo de comparação e de `A_m` incompleta

**O que está errado e onde.** "Predominantemente familiar" não tem limiar nem base (estabelecimentos, área ou valor da produção de banana). A exclusão por "qualquer registro de aeronave" não diz em quais fontes e anos. `A_m` provisório vem do Censo de 2006, treze anos antes da lei, e o parâmetro pede aplicação aérea "às vésperas da lei". A classificação familiar é de 2017, depois de cinco anos de seca. Não há ordem de grandeza de quantos municípios ficam em cada grupo, embora o texto informe que o Censo de 2006 registra aplicação por avião em 7 municípios, o que limita `A_m` provisório por cima.

**Por que importa.** O número de municípios por grupo determina qual procedimento de inferência é utilizável (W8) e o efeito mínimo detectável. O texto remete "os grupos" ao plano de análise, o que é aceitável para os cortes, mas a regra de construção deve constar do projeto.

**Correção proposta.** Necessária: uma frase com a variável e a base do critério familiar e com as fontes e anos da exclusão por aeronave. Opcional: ordem de grandeza do número de municípios por grupo sob a classificação provisória, que é contagem descritiva e não estimativa.

**Severity**: Minor
**Evidence Anchor**: text: §5.2, Grupo de comparação "em que a cultura é predominantemente familiar"
**Confidence**: 4 — especialidade central

### W8: Cinco procedimentos de inferência listados sem designação do primário nem correspondência com as análises

**O que está errado e onde.** A §5.8 lista Conley e Taber, Ferman e Pinto, inferência conformal, Hagemann e Canay, Santos e Shaikh, e não diz qual fornece o valor-p de `H1` e `H2` que entra em Holm. Quatro pontos específicos.

A inferência conformal citada é construída para controle sintético e séries de tempo, e serve à segunda análise secundária, não à Eq. (2). O texto a coloca na lista da "inferência principal".

O procedimento de Canay, Santos e Shaikh exige uma condição de homogeneidade entre clusters que, até onde conheço, pede variação do regressor de interesse dentro de cada cluster. Na Eq. (2), `A_m × P_t × Pos_t` é identicamente zero em todos os municípios de comparação. A aplicação parece caber só dentro dos tratados, sem o grupo de comparação. O autor deve conferir a condição e dizer em que amostra o procedimento é aplicado. A frase também convive mal com a anterior, que declara o bootstrap selvagem indefensável com poucos tratados.

Os tratados são, pelo que o texto descreve, contíguos na Chapada do Apodi. Choques regionais de sazonalidade tornam o número efetivo de clusters tratados independentes menor que o número de municípios, e Conley e Taber supõem independência entre grupos.

Não se promete reportar intervalos, apenas testes.

**Por que importa.** Com cinco procedimentos e nenhum designado, a escolha do valor-p é grau de liberdade do pesquisador exatamente no ponto em que o texto reconhece precisão frágil.

**Correção proposta (necessária).** Designar um procedimento primário para `β` (a escolha natural, pelo próprio texto, é Ferman e Pinto, com placebos formados por conjuntos de municípios de comparação) e rebaixar os demais a sensibilidade, cada um ligado à análise a que se aplica. Dizer como a dependência espacial entra (placebos com conjuntos contíguos, ou agregação dos tratados em um bloco com Hagemann). Prometer intervalos por inversão do teste primário.

**Severity**: Major
**Evidence Anchor**: text: §5.8 "na diferença tripla, em que a variação é interna ao município, aplica-se também"
**Confidence**: 3 — especialidade central em inferência com poucos grupos; a condição exata de Canay, Santos e Shaikh foi citada de memória e deve ser conferida no artigo

### W9: Três definições de tratamento em seções diferentes, e nenhuma fonte mede voos depois da lei

**O que está errado e onde.** A Eq. (2) estima o efeito de estar sob a lei em município com avião (`A_m × Pos_t`). A §5.5 diz que o tratamento "é definido como cessação efetiva de voos e medido como tal". O Quadro 4 diz que o "parâmetro é de intenção de tratar". A terceira linha do Quadro 2 fala em "impedir a volta dos voos". São três estimandos. Além disso, a §5.1 promete medir os elos intermediários, a começar pelo cumprimento, mas os relatórios pedidos ao Ministério vão de 2012 a 2018. Para o pós-lei só há autos de infração, que registram a violação detectada e não a ausência de voo.

**Por que importa.** A distinção entre falha de implementação e falha de mecanismo, que a §5.1 apresenta como razão do desenho, depende de observar voos depois de 2019.

**Correção proposta (necessária).** Declarar a intenção de tratar como estimando da Eq. (2) e a cessação efetiva como medida de cumprimento a documentar. Estender o pedido de relatórios mensais a 2019 a 2024, para o Ceará e o Rio Grande do Norte, o que não tem custo adicional relevante. Dizer, na terceira linha do Quadro 2, qual é o contrafactual. Opcional: definir "vizinho imediato" (contiguidade) e "fora do alcance" na §5.5.

**Severity**: Major
**Evidence Anchor**: text: §5.5 "O tratamento é definido como cessação efetiva de voos e medido como tal"
**Confidence**: 4 — especialidade central; não sei se os relatórios mensais continuam a existir para um estado em que a atividade foi proibida

### W10: Forma reduzida estadual e triangulação com hipóteses e critério de concordância por escrever

**O que está errado e onde.** A §5.6 propõe diferenças-em-diferenças com dose contínua (área de banana) e alvo `ATT(d | d)`, e em seguida apresenta a Eq. (3), que é resultado para tratamento binário mal classificado. Não se diz como a dose contínua vira classificação binária, qual é o grupo de dose nula, nem qual hipótese de tendências paralelas sustenta a análise. O Quadro 3 atribui à aptidão agroclimática o uso "forma reduzida estadual", mas a §5.6 não menciona instrumento nem primeiro estágio, de modo que "forma reduzida" fica sem referente. O critério "só há convencimento se concordarem" não é operacional: as quatro análises têm estimandos diferentes (a Eq. (3) prevê magnitude atenuada por construção), e exigir concordância de quatro análises de baixo poder torna o resultado convincente quase inalcançável mesmo com efeito verdadeiro.

**Por que importa.** A forma reduzida é o que resta na quarta linha do Quadro 2 e é a única análise já executada em rodada exploratória.

**Correção proposta.** Necessária: duas frases com a binarização e o grupo de dose nula, a hipótese de tendências paralelas da forma reduzida e o papel da aptidão agroclimática. Definir concordância como sinal e compatibilidade de intervalos na escala de cada estimando, e não como significância conjunta. Opcional: retirar a comparação de fronteira da lista de análises e mantê-la como descritiva, dado o que o próprio texto diz sobre ela.

**Severity**: Minor
**Evidence Anchor**: equation: Eq. (3), theta = VPP x ATT, apresentada para uma análise de dose contínua
**Confidence**: 3 — especialidade central em tratamento contínuo; a fidelidade da Eq. (3) à fonte citada é do parecerista de domínio

### W11: Pré-compromisso declarado, mas não verificável por terceiros

**O que está errado e onde.** O texto afirma que o plano da forma reduzida foi versionado em setembro de 2026, que a exposição sazonal não foi cruzada com os desfechos e que o plano do desenho principal será fixado antes do pós-lei. Reconhece que são planos em repositório, sem registro público. Como a rodada exploratória usou desfechos do pós-lei e o desenho principal foi escolhido depois dela, a garantia de que o desenho de calendário é cego ao pós-lei depende inteiramente dessas declarações.

**Por que importa.** O valor de um pré-compromisso está em poder ser conferido. A honestidade da declaração é ponto forte (S6), mas ela não substitui o carimbo de data.

**Correção proposta (opcional, de baixo custo).** Depositar o plano de análise com carimbo de data externo antes do terceiro bimestre (registro público, ou ao menos identificador de versão e resumo criptográfico citados no ensaio) e manter registro de acesso às bases do pós-lei. Para a banca, bastaria ver o histórico de versões do repositório e o plano de setembro.

**Severity**: Minor
**Evidence Anchor**: text: §5.8 "São planos versionados em repositório, não pré-registro público"
**Confidence**: 4 — prática corrente de planos de pré-análise

## Arithmetic Receipts

no_recomputable_statistics: o manuscrito é um projeto sem estimativas próprias; conferi todas as seções, os Quadros 1 a 5 e as Eqs. (1) a (3), e os únicos números são contagens descritivas e magnitudes citadas da literatura, sem estatística de teste, graus de liberdade, valor-p ou média com N e escala que algum dos quatro procedimentos cubra
