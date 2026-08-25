# Briefing — reunião de orientação

*Estado do Ensaio 1 e as decisões que dependem de orientador e orientando.
2026-08-24. Companheiro do roteiro em `04-roteiro-qualificacao.md`.*

Este documento não responde as decisões da §3. Ele diz o que está em jogo em cada
uma, o que cada escolha custa, e o que ela muda lá na frente. **A escolha é de
vocês dois.**

---

## 1. A tese em um parágrafo

O Ceará baniu a pulverização aérea de agrotóxicos em **09/01/2019** (Lei
16.820/2019, "Lei Zé Maria do Tomé"), num ban **estadual e simultâneo** — não
escalonado. A dissertação trata a pulverização como **externalidade negativa** e
se divide em dois ensaios. O **Ensaio 1** estima o efeito causal do ban sobre
desfechos de nascimento (SINASC), com a qualidade da água (SISAGUA) como canal; a
identificação vem da variação de **dose** — intensidade agrícola pré-ban — entre
os 184 municípios, com o estimador de tratamento contínuo de **Callaway,
Goodman-Bacon & Sant'Anna (2024)**. O **Ensaio 2** usa Weitzman (1974) para
comparar proibição, taxação e zonas-tampão, **ancorado na curva dose-resposta que
o Ensaio 1 estima**.

---

## 2. Estado do desenho

### Fechado, com fonte primária

| | |
|---|---|
| **Data do tratamento** | sanção **08/01/2019**, publicação e vigência **09/01/2019** (texto oficial AL-CE, em `docs/legislacao/`) |
| **Janela** | 2015 → **19/12/2024**, cortada na Lei 19.135/2024 (exceção para drones) para preservar a cota zero |
| **Desfecho primário** | peso médio ao nascer, município × ano-mês |
| **Estimador** | CGS (2024), tratamento contínuo — **não** é DiD escalonado, não há variação de *timing* |
| **Instrumento** | aptidão agroclimática FAO-GAEZ, receita de Reynier & Rubin (2025) |

**Três marcos de antecipação, não um:** PL 18/2015 apresentado em **24/02/2015**
(notícia), aprovado por unanimidade em **18/12/2018** (certeza), vigência em
**09/01/2019** (obrigação). O STF validou a lei em mai/2023 (ADI 6137, unânime).

### Já é código que roda

Três scripts, 30 testes, tudo validado contra dado simulado — nenhum rodou contra
dado real ainda, porque a rede está fechada (§5).

- **`01_check_dose_variation.py`** — o Gate 1. Mede a dispersão de dose entre
  municípios e **recomenda a especificação** pela escada do CGS. Calcula o efeito
  mínimo detectável em duas contabilidades (contando bebês e contando municípios)
  e responde se um resultado nulo seria legível.
- **`02_clean_births.py`** — SINASC limpo e colapsado a município × ano-mês.
- **`03_clean_fetal_deaths.py`** — óbito fetal do SIM, para o teste de seleção
  para nascimento vivo (§3, D-bis).

### Os dois números que ainda não existem, e que decidem tudo

1. **A DP das tendências municipais de peso ao nascer no pré-período.** É ela, e
   não a dispersão de dose, que determina se o efeito é detectável. Sai só do
   SINASC.
2. **O número de municípios de dose alta.** Sai só do PAM.

Enquanto os dois não existirem, boa parte do que parece questão metodológica é
questão empírica esperando dado. A §4 lista quais.

---

## 3. As decisões que dependem de vocês dois

Estas **não** se resolvem com mais dado. São julgamento.

### D1 — A curva ou o nível como resultado principal? *(a mais importante)*

O CGS separa dois parâmetros com preços diferentes:

| Parâmetro | O que é | Hipótese que exige |
|---|---|---|
| `ATT(d\|d)` | efeito **no nível** de dose *d*, entre quem tem dose *d* | paralelismo tradicional (Assumption 4) |
| `ATE(d)` / `ACR(d)` | a **curva** dose-resposta e sua inclinação | **strong parallel trends** (Assumption 5) |

