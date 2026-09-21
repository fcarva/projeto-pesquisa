# Anexo técnico — as tabelas de dados e o desenho DiD

*Ensaio 1, proibição da pulverização aérea no Ceará. Documento para a reunião de
orientação. PPGEco/UFES, 2026-09-21.*

> **O que este documento é, e o que não é.** Ele responde duas perguntas: **quais
> tabelas este projeto tem** e **qual DiD ele roda**. É anexo técnico —
> complementa o briefing de decisões (`docs/ars/08-briefing-orientador.md`) e a
> justificativa, não os substitui.
>
> ⚠️ **Não há dado real, e portanto não há resultado.** O que está aqui é de dois
> tipos, e a diferença importa:
>
> | | Estatuto |
> |---|---|
> | **Esquema** das tabelas — colunas, grão, o que cada uma mede | real, lido dos arquivos |
> | **Aritmética de desenho** — MDE, 0,70 × MDE, as 31 séries | real; é cálculo, não estimativa |
> | Valores estimados | **ausentes de propósito** |
>
> **Nenhum número simulado foi incluído**, nem rotulado como tal. O pipeline já
> roda de ponta a ponta contra dado sintético, mas número simulado que circula
> num PDF perde o rótulo no primeiro print de tela.

---

# Parte A — os dados

## A1. As seis fontes, e o que já se sabe sobre cada uma

| Base | Recorte | Rota | Vintage |
|---|---|---|---|
| **PAM/IBGE** (tab. 1612, 1613) | CE, municípios, 2015–2018 | API SIDRA, ou CSV do portal | — |
| **SINASC** | CE, 2015–2022 | `pysus`, ou `datazoom.saude` (R) | — |
| **SIM — DO/DOFET** (óbito fetal) | CE, 2015–2022 | idem | — |
| **SIH — AIH reduzida** | CE, 2015–2022 | **só** `datazoom.saude` (R) | — |
| **SISAGUA** | CE | Base dos Dados / MS | — |
| **FAO-GAEZ** | CE | raster GeoTIFF | — |

**A coluna de vintage está vazia nas seis linhas, e isso é o conteúdo da tabela,
não uma omissão.** Sem registrar qual extração foi usada, o resultado não é
reproduzível: a mesma consulta ao SIDRA ou ao DATASUS devolve números diferentes
conforme a revisão da base.

Três armadilhas de extração já mapeadas, que custam tempo se descobertas depois:

- **Óbito fetal não é arquivo separado no SIM moderno.** Vem dentro do DO,
  identificado por `TIPOBITO` (1 = fetal, 2 = não fetal). Mas a rota `datazoom`
  entrega o **DOFET**, que pode **não trazer** `TIPOBITO` — e aí o filtro
  descartaria tudo. Um painel vazio de óbito fetal *parece* o resultado benigno
  do teste de seleção. O script detecta e anuncia.
- **A subnotificação de óbito fetal é heterogênea entre municípios.** O limiar de
  notificação compulsória é ≥ 22 semanas **ou** ≥ 500 g (é "ou", não "e"); abaixo
  disso o registro varia por município e por ano. Como é justamente a variação
  entre municípios que identifica o efeito, isso é confundidor, não ruído. O
  script emite a série restrita ao lado do total: **se divergirem, a divergência
  é o achado.**
- **Os formatos de data divergem entre bases.** `DTNASC` do SINASC é DDMMAAAA;
  `DT_INTER` do SIH é AAAAMMDD. Lido na ordem errada, o mês sai trocado — e num
  painel mensal cujo tratamento entra em janeiro de 2019, mês trocado é
  contaminação da janela do evento.

## A2. As quatro tabelas que o pipeline produz

Grão comum: **município × ano-mês**, chave `cod_ibge6`.

| Tabela | Colunas | O que mede |
|---|---|---|
| `nascimentos_ce_muni_mes` | 17 | peso ao nascer, baixo peso, prematuridade, idade materna |
| `obitos_fetais_ce_muni_mes` | 19 | óbito fetal total e restrito a ≥ 22 sem, com denominador |
| `intoxicacao_ce_muni_mes` | 24 | internação por intoxicação, separada por intenção e por família química |
| **`painel_ensaio1`** | **65** | as três acima + dose + exposição gestacional |

