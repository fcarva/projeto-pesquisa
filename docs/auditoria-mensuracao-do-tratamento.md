# Auditoria da mensuração do tratamento — e a literatura que a flag 7 não sabia que existia

*Auditoria do material produzido até 2026-09-22 (paper §4–§7, pré-especificação,
`auditoria-pre-especificacao.md`) cruzada com busca bibliográfica dirigida.
Feita em 2026-09-22.*

---

## 0. O que esta auditoria é

A auditoria anterior (`auditoria-pre-especificacao.md`) conferiu a
pré-especificação **contra o código que a executa e contra os artigos que ela
cita**. Ela fechou seis achados e não olhou para fora.

Esta olha para fora. A pergunta é a que a §6.8 do paper declara como *"a mais
valiosa que o trabalho deixa em aberto"*:

> *a dose por área plantada mede o que o banimento removeu?*

E a resposta que esta auditoria traz é que **a pergunta tem literatura, tem
estimador e tem um artigo publicado em periódico de econometria aplicada que
trata exatamente do caso deste desenho** — inclusive na direção específica em
que o erro aqui ocorre. O repositório inteiro trata a flag 7 como ameaça
inominada. Ela tem nome: *misclassification / mistargeting do tratamento em
DiD*, e desde 2025 tem solução publicada.

⚠️ **Nada aqui reestima coisa alguma.** Nenhum número do paper foi recalculado.
O que segue são (i) conferência do que está escrito, (ii) literatura verificada
e (iii) contas de desenho sobre os coeficientes **já reportados**.

---

## 1. O que a auditoria confirma

Antes do que falta, o que se sustenta — e é a maior parte.

| item | veredito |
|---|---|
| A inversão de alvo (`slope` → `level`) e seu registro na §8 | ✅ correta e bem defendida. O argumento da não-interpretabilidade da derivada agregada confere com o CGS Teorema 3.2(b) |
| O enquadramento "limite superior informativo" | ✅ é a leitura conservadora e o critério estava fixado antes |
| Recusar o controle sintético puro como achado (§6.7) | ✅ os três rodam sobre a mesma matriz; a recusa é correta |
| A suspensão do SISAGUA | ✅ e é resultado, não lacuna. Quebra de registro em 2020 produziria efeito espúrio de 100% |
| A suspensão do vento (coerência 0,96) | ✅ os alísios tornam "a favor do vento" colinear com geografia |
| A varredura dos bans municipais | ✅ completa e com o achado que importa (Limoeiro, 2009) |
| A banana como âncora | ✅ **e agora tem corroboração externa** — ver §5.3 |
| O teste SPT do CGS §6.3 | ✅ implementado corretamente; a formulação corrigida ("não isola, mas pode falsificar") confere com o texto |

**O diagnóstico de poder da §6 está certo no que afirma.** O problema não é que
ele erre — é que ele apresenta duas leituras como indecidíveis quando a
literatura decide entre elas.

---

## 2. O achado central: as duas leituras não são indecidíveis

A §6.8 do paper e a flag 7 do `CLAUDE.md` põem o problema assim:

> *"As duas leituras pedem coisas opostas, e é por isso que distingui-las importa
> mais do que escolher entre elas. Falta de poder pede mais unidades tratadas.
> Erro de medida do tratamento pede outra variável de dose."*

Isso está certo como diagnóstico e **errado como impasse**. Erro de medida no
tratamento em DiD não é uma leitura interpretativa: é um objeto formal, com
estimando próprio, viés de direção caracterizada e estimador publicado.

### 2.1 O artigo que trata exatamente deste caso

> **Negi, A. & Negi, D. S. (2025).** *Difference-in-Differences With a
> Misclassified Treatment.* **Journal of Applied Econometrics** 40(4): 411–423.
> `doi:10.1002/jae.3116` — ✅ **open access**, conferido 2026-09-22 (metadados e
> resumo pelo registro do periódico).

Do resumo, verbatim:

