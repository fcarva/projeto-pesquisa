# Lacunas de dados — por prioridade, não por lista

*2026-08-25. O pipeline está completo (92 testes, E5–E7 instrumentados).*
*⚠️ Atualizado 2026-09-21: **onze scripts, 139 testes**; ver o histórico abaixo.*

⚠️ **ATUALIZADO em 2026-08-25, mesma data: DUAS FONTES REAIS JÁ FORAM TOCADAS.**
O bloqueio de rede era do **proxy da sessão remota**, não do projeto: na máquina
do pesquisador o SIDRA responde 200 e o DATASUS responde 226 por `ftp://`.
PAM e SINASC estão adquiridos, e os gates E2 e E1.5 têm número real.
**Ver `docs/gates-resultados-dados-reais.md`** — inclusive porque o E1.5
reprova como especificado, e a razão não é a que se esperava.

⚠️ **A lista A1–A6 do roteiro é plana, e a realidade não é.** O achado do E6
reordenou tudo: uma fonte deixou de ser "canal" e virou parte do resultado
principal. Tratar as seis como igualmente urgentes desperdiça o recurso mais
escasso, que é tempo.

---

## 0. O que mudou a prioridade

O sieve do `contdid` faz, no bloco do CCK:

```r
m0 <- mean(dy[dose == 0])    # a curva inteira é centrada nisso
```

**A curva é centrada na variação média do grupo de dose zero.** Então quem está
no `d = 0` não afeta a interpretação — afeta **o nível do número**.

Isso promove o **FAO-GAEZ** de instrumento para **tripla função**:

| Papel | Onde | Status depois do E6 |
|---|---|---|
| Instrumento da exposição endógena | §5.2 da modelagem | como sempre foi |
| **Definição 4 de `d = 0`** | §5.3, construção 4 | ⚠️ **mecânico** |
| **Teste de contaminação do zero** | §5.3, teste | ⚠️ **mecânico** |

E como a construção 3 depende de ANAC/SEMACE — também não adquirido —, **sem
GAEZ três das quatro definições de zero são impossíveis, e o nível da curva fica
sem banda de incerteza.**

**GAEZ não é canal. É o resultado principal.**

---

## 1. As lacunas, por classe de resolução

Cada classe pede uma ação diferente. Misturá-las é o que faz a lista parecer
intransponível.

### Classe A — ✅ **adquirida**, não apenas contornada

| Fonte | Situação em 2026-08-25 |
|---|---|
| **PAM/SIDRA** | ✅ **baixada** — `01_check_dose_variation.py --fonte sidra` roda direto (preflight: 4/4 códigos conferidos) |
| **SINASC** | ✅ **baixado** — `02_clean_births.py --fonte pysus`, 1.001.709 nascimentos, 2015–2022 |
| SIM, SIH | caminho `pysus` desbloqueado e **corrigido** (ver abaixo); ainda não rodados |

⚠️ **O caminho `pysus` estava quebrado, e só rodando se descobriu.** Não existe
`Parquet.to_dataframe()`; o método é `load()`, e é **corotina**. Corrigido em
`02_clean_births.py` e `03_clean_fetal_deaths.py`. É o **quarto** bug de formato
suposto desta linhagem — ler o código de um pacote não substitui executá-lo.

⚠️ ~~**`00_export_datazoom.R` não roda aqui: não há R nesta máquina.**~~
**CORRIGIDO em 2026-09-21: há R.** R 4.6.1 está instalado desde 13/08/2026, só
**fora do PATH** — a verificação anterior testou o PATH e concluiu ausência.
`00_export_datazoom.R` roda por caminho absoluto. O que bloqueia o E6 é
**Rtools + pacotes** (`contdid`, `ptetools`, `pretrends`, `HonestDiD`, `synthdid`,
`renv` — todos ausentes), não a ausência da linguagem. Ver
`docs/gates-resultados-dados-reais.md` §1.1.

### Classe B — falta baixar **e** falta o ingestor

