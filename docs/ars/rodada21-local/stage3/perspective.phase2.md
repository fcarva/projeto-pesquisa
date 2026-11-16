contract_role: perspective

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: warn
trigger: "ressalva conhecida do campo adjacente omitida"

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### Reviewer Identity

Peer Reviewer 3 — Perspective (interdisciplinar). Pesquisador de saúde coletiva e vigilância em saúde ambiental, com formação em epidemiologia perinatal e prática nos sistemas de informação do SUS e na regulação do uso de agrotóxicos. Leio o texto de fora da economia: não avalio identificação nem inferência. Onde uso conhecimento de prática administrativa ou de literatura que não está no manuscrito, marco como [conhecimento externo]; nada disso foi conferido nesta sessão e deve ser lido como pista a verificar, não como fato do texto.

### Overall Recommendation

Minor Revision. A revisão pedida é textual e delimitada (regra de decisão, escopo, ética e natureza das fontes), cabe no plano de análise e não exige nova rodada de dados. O achado W1 precisa estar resolvido antes de qualquer leitura dos registros pedidos.

### Confidence Score

4. Sistemas de informação em saúde, vigilância de populações expostas e fiscalização de agrotóxicos estão no meu campo; a parte agronômica (doença, calendário, produtos) é campo adjacente.

### Calibration Status

`NOT_CALIBRATED`

### Summary Assessment

O manuscrito é um projeto de mestrado que propõe avaliar o efeito da proibição cearense da pulverização aérea sobre o peso ao nascer, por um contraste de calendário gestacional entre municípios com aplicação aérea documentada e municípios de banana familiar, com período de referência fixado antes da seca e uma regra de decisão que diz o que se entrega em cada cenário. Para um leitor de saúde coletiva, o texto é incomumente legível e honesto: separa método de cultura, prescrição de aplicação, relato de registro, e declara a diluição dentro do município e a seleção para o nascimento vivo. A fragilidade principal está no elo que o próprio projeto chama de central, a medida dos voos: a regra de decisão lê o silêncio de um registro administrativo de preservação incerta como ausência de voo, sem critério de completude nem validação cruzada, e é esse ramo que autoriza a conclusão pública mais delicada (a de que a lei não tinha o que proibir). Os demais achados são ressalvas localizadas do campo adjacente: uma proibição municipal dentro do período de referência, o indicador de substituição dependente do esforço de notificação, o perfil químico inferido de análises de água, o § 2º sem delimitação, e lacunas de sigilo e de comunicação pública. Nenhum compromete o desenho; todos são reparáveis por redação.

### S1: O objeto é o método, e o texto tira disso a consequência de medida
O projeto não confunde lavoura com exposição: define o grupo tratado pelo uso de aeronave e trata a distância entre cultura e método como problema de medida a resolver com registro, não com suposição. É o ponto em que estudos ecológicos de agrotóxico e saúde costumam falhar.
**Evidence Anchor**: text: secoes/01-introducao.tex "o grupo tratado relevante é o dos municípios onde havia avião, e não o dos municípios onde havia lavoura"

### S2: A natureza de cada evidência de contexto é declarada
O texto distingue relato jornalístico de registro administrativo e não promove um ao outro; o quadro de cronologia diz quais eventos vêm de fonte secundária.
**Evidence Anchor**: text: secoes/02-contexto.tex "Há relato de pico sazonal, não registro dele."

### S3: Prescrição não é tratada como aplicação
O receituário agronômico é usado como complemento e com a ressalva correta, que é a que um fiscal faria.
**Evidence Anchor**: text: secoes/05-metodologia.tex "cuja guarda é preciso localizar e que registra prescrição, não aplicação"

### S4: Os limites do registro de óbito fetal estão ditos
A seleção para o nascimento vivo é tratada como ameaça, e o texto reconhece subnotificação, contagens mínimas e perdas precoces não observadas, sem prometer um teste que o SIM não sustenta.
**Evidence Anchor**: text: secoes/07-ameacas.tex "O registro de óbito fetal tem subnotificação e contagens quase sempre de zero ou um por município e mês"

### S5: A exposição não depende da idade gestacional registrada
A janela gestacional fixa evita condicionar em variável afetada pelo tratamento e, de quebra, torna a definição de exposição imune à troca de formulário do SINASC em 2011, que o Cap. 6 também declara.
**Evidence Anchor**: text: secoes/05-metodologia.tex "a duração observada da gestação é desfecho"

