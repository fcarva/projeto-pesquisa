# Checklist PRISMA 2020 (SQ1)

*Page et al. 2021, BMJ 372:n71. Estado em 2026-10-13, depois da deduplicação (Etapa 3) e antes da
triagem. "Protocolo" = está planejado em `protocolo.md` e falta reportar no relatório; "feito" = o
repositório já tem o registro; "pendente" = depende da triagem, da extração ou da redação. A
declaração de uso de IA (PRISMA-trAIce) está em `protocolo.md`, seção "Uso de IA".*

| # | item | estado | onde |
|---|---|---|---|
| 1 | Título identifica o relato como revisão sistemática | pendente | relatório |
| 2 | Resumo estruturado (PRISMA 2020 for Abstracts) | pendente | relatório |
| 3 | Justificativa | protocolo | `protocolo.md`, "Justificativa" |
| 4 | Objetivos / perguntas | protocolo | `protocolo.md`, "Objetivos"; `docs/ars/20-…` §1 |
| 5 | Critérios de elegibilidade e agrupamento para síntese | protocolo | `protocolo.md`, "Critérios de elegibilidade" (emendas v1.1, v1.2) |
| 6 | Fontes de informação, com a data da última busca | feito | `protocolo.md`, "Fontes de informação"; datas em `registros/coletas.jsonl` |
| 7 | Estratégia de busca completa de todas as bases | feito | `apendice-a-estrategias.md`; `ferramentas/scopus_wos.md`; `ferramentas/vufind.md` |
| 8 | Processo de seleção (quantos revisores, independência, automação) | protocolo | `protocolo.md`, "Registros" e "Escala da triagem" |
| 9 | Processo de coleta de dados | protocolo | `protocolo.md`, "Coleta de dados"; Apêndice B (pendente) |
| 10a | Desfechos buscados | protocolo | `protocolo.md`, "Desfechos" |
| 10b | Outras variáveis extraídas | protocolo | `protocolo.md`, "Itens de dados" |
| 11 | Avaliação do risco de viés | protocolo | `protocolo.md`, "Risco de viés" (ROBINS-E / ROBINS-I) |
| 12 | Medidas de efeito | protocolo | `protocolo.md`, "Síntese" |
| 13a | Como se decidiu que estudos entram em cada síntese | protocolo | `protocolo.md`, "Síntese" (≥ 3 estudos com desfecho, contraste e métrica comuns) |
| 13b | Preparação dos dados para síntese | protocolo | `protocolo.md`, "Síntese" (métrica padronizada) |
| 13c | Tabulação e apresentação | protocolo | `protocolo.md`, "Síntese" (SWiM; gráfico de direção) |
| 13d | Métodos de síntese, heterogeneidade, software | protocolo | `protocolo.md`, "Síntese" (REML, Q, I², τ², `statsmodels`) |
| 13e | Exploração da heterogeneidade | protocolo | `protocolo.md`, "Subgrupos pré-especificados" |
| 13f | Análises de sensibilidade | protocolo | `protocolo.md`, "Sensibilidade" |
| 14 | Avaliação do viés de relato | protocolo | `protocolo.md`, "Metavieses" |
| 15 | Avaliação da certeza (GRADE) | protocolo | `protocolo.md`, "Certeza da evidência" |
| 16a | Resultados da busca e da seleção, com fluxograma | parcial | `prisma-fluxo.md`; `paper/overleaf/prisma-sq1.tex` (identificação feita; triagem pendente) |
| 16b | Estudos que pareciam elegíveis e foram excluídos, com motivo | pendente | triagem de texto completo |
| 17 | Características dos estudos | pendente | extração |
| 18 | Risco de viés por estudo | pendente | extração |
| 19 | Resultados de cada estudo | pendente | extração |
| 20a | Características e risco de viés dos estudos de cada síntese | pendente | síntese |
| 20b | Resultado de cada síntese | pendente | síntese |
| 20c | Investigação da heterogeneidade | pendente | síntese |
| 20d | Sensibilidade | pendente | síntese |
| 21 | Viés de relato | pendente | síntese |
| 22 | Certeza da evidência por desfecho | pendente | síntese |
| 23a | Interpretação | pendente | relatório |
| 23b | Limitações da evidência | pendente | relatório |
| 23c | Limitações do processo de revisão | parcial | a registrar: triagem por IA com um revisor humano; SciELO/LILACS por exportação; Scopus por API sem resumo; WoS, EconLit, Embase e CAB fora; OASISBR em fatias (`ferramentas/vufind.md`); recall de validação independente não medido |
| 23d | Implicações | pendente | relatório |
| 24a | Registro (ou declarar que não houve) | feito | `protocolo.md`, "Registro": sem registro externo; o carimbo é o commit `1d12f10` |
| 24b | Onde acessar o protocolo | feito | `docs/revisao-sistematica/protocolo.md` (repositório público) |
| 24c | Emendas ao protocolo | feito | `protocolo.md`, "Emendas" (v1.1 `628bf12`; v1.2 `0be66d3`) |
| 25 | Financiamento | pendente | `protocolo.md`, "Financiamento" (a preencher pelo pesquisador) |
| 26 | Conflitos de interesse | pendente | relatório |
| 27 | Disponibilidade de dados, código e materiais | feito | repositório: `ferramentas/` (código), `registros/` (metadados e contagens), `prompts/` (prompts verbatim); resumos fora do git, reconstruíveis com `--reidratar` |
