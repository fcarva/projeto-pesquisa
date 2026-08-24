# Research Plan Summary — Ensaio 1

*ARS `deep-research`, modo `socratic`, fronteira de não-geração mantida.*
*Camadas 1, 2 e 3 fechadas; 4 aberta com as perguntas equipadas; 5 não iniciada.
Última atualização: 2026-08-24.*

Registro do diálogo socrático. Os `[INSIGHT: ...]` são **transcrições literais**
do pesquisador — não paráfrases minhas. O que não convergiu está listado como
aberto e **não foi preenchido**.

---

## Layer 1 — Enquadramento do problema (FECHADA, 1 rodada + convergência)

Pergunta de partida, do esboço: efeito causal do ban sobre desfechos de saúde ao
nascer, qualidade da água e atividade econômica agrícola. Provocação: se só
coubesse um aspecto, qual?

`[INSIGHT: Se eu tivesse que escolher apenas um aspecto: Desfechos de Saúde ao
Nascer (Saúde Perinatal). (...) Os outros dois aspectos (qualidade da água e
atividade agrícola) virariam canais e mecanismos secundários.]`

Três razões, nas palavras dele:

`[INSIGHT: o feto em gestação é o sujeito experimental perfeito para avaliar
externalidades ambientais agudas. Ele tem um histórico de exposição curto e
estritamente delimitado no tempo (9 meses), o que elimina o maior pesadelo das
regressões de saúde de adultos: o viés de histórico de residência e migração de
longo prazo.]`

`[INSIGHT: O SINASC e o SIM (DATASUS) oferecem um painel com cobertura
praticamente universal, diária e com georreferenciamento municipal impecável. Em
contrapartida, os dados de qualidade da água do SISAGUA sofrem com um volume
massivo de dados faltantes.]`

`[INSIGHT: a morte ou a perda de capacidade cognitiva de um recém-nascido é um
dano social irreversível. É onde a tese ganha o peso moral que pauta o debate de
mechanism design à la Zoë Hitzig.]`

Sobre o limite do antecedente local:

`[INSIGHT: o estudo de Rigotto et al. não prova causalidade. (...) os municípios
da Chapada do Apodi diferem dos municípios de controle em dezenas de variáveis
não observadas: renda média, hábitos de fumo, acesso a tratamento de média/alta
complexidade, saneamento básico e estrutura ocupacional.]`

`[INSIGHT: Rigotto et al. observam o município como uma caixa-preta. Sua tese
abrirá essa caixa usando dados físicos.]`

Sobre a contribuição (antecipa a L5, registrado aqui porque foi dito aqui): três
cadeiras nomeadas — ministro relator no STF (ADI 7794 e sucessoras), deputado
relator de CCJ estadual nos estados com projetos análogos, e a cadeira
reguladora ANVISA/MAPA que edita portarias sobre **método de aplicação**, não só
sobre molécula.

**Saída da L1:** desfecho primário = peso ao nascer e prematuridade (SINASC).
Água e produção rebaixadas a canal e a custo.

---

## Layer 2 — Reflexão metodológica (FECHADA, 2 rodadas + devil's advocate)

*Commitment gate L1→L2 pago espontaneamente:* usar a Lei 16.820/2019 como choque
exógeno de intensidade e estimar com o DiD contínuo de CGS.

### Rodada 1 — o que o pesquisador estabeleceu

`[INSIGHT: Esperamos uma curva com comportamento de limiar (threshold) ou
concavidade acentuada, onde os efeitos adversos na saúde humana se concentram na
cauda de alta exposição.]`

`[INSIGHT: o banimento da pulverização aérea gerará um benefício marginal
próximo a zero para a maioria dos municípios de baixa intensidade, mas um salto
de melhora drástico (desproporcional) nos municípios de alta intensidade.]`

`[INSIGHT: O estimador de CGS não impõe restrição de sinal.]` — resposta à
pergunta sobre detectar o efeito contrário ao esperado.