### S6: O que se entrega no cenário nulo está fixado de antemão
Num debate regulatório em curso, dizer antes o que conta como "sem poder" e o que conta como "sem efeito" é o que protege o resultado de leitura oportunista.
**Evidence Anchor**: table: Quadro "Regra de decisão" (secoes/05-metodologia.tex), coluna "O que o ensaio entrega"

### S7: A diluição dentro do município é assumida, não escondida
O texto reconhece que o município de residência não mede proximidade à lavoura e que o efeito médio municipal pode não aparecer mesmo sendo grande para quem mora junto ao bananal.
**Evidence Anchor**: text: secoes/07-ameacas.tex "o efeito médio municipal é o individual multiplicado pela fração exposta"

### W1: A regra de decisão lê silêncio do registro como ausência de voo
**Problem**: A classificação dos municípios e o ramo "ausência de voos" do quadro dependem de relatórios mensais que o próprio texto diz de preservação incerta antes do envio eletrônico. O quadro prevê "registros obtidos" e "não obtidos", mas não o caso mais provável em arquivo administrativo: entrega parcial (alguns anos, algumas superintendências, alguns operadores). Faltam um critério de completude, uma regra para distinguir "mês sem voo" de "mês sem relatório" e uma validação cruzada. Bastar um ano registrado para contar como documentado resolve o falso negativo só pela metade; o município sem nenhum papel preservado vira não tratado ou, pior, entra no grupo de comparação, já que a exclusão desse grupo também depende de haver registro. [conhecimento externo] Relatório entregue pelo regulado só captura operador regular e adimplente; voo de operador de outro estado tende a ser arquivado na superintendência de origem ou na do local, conforme a prática de cada época; e a norma alcança, salvo engano meu, também o operador privado (produtor com aeronave própria), que o texto não menciona ao falar em "empresas de aviação agrícola".
**Evidence Anchor**: text: secoes/05-metodologia.tex, Quadro "Regra de decisão" "Registros mostram ausência de voos no período de referência" e, no parágrafo anterior, "Contam-se como documentados os voos registrados em ao menos um ano do período de referência"
**Why it matters**: É o elo que o projeto declara central. O ramo "ausência de voos" entrega uma "medida do alcance da lei"; se a ausência for de arquivo, a conclusão pública seria que a lei não tinha o que proibir, com base em sub-registro. E tratado classificado como comparação atenua o contraste principal sem que o texto tenha como perceber.
**Suggestion**: (i) Acrescentar ao quadro uma linha para registros parciais e definir, antes de abrir os arquivos, o que conta como série completa por operador e por ano (por exemplo, relatórios "sem movimento" presentes, numeração contínua, lista de operadores registrados no período como denominador). (ii) Pedir junto, no mesmo requerimento, a relação de operadores registrados e de operadores privados com atuação declarada nos dois estados, para saber de quem deveria haver relatório. (iii) Declarar a validação cruzada mínima: Censo de 2006, autos de infração, autos da ação de 2011 e imprensa, com regra para discordância. (iv) Reservar a expressão "ausência de voos" para série comprovadamente completa; fora disso, "sem registro".
**Severity**: Major
**Confidence**: 4 — prática de fiscalização e de uso de arquivo administrativo como fonte; não conferi o texto da norma nesta sessão

### W2: Uma proibição municipal cai dentro do período de referência e da sensibilidade
**Problem**: Limoeiro do Norte proibiu a aplicação aérea de novembro de 2009 a maio de 2010, intervalo que cobre a estação provisória (fevereiro a maio) de 2010. O período de referência é 2007 a 2011, e a sensibilidade proposta contra os eventos de 2011 restringe a referência a 2008 a 2010, que mantém justamente esse ano. O Cap. 6 registra a lei e diz que regras locais "alteram o período de comparação", mas nenhuma especificação trata as coortes afetadas, nem se diz se a proibição foi cumprida.
**Evidence Anchor**: text: secoes/06-dados.tex "um levantamento preliminar encontrou uma proibição, em Limoeiro do Norte, de 2009, revogada em 2010"
**Why it matters**: Se o município estiver entre os tratados e a lei tiver sido cumprida, uma das estações da linha de base já é uma estação sem voo, o que reduz o hiato de referência. Com poucos tratados, um município pesa.
**Suggestion**: Dizer no Cap. 5 como as coortes com início de gestação naquela estação entram (excluídas, ou mantidas com sensibilidade), e usar os relatórios de 2009 e 2010 daquele município, se vierem, como teste de cumprimento da lei municipal.
**Severity**: Minor
**Confidence**: 4 — leitura da cadeia de datas do próprio manuscrito

