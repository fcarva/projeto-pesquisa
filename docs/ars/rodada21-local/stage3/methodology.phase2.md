contract_role: methodology

## Dimension Scores

### D1: methodology_rigor

score: block
trigger: "a fronteira entre análise confirmatória e exploratória não pode ser verificada"
block_class: repairable

### D2: domain_accuracy

score: not_assessed

### D3: argumentative_coherence

score: warn
trigger: "ressalvas declaradas em um trecho e ignoradas em outro"

### D4: cross_disciplinary_relevance

score: not_assessed

### D5: writing_and_structure

score: not_assessed

### D6: venue_fit_and_contribution

score: not_assessed

## Review Body

### Reviewer Identity

Peer Reviewer 1 — Methodology. Econometrista aplicado, com trabalho em diferenças-em-diferenças e diferença tripla com adoção única, tratamento contínuo, inferência com poucos grupos tratados, planos de análise pré-especificados e cálculo de poder em desenhos observacionais com dados administrativos agregados.

### Overall Recommendation

Major Revision

### Confidence Score

4. Confiança é apenas declaração de incerteza e escopo. Onde uso conhecimento externo de econometria, marco como conhecimento do parecerista, não conferido nesta revisão.

### Calibration Status

`NOT_CALIBRATED`

### Summary Assessment

O manuscrito é um projeto de mestrado, sem estimativas, que propõe medir o efeito da proibição cearense da pulverização aérea sobre o peso ao nascer por uma diferença tripla de calendário gestacional: coortes de exposição alta contra coortes expostas só no fim da gestação, período de referência (2007 a 2011) contra pós-lei, municípios com voo documentado contra municípios de banana familiar. O desenho é pensado com cuidado incomum para um projeto: o tratamento é definido pelo método, a estrutura de efeitos fixos absorve corretamente os termos de ordem inferior, a inferência usual é descartada com razão e há uma regra que diz o que se entrega em cada cenário. O problema que impede aceitar o desenho como está é o estatuto confirmatório: o próprio texto informa que o desenho de calendário já foi estimado sobre 2005 a 2024, em variantes, antes deste documento, sem reportar o que se viu e sem registro público; o leitor não tem como verificar o que foi fixado antes e depois de ver o desfecho. Somam-se a isso cinco lacunas de peso: o limiar de poder que decide se há teste depende de um escalar não fixado e de uma referência que o texto reconhece não corresponder ao contraste; o estimando formal não é o que o coeficiente recupera; a inferência principal não trata a contiguidade dos tratados; a separação entre lei e retorno das chuvas repousa numa hipótese que o texto considera frágil; e a regra de decisão não cobre o cenário de registros parciais. Tudo é reparável por reescrita e por compromissos adicionais, sem novo dado.

### S1: Tratamento definido pelo método, com parâmetro de intenção de tratar explícito

A definição separa lei, voo e cultura, declara que o parâmetro inclui descumprimento e substituição terrestre, e justifica ancorar a classificação antes da seca para não esvaziar o grupo tratado. Isso evita o erro comum de tomar área plantada por exposição.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Parâmetro-alvo e cadeia causal "O tratamento é a lei, e não o"

### S2: Estrutura de efeitos fixos coerente com a diferença tripla

Conferi a absorção dos termos de ordem inferior. Com estação comum a todos os municípios, o indicador de exposição é função do mês civil de nascimento, de modo que A×k é absorvido por município×mês do ano, A×Pos e A×Seca por município×ano, e k×Pos, k×Seca por coorte. O coeficiente da interação tripla fica identificado só pela diferença entre grupos na mudança do hiato sazonal. A ressalva está em W8: a absorção depende de a estação ser única.
**Evidence Anchor**: equation: Eq. eq:ddd (secoes/05-metodologia.tex) — efeitos fixos de município por mês do ano, de município por ano de nascimento e de coorte

### S3: Janela gestacional fixa e exposição em grupos

Recusar a duração observada da gestação para definir a exposição evita condicionar em variável afetada pelo tratamento, e a exposição em grupos, com versões saturada e linear como sensibilidade, evita ler um coeficiente linear como efeito por unidade.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Desenho principal "E a janela gestacional é fixa"

### S4: Uma única hipótese confirmatória e recusa da inferência assintótica usual