| Fonte | Serve a | Ingestor existe? |
|---|---|---|
| ~~**FAO-GAEZ**~~ ✅ **ADQUIRIDO 2026-09-21** | instrumento + zero 4 + teste de contaminação | ✅ `06_build_gaez.py` — 184/184 municípios, primeiro estágio confere |
| ANA (ottobacias) | canal-água (montante/jusante) | ❌ |
| SISAGUA | canal-água (qualidade) | ❌ |
| MapBiomas | canal-ar (deriva); melhora a medida de dose | ❌ |
| INMET / FUNCEME | canal-ar (vento a favor/contra) | ❌ |
| População municipal (IBGE) | denominador do canal de intoxicação | ✅ **`11_clean_populacao.py`** — SIDRA 6579 + Censo 4709 |

⚠️ ~~**nenhuma biblioteca geo está instalada**~~ — **não procede na máquina do
pesquisador** (verificado 2026-08-25): `geopandas` 1.1.4, `rasterio` 1.5.1 e
`pyproj` respondem. O `06_build_gaez.py` tem com o que rodar assim que o raster
existir. `data/geo/` continua vazio — falta o **arquivo**, não a biblioteca.

✅ Resolvido: `requirements-geo.txt`. Separado do `requirements.txt` porque
GDAL/PROJ/GEOS são pesados e brigam, e o pipeline 01–05 não precisa deles.
`pypi.org` está liberado no proxy, então é instalável.

### Classe C — administrativamente travada

| Fonte | Ação | Prazo |
|---|---|---|
| ~~**MAPA**~~ ✅ **é DADO ABERTO** — LAI desnecessária | `dados.agricultura.gov.br/dataset/sipeagro`, CC-BY | ⚠️ mas **não serve à definição 3** — ver §1-bis |
| **SEMACE / ANAC / SINDAG** | protocolar a LAI (minuta em `07-layer4-*.md`) | 20 dias + 10. **Único com relógio externo** |
| **Bans municipais < 2019** ⚠️ | levantamento legislativo. **Fase 1 = decil superior (~30)**, não os 184 | nenhum, mas é anterior ao Gate 1 em importância. ✅ **1 achado já confirmado** |

Nenhum script resolve estas. Precisam de uma pessoa.

⚠️ **O segundo deixou de ser condicional em 2026-09-21.** Limoeiro do Norte
proibiu pela **Lei Municipal 1.478, de 20/11/2009** — conferido em fonte primária
—, e ele **está no decil superior da banana** (6º de 169; o decil tem 17
municípios). Então **há**, e não "se houver", unidade já tratada dentro do grupo
de dose alta: ~6% dele. Para essa unidade a dose de 2015–2018 já vem suprimida
pelo próprio ban municipal — **contamina a medida de dose**, não só o desfecho.
A varredura dos outros 16 do decil é o que falta.

### 1-bis. ⚠️ O SIPEAGRO é aberto — e mesmo assim não fecha a definição 3

*2026-09-21.* O `d = 0` da **definição 3** é o zero que mede o **método** (quem
pode pulverizar por ar), não a cultura-proxy. A Classe C dava isso como
bloqueado por LAI. **Não está:** o MAPA publica o SIPEAGRO em dados abertos,
licença CC-BY, em CSV — `dados.agricultura.gov.br/dataset/sipeagro`.

São dois arquivos, e nenhum dos dois entrega o que a definição 3 precisa:

| arquivo | o que tem | por que não serve |
|---|---|---|
| **Registro** (7,7 MB) | 27 estabelecimentos no CE, 16 municípios | ⚠️ **sem coluna de data** — retrato do presente. E **100 de 107 registros são drone**, legalizado no CE só em 19/12/2024. Mede o mundo pós-exceção, não a capacidade pré-2019 |
| **Autorização** (161 MB) | 739.137 autorizações, com `MUNICIPIO_AUTORIZADO` e datas de validade | ⚠️ **a série começa em 2021** (1.234 registros; só 2022 em diante é densa). **Não alcança a janela pré-ban** |

**Conclusão honesta: a definição 3 de `d = 0` continua sem fonte**, e agora se
sabe que não é por barreira administrativa — é porque o registro federal não
tem profundidade histórica. A LAI à SEMACE segue valendo, e agora é a **única**
rota para o pré-período.

### ✅ Mas duas coisas se aproveitam