`[INSIGHT: O produtor, impedido de voar, migra para a aplicação terrestre
(tratores ou manual). Como a aplicação terrestre ocorre ao nível do solo, a
exposição direta do trabalhador agrícola e das residências coladas ao talhão
pode aumentar.]` — canal de substituição, a ser rastreado no SIH.

`[INSIGHT: O Aquífero Jandaíra é um aquífero cárstico (calcário). (...) o veneno
é essencialmente "injetado" de forma direta na água subterrânea.]` — resposta ao
problema de o template montante/jusante do DRS ser de água superficial.

`[INSIGHT: O "ponto de emissão" não será uma coordenada fictícia, mas sim a
borda desses polígonos de plantio intensivo.]` — resposta ao problema de fonte
difusa no desenho de vento.

`[INSIGHT: Utilize o marco temporal de 2024 como o ponto de corte (bound) do seu
período de avaliação principal para garantir a pureza da política de "cota
zero".]`

### Rodada 2 — devil's advocate: duas correções de fidelidade ao CGS

Não são opiniões; são leituras do texto do paper, e mudam o desenho.

**(a) O mapeamento estava invertido.** A Assumption 4 (paralelismo tradicional)
identifica **ATT(d|d)** — o nível. Não identifica a ACRT. CGS §3.2.2 abre com
*"average causal responses are not identified under a traditional parallel trends
assumption"*, porque a diferença de ATT entre doses carrega viés de seleção não
identificado: *"the selection bias is not identified as we do not observe Y(d)
for units that experienced dose d′. Such a result precludes a causal
interpretation of ATT differences across doses."* É a **Assumption 5 (SPT)** que
entrega **ACR e ATE(d)**.

O Teorema C.1 joga a favor: mantida a A4, a A5 equivale a **ATT(d|d) = ATE(d)**,
e os autores ressalvam que isso *"does not impose full treatment effect
homogeneity"* — exclui **selection-on-gains**, não heterogeneidade. O teste
proposto sobrevive com rótulo trocado: põe-se **ATT(d|d) contra ATE(d)**, e a
divergência é a assinatura da seleção-nos-ganhos.

**(b) O placebo pré-tratamento não testa o SPT.** Placebo restringe trajetórias
de resultado potencial *não tratado* — isso é a A4. O SPT envolve `Y_{t=2}(d)`,
trajetórias sob doses não recebidas, e no pré-período ninguém é tratado: não há
análogo. Acresce que não rejeitar ≠ validar, e que com antecipação desde
18/12/2018 um placebo em 2017 deixa só 2015–2016 como pré.

Aceito pelo pesquisador, com a peça de reposição: **bounds da §5.1 do CGS** sob
hipótese de direção do viés.

### Três ressalvas às amarrações da rodada 2

1. **Medir canal não conserta SUTVA.** Vento e ottobacia dizem por onde o veneno
   viaja; não restauram a premissa. SUTVA precisa de instrumento próprio.
2. **2024 não é escalonado.** A Lei 19.135/2024 também é estadual e simultânea —
   segundo evento simultâneo, não adoção escalonada.
3. **A PAM não separa algodão agroecológico de convencional.** A matriz de
   falsificação exigiria Censo Agropecuário ou cadastro de programa.

### Decisões registradas na L2

| Decisão | Escolha |
|---|---|
| Estimando principal | a **curva** (ACR/ATE sob SPT) |
| Identificação parcial | **bounds §5.1 ao lado**, como pacote |
| Escopo de dados | **cheio** (13 fontes) — preocupação de cronograma levantada e reafirmada |
| Janela principal | 2015 → 19/12/2024 (corte na Lei 19.135) |
| Ritmo do diálogo | completo, camadas 2 a 5 |
| Data do tratamento | sanção 08/01/2019, vigência 09/01/2019; três marcos de antecipação — notícia 24/02/2015, certeza 18/12/2018 |

---

## Layer 3 — Estratégia de evidência (FECHADA, 2 rodadas)

*Commitment gate L2→L3 pago: o desenho é curva sob SPT com bounds ao lado,
escopo cheio, janela até dez/2024.*

### Rodada 1 — magnitude, gatilho de abandono, régua torta

