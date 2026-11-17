# Pré-especificação do Ensaio 1 — versão 2 (desenho de fronteira)

**Status:** 🟡 **RASCUNHO** · aberta em 2026-11-16 · fecha com a assinatura do
pesquisador depois da conversa com o orientador.

<!-- PRESPEC_V2_STATUS: RASCUNHO -->

A `pre-especificacao.md` (fechada em 2026-09-21) continua valendo para o
desenho de dose, que agora é apêndice, e continua sendo o que o `make real`
confere. Este arquivo é o plano do desenho novo. Enquanto estiver em rascunho,
**nenhum desfecho pós-2019 do recorte tratado × controle é olhado**.

---

## 0. O que já se sabia ao escrever

Declarar isso é o que separa plano de racionalização.

| já visto | onde | é resultado do desenho novo? |
|---|---|---|
| Estimativas do desenho **antigo** (dose, só Ceará, 2015–2022), inclusive um ATT agregado de −36 g | `paper/secoes/06`, `docs/ars/17` | não: outro tratamento, outro grupo de comparação, sem o RN. Mas é desfecho pós-2019 do Ceará, e foi visto |
| Série **estadual** de banana, CE e RN, 2010–2024 | `leituras-segunda-rodada.md` §5 | não: agregado estadual |
| Área, produção e exportação de banana de Limoeiro + Quixeré, 2017–2020 | nota de Cavalcante (2022), pública | **em parte**: é desfecho econômico pós-2019 de dois tratados, sem o controle |
| Linha de base do avião por município, 2006 | script 18 | não: pré-período |
| Nenhum dado de nascimento, óbito fetal ou intoxicação do Rio Grande do Norte foi baixado | — | — |

Consequência: o desfecho primário (peso ao nascer, CE × RN) é plano genuíno. Os
desfechos econômicos não são cegos, e o texto dirá isso.

---

## 1. Fixado pelo pesquisador em 2026-11-16

**Caminho-alvo.** lei → menos avião → menos deriva → melhor nascimento.

**Especificação principal.**

| elemento | escolha |
|---|---|
| estimador | Callaway & Sant'Anna (2021), pacote `did` |
| coorte | uma: 2019 |
| tratados | municípios cearenses da Chapada do Apodi |
| comparação | municípios potiguares da Chapada, como nunca tratados |
| estimação | duplamente robusta, com covariáveis de linha de base |
| peso | número de nascimentos da célula |
| desfecho primário | peso ao nascer (g), município de residência da mãe |

**Previsão de forma, registrada antes de estimar.** A lei entra em vigor em
09/01/2019. O efeito deve **crescer ao longo de 2019**, à medida que as
gestações passam a ocorrer inteiras sob a lei, e estabilizar a partir das
concepções de 2019. Um efeito que apareça inteiro em janeiro de 2019, ou que
não tenha essa rampa, conta contra a leitura causal.

**Substituição.** O segundo caminho do grafo é a troca de tecnologia de
aplicação, do avião para a aplicação terrestre e para o drone. Mede-se ao lado
do desfecho principal (§3).

---

## 2. A fechar antes da assinatura

| # | item | proposta | quem decide |
|---|---|---|---|
| 1 | Lista de tratados | núcleo: Limoeiro do Norte e Quixeré (os dois com avião medido em 2006). Versão ampla: + Russas e os demais cearenses da Chapada | pesquisador |
| 2 | Lista de controles | os 21 potiguares da RIDE (`RIDE_CHAPADA_RN`, script 15). Sensibilidade sem os colados à divisa | pesquisador |
| 3 | Janela | pré desde 2005 (ou o primeiro ano disponível nos dois estados); pós até 19/12/2024 | orientador |
| 4 | Período de base e antecipação | base anterior ao PL de 02/2015 | orientador |
| 5 | Unidade de tempo do estudo de evento | trimestre de nascimento (o mês é ralo com dois municípios); a rampa de 2019 se lê em trimestres | pesquisador |
| 6 | Covariáveis de linha de base | população e urbanização (Censo 2010); participação da agricultura não familiar (Censo Agro 2017) | pesquisador |
| 7 | Desfechos secundários e correção | baixo peso, duração da gestação, prematuridade, óbito fetal, razão de sexos, número de nascimentos; Holm | pesquisador |
| 8 | Os dois cenários do primeiro estágio | ⚠️ **Revisto em 2026-11-17 (decisão do pesquisador, após o parecer do refine.ink):** 2019 é a única avaliação da lei e estima o efeito total municipal, haja ou não voo até 2018. Se os registros, com cobertura suficiente, documentarem cessação anterior sem retomada, não havia aplicação aérea em curso para a lei interromper; a interrupção anterior pode motivar **estudo complementar, com identificação própria**, que não substitui a avaliação da lei. Critérios de cobertura e classificação voo / sem voo / sem registro: Apêndice B.1 do projeto. (Redação anterior: "o contraste principal passa a ser o de 2012".) | orientador |
| 9 | Robustez | diferença tripla dentro de cada estado; calendário (quadra chuvosa); SDID | orientador |
| 10 | Inferência | permutação entre municípios de controle; Conley & Taber; Ferman & Pinto | pesquisador |