O texto fixa um só desfecho e um só coeficiente confirmatórios, rotula os demais como exploratórios, descritivos ou de falsificação no quadro de especificações, e descarta erros-padrão agrupados convencionais e o wild cluster bootstrap isolado.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Inferência, poder e plano de análise "hipótese confirmatória, sobre o peso ao nascer"

### S5: Entrega definida também para o cenário sem efeito detectável

O projeto se compromete com produtos úteis mesmo sem teste (medida dos voos, efeito mínimo detectável), o que reduz o incentivo a forçar um resultado.
**Evidence Anchor**: text: secoes/08-cronograma.tex, Resultados esperados "o ensaio se entrega como medida do alcance da lei"

### S6: Ligação explícita entre diagrama causal e hipóteses de identificação

O apêndice diz, para cada elemento do diagrama, qual hipótese o cobre e o que o desenho faz, inclusive onde admite que a hipótese não se sustenta (versão única do tratamento) ou está fora do alcance (seleção para o nascimento vivo).
**Evidence Anchor**: table: Quadro qua:dag (Apêndice Do diagrama causal às hipóteses de identificação) — colunas "Hipótese ou papel" e "Como o projeto trata"

### W1: O estatuto confirmatório não é verificável depois das rodadas exploratórias declaradas

**Problem**: O texto informa que, antes deste documento, o desenho de calendário foi estimado sobre os nascimentos de 2005 a 2024, com variantes de limiar, de grupo tratado e de comparação, e que o efeito detectável foi calculado com o período inteiro. Nenhum resultado dessas rodadas é reportado, os planos ficam em repositório sem pré-registro público, e a ratificação com o orientador ainda pode alterar estação, limiar de agricultura familiar, medida de chuva e contrastes de falsificação. As escolhas que o texto dá como fixadas neste projeto (limiar de metade para a exposição alta, três grupos, referência 2007 a 2011, exclusão de 2012 e 2019, pós a partir de 2020) foram, pela cronologia que o próprio texto dá, fixadas depois de o desfecho do pós-lei ter sido cruzado com a exposição.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Inferência, poder e plano de análise "a exposição sazonal já foi cruzada com o desfecho do pós-lei"
**Why it matters**: A salvaguarda oferecida é que municípios tratados e estação virão da medição dos voos. Ela protege só se a medição divergir do que já foi testado. Se os registros apontarem os mesmos municípios do Censo de 2006 e a mesma quadra chuvosa, a análise "confirmatória" repete, nos mesmos dados, uma regressão cujo sinal o analista já conhece, e os parâmetros ainda abertos podem ser fechados com esse conhecimento. Um leitor não distingue esse caso do caso limpo.
**Suggestion**: (i) Reportar as duas rodadas em apêndice: lista completa de variantes e, de preferência, as estimativas; se a opção for não mostrar estimativas, dizer isso e depositar o material com data verificável por terceiro. (ii) Registrar publicamente, com carimbo de tempo, o plano antes de os registros de voo chegarem. (iii) Fechar agora, por regra que não use desfecho, os parâmetros ainda abertos, ou declarar quais deles já foram variados na rodada de novembro. (iv) Pré-especificar que, se a classificação medida coincidir com a provisória, o resultado é rotulado como reestimação em dados já examinados, não como teste confirmatório. (v) Considerar que a escolha final de especificação seja feita por quem não viu as rodadas.
**Severity**: Major
**Confidence**: 5 — núcleo de competência: planos de análise pré-especificados

### W2: O limiar de poder que decide se há teste não está operacionalizado

