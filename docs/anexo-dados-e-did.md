# Anexo técnico — as tabelas de dados e o desenho DiD

*Ensaio 1, proibição da pulverização aérea no Ceará. Documento para a reunião de
orientação. PPGEco/UFES, 2026-09-21, com os dados de 2026-08-25.*

> **O que mudou desde a última conversa.** As bases foram adquiridas e os dois
> gates rodaram contra dado real. O **Gate E2 passa** — há variação de dose, e a
> cultura-âncora **não é o melão**. O **Gate E1.5 reprova como especificado**, e
> a razão da reprovação tem conserto possível — mas o conserto é uma decisão
> metodológica que é sua e do orientador, não do script.
>
> ⚠️ **Ainda não há estimativa de efeito.** Nenhum coeficiente foi produzido, e
> não deve ser antes da pré-especificação e da decisão da §B5.

---

# Parte A — os dados

## A1. As fontes, agora com vintage

| Base | Recorte | Extração | Volume |
|---|---|---|---|
| **PAM/IBGE** (tab. 1612, 1613) | CE, municípios, 2015–2018 | ✅ 2026-08-25 | preflight 4/4 códigos conferidos na API |
| **SINASC** | CE, 2015–2022 | ✅ 2026-08-25 | **1.001.709 nascimentos** |
| **SIM — DOFET** | CE, 2015–2022 | ✅ 2026-08-25 | **11.240 óbitos fetais** |
| **SIH — AIH reduzida** | CE, 2015–2022 | ✅ 2026-08-25 | ~3,9 mi de AIH — ⚠️ ver A4 |
| **Painel E5** | 184 municípios × 96 meses | ✅ 2026-08-25 | 17.664 células × 65 colunas |
| SISAGUA, FAO-GAEZ, ANA, IBAMA | — | ⬜ não adquiridas | — |

⚠️ **Uma correção de diagnóstico que vale registrar:** a rede nunca foi problema
do projeto — era política do proxy da sessão remota. Na máquina local, SIDRA,
DATASUS e IBGE respondem normalmente. O que falta é download manual (raster do
GAEZ, shapefiles da ANA), não liberação de acesso.

## A2. O painel do SINASC — as descritivas reais

| | |
|---|---|
| nascimentos, pós-limpeza | 1.001.709 |
| municípios | 184 |
| células município-mês | 17.654 |
| **peso médio** | **3.211 g** |
| baixo peso (< 2500 g) | 8,34% |
| prematuridade (< 37 sem) | 12,58% |
| peso ausente | 0,01% |
| células com < 5 nascimentos | 2,6% |

As taxas batem com a ordem de grandeza nacional — o teste de sanidade disponível
sem validação externa.

## A3. Os canais: um morreu, e há substituto

⚠️ **O canal de intoxicação aguda (SIH) não existe.** Com a série de oito anos
completa:

| SIH/CE, 2015–2022 | |
|---|---|
| AIH baixadas | ~3,9 milhões |
| internações com CID de agrotóxico | **50** |
| **acidental (X48)** — o canal de substituição | **1** |
| **autoprovocada (X68)** — o placebo | **1** |
| células com < 5 internações | 100% |

**Não se conserta com agregação — não há o que agregar.** E o placebo morre
junto: o desenho depende de contrastar X48 com X68, e com um evento de cada lado
o contraste não existe. A razão é estrutural: SIH é **internação faturada**, e
intoxicação aguda costuma ser atendida em emergência sem internar.

✅ **Há uma fonte melhor, e é a que existe para exatamente isto.** O SINAN/IEXO —
Intoxicação Exógena, notificação compulsória:

| fonte | eventos no Ceará |
|---|---|
| SIH, **oito anos** | 50 — dos quais **1** acidental |
| **SINAN/IEXO**, **um ano** (2015) | **2.914** — dos quais **266** de agrotóxico agrícola |

Um único ano do SINAN entrega ~58× mais eventos que oito anos de SIH. Os códigos
de `AGENTE_TOX` já foram conferidos contra a nota técnica do Ministério da Saúde
(02 = agrícola; **04 = saúde pública**, que é o §2º do art. 28-B). O ingestor
ainda não foi escrito.

## A4. ⚠️ A janela não fecha em 2024

O SINASC definitivo para em **2022** no FTP do DATASUS; 2023 e 2024 não existem,
nem preliminares. Os preliminares disponíveis são de 2025–2026 — posteriores à
exceção de drones (19/12/2024), e contaminam justamente o que o corte da janela
protege.

**Consequência: o pós-ban efetivo do desfecho principal é 2019–2022**, não
2019–2024. Antes de dar a janela por fechada, conferir a Base dos Dados
(BigQuery), que é a rota alternativa já prevista.

## A5. A matriz de degradação — o que ainda falta

