# Framework da dissertação — versão 2 (volta ao básico)

*2026-11-16. Substitui a versão anterior, arquivada em
`docs/arquivo/framework-dissertacao-v1.md`. Este é o documento que manda: o que
estiver em `docs/ars/` e contradisser o que está aqui é histórico. Documentos
antigos que citam "`framework-dissertacao.md` §x" referem-se à versão
arquivada.*

## 0. O que mudou, em cinco linhas

1. **A pergunta volta a ser a do começo:** qual foi o impacto do banimento da
   pulverização aérea sobre saúde ao nascer, saúde da população e economia
   agrícola. Não é mais "qual é a curva dose-resposta".
2. **O tratamento é binário e geográfico:** Chapada do Apodi, lado cearense
   (proibido em 2019) contra lado potiguar (não proibido). O Ceará inteiro
   contra o Rio Grande do Norte inteiro entra como robustez.
3. **O estimador é Callaway & Sant'Anna (2021)**, com uma coorte tratada em
   2019: um estudo de evento com ATT por período. É o DiD da disciplina.
4. **A dose (área de banana) deixa de ser o tratamento** e vira análise de
   heterogeneidade, junto com agricultura familiar × não familiar.
5. **A espinha é a da disciplina de Avaliação de Políticas Públicas:** teoria
   da mudança → resultados potenciais → validade → poder. Uma seção para cada.

### Por que as rodadas anteriores terminavam sempre no mesmo lugar

São dois artigos diferentes, e a confusão entre eles explica a sensação de que
"o Callaway–Sant'Anna é sempre desqualificado":

| | Callaway & Sant'Anna (2021) | Callaway, Goodman-Bacon & Sant'Anna (2024) |
|---|---|---|
| tratamento | binário | contínuo (dose) |
| o que pede | tendências paralelas | tendências paralelas **fortes** para a curva |
| o que aconteceu no projeto | nunca foi o principal | foi o principal, e não se sustentou |

O que não se sustentou foi o segundo, por uma razão de medida e não de método:
a dose era a área de banana do município, e 15 dos 17 municípios de dose alta
não tinham aplicação por aeronave no Censo Agropecuário de 2006. A proxy media
bananicultura, não avião. Cada rodada de revisão tentou salvar a curva
reformulando hipóteses, e o texto foi acumulando ressalvas. O desenho binário
na Chapada não depende dessa proxy: o tratamento é a lei, e a lei tem
fronteira.

Uma correção ao que as rodadas anteriores decidiram: o "gate G1" reprovou o Rio
Grande do Norte porque o lado potiguar tinha pouca aplicação aérea em 2006
(5 estabelecimentos contra 36 no Ceará). Isso não invalida o controle. Num DiD
o grupo de comparação não precisa ter pulverizado; precisa **não ter sido
atingido pela lei** e ter **a mesma tendência** do desfecho. A primeira
condição vale por construção, a segunda se testa no estudo de evento. O G1 muda
a interpretação (§4.4), não a identificação.

---

## 1. Pergunta e plano de avaliação

**Pergunta.** O banimento da pulverização aérea de agrotóxicos no Ceará (Lei
16.820/2019) melhorou a saúde ao nascer nos municípios da Chapada do Apodi, e a
que custo para a produção agrícola?

No formato de plano de avaliação da disciplina (TIP1, s.14):

| pergunta | sub-perguntas | metodologia | indicadores | fonte |
|---|---|---|---|---|
| O ban melhorou a saúde ao nascer? | Peso médio subiu? Baixo peso e prematuridade caíram? Houve mudança em óbito fetal? | DiD com estudo de evento, Chapada CE × RN | peso ao nascer (g); % < 2.500 g; % < 37 semanas; óbitos fetais por mil | SINASC, SIM |
| O ban reduziu agravos agudos? | Intoxicações **não intencionais** por agrotóxico agrícola caíram? Ou subiram, por substituição para aplicação costal? | idem; tentativa de suicídio como placebo | notificações e internações por intoxicação | SINAN/IEXO, SIH |
| O ban custou produção? | Área e produção de banana caíram? Emprego agrícola formal mudou? | idem | área colhida, produção e valor (banana, melão); vínculos na agricultura | PAM, RAIS/CAGED |
| Para quem? | O efeito é maior onde a agricultura é patronal e de exportação? | diferença tripla | os mesmos, por perfil do município | Censo Agro 2017 |

**Desfecho primário: peso ao nascer.** Um só, fixado antes de estimar. Os
demais são secundários e levam correção de multiplicidade (o `09_holm.py` já
existe).

---

## 2. Teoria da mudança

Hipótese causal no gabarito do curso (M03, s.35): *se* a lei proíbe o voo e a
proibição é cumprida, *então* cessa a deriva sobre comunidades e mananciais, o
que reduz a exposição de gestantes, que ao final melhora os desfechos de
nascimento, contribuindo para reduzir a externalidade da fruticultura irrigada
sobre a população do entorno.

