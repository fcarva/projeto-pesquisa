# 20 — Reengate do desenho para o projeto de pesquisa

*ARS `academic-pipeline`, modo `full`, rodada 20, Estágio 1. 2026-11-15.
Entregável da rodada: projeto de pesquisa de 15 páginas (abnTeX2), só Ensaio 1,
sem números de estimativa, prazo 27/11/2026. Texto em `paper/projeto/`.*

> **Correção (2026-11-15, após conferência contra o repositório do ARS).** O
> cabeçalho acima diz "modo `full`", e a rodada **não** seguiu o protocolo do
> plugin: este documento e o rascunho em `paper/projeto/` foram escritos
> diretamente, sem despachar `deep-research` nem `academic-paper`, sem Material
> Passport, sem estimativa de orçamento e sem os Estágios 2.5 (integridade) e
> 3 (revisão). O conteúdo vale como avaliação de estratégias e proposta de
> desenho; não vale como saída auditada do pipeline. A retomada entra pelo
> Estágio 2.5, com o rascunho declarado como material externo. Plugin
> instalado: 3.24.2 (repositório em 3.24.3).

> **Estado de partida.** Nada mudou desde 23/09/2026: LAIs não protocoladas,
> ação de 2011 não conferida, sem retorno do orientador. Esta rodada não faz
> busca nova nem estimação — avalia as estratégias que os docs 16–19 deixaram
> na mesa e fixa o que o **projeto** declara. Precedência: o documento mais
> recente vence.

---

## 1. Decisões do pesquisador nesta rodada (15/11)

| tema | decisão |
|---|---|
| Formato | abnTeX2 padrão; 15 páginas de elementos textuais |
| Escopo | só Ensaio 1; nenhum número de estimativa no texto |
| Janela de nascimentos | 2015 → 19/12/2024 (corte na Lei 19.135/2024) |
| Desenho principal | "avaliar as estratégias para decidir" → §2–§3 |
| Janela da dose | "definir de acordo com avaliação da política pública; a ideia é medir o efeito da proibição da pulverização aérea" → §4 |

---

## 2. Avaliação das estratégias

O critério vem da pergunta: **medir o efeito da proibição da pulverização
aérea**. O tratamento é a retirada de um *método*; uma estratégia serve na
medida em que (i) o grupo tratado é quem de fato usava avião, (ii) a hipótese
de identificação é defensável e verificável, (iii) o dado existe ou tem data
para existir, (iv) há poder para a magnitude que a literatura sugere.

| estratégia | (i) mede o método? | (ii) hipótese de identificação | (iii) dado | (iv) poder | veredito para o projeto |
|---|---|---|---|---|---|
| **A. Forma reduzida pela proxy** — CGS com dose contínua, área de banana (R1) | não: mede a cultura. O efeito sai atenuado pelo VPP (Corolário 1) | tendências paralelas entre municípios com e sem banana; grupo de comparação pequeno | em mãos | baixo por construção: a atenuação é multiplicativa | **linha de base**: reportável, com sinal informativo e magnitude que é limite inferior em módulo |
| **B. Nível com tratados pelo método** — municípios com aeronave (R2) | sim, se o retrato de 2006 valer em 2018 | tendências paralelas | em mãos (Censo Agro 2006) | baixo: poucos tratados e fração exposta pequena | não sustenta sozinho |
| **C. Diferença tripla de calendário** — gestação × estação de fumigação × pré/pós (R3/R4) | sim: tratados pelo método e exposição pelo calendário | **uma** tendência paralela, a do hiato sazonal (Olden & Møen) | R3 em mãos; R4 depende do MAPA | a verificar no pré-período (`make mde-calendario`); cancela a heterogeneidade entre municípios | **desenho principal planejado**, condicionado à etapa de medição |
| **D. Doadores externos** — controle sintético/SDID, Chapada × municípios de outras UFs (R5) | sim | tendências paralelas com doadores externos | em mãos (SINASC multi-UF) | a verificar | **robustez** do C |
| **E. Fronteira CE × RN** (R6) | sim | descontinuidade na divisa | em mãos | — | despriorizada: o RN reprova no gate de aeronaves |
| **F. Identificação parcial** (R7) | limites | monotonicidade | em mãos | limites largos | exploratório |

**Por que não A sozinha.** Responde "o que aconteceu onde havia banana", não
"o que a proibição do avião fez". É a crítica central do parecer de 22/09.

**Por que não C desde já, sem condição.** Todas as estratégias que medem o
método dependem de um fato ainda não conferido: **a pulverização aérea
continuou na Chapada do Apodi depois de 2011?** (doc 19 §2.3). Um projeto que
apostasse em C sem dizer isso prometeria um grupo tratado que pode não existir.

**Por que um projeto pode ser em estágios.** É projeto, não resultado: declarar
a etapa de medição, a regra de decisão e o desenho que cada desfecho da medição
aciona é o *forward engineering* que o gênero pede — e deixa as LAIs e a
consulta à Justiça Federal como atividades com data no cronograma.

---

## 3. Desenho que o projeto declara

**Parâmetro-alvo.** Efeito médio do banimento sobre o peso ao nascer dos
gestados em municípios onde havia aplicação aérea (ATT). Enquanto o tratamento
for medido pela cultura, o que se estima é a **forma reduzida**: sob tendências
paralelas na classificação observada e sem falso negativo, forma reduzida =
VPP × ATT.