> *"identification and estimation of the average treatment effect of a latent
> treated subpopulation in difference-in-difference designs when the observed
> treatment is **differentially (or endogenously) mismeasured** for the truth.
> Common examples include misreporting and **mistargeting**. We propose a
> two-step estimator that corrects for the empirically common phenomenon of
> **one-sided misclassification** in the treatment status. The solution uses a
> single exclusion restriction embedded in a partial observability probit to
> point identify the latent parameter."*

**Três encaixes, e o terceiro é o que surpreende:**

1. ***Mistargeting*** é o termo deles para o problema desta tese: o tratamento
   observado aponta para unidades que não o receberam.
2. ***Differentially / endogenously* mismeasured** — o caso difícil, em que o
   erro se correlaciona com o desfecho. É o caso provável aqui (§2.3).
3. ⚠️ ***One-sided* misclassification — e o repositório JÁ PROVOU que o erro
   daqui é unilateral.** O Censo Agropecuário mostrou que **nenhum** município
   de dose zero tinha aeronave (§5.4 do paper, flag 5 ✅). Isso é exatamente
   dizer que **não há falso negativo**: não existe município marcado `d = 0`
   que fosse de fato tratado. Só há falso positivo — dose alta sem aeronave, 17
   dos 19. A condição que o estimador deles exige não é suposta: está medida,
   e foi medida por outra razão.

Essa é a informação mais valiosa desta auditoria. A verificação da flag 5 foi
feita para defender o grupo de comparação, e **o que ela produziu de fato foi a
condição de identificação do estimador que resolve a flag 7.**

### 2.2 O complemento que não exige restrição de exclusão

> **Denteh, A. & Kédagni, D.** *Misclassification in Difference-in-Differences
> Models.* **arXiv:2207.11890** (v3; SSRN 4181736). ⚠️ **working paper, não
> publicado** — conferido 2026-09-22 contra o texto completo no arXiv.

Menos poderoso e muito mais barato: dá **limites**, não ponto, e não exige
instrumento. Quatro resultados que mordem aqui:

- **Proposição 1.** Sob misclassification arbitrária, o estimando de DiD recupera
  média ponderada do ATT entre corretamente classificados e mal classificados,
  com peso **não-positivo** nos segundos, e os pesos **não somam 1**. Logo o
  sinal pode inverter. ⚠️ *"the consequences of misclassification are more
  severe than previously articulated"* — contra a prática comum de supor que o
  efeito é "só atenuação".
- **Sob misclassification não-diferencial + monotonicidade**, o viés É só
  atenuação: sinal correto, magnitude menor.
- **Corolário 5** — o limite, e é aritmética de uma linha:

  ```
  min{ θ_DID / (1 − λ),  θ_DID }  ≤  ATT  ≤  max{ θ_DID / (1 − λ),  θ_DID }
  ```
  com `λ ≥ P(ε=1|D=1) + P(ε=1|D=0)`, escolhido por **conhecimento
  institucional**. Na aplicação deles (setor de saneamento brasileiro, Kresch
  2020) usam `λ = 2/7 = 0,29`, derivado da defasagem entre data de proposição e
  de aprovação da lei.
- **Múltiplas fontes com taxas de erro diferentes** → identificação parcial
  *data-driven*, sem precisar declarar `λ`. ⚠️ Este projeto tem quatro proxies
  da mesma coisa — PAM (área), GAEZ (aptidão), Censo Agro (equipamento),
  SIPEAGRO (registro). É literalmente o insumo que o método pede.

⚠️ **E os dois artigos se aplicam ao DiD binário, não à curva do CGS.** Isso
*não* os exclui: Denteh & Kédagni nomeiam explicitamente o caso deste desenho —
*"researchers use a mismeasured continuous treatment variable to define a binary
treatment variable for DID estimation [...] The resulting binary variable from
the mismeasured continuous treatment is **necessarily misclassified**."* A
camada binária deste trabalho (event study do HonestDiD, synthdid, controle
sintético) é exatamente esse caso.

