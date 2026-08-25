# Briefing — reunião de orientação

*Estado do Ensaio 1 e as decisões que dependem de orientador e orientando.
Atualizado em 2026-08-25, depois de o pipeline fechar de ponta a ponta e de a
revisão metodológica rodar. Companheiro de `04-roteiro-qualificacao.md`.*

Este documento **não responde** as decisões da §3. Ele diz o que está em jogo em
cada uma, o que cada escolha custa, e o que ela muda adiante. A escolha é de
vocês dois.

---

## 0. Se a conversa for curta, é isto

O pipeline está **completo e testado** — sete scripts, 85 testes, do download à
inferência. Nenhum rodou contra dado real: a rede do ambiente bloqueia IBGE,
DATASUS e FAO.

E é justamente esse bloqueio que mantém aberta a única janela que importa hoje:

> ⚠️ **O pipeline produz 31 séries candidatas a desfecho, e o desenho já sabe que
> o poder é curto. Sem declarar por escrito o que é confirmatório antes do
> primeiro dado real, o projeto deixa aberta a porta que fechou nas outras
> paredes.** Essa é a **D7**, e ela bloqueia as demais.

`docs/pre-especificacao.md` está montado esperando as respostas. `make real` está
travado até ele ser preenchido, datado e **commitado** — o commit é o carimbo de
tempo que prova que o plano é anterior ao dado.

**Ordem sugerida da conversa:** D7 → D1 → D2 → o resto.

---

## 1. A tese em um parágrafo

O Ceará baniu a pulverização aérea de agrotóxicos em **09/01/2019** (Lei
16.820/2019, "Lei Zé Maria do Tomé"), num ban **estadual e simultâneo** — não
escalonado. A dissertação trata a pulverização como **externalidade negativa**, em
dois ensaios. O **Ensaio 1** estima o efeito causal sobre desfechos de nascimento
(SINASC), com água (SISAGUA) e intoxicação aguda (SIH) como canais; a
identificação vem da variação de **dose** — intensidade agrícola pré-ban — entre
os 184 municípios, com o estimador de tratamento contínuo de **Callaway,
Goodman-Bacon & Sant'Anna**. O **Ensaio 2** usa Weitzman (1974) para comparar
proibição, taxação e zonas-tampão, **ancorado na curva dose-resposta do Ensaio 1**.

---

## 2. Estado do desenho

### Fechado, com fonte primária

| | |
|---|---|
| **Data do tratamento** | sanção **08/01/2019**, publicação e vigência **09/01/2019** (texto oficial AL-CE) |
| **Janela** | 2015 → **19/12/2024**, cortada na Lei 19.135/2024 (exceção para drones) |
| **Estimador** | CGS, tratamento contínuo — **não** é DiD escalonado |
| **Instrumento** | aptidão agroclimática FAO-GAEZ (receita de Reynier & Rubin) |

**Três marcos de antecipação, não um:** PL 18/2015 apresentado em **24/02/2015**
(notícia), aprovado por unanimidade em **18/12/2018** (certeza), vigência em
**09/01/2019** (obrigação). STF validou em mai/2023 (ADI 6137, unânime).

### O pipeline, completo

| Etapa | O que faz |
|---|---|
| `00_export_datazoom.R` | ponte R→arquivo para SINASC, DOFET e SIH |
| `01_check_dose_variation.py` | **Gate 1** — dispersão de dose, MDE, e se um nulo seria legível |
| `02_clean_births.py` | SINASC → município × ano-mês |
| `03_clean_fetal_deaths.py` | óbito fetal (SIM) — o teste de seleção |
| `04_clean_poisoning.py` | intoxicação aguda (SIH) — o canal de substituição |
| `05_build_panel.py` | **E5** — dose + desfechos, com retroprojeção gestacional |
| `03_contdid.R` | **E6** — a curva, o event study, o gate do Teorema C.1 |
| `04_robustness.py` | **E7** — três inferências, o gate do MDE, sensibilidade ao zero |

### Os dois números que ainda não existem

1. **A DP das tendências municipais de peso ao nascer no pré-período.** É ela, e
   não a dispersão de dose, que decide se o efeito é detectável. Sai do SINASC.
2. **O número de municípios de dose alta.** Sai do PAM.