| elo | o que é | indicador | premissa (P) e risco (R) |
|---|---|---|---|
| Problema | deriva de fungicidas aplicados por avião sobre bananais atinge casas, escolas e água | amostras de água (Marinho 2010; Milhome 2011); relatos das comunidades | **P: a prática existia às vésperas da lei** (§5.1) |
| Atividade | Lei 16.820/2019, art. 28-B: veda a aplicação aérea; multa | texto legal; autos de infração | P: há fiscalização |
| Produto | deixam de ocorrer voos de aplicação | relatórios mensais ao MAPA (IN 2/2008); SIPEAGRO | R: descumprimento; drones a partir de 2021–2024 |
| Resultado intermediário | menor exposição ambiental de gestantes | não observado diretamente | R: **substituição** por aplicação costal ou tratorizada, com mais calda por hectare e mais trabalhadores expostos |
| Resultado final (saúde) | maior peso ao nascer; menos baixo peso e prematuridade | SINASC | R: seleção para nascimento vivo (se cai o óbito fetal, nascem mais bebês frágeis) |
| Resultado final (economia) | custo de controle da sigatoka sobe; área e produção podem cair | PAM, RAIS | R: realocação da produção para o lado potiguar |

O risco de substituição não é hipotético: produtores da Chapada declararam à
*Globo Rural* (09/04/2021) que passaram de cerca de 25 L/ha de calda por avião
para 250–300 L/ha em aplicação manual, com 12 a 40 trabalhadores no lugar de um
piloto. Isso gera uma previsão testável e de sinal oposto ao do efeito
principal: **a exposição ocupacional pode ter subido** (intoxicações no
SINAN/SIH) enquanto a ambiental caiu (nascimentos). Ver os dois é mais
informativo que ver um.

**Funil de atrito (TdM, s.19–22).** De cada 100 nascimentos nos municípios
tratados, quantos são de mães que moravam perto de um bananal pulverizado por
avião? O dado é municipal e os municípios são grandes; a fração exposta é
pequena. O efeito médio municipal é o efeito sobre as expostas multiplicado por
essa fração. O funil entra direto no cálculo de poder (§6).

---

## 3. Parâmetro

> O grafo causal que sustenta as seções 3 a 5, com os seis caminhos entre a lei
> e o desfecho, o colisor do nascimento vivo e a tradução para o estimador,
> está em **`docs/dag-identificacao.md`**.

Na notação da disciplina (MRP): `Y_i(1)` é o desfecho com o ban, `Y_i(0)` sem
ele. O parâmetro é o **efeito médio sobre os tratados** (EMPT/ATT),

`ATT(t) = E[Y_t(1) − Y_t(0) | município cearense da Chapada]`, para cada ano
`t ≥ 2019`.

É um efeito de **intenção de tratar no nível do município**: o efeito de estar
sob a lei, não o de deixar de ser pulverizado. Declarar isso desde o início
evita a discussão de diluição que consumiu as rodadas anteriores. A conversão
para "efeito sobre o exposto" fica como exercício de calibração, com a fração
exposta declarada como hipótese.

---

## 4. Desenho

### 4.1 Principal: DiD na Chapada do Apodi, CE × RN

- **Tratados:** municípios cearenses da Chapada do Apodi. ⚠️ Russas tem zero
  estabelecimentos com avião no Censo de 2006; o núcleo com medida é Limoeiro e
  Quixeré, e Russas fica na versão ampla até o registro do MAPA dizer
  (`dag-identificacao.md` §0). Texto anterior: núcleo de **Limoeiro
  do Norte, Quixeré e Russas**, que o parecer do Núcleo Tramas/UFC (17/06/2016)
  nomeia como "os principais em que a pulverização aérea ocorre no Ceará", e
  que são os mesmos três de Rigotto et al. (2013). Limoeiro e Quixeré tocam a
  divisa e são os dois do grupo antigo com aeronave no Censo 2006. Versão ampla:
  os municípios cearenses da região (a lista da RIDE do PLP 98/07 tem 9
  cearenses que o repositório ainda não obteve; ⬜ fechar).
- **Controles:** municípios potiguares da Chapada. A delimitação já está no
  código: os 21 da RIDE (`RIDE_CHAPADA_RN`, script 15).
- **Regra:** as duas listas ficam fixadas **antes** de olhar qualquer desfecho
  pós-2019.
- **Unidade e período:** município × ano (mês para o SINASC, agregando quando
  as células forem ralas). Pré: **2010–2018**; pós: 2019–2024, cortado em
  19/12/2024 (Lei 19.135, exceção dos drones). O SINASC consolidado até 2024
  está no FTP do DATASUS para CE e RN.
