# Academic Integrity Verification Report

**Manuscrito:** `paper/projeto/projeto.tex` (resumo), `paper/projeto/secoes/01-introducao.tex` a `08-cronograma.tex`, `paper/projeto/secoes/apendices.tex`; bibliografia em `paper/projeto/referencias-projeto.bib` e `paper/referencias.bib`. Commit conferido: `96dc402` ("Projeto v4: resíduos da re-revisão").
**Data:** 2026-11-16
**Agente:** integrity_verification_agent (ARS v3.24.2), Estágio 4.5

## Verification Mode

**Mode 2: Final check (final-check)**, passada do zero. Nenhum veredito do Estágio 2.5 foi reaproveitado; os textos-fonte guardados em `evidence/sources/` foram reutilizados como insumo, e cada afirmação foi conferida de novo contra o texto atual.

## Verdict

**FAIL**

Não há issue SERIOUS nem MEDIUM. O veredito é FAIL só pela regra do Estágio 4.5, em que MINOR também bloqueia: há **6 MINOR** abertas e nenhuma decisão registrada do pesquisador sobre elas no passport ou no ledger (as duas MINOR herdadas do 2.5 constam como `open_minor: 2`, sem decisão). Todas se resolvem com edição curta; nenhuma toca o desenho, salvo um item da IL-MINOR-3 (c), que pede uma escolha do autor.

## Verification Summary

| Item | Verificado / total | Passou | Observação |
|---|---|---|---|
| Fase A, referências | 46 / 46 (100%) | 46 existem; 44 sem reparo de campo | 2 MINOR de campo (IL-MINOR-4 e 5) |
| Fase B, contextos de citação | 63 / 63 comandos (73 chaves citadas) | 63 adequados | 1 frase factual sem a citação que a sustenta (IL-MINOR-1) |
| Fase C, superfícies de dado | 9 / 9 grupos | 9 | contagens recalculadas das respostas guardadas do SIDRA |
| Fase C2, consistência interna | resumo, título, equação, Quadro da regra, Apêndices A a D, H1 a H5, cronograma | 4 desencontros | IL-MINOR-3 |
| Fase D, originalidade | 54 / 54 parágrafos de prosa (100%; 44 novos ou modificados) | 54 sem coincidência | quadros e figura não sondados; ver limitações |
| Fase E, afirmações registradas | 92 com veredito / 94 registradas | 84 VERIFIED; 8 UNVERIFIABLE_ACCESS | 2 afirmações de primazia vão ao E5 (sem fonte a rastrear) |
| Modos de falha | 7 / 7 | nenhum bloqueio | Modos 1, 3 e 6 cobertos pelo override registrado |

Contagem por severidade: **SERIOUS 0; MEDIUM 0; MINOR 6.** Notas que não bloqueiam: 8 UNVERIFIABLE_ACCESS; 3 linhas ADV-E5; 1 candidato mecânico de cobertura (falso positivo).

Restrições do autor:

- **Nenhum número de estimativa do autor:** cumprida. Os números do texto são contagens de fontes públicas (184 municípios; 36 estabelecimentos em 7 municípios; 23, 18, 16 e 4 pontos de coleta) e magnitudes da literatura (23 a 32 g; 80 g; 150 m; 150 a 2.500 m).
- **15 páginas textuais:** cumprida. O PDF tem 27 páginas; os capítulos 1 a 8 ocupam as páginas impressas 5 a 19 (15 páginas); referências de 20 a 22; apêndices de 23 a 26. O PDF é posterior ao último `.tex` e o log não tem referência indefinida.
- **Só Ensaio 1:** cumprida. O segundo ensaio aparece em `03-referencial.tex:19-22` e `08-cronograma.tex:19-22, 49` como destino do insumo e como uma linha do cronograma.

## Comparação com as issues do Estágio 2.5

| Issue do 2.5 | Estado no 4.5 |
|---|---|
| v2 r1, IL-SERIOUS-1 ("banana familiar não tem o avião") | Resolvida e mantida: `05-metodologia.tex:134-136` trata como hipótese, com verificação e regra de exclusão |
| v2 r1, IL-MEDIUM-1 (terceiro trimestre de Calzada et al.) | Resolvida e mantida: `03-referencial.tex:53-54` diz "estimativa imprecisa no terceiro", o que confere com o manuscrito (-43,17; erro-padrão 37,84) |
| v2 r2, IL-MINOR-1 (Skevas citado com Weitzman) | Resolvida: `skevas2012` não é mais citado |
| v2 r2, IL-MINOR-2 (campos de `ibge2017censoagro`, `agenciabrasil2016ceara`, `globorural2021bananais`) | Aberta em parte: a Globo Rural ganhou data e URL; faltam repórter na Agência Brasil, tabela no Censo 2017 e datas de acesso. Absorvida na IL-MINOR-4 |
| v2 r2, IL-MINOR-3 (completude das entradas normativas; ano do Censo 2006) | Aberta: IL-MINOR-4 e IL-MINOR-5, agora com os valores confirmados |
| 9 UNVERIFIABLE_ACCESS | 8. Saíram a de Canay et al. (a frase sobre variação interna ao município foi retirada) e a do terceiro trimestre no capítulo 5 (frase retirada); entrou `C06` por causa da frase nova sobre doença e frequência |
| 5 ADV-E5 | 3. Saíram do texto "primeira proibição estadual", "registros nunca explorados" e "primeira medida" |
| Modos 3 e 6 SUSPECTED pela regra | Sem mudança no texto; cobertos pelo override registrado |

