# Proibição da pulverização aérea de agrotóxicos no Ceará: efeitos sobre a saúde ao nascer

Projeto de pesquisa — PPGEco/UFES (fonte LaTeX das seções, sem comentários)


<!-- arquivo: paper/projeto/secoes/01-introducao.tex -->

\chapter{Introdução}
\label{cap:introducao}

Em abril de 2010, José Maria Filho, o Zé Maria do Tomé, foi assassinado na
Chapada do Apodi, no interior do Ceará. Ele denunciava havia anos a
pulverização aérea de agrotóxicos sobre os perímetros irrigados da região, onde
aviões sobrevoam plantações de banana e melão vizinhas a casas, escolas e
açudes de abastecimento. A denúncia não tratava do veneno aplicado na lavoura,
mas do veneno que não fica na lavoura. Nove anos depois, o Ceará proibiu a
prática em todo o território, na primeira proibição estadual do gênero no
Brasil, e deu à lei o nome do homem assassinado (Lei Estadual
nº~16.820/2019).

A pulverização aérea é um caso de externalidade em que o mecanismo físico é
visível. Parte da calda liberada pela aeronave não atinge o alvo: é carregada
pelo vento e se deposita fora da área tratada, fenômeno que a literatura
técnica chama de deriva. Quem contrata a aplicação paga pelo serviço e pelo
produto; quem mora a favor do vento arca com o restante. A lei cearense
responde a esse conflito por proibição, e sobre os efeitos dessa resposta
praticamente não há evidência causal no país.

Este projeto pergunta: \textbf{qual é o efeito causal da proibição da
pulverização aérea de agrotóxicos sobre a saúde ao nascer nos municípios
cearenses onde a prática existia?} A pergunta é de avaliação de política
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
replicam a lógica nos Estados Unidos, com aptidão agroclimática como fonte de
variação, e encontram redução do peso ao nascer e da duração da gestação,
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
cearense: mesma cultura, mesmo método, mesma classe de produto.

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
estimativa do que a proibição de fato produziu. Uma avaliação que diga se houve ganho em saúde, onde e de que
tamanho, ou que mostre com rigor por que ele não é mensurável com os registros
existentes, informa tanto os estados que consideram adotar a medida quanto a
decisão de mantê-la, relaxá-la ou substituí-la por outro instrumento.

\section{Contribuição}

A contribuição pretendida tem três camadas. A primeira é de \textbf{objeto}: a
avaliação \emph{ex post} de uma proibição de método de aplicação, instrumento
que o Supremo Tribunal Federal julgou constitucional em 2023 \cite{stf2023adi6137} e que,
por isso, é replicável por outras unidades da federação. A segunda é de
\textbf{medida}: o projeto trata como problema central, e não como nota de
rodapé, a distância entre a cultura plantada e o método de aplicação
efetivamente usado, e propõe medi-la com registros administrativos nunca
explorados para esse fim. A terceira é de \textbf{identificação}: a lei vale
para todo o estado desde a mesma data, de modo que não há variação de
\emph{timing}; o projeto usa um desenho de calendário gestacional
\cite{calzada2023bananas,brainerd2014seasonal}, com os municípios de banana
familiar como grupo de comparação, testa-o no pré-período antes de usar o
pós-lei, e o confronta com um desenho de intensidade de exposição
\cite{callaway2024continuous}.

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

O Quadro~\ref{qua:cronologia} resume a cronologia. Três marcos antecedem o
tratamento e são tratados separadamente: a \emph{notícia} (apresentação do projeto de lei que deu origem à norma, em
2015, precedida de proposição semelhante em 2011 \cite{ceara2011pl134}), a \emph{certeza} (aprovação unânime, em dezembro de
2018) e a \emph{obrigação} (vigência, em janeiro de 2019). Em dezembro de 2024,
a Lei nº~19.135 \cite{ceara2024lei19135} deu nova redação ao artigo e abriu exceção para aeronaves
remotamente pilotadas. O estado não revogou a proibição, mas trocou o
instrumento: de cota zero para regulação de desempenho. Por isso a janela de
análise termina em 19 de dezembro de 2024.

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

