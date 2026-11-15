# Field Analysis Report (v2)

Estágio 3 (REVIEW) do academic-pipeline, rodada 20 — Fase 0 do `academic-paper-reviewer`, modo `full`, refeita para o **projeto_v2**.
Agente: `field_analyst_agent` (ARS v3.24.2). Data: 2026-11-15.
Manuscrito lido no commit `8922a12f06b22dd7cf0c49193888490defa106d5` (2026-11-15 23:01 UTC, "integridade do projeto v2 — PASS WITH NOTES (rodada 2)"), com a árvore de trabalho limpa em `paper/`.
Este relatório substitui `phase0_field_analysis.md`, que foi escrito sobre a versão anterior do manuscrito, não foi aceito pelo pesquisador e fica preservado sem alteração. Nenhum cartão daquele arquivo deve ser usado.
Este relatório configura o painel. Não avalia mérito, não despacha parecerista e não altera o manuscrito.

## Cobertura da leitura

**Relido por inteiro no estado atual (fonte `.tex`, inclusive comentários de cabeçalho):**

| Arquivo | Conteúdo |
|---|---|
| `paper/projeto/projeto.tex` | Preâmbulo, metadados, capa, ordem das seções (agora carrega `tikz`) |
| `secoes/01-introducao.tex` | Cap. 1: abertura, pergunta, Antecedentes, Justificativa, Contribuição |
| `secoes/02-contexto.tex` | Cap. 2: a lei; Chapada, cultura e químico; "O que se sabe sobre onde e quando havia avião" |
| `secoes/03-referencial.tex` | Cap. 3: externalidade (um parágrafo); agrotóxicos e saúde ao nascer; avaliação de política simultânea |
| `secoes/04-objetivos.tex` | Cap. 4: objetivo geral, cinco específicos, H1–H5 |
| `secoes/05-metodologia.tex` | Cap. 5: 5.1 parâmetro-alvo e cadeia causal; 5.2 desenho principal (diferença tripla de calendário, grupo de comparação, chuva); 5.3 diagnóstico de abertura; 5.4 medição do método; 5.5 interferência e versões do tratamento; 5.6 análises secundárias e triangulação; 5.7 regra de decisão; 5.8 inferência, poder e plano de análise |
| `secoes/06-dados.tex` | Cap. 6: unidade e período, fontes, desfechos, exposição, escopo, reprodutibilidade, ética |
| `secoes/07-ameacas.tex` | Cap. 7: quadro de ameaças e três comentários (seca, diluição, sazonalidade) |
| `secoes/08-cronograma.tex` | Cap. 8: resultados esperados e cronograma |

**Quadros lidos (5, todos):** Quadro 1, cronologia legal (`qua:cronologia`, cap. 2; ganhou as linhas de 2012–2017 e de 03/2018); Quadro 2, regra de decisão (`qua:regra`, seção 5.7; refeito); Quadro 3, fontes de dados (`qua:fontes`, cap. 6; ganhou Censo Agropecuário 2017 e precipitação); Quadro 4, ameaças e respostas (`qua:ameacas`, cap. 7; refeito, nove linhas); Quadro 5, cronograma por bimestre (`qua:cronograma`, cap. 8; refeito).

**Figura lida (1):** Figura 1, diagrama causal do desenho de calendário (`fig:dag`, seção 5.2). Li o código TikZ (nós, setas, estilos e a nota de fonte), não a imagem renderizada: sei quais nós e setas existem e quais são tracejados, mas não conferi a legibilidade nem a disposição no PDF.

**Equações lidas (3, todas no cap. 5):** (1) `ATT` condicionado a `A_m = 1` e `S_t = 1` (seção 5.1); (2) especificação da diferença tripla, `eq:ddd` (seção 5.2); (3) `θ = VPP × ATT`, `eq:atenuacao` (seção 5.6). A equação de tendências paralelas por dose da versão anterior não existe mais. Não há tabelas numéricas.

