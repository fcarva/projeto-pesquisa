# Briefing — reunião de orientação

**Ensaio 1 · Externalidade da pulverização aérea no Ceará · setembro de 2026**

*Companheiro de `08-briefing-orientador.md`, que é de agosto e cujo §0 ficou
desatualizado. Este documento cobre o que mudou desde então.*

---

## 0. Se a conversa for curta, é isto

O briefing anterior dizia: *"o pipeline está completo e testado, mas nenhum
script rodou contra dado real"*. **Isso mudou por inteiro.** Todas as fontes
viáveis foram adquiridas, a pré-especificação foi fechada e commitada, o
estimador rodou, e a camada de robustez inteira foi executada.

O resultado principal, em uma linha:

> **O efeito do banimento sobre o peso ao nascer é de −36,2 g, com intervalo de
> 95% em [−66,5 ; −5,9]. A meia-largura do intervalo é 30,3 g, contra o piso de
> 15 g fixado antes de olhar. Pelo critério pré-especificado, isto NÃO é
> achado — é limite superior informativo.**

E o ponto que sustenta a defesa: **a análise de poder *ex ante* acertou**. O
efeito mínimo detectável previsto era 33,4 g; a meia-largura realizada foi
30,3 g. O desenho se comportou exatamente como diagnosticado antes de haver
dado.

**Três coisas precisam de você.** Estão na §5.

---

## 1. O que a rede escondia — e o que ela não escondia

O diagnóstico de agosto atribuía a ausência de dado a bloqueio de rede.
⚠️ **Era bloqueio do proxy da sessão remota, não do projeto.** Na máquina do
pesquisador, IBGE, DATASUS e FAO respondem normalmente.

O mesmo tipo de erro apareceu no R: o projeto registrava *"não há R instalado"*
e por isso dava o E6 como bloqueado. **R 4.6.1 estava instalado há doze dias
quando isso foi escrito.** A verificação tinha testado o `PATH`, e no Windows o
instalador do R não o altera.

⚠️ **E havia um bloqueio real que a ausência aparente de R escondia.** O pacote
`contdid` traz, como valor padrão do argumento que define o grupo de comparação,
um vetor que viola a própria asserção interna do pacote — de modo que
`cont_did()` **não roda com os defaults**. O script do E6 nunca passava esse
argumento. A curva nunca teria saído, com R ou sem R.

**Lição que vale registrar:** ler o código de um pacote não substitui
executá-lo. Foram seis defeitos desta família nesta linhagem de trabalho.

---

## 2. O que foi adquirido — e o que foi suspenso *com razão*

| Fonte | Estado | Observação |
|---|---|---|
| PAM/SIDRA, SINASC, SIM, SIH | ✅ adquiridas | no painel |
| **SINAN/IEXO** | ✅ adquirida | 1.217 notificações de agrotóxico agrícola |
| **População (IBGE)** | ✅ adquirida | ⚠️ 2022 vem do Censo, não de estimativa |
| **FAO-GAEZ** | ✅ adquirida | 184/184 municípios; primeiro estágio confere |
| **Bans municipais** | ✅ varridos | 17 tratados; 1 achado |
| SISAGUA | ⏸️ **suspensa** | ver §3 |
| ANA (ottobacias) | ⏸️ suspensa | bloqueada pela anterior, não por acesso |
| INMET/FUNCEME | ⏸️ suspensa | alísios: direção sem variação espacial |
| MapBiomas | ✘ descartada | banana cai em classe genérica |
| SEMACE (LAI) | ⬜ pendente | única rota para o `d = 0` operacional |

**A distinção entre "não adquirida" e "suspensa" não é burocrática.** Uma fonte
suspensa foi obtida, inspecionada e descartada por defeito identificado — e o
defeito é informação sobre o desenho.

---

## 3. Três coisas que o dado disse e que mudam o que o texto pode prometer

### 3.1 A cultura-âncora não é o melão

