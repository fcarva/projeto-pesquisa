# Proibição da pulverização aérea de agrotóxicos no Ceará: efeitos sobre o peso ao nascer

Projeto de pesquisa — PPGEco/UFES (projeto_v4, após a re-revisão)

## Resumo

Em 2019, o Ceará proibiu a pulverização aérea de agrotóxicos em todo o seu
território. Este projeto propõe avaliar o efeito dessa proibição sobre o peso
ao nascer. O desenho principal é uma diferença tripla de calendário
gestacional: compara coortes com início de gestação dentro e fora da estação
de pulverização, antes e depois da lei, em municípios com aplicação aérea
documentada e em municípios de bananicultura familiar. O período de referência
é fixado antes da seca de 2012--2017, que pode ter suspendido os voos e que
afeta o peso ao nascer por vias próprias. O projeto trata como problema
central a distância entre a cultura plantada e o método de aplicação, propõe
medi-la com registros administrativos e fixa de antemão o que entrega em cada
cenário, inclusive o de não haver efeito detectável.

\textbf{Palavras-chave}: agrotóxicos; pulverização aérea; peso ao nascer;
avaliação de impacto; Ceará.


<!-- arquivo: paper/projeto/secoes/01-introducao.tex -->

\chapter{Introdução}
\label{cap:introducao}

Em abril de 2010, José Maria Filho, o Zé Maria do Tomé, foi assassinado na
Chapada do Apodi, no interior do Ceará. Ele denunciava havia anos a
pulverização aérea de agrotóxicos sobre os perímetros irrigados da região, onde
aviões sobrevoam plantações de banana e melão vizinhas a casas, escolas e
açudes de abastecimento. A denúncia não tratava do veneno aplicado na lavoura,
mas do veneno que não fica na lavoura. Nove anos depois, o Ceará proibiu a
prática em todo o território e deu à lei o nome do homem assassinado (Lei Estadual
nº~16.820/2019).

A pulverização aérea é um caso de externalidade em que o mecanismo físico é
visível. Parte da calda liberada pela aeronave não atinge o alvo: é carregada
pelo vento e se deposita fora da área tratada, fenômeno que a literatura
técnica chama de deriva. Quem contrata a aplicação paga pelo serviço e pelo
produto; quem mora a favor do vento arca com o restante. A lei cearense
responde a esse conflito por proibição, e não se localizou, na literatura
consultada, avaliação causal dos efeitos dessa resposta.

Este projeto pergunta: \textbf{qual é o efeito causal da proibição da
pulverização aérea de agrotóxicos sobre o peso ao nascer nos municípios
cearenses onde a prática existia?} Mais precisamente, o efeito sobre as
coortes cujo início de gestação coincidiria com a estação de pulverização. A pergunta é de avaliação de política
pública. O objeto é a retirada de um \emph{método de aplicação}, e não de uma
substância, e essa distinção organiza o desenho inteiro: o grupo tratado
relevante é o dos municípios onde havia avião, e não o dos municípios onde
havia lavoura.

\section{Antecedentes}

A evidência econômica próxima se divide entre o que uma substância faz à saúde
e o que um método de aplicação faz à saúde. Do lado da substância,
\citeonline{dias2023down} exploram a expansão da soja transgênica no Brasil,
combinada à direção do fluxo d'água dentro das bacias, e documentam piora dos
desfechos ao nascer nas populações a jusante. \citeonline{reynier2025glyphosate}
estudam a difusão do glifosato nos Estados Unidos, com aptidão agroclimática
como fonte de variação, e encontram redução do peso ao nascer e da duração da gestação,
concentrada na cauda inferior da distribuição de peso esperado.
\citeonline{larsen2017agricultural} mostram, na Califórnia, que os efeitos
adversos aparecem apenas entre os expostos ao topo da distribuição de uso de
agrotóxicos, o que recomenda desconfiar de efeitos médios quando a exposição é
concentrada.

Do lado do método, os antecedentes diretos são dois.
\citeonline{camacho2017health} avaliam as consequências sanitárias da aspersão
aérea de herbicida sobre cultivos ilícitos na Colômbia.
\citeonline{calzada2023bananas} estudam a fumigação aérea de bananais no
Equador e encontram déficit de peso ao nascer entre filhos de mães que moravam
junto às plantações e foram expostas, na gestação, aos períodos de fumigação
intensa. Este último é o análogo mais próximo do caso
cearense, pela cultura e pelo método, com diferenças que importam: a doença
combatida e a frequência das aplicações não são as mesmas
(Capítulo~\ref{cap:contexto}).

O que nenhum desses trabalhos oferece é a avaliação de uma \textbf{proibição
de método}. A comparação entre proibir e taxar é antiga na economia ambiental
\cite{weitzman1974,lichtenberg1988,helfand1995}, e há simulações do banimento
de moléculas específicas \cite{bocker2020glyphosate}, mas simulação
\emph{ex ante} não é avaliação \emph{ex post}. Nos estudos de método, a
pulverização aérea é introduzida ou está em curso; no Ceará ela é retirada, e
os sinais esperados se invertem.

\section{Justificativa}

A questão tem relevância prática imediata. A lei cearense foi contestada no
Supremo Tribunal Federal e declarada constitucional, o que assentou a
competência dos estados para legislar sobre a matéria; em 2024 o próprio Ceará
flexibilizou a regra para admitir drones, e a nova redação voltou a ser
questionada na Corte. O debate tem se apoiado em argumentos de plausibilidade, porque não há
estimativa do que a proibição de fato produziu. Uma avaliação que diga se houve ganho em peso ao nascer, onde e de que tamanho, ou que mostre com rigor por que ele não é mensurável com os registros
existentes, informa tanto os estados que consideram adotar a medida quanto a
decisão de mantê-la, relaxá-la ou substituí-la por outro instrumento.

\section{Contribuição}

A contribuição pretendida tem três camadas. A primeira é de \textbf{objeto}: a
avaliação \emph{ex post} de uma proibição de método de aplicação, instrumento
que o Supremo Tribunal Federal julgou constitucional em 2023 \cite{stf2023adi6137} e que,
por isso, é replicável por outras unidades da federação. A segunda é de
\textbf{medida}: o projeto trata como problema central a distância entre a
cultura plantada e o método de aplicação efetivamente usado, e propõe medi-la
com registros administrativos, se eles forem obtidos. A terceira é de \textbf{identificação}: a lei vale
para todo o estado desde a mesma data, de modo que não há variação de
\emph{timing}; o projeto usa um desenho de calendário gestacional
\cite{calzada2023bananas,brainerd2014seasonal}, com os municípios de banana
familiar como grupo de comparação e um período de referência fixado de
antemão, e o confronta com um desenho de intensidade de exposição
\cite{callaway2024continuous}. Em todos os cenários previstos, inclusive o de
não haver efeito detectável, o projeto diz o que entrega
(Seção~\ref{sec:regra}).

