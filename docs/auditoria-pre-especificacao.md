# Auditoria da pré-especificação

*Conferência da `docs/pre-especificacao.md` (fechada em 2026-09-21, commit
`c386514`) contra o código que a executa e contra os artigos que ela cita.
Feita em 2026-09-22, depois da estimação e da redação das §5–§6 do paper.*

---

## ⚠️ Sobre o método desta auditoria

**Não saiu de skill.** As três famílias que se cogitou usar — DiD, economia,
*academic research* — **não estão instaladas** nesta máquina; o que existe é
gstack. E a única skill de DiD já avaliada, `did-analysis`, tem veredito escrito
em `did-analysis-aderencia.md`: o workflow é organizado em torno de **variação
de timing**, e rodá-lo aqui produziria decomposição de Goodman-Bacon e event
study de aparência impecável e **errados**, porque este ban é simultâneo e o
tratamento é contínuo.

O que se fez foi conferir a pré-especificação contra (i) o código que a executa e
(ii) o texto dos artigos, lido direto da fonte.

**Fonte primária desta auditoria:** CGS, *Difference-in-Differences with a
Continuous Treatment*, arXiv:2107.02637, §3.2.1–3.2.2 e §6.3, lidos em
2026-09-22.

---

## Sumário: seis achados

| # | Achado | Gravidade | Estado |
|---|---|---|---|
| 1 | **A correção de Holm nunca foi implementada** | 🔴 alta | ✅ **resolvido** 2026-09-22 |
| 2 | **O alvo primário foi trocado sem entrar na tabela de desvios** | 🔴 alta | ✅ **resolvido** 2026-09-22 |
| 3 | **A camada de robustez não defende o parâmetro pré-especificado** | 🔴 alta | ✅ **resolvido** 2026-09-22 |
| 4 | A numeração das hipóteses do CGS está errada em todo o repositório | 🟡 média | ✅ **resolvido** 2026-09-22 |
| 5 | O piso de 15 g deriva de magnitude que o próprio repo marcou não-verificada | 🟡 média | ⬜ aberto |
| 6 | O paper não informa que o número reportado é a *sensibilidade* declarada | 🟡 média | ✅ resolvido junto com o 2 |

### O que a resolução dos quatro produziu

| achado | o que foi feito | resultado |
|---|---|---|
| 1 | `scripts/estimate/09_holm.py`, no `Makefile` e com 5 testes | Nenhuma hipótese rejeita a 5%, antes ou depois. **A correção não muda a conclusão — e agora isso é fato verificado, não expectativa** |
| 2 e 6 | Terceira linha na §8 da pré-especificação; parágrafo na §6.2 do paper **antes** do número | A troca de alvo deixa de ser silenciosa. ⚠️ A consequência para o Ensaio 2 fica registrada e pendente da §7 |
| 3 | `scripts/estimate/10_spt_pretrend.py` + nova §6.6 do paper | ⚠️ **Nenhum dos 3 cortes placebo rejeita — mas os 3 produzem inclinação MAIOR em módulo que a do desenho real** (25,8 / 31,1 / 13,0 contra 6,8). O ruído de pré-período supera o efeito estimado |
| 4 | Substituição em 66 linhas de 16 arquivos, com guarda para o "canal A5" | Zero `Assumption 4/5` remanescentes; as 4 ocorrências de "canal A5" intactas |

⚠️ **O achado 3 não deu o desfecho que se esperava, e isso importa.** A hipótese
de trabalho era que o teste pudesse *rejeitar*, o que converteria a troca de alvo
do achado 2 de escolha em exigência do dado. Ele não rejeitou. A defesa da §6.2
continua apoiada no argumento de não-interpretabilidade, que é bom mas é
argumento — não medida.

E o que o teste devolveu em lugar disso é um diagnóstico de poder mais duro que o
que já estava escrito: **o desenho não separa o efeito do ruído de pré-período
para o peso ao nascer.** Para o óbito fetal, separa — nenhum dos 3 placebos
alcança a inclinação real. A assimetria entre os dois desfechos é achado novo.

Os três primeiros são **da pré-especificação para o que foi feito** — quebras de
compromisso. Os três últimos são de **fidelidade ao que está escrito**.

---

## 1. 🔴 A correção de Holm nunca foi implementada

A §6 da pré-especificação declara, sem ambiguidade:

> **Correção de família: Holm**, aplicada às duas hipóteses acima.

E justifica: *"Controla FWER sem a perda de potência do Bonferroni — e com poder
curto cada ponto conta."*

**Não existe uma linha de Holm no repositório.** Busca por `holm|Holm` em
`scripts/` e `tests/` devolve zero ocorrências. Os dois confirmatórios foram
estimados e reportados **sem correção de família**.

### Por que importa mesmo com p alto

Os `p` reportados (0,736 / 0,757 / 0,793) não seriam salvos por correção alguma,
e é tentador concluir que o achado é inócuo. Não é, por dois motivos:

- **O compromisso era de procedimento, não de resultado.** Uma
  pré-especificação vale pelo que se cumpre quando o resultado é inconveniente.
  Cumprir só quando não muda nada é não ter procedimento.
- **A versão do desenho que "faria o desenho falar"** — encorpar o grupo tratado,
  §6.8 do paper — produz `p` menores. Holm passa a morder exatamente no cenário
  que o projeto declara querer alcançar.

### O que fazer

Implementar em `04_robustness.py` (ou script novo `09_holm.py`) a correção sobre
os dois `p` confirmatórios, com o procedimento sequencial explícito, e reportar
`p` bruto e `p` ajustado lado a lado. É meia hora de trabalho.

---

## 2. 🔴 O alvo primário foi trocado, e o desvio não foi registrado

A §4 da pré-especificação é explícita sobre qual é o parâmetro principal:

> **Parâmetro-alvo primário:** ✅ **`slope`** — a curva `ACR(d)`.
> [...] O `level` (`ATT(d|d)`) sai sob paralelismo tradicional e será reportado
> como **sensibilidade**.

E dá a razão de fundo: *"o Ensaio 2 precisa da curva — sem ela a comparação de
Weitzman perde âncora empírica e vira exercício teórico."*

**O que o paper reporta é o inverso.** A §6.2 traz o `ATT(d|d)` de −36,19 g como
o número do trabalho, e declara sobre o alvo pré-especificado:

> *O `ACR(d)` agregado não é interpretável, e isso é achado metodológico.*

A troca pode estar certa — o argumento da não-interpretabilidade é bom, e está
bem escrito. **Mas é exatamente o tipo de mudança que a §8 existe para
registrar**, e a §8 tem duas linhas, nenhuma delas esta:

| linha existente | assunto |
|---|---|
| 1 | `d = 0` primária: definição 2 → definição 4 |
| 2 | o documento se redeclara plano pré-estimação |

### ⚠️ E há uma consequência que passa despercebida

O Ensaio 2 foi justificado **pela curva**. Se a curva não é interpretável, a
âncora empírica de Weitzman não existe como planejada, e isso é matéria da §7 do
paper — que ainda não foi escrita. O desvio não é contábil: ele atravessa para o
segundo ensaio.

### O que fazer

Terceira linha na §8, com data de hoje, dizendo que o alvo primário passou de
`slope` para `level`, que o motivo é a não-interpretabilidade da derivada
agregada, e que o resultado original (`slope`) está preservado nos CSV
`cgs_curva_slope__*`. E uma frase na §7 sobre o que isso faz com o Ensaio 2.

---

## 3. 🔴 A camada de robustez não defende o parâmetro pré-especificado

Este é o achado metodológico, e ele tem duas partes: uma correção ao que o
repositório afirma, e uma lacuna que a correção abre.

### 3.1 A afirmação de que o SPT não é testável é forte demais

O repositório afirma, em pelo menos quatro lugares (`CLAUDE.md`,
`02-research-plan-summary.md` §b, `03-modelagem-ensaio1.md` §3.3,
`08-briefing-orientador.md`):

> *Nenhum event study de leads testa a A5, por mais limpo que saia.*

O raciocínio é bom e quase todo certo: o SPT envolve `Y₂(d)` — trajetórias sob
doses não recebidas — e no pré-período ninguém é tratado.

**Mas o CGS §6.3 propõe e roda uma verificação pré-tratamento que fala do SPT**,
e a descreve assim:

> *"Another indirect way to assess the plausibility of SPT that justifies a
> causal interpretation of ACRT^glob is to compute ACRT^es_glob(e), the
> event-study version [...] prior to treatment [...] both Assumptions PT and SPT
> have the same implication: that the average relationship between outcome
> changes for adjacent dose groups should be zero. **Our estimates of these
> pre-trends reject this in 1981, which is a pre-treatment period.**"*