**Bibliografia:** reli por inteiro `paper/projeto/referencias-projeto.bib` (agora 27 entradas; 8 novas: `jones2020invasive`, `rigotto2013trends`, `hagemann2025single`, `limoeiro2010lei1511`, `agenciabrasil2016ceara`, `ceara2018nascer`, `ibge2017censoagro`, `globorural2021bananais`). `paper/referencias.bib` (47 entradas) foi lido por inteiro na passada anterior e não tem diferença nos commits recentes; não o reli linha a linha. O texto cita 44 chaves distintas (conferido contra `projeto.bbl`, 44 `\bibitem`): as 27 do arquivo do projeto e 17 do geral. Dessas 44, 28 são artigos, working papers ou preprints e 16 são fontes normativas, judiciais, estatísticas ou de imprensa. Em relação à versão anterior, saíram das citações `skevas2012`, `cameron2008wild`, `rambachan2023credible` e `roth2023trending`; entrou `canay2021wild`.

**Não lido / não feito:**
- Não li o PDF compilado página a página; usei-o só para contar páginas (21) e palavras e para conferir que sua data (23:01 UTC) coincide com a do commit.
- Não abri nenhuma das obras citadas nem as URLs das fontes de imprensa e institucionais. O cabeçalho do `.bib` diz, sobre as fontes documentais novas, "títulos de notícia tomados do endereço; conferir"; registro isso como declaração do autor, não como fato verificado por mim.
- Não li os documentos que os comentários da fonte apontam como origem do redesenho (`docs/pdf/2026-11-10-desenho-consolidado-chapada-sutva-dags.pdf`, `2026-11-10-dags-ensaio1.pdf`), nem `docs/ars/20-...`, os relatórios do Estágio 2.5, o plano de análise versionado, `paper/main.tex`, scripts ou dados.
- Não li `references/top_journals_by_field.md`: o arquivo de agente não o exige e não há alvo a resolver.
- Não conheço as normas do PPGEco/UFES para projeto de pesquisa.

**Lista de mudanças recebida no despacho:** conferi item a item no texto e todos se confirmam: diferença tripla de calendário como desenho principal, com interação por chuva (5.2); comparação com municípios de banana predominantemente familiar sem registro de aeronave, usados também como tratamento falso (5.2, H4); diagnóstico sazonal no pré-período (5.3); seção de interferência e versões (5.5); Figura 1; forma reduzida por dose como análise secundária (5.6); seca como ameaça central (cap. 7); H1–H5 (cap. 4); Quadros 2 e 5 refeitos. Mudanças que a lista não mencionava e que o painel precisa saber: o painel recua a 2005 (cap. 6); a janela gestacional do desenho passou a ser os dois primeiros trimestres, com o terceiro como contraste (5.2, H3); há um desfecho composto de nascidos vivos e óbitos fetais (cap. 6); há uma comparação de fronteira com municípios potiguares e pedido de registros também para o Rio Grande do Norte (5.4, 5.6); a caracterização de Calzada et al. mudou (cerca de 80 g, até 150 m do bananal; cap. 3); a contextualização de Limoeiro do Norte e os relatos de 2016 e 2021 sobre a persistência dos voos são novos (2.3); o referencial de escolha de instrumento foi reduzido a um parágrafo (3.1).

**Texto dirigido ao painel:** não encontrei no manuscrito nenhuma instrução dirigida a pareceristas. Os comentários `%` da fonte são notas do autor para si (por exemplo, no cap. 8: as datas do cronograma são "uma PROPOSTA"); não aparecem no PDF que a banca lê.

## Paper Basic Information

- **Title**: Proibição da pulverização aérea de agrotóxicos no Ceará: efeitos sobre a saúde ao nascer
- **Tipo de documento**: projeto de pesquisa de mestrado (PPGEco/UFES), em português, abnTeX2. Plano de pesquisa com elementos de plano de pré-análise; sem resultados.
- **Abstract length**: não há resumo nem abstract no documento (0 palavras).
- **Full text length**: cerca de 6.000 palavras de corpo na fonte (contagem aproximada, sem comandos LaTeX); cerca de 7.900 palavras no PDF de 21 páginas, incluídos capa, sumário e referências.
- **Number of references**: 44 citadas.

## Field Analysis

