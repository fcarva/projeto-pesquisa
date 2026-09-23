# 17 — Resposta ao parecer de 2026-09-22

*2026-09-23, sessão remota. O parecer está arquivado sem edição em
`docs/revisao/feedback-2026-09-22.md`: oito comentários pontuais e cinco blocos
gerais. Este documento diz, para cada item, se procede, o que muda e quem
decide. Também lê a conversa com outro assistente que o pesquisador colou, com
o que aproveitar e o que corrigir. Nada aqui foi aplicado ao paper: os textos
propostos (§7) esperam o pesquisador e o orientador.*

---

## 0. Veredito

**Os oito comentários procedem.** Nenhum é de gosto. Por natureza:

| # | tema | natureza da resposta | estado |
|---|---|---|---|
| 1 | mapeamento para Weitzman | reescrever a §7.2 | texto proposto (§7.6) |
| 2 | curvatura de custos | retirar a conclusão sobre `c` | texto proposto (§7.6) |
| 3 | permutação "exata" | texto + código | ✅ código (`0b864e5`), texto proposto (§7.2) |
| 4 | IC que exclui o zero × "compatível com o nulo" | texto + **cálculo local** | ✅ código (`0b864e5`); números saem do `make real` |
| 5 | §7.1 superestima a validação | texto | texto proposto (§7.4) |
| 6 | imprecisão × não identificação | texto | texto proposto (§7.6) |
| 7 | grupo nunca-tratado limpo | texto | texto proposto (§7.5) |
| 8 | poder de 80% não é exclusão | texto + cálculo opcional | texto proposto (§7.3) |

Dos blocos gerais, dois já estavam resolvidos antes do parecer chegar, e o
parecerista leu uma versão anterior. O paper **não diz mais** "17 de 19" nem
trata Limoeiro como vigente desde 2009 (commits `ee0b888`, `f91fffd`, e
`fa7c9bf` para a lei revogadora). Os outros três pedem **decisão** (§5).

---

## 1. O −36 g, relido: o que o comentário 4 abre

> **Revisto em 2026-09-23**, depois de uma crítica a esta seção que o
> pesquisador trouxe. A primeira versão tratava o VPP de 2006 como se fosse o
> tratamento de 2018 e dizia que o paper "já mantém" hipóteses que ele não
> mantém. As duas coisas procediam. O que segue é calibração sob hipóteses
> declaradas, não correção identificada do efeito.

O parecerista pediu inferência robusta sobre o próprio \(ATT(d\,|\,d)\). Ao
montá-la, apareceram quatro coisas que o paper não diz.

**1.1 O agregado é uma diferença de médias, e o lado escasso é o de
controle.** Isto está conferido no código, não só no argumento. No sieve (`cck`), o
`overall_att` do `contdid` não vem da curva: vem de `ptetools::pte_default`
sobre o painel colapsado (contdid `5cfec81`, `R/cont_did.R`, linhas 289–317,
o commit fixado no `renv.lock`). O `pte_attgt` do ptetools (`bda4aa5`,
`R/attgt_functions.R`) toma \(\Delta Y\) e chama `DRDID::drdid_panel` só com
intercepto e pesos iguais. Isso é a diferença de médias. Como o
`03_contdid.R` põe `g = 2` se dose > 0 e `g = 0` caso contrário (linha 319),
\(\text{overall\_att} = E[\Delta Y\,|\,D>0] - E[\Delta Y\,|\,D=0]\), sem
reponderação. É o DiD binarizado: **169 municípios com área positiva de banana
contra 15 de área nula** (14 pela definição 4). A variância é dominada pela
média dos 15. A §6.3 atribui a fragilidade do assintótico aos "dezessete
municípios de dose alta", mas no agregado o grupo escasso é o outro.

**1.2 Os estimadores reutilizam o mesmo pequeno grupo de controle.** O
\(ATT(d\,|\,d)\) compara os 169 com os 15. O event study do HonestDiD, o
synthdid, o controle sintético e o DiD simples comparam o decil superior (17)
com os mesmos 15. O grupo tratado e o estimando variam. O que muda a leitura da
§6.8 é mais limitado do que a primeira versão dizia: a concordância de sinais
não constitui quatro evidências independentes, porque todas as especificações
reutilizam o mesmo pequeno grupo \(d = 0\).

**1.3 Calibração: quão exigente seria ler −36 g como efeito diluído do ban.**
O Corolário 1 de Denteh & Kédagni dá \(\theta = VPP \cdot ATT\) para o
binarizado \(D>0\) contra \(D=0\). Para isso precisa de três hipóteses, e o
paper só mantém a primeira:

1. PT no \(D\) observado. É a hipótese de identificação do paper.
2. Nenhum falso negativo: ninguém no grupo \(d = 0\) exposto à prática
   proibida. O Censo 2006 a apoia para a aplicação agrícola por aeronave
   (flag 5). **Não a estabelece** para 2018, e ninguém mediu o controle
   vetorial aéreo que o §2º do art. 28-B também alcança (comentário 7).
3. O Censo 2006 classifica corretamente quem pulverizava por avião na véspera
   da lei. É **hipótese forte**. O dado tem treze anos de defasagem, conta
   estabelecimentos e não voos, e admite subdeclaração (§§5.4 e 7.4 do paper).

