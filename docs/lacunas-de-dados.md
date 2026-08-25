# Lacunas de dados — por prioridade, não por lista

*2026-08-25. O pipeline está completo (92 testes, E5–E7 instrumentados) e
**nenhuma fonte real foi tocada**. Este documento diz o que falta, quanto custa
cada falta, e o que continua estimável sem ela.*

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

### Classe A — já contornada ✅

| Fonte | Como |
|---|---|
| PAM/SIDRA | `01_check_dose_variation.py --fonte arquivo --caminho tab1612.csv` |
| SINASC, SIM, SIH | `00_export_datazoom.R` (na sua máquina) → `--caminho` nos scripts 02/03/04 |

O bloqueio de rede virou **inconveniência**, não impedimento. Os dois caminhos
estão testados, inclusive contra o preâmbulo do portal do SIDRA e o DOFET sem
`TIPOBITO`.

### Classe B — falta baixar **e** falta o ingestor

| Fonte | Serve a | Ingestor existe? |
|---|---|---|
| **FAO-GAEZ** ⚠️ | instrumento + zero 4 + teste de contaminação | ✅ `06_build_gaez.py` |
| ANA (ottobacias) | canal-água (montante/jusante) | ❌ |
| SISAGUA | canal-água (qualidade) | ❌ |
| MapBiomas | canal-ar (deriva); melhora a medida de dose | ❌ |
| INMET / FUNCEME | canal-ar (vento a favor/contra) | ❌ |
| População municipal (IBGE) | denominador do canal de intoxicação | ❌ |

⚠️ **E há um bloqueio que ninguém tinha notado: nenhuma biblioteca geo está
instalada.** `geopandas`, `rasterio`, `shapely`, `pyproj`, `fiona`,
`rasterstats`, `xarray` — todas ausentes, e `data/geo/` vazio. Mesmo com o raster
do GAEZ baixado, **nada no repositório conseguiria lê-lo**.

✅ Resolvido: `requirements-geo.txt`. Separado do `requirements.txt` porque
GDAL/PROJ/GEOS são pesados e brigam, e o pipeline 01–05 não precisa deles.
`pypi.org` está liberado no proxy, então é instalável.

### Classe C — administrativamente travada

| Fonte | Ação | Prazo |
|---|---|---|
| **SEMACE / ANAC / MAPA / SINDAG** | protocolar a LAI (minuta em `07-layer4-*.md`) | 20 dias + 10. **Único com relógio externo** |
| **Bans municipais < 2019** | levantamento legislativo, município a município | nenhum, mas é anterior ao Gate 1 em importância |

Nenhum script resolve estas. Precisam de uma pessoa.

⚠️ O segundo é mais grave do que a posição na lista sugere: se Limoeiro do Norte
proibiu em **2009**, há unidades **já tratadas** dentro do grupo de dose alta, e
2015–2018 deixa de ser pré-tratamento para todos. **Contamina a própria medida de
dose**, não só o desfecho.

### Classe D — a verificar **antes** de planejar em cima

| Pergunta | Por que importa |
|---|---|
| O catálogo do GAEZ cobre **banana e melão**? | "prioridade zero" da Layer 3. Se não cobrir, o instrumento precisa de outra construção |
| O cadastro da SEMACE é público e tem série com município? | é a definição 3 de `d = 0` |
| O MapBiomas separa banana/melão ou só classes genéricas? | se genérico, não melhora a dose |
| O mapa cárstico do CPRM/SGB é público? | heterogeneidade do canal-água |
| A PAM 2010–2014 é comparável? | insumo da **D4** (recuar a janela) |

Cada uma é **uma consulta**. Nenhuma foi feita. Planejar em cima delas sem
verificar é como o projeto já se queimou três vezes nesta sessão (aliases
datazoom, parser SIDRA, API pysus).

### Classe E — fora de alcance daqui

| Item | Por quê |
|---|---|
| Marx-Stoelting et al. (2025), *Science* | Scholar Gateway é corpus **Wiley**; AAAS não está |
| Larsen et al. (2017), *Nature Communications* | idem (Springer Nature) |
| Reynier & Rubin (2025), *PNAS* | idem |

`api.crossref.org`, `doi.org`, `api.semanticscholar.org` e `pubmed` estão todos
em **000**. As citações continuam **não verificadas**, e agora se sabe por quê.

---

## 2. A matriz de degradação — o que continua estimável sem cada fonte

É esta tabela que permite decidir o que perseguir com tempo limitado.

| Sem esta fonte | O que ainda sai | O que **não** sai |
|---|---|---|
| **FAO-GAEZ** | a curva, com um nível **sem banda** | ⚠️ o instrumento; 3 das 4 definições de zero; o teste de contaminação. **O nível da curva vira indefensável** |
| **SEMACE / ANAC** | tudo, com o estimando renomeado | definição 3 de `d = 0` (a única que mede **método**); a verificação de *enforcement* pelo registro |
| **Bans municipais < 2019** | tudo, aparentemente | ⚠️ a garantia de que 2015–2018 é pré-tratamento. **Falha silenciosa: o resultado sai e está errado** |
| ANA + SISAGUA | Ensaio 1 inteiro | o canal-água; o mecanismo fica postulado, não medido |
| MapBiomas | tudo | melhoria da medida de dose; a deriva fica sem polígono |
| INMET / FUNCEME | tudo | vento a favor/contra — o teste de direção que separa deriva de confundidor |
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
6. Canais (ANA, SISAGUA, MapBiomas, INMET) — depois de existir um número.

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