A Assumption 5 restringe trajetórias sob doses **não recebidas** — e por isso é
**não testável**. Nenhum pré-período informa o que teria acontecido com um
município sob uma dose que ele não teve. ⚠️ **O placebo de tendências pré não
testa a A5**; ele fala da A4. E o Teorema C.1 do CGS mostra que A4 + A5 juntas
excluem *selection-on-gains* — municípios não podem ter escolhido a intensidade
agrícola por antecipar ganhos diferentes. Isso é uma hipótese econômica forte
sobre decisão de plantio.

A decisão registrada até aqui foi **a curva como resultado principal, acompanhada
dos limites de identificação parcial da §5.1 do CGS**, sob hipótese de direção do
viés. Vale reconfirmar, porque:

> ⚠️ **O Ensaio 2 precisa da curva, não do nível.** Weitzman preço-vs-quantidade
> decide pela **inclinação relativa** do dano marginal — isto é, por `ACR(d)`, a
> derivada. Se o Ensaio 1 recuar para `ATT(d|d)`, o Ensaio 2 perde a âncora que o
> projeto lhe deu. **D1 é decisão de arquitetura da dissertação inteira, não de
> gosto econométrico.**

**Ferramentas, e a distinção que não pode virar erro:** HonestDiD (Rambachan &
Roth 2023) formaliza sensibilidade à **A4**; os limites da §5.1 do CGS cobrem a
**A5**. São camadas complementares — usar uma no lugar da outra é o erro a
evitar.

**Custo de cada rota:** a curva entrega o que o Ensaio 2 pede, ao preço de
defender uma hipótese não testável. O nível é mais barato de defender e deixa o
Ensaio 2 sem âncora quantitativa.

### D2 — O que conta como resultado negativo?

Um nulo só é inconclusivo se o intervalo de confiança for largo. Se o IC for
estreito e **excluir** o efeito esperado, um nulo *é* evidência de que o ban não
produziu o efeito que a literatura levaria a esperar — **o desenho falsifica**.

A conta é mecânica: a meia-largura do IC é **0,70 × MDE**, então o desenho
falsifica um efeito de 15 g sempre que o MDE ficar abaixo de **21,4 g**.

**Se a estimativa vier zero, o IC de 95% exclui 15 g?**

| Municípios tratados | DP tend. 10 g | 18 g | 20 g | 30 g | 40 g |
|---|---|---|---|---|---|
| 3 | ±11,4 ✔ | ±20,5 ✘ | ±22,8 ✘ | ±34,2 ✘ | ±45,6 ✘ |
| 5 | ±8,9 ✔ | ±16,0 ✘ | ±17,8 ✘ | ±26,7 ✘ | ±35,5 ✘ |
| **10** | ±6,4 ✔ | **±11,5 ✔** | ±12,7 ✔ | ±19,1 ✘ | ±25,5 ✘ |
| 20 | ±4,6 ✔ | ±8,4 ✔ | ±9,3 ✔ | ±13,9 ✔ | ±18,6 ✘ |
| 40 | ±3,5 ✔ | ±6,3 ✔ | ±7,0 ✔ | ±10,5 ✔ | ±14,0 ✔ |

⚠️ **O piso amostral do ruído já é ≈ 17,7 g** — município de 800 nascimentos/ano,
meia-janela de 2 anos, **sem nenhuma heterogeneidade real, só amostragem**. A
coluna de 20 g é portanto aproximadamente o **melhor caso**, não o caso médio.

**As duas consequências que a reunião precisa registrar:**

1. **O alvo é dez municípios tratados**, não três. Rigotto et al. (2013)
   compararam **três** — e três não falsifica no cenário base.
2. **A referência de magnitude é 23–32 g** (Reynier & Rubin 2025, mesmo desfecho,
   mesmo instrumento GAEZ, publicado em PNAS). O efeito esperado declarado é
   15–25 g.