### W3: A notificação de intoxicação mede também o esforço de notificar
**Problem**: A substituição do avião pela aplicação terrestre é examinada por contagem de notificações de intoxicação ocupacional antes e depois da lei, com as intencionais como contraste. O quadro de fontes anota apenas "Público" para o SINAN, sem ressalva. [conhecimento externo] A notificação de intoxicação exógena é fortemente sub-registrada, capta quase só o caso agudo atendido, e varia com a capacidade local de vigilância (referência em saúde do trabalhador, capacitação, presença de grupos de pesquisa e de movimentos sociais); a obrigatoriedade nacional e a ficha mudaram por volta de 2010 e 2011 [UNVERIFIED]. Os municípios do conflito são exatamente aqueles em que o esforço de notificação mais deve ter mudado ao longo da série.
**Evidence Anchor**: text: secoes/apendices.tex, Quadro "Especificações do desenho de calendário", linha Substituição "Notificações de intoxicação ocupacional por agrotóxico agrícola, por município e ano, antes e depois da lei"
**Why it matters**: Aumento pode ser vigilância, e ausência de aumento não mostra ausência de substituição. O Cap. 5 afirma que o desenho "mede os elos intermediários"; para o elo da substituição, a medida proposta é fraca, e para o elo da exposição das gestantes não há medida.
**Suggestion**: Declarar a limitação no quadro de fontes e na linha da especificação; usar como contraste um agravo de notificação com a mesma dependência de esforço local, além das intencionais; considerar internações por intoxicação e a modalidade prescrita no receituário pós-lei como indicadores paralelos; e dizer explicitamente quais elos da cadeia ficam sem medida.
**Severity**: Minor
**Confidence**: 4 — uso rotineiro do sistema de notificação; a data da mudança de norma não foi conferida

### W4: O perfil químico vem de análises de água, não do que o avião aplicava
**Problem**: O texto caracteriza "o químico" pela tabela de 23 pontos de coleta de água de 2009, citada pela justificativa de um projeto de lei que a atribui ao dossiê, e daí conclui que o caso é de fungicida em banana. Detecção em água reflete toda a agricultura da área (melão e outras culturas, aplicação terrestre incluída) e a persistência e mobilidade de cada molécula, não a calda aérea. [conhecimento externo] O controle da sigatoka costuma usar triazóis, estrobilurinas e protetores em óleo mineral; os produtos listados não são os típicos desse uso, e três deles são inseticidas.
**Evidence Anchor**: text: secoes/02-contexto.tex "procimidona e o inseticida carbaril aparecem em todos, carbofurano em 18"
**Why it matters**: A escolha do análogo e a plausibilidade biológica do efeito apoiam-se no produto aplicado. A conclusão do parágrafo (o glifosato não é o químico relevante) se sustenta; a identificação positiva do que era pulverizado, não.
**Suggestion**: Redigir a tabela como evidência de contaminação da água na região, citar a fonte original pela página do dossiê (que o texto já cita em outro ponto) e remeter a identificação do produto aéreo ao campo "produto" dos relatórios mensais.
**Severity**: Minor
**Confidence**: 3 — campo adjacente (agronomia); toxicologia ambiental no meu campo

### W5: A exposição pode não acompanhar o mês do voo
**Problem**: O contraste de calendário supõe que a exposição gestacional se concentra nos meses de aplicação. O canal hídrico é posto fora da análise confirmatória por falta de dado, mas não se discute o que ele faz ao calendário. [conhecimento externo] No semiárido rural, a água de beber vem em boa parte de cisternas que captam a chuva do telhado, e de açudes; ambos enchem na quadra chuvosa, a mesma em que se voaria, e são consumidos ao longo do ano. Resíduo depositado em superfícies e em poeira doméstica também persiste além do mês da aplicação.
**Evidence Anchor**: text: secoes/06-dados.tex "O canal hídrico, que exigiria medições de agrotóxicos na água de consumo com localização dos pontos de coleta, não integra a análise confirmatória"
**Why it matters**: Se parte da dose chega por água armazenada, as coortes de referência (só o terceiro trimestre na estação) e as concebidas depois dela também são expostas, e o hiato sazonal subestima o efeito por uma via que o texto não lista. O limite declarado no Cap. 5 trata apenas do dano tardio pela exposição direta.
**Suggestion**: Acrescentar a defasagem da exposição por água e por resíduo doméstico à lista de limites do contraste, com o sinal do viés (atenuação), e, se houver dado municipal de cobertura de cisternas, usá-lo como heterogeneidade exploratória.
**Severity**: Minor
**Confidence**: 3 — vigilância da qualidade da água para consumo; magnitude desconhecida para a região