**1. Um teste de *enforcement*, que a flag 3 pedia.** No arquivo de
autorizações, 2022–2026:

| UF | autorizações |
|---|---|
| Piauí | 67.014 |
| Maranhão | 18.100 |
| Bahia | 7.747 |
| **Ceará** | **0** |

Zero contra dezenas de milhares nos vizinhos do mesmo bioma. Não prova ausência
de pulverização — prova ausência de **autorização federal**, que é o que o
registro mede. Mas a flag 3 ("proibir método ≠ proibir molécula") ganha aqui
sua primeira evidência quantitativa de que o ban não é letra morta no cadastro.

⚠️ **Ressalva que não pode sumir:** a série começa em 2021, então isto é
comparação **pós-ban contra pós-ban**. Não há contrafactual pré-ban no arquivo.

**2. O mapa dos drones, para o corte da janela.**
`docs/legislacao/sipeagro-aeroagricola-ce.csv` lista os 16 municípios cearenses
com operador registrado. Como quase tudo ali é drone e drone só é legal desde
19/12/2024, essa tabela descreve exatamente o regime que o corte da janela
**exclui** — é o retrato do que viria depois, útil para o Ensaio 2 (troca de
instrumento) e para justificar o corte.

⚠️ Note que **Limoeiro do Norte tem 5 estabelecimentos e a única aeronave
convencional registrada no estado** — o município que proibiu em 2009 e
revogou a proibição em maio de 2010, num artigo da Lei 1.511/2010 (`docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md` §5).

### 1-ter. ⚠️ O canal-água: SISAGUA adquirido, e ele traz uma armadilha que
inverteria o resultado

*2026-09-21.* `vigilancia_demais_parametros` do SISAGUA
(`s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SISAGUA/`, 105 MB, aberto):

| | |
|---|---|
| medições de agrotóxico no CE | **58.061** |
| municípios | **184 de 184** |
| cobertura anual 2015–2022 | 171 a 184 municípios **todo ano** |
| princípios ativos nomeados | 28, com VMP |

A cobertura é a melhor de qualquer fonte deste projeto. E mesmo assim o canal
**não está pronto**, por três razões — a terceira é séria.

#### ⚠️ 1. Três das quatro moléculas do Dossiê ABRASCO não são monitoradas

A flag 2 do `CLAUDE.md` registra que a tabela do PL 18/2015 achou, na Chapada do
Apodi, **procimidona e carbaril em 23/23** amostras, **carbofurano em 18/23**,
**fenitrotiona em 16/23** — e glifosato em só 4/23.

No SISAGUA/CE:

| molécula | medições |
|---|---|
| **procimidona** (*fungicida de bananal*) | **0** |
| **carbaril** | **0** |
| **fenitrotiona** | **0** |
| carbofurano | 1.833 |
| glifosato + AMPA | 1.563 |

**A lista da Portaria não é a lista da Chapada do Apodi.** O monitoramento mede
bem justamente a molécula que o Dossiê achou de menos (glifosato) e **não mede**
a que ele achou em todas as amostras. O canal-água, como fonte, não alcança a
química que a flag 2 identifica como a do problema.

#### ⚠️ 2. 95% das amostras são de água TRATADA

`Procedência da Coleta`: 55.019 de "SISTEMA DE DISTRIBUIÇÃO" contra **1.284** de
"PONTO DE CAPTAÇÃO (água superficial)". Para deriva de pulverização o que
interessa é o manancial; o que se mede é o que saiu da ETA. E `Latitude`/
`Longitude` vêm preenchidas em **260 de 58.061** registros (0,4%), então o
desenho montante/jusante **não tem coordenada** para se apoiar.

#### ⚠️⚠️ 3. A quebra de registro que produziria um "efeito" inteiro do nada

Detecções (resultado numérico > 0) no Ceará, por ano:

    2015: 41    2016: 13    2017: 5    2018: 20    2019: 44
    2020:  0    2021:  0    2022: 0   ← em 18.480 amostras

Zero exato, três anos seguidos, com **mais** amostras que antes. E a categoria
`MENOR_LQ` aparece exatamente quando o numérico some: 0, 1, 0, 1, 0 → **170,
186, 360**.