| Dimension | Analysis Result |
|-----------|----------------|
| Primary Discipline | Economia aplicada: avaliação de impacto causal de política pública (microeconometria aplicada), na interseção de economia ambiental e economia da saúde |
| Secondary Disciplines | Epidemiologia ambiental e perinatal (janela gestacional de exposição, peso ao nascer, óbito fetal, sazonalidade de nascimentos); agronomia e ciência da exposição (aviação agrícola, fitossanidade da banana, clima do semiárido); direito e administração pública (regulação estadual, registros administrativos, acesso à informação) |
| Research Paradigm | Quantitative Research (desenho observacional com dados administrativos secundários; estágio de plano, sem estimativas) |
| Methodology Type | Experimental / Quasi-experimental (quase-experimental: diferença tripla de calendário gestacional como desenho principal, com modificação de efeito por chuva e grupo de tratamento falso; DiD com tratamento contínuo, controle sintético/SDiD e comparação de fronteira como análises secundárias), com componente de Policy Analysis e uma etapa de medição documental do tratamento |
| Target Journal Tier | `criteria_binding_unavailable`. Não há periódico nem outro alvo confirmado pelo autor; o destinatário é o orientador e a banca do programa. Nenhum tier é atribuído. Observação de campo, sem vínculo a veículo: o texto usa o vocabulário corrente da microeconometria aplicada recente (parâmetro-alvo, diagrama causal, hipótese de identificação nomeada, interferência, inferência com poucos tratados, poder calculado antes da estimação). |
| Paper Maturity | Pre-submission, entendido como "versão para entrega à banca", com ressalvas. Base (só estrutura, citação e acabamento, não mérito): oito capítulos completos e encadeados, cinco quadros e uma figura com fonte, três equações numeradas, citações em formato ABNT resolvidas no `.bbl`, linguagem acabada. Ressalvas visíveis: não há resumo; o texto é uma reescrita do mesmo dia, cujo desenho principal o próprio documento diz que ainda será "ratificado com o orientador" (5.8); fatos centrais do contexto são declarados como relatos de imprensa ou de fonte secundária (2.3, fonte do Quadro 1); as datas do cronograma estão marcadas na fonte como proposta. |

## Recommended Target Journals (Top 3)

Não se aplica. O manuscrito é um projeto de pesquisa de mestrado, não um artigo; o autor não confirmou periódico nem outro alvo; e a instrução de despacho veda nomear alvos. Nenhum periódico é recomendado, e nenhum critério de veículo deve ser inferido pelos pareceristas.

## Reviewer Configuration Cards

Os quatro cartões abaixo cobrem os assentos configuráveis. O quinto assento, Devil's Advocate, é fixo e não recebe cartão. Os cartões dizem o que checar e onde; não antecipam conclusões. As quatro identidades da versão anterior foram mantidas, com ajuste de especialidade nos Cartões 2 e 4; os focos foram reescritos para o desenho atual.

Divisão de território, para evitar sobreposição:
- **Cartão 1**: o documento como projeto (pergunta, coerência interna, escopo, viabilidade no prazo, completude formal).
- **Cartão 2**: identificação, especificação, inferência, poder e pré-compromisso (cap. 5, eqs. 1–3, Figura 1, Quadro 2, parte econométrica do Quadro 4).
- **Cartão 3**: literatura, enquadramento econômico, hipóteses e desfechos de saúde, registros do DATASUS (caps. 1, 3, 4, 6).
- **Cartão 4**: a realidade física, agronômica, climática e administrativa do tratamento e do grupo de comparação (cap. 2, seções 5.4 e 5.5, comentários do cap. 7, linhas de fonte dos Quadros 1 e 3).

### Reviewer Configuration Card #1

