# Protocolo de revisão sistemática (PRISMA-P 2015)

**Exposição ambiental a agrotóxicos de uso agrícola, com ênfase na aplicação
aérea, e desfechos ao nascer: protocolo de revisão sistemática, acompanhado de
duas revisões estruturadas complementares (método e escolha de instrumento)**

*Versão 1.0, com as decisões do pesquisador de 2026-10-12, **confirmada pelo pesquisador em 2026-10-12**. Rascunho 0.9 em 2026-10-11. ARS
`deep-research`, modo `systematic-review`, Fase 1. Registro do processo em
`docs/ars/20-revisao-literatura-pesquisa.md`.*

> **Estado:** ✅ **confirmado pelo pesquisador em 2026-10-12** ("Confirmo o v1.0").
> O carimbo de tempo é o commit que registra esta confirmação, anterior a
> qualquer coleta definitiva (`references/systematic_review_protocol.md`, regra 2).
> A partir daqui, toda mudança entra na tabela de emendas, com data e motivo. As
> strings de busca do Apêndice A vieram da calibração de 2026-10-11: o
> desenvolvimento da estratégia, que é anterior à triagem e não a contamina.

---

## INFORMAÇÕES ADMINISTRATIVAS

### Registro
**Sem registro externo**, por decisão do pesquisador (2026-10-12). O carimbo de
tempo é o **commit deste arquivo no git**, feito antes da busca, como na
`docs/pre-especificacao.md`. O relatório final dirá isso, sem sugerir registro
que não houve.

### Autores e papéis

| # | nome | afiliação | papel |
|---|---|---|---|
| 1 | Felipe Carvalho Souza Santos | PPGEco/UFES | garantidor; revisor humano (amostra de calibração, decisões de texto completo, risco de viés dos quase-experimentais) |
| — | assistência de IA | ver §"Uso de IA" | triagem dupla independente, extração, primeira passada de risco de viés, síntese, redação, sempre sob verificação do item 1 |

O orientador (Prof. Renato Seixas) só entra como autor se ele decidir participar.

### Emendas

| data | seção | mudança | motivo |
|---|---|---|---|
| 2026-10-12 (antes da confirmação) | Elegibilidade, exposição | regras de fronteira (a) população mista com medida ambiental; (b) biomonitoramento de composto de fonte exclusivamente agrícola | Devil's Advocate do checkpoint 1: a regra original excluiria as coortes de clordecona, que a PRESS identificou como as mais próximas do caso da banana |

### Financiamento
⬜ *A preencher pelo pesquisador* (bolsa, se houver). Nenhum financiador tem papel na revisão.

---

## INTRODUÇÃO

### Justificativa
A Lei Estadual nº 16.820/2019 (Ceará) proibiu a pulverização aérea de
agrotóxicos: proibiu o **método**, não uma molécula. A literatura que quantifica
o dano perinatal de agrotóxicos agrícolas tem duas tradições que pouco conversam:

1. **Epidemiológica.** Proximidade residencial, registros de uso e biomonitoramento. A revisão mais citada sobre proximidade residencial e desfechos reprodutivos (Shirangi et al. 2011, *Paediatr Perinat Epidemiol*) é anterior a quase toda a evidência atual.
2. **Econômica quase-experimental**, posterior a 2017: Larsen, Gaines & Deschênes (2017); Camacho & Mejía (2017); Calzada, Gisbert & Moscoso (2023); Dias, Rocha & Soares (2023); Reynier & Rubin (2025).

Nenhuma revisão conhecida pelo projeto organiza a evidência pelo **método de
aplicação** (aérea, terrestre, não especificada), pela via (ar, água) e pela
transferibilidade (molécula × método × cultura × medida de exposição). É esse
corte que interessa a quem avalia a proibição de um método, e ele não existe
pronto. A busca de revisões prévias faz parte da Fase 2: se uma revisão recente
e equivalente aparecer, o protocolo será emendado para atualizá-la, e não para
repeti-la.

### Objetivos

**Revisão sistemática principal (SQ1), em PECOS:**