### 2.3 ⚠️ E há razão para o erro aqui ser diferencial, o que é a hipótese ruim

A Corolário 5 exige misclassification **não-diferencial** para valer como
atenuação. Aqui provavelmente não vale, e a razão é substantiva: ter aeronave
não é sorteio. As 36 aeronaves estão em 7 municípios, e 27 no decil superior —
são as operações de fruticultura irrigada de escala empresarial. Porte do
estabelecimento correlaciona com renda, com infraestrutura de saúde e com
desfecho perinatal. Ou seja: **ε correlaciona com o desfecho potencial**, que é a
definição de erro diferencial.

Consequência, pela Proposição 1: **o sinal pode inverter**, e a coerência de
sinal entre estimadores da §6.8 — *"todos negativos"* — perde valor probatório.
Eles não são quatro medidas independentes que concordam; são quatro estimadores
sobre **a mesma dose mal medida**, herdando o mesmo viés. O paper já faz esse
argumento para a matriz do synthdid (§6.7, razão 1). **Ele não o estende à dose,
e a dose é onde ele morde mais.**

---

## 3. Quanto é o problema: a conta que a §6 não fez

Aplicando o Corolário 5 aos coeficientes **já reportados** no paper. `λ` é o
parâmetro de sensibilidade; a última coluna usa o valor ingênuo que o Censo
sugere (17/19 dos tratados sem aeronave).

| estimador (§6) | λ=0 | λ=0,3 | λ=0,5 | λ=0,7 | λ=0,895 |
|---|---:|---:|---:|---:|---:|
| Synthetic DiD | −20,2 | −28,8 | **−40,3** | −67,2 | −191,5 |
| Controle sintético | −34,6 | **−49,5** | −69,3 | −115,5 | −329,1 |
| DiD simples | −21,9 | −31,2 | **−43,7** | −72,8 | −207,6 |
| CGS `ATT(d\|d)` ⚠️ | −36,2 | **−51,7** | −72,4 | −120,6 | −343,8 |

⚠️ A linha do CGS entra **fora do escopo formal** do corolário (tratamento
contínuo, não binário) e serve só de ordem de grandeza.

**A leitura, e é o parágrafo mais importante deste documento:**

> O MDE deste desenho é **33,4 g**. A partir de `λ = 0,5` — e para o controle
> sintético e o CGS já a partir de `λ = 0,3` — **o efeito implicado sobre os
> genuinamente tratados ultrapassa o MDE do próprio desenho.**

Isto é: sob a leitura de erro de medida, o desenho **teria tido poder** — o que
faltou não foi amostra, foi que o tratamento estava apontado para o lugar
errado. As duas leituras da §6.8 deixam de ser simétricas. A segunda não é uma
ressalva sobre a primeira; é uma hipótese com magnitude computável, e a
magnitude cai dentro do que a âncora reporta para exposição alta
(146–243 g no percentil 90 de Reynier & Rubin).

### Três ressalvas, e são sérias

1. **São limites de estimativa pontual, não intervalos de confiança.** Inferência
   sobre eles exige o arcabouço de *intersection bounds* (Chernozhukov, Lee &
   Rosen), que os autores usam. Com 17 clusters tratados, a largura resultante
   pode engolir a leitura acima.
2. **`λ = 0,895` é indefensável como escolhido**, e está na tabela para mostrar
   que é. O Censo é de **2006**, conta **estabelecimentos** e não voos, e um
   prestador de serviço aeroagrícola sediado em Limoeiro do Norte pulveriza
   lavoura em Quixeré — "não ter aeronave" não é "não receber pulverização". A
   faixa defensável é `λ ∈ [0,3; 0,7]`, e mesmo ela precisa de argumento
   escrito.