**Estágio 1 — linha de base (dado em mãos).** DiD com tratamento contínuo de
Callaway, Goodman-Bacon & Sant'Anna; dose = intensidade pré-ban da
bananicultura (PAM); alvo `ATT(d|d)`; grupo de comparação `d = 0` construído
com a aptidão FAO-GAEZ (linguagem de construção de controle; IV só como
extensão declarada). A curva dose-resposta é diagnóstico, não resultado: exige
*strong parallel trends*.

**Estágio 2 — medir o método.**
1. Relatórios mensais de aviação agrícola (IN MAPA 2/2008, art. 14): LAI federal.
2. Receituário agronômico com modalidade de aplicação (Decreto 4.074/2002,
   art. 66): LAI à ADAGRI.
3. Cadastro estadual (Lei 12.228/1993): LAI à SEMACE.
4. Ação civil pública de 2011 (Justiça Federal, Limoeiro do Norte): desfecho.
5. Censo Agropecuário 2006 (tabela 1008): retrato já em mãos, usado como
   calibração.

**Estágio 3 — desenho principal, condicionado ao estágio 2.** Diferença tripla:
(exposição do 1º trimestre de gestação à estação de fumigação) × (município com
aplicação aérea medida) × (pré/pós-ban). Precedentes: Calzada, Gisbert &
Moscoso (2023); Brainerd & Menon (2014). Ameaça própria: composição sazonal das
mães (Currie & Schwandt 2013; Buckles & Hungerman 2013) e mudança de
sazonalidade em 2020–2021. Robustez: doadores externos (estratégia D).

**Regra de decisão (escrita antes do dado).**

| o estágio 2 mostra | o Ensaio 1 entrega |
|---|---|
| aplicação aérea documentada em 2015–2018, por município e mês | estágio 3 com tratados e calendário medidos |
| prática documentada, sem calendário | estágio 3 com tratados medidos e calendário agronômico (estação chuvosa), declarado como hipótese |
| nenhum registro novo | estágio 3 com os tratados do Censo 2006, como exploratório, + linha de base |
| a prática cessou em 2011 | linha de base + diagnóstico: o ban de 2019 não removeu exposição mensurável; contribuição de mensuração |

**Inferência.** Poucos clusters tratados: Conley–Taber, Ferman–Pinto, inferência
conformal (Chernozhukov, Wüthrich & Zhu); wild cluster bootstrap só como
complemento (MacKinnon & Webb). Na linha de base o grupo escasso é o de
controle, e a inferência do nível tem de respeitá-lo. Duas hipóteses
confirmatórias (peso médio; óbito fetal), correção de Holm.

**Desfechos.** Confirmatórios: peso médio ao nascer e taxa de óbito fetal (a
segunda responde à seleção para nascimento vivo). Exploratórios: baixo peso,
prematuridade. Canal: notificações de intoxicação por agrotóxico agrícola
(SINAN). Canal água: fora do escopo (SISAGUA suspenso).

---

## 4. Janela da dose, decidida pela lógica de avaliação de política

A pergunta é o efeito da **proibição**. A intensidade de tratamento tem de ser
característica **predeterminada**: fixada antes de a política poder alterá-la.
O PL 18/2015 foi apresentado em 24/02/2015; área plantada entre 2015 e 2018
pode já responder à expectativa do ban, e uma dose que responde ao tratamento
deixa de ser dose.

**Decisão declarada no projeto: dose principal = média 2010–2014;
2015–2018 = sensibilidade.** As duas janelas são fortemente correlacionadas e a
maior parte do grupo de dose alta coincide (`docs/lacunas-de-dados.md`), mas não
toda — a diferença é reportada.

⚠️ É **desvio** da pré-especificação (§3: 2015–2018 principal) e entra na
tabela de desvios (§8) quando o pesquisador ratificar. A ressalva honesta: a
janela antiga mede pior a exposição *vigente* em 2018; por isso a sensibilidade
fica no texto, e por isso a medição do método (estágio 2) importa mais que a
escolha da janela.

---

## 5. O que muda em relação aos documentos anteriores

| antes | agora (projeto) |
|---|---|
| desenho único: CGS dose contínua | linha de base + medição + calendário, com regra de decisão |
| dose 2015–2018 principal | 2010–2014 principal (a ratificar; desvio a registrar) |
| painel 2015–2022 | janela declarada 2015 → 19/12/2024 |
| "identificação fechada" | identificação condicionada à medição do método |
| Ensaio 2 ancorado na curva | Ensaio 2 fora do projeto; citado como desdobramento |

## 6. Pendências que o projeto transforma em cronograma

1. Protocolar as três LAIs (MAPA, ADAGRI, SEMACE).
2. Consultar a ação de 2011 na Justiça Federal do Ceará.
3. Estender o painel SINASC/SIM a 2024 e congelar a *vintage*.
4. `make mde-calendario` e `make mde-desenhos` no painel real (poder do estágio 3).
5. Pré-especificar o estágio 3 com o orientador **antes** de cruzar exposição e desfecho.
6. Registrar os desvios na `docs/pre-especificacao.md` §8.