O material de projeto apontava melão e algodão, pela Chapada do Apodi. O Gate 1
os encerrou: **melão tem área positiva em 10 municípios, algodão em 28** —
suporte insuficiente para a curva não-paramétrica.

A **banana** sustenta: 169 municípios, Gini 0,86, 78% da área no decil superior.
E ela casa com a química documentada — procimidona é fungicida de bananal e
aparece em **23 de 23** amostras do Dossiê ABRASCO.

✅ O FAO-GAEZ confirma relevância do instrumento: o decil superior da banana tem
aptidão média 0,37 contra 0,26 do restante. *Banana é plantada onde banana é
apta.* Isso não testa exclusão, que não é testável.

### 3.2 ⚠️ Limoeiro do Norte já estava tratado desde 2009

> ⚠️ **Corrigido em 2026-09-22 — o título desta seção não se sustenta.** A lei
> municipal foi **revogada em maio de 2010**, um mês após o assassinato de Zé
> Maria do Tomé, por um artigo da Lei 1.511, de 26/05/2010, de política
> ambiental (texto integral ainda não lido). Em 2015–2018 Limoeiro não
> estava sob ban, e a contaminação do pré-período é nula. Ver
> `docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md` §5.

A flag deixou de ser hipótese. A **Lei Municipal 1.478, de 20/11/2009**, proíbe
o uso de aeronaves nas pulverizações — nove anos antes da lei estadual. E o
município é o **6º de 169** na banana: está *dentro* do grupo tratado.

A varredura dos 17 tratados está completa: **1 confirmado, 16 conferidos sem
norma, nenhum inconclusivo.** A contaminação é exatamente Limoeiro e não cresce
— Quixeré (21.289 leis no acervo) e Russas (6.901) não têm norma do tema.

### 3.3 ⚠️ O canal-água produziria um efeito inteiro do nada

O SISAGUA tem a melhor cobertura de qualquer fonte deste trabalho: **58.061
medições, 184 municípios, todos os anos.** E mesmo assim não entra.

Detecções de agrotóxico no Ceará, por ano:

```
2015: 41    2016: 13    2017: 5    2018: 20    2019: 44
2020:  0    2021:  0    2022: 0     ← em 18.480 amostras
```

Zero exato, três anos seguidos, com **mais** amostras. E não é fenômeno
nacional: em 2020 o Brasil reporta 49,8% dos resultados em valor numérico e o
Ceará reporta **0,00%**. É mudança de prática laboratorial cearense, começando
no ano seguinte ao ban.

> **Um DiD sobre essa variável concluiria que a lei eliminou 100% das
> detecções.** Grande, significativo, e puro artefato de registro.

Somem-se duas coisas: três das quatro moléculas do Dossiê (procimidona, carbaril,
fenitrotiona) **não são monitoradas**, e 95% das amostras são de água já tratada.

---

## 4. Os resultados, e por que nenhum é apresentado como achado

### 4.1 A pré-especificação foi fechada antes de estimar

`docs/pre-especificacao.md`, fechada em 2026-09-21 e **commitada** — o commit é
o carimbo de tempo. Ela fixou, entre outras coisas: desfecho `peso_medio`,
âncora banana, piso de efeito **15 g**, correção de Holm sobre **duas**
hipóteses confirmatórias, e o compromisso de que resultado abaixo do MDE se
escreve como *limite superior informativo*.

⚠️ **E o documento se corrige a si mesmo na abertura.** Ele não é pré-registro
no sentido estrito, e dizer que fosse seria falso: a janela em que nenhuma fonte
real havia sido tocada fechou em 25/08, e o histórico do git prova. O que existe
é um plano de análise **pós-diagnóstico de desenho e pré-estimação** — categoria
real e defensável, e declarada como tal. A fronteira que ele protege é entre
*desenho* e *efeito*, e essa está intacta.

### 4.2 O quadro converge

