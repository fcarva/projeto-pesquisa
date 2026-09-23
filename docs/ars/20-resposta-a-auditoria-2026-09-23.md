# 20 — Resposta à auditoria de 2026-09-23: o que os números reais dizem

*2026-09-23. Resposta à auditoria externa arquivada em
`docs/revisao/auditoria-2026-09-23/` (sete relatórios, com resultados reproduzidos
nos painéis do pesquisador). Fecha a Fase 3 do ARS da rodada 18 (doc 19 §6): a
condição 1 foi cumprida pela auditoria, que rodou os scripts 13 e 14 no painel
real. Convenção das fontes: **[código]** conferido nesta sessão no código ou nos
dados arquivados; **[aud.]** lido pela auditoria e não relido aqui, porque o proxy
da sessão bloqueia o domínio; **[índice]** trecho de buscador.*

---

## 0. Em uma página

| bloco | veredito | o que mudou |
|---|---|---|
| Reprodução | ✔ o −36,19 g reproduz, com EP 15,47 e IC [−66,51; −5,87] | os números que o doc 14 §3-ter pedia existem agora (§1) |
| Código | ✔ **os 20 achados foram conferidos, e 18 procedem por inteiro**. Os dois restantes, dezembro de 2024 e a proveniência, não afetam o painel atual | 17 arquivos de código alterados, 20 testes novos, 294 passam (§2) |
| Identificação e inferência | ✔ procede | o texto do paper e dos docs 03, 16 e 17 tem afirmações erradas, listadas na §3; textos propostos na §7 |
| Fontes primárias | ✔ procede, e com dados novos | revogação de Limoeiro por **artigo** identificado; lei municipal de 2018 que **regulava** a pulverização aérea; relato de aviões em Tomé em 2018 (§4) |
| Teoria e custos | ✔ procede | a leitura da Conab perdia 72 dos 88 custos de avião; a conclusão "tecnologias mutuamente exclusivas" saiu (§5) |

**O que mais importa, em quatro frases.**

1. **Os placebos pré-ban usavam o pós-ban**, e o erro era meu (script 10). Com a
   janela corrigida, o nível placebo muda de sinal: sai de −8 a −13 g e vai para
   +18 a +28 g.
2. **O −36 g sobrevive à inferência com 14 controles** (p de 0,02 a 0,04 nos
   quatro procedimentos). Mas a diferença entre produtores e não produtores já
   se moveu **+21 g dentro do pré-período**, o sinal é o contrário do previsto e
   a dose não tem gradiente. O parágrafo do paper que o chama de "compatível com
   efeito nulo" está errado (o IC exclui o zero). E a leitura como efeito da
   retirada da pulverização continua sem sustentação.
3. **O desenho de calendário (R3) foi calculado e não tem poder**: com 7
   tratados contra 177 do Ceará, o efeito sobre o bebê exposto teria de ser de
   **165 g com metade dos nascimentos expostos**. O gargalo é a fração exposta
   dentro do município, e o SINASC municipal não a mede.
4. **O nó de 2011 afrouxou**: há relato contemporâneo de aviões em Tomé em 2018.
   Surgiu também uma rota de registro que o projeto não tinha: os **avisos
   prévios de pulverização aérea** que as leis ambientais de Limoeiro (2010 e
   2018) exigiam dos operadores.

---

## 1. Os números reais

Painel `painel_ensaio1.parquet`: 17.664 células, 184 municípios, 96 meses
(2015–2022), 1.001.709 nascimentos, 10 células sem peso. A definição 4 tira do
zero um único município, o 230523 (aptidão 0,5406, acima do p75 de 0,4825).
Ficam 14 controles. [aud.; tabelas em `resultados/`]

### 1.1 O nível, com a inferência que respeita os controles

| construção | tratados × controles | nível | IC 95% (t de Welch) | p Welch-t | p wild | p permutação | jackknife dos controles |
|---|---|---|---|---|---|---|---|
| área zero (def. 1) | 169 × 15 | −35,33 g | [−65,95; −4,71] | 0,026 | 0,023 | 0,024 | [−41,7; −28,9] |
| **área zero + GAEZ (def. 4)** | **169 × 14** | **−36,19 g** | **[−69,15; −3,23]** | **0,034** | **0,038** | **0,034** | **[−43,1; −29,3]** |

A decomposição é o que decide a leitura: **−36,19 = −16,74 (169 produtores) −
19,46 (14 controles)**. **95% da variância** de Welch vem da média dos controles.
Com 14 controles, a t tem 14,4 graus de liberdade, e a cauda normal que o
`p_welch` usava era otimista (0,019 contra 0,034). Holm sobre os dois desfechos
(peso e fetal), bilateral: **0,067**. Unilateral na direção prevista (o ban
aumenta o peso): **1**. [aud.; o IC e o p da t de Welch conferidos aqui a
partir do EP e dos graus de liberdade, com a função nova do `04_robustness.py`]

### 1.2 Placebo, perfil e janelas: por que o número não é o ban