\section{A Chapada do Apodi, a cultura e o químico}

A Chapada do Apodi, no Baixo Jaguaribe, concentra a fruticultura irrigada do
Ceará, com destaque para banana e melão. É a região à qual a lei responde e
onde a exposição da população à deriva foi documentada antes da proibição. Na
bananicultura, a aplicação aérea serve ao controle de doenças fúngicas da
folha, que dependem de umidade. No análogo equatoriano, as aplicações se
intensificam na estação chuvosa \cite{calzada2023bananas}; se o mesmo vale para
o bananal irrigado do semiárido é questão que este projeto verifica.

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
segundo ensaio da dissertação. O que este projeto fornece a ela é a premissa
empírica: saber se a proibição produziu o benefício em saúde que a motivou.

\section{Agrotóxicos e saúde ao nascer}

A literatura econômica recente sobre exposição gestacional a agrotóxicos
converge em três regularidades úteis ao desenho.

A primeira é a ordem de grandeza e a sua dependência da proximidade.
\citeonline{reynier2025glyphosate} estimam reduções médias de peso ao nascer da
ordem de 23 a 32 gramas associadas à difusão do glifosato em áreas rurais dos
Estados Unidos. \citeonline{calzada2023bananas} encontram déficit de cerca de
80 gramas, mas apenas para mães que moravam a até 150 metros do perímetro de
um bananal e tiveram três meses ou mais de fumigação intensiva durante a
gestação; para as que moravam mais longe não há gradiente. No Brasil,
\citeonline{rigotto2013trends} comparam municípios da fruticultura irrigada do
Ceará com municípios de agricultura familiar e documentam piores indicadores
de saúde nos primeiros, em estudo ecológico, sem pretensão causal.

A segunda é a concentração. Os efeitos aparecem no topo da distribuição de
exposição \cite{larsen2017agricultural} e na cauda inferior da distribuição de
peso esperado \cite{reynier2025glyphosate}; entre os poucos estudos que isolam
fungicidas está o de \citeonline{jones2020invasive}. A consequência para este
projeto é direta: se o efeito existe só para quem mora junto ao bananal, a
média de um município inteiro o dilui pela fração de nascimentos exposta, e um
desenho municipal pode não encontrá-lo mesmo que ele seja grande.

A terceira é o calendário. Quando a aplicação tem estação, o efeito é
identificado pelo cruzamento entre o período sensível da gestação e a estação
de aplicação: \citeonline{calzada2023bananas} encontram efeito nos dois
primeiros trimestres e estimativa sem significância estatística no terceiro, com a intensidade da fumigação
ditada pela estação chuvosa, e \citeonline{brainerd2014seasonal} usam o mês da
concepção e a estação de aplicação de agroquímicos na Índia. A ameaça
conhecida é a composição sazonal das mães: quem concebe em cada época do ano
difere em características que afetam o desfecho
\cite{buckles2013season,currie2013within}.

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

\textbf{Objetivo geral.} Estimar o efeito causal da proibição estadual da
pulverização aérea de agrotóxicos (Lei nº~16.820/2019) sobre a saúde ao nascer
nos municípios cearenses onde a prática existia.

\textbf{Objetivos específicos.}
\begin{alineas}
  \item medir onde e quando havia aplicação aérea antes da proibição, com
    registros administrativos federais e estaduais;
  \item verificar, só com dados anteriores à lei, se a exposição à estação de
    pulverização deixava marca sazonal no peso ao nascer;
  \item estimar o efeito da proibição pelo desenho de calendário gestacional,
    com os municípios de banana familiar sem registro de aeronave como grupo
    de comparação;
  \item confrontar essa estimativa com a forma reduzida estadual, o controle
    sintético e a comparação de fronteira;
  \item testar a seleção para o nascimento vivo e o canal de substituição da
    aplicação aérea pela terrestre.
\end{alineas}