| Estimador | τ (g) | IC 95% |
|---|---|---|
| **CGS contínuo, ATT(d\|d)** — *confirmatório* | **−36,2** | [−66,5 ; −5,9] |
| Event study binário (TWFE) | −16 a −33 | cobre zero |
| Synthetic DiD | −20,2 | [−56,4 ; +16,1] |
| DiD simples | −21,9 | [−59,5 ; +15,8] |
| Controle sintético puro | −34,6 | [−67,4 ; **−1,9**] |

Todos negativos. **O gate do MDE não é superado por nenhum confirmatório.**

⚠️ **E aqui está o caso que testa a honestidade do arranjo.** O controle
sintético puro é o **único** estimador cujo IC exclui zero, e sua magnitude
supera — por pouco — o MDE. **Ele não é reportado como achado**, por três
razões:

1. Os três rodam sobre a **mesma matriz**. Divergirem quanto a excluir zero não
   é evidência a favor do que exclui — é evidência de que o resultado depende do
   estimador.
2. Nenhum deles é confirmatório pela §6 da pré-especificação.
3. Selecionar, entre muitos, o que cruzou a linha é exatamente a prática que
   aquele documento existe para impedir.

### 4.3 O sinal negativo não é surpreendente

A seleção para nascimento vivo predizia isto: se o ban reduz óbito fetal, fetos
marginais passam a nascer e entram na cauda inferior de peso — o efeito sobre o
peso médio vem atenuado **ou invertido**. Foi por isso que óbito fetal entrou
como segundo confirmatório. O coeficiente é +0,0002, com IC cobrindo zero: não
sustenta a história de seleção, e também não a exclui.

### 4.4 O placebo tem poder — e agora sabemos quanto

Um teste de pré-tendências que "passa" pode estar passando por falta de poder.
Medido formalmente:

> **O placebo exclui tendências confundidoras capazes de fabricar mais de ~11 g
> de efeito espúrio, e não exclui abaixo disso.**

Não é cego, e também não é tranquilizador — 11 g é da ordem do efeito procurado.

E o `HonestDiD` precifica a hipótese: o intervalo vai de 97 g de largura sob
paralelismo perfeito para 379 g quando se admite violação do tamanho da maior
violação pré observada. **O desenho só fala sob hipótese quase perfeita.**

---

## 5. O que precisa de você

| # | Decisão | Por quê agora |
|---|---|---|
| **1** | **Ofício LAI à SEMACE** | É a **única** rota para o `d = 0` que mede o *método* no pré-ban. O cadastro federal (SIPEAGRO) é dado aberto — a LAI ao MAPA era desnecessária — mas começa em 2021 e não alcança a janela. Tem relógio externo: 20 dias + 10. |
| **2** | **Conta no BigQuery** | A Base dos Dados declara SINASC **1979–2024**; o FTP do DATASUS para em 2022. Uma consulta confirma se há linhas do CE em 2023–24. Se houver, o pós-ban vai de **quatro para seis anos**. |
| **3** | **Encorpar o grupo tratado?** | É a via declarada para o poder — baixar o corte de dose para além do decil superior. Não muda estimando nem exige ponderação. ⚠️ Mas é mudança de especificação e entra na tabela de desvios. |

**E uma pergunta de escopo, que é sua e do orientador:** o canal-água sai do
Ensaio 1, vira descritivo de pré-período, ou justifica pedir o microdado
laboratorial bruto à SESA/CE?

---

## 6. Onde está tudo

| | |
|---|---|
| Documento da qualificação | `paper/main.pdf` — **30 páginas**, §5 e §6 escritas |
| Pré-especificação | `docs/pre-especificacao.md` — fechada, commit `c386514` |
| Números da aquisição | `docs/gates-resultados-dados-reais.md` |
| Estado das lacunas | `docs/lacunas-de-dados.md` |
| Bans municipais | `docs/legislacao/bans-municipais-ce.csv` |
| Pipeline | `make real CULTURA="Banana (cacho)"` — 14 scripts, 139 testes |

⚠️ **A §7 (conclusão) não foi escrita.** Ela é argumento do pesquisador, não
relato de execução.