| diagnóstico | resultado | leitura |
|---|---|---|
| **nível placebo, janela corrigida** (def. 4) | **+20,1; +28,1; +21,6 g** (p de Welch 0,39; 0,17; 0,37) | quando não existe ban nenhum, a mesma comparação se move 20–28 g, e para o outro lado |
| mesma conta, 2017–18 menos 2015–16 | **+21,3 g** (tratados +2,8; controles −18,4) | os controles caíram 18 g dentro do pré-período |
| nível contra cada metade do pré | **−25,6 g** contra 2015–16; **−46,8 g** contra 2017–18 | o tamanho depende de qual pré se usa. Aritmética dos contrastes da auditoria, supondo meses iguais por metade |
| terços da dose positiva | −18,5; −21,1; −10,7 g (controles +18,6) | sem gradiente: o número é produtor × não produtor, não dose |
| sem 2020–2021 | −36,13 g, IC [−83,9; +11,6] | o ponto não é a pandemia; a precisão, sim. Os componentes mudam inteiros (tratados −38,1; controles −2,0) |
| pós desde jan/2019 | −33,72 g | a exclusão das coortes de transição mexe pouco |
| média por bebê dentro do município | −36,55 g | a ponderação mensal também |
| event study, lead e = −1 (dez/2018) | **+100,8 g**, banda [+5,4; +196,3] | a série mensal da diferença é volátil; 48 lags saem NA (limitação do pacote) |
| inclinação placebo, **óbito fetal**, janela corrigida (def. 1) | +0,0033; +0,0037; +0,0018, contra −0,0024 no desenho real | **dois dos três placebos passam o real em módulo**: a "assimetria entre os desfechos" que o paper lê na §6.4 vinha do pós-ban dentro do placebo |

**Leitura.** O −36 g é uma diferença reproduzível e estatisticamente distinta de
zero entre os 169 municípios com banana e os 14 sem. Ela tem o tamanho do
movimento da mesma diferença no pré-período, sinal contrário ao previsto e
nenhuma relação com a dose. E, pela calibração de 2006 (VPP 7/169), o sinal
diluído de um benefício de 150 g seria de uns 6 g. As quatro explicações do doc
17 §1.3 continuam de pé, mas agora com peso diferente. A diferença de trajetórias
na margem extensiva, que era hipótese, tem evidência direta nos placebos. A de
ruído com poucos controles também tem (p ≈ 0,03, com três placebos de 20–28 g).

### 1.3 As especificações binárias (17 × 14)

| estimador | estimativa | IC gravado |
|---|---|---|
| Synthetic DiD | −20,16 g | [−56,43; +16,10] |
| Controle sintético | −34,64 g | **[−67,43; −1,85]** |
| DiD simples | −21,85 g | [−59,54; +15,84] |
| HonestDiD (Mbar = 0) | — | [−72,47; +24,49] |

O controle sintético exclui o zero com o EP jackknife, e o paper já o registra
(§6.6). O que muda é outra coisa: os três incluíam 2019 inteiro no pós, e o
contdid exclui jan–set/2019. Foi corrigido na §2, e esses números vão mudar na
próxima rodada.

### 1.4 As curvas e o fetal

- **Nível por dose:** a banda do pacote exclui o zero em 133 dos 169 pontos.
  ⚠️ **Não vale.** Conferi no código fixado (contdid `5cfec81`, `R/cont_did.R`,
  l. 195–221): a curva é centrada na média dos controles (`m0`), o `npiv` roda só
  nos tratados e o EP é o dele. A incerteza de `m0` fica de fora, e o EP de `m0`
  é de ~15 g (95% dos 15,41² da variância de Welch). Com o valor crítico de
  4,38, a meia-largura mínima passa a 4,38 × 15 ≈ 66 g, e a maior estimativa em
  módulo é 59,1 g: **nenhum ponto exclui o zero**. O `03_contdid.R` agora grava a
  banda com esse termo (§2, item 13), e a próxima rodada confirma. [código]
- **Derivada:** nenhum ponto exclui o zero, e o agregado (−2.946,76) não é
  interpretável (média simples de uma derivada não linear).
- **Fetal:** +0,000176, IC do pacote [−0,0039; +0,0042]. Os pontos e EP das
  curvas reproduzem, mas os valores críticos não (6,79 → 6,28), e sem o manifesto
  da chamada antiga não se sabe por quê. A inferência histórica do fetal não está
  reproduzida.

### 1.5 O que o poder de cada desenho custa, calculado

MDE com 80% de poder, só o pré-período, σ e τ calibrados **no Ceará**.

| contraste | g₁ × g₀ | MDE agrupado | MDE por unidade | o que é |
|---|---|---|---|---|
| decil × resto do CE | 17 × 167 | 33,8 g | 30,5 g | o benchmark dos "33,4 g" — **não é contraste estimado** |
| decil × zero GAEZ | 17 × 14 | **55,0 g** | **52,3 g** | o que SDID/HonestDiD estimam |
| produtores × zero GAEZ | 169 × 14 | 37,1 g | 44,9 g | o agregado principal |
| aeronave 2006 × resto do CE | 7 × 177 | 51,2 g | 43,5 g | R2 |