**Problem**: A regra compara o efeito mínimo detectável com um "efeito plausível" igual a cerca de 80 g vezes a fração de nascimentos exposta, e quem decide é o valor central de uma grade ainda não fixada. Três problemas se somam. Primeiro, a fração exposta não tem fonte no projeto: a aproximação por endereços fica como extensão. Segundo, os 80 g vêm de um contraste (três meses ou mais de fumigação intensiva contra fumigação habitual, a até 150 m) que o próprio referencial diz não ser o da lei e cuja intensidade "não foi convertida"; além disso o coeficiente do projeto mede exposição no início contra exposição no fim da gestação, em intenção de tratar sobre versões que incluem municípios onde já não se voava. Terceiro, o efeito mínimo detectável não tem definição: nível, poder alvo, teste uni ou bilateral, e sobretudo sob qual procedimento de inferência é calculado.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Regra de decisão "fixada no plano de análise; decide o valor central da grade"
**Why it matters**: A comparação entre detectável e plausível é o portão que separa "confirmatório" de "reportado como limite, sem teste". Com um escalar livre de um lado e uma definição aberta do outro, o portão pode abrir ou fechar por escolha feita depois da rodada exploratória. E um efeito plausível superestimado torna "poder suficiente" uma condição fácil de cumprir.
**Suggestion**: Fixar no projeto a grade e o valor decisório, com justificativa que não dependa do desfecho (por exemplo, limite superior da fração de nascimentos em setores censitários contíguos a bananais). Descontar explicitamente do efeito plausível o que o texto já reconhece: contraste início contra fim, fração de anos e municípios com voo esperado, substituição terrestre. Definir o efeito mínimo detectável com nível, poder e lateralidade, e calculá-lo por simulação ou por distribuição de placebos sob o mesmo procedimento de inferência do teste principal. Dizer se o teste de H1 é unilateral.
**Severity**: Major
**Confidence**: 4 — núcleo de competência: cálculo de poder em desenhos observacionais; a transferibilidade da magnitude do análogo fica fora do meu assento

### W3: O estimando formal não é o que o coeficiente recupera

**Problem**: A primeira equação define o efeito da lei sobre as coortes de exposição alta nos municípios com voo. O coeficiente de interesse mede a mudança da diferença entre coortes de exposição alta e coortes de referência, e as de referência também atravessam a estação, no terceiro trimestre. O coeficiente recupera, portanto, o efeito sobre as de exposição alta menos o efeito sobre as de referência, e só coincide com o estimando declarado se a exposição tardia não tiver efeito e se a lei não alterar o hiato no grupo de comparação. O texto reconhece a primeira condição como limite, mas mantém a definição formal, o objetivo geral e a regra de poder escritos para o efeito em nível.
**Evidence Anchor**: equation: primeira equação de secoes/05-metodologia.tex (definição de τ) — condicionamento em A_m = 1, H_t = 1 e pós-lei, sem o contraste com as coortes de referência
**Why it matters**: Sem a hipótese de sinal sobre a exposição tardia, o coeficiente não é sequer limite inferior do estimando declarado. O referencial cita estimativa imprecisa, não nula, para o terceiro trimestre no análogo. A hipótese H1, redigida como contraste relativo, está correta; é a equação do parâmetro e o que dela decorre que precisam acompanhar.
**Suggestion**: Redefinir o estimando como o contraste entre exposição no início e exposição apenas no fim da gestação, enunciar como hipótese mantida (não testável) o sinal do efeito tardio, e dizer em que condição o contraste limita o efeito em nível. Alinhar objetivo geral, resumo e regra de poder a essa definição. A especificação exploratória de terceiro trimestre já prevista pode informar, sem resolver.
**Severity**: Major
**Confidence**: 5 — núcleo de competência: correspondência entre estimando e estimador em diferença tripla

### W4: A inferência principal não trata a contiguidade dos tratados nem a estrutura da diferença tripla

**Problem**: O texto reconhece que os tratados são poucos e contíguos e escolhe como principal um procedimento justificado pela heterocedasticidade por tamanho. Não diz como o procedimento se aplica a um coeficiente de interação tripla com três conjuntos de efeitos fixos (qual estatística por município entra no teste), nem como lida com choques comuns aos tratados. Os tratados estão, pelo contexto, concentrados numa região irrigada, e o desfecho depende de chuva, que é espacialmente correlacionada.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Inferência, poder e plano de análise "Há poucos municípios tratados, contíguos"
**Why it matters**: Conhecimento do parecerista, não conferido nesta revisão: os procedimentos da família Conley–Taber e Ferman–Pinto usam os resíduos dos controles para aproximar a distribuição do erro dos tratados e dependem de os tratados não partilharem um choque que os controles não têm. Se a correlação espacial for forte, o número efetivo de unidades tratadas se aproxima de um, e a precisão fica superestimada mesmo com a correção por tamanho. O método de um único grupo tratado aparece só como sensibilidade.
**Suggestion**: Descrever a estatística: por exemplo, colapsar cada município à mudança do seu hiato sazonal entre referência e pós, líquida da chuva, e aplicar o procedimento sobre essa série. Tratar os tratados contíguos como um agregado, ou em blocos regionais, e comparar com blocos de controles contíguos de tamanho semelhante por permutação. Promover a análise de agregado único a co-principal, ou pré-especificar que a conclusão confirmatória exige concordância entre o procedimento principal e ela. Calcular o efeito mínimo detectável sob o procedimento mais conservador.
**Severity**: Major
**Confidence**: 4 — núcleo de competência: inferência com poucos grupos tratados; não reli os artigos citados