Este documento descreve um desenho, não um resultado: seguem o contexto
institucional, o referencial, os objetivos, a estratégia empírica, os dados, as
ameaças à identificação e o cronograma.


<!-- arquivo: paper/projeto/secoes/02-contexto.tex -->

\chapter{Contexto institucional}
\label{cap:contexto}

\section{A Lei Zé Maria do Tomé}

A Lei Estadual nº~16.820, sancionada em 8 de janeiro de 2019 e vigente desde o
dia seguinte \cite{ceara2019lei16820}, acrescentou o art.~28-B à Lei Estadual
nº~12.228/1993 \cite{ceara1993lei12228}, a norma cearense sobre agrotóxicos. O caput veda ``a pulverização aérea de agrotóxicos
na agricultura no Estado do Ceará''; o §~2º estende a vedação à dispersão por
aeronave para controle vetorial. Dois traços da redação importam ao desenho. A
proibição é de \textbf{método}: nenhum princípio ativo é nomeado, e o produto
continua disponível para aplicação terrestre. E a proibição é \textbf{estadual
e simultânea}: alcança os 184 municípios na mesma data.

O Apêndice~\ref{ap:cronologia} resume a cronologia. Três marcos antecedem o
tratamento e são tratados separadamente: a \emph{notícia} (apresentação do projeto de lei que deu origem à norma, em
2015, precedida de proposição semelhante em 2011 \cite{ceara2011pl134}), a \emph{certeza} (aprovação unânime, em dezembro de
2018) e a \emph{obrigação} (vigência, em janeiro de 2019). Em dezembro de 2024,
a Lei nº~19.135 \cite{ceara2024lei19135} deu nova redação ao artigo e abriu exceção para aeronaves
remotamente pilotadas. O estado não revogou a proibição, mas trocou o
instrumento: de cota zero para regulação de desempenho. Por isso a janela de
análise termina em 19 de dezembro de 2024.


\section{A Chapada do Apodi, a cultura e o químico}

A Chapada do Apodi, no Baixo Jaguaribe, concentra a fruticultura irrigada do
Ceará, com destaque para banana e melão. É a região à qual a lei responde e
onde a exposição da população à deriva foi documentada antes da proibição. Na
bananicultura, a aplicação aérea serve ao controle de doenças fúngicas da
folha, que dependem de umidade; as reportagens sobre o caso cearense nomeiam a
sigatoka-amarela \cite{agenciabrasil2016ceara,globorural2021bananais}. No
análogo equatoriano, a fumigação ocorre o ano inteiro e se intensifica na
estação chuvosa \cite{calzada2023bananas}; no Ceará, um produtor relata duas
aplicações aéreas por ano. Se há pico sazonal no bananal irrigado do
semiárido é questão que este projeto verifica.

Esse perfil distingue o caso da literatura de referência, construída em grande
parte sobre glifosato em grãos transgênicos. A tabela de análises de água
reproduzida na justificativa do Projeto de Lei nº~18/2015, atribuída ao Dossiê
ABRASCO \cite{ceara2015pl18}, registra 23 pontos de coleta na Chapada em 2009: o fungicida
procimidona e o inseticida carbaril aparecem em todos, carbofurano em 18,
fenitrotiona em 16 e glifosato em apenas 4. Trata-se de fungicida e inseticida
sobre fruta irrigada. Os desenhos de referência transferem na forma, não no
mecanismo, e o análogo empírico adequado é o da fumigação aérea de bananais
\cite{calzada2023bananas}.

\section{O que se sabe sobre onde e quando havia avião}
\label{sec:onde-aviao}

O dado público mais direto sobre o uso de aeronaves é o Censo Agropecuário de
2006, que registra os estabelecimentos que aplicaram agrotóxicos por avião. No
Ceará eram 36 estabelecimentos, em 7 dos 184 municípios
\cite{ibge2006censoagro}. A prática era, portanto, geograficamente concentrada,
ao passo que a bananicultura está presente na maior parte do estado
\cite{ibgepam}: a maioria dos municípios com a cultura não tinha registro de
avião.

Esse retrato não vale necessariamente para 2018. A lei municipal que revogou
a proibição de Limoeiro do Norte, em 2010, passou a regular a prática, com
distâncias mínimas de povoações e mananciais \cite{limoeiro2010lei1511}; a
aplicação aérea seguiu, portanto, legal e regulada até a lei estadual. Em
2011 noticiou-se uma proibição na Chapada e o Ministério Público ajuizou ação
civil pública com esse pedido, mas não se localizou instrumento jurídico da
primeira nem desfecho da segunda. O fato mais relevante é outro: em 2016, uma
moradora de comunidade da Chapada relatou que não havia novas aplicações
desde 2012, por causa da pouca chuva \cite{agenciabrasil2016ceara}, o que é
coerente com a dependência que a doença fúngica tem de umidade. Um produtor do
Cariri, por sua vez, declarou ter feito aplicações aéreas em seu bananal até
2018 \cite{globorural2021bananais}. As duas leituras são compatíveis se o
avião era usado quando chovia. Nenhuma delas vem de registro administrativo, e saber em que municípios e meses se voou é a primeira tarefa
do projeto (Seção~\ref{sec:medicao}).


<!-- arquivo: paper/projeto/secoes/03-referencial.tex -->

\chapter{Referencial teórico e empírico}
\label{cap:referencial}

\section{A deriva como externalidade negativa}

O agrotóxico que deriva sobre o vizinho é um caso clássico de externalidade
negativa: o produtor que contrata a aplicação aérea internaliza o custo do
serviço e do produto, mas não o custo em saúde suportado por quem mora a favor
do vento. A solução negociada de \citeonline{coase1960} supõe custos de
transação baixos; aqui a população atingida é difusa e o dano é
probabilístico e de difícil atribuição, o que justifica a intervenção
regulatória. Qual instrumento usar, se proibição, taxa ou regulação de
desempenho, depende das inclinações relativas do benefício e do custo
marginais \cite{weitzman1974} e tem dimensão distributiva
\cite{lichtenberg1988,helfand1995}. Essa escolha é objeto de um
segundo ensaio da dissertação. O que este projeto fornece a ela é
um insumo parcial: uma estimativa, em intenção de tratar, do efeito da
proibição sobre o peso ao nascer.

\section{Agrotóxicos e saúde ao nascer}

A literatura econômica recente sobre exposição gestacional a agrotóxicos
converge em três regularidades úteis ao desenho.

