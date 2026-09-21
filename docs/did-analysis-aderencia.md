# `did-analysis`: o que serve deste skill, e o que não serve

*Avaliação de aderência do skill `did-analysis`
([zhangxiany-tamu/DID](https://github.com/zhangxiany-tamu/DID)) ao desenho desta
dissertação. Escrito em 2026-09-21, contra o registro de pacotes do repositório
na data. Três pacotes foram adotados em `scripts/estimate/setup_r.R`; o workflow,
não.*

---

## O veredito, em um parágrafo

O skill implementa o workflow de cinco passos de **Roth, Sant'Anna, Bilinski &
Poe (2023)** — perfilar a estrutura do tratamento, diagnosticar TWFE, estimar com
robustez a heterogeneidade, poder de pré-tendências, sensibilidade HonestDiD.
É bem construído e é exatamente o [N9] do `estado-da-arte.md`. **E o workflow não
se aplica a este desenho**, porque os cinco passos são organizados em torno de
**variação de timing**, e o ban do Ceará é estadual e simultâneo: sanção em
08/01/2019, vigência em 09/01/2019, os 184 municípios de uma vez. Não há
escalonamento para perfilar, não há "bad comparisons" de Goodman-Bacon para
decompor, não há rollout para visualizar.

## ⚠️ O risco que isso cria

**Rodar `/did-analysis` neste painel não vai falhar.** O skill vai executar
`bacondecomp`, `did`, `panelView`, vai produzir um event study e uma decomposição
de aparência impecável — e tudo estará errado para este desenho, porque o
tratamento é **contínuo** e **não escalonado**. Saída plausível e errada é pior
que erro: erro você conserta, plausível você defende na banca.

O `CLAUDE.md` já registra a regra que isso viola:

> Callaway–Sant'Anna (2021), de Chaisemartin–D'Haultfœuille (2020) e
> Goodman-Bacon (2021) tratam variação de *timing*, não de dose — são referência
> conceitual, **não** os estimadores principais.

E o registro de pacotes do skill confirma o descasamento por omissão: dos 17
pacotes, **nenhum** é `contdid`, e **nenhum** é `ptetools`. Tratamento contínuo
não está coberto.

## O que foi adotado, e por quê

| Pacote | Preenche | Estado antes |
|---|---|---|
| **`pretrends`** (Roth) | poder do teste de pré-tendências | ausente — o projeto calculava MDE do *efeito* e nada sobre o poder do próprio placebo |
| **`HonestDiD`** (Rambachan & Roth) | sensibilidade a violações de tendências paralelas | ausente — mas já anotado no `estado-da-arte.md` [N10] como "munição defensiva de primeira" |
| **`synthdid`** (Arkhangelsky et al.) | o SDID agregado | **declarado não instrumentado** no roteiro E7, e nomeado no `CLAUDE.md` |

O `pretrends` é o que mais morde. Este desenho tem poder curto por admissão
própria — MDE do cenário base acima do efeito esperado de 15–25 g, piso amostral
de ruído em ≈17,7 g. Num desenho assim, **um teste de pré-tendências que "passa"
pode não informar nada**: ele passa porque não tem poder para detectar a
violação, não porque a violação não existe. A D1 inteira se apoia na
credibilidade desse placebo. Medir o poder dele deixa de ser refinamento e vira
pré-requisito.

### A ressalva que não dá para omitir

`HonestDiD` e `pretrends` operam sobre coeficientes de **event study**. E, pela
restrição do `contdid` v0.1.1 já verificada contra `R/cont_did.R`, o sieve não
faz event study (`if (aggregation != "dose") stop("event study not supported with
cck")`). Os *leads* saem de **outro estimador** que a curva.

> **Consequência:** a sensibilidade que esses dois pacotes entregam é sobre o
> objeto vizinho, não sobre o resultado principal. Isso não os torna inúteis —
> torna obrigatório que o texto diga de qual objeto ele está falando quando
> reportar a sensibilidade.

## O que ficou de fora, e a decisão é reversível

**`gsynth`** não entrou. Dois motivos, ambos registrados em comentário no
`setup_r.R` com a ordem de instalação que funciona, caso você discorde:

1. É desenhado para **múltiplas unidades tratadas** com efeitos fixos
   interativos. O plano B da D5 é Ceará contra um Ceará sintético — **uma**
   unidade tratada. O `synthdid` já cobre esse caso.
2. Importa `fect (>= 2.0.0)` **sem declarar `Remotes:`** — a mesma armadilha do
   `ptetools` que este repositório já documentou. E `fect` importa Rcpp, isto é,
   exige toolchain C++ (Rtools no Windows).

Os demais 13 pacotes do registro (`did2s`, `didimputation`, `staggered`,
`bacondecomp`, `TwoWayFEWeights`, `DIDmultiplegt`, `etwfe`, `panelView`…) são de
timing e não têm uso aqui.

## Proveniência

| Afirmação | Como foi conferida |
|---|---|
| Os 17 pacotes do registro, e a ausência de `contdid`/`ptetools` | `skill/references/package-index.md` do repositório, lido na íntegra |
| `pretrends` v0.1.0, GitHub-only, imports leves | `DESCRIPTION` em `jonathandroth/pretrends@master` |
| `HonestDiD` v0.2.8, importa CVXR e ECOSolveR | `DESCRIPTION` em `asheshrambachan/HonestDiD@master` |
| `synthdid` v0.0.9, importa só mvtnorm, autoria Arkhangelsky et al. | `DESCRIPTION` em `synth-inference/synthdid@master` |
| `gsynth` v1.4.0 importa `fect` sem `Remotes:`; `fect` v2.4.5 importa Rcpp | `DESCRIPTION` em `xuyiqing/gsynth@master` e `xuyiqing/fect@master` |
| Restrição de event study do `contdid` | `R/cont_did.R` do autor, já citada em `04-roteiro-qualificacao.md` §E6 |

⚠️ **O CRAN estava inalcançável** da sessão que escreveu isto (403 do proxy),
então a disponibilidade em CRAN de `HonestDiD` e `gsynth` **não foi conferida** —
o registro do skill afirma que estão lá. As linhas de instalação usam a rota do
GitHub, que foi verificada. Se `install.packages()` achar no CRAN, melhor: o
`renv.lock` passa a fixar versão em vez de commit.

⚠️ **Nada disto foi executado.** Não há R nesta sessão. As linhas novas do
`setup_r.R` têm fonte e dependência conferidas; a instalação, não.
