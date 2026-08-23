# Research Plan Summary — Ensaio 1

*ARS `deep-research`, modo `socratic`, fronteira de não-geração mantida.*
*Camadas 1 e 2 fechadas; 3, 4 e 5 abertas. Última atualização: 2026-08-23.*

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
| Data do tratamento | 08/01/2019; antecipação em 18/12/2018 |

---

## Layers 3, 4 e 5 — ABERTAS

Perguntas colocadas, não respondidas. **Não preenchidas por mim.**

**L3 — Estratégia de evidência (rodada 1 pendente)**
- *Commitment gate:* que magnitude de efeito sobre peso ao nascer o desenho deve produzir, se estiver correto? (ver a nota de poder abaixo, que estreita muito a faixa admissível)
- Que resultado no diagnóstico de dose mata a curva e força a migração para bounds ou para especificação discreta?
- Se o SISAGUA falta de forma **seletiva** — ausente justamente onde a dose é alta —, o canal-água é reportado com ressalva ou condicionado a cobertura mínima definida de antemão?
- Cavalcante (2023) indica que a banana **cresceu** pós-ban. Se houve substituição de método sem perda de produtividade, a exposição pode ter caído pouco e o efeito de saúde tem que ser pequeno **por construção**. Como o Ensaio 1 absorve a evidência que fortalece o Ensaio 2 e enfraquece o próprio mecanismo?

**L4 — Autocrítica (não iniciada)**
- Seleção para nascimento vivo: se o ban reduz óbito fetal, fetos marginais passam a nascer e entram na cauda de baixo peso, atenuando ou invertendo o efeito sobre peso médio.
- SUTVA com deriva transfronteiriça, para além do papel de mecanismo.
- Poucos clusters intensamente tratados e lacuna de *enforcement*.
- O adjetivo "irrefutável", que nenhum DiD sustenta.

**L5 — Contribuição (não iniciada)**
- Que magnitude, com que precisão, muda a decisão de cada uma das três cadeiras.

**Decisões em aberto que não são camada:**
- **Controle vetorial entra como exclusão do d = 0 ou como parte do tratamento?**
  O §2º do art. 28-B proíbe também dispersão aérea sanitária. As duas leituras
  são defensáveis e dão estimandos diferentes.
- Cultura-âncora (depende do Gate 1).
- Definição final de d = 0 entre as quatro construções.

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