**O que precisa ser decidido:** o piso de efeito esperado. Se o desenho não
alcançar poder para falsificá-lo, a contribuição do Ensaio 1 muda de natureza —
de *"o ban funcionou?"* para *"eis um limite superior informativo"*. É melhor
combinar isso **antes** de estimar do que depois de ver o coeficiente.

⚠️ **Uma saída que já foi descartada, e por quê.** Trocar o desfecho primário
quando o poder não fecha **não funciona** — os alternativos são piores:

| Desfecho | Razão efeito/ruído |
|---|---|
| **Peso médio** | **1,30 – 1,81** |
| Baixo peso (<2500 g) | 0,44 – 0,80 |
| Prematuridade (<37 sem) | 0,50 |
| Mortalidade infantil | 0,17 |

Média contínua sobre todos os nascimentos bate evento raro por um fator de duas a
oito vezes. Peso médio é o **único com razão acima de 1**. A saída correta é
**encorpar o grupo tratado** baixando o corte de dose — aceitando a diluição do
efeito médio que isso traz.

### D3 — Controle vetorial: dentro ou fora do `d = 0`?

O **§2º do art. 28-B** (redação de 2019) proíbe também *"a incorporação de
mecanismos de controle vetorial por meio de dispersão por aeronave"*. O ban é de
**método**, e dispersão sanitária é método aéreo.

Consequência: um município sem agricultura pulverizada mas com controle aéreo de
dengue **é tratado**. E esses tendem a ser os **maiores** — logo a contaminação
correlaciona com porte, que correlaciona com desfecho perinatal. Não é
contaminação aleatória; tem direção.

As duas leituras são defensáveis e **dão estimandos diferentes**: excluir esses
municípios do `d = 0` estima o efeito do ban agrícola; incluí-los como tratados
estima o efeito do ban de método.

*(Nota: a redação de 2024 **não reproduz** o §2º — a dispersão aérea sanitária
volta a ser possível a partir de 19/12/2024. Mais uma razão para o corte da
janela ali.)*

### D4 — A janela pré-ban recua para 2010–2014?

⚠️ **A janela pré-ban atual começa depois do marco de notícia.** O PL 18/2015 foi
apresentado em **24/02/2015**, e a janela é 2015–2018. A dose medida pode já estar
respondendo à expectativa do ban — e isso **morde a variável de tratamento, não
só o desfecho**. Quatro anos de tramitação com debate público são quatro anos de
sinal.

**Recuar para 2010–2014** eliminaria a contaminação por antecipação, ao preço de
depender da comparabilidade da PAM naquele período (houve mudança de metodologia
ou de classificação de cultura? — verificação pendente) e de atravessar o ban
municipal de 2009 (§4).

Antecipação contra comparabilidade. Nenhum dado decide sozinho.

### D5 — Qual é o plano B se o Gate 1 cair?

Se não houver dispersão de dose utilizável, o desenho de tratamento contínuo cai
inteiro, e a rota volta a ser **controle sintético estadual** (Arkhangelsky et al.
2021) ou **pareamento à la Rigotto** — 3 expostos contra 12 municípios de
agricultura familiar, que é o ancestral direto do PSM+DiD já previsto como camada
de comunicação.

Isso muda a espinha da tese. Combinar antes vale mais que improvisar depois — e
melhor descobrir no Gate 1 que no capítulo 6.

### D6 — E se o *enforcement* voltar vazio?

Se o ban não foi fiscalizado, a dose pré-ban mede **intenção**, não exposição
removida, e a curva mede aderência voluntária. O estimando vira **efeito de
intenção de tratar**, e o parâmetro-alvo declarado no projeto precisa ser
renomeado de acordo.

A fiscalização cabe a **SEMACE, SEARA e Secretaria da Saúde** (arts. 15 e 30 da
Lei estadual 12.228/1993). O pedido pela **Lei de Acesso à Informação** já está
minutado (`07-layer4-perguntas-abertas.md`) e ainda **não foi protocolado** — ver
§5.

É limitação declarável, não impedimento. Mas precisa estar declarada, e a decisão
de renomear o estimando é de vocês.


### D7 — O que é confirmatório e o que é exploratório?

