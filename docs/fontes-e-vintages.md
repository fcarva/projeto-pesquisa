# Fontes e vintages

Registro de qual extração de cada base foi usada. Sem isso, um resultado não é
reproduzível — a mesma consulta ao SIDRA ou ao DATASUS devolve números
diferentes conforme a revisão. Preencher ao baixar, não depois.

| Base | Recorte | Data da extração | Como foi obtida | Arquivo em `data/raw/` |
|---|---|---|---|---|
| PAM/IBGE (tab. 1612, 1613) | CE, municípios, 2015–2018 | *(preencher)* | `scripts/data_prep/01_check_dose_variation.py --fonte sidra` | *(preencher)* |
| SINASC | CE, 2015–2022 | *(preencher)* | pysus / Base dos Dados | *(preencher)* |
| SIM | CE, 2015–2022 | *(preencher)* | pysus / Base dos Dados | *(preencher)* |
| SISAGUA | CE | *(preencher)* | Base dos Dados / MS | *(preencher)* |
| FAO-GAEZ | CE | *(preencher)* | raster → `data/geo/` | *(preencher)* |
| ANA (bacias) | CE | *(preencher)* | shapefile → `data/geo/` | *(preencher)* |
| IBAMA (vendas) | CE | *(preencher)* | portal IBAMA | *(preencher)* |

## Documentos legais para `docs/`

- Lei Estadual 16.820/2019 (CE) — "Lei Zé Maria do Tomé"
- ADI 6137/STF
- Lei 19.135/2024 (CE) — exceção para drones
- ADI 7794

## Nota sobre a checagem de dose

O script `01_check_dose_variation.py` monta a consulta ao SIDRA como
`t/{1612,1613}/n6/in n3 23/v/{109,2313}/c{81,82}/all/p/2015-2018`. Os códigos de
variável e classificação vieram da documentação das tabelas, mas **não foram
verificados contra a API** (o ambiente onde o script foi escrito não tinha
saída para `apisidra.ibge.gov.br`). Na primeira rodada com `--fonte sidra`,
conferir os rótulos impressos contra <https://sidra.ibge.gov.br/tabela/1612> e
`/1613` antes de confiar na tabela.