Das 65 colunas do painel, **13 são de tratamento e exposição**: `dose_ha`,
`dose`, `dose_zero`, `t`, `share_gestacao_pos_ban`, os três `share_tri*_pos_ban`,
`pos_ban_nascimento`, `evento_meses`, `pos_noticia`, `pos_certeza` e
`cultura_ancora`.

**Por que existem duas marcações de pós-ban, e não uma.** A exposição
gestacional é retroprojetada com janela **fixa de nove meses** — e não pela
gestação observada, que seria endógena, já que prematuridade é um dos desfechos.
O tratamento não liga de uma vez em janeiro de 2019: sobe ao longo de nove meses.

| Coorte de nascimento | Fração da gestação pós-ban | Marcação ingênua |
|---|---|---|
| dez/2018 | 0,00 | 0 |
| **jan/2019** | **0,00** | **1** ← o ingênuo diz tratado; a gestação foi toda antes |
| mai/2019 | 0,44 | 1 |
| out/2019 | 1,00 | 1 |

Em 2019 a marcação ingênua conta 12 coortes tratadas onde a exposição real soma
**7** — superconta 5/12, com direção de viés conhecida (atenuação). As duas
construções saem lado a lado: `pos_ban_nascimento` existe para **medir** a
atenuação, não para ser o tratamento.

## A3. As 31 séries candidatas a desfecho

Conferidas contra o esquema do painel, uma a uma.

| Fonte | N | Séries |
|---|---|---|
| **SINASC** | 6 | `peso_medio`, `taxa_baixo_peso`, `taxa_prematuridade`, `n_baixo_peso`, `n_prematuro`, `idade_mae_media` |
| **SIM** (óbito fetal) | 6 | `n_obito_fetal`, `n_obito_fetal_22sem`, as duas taxas correspondentes, `peso_medio_fetal`, `semanas_media` |
| **SIH** (intoxicação) | 19 | `n_internacoes_com_cid`; quatro famílias de intenção × 2 campos; quatro recortes T60 × 2; mais `n_acidental_idade_trabalho` e `n_acidental_obito` |
| | **31** | |

Somadas três janelas de exposição por trimestre, quatro construções do grupo de
dose zero e dois parâmetros-alvo, **o espaço de especificação passa de mil**.

⚠️ **Duas dessas séries não são desfecho, e precisam estar declaradas como tal
antes do primeiro dado.**

| Série | Papel | Previsão da hipótese |
|---|---|---|
| `n_acidental` (**X48**) | canal de substituição | **move** — proibido o avião, a aplicação migra para trator e costal, e o veneno se aproxima do aplicador |
| `n_autoprovocada` (**X68**) | **falsificação** | **não move** — o ban muda *como* se aplica, não *o que* está disponível |

Mesma população, mesmo sistema de registro, mesmos municípios, sinais previstos
opostos. **Se as duas se moverem juntas, a explicação não é substituição de
método** — é algo que move internação em geral.

## A4. A matriz de degradação — o que sobrevive sem cada fonte

Esta é a tabela de prioridade: transforma "faltam seis fontes" numa decisão sobre
o que perseguir com tempo limitado.

| Sem esta fonte | O que ainda sai | O que **não** sai |
|---|---|---|
| **FAO-GAEZ** | a curva, com nível **sem banda** | o instrumento; 3 das 4 definições de zero; o teste de contaminação. ⚠️ **O nível da curva vira indefensável** |
| **Bans municipais < 2019** | tudo, aparentemente | a garantia de que 2015–2018 é pré-tratamento. ⚠️ **Falha silenciosa: o resultado sai e está errado** |
| SEMACE / ANAC | tudo, com o estimando renomeado | a definição 3 de zero — a única que mede **método**; a verificação de *enforcement* |
| ANA + SISAGUA | o Ensaio 1 inteiro | o canal-água; o mecanismo fica postulado, não medido |
| MapBiomas | tudo | melhoria da medida de dose |
| INMET / FUNCEME | tudo | vento a favor/contra — o teste que separa deriva de confundidor |
| População municipal | as contagens de intoxicação | as taxas, e a comparação entre municípios de porte diferente |

**Duas linhas têm consequência qualitativamente diferente das outras.** O
**GAEZ**, porque tira a banda de incerteza do resultado principal. E os **bans
municipais**, porque a falha é silenciosa: o pipeline roda, o número sai, e está
errado sem nada acusar. As demais degradam o escopo, não a validade.

## A5. O que falta liberar de acesso

