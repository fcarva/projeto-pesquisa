contract_role: domain

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "as ressalvas de transferência de um resultado externo estão listadas mas não são levadas às consequências no uso que o texto faz dele"

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### Manuscript Information

- Título: Proibição da pulverização aérea de agrotóxicos no Ceará: efeitos sobre o peso ao nascer
- Natureza: projeto de pesquisa de mestrado, sem estimativa própria
- Data do parecer: 2026-11-16
- Rodada: primeira

### Reviewer Identity

Peer Reviewer 2 (Domain). Economista ambiental e da saúde, com trabalho na literatura de exposição a agrotóxicos e desfechos ao nascer, no semiárido brasileiro e na economia da escolha de instrumentos regulatórios. O parecer cobre a fidelidade e a cobertura da literatura, a alegação de lacuna, a transferência do análogo equatoriano, a narrativa de contexto, a ancoragem de desfecho e janela de exposição, e a ponte com o segundo ensaio. Não avalio a álgebra da diferença tripla nem a inferência, que cabem ao assento de metodologia.

Limite declarado: não tive acesso aos trabalhos citados nem à web. Onde comparo o texto com a literatura de origem, uso memória de parecerista, marcada como "conhecimento do parecerista, não conferido". Nenhum achado com Severity depende só dessa memória: todos se apoiam em trecho do manuscrito ou em ausência verificável nele.

### Overall Recommendation

Minor Revision.

### Confidence Score

3. O tema está dentro da minha área, mas a conferência das magnitudes e dos contrastes dos trabalhos de origem não pôde ser feita nesta sessão.

Calibration Status: NOT_CALIBRATED

### Summary Assessment

O projeto propõe avaliar o efeito da proibição cearense da pulverização aérea sobre o peso ao nascer, com uma diferença tripla de calendário gestacional e uma regra de decisão fixada de antemão. Do ponto de vista de domínio, o texto é incomumente cuidadoso: separa substância de método, declara a natureza de cada fonte de contexto, reconhece que o químico local não é o da literatura de referência e lista as diferenças entre o caso equatoriano e o cearense. Não encontrei fonte central descrita de modo que eu possa demonstrar incompatível com o que ela reporta, nem alegação de lacuna em termos absolutos.

A fragilidade principal está no uso que a regra de decisão faz do análogo. O texto lista as ressalvas de transferência (doença, frequência de ciclos, contraste intensivo contra habitual, raio de 150 metros) e afirma que a intensidade não foi convertida, mas a regra adota um único valor, cerca de 80 gramas, como efeito plausível, e esse valor estima um contraste diferente do que o coeficiente de interesse mede. As demais observações são de menor alcance: delimitação da busca que sustenta a lacuna, evidência química vinda de amostras de água, ancoragem da janela gestacional em um único estudo, escolha do peso médio diante da concentração na cauda, e afirmações técnicas sobre deriva sem fonte.

Recomendo revisão menor porque o achado principal se resolve reescrevendo a regra de decisão e o cálculo de poder, sem dado novo; ele precisa estar resolvido antes do congelamento do plano de análise.

### S1: Natureza das fontes de contexto declarada, com distinção entre relato e registro

O Capítulo 2 atribui cada afirmação à sua fonte (censo, lei, dossiê, reportagem), reconhece que os relatos de frequência divergem e não promove relato a fato. Isso é o que a narrativa de contexto precisa para ser auditável, e é raro em projetos.
**Evidence Anchor**: text: secoes/02-contexto.tex "Há relato de pico sazonal, não registro dele."

### S2: Reconhecimento de que a literatura de referência não transfere no mecanismo

O texto não importa o mecanismo do glifosato em grãos transgênicos para um caso de fungicida em fruticultura, e escolhe o análogo pela cultura e pelo método. A divisão "substância contra método" organiza a literatura citada sem forçar a comparação.
**Evidence Anchor**: text: secoes/02-contexto.tex "Os desenhos de referência transferem na forma, não no mecanismo"

### S3: Ressalvas de transferência do análogo explicitadas

