# Rota 1 — Fase 2 (investigação): o corpus de medida, e a flag 7 deixa de ser adjetivo

*ARS `deep-research`, modo `full`, Fase 2 de 6. Decisão da Fase 1: **travar o
gate antes de investir** (opção A), com o melão reaberto como subpergunta.
2026-09-22.*

---

## 0. O que a Fase 2 foi buscar, e o que achou

A opção A pede o corpus de **medida e gate**: como a literatura mede exposição a
pulverização, o que ela sabe sobre proxies de cultura, e como se decide
viabilidade **antes** de estimar.

O achado central não é um método novo. É que **alguém já mediu exatamente o viés
que a flag 7 descreve**, no cenário aplicado mais próximo que existe — e o
resultado diz que, na configuração deste projeto, a atenuação é **substancial,
não marginal**, por um mecanismo específico que o repositório não nomeava.

---

## 1. O achado central

> **Rull, R. P. & Ritz, B. (2003).** *Historical pesticide exposure in California
> using pesticide use reports and land-use surveys: an assessment of
> misclassification error and bias.* **Environmental Health Perspectives**
> 111(13): 1582–1589. PMID **14527836**. ✅ publicado, periódico revisado por
> pares. ⚠️ Conferido por registro e resumo; **o texto completo não abriu nesta
> sessão** (proxy bloqueia `pmc.ncbi.nlm.nih.gov`) — as magnitudes de simulação
> ficam pendentes de leitura.

Eles simulam **a mesma troca que este projeto faz**: usar proximidade a cultura
(*land-use survey*) no lugar do registro de aplicação (*Pesticide Use Report*).
O achado, no resumo:

> *se a misclassificação é não-diferencial e a **prevalência de exposição é
> baixa**, **pequenas reduções de especificidade** produzem **reduções
> substanciais** na estimativa de risco.*

### Por que isso morde aqui com força incomum

As duas condições valem, e a segunda com folga:

| condição de Rull & Ritz | neste projeto |
|---|---|
| prevalência de exposição **baixa** | **3,8%** dos municípios tinham aeronave (7 de 184). Entre estabelecimentos com agrotóxico: **0,033%** (36 de 110.312) |
| especificidade **imperfeita** | ~90%, o que parece alto — e não é o suficiente |

⚠️ **E o mecanismo é contraintuitivo o bastante para merecer estar escrito.** Com
prevalência baixa, uma especificidade de 90% **não** protege: os falsos positivos
vêm dos 177 municípios sem aeronave, e são tantos que engolem os verdadeiros
positivos. O número que decide não é a especificidade — é o **VPP**.

---

## 2. A flag 7, medida

Do confronto entre a dose (decil superior da banana) e a medida direta (Censo
Agro 2006, aeronave), **com os números que o paper já publica na §5.4**:

| decil | sensibilidade | especificidade | **VPP** | λ teto |
|---:|---:|---:|---:|---:|
| 17 | 28,6% | 91,5% | **11,8%** | 0,912 |
| 19 | 28,6% | 90,4% | **10,5%** | 0,925 |

> **Cerca de nove em cada dez municípios do grupo "tratado" não tinham
> pulverização aérea a perder.** E a dose deixa de fora quase três quartos dos
> municípios que de fato a tinham (sensibilidade de 28,6%).

Reprodutível: `make erro-classificacao` (`scripts/estimate/12_erro_de_classificacao.py`,
8 testes). Roda **sem rede** a partir dos números publicados; com `--censo` e
`--dose` recalcula dos artefatos.

### ⚠️ Uma inconsistência interna que a conta expôs

O repositório reporta o decil superior ora como **17**, ora como **19**
municípios — §6.3 do paper e a flag 0 dizem 17; a §5.4 diz 19. A origem provável
é o denominador (169 com área positiva → 16,9 ≈ 17; 184 → 18,4 ≈ 19), mas isso é
hipótese, não verificação.

**Não muda a conclusão** (VPP ~10–12% nas duas leituras) e **precisa ser
resolvido antes da qualificação**, porque é o tamanho do grupo tratado — o
número que a banca confere primeiro. O script reporta as duas em vez de escolher
em silêncio.

### E o que isso faz com a leitura da §6.8 do paper

A §6.8 põe "falta de poder" e "erro de medida" como duas leituras. Com o VPP na
mão, elas deixam de ter o mesmo estatuto:

- "Falta de poder" é **compatível** com o observado.
- "Erro de medida" é **predito** pelo observado: dada prevalência de 3,8% e VPP
  de ~10%, a literatura aplicada diz que a atenuação **tem** de ser substancial.

Uma leitura descreve; a outra prevê. Isso não prova que a segunda é a verdadeira
— prova que ela não é especulação simétrica à primeira.

---

## 3. O limite, agora com λ que sai de dado

Aplicando o Corolário 5 de Denteh & Kédagni aos coeficientes da §6:

| estimador | λ=0,3 | λ=0,5 | λ=0,7 |
|---|---:|---:|---:|
| Synthetic DiD (−20,2) | −28,8 | **−40,3** | −67,2 |
| Controle sintético (−34,6) | **−49,5** | −69,3 | −115,5 |
| DiD simples (−21,9) | −31,2 | **−43,7** | −72,8 |

**Negrito = o limite ultrapassa o MDE de 33,4 g.** Sob a leitura de erro de
medida, o efeito implicado sobre os genuinamente tratados é de magnitude que
**este desenho teria detectado**.

⚠️ **O λ teto medido é 0,91–0,93, e ele NÃO deve ser usado.** Está na saída do
script justamente para mostrar por que não serve: "ter aeronave em 2006" não é
"ser tratado em 2019" — treze anos antes, conta estabelecimentos e não voos, e
prestador sediado num município pulveriza lavoura do vizinho. A faixa
defensável é 0,3–0,7, e ela **precisa de argumento escrito**, não de tabela.

⚠️ **E o limite não vale sob erro diferencial**, que é o caso provável (aeronave
correlaciona com porte; porte com desfecho). Sob erro diferencial, a Proposição 1
do mesmo artigo diz que o **sinal pode inverter**. Os três avisos estão no
docstring do script e na saída impressa.

---

## 4. O corpus, e o que ele revela sobre a posição deste trabalho

### 4.1 A literatura de exposição residencial mede aplicação, não cultura

A busca devolveu um corpo grande e consistente, quase todo construído sobre o
**California Pesticide Use Reporting (PUR)** — registro **obrigatório,
georreferenciado e completo** de toda aplicação agrícola desde 1990, descrito na
literatura como o sistema mais abrangente do mundo. Sobre ele se constroem
dezenas de estudos de desfecho perinatal, câncer infantil, Parkinson e autismo,
com exposição em raios de 500 m a 4 km.

| trabalho | o que acrescenta |
|---|---|
| Nuckols et al. (2007), *EHP* 115(5):684 | liga o PUR a mapas de cultura — o passo que separa "onde se planta" de "onde se aplica" |
| Rull & Ritz (2003), *EHP* 111(13):1582 | quantifica o custo de **não** dar esse passo |
| Larsen, Gaines & Deschênes (2017), *Nat. Comms* 8:302 | já no `.bib`; efeitos só no topo 5% da exposição |

### 4.2 ⚠️ E a comparação com os dois análogos mais próximos é desconfortável

| trabalho | como mede a exposição |
|---|---|
| Camacho & Mejía (2017), *J. Health Econ.* | **hectares efetivamente pulverizados** — o Estado colombiano registrava cada operação (média de 128 mil ha/ano sob o Plan Colombia) |
| Literatura da Califórnia | **registro obrigatório de aplicação**, georreferenciado |
| **Este trabalho** | **área plantada da cultura-âncora** |

> Os dois análogos mais próximos tiveram **registro de aplicação**. Este não tem,
> porque o Brasil não mantém equivalente do PUR.

**Isso não é fraqueza a esconder; é a contribuição a declarar.** A distância
entre os desenhos não é de método — é de **infraestrutura de dados**. E é o que
converte a LAI à SEMACE e o RAB da ANAC de conveniência em condição: são as
únicas rotas para algo que se aproxime de um registro de aplicação no
pré-período.

### 4.3 A correção de escala que o corpus também impõe

A literatura residencial mede exposição em **500 m a 2 km**. O município é
unidade grosseira por uma ordem de grandeza. A pré-especificação §7 veda descer
de unidade geográfica, com razão declarada (registro de residência do DATASUS), e
**a vedação continua certa**. O que muda é o diagnóstico: a atenuação tem
**duas** fontes somadas — classificação errada do tratamento (§2) e agregação
espacial grosseira — e o paper hoje discute só a primeira.

---

## 5. Onde a Fase 2 deixa o gate

