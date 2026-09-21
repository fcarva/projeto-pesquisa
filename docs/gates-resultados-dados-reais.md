# Gates E1.5 e E2 contra dado real — os primeiros números do projeto

*2026-08-25. Até esta sessão, **nenhuma fonte real tinha sido tocada**: o
pipeline inteiro (92 testes) rodava contra dado simulado. Isto muda aqui.*

⚠️ **Nada neste documento é resultado do ban.** Tudo é pré-período ou desenho.
Os gates decidem se o Ensaio 1 é estimável; não dizem se a lei funcionou.

---

## 0. O que destravou, e por quê importa

`docs/lacunas-de-dados.md` classificava o acesso a dado como bloqueio de rede.
Era bloqueio **do proxy da sessão remota**, não do projeto:

| Fonte | Sessão remota | Máquina do pesquisador |
|---|---|---|
| `apisidra.ibge.gov.br` | bloqueado | ✅ **200** |
| `ftp.datasus.gov.br` (via `ftp://`) | bloqueado | ✅ **226** |
| `servicodados.ibge.gov.br` | — | ✅ 200 |
| `api.crossref.org` | 000 | ✅ 200 |

⚠️ O DATASUS responde por `ftp://`, **não** por `http://` (000). Isso é normal
— o host não serve HTTP —, mas explica diagnósticos de rede enganosos: testar
com `http://` e concluir "DATASUS fora do ar" é erro fácil de cometer.

---

## 1. ⚠️ Três achados de ambiente que mudam o plano

### 1.1 Não há R nesta máquina

`Rscript` não existe aqui. Duas consequências, e a segunda é séria:

- `00_export_datazoom.R` **não roda** — mas isso não custa nada, porque o
  caminho `pysus` funciona e entrega o mesmo dado (ver §2).