\textbf{Hipóteses.} A hipótese principal ($H_1$) é que, após a lei, o peso ao
nascer das coortes gestadas na estação de pulverização aumentou, em relação às
demais coortes, nos municípios onde havia aplicação aérea, comparados aos de
banana familiar. A segunda hipótese confirmatória ($H_2$) é que a taxa de
óbito fetal dessas coortes caiu. Como hipóteses de mecanismo, o efeito deve
ser maior nos anos chuvosos e menor quando só o terceiro trimestre coincide
com a estação ($H_3$), e ausente nos municípios de banana familiar comparados
aos sem banana ($H_4$). Como hipótese de substituição ($H_5$), as notificações de
intoxicação ocupacional por agrotóxico agrícola podem aumentar, se a aplicação
migrou do avião para o trator e o pulverizador costal.


<!-- arquivo: paper/projeto/secoes/05-metodologia.tex -->

\chapter{Metodologia}
\label{cap:metodologia}

\section{Parâmetro-alvo e cadeia causal}

O parâmetro de interesse é o efeito médio da retirada da aplicação aérea de
agrotóxicos em bananais sobre o peso ao nascer das gestações que coincidiriam
com a estação de pulverização, nos municípios cearenses onde a prática existia.
Em notação de resultados potenciais, com $Y(1)$ e $Y(0)$ os desfechos com e
sem a proibição,
\begin{equation}
  ATT = E\left[\,Y_{mt}(1) - Y_{mt}(0) \mid A_m = 1,\ S_t = 1,\ t \text{ pós-lei}\,\right],
\end{equation}
em que $A_m$ indica município com aplicação aérea às vésperas da lei e $S_t$
indica coorte cuja gestação atravessa a estação de pulverização. É um efeito
sobre coortes expostas, e não sobre municípios: ele declara \emph{quem} é
tratado, o que uma medida municipal de intensidade agrícola não consegue fazer.

A cadeia que liga a lei ao desfecho tem elos que podem falhar separadamente: a
lei precisa ter sido cumprida; precisava haver voos a suspender; a suspensão
precisa reduzir a exposição das gestantes, e não apenas trocá-la pela da
aplicação terrestre; e a menor exposição precisa alterar o desfecho. A cada elo
a população efetivamente tratada encolhe: dos municípios do estado para os que
têm banana, destes para os que tinham avião, destes para os em que se voava em
2018, e destes para as gestantes que moravam perto de um bananal pulverizado.
Um efeito nulo no desfecho final não distingue falha de implementação de falha
do mecanismo; por isso o desenho mede os elos intermediários antes do desfecho.

\section{Desenho principal: diferença tripla de calendário}
\label{sec:calendario}

A Figura~\ref{fig:dag} resume as hipóteses causais do desenho. O tratamento é a
interação entre estar sob a proibição e ter a gestação na estação de
pulverização. Compara-se, dentro de cada município, as coortes cujos dois
primeiros trimestres de gestação coincidem com a estação de pulverização com as
demais, antes e depois da lei, e contrasta-se essa diferença entre municípios
com aplicação aérea e municípios de comparação.

\begin{figure}[htb]
\caption{\label{fig:dag}Diagrama causal do desenho de calendário}
\centering
\footnotesize
\begin{tikzpicture}[y=0.88cm,
  box/.style={draw, rounded corners=1pt, align=center, inner sep=3pt, text width=3.4cm},
  lat/.style={box, dashed},
  ar/.style={-{Stealth[length=2mm]}, semithick},
  thr/.style={ar, dashed}]
\node[box] (est) at (0,0) {Gestação na estação de pulverização};
\node[box] (pos) at (5,0) {Município com avião $\times$ pós-lei};
\node[box, fill=black!10] (T) at (5,-2) {\textbf{Lei $\times$ estação}: coorte que deixa de receber o voo};
\node[box] (chu) at (0,-2.9) {Chuva do ano (modifica o efeito)};
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
setas tracejados: não observados ou ameaças que os efeitos fixos não removem.}
\end{figure}

Seja $P_t \in [0,1]$ a fração dos dois primeiros trimestres da coorte $t$ que
cai na estação de pulverização, e $Pos_t$ o indicador de gestação integralmente
posterior a 9 de janeiro de 2019. Estima-se
\begin{equation}
  Y_{mt} = \alpha_{m,s(t)} + \gamma_t + \lambda\,(A_m \times Pos_t)
         + \beta\,(A_m \times P_t \times Pos_t) + \varepsilon_{mt},
  \label{eq:ddd}