### W5: A separação entre a lei e o retorno das chuvas repousa numa hipótese que o texto considera frágil, sem regra para o caso de ela falhar

**Problem**: A referência (2007 a 2011) e o pós-lei (a partir de 2020) estão separados por uma seca que o texto chama de ameaça mais pesada. A especificação principal supõe efeito direto da chuva sobre o hiato comum a municípios irrigados e de sequeiro, e o grupo de comparação é, por construção, de agricultura familiar. A versão que deixa o efeito diferir é sensibilidade. Não há regra que diga qual das duas decide se divergirem. A chuva entra como medida única, do ano, linear, enquanto o canal descrito para os irrigados é a água de irrigação, que depende de estoque acumulado.
**Evidence Anchor**: text: secoes/07-ameacas.tex, A seca "tiver efeito sazonal diferente em municípios irrigados e de sequeiro"
**Why it matters**: O texto admite que, nesse caso, o coeficiente captura a diferença. Como a hipótese é a que separa o efeito da lei do fim da seca, e o desenho compara dois regimes de chuva em grupos que respondem à chuva por vias diferentes, a especificação principal é a menos protegida exatamente contra a ameaça principal. O estudo de evento não ajuda aqui: testa 2005 a 2010 contra 2011 e nada diz sobre a divergência entre 2012 e 2019, que não é testável porque o período pode já estar tratado pela suspensão dos voos.
**Suggestion**: Tornar principal a especificação com efeito da chuva por grupo, ou pré-especificar que a conclusão confirmatória exige que as duas concordem em sinal e ordem de grandeza. Acrescentar medida de disponibilidade de água de irrigação (volume de reservatório) ao lado da chuva local e permitir forma não linear. Comparar a chuva do pós-lei com a da referência e dizer o que se conclui se os dois períodos não forem comparáveis. Um placebo em municípios irrigados sem registro de aeronave, se existirem, isolaria o efeito da irrigação do efeito do voo.
**Severity**: Major
**Confidence**: 4 — núcleo de competência: identificação em diferença tripla com confundidor variante no tempo; a hidrologia do semiárido fica fora do meu assento

### W6: A regra de decisão não cobre registros parciais nem define pico sazonal

**Problem**: O quadro tem cinco linhas que não esgotam os casos. Falta o cenário que o texto trata como provável: registros obtidos em parte (alguns anos, alguns operadores, só depois do envio eletrônico, só um dos estados). Não há critério para "sem pico sazonal", para distinguir "registros mostram ausência de voos" de "registros ausentes", nem para a regra de classificação: "ao menos um ano" de voo, de qualquer cultura ou só de banana, com registros que começam em 2008 enquanto o parâmetro fala em 2007 a 2011.
**Evidence Anchor**: table: Quadro qua:regra (Regra de decisão) — linhas "Voos documentados, sem pico sazonal" e "Registros não obtidos até a data-limite"
**Why it matters**: Com poucos municípios, a entrada ou saída de um deles do grupo tratado e o deslocamento de um mês na estação mudam o coeficiente. Essas decisões serão tomadas depois de o analista ter visto variantes de grupo tratado e de limiar. Uma regra incompleta transfere essa escolha para o momento da análise.
**Suggestion**: Acrescentar a linha de registros parciais com critério de suficiência (cobertura mínima de anos e de operadores). Definir pico sazonal por estatística dos relatórios (por exemplo, concentração mínima da área aplicada em meses consecutivos). Fixar a regra de classificação por cultura e área mínima, e a sensibilidade a "ao menos dois anos". Dizer como a estação é atribuída aos municípios de comparação.
**Severity**: Major
**Confidence**: 4 — núcleo de competência: regras de decisão pré-especificadas