A primeira é a ordem de grandeza e a sua dependência da proximidade.
\citeonline{reynier2025glyphosate} estimam reduções médias de peso ao nascer da
ordem de 23 a 32 gramas associadas à difusão do glifosato em áreas rurais dos
Estados Unidos. \citeonline{calzada2023bananas} encontram déficit de cerca de
80 gramas para mães que moravam a até 150 metros do perímetro de um bananal e
tiveram três meses ou mais de fumigação intensiva na gestação, em comparação
com a fumigação habitual; a estimativa varia com o limiar de intensidade, e os autores não
detectam gradiente de distância entre 150 e 2.500 metros. Como no Ceará as aplicações são
menos frequentes, esse valor é tomado como teto. No Brasil,
\citeonline{rigotto2013trends} comparam municípios da fruticultura irrigada do
Ceará com municípios de agricultura familiar, em estudo ecológico, e
documentam mais internações por neoplasias nos primeiros, sem diferença
estatisticamente significante em óbitos fetais, embora com tendência crescente.

A segunda é a concentração. Os efeitos aparecem no topo da distribuição de
exposição \cite{larsen2017agricultural} e na cauda inferior da distribuição de
peso esperado \cite{reynier2025glyphosate}; \citeonline{jones2020invasive} é dos poucos estudos em que fungicidas têm
peso na variação explorada. A consequência para este
projeto é direta: se o efeito existe só para quem mora junto ao bananal, a
média de um município inteiro o dilui pela fração de nascimentos exposta, e um
desenho municipal pode não encontrá-lo mesmo que ele seja grande.

A terceira é o calendário. Quando a aplicação tem estação, o efeito é
identificado pelo cruzamento entre o período sensível da gestação e a estação
de aplicação: \citeonline{calzada2023bananas} encontram efeito nos dois
primeiros trimestres e estimativa imprecisa no terceiro, com a intensidade da fumigação
ditada pela estação chuvosa, e \citeonline{brainerd2014seasonal} usam o mês da
concepção e a estação de aplicação de agroquímicos na Índia. Duas ameaças a esse desenho são conhecidas. A composição das mães
varia com a época da concepção \cite{buckles2013season}, e a sazonalidade do
peso ao nascer persiste mesmo entre irmãos \cite{currie2013within}. E, no
semiárido brasileiro, a chuva durante a gestação afeta o peso ao nascer por
vias próprias \cite{rocha2015water}, o que faz da seca um confundidor de
primeira ordem neste projeto.

\section{Avaliação de uma política estadual e simultânea}

Como a lei vale para todo o estado desde a mesma data, os estimadores e as
decomposições de diferenças-em-diferenças para adoção escalonada
\cite{callaway2021multiple,goodmanbacon2021,dechaisemartin2020} não se aplicam:
não há variação de \emph{timing}. Restam a variação de \emph{calendário} entre
coortes de nascimento, para a qual a diferença tripla exige uma única hipótese
de tendências paralelas, a da diferença entre os dois contrastes que a compõem
\cite{olden2022triple}, e a variação de \emph{intensidade} prévia entre
municípios, para a qual \citeonline{callaway2024continuous} mostram que o
efeito no nível da dose recebida sai sob tendências paralelas usuais, ao passo
que a curva dose-resposta exige hipótese mais forte.

Quando poucos grupos são tratados, a inferência assintótica usual falha e são
necessários procedimentos próprios \cite{conley2011,ferman2019inference,
chernozhukov2021conformal,hagemann2025single}.


<!-- arquivo: paper/projeto/secoes/04-objetivos.tex -->

\chapter{Objetivos e hipóteses}
\label{cap:objetivos}

\textbf{Objetivo geral.} Estimar o efeito da proibição estadual da
pulverização aérea de agrotóxicos (Lei nº~16.820/2019) sobre o peso ao nascer
das coortes com início de gestação na estação de pulverização, nos municípios
cearenses com aplicação aérea documentada.

\textbf{Objetivos específicos.}
\begin{alineas}
  \item medir onde e quando havia aplicação aérea, antes e depois da
    proibição, com registros administrativos federais e estaduais;
  \item descrever, só com dados anteriores à lei, o hiato sazonal de peso ao
    nascer nos municípios com e sem aplicação aérea;
  \item estimar o efeito da proibição pelo desenho de calendário gestacional,
    com os municípios de banana familiar sem registro de aeronave como grupo
    de comparação;
  \item confrontar essa estimativa com a forma reduzida estadual, o controle
    sintético e a comparação de fronteira;
  \item examinar a seleção para o nascimento vivo e a substituição da
    aplicação aérea pela terrestre.
\end{alineas}

\textbf{Hipóteses.} A hipótese confirmatória ($H_1$) é que, do período de
referência para o pós-lei, o peso ao nascer das coortes com início de gestação
na estação de pulverização aumentou, em relação às demais coortes, nos
municípios com aplicação aérea, comparados aos de banana familiar. As demais
são exploratórias. Se os voos foram suspensos pela seca, o hiato sazonal já
deve ter se reduzido entre 2012 e 2018 ($H_2$). O efeito deve ser maior nos
anos chuvosos, leitura que admite a explicação alternativa de um efeito
próprio da chuva ($H_3$). Os municípios de banana familiar, comparados aos sem
banana, não devem reagir à lei ($H_4$). E as notificações de intoxicação
ocupacional por agrotóxico agrícola podem aumentar, se a aplicação migrou do
avião para o pulverizador costal ($H_5$). O óbito fetal é examinado como teste
de seleção, sem hipótese confirmatória.


<!-- arquivo: paper/projeto/secoes/05-metodologia.tex -->

\chapter{Metodologia}
\label{cap:metodologia}

\section{Parâmetro-alvo e cadeia causal}

O parâmetro de interesse é o efeito da lei, em intenção de tratar, sobre o peso
ao nascer das coortes cujo início de gestação coincide com a estação de
pulverização, nos municípios cearenses com aplicação aérea documentada no
período de referência. Com $Y(1)$ e $Y(0)$ os desfechos com e sem a proibição,
\begin{equation}
  \tau = E\left[\,Y_{mt}(1) - Y_{mt}(0) \mid A_m = 1,\ P_t,\ t \text{ pós-lei}\,\right],
\end{equation}
em que $A_m$ indica município com aplicação aérea documentada entre 2007 e
2011 e $P_t$ mede quanto do início da gestação da coorte $t$ cai na estação.
Três escolhas dessa definição são deliberadas. O tratamento é a lei, e não o
voo: o que se estima inclui o descumprimento e a substituição pela aplicação
terrestre. A referência temporal de $A_m$ é anterior à seca de 2012--2017,
porque nesse intervalo os voos podem ter sido suspensos
(Seção~\ref{sec:onde-aviao}); definir o tratado pelo que ocorria às vésperas
da lei poderia deixar o grupo vazio. E a população é de coortes, e não de
municípios, o que uma medida municipal de intensidade agrícola não consegue
declarar.