\end{equation}
em que $\alpha_{m,s(t)}$ são efeitos fixos de município por mês do ano e
$\gamma_t$, efeitos fixos de coorte. O coeficiente $\beta$ mede quanto o hiato
sazonal de peso ao nascer se alterou, após a lei, nos municípios com aplicação
aérea, em relação aos de comparação; sob a hipótese principal, $\beta > 0$. Os
efeitos fixos absorvem a composição das mães por mês de concepção, a
sazonalidade de base de cada município e os choques comuns a todas as coortes
de um município num dado ano, entre eles os programas estaduais de saúde
materna contemporâneos à lei. A janela gestacional é fixa: a duração observada
da gestação é desfecho, e usá-la para definir a exposição condicionaria em
variável afetada pelo tratamento. O terceiro trimestre, para o qual o análogo
equatoriano encontra estimativa sem significância estatística, serve de
contraste de efeito menor.

\textbf{Grupo de comparação.} Os municípios de comparação são os produtores de
banana em que a cultura é predominantemente familiar, segundo o Censo
Agropecuário de 2017 \cite{ibge2017censoagro}: têm a cultura, o clima e o
calendário agrícola e, por hipótese, não têm o avião. A hipótese é verificada
nos relatórios do Ministério da Agricultura e no Censo de 2006, que registra
aplicação aérea também fora dos polos irrigados; município com qualquer
registro de aeronave é excluído do grupo de comparação. Em nível, essa comparação não seria válida: agricultura familiar e
empresarial diferem em renda, acesso a programas sociais e exposição à
aplicação costal, e a comparação reproduziria essas diferenças. Dentro da
diferença tripla, as diferenças de nível e de tendência geral entre os dois
grupos são absorvidas, e o que se exige é menos: que, na ausência da lei, o
hiato sazonal tivesse evoluído do mesmo modo nos dois \cite{olden2022triple}.
A mesma lógica fornece um teste de tratamento falso: comparados aos municípios
sem banana, os de banana familiar não deveriam reagir à lei.

\textbf{Chuva.} A doença fúngica que motiva o voo depende de umidade. A chuva
da quadra chuvosa modifica o efeito, e por isso entra como interação com o
termo de interesse, e não como controle: prevê-se efeito maior nos anos
chuvosos do pós-lei e pequeno ou nulo nos secos. A chuva também afeta a saúde
por outras vias, como as arboviroses, o que limita essa leitura
(Capítulo~\ref{cap:ameacas}).

\section{Diagnóstico de abertura, sem usar o pós-lei}
\label{sec:diagnostico}

Antes de qualquer contato com os desfechos do pós-lei, o mesmo contraste
sazonal é estimado no pré-período: as coortes gestadas na estação de
pulverização tinham peso menor que as demais, nos municípios com avião em
relação aos de comparação? A pergunta é feita em dois subperíodos: aquele em
que há registro de voos na Chapada e aquele em que, segundo relatos, a seca os
suspendeu (Seção~\ref{sec:onde-aviao}). Um gradiente sazonal presente no
primeiro e ausente no segundo mostraria que a exposição existia, que ela
aparece nos dados municipais e que a seca a interrompeu. A ausência de
gradiente em ambos indicaria que a exposição era pequena ou que sua diluição
na média municipal é total; nos dois casos, a comparação antes e depois da lei
não teria o que detectar. O diagnóstico decide também qual pré-período serve
de referência à Equação~\ref{eq:ddd}, e não consome graus de liberdade da
análise confirmatória.

\section{Medição do método}
\label{sec:medicao}

A classificação $A_m$ e o calendário de pulverização são medidos, e não
supostos. Cinco fontes são mobilizadas, as três primeiras por pedidos de
acesso à informação:
\begin{alineas}
  \item os relatórios mensais que as empresas de aviação agrícola entregam ao
    Ministério da Agricultura \cite{mapa2008in2}, com município, cultura, área
    e produto, de 2012 a 2018, para o Ceará e o Rio Grande do Norte, incluídos
    os operadores sediados em outros estados;
  \item o receituário agronômico, que registra a modalidade de aplicação
    \cite{brasil2002decreto4074};
  \item o cadastro estadual de prestadores de serviço de aplicação e os autos
    de infração posteriores à lei \cite{ceara1993lei12228};
  \item os autos da ação civil pública de 2011, na Justiça Federal;
  \item o Censo Agropecuário de 2006 \cite{ibge2006censoagro}, que fornece a
    classificação provisória enquanto os registros não chegam.