Enquanto não existirem, boa parte do que *parece* questão metodológica é questão
empírica esperando dado. A §4 lista quais.

---

## 3. As decisões que dependem de vocês dois

### D7 — O que é confirmatório e o que é exploratório? ⛔ *bloqueia as outras*

O pipeline produz hoje:

| Fonte | Séries candidatas |
|---|---|
| SINASC | 6 |
| Óbito fetal (SIM) | 6 |
| Intoxicação (SIH) | 19 |
| **Total** | **31** |

Some-se três exposições por trimestre, quatro construções de `d = 0` e dois
parâmetros-alvo: o espaço passa de **mil especificações**.

**Por que isso é grave neste desenho especificamente.** O projeto já sabe que o
poder é curto — o MDE no cenário base fica acima do efeito esperado de 15–25 g.
**Poder curto mais espaço de busca grande é a combinação que produz achado
espúrio com aparência de rigor**: basta um dos 31 se mover, e como cada um tem
justificativa teórica própria, a racionalização vem pronta depois do fato.

**O que fecha, e custa um documento.** Declarar: desfecho primário, exposição
primária, o que é confirmatório, e se há correção de família. O resto vira
**exploratório declarado** — o que é legítimo e honesto.

⚠️ **O placebo não conta como desfecho.** A série X68 (intoxicação autoprovocada)
entra como **falsificação**: a hipótese prevê que ela **não** se mova. Declarar
isso agora é o que impede reinterpretar um movimento nela como achado depois.

### D1 — A curva ou o nível como resultado principal?

| Parâmetro | O que é | Hipótese que exige |
|---|---|---|
| `ATT(d\|d)` | efeito **no nível** de dose *d* | paralelismo tradicional (Assumption 4) |
| `ATE(d)` / `ACR(d)` | a **curva** e sua inclinação | **strong parallel trends** (Assumption 5) |

A A5 restringe trajetórias sob doses **não recebidas** — por isso é **não
testável**. ⚠️ O placebo de tendências pré **não testa a A5**; fala da A4. E o
Teorema C.1 mostra que A4 + A5 juntas excluem *selection-on-gains* — hipótese
econômica forte sobre decisão de plantio.

> ⚠️ **O Ensaio 2 precisa da curva, não do nível.** Weitzman decide pela
> **inclinação relativa** do dano marginal — isto é, por `ACR(d)`, a derivada. Se
> o Ensaio 1 recuar para `ATT(d|d)`, o Ensaio 2 perde a âncora. **D1 é decisão de
> arquitetura da dissertação inteira, não de gosto econométrico.**

**⚠️ E agora a D1 tem um custo que antes não estava visível.** Ao conferir o
pacote `contdid` contra o código-fonte, três restrições apareceram:

| Restrição verificada | Consequência |
|---|---|
| O sieve exige **exatamente 2 períodos** | o "pré" vira **uma média única de 2015–2018** |
| O sieve **não faz event study** | os *leads* saem de **outro** estimador |
| Covariáveis **não suportadas** | ajuste municipal só por fora do CGS |

Juntas com o marco de notícia de 24/02/2015, elas produzem isto:

> **A média pré do estimador principal é potencialmente contaminada por
> antecipação — e a especificação principal não tem como revelar isso.** O event
> study existe, mas é outro estimador: ele não valida a curva, valida um objeto
> vizinho.

Isso não derruba a escolha da curva. Muda o preço dela, e o preço tem de estar no
texto.

### D2 — O que conta como resultado negativo?

Um nulo só é inconclusivo se o IC for largo. Se ele **excluir** o efeito
esperado, um nulo *é* evidência contra. A conta é mecânica: meia-largura do IC =
**0,70 × MDE**; o desenho falsifica 15 g sempre que o MDE ficar abaixo de
**21,4 g**.

**Se a estimativa vier zero, o IC de 95% exclui 15 g?**