`[INSIGHT: o efeito esperado do banimento sobre o peso ao nascer em áreas de
alta dose deve situar-se entre 15 g e 25 g. Esse número assume que a proibição
da pulverização aérea elimina a deriva de longa distância, mas sofre atenuação
porque o produtor substitui o avião pelo trator, mantendo parte da carga
química.]`

Sobre aceitar um desenho que pode não enxergar o próprio efeito esperado:

`[INSIGHT: Eu aceito rodar o Ensaio 1 com o risco de um MDE de 33 g. Se o
resultado for nulo, a conclusão não será "o banimento não teve efeito na saúde".
(...) um resultado nulo aqui é evidência de cegueira do instrumento em pequenas
amostras, exacerbada pela provável substituição para aplicação terrestre, e não
prova de inocuidade.]`

Sobre qual régua torta pesa mais:

`[INSIGHT: A segunda régua (o químico e o instrumento GAEZ) me preocupa
infinitamente mais. A compressão da janela de tempo (Régua 1) é um problema
mecânico de econometria; resolve-se deslizando o período pré-tratamento para
2010–2014 e testando quebras estruturais. Já a Régua 2 ameaça a validade de
construto do desenho.]`

### Rodada 2 — devil's advocate, e uma correção de rota minha

**Correção que eu devia.** Eu havia escrito que, sem poder, a saída era trocar o
desfecho primário. Está errado: o piso amostral do ruído dá razão efeito/ruído de
1,30–1,81 para peso médio contra 0,17–0,80 para baixo peso, prematuridade e
mortalidade. Peso médio é o **único** desfecho com razão acima de 1. E o piso
implica DP de tendência ≈ 17,7 g, o que faz do MDE de 33 g com três municípios o
**cenário base**, não o pessimista. Detalhes em `05-integracao-estado-da-arte.md`
§6.

**Sobre o conflito entre os limiares propostos e a escada do CGS:**

`[INSIGHT: A escada vence: O limiar de 15 unidades é o piso real. (...) Se o
painel entregar algo entre 12 e 14 municípios, a saída correta é colapsar a
variável em doses discretas (ex: alta, média, baixa) e aplicar o estimador de
grupo-tempo para múltiplos tratamentos.]`

Implementado no script: curva a partir de 40, faixas discretas de 15 a 39,
faixas **marcadas como suporte fino** de 12 a 14, binário abaixo de 12.

`[INSIGHT: Você me pegou em um deslize de validade de construto. Para o Ensaio 1,
a escala de área (MIN_AREA_ESTADO_HA = 5000) é inútil se a lavoura não fizer
fronteira com núcleos habitados. O filtro primário para viabilidade de saúde
perinatal deve ser um piso de nascimentos na área de exposição (ou população
rural interceptada), não hectares agronômicos brutos.]`

O piso de área saiu do diagnóstico; o filtro operante é o MDE, que conta
nascimentos. Piso de área permanece critério legítimo — do **Ensaio 2**.

**Sobre o instrumento GAEZ:**

`[INSIGHT: Se a base cobrir banana e melão, nós mantemos a mecânica do
instrumento intacta e apenas trocamos os ingredientes da receita. (...) Verificar
o catálogo do GAEZ é prioridade zero antes de pagar o preço de assumir a dose
administrativa crua.]`

⚠️ Tentei verificar nesta sessão; `gaez.fao.org`, `gaez-services.fao.org` e
`fao.org/gaez` estão todos bloqueados pelo proxy. **Fica como pendência de
prioridade zero, para a máquina do pesquisador.**

**Sobre de onde vêm os clusters que faltam:**

`[INSIGHT: Baixar o corte da dose: Esta é a opção mais sólida e a que o dado vai
permitir. Ao aceitar municípios de "dose média" na definição do tratamento,
aumentamos o N e recuperamos poder estatístico, o que compensa a provável
diluição no tamanho do efeito médio estimado.]`

`[INSIGHT: A limitação submunicipal: Mudar a unidade para distritos ou setores
censitários destrói a confiabilidade do desfecho. O DATASUS sofre com imprecisão
crônica no registro de residência materno quando descemos da escala do
município.]`