\end{alineas}
Sem esses registros, a estação é tomada da quadra chuvosa, como hipótese
agronômica declarada, e $A_m$, do Censo de 2006.

\section{Interferência e versões do tratamento}

O desenho supõe que o tratamento de um município não altera o desfecho de
outro e que o tratamento tem uma só versão. As duas condições são examinadas,
e não presumidas. Quatro canais de interferência são conhecidos: a deriva
sobre municípios vizinhos e o aquífero compartilhado, que melhorariam os
vizinhos e atenuariam a estimativa; a migração do serviço aéreo para áreas sem
proibição, que os pioraria e a inflaria; e a mobilidade das mães. Por isso os
vizinhos imediatos dos municípios tratados são separados dos demais, formando
três grupos: tratados, não tratados expostos e não tratados não expostos.
Quanto às versões, estar sob a lei significa coisas diferentes: ter voado e
parado; ter trocado o avião pela aplicação terrestre; ter passado ao drone;
não ter cumprido; ou não voar desde antes, por causa da seca. O tratamento é
definido como cessação efetiva de voos e medido como tal, e as demais versões
são tratadas como heterogeneidade a documentar.

\section{Análises secundárias e triangulação}

Três análises complementam o desenho principal, e só há convencimento se
concordarem com ele. A primeira é a forma reduzida estadual: um
diferenças-em-diferenças com tratamento contínuo \cite{callaway2024continuous},
em que a dose é a área plantada de banana antes da lei \cite{ibgepam} e o alvo
é o efeito no nível, $ATT(d \mid d)$. Como a área mede a cultura e não o
método, e supondo que não haja avião sem a cultura, o que se identifica é
\begin{equation}
  \theta = VPP \times ATT,
  \label{eq:atenuacao}
\end{equation}
em que $VPP$ é a fração dos classificados como tratados que de fato o eram
\cite{denteh2022misclassification}: o sinal é preservado e a magnitude,
atenuada. A segunda é o controle sintético e o diferenças-em-diferenças
sintético \cite{arkhangelsky2021sdid} para o agregado dos municípios com
avião, com doadores fora do alcance da interferência. A terceira é a
comparação com os municípios potiguares da Chapada do Apodi, do outro lado da
divisa. Ela não é experimento natural limpo, porque tudo o que é estadual muda
junto na divisa e as culturas diferem entre os dois lados, e por isso entra
apenas como uma das diferenças.

\section{Regra de decisão}
\label{sec:regra}

O Quadro~\ref{qua:regra} fixa, antes do dado do pós-lei, o que cada resultado
da medição e do diagnóstico aciona.

\begin{quadro}[htb]
\caption{\label{qua:regra}Regra de decisão}
\centering
\small
\begin{tabular}{@{}p{6.4cm}p{8.1cm}@{}}
\toprule
O que a medição e o diagnóstico mostram & O que o ensaio estima \\
\midrule
Voos documentados às vésperas da lei, com calendário, e gradiente sazonal no pré-período &
Desenho principal com municípios e estação medidos. \\
Voos documentados, sem calendário &
Desenho principal com a quadra chuvosa como hipótese declarada. \\
Voos suspensos pela seca até a lei &
Desenho principal com interação por chuva; o efeito é o de impedir a volta dos voos. \\
Nenhum gradiente sazonal no pré-período e nenhum registro de voo &
Forma reduzida estadual e diagnóstico de medida e de poder, sem estimativa de efeito da pulverização. \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria.}
\end{quadro}

\section{Inferência, poder e plano de análise}