Com os mesmos pesos mensais do nível e EP de Welch, o MDE do agregado 169 × 14 é
de **55,9 g**. Contra θ = (2/17)·0,5·150 = 8,8 g, o poder do 17 × 14 é de
**7,6%**, e não os "até 11%" do doc 16 (conta com 167 controles).

**Calendário (R3), só Ceará, 7 × 177, pico fev–mai:** MDE do hiato **82,5 g**. O
δ mínimo sobre o bebê exposto é **165 g com f = 0,5**, 330 g com f = 0,25 e
825 g com f = 0,1. O arquivo salvo dizia 75,9 g porque usava CE+RN (7 × 344).
Com o RN, a variância de um desenho do Ceará saía calibrada por outra UF. O
default mudou (§2, item 15). [aud.; reconciliação em `resultados/reconciliacao/`]

---

## 2. Código: os 20 achados

Todos conferidos no código antes de mexer. As correções em Python têm teste que
reproduz o contraexemplo da auditoria; conferi que o do placebo falha com o
script antigo. As do R (itens 5, 6, 7, 12, 13, 14 e 17) foram checadas por
sintaxe, e a do item 13 também com dado sintético.

| # | achado | veredito | correção |
|---|---|---|---|
| 1 | **Placebos usavam o pós-ban** (`10_spt_pretrend.py`: pseudo-pós `t >= corte` sem teto) | ✔ **procede; era erro meu** | painel cortado em [início; corte pré] antes de montar os placebos; janela que alcance 2019 é recusada; EP e p de Welch do nível por corte |
| 2 | Holm transforma NaN em p finito (`holm([nan, 0,04])` → `[0,08; 0,08]`) | ✔ | nulo continua nulo; conta como p = 1 para os outros; família marcada incompleta |
| 3 | Holm corrige a inclinação, não o nível que virou alvo | ✔ | **família B** (nível, pós-resultado, adaptativa) ao lado da **família A** original, que continua como foi declarada |
| 4 | Regra "abaixo do MDE → limite superior" (`04_robustness.py`) | ✔ | saiu. O MDE é impresso como informação de desenho |
| 5 | "Falsifica 15 g?" pela meia-largura (`03_contdid.R`) | ✔ | teste de verdade: benefício ≥ 15 g é rejeitado se o limite superior do IC < +15; equivalência por TOST. **No −36,19 g, o benefício ≥ 15 g é rejeitado** (p unilateral 0,002). A regra antiga dizia "não" |
| 6 | Seção "diagnóstico do Teorema C.1" compara level com slope | ✔ | removida (ver §3.2) |
| 7 | `--exposicao` só rotulava o CSV | ✔ | opção removida, e passá-la é erro; as saídas gravam o `contraste` |
| 8 | SIM: ano sem fonte vira taxa fetal zero | ✔ (não afetou 2015–2022) | zero só dentro dos anos cobertos; fora, ausente, com a coluna `sim_ano_coberto` |
| 9 | `make real` rodava o fetal com `--fonte auto` | ✔ | `--fonte dofet`; o teste do Makefile passou a olhar a receita inteira |
| 10 | Proveniência de cada componente perdida no join | ✔ em parte: o sufixo `__simulado` já impedia a mistura automática | colunas `fonte_<componente>`; painel com componente simulado não recebe o rótulo `real` |
| 11 | Dezembro de 2024 inteiro no painel | ✔ em parte: o painel atual vai até 2022 | fim em nov/2024, a exclusão conservadora do mês |
| 12 | Zero sem aptidão: o R mantém, o 07/08 descarta | ✔ | erro nas três rotas (R, 04, 13) |
| 13 | Bandas CCK sem a incerteza do grupo zero | ✔ **confirmado no código fixado** (a auditoria só apontou o risco) | colunas `ep_m0`, `ic_inf_m0` e `ic_sup_m0`, e o relatório conta os pontos pelas duas bandas |
| 14 | `03_contdid.R` sai com status 0 quando a estimação falha | ✔ | CSV antigo removido; status 1 no fim |
| 15 | Calendário e MDE calibrados no CE+RN | ✔ | `14`: universo `--ufs 23` por padrão; `13`: cada desenho calibra nas UFs das suas unidades, e entram os contrastes estimados (17×14, 169×15, 169×14) |
| 16 | `12_erro_de_classificacao.py` fixa MDE = 33,4 | ✔ | MDE vem de `--mde` ou do `mde_desenhos.csv` (linha do 17×14); o legado só com aviso |
| 17 | HonestDiD/SDID com 2019 inteiro no pós | ✔ | `--corte-pre/--corte-pos` (padrão 2018-12/2020-01): 2019 sai inteiro, porque meio ano viraria célula anual de três meses; `--corte-pos 2019-01` reproduz o antigo |
| 18 | Nível do 04 com 15 controles; `D_ZERO` só chegava ao contdid | ✔ | `--d-zero` no 04, 09 e 10, e o `make real` passa `D_ZERO`; o nome do arquivo leva desfecho e definição |
| 19 | `p_welch` era cauda normal | ✔ | t com graus de liberdade de Welch–Satterthwaite; `p_normal` fica ao lado; conferido contra o `scipy` |
| 20 | Conab: rótulo por prefixo literal e ausente virando zero | ✔ | rótulo normalizado; ausente fica ausente; coluna `leiaute`; o relatório não afirma mais exclusividade nem maioria |
| — | Weitzman com σ = 0 classifica por inclinação | ✔ | "empate" |