- **P, população:** gestações e nascidos vivos humanos, em qualquer país.
- **E, exposição:** exposição **ambiental ou comunitária** durante a gestação a agrotóxicos aplicados na agricultura, medida por
  (i) proximidade residencial a aplicações ou lavouras;
  (ii) uso agrícola por área (registros de uso, intensidade de cultura);
  (iii) campanhas de aplicação aérea ou fumigação;
  (iv) contaminação da água de abastecimento por agrotóxico agrícola;
  (v) choques de política que deslocam o uso (proibições, liberações, adoção de sementes GM).
  Também é elegível a **aplicação aérea para controle vetorial**, porque o §2º do art. 28-B da Lei 16.820/2019 a alcança (CLAUDE.md, flag 5).
- **C, comparador:** exposição menor ou nula: gradiente de distância ou intensidade, períodos sem aplicação, áreas não expostas, antes/depois de choque.
- **O, desfechos:** primários e secundários na seção Métodos.
- **S, desenho:** quase-experimentais (DiD, VI, regressão descontínua, estudo de evento, experimento natural), coortes, caso-controle, estudos ecológicos ou de painel com exposição espaço-temporal explícita, e transversais com atribuição individual de exposição.

**Pergunta:** *Qual é a associação, e quando o desenho a identifica, o efeito
causal, entre a exposição ambiental na gestação a agrotóxicos de uso agrícola e
o peso ao nascer, o baixo peso e a prematuridade, e como ela varia com o método
de aplicação?*

**Revisões estruturadas complementares (SQ2, SQ3).** Não são perguntas de
efeito em formato PECOS, e por isso **não** recebem risco de viés nem GRADE: são
buscas documentadas com elegibilidade explícita, triagem dupla e síntese
temática. O relatório não as chamará de "revisão sistemática".
- **SQ2 (método):** estimadores e hipóteses para choque simultâneo com intensidade contínua, tratamento mal classificado e poucos clusters (desvio de escopo aprovado em 2026-10-11).
- **SQ3 (Ensaio 2):** que forma da função de dano a literatura de escolha de instrumento para agrotóxicos supõe, e que parâmetro empírico ela exige para ordenar proibição, taxação e zonas-tampão.

---

## MÉTODOS

### Critérios de elegibilidade (SQ1)

| critério | inclui | exclui, com motivo |
|---|---|---|
| Desenho | quase-experimental; coorte; caso-controle; ecológico/painel com exposição espaço-temporal; transversal com exposição individual atribuída | relato/série de casos; revisões (vão para busca de citações); editoriais e comentários; estudos em animais e *in vitro*; modelagem de exposição sem dado de saúde |
| Exposição | via ambiental/comunitária de agrotóxico **agrícola**; aplicação aérea para controle vetorial. **Regras de fronteira (DA-1):** (a) população que inclui trabalhadoras rurais é elegível se a **medida** de exposição for residencial, espacial ou ambiental; (b) biomonitoramento é elegível quando o composto tem **fonte exclusivamente agrícola no contexto** (p. ex. clordecona nas Antilhas Francesas, usada só em bananais) | **exposição medida só pela ocupação** (própria ou do parceiro): a externalidade recai sobre terceiros, e a exposição do trabalhador tem outra via e outra seleção; **uso doméstico ou intradomiciliar**; **biomonitoramento de composto com fontes múltiplas sem atribuição agrícola** (p. ex. metabólitos DAP na população geral), porque não informa a regulação de um método de aplicação; fertilizantes e nitrato sem agrotóxico |
| Desfecho | ao menos um desfecho primário ou secundário | só marcadores intermediários (biomarcadores, comprimento de telômero etc.) |
| Período | 1990 a 2026-10-11 | antes de 1990: anterior à atribuição de exposição por SIG e aos registros de uso |
| Idioma | inglês, português, espanhol | outros, por viabilidade; os excluídos por idioma são contados |
| Status | artigo revisado por pares; *working paper* de séries reconhecidas (NBER, IZA, CEPR, SSRN, RePEc, Banco Mundial, BID, IPEA); *preprint* (medRxiv, arXiv, SSRN) | resumo de congresso sem texto completo; teses e dissertações, por viabilidade (declarado como limitação); notícia |
| Versões | quando há WP e artigo publicado, vale o **publicado**; o WP só entra se reportar resultado que o publicado omite, e isso é registrado | — |