| Municípios tratados | DP tend. 10 g | 18 g | 20 g | 30 g | 40 g |
|---|---|---|---|---|---|
| 3 | ±11,4 ✔ | ±20,5 ✘ | ±22,8 ✘ | ±34,2 ✘ | ±45,6 ✘ |
| 5 | ±8,9 ✔ | ±16,0 ✘ | ±17,8 ✘ | ±26,7 ✘ | ±35,5 ✘ |
| **10** | ±6,4 ✔ | **±11,5 ✔** | ±12,7 ✔ | ±19,1 ✘ | ±25,5 ✘ |
| 20 | ±4,6 ✔ | ±8,4 ✔ | ±9,3 ✔ | ±13,9 ✔ | ±18,6 ✘ |
| 40 | ±3,5 ✔ | ±6,3 ✔ | ±7,0 ✔ | ±10,5 ✔ | ±14,0 ✔ |

⚠️ **O piso amostral do ruído já é ≈ 17,7 g** — sem heterogeneidade real, só
amostragem. A coluna de 20 g é aproximadamente o **melhor caso**.

**Duas consequências:** o alvo é **dez** municípios tratados, não três (Rigotto et
al. compararam três). E a referência de magnitude é **23–32 g** (Reynier & Rubin,
PNAS), contra 15–25 g esperados.

⚠️ **Trocar o desfecho quando o poder não fecha não funciona** — peso médio é o
**único** com razão efeito/ruído acima de 1 (1,30–1,81, contra 0,44–0,80 baixo
peso, 0,50 prematuridade, 0,17 mortalidade). A saída é **encorpar o grupo
tratado** baixando o corte de dose.

### D3 — Controle vetorial: dentro ou fora do `d = 0`?

O **§2º do art. 28-B** proíbe também dispersão aérea para controle vetorial. Um
município sem agricultura pulverizada mas com controle aéreo de dengue **é
tratado** — e esses tendem a ser os **maiores**, logo a contaminação correlaciona
com porte, que correlaciona com desfecho.

⚠️ **E isso deixou de ser ressalva de texto.** O sieve do `contdid` faz:

```r
m0 <- mean(dy[dose == 0])    # a curva inteira é centrada nisso
```

**Contaminação do zero não acrescenta ruído: desloca o nível da curva inteira.**
As quatro construções de zero da §5.3 têm de ser rodadas, e a dispersão entre
elas **é** a incerteza sobre o nível.

### D4 — A janela pré-ban recua para 2010–2014?

O PL é de **24/02/2015** — a janela atual começa *depois* do marco de notícia, e a
dose medida pode já estar respondendo à expectativa. Isso **morde a variável de
tratamento**, não só o desfecho. Recuar elimina isso, ao preço da comparabilidade
da PAM em 2010–2014 e de atravessar o ban municipal de 2009.

⚠️ **A D4 ganhou peso com a restrição de 2 períodos** (ver D1): com o pré virando
média única, a contaminação por antecipação fica invisível dentro da
especificação principal.

### D5 — Qual é o plano B se o Gate 1 cair?

Sem dispersão de dose utilizável, a rota vira **controle sintético estadual** ou
**pareamento à la Rigotto** — 3 expostos contra 12 de agricultura familiar, o
ancestral direto do PSM+DiD. Muda a espinha da tese; combinar antes vale mais que
improvisar depois.

### D6 — E se o *enforcement* voltar vazio?

Sem registro de autuação, a dose pré-ban mede **intenção**, não exposição
removida: o estimando vira **efeito de intenção de tratar** e o parâmetro-alvo
precisa ser renomeado. O pedido LAI está minutado e **não foi protocolado**.

⚠️ **Mas agora há uma segunda via.** Se a série de intoxicação **acidental** (X48)
se mover com a dose, isso é evidência **independente** de que o ban mudou
comportamento no campo — sem depender de ninguém responder ofício.

### D-bis — Seleção para nascimento vivo *(decisão só depois de um teste)*

Se o ban reduziu óbito fetal, fetos marginais passam a nascer vivos e entram pela
**cauda de baixo peso** — na direção *oposta* ao efeito esperado. Um efeito real
pode aparecer como zero.

**Antes de escolher correção, verificar se o problema existe:** o script 03 já
prepara a série. Se não se move, acaba num parágrafo de limitações. Se se move, a
escolha é de vocês:

| Rota | O que faz | Custo |
|---|---|---|
| Reporte conjunto | peso e óbito fetal lado a lado | mais honesto, menos conclusivo |
| Desfecho composto | vivos + óbitos como uma coorte | resolve por construção; o desfecho muda de nome |
| Limites de seleção | faixa sob cenários extremos | não exige escolha substantiva; some com precisão |