**Procedem e ficaram para depois**, com o motivo:

| achado | por que não agora |
|---|---|
| **SIH esparso**: 46 das 17.664 células observadas; no contraste principal, 3 municípios positivos e **nenhum controle** | o canal A5 é o SINAN (pré-especificação §6), e o SIH é série secundária que nenhuma estimação usa. O conserto exige registrar cobertura por **competência** do RD, que não é data de internação, antes de pôr zero. Até lá, fica registrado em `lacunas-de-dados.md` como inadequado para DiD |
| Célula de 2016 com um óbito fetal, nenhum nascido e taxa 1 | aritmeticamente certa, marcada em `sem_denominador`; entra numa sensibilidade que a exclua, não numa exclusão automática |
| Média dos meses disponíveis no colapso pré/pós (`03_contdid.R`) | ausência seletiva muda o peso implícito, mas são 10 células em 17.664; documentado, sem mudança |
| Metadados das saídas antigas (chamada, seed, cortes) | as saídas novas gravam desfecho, definição do zero, cortes, seed e `contraste`; as antigas ficam como estão, com o aviso deste doc |

O R instalado na sessão (4.3, só com o data.table) não tem os pacotes do
projeto. Deu para checar a sintaxe de todos os `.R` e rodar as funções novas do
`03_contdid.R` com dado sintético. O pipeline R inteiro precisa do `renv.lock` e
roda na máquina do pesquisador (§9).

---

## 3. Identificação e inferência: o que estava errado no texto

### 3.1 MDE, significância e o piso de 15 g

- **Os 33,4 g são do decil contra os 167 restantes.** Os estimadores do decil
  usam 17 × 14 (MDE ≈ 52–55 g), e o agregado usa 169 × 14 (≈ 45–56 g, conforme a
  conta). O doc 16, a calibração do script 12 e o paper usavam 33,4 g como MDE
  de contrastes que não eram o dele.
- **O MDE não classifica a estimativa.** Com 80% de poder, MDE ≈ 2,8·EP, e a
  significância começa em 1,96·EP. "Abaixo do MDE, logo limite superior" é
  falso. A §5 e a §7 da pré-especificação estão escritas assim. A emenda
  proposta preserva o compromisso datado e troca a regra pelo teste (linha nova
  na §8, a ratificar).
- **O doc 17 errou duas vezes.** Na §7.1: "a meia-largura é o dobro do piso" não
  é razão, porque largura não testa efeito mínimo. Na §3.5 e na §7.4:
  "concordância entre MDE previsto (33,4) e meia-largura realizada (30,3) valida
  o diagnóstico" compara objetos diferentes. MDE de 33,4 implica meia-largura de
  23,4, e meia-largura de 30,3 implica MDE de 43,3. Corrigido lá, com remissão a
  este doc.

### 3.2 ATT(d|d) contra ATE(d) não é teste de nada

Pelo Teorema C.1 (CGS, v4), sob PT a expressão E[ΔY|D=d] − E[ΔY|D=0] identifica
ATT(d|d); sob SPT, **a mesma expressão** identifica ATE(d). Não existem duas
curvas para comparar. `level` contra `slope` compara uma função com a sua
derivada. O diagnóstico do doc 03 §4.1 e o cabeçalho do `03_contdid.R` estavam
errados. O que existe de testável é o placebo do pré-período (script 10), e ele
falsifica, não valida.

### 3.3 Corolário 1: o teorema está certo, a premissa não foi verificada

"Sem falso negativo — verificado pela flag 5" era forte demais. O Censo de 2006
mostra que nenhum município de área zero tinha estabelecimento com aplicação por
aeronave **em 2006**. Não mostra 2018. Aplicação por prestador de fora, mudança
entre 2006 e 2018, deriva e controle vetorial ficam de fora do Censo. θ/VPP
continua como **cenário**, com VPP e falso negativo de 2018 desconhecidos. E
"aumentar N sem aumentar o VPP não resolve" é falso como regra: com VPP fixo e
positivo, mais unidades reduzem o EP. O que vale aqui é mais estreito. No Ceará,
os municípios que entram ao baixar o corte têm VPP menor, e a mistura piora mais
depressa do que o EP cai (doc 16 §6).

### 3.4 Calzada, calendário e o que a DDD estima