#### Desfechos
**Primários:**
1. peso ao nascer (g, contínuo);
2. baixo peso ao nascer (< 2.500 g);
3. prematuridade (< 37 semanas).

**Secundários:** pequeno para a idade gestacional; óbito fetal ou natimorto;
mortalidade neonatal ou infantil; anomalias congênitas; idade gestacional
(contínua).

#### Janela
Exposição durante a gestação, com ou sem decomposição por trimestre; exposição
pré-concepcional só se reportada junto.

### Critérios de elegibilidade (SQ2 e SQ3)
- **SQ2:** artigos metodológicos de econometria ou estatística, publicados ou em *working paper*/arXiv, que proponham ou avaliem estimadores ou inferência para:
  (a) DiD com tratamento contínuo ou multivalorado;
  (b) efeitos de tratamento ou DiD com tratamento mal classificado ou medido com erro;
  (c) inferência com poucos clusters tratados ou de controle;
  (d) controle sintético ou DiD sintético com poucas unidades;
  (e) aptidão agroclimática (FAO-GAEZ) como instrumento ou preditor de exposição, e instrumentos *shift-share* ou de fórmula.
  Excluídos: aplicações que não contribuem com método; notas de software sem resultado.
- **SQ3:** análises econômicas (teóricas, de simulação ou empíricas) de instrumentos para agrotóxicos: taxas, proibições ou retiradas de moléculas ou de **métodos**, zonas-tampão e recuos, cotas, instrumentos de informação; avaliações *ex post* de proibições ou restrições (sobre uso, produtividade ou saúde, inclusive proibições de agrotóxicos altamente perigosos e suicídio); escolha de instrumento para poluição difusa aplicada a agrotóxicos. Excluídos: agronomia de eficácia sem dimensão econômica ou regulatória.

### Fontes de informação

| fonte | acesso nesta sessão | cobertura | por quê |
|---|---|---|---|
| **OpenAlex** | API REST **direta** (rede irrestrita desde 2026-10-12), com **chave gratuita do pesquisador** (`OPENALEX_API_KEY`); sem chave, a cota diária do IP compartilhado se esgota | multidisciplinar; agrega Crossref, PubMed, arXiv, repositórios | base principal, com contagem reprodutível, operadores booleanos e eco da consulta (`meta.x_query`) para auditoria |
| **PubMed (MEDLINE)** | **API oficial E-utilities**, acesso direto | biomédica, com MeSH | epidemiologia; vocabulário controlado |
| **Índice PubMed/medRxiv/bioRxiv/arXiv** | Firecrawl `research_search_papers` | biomédica e arXiv | busca semântica complementar; ranqueada, sem contagem |
| **Wiley Scholar Gateway** | MCP | texto completo Wiley | econ. agrícola e da saúde (AJAE, *Health Econ*, JAE) |
| **SciELO** | **exportação feita pelo pesquisador** no navegador (o site bloqueia IP de datacenter mesmo com navegador sem interface), com as strings do Apêndice A, em `registros/importados/` | América Latina | literatura brasileira e latino-americana |
| **LILACS (BVS)** | **exportação feita pelo pesquisador** no portal BVS (mesmo bloqueio), com `filter[db][]=LILACS`, a linha DeCS e as strings do Apêndice A | saúde, América Latina | idem, com a tradição Rigotto/ABRASCO |
| **Scopus** | **exportação feita pelo pesquisador** pelo Portal de Periódicos CAPES (CAFe), com a string do Apêndice A, em RIS/CSV com resumo, em `registros/importados/`, com data e contagem anotadas (decisão de 2026-10-12) | multidisciplinar | fecha a lacuna de economia que o PubMed não cobre (JAERE, ReStud) |
| **Web of Science** | **não será buscada** (decisão do pesquisador de 2026-10-12); a ausência é declarada | — | — |
| **Literatura cinzenta** | Firecrawl `search`, Parallel Search | NBER, IZA, SSRN, RePEc/IDEAS, AgEcon Search, Banco Mundial, BID, IPEA, ANPEC | *working papers* são a norma em economia; reduz o viés de publicação |
| **Citações** | OpenAlex (`referenced_works`, filtro `cites:`) e Crossref `reference` | — | **retrospectiva e prospectiva** de todos os incluídos e das revisões relevantes, iterando até não aparecer incluído novo. Os clássicos anteriores a 1990 (SQ3) são conferidos à mão nas listas de referências de 2 ou 3 revisões, porque o OpenAlex os cobre mal |

