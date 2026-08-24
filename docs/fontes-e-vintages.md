# Fontes e vintages

Registro de qual extração de cada base foi usada. Sem isso, um resultado não é
reproduzível — a mesma consulta ao SIDRA ou ao DATASUS devolve números
diferentes conforme a revisão. Preencher ao baixar, não depois.

| Base | Recorte | Data da extração | Como foi obtida | Arquivo em `data/raw/` |
|---|---|---|---|---|
| PAM/IBGE (tab. 1612, 1613) | CE, municípios, 2015–2018 | *(preencher)* | `scripts/data_prep/01_check_dose_variation.py --fonte sidra` | *(preencher)* |
| SINASC | CE, 2015–2022 | *(preencher)* | `scripts/data_prep/02_clean_births.py` (pysus / Base dos Dados) | *(preencher)* |
| SIM — DO (óbito fetal) | CE, 2015–2022 | *(preencher)* | `scripts/data_prep/03_clean_fetal_deaths.py` (pysus, grupo CID10) | *(preencher)* |
| SISAGUA | CE | *(preencher)* | Base dos Dados / MS | *(preencher)* |
| FAO-GAEZ | CE | *(preencher)* | raster → `data/geo/` | *(preencher)* |
| ANA (bacias) | CE | *(preencher)* | shapefile → `data/geo/` | *(preencher)* |
| IBAMA (vendas) | CE | *(preencher)* | portal IBAMA | *(preencher)* |

## Documentos legais para `docs/`

Cronologia estabelecida, transcrição dos dispositivos e status de download em
**`docs/legislacao/README.md`**. Resumo do que está pendente:

- Lei Estadual 16.820/2019 (CE) — "Lei Zé Maria do Tomé" — ✅ obtida (AL-CE, 2026-08-23)
- Lei Estadual 12.228/1993 (CE) — norma-mãe, **consolidada** com o art. 28-B nas duas redações — ✅ obtida
- ADI 6137/STF (acórdão) — ❌ não baixado
- Lei 19.135/2024 (CE) — exceção para drones — ✅ texto integral transcrito na ADI 7794
- ADI 7794 (petição inicial, PSOL) — ✅ na pasta do Drive

## Data do tratamento — proveniência

**Sanção 08/01/2019; publicação e vigência 09/01/2019.** O texto oficial diz "LEI N.º 16.820, DE 08.01.19 (D.O. 09.01.19)" e o art. 2º manda entrar em vigor na data da publicação. Num painel mensal a distinção não muda nada; no texto da dissertação, muda. A petição inicial da ADI 7794 cita o texto da lei: "Em 08 de
janeiro de 2019, foi acrescentado à referida norma o artigo 28-B, pela Lei nº
16.820/2019 do Estado do Ceará", com nota de rodapé apontando para o repositório
oficial da ADAGRI-CE. O `CLAUDE.md` dizia "jun/2019" até 2026-08-23; corrigido.

**18/12/2018 — antecipação.** A mesma petição registra que o PL 18/2015 foi
aprovado por unanimidade na ALECE em 18/12/2018, após quatro anos de tramitação.
A janela de antecipação começa aí, no mínimo — e possivelmente antes, já que
quatro anos de tramitação com debate público são quatro anos de sinal.
Consequência para o desenho: 2019 é ano de transição, e os *leads* do event study
têm que alcançar 2018.

✅ **Conferido contra o texto oficial** (AL-CE) em 2026-08-23. Ressalva que a
própria fonte traz: "O texto desta Lei não substitui o publicado no Diário
Oficial" — para citação final, conferir o DOE.

## Nota sobre o SIM — duas armadilhas de extração

**1. Óbito fetal não é arquivo separado.** No SIM moderno ele vem dentro do DO
(`DO<UF><ano>`, grupo `CID10` no pysus), identificado por **TIPOBITO: 1 = fetal,
2 = não fetal**. Baixar o DO e esquecer o filtro mistura óbito infantil com óbito
fetal — populações e desfechos diferentes. O script 03 filtra por TIPOBITO antes
de qualquer outra coisa, e o teste `test_tipobito_nao_fetal_e_descartado` existe
para isso não regredir em silêncio.

**2. ⚠️ Subnotificação é heterogênea entre municípios — e isso é confundidor,
não ruído.** A notificação compulsória alcança perdas de **≥ 22 semanas OU
≥ 500 g** (é "ou", não "e"); abaixo desse limiar o registro é irregular e varia
por município e por ano. Como a variação entre municípios é justamente o que o
desenho usa para identificar, um padrão espúrio de registro entra direto no
estimador. Daí o script emitir a série restrita (`n_obito_fetal_22sem`) ao lado
do total: **rodar o teste de seleção nas duas.** Se divergirem, a divergência é o
achado — subnotificação diferencial —, não um detalhe a escolher entre.

Vale registrar o que a rodada simulada já mostrou sobre o desfecho, e que vale
para o dado real: **no nível município×mês, óbito fetal é raro a ponto de a taxa
quase não existir** (≈ 1% das gestações registradas; a esmagadora maioria das
células fica abaixo de 5 óbitos). O teste vai precisar de agregação mais grossa —
município×ano, ou faixas de dose empilhadas. É propriedade do desfecho, não
defeito de limpeza.

## Nota sobre a checagem de dose

O script `01_check_dose_variation.py` monta a consulta ao SIDRA como
`t/{1612,1613}/n6/in n3 23/v/{109,2313}/c{81,82}/all/p/2015-2018`. Os códigos de
variável e classificação vieram da documentação das tabelas, mas **não foram
verificados contra a API** (o ambiente onde o script foi escrito não tinha
saída para `apisidra.ibge.gov.br`). Na primeira rodada com `--fonte sidra`,
conferir os rótulos impressos contra <https://sidra.ibge.gov.br/tabela/1612> e
`/1613` antes de confiar na tabela.