O texto diz que a fumigação equatoriana é mais frequente, que a intensidade não foi convertida e que o contraste da lei não é o do artigo. As diferenças que condicionam a transferência estão à vista do leitor; o que falta é levá-las à regra de decisão (W1).
**Evidence Anchor**: text: secoes/03-referencial.tex "O valor serve de referência, e não de limite"

### S4: Enquadramento de externalidade proporcional à entrega

A seção sobre externalidade e escolha de instrumento ocupa um parágrafo, remete a comparação entre instrumentos ao segundo ensaio e não promete mais do que uma estimativa em intenção de tratar sobre um desfecho.
**Evidence Anchor**: text: secoes/03-referencial.tex "um insumo parcial: uma estimativa, em intenção de tratar"

### S5: Ameaças do desenho de calendário ancoradas na literatura pertinente

A sazonalidade da composição materna, a sazonalidade do peso entre irmãos e o efeito próprio da chuva no semiárido são trazidos das fontes adequadas e tratados como ameaças de primeira ordem, não como nota de rodapé.
**Evidence Anchor**: text: secoes/03-referencial.tex "o que faz da seca um confundidor de primeira ordem neste projeto"

### W1: O efeito plausível da regra de decisão é um valor único que estima outro contraste

**Problem**: A regra de decisão toma cerca de 80 gramas, da especificação principal do análogo equatoriano, multiplica pela fração de nascimentos exposta e compara com o efeito mínimo detectável; o valor central da grade decide se o teste é confirmatório. Três diferenças que o próprio texto declara não entram nessa conta. (a) Segundo o Capítulo 3, os 80 gramas comparam fumigação intensiva por três meses ou mais com fumigação habitual; a lei contrasta voo com ausência de voo. (b) O texto afirma que a fumigação equatoriana tem vinte ou mais ciclos por ano, contra dois a oito nos relatos cearenses, e que a intensidade não foi convertida. (c) O coeficiente de interesse compara coortes expostas no início da gestação com coortes expostas apenas no terceiro trimestre, e o texto admite que ele subestima o efeito se a exposição tardia causar dano; os 80 gramas não são uma estimativa dessa diferença entre início e fim. A grade prevista varia só a fração exposta, não a magnitude.
**Evidence Anchor**: text: secoes/05-metodologia.tex, seção Regra de decisão "O efeito plausível é o da especificação principal do análogo equatoriano, cerca de 80 gramas, multiplicado pela fração de nascimentos exposta"
**Why it matters**: A regra de decisão é o que o projeto apresenta como compromisso prévio, e ela separa "desenho confirmatório" de "desenho reportado como limite". Se o valor importado superestima o que o coeficiente pode capturar (menos ciclos, desconto do efeito tardio), o projeto roda como confirmatório um teste sem poder para o efeito realmente plausível; se subestima (contraste voo contra nenhum voo), descarta um teste viável. As ressalvas (a) e (b) puxam em sentidos opostos, e o texto não diz qual domina. Usar o resultado externo fora do contraste que a fonte, tal como descrita pelo próprio manuscrito, autoriza é o ponto central do meu assento.
**Suggestion**: Trocar o valor único por uma grade em duas dimensões, magnitude individual e fração exposta, com a faixa de magnitude justificada pelas diferenças listadas (por exemplo, do efeito por ciclo ou por mês de exposição, se o artigo de origem permitir extraí-lo, ao limite superior de 150 gramas que o texto já cita). Declarar qual parcela do efeito por gestação o contraste início contra fim pode recuperar, usando a estimativa de terceiro trimestre do próprio análogo, ainda que imprecisa, como cenário. Dizer na regra o que decide quando os cenários de magnitude discordam. Nada disso exige dado novo nem altera o período de referência.
**Severity**: Major
**Confidence**: 4 — área central (transferência de magnitudes entre estudos de exposição); a descrição do contraste do artigo de origem é a do manuscrito, não conferida na fonte.

### W2: A alegação de lacuna é delimitada por "literatura consultada", mas a consulta não é descrita