### W7: Os diagnósticos de identificação têm alcance menor que o enunciado e não entram na regra

**Problem**: O texto diz que os anos de 2005 a 2010 "testam" a pré-tendência. Com poucos tratados o teste tem pouco poder, cobre só o intervalo anterior à referência, e usa uma classificação cujos registros começam em 2008. O tratamento falso examina o grupo de comparação, não o contrafactual dos tratados. E a seção de diagnóstico declara que a análise confirmatória depende apenas da medição e do poder: não há consequência prevista para um estudo de evento ou um tratamento falso desfavoráveis.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Grupo de comparação "testam a pré-tendência"
**Why it matters**: Um resultado pode ser rotulado confirmatório mesmo com evidência contrária à hipótese de identificação. Não rejeitar com pouco poder não a sustenta.
**Suggestion**: Reformular como exame, não teste. Pré-especificar como os diagnósticos são lidos e reportados junto ao coeficiente: por exemplo, intervalo de sensibilidade a desvios da tendência paralela do tamanho observado no pré-período. Conhecimento do parecerista, não conferido: condicionar o teste principal a um pré-teste tem custos próprios, e por isso sugiro relato conjunto em vez de portão.
**Severity**: Minor
**Confidence**: 4 — núcleo de competência: diagnósticos de tendências paralelas

### W8: Definições da equação principal ainda permitem regressões diferentes

**Problem**: Faltam, para que dois analistas cheguem à mesma regressão: a convenção de cálculo de P_t (duração da janela, mês civil ou semanas, tratamento de meses parciais); o ano da chuva atribuído a cada coorte; se a estação é única ou varia por região, como o capítulo de ameaças sugere; se os vizinhos imediatos dos tratados ficam dentro ou fora do grupo de comparação na especificação principal; e o tratamento do mês truncado em dezembro de 2024. Pela minha conta, sob a estação provisória de fevereiro a maio e janela de nove meses por mês civil, as coortes de exposição alta nascem de agosto a dezembro e as de referência de março a maio, ambas ligadas à quadra chuvosa do ano de nascimento; já as intermediárias nascidas em janeiro e fevereiro têm o início da gestação na quadra do ano anterior, e a chuva indexada pelo ano de nascimento fica trocada para elas.
**Evidence Anchor**: equation: Eq. eq:ddd (secoes/05-metodologia.tex) — termos k_t × C_{m,a(t)} e a definição de P_t que os alimenta
**Why it matters**: Se a estação variar por município, a exposição deixa de ser função só da coorte, k×Pos e k×Seca deixam de ser absorvidos pelo efeito fixo de coorte, e a equação como escrita fica incompleta. Parte disso cabe ao plano de análise; a indexação da chuva e a unicidade da estação são da própria equação.
**Suggestion**: Dar a fórmula de P_t e uma tabela mês de nascimento por grupo sob a estação provisória; indexar a chuva pela quadra a que a coorte foi exposta; declarar que a estação é única ou reescrever a equação com os termos adicionais; dizer onde ficam os vizinhos.
**Severity**: Minor
**Confidence**: 4 — núcleo de competência: especificação de efeitos fixos; a conta dos meses é minha e não foi conferida por terceiro

### W9: O critério de concordância entre análises não discrimina

**Problem**: As análises secundárias são ditas concordantes quando sinais coincidem e intervalos se sobrepõem. Elas têm estimandos diferentes (forma reduzida atenuada pela classificação por cultura, agregado sintético, fronteira), procedimentos de inferência diferentes e, pelo próprio texto, pouco poder.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Análises secundárias e triangulação "sinais coincidem e os intervalos se sobrepõem"
**Why it matters**: Intervalos largos quase sempre se sobrepõem. O critério tende a declarar concordância em qualquer resultado e não informa a leitura do coeficiente principal.
**Suggestion**: Dizer, para cada análise secundária, que valor seria esperado sob o efeito principal (por exemplo, o principal multiplicado pela atenuação prevista) e tratar a comparação como descritiva, sem rótulo de concordância; ou adotar critério de equivalência com margem declarada.
**Severity**: Minor
**Confidence**: 4 — núcleo de competência: triangulação de estimadores