A cadeia que liga a lei ao desfecho tem elos que podem falhar separadamente: a
lei precisa ter sido cumprida; precisava haver voos a suspender ou a impedir
de voltar; a ausência de voos precisa reduzir a exposição das gestantes, e não
apenas trocá-la pela da aplicação terrestre; e a menor exposição precisa
alterar o desfecho. A cada elo a população tratada encolhe, até as gestantes
que moravam junto a um bananal pulverizado. Um efeito nulo no desfecho final
não distingue falha de implementação de falha do mecanismo, e por isso o
desenho mede os elos intermediários.

\section{Desenho principal: diferença tripla de calendário}
\label{sec:calendario}

A Figura~\ref{fig:dag} resume as hipóteses causais. Compara-se, dentro de cada
município, as coortes com início de gestação na estação de pulverização com as
demais; compara-se essa diferença, o hiato sazonal, entre o período de
referência e os períodos seguintes; e contrasta-se essa variação entre os
municípios com aplicação aérea e os de comparação.

\begin{figure}[htb]
\caption{\label{fig:dag}Diagrama causal do desenho de calendário}
\centering
\footnotesize
\begin{tikzpicture}[y=0.88cm,
  box/.style={draw, rounded corners=1pt, align=center, inner sep=3pt, text width=3.4cm},
  lat/.style={box, dashed},
  ar/.style={-{Stealth[length=2mm]}, semithick},
  thr/.style={ar, dashed}]
\node[box] (est) at (0,0) {Início da gestação na estação de pulverização};
\node[box] (pos) at (5,0) {Município com avião $\times$ pós-lei};
\node[box, fill=black!10] (T) at (5,-2) {\textbf{Lei $\times$ estação}: coorte que deixa de receber o voo};
\node[box] (chu) at (0,-2.9) {Chuva do ano};
\node[box] (voo) at (5,-4) {Voo durante a gestação};
\node[box] (ter) at (10,-4) {Aplicação terrestre substituta};
\node[box] (exp) at (5,-5.4) {Exposição gestacional};
\node[lat] (out) at (0,-6.8) {Outra causa que altere o hiato sazonal só ali, após a lei};
\node[lat] (sau) at (5,-6.8) {Saúde fetal};
\node[lat] (sel) at (10,-6.8) {Seleção: só nascidos vivos são observados};
\node[box] (ef) at (10,-8.6) {Absorvidos por efeitos fixos: composição materna, sazonalidade, choques município-ano};
\node[box, fill=black!10] (peso) at (5,-8.6) {\textbf{Peso ao nascer}};
\draw[ar] (est.south east) -- (T.north west);
\draw[ar] (pos) -- (T);
\draw[ar, very thick] (T) -- (voo);
\draw[ar, very thick] (voo) -- (exp);
\draw[ar, very thick] (exp) -- (sau);
\draw[ar, very thick] (sau) -- (peso);
\draw[ar] (T.south east) -- (ter.north west);
\draw[ar] (ter.south) |- (exp.east);
\draw[ar] (chu.east) -- (voo.north west);
\draw[ar] (chu.south) -- ++(0,-1.0) -- (sau.north west);
\draw[ar] (ef) -- (peso);
\draw[thr] (out) -- (sau);
\draw[thr] (out.west) -- ++(-4mm,0) |- ([yshift=2mm]T.west);
\draw[thr] (sau) -- (sel);
\draw[thr] (sel.south west) -- (peso.north east);
\end{tikzpicture}
\fonte{Elaboração própria. Setas grossas: caminho causal de interesse. Nós e
setas tracejados: não observados ou ameaças que os efeitos fixos não removem.
O canal de emprego e renda da fruticultura, omitido da figura, é tratado no
Capítulo~\ref{cap:ameacas}.}
\end{figure}

Seja $P_t \in [0,1]$ a fração dos dois primeiros trimestres de gestação da
coorte $t$ que cai na estação de pulverização, $Seca_t$ o indicador das coortes nascidas de 2013 a 2018, $Pos_t$ o das nascidas
a partir de 2020 e $C_{m,a}$ a chuva da quadra chuvosa no município e ano.
Estima-se, com ponderação pelo número de nascimentos,
\begin{equation}
  Y_{mt} = \alpha_{m,s(t)} + \mu_{m,a(t)} + \gamma_t
         + \theta\,(P_t \times C_{m,a(t)})
         + \beta_S\,(A_m \times P_t \times Seca_t)
         + \beta\,(A_m \times P_t \times Pos_t) + \varepsilon_{mt},
  \label{eq:ddd}
\end{equation}
em que $\alpha_{m,s(t)}$ são efeitos fixos de município por mês do ano,
$\mu_{m,a(t)}$ de município por ano de nascimento e $\gamma_t$ de coorte. Os primeiros
absorvem a sazonalidade de base de cada município; os segundos, os choques
comuns a todas as coortes de um município num ano, entre eles os programas
estaduais de saúde materna contemporâneos à lei; as coortes de transição, nascidas em 2012 e em 2019, são excluídas, de modo
que os termos de ordem inferior são absorvidos por esses efeitos fixos. O coeficiente $\beta$ mede quanto o
hiato sazonal de peso ao nascer mudou, do período de referência para o
pós-lei, nos municípios com aplicação aérea em relação aos de comparação; sob
a hipótese principal, $\beta > 0$. O coeficiente $\beta_S$ mede a mesma
variação no período de seca e é descritivo.

Dois limites dessa especificação são declarados. Com uma estação de quatro
meses, toda gestação a termo atravessa a estação em algum trimestre: as coortes
com $P_t = 0$ são as que têm apenas o terceiro trimestre na estação, e $P_t$
não chega a um. O coeficiente $\beta$ compara, portanto, exposição no início da
gestação com exposição no fim, e subestima o efeito se a exposição tardia
também causar dano; a hipótese de que ela não causa não é imposta, e o efeito
é reportado por unidade de $P_t$ e no contraste entre os extremos observados.
A janela gestacional é fixa: a duração observada da gestação é desfecho, e
usá-la para definir a exposição condicionaria em variável afetada pelo
tratamento.

\textbf{Período de referência.} O período de referência é fixado neste
projeto: as coortes nascidas de 2007 a 2011, anos em que há relatos de voos na
Chapada e que antecedem a seca. Ele não é escolhido pelos dados. As coortes de
2005 e 2006 entram apenas no estudo de evento. Dois limites são conhecidos: os
registros pedidos começam em 2008, e em 2011 já havia notícia de proibição; uma
estimativa com a referência restrita a 2008--2010 é reportada.