**Problem**: A formulação é adequadamente cautelosa, e não absoluta. Falta dizer o que foi consultado: bases, idiomas, termos, data. Além disso, o texto passa da forma cautelosa para formas mais fortes ("O que nenhum desses trabalhos oferece", "não se conhece estimativa causal") sem acrescentar base. A seção de antecedentes não menciona restrições ou proibições de pulverização aérea fora do Brasil, que são o lugar natural onde uma avaliação anterior de proibição de método existiria.
**Evidence Anchor**: text: secoes/01-introducao.tex "não se localizou, na literatura consultada, avaliação causal dos efeitos dessa resposta"
**Why it matters**: A primeira camada da contribuição alegada, a de objeto, depende de a lacuna existir. Uma banca pode aceitar a cautela, mas precisa saber o alcance da busca para julgar a originalidade.
**Suggestion**: Acrescentar uma frase com o protocolo da busca e a data, e um parágrafo curto sobre precedentes regulatórios de método em outros países, dizendo se foram avaliados. Pistas, conhecimento do parecerista, não conferido, a verificar antes de qualquer uso: a Diretiva 2009/128/CE da União Europeia restringe a pulverização aérea com derrogações; houve portaria municipal contra a pulverização aérea em bananais em Davao, nas Filipinas; e há literatura de avaliação de banimentos de moléculas sobre desfechos de saúde (ver sugestões ao final). Não afirmo que qualquer delas contenha avaliação causal de proibição de método; são onde eu procuraria. [FIELD-NORM UNVERIFIED]
**Severity**: Minor
**Confidence**: 3 — conheço a literatura econômica próxima; não tenho como atestar a inexistência de avaliação anterior.

### W3: A evidência sobre o químico vem de amostras de água, em citação de segunda mão, e não identifica o que o avião aplicava

**Problem**: O perfil químico que distingue o caso (procimidona e carbaril em todos os pontos, glifosato em poucos) é tirado de uma tabela de análises de água de 2009 reproduzida na justificativa de um projeto de lei e "atribuída" ao Dossiê ABRASCO. Dois limites não são tirados. Resíduo em água reflete todas as aplicações da bacia, terrestres e aéreas, em todas as culturas irrigadas, e não o que era aplicado por aeronave em bananal. E a fonte é de segunda mão, embora o Dossiê seja citado diretamente, com página, em outro ponto do mesmo capítulo. Há ainda uma assimetria: a única evidência química do projeto é do canal hídrico, que o Capítulo 6 retira da análise.
**Evidence Anchor**: text: secoes/02-contexto.tex "registra 23 pontos de coleta na Chapada em 2009"
**Why it matters**: A conclusão de que os desenhos de referência "transferem na forma, não no mecanismo" e a escolha do análogo pela fumigação de bananais apoiam-se nesse perfil. A conclusão provavelmente se sustenta por outras vias (a doença fúngica da folha, nomeada nas reportagens), mas o texto não deveria inferir a calda do avião a partir da água. Conhecimento do parecerista, não conferido: os ativos listados não são os tipicamente associados ao controle de sigatoka em banana, o que reforça que a tabela descreve o conjunto da fruticultura irrigada, não a aplicação aérea.
**Suggestion**: Citar a tabela na fonte primária (o Dossiê, com página, ou o estudo que o Dossiê reproduz). Dizer explicitamente que ela documenta contaminação hídrica agregada e não a composição da aplicação aérea. Indicar que os relatórios mensais pedidos, que segundo o texto trazem cultura e produto, são a fonte que responderá a essa pergunta.
**Severity**: Minor
**Confidence**: 3 — a leitura do que uma amostra de água identifica é segura; a observação agronômica sobre os ativos é de memória.

### W4: A janela dos dois primeiros trimestres está ancorada em um único estudo, cuja estimativa de terceiro trimestre é imprecisa, não nula