### W6: O desfecho composto mistura registros com calendários diferentes
**Problem**: O composto soma nascidos vivos e óbitos fetais no denominador, por coorte. A coorte é definida pelo mês de nascimento com janela gestacional fixa; um óbito fetal ocorre, por definição, antes do termo, de modo que o mesmo mês de evento corresponde a um início de gestação mais tardio. O texto não diz como o óbito fetal é alocado à coorte. [conhecimento externo] O campo de idade gestacional do óbito fetal no SIM tem completude pior que a do SINASC.
**Evidence Anchor**: text: secoes/06-dados.tex "a proporção de gestações registradas que terminam em nascido vivo com 2.500 gramas ou mais"
**Why it matters**: Alocado pelo mês do evento com a janela fixa de um nascimento a termo, o óbito fetal cai sistematicamente na classe de exposição errada, o que enfraquece o teste de seleção que o desenho oferece. O desfecho é exploratório, daí a banda.
**Suggestion**: Declarar a regra de alocação (pela idade gestacional registrada quando houver, com análise de sensibilidade para os registros sem o campo) e reportar a completude desse campo por grupo e período.
**Severity**: Minor
**Confidence**: 4 — epidemiologia perinatal com SIM e SINASC

### W7: O § 2º da lei aparece no contexto e some do desenho
**Problem**: O Cap. 2 informa que a vedação alcança a dispersão por aeronave para controle vetorial. Depois disso, o tema não volta: não se diz se houve dispersão aérea para controle de vetores no Ceará antes de 2019, em quais municípios, nem se isso altera a definição de município tratado ou as versões do tratamento. As notificações de arboviroses entram apenas "como controle", sem explicação do uso.
**Evidence Anchor**: absence: secoes/05-metodologia.tex e secoes/06-dados.tex — expected delimitação do alcance do § 2º do art. 28-B (controle vetorial por aeronave) no escopo ou nas versões do tratamento; checked Cap. 2, Cap. 5, Cap. 6 (parágrafo Escopo), Cap. 7 e os apêndices de fontes, ameaças, especificações, cronologia e diagrama
**Why it matters**: Se a prática existiu, há municípios tratados por outra via, possivelmente urbanos e fora do grupo com avião agrícola; se nunca existiu, uma frase resolve. O leitor de vigilância em saúde fará a pergunta. [conhecimento externo] Até onde sei, a dispersão aérea para controle de Aedes foi autorizada em lei federal de 2016 e não chegou a ser adotada como rotina, mas não conferi o caso cearense.
**Suggestion**: Uma frase no parágrafo de escopo, com a fonte consultada (secretaria estadual de saúde), dizendo se houve ou não a prática, e o papel exato das notificações de arboviroses na análise.
**Severity**: Minor
**Confidence**: 3 — a pergunta é do meu campo; a resposta factual não foi verificada

### W8: O compromisso de sigilo não cobre a identificação indireta
**Problem**: O texto promete não divulgar resultado com identificação de empresa ou pessoa e, ao mesmo tempo, lista como entrega a medida municipal e mensal da aplicação aérea antes e depois da proibição. Com a prática concentrada em poucos municípios, município e mês bastam para apontar o operador ou o contratante; no pós-lei, a mesma tabela é indício de infração. A regra de supressão ("células com poucos eventos") não tem limiar nem diz se vale para a medida de voos. Não se declara a guarda dos documentos recebidos, que trazem nome de responsável técnico (dado pessoal) e, no caso do receituário e dos autos judiciais, de terceiros. O enquadramento ético trata só dos dados de saúde.
**Evidence Anchor**: text: secoes/06-dados.tex "nenhum resultado será divulgado com identificação de empresa ou pessoa"
**Why it matters**: O conflito em torno do tema já produziu violência, como o próprio texto abre lembrando, e a matéria está em litígio. O risco é para terceiros e para o pesquisador, e a promessa, como está, não é cumprível junto com a entrega (iii).
**Suggestion**: Fixar limiar de supressão e nível de agregação da medida de voos a divulgar (por exemplo, microrregião ou grupo de municípios, ou indicador binário por estação); descrever guarda, acesso e descarte dos documentos; dizer que o enquadramento na resolução citada foi conferido também para os registros identificados, ou consultar o comitê de ética sobre a dispensa.
**Severity**: Minor
**Confidence**: 4 — prática de pesquisa com registros de fiscalização; não sou jurista