Há poucos municípios tratados, e a lei é atribuída no nível do estado. Erros-padrão
agrupados por município, com aproximação assintótica, superestimam a
precisão, e o \emph{wild cluster bootstrap} isolado não é defensável com tão
poucos tratados \cite{mackinnon2018wild}. A inferência principal usa os
procedimentos de \citeonline{conley2011} e de \citeonline{ferman2019inference},
este último com heterocedasticidade por tamanho de município, a inferência
conformal de \citeonline{chernozhukov2021conformal} e, para o caso-limite, o
procedimento de \citeonline{hagemann2025single}; na diferença tripla, em que a
variação é interna ao município, aplica-se também \citeonline{canay2021wild}.

Dois fatores limitam o poder e nenhum se resolve com mais anos de dados: o
número de municípios com aplicação aérea e a fração dos nascimentos de cada um
efetivamente exposta. O efeito mínimo detectável de cada análise é calculado
apenas com dados do pré-período e comparado às magnitudes da literatura para
diferentes frações expostas; análise cujo efeito mínimo detectável supere o
efeito plausível é reportada como limite, e não como teste. Duas hipóteses são
confirmatórias, com correção de Holm, e as demais são exploratórias.

A estação, o corte de chuva, os grupos e os contrastes de falsificação são
fixados em plano de análise versionado antes de qualquer cruzamento com os
desfechos do pós-lei, e a escolha do desenho principal é ratificada com o
orientador nesse momento. Um plano para a forma reduzida estadual foi escrito
e versionado em setembro de 2026; uma rodada exploratória dessa análise já foi
executada e levou a rever seu alvo, da curva para o nível. Ela não é reportada aqui e será refeita a partir das bases originais; o
desenho de calendário foi adotado como principal depois dela, sem que a
exposição sazonal tenha sido cruzada com os desfechos. São planos versionados em
repositório, não pré-registro público.


<!-- arquivo: paper/projeto/secoes/06-dados.tex -->

\chapter{Dados}
\label{cap:dados}

A unidade de análise é o município por mês de nascimento, para os 184
municípios do Ceará. O período de avaliação da lei vai até 19 de dezembro de
2024; o painel recua a 2005 para o diagnóstico do pré-período. Os desfechos
vêm de registros administrativos de cobertura universal; o
Quadro~\ref{qua:fontes} resume as fontes e a forma de acesso. Todo o
processamento será feito a partir das bases originais.

\begin{quadro}[htb]
\caption{\label{qua:fontes}Fontes de dados}
\centering
\small
\begin{tabular}{@{}p{3.8cm}p{6.4cm}p{4.2cm}@{}}
\toprule
Fonte & Uso & Acesso \\
\midrule
SINASC (DATASUS) & Peso ao nascer, baixo peso, prematuridade & Público \\
SIM (DATASUS) & Óbito fetal & Público \\
SINAN (DATASUS) & Notificações de intoxicação por agrotóxico & Público \\
PAM (IBGE) & Área plantada por cultura: dose & Público \\
Censo Agropecuário 2006 (IBGE) & Estabelecimentos com aplicação por aeronave & Público \\
Censo Agropecuário 2017 (IBGE) & Participação da agricultura familiar: grupo de comparação & Público \\
Precipitação (FUNCEME, INMET) & Chuva da quadra chuvosa: modificador de efeito & Público \\
FAO-GAEZ & Aptidão agroclimática: forma reduzida estadual & Público \\
População (IBGE) & Denominadores & Público \\
Leis municipais & Proibições locais anteriores a 2019 & Público (câmaras municipais) \\
Relatórios mensais (MAPA) & Aplicação aérea por município e mês, CE e RN & Pedido de acesso à informação \\
Receituário (ADAGRI) & Modalidade de aplicação & Pedido de acesso à informação \\
Cadastro (SEMACE) & Prestadores de aplicação aérea & Pedido de acesso à informação \\
Autos judiciais (JFCE) & Prática na Chapada após 2011 & Consulta processual \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria.}
\end{quadro}