⚠️ **Sem acesso nesta sessão:** EconLit, Embase e CAB Abstracts. O Europe PMC
e o RePEc direto estão bloqueados pela política de rede; o RePEc é coberto por
busca na web, e o Europe PMC é redundante com PubMed + medRxiv. O relatório
declara essas lacunas.

⚠️ **Limites operacionais:**
- o Firecrawl aceita cerca de 13 a 25 requisições por minuto, compartilhadas;
- o Parallel `web_fetch` pode devolver resposta em *cache* para URLs longas quase idênticas. Por isso, toda contagem registrada confere o eco da consulta (`meta.x_query`) e usa um parâmetro distinto contra o *cache*;
- falhas de requisição são registradas e refeitas, nunca silenciadas.

### Estratégia de busca
As strings por bloco e base, com contagem, recuperação dos itens conhecidos e
a revisão PRESS 2015 (McGowan et al. 2016), estão no **Apêndice A**. A revisão
PRESS foi feita por um agente de IA independente do que desenhou a string, e
**não** por um bibliotecário. Isso fica declarado.

**Teste de sensibilidade da busca (itens conhecidos).** Cada bloco tem um
conjunto semente de estudos que a busca precisa recuperar (Apêndice A). A
recuperação é reportada sobre os itens indexados.

### Registros

**Gestão.** Metadados bibliográficos (ID OpenAlex, DOI, título, ano, periódico,
fonte, string) em `docs/revisao-sistematica/registros/`, versionados no git. Não
há dado pessoal nem microdado.

**Deduplicação.** Por script: DOI normalizado, depois título normalizado + ano.
As contagens antes e depois entram no fluxograma PRISMA.

**Seleção, em três estágios:**
1. **Título/resumo.** Dois triadores de IA **independentes** (instâncias separadas, mesmos critérios, cegas uma à outra), com a regra "na dúvida, inclui". As divergências vão a um terceiro agente adjudicador, que vê as duas justificativas. O resumo vem do OpenAlex (índice invertido) ou, quando ele não tiver, do Crossref ou do índice PubMed. Registro sem resumo passa para o estágio 2 se o título não o excluir.
2. **Texto completo.** Dois revisores de IA independentes, com motivo de exclusão de uma lista fechada; adjudicação por um terceiro. **O pesquisador revê todas as inclusões e todas as exclusões com motivo "exposição" ou "desenho"**, onde estão os casos de fronteira.
3. **Busca de citações** sobre os incluídos, com os mesmos dois estágios.

**Escala da triagem (decisão do pesquisador, 2026-10-12).**
- **SQ1:** triagem **dupla independente** em todos os registros, como descrito acima.
- **SQ2 e SQ3:** **um** triador de IA, com os registros na ordem de relevância do OpenAlex (`sort=relevance_score:desc`) e **regra de parada declarada**: parar depois de **200 exclusões seguidas**, desde que pelo menos **30%** do conjunto tenha sido triado.
- **Auditoria das SQ2/SQ3:** (i) **10%** dos registros triados, sorteados com semente fixa, vão a um segundo triador independente, para medir a concordância; (ii) **5%** da cauda não triada, também sorteados, são triados. Se aparecer um único registro incluível na cauda, a triagem continua por mais 500 registros e a regra é reaplicada.
- O fluxograma PRISMA separa os registros triados dos não triados por causa da regra de parada.