**Problem**: A exposição é definida pela fração dos dois primeiros trimestres na estação, e a referência são as coortes com apenas o terceiro trimestre exposto. O apoio citado é o análogo equatoriano, que, segundo o texto, encontra efeito nos dois primeiros trimestres e estimativa imprecisa no terceiro. Imprecisão não é evidência de ausência. O segundo trabalho citado para o calendário usa o mês da concepção e trata de agroquímicos na água, canal que este projeto exclui. Não há referência toxicológica ou epidemiológica sobre o período sensível para as classes químicas que o próprio Capítulo 2 lista.
**Evidence Anchor**: text: secoes/03-referencial.tex "encontram efeito nos dois primeiros trimestres e estimativa imprecisa no terceiro"
**Why it matters**: O texto declara o limite (o coeficiente subestima o efeito se a exposição tardia causar dano) e prevê uma especificação exploratória de terceiro trimestre, o que é correto. O problema de domínio é que a escolha da referência não está apoiada em evidência de que o terceiro trimestre seja de fato menos sensível para peso ao nascer. Conhecimento do parecerista, não conferido: em outras literaturas de exposição gestacional o ganho de peso fetal concentra-se no fim da gestação e efeitos de terceiro trimestre sobre peso são comuns.
**Suggestion**: Reportar, do artigo de origem, as estimativas pontuais e os intervalos por trimestre, e não apenas o adjetivo. Acrescentar uma ou duas referências sobre período sensível para peso ao nascer sob exposição a fungicidas ou a agrotóxicos em geral, ou declarar que não foram encontradas. Ligar essa incerteza à faixa de magnitude da regra de decisão (W1).
**Severity**: Minor
**Confidence**: 3 — domínio próximo; a caracterização do terceiro trimestre no artigo de origem é a do manuscrito.

### W5: O peso médio é o desfecho confirmatório sem justificativa, depois de o texto recomendar desconfiança de efeitos médios

**Problem**: A revisão destaca que os efeitos aparecem no topo da distribuição de exposição e na cauda inferior do peso esperado, e conclui que isso "recomenda desconfiar de efeitos médios". O Capítulo 6 fixa o peso médio como desfecho confirmatório e deixa baixo peso e prematuridade como exploratórios, sem dizer por quê. A diluição pela fração exposta é tratada; a escolha entre média e cauda não é.
**Evidence Anchor**: absence: secoes/06-dados.tex, parágrafo Desfechos — expected justificativa da escolha do peso médio como desfecho confirmatório diante da concentração na cauda destacada no Capítulo 3; checked Cap. 3 (segunda regularidade), Cap. 4, Cap. 5 (inferência, poder e plano de análise), Cap. 6 e Cap. 7
**Why it matters**: Pode haver boa razão (uma proporção rara em células municipais pequenas tem menos poder que a média; o análogo reporta o efeito em gramas), mas o leitor fica com uma tensão entre a segunda regularidade e a escolha do desfecho.
**Suggestion**: Acrescentar duas frases que justifiquem a média como confirmatória e digam como a concentração na cauda será lida nos exploratórios. Se os microdados permitem, considerar um desfecho de cauda construído no nível individual antes da agregação, como exploratório declarado.
**Severity**: Minor
**Confidence**: 4 — ponto de coerência entre a literatura citada e a escolha de desfecho.

### W6: Afirmações técnicas sobre deriva sem fonte

**Problem**: O texto invoca "a literatura técnica" para definir deriva e afirma que ela "opera em escala de centenas de metros", usando essa escala para dizer que a interferência entre municípios por essa via deve ser pequena. Nenhuma referência técnica sobre distância e determinantes da deriva em aplicação aérea aparece. O único número de distância citado é o raio de 150 metros do análogo, que é um resultado de saúde, não uma medida de deposição.
**Evidence Anchor**: absence: secoes/01-introducao.tex e secoes/05-metodologia.tex (seção Interferência e versões do tratamento) — expected referência técnica sobre distância e determinantes da deriva em aplicação aérea; checked Cap. 1, Cap. 2, Cap. 3, Cap. 5 e a lista de referências
**Why it matters**: A escala da deriva sustenta dois argumentos do projeto: a diluição dentro do município e a pequena interferência entre municípios. Ela varia com altura de voo, tamanho de gota, vento e formulação, e a deposição a distâncias maiores que centenas de metros é documentada para aplicação aérea (conhecimento do parecerista, não conferido).
**Suggestion**: Citar uma fonte técnica ou regulatória para a escala, ou enfraquecer a frase. As distâncias mínimas que o texto diz constarem da lei municipal de 2010 e da instrução normativa federal já citada são, elas próprias, um dado regulatório sobre a escala presumida e poderiam ser reportadas. [FIELD-NORM UNVERIFIED]
**Severity**: Minor
**Confidence**: 3 — área adjacente (agronomia de aplicação).