\textbf{Grupo de comparação.} Os municípios de comparação são os produtores de
banana em que a cultura é predominantemente familiar, segundo o Censo
Agropecuário de 2017 \cite{ibge2017censoagro}, com limiar a fixar no plano de
análise. Supõe-se que não tenham aplicação aérea, o que se verifica nos
registros e no Censo de 2006, que a registra também fora dos polos irrigados;
município com qualquer registro de aeronave é excluído. Em nível, a comparação
não seria válida: agricultura familiar e empresarial diferem em renda, acesso
a programas sociais e exposição à aplicação costal. Dentro da diferença
tripla exige-se menos: que, na ausência da lei, o hiato sazonal tivesse
evoluído do mesmo modo nos dois grupos desde o período de referência
\cite{olden2022triple}. A hipótese é examinada por um estudo de evento,
com um coeficiente por ano e 2011 como base, de modo que os anos de 2005 a 2010
testam a pré-tendência, e por um tratamento falso: comparados aos municípios sem banana, os de banana familiar não
deveriam reagir à lei.

\textbf{Chuva.} A chuva entra de dois modos. Como a precipitação durante a
gestação afeta o peso ao nascer no semiárido por vias que não passam pelo
avião \cite{rocha2015water}, a chuva da quadra chuvosa, interagida com $P_t$,
é controle nos dois grupos; a hipótese adicional, declarada, é que esse efeito
direto seja comum a municípios de lavoura irrigada e de sequeiro, e uma
especificação que o deixa diferir é reportada. E, como a doença que motiva o
voo depende de umidade, examina-se, em caráter exploratório, se $\beta$ é maior
nos anos chuvosos. As especificações estão no Apêndice~\ref{ap:espec}.

\section{Diagnóstico descritivo do pré-período}
\label{sec:diagnostico}

Antes de qualquer contato com os desfechos do pós-lei, descreve-se o hiato
sazonal nos dois grupos no período de referência e no período de seca. O
diagnóstico responde se a exposição à estação aparece nos dados municipais e
se a seca a alterou. Ele é descritivo: não escolhe o período de referência,
que já está fixado, e não autoriza nem impede a análise confirmatória, que
depende apenas da medição dos voos e do cálculo de poder
(Seção~\ref{sec:regra}). A cautela se justifica porque um hiato achado por
acaso no pré-período regrediria no pós-lei e produziria um coeficiente
positivo sem efeito algum da lei. A leitura do diagnóstico tem um limite que
se declara: os dois períodos diferem pela própria seca, que altera a
sazonalidade do peso ao nascer por outras vias, de modo que o fechamento do
hiato em 2012--2018 é compatível com a suspensão dos voos, mas não a
demonstra.

\section{Medição do método}
\label{sec:medicao}

A classificação $A_m$ e o calendário de pulverização são medidos, e não
supostos. As fontes, com sua guarda e seus riscos, estão no
Apêndice~\ref{ap:fontes}. A principal são os relatórios mensais que as
empresas de aviação agrícola entregam ao Ministério da Agricultura
\cite{mapa2008in2}, com município, cultura, área e produto; pedem-se os de 2008
a 2024, para o Ceará e o Rio Grande do Norte, incluídos os operadores sediados
em outros estados. Os anos posteriores à lei servem para medir o cumprimento
e, desde 2021, o uso de drones. Não se sabe se os relatórios anteriores ao
envio eletrônico foram preservados nas superintendências, e por isso a entrega
da medida é condicional. Complementam-na o cadastro estadual de prestadores e
os autos de infração \cite{ceara1993lei12228}, o receituário agronômico
\cite{brasil2002decreto4074}, cuja guarda é preciso localizar e que registra
prescrição, não aplicação, e os autos da ação civil pública de 2011. O Censo
Agropecuário de 2006 \cite{ibge2006censoagro} fornece a classificação
provisória; por não distinguir cultura e ser anterior à seca, pode apontar
para municípios diferentes daqueles em que se voava em 2018.

\section{Interferência e versões do tratamento}

O desenho supõe que o tratamento de um município não altera o desfecho de
outro e que o tratamento tem uma só versão. Quatro canais de interferência
são conhecidos: a deriva sobre municípios vizinhos e o aquífero compartilhado,
que melhorariam os vizinhos e atenuariam a estimativa; a migração do serviço
aéreo para áreas sem proibição, que os pioraria e a inflaria; e a mobilidade
das mães. Como a deriva opera em escala de centenas de metros, a interferência
entre municípios por essa via deve ser pequena, mas os vizinhos imediatos dos
tratados são separados dos demais, formando três grupos. Quanto às versões,
estar sob a lei significa coisas diferentes: ter voado e parado; ter trocado o
avião pela aplicação terrestre; ter passado ao drone; não ter cumprido; ou não
voar desde antes, por causa da seca. O parâmetro, por ser de intenção de
tratar, é a média sobre essas versões, e os registros posteriores à lei
permitem documentar a composição.

\section{Análises secundárias e triangulação}

Três análises complementam o desenho principal. A primeira é a forma reduzida
estadual: um diferenças-em-diferenças com tratamento contínuo
\cite{callaway2024continuous}, em que a dose é a área plantada de banana antes
da lei \cite{ibgepam}, o grupo de dose nula é construído também pela aptidão
agroclimática e o alvo é o efeito no nível da dose recebida. Como a área mede
a cultura e não o método, classificar pela cultura produz falsos positivos; se
não produzisse falsos negativos, a forma reduzida identificaria
\begin{equation}
  \theta = VPP \times ATT,
  \label{eq:atenuacao}
\end{equation}
em que $VPP$, o valor preditivo positivo, é a fração dos classificados como
tratados que de fato o eram \cite{denteh2022misclassification}. O Censo de
2006 sugere que a condição não vale exatamente, e por isso a forma reduzida é
lida como descritiva. A segunda é o controle sintético e o
diferenças-em-diferenças sintético \cite{arkhangelsky2021sdid} para o agregado
dos municípios com avião, com doadores fora do alcance da interferência. A
terceira é a comparação com os municípios potiguares da Chapada do Apodi, que
não é experimento natural limpo, porque tudo o que é estadual muda junto na
divisa e as culturas diferem. Entende-se que as análises concordam quando os
sinais coincidem e os intervalos se sobrepõem; a divergência é reportada como
resultado.

\section{Regra de decisão}
\label{sec:regra}

O Quadro~\ref{qua:regra} fixa o que cada resultado da medição e do cálculo de
poder aciona. Nenhum critério usa o desfecho. O efeito plausível é o do
análogo equatoriano, tomado como teto, multiplicado pela fração de nascimentos
exposta, para uma grade de frações fixada no plano de análise; decide o valor
central da grade. Poder suficiente é condição necessária para o teste, não
garantia de que o efeito exista nessa magnitude. Contam-se como documentados
os voos registrados em ao menos um ano do período de referência. A
data-limite para os registros é o fim do terceiro bimestre.

