# Pré-especificação — Ensaio 1

**Status:** ✅ **FECHADA** · **Data de fechamento:** 2026-09-21 · **Assinatura:** Felipe Carvalho Souza Santos (o commit é o carimbo de tempo)

<!-- PRESPEC_STATUS: FECHADA -->

---

## ⚠️ 0. O que este documento é — e o que ele NÃO é

**Este NÃO é um pré-registro no sentido estrito, e dizer que fosse seria falso.**

A versão anterior deste arquivo dizia: *"a janela para escrever isto ainda está
aberta justamente porque a rede está bloqueada e nenhuma fonte real foi tocada.
Ela fecha na primeira rodada com dado."* **Essa janela fechou em 2026-08-25**, e
o histórico do git prova a data. Escrever agora fingindo o contrário seria
exatamente a "racionalização com data" contra a qual o próprio documento avisa.

O que isto é: **um plano de análise escrito depois dos diagnósticos de desenho e
antes de qualquer estimação.** É categoria real e defensável — mas só enquanto
declarada.

### O que já era conhecido ao assinar

| conhecido | onde | é resultado do ban? |
|---|---|---|
| Distribuição de dose por cultura (Gate 1) | gates §4 | ✘ pré-período |
| DP das tendências municipais e sua decomposição | gates §5–6 | ✘ pré-período (placebo por construção) |
| MDE por cultura, e que ele **reprova** como especificado | gates §5 | ✘ conta de desenho *ex ante* |
| Contagens do SINAN, SIH, SIM, população | gates §7-bis | ✘ descritivo |
| Primeiro estágio do GAEZ (aptidão × dose) | gates §7-quater | ✘ relevância do instrumento |
| Bans municipais < 2019 | legislacao §1 | ✘ saneamento de pré-período |

### O que NÃO era conhecido ao assinar

**Nenhuma estimativa de efeito.** `03_contdid.R` nunca produziu coeficiente:
a única execução, acidental em 2026-09-21, abortou na asserção de
`control_group` e **não gravou arquivo algum** (conferido). Nenhum `ATT`,
nenhum `ACR(d)`, nenhum event study existe neste repositório.

> **A fronteira que este documento protege** é entre *desenho* e *efeito*, não
> entre *nenhum dado* e *dado*. A primeira fronteira ainda está intacta e é
> verificável no git. A segunda já não estava, e fingir que sim custaria mais
> credibilidade do que a honestidade custa.

---

## 1. Desfecho primário

**Escolha: `peso_medio`** (peso médio ao nascer, município × ano-mês, SINASC).

Ratificado. É o único dos quatro candidatos com razão efeito/ruído acima de 1
(1,30–1,81, contra 0,44–0,80 do baixo peso, 0,50 da prematuridade e 0,17 da
mortalidade infantil — `05-integracao-estado-da-arte.md` §6). Média contínua
sobre todos os nascimentos bate evento raro por um fator de duas a oito vezes.

⚠️ **A flag 6 permanece uma ameaça, não uma solução.** Se o ban reduz óbito
fetal, fetos marginais passam a nascer e entram na cauda de baixo peso, e o
efeito sobre peso médio vem **atenuado ou invertido**. Por isso o óbito fetal
entra como confirmatório #2 (§6) — não como acessório.

## 2. Exposição primária

**Escolha: `share_gestacao_pos_ban`.**

É a fração da gestação exposta ao regime pós-ban, por retroprojeção gestacional.
Os três `share_tri1/2/3` ficam **exploratórios declarados**: qual trimestre
importa é pergunta empírica, e rodar os quatro contando o que se move é
exatamente o que a §6 existe para impedir.

⚠️ `pos_ban_nascimento` (marcação ingênua pela data de nascimento) **não é
exposição** — está no painel só para medir a atenuação que ela embutiria.

## 3. Cultura-âncora

**Escolha: `Banana (cacho)`.**

Ratificada contra o Gate 1, que é o teste empírico que a flag 1 exigia:

| critério | banana |
|---|---|
| municípios com área positiva | **169** |
| Gini da dose | **0,86** |
| área no decil superior | **78%** |
| especificação recomendada pelo script 01 | **curva** |

Dispersão alta **com** suporte largo — a combinação que o sieve exige. Converge
com três fontes independentes (dissertação UFC, ADI 7794, Cavalcante 2023) e com
a química documentada: **procimidona é fungicida de bananal**, e aparece em 23
de 23 amostras do Dossiê ABRASCO.