3. **Se o erro for diferencial** (§2.3), o Corolário 5 não vale e a rota correta
   é Negi & Negi, que exige restrição de exclusão. **O projeto não tem uma
   pronta.** O GAEZ já está gasto como instrumento da dose. Candidato natural:
   **distância a pista aeroagrícola registrada** — relevante para ter aeronave,
   plausivelmente excluível do desfecho perinatal condicional a aptidão e porte.
   Isso é hipótese a testar, não solução em mão.

---

## 4. As três rotas, ordenadas por razão valor/custo

### Rota 1 — Atravessar a fronteira estadual. ⭐ **A mais barata e a mais subutilizada**

**O achado:** a Chapada do Apodi **não é cearense**. É microrregião dos **dois**
estados — há uma Chapada do Apodi no Ceará e uma no Rio Grande do Norte, mesmo
complexo de fruticultura irrigada, mesmas culturas, mesmo aquífero Jandaíra,
separados por uma linha administrativa. **O Ceará proibiu em 2019; o Rio Grande
do Norte não.** Nenhuma outra UF tinha lei estadual à época — o Ceará foi o
**primeiro estado**, e os 8 municípios que haviam proibido antes estão no
Centro-Oeste, Sul e Sudeste, não no RN.

**Por que isso resolve coisas que nenhum ajuste interno resolve:**

- O grupo de comparação deixa de ser *"município cearense com área zero de
  banana"* — cuja contaminação o próprio projeto declara como ameaça aberta — e
  passa a ser *"município potiguar com banana e aeronave, do outro lado da
  linha"*. Comparação entre **iguais**, não entre quem tem e quem não tem
  agricultura.
- O `d = 0` deixa de carregar a identificação. O tratamento passa a ser
  **estado × período**, que é medido sem erro. **A flag 7 desaparece do desenho
  principal** em vez de ser limitada.
- O synthetic DiD **volta a ser o previsto**. A §6.7 diz que a versão estadual
  *"não é executável com os dados adquiridos, que cobrem apenas municípios
  cearenses"*. Isso é limite de **aquisição**, não de desenho.
- Encorpa o grupo tratado e o de controle ao mesmo tempo — sem o efeito colateral
  que a §6.8 teme (baixar o corte de dose **piora** a diluição; atravessar a
  fronteira não).

**O custo é de parâmetro, não de código.** O pipeline está *hard-coded* em UF 23
em três pontos, e todos são de uma linha:

| arquivo | linha | o que é |
|---|---|---|
| `scripts/data_prep/01_check_dose_variation.py` | 61, 86, 466 | `UF_CEARA = "23"`, `SIDRA_TERRITORIO = "in n3 23"`, filtro `startswith` |
| `scripts/data_prep/02_clean_births.py` | 52, 242, 386 | `UF_CEARA`, filtro de residência, `search(state="CE")` |

PAM/SIDRA é nacional; SINASC e SIM são nacionais; o GAEZ **já foi calculado em
percentil nacional sobre 5.570 municípios** (gates §7-quater) — o índice do RN
sai sem reprocessar raster.

⚠️ **A ameaça que isso cria, e ela é conhecida.** SUTVA: deriva atravessa a
fronteira, e `framework-dissertacao.md:152` já a registra. O viés é de
contaminação do controle, isto é, **atenuante** — conservador, e é a direção
certa de errar. Mitigação padrão: excluir a faixa imediata de fronteira como
robustez, o que o `04-roteiro-qualificacao.md:355` já prevê.

⚠️ **E uma ameaça nova, que precisa ser checada antes de investir:** o RN é
comparável em *saúde* e em *registro*? Cobertura do SINASC, qualidade do
preenchimento de peso, e nível de mortalidade infantil precisam bater. É uma
consulta descritiva, não um projeto.

### Rota 2 — Estimar onde o efeito está, não onde ele é pequeno

A §6.8 registra como *"segundo caminho, que não estava declarado"* o achado
distributivo de Reynier & Rubin: efeito **doze vezes** maior no decil inferior
de peso esperado (75 g contra 6 g). Contra o MDE de 33,4 g, a cauda é detectável
e a média não. O paper para aí, corretamente, porque não estava pré-especificado.