---

## 4. O que **não** é pergunta para esta reunião

| Pergunta | Quem responde |
|---|---|
| A cultura-âncora é banana, melão ou outra? | PAM — Gate 1 (três fontes convergem para banana, mas convergência é hipótese) |
| Qual a DP das tendências municipais? | SINASC — script 02 |
| Quantos municípios de dose alta existem? | PAM — script 01 |
| Quais municípios tinham ban próprio antes de 2019? | levantamento legislativo — **ver abaixo** |
| MapBiomas separa banana e melão? | catálogo MapBiomas |
| A cobertura do SISAGUA correlaciona com a dose? | SISAGUA |
| A PAM 2010–2014 é comparável? | metodologia IBGE — insumo da D4 |

⚠️ **Um item é mais grave que os outros.** O art. 29 da Lei 12.228/1993 autoriza
municípios a legislar supletivamente, e **Limoeiro do Norte teria proibido a
pulverização aérea em 2009** — dez anos antes, e é um dos três municípios de alta
exposição de Rigotto. Se procede, há unidades **já tratadas** dentro do grupo de
dose alta, e 2015–2018 deixa de ser pré-tratamento para todos. Contamina a
própria medida de dose.

### Duas coisas da literatura que valem para o enquadramento

**O ban proíbe método, não molécula — e o químico não é o glifosato.** A tabela do
Dossiê ABRASCO no PL 18/2015 (23 pontos, Chapada do Apodi, 2009) mostra
**procimidona e carbaril em 23/23, carbofurano em 18/23, fenitrotiona em 16/23 — e
glifosato em 4/23**. Fungicida em banana, por avião. Logo o template de Dias,
Rocha & Soares (soja TH + glifosato) **não transfere quimicamente**, e a receita
GAEZ de Reynier & Rubin é construída sobre culturas **GM** — banana não é.

**O efeito se concentra na cauda alta.** Larsen et al. (2017) acham efeitos de
5–9% **apenas no top 5%** da exposição. Reforça a hipótese de limiar — e aperta o
problema: efeito só na cauda, suporte fino na cauda.

---

## 5. O que está travado, e em quem

| O quê | Em quem | Prazo |
|---|---|---|
| **Preencher `docs/pre-especificacao.md`** | **vocês dois** | ⛔ trava `make real` |
| **Pedido LAI à SEMACE** | **você** — minuta pronta | 20 dias + 10. Único com relógio externo |
| **Liberar a rede do ambiente** | **você** | IBGE, DATASUS, Base dos Dados, FAO |
| Verificar Marx-Stoelting et al. (2025) | citação não conferida | ⚠️ *Science* não está em nenhuma base alcançável daqui |

O pedido LAI mata dois coelhos: serve ao *enforcement* (D6) **e** ao `d = 0`
operacional — o art. 8º da Lei 12.228/1993 obriga prestadoras de aplicação a se
registrarem na SEMACE.

---

## 6. Cronograma até a qualificação

```
E0   antecipação + bans municipais < 2019   ⚠️ pendente
E1   data e janela                          ✅ fechada
E1.5 DP das tendências (SINASC)             ⚠️ o gate que decide o ensaio
E2   variação de dose (PAM) — Gate 1        ⬜ espera rede
E3   escolha de especificação               ⬜ depende de D1
E4   grupo d = 0 e contaminação             ⬜ depende de D3
E5   painel                                 ✅ instrumentado
E6   estimação (contdid)                    ✅ instrumentado
E7   robustez e inferência                  ✅ instrumentado
E8   texto da qualificação                  ⬜
```

**A escada de especificação**, que E3 aplica e o script já calcula:

| Municípios com dose > 0 | Especificação |
|---|---|
| ≥ 40, suporte espalhado | curva não-paramétrica (sieve) |
| 15 a 39 | faixas discretas, indicadores múltiplos |
| 12 a 14 | faixas discretas — **suporte fino** |
| < 12 | binário sob Assumption 4-Agg; curva abandonada |

Descer um degrau não é fracasso. Descer sem registrar, é.

---

## Resumo de uma linha

**O código está pronto e os dados não chegaram — e essa folga é exatamente a
janela para escrever o que conta como resultado antes de ver o primeiro
coeficiente. É a única coisa desta lista que fica impossível depois.**