✅ E o GAEZ confirma **relevância do instrumento**: o decil superior da banana
tem aptidão média 0,372 contra 0,263 do resto (mediana 0,500 contra 0,195).
Banana é plantada onde banana é apta.

⚠️ **Melão e algodão estão empiricamente encerrados** para a curva — 10 e 28
municípios com área positiva. Eram a hipótese do material de projeto pela
Chapada do Apodi; o dado a descartou. Registrado aqui para que a troca não
pareça, depois, conveniência.

## 4. Especificação

- **Degrau da escada do CGS:** `curva` — sieve não-paramétrico (CCK), que é o
  que a coluna `especificacao` do script 01 recomenda para a banana.
- **Parâmetro-alvo primário:** ✅ **`slope`** — a curva `ACR(d)`.

  ⚠️ **E ela custa mais caro que o nível, o que fica declarado aqui.** A curva
  exige **strong parallel trends** (Assumption SPT de CGS), que exclui
  *selection-on-gains* e **não é testável** por placebo pré-tratamento. O
  `level` (`ATT(d|d)`) sai sob paralelismo tradicional e será reportado como
  **sensibilidade**: a distância entre os dois é informação sobre quanto a
  Assumption SPT está carregando.

  A justificativa de fundo é que o Ensaio 2 precisa da curva — sem ela a
  comparação de Weitzman perde âncora empírica e vira exercício teórico.

- **Construção de `d = 0` primária:** ✅ **definição 4** (baixa aptidão FAO-GAEZ).

  ⚠️ **Isto é um desvio da recomendação que o documento original trazia**, e o
  motivo é que a restrição mudou: a versão anterior dizia *"primária = definição
  2, porque 3 e 4 não estarão disponíveis"*. **O GAEZ foi adquirido em
  2026-09-21**, 184/184 municípios. Entra na tabela de desvios da §8.

  É o zero que **não depende de registro administrativo estar completo**, e é o
  único que permite o teste de contaminação da §5.3 — quebrar o `d = 0` por
  aptidão: se os de alta aptidão com área zero se comportam como os de baixa, o
  zero é real; se divergem, o zero é medida, e a divergência estima a
  contaminação.

  ⚠️ O sieve centra a curva em `mean(dy[dose == 0])`, então esta escolha **move
  o nível do resultado**, não a interpretação. A definição 2 será reportada como
  sensibilidade, e a distância entre as duas é a banda do nível.

  ⚠️ **A definição 3 segue impossível** — mede o *método*, e nenhuma fonte a
  alcança no pré-ban: o SIPEAGRO é dado aberto mas o registro não tem data e é
  93% drone pós-2024, e as autorizações começam em 2021. A LAI à SEMACE é a
  única rota, e não chegou.

- **Grupo de comparação (`control_group`):** `nevertreated`.

  ⚠️ Não é detalhe técnico: define **quem são as unidades de comparação**. O ban
  é simultâneo, então não existe "not yet treated" em sentido de *timing*, e a
  comparação é por dose. **E isto colide com a flag 5**: `nevertreated` são os
  `d = 0`, que a flag 5 diz não serem zero de tratamento — o §2º do art. 28-B
  alcança controle vetorial aéreo. Esta escolha e a construção do zero acima são
  **a mesma decisão**.

- **Cortes do colapso pré/pós:** `--corte-pre 2018-12` · `--corte-pos 2019-10`.

  As coortes cuja gestação atravessa o ban são descartadas (1.656 células, 9,4%).
  É a escolha conservadora; incluí-las embute atenuação.

- **Janela que define a dose:** **2015–2018 como primária**, com **2010–2014 como
  sensibilidade declarada**.

  ⚠️ A janela primária **começa depois do marco de notícia** (PL 18/2015
  apresentado em 24/02/2015), então a dose pode já responder à expectativa —
  ameaça que morde a *variável de tratamento*, não só o desfecho. A janela
  recuada é comparável (184 municípios e 86 culturas em ambas, costura suave),
  e custa 24% de troca no grupo tratado. Se os resultados não dependerem da
  janela, a ameaça fica endereçada empiricamente em vez de suposta.

## 5. Critério de falsificação

**Piso de efeito esperado: 15 g.**

O extremo inferior da faixa de 15–25 g registrada na Layer 3 — a escolha
**estrita**, porque piso menor é mais difícil de falsificar. O script 01 emite
`falsifica` comparando a meia-largura do IC contra este piso.

### ✅ Proveniência, rastreada em 2026-09-22