Sob essas hipóteses, e só sob elas, 7 dos 169 municípios com área positiva
seriam verdadeiros positivos, e \(VPP = 7/169 = 4{,}1\%\):

| calibração pela classificação de 2006 | conta | resultado |
|---|---|---:|
| efeito implícito nos verdadeiramente tratados, agregado dos 169 | −36,19 / (7/169) | ≈ −874 g |
| o mesmo, no decil (2 de 17) | −36,19 / (2/17) | ≈ −308 g |
| teto de \(\lvert\theta\rvert\) no agregado, com δ = 150 g (topo de Calzada et al. 2023) e **toda** a população exposta (f = 1) | (7/169)·1·150 | ≈ 6 g |
| teto no decil, mesmas hipóteses generosas | (2/17)·1·150 | ≈ 18 g |
| VPP de 2018 que reconciliaria −36 g com δ = 150 g e f = 1 | 36,19/150 | ≥ 24%, ou 41 dos 169, contra 7 em 2006 |

Essa magnitude torna difícil interpretar −36,19 g como mera versão atenuada de
um efeito sanitário plausível: exigiria ~870 g por nascimento exposto, seis
vezes o topo do análogo mais próximo (80–150 g, Calzada et al. 2023, pelo
resumo). **O cálculo não identifica o efeito verdadeiro**, porque o Censo de
2006 não estabelece o status de tratamento em 2018. O que ele mede é quão
exigente teria de ser a atualização da pulverização aérea para reconciliar a
estimativa com a interpretação causal pretendida.

Na calibração baseada em 2006, **quatro explicações permanecem**, e o paper
não tem como distingui-las:

- o Censo deixou de representar a distribuição da pulverização até 2018, por
  crescimento da aviação agrícola, subdeclaração ou operações que a contagem de
  estabelecimentos não capta;
- o coeficiente reflete diferenças de trajetória entre municípios com e sem
  área de banana, isto é, violação de PT na margem extensiva;
- a inferência assintótica subestima a incerteza produzida pelos 15
  controles;
- houve exposição omitida no grupo de comparação, por exemplo por controle
  vetorial aéreo. Aí o Corolário 1 não vale, e a Proposição 1 admite \(\theta\)
  negativo mesmo com efeito protetor: se o ban removeu exposição dos
  controles, eles melhoram mais que os tratados.

**O cadastro operacional pré-banimento (LAI à ADAGRI) é o dado que distingue
as quatro.** As três primeiras se testam em parte com o que o `make real` já
produz (jackknife, perfil, placebos de nível). A quarta, não.

**1.4 O perfil por faixa de dose: diagnóstico descritivo.** O nível dá −36 g;
a inclinação em dose dá +6,81 g por unidade de dose normalizada. Um
deslocamento de nível entre \(D=0\) e \(D>0\) sem gradiente entre as doses
positivas é mais compatível com uma diferença entre municípios com e sem
banana do que com uma resposta crescente à intensidade. O perfil mostra onde
está a variação, mas não identifica a origem dela. ⚠️ A inclinação do paper
também não é só entre doses positivas: `estima` regride sobre **todos** os
municípios, zeros incluídos, e herda parte do deslocamento do grupo zero
(teste `test_perfil_mostra_quando_o_nivel_e_so_o_zero`).

**1.5 E o "limite superior informativo" não limita o efeito da
pulverização.** O intervalo do coeficiente limita o efeito de forma reduzida
da proibição segundo a área de banana. Ele não limita o efeito entre os
municípios efetivamente expostos à pulverização aérea. Na mesma calibração
condicional de 2006, \(\lvert\theta\rvert \le 66{,}5\) g corresponderia a
\(\lvert ATT\rvert \le 66{,}5 / 0{,}041 \approx 1.600\) g nos verdadeiramente
tratados, um limite sem conteúdo. O número herda todas as hipóteses do §1.3. O
ponto conceitual não depende delas: é o que o comentário 5 e o primeiro bloco
geral dizem.

**Síntese.** O coeficiente não tem interpretação causal plausível como efeito
diluído da retirada da pulverização aérea sob a classificação observada em
2006. Como essa classificação não mede o tratamento verdadeiro em 2018, o
exercício calibra a severidade do erro de mensuração. Não é correção
identificada do efeito.

### O que já roda (commit `0b864e5`)

`make real` passa a produzir, sem mudar nada no fluxo:

| saída | o que traz |
|---|---|
| `robustez_inferencia.csv`, colunas `nivel_*` | o nível, com EP de Welch, wild bootstrap com nulo imposto, permutação do rótulo (studentizada, dita análise) e jackknife dos controles, com o código de quem move o número |
| `robustez_perfil_dose.csv` | \(\Delta Y\) médio no zero e nos terços da dose positiva |
| `robustez_inferencia.csv`, `ic_inv_*` | o IC da inclinação por inversão do teste, feita de fato (§2, comentário 3) |
| `spt_pretrend__<desfecho>.csv`, coluna `nivel` | o nível em cada corte placebo do pré-período |

E, fora do `make real`, a permutação condicional à aptidão:

```powershell
python scripts/estimate/04_robustness.py --painel data/processed/painel_ensaio1.parquet `
  --estratos-aptidao 3 --out-dir data/processed/estratos3