**Sobre o grupo d = 0 no Gate 1:**

`[INSIGHT: Concordo em seguirmos o Gate 1 com o Zero Ampliado para avaliar a
viabilidade na cauda positiva, reportando as duas definições (Ampliado vs.
Operacional) lado a lado na reta final.]`

### Decisões registradas na L3

| Decisão | Escolha |
|---|---|
| Efeito esperado | **15–25 g** nos municípios de dose alta |
| Resultado nulo | reportado como **cegueira do instrumento**, não como inocuidade |
| Escada de especificação | curva ≥ 40; faixas 15–39; faixas finas 12–14; binário < 12 |
| Filtro de viabilidade | **nascimentos**, via MDE — não hectares |
| Instrumento GAEZ | **manter**, trocando a receita, **se** a base cobrir banana/melão |
| Clusters faltantes | **baixar o corte de dose**, não descer de unidade |
| d = 0 no Gate 1 | **Zero Ampliado**; Operacional em paralelo, reportados lado a lado |

---

## Layer 4 — Autocrítica (ABERTA, rodada 1 respondida com "não sei")

Perguntei três coisas duras de uma vez e a resposta foi **"não sei"**. Registrado
como está: **nenhum INSIGHT nesta rodada**, porque não houve resposta a
transcrever, e nada preenchido por mim.

O erro foi meu ao perguntar: as três não são do mesmo tipo, e eu não marquei
isso. Uma é lógica, uma é empírica-barata, uma é administrativa. Em vez de
repetir as perguntas, elas foram **equipadas** em
`07-layer4-perguntas-abertas.md`:

| Pergunta | Estado | O que a destrava |
|---|---|---|
| **Falsificação** — que resultado seria evidência contra o ban? | destravada **por lógica** | era pergunta de poder disfarçada: um nulo falsifica quando o IC exclui o efeito esperado. No piso amostral, isso acontece a partir de **~10 municípios tratados** — que vira o alvo numérico da decisão da L3 de baixar o corte de dose |
| **Seleção para nascimento vivo** — como separar do efeito? | destravada **por teste barato** | rodar óbito fetal do SIM contra a dose *antes* de escolher correção. Se não se move, é problema teórico. Se se move, há três rotas conhecidas, listadas como **menu, não recomendação** |
| **Enforcement** — a dose mede intenção ou exposição removida? | destravada **por ofício** | pedido LAI (Lei 12.527/2011) à SEMACE, com minuta pronta. Prazo legal de 20 dias — é a única com relógio externo, e por isso a primeira a disparar |

**O que continua sendo pergunta dele, e não foi respondido:** o piso de
falsificação (hoje 15 g, mas é escolha dele); qual rota de seleção adotar **se** o
teste acusar movimento; e o que escrever se o enforcement voltar vazio.

Ainda não tocados na L4: SUTVA transfronteiriço para além do papel de mecanismo,
e o adjetivo "irrefutável" que apareceu na L1.

## Layer 5 — Contribuição (NÃO INICIADA, com dependência)

A L5 pergunta que magnitude, com que precisão, muda a decisão de cada uma das
três cadeiras (STF, CCJ estadual, ANVISA/MAPA). Ela **depende** de saber se
existe magnitude estimável — que é exatamente o que a pergunta 2 da L4 e o gate
E1.5 vão dizer. Abrir agora seria pedir especulação sobre um número que o desenho
ainda não sabe se produz.

**Decisões em aberto que não são camada:**
- **Controle vetorial entra como exclusão do d = 0 ou como parte do tratamento?**
- Cultura-âncora (depende do Gate 1).
- **Janela pré-ban recua para 2010–2014?** A L3 registra a intenção
  ("resolve-se deslizando o período pré-tratamento"), sujeita a verificar
  comparabilidade da PAM no período.
- **Papel do glifosato** depois da contagem ABRASCO (4/23).

---

## Pendências de integridade