**O estimador existe, é publicado e tem comando pronto:**

> **Sasaki, Y. & Wang, Y. (2024).** *Extreme Changes in Changes.* **Journal of
> Business & Economic Statistics** 42(2): 812–824.
> `doi:10.1080/07350015.2023.2249509` — comando Stata `ecic` (`ssc install
> ecic`). ✅ conferido 2026-09-22.

Por que serve com precisão incomum:

- Estende *changes-in-changes* (Athey & Imbens 2006, *Econometrica* 74:431–497)
  para **quantis extremos** (`q < 0,05`), onde o CIC convencional é
  inconsistente. Os autores recomendam CIC convencional para quantis
  intermediários e o deles para as caudas.
- **A aplicação empírica deles é peso ao nascer em quantis extremamente baixos**
  (reforma do EITC de 1993). Não é analogia — é o mesmo desfecho e a mesma
  cauda.
- CIC **dispensa tendências paralelas**, trocando-a por invariância de ranking.
  Como o teste SPT da §6.6 mostrou que *"o ruído de pré-período do próprio painel
  é maior que o efeito estimado"*, sair da família que depende de paralelismo é
  ganho, não perda.
- Escala: nas simulações calibradas eles usam células de ~13 a 27 mil
  observações. O painel tem **1.001.709** nascidos vivos; o grupo tratado sozinho
  (17 municípios × ~403 nascimentos/ano × 4 anos pré) fica nessa ordem.

⚠️ **E o que ele NÃO resolve, que precisa estar escrito antes de rodar.** O eCIC
opera sobre a distribuição individual de nascimentos, e sua variância assintótica
trata as observações como independentes. **Os clusters tratados continuam sendo
17.** Tratar 27 mil nascimentos como 27 mil informações independentes é
exatamente a precisão falsa que a §6.3 existe para desmentir. O ganho real é de
**sinal** — mirar onde o efeito é 12× maior —, não de ruído. Prometer o segundo
seria repetir, em outra chave, o erro que o projeto vem evitando.

⚠️ E é **exploratório declarado**, pré-especificado para o ciclo seguinte. A §5
da pré-especificação já fixou isso.

### Rota 3 — Medir o método, não a cultura

A dose certa é número de aeronaves / operações aeroagrícolas por município no
pré-ban. Três fontes, em ordem de custo:

| fonte | estado | o que dá |
|---|---|---|
| **ANAC / RAB** | ⚠️ **não mapeado no repositório** — dados abertos, CSV/JSON, com categoria de aeronave e operador | frota agrícola por endereço de operador, com data de registro → reconstrói o estoque de 2018 |
| **SINDAG** | ⚠️ não mapeado | publica ranking de frota por estado e análises históricas; o corte municipal exige contato |
| **SEMACE (LAI)** | ⏸️ minuta pronta (`lai-semace-minuta.md`), não protocolada | cadastro aeroagrícola pré-ban — a rota que o projeto já elegeu prioridade |

⚠️ **O RAB é a novidade desta auditoria e não está em `lacunas-de-dados.md`.** É
dado aberto federal, não depende de LAI e não tem prazo de 20 dias. Ressalva
séria: registro é por **endereço do operador**, que não é onde a aeronave voa —
um prestador sediado em Limoeiro pulveriza a Chapada inteira. Mede operador, não
exposição. Mesmo assim é uma **segunda proxy com taxa de erro diferente da
PAM** — que é precisamente o insumo do método de múltiplas fontes de
Denteh & Kédagni (§2.2).

---

## 5. Notas de literatura que não entram nas rotas mas mudam o texto

### 5.1 Camacho & Mejía (2017) tem pendência aberta e ela vale fechar