\begin{quadro}[htb]
\caption{\label{qua:regra}Regra de decisão}
\centering
\small
\begin{tabular}{@{}p{4.6cm}p{3.6cm}p{6.3cm}@{}}
\toprule
Medição dos voos & Poder & O que o ensaio entrega \\
\midrule
Voos documentados por município e mês & Efeito detectável $\leq$ plausível &
Desenho principal, confirmatório, com municípios e estação medidos. \\
Voos documentados & Efeito detectável $>$ plausível &
Medida dos voos e desenho principal reportado como limite, sem teste. \\
Voos documentados, sem pico sazonal & Qualquer &
Medida dos voos; o desenho de calendário não se aplica; forma reduzida descritiva. \\
Registros mostram ausência de voos no período de referência & Qualquer &
Medida do alcance da lei; forma reduzida estadual descritiva; sem estimativa de efeito da pulverização. \\
Registros não obtidos até a data-limite & Calculado com a classificação provisória &
Desenho principal com o Censo de 2006 e a quadra chuvosa, declarado exploratório, e o cálculo de poder. \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria.}
\end{quadro}

\section{Inferência, poder e plano de análise}

Há poucos municípios tratados, contíguos, e a lei é atribuída no nível do
estado. Erros-padrão agrupados por município, com aproximação assintótica,
superestimam a precisão, e o \emph{wild cluster bootstrap} isolado não é
defensável com tão poucos tratados \cite{mackinnon2018wild}. O procedimento
principal é o de \citeonline{ferman2019inference}, que admite
heterocedasticidade por tamanho de município; os de \citeonline{conley2011},
\citeonline{canay2021wild} e \citeonline{hagemann2025single} são reportados
como sensibilidade, e a inferência conformal de
\citeonline{chernozhukov2021conformal} é usada no controle sintético.

Dois fatores limitam o poder e nenhum se resolve com mais anos de dados: o
número de municípios com aplicação aérea e a fração dos nascimentos de cada um
efetivamente exposta. O efeito mínimo detectável de $\beta$ é calculado apenas
com dados do período de referência e do período de seca. Há uma única
hipótese confirmatória, sobre o peso ao nascer; os demais desfechos e
contrastes são exploratórios.

A estação, o limiar de agricultura familiar, a medida de chuva e os contrastes
de falsificação são fixados em plano de análise versionado antes de qualquer
cruzamento com os desfechos do pós-lei. A ratificação com o orientador, nesse
momento, pode alterar esses parâmetros, mas não o período de referência nem a
regra de decisão. Um plano para a forma reduzida estadual foi escrito e
versionado em setembro de 2026; uma rodada exploratória dessa análise já foi
executada e levou a rever seu alvo, da curva para o nível. Ela não é reportada
aqui e será refeita a partir das bases originais; o desenho de calendário foi
adotado como principal depois dela, sem que a exposição sazonal tenha sido
cruzada com os desfechos. São planos versionados em repositório, não
pré-registro público.


<!-- arquivo: paper/projeto/secoes/06-dados.tex -->

\chapter{Dados}
\label{cap:dados}

A unidade de análise é o município por mês de nascimento. O painel principal
cobre os municípios cearenses com aplicação aérea e os de comparação, de 2005
a 19 de dezembro de 2024; os 184 municípios do estado entram na forma reduzida,
e municípios de estados vizinhos, no controle sintético e na fronteira. O
Apêndice~\ref{ap:fontes} lista as fontes, o uso de cada uma e as condições de
acesso. Todo o processamento será feito a partir das bases originais.

\textbf{Desfechos.} Do SINASC obtêm-se o peso médio ao nascer, desfecho
confirmatório, e a proporção de nascidos com menos de 2.500 gramas e com menos
de 37 semanas de gestação, exploratórios. A série atravessa a troca do
formulário de nascido vivo, em 2011, que alterou o registro da idade
gestacional; o peso ao nascer não foi afetado do mesmo modo, e a
prematuridade é analisada com essa ressalva. Usa-se o município de residência
da mãe. Do SIM obtém-se o óbito fetal, exploratório, e constrói-se um desfecho
composto, a proporção de gestações registradas que terminam em nascido vivo
com 2.500 gramas ou mais. Do SINAN obtêm-se as notificações de intoxicação por
agrotóxico agrícola, por circunstância, para o canal de substituição, e as de
arboviroses, como controle. As intoxicações intencionais são examinadas como
contraste, com a ressalva de que a troca do avião pelo pulverizador costal
pode alterar a disponibilidade doméstica do produto.

\textbf{Exposição.} A classificação pelo método vem dos registros da
Seção~\ref{sec:medicao} e, provisoriamente, do Censo Agropecuário de 2006; o
grupo de comparação, do Censo Agropecuário de 2017; a chuva, das séries de
precipitação por município. Como a lei estadual de 1993 autoriza os municípios
a legislar supletivamente, regras locais anteriores a 2019 alteram o período
de comparação; um levantamento preliminar encontrou uma proibição, em Limoeiro
do Norte, de 2009, revogada em 2010 por lei que passou a regular a prática
\cite{limoeiro2010lei1511}. O levantamento será refeito, com conferência de
vigência.

\textbf{Escopo.} O canal hídrico, que exigiria medições de agrotóxicos na
água de consumo com localização dos pontos de coleta, não integra a análise
confirmatória, e a exposição não é medida no nível da residência. Uma
avaliação preliminar do monitoramento da qualidade da água e do mapeamento de
uso da terra por satélite indicou limitações para esses fins; ela será refeita
e documentada antes de qualquer uso.

\textbf{Reprodutibilidade e sigilo.} O processamento será feito por rotinas
versionadas, com a data de extração de cada base registrada. Os microdados não
são redistribuídos, e células com poucos eventos não são divulgadas.

\textbf{Aspectos éticos.} Os dados de saúde são secundários, de acesso público
e sem identificação individual; pesquisas dessa natureza não são submetidas ao
sistema CEP/CONEP, nos termos da Resolução nº~510/2016 do Conselho Nacional de
Saúde \cite{cns2016res510}. Os registros obtidos pela Lei de Acesso à
Informação identificam empresas e responsáveis técnicos; eles serão usados
apenas para classificar municípios e meses, e nenhum resultado será divulgado
com identificação de empresa ou pessoa.


<!-- arquivo: paper/projeto/secoes/07-ameacas.tex -->

\chapter{Ameaças à identificação}
\label{cap:ameacas}

O Apêndice~\ref{ap:ameacas} reúne as ameaças conhecidas, o que cada uma faz à
estimativa e o que o desenho lhe opõe. Quatro merecem comentário.

\textbf{A seca.} É a ameaça que mais pesa, por três vias. Ela pode ter
suspendido os voos, de modo que a lei teria impedido a sua volta, e não
interrompido uma prática em curso. Ela também restringiu a água disponível para a irrigação no Baixo Jaguaribe
\cite{pereira2015conflitos}; se isso alterou área plantada, emprego e
composição das mães nos municípios tratados é questão a verificar nas séries
de área e de emprego. E ela afeta o peso
ao nascer diretamente \cite{rocha2015water}. Além disso, o fim da seca é
próximo da vigência da lei. O desenho responde fixando a referência antes da
seca, controlando a chuva nos dois grupos e reportando o período de seca em
separado, mas não separa por completo a lei do retorno das chuvas: se a chuva
tiver efeito sazonal diferente em municípios irrigados e de sequeiro, $\beta$ o
captura. As fontes da suspensão dos voos são de imprensa e de parte
interessada, e por isso ela é tratada como hipótese.