- **Estimador:** Callaway & Sant'Anna (2021), pacote `did`, uma coorte
  (g = 2019), grupo de comparação "nunca tratado", duplamente robusto com
  covariáveis de 2010 (população, urbanização, cobertura de atenção básica).
  Saída: um `ATT(t)` por ano, com os anos pré como teste de tendência.
  Células ponderadas pelo número de nascimentos: taxa municipal sem peso é
  dominada por município minúsculo (é um dos problemas de Januzzi 2025).
- **Especificação de conferência:** o mesmo estudo de evento por TWFE em
  `pyfixest`. Com uma coorte só os dois coincidem; reportar os dois fecha a
  pergunta antes que a banca a faça.

A fronteira entre linguagens continua sendo arquivo: Python monta o painel,
`Rscript` estima, Python lê o CSV de volta.

### 4.2 Robustez, em três camadas

1. **Estados inteiros.** Todos os municípios do CE (184) contra todos do RN
   (167), mesmo estimador. Muito mais poder, efeito muito mais diluído: serve
   para mostrar que o resultado da Chapada não é artefato de meia dúzia de
   municípios, e para os desfechos econômicos agregados.
2. **Diferença tripla.** (Chapada − resto do estado) no CE contra o mesmo no
   RN: é o que fecha choques estaduais, a única ameaça que o desenho de
   fronteira deixa aberta (`dag-identificacao.md` §5.2). O "resto" são os
   municípios sem aplicação por aeronave em 2006. Variante: CE × pós-2019 ×
   município de fruticultura patronal (§4.3). Remove qualquer choque de 2019 que tenha atingido o Ceará inteiro
   (política estadual de saúde, por exemplo) e não só a fruticultura. Exige
   uma única tendência paralela, a da diferença entre os dois DiDs (Olden &
   Møen 2022).
3. **Controle sintético / SDID** para Limoeiro + Quixeré contra doadores do RN
   e, se preciso, de outros estados (`08_synthdid.R` já existe). É também o
   método da última aula da disciplina.

### 4.3 Heterogeneidade: familiar × não familiar

A lei atinge quem aplica por avião, e quem aplica por avião é a fruticultura
patronal de exportação. A agricultura familiar da mesma região usa agrotóxico,
mas não avião. Daí a previsão: **o efeito deve se concentrar onde a agricultura
não familiar domina**.

- **Medida:** participação da agricultura não familiar no município, pelo
  Censo Agropecuário, que classifica os estabelecimentos pela Lei 11.326.
  Tabelas conferidas na API do IBGE em 2026-11-16, todas com nível municipal:
  **6851** (2017: tipologia × uso de agrotóxico) e **2069** (2006: uso ×
  **tipo de equipamento, com "por aeronave"** × familiar e não familiar). A
  2069 mede diretamente quantos estabelecimentos não familiares usavam avião
  em cada município, antes da lei, da seca e do PL. ✅ Ingestor escrito
  (script 18): em Limoeiro e Quixeré, 22 dos 27 estabelecimentos com avião são
  não familiares; o lado potiguar da Chapada tem zero; Russas tem zero
  (`dag-identificacao.md` §0).
- **Uso:** (i) corte da amostra em dois grupos e ATT em cada um; (ii) a
  diferença tripla de §4.2.
- **Leitura honesta:** é medida municipal, não individual. Diz que o efeito é
  maior em municípios de agricultura patronal, não que mães de famílias
  assalariadas do agronegócio foram mais afetadas.

A dose antiga (área de banana, PAM 2015–2018) entra aqui, como segunda variável
de heterogeneidade, com o estimador contínuo de CGS (2024) relegado a apêndice.
O que já foi estimado não se perde: muda de lugar.

### 4.4 O Rio Grande do Norte é o grupo de controle

O critério é jurídico e não depende de proxy: a proibição da pulverização
aérea aconteceu no Ceará e **não aconteceu no Rio Grande do Norte**. Os
municípios potiguares da Chapada compartilham com os cearenses o clima, o
aquífero, as culturas e parte das empresas, e ficaram sob o regime federal
anterior (IN MAPA 2/2008) durante toda a janela.

Conferido em 2026-11-16 (`docs/leituras-segunda-rodada.md` §2): não há lei
estadual potiguar de proibição; um projeto apresentado em novembro de 2019 não
virou lei; nenhum estado vizinho do Ceará mudou de regime até 2024. Há um
relato de imprensa de aviões operando do lado potiguar até a divisa depois de
2019, o que reforça a sensibilidade sem os municípios de fronteira imediata.

Quanto avião havia do lado potiguar muda a leitura do contraste, não a sua
validade. Se pulverizava e continuou, o DiD compara "parou" com "continuou". Se
quase não pulverizava, compara "parou" com "nunca fez", e o controle informa a
tendência. Nos dois casos o ATT é identificado sob tendências paralelas, que o
estudo de evento com nove anos de pré-período testa. A LAI ao MAPA responde
também a isso, porque o relatório mensal é entregue na superintendência de cada
estado.