O gate (`14_gate_fronteira.py`) já está escrito e testado. A Fase 2 acrescenta a
ele **uma pergunta que não estava lá**, e que agora parece a mais informativa:

> Aplicar as mesmas três métricas — sensibilidade, especificidade, VPP — à
> classificação **de fronteira**. Se o desenho CE×vizinho classifica tratamento
> por `estado × período`, o VPP dessa classificação é **1 por construção** do
> lado tratado (todo município cearense foi alcançado pela lei). O que ele não
> resolve é a **sensibilidade**: a lei alcança 184 municípios, e ~7 tinham
> aeronave.

⚠️ **E essa observação é desconfortável para a Rota 1.** Ela troca um problema de
**VPP** por um problema de **sensibilidade**: em vez de tratar 19 municípios dos
quais 2 eram tratados, trataria 184 dos quais ~7 eram. O VPP cairia de ~11% para
~4%.

**Isso não mata a rota**, por uma razão que importa: no desenho de fronteira o
estimando **muda de nome**. Não é mais "efeito de remover pulverização aérea em
quem a tinha" (ATT), e sim "efeito de proibir pulverização aérea num estado"
(intenção de tratar, com a diluição dentro do estimando, por construção e
declaradamente). É um parâmetro **menor e honesto**, não um parâmetro
contaminado.

> **É esta a escolha que a Fase 3 tem de encarar, e ela não é técnica:** um ATT
> grande sobre um grupo mal identificado, ou um ITT pequeno sobre um grupo
> perfeitamente identificado. A pré-especificação escolheu o primeiro sem saber
> que o segundo existia.

---

## 5-bis. A busca desconfirmatória, feita — e ela achou um contrapeso real

O Checkpoint 2 registrou que a busca tinha formato confirmatório. A busca
desconfirmatória foi então executada: *literatura que defenda proxies de cultura
como boa medida de exposição*.

**Ela existe, e é preciso ser justo com ela:**

> **Nuckols et al. (2007)**, *EHP* 115(5):684 — integrando mapas de cultura ao
> PUR, *"for all six pesticides we found **good agreement (88–98%)** as to
> whether the pesticide use was predicted."*

⚠️ **Mas o contrapeso responde a outra pergunta**, e a distinção é o ponto:

| pergunta | o que a literatura diz |
|---|---|
| a cultura prediz **qual molécula**? | ✅ **sim, 88–98%** (Nuckols et al.) |
| a proximidade à cultura prediz **se houve exposição**? | ✘ **não** — *"considerable effect estimate attenuation also occurred when we used residential distance to crops as a proxy for pesticide application"* (Rull & Ritz, resumo) |
| a área da cultura prediz se a aplicação foi **aérea**? | ⚠️ **ninguém testou** — a pergunta não existe na literatura da Califórnia, porque lá o PUR registra o método |

> **O problema de medida deste projeto é estritamente mais difícil que o da
> literatura de referência**, e agora dá para dizer por quê em uma linha: ele
> precisa de uma terceira camada — o **método** de aplicação — que nenhum dos
> dois achados acima cobre, e que 0,03% dos estabelecimentos usavam.

Isso **não** enfraquece o achado da §1: o elo que falha é justamente o que este
trabalho usa. Mas corrige uma leitura preguiçosa que o §4.1 convidava — a de que
"proxy de cultura não presta". Ela presta para o que a cultura de fato determina,
que é a química. A §5.3 da pré-especificação (procimidona é fungicida de bananal)
está, portanto, **apoiada** por esta literatura, não enfraquecida.

---

## 5-ter. ⚠️ O teste que Camacho & Mejía rodaram, e que este desenho não pode rodar

Lendo o resumo completo do análogo mais direto, apareceu a frase que mais importa
de tudo que esta fase encontrou:

> *"The results are robust to **controlling for the extent of coca cultivation**
> of illicit crops in the municipality of residence."*

Eles **separam a pulverização da cultura** porque têm as duas coisas: registro de
aplicação **e** extensão do cultivo. Controlando a segunda, mostram que o efeito
vem da primeira.

**Este desenho tem só a cultura.** Logo não pode rodar esse teste — e isso
significa que o coeficiente estimado aqui é, por construção, uma **mistura**:
efeito da pulverização aérea **mais** tudo que a intensidade agrícola faz com
saúde perinatal por outras vias (renda, trabalho no campo, aplicação terrestre,
nitrato). A flag 2 já dizia "área plantada é proxy de intensidade agrícola";
o que faltava era o nome do teste que separaria as duas e a constatação de que
o análogo o rodou.