**Não é fenômeno nacional.** Comparação do percentual de resultados numéricos:

| ano | Ceará | Brasil |
|---|---|---|
| 2015–2019 | 0,1 – 0,6% | 14 – 51% |
| **2020** | **0,00%** | 49,8% |
| **2021** | **0,00%** | 31,9% |
| 2022 | 0,00% | 4,0% |

Em 2020 o Brasil reporta metade dos resultados como número e o Ceará reporta
**nenhum**. É mudança de prática laboratorial cearense, e ela começa no ano
seguinte ao ban.

> ⚠️ **Um DiD sobre "agrotóxico detectado na água" acharia que o ban eliminou
> 100% das detecções — e isso seria artefato de registro, não efeito
> ambiental.** O achado seria grande, significativo, e completamente espúrio.
> É o pior caso do repositório: o pipeline roda, o número sai, e está errado.

#### O que resta do canal

Não é inutilizável, mas o que sobra é menor do que se esperava:

- **pré-período 2015–2018 é usável** — detecções variam (41, 13, 5, 20) e a
  cobertura municipal é quase completa;
- **o pós-período não é comparável ao pré** na variável de detecção;
- a alternativa é tratar `MENOR_LQ` como categoria ordinal, mas ela **só existe
  a partir de 2020** — não há pré-período para ela.

**Decisão que é sua:** o canal-água vira (a) descritivo de pré-período, (b)
alvo de uma requisição de microdado laboratorial à SESA/CE com os valores
brutos, ou (c) sai do escopo. A matriz da §2 dizia que sem ele "o mecanismo
fica postulado, não medido" — continua assim, e agora se sabe por quê.

#### ⚠️ AUDITADO em 2026-09-22 — o alerta procede, a explicação não

`scripts/data_prep/17_audita_sisagua.py`. **O aviso acima continua de pé: um
DiD sobre "detectado" acharia eliminação de 100% e estaria errado.** Mas as
razões mudam, e uma das conclusões se inverte.

**1. A quebra NÃO é de sensibilidade analítica.** Era a hipótese natural e
ninguém a tinha testado. LD e LQ medianos do Ceará ficam em **0,10 e 0,30
µg/L de 2019 a 2023**, atravessando a quebra sem se mexer.

**2. E as detecções antigas sobreviveriam ao regime novo.** Das 123 detecções
numéricas de 2015–2019, só **2,4%** ficam abaixo do próprio LQ do registro
(mediana 0,37 µg/L; máximo 10,25). **56% continuariam quantificáveis** sob o LQ
de 0,30 vigente em 2020–2023 — e **78%** sobreviveriam ao LD. Nenhuma
reapareceu. O zero não é censura; é reporte.

**3. São quatro anos, e os numéricos voltam.** 2023 também é zero (4.957
amostras, 100% `MENOR_LD`). Em **2024 o LQ mediano cai ~30×** (0,30 → 0,0101) e
os numéricos reaparecem junto. A `MENOR_LQ` aparece só em 2020–2022 e some em
2023: convenção adotada e abandonada.

**4. ⚠️ São TRÊS categorias, não duas.** O texto acima só cita `MENOR_LQ`.
`MENOR_LD` é a maior de todas — 280 mil dos 476 mil registros nacionais, e
~99% dos cearenses **em todos os anos, inclusive no pré**.

**5. ⚠️ E "não é fenômeno nacional" não se sustenta.** Zerar o numérico é
comum: **5 a 9 de ~20 UFs** zeram em qualquer ano dado; Paraíba e Tocantins
zeram em quase todos; o Ceará já zerava em **2014**. O resto do país também
desaba — 57% de numéricos em 2020, 5,0% em 2022.

> **A conclusão muda de forma, e fica pior para o canal.** O problema não é uma
> quebra em 2020: é que a série **nunca teve variância**. São 123 detecções em
> ~31 mil amostras de 2015–2019 — **0,4%**, contra 7–55% no resto do país. A
> frase "o pré-período 2015–2018 é usável" é a que **não sobrevive**, mais do
> que a do pós. A saída (a) — descritivo de pré-período — perde a base; as
> saídas (b) e (c) ficam de pé.

### 1-quater. ✅ A D4 é viável — e o que ela custa