| Domínio | Serve a | Etapa |
|---|---|---|
| `apisidra.ibge.gov.br` | valores do SIDRA (PAM) | **Gate 1** |
| `servicodados.ibge.gov.br` | metadados do SIDRA — o preflight | **Gate 1** |
| `ftp.datasus.gov.br` | SINASC e SIM | E1.5 |
| `basedosdados.org` | rota alternativa | A1, A3 |
| `gaez.fao.org` | raster de aptidão | A2 |

Enquanto não abrirem, os scripts aceitam arquivo baixado à mão. O primeiro
comando a rodar quando abrir é o **preflight** — ele confere os códigos de
variável do SIDRA contra a API de metadados, porque um código errado faz o SIDRA
devolver **vazio, não erro**.

---

# Parte B — o desenho DiD

## B1. O parâmetro-alvo, e o que cada um custa

O tratamento é **contínuo** (intensidade de exposição pré-ban), e a proibição é
**estadual e simultânea** — não escalonada.

| Parâmetro | O que é | Hipótese que exige | Testável? |
|---|---|---|---|
| `ATT(d\|d)` | efeito **no nível** de dose *d* | paralelismo tradicional | parcialmente, por pré-tendências |
| **`ATE(d)` / `ACR(d)`** | a **curva** e sua inclinação | *strong parallel trends* | ⚠️ **não** |

A hipótese forte restringe trajetórias sob doses **não recebidas** — daí não ser
testável. E o placebo de pré-tendências fala da hipótese fraca, não da forte.

> **Por que a curva, apesar do preço.** Weitzman decide preço contra quantidade
> pela **inclinação relativa** do dano marginal — isto é, por `ACR(d)`, a
> derivada. O Ensaio 2 consome a curva. Um Ensaio 1 que recue para o efeito num
> ponto deixa o Ensaio 2 sem âncora. **É decisão de arquitetura da dissertação,
> não de gosto econométrico.**

## B2. Três restrições do estimador, conferidas no código

Verificadas contra `R/cont_did.R` do `contdid` v0.1.1 — não supostas.

| Restrição | Consequência para o desenho |
|---|---|
| O sieve exige **exatamente dois períodos** | a curva **não roda no painel mensal**; exige colapso pré/pós, e o "pré" vira média única de 2015–2018 |
| **Sem event study** no sieve | os *leads* saem de **outro estimador** que a curva — duas rodadas, e o texto tem de dizer isso |
| **Covariáveis não suportadas** | ajuste municipal só por fora do estimador |

⚠️ **A tensão que isso produz.** O PL foi apresentado em 24/02/2015 — a janela
pré-ban começa **depois** do marco de notícia. Com o pré colapsado numa média
única, **a contaminação por antecipação fica invisível dentro da especificação
principal.** O event study existe, mas valida um objeto vizinho, não a curva.

## B3. O grupo de comparação — quatro construções, todas reportadas

O zero da PAM é zero de *proxy* (área nula), não zero de tratamento.

1. área nula da cultura-âncora;
2. área nula de qualquer cultura candidata a aplicação aérea;
3. ausência de operador aeroagrícola registrado — **a única que mede método**;
4. baixa aptidão agroclimática (GAEZ).

> **Por que a dispersão entre elas é o número, e não uma nota de rodapé.** O
> estimador centra a curva na variação média do grupo de dose nula:
> `m0 <- mean(dy[dose == 0])`. Trocar quem compõe esse grupo **não adiciona
> ruído: desloca o nível da curva inteira.** A escolha do zero é aritmética do
> estimador.

Duas contaminações conhecidas do zero: o §2º do art. 28-B alcança **dispersão
aérea para controle vetorial** — município sem agricultura pulverizada mas com
controle aéreo de endemias **é tratado**, e esses tendem a ser os maiores, logo a
contaminação correlaciona com porte, que correlaciona com desfecho. E as
proibições municipais anteriores a 2019.

## B4. A escada de especificação

O diagnóstico de dose **recomenda** o degrau; o pesquisador ratifica.

| Municípios com dose > 0 | Especificação |
|---|---|
| ≥ 40, suporte espalhado | curva não-paramétrica (sieve) |
| 15 a 39 | faixas discretas, indicadores múltiplos |
| 12 a 14 | faixas discretas — **suporte fino** |
| < 12 | binário; curva abandonada |

**Descer um degrau não é fracasso. Descer sem registrar, é.**

## B5. As três inferências — e por que são três

