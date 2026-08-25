# Revisão metodológica do desenho, antes dos resultados

*Lente do `academic-paper-reviewer` do ARS, modo `methodology-focus`, aplicada ao
pipeline como construído. 2026-08-25.*

⚠️ **O que isto é e não é.** O plugin ARS **não está instalado nesta sessão** — o
repositório `imbad0202/academic-research-skills` foi clonado só para leitura. Não
houve invocação de `/ars-reviewer`. O que segue é o critério do
`methodology_reviewer_agent` — *"Can this paper's methods answer the questions it
poses? … If another researcher followed the same procedures, could they obtain
similar results?"* — aplicado por mim ao desenho. É revisão, não saída de
ferramenta.

Revisado: `CLAUDE.md`, `docs/ars/03`–`08`, e os sete scripts do pipeline.
**Não** revisado: resultados, porque não existem.

---

## O que já está coberto, e por isso não é achado

O desenho já registra e instrumenta: a não testabilidade da Assumption 5 e os
limites da §5.1; a aritmética de poder e o piso de falsificação; a contaminação
do `d = 0`; os três marcos de antecipação; a seleção para nascimento vivo; e a
lacuna de *enforcement*. Um revisor não precisa levantar nenhuma dessas — elas
estão nos documentos com endereço e, na maioria, com código.

O que segue são **quatro coisas que a revisão encontra e que não estão
registradas em lugar nenhum**.

---

## M1 — *Major.* 31 séries candidatas a desfecho, e nenhum plano de multiplicidade

O pipeline hoje produz, contando só o que já é coluna gravada:

| Fonte | Séries candidatas |
|---|---|
| SINASC (script 02) | 6 |
| SIM / óbito fetal (script 03) | 6 |
| SIH / intoxicação (script 04) | 19 |
| **Total** | **31** |

Some-se a isso: três definições de exposição por trimestre, quatro construções de
`d = 0`, e duas parametrizações de alvo (`level` / `slope`). O espaço de
especificações passa de mil.

**Por que isto é *major* e não zelo.** O desenho já sabe que o poder é curto — o
MDE agrupado no cenário base fica acima do efeito esperado de 15–25 g. Poder
curto **mais** espaço de busca grande é a combinação que produz achado espúrio
com aparência de rigor: basta um dos 31 se mover. E como cada série tem
justificativa teórica própria, a racionalização vem pronta depois do fato.

Nada nos documentos declara: **qual é o desfecho primário**, quais são
secundários, e o que se faz com a família de testes.

**O que fecha isto, e é barato.** Um documento de pré-especificação, escrito
**antes** de rodar contra dado real, declarando: (a) o desfecho primário —
`peso_medio` já está argumentado como o único com razão efeito/ruído acima de 1;
(b) a exposição primária — uma das quatro; (c) o que é confirmatório e o que é
exploratório; (d) se há correção de família e qual. O resto vira exploratório
declarado, o que é legítimo e honesto.

⚠️ Isto é decisão do pesquisador com o orientador — entra como **D7** na pauta do
`08-briefing-orientador.md`.

---

## M2 — *Major.* O estimador que produz o resultado principal é o único que **não** consegue mostrar a antecipação

Este é o achado que só aparece depois do E6, e ele é uma tesoura entre duas
restrições já documentadas separadamente.

1. O sieve (CCK) exige **exatamente dois períodos** → o "pré" vira **uma média
   única de 2015–2018**.
2. O PL 18/2015 foi apresentado em **24/02/2015** → **toda** a janela pré é
   posterior ao marco de notícia.
3. O sieve **não faz event study** → dentro da especificação principal não há
   *leads* que mostrem se a série já estava se movendo.

Juntas: **a média pré do estimador principal é potencialmente contaminada por
antecipação, e a especificação principal não tem como revelar isso.** O event
study existe, mas é outro estimador, outra agregação, outra rodada — então ele
não valida a curva; ele valida um objeto vizinho.