Duas referências entraram na argumentação e **não foram verificadas**. Nenhuma
está na pasta do Drive; o corpus disponível na sessão não as retorna.

- **Larsen et al. (2017)** — pesticidas na Califórnia, efeito concentrado no topo
  da distribuição de exposição.
- **Marx-Stoelting et al. (2025)** — crítica metodológica a Frank (2024) sobre
  falácia ecológica em dados agregados.

A crítica de falácia ecológica é válida independentemente da citação. Conferir
ambas contra DOI/Crossref antes de qualquer redação final.

Também não lido: `2023_tese_lmgreges.pdf` (PDF digitalizado, sem camada de texto).

---

## Nota de poder — por que os três limiares do script são a pergunta errada

O pesquisador devolveu a pergunta sobre `MIN_MUNI_POSITIVOS`,
`MIN_AREA_ESTADO_HA` e `MAX_SHARE_TOP5`. Resposta registrada aqui porque muda o
que o Gate 1 significa: **essas três constantes são um andaime diagnóstico, não
um critério de identificação.** Trocar o meu palpite pelo dele não melhora nada.
O que decide é outra coisa, e é calculável antes do dado.

**O que substitui `MIN_MUNI_POSITIVOS`: a escada de especificação do CGS.** Não é
um número, é uma escolha de estimador que o próprio paper organiza —

| Municípios com dose > 0 | Especificação defensável |
|---|---|
| ~40 ou mais, com dose espalhada | curva não-paramétrica (sieve à la Chen, Christensen & Kankanala) |
| ~15 a 40 | dose **discreta** em faixas, com indicadores múltiplos — CGS: *"when the treatment is discrete, this is as simple as running a linear regression with multiple treatment indicators"* |
| menos de ~15 | binário sob **Assumption 4-Agg** (paralelismo agregado); a curva é abandonada |

**O que substitui `MIN_AREA_ESTADO_HA`: nascimentos, não hectares.** O limiar
relevante não é área plantada — é quantos nascimentos existem no grupo de dose
alta. Hectare não move desfecho perinatal; gente exposta move.

**O que substitui `MAX_SHARE_TOP5`: o efeito mínimo detectável no topo.** Com
poucos clusters tratados o *n* efetivo é o número de **municípios**, não o de
bebês. A conta, para peso ao nascer (DP individual 500 g, 80% de poder, 5%
bilateral):

| | 3 municípios | 10 | 20 | 40 |
|---|---|---|---|---|
| DP das tendências municipais = 10 g | 16,3 g | 9,1 g | 6,6 g | 5,0 g |
| DP = 20 g | 32,6 g | 18,2 g | 13,3 g | 10,0 g |
| DP = 40 g | 65,2 g | 36,4 g | 26,5 g | 20,0 g |

Para comparar: uma regressão ingênua que ignora o *cluster* reportaria MDE de
**9,9 g** com três municípios tratados e 20 mil nascimentos. A diferença entre
9,9 g e 65,2 g é inteiramente artefato de contabilizar bebês em vez de
municípios — e é por isso que Conley–Taber e wild bootstrap não são acessório.

**A colisão que isso revela.** A hipótese registrada na L2 é que o efeito se
concentra na **cauda de alta exposição**. É exatamente onde o suporte é mais
fino. Quanto mais o pesquisador estiver certo sobre o formato, menos municípios
carregam o efeito, e maior o MDE. A hipótese e a restrição de dado apontam em
direções opostas — e isso precisa estar escrito na seção de limitações, não
descoberto na arguição.

**O que o Gate 1 passa a reportar:** número de municípios com dose positiva,
número de valores distintos de dose acima da mediana, contagem no decil superior,
nascimentos acumulados no grupo de dose alta, e o MDE implicado. A escolha de
especificação sai daí, não de um limiar arbitrário.

⚠️ O cálculo acima usa DP individual de 500 g e nascimentos anuais aproximados de
Limoeiro do Norte, Quixeré e Russas. **Substituir pelos números reais do SINASC**
assim que o script 02 rodar com dado verdadeiro; a DP das tendências municipais é
estimável no pré-período.