⚠️ **Achado da revisão metodológica** (`09-revisao-metodologica.md`, M1), e o
único que ela classifica como impeditivo hoje.

O pipeline produz hoje **31 séries candidatas a desfecho** — 6 do SINASC, 6 do
óbito fetal, 19 do canal de intoxicação. Some-se três definições de exposição por
trimestre, quatro construções de `d = 0` e dois parâmetros-alvo: o espaço de
especificações passa de mil.

**Por que isso é grave justamente neste desenho.** O projeto já sabe que o poder
é curto — o MDE no cenário base fica acima do efeito esperado de 15–25 g. **Poder
curto mais espaço de busca grande é a combinação que produz achado espúrio com
aparência de rigor**: basta um dos 31 se mover, e como cada um tem justificativa
teórica própria, a racionalização vem pronta depois do fato.

Um desenho que declara honestamente ter pouco poder e ao mesmo tempo mantém 31
desfechos em aberto está deixando aberta a porta que ele mesmo fechou nas outras
paredes.

**O que fecha, e custa um documento:** `docs/pre-especificacao.md` já está
montado, com o que já foi argumentado pré-preenchido e o que é de vocês em
branco. Declarar desfecho primário, exposição primária, o que é confirmatório, e
se há correção de família. O resto vira **exploratório declarado**, o que é
legítimo e honesto.

⚠️ **A janela para isso fecha na primeira rodada com dado real** — e ela ainda
está aberta só porque a rede está bloqueada. Um plano escrito depois de ver o
coeficiente não é plano.

*(O `make real` está bloqueado até o documento ser fechado e commitado. O commit
é o carimbo de tempo: o histórico do git prova que o plano é anterior ao dado.)*

### D-bis — a que depende de um teste, e só depois vira decisão

**Seleção para nascimento vivo.** Se o ban reduziu óbito fetal, fetos marginais
passam a nascer vivos e entram pela **cauda de baixo peso**, puxando a média para
baixo — na direção *oposta* ao efeito esperado e competindo pelo mesmo espaço de
magnitude. Um efeito real pode aparecer como zero.

**Antes de escolher correção, verificar se o problema existe:** rodar a série de
óbito fetal do SIM contra a dose, com o mesmo desenho. O script 03 já prepara essa
série. Se óbito fetal não se move com a dose, a discussão acaba num parágrafo de
limitações com o teste como evidência.

Se **se mover**, aí a escolha é de vocês, entre três rotas conhecidas:

| Rota | O que faz | Custo |
|---|---|---|
| Reporte conjunto | peso e óbito fetal lado a lado, sem compor | mais honesto, menos conclusivo |
| Desfecho composto | vivos + óbitos fetais como uma coorte | resolve por construção; o desfecho deixa de ser "peso ao nascer" |
| Limites de seleção | faixa sob cenários extremos de quem entrou na amostra | não exige escolha substantiva; some com a precisão que já é escassa |

---

## 4. O que **não** é pergunta para esta reunião

Estas se resolvem com dado, não com discussão. Registrar e seguir.

| Pergunta | Quem responde |
|---|---|
| A cultura-âncora é banana, melão ou outra? | PAM — Gate 1. Três fontes independentes convergem para **banana**, mas convergência é hipótese, não escolha |
| Qual a DP das tendências municipais? | SINASC — script 02 |
| Quantos municípios de dose alta existem? | PAM — script 01 |
| Quais municípios tinham ban próprio antes de 2019? | levantamento legislativo (⚠️ ver abaixo) |
| MapBiomas separa banana e melão, ou só classes genéricas? | catálogo MapBiomas |
| A cobertura do SISAGUA correlaciona com a dose? | SISAGUA |
| O catálogo GAEZ cobre banana e melão? | catálogo FAO-GAEZ |
| A PAM 2010–2014 é comparável? | metodologia IBGE — insumo da D4 |