\textbf{A diluição.} O análogo mais próximo estima o efeito para mães que
moravam a até 150 metros do bananal. O registro de nascimentos identifica
o município de residência, não a distância à lavoura. Mesmo nos municípios com
aplicação aérea, a maior parte dos nascimentos é de mães não expostas, e o
efeito médio municipal é o individual multiplicado por essa fração. O desenho
concentra a comparação no tempo, não no espaço. A fração de domicílios
próximos aos bananais poderia ser aproximada com o cadastro de endereços do
Censo de 2022, o que fica como extensão; a resposta deste projeto é dizer de
antemão qual efeito consegue detectar.

\textbf{A sazonalidade.} O desenho só tem o que medir se a aplicação aérea
tiver pico sazonal. Em bananal irrigado, e com poucas aplicações por ano, o
pico pode ser fraco ou não coincidir com a quadra chuvosa, que além disso não
é a mesma em todas as regiões do estado. A existência e a posição do pico são
verificadas nos relatórios mensais antes da estimação. Há também outras
fontes de sazonalidade do peso ao nascer, como as arboviroses, o calor e a
renda agrícola; as que são comuns aos dois grupos se cancelam, e as que não
são ameaçam a hipótese de identificação.

\textbf{A seleção.} Se a proibição reduz perdas fetais, gestações que antes
não chegariam ao nascimento vivo passam a entrar na amostra, possivelmente na
cauda de baixo peso, e o efeito sobre o peso médio sai atenuado. O óbito fetal, o número de nascidos vivos por coorte e a razão de sexo ao
nascer são examinados por isso. O óbito fetal tem duas limitações: o registro tem subnotificação, e as
contagens por município e mês são quase sempre zero ou um. As perdas precoces
não são observadas.


<!-- arquivo: paper/projeto/secoes/08-cronograma.tex -->

\chapter{Resultados esperados e cronograma}
\label{cap:cronograma}

\textbf{Resultados esperados.} O que o projeto entrega depende do que a
medição mostrar, conforme o Quadro~\ref{qua:regra}. Em qualquer cenário,
entrega (i) a descrição do hiato sazonal de peso ao nascer antes da lei e
(ii) o efeito mínimo detectável de cada análise, calculado antes da
estimação. Se os registros forem obtidos, entrega (iii) a medida municipal e
mensal da aplicação aérea de agrotóxicos no Ceará antes e depois da
proibição. Se houver voos documentados e poder suficiente, entrega (iv) a
estimativa do efeito da proibição sobre o peso ao nascer pelo desenho de
calendário, confrontada com as análises secundárias. Nos demais cenários, o
ensaio se entrega como medida do alcance da lei e diagnóstico de poder de uma
política cujo efeito os registros disponíveis não permitem estimar, resultado
que também informa o debate. A estimativa, quando houver, é insumo parcial do
segundo ensaio da dissertação, sobre a escolha entre proibir, taxar e regular
a aplicação; esse ensaio tem cronograma próprio, e aqui aparece apenas o seu
início.

\textbf{Cronograma.} O Quadro~\ref{qua:cronograma} distribui as atividades em
bimestres. Os pedidos de acesso à informação são protocolados no primeiro
bimestre; se os registros não chegarem até o fim do terceiro, segue-se com a
classificação provisória, como prevê a regra de decisão. O plano de análise é escrito antes do diagnóstico; a classificação
e a estação medidas entram nele por adendo datado, quando os registros
chegarem. A ordem de prioridade, se o prazo apertar, é: medição, desenho
principal, análises secundárias.

\begin{quadro}[htb]
\caption{\label{qua:cronograma}Cronograma de atividades, por bimestre}
\centering
\small
\begin{tabular}{@{}p{8.6cm}*{6}{>{\centering\arraybackslash}p{0.75cm}}@{}}
\toprule
Atividade & 1 & 2 & 3 & 4 & 5 & 6 \\
\midrule
Pedidos de acesso à informação (MAPA, ADAGRI, SEMACE) & X & & & & & \\
Consulta aos autos da ação civil pública de 2011 & X & & & & & \\
Montagem do painel (2005--2024) e congelamento das bases & X & X & & & & \\
Plano de análise, ratificado com o orientador & & X & & & & \\
Diagnóstico descritivo do pré-período e cálculo de poder & & X & X & & & \\
Classificação dos municípios pelo método e pela agricultura familiar & & X & X & & & \\

Desenho principal, análises secundárias e triangulação & & & X & X & & \\
Redação do ensaio e qualificação & & & & X & X & \\
Início do segundo ensaio (escolha de instrumento) & & & & & & X \\
Revisão final e defesa & & & & & & X \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria. Bimestre 1: dezembro de 2026 e janeiro de 2027.}
\end{quadro}


<!-- arquivo: paper/projeto/secoes/apendices.tex -->

\begin{apendicesenv}
\clearpage
\chapter{Fontes de dados}
\label{ap:fontes}

\begin{quadro}[htb]
\caption{\label{qua:fontes}Fontes de dados, uso e acesso}
\centering
\footnotesize
\begin{tabular}{@{}p{3.6cm}p{5.6cm}p{5.3cm}@{}}
\toprule
Fonte & Uso & Acesso, guarda e risco \\
\midrule
SINASC (DATASUS) & Peso ao nascer, baixo peso, prematuridade; 2005--2024 & Público. Troca de formulário em 2011 afeta a idade gestacional. \\
SIM (DATASUS) & Óbito fetal & Público. Subnotificação. \\
SINAN (DATASUS) & Intoxicações por agrotóxico; arboviroses & Público. \\
Censo Agropecuário 2006 (IBGE) & Estabelecimentos com aplicação por aeronave: classificação provisória & Público. Não distingue cultura. \\
Censo Agropecuário 2017 (IBGE) & Participação da agricultura familiar na banana: grupo de comparação & Público. \\
PAM (IBGE) & Área plantada por cultura: dose da forma reduzida & Público. \\
FAO-GAEZ & Aptidão agroclimática: grupo de dose nula da forma reduzida & Público. \\
Precipitação (FUNCEME, INMET) & Chuva da quadra chuvosa, por município e ano & Público. \\
SINASC de estados vizinhos & Doadores do controle sintético; fronteira & Público. \\
Relatórios mensais da aviação agrícola (MAPA) & Aplicação aérea por município e mês, 2008--2024, CE e RN & Pedido de acesso à informação. Em papel até 2021; preservação incerta. \\
Cadastro de prestadores e autos de infração (órgãos estaduais) & Operadores; cumprimento após a lei & Pedido de acesso à informação. \\
Receituário agronômico & Modalidade de aplicação prescrita & Guarda a localizar; registra prescrição. \\
Autos judiciais (Justiça Federal) & Prática na Chapada após 2011 & Consulta processual. \\
Leis municipais & Proibições e regras locais anteriores a 2019 & Público (câmaras municipais). \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria.}
\end{quadro}