**O que fecha, em ordem de custo.** (a) Reportar o event study como pré-requisito
declarado da curva, dizendo explicitamente que são estimadores distintos.
(b) Rodar a curva também com pré recuado para 2010–2014, se a comparabilidade da
PAM permitir — é a **D4** do briefing, que ganha peso com isto. (c) Rodar a curva
com o pré partido (2015–2016 contra 2017–2018) e reportar a diferença como
medida da contaminação.

---

## M3 — *Moderate.* A retroprojeção gestacional não sobrevive à especificação principal

O E5 construiu `share_gestacao_pos_ban`, e ela é boa: mostra que marcar por data
de nascimento superconta 5/12 em 2019. Mas o colapso pré/pós do E6 **descarta as
coortes de transição e volta a um binário**. Ou seja: na especificação principal,
a retroprojeção sobrevive apenas como **regra de corte** — decide quais meses
jogar fora, não entra no estimador.

Isso não é erro; é consequência da restrição do pacote. Mas o texto não pode
apresentar a retroprojeção como parte do estimador principal quando ela é
critério de amostragem. E há um custo escondido: descartar as coortes de
transição joga fora ~9% das células, e são justamente as mais próximas do evento
— as de maior informação sobre timing.

**O que fecha.** Declarar a retroprojeção como o que ela é (regra de trimagem na
especificação principal, exposição contínua no event study) e reportar
sensibilidade a `--corte-pre` / `--corte-pos`, que já são parâmetros.

---

## M4 — *Minor, já corrigido.* A proveniência não atravessava a fronteira R

`04_robustness.py` grava `fonte` no CSV; **`03_contdid.R` não lia nem propagava**.
Um painel simulado podia ser estimado e o CSV de saída não diria isso.

Isso importa mais aqui que na média dos projetos porque **já aconteceu uma vez
nesta pesquisa**: um CSV simulado foi lido como real, e a resposta na época foi
justamente pôr proveniência dentro do arquivo, não só no nome. A fronteira R era
o furo restante.

✅ **Corrigido nesta rodada:** o script lê `fonte`, imprime aviso em bloco quando
o painel não é real, e propaga a coluna para todos os CSV de saída.

---

## Reprodutibilidade — o que passa e o que não

| Critério | Estado |
|---|---|
| Seeds fixas | ✅ `SEED = 20190613` nos cinco scripts Python |
| Ambiente declarado | ✅ `requirements.txt` + `renv.lock`, com `pyyaml` e `ptetools` já corrigidos |
| Fronteira Python/R por arquivo | ✅ e agora com proveniência atravessando |
| *Vintage* das fontes | ⚠️ `docs/fontes-e-vintages.md` existe e está **em branco** — nenhuma extração feita |
| Cobertura de teste | ✅ 85 testes; ⚠️ nenhum contra dado real |
| Ordem de execução documentada | ⚠️ os scripts são numerados, mas **não há um `make` ou runbook** que fixe a sequência 00→01→02→03→04→05→06→07 |

O último é barato e vale: sete scripts com dependências entre si, sem um alvo
único que os rode na ordem, é convite a rodar com painel velho.

---

## Veredito do revisor

**O desenho responde à pergunta que faz?** Sim, condicionalmente — e as condições
estão declaradas com honestidade acima da média: as hipóteses não testáveis estão
nomeadas, o poder está calculado antes de estimar, e o critério de falsificação
existe. Isso é raro e é a força do projeto.

**O que impede um "aceito" de método hoje** não é nenhuma dessas: é o **M1**. Um
desenho que declara honestamente que tem pouco poder e ao mesmo tempo mantém 31
desfechos em aberto está deixando a porta que ele mesmo fechou nas outras
paredes. Pré-especificar é a peça que falta, custa um documento, e tem de ser
escrita **antes** do primeiro contato com dado real — que, dado o bloqueio de
rede, é uma janela que ainda está aberta.

**Recomendação:** *Major revision* — endereçar M1 antes de qualquer rodada real,
e M2/M3 no texto do capítulo de identificação.