**Role**: EIC
**Display role**: Journal-Fit Reviewer
**Identity Description**: Professor de pós-graduação em Economia com experiência em bancas de projeto e de qualificação de mestrado em economia aplicada, leitor generalista de avaliação de políticas públicas (não especialista em agrotóxicos nem nos estimadores usados). Como não há veículo confirmado (`criteria_binding_unavailable`), o "fit" avaliado é o de um projeto de mestrado perante orientador e banca, em termos gerais de campo; este assento não escolhe periódico substituto nem presume normas específicas do PPGEco/UFES.
**Review Focus**:
  1. Clareza e constância da pergunta: conferir se a pergunta em negrito do cap. 1 e o objetivo geral do cap. 4 (efeito nos "municípios onde a prática existia") dizem a mesma coisa que o parâmetro-alvo da seção 5.1 (efeito sobre coortes gestadas na estação de pulverização, "e não sobre municípios"), que H1–H2 e que os resultados esperados (i)–(iv) do cap. 8. Registrar onde a população, o desfecho ou o contraste mudam de uma formulação para outra.
  2. Rastreabilidade objetivo → hipótese → análise → dado → atividade: para cada um dos cinco objetivos específicos e cada uma das cinco hipóteses, localizar a seção do cap. 5 que os atende, a linha do Quadro 3 que os alimenta e a linha do Quadro 5 que os agenda. Registrar elos ausentes, com atenção ao que o texto menciona fora do Quadro 3 (dados do Rio Grande do Norte e de doadores externos para a fronteira e o controle sintético; arboviroses notificadas citadas no Quadro 4) e ao que aparece no Quadro 3 sem uso descrito no cap. 5 (FAO-GAEZ).
  3. Viabilidade e escopo no prazo: ler o Quadro 5 contra o Quadro 2. Checar se o diagnóstico sazonal e a classificação pelo método (bimestres 2–3) podem ocorrer antes do retorno dos pedidos de acesso protocolados no bimestre 1; o que o cronograma prevê se os registros não chegarem; se uma lista que soma desenho principal, três análises secundárias, três grupos de interferência, painel de 2005 a 2024 e um segundo ensaio (bimestres 5–6) é declarada como cabível em seis bimestres.
  4. Contribuição e significância declaradas: checar se as três camadas da seção "Contribuição" (objeto, medida, identificação) descrevem o desenho atual e se cada uma sobrevive nas quatro linhas do Quadro 2, inclusive na última ("sem estimativa de efeito da pulverização"), que o cap. 8 apresenta como entrega válida.
  5. Completude e estado do documento: ausência de resumo e de seção de orçamento/recursos; adequação do título a um projeto que admite cenário sem estimativa de efeito; e o estatuto de um desenho principal que a seção 5.8 declara ainda a ser "ratificado com o orientador". Registrar como pontos a confirmar pelo autor e pelas normas do programa, que este assento não conhece.
**Will particularly care about**: Se um membro de banca que lê só os caps. 1, 4 e 8 entende o que será entregue em cada cenário e quando, e se percebe qual análise é a principal. Se o documento distingue com clareza o que é desenho, o que é fato conferido e o que é relato.
**Possible blind spots**: Não tem como julgar se a hipótese de identificação da diferença tripla é suficiente nem se a especificação a implementa (Cartão 2). Tende a aceitar a caracterização da literatura como dada (Cartão 3) e a tomar a obtenção dos registros e a premissa agronômica como questões só de prazo (Cartão 4). Pode confundir acabamento de redação com solidez do desenho.

### Reviewer Configuration Card #2