⚠️ **Um item desta lista é mais grave que os outros.** O art. 29 da Lei
12.228/1993 autoriza municípios a legislar supletivamente, e **Limoeiro do Norte
teria proibido a pulverização aérea em 2009** — dez anos antes da lei estadual, e
é um dos três municípios de alta exposição do estudo de Rigotto. Se procede, há
unidades **já tratadas** dentro do grupo de dose alta, e 2015–2018 deixa de ser
pré-tratamento para todos. Isso contamina a própria medida de dose, e é anterior
ao Gate 1 em importância.

### Duas coisas que a literatura já diz, e que valem para o enquadramento

- ⚠️ **O ban proíbe método, não molécula — e o químico não é o glifosato.** A
  tabela do Dossiê ABRASCO reproduzida no PL 18/2015 (23 pontos de coleta,
  Chapada do Apodi, 2009) mostra **procimidona e carbaril em 23/23, carbofurano
  em 18/23, fenitrotiona em 16/23 — e glifosato em 4/23**. Fungicida em banana,
  por avião. Consequência: o template de Dias, Rocha & Soares (soja TH +
  glifosato) **não transfere quimicamente**, e a receita GAEZ de Reynier & Rubin
  é construída sobre culturas **GM** — banana não é.
- **O efeito na literatura se concentra na cauda alta.** Larsen et al. (2017,
  *Nature Communications* 8:302) acham efeitos adversos de 5–9% **apenas no top
  5%** da exposição. Isso reforça a hipótese de limiar — e aperta o problema:
  efeito só na cauda + suporte fino na cauda.

---

## 5. O que está travado, e em quem

| O quê | Em quem | Prazo |
|---|---|---|
| **Pedido LAI à SEMACE** (autos de infração 2019–2024 + cadastro de prestadoras) | **você** — minuta pronta, falta protocolar | 20 dias legais + 10 de prorrogação. **É o único com relógio externo — dispare primeiro** |
| **Liberar a rede do ambiente** | **você** — configurações em claude.ai/code | libera `apisidra`, `servicodados`, `ftp.datasus.gov.br`, `basedosdados.org`, `gaez.fao.org` |
| Aquisição SINASC/SIM/PAM/GAEZ | depende da rede acima, ou download manual | — |
| Verificar Marx-Stoelting et al. (2025) | citação ainda não conferida contra DOI | — |

O pedido LAI mata dois coelhos: serve ao *enforcement* (D6) **e** ao `d = 0`
operacional, porque o art. 8º da Lei 12.228/1993 obriga prestadoras de serviço de
aplicação a se registrarem na SEMACE — fonte estadual, provavelmente melhor que
ANAC/MAPA/SINDAG.

---

## 6. Cronograma até a qualificação

Duas trilhas em paralelo. Cada etapa tem um **gate falsificável** — a pergunta
cuja resposta negativa manda voltar, não seguir.

```
E0   antecipação + bans municipais < 2019   ⚠️ pendente
E1   data e janela                          ✅ fechada
E1.5 DP das tendências (SINASC)             ⚠️ o gate que decide o ensaio
E2   variação de dose (PAM)                 — Gate 1
E3   escolha de especificação               — depende de D1
E4   grupo d = 0 e contaminação             — depende de D3
E5   build_panel
E6   estimação (contdid, R)                 — Teorema C.1 decide curva vs bounds
E7   robustez (Conley–Taber, SDID, PSM+DiD)
E8   texto da qualificação
```

**A escada de especificação**, que E3 aplica e que o script já calcula:

| Municípios com dose > 0 | Especificação |
|---|---|
| ≥ 40, suporte espalhado | curva não-paramétrica (sieve) |
| 15 a 39 | faixas discretas, indicadores múltiplos |
| 12 a 14 | faixas discretas — **suporte fino** |
| < 12 | binário sob Assumption 4-Agg; curva abandonada |

Descer um degrau não é fracasso. Descer sem registrar, é.

---

## Resumo de uma linha

**O desenho está fechado e o código está pronto; faltam dois números — a DP das
tendências e o número de municípios de dose alta — e seis decisões que nenhum
dado resolve. A D1 é a que amarra os dois ensaios.**
