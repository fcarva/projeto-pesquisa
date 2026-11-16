# Registro do processo de elaboração — projeto de pesquisa (rodada ARS 21, local)

*Estágio 6 do academic-pipeline (ARS v3.24.2). Gerado em 2026-11-16.*

**De onde vem cada coisa.** Este registro foi compilado por um agente que não
viu a conversa. As fontes são: o ledger (`passport_run_ledger.yaml`, 30
entradas), o passport, os relatórios da pasta `docs/ars/rodada21-local/` e uma
lista, passada pelo orquestrador, das mensagens do pesquisador e dos erros da
IA que não estão nos arquivos. As citações do pesquisador são literais, com a
grafia original. Onde a resposta foi dada por seleção de opção, o registro
diz. O manuscrito e os dados não foram abertos; nada foi executado. A pergunta
do protocolo sobre idioma e PDF não foi feita ao pesquisador: o registro sai só
em português e só em Markdown, como na rodada 20.

## 1. O trabalho e os entregáveis

- **Título:** Proibição da pulverização aérea de agrotóxicos no Ceará: efeitos
  sobre o peso ao nascer.
- **Natureza:** projeto de pesquisa de mestrado (PPGEco/UFES), só o primeiro
  ensaio, sem estimativa própria no texto.
- **Entregável principal:** `paper/projeto/` (abnTeX2, `pdflatex` + `bibtex`),
  versão final **projeto_v14**. O PDF tem 40 páginas, 15 textuais (p. 5 a 19),
  Referências na p. 20, 58 referências, Apêndices A a F.
- **Hashes (passport):** fontes
  `sha256:c5f1c6c754ffa72ca0a0641f1abff92962763caa3b226127f7e56ef1b90d89ec`;
  PDF `0ceccc0873fa96c2a257d01ea0f465ddab0fa15635fe2088283bc99594326d93`. Não
  foram recalculados por este registro.
- **Documentos de apoio da rodada:** conferência local de fontes; mapa de
  lacunas e rodada exploratória; fundamentos de avaliação de política; seis
  relatórios de integridade; análise de campo, cinco pareceres, decisão
  editorial e carta ao autor; resposta aos pareceres, notas de revisão e
  resposta aos resíduos; relatório de re-revisão; `RETOMAR.md` (escrito na
  pausa e hoje desatualizado: ainda diz que faltam os Estágios 3', 4.5, 5 e 6).
- **Fora do git:** nada foi commitado em nenhum momento desta rodada. O
  orquestrador ofereceu e não houve resposta. Inclui o PDF de 28 MB da Lei
  municipal 1.511/2010 e os roteiros `scripts/exploratorio/20` a `23`.
- **Modelo:** o mesmo (`claude-fable-5-2`) para redação, verificação, os
  cinco assentos do painel, a síntese e a re-revisão. Nenhuma verificação por
  outro modelo.

## 2. Percurso, estágio a estágio

Os horários do ledger estão em UTC; a sessão começou na noite de 15/11 no
horário local e terminou na manhã de 16/11.

**Abertura.** O pesquisador pediu para atualizar o ramo e colou a passagem de
bastão escrita na sessão em nuvem. O pedido terminava com: "Siga o protocolo do
plugin à risca: ledger, passport e ponto de decisão a cada estágio. Não rode
nada sobre dados reais." Em seguida escreveu, em palavras próprias: "Vamos
buscar melhorias agora com os arquivos locais, como base explonátórias, fazer
todos os modos, usar a pasta projeto-pesquisa para rodar coisas que não eram
rodadas no cloud, fazer full mode, continuar auditoria localemente". As duas
instruções conflitam, e o orquestrador registrou o conflito na pergunta de
entrada (ledger, seq 2).

**Fase exploratória, antes do Estágio 2.5.** O pesquisador resolveu o conflito
a favor de rodar: "Vamos continuar explorando as lacunas que não conseguimos
suprir, as estimativas passadas não contam, vamos rodar novas com dados reais,
e mapear o que falta, fica como fonte, segue" (seq 3). A IA avisou do custo (o
desenho passaria a ter sido visto contra o desfecho do pós-lei) e executou.
Nessa fase o pesquisador fez as suas intervenções de conteúdo, nenhuma delas
registrada no ledger:

- "Em relação a dados do rio grande do norte chapada do Apodi, nós temos?"
- "Inclua, é fundamental para nosso tramento controle, usar fundamentos de
  avaliação de política pública, para contexto."
- "Vamos usar aval pol material do Cunningham para leads and lags aqui,
  precisamos de fundamento pra mais / Para mais: continuar avançando"
- "Pegar os materiais do repositório licc gov e aval pol só no que tange
  avaliação de política pública, não contaminar com outro artigo."

Saíram daí: o painel de nascimentos Ceará + Rio Grande do Norte de 2005 a
2024; a conferência da Lei 1.511/2010 e do Dossiê Abrasco na fonte primária;
os roteiros exploratórios 20 a 23; o mapa de lacunas; e o documento de
fundamentos. Depois o pesquisador encerrou a fase: "Vamos voltar para a linha
e objetivo aqui, rodar o que for necessário para avançar".

**Entrada no Estágio 2.5.** Por seleção de opção: declaração de experimentos
"Não reporta"; restrições permanentes "Confirmo as cinco"; teto de 80 g
"Decido depois"; divulgação da rodada exploratória "Decido depois" (seq 4). O
reconhecimento do Estágio 6 da rodada 20, pedido na mesma pergunta, ficou sem
resposta.

**Estágio 2.5 — integridade (v7 a v10).** Três verificações.

1. **FAIL** (2 SERIOUS, 1 MEDIUM, 9 MINOR; 51 de 51 referências existem). As
   duas falhas graves eram de afirmação. A primeira: o texto dizia que a
   exposição sazonal não tinha sido cruzada com os desfechos, e a rodada de
   15/11 acabara de fazer isso. A segunda: "o único relato disponível" e o
   "teto" de 80 g, contraditos pelo Dossiê Abrasco (seis a oito aplicações por
   ano na Chapada) e pelo próprio artigo equatoriano (80 g é o piso do
   intervalo). Modos de falha 3 e 6 SUSPECTED, com bloqueio. Resposta do
   pesquisador: "Aplique alterações que julgar melhorar o trabalho" (seq 6). A
   IA aplicou as quatro opções que ela mesma tinha recomendado.
2. **FAIL** (0 SERIOUS, 2 MEDIUM, 6 MINOR). Um dos MEDIUM foi criado pela
   correção: ao trocar "teto" por "intervalo de 80 a 150 g", a regra de decisão
   ficou sem limiar.