`referencias-verificadas.md:107` e `04-roteiro-qualificacao.md:402` registram que
o artigo está **sem abstract depositado** e que a descrição no repositório se
apoia no título. Ele é o análogo mais direto do objeto — pulverização **aérea**,
economia, identificação causal — e a busca confirma que eles exploram *"variation
in aerial spraying across time and space"* com **hectares efetivamente
pulverizados** (média de 128 mil ha/ano sob o Plan Colombia, pico de 172 mil em
2006), não proxy de cultura.

⚠️ **Isto é diretamente relevante à flag 7 e o repositório não o explora:** o
análogo mais próximo desta tese **mediu o método diretamente** porque o Estado
colombiano registrava cada operação. A distância entre os dois desenhos não é de
método — é de disponibilidade de cadastro. Dizer isso no paper transforma uma
fraqueza em contribuição declarada: é a razão pela qual a LAI à SEMACE e o RAB
deixam de ser conveniência.

⚠️ O PDF do working paper (CGD WP 408) está **bloqueado pelo proxy de egresso**
desta sessão. A verificação contra texto completo **continua pendente** — esta
auditoria não a fechou.

### 5.2 A literatura de exposição residencial dá o gradiente que a dose municipal apaga

A busca devolveu um corpo grande e consistente (San Joaquin Valley, Patagônia,
Costa Rica) em que a exposição é medida por **proximidade residencial em
raio de 500 m a 2 km**, e não por intensidade municipal. Dois itens com encaixe
direto:

- **Larsen, Gaines & Deschênes (2017)**, *Nature Communications* 8:302 — já está
  no `.bib` (`larsen2017agricultural`). Efeitos adversos aparecem **só no topo
  5%** da distribuição de exposição. Reforça a Rota 2: o efeito é de cauda, dos
  dois lados.
- ⚠️ **Um estudo de mancozebe e pulverização aérea em plantações de banana** com
  gestantes (contexto Costa Rica) apareceu na busca e **não está no `.bib`**.
  Fungicida, banana, aplicação aérea, gestação — o cruzamento exato da química
  documentada pelo Dossiê ABRASCO. ⚠️ Não consegui recuperar o texto completo
  nesta sessão; entra como **referência a verificar**, não como citação.

**A implicação metodológica é desconfortável e deve estar no paper.** Se a
exposição real opera em raio de quilômetros, o município é unidade grosseira, e
agregá-la a município **dilui** — que é o mesmo vetor da flag 7, por outra via. A
pré-especificação veda descer de unidade geográfica (§7), com razão declarada
(registro de residência do DATASUS). A vedação continua certa; o que muda é que
a **razão pela qual o efeito é pequeno** passa a ter duas fontes somadas, não
uma.

### 5.3 A banana ganhou corroboração externa

O Gate 1 escolheu banana por critério estatístico (169 municípios, Gini 0,86) e
por química (procimidona é fungicida de bananal). A busca acrescenta
corroboração independente do contexto produtivo: **o Ceará é o segundo maior
produtor nacional de banana, com a produção concentrada na Chapada do Apodi e no
Cariri**, e foi o segundo maior exportador em 2018.

⚠️ **E uma afirmação que NÃO consegui verificar e que não deve ser usada:** uma
fonte secundária de advocacy afirma que a banana era a cultura mais pulverizada
por avião no Ceará e que a produção **aumentou** após o ban. A busca dirigida
**não confirmou** nenhuma das duas. A segunda é matéria do Ensaio 2 (lado do
custo) e é **checável em uma linha na PAM que o projeto já tem** — série de área
e produção de banana, 2015–2024, Ceará. Se procede, é achado; enquanto não se
checa, não é nada.

---

## 6. O que fazer, em ordem