```

⚠️ **Conferência de consistência antes de usar:** o `nivel` do 04 tem de bater
com os −36,19 g do `03_contdid.R`. A identidade foi conferida no código (§1.1),
então uma diferença só pode vir da amostra: `BMisc::make_balanced_panel` no R
contra o `dropna` de `primeira_diferenca` no Python, ou janelas de pré e pós
diferentes. É o primeiro lugar a procurar, antes de usar qualquer número do
nível.

---

## 2. Comentário a comentário

### 1 — O mapeamento para Weitzman não segue dos estimandos ✔ procede

Os três erros apontados são reais: \(ATT(q\,|\,q) \neq ATE(q)\), a derivada de
\(\lvert f\rvert\) é \(\mathrm{sgn}(f)\,f'\), e a dose municipal não é a
quantidade de abatimento que o regulador escolhe. Há um quarto, que o parecer
não nomeia. **O ban é uma cota fixada em zero sobre o método aéreo**, isto é,
uma solução de canto. A comparação de Weitzman é entre o preço e a quantidade
**ótima esperada**, via aproximação quadrática local em torno de \(q^*\). A
proibição só coincide com o instrumento-quantidade de Weitzman se o ótimo
esperado for o canto. E banir um método é padrão tecnológico, não teto de
emissão (Helfand 1991, *standards versus standards*). Resposta: a §7.2 deixa
de inserir estimandos na regra e passa a listar o que a regra exigiria, e quais
desses objetos o Ensaio 1 informa (texto na §7.6).

### 2 — A curvatura de custos não decorre da heterogeneidade ✔ procede

Heterogeneidade do prêmio de conversão é uma fonte de \(C''\) entre várias:
custo marginal crescente dentro do produtor, custo fixo, indivisibilidade,
capacidade e escala. E custo contábil de sistemas que **escolheram** avião ou
trator não identifica o custo contrafactual de converter quem usava avião. Há
seleção: quem escolheu avião é, plausivelmente, quem tinha trator mais caro
(terreno, porte, solo encharcado). A frase "\(c\) tende a zero" sai. Os dados
da Conab ficam para o que dão, que é a ordem de grandeza do custo do ban
(~1,5% do custo de produção), e não \(c\).

### 3 — A permutação da dose carece de mecanismo de atribuição ✔ procede, código já mudou

A permutação seria exata se a dose tivesse sido atribuída de forma
intercambiável. Não foi: segue aptidão e geografia. O código mudou em três
pontos:

1. **"exata" sai** das docstrings e do relatório, e a hipótese de
   intercambiabilidade entra. É análise de permutação (Canay, Romano & Shaikh
   2017).
2. **`--estratos-aptidao K`** permuta dentro de faixas de aptidão GAEZ. A
   hipótese passa a ser intercambiabilidade condicional à aptidão. É mais fraca,
   mas continua sendo hipótese, e o texto tem de dizê-lo.
3. **O IC "por inversão" do paper era atalho**: \(\hat\beta\) menos os quantis
   da distribuição de referência. A inversão feita de fato, `ic_inversao`, usa
   \(\text{slope}(\Delta Y - \beta_0 d,\ d_\pi) = a_\pi - \beta_0 b_\pi\). O
   atalho supõe \(b_\pi = 0\), ou seja, dose permutada sem correlação com a
   verdadeira. Num painel sintético de teste, atalho e inversão diferiram em
   até ~15 g nas bordas. **O \([-46{,}45;\ +57{,}85]\) do paper tem de
   ser recalculado.** O p-valor não muda: sem estratos, a sequência de
   sorteios é a de sempre (teste de regressão).

### 4 — Compatibilidade com o nulo em conflito na §6.2 e §7.1 ✔ procede, e é o mais consequente

Ver §1. Duas correções de texto são obrigatórias. **O IC do \(ATT(d\,|\,d)\)
exclui o zero, e o texto tem de dizer isso**, em vez de chamá-lo de
"compatível com efeito nulo". E as conclusões ficam **separadas por estimando e
procedimento**: nível pelo multiplicador, nível pela inferência que respeita os
15 controles, inclinação pelos três procedimentos, event study binário pelo
HonestDiD. O que justifica não tratar o −36 g como achado não é "compatível com
zero". São três razões, escritas na §7.1: precisão abaixo do critério ex ante,
inferência no mesmo estimando (números do `make real`) e a calibração pela
classificação de 2006, que torna implausível lê-lo como efeito diluído do ban.
A calibração é condicional a hipóteses fortes (§1.3) e não substitui a
inferência.

### 5 — A §7.1 superestima a validação da dose ✔ procede

"Identificação fechada" e "dose verificada contra o dado" não se sustentam
depois do Censo Agro: 15 dos 17 do decil sem aeronave, 7 dos 169 no agregado. A
concordância entre MDE previsto (33,4 g) e meia-largura realizada (30,3 g)
valida o diagnóstico **amostral** da especificação, e só ele. Texto na §7.4.

> ⚠️ **ERRATA de 2026-09-23 (auditoria externa):** a frase acima está errada. MDE
> (≈ 2,8·EP) e meia-largura (1,96·EP) são objetos diferentes: 33,4 g de MDE
> implicam 23,4 g de meia-largura, e 30,3 g de meia-largura implicam 43,3 g de
> MDE. E os dois vêm de contrastes diferentes (17 × 167 contra 169 × 14). A
> concordância não valida nada. Ver `docs/ars/20-resposta-a-auditoria-2026-09-23.md` §3.1.

### 6 — A §7.2 confunde imprecisão com não identificação ✔ procede

A curva é identificada sob SPT, que é hipótese mantida e só falsificável. O que
falta é precisão e credibilidade da SPT. Intervalos pontuais que cobrem o zero
não mostram que \(ACR'\) seja irrestrito: isso exigiria inferência para
derivadas, com bandas uniformes e hipótese de suavidade. A frase honesta é que o
Ensaio 1 **não produz informação utilizável sobre \(\beta\) com a precisão
obtida** (Lewbel 2019 dá a linguagem). Texto na §7.6.

### 7 — O grupo limpo não está estabelecido na §6.5 ✔ procede

Adoção simultânea afasta o viés das comparações entre coortes, e só isso. A
limpeza do nunca-tratado é hipótese: o Censo 2006 a apoia para aplicação
agrícola por aeronave, mas não mede controle vetorial aéreo (§2º do art. 28-B).
E, pelo §1, o peso dessa hipótese é maior do que o paper admite, porque os 15
municípios de área nula sustentam **sozinhos** todos os níveis da §6. Texto na
§7.5.

### 8 — Poder de 80% não permite exclusão na §6.4 ✔ procede

Poder de 80% contra 11,4 g acumulados significa que uma tendência desse
tamanho passaria despercebida em uma de cada cinco amostras. Tampouco limita
violação não linear. Texto na §7.3. O cálculo que autoriza a palavra
"descartar" é o de Bilinski & Hatfield (2026): o IC de 95% da diferença entre o
ATT sob paralelismo e o ATT com tendência linear diferencial. Valores fora dele
são vieses que o dado descarta a 95%. ⬜ Não implementado: exige reestimar o
event study binário com e sem a tendência diferencial, com bootstrap por
município para a covariância. Proposto como próximo passo, se o orientador
quiser a frase de exclusão de volta.

---

## 3. Blocos gerais

**Mensuração e diluição.** ✅ Formalizado no doc 16: Corolário 1, \(\theta =
VPP\cdot ATT\), atenuação pura e calibração. O paper ainda trata a diluição
como "leitura concorrente" à falta de poder (§6.8). Ela é o **mecanismo** da
falta de poder. E a §6.8 ainda recomenda "encorpar o grupo tratado, baixando o
corte de dose", que o doc 16 §7 mostrou **piorar** o VPP: os próximos da fila
são serra e sertão. O parecerista chegou à mesma conclusão por conta própria.
⬜ Reescrever a §6.8 (parágrafo "O que faria o desenho falar").

**GAEZ: instrumento ou construção de controle.** ✔ procede. Hoje a aptidão
entra como checagem de relevância (primeiro estágio descritivo, doc
gates §7-quater) e como construção do \(d = 0\) (definição 4). Nenhum estimando IV é
estimado. **Recomendação:** alinhar a linguagem da Introdução e da §5.3 ao que
se faz, e manter o IV como extensão declarada, com estimando e restrição de
exclusão próprios. Há razão substantiva para não correr ao IV: aptidão
agroclimática no semiárido correlaciona com disponibilidade de água, e escassez
de água afeta desfechos ao nascer diretamente (Rocha & Soares 2015). A
exclusão é frágil exatamente onde o Ceará está. ⬜ **Decisão do pesquisador com o
orientador**: é linguagem da estratégia de identificação (CLAUDE.md, "perguntar
antes").

**Janela da dose anterior à notícia.** ✔ procede, e o paper já tem a janela
2010–2014 como sensibilidade (§7.4 da conclusão). Promovê-la a principal é
mudança de pré-especificação. ⬜ Decisão. Duas ressalvas para a reunião: (i)
2010–2014 entra na seca de 2012–2017, e a área de banana responde à água, de
modo que as duas janelas carregam seca; (ii) vale medir antes a correlação de
postos entre as doses das duas janelas. Se for alta, a troca é de rótulo; se for
baixa, o grupo tratado muda, e com ele o VPP.

**Regra inferencial.** Coberto pelos comentários 3 e 4 e pelo §1.

**Cronologia legal e vintage.**

| discrepância apontada | leitura | estado |
|---|---|---|
| Limoeiro vigente desde 2009 × revogação "não pacificada" | revogada pela **Lei 1.511, de 26/05/2010**, num artigo do corpo | ✅ `fa7c9bf`; ⬜ texto integral (5 min local, doc 14 §3-bis) |
| 17 × 19 tratados | 17 é o grupo dos estimadores; 19 era outra conta | ✅ doc 16 §1 |
| 17.664 × 17.654 células | **não é discrepância**: 184 × 96 = 17.664 no painel balanceado, e 17.654 células têm nascimento. As 10 vazias dão a cobertura de 99,9% (doc gates §7-ter) | ✅ explicar na legenda |
| 3.208 × 3.211 g | provavelmente média das médias de célula × média individual dos 1.001.709 nascimentos | ⬜ conferir e rotular na Tabela de descritivas |
| SINASC até 2022 com 2023–2024 disponíveis | procede: o FTP tem a série consolidada de 2007 a 2024 para o CE (doc gates §7-bis.4, resolvido em 2026-09-22), e a janela principal do CLAUDE.md já vai a 19/12/2024. O painel para em 2022 só porque `ANOS_PADRAO` do script 02 pede. A §7.5 da conclusão ainda trata a disponibilidade como dúvida | ⬜ decisão de vintage com o orientador: estender `ANOS_PADRAO` até 2024 (truncado em 19/12), refazer painel e MDE, congelar com data de extração em `docs/fontes-e-vintages.md` |

---

## 4. A conversa com o outro assistente

É útil como mapa de literatura. Seis pontos estão errados ou desatualizados:

1. **A fórmula de Weitzman.** Ela escreve
   \(\Delta W \approx \sigma^2(\beta - c)/[2(c+\beta)]\). O denominador está
   errado. No modelo linear-quadrático de Weitzman (1974), com choque aditivo
   de variância \(\sigma^2\) no custo marginal,
   \(E[W_P] - E[W_Q] = \sigma^2 (c - \beta)/(2c^2)\). É o que
   `scripts/estimate/11_weitzman_inversao.py` implementa (linha 102). O sinal e
   o limiar \(\beta = c\) coincidem; a magnitude não.
2. **Bilinski & Hatfield.** A conversa atribui o artigo a *Epidemiology* 31(5),
   2020. A versão publicada é **"Nothing to See Here? A Non-Inferiority Approach
   to Parallel Trends", *Statistics in Medicine* 45(3–5), 2026,
   doi:10.1002/sim.70296** (conferido no Scholar Gateway/Wiley). O título que a
   conversa usa é o do preprint.
3. **"17 dos 19".** É a conta antiga. São 15 de 17 no decil e 7 de 169 no
   agregado.
4. **O "experimento" de Limoeiro 2009.** A premissa falha. O ban municipal
   durou seis meses: foi revogado pela Lei 1.511 em maio de 2010. A predição de
   que "Limoeiro, já tratado, não deveria apresentar nova ruptura" em 2019 é o
   contrário do que vale, porque Limoeiro e Quixeré são tratamento genuíno em
   2019. Seis meses num município só também não dão desenho próprio.
5. **Hitzig.** A conversa supõe que *normative gap* seja a distância entre
   evidência positiva e recomendação normativa, e avisa que está supondo. Não é
   isso. Hitzig (2020, *Economics and Philosophy* 36(3):407–434) chama de
   normative gap a distância entre **os objetivos de quem faz a política e os
   objetivos que o economista embute no desenho**, e argumenta que o desenho
   pode obstruir os primeiros. Ver §6.
6. **Drones e a regra federal.** A conversa discute a exceção cearense de 2024
   e omite a **Portaria MAPA nº 298, de 22/09/2021**, que regula a aplicação de
   agrotóxicos por aeronave remotamente pilotada em todo o país (conferida no
   gov.br). Consequência nova para a **Rota 1**: nos estados vizinhos, a
   aplicação por drone é regulada desde setembro de 2021, e no Ceará a Lei
   16.820 a vedava até a Lei 19.135/2024 (o art. 28-B original vedava "a
   pulverização aérea", sem exceção; a exceção para ARP/VANT/drones é a
   redação de 2024, `docs/legislacao/lei-12228-1993-consolidada.md`). O
   controle potiguar da fronteira não é "sempre terrestre" depois de 2021, e o
   pós-período da fronteira tem controle que se move. ✅ Registrado no doc 16
   §8.

Um ponto menor: Lewbel (2007) é a referência clássica de tratamento binário mal
classificado, mas identifica com uma variável auxiliar. Aqui a estrutura sem
falso negativo dá identificação pontual dado o VPP (Corolário 1). Lewbel entra
como contexto, não como método.

**O que aproveitar:**

- **Helfand (1991)**, padrão sobre insumo ou tecnologia contra padrão sobre
  emissão. É o enquadramento certo do ban para o Ensaio 2. E o `.bib` já tem
  Helfand & House (1995), sobre poluição difusa com heterogeneidade.
- **Segerson (1988)**, poluição difusa: o regulador não observa a contribuição
  individual. O instrumento depende do que se monitora, não só de \(B''\) e
  \(C''\).
- **Goulder & Parry (2008)** e **Hepburn (2006)**, Weitzman como caso de
  referência dentro da escolha de instrumento.
- **Malani & Reif (2015)**, antecipação lida como pré-tendência, que é
  diretamente a ameaça dos três marcos (doc 06).
- **Ferman & Pinto (2019)**, poucos grupos e heterocedasticidade. ⚠️ Aqui o
  grupo escasso é o de controle (§1.1). A lógica de Conley–Taber e
  Ferman–Pinto usa o grupo numeroso para aprender a distribuição do erro do
  escasso. Com os papéis invertidos, os 169 ensinariam o erro da média dos 15.
  É um candidato natural para a inferência do nível. ⬜ Decisão com o orientador.
- **Assunção, Gandour & Rocha (2023)**, lei ≠ fiscalização ≠ cumprimento, que
  é a flag 3 com template brasileiro.
- **Drones**: os três estimandos que ela separa (ITT da reforma de 2024,
  efeito da adoção, dose-resposta do uso) estão certos, e a conta das coortes
  também. Gestação inteira sob a nova regra só nasce a partir de ~out/2025, e
  SINASC 2025 consolidado não sai antes de 2027. **Nada disso é estimável na
  dissertação.** A janela principal já corta em 19/12/2024 (CLAUDE.md).

---

## 5. O que depende de decisão (para a reunião)

1. **Estimando declarado.** Forma reduzida do ban segundo a proxy de
   intensidade da bananicultura (recomendado, e é o que o §1.5 mostra ser o
   único que o desenho limita). A alternativa seria dose-resposta da
   pulverização aérea. Pela calibração de 2006 (VPP ≈ 4%) ela exigiria o
   cadastro operacional pré-banimento para se sustentar.
2. **GAEZ**: linguagem de construção de controle agora, IV como extensão
   declarada (§3).
3. **Janela da dose**: 2010–2014 como principal ou sensibilidade (§3).
4. **Vintage**: SINASC até 2024 e congelamento com data (§3).
5. **Inferência do nível com 15 controles**: Conley–Taber/Ferman–Pinto
   invertido como procedimento principal? (§4)
6. **Ensaio 2**: suficiência informacional + padrão tecnológico (Helfand) +
   normative gap (§6), no lugar de ancorar em \(ATT(d\,|\,d)\).

---

## 6. Hitzig, lido pelo que o artigo diz

Hitzig (2020) mostra que o desenho econômico costuma adotar um objetivo
próprio, como eficiência ou bem-estar esperado, enquanto quem faz a política
persegue outro, por exemplo uma teoria de justiça. O desenho pode então
obstruir o objetivo de quem o encomendou. Sönmez (2024, *minimalist market
design*, arXiv:2401.00307) propõe a resposta construtiva: tomar os objetivos do
formulador como primitivos e desenhar o mínimo que os realize.

**Adaptação ao Ensaio 2.** A regra de Weitzman compara instrumentos pelo
excedente esperado. A Lei 16.820 e o STF, ao validá-la na ADI 6137, raciocinam
em outros termos: saúde, meio ambiente, precaução e exposição involuntária de
terceiros. ⬜ Os fundamentos exatos do acórdão ainda não foram lidos, e a
petição e o acórdão estão pendentes em `docs/legislacao/`. Ranquear proibição e
taxa por \(E[W]\) responde a uma pergunta que o legislador não fez. Esse é o
normative gap do Ensaio 2.

**Pergunta minimalista.** Dado o objetivo declarado da lei (exposição aérea
zero), qual instrumento o realiza com menor custo e maior confiabilidade sob
incerteza? Sob esse critério, a comparação com a taxa passa a ser de
custo-efetividade e de confiabilidade. Uma taxa não garante exposição zero com
custos incertos, e é justamente o ponto de Weitzman lido ao contrário. Isso
aproxima o Ensaio 2 do que a lei é, sem pedir ao Ensaio 1 a curvatura que ele
não tem. A redação que a outra conversa propõe para a §3.4 é aproveitável se
trocar "evidência positiva × recomendação normativa" por "objetivo do
formulador × objetivo do desenho".

---

## 7. Textos propostos (não aplicados)

> ⚠️ **ERRATA de 2026-09-23 — 7.1 e 7.4 foram substituídos pelo doc 20 §7.**
> A primeira razão do 7.1 ("a meia-largura é o dobro do piso") não é razão:
> largura não testa efeito mínimo, e, testado como teste, o piso de 15 g é
> rejeitado pelo −36,19 g. O fecho do 7.4 compara MDE com meia-largura. Os
> colchetes do 7.1 e do 7.2 já têm número (doc 20 §1.1). Os dois textos ficam
> abaixo como registro, e **não devem ir para o `.tex`**.

Em português, prontos para ir ao `.tex`. Os números entre colchetes saem do
`make real`.

### 7.1 §6.2 — o parágrafo do −36 g (comentário 4)

> O \(ATT(d\,|\,d)\) agregado é de \(-36{,}19\) g, com erro-padrão de 15,47 g
> pelo \emph{bootstrap} multiplicador e intervalo de 95\% em
> \([-66{,}51;\ -5{,}87]\), que exclui o zero. Três razões impedem tratá-lo
> como achado, e nenhuma delas é compatibilidade com o nulo. A primeira é o
> critério fixado antes de olhar: a meia-largura, de 30,32 g, é o dobro do
> piso de 15 g. A segunda é a inferência. O agregado é a diferença entre a
> variação média dos 169 municípios com área positiva de banana e a dos 15 de
> área nula, e com quinze controles o multiplicador é otimista. No mesmo
> estimando, o \emph{wild bootstrap} dá \(p = [\cdot]\), a análise de
> permutação dá \(p = [\cdot]\), e retirar um único controle move o número
> entre \([\cdot]\) e \([\cdot]\) g. A terceira é uma calibração. Suponha-se
> que o Censo Agropecuário de 2006 classifique corretamente os municípios que
> pulverizavam por avião na véspera da lei e que não haja exposição omitida no
> grupo de comparação, inclusive por controle vetorial. Sob essas hipóteses
> fortes, 7 dos 169 municípios com dose positiva seriam verdadeiros
> positivos, e a identidade de correção por classificação incorreta
> \citep{denteh2022misclassification} implicaria um efeito de
> aproximadamente \(-874\) g entre os verdadeiramente tratados, seis vezes o
> maior efeito do análogo mais próximo \citep{calzada2023bananas}. Essa
> magnitude torna difícil ler o coeficiente como versão atenuada de um efeito
> sanitário plausível. O cálculo não identifica o efeito verdadeiro, porque o
> Censo de 2006 não estabelece o status de tratamento em 2018. O que ele mostra
> é quão exigente teria de ser a atualização da pulverização aérea para
> reconciliar a estimativa com a leitura causal pretendida.

### 7.2 §6.3 — a permutação (comentário 3)

> A lógica é a de \citet{conley2011}: não confiar no assintótico quando as
> unidades tratadas são poucas. O procedimento é permutar a dose entre
> municípios, e o resultado é análise de permutação, não inferência exata. A
> exatidão exigiria que a dose tivesse sido atribuída de forma intercambiável.
> A dose é área de banana, que segue aptidão e geografia, e a hipótese não
> vale globalmente. Restrita a faixas de aptidão, a permutação supõe
> intercambiabilidade condicional, que é mais fraca e ainda é hipótese: \(p =
> [\cdot]\). O intervalo de 95\% por inversão do teste é \([\cdot;\ \cdot]\)
> para a inclinação em dose, que é outro estimando que o nível da §6.2.

### 7.3 §6.4 — o placebo (comentário 8)

> O teste conjunto dos \emph{leads} tem poder de 80\% contra uma tendência
> linear de 0,238 g por mês, que acumularia 11,4 g em quatro anos de
> pós-tratamento, e de 90\% contra 0,429 g por mês (20,6 g). O placebo não
> rejeitou. Isso é compatível com tendências menores que essas e, em uma de
> cada cinco amostras, com tendências daquele tamanho. Nada diz sobre
> violações não lineares. Não se escreve, portanto, que o placebo exclua
> vieses de 11 g: escreve-se que ele os detectaria quatro vezes em cinco, e
> 11 g é da ordem do efeito procurado.

### 7.4 §7.1 — o que o ensaio estabelece (comentário 5)

> Este ensaio especificou um desenho de avaliação causal para o banimento da
> pulverização aérea no Ceará e o levou até o fim: estratégia de identificação
> declarada, dose construída com variação verificada no PAM, plano de análise
> datado e versionado, estimação executada e camada de robustez aplicada. A
> confrontação da dose com o uso de aeronave no Censo Agropecuário de 2006
> indica que ela mede intensidade da bananicultura, não pulverização aérea:
> naquele ano, 7 dos 169 municípios com área positiva de banana tinham
> aplicação por aeronave. O que se estima é, portanto, o efeito de forma
> reduzida do banimento segundo essa proxy. A
> concordância entre o efeito mínimo detectável previsto (33,4 g) e a
> meia-largura realizada (30,3 g) valida o diagnóstico amostral da
> especificação. Não valida a mensuração do tratamento nem a identificação do
> efeito da proibição onde havia pulverização aérea a remover.

### 7.5 §6.5 — efeitos fixos de dois sentidos (comentário 7)

> A advertência contra o \emph{event study} de efeitos fixos sob adoção
> escalonada \citep{goodmanbacon2021,sunabraham2021} vem das comparações entre
> unidades tratadas em datas diferentes. O ban é simultâneo, e esse viés não
> existe aqui. Outra coisa é o grupo de comparação ser nunca-tratado e limpo, e
> isso é hipótese. O Censo Agropecuário de 2006 a apoia para a aplicação
> agrícola por aeronave, mas não mede a dispersão aérea para controle vetorial,
> que o §2º do art. 28-B também alcança. A Tabela~\ref{tab:honestdid} condiciona
> a essa hipótese e não corrige uma eventual exposição do grupo \(d = 0\) à
> política. O peso dela é maior do que parece: os quinze municípios desse grupo
> são o controle de todos os estimadores binários desta seção.

### 7.6 §7.2 — abertura e o que sai (comentários 1, 2 e 6)

> A regra de \citet{weitzman1974} entra aqui como referência para organizar o
> que a escolha de instrumento exigiria, não como fórmula que receba os
> estimandos do Ensaio 1. Aplicá-la pede três objetos definidos sobre a mesma
> quantidade: a quantidade regulada (hectares tratados por via aérea, ou a
> exposição que eles produzem), a inclinação do benefício marginal social em
> relação a ela e a inclinação do custo marginal agregado de abatê-la. A dose
> do Ensaio 1 mede intensidade da bananicultura e não equivale, sem hipóteses
> adicionais, a essa quantidade. O \(ATT(d\,|\,d)\) não é o benefício social, e
> sua derivada não é a do benefício marginal. E a proibição é uma cota fixada
> em zero, isto é, um padrão tecnológico \citep{helfand1991}: ela só coincide
> com o instrumento-quantidade de Weitzman se o ótimo esperado for a solução de
> canto. O Ensaio 1 não produz, com a precisão obtida, informação utilizável
> sobre a inclinação do benefício marginal. Os intervalos cobrem o zero em
> todas as faixas de dose. Isso é imprecisão sob hipóteses mantidas, não prova
> de que a inclinação seja irrestrita. Do lado do custo, a planilha da Conab dá
> a ordem de grandeza do custo do banimento, cerca de 1,5\% do custo de
> produção, e não a curvatura, que depende de custos marginais dentro do
> produtor, custos fixos, capacidade e escala, além da heterogeneidade entre
> produtores.

**Sai da §7.2:** o mapeamento \(B = \lvert ATT\rvert \to B' = \lvert ACR\rvert
\to B'' = ACR'\); a frase "a derivada de uma curva não identificada não é
identificada"; "não exclui nenhuma região do espaço de parâmetros"; e todo o
parágrafo "Se o prêmio de conversão for aproximadamente homogêneo, \(c\) tende a
zero [...] basta que \(\beta > 0\)".

⚠️ Duas chaves citadas acima **não estão no `.bib`**. `helfand1991`: o que
está é `helfand1995` (Helfand & House), e a de 1991 entra depois da passada
Crossref (§8). `denteh2022misclassification`: Denteh & Kédagni, arXiv:2207.11890,
já conferida no arXiv (`docs/referencias-verificadas.md`), mas sem entrada no
`.bib`. É *working paper*; a entrada tem de ser criada a partir do registro do
arXiv, com a versão (v3) citada.

---

## 8. Referências citadas aqui e na conversa

✅ conferida nesta sessão (fonte entre parênteses) · ⬜ de memória, conferir
no Crossref local antes do `.bib` (`docs/referencias-verificadas.md` §7).

| referência | estado |
|---|---|
| Bilinski & Hatfield (2026), *Stat Med* 45(3–5), doi:10.1002/sim.70296 | ✅ (Scholar Gateway/Wiley) |
| Canay, Romano & Shaikh (2017), *Econometrica* 85(3), doi:10.3982/ECTA13081 | ✅ (Wiley) |
| Roth (2022), *AER: Insights* 4(3):305–322, doi:10.1257/aeri.20210236 | ✅ (AEA) |
| Lewbel (2007), *Econometrica* 75(2):537–551, doi:10.1111/j.1468-0262.2006.00756.x | ✅ (Econometric Society) |
| Ferman & Pinto (2019), *REStat* 101(3):452–467 | ✅ (MIT Press/RePEc) · DOI a conferir |
| Malani & Reif (2015), *J Public Econ* 124:1–17 | ✅ (ScienceDirect/RePEc) · DOI a conferir |
| Helfand (1991), *AER* 81(3):622–634 | ✅ (RePEc/JSTOR) |
| Goulder & Parry (2008), *REEP* 2(2):152–174 | ✅ (RePEc) · DOI a conferir |
| Hitzig (2020), *Economics and Philosophy* 36(3):407–434 | ✅ (RePEc/PhilPapers/Cambridge) · DOI a conferir |
| Sönmez (2024), *Minimalist Market Design*, arXiv:2401.00307 | ✅ existência (arXiv) · *working paper* |
| Hepburn (2006), *OxREP* 22(2):226–247 | ✅ (conferida antes da compactação desta sessão) |
| de Chaisemartin, D'Haultfœuille, Pasquier & Vazquez-Bare, arXiv:2201.06898 | ✅ existência · *working paper* |
| Portaria MAPA nº 298, de 22/09/2021 | ✅ (gov.br, LegisWeb) |
| Segerson (1988), *JEEM* 15(1); Stavins (1996), *JEEM* 30(2); Montgomery (1972), *JET* 5(3); Newell & Stavins (2003), *J Regul Econ* 23; Roberts & Spence (1976), *J Public Econ* 5; Pizer (2002), *J Public Econ* 85; Newell & Pizer (2003), *JEEM* 45 | ⬜ |
| Lewbel (2019), *JEL* 57(4); Imai & Yamamoto (2010), *AJPS* 54(2); Battistin & Sianesi (2011), *REStat* 93(2); Angrist & Imbens (1995), *JASA* 90(430); Conley, Hansen & Rossi (2012), *REStat* 94(1); Hagemann (2019), *J Econometrics* 213(1); Chung & Romano (2013), *Ann Stat* 41(2) | ⬜ |
| Lipscomb & Mobarak (2017), *REStud* 84(1); Assunção, Gandour & Rocha (2023), *AEJ: Applied* 15(2); Ponticelli & Alencar (2016), *QJE* 131(3); Rocha & Soares (2015), *J Dev Econ* 112 | ⬜ |
| Solomon et al. (2005), relatório CICAD/OEA; Arbuckle, Lin & Mery (2001), *EHP* 109(8); Bell et al. (2001), *Epidemiology* 12(2) | ⬜ |
| Camacho & Mejía (2017); Larsen, Gaines & Deschênes (2017); CGS (2024); Rambachan & Roth (2023); Weitzman (1974) | já no `.bib` |

---

## 9. Arquivos desta rodada

| arquivo | o quê |
|---|---|
| `docs/revisao/feedback-2026-09-22.md` | o parecer, sem edição |
| `scripts/estimate/04_robustness.py` | nível e inferência no nível, perfil por faixa, inversão do teste, estratos de aptidão, "exata" retirado |
| `scripts/estimate/10_spt_pretrend.py` | nível nos cortes placebo |
| `tests/test_data_prep.py` | 9 testes novos (270 no total) |
| este documento | a resposta |