\clearpage
\chapter{Ameaças à identificação e respostas do desenho}
\label{ap:ameacas}

\begin{quadro}[htb]
\caption{\label{qua:ameacas}Ameaças à identificação e respostas do desenho}
\centering
\footnotesize
\begin{tabular}{@{}p{3.6cm}p{4.7cm}p{6.2cm}@{}}
\toprule
Ameaça & Efeito sobre a estimativa & Resposta \\
\midrule
Voos suspensos pela seca antes da lei &
A lei impede a volta, não interrompe; efeito depende da chuva &
Referência em 2007--2011; período de seca em separado; relatórios mensais. \\
Seca com efeito próprio e fim próximo da lei &
Confunde a lei com o retorno das chuvas &
Chuva como controle nos dois grupos; especificação com efeito distinto por grupo; limitação declarada. \\
Possível retração da lavoura irrigada e do emprego &
Muda renda e composição materna nos tratados &
Efeitos fixos de município por ano; séries de área e emprego; características maternas como placebo. \\
Diluição dentro do município &
Efeito individual multiplicado pela fração exposta &
Poder calculado para uma grade de frações; resultado sem poder lido como limite. \\
Mudança de sazonalidade só nos tratados, após a lei &
Viola a hipótese de identificação &
Estudo de evento do hiato sazonal; tratamento falso; estimativas com e sem 2020--2021. \\
Classificação provisória de 2006 &
Tratados mal identificados; atenuação &
Relatórios mensais; exclusão de qualquer município com aeronave do grupo de comparação. \\
Seleção para o nascimento vivo &
Efeito sobre o peso médio atenuado ou invertido &
Óbito fetal e desfecho composto, exploratórios. \\
Interferência entre municípios &
Sinal indeterminado &
Três grupos; doadores fora do alcance; registros do estado vizinho. \\
Substituição terrestre, drones e descumprimento &
Parâmetro é de intenção de tratar &
Registros posteriores à lei; notificações de intoxicação. \\
Antecipação (projetos de lei de 2011 e 2015) &
Comportamento muda antes da vigência &
Referência em sua maior parte anterior aos projetos; sensibilidade com 2008--2010. \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria.}
\end{quadro}

\clearpage
\chapter{Especificações}
\label{ap:espec}

\begin{quadro}[htb]
\caption{\label{qua:espec}Especificações do desenho de calendário}
\centering
\footnotesize
\begin{tabular}{@{}p{3.4cm}p{6.0cm}p{5.1cm}@{}}
\toprule
Análise & Especificação & Amostra e estatuto \\
\midrule
Principal ($H_1$) & Equação~\ref{eq:ddd}; coeficiente $\beta$ & Municípios com aplicação aérea e de banana familiar; confirmatória. \\
Período de seca ($H_2$) & Equação~\ref{eq:ddd}; coeficiente $\beta_S$ & Mesma amostra; descritiva. \\
Estudo de evento & Um coeficiente de $A_m \times P_t$ por ano, com 2011 como base & Mesma amostra; verificação da hipótese de identificação. \\

Chuva por grupo & Acrescenta $A_m \times P_t \times C_{m,a}$ & Mesma amostra; sensibilidade. \\
Efeito por chuva ($H_3$) & Acrescenta $A_m \times P_t \times Pos_t \times C_{m,a}$ e os termos de ordem inferior & Mesma amostra; exploratória. \\
Terceiro trimestre & $P_t$ redefinido como fração do terceiro trimestre na estação & Mesma amostra; exploratória. \\
Tratamento falso ($H_4$) & Equação~\ref{eq:ddd} com banana familiar no lugar de $A_m$ & Municípios de banana familiar e sem banana; falsificação. \\
Interferência & Equação~\ref{eq:ddd} com indicador de vizinho imediato de município tratado & Vizinhos e demais não tratados; exploratória. \\
Composição materna & Idade e escolaridade da mãe como desfecho na Equação~\ref{eq:ddd} & Mesma amostra; placebo. \\
Seleção & Óbito fetal, desfecho composto, nascidos vivos por coorte e razão de sexo como desfecho & Mesma amostra; exploratória. \\
Substituição ($H_5$) & Notificações de intoxicação ocupacional por agrotóxico agrícola, por município e ano, antes e depois da lei & Tratados e comparação; exploratória. \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria. A quadra chuvosa é tomada, provisoriamente, como
fevereiro a maio; os meses e a medida de chuva são fixados no plano de
análise. Todas as regressões são ponderadas pelo número de nascimentos da célula.}
\end{quadro}
\clearpage
\chapter{Cronologia legal}
\label{ap:cronologia}

\begin{quadro}[htb]
\caption{\label{qua:cronologia}Cronologia legal do tratamento}
\centering
\small
\begin{tabular}{@{}lp{11.2cm}@{}}
\toprule
Data & Evento \\
\midrule
09/12/1993 & Lei Estadual nº 12.228: norma-mãe sobre agrotóxicos no Ceará. \\
20/11/2009 & Limoeiro do Norte proíbe a pulverização aérea por lei municipal (Lei nº 1.478). \\
2010 & Assassinato de Zé Maria do Tomé (abril). Em maio, a Lei municipal nº 1.511 revoga a proibição e passa a regular a prática. \\
2011 & Notícia de proibição na Chapada do Apodi (março); projeto de lei estadual com a mesma vedação (PL nº 134, maio); ação civil pública do Ministério Público (julho), de desfecho não localizado. \\
2012--2017 & Seca no semiárido; relatos de suspensão dos voos na Chapada. \\
24/02/2015 & Apresentação do Projeto de Lei nº 18/2015 (marco de notícia). \\
03/2018 & O estado lança programa de redução da mortalidade materna e neonatal \cite{ceara2018nascer}. \\
18/12/2018 & Aprovação por unanimidade na Assembleia Legislativa (marco de certeza). \\
09/01/2019 & Vigência da Lei nº 16.820 (marco de obrigação). \\
05/2023 & O Supremo Tribunal Federal julga a lei constitucional (ADI 6137). \\
19/12/2024 & Lei nº 19.135: exceção para drones. Fim da janela de análise. \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria, a partir dos textos legais e da tramitação legislativa; os eventos de 2011 a 2017 provêm de fontes secundárias.}
\end{quadro}
\end{apendicesenv}