### W10: A sensibilidade duplamente robusta condiciona em outra coisa e não tem critério de acionamento

**Problem**: O referencial afirma que, quando a identificação depende de covariáveis, a regressão de efeitos fixos em geral deixa de valer na diferença tripla. A especificação principal é uma regressão de efeitos fixos com covariável variante no tempo interagida; a alternativa usa chuva média de 2007 a 2011, sem a chuva do ano, em dois períodos, e só é estimada "se o número de municípios tratados permitir", sem número.
**Evidence Anchor**: table: Quadro qua:espec (Especificações do desenho de calendário) — linha "Duplamente robusto"
**Why it matters**: As duas especificações respondem a hipóteses de identificação diferentes; divergência entre elas não tem leitura prevista, e a ausência da segunda não tem critério.
**Suggestion**: Fixar o número mínimo de tratados, declarar qual hipótese condicional cada versão mantém, e dizer por que a ressalva citada não atinge a especificação principal ou em que medida atinge.
**Severity**: Minor
**Confidence**: 3 — campo adjacente: conheço o resultado citado em linhas gerais, não o reli

### W11: A ponderação por nascimentos muda o estimando e concentra a estimativa

**Problem**: Todas as regressões são ponderadas pelo número de nascimentos da célula. Com poucos tratados de tamanhos desiguais, o coeficiente é dominado pelo maior município. A definição do parâmetro não diz se a média é por nascimento ou por município, e o peso é ele mesmo um possível desfecho, pela seleção para o nascimento vivo.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Desenho principal "Estima-se, com ponderação pelo número de nascimentos"
**Why it matters**: A leitura do coeficiente como efeito "nos municípios com aplicação aérea" pode ser, na prática, o efeito em um deles.
**Suggestion**: Declarar o estimando como média por nascimento, reportar a versão sem pesos e a exclusão de um tratado por vez, e usar pesos do período de referência.
**Severity**: Minor
**Confidence**: 4 — núcleo de competência: agregação e ponderação em painéis municipais

### W12: Afirmações de independência em relação aos dados não se conciliam com a cronologia declarada

**Problem**: O texto afirma que o período de referência "não é escolhido pelos dados" e que nenhum critério usa o desfecho do pós-lei. Mais adiante informa que a rodada de novembro estimou o desenho sobre o período inteiro, em variantes, antes deste documento. Do mesmo modo, o referencial ressalva que o contraste do análogo não é o da lei, e a regra de decisão usa os 80 g sem desconto.
**Evidence Anchor**: text: secoes/05-metodologia.tex, Período de referência "Ele não é escolhido pelos dados"
**Why it matters**: A justificativa substantiva da referência (relatos de voo e anterioridade à seca) é plausível, mas o leitor não pode aceitar a afirmação de independência como fato; a ressalva feita num trecho é ignorada em outro. É a base da nota em D3.
**Suggestion**: Trocar a afirmação por uma descrição verificável: o que foi decidido, quando, com que informação à vista, e se o período de referência foi variado nas rodadas exploratórias.
**Severity**: Minor
**Confidence**: 5 — leitura direta do texto

### Detailed Comments

#### Research Questions & Hypotheses

A pergunta é clara e respondível em princípio. H1 está redigida como contraste relativo e corresponde ao coeficiente; a definição formal do parâmetro não corresponde (W3). O estatuto das demais hipóteses (exploratórias, descritiva, falsificação) está declarado de forma consistente entre o capítulo de objetivos e o quadro de especificações.

#### Research Design

A diferença tripla de calendário é adequada à ausência de variação na data de adoção. A hipótese de identificação está enunciada corretamente como tendência paralela do hiato sazonal. O ponto fraco é o intervalo de nove ou mais anos entre referência e pós-lei, ocupado por um choque que atinge os dois grupos de modo presumivelmente diferente (W5), e o alcance limitado dos diagnósticos (W7).

#### Sampling Strategy

O grupo tratado é desconhecido no momento do projeto e pode ter de dois a sete municípios; o texto é franco quanto a isso. A regra de classificação precisa ser fechada (W6). O grupo de comparação depende de um limiar ainda aberto.

#### Data Collection

A medição dos voos por registros administrativos é a contribuição metodológica mais forte e também a maior incerteza de execução. A data-limite e o plano alternativo existem; falta o caso intermediário (W6).