### W7: As magnitudes que alimentam a regra de decisão são citadas sem localizador

**Problem**: Os números do análogo (cerca de 80 gramas, até 150, raio de 150 metros, três meses ou mais, vinte ou mais ciclos por ano) são dados sem tabela, coluna ou página, embora o texto use localizador de página para o Dossiê. Como artigos desse tipo costumam ter versões de trabalho com números diferentes dos publicados, a ausência de localizador impede a conferência.
**Evidence Anchor**: text: secoes/03-referencial.tex "80 gramas na especificação principal, e de até 150 conforme a exposição"
**Why it matters**: É o parâmetro numérico de que a regra de decisão depende. Não tenho base para dizer que os números estão errados; digo que não são conferíveis como estão, e que minha lembrança das magnitudes desse artigo não é segura o bastante para confirmá-los.
**Suggestion**: Indicar tabela e coluna da versão publicada para cada número, e o mesmo para a faixa de 23 a 32 gramas do estudo norte-americano.
**Severity**: Minor
**Confidence**: 4 — prática de citação de magnitudes; sem acesso à fonte.

### W8: A documentação prévia da exposição à deriva na Chapada é afirmada sem citação

**Problem**: O Capítulo 2 diz que a exposição da população à deriva foi documentada antes da proibição, e a Introdução descreve aviões sobre plantações vizinhas a casas, escolas e açudes, sem fonte em nenhum dos dois pontos. O restante do capítulo é rigoroso em atribuir cada afirmação; esta, que é a premissa factual do caso, não é atribuída.
**Evidence Anchor**: text: secoes/02-contexto.tex "onde a exposição da população à deriva foi documentada antes da proibição"
**Why it matters**: É a afirmação que liga o método aéreo à exposição humana no local do estudo. O Dossiê e o estudo ecológico já citados talvez a sustentem, mas o texto não os invoca aqui.
**Suggestion**: Citar a fonte com página e dizer o que foi documentado (resíduo em água, relato de moradores, medição de deposição, biomonitoramento), já que a natureza da documentação importa para o mecanismo.
**Severity**: Minor
**Confidence**: 4 — verificação direta no texto.

### Detailed Comments

**Cobertura e organização da literatura.** A divisão entre substância e método funciona e os cinco trabalhos empíricos centrais são os que eu esperaria. As descrições de Dias, Rocha e Soares, de Reynier e Rubin, de Larsen e coautores, de Rocha e Soares e de Brainerd e Menon são compatíveis com o que lembro desses trabalhos (conhecimento do parecerista, não conferido). Duas descrições merecem conferência pelos autores porque não consigo confirmá-las de memória: a de que Jones (2020) é "dos poucos estudos em que fungicidas têm peso na variação explorada", e os números do análogo equatoriano (W7). Camacho e Mejía são citados sem resultado; pela minha lembrança, não conferida, o trabalho reporta efeito sobre abortos espontâneos, o que seria diretamente pertinente à ameaça de seleção para o nascimento vivo que o Capítulo 7 discute.

**Alegação de lacuna.** Formulada com cautela adequada; falta o alcance da busca (W2).

**Transferência do análogo.** O texto lista corretamente as diferenças. O defeito está em não as levar à regra de decisão (W1). A diferença de doença é mencionada ("a doença combatida não é a mesma") sem nomear a do caso equatoriano; nomeá-la ajudaria o leitor a julgar a diferença de frequência de ciclos.

**Narrativa de contexto.** É o ponto mais forte do texto em termos de disciplina de fonte (S1). As duas exceções são W3 e W8. O Capítulo 2 menciona banana e melão como culturas da Chapada, e o desenho segue apenas com a banana; como o Censo de 2006 não distingue cultura, vale uma frase sobre por que o melão sai e sobre o que isso implica para a estação de pulverização, que o texto já promete verificar nos relatórios.