*2026-09-21.* A **D4** pergunta se a janela que define a dose recua de 2015–2018
para 2010–2014. Ela importa porque o `CLAUDE.md` registra três marcos de
antecipação, e o primeiro é **24/02/2015** — a apresentação do PL 18/2015. A
janela atual **começa depois do marco de notícia**, então a dose medida pode já
estar respondendo à expectativa do ban. Isso morde a **variável de tratamento**,
não só o desfecho.

**Comparabilidade: passa nos três testes.**

| teste | resultado |
|---|---|
| mesmas tabelas/códigos | ✅ 1612/1613, variáveis 109/2313, classificações 81/82 — período 1974–2025 |
| mesmos municípios | ✅ **184 em ambos**, zero entram, zero saem |
| mesmas culturas | ✅ **86 em ambos**, nenhuma aparece ou some |
| costura 2014→2015 | ✅ banana 46.654 → 44.482, dentro da tendência. Sem degrau |

**⚠️ Mas recuar a janela troca quem é tratado:**

| cultura | ρ de Spearman | tratados que coincidem |
|---|---|---|
| **Banana** | 0,848 | **13 de 17 (76%)** |
| Castanha de caju | 0,957 | 15/17 (88%) |
| Coco-da-baía | 0,886 | 15/17 (88%) |

Quatro dos 17 tratados da banana mudam. Não é ruído de borda: é **24% do grupo
tratado**, e o MDE do gates doc §6 é calculado sobre exatamente esses 17.

⚠️ **Limoeiro do Norte é tratado nas DUAS janelas** — a contaminação da flag 0
não se resolve recuando a janela.

**Instrumentado, não decidido.** O script 01 ganhou `--anos`, e a janela
não-padrão grava com sufixo próprio (`__2010_2014`). Sem o sufixo, rodar a
sensibilidade sobrescreveria o painel canônico e o script 05 leria o arquivo de
sempre com dose de outra janela — sem nada acusar. Dois testes de regressão
prendem isso.

⚠️ E um bug apareceu no caminho: `carrega_pam_arquivo` usava `ANOS_PRE_BAN`
fixo, então `--anos 2010 … 2014 --fonte arquivo` filtrava para 2015–2018 e
devolvia **vazio, sem erro**. Corrigido.

**A decisão continua sua:** recuar a janela compra um pré-período anterior ao
marco de notícia e paga com 24% de troca no grupo tratado. As duas rodadas
existem lado a lado em `data/processed/`; a escolha vai para a §4 da
pré-especificação com a razão declarada.

### 1-quinquies. ⚠️ O vento: dado excelente, desenho bloqueado a montante

*2026-09-21.* O último canal aberto. A matriz da §2 promete que sem ele falta
"o teste de direção que separa deriva de confundidor".

**O dado existe, é aberto e é bom.** `portal.inmet.gov.br/uploads/dadoshistoricos/
<ano>.zip` (102 MB/ano). Para o Ceará, **14 estações automáticas**, horárias,
com **direção em graus, velocidade e rajada — 100% preenchidos** (8.783 de
8.784 horas em 2016, na estação de Jaguaribe).

⚠️ A **API** `apitempo.inmet.gov.br/estacao/...` devolve **HTTP 204 para todas
as estações** em datas históricas. Quem testar por ela conclui "o INMET não tem
o dado". O ZIP anual tem.

#### ⚠️ E aqui o achado inverte a expectativa

Direção média do vento, por estação, 2016:

| | |
|---|---|
| faixa entre as 14 estações | **63° a 112°** — todas de leste/nordeste |
| **coerência circular ENTRE estações** | **0,96** |
| direção média estadual | **89°** (leste — os alísios) |

**São os alísios, e eles sopram sempre igual.** A coerência de 0,96 significa
que **não há variação espacial de direção** no Ceará.

> ⚠️ **É a regularidade que mata o teste transversal.** Se o vento vem sempre de
> leste, "a favor do vento" é perfeitamente colinear com "está a oeste da
> fonte" — e isso é **geografia, não vento**. Qualquer confundidor com gradiente
> leste-oeste (distância do litoral, altitude, chuva, e no Ceará os três
> variam assim) seria indistinguível de deriva. O teste não separaria o que
> promete separar.