---

## 3. Como se mede a substituição de tecnologia

O que se quer saber: quando o avião sai, o que entra no lugar, e com que
exposição. No Ceará, entre 2019 e 19/12/2024, a lei vedava também o drone, de
modo que **dentro da janela a substituição cearense é para a aplicação
terrestre**. O drone entra de dois modos: no lado potiguar, onde é permitido
pela regra federal (o repositório registra uso a partir de ~2021; ⬜ conferir a
norma e a data), e no Ceará depois da Lei 19.135/2024, fora da janela.

| o que mede | fonte | o que dá | estado |
|---|---|---|---|
| Linha de base do equipamento | Censo Agro 2006, tabelas 1008 e 2069 | estabelecimentos por costal, tração mecânica e aeronave, por tipo de agricultura | ✅ script 18. O Censo 2017 não repetiu a pergunta |
| Modalidade de aplicação receitada | receituário agronômico, ADAGRI (Decreto 4.074/2002, art. 66) | terrestre × aérea, por receita, antes e depois de 2019 | ⬜ LAI minutada. **É a medida direta da troca** |
| Voos e área aplicada | relatórios mensais ao MAPA (IN 2/2008) | aérea tripulada, por município e mês, CE e RN | ⬜ LAI minutada |
| Operadores de drone | SIPEAGRO/MAPA | registro de operadores; no arquivo do CE, 100 de 107 são drones. Retrato do presente, sem data | ✅ baixado para o CE; ⬜ RN; ⬜ ver se há data de registro em outra tabela |
| Custo por hectare de cada tecnologia | planilhas da Conab (script 12) | item "operação com avião" × "trator", série 2008–2025 | ✅ |
| Volume de calda e mão de obra | depoimentos de produtores; RAIS (vínculos e ocupações na cultura da banana) | de 25 L/ha por avião para 250–300 L/ha manual; mais aplicadores | imprensa lida; RAIS ⬜ |
| Exposição ocupacional | SINAN, intoxicação **não intencional** por agrotóxico agrícola, circunstância ocupacional; SIH | sobe se a troca expõe mais trabalhadores | CE ✅; RN ⬜ |

**Previsões, registradas antes de estimar.**

- Se a substituição foi para a aplicação terrestre, a intoxicação ocupacional
  **não cai** e pode subir no lado cearense depois de 2019, enquanto os
  desfechos de nascimento melhoram ou ficam estáveis.
- Se o lado potiguar adota drone a partir de ~2021, o controle muda de
  tecnologia no meio do pós-período. A especificação com pós até 2021 é a que
  não sofre com isso, e fica registrada como a sensibilidade que decide.
- O drone, quando entrar no Ceará (2025 em diante), é um terceiro regime: aéreo
  de baixa deriva. Fica fora deste ensaio e é a extensão natural.

⚠️ O SINAN mede notificação, que depende de vigilância e hospital. A leitura do
terceiro item exige conferir no CNES se a capacidade de notificação evolui
igual nos dois lados, e usa a tentativa de suicídio como placebo.

---

## 4. O que conta como resultado

- O intervalo de confiança decide. O efeito mínimo detectável é de planejamento
  e não rebaixa depois um intervalo que exclui o zero, nem promove um que o
  inclui.
- O efeito esperado na média municipal é de 1 a 2 gramas
  (`leituras-segunda-rodada.md` §4.3). Um intervalo que inclua o zero e exclua,
  por exemplo, efeitos maiores que 20 gramas é um resultado: diz que a lei não
  produziu melhora grande na média, e não diz que não protegeu quem morava ao
  lado do bananal.
- Um resultado nulo no contraste de 2019 só se interpreta junto com o primeiro
  estágio: se o avião já não voava, é o esperado.