- 80–150 g é o contraste de **intensificação sazonal** sob exposição alta em
  Calzada et al., medido por galões por hectare em células de 5 × 5 km [aud.].
  É cenário, não teto biológico transportável para o Ceará. "Impossível" e "não
  passa de" saem do texto. E os 38–89 g do working paper não se misturam com os
  80–150 g da versão publicada (corrigido no script 14 e no doc 14).
- A diferença tripla estima **ATT_pico − ATT_fora**, não o efeito anual.
  Resultado zero pode significar efeitos iguais nos dois grupos de coortes.
- "A mudança de sigatoka com o fim da seca é substituição, parte do efeito"
  (doc 19 §6) está errado como estava. Substituição causada pelo ban é
  mecanismo. Clima que mudaria aplicação e saúde sem ban é confundidor.

### 3.5 Poucos controles

Permutação global não é aleatorização, e a estratificada por GAEZ supõe
intercambiabilidade condicional. Conley–Taber "invertido" (resíduos dos 169
tratados como referência para os 14 controles) exigiria choques i.i.d. e efeito
homogêneo: os resíduos dos tratados carregam efeito heterogêneo. Não se promove
nenhum desses a método validado. O que o projeto reporta é a distância entre
eles, e ela é pequena no nível (p de 0,02 a 0,04).

---

## 4. Fontes primárias: o que mudou

| fato | antes | agora |
|---|---|---|
| **Revogação da Lei 1.478/2009 de Limoeiro** | secundária (imprensa) | **art. 212 da Lei 1.511/2010**: "Fica revogada a Lei nº. 1.478, de 20 de novembro de 2.009." (PDF da Câmara, p. 65, digitalizado, sem camada de texto; SHA-256 `affb588f…`) [aud.]. Um **acórdão** indexado registra a "superveniente revogação da Lei nº 1.478/2009 pela Lei nº 1.511/2010", que levou à "perda de interesse recursal" [índice, Jusbrasil]. A fonte vira `primaria`, com a ressalva de que a leitura é da auditoria |
| **A lei de 2010 não proibia, regulava** | — | na mesma página começa o **art. 214**, que submete a pulverização aérea a condições [aud.] |
| **Lei 2.054/2018 de Limoeiro** (27/08/2018, política ambiental) | desconhecida | arts. 152–159 [aud.]. Art. 153: afastamento de 1.000/500 m, **aviso prévio de cinco dias**, comunicação dos produtos, multa, suspensão e proibição por reincidência. Art. 155: exame da água e suspensão diante de contaminação. Não é novo ban. Em **agosto de 2018** o município ainda regulava a pulverização aérea |
| **2011** | ameaça aberta | a nota da SDH de 11/03/2011 existe em reprodução de 12/03/2011 (racismoambiental), sem ato, juízo ou prazo [aud.]. A ACP de julho de 2011 aparece no Mapa de Conflitos da Fiocruz, sem prova de deferimento; uma notícia de ago/2011 fala em declínio de competência. O número `0011509-12.2012.8.06.0115`, citado numa dissertação, tem sufixo `.8.06`, de justiça **estadual** [aud.]. **Nada primário mostra ban regional efetivo em 2011–2018** |
| **Aplicação aérea em 2018** | desconhecida | Repórter Brasil, jun/2018: "o Brasil continua aplicando agrotóxicos por avião. Em Tomé, é difícil encontrar quem nunca viu ou passou perto da rota desses aviões" [índice]. A auditoria cita, na reprodução do UOL, professora que via avião pulverizar da escola em Tomé [aud.; não achei o trecho]. O Povo (2025) atribui ao Sindag "quatro aviões" no estado em 2019 (parte interessada) [aud.] |
| **IN MAPA 2/2008** | art. 14 lido pelo índice | **art. 12, VI**: operador de outra UF remete o relatório à SFA do estado onde atuou. **Art. 14**: relatório mensal com município, cultura, área trabalhada e produtos comerciais, **sem** dose. **Inciso III**: declaração quando não houve atividade. **Art. 9º §8º**: mapa DGPS só se o equipamento grava. **§9º**: guarda mínima de dois anos, que não é ordem de descarte [aud.] |
| **Censo 2006** | "36 aeronaves" em alguns docs | **36 estabelecimentos com aplicação por aeronave**, de 110.312 (tab. 2.2.11 da 2ª apuração) [aud.]. Não conta aviões nem voos |
| **Lei 19.135/2024** | "exceção de drones" | vale desde **19/12/2024** e **substitui o antigo §2º** do art. 28-B (controle vetorial) por regra de altura e vento [aud.; índice confirma a regra de altura]. A janela termina antes disso de qualquer forma |
| **ADI 7.794** | — | existência confirmada (STF, 12/03/2025), andamento atual não [aud.] |
| **Januzzi (2025)** | "nulo nacional" | **duas versões**. A dissertação (UFV) não acha efeito nos quatro desfechos. O artigo do ENABER 2025 (Januzzi, Cardoso e Rodrigues) relata **+1,2 caso de baixo peso por mil nascidos para cada kg/ha a mais** [índice, Semantic Scholar]. Cita-se a versão, não "o nulo" |