#### Analysis Methods

Especificação principal bem construída (S2), com lacunas de definição (W8). Tratamento da chuva em W5. Inferência em W4. Poder em W2.

#### Results Presentation

Não se aplica: o manuscrito é um projeto e declara não trazer resultados. A consequência relevante é a não divulgação das rodadas exploratórias (W1).

#### Reproducibility

Rotinas versionadas, data de extração registrada e reestimação a partir das bases originais são compromissos adequados. Falta registro público com data verificável (W1). Aspectos éticos e sigilo estão tratados.

#### Statistical Reporting Adequacy

Julgamento sobre o relato planejado, já que não há estatísticas: `PARTLY_MEETS`. Estão previstos efeito mínimo detectável por análise, hipótese confirmatória única e procedimentos de inferência nomeados. Faltam nível de significância, poder alvo, lateralidade do teste, intervalo de confiança do coeficiente principal sob o procedimento escolhido e tratamento de células municipais sem nascimentos.

#### Methodological Fallacies Detected

Nenhuma falácia consumada, por não haver resultados. Riscos declarados e tratados pelo próprio texto: inferência ecológica (efeito municipal não é individual; o texto o diz), viés de sobrevivência (seleção para o nascimento vivo), regressão à média de um hiato achado no pré-período. Risco não resolvido: bifurcação de caminhos do analista depois de ver o desfecho (W1, W2, W6).

### Criterion-Bound Judgements

Não some, pondere nem converta estes julgamentos em recomendação por regra fixa.

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D1 methodology_rigor | contrato reviewer_full, plano de pontuação da Fase 1 | DOES_NOT_MEET | W1, W2, W3, W4, W5, W6 | Fronteira confirmatório/exploratório não verificável; portão de poder, estimando, inferência, chuva e regra de decisão com lacunas | Projeto sem resultados; parte das lacunas é legitimamente do plano de análise | Sim; reparável por reescrita e compromissos adicionais |
| D3 argumentative_coherence | contrato reviewer_full, plano de pontuação da Fase 1 | PARTLY_MEETS | W12, W3, W9 | Cadeia pergunta, estimando, método é coerente; ressalvas feitas num trecho e ignoradas em outro | O assento dono é outro | Sim, em grau menor |
| Relato estatístico planejado | references/statistical_reporting_standards.md | PARTLY_MEETS | W2, W4 | Procedimentos nomeados, parâmetros do teste ausentes | Não há estatística reportada | Não isoladamente |

### Questions for Authors

1. A rodada de novembro variou o período de referência, o limiar de exposição alta ou a exclusão de 2012 e 2019? Quais variantes exatamente foram estimadas, e o autor está disposto a reportá-las?
2. Se os relatórios de voo apontarem os mesmos municípios do Censo de 2006 e a quadra de fevereiro a maio, em que a análise confirmatória difere da já estimada, além da chuva?
3. Como o procedimento de inferência principal é aplicado ao coeficiente da interação tripla, e qual é o número efetivo de unidades tratadas que o autor considera defensável dado que são contíguas?
4. Se a especificação com efeito da chuva por grupo e a principal divergirem, qual delas sustenta a conclusão?

### Minor Issues

- A frase que liga a exclusão das coortes de 2012 e 2019 à absorção dos termos de ordem inferior sugere causalidade que não existe: a absorção decorre dos efeitos fixos, não da exclusão.
- Dezembro de 2024 é mês truncado no dia 19 e pertence ao grupo de exposição alta; dizer se entra.
- O estudo de evento usa 2005 e 2006, anteriores ao início dos registros de voo; dizer com que classificação.
- O quadro de especificações tem uma linha em branco entre "Estudo de evento" e "Perfil saturado".

## Arithmetic Receipts

no_recomputable_statistics: o manuscrito é um projeto sem estimativas; percorri resumo, capítulos 1 a 8, quadros e apêndices e não há estatística de teste com p, graus de liberdade com N, nem média ou desvio-padrão de escala discreta com N; os números presentes são contagens descritivas (36 estabelecimentos em 7 de 184 municípios; 23 pontos de coleta) e magnitudes citadas da literatura (23 a 32 g; 80 e 150 g), fora dos quatro procedimentos