**Role**: Peer Reviewer 1
**Display role**: Peer Reviewer 1
**Identity Description**: Econometrista aplicado especializado em diferenças-em-diferenças e diferença tripla com poucas unidades tratadas, em desenhos de calendário ou sazonalidade de exposição, em inferência com poucos grupos (Conley–Taber, Ferman–Pinto, inferência conformal, Hagemann, Canay–Santos–Shaikh), em interferência entre unidades e em DiD com tratamento contínuo e erro de classificação; com prática em diagramas causais, planos de pré-análise e cálculo de poder para painéis município × mês.
**Review Focus**:
  1. Coerência entre parâmetro-alvo, diagrama e especificação: comparar a eq. (1) (condicionada a `A_m = 1`, `S_t = 1`, com `S_t` indicador) com a eq. (2) (`P_t` contínuo em [0,1], definido sobre os dois primeiros trimestres) e com a Figura 1. Checar o que `β` estima em relação ao `ATT` da eq. (1); quais termos de ordem inferior estão incluídos ou absorvidos por `α_{m,s(t)}` e `γ_t`; o papel de `λ`; e se o que o texto e a Figura 1 dizem que os efeitos fixos absorvem (composição materna por mês de concepção, sazonalidade de base, "choques comuns a todas as coortes de um município num dado ano") corresponde aos efeitos fixos efetivamente escritos na eq. (2).
  2. Elementos do desenho principal que o texto descreve e a eq. (2) não mostra: a interação por chuva (parágrafo "Chuva" e H3), o contraste de terceiro trimestre (H3), a amostra em que a eq. (2) é estimada (tratados e banana familiar; onde entram os municípios sem banana) e o teste de tratamento falso (H4). Checar se cada um tem especificação, variável e contraste definidos, e o que fica remetido ao plano de análise futuro (5.8).
  3. Hipótese de identificação e grupo de comparação: seção 5.2, parágrafo "Grupo de comparação". Checar o enunciado da hipótese única (evolução do hiato sazonal na ausência da lei); o critério operacional de "predominantemente familiar" e de exclusão por registro de aeronave; o uso de uma classificação medida em 2017 e de `A_m` provisório do Censo de 2006; e o que o tratamento falso é capaz de detectar e o que não é. Conferir, no Quadro 4, a que ameaças a resposta "absorvida pelos efeitos fixos" é atribuída.
  4. O diagnóstico de abertura como etapa de decisão (5.3) e a regra do Quadro 2: checar o que é estimado, em que subperíodos e com que classificação; a afirmação de que o diagnóstico "decide qual pré-período serve de referência" e "não consome graus de liberdade da análise confirmatória"; se as quatro linhas do Quadro 2 são mutuamente exclusivas e exaustivas frente às combinações possíveis de medição e diagnóstico; se os critérios de cada linha são observáveis e fixados antes do dado; e a mudança de estimando declarada na terceira linha ("impedir a volta dos voos").
  5. Interferência, versões e análises secundárias: seção 5.5 (três grupos; como se define "vizinho imediato" e "fora do alcance"; como as versões do tratamento entram na estimação) e seção 5.6 (hipóteses sob as quais a forma reduzida por dose e a eq. (3) valem, agora sem equação de tendências paralelas nem descrição do grupo de dose nula; critério de "concordância" entre as quatro análises; estatuto da comparação de fronteira).
  6. Inferência, multiplicidade, poder e pré-compromisso (5.8): adequação declarada de cada procedimento ao número de tratados e à estrutura da diferença tripla; a que coeficiente e a que análise se aplicam H1 e H2 sob Holm; como o efeito mínimo detectável será calculado para `β` e com que frações expostas; e o que o último parágrafo declara sobre a ordem dos fatos (rodada exploratória da forma reduzida já executada, desenho de calendário adotado depois dela, plano ainda a escrever e a ratificar).
**Will particularly care about**: Se a equação estimada implementa o desenho que o texto e a figura descrevem, e se as escolhas ainda abertas (estação, corte de chuva, grupos, pré-período de referência) estão amarradas a um momento anterior ao contato com os desfechos do pós-lei. Se o desenho distingue "teste" de "limite" de modo operacional.
**Possible blind spots**: Pode tratar a existência de pico sazonal de voos, a relação entre chuva e aplicação e o conteúdo dos registros como dados do problema (Cartão 4), e a janela gestacional sensível e a qualidade dos registros de nascimento e óbito como externas ao desenho (Cartão 3). Pode exigir de um projeto de mestrado o detalhamento de um plano de pré-análise completo; a proporcionalidade é do Cartão 1 e do sintetizador.

### Reviewer Configuration Card #3