**Mecanismo e desfecho.** Ver W4 e W5. O estudo ecológico de Rigotto e coautores está sob a "primeira regularidade" (ordem de grandeza e proximidade), mas, como descrito, trata de internações por neoplasias e de óbitos fetais; caberia melhor no contexto ou na discussão de seleção.

**Ponte com o segundo ensaio.** Proporcional (S4). Uma precisão: Helfand e House é citado para a "dimensão distributiva" da escolha de instrumento; pela minha lembrança, não conferida, o artigo trata de instrumentos uniformes contra diferenciados sob condições heterogêneas, o que é heterogeneidade e não distribuição. Se for assim, a frase deve separar as duas ideias.

### Missing Key References

Todas as indicações abaixo são sugestões a verificar pelos autores antes de qualquer uso; são conhecimento do parecerista, não conferido nesta sessão, e nenhuma é condição para aceitação.

- Pignati, Machado e Cabral (2007), sobre o episódio de deriva de pulverização aérea em Lucas do Rio Verde: antecedente brasileiro de saúde coletiva sobre o método, pertinente a W8.
- Gunnell e coautores (2007), sobre regulação de agrotóxicos e suicídio no Sri Lanka: exemplo de avaliação posterior de banimento de moléculas sobre desfecho de saúde, pertinente a W2 e ao contraste que acompanha a hipótese de substituição.
- Frank (2024), sobre aumento de inseticidas após perda de controle biológico e mortalidade infantil: literatura econômica recente de exposição a agrotóxicos e saúde infantil, fora do eixo do glifosato.
- Skidmore, Sims e Gibbs (2023), sobre intensificação agrícola e câncer infantil no Brasil: evidência brasileira de exposição por via hídrica.

~~~yaml suggested-references
- title: "Acidente rural ampliado: o caso das chuvas de agrotóxicos sobre a cidade de Lucas do Rio Verde - MT"
  authors: ["Pignati, W. A.", "Machado, J. M. H.", "Cabral, J. F."]
  year: "2007"
  doi: null
  arxiv_id: null
- title: "The impact of pesticide regulations on suicide in Sri Lanka"
  authors: ["Gunnell, D."]
  year: "2007"
  doi: null
  arxiv_id: null
- title: "The economic impacts of ecosystem disruptions: Costs from substituting biological pest control"
  authors: ["Frank, E. G."]
  year: "2024"
  doi: null
  arxiv_id: null
- title: "Agricultural intensification and childhood cancer in Brazil"
  authors: ["Skidmore, M. E.", "Sims, K. M.", "Gibbs, H. K."]
  year: "2023"
  doi: null
  arxiv_id: null
~~~

### Questions for Authors

1. Os 80 gramas da especificação principal do análogo referem-se a exposição em qual período da gestação e a qual contraste exato? Qual é a estimativa pontual, com intervalo, para o terceiro trimestre? Indiquem tabela e coluna da versão publicada.
2. Com base em que a grade de frações de nascimentos expostas será construída, se a residência não é observada e a aproximação pelo cadastro de endereços fica como extensão?
3. Para quais culturas voavam as aeronaves dos 7 municípios do Censo de 2006? Se parte servia a culturas de estação seca, a estação de pulverização relevante pode não ser a quadra chuvosa.
4. A caracterização de Jones (2020) como estudo em que fungicidas têm peso na variação explorada foi conferida no artigo?
5. O que exatamente foi documentado sobre a exposição da população à deriva na Chapada antes de 2019, e por qual método?

### Minor Issues

- A Introdução descreve os voos no presente ("aviões sobrevoam") para uma prática que o próprio texto diz proibida desde 2019 e possivelmente suspensa desde 2012.
- A doença combatida no caso equatoriano não é nomeada.
- Camacho e Mejía aparecem sem resultado reportado.
- O estudo de Rigotto e coautores está alocado na regularidade de "ordem de grandeza", à qual não se refere.
- A citação de Helfand e House para "dimensão distributiva" merece conferência.
- A chave da referência ao documento de consolidação do SINASC indica 2011 e a entrada sai com 2013; o texto cita o ano da troca de formulário, o que pode confundir o leitor.