⚠️ **O que isto faz com o nó de 2011.** Não há prova de que a pulverização
parou. Há quatro indícios de que continuou em Limoeiro. Uma lei municipal de 2018
a regulava. Havia relato de aviões em Tomé em 2018. O Sindag fala em aviões no
estado em 2019. E uma ação judicial ficou sem objeto porque a proibição de 2009
tinha sido revogada. Nada disso vira painel. Mas o nó passa de "talvez ninguém
tenha sido tratado" para "pelo menos Limoeiro provavelmente foi", e a pergunta
útil vira **quando e quanto**.

🆕 **A rota que faltava.** Se a Lei 1.511/2010 (art. 214) e a 2.054/2018
(art. 153) exigiam aviso prévio e comunicação dos produtos, a Prefeitura de
Limoeiro deveria ter os avisos de 2010 a 2018. Esse seria o registro, por
operador e por data, de cada aplicação aérea no principal município tratado.
Pedido E minutado em `docs/legislacao/lai-limoeiro-avisos-previos-minuta.md`.

---

## 5. Teoria e custos

- **B(q) = |ATT(q|q)|, B′ = |ACR|, B″ = ACR′** (`07-conclusao.tex`) não decorre
  dos estimandos. A dose é hectare normalizado pelo máximo, o desfecho é grama e
  o contraste é mudança de regime legal. Falta a ponte abatimento → exposição →
  saúde → valor, e o módulo apaga o sinal. O doc 17 §2.1 já dizia isso; o paper
  ainda não.
- **Proibição é o canto da cota**, não a cota ótima. Mostrar que a cota ótima
  vence a taxa ótima não mostra que o canto vence.
- **c → 0:** a divergência de Δ = σ²(c − β)/(2c²) é da aproximação local. Com
  abatimento limitado e choques de esperança finita, a diferença de bem-estar é
  finita. O argumento "a quantidade domina para qualquer β > 0" sai.
- **Conab:** a reexecução na planilha oficial deixava ausentes 72 dos 88 custos
  de avião, 69 dos 88 de trator e 57 dos 88 totais. Os 4 aviões positivos são o
  mesmo sistema (banana-prata, Bom Jesus da Lapa/BA, 2021–2024). "Mutuamente
  exclusivas" e "escolha da maioria" saíram. O script agora não converte
  ausente em zero.
- **Helfand & House e Skevas** são resultados de contexto: alface em Salinas; a
  agricultura holandesa, com defesa de combinação de instrumentos. Não são
  ordem universal entre taxa e quantidade.
- **As seis predições da §3 do paper** passam a condicionais. Duas mudam de
  natureza: "a substituição terrestre aumenta a intoxicação ocupacional" não tem
  sinal necessário, e "a intoxicação autoprovocada não se move" é controle
  negativo **candidato**, porque a lei pode mexer em compra, estoque e renda.

---

## 6. A matriz do doc 19, com os números (Fase 3)

| rota | antes | agora |
|---|---|---|
| R1 — nível por área (status quo) | manter como forma reduzida | **idem**, com a leitura da §1.2 e a inferência da §1.1 |
| R2 — nível, 7 da aeronave (2006) | "~50 g, subpotente salvo f alto" | MDE **43,5 g**. Poder de **73%** com f = 0,5 e δ = 80, de **25%** com f = 0,25, e de 8% com f = 0,1. Depende de 2006 valer em 2018 e é mudança de identificação |
| R3 — calendário, 7 da aeronave, pico hipotético | "o mais promissor: rodar o 14" | ✘ **rodado, e sem poder**: δ mínimo de 165 g com f = 0,5. Só compete com a R2 se o efeito se concentrar nas coortes do pico, e aí paga o preço da hipótese sazonal |
| R4 — calendário com o MAPA | o melhor, se o dado existir | continua. Mas o MAPA dá **quando e onde**, não **quem**: f continua sem medida |
| R5 — poucos tratados × doadores de fora | complementar | idem |
| R6 — fronteira | despriorizar | idem |
| R7 — limites | secundário | idem |
| R8 — Ensaio 1 como diagnóstico honesto | sempre válido | **a resposta provável se f for baixo**, agora com números. Com f = 0,25, a R2 tem 25% de poder contra 80 g, e a R3 exige 330 g. Só com metade ou mais dos nascimentos expostos a R2 passa a detectar 80 g (73%) |
| 🆕 R9 — medir o tratamento em Limoeiro | — | avisos prévios municipais (Pedido E) + relatórios do MAPA (Pedido D). Não aumenta o poder. **Decide se houve tratamento e quando**, que é a premissa de tudo acima |

**Leitura.** Com o SINASC por município, o fator que decide o poder é a **fração
dos nascimentos de cada município tratado que estava exposta** (f). Nenhum
registro de aplicação a mede. Os pedidos D e E respondem se houve tratamento e
quando, não quem foi exposto. Resta uma verificação barata, que só a máquina
local faz: se o DN público de 2015–2022 traz algum campo **submunicipal** de
residência preenchido para Limoeiro e Quixeré (bairro ou localidade). Se trouxer,
dá para separar as comunidades da Chapada da sede, e f deixa de ser grade. Se não
trouxer, como é provável, o Ensaio 1 tem o seu resultado mais forte na R8. A
contribuição passa a ser mostrar, com números, por que o desenho municipal não
alcança o efeito, e quais registros o alcançariam.