### E daqui sai o argumento a favor da Rota 1 que eu não havia articulado

O desenho de fronteira **é** uma forma de rodar aquele teste com os dados que
existem. Comparando municípios de **extensão de cultivo semelhante** dos dois
lados da linha, a extensão fica aproximadamente fixa e o que varia é o **regime
de pulverização**. É a separação de Camacho & Mejía, obtida por geografia em vez
de por registro.

> Isto reordena a justificativa da Rota 1. Ela não vale principalmente por
> encorpar o grupo tratado, nem por eliminar a flag 7 — vale porque é **a única
> via disponível para separar o efeito do método do efeito da cultura**, que é
> a confusão que a §4.2 do paper declara e nunca endereça.

⚠️ E isso continua **condicionado ao gate**: se o vizinho não tinha pulverização
aérea, não há regime a contrastar e a separação não acontece.

---

## 6. Estado do checkpoint e o que falta

**Devil's Advocate — Checkpoint 2 (cherry-picking, viés de confirmação):**
✅ **PASS.** A busca inicial tinha formato confirmatório, e as duas mitigações
foram executadas: (i) o §5 registra o achado que **contraria** a rota preferida
— o VPP piora no desenho de fronteira —, escrito antes de qualquer conclusão
sobre qual rota vence; (ii) a busca desconfirmatória foi feita (§5-bis), achou
um contrapeso real (Nuckols et al., 88–98%) e ele está caracterizado pelo que
de fato mostra, não pelo que conviria. O resultado da desconfirmação **estreitou**
a afirmação em vez de apagá-la: proxy de cultura prediz bem a **química** e mal a
**ocorrência**, e nada na literatura cobre o **método**.

### Pendências desta fase

- ⚠️ **Rull & Ritz não abriu em texto completo.** As magnitudes de simulação —
  quanto de atenuação, para que combinações de sensibilidade e especificidade —
  ficam por ler. O que se usa aqui é o achado do resumo, que é qualitativo.
- ⚠️ **A inconsistência 17 vs 19** precisa de resolução, não de nota.
- ⚠️ **Camacho & Mejía**: o **resumo** foi recuperado e conferido nesta sessão
  (ver §5-ter) — a pendência de `referencias-verificadas.md:107` ("sem abstract
  depositado") pode ser **reduzida**, não fechada. O **texto completo** segue
  sem leitura pela terceira sessão: o proxy bloqueia CGD, ScienceDirect e RePEc.
- ✅ **Busca desconfirmatória** feita — ver §5-bis.
- ⚠️ **Nuckols et al. (2007)** conferido por resumo; autoria completa e texto por ler.

---

## 7. O que foi construído nesta fase

| arquivo | o que é |
|---|---|
| `scripts/estimate/12_erro_de_classificacao.py` | as três métricas + o limite do Corolário 5; roda sem rede |
| `Makefile` | alvo `erro-classificacao` |
| `tests/test_data_prep.py` | 8 testes novos; suíte 175 → **183** |

O teste que carrega mais sentido é
`test_especificidade_alta_nao_salva_o_vpp_com_prevalencia_baixa` — ele trava o
mecanismo de Rull & Ritz como propriedade, não como número.

---

## Referências novas desta fase

```bibtex
@article{rullritz2003misclassification,
  author  = {Rull, Rudolph P. and Ritz, Beate},
  title   = {Historical pesticide exposure in {California} using pesticide use
             reports and land-use surveys: an assessment of misclassification
             error and bias},
  journal = {Environmental Health Perspectives},
  volume  = {111}, number = {13}, pages = {1582--1589}, year = {2003},
  note    = {PMID 14527836. ⚠️ conferido por registro/resumo; texto completo
             nao lido}
}
@article{nuckols2007linkage,
  author  = {Nuckols, John R. and others},
  title   = {Linkage of the {California} Pesticide Use Reporting Database with
             Spatial Land Use Data for Exposure Assessment},
  journal = {Environmental Health Perspectives},
  volume  = {115}, number = {5}, pages = {684}, year = {2007},
  note    = {⚠️ autoria completa a conferir antes de citar}
}
```

⚠️ Nenhuma das duas entra no `paper/referencias.bib` antes de leitura do texto
completo. Ficam aqui, com a ressalva visível.