| # | Ação | Custo | Por que nesta posição |
|---|---|---|---|
| 1 | **Rodar a tabela do Corolário 5** sobre os coeficientes que já existem, com `λ` declarado e justificado | ~2 h | Converte a flag 7 de ameaça inominada em **faixa reportável**. Não depende de dado novo, de rede, nem de decisão do orientador |
| 2 | **Descritivas do RN** — cobertura SINASC, banana na PAM, aptidão GAEZ, comparabilidade de registro | ~4 h | Decide a Rota 1 antes de investir nela. Se o RN não for comparável, morre barato |
| 3 | **Ler Negi & Negi (2025)** pelo texto completo (é open access) e decidir se a restrição de exclusão existe | ~3 h | É o único caminho de **identificação pontual**; e a condição de erro unilateral já está verificada |
| 4 | **Baixar o RAB da ANAC** e cruzar com o decil superior | ~4 h | Segunda proxy independente → habilita os limites de múltiplas fontes, e não depende de LAI |
| 5 | **Checar a série de banana pós-ban na PAM** | ~30 min | Fecha a afirmação não-verificada da §5.3, nos dois sentidos |
| 6 | Protocolar a LAI à SEMACE | externo | Continua sendo a única rota para o cadastro pré-ban; tem prazo, então dispara em paralelo |

**Os itens 1, 2 e 5 fecham dentro de uma sessão e não dependem de nada externo.**

---

## 7. O que esta auditoria NÃO faz

- **Não reestima.** Os números da §3 são transformações aritméticas de
  coeficientes já reportados, não estimação nova.
- **Não decide a rota.** As três da §4 não são exclusivas e a escolha é do
  pesquisador com o orientador. A Rota 1 é a recomendada por razão de
  custo/benefício, não por superioridade metodológica intrínseca.
- **Não fecha Camacho & Mejía.** O PDF está bloqueado pelo proxy desta sessão; a
  pendência de `referencias-verificadas.md:107` **permanece aberta**.
- **Não verificou o artigo de mancozebe/banana** — apareceu na busca, não abriu o
  texto completo. Não entra no `.bib` até abrir.
- **Não conferiu as 40 entradas do `.bib`.** Conferiu as três novas
  (Negi & Negi, Sasaki & Wang, Denteh & Kédagni) contra registro do periódico ou
  texto no arXiv.
- **Não alterou o paper nem a pré-especificação.** Se a §3 for adotada, ela é
  **desvio** e entra na §8 com data — o alvo não muda, mas a camada de robustez
  ganha procedimento que não estava declarado.

---

## Referências novas verificadas nesta auditoria

```bibtex
@article{neginegi2025misclassified,
  author  = {Negi, Akanksha and Negi, Digvijay Singh},
  title   = {Difference-in-Differences With a Misclassified Treatment},
  journal = {Journal of Applied Econometrics},
  volume  = {40}, number = {4}, pages = {411--423}, year = {2025},
  doi     = {10.1002/jae.3116},
  note    = {open access; verificado 2026-09-22}
}
@article{sasakiwang2024extreme,
  author  = {Sasaki, Yuya and Wang, Yulong},
  title   = {Extreme Changes in Changes},
  journal = {Journal of Business \& Economic Statistics},
  volume  = {42}, number = {2}, pages = {812--824}, year = {2024},
  doi     = {10.1080/07350015.2023.2249509},
  note    = {comando Stata \texttt{ecic}; verificado 2026-09-22}
}
@article{atheyimbens2006cic,
  author  = {Athey, Susan and Imbens, Guido W.},
  title   = {Identification and Inference in Nonlinear Difference-in-Differences Models},
  journal = {Econometrica},
  volume  = {74}, number = {2}, pages = {431--497}, year = {2006}
}
@unpublished{dentehkedagni2026misclassification,
  author = {Denteh, Augustine and K{\'e}dagni, D{\'e}sir{\'e}},
  title  = {Misclassification in Difference-in-Differences Models},
  note   = {arXiv:2207.11890; SSRN 4181736. NAO PUBLICADO --- citar como working paper},
  year   = {2026}
}
```

⚠️ `atheyimbens2006cic` entra pela citação em Sasaki & Wang, que é fonte
confiável mas **secundária**. Conferir volume/páginas contra o periódico antes
de fechar o `.bib`.