#### O que sobra, e por que também não fecha

A variação **temporal** existe: em Jaguaribe, a estação mais próxima da Chapada
do Apodi, só **42%** das horas ficam a ±45° da direção média e **22%** saem do
quadrante leste (coerência interna 0,42 — a menor do estado).

Isso permitiria um teste de **timing**: efeito maior quando o vento soprou da
lavoura para o receptor. ⚠️ **Mas exige saber QUANDO se pulverizou** — e o
cadastro aeroagrícola do MAPA, conferido na §1-bis, **começa em 2021 e tem zero
registros para o Ceará**. A data de aplicação não existe para a janela pré-ban.

**Conclusão: o vento não é lacuna de aquisição, é desenho bloqueado a montante.**
Adquiri-lo agora seria escrever ingestor para um teste sem o outro insumo — o
que a §5 deste documento proíbe.

✅ **Um detalhe que corrobora o mecanismo, de graça:** a velocidade mínima do
dia em Jaguaribe é às **08h UTC (05h local): 2,0 m/s**, contra 3,6 m/s à tarde.
É exatamente a janela em que a pulverização aérea é feita — de madrugada,
justamente para minimizar deriva. O dado de vento confirma a prática descrita
na literatura, ainda que não sirva ao teste de direção.

### Classe D — ✅ **quatro respondidas em 2026-09-21**, uma segue aberta

| Pergunta | Resposta | Consequência |
|---|---|---|
| O catálogo do GAEZ cobre **banana**? | ✅ **sim** — "Banana" consta das *GAEZ Summary Tables* (gaez.fao.org) e há camada "Banana Plantain Suitability Index" pela metodologia GAEZ | **O instrumento é viável para a âncora que o Gate 1 recomenda.** Destrava o item 4 da §3 |
| …e **melão**? | ⚠️ **não conferido** — o portal é JS e a lista completa não saiu nem do FAQ nem do catálogo DCAT | Pesa pouco: o Gate 1 já descartou o melão para a curva (10 municípios) |
| O cadastro da SEMACE é público e tem série com município? | ⚠️ **parcialmente, e provavelmente não serve.** Existe o **SICRA** (ce.gov.br/semace/…/sicra), mas ele cadastra *"empresas Registrantes/Fabricantes e seus produtos"* — **fabricante e produto, não prestador de aplicação por município** | ⚠️ **Não é a definição 3 de `d = 0`.** O art. 8º pede o registro de quem *aplica*; o SICRA registra quem *fabrica*. A LAI continua necessária. Rota alternativa achada: **SIPEAGRO/MAPA**, onde operadores aeroagrícolas se registram |
| O MapBiomas separa banana/melão ou só classes genéricas? | ✅ **só genéricas.** Têm classe própria: soja (39), cana (20), café (46), citrus (47), dendê (35), algodão (62), arroz (40). **Banana cai em "Outras culturas perenes" (48)**; melão, em "Outras lavouras temporárias" (41) | **MapBiomas NÃO melhora a medida de dose** para este desenho. A flag do `CLAUDE.md` está resolvida no sentido pessimista — e isso *economiza* trabalho: o ingestor não vale a pena |
| O mapa cárstico do CPRM/SGB é público? | ✅ **sim, e há fonte melhor.** A **ANA** publica "Sistemas Aquíferos" com classificação **Cárstico** em shapefile aberto (`dadosabertos.ana.gov.br`), catalogado no SNIRH | Vem da **mesma fonte e formato** que as ottobacias que o canal-água já usaria. Um download, não dois |
| A **Base dos Dados** tem SINASC 2023–2024? | ⚠️ **pergunta superada em 2026-09-22 — a premissa era falsa.** Ela nasceu de "2013–2022 no FTP do DATASUS", e a série **consolidada** do FTP (`/dissemin/publicos/SINASC/1996_/Dados/DNRES`, irmã da `PRELIM`) tem **até 2024** para CE, RN, PI e PE. Conferido listando o diretório, não lendo página | **A janela pode fechar em 19/12/2024 pelo próprio DATASUS**, sem BigQuery e sem credencial. A Base dos Dados vira redundância, não rota. Ver `gates-resultados-dados-reais.md` §7-bis.4 |
| A PAM 2010–2014 é comparável? | ✅ **SIM**, conferido em 2026-09-21: mesmas tabelas (1612/1613), mesmos códigos, **184 municípios e 86 culturas em ambos os períodos**, nenhuma cultura entra ou sai, e a costura 2014→2015 é suave na banana | **A D4 é viável.** ⚠️ Mas não é grátis — ver §1-quater |