---

## 5. Validade

### 5.1 O primeiro estágio: quanto avião havia em 2015–2018

Medir isso **é parte do trabalho, não um obstáculo a ele**. A literatura
acadêmica documenta a pulverização aérea na Chapada de 2000 a 2010 e se cala
depois; o que existe para os anos anteriores à lei são relatos. O projeto
propõe-se a preencher essa lacuna com registro administrativo, por três vias:

| via | o que mede | estado |
|---|---|---|
| LAI ao MAPA: relatórios mensais dos operadores aeroagrícolas (IN 2/2008, Anexo V) | município, cultura, área e mês de cada aplicação aérea, 2008–2018, **nos dois estados** | minuta pronta; ⬜ protocolar |
| LAI à ADAGRI: receituário agronômico (Decreto 4.074/2002, art. 66) | modalidade de aplicação, obrigatória quando aérea | minuta pronta; ⬜ protocolar |
| LAI à SEMACE e registros municipais (câmaras, licenças) | cadastro estadual e normas locais | minuta pronta; varredura das câmaras feita |

Com esses registros o Ensaio 1 passa a ter um **primeiro estágio medido**: a
lei reduziu a área aplicada por avião de X para zero nos municípios tratados, e
o lado potiguar seguiu como estava. Sem eles, o desenho continua válido como
efeito de estar sob a lei; com eles, ganha a medida do que a lei removeu.

⚠️ **Atualizado em 2026-11-16, depois da segunda rodada de leituras**
(`docs/leituras-segunda-rodada.md` §3). Três fontes independentes, entre elas
Raquel Rigotto em outubro de 2016, dizem que a pulverização aérea na Chapada
**parou por volta de 2012, com a seca**. Se for assim, a exposição não muda em
2019, e o contraste que os dados contêm está em 2012. O mesmo desenho de
fronteira serve aos dois casos; o que muda é o início do pré-período:

| cenário | o que a lei fez | o que se estima |
|---|---|---|
| **A.** havia voo em 2015–2018 | removeu exposição em curso | o ATT de 2019, como planejado |
| **B.** o voo parou em 2012 | impediu a retomada quando as chuvas voltaram | **dois contrastes**, com pré-período desde 2005: o de 2012 (fim dos voos no lado cearense, seca comum aos dois lados) e o de 2019 (a lei acrescentou algo?) |

⬜ **Decisão do orientador:** pré-especificar os dois cenários antes de o
registro do MAPA chegar, para a escolha não ser feita depois de ver resultado.

Enquanto os registros não chegam, o que se sabe é isto:

| evidência | fonte | sentido |
|---|---|---|
| Em março de 2011 a Comissão Nacional de Combate à Violência no Campo anunciou a proibição na Chapada; em julho de 2011 MPF, MPT e MPCE pediram a proibição à Justiça Federal | SDH via SINAIT (15/03/2011); MPT-CE (07/07/2011) | a prática pode ter parado. ⬜ desfecho da ação desconhecido |
| "A partir de 2012 não houve novas aplicações [na comunidade do Tomé] devido à baixa intensidade das chuvas" | moradora, Agência Brasil (16/07/2016) | a seca de 2012–2017 reduziu a sigatoka e, com ela, os voos |
| Produtor com 300 ha na Chapada descreve a troca do avião pela aplicação manual e diz que a pulverização "é necessária apenas quando chove", sem datar o último voo. (O "até 2018 fazia duas aplicações aéreas anuais" da mesma matéria é de um produtor do **Cariri**, não da Chapada: corrigido em 2026-11-16) | Globo Rural (09/04/2021) | compatível com os dois cenários |
| "Atualmente, a pulverização aérea não tem acontecido na região em função da seca" | Raquel Rigotto, entrevista ao IHU, 06/10/2016 | **a favor do cenário B**, e vem de quem mais estudou a região |
| Em 2009, contrato de 1.000 ha (820 de duas empresas, 180 de vinte parceiros); primeira aplicação do ano em 637 ha, 29 voos em cinco dias | Marinho, Carneiro & Almeida (2011), p. 171–173, com planilha da empresa | a medida observada da área; os "4 milhões de litros" são teto calculado |
| Limoeiro, Quixeré e Russas são "os principais em que a pulverização aérea **ocorre** no Ceará" (presente, em junho de 2016) | parecer do Núcleo Tramas/UFC à Assembleia, 17/06/2016, lido na íntegra | a prática existia em 2016, e é localizada nesses três municípios |
| Dos 43.900 ha de banana do Ceará, cerca de **1.000 ha (2,27%)** "tiveram pulverização aérea entre 2003 e 2015" | nota técnica de F. Zuza de Oliveira (2016), do lado dos produtores, citada no mesmo parecer | a prática existia até 2015, e é **pequena e concentrada** |
| Uma mãe que trabalhava a ~100 m do campo de pouso presenciou "muitos episódios" entre 2010 e 2014; outra morava a ~50 m de bananal pulverizado por avião em 2014 | Aguiar (2017), p. 108–109 e 119 | a prática sobreviveu a 2011 |
| Em julho de 2017, uma moradora diz que as empresas pulverizavam por avião "até alguns anos atrás" | Aguiar (2017), p. 115 | no entorno dela, tinha parado antes de 2017 |
| A lei foi aprovada em 2018 contra uma prática descrita como corrente, e o setor foi ao STF (ADI 6137) para derrubá-la | autos | ninguém litiga por algo que não usa |

