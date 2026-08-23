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

Cronologia estabelecida, transcrição dos dispositivos e status de download em
**`docs/legislacao/README.md`**. Resumo do que está pendente:

- Lei Estadual 16.820/2019 (CE) — "Lei Zé Maria do Tomé" — ❌ download bloqueado pelo proxy
- Lei Estadual 12.228/1993 (CE) — norma-mãe — ❌ idem
- ADI 6137/STF (acórdão) — ❌ não baixado
- Lei 19.135/2024 (CE) — exceção para drones — ✅ texto integral transcrito na ADI 7794
- ADI 7794 (petição inicial, PSOL) — ✅ na pasta do Drive

## Data do tratamento — proveniência

**08/01/2019.** A petição inicial da ADI 7794 cita o texto da lei: "Em 08 de
janeiro de 2019, foi acrescentado à referida norma o artigo 28-B, pela Lei nº
16.820/2019 do Estado do Ceará", com nota de rodapé apontando para o repositório
oficial da ADAGRI-CE. O `CLAUDE.md` dizia "jun/2019" até 2026-08-23; corrigido.

**18/12/2018 — antecipação.** A mesma petição registra que o PL 18/2015 foi
aprovado por unanimidade na ALECE em 18/12/2018, após quatro anos de tramitação.
A janela de antecipação começa aí, no mínimo — e possivelmente antes, já que
quatro anos de tramitação com debate público são quatro anos de sinal.
Consequência para o desenho: 2019 é ano de transição, e os *leads* do event study
têm que alcançar 2018.

⚠️ **Conferir ao baixar.** A data acima vem da citação da ADI, não do texto
oficial. Se o DOE divergir, o oficial manda e o `CLAUDE.md` volta a mudar.

## Nota sobre a checagem de dose

O script `01_check_dose_variation.py` monta a consulta ao SIDRA como
`t/{1612,1613}/n6/in n3 23/v/{109,2313}/c{81,82}/all/p/2015-2018`. Os códigos de
variável e classificação vieram da documentação das tabelas, mas **não foram
verificados contra a API** (o ambiente onde o script foi escrito não tinha
saída para `apisidra.ibge.gov.br`). Na primeira rodada com `--fonte sidra`,
conferir os rótulos impressos contra <https://sidra.ibge.gov.br/tabela/1612> e
`/1613` antes de confiar na tabela.