⚠️ **Duas ressalvas de proveniência, e elas são do mesmo tipo que a coluna
`confianca` do CSV de bans exige de qualquer varredura:**

1. ~~**"Declara 1979–2024" não é "tem as linhas".**~~ ✅ **Encerrada em
   2026-09-22, e a lição é outra:** a consulta ao BigQuery ficou desnecessária
   porque o **FTP já tem 2023 e 2024**. O que precisava de verificação não era
   a cobertura anunciada da Base dos Dados — era a **premissa** de que o FTP
   parava em 2022, que ninguém tinha listado. A regra de conferir executando em
   vez de ler continua; ela só apontava para o lado errado.
2. **Ausência de evidência sobre o melão no GAEZ não é evidência de ausência.**
   O portal não renderiza sem JS; a lista completa exige `/scrape` com browser,
   não `WebFetch`. Fica marcado como não conferido, não como "não tem".

### Classe E — ✅ **resolvida em 2026-08-25** (era bloqueio de proxy, não do projeto)

⚠️ **A classe E não era uma propriedade do projeto; era do proxy da sessão
remota.** Na máquina do pesquisador, `api.crossref.org` responde normalmente.

**Conferência feita:** 40 DOIs resolvidos, `paper/referencias.bib` gerado
**a partir da resposta do Crossref** (sem digitação, logo sem erro de
transcrição). Log completo, correções e lacunas: `docs/referencias-verificadas.md`.

| Item | Situação |
|---|---|
| Larsen et al. (2017), *Nature Communications* | ✅ conferido, e o achado (5–9%, só acima do p95) confere com o *abstract* |
| Reynier & Rubin (2025), *PNAS* | ✅ conferido. ⚠️ a magnitude "23–32 g" **não** consta do *abstract* — ver o log |
| Marx-Stoelting et al. (2025), *Science* | ⚠️ **continua não encontrada** no Crossref. Não entra no `.bib` nem é citada |

⚠️ **A distinção que o log estabelece:** DOI conferido autoriza a **citação**;
não autoriza a **afirmação sobre o achado**. A segunda exige *abstract* ou texto
integral, e duas atribuições da introdução foram corrigidas por isso.

---

## 2. A matriz de degradação — o que continua estimável sem cada fonte

É esta tabela que permite decidir o que perseguir com tempo limitado.

| Sem esta fonte | O que ainda sai | O que **não** sai |
|---|---|---|
| ~~**FAO-GAEZ**~~ ✅ **resolvido** | — | ~~o instrumento; 3 das 4 definições de zero~~. Restam impossíveis só as que dependem de ANAC/SEMACE (definição 3) |
| **SEMACE / ANAC** | tudo, com o estimando renomeado | definição 3 de `d = 0` (a única que mede **método**); a verificação de *enforcement* pelo registro |
| **Bans municipais < 2019** | tudo, aparentemente | ⚠️ a garantia de que 2015–2018 é pré-tratamento. **Falha silenciosa: o resultado sai e está errado.** Já não é risco hipotético — 1 dos 17 tratados da banana teve lei em 2009. ⚠️ **Revogada em maio de 2010** (Lei 1.511, de 26/05/2010; texto integral a conferir): em 2015–2018 não havia ban vigente. A lição fica: lei achada ≠ lei vigente |
| ~~ANA + SISAGUA~~ ⏸️ **SUSPENSO 2026-09-21** | Ensaio 1 inteiro | o canal-água. ⚠️ Não por indisponibilidade: o SISAGUA foi ADQUIRIDO e tem 58.061 medições em 184 municípios. Suspenso porque a variável de detecção tem quebra de registro no CE a partir de 2020 que produziria efeito espúrio. Ver §1-ter |
| MapBiomas | tudo | melhoria da medida de dose; a deriva fica sem polígono |
| ~~INMET / FUNCEME~~ ⏸️ **SUSPENSO 2026-09-21** | tudo | ⚠️ Não por indisponibilidade: o dado é aberto, horário e 100% preenchido. O teste transversal **não funciona** porque os alísios dão coerência 0,96 entre estações — 'a favor do vento' vira 'a oeste', que é geografia. O teste temporal exigiria data de pulverização, que não existe no pré-ban. Ver §1-quinquies |
| População municipal | contagens do canal de intoxicação | taxas; a comparação entre municípios de porte diferente |