O número dos 1.000 ha explica, sozinho, por que a dose estadual falhou: 97,7%
da banana cearense nunca viu avião, e a área de banana do município não tinha
como medir o tratamento. E justifica o desenho novo: o tratamento está em três
municípios, na Chapada.

A linha do tempo completa, com a fonte e o tipo de cada evidência, está em
`docs/literatura-brasil-agrotoxicos.md` §4.1. A literatura acadêmica documenta
2000–2010 e se cala sobre 2012–2018.

Leitura provisória: o peso da evidência passou para o cenário B. A prática
está documentada com medida até 2009–2010, tem testemunho até 2014, e as duas
fontes mais próximas do campo (uma moradora e a pesquisadora que coordenou o
estudo epidemiológico) dizem em 2016 que os voos tinham parado com a seca. A
aplicação é sazonal, na quadra chuvosa de fevereiro a maio, e não houve quadra
chuvosa normal entre 2012 e 2017. Isso não derruba o desenho de fronteira;
desloca o contraste informativo de 2019 para 2012.

O que fecha a questão é o relatório mensal que todo operador aeroagrícola
entrega ao MAPA (IN 2/2008, Anexo V: município, cultura, área, mês). O pedido
de LAI está minutado em `docs/legislacao/lai-mapa-relatorios-mensais-minuta.md`
e **é o item de maior retorno do projeto inteiro**. Protocolar esta semana.

### 5.2 Ameaças à validade interna

No vocabulário da disciplina (IC, s.6: o grupo de comparação precisa ter a
mesma tendência, não ser afetado pelo tratamento e reagir igual):

| ameaça | o que é aqui | resposta |
|---|---|---|
| Tendências não paralelas | CE e RN divergindo por razões alheias à lei | estudo de evento 2010–2018; HonestDiD (`07_honestdid.R`) para dizer quanto de violação o resultado aguenta |
| Tratamento composto | outra política cearense de 2019 em diante (saúde materna, por exemplo) | diferença tripla (§4.2) |
| Contaminação do controle (SUTVA) | deriva e água cruzam a divisa (o parecer do Tramas cita Chaim/Embrapa 2004: deriva de até 32 km; o Aquífero Jandaíra é comum aos dois estados); produção pode migrar para o RN | usar município de **residência** da mãe; testar PAM do lado potiguar; excluir municípios colados à divisa como sensibilidade. O viés vai contra achar efeito |
| Antecipação | PL apresentado em 02/2015, aprovado em 12/2018 | pré-período começando em 2010; reportar o ATT com e sem 2015–2018 na base |
| Choque simultâneo | fim da seca (2018) e pandemia (2020–21) | atingem os dois lados da Chapada, que têm o mesmo clima: é o argumento a favor do desenho de fronteira |
| Drones | Lei 19.135/2024 no CE; uso no RN desde ~2021 | corte em 19/12/2024; sensibilidade com pós até 2021 |
| Seleção para nascimento vivo | menos óbito fetal → mais nascidos frágeis | óbito fetal (SIM) como desfecho próprio |
| Regime de notificação | o SINAN mede notificação, e notificar depende de vigilância e hospital (Rodrigues 2022: os municípios que notificam quase triplicam entre 2006 e 2017) | conferir no CNES se unidades de vigilância e hospitais evoluem igual nos dois lados; usar o SIH como segunda medida; não usar óbito por intoxicação, que não tem casos |
| Controles que respondem ao tratamento | pré-natal e parto hospitalar podem mudar com a lei | covariáveis só de linha de base (2010); das características maternas, gemelaridade e idade |

### 5.3 Validade externa

O resultado vale para um ban de método em fruticultura irrigada de exportação,
com fungicida em banana. Não se transporta para soja e glifosato, e o texto
deve dizer isso em vez de se apoiar em Dias, Rocha & Soares como se o químico
fosse o mesmo. O análogo é Calzada, Gisbert & Moscoso (2023).

---

## 6. Poder

O gargalo é o número de municípios tratados, não o de nascimentos.