**Devil's advocate.** "Isso é desistir do efeito causal." Não. O efeito da
**lei** sobre o contraste por proxy está estimado e reportado (R1). O que não
existe é dado para ligar esse contraste à **retirada da pulverização onde ela
acontecia**. Isso não é juízo: é conta, com MDE, VPP e f na mesa. O risco
oposto também existe: continuar refinando estimadores sobre a mesma medida.
Seria a "multiplicação de estimadores" que a auditoria critica.

---

## 7. Textos propostos (não aplicados ao `.tex`)

**7.1 §6.2 — substitui o `quote` "Pelo critério fixado antes de olhar…".**

> O intervalo exclui o zero. Com a inferência que respeita os quatorze
> controles, o resultado se mantém: IC de 95% pela t de Welch em
> \([-69{,}15;\ -3{,}23]\), \emph{wild bootstrap} com \(p = 0{,}038\), análise de
> permutação com \(p = 0{,}034\), e retirar um único controle move o número entre
> \(-43{,}1\) e \(-29{,}3\) g. Três fatos impedem lê-lo como efeito da retirada da
> pulverização aérea. O sinal é o contrário do previsto, e a hipótese direcional
> não rejeita. A diferença não cresce com a dose: os terços da dose positiva
> variam \(-18{,}5\), \(-21{,}1\) e \(-10{,}7\) g, contra \(+18{,}6\) g dos
> controles. E a mesma comparação, feita só dentro do pré-período, move-se entre
> \(+20\) e \(+28\) g. O que o número estima é a diferença de trajetória entre
> municípios com e sem banana. Lê-lo como efeito exige tendências paralelas, e
> os placebos, que não as rejeitam, mas se movem do mesmo tamanho e no sentido
> oposto, não dão segurança a essa hipótese.

**7.2 §6.4 — o placebo.** Mantém-se o 7.3 do doc 17, com uma frase a mais: "Os
cortes placebo em nível, restritos ao pré-período, dão \(+20\) a \(+28\) g."

**7.2-bis §6.4 — a tabela da sonda do SPT e a "assimetria".** A tabela atual
usa placebos que levavam 2019–2022 dentro (§2, item 1). Com a janela corrigida
(definição 1, 184 municípios, como a tabela atual):

| corte placebo | peso: incl. | p | óbito fetal: incl. | p |
|---|---|---|---|---|
| 2016-01 / 2016-11 | 31,37 | 0,303 | 0,00331 | 0,557 |
| 2016-07 / 2017-05 | 33,86 | 0,259 | 0,00369 | 0,461 |
| 2017-01 / 2017-11 | 19,68 | 0,519 | 0,00184 | 0,732 |
| *desenho real* | *6,81* | *0,794* | *−0,00244* | *0,433* |

O parágrafo do peso fica (os placebos continuam maiores que o real). O parágrafo
"E a assimetria entre os dois desfechos é informativa" **sai**: dois dos três
placebos fetais passam o real em módulo, e o óbito fetal não separa sinal de
ruído melhor que o peso. Com `D_ZERO=4` os números mudam um pouco; a tabela
final sai do `make real`.

**7.3 §6.5 — "O que faria o desenho falar".** Troca "encorpar o grupo tratado"
por: "Encorpar o grupo tratado com municípios de dose menor reduz o erro-padrão e
dilui o tratamento ao mesmo tempo; no Ceará, a segunda coisa anda mais depressa
(doc 16 §6). O que faria o desenho falar é medir a aplicação, e não aumentar N."

**7.4 §7.1 — o que o ensaio estabelece.** Substitui a última frase do 7.4 do doc
17 por: "O que o ensaio estabelece é a magnitude do problema de mensuração.
Contra o sinal que a calibração de 2006 prevê, o desenho tem poder abaixo de 10%.
E o desenho de calendário exigiria efeitos acima de 160 g com metade dos
nascimentos expostos."

**7.5 §7.2 — a ponte.** Troca a cadeia B(q) = |ATT| … por: "Ligar o ATT a B(q)
exige uma função abatimento → exposição, uma resposta de saúde e uma
monetização, nenhuma das quais este ensaio identifica. O Ensaio 2 trabalha com
cenários explícitos para elas."

**7.6 §2 e estado da arte — Januzzi:** "A dissertação de Januzzi (2025) não
encontra efeito nos quatro desfechos; a versão apresentada no ENABER 2025, com
coautores, reporta aumento de 1,2 caso de baixo peso por mil nascidos por kg/ha
adicional. As duas usam exposição por índice geral de uso, não aplicação aérea."

⬜ Antes de 7.6 entrar no `.tex`: Crossref e leitura do PDF do ENABER, que o
proxy bloqueou.

