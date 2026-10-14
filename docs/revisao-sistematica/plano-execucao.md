# Plano de execução: fontes brasileiras, APIs e PRISMA completo

*Montado em 2026-10-13, na sessão do Claude Code
[`session_015S6CpC5WjjrbE2G1Scz7wd`](https://claude.ai/code/session_015S6CpC5WjjrbE2G1Scz7wd).
Branch: `claude/admiring-carson-3l2d8h`. Último commit antes deste plano: `376a927`.*

Este arquivo é o roteiro. Cada **etapa** abaixo traz o prompt para colar numa sessão do
Claude Code, a especificação técnica que a sessão segue e o critério de "pronto". As
etapas rodam em sessões separadas, cada uma pequena o bastante para não estourar o
limite de gasto. Marque o `⬜` → `✅` aqui mesmo, com o commit, ao terminar cada uma.

---

## Onde estamos

| item | estado | onde |
|---|---|---|
| Protocolo v1.0 | ✅ confirmado (carimbo `1d12f10`) | `protocolo.md` |
| PubMed (SQ1 #5 = 2.054; SQ3 P1 = 578) | ✅ coletado; as contagens batem com as congeladas | `registros/pubmed-*.csv`, commit `817f7d6` |
| OpenAlex (28 linhas, 4 blocos) | ✅ coletado (Etapa 2, `f92e7ae`) | `registros/openalex-*.csv` |
| Scopus API (SQ1) | ✅ 4.945, visão reduzida (`83500d6`) | `registros/scopus-api-sq1.csv` |
| Fontes brasileiras | ✅ LA Referencia (544, `6e0a5ea`); OASISBR (878, emenda v1.2) | `registros/vufind-*.csv` |
| Deduplicação, PRISMA, triagem | ⬜ | — |

**Teste de acesso (2026-10-13, a partir da nuvem):**

| fonte | resultado | rota |
|---|---|---|
| LA Referencia (API VuFind, `buscador.lareferencia.info/api/v1/search`) | ✅ string SQ1-AL #1 AND #2 inteira: **544** (251 artigos, 292 teses/dissertações), com resumo | script |
| OASISBR/IBICT (API VuFind, `oasisbr.ibict.br/vufind/api/v1/search`) | ✅ booleano e facetas; **403 a consulta com ~10 termos ou mais** (regra de firewall, não tamanho de URL) | script, em fatias de ≤ 5 + 5 termos (emenda v1.2) |
| Crossref | ✅ (só relevância) | script, para hidratar DOI/resumo |
| Portal de Periódicos CAPES | ✘ não tem API: é porta via CAFe para bases pagas | — |
| Scopus (Elsevier API) | ✘ "Invalid API Key": a injeção do proxy não chega ao `X-ELS-APIKey`. Fora da rede da UFES, só a visão reduzida, sem resumo | script com variável de ambiente + **exportação pela CAPES** |
| SciELO (busca), BVS/LILACS | ✘ 403, bloqueio de IP de datacenter | **exportação do pesquisador** |

**Decisões do pesquisador (2026-10-13):**
1. Teses e dissertações com dado original **entram na SQ1**, como literatura cinzenta. Se a tese virou artigo, vale o artigo (emenda v1.1).
2. Scopus **por API (visão reduzida, para identificação) + exportação completa pela CAPES** (emenda v1.1).
3. **TCCs de graduação com dado original** também entram na SQ1, e o OASISBR é coletado em fatias de ≤ 5 + 5 termos (emenda v1.2, `0be66d3`). Motivo: num teste com duas consultas curtas e idênticas, a LA Referencia saiu **subconjunto** do OASISBR, e o OASISBR trouxe 30 de 45 e 23 de 47 registros a mais, entre eles dissertações centrais e TCCs.

---

## Parte A: o que você faz (fora do Claude Code)

- [ ] **A1. Chaves como variáveis de ambiente.** No menu do ambiente (barra de título da sessão → *Edit*), em **variáveis de ambiente**, e não em *Network secrets* (a injeção falhou para as duas). Nunca cole uma chave no chat.
  - `OPENALEX_API_KEY` = chave do OpenAlex (gratuita, em openalex.org);
  - `ELSEVIER_API_KEY` = chave do dev.elsevier.com;
  - opcional, depois: `ELSEVIER_INSTTOKEN`, se a biblioteca da UFES conseguir um *insttoken* com a Elsevier. Ele libera o Scopus completo pela API, de qualquer rede.

  Se quiser manter o OpenAlex em *Network secrets*, corrija o host para `api.openalex.org`, sem restrição de caminho. Hoje está cadastrado como `*.example.com`. **A variável só entra numa sessão nova.**
- [ ] **A2. Exportação do Scopus pela CAPES.** Portal de Periódicos → login CAFe (UFES) → Scopus → busca avançada com a string de `ferramentas/scopus_wos.md`. Antes, teste as sementes (`AND DOI(10.1086/725349)` etc., como diz o arquivo). Exporte **todos** os registros em RIS ou CSV **com resumo**, com o nome `scopus-sq1-AAAA-MM-DD.ris`. Anote a **contagem** e a **data**.
- [ ] **A3. Exportação de SciELO e LILACS** (opcional, mas recomendada para a literatura brasileira de saúde). Use as strings S1'/S2'/S2b/S3 e L1'/L2''/L2b do Apêndice A (seção SQ1-AL), em RIS, com nome `scielo-sq1-AAAA-MM-DD.ris` e `lilacs-sq1-AAAA-MM-DD.ris`. Anote contagem e data.
- [ ] **A4.** Coloque os arquivos de A2/A3 em `docs/revisao-sistematica/registros/importados/`, faça o commit pelo GitHub (upload) ou peça ao Claude Code para fazê-lo, e crie `registros/importados/LEIAME.md` com contagem e data de cada exportação.

---

## Parte B: sessões no Claude Code

Em todas as sessões: abra uma sessão nova **sobre a branch `claude/admiring-carson-3l2d8h`**
e cole o prompt. A sessão lê este arquivo, executa a etapa, faz o commit e o push.

### Etapa 1: emendas v1.1/v1.2 + coleta OASISBR/LA Referencia ✅
*2026-10-13, sessão local: emenda v1.1 (`628bf12`); **LA Referencia ✅** (544 = chamada única,
`6e0a5ea`). 2026-10-13, sessão na nuvem: emenda v1.2 (`0be66d3`: TCCs; OASISBR em fatias de
≤ 5 + 5 termos); **OASISBR ✅: 878 registros** em 192 fatias (317 dissertações, 254 artigos,
153 teses, 71 TCCs, 52 sem formato; 838 com resumo, 78 com DOI), `registros/vufind-oasisbr-sq1.csv`.
Conferência do método: as mesmas 192 fatias rodadas na LA Referencia dão 544, igual à chamada
única. A cobertura dos BR_ da LA Referencia na união do OASISBR é 289/337: dos 48 faltantes, 40
estão indexados no OASISBR com o mesmo título e resumo, mas o motor dele não os casa com a
string. Eles entram no conjunto da SQ1 pela LA Referencia, e boa parte é ruído (*Spodoptera*,
Bt). Detalhes em `ferramentas/vufind.md`.*
*Não depende de chave: pode rodar já.*

**Prompt:**
> Leia `docs/revisao-sistematica/plano-execucao.md` e execute a **Etapa 1** sobre a branch `claude/admiring-carson-3l2d8h`. Commit da emenda isolado, antes de qualquer coleta nova. No fim, atualize o ⬜ da etapa neste arquivo e faça o push.

**Especificação:**
1. **Emenda v1.1** em `protocolo.md`, num commit isolado (é o carimbo da emenda):
   - tabela *Emendas* + *Histórico de versões*: v1.1, 2026-10-13, motivo "lacuna de literatura brasileira", com as duas decisões acima;
   - *Status* (SQ1): teses e dissertações com dado original passam a elegíveis; a regra "vale o publicado" vale também para tese → artigo; a linha "teses e dissertações, por viabilidade" sai das exclusões;
   - *Fontes de informação*: OASISBR, LA Referencia, Scopus API (visão reduzida, só identificação; resumo hidratado por DOI via OpenAlex/Crossref);
   - *USO DE IA*, item M2: acrescentar as fontes;
   - registrar a emenda em `docs/ars/20-revisao-literatura-pesquisa.md` (§9).
2. **`ferramentas/coleta_vufind.py`** (OASISBR + LA Referencia, SQ1):
   - consulta = blocos congelados **SQ1-AL #1 (exposição) AND #2 (desfecho)**, lidos por `blocos_al()` + `carrega()`, **importados** de `ferramentas/coleta_openalex.py`, nunca redigitados. Sem o #3 (geografia), porque a fonte já é brasileira/latino-americana; registrar isso na emenda;
   - **fatiamento** contra o 403 do OASISBR: dividir os termos de #1 (e, se preciso, de #2) em fatias com URL < ~1.800 caracteres. `(E1 OR E2) AND O = (E1 AND O) ∪ (E2 AND O)`; unir por `id`. O `--plano` confere, sem rede, que a união dos termos das fatias é exatamente o bloco;
   - API: `lookfor=<consulta>&type=AllFields&limit=100&page=N`, campos `field[]=id,title,formats,languages,publicationDates,summary,primaryAuthors,urls`. DOI extraído das URLs (`doi.org/…`) quando houver. Pausa entre chamadas; falha → tenta de novo, nunca silencia;
   - **verificação obrigatória**: na LA Referencia, a união deduplicada das fatias tem de dar a contagem da chamada única (544 em 2026-10-13, ou a de hoje). Se não der, parar e registrar;
   - saída no padrão de `coleta_pubmed.py` (reusar o esquema, `sha()` e `loga()`): `registros/vufind-{oasisbr,lareferencia}-sq1.csv` (metadados + `formato` + SHA-256 do resumo), resumo em `data/raw/revisao-sistematica/`, uma linha por fatia em `registros/coletas.jsonl`;
   - **recall**: conferir os itens conhecidos brasileiros da calibração SQ1-AL (`calibracao/sq1-america-latina*.json`) por título, e registrar as linhas novas e as contagens como **linhas congeladas no Apêndice A** (PRISMA-S).
3. Rodar a coleta nas duas fontes, fazer o commit e o push.

**Pronto quando:** emenda commitada antes da coleta; dois CSV em `registros/`; LA Referencia com união = chamada única; Apêndice A com as linhas novas.

### Etapa 2: OpenAlex + Scopus API ✅
*2026-10-13, sessão local. **OpenAlex ✅**: 28 linhas (26 de conjunto, 1 de marca, 1 de conferência),
cada uma com os distintos = contagem de hoje; contagens de hoje aceitas pelo pesquisador apesar da
SQ2 #11 a −6,9% (27 × 29). O cursor do OpenAlex repete e pula obras entre passadas: o coletor une
passadas por ID e refaz a ordem pelo `relevance_score` (SQ2 #5 precisou de 2). **Scopus API ✅**: 4.945 registros (visão STANDARD, sem resumo; 4.276 com DOI;
as 3 sementes de `scopus_wos.md` recuperadas), em `registros/scopus-api-sq1.csv`. Sem assinatura, o
`cursor` é recusado: paginação por `start` (teto de 5.000) com ordem `-coverDate`, porque a ordem padrão
repete registros entre páginas.*
*Depende de A1 (chaves) e de uma sessão nova aberta depois delas.*

**Prompt:**
> Leia `docs/revisao-sistematica/plano-execucao.md` e execute a **Etapa 2** sobre a branch `claude/admiring-carson-3l2d8h`. Primeiro confirme que `OPENALEX_API_KEY` e `ELSEVIER_API_KEY` existem no ambiente, sem imprimir o valor. Se faltar alguma, pare e me diga qual.

**Especificação:**
1. `python3 ferramentas/coleta_openalex.py --conferir`: contagem de hoje × congelada, linha a linha. Diferença > 5% numa linha → parar e reportar antes de coletar.
2. `python3 ferramentas/coleta_openalex.py`: coleta as 28 linhas. Se o `select` recusar `relevance_score`, o script segue sem ele e registra no log; nesse caso, avisar, porque a ordem por relevância importa para a regra de parada da SQ2/SQ3.
3. **`ferramentas/coleta_scopus.py`**: lê `ELSEVIER_API_KEY` (e `ELSEVIER_INSTTOKEN`, se houver) e envia `X-ELS-APIKey`/`X-ELS-Insttoken` ele mesmo. A string é a tradução Scopus de `ferramentas/scopus_wos.md`, sem redigitar: ler do arquivo. Scopus Search com `cursor=*`, guardando `eid`, DOI, título, periódico, ano e tipo. Registra no log se a visão foi reduzida ou completa. Com 401/403, para sem gravar e diz a causa provável (chave inválida × falta de assinatura).
4. Commit e push.

**Pronto quando:** `registros/openalex-*.csv` das 26 linhas de conjunto + 1 de marca; o log com as contagens; `registros/scopus-api-sq1.csv` ou o motivo registrado de não ter rodado.

### Etapa 3: importação + deduplicação ✅ (reabre quando chegarem as exportações)
*2026-10-13, sessão na nuvem (`5dce0f5` e seguintes). `importa_exportacoes.py` pronto, sem arquivos ainda;
`deduplica.py` + `teste_deduplica.py` (casos sintéticos, todos passam); `hidrata_resumos.py`.*

| | SQ1 | SQ2 | SQ3 |
|---|---:|---:|---:|
| bruto (soma das linhas) | 14.200 | 4.132 | 6.373 |
| únicos | 9.416 | 3.920 | 6.029 |
| excluídos por metadado | 693 período + 130 idioma | — | 7 paratext + 6 retratados |
| **a triar** | **8.593** | **3.920** | **6.016** |
| sem resumo, depois do Crossref | 2.568 (2.014 só no Scopus API) | 512 | 1.404 |

*SQ1 por camada: 3.694 / 4.265 / 634. Exclusivos por fonte (SQ1, a triar): OpenAlex 2.854, Scopus
API 2.561, OASISBR 542, PubMed 270, LA Referencia 158. 38 pares tese ↔ artigo para conferência
(`registros/pares-tese-artigo-sq1.csv`). Hidratação: 4.668 DOIs sem resumo; o Crossref trouxe 932;
o OpenAlex estava sem cota (sem chave nesta sessão). **Pendente:** (a) rodar `hidrata_resumos.py`
numa sessão com `OPENALEX_API_KEY`, que tenta o OpenAlex nos DOIs que ficaram sem resumo, e depois
`deduplica.py`; (b) quando as exportações de A2/A3 chegarem: `importa_exportacoes.py` →
`deduplica.py` → `hidrata_resumos.py` → `deduplica.py`.*

*Especificação original:*

**Prompt:**
> Leia `docs/revisao-sistematica/plano-execucao.md` e execute a **Etapa 3** sobre a branch `claude/admiring-carson-3l2d8h`.

**Especificação:**
1. **`ferramentas/importa_exportacoes.py`**: lê RIS e CSV do Scopus em `registros/importados/` e normaliza no esquema comum (fonte, linha, IDs, DOI, título, ano, periódico, idioma, tipo, SHA-256 do resumo). Contagem e data vêm do `LEIAME.md` de A4 e vão para o log.
2. **`ferramentas/deduplica.py`**:
   - *pools* por SQ: SQ1 (PubMed SQ1 + OpenAlex SQ1-intl e SQ1-AL + VuFind + importados), SQ2 e SQ3, com a pertença cruzada registrada (a SQ3 #7b e #9 também marcam SQ1);
   - chaves, nesta ordem: DOI normalizado (minúsculo, sem `https://doi.org/`) → PMID → ID OpenAlex / EID → título normalizado (minúsculo, sem acento nem pontuação) + ano. União por *union-find*;
   - **tese ↔ artigo**: pares com o mesmo sobrenome do primeiro autor, títulos parecidos e ano do artigo ≥ ano da tese ficam marcados para conferência, **sem fusão automática**;
   - exclusões automáticas por metadado, contadas à parte: SQ1 com ano < 1990 ou idioma fora de en/pt/es; SQ3 com *paratext* ou retratados;
   - camadas e ordem de triagem conforme as `screening_priority_rule` dos `calibracao/*-final.json` (SQ1: marca informativa; SQ2/SQ3: a ordem importa para a regra de parada);
   - resumo que faltar (Scopus API, importados) hidratado por DOI via OpenAlex e, na falta, Crossref;
   - **VuFind (LA Referencia, OASISBR):** quase sem DOI (89 de 544 na LA Referencia), então a chave efetiva é título normalizado + ano. As duas fontes trazem o mesmo registro com ids diferentes (a LA Referencia é subconjunto do OASISBR);
   - **TCC (`bachelorThesis`) não é excluído por formato** (emenda v1.2). O par "tese/dissertação/TCC ↔ artigo" fica marcado para conferência;
   - arquivo de marca da camada 1 da SQ1-intl: `registros/openalex-sq1-internacional-8-ids.csv`;
   - saída: `registros/deduplicado-sq{1,2,3}.csv` + `registros/contagens-prisma.json`.
3. Teste com casos sintéticos: o mesmo DOI com caixa diferente; PMID sem DOI; título com acento × sem acento; tese e artigo do mesmo autor. Commit e push.

**Pronto quando:** três CSV deduplicados; `contagens-prisma.json` com as identidades fechando (identificados − duplicatas − excluídos por automação = a triar).

### Etapa 4: PRISMA 2020 completo ✅ (identificação; triagem em diante, "pendente")
*2026-10-13, sessão na nuvem. `ferramentas/prisma.py` gera `paper/overleaf/prisma-sq{1,2,3}.tex`
(TikZ, classe standalone; compilação testada com Tectonic), `prisma-fluxo.md` e
`registros/prisma-fluxo.json`, e falha se uma identidade não fechar. As caixas de triagem em
diante saem como "pendente" até existir `registros/decisoes-<sq>.csv`, com as colunas `id_unico`,
`titulo_resumo`, `texto_obtido`, `texto_completo`, `motivo` e `estudo` (formato na docstring). A
Etapa 5 tem de gravar nesse formato. Checklists: `checklist-prisma2020.md` e `checklist-prisma-s.md`.*
**Prompt:**
> Leia `docs/revisao-sistematica/plano-execucao.md` e execute a **Etapa 4** sobre a branch `claude/admiring-carson-3l2d8h`.

**Especificação:**
1. **`ferramentas/prisma.py`**: lê `contagens-prisma.json` (e, depois, as decisões de triagem) e gera o **fluxograma PRISMA 2020**, com a coluna "bases e registros" e a coluna "outros métodos" (citações, sites de literatura cinzenta):
   - TikZ para o Overleaf em `paper/overleaf/prisma-sq1.tex`, e versões para SQ2/SQ3 se couber;
   - Markdown em `docs/revisao-sistematica/prisma-fluxo.md`;
   - caixas de triagem e elegibilidade com "pendente" enquanto não houver decisões;
   - o script **falha** se uma identidade não fechar.
2. **`checklist-prisma2020.md`** (27 itens) e **`checklist-prisma-s.md`** (16 itens de busca): cada item com onde está reportado (arquivo/seção) ou "pendente".
3. Commit e push.

**Pronto quando:** o fluxograma compila no Overleaf com os números da Etapa 3; os dois checklists estão preenchidos.

### Etapa 5: piloto + triagem 🟡 (piloto ✅; triagem completa aguarda aprovação)
*2026-10-14, sessão na nuvem.*
- **Prompt aprovado** (`prompts/04-triagem-titulo-resumo-sq1.md`); triadores **Sonnet**, adjudicador no modelo da sessão.
- **Piloto** (50 registros da SQ1, 30/15/5 por camada): κ de Cohen **0,91**, concordância de 49/50, citação literal em 99/100, mesmo motivo em 40/43 exclusões em comum. A única divergência foi adjudicada como exclusão. Resultado final: 6 incluídos e 44 excluídos (`registros/triagem/sq1-piloto-*`).
- **Consumo medido:** cerca de 132 mil tokens por chamada de triador com 50 registros, e 77 mil na chamada do adjudicador com 1 registro. Ou seja, uns 75 mil de sobrecarga fixa por chamada e uns 1,1 mil por registro.
- **Camada 1 (aprovada: lotes de 100, em grupos):** 26 lotes prontos (2.534 registros) e 1.130 pendentes do OpenAlex (`registros/triagem/sq1-camada1-pendentes.csv`). Os lotes 001–010 estão feitos (1.000 registros), com κ = 0,91, citação literal em 2.000/2.000, 248 inclusões de consenso e 35 divergências à espera da adjudicação. O κ por lote vai de 0,80 (lote 007) a 1,00 (lote 010). Em 2026-10-14, um grupo de 16 triadores esgotou o limite de uso do pesquisador. Desde então, os grupos são de 4 lotes (8 triadores).
- **Como retomar** (sessão nova, branch `claude/admiring-carson-3l2d8h`): ver quais lotes já têm `registros/triagem/sq1-camada1-lote-NNN-triador-{1,2}.json`; para cada lote que falta, lançar os dois triadores (Sonnet) com o texto de `prompts/04c-chamada-triador-arquivo.md`, trocando `<LOTE>` e `<SAIDA>`; depois rodar `python3 ferramentas/concordancia.py --sq sq1 --modo camada1`. No fim da camada, adjudicar as divergências com `prompts/05b` e o arquivo `data/raw/.../triagem/sq1-camada1-divergencias.json`. Os lotes ficam em `data/raw` (fora do git); se a sessão for nova, recriá-los com `python3 ferramentas/prepara_triagem.py --completo --sq sq1 --camada 1 --tamanho 100 --so-com-resumo`, que produz os mesmos lotes se os resumos locais forem os mesmos (conferir os SHA-256 no manifesto).
**Prompt:**
> Leia `docs/revisao-sistematica/plano-execucao.md` e execute a **Etapa 5** sobre a branch `claude/admiring-carson-3l2d8h`. Antes de rodar agentes, me mostre o prompt de triagem e o custo estimado.

**Especificação** (protocolo, "Seleção" e "Calibração humana"):
1. Prompt de triagem título/resumo **verbatim** em `prompts/03-triagem-titulo-resumo.md`: critérios da SQ1 (com a emenda v1.1), "na dúvida, inclui", saída JSON com decisão, motivo e citação literal.
2. **Piloto**: 50 registros da SQ1, sorteados com semente fixa e estratificados por camada; dois triadores de IA independentes → κ de Cohen. Mudança de redação dos critérios só **com a sua aprovação**, registrada como emenda.
3. Triagem da SQ1 dupla, com adjudicação; SQ2/SQ3 com triador único, regra de parada e auditoria (protocolo, "Escala da triagem").
4. **Amostra de referência** (50 = 25/25 pelo consenso da IA): só depois que a triagem da SQ1 tiver ≥ 25 inclusões de consenso. Gera uma planilha cega para você, **sem a decisão da IA**.

**Pronto quando:** κ do piloto reportado; triagem concluída; planilha cega entregue.

---

## Seus pontos de decisão
- Etapa 1: aprovar o texto das emendas v1.1 e v1.2 antes do commit (✅ ambas aprovadas em 2026-10-13).
- Etapa 2: se uma linha do OpenAlex divergir > 5% da congelada, decidir entre aceitar a contagem de hoje ou investigar.
- Etapa 5: aprovar o prompt de triagem e qualquer ajuste de critério depois do piloto.

## Cuidados (aprendidos nas sessões anteriores)
- Coleta, deduplicação e PRISMA são **script**; agentes só na triagem (o limite de gasto da organização derrubou rodadas de agentes duas vezes).
- O resumo **não vai para o git** (repositório público): fica em `data/raw/revisao-sistematica/`, reconstruível com `--reidratar`, e o SHA-256 versionado prova qual texto foi triado.
- GET longo no PubMed dá 414 (usar o *history server*); o OASISBR dá 403 a consulta com ~10 termos ou mais e depois bloqueia o IP (fatias de ≤ 5 + 5, pausa de 3 s, coleta retomável); o OpenAlex não tem curinga e não junta acentos.
- O Firecrawl está sem créditos. O Parallel `web_fetch` alcança o OpenAlex para uma contagem avulsa de conferência, mas não serve para coleta em massa.