A auditoria (`auditoria-pre-especificacao.md`, achado 5) apontou que este número
— o mais carregado do documento, porque decide entre *achado* e *limite superior*
— descendia de um bloco `[INSIGHT: ...]` sem citação. Rastreado até a fonte:

| elo | estado |
|---|---|
| **23–32 g** atribuído a Reynier & Rubin (2025) | ✅ **confere, verbatim** — *"reduced average birthweight by 23 to 32 g at the average level of glyphosate exposure"*, Discussão, PMC11761964. Estimativa central **29,8 g** à intensidade média de 2012 |
| 23–32 g → **15–25 g** (expectativa do pesquisador) | ⚠️ **juízo, não medida.** O ajuste para baixo supõe atenuação por substituição do avião pelo trator. Permanece hipótese declarada — mas agora é juízo contra âncora verificada, não contra número solto |
| 15–25 g → **piso de 15 g** | ✅ escolha estrita do extremo inferior, fixada antes do dado |

⚠️ **E o transporte da âncora tem um limite que a flag 2 já previa.** Reynier &
Rubin medem o efeito de **acrescentar** glifosato; aqui mede-se o de **remover**
um método de aplicação, e de outra classe química — procimidona e carbaril, não
glifosato. A âncora é **analógica**, e é assim que o texto tem de citá-la.

⚠️ **Dias, Rocha & Soares (2023) NÃO ancora magnitude em gramas.** O resultado
principal deles é **+5% de mortalidade infantil**; não há efeito de peso em
gramas no resumo. Eles são o template de *desenho*, não de magnitude.

### ⚠️ E a âncora verificada diz onde este desenho teria poder

Confrontando as duas magnitudes com o MDE de 33,4 g do cenário base:

| alvo de Reynier & Rubin | magnitude | o desenho detecta? |
|---|---|---|
| efeito **médio** | 23–32 g | ✘ abaixo do MDE |
| **decil inferior** de peso esperado | **75 g** | ✅ bem acima do MDE |
| exposição no percentil 90 | 146–243 g | ✅ |

O achado central daquele artigo é que o efeito se concentra **doze vezes** mais
no decil inferior. Se o mesmo padrão distributivo valer aqui, **este desenho tem
poder para a cauda vulnerável e não para a média** — e isso é caminho de
especificação, não consolo retórico.

⚠️ Mas é **exploratório**, não confirmatório: não foi declarado antes do dado, e
promovê-lo agora seria exatamente o que a §6 existe para impedir. Entra como
hipótese a pré-especificar para o próximo ciclo.

⚠️ **Trocar o piso depois de ver o IC inverte o sentido do teste.** Está fixado
aqui, com data.

**O que se escreve se o desenho não falsificar: limite superior informativo.**

✅ **E esta é a via escolhida para o problema de poder da §7 do gates doc.** O
MDE do cenário base para a banana é 33,4 g, acima do efeito esperado. As
alternativas foram consideradas e recusadas:

| via | por que não |
|---|---|
| ponderar por nascimento | ⚠️ **muda o estimando** — o alvo passaria a ser efeito por criança, não por município. É mudança de parâmetro-alvo, não de precisão |
| cortar por porte | ⚠️ **destrói o grupo tratado**: a mediana do decil superior da banana é 403 nascimentos/ano e só 3 de 17 têm ≥800 |

A via escolhida **não exige decisão metodológica nova** — exige apenas não
chamar de achado o que está abaixo do MDE do próprio desenho. É o compromisso
que a §4.6 do `paper/` já declara.

## 6. Multiplicidade — o núcleo do M1

**Confirmatório** — tudo que não estiver nesta lista é exploratório:

| # | Desfecho | Exposição | Hipótese e direção esperada |
|---|---|---|---|
| 1 | `peso_medio` | `share_gestacao_pos_ban` | `ACR(d) > 0` — remover a exposição aumenta o peso ao nascer, e o efeito cresce com a dose pré-ban |
| 2 | `taxa_obito_fetal` | `share_gestacao_pos_ban` | `ACR(d) < 0` — o ban reduz óbito fetal. ⚠️ **Entra por causa da flag 6**, não apesar dela: se só o peso for testado, a seleção para nascimento vivo fica indistinguível de efeito nulo |

**Correção de família: Holm**, aplicada às duas hipóteses acima.

Controla FWER sem a perda de potência do Bonferroni — e com poder curto cada
ponto conta. ⚠️ A correção **não** se estende ao exploratório: corrigir uma
família que não se declarou como confirmatória seria dar a ele estatuto que não
tem.