Achados da re-revisão (Estágio 3') conferidos aqui: NEW-2 (Pereira e Cuellar) está corrigido no texto; S14 (Rigotto et al.) está corrigido; NEW-1 (período de referência) está corrigido na definição, com um resíduo na IL-MINOR-3 (a).

## Phase A: Reference Verification Results

Fonte da verdade: as 46 chaves citadas no texto atual (46 entradas no `.bbl`). `skevas2012` e as demais entradas não citadas não foram verificadas.

- **29 com DOI:** todas resolvem no Crossref nesta rodada (consulta nova a cada DOI), com título, periódico, volume, número, páginas, ano e sobrenomes dos autores comparados por script. Quatro alertas do script eram falsos: acento em Wüthrich e em *Estudos Avançados*; Böcker et al. tem ano de publicação eletrônica 2019 e de fascículo 2020, e o Crossref não devolve páginas (371–402 confirmadas em rodada anterior por outra via); Weitzman tem só a página inicial no Crossref (477–491 confirmadas no RePEc).
- **Pré-verificação em lote (Semantic Scholar):** 24 de 29 DOIs encontrados; os 5 ausentes (Olden e Møen; Buckles e Hungerman; NBER w32117; Callaway e Sant'Anna; Arkhangelsky et al.) existem no Crossref.
- **1 preprint:** `denteh2022misclassification`, arXiv:2207.11890, versão 3 atualizada em 2026-04-30, título e primeiro autor conferem.
- **Novas na revisão:** `rocha2015water` (JDE 112:72–91, 2015) e `pereira2015conflitos` (*Estudos Avançados* 29(84):115–137, 2015) existem e todos os campos conferem com Crossref e OpenAlex.
- **16 sem DOI** (normas, bases estatísticas e imprensa): todas existem. Reconferidas hoje por acesso direto: Lei 12.228/1993, Lei 16.820/2019, Lei 19.135/2024, PL 18/2015 e PL 134/2011 (páginas da ALECE, HTTP 200), Lei municipal 1.511/2010 (PDF da Câmara, HTTP 200), Agência Brasil e Globo Rural (HTTP 200), IN MAPA 2/2008 (trechos do PDF do gov.br, com as alterações da IN 37/2020). Conferidas só nas cópias guardadas em rodadas anteriores: Decreto 4.074/2002 (uma alínea), Resolução CNS 510/2016 (PDF), ADI 6137 (notícia do STF), tabelas do SIDRA. A página do HGCC (`ceara2018nascer`) devolveu erro de conexão hoje; foi lida em 15/11.

Resultado: nenhuma referência inexistente; nenhuma SERIOUS. Os reparos de campo estão nas IL-MINOR-4 e IL-MINOR-5.

## Phase B: Citation Context Verification Results

63 comandos de citação (73 chaves): 01 (10), 02 (13), 03 (18), 05 (17), 06 (2), 07 (2), apêndices (1). Todos foram lidos no contexto; 61 estão no registro de afirmações e 2 são citações de uso sem afirmação factual própria (`02-contexto.tex:48-49`, Calzada et al. como análogo; `05-metodologia.tex:212-213`, PAM como fonte da dose). Nenhuma citação aponta para trabalho que não sustenta a frase.

Pontos que o coordenador pediu:

- **Rocha e Soares (2015)**, três contextos (`03-referencial.tex:58-61`; `05-metodologia.tex:146-148`; `07-ameacas.tex:15-16`): conferem com o resumo da versão publicada ("negative rainfall shocks are robustly correlated with higher infant mortality, lower birth weight, and shorter gestation periods"). O texto integral não foi lido.
- **Pereira e Cuellar (2015)** (`07-ameacas.tex:12-15`): o texto agora atribui ao artigo só a restrição de água para irrigação, e deixa a retração da lavoura como pergunta ("é questão a verificar nas séries de área e de emprego"). Confere: racionamento a partir de meados de 2014, corte de 50% para o arroz e de 8,5% para as frutas em Tabuleiro de Russas, rebaixamento do aquífero Jandaíra na Chapada. O artigo cobre 2012 a 2014 e relata aumento da produção dos perímetros até então. O Apêndice B (`apendices.tex:55`) diz "Possível retração", coerente.
- **Calzada et al.**: "três meses ou mais de fumigação intensiva", "em comparação com a fumigação habitual", variação com o limiar, ausência de gradiente entre 150 e 2.500 m e "estimativa imprecisa no terceiro" conferem com o manuscrito de março de 2023. A versão publicada no JAERE não foi lida (ver Fase E).
- **Rigotto et al.** (`03-referencial.tex:38-41`): confere com o texto completo, lido nesta rodada. Razão de taxas de internação por neoplasias 1,76; "there were no statistically significant differences in the comparison of rates of fetal death (p > 0.05)"; "an increasing and statistically significant trend is observed (p < 0.05) in mortality rates of the study cities".
- **Jones (2020)** e **Reynier e Rubin (2025)**: conferem (resumo e texto completo, respectivamente). Reynier e Rubin relatam redução do peso e da duração da gestação, como diz `01-introducao.tex:40-43`.
- **"as reportagens … nomeiam a sigatoka-amarela"** (`02-contexto.tex:34-35`): as duas reportagens citadas nomeiam a doença.

## Phase C: Data Verification Results

**C1, superfícies de dado (9 grupos de 9):**

| Local | Dado | Resultado |
|---|---|---|
| `02-contexto.tex:16` | 184 municípios | Confere (SIDRA, UF 23) |
| `02-contexto.tex:55-57` | 36 estabelecimentos em 7 municípios | Recalculado: Limoeiro do Norte 18, Quixeré 9, Aiuaba 5, Jaguaruana, Mauriti, Quiterianópolis e Quixeramobim 1 cada |
| `02-contexto.tex:58-60` | maioria dos municípios com banana sem registro de avião | Recalculado: 169 com área (2015–2018); 162 sem registro |
| `02-contexto.tex:44-46` | 23 pontos; todos; 18; 16; 4 | Confere (recontagem de rodada anterior; hoje só a presença da tabela) |
| `03-referencial.tex:30-31` | 23 a 32 g | Confere (texto completo) |
| `03-referencial.tex:32-36`; `07-ameacas.tex:24-25` | 80 g; 150 m; três meses; 150 a 2.500 m | Confere no manuscrito de 2023 |
| datas legais (capítulo 2 e Apêndice D) | 09/12/1993; 20/11/2009; 26/05/2010; 31/05/2011; 24/02/2015; 08 e 09/01/2019; 05/2023; 19/12/2024 | Conferem em fonte primária |
| datas por fonte secundária | 04/2010; 03 e 07/2011; 2012–2017; 18/12/2018 | Conferem; o Apêndice D declara a origem secundária dos eventos de 2011 a 2017 |
| `apendices.tex:132` | 03/2018 | Confere (26/03/2018) |

**C2, consistência interna.** Resumo contra o corpo: confere em todos os pontos (objeto, desenho, grupos, período de referência, seca de 2012–2017, entrega por cenário). Título ("efeitos sobre o peso ao nascer") confere com a hipótese confirmatória única. Equação contra o Apêndice C: `β` (H1) e `β_S` (H2) conferem; estudo de evento com 2011 como base nos dois lugares. Regra de decisão contra o capítulo 8 e o cronograma: data-limite no fim do terceiro bimestre nos três lugares; cinco linhas do quadro coerentes com `08-cronograma.tex:8-22`. Sensibilidade 2008–2010 confere entre `05-metodologia.tex:128-129` e `apendices.tex:78`. Contagens anunciadas e itens listados conferem em 14 de 15 casos. Referências cruzadas aos quadros movidos (`ap:fontes`, `ap:ameacas`, `ap:espec`, `ap:cronologia`, `qua:regra`, `qua:cronograma`, `sec:regra`, `sec:medicao`, `sec:onde-aviao`, `eq:ddd`, `fig:dag`) resolvem. Os quatro desencontros estão na IL-MINOR-3.

**C3, figuras e tabelas.** A Figura 1 é um diagrama desenhado no próprio `.tex`, sem pacote de figura a rastrear (nota: rastreio indisponível, não é issue). O conteúdo confere com o texto: efeitos fixos da equação, chuva com seta para o voo e para a saúde fetal, canal de emprego remetido ao capítulo 7.

**C4/D7, declaração de experimentos.** This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS. A declaração segue `no_experiments_declared`. O texto não reporta resultado próprio. Ele divulga, sem número, que uma rodada exploratória da forma reduzida foi executada e levou a rever o alvo (`05-metodologia.tex:291-296`), que um levantamento preliminar achou a lei de Limoeiro do Norte (`06-dados.tex:33-36`) e que uma avaliação preliminar apontou limitações em duas bases (`06-dados.tex:41-43`). As três frases conferem com o repositório (`docs/pre-especificacao.md`, linhas de 2026-09-21 e 2026-09-22; `docs/legislacao/README.md`; `docs/lacunas-de-dados.md`). A discordância entre a declaração e a divulgação é a mesma do 2.5 e está coberta pelo override registrado (ver checklist).

## Phase D: Originality Verification Results

Foram sondados os 54 parágrafos de prosa do resumo, dos capítulos e do rodapé do Apêndice C (100%), dos quais 44 são novos ou modificados desde `8922a12`. Método: uma sequência de 10 palavras do período mais longo de cada parágrafo, entre aspas, em um buscador (Bing), com verificação por script de ocorrência exata na página de resultados. **Nenhuma coincidência exata.** Não foram sondados os seis quadros nem a figura.

Limites: um buscador só; uma frase por parágrafo; a checagem pega cópia literal, não paráfrase nem tradução. D2 (autoplágio em publicações anteriores do autor) não foi executado, porque exigiria enviar o nome do autor a serviços externos.

**Falha minha a registrar:** o script de sondagem tratou três blocos do preâmbulo de `projeto.tex` como parágrafos, e uma das consultas enviadas ao buscador continha o nome do autor (campo `pdfauthor`). Foi uma consulta, sem outro dado do projeto além do nome. Contraria a regra de não enviar dados pessoais a serviços externos; não tem efeito sobre o resultado.

## Phase E: Claim Verification Results

**Critério declarado:** VERIFIED quando o resumo, o texto completo ou a fonte primária da versão citada contém a afirmação; UNVERIFIABLE_ACCESS quando a versão citada não pôde ser lida, ainda que outra versão confirme.

- **Registro (E1):** 94 afirmações em 10 arquivos (`claim_registry__<arquivo>.json`), todas com faixa exata de bytes e SHA-256 do arquivo-fonte, camada `ALL`.
- **Cobertura (E1.1):** `coverage__<arquivo>.json`, replay PASS nos 10. Um candidato mecânico não registrado, o intervalo `[0,1]` em `05-metodologia.tex:91`, que é notação e não afirmação. A cobertura semântica não é detectável por máquina: o detector não reconhece `\cite{}` nem unidades em português.
- **Verificação (E3):** 92 de 92 com veredito: **84 VERIFIED; 8 UNVERIFIABLE_ACCESS; 0 MINOR_DISTORTION; 0 MAJOR_DISTORTION; 0 UNVERIFIABLE.** As 2 restantes (N01, N02) são afirmações de ausência de literatura, que não têm fonte a rastrear, e seguem para o E5.
- **Linhas de evidência (E3.1):** 114 linhas em `evidence_rows.json`, validação PASS contra `evidence/sources/` (43 arquivos; proveniência em `sources_manifest.json`). 76 com trecho extraído por este agente; 35 sem âncora (fatos sem citação no texto, conferidos em fonte externa descrita no campo `detail`); 3 com falha de acesso.

**UNVERIFIABLE_ACCESS (8, notas):**

| ID | Local | Motivo |
|---|---|---|
| C06 | `01-introducao.tex:55-57` | Calzada et al.: só o manuscrito de março de 2023; versão do JAERE não lida |
| C08 | `02-contexto.tex:35-37` | idem |
| C15 | `03-referencial.tex:32-36` | idem. O resumo publicado fala em 80 a 150 g; o texto usa 80 g, da especificação principal do manuscrito |
| C18 | `03-referencial.tex:53-56` | idem |
| H14 | `07-ameacas.tex:24-25` | idem |
| C07 | `01-introducao.tex:61-63` | Weitzman (1974) não lido; as outras três fontes conferem no resumo |
| C11 | `03-referencial.tex:16-18` | Weitzman (1974) não lido |
| C10 | `03-referencial.tex:13-14` | Coase (1960) não lido |

**Afirmações VERIFIED com ressalva de alcance:** conferidas só no resumo (não no texto integral): Dias et al., Larsen et al., Camacho e Mejía, Lichtenberg et al., Helfand e House, Buckles e Hungerman, Currie e Schwandt, Brainerd e Menon, Rocha e Soares, Goodman-Bacon, de Chaisemartin e D'Haultfœuille, Olden e Møen, Arkhangelsky et al., Conley e Taber, Ferman e Pinto, Chernozhukov et al., MacKinnon e Webb, Hagemann, Canay et al., Jones; só no título: Callaway e Sant'Anna (2021). Pereira e Cuellar: resumo e cinco trechos do texto, não o texto integral.

**Fatos novos sem citação própria, conferidos em fonte externa** (detalhe nas IL-MINOR-1 e 6):

| Local | Afirmação | Fonte encontrada |
|---|---|---|
| `02-contexto.tex:37-38` | produtor relata duas aplicações por ano | Globo Rural, 09/04/2021 (citada no parágrafo, não na frase) |
| `05-metodologia.tex:125-126` | relatos de voos em 2007–2011 | Agência Brasil: aplicações mais intensas de 2004 a 2010 e nenhuma desde 2012; para 2011, só inferência |
| `05-metodologia.tex:128` | em 2011 já havia notícia de proibição | Mapa de Conflitos da Fiocruz (fonte secundária) |
| `05-metodologia.tex:181-182` | relatórios registram drones desde 2021 | Portaria MAPA 298/2021, arts. 11 e 19, I (fonte primária) |
| `06-dados.tex:16-18`; `apendices.tex:18` | troca do formulário do SINASC em 2011 alterou a idade gestacional | Ministério da Saúde, consolidação do SINASC 2011 (fonte primária) |
| `apendices.tex:27` | relatórios em papel até 2021 | notas do SINDAG de 17/06/2021 e 07/04/2023 (parte interessada) |

**E4 (escopo):** nenhuma linha.

**Novelty-claim classification (#548), advisory-only.** Não bloqueiam e não entram na contagem de issues.

| ID | Local | Redação | Classificação | Observação |
|---|---|---|---|---|
| ADV-E5-1 | `01-introducao.tex:22-23` | "não se localizou, na literatura consultada, avaliação causal dos efeitos dessa resposta" | UNRESOLVED | A redação é limitada à busca, mas não há estratégia de busca documentada nem data da busca |
| ADV-E5-2 | `01-introducao.tex:74-75` | "não há estimativa do que a proibição de fato produziu" | UNRESOLVED | Redação absoluta. Uma busca minha achou um capítulo de livro de 2023 (*Ambiente, saúde e agrotóxicos: desafios e perspectivas…*) que compara a produção e a exportação de banana no Ceará antes e depois da lei (2017 a 2021), de forma descritiva. Não trata de saúde e não é estimativa causal, mas contradiz a forma absoluta. Li só os trechos devolvidos pela busca; não identifiquei os autores do capítulo |
| ADV-E5-3 | `03-referencial.tex:44-46` | Jones "é dos poucos estudos em que fungicidas têm peso" | UNRESOLVED | A parte sobre fungicidas confere; "dos poucos" não tem base de busca |

**E6 (deriva de força na revisão):** não executado; não há pacote de revisão no formato que o protocolo consome. A re-revisão correu em modo legado (`[LEGACY-NO-CONTRACT]`), sem registros `previously_missed` ou `indeterminate` a consumir.

## Issue List (Sorted by Severity)

### SERIOUS (Must Fix)

Nenhuma.

### MEDIUM (Must Fix)

Nenhuma.

### MINOR (Recommended Fix at Stage 2.5; Must Fix at Stage 4.5)

**IL-MINOR-1. Declaração atribuída a um produtor, sem citação.** `paper/projeto/secoes/02-contexto.tex:37-38`: "no Ceará, um produtor relata duas aplicações aéreas por ano." A fonte é a reportagem da Globo Rural, citada duas frases antes para outro fato; o produtor é do Cariri, não da Chapada, que é o assunto da seção.
Correção: `no Ceará, um produtor do Cariri relata duas aplicações aéreas por ano \cite{globorural2021bananais}.`

**IL-MINOR-2. Generalização a partir de um relato.** `paper/projeto/secoes/03-referencial.tex:35-36`: "Como no Ceará as aplicações são menos frequentes, esse valor é tomado como teto." O único apoio é o relato de um produtor, em reportagem; o capítulo 2 o apresenta como relato e o capítulo 7 diz que a frequência será verificada.
Correção: `Como o único relato disponível para o Ceará indica aplicações menos frequentes (Capítulo~\ref{cap:contexto}), esse valor é tomado como teto.`
Mesmo ajuste, opcional, em `01-introducao.tex:56-57` ("a doença combatida e a frequência das aplicações não são as mesmas" → "a doença combatida não é a mesma e, pelo relato disponível, a frequência das aplicações é menor") e em `07-ameacas.tex:35` ("e com poucas aplicações por ano" → "e se as aplicações forem poucas por ano").

**IL-MINOR-3. Quatro desencontros internos.**
(a) Período de seca. A equação define `Seca_t` como as coortes nascidas de 2013 a 2018 e exclui a de 2012 (`05-metodologia.tex:92, 106`), mas H2 fala em "entre 2012 e 2018" (`04-objetivos.tex:31-32`) e o diagnóstico em "fechamento do hiato em 2012--2018" (`05-metodologia.tex:169`). Correção nos dois lugares: `nas coortes nascidas de 2013 a 2018`.
(b) Estatuto de H2. `04-objetivos.tex:30-31` diz "As demais são exploratórias"; `05-metodologia.tex:110-111` e `apendices.tex:97` dizem que `β_S` é "descritivo". Correção em `04-objetivos.tex`: `As demais são exploratórias, e a do período de seca, descritiva.`
(c) Sensibilidade só no apêndice. `apendices.tex:63` promete "estimativas com e sem 2020--2021", que não aparece no capítulo 5 nem no quadro de especificações. Correção, à escolha do autor: acrescentar ao Apêndice C a linha `Sem 2020--2021 & Equação~\ref{eq:ddd} sem as coortes nascidas em 2020 e 2021 & Mesma amostra; sensibilidade. \\`, ou retirar o trecho do Apêndice B.
(d) Contagem. `03-referencial.tex:56` anuncia "Duas ameaças a esse desenho" e seguem três (composição das mães; sazonalidade que persiste entre irmãos; chuva). Correção: `Três ameaças a esse desenho são conhecidas.`

**IL-MINOR-4. Entradas normativas, estatísticas e de imprensa incompletas** (`paper/projeto/referencias-projeto.bib`). Em todas falta a data de acesso; no abnTeX2 o campo é `urlaccessdate` (por exemplo, `urlaccessdate = {15 nov. 2026}`, com a data em que o autor de fato acessou). Valores confirmados por mim hoje, salvo indicação:

| Entrada | Falta | Valor confirmado |
|---|---|---|
| `ceara2019lei16820` | URL, acesso | `https://www2.al.ce.gov.br/legislativo/legislacao5/leis2018/16820.htm` (a pasta é `leis2018`) |
| `ceara1993lei12228` | data do D.O., URL, acesso | `Diário Oficial do Estado, Fortaleza, 14 dez. 1993`; `https://www2.al.ce.gov.br/legislativo/legislacao5/leis93/12228.htm` |
| `ceara2024lei19135` | data do D.O., URL, acesso | `Diário Oficial do Estado, Fortaleza, 19 dez. 2024`; `https://www2.al.ce.gov.br/legislativo/legislacao5/leis2024/19135.htm` |
| `ceara2015pl18` | URL, acesso | `https://www2.al.ce.gov.br/legislativo/tramit2015/pl18_15.htm` |
| `ceara2011pl134` | URL, acesso | `https://www2.al.ce.gov.br/legislativo/tramit2011/pl134_11.htm` |
| `cns2016res510` | data e página do DOU, URL, acesso | `Diário Oficial da União, Brasília, 24 maio 2016, Seção 1, p. 44-46` (do PDF do Conselho); URL não reconferida hoje |
| `brasil2002decreto4074` | data do DOU, URL, acesso | não confirmei a data do DOU (o planalto.gov.br não responde a esta sessão); o autor precisa conferir |
| `mapa2008in2` | URL, acesso | `https://www.gov.br/agricultura/pt-br/assuntos/insumos-agropecuarios/aviacao-agricola/legislacao/3-in-2-de-03-de-janeiro-de-2008-com-alteracoes-da-in-37-2020.pdf` (texto com as alterações da IN 37/2020) |
| `ibge2017censoagro` | número da tabela, URL, acesso | tabelas 6955 e 6956 (produtos da lavoura permanente por tipologia), conferidas em rodada anterior; hoje o SIDRA recusou a consulta de metadados. O autor deve pôr a tabela que de fato usar |
| `ibgepam` | URL | `https://sidra.ibge.gov.br/tabela/1613` (não reconferida hoje) |
| `limoeiro2010lei1511` | acesso | URL presente e ativa |
| `agenciabrasil2016ceara` | repórter, acesso | Edwirges Nogueira (assinatura na página); forma ABNT: `author = {Nogueira, Edwirges}`, com `Agência Brasil` na nota |
| `globorural2021bananais` | acesso | URL ativa; não identifiquei a autoria |
| `ceara2018nascer` | acesso | URL lida em 15/11; hoje devolveu erro de conexão |
| `stf2023adi6137` | nada obrigatório | completa |

**IL-MINOR-5. Ano de publicação do Censo Agropecuário 2006.** `ibge2006censoagro` traz `year = {2006}`, que é o ano de referência. Os resultados saíram em 30/09/2009; em 2012 o IBGE publicou a segunda apuração (*Censo agropecuário: 2006: Brasil, grandes regiões e unidades da federação: segunda apuração*. Rio de Janeiro: IBGE, 2012. 758 p.), cuja apresentação diz que a nova base "substitui integralmente a edição anterior" e inclui a recarga das tabelas no SIDRA.
Correção: `title = {Censo Agropecu{\'a}rio 2006: segunda apura{\c c}{\~a}o}`, `year = {2012}`, `note = {Sistema IBGE de Recupera{\c c}{\~a}o Autom{\'a}tica (SIDRA), tabela 1008. Rio de Janeiro}`, `url = {https://sidra.ibge.gov.br/tabela/1008}`, mais `urlaccessdate`.
Ressalva: não consegui abrir hoje os metadados da tabela 1008 para ler nela o rótulo da apuração; a atribuição a 2012 vem da declaração do IBGE de que a base foi substituída.

**IL-MINOR-6. Fatos institucionais novos sem fonte na bibliografia.** Os três conferem; falta dar a fonte ao leitor.
(a) `06-dados.tex:16-18` e `apendices.tex:18`, troca do formulário do SINASC em 2011. Fonte: BRASIL. Ministério da Saúde. Secretaria de Vigilância em Saúde. *Consolidação do Sistema de Informações sobre Nascidos Vivos – 2011*. Brasília. `http://tabnet.datasus.gov.br/cgi/sinasc/Consolida_Sinasc_2011.pdf` (ano do documento a conferir pelo autor; o arquivo é de 2013). O documento informa que em 2011 os dois formulários conviveram (58% dos registros no novo), o que interessa à ressalva sobre a prematuridade.
(b) `05-metodologia.tex:181-182`, drones nos relatórios desde 2021. Fonte: BRASIL. Ministério da Agricultura, Pecuária e Abastecimento. Portaria nº 298, de 22 de setembro de 2021. *Diário Oficial da União*, Brasília, 24 set. 2021, Seção 1, p. 14 (em vigor desde 01/10/2021; arts. 11 e 19, I). O relatório do operador de drone traz município, aeronave, área, tipo de atividade e produto, sem cultura.
(c) `apendices.tex:27`, "Em papel até 2021". O apoio que encontrei é do sindicato do setor (SINDAG, "Setor ganha plataforma digital para envio de relatórios ao Mapa", 17/06/2021, `https://sindag.org.br/setor-ganha-plataforma-digital-para-envio-de-relatorios-ao-mapa`). Correção: citar essa nota, ou escrever `Envio eletrônico só a partir de 2021, segundo o setor; preservação incerta.`
(d) `05-metodologia.tex:125-126`, "anos em que há relatos de voos na Chapada". Correção: acrescentar `(Seção~\ref{sec:onde-aviao})`. O relato citado cobre 2004 a 2010 de forma explícita; 2011 só por inferência, o que o parágrafo já admite ao reportar 2008–2010.

## AI Research Failure Mode Checklist

Declaração no passport: `no_experiments_declared`. Override dos Modos 1, 3 e 6 registrado em `passport.yaml` (`integrity_stage_2_5.failure_mode_overrides`), decidido pelo pesquisador com as palavras: "como é um projeto de pesquisa essa parte vai ser feita ao longo do ano, então é só o que eu vou fazer". O passport manda reavaliar no 4.5. Reavaliação: **o texto da v4 não muda nada nesse ponto.** A revisão alterou o desenho (referência fixa em 2007–2011, coeficiente próprio para a seca, efeito fixo de município por ano, chuva como controle, hipótese confirmatória única, regra de decisão em dois eixos) e não acrescentou análise executada pelo autor nem resultado. As frases que divulgam trabalho preliminar são as mesmas do 2.5 e conferem com o repositório.

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | INSUFFICIENT EVIDENCE, coberto pelo override registrado | Nenhum código nem resultado é apresentado; a rodada exploratória divulgada não é reportada | no |
| 2. Hallucinated citation | CLEAR | 46 de 46 referências existem; as duas novas conferem em todos os campos e no conteúdo | no |
| 3. Hallucinated experimental result | SUSPECTED pela regra da declaração, resolvido por override do pesquisador com justificativa | Nenhum resultado próprio no texto; as contagens descritivas foram recalculadas de fonte pública | no |
| 4. Shortcut reliance | CLEAR | Não há resultado que possa depender de atalho; o desenho declara de antemão o que cada cenário entrega, inclusive o de ausência de voos | no |
| 5. Implementation bug reframed as novel insight | NOT APPLICABLE | Sem resultado | no |
| 6. Methodology fabrication | SUSPECTED pela regra da declaração, resolvido por override do pesquisador com justificativa | Métodos descritos como plano; as três divulgações de trabalho preliminar conferem com o repositório | no |
| 7. Frame-lock at early pipeline stage | CLEAR | A revisão reabriu o desenho em resposta ao painel. As premissas sem registro (voos em 2007–2011; pico sazonal; ausência de avião na banana familiar) estão como hipóteses, com verificação antes da estimação e saída na regra de decisão (`05-metodologia.tex:245-266`) | no |

**Resultado do checklist:** nenhum bloqueio. Modo 4 não está SUSPECTED. Os modos SUSPECTED no 2.5 (3 e 6) estão resolvidos na forma que a regra do 4.5 admite, por override do usuário com justificativa registrada. Observação para o coordenador: o override foi dado na v1 e mantido na v2 por leitura do orquestrador; para a v4 não há nova manifestação do pesquisador. Se o coordenador entender que a v4 pede confirmação, a pergunta é dele ao pesquisador; o texto não a torna necessária.

## Tool Limitation Disclaimer

- A versão publicada de Calzada, Gisbert e Moscoso (2023) no JAERE não foi lida em nenhuma rodada; as cinco afirmações que dependem do corpo do artigo foram conferidas no manuscrito de março de 2023.
- Weitzman (1974) e Coase (1960): só metadados.
- A maior parte dos artigos foi conferida só no resumo (lista na Fase E). Resumo confirma o achado principal, não detalhes.
- Pereira e Cuellar (2015): resumo e trechos extraídos por ferramenta de busca; não li o artigo de ponta a ponta.
- SIDRA: as contagens foram recalculadas de respostas guardadas em 15/11; hoje o serviço devolveu desafio anti-robô, e os metadados das tabelas 1008, 6955 e 6956 não foram reabertos.
- Decreto 4.074/2002: só a alínea guardada; data do DOU não confirmada.
- Acórdão da ADI 6137 e PDF da Lei municipal 1.511/2010: lidos em rodadas anteriores, não reabertos.
- Fontes secundárias sustentam os eventos de 2010, 2011, 2012–2017 e a votação de 18/12/2018; não há fonte primária para eles.
- "Sem que a exposição sazonal tenha sido cruzada com os desfechos" (`05-metodologia.tex:295-296`): conferi que o repositório não registra tal cruzamento; ausência não se prova.
- Fase D: um buscador, uma frase por parágrafo, só cópia literal; quadros e figura fora; D2 não executado.
- Cobertura semântica do registro de afirmações não é detectável por máquina.
- O mérito do desenho (identificação, absorção dos termos da equação pelos efeitos fixos, poder) não é objeto desta verificação.

## Verification Audit Trail

- Fase A: Crossref (`api.crossref.org/works/<doi>`), 29 consultas novas em 2026-11-16; Semantic Scholar em lote (24 de 29); `export.arxiv.org` para arXiv:2207.11890; acesso direto às páginas da ALECE, da Câmara de Limoeiro do Norte, da Agência Brasil e da Globo Rural.
- Fontes novas lidas nesta rodada: resumo de Rocha e Soares (RePEc/IDEAS e Semantic Scholar); resumo de Pereira e Cuellar (OpenAlex) e trechos do SciELO; texto completo de Rigotto et al. (PDF); resumo de Brainerd e Menon (RePEc); resumo de Arkhangelsky et al. (OpenAlex); Portaria MAPA 298/2021 (DOU, por trechos); consolidação do SINASC 2011 (DATASUS, por trechos); notas do SINDAG de 17/06/2021 e 07/04/2023; catálogo e apresentação da segunda apuração do Censo Agropecuário 2006 (IBGE).
- Fase C: script sobre `censo.json` (tabela 1008) e `pam1518.json` (banana, 2015–2018); `pdfinfo` e `pdftotext` sobre `projeto.pdf`; `projeto.log`.
- Fase D: 54 consultas com frase entre aspas, resultado por script.
- Fase E: `claim_registry__*.json` (10), `coverage__*.json` (10, replay PASS), `evidence_rows.json` (114 linhas, validação PASS), `sources_manifest.json` e `sources/` (43 arquivos), todos em `docs/ars/pipeline-rodada20/evidence/`. Os artefatos das rodadas do 2.5 nessa pasta foram substituídos pelos desta rodada.
- Documentos de contexto lidos: `passport.yaml`, `passport_run_ledger.yaml` (entradas 21 a 23), `stage3prime/re_review_report.md`, `stage4/author_adjudication_and_response.md` (por busca dirigida, não de ponta a ponta); `stage3/editorial_decision.md` não foi aberto.
- Nenhum arquivo do manuscrito nem `.bib` foi alterado. Nada foi commitado.