**Leitura da matriz.** Duas linhas têm consequência qualitativamente diferente
das outras: **GAEZ**, porque tira a banda do resultado principal, e **bans
municipais**, porque a falha é **silenciosa** — o pipeline roda, o número sai, e
está errado sem nada acusar. As demais degradam o escopo, não a validade.

---

## 3. A ordem recomendada

1. **Levantar os bans municipais < 2019.** Não custa download nenhum, é a única
   lacuna cuja ausência produz resultado **errado em silêncio**, e é anterior ao
   Gate 1.
2. **Protocolar a LAI.** Único com relógio externo; a resposta demora, o resto
   não. Mata dois coelhos (D6 + definição 3 de `d = 0`).
3. **Verificar o catálogo GAEZ** (banana e melão?) — uma consulta, e ela decide
   se o item 4 é viável.
4. **Baixar o GAEZ** e rodar `06_build_gaez.py`. É o que devolve a banda ao nível
   da curva.
5. **PAM + SINASC** pelo caminho manual → Gate 1 e E1.5, os dois números que
   decidem se o ensaio tem chance.
6. ⏸️ Canais — reordenados em 2026-09-21, porque três dos quatro já foram
   investigados e dois estão FECHADOS, não pendentes:
   - **MapBiomas**: ✅ conferido — só classes genéricas, banana cai em "Outras
     culturas perenes". **Não melhora a dose.** Não escrever ingestor.
   - **SISAGUA**: ✅ adquirido, ⏸️ **suspenso** — ver §1-ter. A decisão pendente
     não é de aquisição, é de escopo.
   - **ANA**: ⏸️ **bloqueado pelo SISAGUA**, não por disponibilidade. As
     ottobacias servem ao desenho montante/jusante, que precisa de coordenada
     do ponto de coleta — o SISAGUA tem 0,4%. Baixar agora seria construir
     infraestrutura para um desenho sem insumo.
   - **INMET / FUNCEME**: ⬜ ainda aberto. É o teste de direção do vento, que
     separa deriva de confundidor — e não depende do SISAGUA.

⚠️ Os itens 1 a 3 **não dependem da rede**. Podem ser feitos hoje.

---

## 4. O acoplamento com a pré-especificação (D7)

`docs/pre-especificacao.md` §4 pergunta qual construção de `d = 0` é primária.
**As definições 3 e 4 dependem de fontes não adquiridas.**

Então a D7 não pode ser preenchida com honestidade sem saber o que vai existir. E
a saída correta não é adiar: é **declarar**.

> "Primária = definição 2, porque 3 e 4 não estarão disponíveis até a
> qualificação" é honesto e defensável.
>
> Escolher a 4, não conseguir o GAEZ, e trocar em silêncio — não é.

Isso entra na tabela de desvios da §8 da pré-especificação se a situação mudar.

---

## 5. O que este repositório **não** vai fazer sozinho

- **Escrever ingestores para ANA, SISAGUA, MapBiomas e INMET antes de haver
  arquivo.** Seriam quatro superfícies escritas contra formato **suposto** — e
  esta sessão já achou bugs em três lugares exatamente assim (aliases do
  datazoom, parser do SIDRA, API do pysus). O ingestor se escreve quando houver
  o arquivo na mão.
- **Afirmar que uma fonte é pública sem ter conferido.** Classe D é "a
  verificar", não "disponível".
- **Decidir qual lacuna vale a pena aceitar.** A matriz da §2 dá o custo de cada
  uma; o corte de escopo é decisão do pesquisador com o orientador.