| Procedimento | Supõe | Como ler |
|---|---|---|
| cluster-robusto ingênuo | assintótico no nº de clusters | **linha de base a desmentir**, não resultado |
| wild cluster bootstrap | idem, pesos de Rademacher | ⚠️ **sub-rejeita** com poucos tratados: p alto informa, p baixo não absolve |
| **inferência por aleatorização** | nada — permuta a dose | o mais duro, e o mais difícil de contestar |

> **O achado é a distância entre elas.** Se a ingênua der p = 0,01 e a
> aleatorização der p = 0,31, o resultado não é "significante": é **"o desenho
> não distingue"**. O script emite os três lado a lado e avisa quando a razão
> passa de 3×.

*Nota de nomenclatura:* Conley–Taber (2011) tratam tratamento **binário**. Aqui o
tratamento é contínuo, e a adaptação fiel é permutar a dose. A lógica é a mesma;
o procedimento, não. O script chama de "inferência por aleatorização".

## B6. Poder, e o que conta como resultado negativo

Efeito esperado: **15 a 25 g** sobre o peso médio ao nascer. Referência de
magnitude na literatura: 23 a 32 g.

A meia-largura do intervalo de confiança é **0,70 × MDE**. Logo o desenho
**falsifica 15 g sempre que o MDE ficar abaixo de 21,4 g**:

| Municípios tratados | DP das tendências 10 g | 18 g | 20 g | 30 g |
|---|---|---|---|---|
| 3 | ±11,4 ✔ | ±20,5 ✘ | ±22,8 ✘ | ±34,2 ✘ |
| 5 | ±8,9 ✔ | ±16,0 ✘ | ±17,8 ✘ | ±26,7 ✘ |
| **10** | ±6,4 ✔ | **±11,5 ✔** | ±12,7 ✔ | ±19,1 ✘ |
| 20 | ±4,6 ✔ | ±8,4 ✔ | ±9,3 ✔ | ±13,9 ✔ |

⚠️ **O piso amostral de ruído já é ≈ 17,7 g**, sem nenhuma heterogeneidade real.
A coluna de 20 g é aproximadamente o melhor caso.

**Duas consequências.** O alvo é **dez** municípios tratados, não três — e a
saída, se o poder não fechar, é **baixar o corte de dose** para encorpar o grupo
tratado, não trocar de desfecho: peso médio é o único com razão efeito/ruído
acima de 1 (1,30–1,81, contra 0,44–0,80 para baixo peso e 0,17 para
mortalidade).

**E por isso um nulo é entregável declarado**, não fracasso: um nulo cujo
intervalo exclui o efeito esperado é evidência contra o efeito. Sem a
pré-especificação escrita antes do dado, porém, é só silêncio — daí a execução
contra dado real estar travada por portão automático até que ela seja preenchida,
datada e **commitada**. O commit é o carimbo de tempo.

## B7. A camada de robustez — e o que não se aplica

**Entram**, preenchendo lacunas declaradas:

| Pacote | Preenche |
|---|---|
| `pretrends` (Roth) | **poder do teste de pré-tendências** — num desenho com poder curto, um placebo que "passa" pode passar por falta de poder, não por ausência de violação |
| `HonestDiD` (Rambachan & Roth) | sensibilidade a violações de tendências paralelas |
| `synthdid` (Arkhangelsky et al.) | o SDID agregado; aguenta uma única unidade tratada |

*Ressalva:* os dois primeiros operam sobre coeficientes de **event study** — que,
pela restrição B2, saem de estimador diferente do que produz a curva. A
sensibilidade que entregam é sobre o objeto vizinho.

⚠️ **Não se aplica**: a maquinaria de DiD **escalonado** — decomposição de
Goodman-Bacon, `did`, `staggered`, diagnósticos de pesos do TWFE. Ela pressupõe
variação de *timing*, e aqui os 184 municípios são alcançados no mesmo dia.

**O risco não é ela falhar; é ela não falhar.** Rodada neste painel, produz event
study e decomposição de boa aparência, e tudo está errado para o desenho. Saída
plausível e errada é pior que erro: erro se conserta, plausível se defende.

---

*Proveniência: esquemas lidos dos arquivos do pipeline; restrições do estimador
conferidas contra o código-fonte do autor do pacote; cronologia legal contra o
texto oficial em `docs/legislacao/`. A aritmética de poder é cálculo do próprio
desenho. **Nenhum coeficiente estimado consta deste documento.***