### W9: Uso público prometido sem registro público do plano, e com desfecho único
**Problem**: A Justificativa oferece o resultado à decisão de manter, relaxar ou substituir a lei. O plano de análise fica em repositório, sem pré-registro público, e o texto informa, com franqueza, que uma rodada exploratória já cruzou a exposição sazonal com o desfecho do pós-lei. Além disso, o único desfecho confirmatório é o peso médio municipal ao nascer, enquanto os danos que motivaram a lei, no próprio relato do texto, incluem intoxicação, contaminação de água e doença crônica.
**Evidence Anchor**: text: secoes/05-metodologia.tex "Os planos são versionados em repositório, sem pré-registro público"
**Why it matters**: Num litígio em curso, um resultado nulo ou sem poder em um desfecho será citado como "a proibição não trouxe ganho de saúde". O texto se protege do "sem poder", mas não do salto de um desfecho para o juízo sobre a política; e a credibilidade externa de um plano que só o autor pode datar é menor do que precisa ser.
**Suggestion**: Depositar o plano com carimbo de tempo de terceiro (registro público ou embargo), o que custa pouco; e acrescentar à Justificativa e à regra de decisão uma frase de alcance: o ensaio informa um desfecho, por uma via, em nível municipal, e não mede os demais danos alegados.
**Severity**: Minor
**Confidence**: 3 — comunicação de evidência em vigilância; convenções de registro da economia fora do meu campo

### W10: Fontes primárias disponíveis substituídas por secundárias, e uma lei sem referência
**Problem**: A lei municipal de 2009 que institui a proibição em Limoeiro do Norte é citada por número no quadro de cronologia e não tem entrada na lista de referências (só a lei revogadora tem). A aprovação unânime de dezembro de 2018 é apoiada em reportagem, embora a nota do quadro diga que a cronologia vem dos textos legais e da tramitação; a seca de 2012 a 2017, em portal de notícias, embora o projeto vá usar séries oficiais de chuva; a ação de 2011, em nota de imprensa do órgão, sem número de processo.
**Evidence Anchor**: absence: lista de referências (projeto.bbl) — expected entrada para a Lei municipal nº 1.478/2009 de Limoeiro do Norte; checked todas as entradas da lista e as citações do Cap. 2, do Cap. 6 e do Apêndice de cronologia
**Why it matters**: O quadro declara a natureza das fontes, e esses pontos destoam do padrão que o próprio texto adota. O número do processo é também condição prática para a consulta prevista no primeiro bimestre.
**Suggestion**: Incluir a lei de 2009 na lista; citar a tramitação oficial para a votação de 2018; apoiar a datação da seca nas séries de precipitação; localizar e registrar o número da ação.
**Severity**: Minor
**Confidence**: 4 — conferência direta da lista de referências do manuscrito

### Criterion-Bound Judgements

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D4 cross_disciplinary_relevance | contrato reviewer_full v2, escala sprint_contract | warn | ver S1 a S7 e W1 a W10 | Enquadramento e definições legíveis para campo adjacente e limites em geral declarados; ressalvas conhecidas da vigilância em saúde omitidas em pontos localizados, a mais séria na leitura do registro administrativo | Conhecimento externo não conferido nesta sessão; texto da norma federal não lido | sim: W1 deve ser resolvido antes da leitura dos registros |

### Detailed Comments

**Assumption Audit.** Explícitas: o texto declara intenção de tratar, versões múltiplas do tratamento e ausência de interferência, e não as defende além do que pode. Implícitas: (a) que o que não está no arquivo não voou (W1); (b) que a exposição acompanha o mês do voo (W5); (c) que a contagem de notificações acompanha a ocorrência de intoxicações (W3); (d) que os produtos achados na água são os da calda aérea (W4). Paradigmática: o município como unidade. O texto a reconhece como limite e não a contorna, o que é aceitável num desenho em intenção de tratar; do meu campo eu pediria ao menos a descrição de quantos nascimentos por município vêm de setores vizinhos aos perímetros irrigados, que o texto deixa como extensão.

**Validade de medida da exposição (foco 1).** Além de W1: o Censo de 2006 conta estabelecimentos que declararam uso de aeronave, no município do estabelecimento, sem cultura e sem mês. Como classificação provisória é defensável; como calendário não serve, e o cenário de contingência do quadro usa a quadra chuvosa como estação sem nenhum registro de que os voos se concentravam nela. O texto declara esse cenário exploratório, o que é a rotulagem correta.