\textbf{Desfechos.} Do SINASC obtêm-se o peso médio ao nascer (desfecho
confirmatório), a proporção de nascidos com menos de 2.500 gramas e a
proporção de nascidos com menos de 37 semanas de gestação (exploratórios). Do SIM obtém-se a taxa de óbito fetal, segundo desfecho confirmatório, e
constrói-se um desfecho composto que soma nascidos vivos e óbitos fetais. O óbito
fetal tem função dupla: é desfecho de saúde e é teste de seleção. Se a
proibição reduz perdas fetais, gestações que antes não chegariam ao nascimento
vivo passam a entrar na amostra de nascidos, possivelmente na cauda de baixo
peso, e o efeito sobre o peso médio sai atenuado. Do SINAN obtêm-se as
notificações de intoxicação por agrotóxico agrícola, por circunstância, para o
canal de substituição; as intoxicações intencionais, que respondem à
disponibilidade do produto e não ao método de aplicação, servem de placebo.

\textbf{Exposição.} A classificação pelo método vem do Censo Agropecuário de
2006 e, na medida do retorno dos pedidos de acesso, dos registros da
Seção~\ref{sec:medicao}; o grupo de comparação, do Censo Agropecuário de 2017;
a dose da forma reduzida, da PAM. Como a lei estadual de 1993
autoriza os municípios a legislar supletivamente, proibições locais
anteriores a 2019 contaminariam o período de comparação; um levantamento
preliminar encontrou uma, em Limoeiro do Norte, de 2009, revogada em 2010
\cite{limoeiro2010lei1511}. O levantamento será refeito, com conferência de
vigência.

\textbf{Escopo.} O canal hídrico, que exigiria medições de agrotóxicos na
água de consumo com localização dos pontos de coleta, não integra a análise
confirmatória, e a exposição não é medida no nível da residência. Uma avaliação preliminar do monitoramento da qualidade da água e do mapeamento
de uso da terra por satélite indicou limitações para esses fins; ela será
refeita e documentada antes de qualquer uso.

\textbf{Reprodutibilidade e sigilo.} O processamento será feito por rotinas
versionadas, com a data de extração de cada base registrada. Os microdados não
são redistribuídos, e células com poucos eventos não são divulgadas.

\textbf{Aspectos éticos.} A pesquisa utiliza exclusivamente dados secundários
de acesso público, sem identificação individual, e informações obtidas por meio
da Lei de Acesso à Informação. Pesquisas dessa natureza não são submetidas ao
sistema CEP/CONEP, nos termos da Resolução nº~510/2016 do Conselho Nacional de
Saúde \cite{cns2016res510}.


<!-- arquivo: paper/projeto/secoes/07-ameacas.tex -->

\chapter{Ameaças à identificação}
\label{cap:ameacas}

O Quadro~\ref{qua:ameacas} reúne as ameaças conhecidas, o que cada uma faz à
estimativa e o que o desenho lhe opõe. Três merecem comentário.

\begin{quadro}[htb]
\caption{\label{qua:ameacas}Ameaças à identificação e respostas do desenho}
\centering
\footnotesize
\begin{tabular}{@{}p{3.6cm}p{4.7cm}p{6.2cm}@{}}
\toprule
Ameaça & Efeito sobre a estimativa & Resposta \\
\midrule
Voos suspensos pela seca antes da lei &
Pouco tratamento a retirar; nulo por ausência de exposição &
Relatórios do MAPA; diagnóstico no pré-período; interação com a chuva. \\
Diluição dentro do município &
Efeito individual multiplicado pela fração exposta &
Poder calculado para diferentes frações; resultado abaixo do detectável lido como limite. \\
Mudança de sazonalidade só nos municípios com avião, após a lei &
Viola a hipótese de identificação do desenho principal &
Tratamento falso com banana familiar; estimativas com e sem 2020--2021. \\
Políticas estaduais de saúde materna contemporâneas &
Melhora geral do Ceará no pós-lei &
Absorvida pelos efeitos fixos se comum às coortes; ameaça a fronteira e a forma reduzida. \\
Chuva com efeito próprio sobre a saúde &
Confunde a interação por chuva &
Interação lida como mecanismo, não como teste; controle por arboviroses notificadas. \\
Seleção para o nascimento vivo &
Efeito sobre o peso médio atenuado ou invertido &
Óbito fetal confirmatório; desfecho composto com nascidos vivos e óbitos fetais. \\
Interferência entre municípios &
Sinal indeterminado: deriva e aquífero atenuam, realocação infla &
Três grupos; doadores fora do alcance; pedido ao MAPA também para o estado vizinho. \\
Substituição pela aplicação terrestre e fiscalização desconhecida &
Parâmetro é de intenção de tratar; exposição ocupacional pode subir &
Notificações de intoxicação; autos de infração; faz parte do efeito da política. \\
Antecipação (projetos de lei de 2011 e 2015) &
Dose e pré-período respondem antes da vigência &
Coortes de transição excluídas; o desenho principal não usa a dose. \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria.}
\end{quadro}