- ⚠️ **O `contdid` também não roda.** O estimador **primário** do Ensaio 1
  (Callaway, Goodman-Bacon & Sant'Anna) é pacote **R**, e o E6 depende dele.
  A fronteira Python↔R por arquivo, que o `CLAUDE.md` fixa, pressupõe que os
  dois lados existam. Hoje só um existe.

**Isto é bloqueio do E6, e não estava em nenhuma lista.** Instalar R + `contdid`
+ `renv` é pré-requisito da estimação, não detalhe de ambiente.

### 1.2 As bibliotecas geo **estão** instaladas

`docs/lacunas-de-dados.md` afirma que "nenhuma biblioteca geo está instalada".
**Não procede nesta máquina:** `geopandas` 1.1.4, `rasterio` 1.5.1 e `pyproj`
respondem. O `06_build_gaez.py` tem com o que rodar assim que o raster existir.

### 1.3 ⚠️ Instalar `pysus` rebaixou o `pandas` do sistema

`pip install pysus==2.10.0` trouxe `pandas 3.0.0 → 2.3.3`, e isso **quebrou um
pacote não relacionado** (`baoba 0.2.0`, que exige `pandas==3.0.0`). O ambiente
Python aqui é global, não virtual.

**Recomendação:** criar um `.venv` para este projeto antes de mais instalações.
O `requirements.txt` já pina as versões; falta o isolamento.

---

## 2. O bug do `pysus`, achado rodando e não lendo

O commit `28fe523` ("Verifica a API do pysus contra o pacote") conferiu a API
**lendo o código** do pacote, porque a sessão remota não podia executá-lo. A
leitura acertou `PySUSClient`, `get_ftp()`, `datasets()` e `search()` — e errou
o último passo:

```python
parquet = client.download_to_parquet(arquivo)
pedacos.append(parquet.to_dataframe())   # ❌ não existe
```

Rodando, dois erros em sequência:

1. `AttributeError: 'Parquet' object has no attribute 'to_dataframe'` — o método
   é **`load()`**;
2. `AttributeError: 'coroutine' object has no attribute 'shape'` — **`load()` é
   corotina**, precisa de `_run_async`, como `datasets()` e `search()`.

Correção aplicada em `02_clean_births.py` e `03_clean_fetal_deaths.py`:

```python
pedacos.append(client._run_async(parquet.load()))
```

⚠️ **É o quarto bug de formato suposto** desta linhagem (aliases datazoom,
parser SIDRA, API pysus, agora `Parquet.load`). O padrão é consistente: **ler o
código de um pacote não substitui executá-lo.**

### O que se conferiu ao rodar, e que a leitura não daria

- `download_to_parquet(..., add_dv=True)` aplica dígito verificador do IBGE. A
  suspeita era que `CODMUNRES` voltasse com **7** dígitos e quebrasse o join por
  `cod_ibge6`. **Não acontece:** conferido, 132.516/132.516 registros de 2015
  com `CODMUNRES` de **6 dígitos**. O join está seguro.
- As 8 colunas de `COLUNAS_SINASC` existem todas na fonte real.

---

## 3. SINASC real — o painel

```
python scripts/data_prep/02_clean_births.py --fonte pysus --anos 2015 ... 2022
```

| | |
|---|---|
| nascimentos (CE, pós-limpeza) | **1.001.709** |
| municípios | 184 |
| células município-mês | 17.654 |
| peso médio | 3.211 g |
| baixo peso (<2500 g) | 8,34% |
| prematuridade (<37 sem) | 12,58% |
| peso ausente | 0,01% |
| células com <5 nascimentos | 2,6% |

As taxas batem com a ordem de grandeza nacional, o que é o teste de sanidade
disponível sem validação externa.

---

## 4. Gate E2 — a variação de dose existe, e a cultura-âncora **não** é o melão

`01_check_dose_variation.py --fonte sidra` (preflight: 4/4 códigos SIDRA
conferidos contra a API de metadados do IBGE).

| cultura | muni c/ área>0 | Gini | % área no decil sup. | especificação recomendada |
|---|---|---|---|---|
| Milho, Feijão | 184 | 0,49–0,51 | 35–37% | curva |
| **Banana (cacho)** | **169** | **0,86** | **78%** | **curva** |
| Castanha de caju | 170 | 0,84 | 70% | curva |
| Coco-da-baía | 165 | 0,92 | 91% | curva |
| Manga | 170 | 0,74 | 60% | curva |
| **Algodão herbáceo** | **28** | 0,96 | 65% | faixas discretas |
| **Melão** | **10** | 0,98 | 35% | ⚠️ **binário — curva abandonada** |

**O gate passa:** há dispersão de dose utilizável e sobra para a curva
não-paramétrica.

⚠️ **E ele responde à flag 1 do `CLAUDE.md`, nos dois sentidos.** O material de
projeto tratava *melão* e *algodão* como candidatos naturais à cultura-âncora,
pela Chapada do Apodi. O dado diz que **nenhum dos dois sustenta a curva**:
melão tem 10 municípios com área positiva, algodão tem 28. Já a **banana** tem
169 municípios, Gini 0,86 e 78% da área no decil superior — dispersão alta *com*
suporte largo, que é a combinação que a curva exige.

A banana também é a cultura que **casa com a química documentada**: procimidona
é fungicida de bananal, e é o princípio ativo que aparece em 23 de 23 amostras
do Dossiê ABRASCO. Milho e feijão têm suporte largo mas Gini baixo — são
lavoura de subsistência espalhada, não alvo de avião.

**A decisão continua sua.** O script recomenda; o `CLAUDE.md` proíbe hard-codar
a âncora. Mas a hipótese "melão" pode ser encerrada empiricamente.

---

## 5. ⚠️ Gate E1.5 — reprova como especificado

O E1.5 pergunta: *a DP das tendências municipais permite detectar 15–25 g com o
número de municípios que o Gate 1 entregou?*

**DP das tendências (não ponderada, como o script 01 calcula): 47,5 g.**

O roteiro previa piso amostral de ~17,7 g e tratava 20 g como "aproximadamente o
melhor caso". O observado é **2,7× o piso**. Consequência:

| cultura | tratados | MDE agrupado | falsifica 15 g? |
|---|---|---|---|
| Banana | 17 | 33,8 g | ✘ |
| Milho / Feijão | 19 | 32,2 g | ✘ |
| Algodão | 3 | 77,4 g | ✘ |
| Melão | 1 | 133,2 g | ✘ |

**✘ em todas as 18 culturas.** Com o efeito esperado de 15–25 g abaixo do MDE de
todas elas, um resultado nulo seria **ilegível** — não distinguiria "o ban não
funcionou" de "o desenho não enxerga".

---

## 6. Mas 63% dessa DP é ruído de amostragem, não heterogeneidade

`07_diagnose_trend_sd.py` (novo) separa as duas componentes. Para cada
município, a variância da diferença de médias tem uma parte que é aritmética de
amostragem, conhecida sem suposição: `s²·(1/n_ini + 1/n_fim)`.

```
DP observada das variações       :  46,9 g
  componente de RUÍDO AMOSTRAL   :  37,3 g
  componente de HETEROGENEIDADE  :  28,4 g   <- é esta que governa o MDE
  fração da variância que é ruído:  63,3%
```

E por porte do município:

| nascimentos/ano | n | DP observada | ruído esperado |
|---|---|---|---|
| < 150 | 32 | 68,2 g | 59,7 g |
| 150–300 | 65 | 49,7 g | 38,2 g |
| 300–800 | 57 | 39,4 g | 26,2 g |
| **≥ 800** | **30** | **17,9 g** | 15,8 g |

⚠️ **O estrato de ≥800 nascimentos/ano dá 17,9 g — praticamente o piso de 17,7 g
que o roteiro calculou.** A conta do roteiro estava certa; o que ela não
antecipou é que a mediana municipal do Ceará é de **283 nascimentos/ano**, não
800. A DP de 47,5 g não mede o mundo: mede municípios pequenos.

### O que muda se o ruído for neutralizado

| cultura | tratados | mediana nasc/ano | MDE (DP obs.) | MDE (DP real) | falsifica 15 g? |
|---|---|---|---|---|---|
| **Banana** | 17 | 403 | 33,4 g | **20,3 g** | **sim** |
| Castanha de caju | 17 | 408 | 33,4 g | 20,3 g | sim |
| Manga | 17 | 656 | 33,4 g | 20,3 g | sim |
| Coco-da-baía | 17 | 937 | 33,4 g | 20,3 g | sim |
| Mamão | 11 | 595 | 40,8 g | 24,7 g | não |
| Algodão | 3 | 1.133 | 76,4 g | 46,3 g | não |

**O veredito do gate se inverte para a banana** — de ✘ para ✔ — condicional a
neutralizar o ruído amostral.

### ⚠️ Mas a própria estimativa de 28,4 g é imprecisa, e isso importa

A decomposição é não-viesada, não precisa. O erro da variância observada é de
ordem `var·√(2/n)`, e com n = 184 municípios isso dá:

| | |
|---|---|
| heterogeneidade real (ponto) | **28,4 g** |
| IC 95% aproximado | **[18,9 ; 35,5] g** |

O que isso faz com o veredito da banana:

| cenário | DP real | MDE banana | meia-largura | falsifica 15 g? |
|---|---|---|---|---|
| piso do IC | 18,9 g | 13,5 g | 9,4 g | **sim, com folga** |
| ponto | 28,4 g | 20,3 g | 14,2 g | **sim, no limite** |
| teto do IC | 35,5 g | 25,3 g | 17,7 g | ⚠️ **não** |

**Leitura honesta:** a inversão do gate é **plausível, não estabelecida**. No
ponto estimado ela passa raspando — meia-largura de 14,2 g contra um piso de
15 g —, e no teto do intervalo ela não passa. Tratar "MDE(real) = 20,3 g" como
número firme seria repetir, na direção otimista, o mesmo erro que a DP não
ponderada comete na direção pessimista.

Duas saídas que **não** dependem de resolver essa imprecisão: aumentar o número
de tratados (baixar o corte de dose, que é a saída já ratificada na L3 para o
E1.5) e reportar o resultado como limite superior informativo, que a §4.6 do
`paper/` já se compromete a fazer.

---

## 7. ⚠️ E aqui está a decisão que é sua, não do script

Neutralizar o ruído **não acontece sozinho**. Há duas vias, e nenhuma é neutra:

**(a) Ponderar por nascimento.** Encolhe o ruído sem descartar município algum.
⚠️ **Mas muda o estimando:** o alvo passa a ser efeito por *criança*, não por
*município*. É defensável — para bem-estar talvez seja o alvo certo — mas é
mudança de parâmetro-alvo, e a §4 do `paper/` teria de dizer isso. Além disso,
o `contdid` com `xformula = ~1` **não aceita covariáveis**; se aceita pesos é
questão a conferir no pacote (e agora se sabe: **conferir rodando**).

**(b) Cortar por porte.** Simples, mas ⚠️ **remove o grupo tratado se os
municípios de dose alta forem os pequenos.** Para a banana, a mediana do decil
superior é de **403 nascimentos/ano**, e só **3 de 17** têm ≥800. Um corte em
800 destruiria o desenho; um corte em 150 preservaria 15 de 17.

**O que o dado diz sobre a via (b), por cultura:** o decil superior da banana
está no estrato 300–800, onde a DP observada é 39,4 g contra ruído de 26,2 g.
Não é o pior caso, e não é o piso.

**Terceira via, que não é ponderação:** aceitar o MDE observado e reportar o
resultado como **limite superior informativo**, que é o compromisso que a §4.6
do `paper/` já declara. Isso não exige decisão metodológica nova — exige apenas
não chamar de achado o que está abaixo do MDE.

---

## 7-bis. Os canais: SIM construído, SIH vazio, e uma fonte melhor que ninguém tinha olhado

*Acrescentado 2026-08-25, na mesma sessão.*

### 7-bis.1 ⚠️ Óbito fetal NÃO está no DO — a nota do script estava errada

`03_clean_fetal_deaths.py` afirmava, em docstring: *"Óbito fetal não é arquivo
separado. No SIM moderno vem dentro do DO (`DO<UF><ano>`), identificado por
TIPOBITO"*. **Falso**, e conferido rodando: em `DOCE2015.dbc` os **55.258
registros têm TIPOBITO = 2**. Nem um óbito fetal.

A série fetal está em `SIM/CID10/DOFET/DOFET<AA>.dbc` — **nacional**, não por
UF, e com TIPOBITO = 1 em 100% das linhas. ⚠️ **O `pysus` não alcança esses
arquivos**: o dataset SIM dele indexa só `CID10/DORES` e `CID9/DORES`
(conferido em `sim.paths`). Daí a nova fonte `--fonte dofet`, que baixa por FTP.

**Três bugs a mais, todos silenciosos, todos achados rodando:**

| Sintoma | Causa real |
|---|---|
| `search(group="DO", ...)` devolve `[]` | ⚠️ o kwarg `group` é aceito e **ignorado em silêncio**, embora `group_definitions` anuncie `'DO'`. Sem ele, vem o arquivo certo |
| `TypeError: agg function failed [how->mean,dtype->object]` | `IDADEMAE` vem como **texto** das fontes reais e o colapso faz `mean` nela |
| painel com **185** municípios | ⚠️ `230000` ("município ignorado") não era descartado — o script 02 já descartava. Uma unidade sem denominador possível, e taxa com numerador que o denominador não cobre |

**Painel construído:**

| | |
|---|---|
| óbitos fetais (CE, pós-limpeza) | **11.240** |
| municípios | 184 ✅ (bate com o painel de nascidos vivos) |
| acima do limiar de notificação | 10.625 (94,5%) |
| taxa de óbito fetal | **1,11%** |
| ⚠️ células com < 5 óbitos | **98,7%** |

A taxa é plausível. ⚠️ Mas 98,7% das células município-mês têm menos de 5
óbitos: o teste de seleção da flag 6 **não roda no nível município-mês** —
precisa de município-ano ou de faixas de dose empilhadas. Isso é propriedade do
desfecho, não defeito do dado.

### 7-bis.2 O SIH agora dispensa R — e mostra que o canal A5 não existe nele

`04_clean_poisoning.py` só aceitava arquivo do `00_export_datazoom.R`. ⚠️ Sem R
instalado, o canal A5 inteiro estava inacessível **por uma razão de linguagem,
não de dado**. Foi acrescentada a fonte `--fonte pysus` (AIH Reduzida, mensal).

⚠️ **E o resultado é um gate negativo, agora com a série de 8 anos completa.**

| SIH/CE, 2015–2022 | |
|---|---|
| AIH baixadas | ~3,9 milhões |
| internações com CID de agrotóxico | **50** |
| municípios alcançados | 27 de 184 |
| células município-mês | 46 de 17.664 |
| ⚠️ **acidental** (o canal de substituição) | **1** |
| ⚠️ **autoprovocada** (o placebo) | **1** |
| células com < 5 internações | **100%** |

**O gate do A5 no roteiro** pergunta se a série acidental tem suporte para ser
estimável. **Não tem, e a margem é absurda:** *uma* internação acidental em oito
anos no estado inteiro. Não se conserta com agregação — não há o que agregar.

⚠️ **E o placebo morre junto.** O desenho do canal depende de contrastar
acidental (X48) com autoprovocada (X68); com 1 evento de cada lado, o contraste
não existe. Note ainda a assimetria: 48 das 50 internações têm código **T60**
(a molécula) mas **não** têm código de intenção. No SIH, a divisão por intenção
— que **é** o desenho do placebo — praticamente não é preenchida.

A razão é estrutural: SIH é **internação faturada**, e intoxicação aguda por
agrotóxico costuma ser atendida em emergência sem internar.

### 7-bis.3 ✅ SINAN/IEXO — o sistema que existe para exatamente isto

O `pysus` expõe o SINAN, e entre seus 49 agravos está **`IEXO` — Intoxicação
Exógena**, a notificação compulsória específica. Comparação para o Ceará, 2015:

| fonte | eventos no Ceará |
|---|---|
| SIH, **8 anos** (2015–2022) | **50** — dos quais **1** acidental |
| **SINAN/IEXO**, **1 ano** (2015) | **2.914** — dos quais **266** de agrotóxico agrícola |

Ou seja: um único ano de SINAN entrega ~58× mais eventos que oito anos de SIH,
e ~266 vezes mais eventos de agrotóxico agrícola do que o SIH entrega de
intoxicação acidental na janela inteira.

E o formulário traz, nomeadamente, os campos que o desenho do canal pede:

| campo | serve a |
|---|---|
| `AGENTE_TOX` | separar agrotóxico dos demais agentes |
| **`CIRCUNSTAN`** | ⚠️ **a divisão acidental × autoprovocada — que É o placebo** da §7-bis |
| `ID_OCUPA_N` | exposição ocupacional, que é a hipótese de substituição |
| `ID_MUNICIP`, `DT_NOTIFIC` | a chave do painel |
| `ZONA` | urbano/rural |

Distribuição no Ceará em 2015: `AGENTE_TOX` = 02 aparece 266 vezes, 03 aparece
45; `CIRCUNSTAN` = 10 aparece 739 vezes, 02 aparece 295.

### ✅ Os códigos do agente tóxico, conferidos contra a fonte oficial

Não ficaram na suposição. A **Nota Técnica nº 5/2026-CGVAM/DVSAT/SVSA/MS**
(`ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DOCS/Nota_Tecnica_Intoxicacao_Exogena.pdf`),
§3.5, enumera o *Campo 49 — Grupo do Agente Tóxico / Classificação Geral*:

| código | significado | uso no Ensaio 1 |
|---|---|---|
| **02** | **Agrotóxico de uso agrícola** | ✅ **é o canal A5** — 266 notificações no CE em 2015 |
| 03 | Agrotóxico de uso doméstico | contraste: não passa por avião |
| **04** | **Agrotóxico de uso em saúde pública** | ⚠️ **é o §2º do art. 28-B** — o controle vetorial, que é a flag 5 |
| 05 | Raticidas | fora do escopo |
| 06 | Produtos veterinários | fora do escopo |

⚠️ **O código 04 não é detalhe.** O §2º da redação de 2019 proíbe a dispersão
aérea para **controle vetorial**, e é dela que vem a contaminação do grupo
`d = 0` da flag 5 — municípios sem agricultura pulverizada mas com controle
aéreo de endemias **são tratados**. O SINAN separa esse agente dos demais, de
modo que a contaminação deixa de ser hipótese e passa a ser **mensurável**.

⚠️ **E há mais: o SINAN nomeia a molécula.** A mesma nota (§3.1) registra que o
*Campo 50* traz `AGENTE_1/2/3`, `P_ATIVO_1/2/3` e `OUT_AGENTE` — nome comercial
e **princípio ativo**. Isso alcança diretamente a química que o Dossiê ABRASCO
achou na Chapada do Apodi (procimidona, carbaril, carbofurano, fenitrotiona), e
que a flag 2 do `CLAUDE.md` diz não ser glifosato. ⚠️ São **campos abertos**,
com grafia heterogênea — a própria nota técnica existe porque a filtragem por
descritor textual é trabalhosa e precisa de lista de variantes.

⚠️ **`CIRCUNSTAN` continua NÃO conferido.** A nota trata do agente, não da
circunstância. A leitura provável (10 = tentativa de suicídio, 02 = acidental)
segue **suposição** — e é justamente a divisão que sustenta o placebo. Conferir
na Ficha de Investigação antes de escrever o ingestor.

⚠️ **E `ID_MUNICIP` tem 7 dígitos** (com dígito verificador), contra os 6 de
`cod_ibge6`. A truncagem é obrigatória, e é o mesmo tipo de armadilha que o
`add_dv` do `pysus` quase criou no SINASC.

**Decisão que é sua:** trocar a fonte do canal A5 de SIH para SINAN/IEXO. Não é
mudança de estratégia de identificação — o canal e sua predição continuam os
mesmos —, mas é troca de fonte declarada, e o `CLAUDE.md` pede que fonte tenha
*vintage* registrada. O SIH pode ficar como série secundária: ele mede **caso
grave internado**, que é outro estimando, não um pior.

### 7-bis.4 ⚠️ A janela não fecha em 2024 — o SINASC para em 2022

Pergunta em aberto no roteiro: *"SINASC 2024 já está disponível na vintage
necessária? (define se a janela fecha em 2024 ou 2023)"*. **Resposta: nenhum
dos dois.** Listagem do FTP do DATASUS em 2026-08-25:

| base | anos disponíveis para CE |
|---|---|
| **SINASC definitivo** (`NOV/DNRES`) | 2013 – **2022** |
| SINASC preliminar (`PRELIM/DNRES`) | ⚠️ **apenas 2025 e 2026** |
| SIM DO (`CID10/DORES`) | até **2024** |
| SIM DOFET | até **2024** |

⚠️ **2023 e 2024 do SINASC não estão no FTP** — nem definitivos nem
preliminares. Há um vão entre o que saiu do preliminar e o que entrou no
definitivo.

**Consequência para o desenho, e ela é séria.** A janela declarada é
2015 → 19/12/2024, cortada na Lei 19.135/2024 para preservar a cota zero. Para
o **desfecho principal**, o pós-ban disponível é **2019–2022** — quatro anos, e
não seis. Os anos preliminares de 2025–2026 existem, mas são **posteriores à
exceção de drones**: usá-los contamina exatamente o que o corte da janela
protege.

Isso **não** invalida o desenho: quatro anos de pós-ban são suficientes para o
colapso pré/pós que o `contdid` exige. Mas muda o que o texto pode prometer, e
deve entrar na §4 do `paper/` junto com a janela. **Conferir se a Base dos
Dados (BigQuery) tem 2023–2024** antes de dar a janela por fechada — é a rota
alternativa que o `CLAUDE.md` já lista para o SINASC.

---

## 7-ter. ✅ Gate E5 — as trilhas se encontram, e o painel existe

`05_build_panel.py --cultura "Banana (cacho)"` contra as bases reais:

| | |
|---|---|
| municípios | **184** |
| meses | 96 (2015–2022) |
| células (balanceado) | **17.664** |
| colunas | 65 |
| dose > 0 | 169 municípios; dose = 0 em 15 |
| cobertura de `peso_medio` | 99,9% |
| cobertura de `n_obito_fetal` | 99,9% |

**O gate E5 pergunta se as chaves casam** — PAM tem código IBGE de 7 dígitos,
SINASC tem `CODMUNRES` de 6. **Casam:** 184 × 96 = 17.664 sem célula órfã, e os
três painéis (dose, nascimentos, óbito fetal) entram com ~100% de cobertura.

⚠️ **A cultura passada é `Banana (cacho)` porque é a que o Gate 1 sustenta —
não porque esteja ratificada.** O script exige `--cultura` e se recusa a
escolher; a flag 1 continua aberta até você decidir.

**E a retroprojeção gestacional se comporta como o desenho previa:**

| coorte | gestação pós-ban | marcação ingênua |
|---|---|---|
| 2018-12 | 0,00 | 0 |
| **2019-01** | **0,00** | **1** ← ingênuo diz tratado; a gestação foi toda antes |
| 2019-05 | 0,44 | 1 |
| 2019-10 | 1,00 | 1 |

### ⚠️ O bug que impedia o encontro era o NOME DO ARQUIVO

O script 01 grava `pam_ce_muni_cultura_media__sidra.parquet` — **sempre com o
nome da fonte**, de propósito, para que diagnóstico simulado nunca ocupe o nome
canônico. O script 05 procurava apenas por `""` e `__simulado`.

Resultado: o PAM real existia na pasta, o painel não montava, e a mensagem de
erro mandava *"rode antes o script 01"* — que **já tinha rodado**. Duas
convenções de nome dentro do mesmo pipeline, e o erro apontando para o lugar
errado.

Corrigido com `resolve_pam()`, agora função de módulo e coberta por **4 testes
de regressão** — inclusive o de que `--fonte real` nunca cai no simulado, que é
o erro que nenhum resultado denuncia.

---

## 8. O que fazer em seguida, em ordem

1. ⚠️ **Instalar R + `contdid`.** É bloqueio do E6 e não estava mapeado. Sem
   isso não há estimação, por mais limpo que o painel esteja.
2. **Decidir a via da §7** — ponderação, corte de porte, ou limite superior — e
   registrar com data, porque o E3 exige que a escada de especificação seja
   declarada antes de estimar.
3. **Ratificar (ou recusar) a banana como cultura-âncora**, agora que melão e
   algodão estão empiricamente descartados para a curva.
4. **Criar um `.venv`** — ver §1.3.
5. **Levantar os bans municipais < 2019.** Continua sendo a única lacuna cuja
   ausência produz resultado errado **em silêncio**, e continua sem depender de
   rede.
6. ~~Rodar `03_clean_fetal_deaths.py` contra o SIM real~~ — ✅ **feito**, via a
   nova fonte `--fonte dofet`. Ver §7-bis.1.
7. **Decidir a fonte do canal A5**: SINAN/IEXO (2.914 eventos/ano no Ceará)
   contra SIH (4). Ver §7-bis.3 — e conferir o dicionário de `AGENTE_TOX` e
   `CIRCUNSTAN` **antes** de escrever o ingestor.
8. ⚠️ **Conferir se a Base dos Dados tem SINASC 2023–2024.** O FTP do DATASUS
   não tem, e sem eles o pós-ban do desfecho principal é 2019–2022. Ver
   §7-bis.4.

---

## 9. Reprodução

```bash
python scripts/data_prep/01_check_dose_variation.py --verificar-codigos
python scripts/data_prep/01_check_dose_variation.py --fonte sidra
python scripts/data_prep/02_clean_births.py --fonte pysus --anos 2015 2016 2017 2018 2019 2020 2021 2022
python scripts/data_prep/01_check_dose_variation.py --fonte sidra \
    --nascimentos data/processed/nascimentos_ce_muni_mes.parquet
python scripts/data_prep/07_diagnose_trend_sd.py
```

Vintages: SIDRA/PAM tabelas 1612 e 1613, extração **2026-08-25**; SINASC via
`pysus` 2.10.0, arquivos `DNCE2015`–`DNCE2022`, extração **2026-08-25**.
Saídas em `data/processed/` — gitignored, como manda o `CLAUDE.md`.