**Calibração humana (PRISMA-trAIce M8/M9).** Antes da triagem completa:
- **piloto:** 50 registros triados pelos dois agentes, para medir a concordância (κ de Cohen) e ajustar a redação dos critérios, com registro de cada mudança;
- **amostra de referência:** **50 registros** da SQ1 (decisão do pesquisador, 2026-10-12), sorteados com semente fixa e estratificados pela decisão de consenso (25 incluídos, 25 excluídos), triados pelo pesquisador **sem ver a decisão da IA**. A partir dela, sensibilidade, especificidade e κ da triagem por IA, **com IC de 95% exato** (Clopper–Pearson). Com 25 incluídos, o IC da sensibilidade é largo, e isso fica declarado. **Se a sensibilidade estimada for < 0,95, os critérios são revistos e todas as exclusões são triadas de novo.**

**Coleta de dados.** Formulário do Apêndice B, preenchido por um agente e
verificado por um segundo contra o texto. Todo número extraído leva uma âncora:
página, tabela ou citação literal. Item ausente vira `NR`; não há contato com
autores, por viabilidade, e isso é declarado.

### Itens de dados
- metadados;
- país e período;
- desenho e estratégia de identificação;
- **construção da exposição:** via (ar ou água), **método de aplicação** (aérea, terrestre, mista, não especificada), classe química e molécula, cultura e se é GM, métrica de exposição, janela ou trimestre;
- comparador;
- desfechos e definição;
- estimativa com IC/EP e unidade;
- N;
- controles e efeitos fixos;
- insumos de risco de viés;
- financiamento e conflito de interesse;
- **codificação de transferibilidade ao Ceará** (molécula × método × cultura × medida), exigida pelo DA, M3;
- **direção do resultado, inclusive nulo e efeito só na cauda**, exigida pelo DA, M2.

### Risco de viés
- **Estudos de exposição** (a maioria): **ROBINS-E** (Higgins et al. 2024, *Environ Int* 186:108602).
- **Estudos que avaliam uma intervenção de política** (proibição, liberação): **ROBINS-I** (Sterne et al. 2016, *BMJ* i4919).
- ⚠️ **Desvio do default do ARS**, que prevê RoB 2/ROBINS-I: o ROBINS-I é para intervenções, e a exposição ambiental é o caso para o qual o ROBINS-E foi feito.
- **Processo:** dois avaliadores de IA independentes, com adjudicação; o pesquisador revê **todas** as avaliações dos quase-experimentais e das que concluírem risco "baixo".
- **Uso na síntese:** análise de sensibilidade sem os de risco alto ou crítico, e rebaixamento no GRADE.

### Síntese
**Meta-análise.** Só quando ≥ 3 estudos compartilham desfecho, tipo de contraste
de exposição e métrica (por exemplo, OR de baixo peso para proximidade binária
num raio comparável). Modelo de efeitos aleatórios (REML), com Q, I², τ² e
intervalo de predição, em Python (`statsmodels`), conforme a convenção do
repositório.

**Quando não houver o que agregar (o esperado, dada a heterogeneidade das
métricas):** síntese sem meta-análise conforme o **SWiM** (Campbell et al. 2020,
*BMJ* l6890):
- agrupamento por via × método de aplicação;
- métrica padronizada quando possível (gramas por contraste de exposição; variação percentual de baixo peso e prematuridade);
- gráfico de direção do efeito;
- contagem por direção, **não** por significância.

**Subgrupos pré-especificados:**
1. **método de aplicação: aéreo × terrestre × não especificado.** É o moderador que interessa à tese;
2. desenho: quase-experimental × epidemiológico convencional;
3. classe química: fungicida, inseticida, herbicida, mistura;
4. renda do país;
5. janela de exposição (trimestre).

**Sensibilidade:** sem risco alto/crítico; deixar um de fora; sem os que só existem como WP.

**Metavieses:** funil + Egger só com ≥ 10 estudos num mesmo agregado;
comparação WP × publicado para relato seletivo.