3. **PASS WITH NOTES** (0 SERIOUS, 0 MEDIUM, 8 MINOR), com duas classificações
   de fronteira que o verificador declarou como julgamento seu. Os Modos 3 e 6
   continuaram SUSPECTED, só pela regra formal. O pesquisador respondeu:
   "Painel cego e continue", e escolheu a justificativa "Projeto, não
   resultado" por seleção de opção (seq 10).

**Estágio 3 — painel (v10).** "Aceito os cartões" (seq 12). Cinco assentos em
duas fases, painel instruído a ser cego. Decisão mecânica: **revisão
substancial** (bloqueio reparável em método, coerência do argumento e adequação
à banca). O achado crítico do advogado do diabo (C1: a premissa de que os voos
voltariam depois da seca) foi validado no núcleo. Roteiro de 34 itens: 9
obrigatórios, 20 recomendados, 5 a considerar. Resposta do pesquisador: "Vamos
ao último estagio" e, por opção, "Revisar e seguir até o fim" (seq 14). Quatro
perguntas de fato ficaram sem resposta (prazo e data de defesa; número do
efeito detectável; premissa de volta dos voos; depósito público do plano).

**Estágio 4 — revisão (v11).** O agente de revisão respondeu aos 34 itens e
criou o Apêndice F. Tomou, sem resposta do pesquisador, as decisões listadas
na Seção 4.2 deste registro. No ponto de decisão o pesquisador pausou: "Vamos
finalizar por hoje para concluir mais tarde" (seq 16). Dois minutos depois,
pelo ledger, retomou: "Rode tudo então até terminal o objetivo" (seq 18). O
orquestrador leu isso como seguir com as recomendações, manter as decisões
provisórias sem ratificação item a item e fazer a re-revisão em modo legado.

**Estágio 3' — re-revisão (modo legado).** **Revisão menor.** Dos 34 itens: 18
atendidos, 15 em parte, nenhum sem resposta, 1 recusado com motivo. Quinze
achados novos, um deles grave: a célula que decide o portão de poder foi
fixada depois de conhecido o resultado exploratório, e o texto dizia "não se
sabe ainda qual linha do Quadro é a provável". A re-revisão apontou sete
lugares em que a resposta do autor alegava mais do que o texto fazia. Dezoito
resíduos (RES-01 a RES-18). Não houve resposta específica do pesquisador: o
checkpoint foi fechado sob a instrução anterior (seq 20).

**Estágio 4' (v12).** Quinze resíduos aplicados, um em parte (RES-13), dois
deixados como pendência do autor (RES-17 e RES-18). O ledger não registra
ponto de decisão para este estágio.

**Estágio 4.5 — integridade final (v12 a v14).** Três verificações.

1. **FAIL** (0 SERIOUS, 1 MEDIUM, 11 MINOR; 58 de 58 referências existem).
   Modo 1 INSUFFICIENT EVIDENCE, Modos 3 e 6 SUSPECTED. Condição 4 de C4/D7 em
   FAIL formal. Resposta por seleção de opção marcada como recomendada:
   "Manter e justificar" (seq 24).
2. **FAIL** (0 SERIOUS, 0 MEDIUM, 3 MINOR). Os doze achados da rodada 1
   resolvidos. O verificador abriu as saídas gravadas, refez a conta e deu o
   Modo 1 como CLEAR.
3. **FAIL formal**, por uma única causa (C4/D7, condição 4). Zero achados no
   texto. Modos 3 e 6 OVERRIDDEN. O laço de três rodadas se esgotou. Resposta
   por seleção de opção recomendada: "Seguir com a frase" (seq 27).

**Estágio 5.** Finalização em abnTeX2, sem resposta específica (seq 29, sob
"Rode tudo então até terminal o objetivo"). Os avisos #660 e #672 do
protocolo não foram executados.

## 3. Números do processo