| Sem esta fonte | O que ainda sai | O que **não** sai |
|---|---|---|
| **FAO-GAEZ** | a curva, com nível **sem banda** | o instrumento; 3 das 4 definições de zero; o teste de contaminação. ⚠️ **O nível da curva vira indefensável** |
| **Bans municipais < 2019** | tudo, aparentemente | a garantia de que 2015–2018 é pré-tratamento. ⚠️ **Falha silenciosa: o resultado sai e está errado** |
| SEMACE / ANAC | tudo, com o estimando renomeado | a definição 3 de zero — a única que mede **método** |
| ANA + SISAGUA | o Ensaio 1 inteiro | o canal-água; o mecanismo fica postulado |
| INMET / FUNCEME | tudo | vento a favor/contra |

As bibliotecas geo **estão** instaladas na máquina local — falta o raster, não a
biblioteca. Dos itens acima, os **bans municipais** continuam sendo o único cuja
ausência produz resultado errado sem nada acusar, e o único que não depende de
download nenhum.

---

# Parte B — o desenho DiD, e a decisão que ele força

## B1. ✅ Gate E2 passa — e responde à flag 1

Há dispersão de dose utilizável, com sobra para a curva não-paramétrica. Mas a
cultura-âncora **não é a que o material de projeto supunha**:

| cultura | municípios c/ área > 0 | Gini | % área no decil sup. | especificação |
|---|---|---|---|---|
| **Banana (cacho)** | **169** | **0,86** | **78%** | **curva** |
| Coco-da-baía | 165 | 0,92 | 91% | curva |
| Castanha de caju | 170 | 0,84 | 70% | curva |
| Milho, Feijão | 184 | 0,49–0,51 | 35–37% | curva |
| **Algodão herbáceo** | **28** | 0,96 | 65% | faixas discretas |
| **Melão** | **10** | 0,98 | 35% | ⚠️ **binário — curva abandonada** |

**Melão e algodão estão empiricamente descartados para a curva** — 10 e 28
municípios. A **banana** tem 169, Gini 0,86 e 78% da área no decil superior:
dispersão alta *com* suporte largo, que é a combinação que a curva exige.

E ela casa com a química documentada: **procimidona é fungicida de bananal**, e
é o princípio ativo que aparece em 23 de 23 amostras do Dossiê ABRASCO. Milho e
feijão têm suporte largo mas Gini baixo — lavoura espalhada, não alvo de avião.

*A decisão de ratificar a âncora continua sua; o script recomenda e não escolhe.*

## B2. ⚠️ Gate E1.5 reprova como especificado

A DP das tendências municipais de peso ao nascer, como o script a calcula (não
ponderada), é **47,5 g** — contra o piso de ~17,7 g que o roteiro previa, e que
tratava 20 g como "aproximadamente o melhor caso". O observado é **2,7× o piso**.

| cultura | tratados | MDE agrupado | falsifica 15 g? |
|---|---|---|---|
| Banana | 17 | 33,8 g | ✘ |
| Milho / Feijão | 19 | 32,2 g | ✘ |
| Algodão | 3 | 77,4 g | ✘ |
| Melão | 1 | 133,2 g | ✘ |

**✘ nas 18 culturas.** Com o efeito esperado abaixo do MDE de todas elas, um
nulo seria **ilegível**: não distinguiria "o ban não funcionou" de "o desenho não
enxerga".

## B3. Mas 63% dessa dispersão é ruído de amostragem

Um script novo separa as duas componentes. A parte amostral é aritmética
conhecida, sem suposição:

| | |
|---|---|
| DP observada das variações | 46,9 g |
| componente de **ruído amostral** | 37,3 g |
| componente de **heterogeneidade** | **28,4 g** ← é esta que governa o MDE |
| fração da variância que é ruído | **63,3%** |

Por porte de município, a razão fica evidente:

| nascimentos/ano | n | DP observada | ruído esperado |
|---|---|---|---|
| < 150 | 32 | 68,2 g | 59,7 g |
| 150–300 | 65 | 49,7 g | 38,2 g |
| 300–800 | 57 | 39,4 g | 26,2 g |
| **≥ 800** | **30** | **17,9 g** | 15,8 g |

⚠️ **O estrato de ≥ 800 nascimentos/ano dá 17,9 g — praticamente o piso de
17,7 g do roteiro.** A conta do roteiro estava certa; o que ela não antecipou é
que a mediana municipal do Ceará é de **283 nascimentos/ano**, não 800. **A DP de
47,5 g não mede o mundo: mede municípios pequenos.**

## B4. O veredito se inverte para a banana — mas por pouco

| cultura | tratados | mediana nasc/ano | MDE (DP obs.) | MDE (DP real) | falsifica 15 g? |
|---|---|---|---|---|---|
| **Banana** | 17 | 403 | 33,4 g | **20,3 g** | **sim** |
| Manga, Coco, Caju | 17 | 408–937 | 33,4 g | 20,3 g | sim |
| Mamão | 11 | 595 | 40,8 g | 24,7 g | não |
| Algodão | 3 | 1.133 | 76,4 g | 46,3 g | não |