- **Antes de estimar:** rodar `make mde-desenhos` e `make mde-calendario` (script 13, desenho
  `chapada2_vs_ride_rn` e a versão ampla). Ele usa só o pré-período e devolve o
  efeito mínimo detectável. Estender o pré para 2010–2018 reduz o MDE.
- **Tamanho da exposição:** cerca de 1.000 ha pulverizados (§5.1) em três
  municípios que somavam ~160 mil habitantes (parecer do Tramas). A fração de
  gestantes expostas é pequena, e o cálculo de poder tem de partir daí.
- **Efeito de referência**, agora pela leitura integral: Calzada et al. acham
  **−80 g (EP 30,8)** para quem mora a até **150 m** do bananal e atravessa a
  estação de fumigação intensa (Tab. 3, col. 2). O "150 g" do resumo é soma de
  dois trimestres, não intervalo. Além de 150 m o efeito some.
- **Efeito municipal esperado:** com a densidade equatoriana transposta a 1.000
  ha, a fração exposta fica perto de 1,4%, e o efeito sobre o peso médio
  municipal, perto de **1 a 2 gramas**; sobre baixo peso, 0,04 p.p. Com três
  municípios tratados isso não é detectável. A conta e as premissas estão em
  `docs/leituras-segunda-rodada.md` §4.3; ⬜ substituir a premissa pela medida,
  cruzando setores censitários de 2022 com a área de banana.
- **O que fazer com isso.** (i) Concentrar o sinal: diferença tripla com a
  coorte cujo 1º e 2º trimestre caem na quadra chuvosa (fev–mai), que é quando
  se pulveriza; `14_mde_calendario.py` já calcula o poder. (ii) Acrescentar
  desfechos que não são peso médio: duração da gestação, óbito fetal e razão de
  sexos ao nascer. (iii) Reportar intervalo e dizer o que ele exclui.
- **Inferência:** com dois a nove tratados, erro-padrão agrupado convencional
  não serve. Usar Conley & Taber (2011) e Ferman & Pinto (2019), mais
  inferência por permutação entre municípios do controle (placebo no espaço),
  apresentada como permutação e não como "exata".
- **Regra de leitura, fixada agora:** o intervalo de confiança decide. O MDE é
  de planejamento e não rebaixa depois um intervalo que exclui o zero.

---

## 7. Literatura: quatro blocos

Estado de verificação: ✅ conferido em fonte primária ou registro (DOI);
🔎 localizado por busca, falta ler; ⬜ a conferir.

**A. A Chapada do Apodi: o dano documentado (o que faltava no texto).**
É a base da seção de *background* e do "problema" na teoria da mudança.

- ✅ Rigotto, Silva, Ferreira, Rosa & Aguiar (2013), *Rev. Bras. Epidemiol.*
  16(3):763–773, `10.1590/S1415-790X2013000300019`. Limoeiro, Quixeré e Russas
  contra municípios de agricultura familiar, 2000–2010: internação por
  neoplasia 1,76 vez maior e óbito por neoplasia 1,38 vez maior; **sem
  diferença** em óbito fetal e malformação. É o antecedente direto da
  comparação patronal × familiar, sem identificação causal.
- ◐ Rigotto (org.) (2011), *Agrotóxicos, trabalho e saúde*, Edições UFC,
  612 p. Lidos o cap. 17 (Teixeira, p. 524–545: a pulverização aérea e a lei
  municipal) e o cap. 5 (Marinho, Carneiro & Almeida: o contrato de 1.000 ha e
  o cronograma de voos de 2009).
- ✅ Cavalcante (2022), nota técnica UFRN/SEMIAR sobre produção e exportação de
  banana depois da lei. Antes e depois, sem grupo de comparação; os dados
  conferem com a PAM. Ficha em `docs/leituras-segunda-rodada.md` §5.
- 🔎 Marinho (2010), dissertação UFC, e Marinho, Carneiro & Almeida (2011):
  volume de calda e ingredientes ativos da pulverização aérea na banana. Citado
  no acórdão da ADI 6137.
- 🔎 Milhome (2011), tese UFC, e trabalho no 26º Congresso da ABES:
  propiconazol e difenoconazol em águas superficiais e subterrâneas do
  perímetro Jaguaribe–Apodi.
- 🔎 Aguiar (2017), dissertação UFC: malformações congênitas e puberdade
  precoce na comunidade do Tomé.
- 🔎 Carneiro et al. (org.) (2015), *Dossiê Abrasco*.
- ✅ Rocha & Rigotto (2017), já no `.bib`.
- ✅ Diógenes & Rigotto (2016), parecer técnico do Núcleo Tramas/UFC sobre o PL
  18/2015, 17/06/2016 (Drive, lido na íntegra). Fonte das linhas novas da
  §5.1; dele saem ainda, a localizar: 🔎 Gama, Oliveira & Cavalcante (2013),
  *Química Nova* 36(3):462–467 (inventário de agrotóxicos e risco hídrico no
  Baixo Jaguaribe); 🔎 COGERH (2011), águas subterrâneas da Bacia Potiguar
  (difenoconazol no Aquífero Jandaíra, Quixeré); 🔎 Ferreira Filho (2013),
  dissertação UFC (alterações citogenômicas em trabalhadores da banana);
  ⬜ a nota técnica de Zuza de Oliveira (2016), que é a fonte primária dos
  1.000 ha.