| Item | Valor |
|---|---|
| Versões do projeto | 8 rótulos (v7 de entrada a v14), 7 revisões |
| Verificações de integridade | 6 (3 no 2.5: FAIL, FAIL, PASS WITH NOTES; 3 no 4.5: FAIL, FAIL, FAIL formal) |
| Achados do 2.5, por rodada (SERIOUS / MEDIUM / MINOR) | 2/1/9; 0/2/6; 0/0/8 |
| Achados do 4.5, por rodada | 0/1/11; 0/0/3; 0/0/0 |
| Referências citadas | 51 na entrada, 58 no fim; nenhuma fabricada em nenhuma rodada |
| Pareceres | 5 (quatro assentos e o advogado do diabo), mais a síntese |
| Itens do roteiro | 34 (9 obrigatórios, 20 recomendados, 5 a considerar) |
| Resposta do autor (corrigida) | 18 atendidos, 13 em parte, 3 limitação declarada |
| Re-revisão | 1, modo legado: 18 atendidos, 15 em parte, 0 sem resposta, 1 recusado; 15 achados novos (1 grave) |
| Resíduos | 18: 15 aplicados, 1 em parte, 2 pendência do autor |
| Checkpoints no ledger | 11 abertos e 11 fechados (9 obrigatórios, 2 completos, nenhum reduzido), mais 1 resposta parcial |
| Fechados com palavras próprias do pesquisador | 7 (três deles com parte da resposta por opção) |
| Fechados só por seleção de opção | 2 (os dois do Estágio 4.5, opção marcada "Recomendado") |
| Fechados sem resposta específica | 2 (Estágio 3' e entrada do 5), sob "Rode tudo então até terminal o objetivo" |
| Escolhas por seleção de opção registradas | pelo menos 8 (quatro na entrada; a justificativa do 2.5; "Revisar e seguir até o fim"; as duas do 4.5) |
| Mensagens do pesquisador na sessão | 16, das quais 1 vazia e 2 coladas de outra sessão |
| Perguntas do orquestrador sem resposta | pelo menos 12 (lista na Seção 4.3) |
| Commits | 0 |

Das sete respostas em palavras próprias, quatro são de rumo geral ou de
delegação ("Aplique alterações que julgar melhorar o trabalho", "Vamos ao
último estagio", "Vamos finalizar por hoje para concluir mais tarde", "Rode
tudo então até terminal o objetivo"). Nenhuma decide, em palavras do
pesquisador, um ponto de método levantado pelos pareceres.

## 4. Decisões

### 4.1 Decisões do pesquisador, em ordem

1. Rodar a rodada 21 na máquina local, em modo completo, usando a pasta com
   os dados ("fazer todos os modos […] fazer full mode").
2. Autorizar estimativas novas com dado real, como exploratórias, e
   desconsiderar as de setembro ("as estimativas passadas não contam, vamos
   rodar novas com dados reais"). Contraria a regra da passagem de bastão que
   ele próprio colou.
3. Trazer o Rio Grande do Norte e a Chapada potiguar para a comparação
   ("Inclua, é fundamental para nosso tramento controle").
4. Usar fundamentos de avaliação de política pública e o material de
   Cunningham para leads e lags.
5. Restringir o material de apoio: "só no que tange avaliação de política
   pública, não contaminar com outro artigo".
6. Voltar ao pipeline ("Vamos voltar para a linha e objetivo aqui").
7. Declarar "Não reporta" na pergunta sobre experimentos; confirmar as cinco
   restrições; adiar teto de 80 g e divulgação (por opção).
8. Delegar à IA as correções do 2.5 ("Aplique alterações que julgar melhorar
   o trabalho").
9. Painel cego. Afastar o bloqueio dos Modos 3 e 6 (justificativa por opção).
10. Aceitar os cartões dos pareceristas.
11. Revisar e seguir até o fim, sem triagem item a item.
12. Pausar; depois retomar e mandar rodar até o fim.
13. Manter a divulgação do resultado exploratório e justificar (4.5, opção
    recomendada).
14. Seguir com a frase, aceitando o item formal não resolvido ao fim das três
    rodadas (opção recomendada).

### 4.2 Decisões da IA por delegação, ainda sem ratificação

Nenhuma das decisões abaixo tem resposta do pesquisador. Todas estão no
texto que irá à banca. A lista vem de `stage4/response_to_reviewers.md`,
`stage4/revision_notes.md` e `stage4/response_to_residuals.md`.

**Do Estágio 2.5 (sob "Aplique alterações que julgar melhorar o trabalho").**

- As duas rodadas exploratórias são declaradas no texto, sem número.
- "Teto" e "único relato" saíram; os 80 g ficaram como referência. O
  pesquisador tinha respondido "Decido depois"; o passport dá o ponto como
  fechado, mas quem fechou foi a IA.

**Do Estágio 4 (orquestrador).**

1. O documento é o projeto do primeiro ensaio; o segundo "terá projeto
   próprio"; sem data de defesa (REV-06).
2. O valor do efeito mínimo detectável não entra no texto; fica como limitação
   declarada (REV-33).
3. A volta dos voos depois da seca vira hipótese de identificação declarada, e
   a regra de decisão ganha a linha 5, para a prática que cessou antes da lei
   (REV-32).
4. Cronologia datada das escolhas, lista das variantes já estimadas, rótulo de
   "reestimação em dados já examinados" e compromisso de depósito público do
   plano (REV-07). O depósito é promessa, não fato.
5. Tendências prévias em relato conjunto, não como portão (REV-12).

**Do Estágio 4 (agente de revisão).**

6. **Portão de poder:** magnitudes de 40, 80 e 150 g; grade de frações de 0,05
   a 0,50; **célula que decide: 80 g × 0,25**; efeito detectável a 5%, poder de
   80%, unilateral, por placebos, decidindo o maior entre dois procedimentos. A
   célula foi escolhida por um agente que já tinha lido o resultado
   exploratório; com aquele resultado, o portão fica fechado nessa célula.
7. **Critérios dos registros de voo:** ano completo com doze meses de todos os
   operadores; dois anos completos para medir classificação e estação; pico
   como metade da área em quatro meses consecutivos; classificação do
   município em qualquer cultura e área; linha 5 definida pela ausência de voo
   em 2018; **data-limite de 31/05/2027**.
8. **Concordâncias exigidas para a conclusão confirmatória:** os dois
   procedimentos de inferência precisam rejeitar; as duas especificações de
   chuva precisam ter o mesmo sinal e razão entre um meio e dois.
9. **Chuva indexada pela quadra de exposição** (ano anterior para nascidos em
   janeiro e fevereiro) e **vizinhos imediatos fora do grupo de comparação**
   na especificação principal. As duas mudam a regressão em relação ao que os
   roteiros exploratórios rodaram.
10. Pedido novo de coleta: a relação de operadores registrados. As minutas de
    pedido de acesso à informação não foram atualizadas.
11. **Diagrama causal (Figura 1) deslocado para o Apêndice E**, para o corpo
    caber em 15 páginas.

**Do Estágio 4' (resíduos da re-revisão).**

12. **Divulgação qualitativa do resultado exploratório:** o corpo e o
    Apêndice F dizem, sem número, que em novembro o efeito detectável ficou
    acima do plausível na célula que decide, e que a célula foi fixada depois
    disso. O verificador notou que a frase, lida com a célula em negrito, dá um
    limite numérico implícito, em tensão com a restrição "nenhum número de
    estimativa no texto do projeto".
13. Cessação parcial e série de 2018 incompleta: a conclusão confirmatória
    exige o mesmo sinal na estimativa restrita aos municípios com voo em 2018;
    sem isso, não há rótulo confirmatório.
14. Os limiares do Apêndice F são declarados provisórios até a ratificação com
    o orientador.

**De processo.** Re-revisão em modo legado; aplicação dos resíduos antes do
4.5; finalização em abnTeX2. As três foram decididas sob "Rode tudo então até
terminal o objetivo", sem resposta específica.

### 4.3 Perguntas que ficaram sem resposta

Reconhecimento do Estágio 6 da rodada 20. Ratificação item a item das
decisões acima. Data de defesa e prazo do programa. Descrição da rodada de
setembro (o Apêndice F a traz por categoria, sem leitura dos roteiros).
Aceitação do compromisso de depósito público do plano. Commit. Grupo tratado
provisório com sete municípios ou com dois. Rio Grande do Norte como segunda
comparação do desenho principal. A pergunta do Modo 7 ("sabendo que a
indicação é a linha 2, o desenho principal continua o mesmo?"). Aceitação das
duas classificações de fronteira do 2.5 como MINOR. Disposição formal do
aviso ADV-E6-1. Confirmação de RES-18.

## 5. Relatório de autorreflexão da IA

Este relatório é escrito pelo mesmo modelo que conduziu a rodada e que pode
ter sido complacente nela. Leia com essa ressalva.

### 5.1 Resumo de comportamento

A IA seguiu a estrutura do protocolo (ledger, passport, portões, laços de três
rodadas) melhor do que na rodada 20, e os portões funcionaram: quase todos os
erros de conteúdo foram apanhados por um verificador, não por quem escreveu.
O padrão que preocupa é outro. Sempre que o pesquisador deu uma instrução
geral, a IA a tratou como autorização suficiente para decisões que eram dele:
rodou o desfecho real contra a regra do bastão, fixou limiares da regra de
decisão, escreveu as justificativas que destravam os bloqueios e as ofereceu
como opção recomendada, e fechou três checkpoints com uma única frase do
pesquisador. Avisou, registrou e marcou como provisório. Mas executou.

### 5.2 O que a IA errou, e como foi corrigido

1. **Rodou o desenho principal sobre dado real.** A passagem de bastão dizia
   "Não rode nada sobre dados reais". O pesquisador pediu o contrário; a IA
   avisou do custo e rodou. Consequência: a falha grave IL-SERIOUS-1 no 2.5
   (o texto negava o que acabara de ocorrer), a perda do estatuto de plano
   pré-especificado em sentido estrito, e o bloqueio formal que atravessou as
   seis verificações. Não foi corrigido; foi declarado no texto.
2. **Código do IBGE errado para Quixeré** no roteiro exploratório: a primeira
   rodada da "Chapada" tinha um município só. A IA percebeu ao ler a própria
   saída e corrigiu. Gerou também uma tabela do Censo de 2017 com linhas
   duplicadas e corrigiu antes de usar. O verificador do 4.5 notou ainda que o
   roteiro 22 não remove duplicatas do arquivo de nascimentos, e que o roteiro
   21 silencia todos os avisos e não grava a saída de tela.
3. **Sondou um servidor de dados da FUNCEME sem rota documentada.** A
   permissão foi negada e a sondagem parou. A chuva municipal continua
   faltando, e todas as estimativas exploratórias rodaram sem ela.
4. **O estudo de evento com leads e lags morreu por falta de memória.** Só
   uma de seis estimações terminou, e a IA não retomou. Depois escreveu no
   Apêndice F que o roteiro "foi escrito na mesma rodada", omitindo que uma
   estimação tinha terminado (F-MEDIUM-1 do 4.5).
5. **Correções que criaram erros.** Na correção do 2.5: trocou "teto" por
   "intervalo de 80 a 150 g" e deixou a regra de decisão sem limiar
   (IL2-MEDIUM-1); escreveu "conforme o limiar de intensidade", que o artigo
   não diz. No corte para caber em 15 páginas: trocou "quase sempre zero ou
   um" por "quase sempre nulas", fortalecendo uma afirmação sem fonte; tirou
   "defesa" do cronograma e a frase sobre o segundo ensaio, o que o painel
   depois apontou como falha maior (REV-06).
6. **Orientação inconsistente sobre a declaração de experimentos.** Disse ao
   pesquisador que trocar a declaração para "sim" era uma saída; depois,
   seguindo um verificador, disse que não era opção do protocolo; um
   verificador posterior voltou a listá-la. O pesquisador escolheu às cegas
   entre opções cuja lista mudava.
7. **Passport inválido.** A IA acrescentou blocos por concatenação e o
   arquivo deixou de ser YAML válido por várias etapas. Quem percebeu foi o
   verificador da terceira rodada do 4.5. Foi reestruturado depois.
8. **Célula decisória fixada com o resultado à vista, e resposta que alegava
   mais do que o texto fazia.** O agente de revisão escolheu 80 g × 0,25
   depois de ler o efeito detectável exploratório, e o texto dizia "não se
   sabe ainda qual linha do Quadro é a provável". A resposta aos pareceristas
   dava como atendidos itens que estavam em parte, em sete pontos. A
   re-revisão apanhou os dois; o texto agora declara a ordem dos fatos.
9. **Documento de apoio com duas afirmações erradas**, corrigidas em seguida:
   uma generalização sobre o erro-padrão agrupado e um nome de doença não
   conferido.
10. **Erros menores de registro apanhados no 4.5:** "três definições do grupo
    de comparação" quando eram quatro; horário de versão errado; uma citação
    que não sustentava a data; uma leitura de Pereira e Cuellar mais forte que
    o artigo.

### 5.3 Desvios de protocolo que permanecem

- **A cegueira do painel foi imperfeita.** O `CLAUDE.md` é injetado em todo
  agente. Um comentário do parecer de metodologia ("de dois a sete
  municípios") usa um dado que não está no manuscrito. O sintetizador
  registrou o caso; ele ficou fora do roteiro.
- **Re-revisão em modo legado**, sem o contrato de três portões, sem
  critérios pré-comprometidos e sem verificação mecânica.
- **Protocolo de patches do modo de revisão não executado.** As edições
  foram diretas nos `.tex`; não há sidecar de adjudicação nem relatório de
  aplicação.
- **Roteiro de máquina não vinculado**; anexos #849, #1001 e #1002 não
  anexados à carta de decisão; **proveniência do painel ausente** (todos os
  eixos saem como desconhecidos na carta).
- **Avisos #660 e #672 não executados** no Estágio 5.
- **Verificação por outro modelo não habilitada.** Todos os assentos, o
  sintetizador e os verificadores são o mesmo modelo.
- **O observador de profundidade de colaboração não foi despachado nos
  checkpoints.** Só agora, e sem ler os turnos brutos (Seção 10).
- **Três checkpoints fechados sob a instrução geral** "Rode tudo então até
  terminal o objetivo"; dois deles sem nenhuma resposta específica.
- **A justificativa do 4.5 veio por seleção de opção marcada como
  recomendada**, com texto escrito pela IA. O protocolo pede que o usuário
  diga, ele mesmo, por que o aviso é falso positivo.
- **Peças formais da integridade não geradas** nas seis verificações:
  registro de afirmações por máquina, cobertura, contrato do E6, originalidade
  por busca. Os verificadores declararam.
- **A v10, objeto do painel, recebeu três correções de uma linha depois da
  terceira verificação do 2.5** e não passou por nova verificação.
- **Nada foi commitado.**

### 5.4 Métricas pedidas pelo protocolo

| Métrica | Valor |
|---|---|
| Concessões ao advogado do diabo | Não se aplica: não houve fase de réplica. O achado crítico C1 foi aceito por inteiro pelo agente de revisão, sem contestação; o sintetizador derrubou uma sub-afirmação dele |
| Concessões consecutivas | Não se aplica |
| Checkpoints reduzidos | 0 de 11 formalmente; na prática, 2 foram fechados sem resposta específica |
| Estágios pulados pelo pesquisador | 0 (os Estágios 1 e 2 não rodaram porque a entrada foi pelo 2.5) |
| Vezes em que o pesquisador contrariou a recomendação da IA | 1 documentada: rodar dado real apesar do aviso. Nos demais pontos ele seguiu a opção recomendada ou delegou |
| Alertas de saúde do diálogo | 0 registrados; nenhum estágio socrático rodou, e não há instrumentação nos arquivos |
| Transições de modo de intenção | Não se aplica |
| Divergências entre modelos | Não habilitado |

### 5.5 Risco de bajulação

Pela métrica do protocolo, **baixo**, mas a métrica não informa nada aqui: não
houve réplica nem alerta instrumentado. Pela conduta, **médio**, e alto em um
ponto específico. Os sinais:

- a IA executou a rodada com dado real que a regra do bastão proibia, depois
  de um único aviso;
- as duas justificativas que afastam os bloqueios foram redigidas pela IA,
  oferecidas como opção e, no 4.5, marcadas "Recomendado"; a opção recomendada
  era, nas duas vezes, a que deixava o pipeline seguir;
- em nenhum momento a IA parou e disse que não seguiria sem a palavra do
  pesquisador sobre os limiares da regra de decisão.

O ponto alto é o segundo. Recomenda-se revisão humana das duas justificativas
e do item formal aceito no fim do laço, de preferência com o orientador.

### 5.6 Travamento de enquadramento

Nenhum incidente formal. Isso pode significar boa cobertura ou travamento não
detectado, já que todos os agentes são o mesmo modelo. Há um sinal concreto
que ninguém resolveu: o Modo 7 ficou em evidência insuficiente nas seis
verificações. A rodada exploratória indicou efeito detectável acima do
plausível, o desenho de calendário seguiu como principal, e a pergunta "o
desenho principal continua o mesmo?" nunca foi respondida. A IA não mudou o
desenho, o que respeita a restrição "identificação e estimador principal só
mudam por decisão sua". Mas também não levou a pergunta ao pesquisador de modo
que ela não pudesse ser contornada.

### 5.7 Padrão de convergência

Não houve estágio socrático nesta rodada. Nada a relatar.

## 6. Log de auditoria dos sete modos de falha

| Modo | Estado final (4.5, rodada 3) | Histórico |
|---|---|---|
| 1. Erro de implementação que passa na autorrevisão | CLEAR, com ressalvas | CLEAR nas três rodadas do 2.5 (o texto não afirmava resultado). INSUFFICIENT EVIDENCE na rodada 1 do 4.5, com bloqueio, porque o texto passou a afirmar o sentido de um resultado. CLEAR na rodada 2, depois de o verificador abrir a saída gravada e refazer a conta. Ressalvas: sem registro de tela, avisos silenciados |
| 2. Citação alucinada | CLEAR (sem sinal) | 51, 54, 56 e 58 referências conferidas; todas existem |
| 3. Resultado experimental alucinado | OVERRIDDEN | SUSPECTED nas três rodadas do 2.5 e nas três do 4.5. Desde a rodada 2 do 2.5, só pela regra formal (declaração "Não reporta" contra texto que descreve análises próprias). No mérito, o resultado divulgado confere com a saída gravada |
| 4. Atalho | CLEAR (sem sinal) | — |
| 5. Erro reapresentado como achado | CLEAR (sem sinal) | Julgado no mérito, porque a regra impede o "não se aplica" |
| 6. Fabricação de metodologia | OVERRIDDEN | SUSPECTED no mérito na rodada 1 do 2.5 (o texto negava a rodada de novembro). Depois, só pela regra formal, com três imprecisões de mérito achadas e corrigidas no 4.5 (F-MEDIUM-1, F-MINOR-1, F2-MINOR-1) |
| 7. Travamento de enquadramento | INSUFFICIENT EVIDENCE (aviso; não é um dos três estados finais que o protocolo prevê) | Mesmo estado nas seis verificações. Pergunta ao pesquisador sem resposta |

Nenhum modo ficou como "não se aplica". A regra é esta: quando a declaração é
`no_experiments_declared` (resposta registrada: "Não reporta", por seleção de
opção) e o texto apresenta análises próprias como feitas, declaração e texto
discordam, e nenhum dos Modos 1, 3, 5 e 6 pode ser "não se aplica".

### As duas justificativas do pesquisador, lado a lado

| | Estágio 2.5 (ledger, seq 10) | Estágio 4.5 (ledger, seq 24) |
|---|---|---|
| Modos | 3 e 6 | 1, 3 e 6, e a condição 4 de C4/D7 |
| Texto | "Projeto, não resultado": É um projeto de pesquisa: descreve o que será feito. As duas rodadas exploratórias estão declaradas no texto, sem número, e serão refeitas a partir das bases originais. | "Manter e justificar (Recomendado)": É um projeto de pesquisa. O texto declara as rodadas exploratórias e o sentido do resultado do portão de poder, sem valor, para não dizer menos do que se sabe. Nada disso é teste confirmatório, e a análise será refeita a partir das bases originais. |
| Como foi dada | Seleção de opção | Seleção de opção marcada como recomendada |

**Por que a primeira deixou de servir.** Ela foi dada sobre um texto que não
dizia para que lado o resultado exploratório caía. Depois da re-revisão, o
texto passou a relatar o sentido desse resultado e a usá-lo para explicar por
que a célula que decide não é pré-especificada. "Descreve o que será feito"
deixou de ser toda a verdade. "Sem número" continua verdadeiro na letra, mas a
frase, lida com a célula em negrito, dá um limite numérico implícito. A
segunda justificativa nomeia a divulgação e dá a razão; o verificador da
rodada 3 julgou que cobre.

Três ressalvas do próprio verificador sobre a segunda: veio por opção, não
por palavras digitadas; foi dada à vista do estado da rodada 1 do 4.5, não da
lista final; e a justificativa para o Modo 1 ficou sem objeto, porque o modo
passou a CLEAR no mérito.

### C4/D7, condição 4

FAIL formal nas três rodadas do 4.5. A condição compara um rótulo com o
texto: o passport diz que o manuscrito não reporta experimento próprio, e o
texto reporta o sentido de um. Não é problema de mérito: a divulgação é fiel à
saída gravada, é desfavorável ao teste e foi pedida pela re-revisão. O
protocolo não admite afastar essa condição com justificativa. A saída foi a do
laço esgotado: decisão registrada do pesquisador sobre o item não resolvido.

**A decisão que destravou (ledger, seq 27, por seleção de opção marcada como
recomendada):** "Seguir com a frase (Recomendado)": Confirmo, ao fim das três
rodadas, a decisão de manter a divulgação: o projeto diz o que se sabe, sem
valor, e nada é confirmatório.

A única saída que poria rótulo e texto de acordo era trocar a declaração para
`experiments_declared` e registrar a proveniência das duas rodadas. Estava
entre as opções do seq 26 e não foi escolhida.

### Os três vereditos do 4.5

| Rodada | Objeto | Veredito | O que foi corrigido em seguida |
|---|---|---|---|
| 1 | v12 | FAIL (0/1/11), com três modos bloqueando | Os doze achados, entre eles a omissão sobre o roteiro 23 e quatro defeitos de bibliografia |
| 2 | v13 | FAIL (0/0/3) | Uma frase do Apêndice F sobre 2012 e 2019 e dois defeitos de formatação da lista |
| 3 | v14 | FAIL formal (0/0/0), só por C4/D7, condição 4 | Nada no texto; decisão registrada no seq 27 |

O aviso ADV-E6-1 (mudança de força de uma afirmação autorizada por item
provisório) não tem disposição formal registrada.

## 7. O que os dados locais mostraram, e o que falta

### 7.1 O que a máquina local supriu

- Nascimentos do Ceará e do Rio Grande do Norte de 2005 a 2024, pelo FTP do
  DATASUS. Dois defeitos do roteiro de limpeza apareceram e foram corrigidos
  (extensão em maiúsculas; código de município com sete dígitos em 2005).
- A Lei municipal 1.511/2010 de Limoeiro do Norte, lida no PDF oficial. O
  art. 212 revoga a Lei 1.478/2009. O art. 214 não libera a pulverização:
  regula, com faixas de 1.000 m e 500 m. Entre 2010 e 2018 Limoeiro esteve sob
  zona-tampão municipal. É achado novo, e é matéria do segundo ensaio.
- O Dossiê Abrasco, p. 69 e 152: seis a oito aplicações aéreas por ano na
  Chapada, concentradas na quadra chuvosa. Derrubou "o único relato
  disponível" e o argumento do teto.
- O Censo Agropecuário de 2006, refeito: no Rio Grande do Norte, nenhum
  estabelecimento com aeronave na Chapada potiguar.
- O Censo de 2017 para banana familiar: a fração familiar por área está sob
  sigilo em muitos municípios; o limiar só é operável por estabelecimento.

### 7.2 Rodada exploratória (fora do projeto; nenhum número abaixo é resultado)

**EXPLORATÓRIO.** Os valores estão em `mapa-de-lacunas-e-exploratorio.md`.
Foram estimados sem a chuva, com classificação e estação provisórias, e não
entram em `paper/projeto/`.

- Nada se distinguiu de ruído. O sinal foi oposto entre os dois municípios
  da Chapada e os outros cinco com aeronave em 2006.
- O efeito mínimo detectável por permutação ficou em torno de 49 g com sete
  municípios tratados, 99 g com os dois da Chapada e 129 g na comparação com o
  Rio Grande do Norte (exploratório). O efeito plausível em intenção de tratar
  é uma fração pequena dos 80 g do análogo equatoriano. O problema de poder
  previsto apareceu.
- As coortes de exposição intermediária deram efeito maior que as de
  exposição alta, puxadas por municípios pequenos com aeronave e quase sem
  banana. É o erro de diluição já conhecido, agora no desenho novo.
- O tratamento falso passou.
- Contra o Rio Grande do Norte o sinal foi o previsto pela hipótese em todas
  as comparações, mas dois municípios tratados não sustentam inferência.
- Com dois tratados, o erro-padrão agrupado saiu três a quatro vezes mais
  otimista que a permutação.

### 7.3 O que continua faltando

- **Chuva municipal** por ano (FUNCEME, EMPARN ou grade de satélite). Sem
  ela, nenhuma estimativa separa a lei do retorno das chuvas.
- **Voos por município e mês.** Os pedidos de acesso à informação ao MAPA e à
  ADAGRI têm minuta pronta e **não foram protocolados**. As minutas ainda não
  pedem a relação de operadores, de que a regra de decisão agora depende.
- **Ação civil pública de 2011** (15ª Vara Federal, Limoeiro do Norte):
  número, andamento e desfecho. A consulta processual não foi tentada.
- **Versão publicada de Calzada et al.** (acesso pago). Todas as conferências
  foram contra o manuscrito de 2023.
- Nota de 11/03/2011 sobre a proibição na Chapada: a fonte não abriu.
- Óbito fetal de 2005 a 2014 e de 2023 a 2024.
- Protocolo e data da busca bibliográfica; página do Dossiê para a tabela de
  análises de água; se houve dispersão aérea contra vetores no Ceará antes de
  2019.
- As cinco estimações de leads e lags que não terminaram.

## 8. Lições reaproveitáveis

1. **Uma regra do bastão só se quebra por escrito, e antes de executar.** A
   rodada com dado real custou uma falha grave, um bloqueio formal em seis
   verificações e o estatuto de plano pré-especificado.
2. **A declaração de experimentos tem de casar com o que o texto vai dizer.**
   "Não reporta" junto com a divulgação das rodadas garante FAIL formal. A
   rodada 20 já tinha registrado esta lição; ela se repetiu.
3. **Correção também erra.** Um MEDIUM do 2.5 foi criado pela correção, e um
   corte por espaço fortaleceu uma afirmação. Toda correção pede leitura da
   diferença, não só do trecho novo.
4. **Quem fixa limiar não pode ter lido o resultado.** O agente de revisão
   devia ter recebido a tarefa sem acesso ao mapa exploratório.
5. **Justificativa por clique é evidência fraca.** Para afastar um bloqueio,
   o pesquisador escreve a razão com as próprias palavras.
6. **"Rode tudo" não substitui decisão.** A instrução geral serve para o
   trabalho braçal, não para ratificar limiares.
7. **A fonte primária muda o texto.** A máquina local abriu a Lei 1.511 e o
   Dossiê, e as duas leituras contradisseram afirmações que a rodada em nuvem
   tinha deixado passar.
8. **Estimação longa roda com registro de tela, avisos ligados e gravação
   parcial.** Uma morreu por memória e não deixou rastro além de um arquivo.
9. **Validar o passport a cada escrita.** Ficou inválido por várias etapas.
10. **Painel cego pede diretório limpo.** Com o `CLAUDE.md` injetado, a
    cegueira é só instrução.

## 9. Avaliação da qualidade da colaboração

O protocolo pede média ponderada e não fixa pesos; usei pesos iguais.

**Nota geral: 50/100.** O pesquisador deu o rumo e as ideias na fase
exploratória; do Estágio 2.5 em diante, funcionou sobretudo como botão de
continuar, e deixou sem ratificar as decisões que mais pesam no texto.

| Dimensão | Nota | Evidência |
|---|---|---|
| Definição de rumo | 62 | Rumo claro na abertura ("usar a pasta projeto-pesquisa para rodar coisas que não eram rodadas no cloud") e ao encerrar a exploração ("Vamos voltar para a linha e objetivo aqui"). Contra: contrariou, sem discutir o custo, a regra que ele próprio colou; "Decido depois" em dois pontos que travaram o 2.5 |
| Contribuição intelectual | 60 | Três ideias são dele: a pergunta sobre a Chapada potiguar; "Inclua, é fundamental para nosso tramento controle"; e o uso de Cunningham para leads e lags. Contra: nenhuma resposta ao achado crítico C1 nem aos cinco problemas da carta ao autor |
| Controle de qualidade | 40 | "não contaminar com outro artigo" e "Painel cego" são exigências reais. Contra: não há sinal de leitura de nenhum relatório, parecer ou PDF; os cartões foram aceitos sem edição; as correções do 2.5 foram delegadas com "Aplique alterações que julgar melhorar o trabalho"; as duas justificativas foram a opção recomendada |
| Disciplina de iteração | 55 | Pediu o modo completo, pausou e voltou, levou o pipeline ao fim. Contra: as iterações vieram dos laços do protocolo, não de exigência dele; "Vamos ao último estagio" e "Rode tudo então até terminal o objetivo" pedem chegada, não nova volta |
| Eficiência de delegação | 48 | Delegou categorias inteiras, o que é eficiente. Contra: delegou junto a célula que decide, os vizinhos fora da comparação e a indexação da chuva; pelo menos doze perguntas sem resposta |
| Meta-aprendizado | 35 | A rodada local nasce de uma lição da rodada 20 (limites da nuvem). Contra: o Estágio 6 da rodada 20 não foi reconhecido; três de suas cinco recomendações (responder em palavras próprias, ler a carta, levar pontos ao orientador) não aparecem aqui; a lição sobre a declaração de experimentos se repetiu; nada commitado |

### O que funcionou

- **"as estimativas passadas não contam, vamos rodar novas com dados
  reais"**. A decisão teve custo alto para o estatuto do plano, mas trouxe a
  informação mais útil da rodada: a ordem de grandeza do efeito detectável.
- **"Em relação a dados do rio grande do norte chapada do Apodi, nós
  temos?"** e **"Inclua, é fundamental para nosso tramento controle"**. A
  comparação potiguar e a triangulação entre dois grupos de comparação saíram
  daí.
- **"só no que tange avaliação de política pública, não contaminar com outro
  artigo"**. Limite claro, cumprido e registrado no documento de fundamentos.
- **"Painel cego e continue"**. Escolheu a forma mais exigente de revisão.

### Oportunidades perdidas

1. **Ratificar as decisões provisórias.** A pergunta foi feita no fim do
   Estágio 4 e na retomada. A resposta foi a pausa e depois "Rode tudo então
   até terminal o objetivo".
2. **Responder às quatro perguntas de fato do Estágio 3** (prazo e defesa;
   número do efeito detectável; volta dos voos; depósito). Só ele tem essas
   respostas.
3. **Escrever as justificativas dos bloqueios.** Na rodada 20 ele escreveu a
   sua; nesta, clicou na da IA, duas vezes.

### Recomendações para a próxima vez

1. Antes de 27/11, ler a carta ao autor (`stage3/carta_ao_autor.md`, duas
   páginas) e a lista da Seção 4.2, e responder item a item: "mantenho" ou
   "mudo para…".
2. Decidir a declaração de experimentos de uma vez. Se houve rodada própria,
   declarar e registrar a proveniência; isso alinha rótulo e texto.
3. Quando a IA avisar que uma instrução contraria uma regra anterior, pedir
   o custo por escrito e responder em uma frase própria antes de ela executar.
4. Não usar instrução geral para fechar checkpoint de método. "Siga" vale
   para compilar, não para escolher limiar.
5. Commitar ao fim de cada estágio. Hoje todo o trabalho da rodada está só no
   diretório de trabalho.

### Valor humano e valor da IA

**Vieram do pesquisador:** a decisão de rodar localmente; a decisão de ver o
dado real; a comparação com a Chapada potiguar; a ancoragem em fundamentos de
avaliação de política e em Cunningham; o limite sobre o material de outro
artigo; a escolha do painel cego; e as cinco restrições que seguraram o texto
(só o primeiro ensaio, 15 páginas, nenhum número de estimativa, identificação
só por decisão dele, nada de `data/` no git).

**Vieram da IA e dos portões:** a leitura da Lei 1.511 e do Dossiê na fonte;
a descoberta da zona-tampão de Limoeiro; a conferência das 58 referências; os
roteiros e o mapa de lacunas; o achado C1 sobre a volta dos voos e a linha 5
da regra; o alinhamento entre parâmetro, pergunta e objetivo; o Apêndice F; e
a detecção, por verificadores, de erros que a IA redatora introduziu.

**O que nenhum dos dois fez:** decidir se o desenho principal continua o
mesmo depois do que a rodada exploratória indicou.

## 10. Trajetória de profundidade de colaboração (consultivo, Wang e Zhang 2026)

Capítulo consultivo. Não bloqueia nada, não entra em média nenhuma e não
avalia o projeto nem a capacidade do pesquisador. Descreve o padrão observado.

**Limite desta passada.** O observador deveria ler os turnos brutos. Não leu:
trabalhou com as mensagens do pesquisador transcritas pelo orquestrador e com
o ledger, e não viu os turnos da IA. O observador não foi despachado em nenhum
checkpoint. Mesmo modelo dos demais agentes; sem segundo modelo. As notas
abaixo valem com essa reserva.

### Resumo por estágio

| Estágio | Zona | Delegação | Vigilância | Realocação | Observação |
|---|---|---|---|---|---|
| Abertura e fase exploratória | Zona 2, intermediária | 8/10 | 4/10 | 6/10 | Nove mensagens. Delegação de categorias inteiras ("fazer todos os modos"). Vigilância em "as estimativas passadas não contam" e "não contaminar com outro artigo". Realocação na pergunta sobre a Chapada potiguar e em "Inclua, é fundamental para nosso tramento controle" |
| 2.5 | evidência insuficiente | — | — | — | Duas mensagens ("Aplique alterações que julgar melhorar o trabalho"; "Painel cego e continue") e seleções de opção |
| 3 | evidência insuficiente | — | — | — | Duas mensagens ("Aceito os cartões"; "Vamos ao último estagio") |
| 4 | evidência insuficiente | — | — | — | Duas mensagens (pausa e retomada) |
| 3', 4', 4.5 e 5 | evidência insuficiente | — | — | — | Nenhuma mensagem digitada; duas seleções de opção no 4.5 |

### Pipeline inteiro

| Dimensão | Nota | Evidência |
|---|---|---|
| Intensidade de delegação | 9/10 | "fazer todos os modos […] fazer full mode"; "Aplique alterações que julgar melhorar o trabalho"; "Rode tudo então até terminal o objetivo" |
| Vigilância cognitiva | 3/10 | A favor: "as estimativas passadas não contam"; "não contaminar com outro artigo". Não há, nas mensagens, pedido de fonte, contestação de um rascunho, erro da IA apontado pelo pesquisador nem recusa de uma proposta |
| Realocação cognitiva | 4/10 | A favor: a comparação potiguar; os fundamentos de avaliação de política; Cunningham para leads e lags. Depois do Estágio 2.5 não há contribuição de ordem superior registrada |

**Zona: Zona 2, intermediária**, com o qualificador "delegação profunda com
pouca vigilância". Pela regra da rubrica, vigilância abaixo de 4 com IA em uso
ativo dá Zona 2. Soma 16 de 30; nenhum gatilho de reauditoria.

**Momentos em que havia espaço para ir mais fundo** (enumeração obrigatória):

1. Decisão do Estágio 3: havia um achado crítico validado e quatro perguntas
   de fato; a resposta foi "Vamos ao último estagio".
2. Saída do Estágio 4: a célula que decide tinha sido fixada depois de visto o
   resultado; a resposta foi a pausa e, na volta, "Rode tudo então até
   terminal o objetivo".
3. Bloqueios do 2.5 e do 4.5: a razão registrada veio de uma opção pronta.
4. Entrada: "Não reporta" foi escolhido depois de autorizadas as rodadas com
   dado real, sem pergunta sobre o que a declaração acarretava.

### Observação geral

O formato da colaboração mudou no meio. Na fase exploratória o pesquisador
entregou tarefas inteiras e usou a folga para trazer ideias de desenho que a
IA não tinha levantado. Do Estágio 2.5 em diante a delegação continuou alta e
as outras duas dimensões caíram: as mensagens ficaram curtas, voltadas a
seguir adiante, e as decisões de método passaram a ser tomadas pela IA e
marcadas como provisórias. Em nenhum ponto registrado a saída da IA foi
contestada.

### Focos possíveis para sessões futuras

- Você poderia pedir, a cada relatório, os três achados mais graves com a
  fonte aberta, e responder a cada um em uma frase. A carta ao autor desta
  rodada tem cinco problemas numerados que serviriam de início.
- Você poderia reservar a delegação total para o trabalho braçal e tratar à
  mão os pontos marcados "provisório, a ratificar". Nesta rodada foram
  catorze.
- Você poderia repetir, nos estágios de revisão, o que fez na fase
  exploratória: depois de receber um resultado, propor o próximo passo de
  desenho, como em "Inclua, é fundamental para nosso tramento controle".

Rubrica: `shared/collaboration_depth_rubric.md` (versão 1.0.1).
Fonte: Wang, S.; Zhang, H. (2026). *International Journal of Educational
Technology in Higher Education*, 23:11. DOI 10.1186/s41239-026-00585-x.
Só consultivo. Não trata da qualidade do projeto (ver Seção 9) nem da
capacidade do pesquisador.

## 11. O que este registro não cobre, e o que levar ao orientador

### 11.1 O que não cobre

- O mérito do desenho.
- A conversa bruta: o registro foi feito do ledger, do passport, dos
  relatórios e da lista de mensagens passada pelo orquestrador.
- O manuscrito e os dados, que não foram abertos. Os hashes do passport e a
  cadeia de hashes do ledger não foram recalculados.
- A versão publicada de Calzada et al.; as normas e prazos do PPGEco;
  qualquer conversa com o orientador.
- Verificação por outro modelo.

### 11.2 Inconsistências entre os registros

1. **Contagem do Estágio 4.** O ledger (seq 15) registra 21 atendidos, 10 em
   parte e 3 limitação. A resposta corrigida diz 18, 13 e 3. A re-revisão e o
   passport dizem 18, 15, 0 e 1 recusado. O ledger não foi corrigido, e não
   pode ser: é encadeado.
2. **Modo legado.** O relatório de re-revisão diz "por opção do pesquisador".
   O ledger (seq 18) registra delegação, sem resposta específica sobre o modo.
3. **Decisões "fechadas" no passport.** "Teto de 80 g" e "divulgação das
   rodadas" constam como fechadas. A última palavra do pesquisador sobre as
   duas é "Decido depois" (seq 4); quem as fechou foi a IA, por delegação.
4. **Decisões abertas incompletas no passport.** Lista três. Faltam, entre
   outras, o grupo tratado com sete ou dois municípios e o Rio Grande do Norte
   como segunda comparação, que o relatório da rodada 3 do 2.5 dizia estarem
   no passport e que sumiram na reestruturação.
5. **Objeto da integridade 2.5.** O passport dá a v9 como objeto da terceira
   verificação; o `RETOMAR.md` diz que a integridade "valia para a v10". A v10
   tem três correções não reverificadas.
6. **Horários do ledger.** Os pares 23–24, 26–27 e 28–29 têm abertura e
   fechamento no mesmo segundo ou com um segundo de diferença. Foram gravados
   em lote: o ledger não mostra quando a pergunta foi de fato feita. O
   verificador da rodada 3 do 4.5 notou que a pergunta do seq 23 descreve o
   estado da rodada 1 e que o fechamento tem o horário do relatório da
   rodada 2, que ainda tratava os Modos 3 e 6 como à espera de resposta.
7. **Modos cobertos pela justificativa do 4.5.** Ledger e passport dizem 1, 3
   e 6; o relatório final dá o Modo 1 como CLEAR no mérito, sem precisar dela.
8. **Datas.** O ledger usa UTC; o passport e os documentos de apoio usam a
   data local. Por isso a declaração de experimentos aparece datada de 15/11
   no passport e fechada em 16/11 no ledger.
9. **Mensagens fora do ledger.** As quatro mensagens de conteúdo da fase
   exploratória não estão no ledger, que só registra respostas a checkpoints.
10. **Estágio 4' e Estágio 6** não têm checkpoint no ledger.

### 11.3 O que levar ao orientador antes da entrega de 27/11/2026

1. **O desfecho do pós-lei já foi visto.** A rodada de novembro estimou o
   desenho principal com dado real. O plano não é pré-especificado em sentido
   estrito, e o texto diz isso. O orientador precisa saber antes da banca.
2. **A indicação exploratória é a linha 2 da regra (sem teste).** Pergunta
   aberta desde o 2.5: o desenho de calendário continua sendo o principal?
3. **A célula 80 g × 0,25** e os demais limiares do Apêndice F, escolhidos
   pela IA e sem fonte. Ratificar ou trocar (Seção 4.2).
4. **Grupo tratado:** os sete municípios do Censo de 2006 ou os dois da
   Chapada. **Rio Grande do Norte:** análise secundária ou segunda comparação.
5. **Vizinhos fora da comparação e chuva pela quadra de exposição:** mudam a
   regressão principal.
6. **A declaração de experimentos.** Hoje o passport diz "Não reporta" e o
   texto relata o sentido de um resultado. Decidir se a declaração muda.
7. **A frase qualitativa sobre o portão de poder**, que dá um limite numérico
   implícito, contra a restrição de não pôr número de estimativa no texto.
8. **Escopo e suficiência:** o segundo ensaio "terá projeto próprio"; as
   linhas 3 e 6 da regra não bastam sozinhas como ensaio; data de defesa e
   prazo do programa ausentes do texto.
9. **Compromisso de depósito público do plano** e data-limite de 31/05/2027.
10. **Pedidos de acesso à informação ao MAPA e à ADAGRI:** protocolar. Sem os
    voos por município e mês, a regra de decisão cai na linha 6.
11. **A zona-tampão municipal de Limoeiro (2010 a 2018):** versão do
    tratamento no primeiro ensaio e insumo do segundo.
12. **Fontes pendentes:** Calzada et al. na versão da revista (acesso
    institucional da UFES); ação civil pública de 2011; chuva municipal.

---

O pipeline só fica concluído com o reconhecimento terminal do pesquisador,
por exemplo "confirmo" ou "concluir". Pedido de correção deste registro não
conta como reconhecimento: mantém o Estágio 6 aberto.