\textbf{A seca.} É a ameaça que mais muda o desenho. Se os voos estavam
suspensos de 2012 até as vésperas da lei, a comparação entre os quatro anos
anteriores e os posteriores a 2019 opõe pouco avião a nenhum avião, e a lei
teria mordido apenas quando a chuva e a doença voltaram. As fontes dessa
suspensão são de imprensa e de parte interessada, e não registros; por isso
ela é tratada como hipótese, a ser decidida pelos relatórios mensais e pelo
diagnóstico do pré-período, e não como fato.

\textbf{A diluição.} O análogo mais próximo encontra efeito apenas a até 150 metros
do bananal. O registro de nascimentos identifica o
município de residência da mãe, não a distância à lavoura. Mesmo nos
municípios com aplicação aérea, a maior parte dos nascimentos é de mães não
expostas, e o efeito médio municipal é o individual multiplicado por essa
fração. Concentrar a comparação nas coortes da estação reduz o problema no
tempo, mas não no espaço, e nenhuma fonte disponível o resolve. A resposta é
dizer de antemão qual efeito o desenho consegue detectar.

\textbf{A sazonalidade.} O desenho principal só tem o que medir se a aplicação
aérea tiver pico sazonal: se ela for uniforme ao longo do ano, como pode
ocorrer em bananal irrigado, o desenho mede zero por construção. A existência
do pico é verificada antes da estimação, nos relatórios mensais e no
diagnóstico do pré-período.


<!-- arquivo: paper/projeto/secoes/08-cronograma.tex -->

\chapter{Resultados esperados e cronograma}
\label{cap:cronograma}

\textbf{Resultados esperados.} O projeto entrega, em qualquer dos cenários do
Quadro~\ref{qua:regra}: (i) a primeira medida municipal e mensal da aplicação
aérea de agrotóxicos no Ceará antes da proibição, a partir de registros
administrativos; (ii) o diagnóstico, só com dados do pré-período, de se essa
exposição deixava marca sazonal no peso ao nascer; e (iii) o efeito mínimo
detectável de cada análise, calculado antes da estimação. Se a medição e o
diagnóstico confirmarem a exposição, entrega também (iv) a estimativa do
efeito da proibição pelo desenho de calendário, confrontada com a forma
reduzida estadual, o controle sintético e a fronteira. Se não confirmarem, o
ensaio se entrega como diagnóstico de medida e de poder de uma política cujo
efeito os registros disponíveis não permitem estimar, resultado que também
informa o debate. A estimativa do benefício em saúde é o insumo empírico do
segundo ensaio da dissertação, sobre a escolha entre proibir, taxar e regular
a aplicação.

\textbf{Cronograma.} O Quadro~\ref{qua:cronograma} distribui as atividades em
bimestres. Os pedidos de acesso à informação são protocolados no primeiro
bimestre porque seu prazo de resposta condiciona o desenho principal.

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
Diagnóstico sazonal do pré-período e cálculo de poder & & X & & & & \\
Classificação dos municípios pelo método e pela agricultura familiar & & X & X & & & \\
Plano de análise, ratificado com o orientador & & & X & & & \\
Desenho principal, análises secundárias e triangulação & & & X & X & & \\
Redação do ensaio e qualificação & & & & X & X & \\
Segundo ensaio (escolha de instrumento) & & & & & X & X \\
Revisão final e defesa & & & & & & X \\
\bottomrule
\end{tabular}
\fonte{Elaboração própria. Bimestre 1: dezembro de 2026 e janeiro de 2027.}
\end{quadro}