- ◐ Aguiar (2017), lida em boa parte: estudo de casos na comunidade do Tomé,
  8 famílias; fonte dos testemunhos de 2010–2014 da §5.1.
- ◐ Reges (2023), tese de doutorado em História, UFC: a construção do mártir
  Zé Maria do Tomé. Contexto para o *background*; não citar datas e números de
  lei por ela (tem inconsistências internas).
- 🔎 Olivete, Thomaz Junior & Barreto (2025), *Caderno Prudentino de Geografia*
  47(1):226–246, ✅ lido: panorama das leis e projetos de proibição. Não
  menciona o Rio Grande do Norte. ⬜ Conferir na Assembleia do RN se houve
  projeto ou restrição no período.
- 🔎 Siqueira et al. (2010), *Bull. Environ. Contam. Toxicol.* 84:647–651,
  `10.1007/s00128-010-0027-8`: estudo ecológico nacional, uso de agrotóxico e
  prematuridade, baixo peso e malformação. Antecedente descritivo.

**B. Agrotóxico e nascimento, com identificação causal.**

- ✅ Calzada, Gisbert & Moscoso (2023), *JAERE* 10(6), `10.1086/725349`: o
  análogo (avião, banana, fungicida, peso ao nascer). Lido na íntegra o
  manuscrito aceito; ficha em `docs/leituras-segunda-rodada.md` §4.
- ✅ Dias, Rocha & Soares (2023), *REStud* 90(6), `10.1093/restud/rdad011`.
- ✅ Camacho & Mejía (2017), *J. Health Econ.*; Larsen, Gaines & Deschênes
  (2017), *Nat. Commun.*; Reynier & Rubin (2025), *PNAS*.
- 🔎 Skidmore, Sims & Gibbs (2023), *PNAS*, `10.1073/pnas.2306003120`: soja e
  câncer infantil no Brasil.
- ◐ Jones (2020), *Land Economics* 96(2), `10.3368/le.96.2.149`: lidos só o
  resumo e os apêndices. **Não isola fungicida** (mesmo instrumento para
  inseticida e fungicida). Citar como contexto.
- **Viçosa (UFV, PPGEA)**, lidos na íntegra: ✅ Rodrigues (2022), tese,
  `10.47328/ufvbbt.2022.752` (intoxicação aguda e produtividade do agrotóxico);
  ✅ Januzzi (2025), dissertação, `10.47328/ufvbbt.2025.749` (nascimentos e
  saúde infantil; **nulo** com efeitos fixos de município e ano, nas duas
  versões: o "+1,2, p < 0,10" do congresso é a coluna sem efeito de ano);
  ✅ Rodrigues, Fortini & Neves (2023), `10.1007/s13762-022-04032-y`;
  🔎 Rodrigues & Féres (2022), *RESR*, `10.1590/1806-9479.2021.244491`. O que o
  grupo dá ao projeto: a evidência nacional de média, com proxies que não
  enxergam banana nem método de aplicação, e nenhuma avaliação de política. A
  leitura completa, com as referências deles triadas pelo desenho, está em
  **`docs/literatura-brasil-agrotoxicos.md`**.

**C. Método.**

- ✅ Callaway & Sant'Anna (2021); Sant'Anna & Zhao (2020); Roth et al. (2023);
  Rambachan & Roth (2023); Conley & Taber (2011); Arkhangelsky et al. (2021):
  todos no `.bib`.
- 🔎 Ferman & Pinto (2019), *REStat*; Olden & Møen (2022), *Econometrics J.*
- Da disciplina: Gertler et al., *Avaliação de impacto na prática*; e
  ⬜ Bucher & Seixas (2026), *Ecological Economics* 242,
  `10.1016/j.ecolecon.2025.108884`: DiD do orientador sobre o Reflorestar, que
  é o molde de idioma para a seção empírica. DOI transcrito do slide, a
  conferir.

- Molde de redação em português, na *RESR* (Drive): 🔎 Lima et al. (2025),
  `10.1590/1806-9479.2025.287073` (TWFE com tratamento contínuo, Matopiba), e
  🔎 Daniel et al., soja e finanças municipais com DiD escalonado. Mostram como
  a revista de economia rural brasileira apresenta um DiD.