**Role**: Peer Reviewer 2
**Display role**: Peer Reviewer 2
**Identity Description**: Pesquisador sênior em economia ambiental e da saúde, com trabalhos sobre exposição a agrotóxicos e poluição e desfechos ao nascer em países de renda média, familiarizado com a literatura que o projeto mobiliza (soja transgênica e glifosato no Brasil, aspersão aérea na Colômbia, fumigação de bananais no Equador, estudos dos EUA, sazonalidade de nascimentos) e usuário dos registros do DATASUS (SINASC, SIM, SINAN) em painéis municipais longos.
**Review Focus**:
  1. Fidelidade e completude da revisão: nas seções "Antecedentes" (cap. 1) e 3.2, abrir as fontes e checar se cada estudo é caracterizado corretamente quanto a desenho, população e resultado. Atenção ao que mudou nesta versão: a descrição de Calzada et al. (cerca de 80 g; apenas até 150 m do perímetro; três meses ou mais de fumigação intensiva; efeito nos dois primeiros trimestres e não significativo no terceiro), que sustenta a janela gestacional, a hipótese H3 e o argumento de diluição; e as duas referências novas, Rigotto et al. (2013) e Jones (2020), quanto ao que de fato comparam e concluem. Indicar literatura relevante ausente. A Fase 0 não abriu nenhuma fonte.
  2. A lacuna e o grupo de comparação à luz da literatura: verificar a afirmação de que não existe avaliação ex post de uma proibição de método (cap. 1); e se a literatura citada dá base para tratar municípios de agricultura familiar como comparação para os de fruticultura irrigada no que toca à sazonalidade de desfechos ao nascer (3.2, 5.2).
  3. Hipóteses e desfechos de saúde: cap. 4 e parágrafo "Desfechos" do cap. 6. Checar a justificativa de peso médio e óbito fetal como confirmatórios; a direção esperada em H2 e o duplo papel do óbito fetal (desfecho e teste de seleção); a definição e a função do desfecho composto de nascidos vivos e óbitos fetais; a plausibilidade, na literatura, de H3 (efeito maior em ano chuvoso, menor no terceiro trimestre) e de H4 (ausência de reação na banana familiar); e o uso das intoxicações intencionais como placebo em H5.
  4. Sazonalidade de nascimentos como ameaça de domínio: seção 3.2 (terceira regularidade), linhas "Mudança de sazonalidade" e "Chuva com efeito próprio sobre a saúde" do Quadro 4. Checar se o projeto trata, com apoio na literatura que cita, as fontes de sazonalidade do peso ao nascer no semiárido que não passam pelo avião (composição materna, arboviroses, nutrição e renda agrícola, calor) e os choques de 2020–2021.
  5. Qualidade e comparabilidade dos registros de saúde no período ampliado: cap. 6 e Quadro 3. Checar o que o projeto diz, ou deixa de dizer, sobre a comparabilidade de SINASC e SIM de 2005 a 2024 (mudanças de formulário e de registro da idade gestacional, cobertura e sub-registro de óbito fetal), município de residência contra de ocorrência, células pequenas em município × mês nos poucos municípios tratados, e a fonte das notificações de arboviroses citadas no Quadro 4.
  6. Enquadramento e ligação com o segundo ensaio: seção 3.1 e último período do cap. 8. Checar se a promessa de fornecer a "premissa empírica" e o "insumo empírico" do segundo ensaio é compatível com um parâmetro definido sobre coortes da estação, descrito como intenção de tratar e, em um dos cenários, como efeito de "impedir a volta dos voos".
**Will particularly care about**: Se a contribuição alegada é genuína frente ao que já existe e se as magnitudes e janelas tomadas da literatura estão reproduzidas com fidelidade, já que delas dependem a hipótese de mecanismo e o cálculo de poder. Se o projeto separa efeito populacional de efeito ocupacional ao falar de "saúde".
**Possible blind spots**: Pode avaliar o desenho por analogia com os estudos de referência e subestimar o que muda quando o tratamento é uma retirada estadual e simultânea com poucos municípios tratados (Cartão 2). Tende a tomar a estação de pulverização e a classificação dos municípios como conhecidas (Cartão 4). Menos atento ao calendário e à forma do documento (Cartão 1).

### Reviewer Configuration Card #4