⚠️ **E a própria estimativa de 28,4 g é imprecisa.** A decomposição é
não-viesada, não precisa: IC 95% aproximado de **[18,9 ; 35,5] g**.

| cenário | DP real | MDE banana | meia-largura | falsifica 15 g? |
|---|---|---|---|---|
| piso do IC | 18,9 g | 13,5 g | 9,4 g | **sim, com folga** |
| ponto | 28,4 g | 20,3 g | 14,2 g | **sim, no limite** |
| teto do IC | 35,5 g | 25,3 g | 17,7 g | ⚠️ **não** |

**Leitura honesta: a inversão do gate é plausível, não estabelecida.** No ponto
estimado ela passa raspando — meia-largura de 14,2 g contra um piso de 15 g — e
no teto do intervalo não passa. Tratar 20,3 g como número firme repetiria, na
direção otimista, o mesmo erro que a DP não ponderada comete na pessimista.

## B5. ⛔ A decisão que é de vocês dois

Neutralizar o ruído **não acontece sozinho**. Três vias, nenhuma neutra:

| Via | O que faz | O que custa |
|---|---|---|
| **(a) Ponderar por nascimento** | encolhe o ruído sem descartar município | ⚠️ **muda o estimando** — o alvo passa a ser efeito por *criança*, não por *município*. Defensável, talvez até preferível para bem-estar, mas é mudança de parâmetro-alvo e o texto tem de declarar |
| **(b) Cortar por porte** | simples | ⚠️ **pode remover o grupo tratado.** Para a banana, só **3 de 17** municípios têm ≥ 800 nascimentos/ano. Corte em 800 destrói o desenho; corte em 150 preserva 15 de 17 |
| **(c) Aceitar e reportar como limite superior informativo** | não exige decisão metodológica nova | não entrega a precisão desejada — mas é o compromisso que o texto **já** declara |

Duas saídas independem de resolver a imprecisão: **baixar o corte de dose** para
encorpar o grupo tratado (a saída já ratificada para o E1.5) e **reportar como
limite superior**.

## B6. O estimador, e um bloqueio novo

O tratamento é **contínuo**; a proibição é **estadual e simultânea**.

| Parâmetro | Hipótese que exige | Testável? |
|---|---|---|
| `ATT(d&#124;d)` — efeito no nível | paralelismo tradicional | parcialmente |
| **`ATE(d)` / `ACR(d)`** — a curva e sua inclinação | *strong parallel trends* | ⚠️ **não** |

A curva é o resultado principal porque **Weitzman decide pela inclinação** — o
Ensaio 2 consome a derivada. É decisão de arquitetura da dissertação.

Três restrições do pacote, conferidas no código do autor: o estimador da curva
exige **exatamente dois períodos** (o pré vira média única de 2015–2018), **não
faz event study** (os *leads* saem de outro estimador) e **não aceita
covariáveis**.

⛔ **E um bloqueio que não estava mapeado: não há R instalado na máquina.** Sem R
+ `contdid` + `renv`, **não há estimação**, por mais limpo que o painel esteja.
É o primeiro item da lista de próximos passos.

## B7. A camada de robustez, e o que não se aplica

| Entra | Preenche |
|---|---|
| `pretrends` | **poder do teste de pré-tendências** — num desenho com poder curto, um placebo que "passa" pode passar por falta de poder, não por ausência de violação |
| `HonestDiD` | sensibilidade a violações de tendências paralelas |
| `synthdid` | o SDID agregado; aguenta uma única unidade tratada |

*Ressalva:* os dois primeiros operam sobre coeficientes de **event study** — que,
pela restrição acima, saem de estimador diferente do que produz a curva.

⚠️ **Não se aplica:** a maquinaria de DiD **escalonado** (decomposição de
Goodman-Bacon, `did`, `staggered`, diagnósticos de pesos do TWFE). Ela pressupõe
variação de *timing*, e aqui os 184 municípios são alcançados no mesmo dia.
Rodada neste painel, **não falha**: produz event study e decomposição de boa
aparência, e tudo está errado para o desenho. **Saída plausível e errada é pior
que erro: erro se conserta, plausível se defende.**

---

## Próximos passos, em ordem

1. ⛔ **Instalar R + `contdid`** — bloqueio da estimação.
2. **Decidir a via da §B5** e registrar com data, antes de estimar.
3. **Ratificar ou recusar a banana** como cultura-âncora.
4. **Levantar os bans municipais anteriores a 2019** — única lacuna que produz
   resultado errado em silêncio, e não depende de download.
5. **Decidir a fonte do canal de intoxicação**: SINAN/IEXO contra SIH.
6. **Conferir se a Base dos Dados tem SINASC 2023–2024**, que decide se a janela
   fecha em 2022 ou em 2024.

---

*Números de `docs/gates-resultados-dados-reais.md`, rodada de 2026-08-25.
Esquemas lidos dos arquivos do pipeline; restrições do estimador conferidas
contra o código-fonte do autor. **Nenhuma estimativa de efeito foi produzida.***