**Exploratório declarado:** os três `share_tri1/2/3`; o parâmetro `level`; a
definição 2 de `d = 0`; a janela 2010–2014; o canal A5 inteiro; `baixo_peso` e
`prematuridade`; e todos os recortes de molécula. Reportar exploratório como
exploratório é legítimo; reportá-lo como confirmatório não é.

⚠️ **O placebo NÃO conta como desfecho.** A série **intencional** do SINAN/IEXO
(`CIRCUNSTAN ∈ {10,11,12}` — suicídio, aborto, violência) entra como
**falsificação**: a hipótese prevê que ela **não** se mova. Declarar isso aqui é
o que impede que um movimento nela seja reinterpretado como achado depois.

⚠️ **E a fraqueza do placebo fica declarada:** 32,7% das notificações do SINAN
têm `CIRCUNSTAN` ignorada. O contraste existe sobre dois terços do dado.

**Fonte do canal A5: SINAN/IEXO**, não SIH. Em 2015–2022: 1.217 notificações de
agrotóxico agrícola e 5.130 não-intencionais, contra **1** internação acidental
no SIH em oito anos. Com 1 evento o canal não é estimável; com 1.217 é. O SIH
fica como série secundária — ele mede *caso grave internado*, que é outro
estimando, não um pior.

## 7. O que NÃO será feito

- ☑ **Não trocar o desfecho primário se o poder não fechar.** A saída é a §5:
  limite superior informativo.
- ☑ **Não descer de unidade geográfica.** O registro de residência materna do
  DATASUS não aguenta escala submunicipal.
- ☑ **Não reportar coeficiente abaixo do MDE do próprio desenho como achado.**
- ☑ **Não usar o canal-água como desfecho.** O SISAGUA tem quebra de registro no
  Ceará a partir de 2020 — detecções vão de 44 em 2019 para **zero** em
  2020–2022, com mais amostras, enquanto o Brasil segue reportando ~50% de
  resultados numéricos. Um DiD ali acharia que o ban eliminou 100% das
  detecções, e seria artefato de laboratório.
- ☑ **Não usar o teste de direção do vento.** Os alísios dão coerência 0,96
  entre estações: "a favor do vento" é colinear com "a oeste da fonte", que é
  geografia. O teste não separaria o que promete separar.
- ☑ **Não tratar `inconclusivo` como ausência.** Municípios cuja varredura
  legislativa não concluiu entram como desconhecidos, não como não-tratados.

## 8. Desvios

Qualquer desvio do acima entra nesta tabela, **com data e motivo**, e o texto
final reporta as duas versões.