**Role**: Peer Reviewer 3
**Display role**: Peer Reviewer 3
**Identity Description**: Pesquisador de ciência da exposição e saúde ambiental com formação agronômica, especializado em tecnologia de aplicação de agrotóxicos (aviação agrícola, deriva), em fitossanidade da bananicultura irrigada e de sequeiro no semiárido nordestino e sua relação com o regime de chuvas, e com experiência em reconstruir exposição histórica a partir de registros regulatórios e administrativos brasileiros (relatórios da aviação agrícola ao MAPA, receituário agronômico, cadastros estaduais, censos agropecuários, autos judiciais) obtidos por Lei de Acesso à Informação. Não é economista: lê o projeto perguntando se o "tratamento", a "estação" e o "grupo de comparação" descritos correspondem ao que acontecia no campo e ao que os arquivos públicos de fato guardam.
**Review Focus**:
  1. A premissa de que o voo tem estação e segue a chuva: seções 2.2 e 5.2 (parágrafo "Chuva"), comentário "A sazonalidade" do cap. 7. Checar a base agronômica apresentada para pico sazonal de aplicação aérea em bananal irrigado do semiárido, para o uso da quadra chuvosa como estação na falta de registros (5.4), para a transposição do caso equatoriano, e o que o projeto prevê se a aplicação for uniforme ao longo do ano. Checar também como a chuva é medida e atribuída ao município (Quadro 3, linha "Precipitação") e se "ano chuvoso" tem definição.
  2. A hipótese da seca e suas fontes: seção 2.3, linha "2012–2017" do Quadro 1, comentário "A seca" do cap. 7 e terceira linha do Quadro 2. Checar quais afirmações sobre a suspensão e a persistência dos voos repousam em quais fontes (relato de moradora em 2016, declaração de produtor em 2021, lei municipal de 2010, notícia e ação de 2011), se o texto as apresenta com o grau de certeza que cada uma comporta, e se o plano de conferência é capaz de decidir entre as linhas do Quadro 2. As URLs e os títulos das fontes de imprensa não foram abertos na Fase 0.
  3. O que cada fonte de medição pode e não pode mostrar: seção 5.4 e Quadro 3, fonte por fonte. Para os relatórios mensais do MAPA (2012–2018, CE e RN, operadores de outros estados), o receituário, o cadastro e os autos de infração, os autos de 2011 e o Censo Agropecuário de 2006: o que o projeto afirma que o registro contém, com que base normativa, para que anos e em que unidade, sob guarda de quem, e se declara riscos de retenção, lacuna, sigilo ou negativa. Checar como dessas fontes se chega a `A_m`, ao calendário e à definição de tratamento como "cessação efetiva de voos" (5.5), e o que serve de fonte para a classificação nos anos do diagnóstico anteriores a 2012 (painel desde 2005).
  4. Validade de campo do grupo de comparação e do tratamento falso: seção 5.2 e H4. Checar a premissa de que municípios de banana predominantemente familiar compartilham "a cultura, o clima e o calendário agrícola" dos tratados (irrigado contra sequeiro, serra contra chapada, variedades e manejo de doenças) e "não têm o avião"; como "predominantemente familiar" é medido no Censo de 2017; e se a aplicação costal nesses municípios tem sazonalidade própria que o projeto considere.
  5. Canais físicos de interferência e versões: seção 5.5 e linha "Interferência" do Quadro 4. Checar a escala espacial atribuída à deriva e ao aquífero frente à definição de "vizinhos imediatos"; a base para a hipótese de migração do serviço aéreo para áreas sem proibição e o que o pedido de registros do estado vizinho permite observar; e como drone, aplicação terrestre substituta e descumprimento seriam identificados nos registros pós-lei (autos de infração, janela até 19/12/2024).
  6. Diluição espacial e ética dos registros: comentário "A diluição" do cap. 7 e parágrafos "Escopo" e "Aspectos éticos" do cap. 6. Checar a afirmação de que "nenhuma fonte disponível" resolve a distância entre residência e bananal, e a afirmação ética à luz do tipo de dado que os pedidos de acesso podem devolver (registros com identificação de empresas, produtores ou responsáveis técnicos).
**Will particularly care about**: Se a estação de pulverização, a relação entre chuva e voo e a ausência de avião na banana familiar têm base local verificável ou são hipóteses transpostas, e se o projeto sabe, antes de pedir, o que os arquivos administrativos guardam. Se o município é unidade defensável para um fenômeno que o próprio texto situa a 150 metros da lavoura.
**Possible blind spots**: Não avalia identificação, especificação nem inferência (Cartão 2) e pode pedir uma precisão de medida de exposição que um desenho de intenção de tratar não exige. Não julga a posição do projeto na literatura econômica nem a qualidade dos registros de saúde (Cartão 3). Pode subestimar restrições de prazo e de escopo de um mestrado ao sugerir fontes adicionais (Cartão 1).