**D. Ensaio 2** (custo-benefício e escolha de instrumento). À lista anterior
somam-se três textos que estão no Drive e servem ao lado do custo:
✅ Lichtenberg, Parker & Zilberman (1988), já no `.bib`; 🔎 Soares & Porto
(2009), *Ecological Economics* 68:2721–2728 (custo social da intoxicação aguda,
Paraná: o molde brasileiro de valoração); 🔎 Cunha & Soares (2020), *Cad. Saúde
Pública* 36(10), `10.1590/0102-311X00225919` (desoneração fiscal de R$ 9,8
bilhões em 2017: o instrumento-preço operando ao contrário). Ver §8.

---

## 8. O que isto faz com o Ensaio 2

O Ensaio 2 dependia da curvatura da dose-resposta para aplicar Weitzman, e o
parecer de 22/09 já havia mostrado que essa ponte não se sustentava. Com o
Ensaio 1 binário, o Ensaio 2 fica mais simples e mais defensável:

- **Custo-benefício do ban** (TIP1, s.22–23): benefício em saúde (ATT sobre
  peso ao nascer, valorado pela literatura de retornos ao peso ao nascer) contra
  custo em produção (ATT sobre área, produção e emprego). Os dois números saem
  do mesmo desenho.
- **Comparação de instrumentos** como discussão qualitativa informada por esses
  dois números e pelo achado de substituição (§2): proibir o método não proíbe
  a molécula, e uma zona-tampão ou uma taxa teriam efeitos diferentes sobre a
  exposição ocupacional.

Weitzman continua como referencial teórico, não como exercício de calibração.
**Decisão do orientador.**

O plano completo está em **`docs/ensaio2-custo-beneficio.md`**: a estrutura de
benefícios e custos, os preços disponíveis na literatura brasileira (Soares &
Porto 2009, 2012), os fatos que informam a escolha de instrumento (a
desoneração de R$ 9,8 bilhões de Cunha & Soares 2020; a receita marginal de
R$ 1,35 no Nordeste de Rodrigues 2022) e a tabela do que o ensaio conclui em
cada cenário de resultado do Ensaio 1, escrita antes de estimar.

---

## 9. O que se aproveita do repositório

| destino | o quê |
|---|---|
| **Fica, sem mudança** | pipeline de dados (scripts `data_prep/01–04`, `10`, `11`, `15`, `16`); transporte FTP do DATASUS multi-UF; `docs/legislacao/` inteiro; `referencias.bib` |
| **Fica, com novo papel** | `13_mde_desenhos.py` (vira o cálculo de poder do desenho principal); `08_synthdid.R` (robustez 3); `07_honestdid.R`, `06_pretrends.R`, `09_holm.py`; `04_robustness.py` (inferência com poucos tratados) |
| **Vai para apêndice** | `03_contdid.R`, `10_spt_pretrend.py`, `12_erro_de_classificacao.py`, GAEZ (`06_build_gaez.py`): a dose como heterogeneidade |
| **Sai do texto** | `11_weitzman_inversao.py`; canal-água (SISAGUA segue suspenso); vento |
| **A escrever** | `scripts/estimate/01_did_chapada.R` (CS 2021, uma coorte) e o espelho TWFE em Python; ingestor do Censo Agro 2017 (familiar × não familiar); ingestor RAIS/CAGED; alvo `make chapada` no Makefile |
| **Histórico** | `docs/ars/01–19`: registro do caminho. Não orientam mais o texto, e três achados deles seguem valendo: Limoeiro não estava sob ban municipal em 2015–2018; o FTP tem SINASC até 2024; o químico é fungicida, não glifosato |

O `paper/secoes/04-identificacao.tex` e o `06-diagnostico-poder.tex` precisam
ser reescritos a partir deste documento. As seções 01–03 e 05 se aproveitam
com cortes.

---

## 10. Próximos passos, em ordem

1. **Protocolar a LAI ao MAPA** (relatórios mensais 2008–2018, CE e RN). Fecha
   a §5.1 e, de quebra, mede a aplicação aérea do lado potiguar.
2. **Fixar as duas listas de municípios** (tratados e controles da Chapada) e
   registrar em `docs/pre-especificacao.md`, antes de qualquer desfecho pós.
3. **Montar o painel CE + RN, 2010–2024** (`make fronteira VIZINHO=24` com a
   janela estendida) e rodar `make mde-desenhos`. Só pré-período.
4. **Levar ao orientador** três decisões: (a) o desenho deste documento como
   principal; (b) pré-período a partir de 2010; (c) o Ensaio 2 como
   custo-benefício (§8).
5. **Estimar**, nesta ordem: estudo de evento do peso ao nascer na Chapada →
   estados inteiros → diferença tripla → desfechos secundários e econômicos.
6. **Reescrever** `04-identificacao.tex` seguindo as seções 2 a 6 daqui.

Nada foi estimado para este documento. `data/` está vazio nesta sessão; os
números citados vêm de documentos anteriores do repositório ou das fontes
indicadas.