**Exequibilidade (foco 2).** O pedido cobre dezessete anos, dois estados e operadores de outros estados, com prazo até o fim do terceiro bimestre. [conhecimento externo] Pedidos que exigem consolidação de documentos em papel costumam ser negados por trabalho adicional ou atendidos por vista presencial, e a tabela de temporalidade do órgão pode ter autorizado a eliminação de relatórios antigos. Convém pedir primeiro a existência e o volume dos arquivos por ano, e só depois o conteúdo, e prever recurso dentro do prazo. A consulta à ação de 2011 depende do número do processo (W10).

**Registros de saúde (foco 3).** O tratamento da troca de formulário e do município de residência está correto. Falta uma frase sobre a completude do peso ao nascer por grupo e período; no SINASC ela é alta, mas o projeto deveria mostrar, não supor. A janela gestacional fixa não tem a duração declarada (ver Minor Issues).

**Calendário (foco 4).** O texto reconhece que, em bananal irrigado, o pico pode ser fraco e que os relatos divergem entre seis a oito e duas aplicações por ano. Do ponto de vista perinatal, escolher os dois primeiros trimestres segue o análogo citado; como o ganho de peso fetal se concentra no fim da gestação, a análise do terceiro trimestre, hoje exploratória, é a que um epidemiologista leria primeiro. Não peço mudança de estatuto, apenas que a justificativa da janela diga que ela vem do análogo e não de mecanismo estabelecido para os produtos em questão.

**Cadeia legal (foco 5).** As datas conferem entre o Cap. 2, o Cap. 6 e o quadro de cronologia: sanção e vigência de janeiro de 2019, lei municipal de novembro de 2009 e revogação de maio de 2010, projetos de maio de 2011 e fevereiro de 2015, aprovação de dezembro de 2018, julgamento de maio de 2023, lei de dezembro de 2024. Não encontrei contradição interna. O problema é de consequência (W2) e de natureza da fonte (W10).

**Populações e vias fora do desenho (foco 7).** A exposição ocupacional e para-ocupacional de gestantes que trabalham na fruticultura ou moram com quem trabalha não depende de avião nem de distância ao bananal e não é retirada pela lei. O texto trata emprego apenas como via de composição materna. Vale uma frase de escopo.

### Cross-Disciplinary Reading Recommendations

Não recomendo obra específica que eu não possa atestar nesta sessão. Pistas de busca, todas [UNVERIFIED]: estudos de avaliação da completude e da subnotificação das intoxicações por agrotóxicos no sistema de notificação; avaliações da qualidade do registro de óbito fetal no sistema de mortalidade; a diretriz federal de vigilância em saúde de populações expostas a agrotóxicos; a literatura agronômica sobre manejo da sigatoka-amarela em bananal irrigado no semiárido.

~~~yaml suggested-references
[]
~~~

### Questions for Authors

1. Se os relatórios vierem para alguns anos ou operadores e não para outros, em que linha do quadro de decisão o projeto cai, e quem decide isso antes de abrir os arquivos?
2. Os operadores privados (produtor com aeronave própria) entregavam o mesmo relatório mensal no período de referência? Se não, como seus voos entram na medida?
3. A proibição municipal de novembro de 2009 a maio de 2010 foi cumprida? As coortes com início de gestação naquela estação ficam na referência?
4. Houve dispersão aérea para controle de vetores no Ceará antes de 2019?
5. Em que nível de agregação a medida de voos será publicada, de modo que a promessa de não identificar empresa seja cumprível?

### Minor Issues

- Cap. 5: declarar a duração da janela gestacional fixa usada para datar o início da gestação a partir do mês de nascimento.
- Cap. 6: a expressão "como controle" para as notificações de arboviroses não diz se é covariável, placebo ou contraste.
- Cap. 2: "ao menos seis na quadra chuvosa" ao lado de "de seis a oito aplicações por ano" pede uma frase que diga se quase todas as aplicações relatadas caem na estação.
- Apêndice de fontes: a linha do SINAN traz apenas "Público"; as demais fontes de saúde trazem a ressalva correspondente.
- Apêndice de fontes: "órgãos estaduais" sem nome do órgão dificulta ao leitor avaliar a guarda do cadastro e dos autos.
- Cap. 8: a nota do cronograma data o primeiro bimestre, mas a data-limite dos registros é dada só como "fim do terceiro bimestre"; convém o mês.