## Review Strategy Recommendations

- **É um plano, não um artigo com resultados.** Os critérios de `review_criteria_framework.md` § 2.1 se aplicam ao desenho prometido. "Statistical reporting completeness" e "Conclusion conservatism" devem ser aplicados ao que o texto se compromete a reportar e a concluir (seção 5.8, cap. 8) ou marcados `NOT_ASSESSED`. A ausência de números de estimativa é regra declarada do documento, não lacuna.
- **Sem alvo vinculante.** `criteria_binding_unavailable` vale para todos os assentos. Nenhum parecer deve invocar padrões de um periódico específico nem normas do PPGEco/UFES que não tenha lido.
- **Avaliar a versão atual.** Os pareceristas recebem só o projeto_v2. Nenhum achado deve se referir ao desenho anterior (três estágios, forma reduzida como primeiro estágio) nem aos cartões do arquivo v1.
- **Afirmações que o manuscrito não permite conferir:** a existência e a data do plano versionado da forma reduzida, o conteúdo da rodada exploratória, a declaração de que a exposição sazonal não foi cruzada com os desfechos, as avaliações "preliminares" de fontes. Tratar como declarações e dizer o que seria preciso ver.
- **Fontes não abertas na Fase 0.** A fidelidade das caracterizações da literatura cabe ao Cartão 3; a das bases normativas dos registros e das fontes de imprensa e institucionais sobre a seca e a persistência dos voos cabe ao Cartão 4. O próprio `.bib` marca as fontes documentais novas como "a reconferir".
- **Tensão esperada entre Cartões 2 e 4.** O desenho principal depende de três premissas de campo (o voo tem estação, a estação segue a chuva, a banana familiar não tem avião). O Cartão 2 pode aceitá-las como hipóteses declaradas e testáveis pelo diagnóstico; o Cartão 4 pode considerá-las condição prévia sem a qual o tratamento não está definido. O sintetizador deve manter a divergência visível.
- **Tensão esperada entre Cartões 2 e 3.** O diagnóstico do pré-período usa a sazonalidade do peso ao nascer como evidência de exposição; a literatura de sazonalidade de nascimentos, que o próprio texto cita como ameaça, oferece outras leituras do mesmo padrão. As duas avaliações devem aparecer lado a lado.
- **Tensão esperada entre Cartão 1 e os demais.** Exigências de detalhamento e de novas fontes competem com o prazo de seis bimestres e com o escopo de um mestrado. Distinguir, em cada achado, revisão necessária de sugestão opcional.
- **Fronteira com o Devil's Advocate.** Os quatro cartões cobrem o que o projeto declara. O assento fixo fica livre para atacar o que ele não declara.
- **Idioma.** Pareceres em português.
- **Comentários da fonte.** Os comentários `%` dos arquivos `.tex` não aparecem no PDF. Servem de contexto, mas nenhum achado deve depender de informação que só exista neles sem dizer isso.

## Quality Gates

- [x] As 6 dimensões foram analisadas (a quinta, declarada `criteria_binding_unavailable`).
- [x] Os 4 cartões foram produzidos; nenhum quinto cartão foi emitido para o Devil's Advocate.
- [x] Os focos dos 4 assentos não se sobrepõem (territórios declarados antes dos cartões). Onde dois assentos olham o mesmo trecho (por exemplo, o grupo de comparação na seção 5.2), cada um checa um aspecto distinto: hipótese de identificação (Cartão 2), base na literatura (Cartão 3), validade de campo (Cartão 4).
- [x] O Cartão 4 parte de outra disciplina (agronomia e ciência da exposição, registros regulatórios), não de uma versão "mais ampla" dos outros.
- [n/a] Periódicos-alvo recomendados: não se aplica, pelas razões da seção própria.
- [x] As descrições de identidade são específicas quanto a método, área e objeto.
