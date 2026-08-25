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

## Nota sobre o datazoom.saude — é pacote R, e a língua é armadilha

`datazoompuc/datazoom.saude` (v0.1.1, MIT, PUC-Rio) baixa e padroniza SINASC,
SIM, SIH, SIASUS e CNES. É rota alternativa ao `pysus` para o DATASUS.

⚠️ **É um pacote R.** A fronteira com o Python é **arquivo**, como já vale para o
`contdid` (ver `CLAUDE.md`): exporte de lá, leia com `--fonte arquivos` aqui.

⚠️ **O pacote renomeia as colunas do DATASUS, e em duas convenções.** O parâmetro
`language` aceita `"pt"` e `"eng"`, e **o padrão é `"eng"`**. Os scripts 02 e 03
cobrem as duas em `ALIASES_DATAZOOM`, conferido contra `R/dictionary.R` do
repositório. As traduções que mais importam, porque não são óbvias:

| DATASUS | datazoom `pt` | datazoom `eng` (padrão) |
|---|---|---|
| `DTNASC` (SINASC) | `data_nascimento_recemnascido` | `newborn_birth_date` |
| `GESTACAO` (SINASC) | `semanas_gestacao_agrupado` | `grouped_gestational_weeks` |
| `SEMAGESTAC` (SINASC) | `semanas_gestacao` | `gestational_weeks` |
| `PESO` (SIM) | `peso_nascimento` | `birth_weight` |
| `GESTACAO` (SIM) | `duracao_gestacao` | `gestational_duration` |

Duas ciladas dentro dessa tabela:

- `semanas_gestacao` e `semanas_gestacao_agrupado` são **campos diferentes** —
  contagem contra faixa categórica. Trocá-los inverte desfecho e fallback.
- **O dicionário do SIM não tem `semagestac`**: a duração gestacional só vem
  agrupada. Com fonte datazoom, o fallback categórico vira o único caminho e
  `share_gest_por_faixa` sai 100%. Não é defeito; é o que a fonte oferece, e a
  coluna existe para deixar isso visível.

E `idade` (idade do falecido, código composto) **não** é `idademae`. São campos
separados no dicionário; confundi-los põe `401` dentro de `idade_mae_media`.

## Acesso à rede na sessão remota — o que precisa ser liberado

**O bloqueio é política de rede do ambiente, não instabilidade das fontes.** O
proxy da sessão responde **403 ao CONNECT** para os domínios não liberados. A
evidência é direta:

```
$ curl -sS "$HTTPS_PROXY/__agentproxy/status"
"recentRelayFailures": [
  {"kind": "connect_rejected",
   "detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
   "host": "apisidra.ibge.gov.br:443"}, ...
]
```

Domínios a liberar, por etapa do roteiro:

| Domínio | Serve a | Etapa |
|---|---|---|
| `apisidra.ibge.gov.br` | valores do SIDRA (PAM) | **E2 — Gate 1** |
| `servicodados.ibge.gov.br` | metadados do SIDRA (o preflight) | **E2 — Gate 1** |
| `ftp.datasus.gov.br` | SINASC e SIM via pysus | E1.5, A1 |
| `basedosdados.org` | rota alternativa para SINASC/SIM/SISAGUA | A1, A3 |
| `gaez.fao.org` | raster de aptidão agroclimática | A2 |

A política é escolhida na criação do ambiente, nas configurações em
claude.ai/code — ver <https://code.claude.com/docs/en/claude-code-on-the-web>.
**Enquanto não estiver liberada**, os três scripts aceitam arquivo baixado à mão
(`--fonte arquivo --caminho …` no 01; `--caminho …` no 02 e no 03), e o script 01
distingue na mensagem de erro bloqueio-de-rede de erro-do-IBGE — as duas causas
pedem ações diferentes.

## Nota sobre a checagem de dose

O script `01_check_dose_variation.py` monta a consulta ao SIDRA como
`t/{1612,1613}/n6/in n3 23/v/{109,2313}/c{81,82}/all/p/2015-2018`.

⚠️ **Os códigos de variável e classificação vieram da documentação das tabelas e
continuam não verificados contra a API** — o ambiente onde o script foi escrito
não tem saída para `servicodados.ibge.gov.br`. Isso importa mais do que parece:
um código errado faz o SIDRA devolver **vazio, não erro**, e vazio caía
silenciosamente para o simulado.

**O preflight resolve isso, e é a primeira coisa a rodar quando a rede abrir:**

```bash
python scripts/data_prep/01_check_dose_variation.py --verificar-codigos
```

Ele bate cada código contra `servicodados.ibge.gov.br/api/v3/agregados/{t}/metadados`
e, se algum não existir, **lista os que existem** — a correção não vira
adivinhação. `--fonte sidra` roda o preflight antes de baixar e aborta se ele
reprovar. **Registrar aqui a data em que o preflight passar** é o que fecha esta
pendência.