| Data | O que mudou | Por quê | Resultado original preservado em |
|---|---|---|---|
| 2026-09-21 | `d = 0` primária: definição 2 → **definição 4** | A recomendação original era condicional — *"definição 2 porque 3 e 4 não estarão disponíveis"*. O FAO-GAEZ foi adquirido em 2026-09-21, 184/184 municípios. A restrição que justificava a 2 deixou de existir | A definição 2 é reportada como sensibilidade; `data/processed/gaez_aptidao_muni.parquet` e o commit `11c9dca` registram a aquisição |
| 2026-09-21 | Este documento passa a se declarar **plano pré-estimação**, não pré-registro | A janela de "nenhuma fonte tocada" fechou em 2026-08-25, e o git prova. Ver §0 | Histórico do git; `docs/gates-resultados-dados-reais.md` |
| 2026-09-22 | ⚠️ **Alvo primário: `slope` (`ACR(d)`) → `level` (`ATT(d\|d)`)** | A derivada agregada que o pacote reporta é **média simples sobre os pontos**, e é dominada pela faixa de dose < 0,1% — 48 dos 169 pontos — onde o erro-padrão supera a estimativa. A curva inverte de sinal ao longo da dose e nenhum ponto exclui zero em faixa alguma. O agregado, portanto, não é interpretável, e reportá-lo como resultado principal seria reportar um artefato de agregação. O `level` era a sensibilidade declarada na §4 e passa a principal | `data/processed/cgs_curva_slope__peso_medio__d0-4.csv` preserva a curva; a §6.2 do paper traz a decomposição por faixa. ⚠️ **Consequência para o Ensaio 2:** ele foi justificado *pela curva*, e a §7 do paper tem de dizer o que isso faz com a âncora de Weitzman |
| 2026-09-22 | Correção de fato: **"o SPT não é testável por placebo" → "o placebo não o isola, mas pode falsificá-lo"** | O CGS §6.3 propõe e **roda** verificação pré-tratamento que fala do SPT — a inclinação em dose do `ACRT^es` — e na aplicação dos próprios autores ela **rejeita**. A afirmação anterior era forte demais. Ver `docs/auditoria-pre-especificacao.md` achado 3 | O teste foi implementado em `scripts/estimate/10_spt_pretrend.py` e rodado: nenhum dos 3 cortes placebo rejeita. ⚠️ Mas os 3 produzem inclinação **maior em módulo** que a do desenho real |
| 2026-09-22 | Proveniência do **piso de 15 g** escrita na §5; o piso **não muda** | Ele descendia de bloco `[INSIGHT: ...]` sem citação. Rastreado: os 23–32 g de Reynier & Rubin **conferem verbatim** no texto completo (Discussão, PMC11761964), e não estavam no *abstract* porque o PNAS publica *Significance* ali. ⚠️ Dois documentos internos se contradiziam sobre isso e foram conciliados | `docs/referencias-verificadas.md` e `docs/justificativa.md`, ambos corrigidos com a localização. A decisão de 15 g permanece intacta — só a justificativa passou a existir |
| 2026-09-22 | A correção de **Holm** passa a existir de fato | A §6 a declarava desde o fechamento e **nenhuma linha a implementava** — a família confirmatória foi estimada sem correção até aqui. Ver auditoria, achado 1 | `scripts/estimate/09_holm.py`; `data/processed/holm_confirmatorios.csv`. Nenhuma hipótese rejeita a 5%, antes ou depois |
| 2026-09-23 | 🔴 **Correção de implementação: os placebos do script 10 usavam o pós-ban.** A linha de 2026-09-22 acima ("nenhum dos 3 cortes placebo rejeita") descrevia placebos que levavam 2019–2022 dentro | Achado da auditoria externa de 2026-09-23, conferido no código: o pseudo-pós era `t >= corte`, sem teto | Com a janela corrigida, nenhum rejeita também, mas os números mudam. O nível placebo vai de −8/−13 g para +18/+28 g. No óbito fetal, dois dos três placebos passam o desenho real em módulo. Os CSV antigos ficam em `docs/revisao/auditoria-2026-09-23/resultados/spt-original/`; `docs/ars/20-resposta-a-auditoria-2026-09-23.md` §1.2 |
| 2026-09-23 | ⬜ **Emenda metodológica proposta, a ratificar pelo pesquisador:** o critério da §5 ("meia-largura do IC contra o piso de 15 g") e o da §7 ("abaixo do MDE → limite superior") saem, e entram o teste do piso (benefício ≥ 15 g rejeitado se o limite superior do IC de 95% < +15) e o TOST a ±15 g | Largura não testa efeito mínimo: IC [20; 30] passaria e [−66,5; −5,9] não, embora o segundo exclua +15. E o MDE (≈ 2,8·EP) não classifica uma estimativa (a significância começa em 1,96·EP) | Os critérios antigos continuam escritos nas §§5 e 7. **Com o teste, o benefício ≥ 15 g no agregado é rejeitado** (p unilateral 0,002). Pela regra antiga, "não falsifica". As duas leituras vão para o texto |
| 2026-09-23 | Família de Holm **B, pós-resultado**, sobre o nível, ao lado da **A** original | A família da §6 é sobre o ACR, e o `09_holm.py` a testa pela inclinação. O nível virou principal em 2026-09-22, depois de ver a curva, e ficou sem correção. A B é **adaptativa**, e não confirmatória prospectiva | A família A continua como foi declarada. Na B, Holm bilateral de Welch dá 0,067 para o peso; o unilateral na direção prevista dá 1 |

---

## Como usar

1. ~~Preencher com o orientador~~ — preenchido em 2026-09-21. As escolhas de 1 a
   6 são as **D1–D7** do `docs/ars/08-briefing-orientador.md`.
2. Datar, assinar, **commitar**. Feito: o commit é o carimbo de tempo.
3. Só então rodar contra fonte real: `make real CULTURA="Banana (cacho)"`.

⚠️ **O que ainda bloqueia o E6**, e não é este documento:
- a escada de especificação do script 01 precisa rodar na janela ratificada;
- `03_contdid.R` nunca produziu coeficiente — a primeira execução real está por
  vir, e o `control_group` corrigido nunca foi exercitado ponta a ponta.