**Certeza da evidência:** GRADE (Guyatt et al. 2008, *BMJ* 336:924) por desfecho
primário, com o ponto de partida conforme a ferramenta de risco de viés usada.

### Revisões complementares (SQ2, SQ3)
Mesmas fontes, strings próprias (Apêndice A), triagem dupla de título/resumo e
texto completo sem amostra de calibração humana. Síntese temática, com um quadro
por subtema. Para a SQ3, uma coluna obrigatória: **que parâmetro de dano o
estudo supõe ou exige** (inclinação, nível, convexidade, limiar).

---

## USO DE IA (PRISMA-trAIce, itens de Métodos)

| item | conteúdo |
|---|---|
| M1 protocolo | o uso de IA está **pré-especificado neste protocolo**; desvios entram na tabela de emendas |
| M2 ferramentas | (a) Claude (Anthropic), via Claude Code em sessão na nuvem; ⬜ **versão do modelo a preencher pelo pesquisador**; (b) Academic Research Skills (ARS), Imbad0202/academic-research-skills, v3.23.0, commit `d1e5171`; (c) Firecrawl (busca, *scrape*, índice de pesquisa), API hospedada; (d) OpenAlex API; (e) Wiley Scholar Gateway; (f) Parallel Search. Sem versão pública para (c)–(f): registra-se a data de acesso |
| M3 finalidade e etapa | IA na: calibração das strings e revisão PRESS; triagem dupla (título/resumo e texto completo); adjudicação; extração com verificação; risco de viés (primeira passada); síntese e redação. Humano em: escolha das perguntas e critérios, amostra de referência, revisão das decisões de texto completo e do risco de viés dos quase-experimentais, aprovação final |
| M4 dados de entrada | sem *fine-tuning*. Entram metadados e resumos públicos (OpenAlex, Crossref, PubMed) e textos completos de acesso aberto ou WP |
| M5 saída | JSON validado por esquema (decisão, motivo, citação literal); pós-processamento por script versionado em `docs/revisao-sistematica/ferramentas/` |
| M6 prompts | **todos os prompts, na íntegra**, em `docs/revisao-sistematica/prompts/` (os scripts de *workflow* executados, verbatim). Parâmetros de amostragem (temperatura etc.) **não são expostos** pelo Claude Code e ficam declarados como padrão da plataforma |
| M7 | não se aplica (sem ML clássico) |
| M8 interação humano-IA | 1 revisor humano (mestrando em economia) + triadores de IA; supervisão pela amostra de referência e pela revisão humana das decisões listadas acima |
| M9 avaliação | sensibilidade, especificidade e κ da triagem por IA contra a amostra de referência do pesquisador; κ entre os dois agentes; recuperação dos itens conhecidos na busca |
| M10 dados | só metadados bibliográficos públicos, guardados no repositório; nenhum dado pessoal |

---

## APÊNDICES

### Apêndice A — Estratégias de busca, contagens e recuperação
Em arquivo próprio, **`apendice-a-estrategias.md`**: strings congeladas por bloco e
base, notas de sintaxe, recall de itens conhecidos, volume esperado e traduções
para Scopus/WoS. Logs completos em `calibracao/`.

### Apêndice B — Formulário de extração
Campos de "Itens de dados", em JSON, com âncora textual obrigatória para todo número.

### Apêndice C — Lista PRISMA-P
Conferida no Estágio 2.5 (integridade).

## Histórico de versões

| versão | data | mudança |
|---|---|---|
| 0.9 | 2026-10-11 | rascunho para confirmação |
| 1.0 | 2026-10-12 | (rev.) acesso direto a PubMed, Crossref, arXiv e RePEc; OpenAlex com chave; SciELO e LILACS exportados pelo pesquisador |
| 1.0 | 2026-10-12 | Apêndice A congelado (PRESS); emenda DA-1 nas regras de exposição; decisões do pesquisador: escala da triagem, amostra de referência de 50, sem registro externo, Scopus sim e WoS não |
| 1.0 | 2026-10-12 | **confirmado pelo pesquisador**; carimbo = o commit desta linha. A busca definitiva começa depois dele |