Isto é: existe implicação pré-tratamento comum a PT e SPT, ela é **testável**, e
na aplicação dos próprios autores ela **rejeita**.

A formulação correta é mais estreita que a do repositório: o placebo
pré-tratamento **não isola** o SPT — passar não o valida, porque a implicação é
comum às duas hipóteses. **Mas pode falsificá-lo.** "Não distingue" e "não testa"
são coisas diferentes, e o repositório escreveu a segunda.

### 3.2 ⚠️ E o teste que foi feito não é esse

O que o projeto rodou — `pretrends` e `HonestDiD` — opera sobre o **event study
binário do TWFE**, em **níveis**. Isso fala da PT.

O teste que o CGS descreve é sobre a **inclinação em dose**: se a relação entre
*variação* do desfecho e dose é plana no pré-período. São objetos diferentes, e o
segundo nunca foi computado.

**Consequência:** a hipótese de que o alvo **pré-especificado como primário**
precisava — o SPT — é a única que não foi sondada. A §6.5 do paper chega perto de
dizer isso (*"é sobre o event study vizinho, não sobre a curva"*), mas não diz o
que importa: a camada inteira de robustez defende o parâmetro que a
pré-especificação chamava de sensibilidade, e não o que ela chamava de primário.

### O que fazer — e é barato

O teste **não depende do `contdid`**, e portanto não esbarra na limitação do
*sieve* CCK. Sobre o painel que já existe:

1. Restringir ao pré-período (até 2018-12).
2. Para janelas sucessivas, calcular `Δy` por município.
3. Regredir `Δy` sobre `dose` e testar inclinação = 0.
4. Rejeitar é evidência **contra** o SPT — e portanto contra a interpretação
   causal da curva.

Se rejeitar, a decisão de reportar o `level` em vez do `slope` (achado 2) deixa
de ser conveniência e passa a ser **exigida pelo dado** — o que é uma defesa
muito mais forte na banca do que o argumento de não-interpretabilidade sozinho.

---

## 4. 🟡 A numeração das hipóteses do CGS está errada

O repositório usa, de forma consistente, **"Assumption 4"** para paralelismo
tradicional e **"Assumption 5"** para *strong parallel trends*. Aparece em
`CLAUDE.md`, em quatro documentos `docs/ars/`, no roteiro de qualificação, no
briefing e nas mensagens que `03_contdid.R` imprime no console.

**O artigo não numera assim.** Lido em 2026-09-22 (arXiv:2107.02637):

| no artigo | é |
|---|---|
| Assumption 1 | Random Sampling |
| Assumption 2 | Treatment / Support |
| Assumption 3 | No-Anticipation |
| **Assumption 4** | **Continuous or Multi-Valued Discrete Treatment** — condição de suporte/regularidade |
| **Assumption PT** | Parallel Trends — **nomeada, não numerada** |
| **Assumption SPT** | Strong Parallel Trends — **nomeada, não numerada** |

E não existe Assumption 5.

⚠️ **A substância do repositório está certa** — e isso merece ser dito, porque o
erro é de rótulo, não de entendimento. O Teorema 3.1 identifica `ATT(d|d)` sob
PT; o Teorema 3.3 identifica `ACRT(d)` e `ATT(d)` sob SPT; o Teorema 3.2(b)
mostra que sob PT a derivada observada é `ACRT(d|d) + viés de seleção local`, que
é exatamente o que a §6.2 do paper argumenta. As citações verbatim que o
repositório reproduz conferem.

**Mas o rótulo é o que a banca abre o PDF para checar.** Quem procurar a
"Assumption 4" do CGS vai encontrar uma condição sobre o suporte da dose, e a
"Assumption 5" não vai encontrar. É possível que alguma versão anterior do
*working paper* numerasse assim; a versão corrente, que é a que o `.bib` aponta,
não numera.

### O que fazer

Substituição mecânica em todo o repositório: `Assumption 4` → `Assumption PT`,
`Assumption 5` → `Assumption SPT`, `A4` → `PT`, `A5` → `SPT`. Incluir as strings
de console do `03_contdid.R`, que hoje imprimem `-> ATT(d|d), sob Assumption 4`.

---