---

## 8. Onde a auditoria erra ou exagera

Pouco, e em pontos menores:

- **H01** ("a lei começa na sanção"): o projeto já distinguia sanção (08/01) de
  vigência (09/01), no `CLAUDE.md` e no `02-background.tex`. Não era erro.
- **Janela anual do SDID/HonestDiD:** harmonizei tirando 2019 inteiro. O contdid
  mantém out–dez/2019, e a diferença é de três meses de coortes. Com dado anual
  não há corte melhor, e está declarado.
- **"Aumentar N não resolve" (§3.3):** a crítica é certa em geral. Mas o doc 16
  já restringia a frase ao Ceará, com os municípios que entrariam. O defeito era
  de redação, e ela foi corrigida no `CLAUDE.md`.

---

## 9. O que rodar agora (máquina local)

```powershell
git pull origin claude/exciting-noether-17cl74
pip install -r requirements.txt           # scipy agora é declarado
python -m pytest tests/ -q                # esperado: 294 passed
make real                                 # com D_ZERO=4, que é o padrão
make mde-desenhos
make mde-calendario
```

Ler, nesta ordem:

1. `cgs_curva_level__peso_medio__d0-4.csv`: quantos pontos excluem o zero pela
   banda com `ep_m0`. A previsão é **nenhum**. Se forem muitos, a §1.4 está errada.
2. `robustez_inferencia__peso_medio__d0-4.csv`: `nivel` = −36,19;
   `nivel_p_welch` ≈ 0,034; `nivel_rejeita_beneficio_piso` = True.
3. `spt_pretrend__peso_medio__d0-4.csv`: níveis +20,1, +28,1 e +21,6.
4. `holm_confirmatorios__d0-4.csv`: família B, bilateral Welch Holm ≈ 0,067.
5. `synthdid__peso_medio.csv` e `honestdid__peso_medio.csv`, que agora usam
   2020–2022 como pós: números novos, a registrar na §6 do paper.
6. `mde_desenhos.csv`: as linhas `decil17_vs_ce_zero_gaez` (≈ 52 g) e
   `positivos_vs_ce_zero_gaez` (≈ 45 g), com `universo_calibracao` = 23.

E, fora do código:

- **Pedido E** (novo): avisos prévios de pulverização aérea em Limoeiro,
  2010–2018 (`docs/legislacao/lai-limoeiro-avisos-previos-minuta.md`).
- **Pedido D**, corrigido com o art. 12, VI e o art. 14, III: protocolar.
- **SINASC:** conferir se o DN de 2015–2022 do Ceará traz campo de bairro ou
  localidade de residência preenchido para 230760 e 231150 (§6). Cinco minutos
  sobre os `.dbc` já baixados.

---

## 10. Decisões para o orientador

As seis do doc 17 §5 continuam, com mudanças:

1. **Estimando declarado.** O nível é pós-resultado. A família B de Holm o trata
   assim, e a pré-especificação ganha linha na §8, a ratificar.
2. **Emenda do critério de falsificação.** Troca-se "meia-largura < 15 g" e
   "abaixo do MDE → limite superior" pelo teste do piso e pelo TOST. Com isso, o
   benefício ≥ 15 g no agregado passa a **rejeitado**.
3. **Janela dos estimadores binários:** aceitar 2020–2022 como pós do
   SDID/HonestDiD, ou manter a antiga, rotulada como outro estimando.
4. **R2 como especificação**: mudança de identificação (tratado pelo método de
   2006).
5. **Enquadramento do Ensaio 1 como R8/R9**: o resultado é o diagnóstico de
   mensuração e poder, e o registro de tratamento como contribuição de dado.
6. **Ensaio 2 por cenários**, sem ponte estimada.

---

## 11. Arquivos desta rodada

- **Código:** `scripts/estimate/03_contdid.R`, `04_robustness.py`,
  `07_honestdid.R`, `08_synthdid.R`, `09_holm.py`, `10_spt_pretrend.py`,
  `11_weitzman_inversao.py`, `12_erro_de_classificacao.py`, `13_mde_desenhos.py`,
  `14_mde_calendario.py`; `scripts/data_prep/03_clean_fetal_deaths.py`,
  `08_alvos_legislativos.py` (semente de Limoeiro), `12_clean_conab_custos.py`;
  `scripts/build_panel/05_build_panel.py`; `Makefile`; `requirements.txt`.
- **Testes:** 20 novos em `tests/test_data_prep.py` (294 no total).
- **Docs:** este; `docs/revisao/auditoria-2026-09-23/`;
  `docs/legislacao/lai-limoeiro-avisos-previos-minuta.md` (novo);
  `lai-mapa-relatorios-mensais-minuta.md`, `README.md` e
  `bans-municipais-ce.csv` de `docs/legislacao/`; `CLAUDE.md`;
  `docs/pre-especificacao.md` (linha na §8); docs 03, 13, 14, 16, 17 e 19
  (erratas); `docs/estado-da-arte.md`; `docs/lacunas-de-dados.md`.