## 5. 🟡 O piso de 15 g apoia-se em magnitude não verificada — e o repo se contradiz

O piso de falsificação é **o número mais carregado da pré-especificação**: é ele
que decide se o trabalho escreve *achado* ou *limite superior informativo*. A §5
o apresenta como derivado da literatura:

> O extremo inferior da faixa de 15–25 g **registrada na Layer 3**.

Seguindo a cadeia para trás:

```
15 g (piso)
  ← 15–25 g  (02-research-plan-summary.md:154, bloco [INSIGHT: ...], SEM citação)
  ← 23–32 g  (atribuído a Reynier & Rubin 2025)
```

E sobre o último elo o repositório **já havia registrado a ressalva**:

> `referencias-verificadas.md:104` — *"a magnitude vem do material de projeto,
> **não** do abstract. Trocada pelo que consta: redução de peso e de duração
> gestacional, com efeito doze vezes maior no decil inferior."*
>
> `lacunas-de-dados.md:386` — *"⚠️ a magnitude '23–32 g' **não** consta do
> abstract."*

⚠️ **E `justificativa.md:191` ainda lista a mesma afirmação como `V` —
verificada.** Dois documentos do repositório dizem coisas opostas sobre a mesma
magnitude, e o piso de falsificação pende do lado que a própria auditoria de
referências marcou como não confirmado.

### Por que isto não invalida o que foi escrito

A §6 do paper reporta *limite superior informativo* — que é a conclusão
**conservadora**. Piso maior tornaria a falsificação mais fácil, não mais
difícil; o compromisso escolhido foi o estrito. Então o erro não contamina a
conclusão publicada.

**O que ele contamina é a defesa.** Perguntado na banca de onde vem o 15 g, o
trabalho hoje responde com um bloco de *insight* sem fonte, e com dois documentos
internos em desacordo.

### O que fazer

Ler Reynier & Rubin (2025) e Dias, Rocha & Soares (2023) pelo texto completo,
extrair a magnitude **com tabela e página**, e reescrever a §5 com a fonte. Se a
faixa mudar, o piso muda — e como o resultado já está escrito, a mudança entra na
§8 como desvio, com a versão original preservada. Conciliar
`justificativa.md:191` com `referencias-verificadas.md:104` no mesmo passo.

---

## 6. 🟡 O paper não informa que o número reportado é a sensibilidade declarada

Decorrência do achado 2, mas vale separado porque a correção é de uma frase.

A §6 do paper apresenta o `ATT(d|d)` sem dizer ao leitor que a
pré-especificação o designava como **sensibilidade**, e que o alvo primário
declarado era outro. Um leitor que abra os dois documentos encontra a troca
sozinho — e a encontra sem explicação, que é a pior ordem possível.

### O que fazer

Uma frase na §6.2, antes do número: dizer que o alvo pré-especificado era o
`ACR(d)`, que ele se mostrou não-interpretável pela razão que o parágrafo
seguinte expõe, e que o que se reporta é portanto a sensibilidade declarada,
promovida a principal — com o registro na §8.

---

## O que esta auditoria NÃO faz

- **Não reestima nada.** Nenhum número do paper foi recalculado; a auditoria é de
  procedimento e de fidelidade.
- **Não verifica as 40 entradas do `.bib`** uma a uma. Conferiu-se o CGS pela
  fonte e o Reynier & Rubin pelo registro interno. As demais seguem como estão.
- **Não roda o teste de inclinação pré-tratamento** do achado 3 — só especifica o
  procedimento.
- **Não decide** se o piso deve mudar. Isso depende da leitura das fontes, e a
  decisão é do pesquisador com o orientador.

---

## Ordem sugerida

| # | Ação | Custo | Por quê primeiro |
|---|---|---|---|
| 1 | Holm em `04_robustness.py` | ~30 min | compromisso explícito descumprido |
| 2 | Terceira linha na §8 + frase na §6.2 | ~15 min | o desvio existe e está sem registro |
| 3 | Substituição `A4/A5` → `PT/SPT` | ~15 min | mecânico, e é o que a banca confere |
| 4 | Teste de inclinação pré-tratamento em dose | ~2 h | **pode converter o achado 2 de escolha em exigência** |
| 5 | Rastrear 15–25 g até tabela e página | depende de acesso | conciliar os dois docs em desacordo |

Os quatro primeiros fecham dentro de uma sessão.
