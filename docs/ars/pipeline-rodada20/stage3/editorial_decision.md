# Editorial Decision

Síntese editorial (Fase 2) da revisão `reviewer_full` (Schema 13.2), Estágio 3 do pipeline. O texto está em português; os títulos de seção seguem o template do plugin. Abreviações dos assentos: EIC (assento de adequação e contribuição), Met (metodologia, assento R1), Dom (domínio, assento R2), Persp (perspectiva interdisciplinar, assento R3), DA (advogado do diabo). Os rótulos `R1..R15` e `S1..S44` das tabelas de revisão são referências de transporte de itens, não assentos nem ordem de trabalho.

## Calibration Resolution

`calibration_status: NOT_CALIBRATED`

Nenhum perfil de calibração foi aplicado. As confianças de 1 a 5 são declarações de cada assento sobre a própria incerteza e não entram em nenhuma conta.

## Manuscript Information
- **Title**: Proibição da pulverização aérea de agrotóxicos no Ceará: efeitos sobre a saúde ao nascer
- **Manuscript ID**: `docs/ars/pipeline-rodada20/stage3/manuscript.md` (fonte LaTeX das seções do projeto de pesquisa, PPGEco/UFES)
- **Submission Date**: NOT PROVIDED
- **Decision Date**: 2026-11-15
- **Review Round**: Round 1
- **Tipo de documento**: projeto de pesquisa de mestrado, sem resultados. Destinatários: orientador e banca.
- **Vínculo de critérios**: `criteria_binding_unavailable`. Não há veículo confirmado, e esta carta não faz afirmação de adequação a periódico. Quatro cartões da Fase 2 trazem o marcador literal; o cartão de Persp traz a declaração em prosa ("não faço afirmação de adequação a veículo") e o marcador só no cartão da Fase 1. Registro a diferença sem corrigir o cartão.

## Review Panel Provenance (#540/#740)

- **Typed artifact**: `docs/ars/pipeline-rodada20/stage3/panel_provenance.json` (manifesto de entrada: `panel_provenance_input.json`, na mesma pasta)
- **Artifact SHA-256**: `7ebdf11aff7f3a182c050c471beafd3e35aa0888873992185e43ac0cfbefe03d`
- **Panel ID**: `rodada20-stage3-round1`
- **Normalized manifest SHA-256**: `1f190ad3650c43f6822bf8498ae85d1aab484932cd601da3b1628a49886ee695`
- **Execution topology SHA-256**: `98178cc78383458850cf91099ee8c8636d625e0a937394c78438fa0ee879370f`
- **Fresh-context scope**: `within_panel_attempt_only` (não compara tentativas nem rodadas anteriores)

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| EIC | eic | model | unknown | unknown | claude | anthropic | null |
| R1 | methodology | model | unknown | unknown | claude | anthropic | null |
| R2 | domain | model | unknown | unknown | claude | anthropic | null |
| R3 | perspective | model | unknown | unknown | claude | anthropic | null |
| DA | da | model | unknown | unknown | claude | anthropic | null |

| Provenance axis | Status (`true` / `false` / `unknown`) |
|---|---|
| Role-separated | `true` |
| Within-panel invocation-context separation | `unknown` |
| Blind to peer outputs | `unknown` |
| Model-family distinct | `false` |
| Provider distinct | `false` |
| Human-reviewer distinct | `false` |

- **Binary independence claim**: Not computed. A separação de papéis prova apenas `role_separated`; o painel não é descrito como independente.
- **Correlated-error disclosure**: All model-executed review seats used one model family; role separation does not remove correlated-error risk.

O que foi observado nesta execução, e o que ficou `unknown`:

- Os cinco assentos rodaram como subagentes separados de uma mesma sessão, com o mesmo modelo (`claude-fable-5-2`) e o mesmo provedor. Não houve revisor humano.
- Cada assento teve um contexto de invocação na Fase 1 e outro, novo, na Fase 2 (dez contextos, segundo a sessão despachante). Não há identificadores de contexto verificáveis, e por isso o campo ficou vazio e o eixo de separação de contexto saiu `unknown`, embora o relato seja de contextos distintos.
- Nenhum assento recebeu saída de outro no despacho, e todos foram instruídos a não abrir os arquivos dos pares. Isso é controle de instrução: o sistema de arquivos estava acessível. O eixo de cegueira às saídas dos pares ficou `unknown`, nem `true` nem `false`.
- A Fase 1 não foi estritamente cega ao projeto: o arquivo de instruções do repositório, que descreve o desenho, é injetado em todo agente, e um assento relatou isso.
- O assento DA relatou ter lido por acidente os Cartões 3 e 4 de configuração do painel. São cartões de configuração, não saídas de assento.
- O contrato usado (`contract.json`) difere do contrato canônico do plugin apenas no campo `generated_at`; o resumo criptográfico gravado no artefato é o do arquivo canônico, como o esquema exige.

---

## Decision *

### Major Revision

Decisão mecânica do contrato `reviewer/reviewer_full/v2`. Linhas de auditoria:

```
dimension_verdicts: [D1=warn, D2=block, D3=block, D4=warn, D5=warn, D6=warn]
fired_conditions: [F2, F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision
```

Matriz por dimensão (só assentos elegíveis; `not_assessed` fica fora do numerador e do denominador):

| Dimensão | Prioridade | Assentos elegíveis | Notas avaliadas | Veredito (pior nota) |
|---|---|---|---|---|
| D1 methodology_rigor | mandatory | Met | Met = warn | warn |
| D2 domain_accuracy | mandatory | Dom | Dom = block (repairable) | block |
| D3 argumentative_coherence | mandatory | DA, Met | DA = block (repairable); Met = warn | block |
| D4 cross_disciplinary_relevance | high | Persp | Persp = warn | warn |
| D5 writing_and_structure | normal | EIC | EIC = warn | warn |
| D6 venue_fit_and_contribution | mandatory | EIC | EIC = warn | warn |

Condições de falha:

| Condição | Severidade | Expressão (quantificador) | Avaliação | Disparou |
|---|---|---|---|---|
| F1 | 95 | any mandatory dimension has a fatal block (any) | Nenhum assento declarou bloqueio fatal; os dois bloqueios são `repairable`. | não |
| F2 | 90 | any mandatory dimension scores 'block' (any) | D2 (Dom) e D3 (DA). | sim |
| F3 | 70 | two or more mandatory dimensions score 'warn' or worse (majority) | D1 (1 de 1), D2 (1 de 1), D3 (2 de 2), D6 (1 de 1): quatro dimensões. | sim |
| F4 | 60 | any high-priority dimension scores 'block' (any) | D4 = warn. | não |
| F5 | 40 | any dimension scores 'warn' or worse (any) | Todas as seis. | sim |
| F0 | 10 | every dimension scores 'pass' (all) | Nenhuma em `pass`. | não |

Precedência: entre F2, F3 e F5, a de maior severidade é F2 (90), cuja ação é revisão maior. A tabela CRITICAL do DA está vazia, e por isso a lista de adjudicações é vazia. Nenhuma expressão ficou fora do vocabulário reconhecido. `ARS_CROSS_MODEL` não está configurado: a checagem cega de decisão por outro modelo não se aplica.

As quatro restrições permanentes do autor (15 páginas, nenhum número de estimativa próprio, só o Ensaio 1, mudança de identificação só por decisão dele) não entram nessa conta. Elas aparecem item a item no roteiro.

---

## Blocking Issues * (0–3, immutable source order)

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---------------|----------------|--------------------|-----------------|------------------------|
| R8 | Falta a literatura sobre chuva e saúde ao nascer no semiárido; sem ela, um padrão produzido pela seca pode ser lido como prova de exposição. O cartão a aponta como decisiva para o bloqueio em D2, em conjunto com R7 e R9. | Dom W2; mesmo sub-argumento em Met W4, Persp W5, DA M3 e DA M4 | `text: seção 5.3 "Um gradiente sazonal presente no primeiro e ausente no segundo mostraria que a exposição existia"` | REV-21 |
| R12 | O diagnóstico do pré-período escolhe a referência pelo mesmo contraste que o teste confirmatório mede; um gradiente achado por ruído regride no pós-lei e confirma H1 sem efeito da lei. Base do bloqueio em D3, em conjunto com R13, R14 e R15. | DA M1; Met W4 | `text: §5.3 "não consome graus de liberdade"` | REV-43 (e REV-12) |
| R13 | No cenário de voos suspensos até a lei, o parâmetro declarado não tem população e a Eq. (2) não identifica um contrafactual de retorno dos voos. | DA M2; EIC W1; Met W5; Met W9 | `text: Quadro 2 "o efeito é o de impedir a volta dos voos"; §5.1 "indica município com aplicação aérea às vésperas da lei"` | REV-44 (e REV-1, REV-13, REV-17) |

---

## Reviewer Summary

Os cartões são de contrato: trazem notas por dimensão, não recomendação de aceite ou rejeição. A coluna de recomendação registra isso em vez de inventar uma.

| Reviewer | Role | Recommendation | Confidence |
|----------|------|---------------|------------|
| Journal-Fit Reviewer (EIC) | Membro de banca generalista em avaliação de políticas públicas | n/d; D5 = warn, D6 = warn | por achado, 3 a 4 |
| Reviewer 1 (Met) | Metodologia: diferença tripla, desenhos de calendário, inferência com poucos grupos | n/d; D1 = warn, D3 = warn | por achado, 3 a 5 |
| Reviewer 2 (Dom) | Domínio: economia da saúde e do meio ambiente, literatura de agrotóxicos e saúde ao nascer | n/d; D2 = block (repairable) | por achado, 3 a 5 |
| Reviewer 3 (Persp) | Agronomia e ciência da exposição; registros da aviação agrícola | n/d; D4 = warn | por achado, 3 a 5 |
| Devil's Advocate | Fixed adversarial seat | N/A — findings only; D3 = block (repairable) | N/A — per-finding only |

`criterion_judgements` (escala `sprint_contract`, copiada dos cartões sem tradução): EIC {D5: warn, D6: warn, demais: not_assessed}; Met {D1: warn, D3: warn, demais: not_assessed}; Dom {D2: block, demais: not_assessed}; Persp {D4: warn, demais: not_assessed}; DA {D3: block, demais: not_assessed}.

Nenhum assento encontrou no manuscrito texto dirigido ao parecerista, e eu também não encontrei.

---

## Consensus Analysis *

A contagem de consenso usa os quatro assentos que não são o DA (EIC, Met, Dom, Persp). Silêncio não conta como concordância. O DA é registrado à parte. O inventário de sub-argumentos abaixo cobre os pontos em que mais de um cartão se pronuncia; os demais achados são de um só assento e aparecem no roteiro com `—` na coluna de sub-argumento.

### Points of Agreement (Consensus)

**Pontos fortes**

**[CONSENSUS-4]** O projeto diz de antemão em que condição não detecta efeito e o que entrega nesse caso, e se compromete a ler resultado sem poder como limite, não como teste. EIC S2 (Quadro 2 e cap. 8), Met S4 (regra entre teste e limite, §5.8), Dom S3 (diluição lida como limite), Persp S4 (condição em que o desenho é vazio). O DA concorda e registra que a regra não protege contra falso positivo.

**[CONSENSUS-3]** A distinção entre método e cultura, ou entre método e substância, organiza o desenho e é a pergunta certa. EIC S1, Dom S2, Persp S1. Met não trata desse ponto (elogia, em S1, o parâmetro definido sobre coortes). O DA concorda.

Corroborados por dois assentos, sem conflito: a declaração da ordem dos fatos e da rodada exploratória (EIC S5, Met S6); a separação entre fato conferido, hipótese e relato nas fontes sobre a seca (EIC S3, Persp S3); o reconhecimento do descasamento químico em relação à literatura de glifosato (Dom S4, Persp S5). De um só assento: a fidelidade das magnitudes tomadas da literatura (Dom S1, que abriu as fontes); a janela gestacional fixa (Met S2); a hipótese de identificação única e enunciada (Met S3); a seleção para o nascimento vivo tratada como desfecho (Met S5); a descrição do relatório mensal do MAPA conferida contra a norma (Persp S2); o quadro de ameaças legível (EIC S4).

**Fraquezas**

**[CONSENSUS-3]** SC-2: o contraste entre o subperíodo com voos e o subperíodo de seca não isola a exposição ao avião, porque a seca altera a sazonalidade do peso ao nascer por outras vias. Met W4 (renda, alimentação e doença), Dom W2 (água, saneamento e a literatura de Rocha e Soares), Persp W5 (retração da lavoura irrigada, emprego e área). EIC é o assento silencioso. O DA diz o mesmo em M4.

**[CONSENSUS-3]** SC-16: a classificação do município com avião vem do Censo de 2006, e o parâmetro pede aplicação aérea às vésperas da lei, sem que o texto diga qual referência vale. EIC W1, Met W7, Persp W4. Dom é o assento silencioso.

Nenhuma fraqueza reuniu os quatro assentos.

**Achados corroborados por dois assentos, sem conflito (abaixo do limiar de consenso)**

| Sub-argumento | Conteúdo | Assentos (dos quatro) | DA |
|---|---|---|---|
| SC-4 | O fim da seca é contemporâneo à lei e pode mudar o hiato sazonal de modo diferente entre os grupos; o tratamento falso com banana familiar não testa isso. | Dom W2, Met W6 | M3 |
| SC-5 | O Quadro 2 não é exaustivo: faltam voos documentados sem gradiente e gradiente sem registro. | EIC W2, Met W5 | M5 |
| SC-6 | Na linha 3 do Quadro 2, o estimando ("impedir a volta dos voos") não tem população nem contrafactual declarados, e o tratamento é definido de mais de um modo. | EIC W1, Met W5 e W9 | M2 |
| SC-7 | A entrega (i) é prometida em qualquer cenário e depende de terceiros e de um arquivo cuja existência não está assegurada. | EIC W2, Persp W2 | M6 |
| SC-8 | Estimativa sem significância no terceiro trimestre não é efeito menor; se ele importa, as coortes de referência estão parcialmente tratadas e β sai atenuado. | Met W2, Dom W1 | menor 4 |
| SC-9 | Os 80 gramas do análogo equatoriano são régua otimista para o Ceará. | Dom W1, Persp W1 | — |
| SC-10 | A escala de 150 metros é citada com mais força do que a fonte sustenta, e não combina com deriva entre municípios. | Dom W1, Persp W9 | — |
| SC-13 | Os efeitos fixos só absorvem a composição sazonal constante no tempo; a sazonalidade tem componente ambiental que varia de ano para ano. | Met W1, Dom W7 | alternativa 4 |
| SC-14 | A hipótese de que o hiato sazonal evoluiria igual nos dois grupos não tem verificação dinâmica prevista nem apoio na literatura citada. | Met W6, Dom W7 (Persp W7 é vizinho: semelhança dos grupos afirmada, não mostrada) | — |
| SC-15 | H2 é confirmatória sem especificação e com desfecho de medida frágil. | Met W3, Dom W3 | — |
| SC-17 | "Predominantemente familiar" não tem limiar nem base. | Met W7, Persp W7 | — |
| SC-19 | "Forma reduzida estadual" e a linha do GAEZ no Quadro 3 não têm referente no cap. 5. | EIC W4 e W5, Met W10 | — |
| SC-20 | O controle por arboviroses não tem fonte no Quadro 3. | EIC W4, Dom W8 | alternativa 3 |
| SC-23 | "Saúde ao nascer" e "benefício em saúde" prometem mais do que o parâmetro (peso ao nascer das coortes da estação) entrega. | EIC W1, Dom W10 | menor 5 |

**De um só assento entre os quatro, com corroboração do DA**: SC-1, a seleção do pré-período de referência pelo desfecho (Met W4; DA M1); SC-3, o subperíodo com voos é anterior a 2012 e os relatórios pedidos começam em 2012 (Met W4; DA M4); SC-12, a Eq. (2) não tem o efeito fixo de município por ano que o texto e a Figura 1 descrevem (Met W1; DA menor 1); SC-21, o critério de concordância da triangulação não é operacional (Met W10; DA menor 3); SC-24, o cronograma não tem marco nem contingência para atraso ou negativa dos pedidos (EIC W3; DA M6); SC-26, falta o canal de emprego, renda e produção (Persp W12; DA alternativa 4). SC-25, o pré-compromisso não verificável por terceiros, é de Met W11; EIC S5 e uma observação do DA registram o mesmo limite sem tratá-lo como defeito.

### Points of Disagreement

**Disagreement 1: nota de D3 (coerência argumentativa)**
- **DA view**: `block` reparável. Nenhum achado isolado é crítico; o bloqueio vem do efeito conjunto de M1 a M4 sobre um mesmo elo, o portão formado pelo diagnóstico do pré-período e pela regra de decisão.
- **Met view**: `warn`. A cadeia é em geral contínua e os descompassos (W5, W9, W10, W2) são localizados; em D1, o mesmo assento trata o condicionamento do diagnóstico (W4) como problema corrigível na redação.
- **Disagreement type**: Severity disagreement.
- **Editor's Resolution**: Não arbitrado. O contrato decide: o quantificador de F2 é `any`, e o veredito da dimensão é a pior nota avaliada. D3 fica em `block`.
- **Resolution Rationale**: O protocolo proíbe média, voto ou atenuação de condição disparada. Os dois assentos concordam no conteúdo (seleção pelo desfecho, linha 3 do Quadro 2, regra incompleta) e em que o reparo é de redação do plano, sem fonte nova e sem redesenho. A diferença é só de nota, e não muda a decisão: D2 também está em `block`.

**Disagreement 2: SC-11, severidade de o pedido ao MAPA terminar em 2018**
- **Met view** (W9, Major): sem voos observados depois de 2019, a distinção entre falha de implementação e falha de mecanismo não se sustenta; o achado vem junto com as três definições de tratamento.
- **Persp view** (W8, Minor): o relatório mensal continua obrigatório depois da lei e desde 2021 alcança drones; basta estender o pedido.
- **Disagreement type**: Severity disagreement.
- **Editor's Resolution**: O remédio é o mesmo nos dois cartões (estender o pedido a 2019–2024, para os dois estados) e não está em disputa. As severidades seguem transportadas como cada assento as deu.
- **Resolution Rationale**: A severidade Major de Met pertence ao achado inteiro, que inclui o estimando da linha 3; a parte do pedido, isolada, é a que Persp classifica como Minor. Persp é o assento com competência declarada sobre o conteúdo e a periodicidade dos relatórios (confiança 5), e Met declara não saber se os relatórios continuam a existir. A diferença não altera nenhum veredito de dimensão.

**Disagreement 3: SC-18, definir os meses da estação agora ou no plano de análise**
- **EIC view** (W5) e **Persp view** (W6): "quadra chuvosa" precisa de meses no texto do projeto; Persp acrescenta que o Cariri tem regime próprio e pede estação por macrorregião quando faltarem os relatórios.
- **Met view** (W3): os cortes numéricos, entre eles os meses da estação, podem ficar para o plano de análise, como o texto já prevê.
- **Disagreement type**: Direction disagreement (sobre o remédio, não sobre a existência do problema).
- **Editor's Resolution**: Escrever no projeto os meses como hipótese provisória declarada, com a fonte, e deixar o corte definitivo para o plano de análise. A estação por macrorregião fica como escolha do autor.
- **Resolution Rationale**: As duas posições são compatíveis nessa forma. A §5.4 já trata a quadra chuvosa como "hipótese agronômica declarada" sem dizer quais meses, e o próprio Met precisou supor quatro meses para conferir a álgebra de W2. Diferenciar a estação por região muda a definição de exposição e é decisão de identificação, reservada ao autor.

**Disagreement 4: SC-22, as afirmações de ineditismo**
- **EIC view** (W7) e DA (menor 6): três afirmações sustentam a novidade sem citação nem busca declarada; EIC remete a verificação ao assento de domínio.
- **Dom view** (S2 e W11): a lacuna alegada resistiu a uma busca não exaustiva; ao mesmo tempo, existem precedentes de restrição do método em outros países, sem avaliação ex post localizada, que o texto não menciona.
- **Disagreement type**: Existence disagreement, parcial.
- **Editor's Resolution**: A alegação de que não há avaliação ex post de proibição de método fica sustentada no conteúdo pela busca de Dom, mas o texto ainda precisa dizer em que busca se apoia (EIC W7) e registrar os precedentes (Dom W11). "Primeira proibição estadual do gênero" e registros "nunca explorados para esse fim" não foram verificadas por nenhum assento e seguem como EIC as descreveu.
- **Resolution Rationale**: Evidência primeiro. EIC aponta falta de apoio no texto, não falsidade; Dom verificou uma das três afirmações e só ela. As posições não se contradizem depois de separadas por afirmação.

**Disagreement 5: redesenho ou reparo de redação**
- **DA view** (alternativa 6 e premissa não examinada, ambas fora das tabelas de severidade): há um caminho não discutido, o de restringir o grupo tratado à Chapada com avião documentado, e uma premissa não examinada, a de que o município por mês consegue carregar a pergunta; a alternativa seria perguntar o que a lei fez aos voos.
- **EIC, Met e Dom view**: as correções não exigem alterar o desenho (EIC, avaliação de conjunto), nenhum ponto exige redesenho (Met, D1), nada invalida a pergunta ou o desenho (Dom, síntese). Persp não avalia identificação.
- **Disagreement type**: Perspective difference.
- **Editor's Resolution**: Dissenso não resolvido, deixado ao autor. Os dois pontos entram no roteiro como `consider` (REV-58 e REV-59).
- **Resolution Rationale**: O DA não classificou esses pontos como defeito e não lhes deu severidade; os três assentos falam de suficiência do desenho atual, não da comparação entre desenhos. Não há evidência nos cartões que decida entre os caminhos, e a mudança de estratégia de identificação é decisão do autor.

**Remédios diferentes para o mesmo problema, sem conflito**: para SC-8 (terceiro trimestre), Met oferece redefinir o alvo ou declarar a hipótese de exclusão, e Dom oferece pré-especificar a exposição na gestação inteira ou declarar a atenuação; os dois cardápios se sobrepõem em "declarar a atenuação", e a escolha entre os demais é de identificação. Para SC-15 (H2), Met pede a especificação e Dom oferece especificar ou rebaixar; a primeira opção de Dom é a de Met. Para SC-9 (magnitude), Dom pede o intervalo do próprio artigo e Persp pede a magnitude equatoriana como teto; as duas leituras concordam em que 80 gramas não é valor central para o Ceará.

**Alcance declarado pelos assentos, que limita o peso de alguns achados**: Dom leu só o resumo de Jones (W6) e trechos de Rocha e Soares, sem as tabelas (W2); a diferença de infraestrutura hídrica entre os grupos é conjectura do assento, a verificar. Persp leu as páginas oficiais por trechos devolvidos pela busca, não por abertura direta, e a repartição do Censo de 2006 por mesorregião vem de fonte secundária (W4). Met citou de memória a condição de Canay, Santos e Shaikh (W8) e a referência a Roth (W4), ambas marcadas como a conferir. O DA não conferiu a referência a Roth nem as magnitudes da literatura.

---

## Decision Rationale *

A decisão é revisão maior porque duas dimensões obrigatórias receberam `block` reparável, e o contrato manda aplicar a condição disparada de maior severidade (F2). Em D2, Dom mostra que falta a literatura sobre chuva e desfechos ao nascer no semiárido (W2) e que o uso do análogo equatoriano e a hipótese sobre óbito fetal vão além das fontes (W1, W3). Em D3, o DA mostra que o portão formado pelo diagnóstico do pré-período e pela regra de decisão não se sustenta como escrito (M1 a M4). Os dois bloqueios convergem no mesmo trecho do projeto, a §5.3 e o Quadro 2, e três dos quatro assentos de nota dizem, por caminhos diferentes, que o contraste entre os subperíodos não isola a exposição (SC-2).

Não é rejeição: nenhum assento declarou bloqueio fatal, a tabela CRITICAL do DA está vazia, e Dom e DA classificam seus bloqueios como reparáveis por redação, sem fonte nova. Não é revisão menor: o contrato não permite atenuar F2, e a nota `warn` de Met em D3 não desfaz o `block` do DA na mesma dimensão (Disagreement 1).

As divergências não alteram a decisão. Duas são de severidade, uma é de remédio e foi conciliada, uma se resolve separando as afirmações, e uma fica como dissenso deixado ao autor.

O que pesa a favor do projeto é consenso dos quatro assentos: ele declara de antemão o cenário sem estimativa de efeito e a regra para ler resultado sem poder. É esse dispositivo que os achados pedem para completar, não para substituir.

Há um ponto que os cartões não resolvem. Cada assento afirma que suas correções cabem no formato (EIC: poucas frases; Met: cerca de uma página; Dom: cabe nas 15 páginas; Persp: dentro de 15 páginas). Nenhum deles viu as correções dos outros, e o texto já está em 15 páginas. Somados, os remédios não cabem sem cortes, e nenhum cartão indica o que cortar.

---

## Required Revisions * (Must Fix)

Regra de obrigação usada, independente da severidade transportada: `must_fix` é o achado numerado que o próprio assento aponta como base de um `block` em dimensão obrigatória (Dom W1 a W3; DA M1 a M4) ou o achado numerado de outro assento que contém o mesmo sub-argumento, porque o bloqueio não se levanta sem ele. `should_fix` é o achado restante de severidade Major e o achado Minor que o assento aponta como base de um `warn` em dimensão obrigatória. `consider` é o restante. A obrigação é uma porta editorial, não uma ordem de trabalho; a ordem das linhas é a da fonte (EIC, Met, Dom, Persp, DA; depois a ordem do cartão).

| Transport ref | Roadmap ID | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source Reviewer | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | REV-1 | População, contraste e desfecho da pergunta mudam entre os capítulos 1, 4, 5 e 8 | SC-6, SC-16, SC-23 | major | `text: seção 5.1 "sobre coortes expostas, e não sobre municípios"` | 4 | EIC W1 | must_fix | sentence: cap. 1, cap. 4, §5.1, Quadro 2, cap. 8 | interpretive_ambiguity_remains → claim: pergunta e parâmetro-alvo |
| R2 | REV-10 | O β da Eq. (2) não é o ATT da Eq. (1) sem hipóteses não escritas | SC-8 | major | `equation: Eq. (1), condicionamento em S_t = 1, frente a P_t em [0,1] na Eq. (2)` | 4 | Met W2 | must_fix | sentence: §5.1 e §5.2 | interpretive_ambiguity_remains → claim: β como ATT |
| R3 | REV-11 | Componentes do desenho principal descritos no texto e ausentes da especificação | SC-15, SC-18 | major | `absence: §5.2 e cap. 4 — esperada especificação da interação por chuva, do terceiro trimestre, de H2 e de H4; conferidos §5.2, §5.3, §5.5, §5.8, cap. 4, cap. 6 e Quadro 2` | 4 | Met W3 | must_fix | section: quadro de especificações no cap. 5 | method_reproducibility_unresolved → section: cap. 5 |
| R4 | REV-12 | O diagnóstico de abertura condiciona a análise confirmatória no desfecho do pré-período | SC-1, SC-2, SC-3 | major | `text: §5.3 "não consome graus de liberdade da análise confirmatória"` | 4 | Met W4 | must_fix | sentence: §5.3 | acceptance_criterion_unmet → claim: taxa de erro do teste confirmatório |
| R5 | REV-13 | Quadro 2 não cobre o resultado que o próprio texto torna mais provável | SC-5, SC-6 | major | `table: Quadro 2 — quatro linhas, sem a combinação de voos documentados com ausência de gradiente sazonal no pré-período` | 5 | Met W5 | must_fix | section: Quadro 2 | interpretive_ambiguity_remains → table: Quadro 2 |
| R6 | REV-17 | Três definições de tratamento, e nenhuma fonte mede voos depois da lei | SC-6, SC-11 | major | `text: §5.5 "O tratamento é definido como cessação efetiva de voos e medido como tal"` | 4 | Met W9 | must_fix | sentence: §5.4, §5.5, Quadro 2 | interpretive_ambiguity_remains → claim: definição do tratamento |
| R7 | REV-20 | Leitura de Calzada et al. além do que o artigo sustenta em trimestre, magnitude e distância | SC-8, SC-9, SC-10 | major | `text: seção 5.2 "O terceiro trimestre, para o qual o análogo equatoriano encontra estimativa sem significância estatística, serve de contraste de efeito menor."` | 4 | Dom W1 | must_fix | sentence: §3.2, §5.2, cap. 4, cap. 7 | claim_scope_unsupported → claim: uso do análogo equatoriano |
| R8 | REV-21 | Falta a literatura sobre chuva e saúde ao nascer no semiárido, que muda a leitura do diagnóstico, de H3 e do desenho principal | SC-2, SC-4 | major | `text: seção 5.3 "Um gradiente sazonal presente no primeiro e ausente no segundo mostraria que a exposição existia"` | 4 | Dom W2 | must_fix | section: §3.2, §5.3, Quadro 4 | evidence_gap_remains → claim: leitura do diagnóstico e hipótese de identificação |
| R9 | REV-22 | H2 (óbito fetal) com pouco apoio na literatura citada e problema de medida | SC-15 | major | `text: cap. 6, Desfechos "Do SIM obtém-se a taxa de óbito fetal, segundo desfecho confirmatório"` | 4 | Dom W3 | must_fix | section: cap. 4 e cap. 6 | claim_scope_unsupported → claim: H2 confirmatória |
| R10 | REV-31 | A doença não é nomeada e o regime de aplicação é tomado do Equador | SC-9 | major | `text: seção 1.1 "mesma cultura, mesmo método, mesma classe de produto"` | 4 | Persp W1 | must_fix | sentence: §1.1, §2.2, §5.8 | claim_scope_unsupported → claim: análogo equatoriano |
| R11 | REV-35 | A seca é lida só como falta de umidade para o fungo, e também encolheu a lavoura irrigada | SC-2 | major | `text: seção 5.3 "mostraria que a exposição existia"` | 3 | Persp W5 | must_fix | sentence: §5.3 e Quadro 4 | evidence_gap_remains → claim: leitura do diagnóstico |
| R12 | REV-43 | O diagnóstico condiciona o teste confirmatório ao contraste que ele mesmo mede | SC-1 | major | `text: §5.3 "não consome graus de liberdade"` | 4 | DA M1 | must_fix | sentence: §5.3 | acceptance_criterion_unmet → claim: taxa de erro do teste confirmatório |
| R13 | REV-44 | No cenário de voos suspensos, o parâmetro declarado não tem população e a Eq. (2) não identifica um contrafactual de retorno | SC-6 | major | `text: Quadro 2 "o efeito é o de impedir a volta dos voos"; §5.1 "indica município com aplicação aérea às vésperas da lei"` | 4 | DA M2 | must_fix | sentence: Quadro 2 e §5.1 | interpretive_ambiguity_remains → table: Quadro 2 |
| R14 | REV-45 | O pós-lei confunde a lei com o fim da seca, e a interação por chuva não os separa | SC-4 | major | `text: cap. 7 "teria mordido apenas quando a chuva e a doença voltaram"` | 3 | DA M3 | must_fix | sentence: cap. 7 e §5.2 | evidence_gap_remains → claim: hipótese de identificação |
| R15 | REV-46 | O padrão dos dois subperíodos não discrimina exposição de seca, e o subperíodo com voos só tem o Censo de 2006 | SC-2, SC-3 | major | `text: §5.3 "mostraria que a exposição existia"; §5.4 "de 2012 a 2018"` | 4 | DA M4 | must_fix | sentence: §5.3 | claim_scope_unsupported → claim: leitura do diagnóstico |

A coluna `Sub-Claim(s)` traz os identificadores do inventário acima; `—` indica achado de um só assento, não decomposto.

### Required Item Details

**R1: População, contraste e desfecho da pergunta mudam entre os capítulos 1, 4, 5 e 8** (REV-1)
- **Problem**: População, contraste e desfecho da pergunta mudam entre os capítulos 1, 4, 5 e 8. Localização: cap. 1; cap. 4; §5.1; Quadro 2 (linha 3); cap. 8.
- **Source**: EIC W1, severidade major, confiança 4; âncora `text: seção 5.1 "sobre coortes expostas, e não sobre municípios"`. Alcance da obrigação: A parte que sustenta o bloqueio é a linha 3 do Quadro 2 (SC-6); o restante do achado tem o mesmo remédio.
- **Requirement**: Adotar uma só formulação e repeti-la nos quatro lugares; fixar em uma frase o período de referência de A_m e o que vale no cenário de voos suspensos; dizer no cap. 1 que "saúde ao nascer" são dois desfechos confirmatórios.
- **Author constraints touched**: (a) frases; (d) a definição de A_m e do estimando no cenário 3
- **Acceptance criteria**: A pergunta do cap. 1, o objetivo geral do cap. 4, a §5.1 e o cap. 8 trazem a mesma população, o mesmo contraste e os mesmos desfechos, e a linha 3 do Quadro 2 diz qual é o conjunto A_m nesse cenário.

**R2: O β da Eq. (2) não é o ATT da Eq. (1) sem hipóteses não escritas** (REV-10)
- **Problem**: O β da Eq. (2) não é o ATT da Eq. (1) sem hipóteses não escritas. Localização: §5.1; §5.2.
- **Source**: Met W2, severidade major, confiança 4; âncora `equation: Eq. (1), condicionamento em S_t = 1, frente a P_t em [0,1] na Eq. (2)`. Alcance da obrigação: A parte que sustenta o bloqueio é o terceiro trimestre como referência (SC-8).
- **Requirement**: Redefinir S_t pelos dois primeiros trimestres ou reescrever o alvo como diferença entre exposição precoce e tardia; declarar a hipótese de exclusão e o sentido do viés; informar o suporte de P_t.
- **Author constraints touched**: (a) frases; (d) redefinição do estimando
- **Acceptance criteria**: A Eq. (1) e a Eq. (2) definem a mesma subpopulação de coortes, e o texto traz a hipótese de exclusão sobre as coortes de referência, com o sentido do viés se ela falhar.

**R3: Componentes do desenho principal descritos no texto e ausentes da especificação** (REV-11)
- **Problem**: Componentes do desenho principal descritos no texto e ausentes da especificação. Localização: §5.2; cap. 4; cap. 6.
- **Source**: Met W3, severidade major, confiança 4; âncora `absence: §5.2 e cap. 4 — esperada especificação da interação por chuva, do terceiro trimestre, de H2 e de H4; conferidos §5.2, §5.3, §5.5, §5.8, cap. 4, cap. 6 e Quadro 2`. Alcance da obrigação: A parte que sustenta o bloqueio é a especificação de H2 (SC-15); chuva, terceiro trimestre e H4 seguem o mesmo quadro.
- **Requirement**: Quadro de meia página com uma linha por hipótese (desfecho, amostra, coeficiente, ponderação, estatuto) e Eq. (2) estendida com os termos de chuva; cortes numéricos podem ficar para o plano.
- **Author constraints touched**: (a) bloco de meia página; (d) especificação
- **Acceptance criteria**: Existe especificação escrita para H2 (desfecho, denominador, amostra, ponderação) e, na extensão que o autor adotar, para a interação por chuva, o terceiro trimestre e H4.

**R4: O diagnóstico de abertura condiciona a análise confirmatória no desfecho do pré-período** (REV-12)
- **Problem**: O diagnóstico de abertura condiciona a análise confirmatória no desfecho do pré-período. Localização: §5.3; Quadro 2.
- **Source**: Met W4, severidade major, confiança 4; âncora `text: §5.3 "não consome graus de liberdade da análise confirmatória"`. Alcance da obrigação: Achado inteiro.
- **Requirement**: Escolher e escrever uma saída: referência fixada sem usar o desfecho; amostras separadas; ou distribuição de referência do procedimento inteiro em placebos. Definir "gradiente" e retirar a frase.
- **Author constraints touched**: (a) frases; (d) regra de escolha do pré-período
- **Acceptance criteria**: A §5.3 diz por qual critério o pré-período de referência é escolhido sem usar o contraste testado, ou como a distribuição de referência incorpora a seleção; "gradiente" está definido; a frase sobre graus de liberdade saiu.

**R5: Quadro 2 não cobre o resultado que o próprio texto torna mais provável** (REV-13)
- **Problem**: Quadro 2 não cobre o resultado que o próprio texto torna mais provável. Localização: §5.7 (Quadro 2).
- **Source**: Met W5, severidade major, confiança 5; âncora `table: Quadro 2 — quatro linhas, sem a combinação de voos documentados com ausência de gradiente sazonal no pré-período`. Alcance da obrigação: A parte que sustenta o bloqueio é a linha 3 do Quadro 2 (SC-6); a cobertura das células ausentes (SC-5) é a mesma de DA M5.
- **Requirement**: Reescrever o quadro como cruzamento de medição e diagnóstico, uma ação por célula, com os critérios definidos em uma linha cada.
- **Author constraints touched**: (a) bloco; (d) regra de decisão
- **Acceptance criteria**: O Quadro 2 diz o estimando e o contrafactual do cenário de voos suspensos e tem critérios observáveis para cada linha.

**R6: Três definições de tratamento, e nenhuma fonte mede voos depois da lei** (REV-17)
- **Problem**: Três definições de tratamento, e nenhuma fonte mede voos depois da lei. Localização: §5.1; §5.5; Quadro 2 (linha 3); Quadro 4.
- **Source**: Met W9, severidade major, confiança 4; âncora `text: §5.5 "O tratamento é definido como cessação efetiva de voos e medido como tal"`. Alcance da obrigação: A parte que sustenta o bloqueio é o estimando da linha 3 (SC-6); a extensão do pedido ao MAPA é SC-11.
- **Requirement**: Declarar a intenção de tratar como estimando da Eq. (2) e a cessação efetiva como medida de cumprimento; estender o pedido de relatórios a 2019–2024 (CE e RN); dizer o contrafactual da linha 3 do Quadro 2.
- **Author constraints touched**: (a) frases; (d) declaração do estimando
- **Acceptance criteria**: O texto usa uma só definição de tratamento para a Eq. (2) e diz o contrafactual da linha 3 do Quadro 2.

**R7: Leitura de Calzada et al. além do que o artigo sustenta em trimestre, magnitude e distância** (REV-20)
- **Problem**: Leitura de Calzada et al. além do que o artigo sustenta em trimestre, magnitude e distância. Localização: §3.2; §5.2; cap. 4 (H3); cap. 7.
- **Source**: Dom W1, severidade major, confiança 4; âncora `text: seção 5.2 "O terceiro trimestre, para o qual o análogo equatoriano encontra estimativa sem significância estatística, serve de contraste de efeito menor."`. Alcance da obrigação: Achado inteiro (base declarada do bloqueio em D2, em conjunto com W2 e W3).
- **Requirement**: Tratar o terceiro trimestre como pergunta (pré-especificar a exposição na gestação inteira ao lado da de dois trimestres e dizer a principal, ou manter e declarar a atenuação); parte de H3 sobre o trimestre como exploratória; no poder, usar o intervalo do próprio artigo e dizer que mede intensificação sazonal; trocar "apenas a até 150 metros".
- **Author constraints touched**: (a) frases; (d) definição de P_t e estatuto de H3
- **Acceptance criteria**: O terceiro trimestre deixa de ser premissa, ou a atenuação esperada está declarada; o cálculo de poder cita o intervalo do artigo e o que ele mede; "apenas" sai da frase dos 150 metros.

**R8: Falta a literatura sobre chuva e saúde ao nascer no semiárido, que muda a leitura do diagnóstico, de H3 e do desenho principal** (REV-21)
- **Problem**: Falta a literatura sobre chuva e saúde ao nascer no semiárido, que muda a leitura do diagnóstico, de H3 e do desenho principal. Localização: §3.2; §5.3; cap. 7 (Quadro 4); H3.
- **Source**: Dom W2, severidade major, confiança 4; âncora `text: seção 5.3 "Um gradiente sazonal presente no primeiro e ausente no segundo mostraria que a exposição existia"`. Alcance da obrigação: Achado inteiro (o cartão o aponta como decisivo para o bloqueio em D2).
- **Requirement**: Citar Rocha e Soares (2015) em 3.2 e no cap. 7; pré-especificar a chuva na gestação como controle, interagida com o grupo e com a cobertura de água e saneamento; reescrever o parágrafo do diagnóstico (compatível com exposição, não demonstração) com um contraste que separe as leituras; linha "fim da seca contemporâneo à lei" no Quadro 4.
- **Author constraints touched**: (a) bloco; (d) chuva como controle interagido
- **Acceptance criteria**: Rocha e Soares (2015) está citado e enfrentado; o parágrafo do diagnóstico não afirma demonstração; o Quadro 4 tem a linha do fim da seca com uma resposta do desenho.

**R9: H2 (óbito fetal) com pouco apoio na literatura citada e problema de medida** (REV-22)
- **Problem**: H2 (óbito fetal) com pouco apoio na literatura citada e problema de medida. Localização: cap. 4 (H2); cap. 6.
- **Source**: Dom W3, severidade major, confiança 4; âncora `text: cap. 6, Desfechos "Do SIM obtém-se a taxa de óbito fetal, segundo desfecho confirmatório"`. Alcance da obrigação: Achado inteiro (base declarada do bloqueio em D2, em conjunto com W1 e W2).
- **Requirement**: Uma de duas: manter H2 confirmatória com justificativa, definição da taxa e do desfecho composto, janela de registro comparável e efeito mínimo detectável antes; ou rebaixá-la e usar nascidos vivos por coorte de concepção e razão de sexo como teste de seleção. Dizer que perdas precoces não são observadas.
- **Author constraints touched**: (a) frases; (d) estatuto de H2; (b) só se o efeito mínimo detectável for posto no projeto
- **Acceptance criteria**: H2 está justificada e especificada como confirmatória, ou foi rebaixada com o teste de seleção substituto; o texto diz que perdas precoces não são observadas.

**R10: A doença não é nomeada e o regime de aplicação é tomado do Equador** (REV-31)
- **Problem**: A doença não é nomeada e o regime de aplicação é tomado do Equador. Localização: §1.1; §2.2; §5.8.
- **Source**: Persp W1, severidade major, confiança 4; âncora `text: seção 1.1 "mesma cultura, mesmo método, mesma classe de produto"`. Alcance da obrigação: A parte que sustenta o bloqueio é o uso da magnitude equatoriana (SC-9); nomear a doença é do mesmo achado.
- **Requirement**: Nomear a doença e dizer que o Ceará é área livre de sigatoka-negra; trocar a identidade com o Equador por semelhança com diferença declarada de patógeno e frequência; apoiar a hipótese de estação em fontes locais; usar a magnitude equatoriana como teto.
- **Author constraints touched**: (a) frases
- **Acceptance criteria**: A comparação de poder não toma 80 gramas como valor central para o Ceará, e o texto declara a diferença de patógeno e de frequência em relação ao Equador.

**R11: A seca é lida só como falta de umidade para o fungo, e também encolheu a lavoura irrigada** (REV-35)
- **Problem**: A seca é lida só como falta de umidade para o fungo, e também encolheu a lavoura irrigada. Localização: §5.3; §5.6; Quadro 4.
- **Source**: Persp W5, severidade major, confiança 3; âncora `text: seção 5.3 "mostraria que a exposição existia"`. Alcance da obrigação: Achado inteiro (mesmo sub-argumento de Dom W2 e DA M4, SC-2).
- **Requirement**: Acrescentar ao diagnóstico as séries de área colhida de banana irrigada e de área irrigada; dizer que a leitura de exposição só se sustenta se os relatórios mostrarem a queda dos voos; listar a retração da lavoura no Quadro 4.
- **Author constraints touched**: (a) frases
- **Acceptance criteria**: O diagnóstico considera a retração da lavoura irrigada como explicação concorrente e condiciona a leitura de exposição aos registros de voo.

**R12: O diagnóstico condiciona o teste confirmatório ao contraste que ele mesmo mede** (REV-43)
- **Problem**: O diagnóstico condiciona o teste confirmatório ao contraste que ele mesmo mede. Localização: §5.3; Quadro 2.
- **Source**: DA M1, severidade major, confiança 4; âncora `text: §5.3 "não consome graus de liberdade"`. Alcance da obrigação: Achado inteiro (base declarada do bloqueio em D3).
- **Requirement**: Separar os anos usados para decidir dos usados como referência, ou fixar a referência antes de olhar o gradiente.
- **Author constraints touched**: (d) regra de escolha do pré-período
- **Acceptance criteria**: Mesmo critério de Met W4: a escolha da referência não usa o contraste testado, ou a inferência incorpora a seleção.

**R13: No cenário de voos suspensos, o parâmetro declarado não tem população e a Eq. (2) não identifica um contrafactual de retorno** (REV-44)
- **Problem**: No cenário de voos suspensos, o parâmetro declarado não tem população e a Eq. (2) não identifica um contrafactual de retorno. Localização: Quadro 2 (linha 3); §5.1; §5.5.
- **Source**: DA M2, severidade major, confiança 4; âncora `text: Quadro 2 "o efeito é o de impedir a volta dos voos"; §5.1 "indica município com aplicação aérea às vésperas da lei"`. Alcance da obrigação: Achado inteiro (base declarada do bloqueio em D3).
- **Requirement**: Dizer o estimando, o pré-período e a hipótese desse cenário.
- **Author constraints touched**: (a) frases; (d) estimando do cenário 3
- **Acceptance criteria**: O cenário de voos suspensos tem estimando, população, pré-período e hipótese de identificação escritos.

**R14: O pós-lei confunde a lei com o fim da seca, e a interação por chuva não os separa** (REV-45)
- **Problem**: O pós-lei confunde a lei com o fim da seca, e a interação por chuva não os separa. Localização: cap. 7; §5.2; Quadro 4.
- **Source**: DA M3, severidade major, confiança 3; âncora `text: cap. 7 "teria mordido apenas quando a chuva e a doença voltaram"`. Alcance da obrigação: Achado inteiro (base declarada do bloqueio em D3).
- **Requirement**: Examinar a resposta diferencial à chuva entre municípios irrigados e de comparação; o cartão indica reparo possível com os anos anteriores a 2012 do painel.
- **Author constraints touched**: (a) frases; (d) acréscimo de verificação ao desenho
- **Acceptance criteria**: O texto diz como o desenho separa a lei do fim da seca, ou declara que não separa e o que isso faz à leitura de β.

**R15: O padrão dos dois subperíodos não discrimina exposição de seca, e o subperíodo com voos só tem o Censo de 2006** (REV-46)
- **Problem**: O padrão dos dois subperíodos não discrimina exposição de seca, e o subperíodo com voos só tem o Censo de 2006. Localização: §5.3; §5.4.
- **Source**: DA M4, severidade major, confiança 4; âncora `text: §5.3 "mostraria que a exposição existia"; §5.4 "de 2012 a 2018"`. Alcance da obrigação: Achado inteiro (base declarada do bloqueio em D3).
- **Requirement**: Deixar de ler o contraste como prova de exposição e dizer que medida de voo existe para cada subperíodo.
- **Author constraints touched**: —
- **Acceptance criteria**: A §5.3 não apresenta o contraste entre subperíodos como prova de exposição e diz que medida de voo cobre cada subperíodo.


---

## Suggested Revisions (Should Fix)

| Transport ref | Roadmap ID | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source Reviewer | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | REV-2 | Contribuição enunciada sem condicional; entrega (i) prometida em qualquer cenário embora dependa de terceiros | SC-5, SC-7 | major | `text: cap. 8 "O projeto entrega, em qualquer dos cenários do"` | 4 | EIC W2 | should_fix | sentence: §1.3, Quadro 2, cap. 8 | claim_scope_unsupported → claim: entrega (i) e três camadas |
| S2 | REV-3 | Cronograma não mostra dependências nem prioridades | SC-24 | major | `table: Quadro 5 (Cronograma de atividades, por bimestre), linhas 1 a 9, cap. 8` | 3 | EIC W3 | should_fix | section: Quadro 5 e parágrafo do cronograma | reporting_requirement_unmet → table: Quadro 5 |
| S3 | REV-4 | Elos ausentes entre objetivos, análises, fontes e atividades | SC-19, SC-20 | minor | `text: cap. 6 "A unidade de análise é o município por mês de nascimento, para os 184"` | 4 | EIC W4 | consider | section: Quadro 3 e cap. 5 | reader_traceability_reduced → table: Quadro 3 |
| S4 | REV-5 | Termos de trabalho usados antes de definidos ou nunca definidos | SC-18, SC-19 | minor | `text: cap. 4 "confrontar essa estimativa com a forma reduzida estadual, o controle"` | 4 | EIC W5 | consider | sentence: primeiras ocorrências | reader_traceability_reduced → manuscript: termos de trabalho |
| S5 | REV-6 | Sem resumo e sem seção de recursos (a confirmar contra as normas do programa) | — | minor | `absence: elementos pré-textuais e capítulos — esperado resumo com palavras-chave e seção de recursos; conferidos capa, folha de rosto, sumário e caps. 1 a 8` | 3 | EIC W6 | consider | section: resumo | editorial_conformance_unmet → manuscript: elementos pré-textuais |
| S6 | REV-7 | Afirmações de ineditismo sem apoio | SC-22 | minor | `text: cap. 1 "prática em todo o território, na primeira proibição estadual do gênero no"` | 3 | EIC W7 | should_fix | sentence: cap. 1 e §1.3 | claim_scope_unsupported → claim: ineditismo |
| S7 | REV-8 | Estatuto do desenho principal fica em aberto | — | minor | `text: seção 5.8 "desfechos do pós-lei, e a escolha do desenho principal é ratificada com o"` | 3 | EIC W8 | consider | sentence: §5.8 | interpretive_ambiguity_remains → section: §5.8 |
| S8 | REV-9 | Eq. (2) não contém o efeito fixo que o texto e a Figura 1 dizem absorver os choques município-ano | SC-12, SC-13 | major | `equation: Eq. (2), termos alpha_{m,s(t)} e gamma_t, sem efeito fixo de município por ano` | 5 | Met W1 | should_fix | sentence: §5.2, Figura 1, Quadro 4 | method_reproducibility_unresolved → section: Eq. (2) |
| S9 | REV-14 | Sem verificação dinâmica planejada da hipótese de identificação | SC-4, SC-14 | major | `absence: §5.2, §5.3 e Quadro 4 — esperado estudo de evento ou placebo no tempo para o hiato sazonal relativo; conferidos §5.2, §5.3, §5.6, §5.8, Quadros 2 e 4` | 4 | Met W6 | should_fix | sentence: §5.2 ou §5.8 | evidence_gap_remains → claim: hipótese de identificação |
| S10 | REV-15 | Definição operacional do grupo de comparação e de A_m incompleta | SC-16, SC-17 | minor | `text: §5.2 "em que a cultura é predominantemente familiar"` | 4 | Met W7 | consider | sentence: §5.2 | method_reproducibility_unresolved → section: §5.2 |
| S11 | REV-16 | Cinco procedimentos de inferência sem designação do primário | — | major | `text: §5.8 "na diferença tripla, em que a variação é interna ao município, aplica-se também"` | 3 | Met W8 | should_fix | sentence: §5.8 | method_reproducibility_unresolved → section: §5.8 |
| S12 | REV-18 | Forma reduzida e triangulação com hipóteses e critério de concordância por escrever | SC-19, SC-21 | minor | `equation: Eq. (3), theta = VPP x ATT, apresentada para uma análise de dose contínua` | 3 | Met W10 | should_fix | sentence: §5.6 | interpretive_ambiguity_remains → section: §5.6 |
| S13 | REV-19 | Pré-compromisso declarado, mas não verificável por terceiros | SC-25 | minor | `text: §5.8 "São planos versionados em repositório, não pré-registro público"` | 4 | Met W11 | consider | other (registro_externo): plano de análise | reader_traceability_reduced → claim: pré-compromisso |
| S14 | REV-23 | Rigotto et al. citado na seção de saúde ao nascer por um resultado que é de neoplasias | — | minor | `text: seção 3.2 "documentam piores indicadores de saúde nos primeiros, em estudo ecológico, sem pretensão causal"` | 5 | Dom W4 | consider | sentence: §3.2 | claim_scope_unsupported → claim: citação de Rigotto et al. |
| S15 | REV-24 | Reynier e Rubin não replicam a lógica de Dias, Rocha e Soares | — | minor | `text: cap. 1, Antecedentes "replicam a lógica nos Estados Unidos, com aptidão agroclimática como fonte de variação"` | 5 | Dom W5 | consider | sentence: §1.1 | claim_scope_unsupported → claim: citação de Reynier e Rubin |
| S16 | REV-25 | Jones (2020) não isola fungicidas (lido só o resumo) | — | minor | `text: seção 3.2 "entre os poucos estudos que isolam fungicidas está o de"` | 3 | Dom W6 | consider | sentence: §3.2 | claim_scope_unsupported → claim: citação de Jones |
| S17 | REV-26 | Ameaça de sazonalidade reduzida à composição materna; comparabilidade sazonal dos grupos sem base na literatura citada | SC-13, SC-14 | minor | `text: seção 3.2 "A ameaça conhecida é a composição sazonal das mães"` | 4 | Dom W7 | consider | sentence: §3.2 e cap. 7 | claim_scope_unsupported → claim: ameaça de sazonalidade |
| S18 | REV-27 | Nada sobre a comparabilidade de SINASC e SIM entre 2005 e 2024 | SC-20 | minor | `absence: cap. 6 e Quadro 3 — esperada nota sobre a troca de formulários de 2011, a regra de residência e a fonte das arboviroses; conferidos caps. 5, 6 e 7, Quadros 3 e 4` | 4 | Dom W8 | consider | section: cap. 6 | reporting_requirement_unmet → section: cap. 6 |
| S19 | REV-28 | Intoxicações intencionais não são placebo limpo, e a premissa vem sem referência | — | minor | `text: cap. 6, Desfechos "as intoxicações intencionais, que respondem à disponibilidade do produto e não ao método de aplicação, servem de placebo"` | 3 | Dom W9 | consider | sentence: cap. 6 | claim_scope_unsupported → claim: placebo |
| S20 | REV-29 | O que o primeiro ensaio entrega ao segundo é menos do que as frases de ligação prometem | SC-23 | minor | `text: seção 3.1 "saber se a proibição produziu o benefício em saúde que a motivou"` | 3 | Dom W10 | consider | sentence: §3.1 e cap. 8 | claim_scope_unsupported → claim: insumo do segundo ensaio |
| S21 | REV-30 | Precedentes de restrição do método ficam fora do texto | SC-22 | minor | `absence: cap. 1 (Antecedentes) e seção 3.1 — esperada menção a restrições de método já adotadas em outros países; conferidos caps. 1, 2 e 3` | 3 | Dom W11 | consider | sentence: §1.1 | evidence_gap_remains → section: §1.1 |
| S22 | REV-32 | Medida municipal e mensal prometida em qualquer cenário, sem dizer onde os registros estão nem se sobreviveram | SC-7 | major | `text: cap. 8 "a primeira medida municipal e mensal da aplicação"` | 4 | Persp W2 | should_fix | sentence: cap. 8, §5.4, Quadro 3 | claim_scope_unsupported → claim: entrega (i) |
| S23 | REV-33 | Receituário atribuído a órgão que, pelo decreto, não o guarda | — | minor | `table: Quadro 3 (Fontes de dados), linha "Receituário (ADAGRI)", coluna Acesso` | 4 | Persp W3 | consider | sentence: §5.4 e Quadro 3 | evidence_gap_remains → dataset: receituário agronômico |
| S24 | REV-34 | Classificação provisória pelo Censo de 2006 pode apontar para a região errada em 2018 | SC-16 | major | `dataset: Censo Agropecuário 2006 (tabela SIDRA 1008) — quesito de equipamento de aplicação sem recorte por cultura, usado como classificação provisória` | 3 | Persp W4 | should_fix | sentence: §5.4 | interpretive_ambiguity_remains → dataset: Censo Agropecuário 2006 |
| S25 | REV-36 | Uma só quadra chuvosa para o estado, sem meses, sem definição de ano chuvoso nem de chuva municipal | SC-18 | minor | `text: seção 5.2 "da quadra chuvosa modifica o efeito"` | 4 | Persp W6 | consider | sentence: §5.2 e §5.4 | method_reproducibility_unresolved → section: §5.2 |
| S26 | REV-37 | Semelhança entre banana familiar e empresarial afirmada, não mostrada | SC-14, SC-17 | minor | `text: seção 5.2 "têm a cultura, o clima e o"` | 3 | Persp W7 | consider | section: §5.2 | claim_scope_unsupported → claim: comparabilidade dos grupos |
| S27 | REV-38 | Tratamento definido como cessação efetiva, e o pedido de registros termina em 2018 | SC-11 | minor | `text: seção 5.4 "de 2012 a 2018, para o Ceará e o Rio Grande do Norte"` | 5 | Persp W8 | consider | sentence: §5.4 | evidence_gap_remains → dataset: relatórios mensais do MAPA |
| S28 | REV-39 | Escala atribuída à deriva não combina com a definição de vizinhos imediatos | SC-10 | minor | `text: seção 5.5 "sobre municípios vizinhos e o aquífero compartilhado, que melhorariam os"` | 4 | Persp W9 | consider | sentence: §5.5 | claim_scope_unsupported → claim: canal de deriva |
| S29 | REV-40 | Há fonte pública que mede a fração de domicílios perto dos bananais | — | minor | `text: cap. 7 "nenhuma fonte disponível o resolve"` | 4 | Persp W10 | consider | sentence: cap. 7 | evidence_gap_remains → claim: fração exposta |
| S30 | REV-41 | Registros pedidos por acesso à informação identificam empresas e profissionais | — | minor | `text: cap. 6 "de acesso público, sem identificação individual"` | 3 | Persp W11 | consider | sentence: cap. 6 | editorial_conformance_unmet → section: Aspectos éticos |
| S31 | REV-42 | Diagrama não tem o canal de emprego e produção | SC-26 | minor | `figure: Figura 1 (diagrama causal) — entre o nó Lei × estação e o nó Saúde fetal há só as vias voo e aplicação terrestre` | 3 | Persp W12 | consider | sentence: Figura 1 e Quadro 4 | interpretive_ambiguity_remains → figure: Figura 1 |
| S32 | REV-47 | Regra de decisão com quatro linhas para um espaço de pelo menos três eixos | SC-5 | major | `table: Quadro 2 (Regra de decisão), as quatro linhas` | 4 | DA M5 | should_fix | section: Quadro 2 | interpretive_ambiguity_remains → table: Quadro 2 |
| S33 | REV-48 | Promessa da medida além dos meios, sem contingência no cronograma | SC-7, SC-24 | major | `text: cap. 8 "em qualquer dos cenários"; §5.4 "Sem esses registros, a estação é tomada da quadra chuvosa"` | 4 | DA M6 | should_fix | sentence: cap. 8 e Quadro 5 | claim_scope_unsupported → claim: entrega (i) |
| S34 | REV-49 | Texto e Figura 1 dizem que os efeitos fixos absorvem choques município-ano que não constam da Eq. (2) | SC-12 | minor | `equation: Eq. (2) e Figura 1 [ANCHOR: prosa do cartão, sem âncora tipada]` | 4 | DA menor 1 | consider | sentence: §5.2 | method_reproducibility_unresolved → section: Eq. (2) |
| S35 | REV-50 | A Eq. (3) supõe ausência de falso negativo que o próprio texto põe em dúvida | — | minor | `equation: Eq. (3), hipótese "que não haja avião sem a cultura" [ANCHOR: prosa do cartão, sem âncora tipada]` | 3 | DA menor 2 | consider | sentence: §5.6 | interpretive_ambiguity_remains → section: §5.6 |
| S36 | REV-51 | O critério de concordância da triangulação não define concordância | SC-21 | minor | `text: §5.6 "só há convencimento se" [ANCHOR: prosa do cartão, sem âncora tipada]` | 3 | DA menor 3 | consider | sentence: §5.6 | interpretive_ambiguity_remains → section: §5.6 |
| S37 | REV-52 | Terceiro trimestre como contraste de efeito menor com base em estimativa sem significância | SC-8 | minor | `text: §5.2, terceiro trimestre como contraste "de efeito menor" [ANCHOR: prosa do cartão, sem âncora tipada]` | 3 | DA menor 4 | consider | sentence: §5.2 | claim_scope_unsupported → claim: terceiro trimestre |
| S38 | REV-53 | Generalização de peso ao nascer para o benefício da lei | SC-23 | minor | `text: seção 3.1 "saber se a proibição produziu o benefício em saúde que a motivou" [ANCHOR: prosa do cartão, sem âncora tipada]` | 4 | DA menor 5 | consider | sentence: §3.1 | claim_scope_unsupported → claim: benefício em saúde |
| S39 | REV-54 | "Primeira proibição estadual do gênero" e registros "nunca explorados" sem lastro | SC-22 | minor | `text: cap. 1 e §1.3, alegações negativas [ANCHOR: prosa do cartão, sem âncora tipada]` | 2 | DA menor 6 | consider | sentence: cap. 1 | claim_scope_unsupported → claim: ineditismo |
| S40 | REV-55 | Epidemias sazonais de arbovírus no pré-período tratadas só como confusão da interação por chuva, não do coeficiente principal | SC-20 | minor [SEVERITY-SOURCE: letter-fallback] | `text: cap. 7 e §5.2, arboviroses [ANCHOR: prosa do cartão, sem âncora tipada]` | n/d [CONFIDENCE-SOURCE: ausente no cartão] | DA alternativa 3 | consider | sentence: cap. 7 | evidence_gap_remains → claim: hipótese de identificação |
| S41 | REV-56 | Mudança de composição das mães induzida pela própria lei, via sazonalidade do emprego | SC-13, SC-26 | minor [SEVERITY-SOURCE: letter-fallback] | `text: §5.2, efeitos fixos de município por mês do ano [ANCHOR: prosa do cartão, sem âncora tipada]` | n/d [CONFIDENCE-SOURCE: ausente no cartão] | DA alternativa 4 | consider | sentence: cap. 7 | evidence_gap_remains → claim: hipótese de identificação |
| S42 | REV-57 | A antecipação atinge o desenho principal: o pré-período pode já estar parcialmente tratado | — | minor [SEVERITY-SOURCE: letter-fallback] | `table: Quadro 4, linha Antecipação, "o desenho principal não usa a dose" [ANCHOR: prosa do cartão, sem âncora tipada]` | n/d [CONFIDENCE-SOURCE: ausente no cartão] | DA alternativa 5 | consider | sentence: Quadro 4 | interpretive_ambiguity_remains → table: Quadro 4 |
| S43 | REV-58 | Caminho não discutido: restringir o grupo tratado à Chapada com avião documentado, como estudo de caso com inferência de poucos tratados | — | minor [SEVERITY-SOURCE: letter-fallback] | `text: cap. 5, desenho principal [ANCHOR: prosa do cartão, sem âncora tipada]` | n/d [CONFIDENCE-SOURCE: ausente no cartão] | DA alternativa 6 | consider | sentence: cap. 5 | interpretive_ambiguity_remains → section: cap. 5 |
| S44 | REV-59 | Premissa não examinada: o município por mês como unidade capaz de carregar a pergunta; alternativa de perguntar o que a lei fez aos voos | — | minor [SEVERITY-SOURCE: letter-fallback] | `text: cap. 7 "nenhuma fonte disponível o resolve"; cap. 8, entrega (i) [ANCHOR: prosa do cartão, sem âncora tipada]` | n/d [CONFIDENCE-SOURCE: ausente no cartão] | DA premissa | consider | sentence: cap. 1 | interpretive_ambiguity_remains → claim: pergunta de pesquisa |

Os achados do DA fora das tabelas de severidade ("menor 1" a "menor 6", da lista "Achados menores"; "alternativa 3" a "alternativa 6" e "premissa", das listas de explicações alternativas e de premissa não examinada) não têm âncora tipada no cartão, e os cinco últimos não têm severidade nem confiança por achado. As marcas `[ANCHOR: ...]`, `[SEVERITY-SOURCE: letter-fallback]` e `[CONFIDENCE-SOURCE: ...]` registram isso. As alternativas 1 e 2 do DA repetem M3 e M1 e não geram item.

Perguntas de Persp ao autor (transportadas, não são itens): (1) qual é a doença-alvo e quantas aplicações aéreas por ano um bananal da Chapada e um do Cariri recebiam antes de 2012 e em 2018; (2) se a ADAGRI ou a SEMACE mantinham acervo de receitas ou cadastro de prestadores no período, e em que suporte; (3) se o produtor que opera aeronave própria entrega relatório mensal; (4) se municípios hoje classificados como de banana familiar passam ao grupo tratado ou saem da amostra caso os relatórios mostrem voo.

---

## Revision Roadmap *

`schema_version: revision-roadmap/1.0` (núcleo do parecer, imutável, sem ordenação por prioridade). Total: 59 itens; `must_fix` 15, `should_fix` 11, `consider` 33. O artefato de máquina em JSON não foi emitido: o esquema exige `block_manifest_sha256` e `proposed_targets` com identificadores de bloco de um manifesto de blocos que não existe para este manuscrito. Esta lista é a forma legível do roteiro.

Restrições permanentes do autor, marcadas em cada item que as toca: (a) máximo de 15 páginas textuais, e o texto já está em 15, de modo que todo acréscimo pede um corte equivalente; (b) nenhum número de estimativa do autor no texto; (c) só o Ensaio 1; (d) mudança de estratégia de identificação só por decisão do autor. A marca não muda a obrigação do item nem a decisão: ela diz onde o remédio pedido pelo parecerista e a restrição se encontram, e a escolha é do autor.

### Source-traceability checklist

- [ ] **REV-1** (R1) — EIC W1 — cap. 1; cap. 4; §5.1; Quadro 2 (linha 3); cap. 8 — severidade major — obligation `must_fix` — População, contraste e desfecho da pergunta mudam entre os capítulos 1, 4, 5 e 8. Remédio mínimo: Adotar uma só formulação e repeti-la nos quatro lugares; fixar em uma frase o período de referência de A_m e o que vale no cenário de voos suspensos; dizer no cap. 1 que "saúde ao nascer" são dois desfechos confirmatórios. Restrições do autor: (a) frases; (d) a definição de A_m e do estimando no cenário 3
- [ ] **REV-2** (S1) — EIC W2 — §1.3; §5.4; Quadro 2; cap. 8 — severidade major — obligation `should_fix` — Contribuição enunciada sem condicional; entrega (i) prometida em qualquer cenário embora dependa de terceiros. Remédio mínimo: Dizer quais camadas da contribuição valem em cada linha do Quadro 2; condicionar a entrega (i) ao retorno dos pedidos e dizer o que a substitui; separar no Quadro 2 "registros obtidos sem voos" de "registros não obtidos". Restrições do autor: (a) frases
- [ ] **REV-3** (S2) — EIC W3 — Quadro 5; cap. 8; §5.3; §5.8 — severidade major — obligation `should_fix` — Cronograma não mostra dependências nem prioridades. Remédio mínimo: Linha de marco, com data, para seguir com a classificação provisória; fixar antes do diagnóstico as definições que ele usa (ou declarar que usa as provisórias da §5.4); ordem de prioridade das análises secundárias. Restrições do autor: (a) bloco; (c) a pergunta sobre escopo reduzido do segundo ensaio sai do Ensaio 1
- [ ] **REV-4** (S3) — EIC W4 — cap. 4; §5.5; §5.6; Quadros 3, 4 e 5 — severidade minor — obligation `consider` — Elos ausentes entre objetivos, análises, fontes e atividades. Remédio mínimo: Linhas no Quadro 3 para as bases do RN, dos doadores e das arboviroses, ou retirada das análises sem dado; uma frase sobre o uso do GAEZ ou exclusão da linha; parágrafo curto no cap. 5 para o objetivo (e). Restrições do autor: (a) bloco
- [ ] **REV-5** (S4) — EIC W5 — §1.3; cap. 4; §5.2; §5.4; §5.6 — severidade minor — obligation `consider` — Termos de trabalho usados antes de definidos ou nunca definidos. Remédio mínimo: Uma frase de definição na primeira ocorrência (banana familiar, forma reduzida estadual, quadra chuvosa em meses, VPP, estação de pulverização); remissões no cap. 4. Restrições do autor: (a) frases
- [ ] **REV-6** (S5) — EIC W6 — pré-textuais; cap. 6 — severidade minor — obligation `consider` — Sem resumo e sem seção de recursos (a confirmar contra as normas do programa). Remédio mínimo: Conferir as normas; se admitirem, resumo de até 200 palavras e uma frase sobre recursos. Restrições do autor: (a) bloco, salvo se o resumo for pré-textual e não contar nas 15 páginas
- [ ] **REV-7** (S6) — EIC W7 — cap. 1 (1º e 2º parágrafos); §1.3 — severidade minor — obligation `should_fix` — Afirmações de ineditismo sem apoio. Remédio mínimo: Citar fonte para "primeira proibição estadual"; para as duas alegações de ausência, dizer a busca que as sustenta ou atenuar a redação. Restrições do autor: —
- [ ] **REV-8** (S7) — EIC W8 — §5.8; Quadro 5 — severidade minor — obligation `consider` — Estatuto do desenho principal fica em aberto. Remédio mínimo: Uma frase dizendo o que a ratificação pode alterar, ou declarar que essa escolha é o que se submete à banca. Restrições do autor: (d) é a própria regra de que a escolha do desenho cabe ao autor
- [ ] **REV-9** (S8) — Met W1 — §5.2; Figura 1; Quadro 4 — severidade major — obligation `should_fix` — Eq. (2) não contém o efeito fixo que o texto e a Figura 1 dizem absorver os choques município-ano. Remédio mínimo: Ou acrescentar o efeito fixo de município por ano à Eq. (2) (λ sai), ou manter a equação e corrigir a frase, a Figura 1 e o Quadro 4. Restrições do autor: (d) só a primeira opção, que muda a especificação
- [ ] **REV-10** (R2) — Met W2 — §5.1; §5.2 — severidade major — obligation `must_fix` — O β da Eq. (2) não é o ATT da Eq. (1) sem hipóteses não escritas. Remédio mínimo: Redefinir S_t pelos dois primeiros trimestres ou reescrever o alvo como diferença entre exposição precoce e tardia; declarar a hipótese de exclusão e o sentido do viés; informar o suporte de P_t. Restrições do autor: (a) frases; (d) redefinição do estimando
- [ ] **REV-11** (R3) — Met W3 — §5.2; cap. 4; cap. 6 — severidade major — obligation `must_fix` — Componentes do desenho principal descritos no texto e ausentes da especificação. Remédio mínimo: Quadro de meia página com uma linha por hipótese (desfecho, amostra, coeficiente, ponderação, estatuto) e Eq. (2) estendida com os termos de chuva; cortes numéricos podem ficar para o plano. Restrições do autor: (a) bloco de meia página; (d) especificação
- [ ] **REV-12** (R4) — Met W4 — §5.3; Quadro 2 — severidade major — obligation `must_fix` — O diagnóstico de abertura condiciona a análise confirmatória no desfecho do pré-período. Remédio mínimo: Escolher e escrever uma saída: referência fixada sem usar o desfecho; amostras separadas; ou distribuição de referência do procedimento inteiro em placebos. Definir "gradiente" e retirar a frase. Restrições do autor: (a) frases; (d) regra de escolha do pré-período
- [ ] **REV-13** (R5) — Met W5 — §5.7 (Quadro 2) — severidade major — obligation `must_fix` — Quadro 2 não cobre o resultado que o próprio texto torna mais provável. Remédio mínimo: Reescrever o quadro como cruzamento de medição e diagnóstico, uma ação por célula, com os critérios definidos em uma linha cada. Restrições do autor: (a) bloco; (d) regra de decisão
- [ ] **REV-14** (S9) — Met W6 — §5.2; §5.3; Quadro 4 — severidade major — obligation `should_fix` — Sem verificação dinâmica planejada da hipótese de identificação. Remédio mínimo: Prometer o estudo de evento da diferença tripla (β por ano, ano de referência fixado, mesma inferência) e dizer de antemão como os anos de seca entram. Restrições do autor: (a) frases; (d) acréscimo de análise ao desenho
- [ ] **REV-15** (S10) — Met W7 — §5.2; §5.4 — severidade minor — obligation `consider` — Definição operacional do grupo de comparação e de A_m incompleta. Remédio mínimo: Uma frase com a variável e a base do critério familiar e com as fontes e anos da exclusão por aeronave. Opcional: ordem de grandeza de municípios por grupo. Restrições do autor: (a) frase; (b) limítrofe, só a parte opcional (contagem descritiva)
- [ ] **REV-16** (S11) — Met W8 — §5.8 — severidade major — obligation `should_fix` — Cinco procedimentos de inferência sem designação do primário. Remédio mínimo: Designar um procedimento primário para β e rebaixar os demais a sensibilidade, cada um ligado à sua análise; dizer como entra a dependência espacial; prometer intervalos. A condição de Canay, Santos e Shaikh foi citada de memória pelo assento e deve ser conferida. Restrições do autor: (d) escolha do procedimento primário
- [ ] **REV-17** (R6) — Met W9 — §5.1; §5.5; Quadro 2 (linha 3); Quadro 4 — severidade major — obligation `must_fix` — Três definições de tratamento, e nenhuma fonte mede voos depois da lei. Remédio mínimo: Declarar a intenção de tratar como estimando da Eq. (2) e a cessação efetiva como medida de cumprimento; estender o pedido de relatórios a 2019–2024 (CE e RN); dizer o contrafactual da linha 3 do Quadro 2. Restrições do autor: (a) frases; (d) declaração do estimando
- [ ] **REV-18** (S12) — Met W10 — §5.6; Quadro 3 — severidade minor — obligation `should_fix` — Forma reduzida e triangulação com hipóteses e critério de concordância por escrever. Remédio mínimo: Duas frases: binarização, grupo de dose nula, hipótese de tendências paralelas e papel do GAEZ. Definir concordância como sinal e compatibilidade de intervalos. Restrições do autor: (a) frases
- [ ] **REV-19** (S13) — Met W11 — §5.8 — severidade minor — obligation `consider` — Pré-compromisso declarado, mas não verificável por terceiros. Remédio mínimo: Opcional: depositar o plano com carimbo de data externo antes do terceiro bimestre e citar identificador de versão. Restrições do autor: —
- [ ] **REV-20** (R7) — Dom W1 — §3.2; §5.2; cap. 4 (H3); cap. 7 — severidade major — obligation `must_fix` — Leitura de Calzada et al. além do que o artigo sustenta em trimestre, magnitude e distância. Remédio mínimo: Tratar o terceiro trimestre como pergunta (pré-especificar a exposição na gestação inteira ao lado da de dois trimestres e dizer a principal, ou manter e declarar a atenuação); parte de H3 sobre o trimestre como exploratória; no poder, usar o intervalo do próprio artigo e dizer que mede intensificação sazonal; trocar "apenas a até 150 metros". Restrições do autor: (a) frases; (d) definição de P_t e estatuto de H3
- [ ] **REV-21** (R8) — Dom W2 — §3.2; §5.3; cap. 7 (Quadro 4); H3 — severidade major — obligation `must_fix` — Falta a literatura sobre chuva e saúde ao nascer no semiárido, que muda a leitura do diagnóstico, de H3 e do desenho principal. Remédio mínimo: Citar Rocha e Soares (2015) em 3.2 e no cap. 7; pré-especificar a chuva na gestação como controle, interagida com o grupo e com a cobertura de água e saneamento; reescrever o parágrafo do diagnóstico (compatível com exposição, não demonstração) com um contraste que separe as leituras; linha "fim da seca contemporâneo à lei" no Quadro 4. Restrições do autor: (a) bloco; (d) chuva como controle interagido
- [ ] **REV-22** (R9) — Dom W3 — cap. 4 (H2); cap. 6 — severidade major — obligation `must_fix` — H2 (óbito fetal) com pouco apoio na literatura citada e problema de medida. Remédio mínimo: Uma de duas: manter H2 confirmatória com justificativa, definição da taxa e do desfecho composto, janela de registro comparável e efeito mínimo detectável antes; ou rebaixá-la e usar nascidos vivos por coorte de concepção e razão de sexo como teste de seleção. Dizer que perdas precoces não são observadas. Restrições do autor: (a) frases; (d) estatuto de H2; (b) só se o efeito mínimo detectável for posto no projeto
- [ ] **REV-23** (S14) — Dom W4 — §3.2 — severidade minor — obligation `consider` — Rigotto et al. citado na seção de saúde ao nascer por um resultado que é de neoplasias. Remédio mínimo: Dizer o que o estudo encontra: mais neoplasias; óbito fetal sem diferença de nível e com tendência crescente; nenhum desfecho de peso ou prematuridade. Restrições do autor: —
- [ ] **REV-24** (S15) — Dom W5 — §1.1 — severidade minor — obligation `consider` — Reynier e Rubin não replicam a lógica de Dias, Rocha e Soares. Remédio mínimo: Trocar "replicam a lógica" por descrição: variação semelhante, exposição local, sem o canal hídrico. Restrições do autor: —
- [ ] **REV-25** (S16) — Dom W6 — §3.2 — severidade minor — obligation `consider` — Jones (2020) não isola fungicidas (lido só o resumo). Remédio mínimo: Reescrever ("reportam estimativas para fungicidas, sem separá-los dos inseticidas") ou conferir no texto integral. Restrições do autor: —
- [ ] **REV-26** (S17) — Dom W7 — §3.2; cap. 7 — severidade minor — obligation `consider` — Ameaça de sazonalidade reduzida à composição materna; comparabilidade sazonal dos grupos sem base na literatura citada. Remédio mínimo: Dizer que a sazonalidade tem componente ambiental; declarar no cap. 7 que a comparabilidade sazonal dos grupos é hipótese a examinar ano a ano no pré-período; descrever Brainerd e Menon pelo que fazem. Restrições do autor: (a) frases
- [ ] **REV-27** (S18) — Dom W8 — cap. 6; Quadro 3 — severidade minor — obligation `consider` — Nada sobre a comparabilidade de SINASC e SIM entre 2005 e 2024. Remédio mínimo: Um parágrafo no cap. 6: residência como regra; prematuridade só a partir de 2012 ou com quebra explícita; peso como desfecho estável; fonte das arboviroses no Quadro 3. Restrições do autor: (a) bloco
- [ ] **REV-28** (S19) — Dom W9 — cap. 6 — severidade minor — obligation `consider` — Intoxicações intencionais não são placebo limpo, e a premissa vem sem referência. Remédio mínimo: Citar a base da premissa e tratá-las como contraste informativo, com o sinal esperado sob substituição declarado. Restrições do autor: (a) frase
- [ ] **REV-29** (S20) — Dom W10 — §3.1; cap. 8 — severidade minor — obligation `consider` — O que o primeiro ensaio entrega ao segundo é menos do que as frases de ligação prometem. Remédio mínimo: Ajustar as duas frases: limite inferior, restrito à saúde ao nascer e às coortes da estação, para um componente do benefício. Restrições do autor: (c) compatível: reduz o que se diz do segundo ensaio
- [ ] **REV-30** (S21) — Dom W11 — §1.1; §3.1 — severidade minor — obligation `consider` — Precedentes de restrição do método ficam fora do texto. Remédio mínimo: Duas frases em Antecedentes registrando os precedentes e dizendo que não se localizou avaliação ex post de seus efeitos sobre a saúde. Restrições do autor: (a) frases
- [ ] **REV-31** (R10) — Persp W1 — §1.1; §2.2; §5.8 — severidade major — obligation `must_fix` — A doença não é nomeada e o regime de aplicação é tomado do Equador. Remédio mínimo: Nomear a doença e dizer que o Ceará é área livre de sigatoka-negra; trocar a identidade com o Equador por semelhança com diferença declarada de patógeno e frequência; apoiar a hipótese de estação em fontes locais; usar a magnitude equatoriana como teto. Restrições do autor: (a) frases
- [ ] **REV-32** (S22) — Persp W2 — cap. 8; §5.4; Quadro 3 — severidade major — obligation `should_fix` — Medida municipal e mensal prometida em qualquer cenário, sem dizer onde os registros estão nem se sobreviveram. Remédio mínimo: Condicionar (i) à existência dos relatórios e dizer o que se entrega se vierem em papel, com lacunas ou não vierem; endereçar as superintendências do CE e do RN; pedir a lista de operadores por ano e os relatórios de nenhuma atividade; linha de retenção e suporte no quadro de fontes. Restrições do autor: (a) frases
- [ ] **REV-33** (S23) — Persp W3 — Quadro 3; §5.4 — severidade minor — obligation `consider` — Receituário atribuído a órgão que, pelo decreto, não o guarda. Remédio mínimo: Dizer que a existência de acervo estadual é a primeira pergunta do pedido e que a receita mede intenção de aplicar; sem acervo, retirar ou rebaixar a fonte. Restrições do autor: (a) frase
- [ ] **REV-34** (S24) — Persp W4 — §2.3; §5.4; Quadro 2 (linha 2) — severidade major — obligation `should_fix` — Classificação provisória pelo Censo de 2006 pode apontar para a região errada em 2018. Remédio mínimo: Declarar o quesito como aeronave em qualquer cultura; cruzar com a banana irrigada de grande porte (Censo 2017) e com operadores registrados; tratar o Cariri como candidato a tratado enquanto os relatórios não chegam; dizer que a classificação provisória serve melhor a 2005–2011. Restrições do autor: (a) frases; (d) composição do grupo tratado
- [ ] **REV-35** (R11) — Persp W5 — §5.3; §5.6; Quadro 4 — severidade major — obligation `must_fix` — A seca é lida só como falta de umidade para o fungo, e também encolheu a lavoura irrigada. Remédio mínimo: Acrescentar ao diagnóstico as séries de área colhida de banana irrigada e de área irrigada; dizer que a leitura de exposição só se sustenta se os relatórios mostrarem a queda dos voos; listar a retração da lavoura no Quadro 4. Restrições do autor: (a) frases
- [ ] **REV-36** (S25) — Persp W6 — §5.2; §5.4 — severidade minor — obligation `consider` — Uma só quadra chuvosa para o estado, sem meses, sem definição de ano chuvoso nem de chuva municipal. Remédio mínimo: Definir a quadra em meses; prever estação por macrorregião da FUNCEME quando faltarem relatórios; dizer como a chuva municipal e o ano chuvoso serão construídos. Restrições do autor: (a) frases; (d) estação por macrorregião muda a definição de exposição
- [ ] **REV-37** (S26) — Persp W7 — §5.2 — severidade minor — obligation `consider` — Semelhança entre banana familiar e empresarial afirmada, não mostrada. Remédio mínimo: Tabela curta por grupo (parcela irrigada, macrorregião, variedade, limiar de agricultura familiar); dizer que a aplicação costal no grupo de comparação também segue a chuva. Restrições do autor: (a) bloco; (b) limítrofe: tabela descritiva com dados do próprio autor
- [ ] **REV-38** (S27) — Persp W8 — §5.4; §5.5 — severidade minor — obligation `consider` — Tratamento definido como cessação efetiva, e o pedido de registros termina em 2018. Remédio mínimo: Estender o pedido a dezembro de 2024, para os dois estados, incluindo aeronaves remotamente pilotadas. Restrições do autor: —
- [ ] **REV-39** (S28) — Persp W9 — §5.5; cap. 7 — severidade minor — obligation `consider` — Escala atribuída à deriva não combina com a definição de vizinhos imediatos. Remédio mínimo: Manter os três grupos pelo aquífero e pela realocação; dizer que a deriva entre municípios só importa onde o bananal encosta na divisa; citar as distâncias legais e tratar seu cumprimento como incógnita. Restrições do autor: (a) frases
- [ ] **REV-40** (S29) — Persp W10 — cap. 7; §5.8 — severidade minor — obligation `consider` — Há fonte pública que mede a fração de domicílios perto dos bananais. Remédio mínimo: Reescrever a frase (nenhuma fonte localiza a mãe) e incluir o cadastro de endereços do Censo 2022 como insumo do cálculo de poder, com a limitação de data. Restrições do autor: (a) frase
- [ ] **REV-41** (S30) — Persp W11 — cap. 6 (Aspectos éticos) — severidade minor — obligation `consider` — Registros pedidos por acesso à informação identificam empresas e profissionais. Remédio mínimo: Separar na frase os dados de saúde dos registros administrativos e dizer a regra de divulgação (agregar por município e mês, não nomear operador nem contratante). Restrições do autor: (a) frase
- [ ] **REV-42** (S31) — Persp W12 — Figura 1; Quadro 4 — severidade minor — obligation `consider` — Diagrama não tem o canal de emprego e produção. Remédio mínimo: Acrescentar o nó ao diagrama e uma linha ao Quadro 4; dizer que área colhida e emprego formal agrícola dimensionam o canal. Restrições do autor: (a) linha de quadro
- [ ] **REV-43** (R12) — DA M1 — §5.3; Quadro 2 — severidade major — obligation `must_fix` — O diagnóstico condiciona o teste confirmatório ao contraste que ele mesmo mede. Remédio mínimo: Separar os anos usados para decidir dos usados como referência, ou fixar a referência antes de olhar o gradiente. Restrições do autor: (d) regra de escolha do pré-período
- [ ] **REV-44** (R13) — DA M2 — Quadro 2 (linha 3); §5.1; §5.5 — severidade major — obligation `must_fix` — No cenário de voos suspensos, o parâmetro declarado não tem população e a Eq. (2) não identifica um contrafactual de retorno. Remédio mínimo: Dizer o estimando, o pré-período e a hipótese desse cenário. Restrições do autor: (a) frases; (d) estimando do cenário 3
- [ ] **REV-45** (R14) — DA M3 — cap. 7; §5.2; Quadro 4 — severidade major — obligation `must_fix` — O pós-lei confunde a lei com o fim da seca, e a interação por chuva não os separa. Remédio mínimo: Examinar a resposta diferencial à chuva entre municípios irrigados e de comparação; o cartão indica reparo possível com os anos anteriores a 2012 do painel. Restrições do autor: (a) frases; (d) acréscimo de verificação ao desenho
- [ ] **REV-46** (R15) — DA M4 — §5.3; §5.4 — severidade major — obligation `must_fix` — O padrão dos dois subperíodos não discrimina exposição de seca, e o subperíodo com voos só tem o Censo de 2006. Remédio mínimo: Deixar de ler o contraste como prova de exposição e dizer que medida de voo existe para cada subperíodo. Restrições do autor: —
- [ ] **REV-47** (S32) — DA M5 — Quadro 2 — severidade major — obligation `should_fix` — Regra de decisão com quatro linhas para um espaço de pelo menos três eixos. Remédio mínimo: Acrescentar as combinações ausentes, em especial voos documentados sem gradiente e gradiente sem registro de voo. Restrições do autor: (a) bloco; (d) regra de decisão
- [ ] **REV-48** (S33) — DA M6 — cap. 8; §5.4; Quadro 5 — severidade major — obligation `should_fix` — Promessa da medida além dos meios, sem contingência no cronograma. Remédio mínimo: Condicionar a promessa ao retorno dos pedidos e pôr no cronograma contingência para negativa ou atraso. Restrições do autor: (a) frases
- [ ] **REV-49** (S34) — DA menor 1 — §5.2; Figura 1 — severidade minor — obligation `consider` — Texto e Figura 1 dizem que os efeitos fixos absorvem choques município-ano que não constam da Eq. (2). Remédio mínimo: Mesmo ponto de Met W1; o cartão o remete ao assento de metodologia. Restrições do autor: —
- [ ] **REV-50** (S35) — DA menor 2 — §5.6; cap. 1; §5.2 — severidade minor — obligation `consider` — A Eq. (3) supõe ausência de falso negativo que o próprio texto põe em dúvida. Remédio mínimo: O cartão não propõe remédio; cabe ao autor dizer como a hipótese se sustenta e se o grupo sem banana de H4 pode conter avião. Restrições do autor: —
- [ ] **REV-51** (S36) — DA menor 3 — §5.6 — severidade minor — obligation `consider` — O critério de concordância da triangulação não define concordância. Remédio mínimo: Mesmo ponto de Met W10. Restrições do autor: —
- [ ] **REV-52** (S37) — DA menor 4 — §5.2 — severidade minor — obligation `consider` — Terceiro trimestre como contraste de efeito menor com base em estimativa sem significância. Remédio mínimo: Mesmo ponto de Dom W1 e Met W2. Restrições do autor: —
- [ ] **REV-53** (S38) — DA menor 5 — §3.1; cap. 8 — severidade minor — obligation `consider` — Generalização de peso ao nascer para o benefício da lei. Remédio mínimo: Mesmo ponto de Dom W10. Restrições do autor: (c) compatível
- [ ] **REV-54** (S39) — DA menor 6 — cap. 1; §1.3 — severidade minor — obligation `consider` — "Primeira proibição estadual do gênero" e registros "nunca explorados" sem lastro. Remédio mínimo: Mesmo ponto de EIC W7. Restrições do autor: —
- [ ] **REV-55** (S40) — DA alternativa 3 — §5.2; Quadro 4 — severidade minor [SEVERITY-SOURCE: letter-fallback] — obligation `consider` — Epidemias sazonais de arbovírus no pré-período tratadas só como confusão da interação por chuva, não do coeficiente principal. Remédio mínimo: O cartão não propõe remédio; cabe ao autor dizer como o coeficiente principal é protegido. Restrições do autor: —
- [ ] **REV-56** (S41) — DA alternativa 4 — §5.2; cap. 7 — severidade minor [SEVERITY-SOURCE: letter-fallback] — obligation `consider` — Mudança de composição das mães induzida pela própria lei, via sazonalidade do emprego. Remédio mínimo: O cartão não propõe remédio; ver Met W1, Dom W7 e Persp W12. Restrições do autor: —
- [ ] **REV-57** (S42) — DA alternativa 5 — Quadro 4 — severidade minor [SEVERITY-SOURCE: letter-fallback] — obligation `consider` — A antecipação atinge o desenho principal: o pré-período pode já estar parcialmente tratado. Remédio mínimo: O cartão não propõe remédio; cabe ao autor responder na linha do Quadro 4. Restrições do autor: —
- [ ] **REV-58** (S43) — DA alternativa 6 — cap. 5 — severidade minor [SEVERITY-SOURCE: letter-fallback] — obligation `consider` — Caminho não discutido: restringir o grupo tratado à Chapada com avião documentado, como estudo de caso com inferência de poucos tratados. Remédio mínimo: Nenhuma alteração exigida; dizer em uma frase por que o caminho não foi adotado, se o autor o mantiver fora. Restrições do autor: (d) mudança de estratégia: decisão do autor
- [ ] **REV-59** (S44) — DA premissa — cap. 7; cap. 8 — severidade minor [SEVERITY-SOURCE: letter-fallback] — obligation `consider` — Premissa não examinada: o município por mês como unidade capaz de carregar a pergunta; alternativa de perguntar o que a lei fez aos voos. Remédio mínimo: Nenhuma alteração exigida; ponto de decisão do autor sobre a pergunta. Restrições do autor: (d) mudança de pergunta e de estratégia: decisão do autor

---

## Journal-Supplied Deadline (Optional Transport)

- **Exact deadline from source letter**: NOT PROVIDED
- Nenhum prazo foi inferido.

---

## Response Letter Instructions

A resposta item a item segue `templates/revision_response_template.md` do plugin: uma resposta para cada revisão obrigatória, uma para cada sugerida (adotada, ou a razão de não adotar), as mudanças marcadas no texto revisto e a tabela de correspondência de páginas. Os itens marcados com (d) e os dois dissensos deixados ao autor aceitam como resposta a decisão fundamentada de não alterar.

---

## Closing

Revisão maior, com nova rodada de revisão depois da resposta. Os pareceres concordam em que a pergunta e o objeto estão bem postos e em que o projeto tem a virtude de declarar o cenário sem efeito estimável. O que pedem é que o diagnóstico do pré-período e a regra de decisão fiquem à altura dessa declaração, e que a leitura da seca e do análogo equatoriano não vá além das fontes.

---

## Appendix: Full Reviewer Reports

Os cinco cartões completos da Fase 2 estão, sem alteração, em `docs/ars/pipeline-rodada20/stage3/`: `eic.phase2.md`, `methodology.phase2.md`, `domain.phase2.md`, `perspective.phase2.md`, `da.phase2.md`.

- **EIC**: D5 = warn, D6 = warn. Ponto central: fechar o documento como projeto, com uma só formulação da população e do contraste, a contribuição declarada por cenário e um cronograma com dependências.
- **Met**: D1 = warn, D3 = warn. Ponto central: a Eq. (2) não implementa o que o texto descreve, β não é o ATT da Eq. (1) sem hipóteses por escrever, e o diagnóstico de abertura condiciona o teste confirmatório.
- **Dom**: D2 = block (repairable). Ponto central: falta a literatura de chuva e saúde ao nascer no semiárido, e três leituras da literatura são mais fortes do que as fontes.
- **Persp**: D4 = warn. Ponto central: a fitossanidade local, a guarda dos registros e o efeito da seca sobre a lavoura irrigada ficam sugeridos e não desenvolvidos.
- **Devil's Advocate**: Recommendation N/A — findings only. D3 = block (repairable). Nenhum achado CRITICAL; o contraditório mais forte é que o portão do diagnóstico pode confirmar H1 por regressão à média ou pelo fim da seca.

---

## Notas da camada despachante sobre os anexos

Os três anexos abaixo foram acrescentados depois de a síntese passar no verificador (`check_panel_synthesis.py`, saída 0). São saídas de script, consultivas: não alteram a decisão, a contagem de consenso nem o roteiro, e nenhum item do roteiro vem deles.

Desvio de protocolo no segundo anexo: o protocolo manda enviar o `prompt.md` a um subagente sem ferramentas. Nesta execução o juiz foi o próprio sintetizador, que já tinha lido os cinco cartões com a identificação dos assentos e escrito a síntese; ele não é cego nem independente da síntese. A resposta do juiz está em `claim_audit/reply.jsonl`. Dos 48 achados, o juiz marcou 3 como contraditos em uma afirmação pontual (em cada um, o restante do achado confere com o texto) e 4 como não verificáveis só com o manuscrito. Dois destes últimos (Persp W5 e Persp W11) trazem um dado que não está no manuscrito: a janela de 2015 a 2018 da dose e a contagem de dois municípios tratados.

---

## Attachment: Suggested-Reference Check (advisory, #1001)

Suggested-reference check (script output, not a reviewer finding; #1001)
Seats read: R2, R3 (complete).

| Seat | # | Reference | Result |
|---|---|---|---|
| R2 | 1 | Rocha, R. et al. (2015) "Water scarcity and birth outcomes in the Brazilian semiarid" doi:10.1016/j.jdeveco.2014.10.003 | Found in an index |
| R2 | 2 | Gunnell, D. et al. (2007) "The impact of pesticide regulations on suicide in Sri Lanka" doi:10.1093/ije/dym164 | Found in an index |
| R2 | 3 | Matijasevich et al. (2013) "Estimativas corrigidas da prevalência de nascimentos pré-termo no Brasil, 2000 a 2011" doi:10.5123/S1679-49742013000400002 | Found in an index |
| R2 | 4 | Rodrigues et al. (2019) "Completitude e confiabilidade do Sistema de Informações sobre Mortalidade para óbitos perinatais no Brasil, 2011-2012: um estudo descritivo" doi:10.5123/S1679-49742019000100007 | Found in an index |
| R3 | 1 | Embrapa (2014) "Cultivo da Bananeira para o Agropolo Jaguaribe-Apodi, Ceará" | Title not matched; no DOI or arXiv ID to check |
| R3 | 2 | Rios, S. A. (2013) "Sistema de pré-aviso para controle de Sigatoka-amarela no norte de Minas Gerais" doi:10.5007/2175-7925.2013v26n3p109 | Found in an index |
| R3 | 3 | Pereira, G. R. et al. (2015) "Conflitos pela água em tempos de seca no Baixo Jaguaribe, Estado do Ceará" doi:10.1590/S0103-40142015000200008 | Found in an index |
| R3 | 4 | IBGE (2024) "Censo Demográfico 2022: Cadastro Nacional de Endereços para Fins Estatísticos - CNEFE (Notas metodológicas n. 04)" | Title not matched; no DOI or arXiv ID to check |

"Found" means an index holds a record with this DOI or arXiv ID and title, or with this title. It does not show that the work supports the recommendation, or that the authors and year are right.

---

## Attachment: Reviewer Claim Check (advisory, #1002)

The judge answered 48 of 48 findings from 5 reviewers: it marked 3 as contradicted, and 4 cannot be checked from the manuscript alone.

The judge marked these findings as contradicted by the manuscript. The script checked only the words of each quote: that they occur in the manuscript, or, for words the finding quotes, that they do not. The judge gave the locations, and the script did not check them. Read each quote to decide:
- Journal-Fit Reviewer · W3: O cronograma não mostra as dependências nem as prioridades de um escopo extenso
  > “Montagem do painel (2005--2024) e congelamento das bases” (Quadro 5, linha 3)
- Reviewer 1 · W5: O Quadro 2 não cobre o resultado que o próprio texto torna mais provável
  > “Voos documentados às vésperas da lei, com calendário, e gradiente sazonal no pré-período” (Quadro 2, linha 1)
- Reviewer 1 · W10: Forma reduzida estadual e triangulação com hipóteses e critério de concordância por escrever
  > “efeito no nível da dose recebida sai sob tendências paralelas usuais” (Seção 3.3, primeiro parágrafo)

The author decides what to do with each row. This check does not change the decision, the consensus counts, or the Revision Roadmap. The judge is the session model; as this judge, the #1002 contrast test passed Claude Opus 5.5 and Claude Fable 5.1 (gpt-6-astra and Gemini 4 Argon passed it in part one, through other transports); other models are untested.

---

## Attachment: Acronym Check (advisory, #849)

### Acronym check (advisory; no reply needed)
Coverage: body (partial)
Not in this input: English abstract, Chinese abstract.
Not checked:
- Body, line 589: IBGE (the initials before its parentheses do not spell it)
- Body, line 592: INMET (the initials before its parentheses do not spell it)
- Body, line 596: MAPA (the initials before its parentheses do not spell it)
- Body, line 597: ADAGRI (the initials before its parentheses do not spell it)
- Body, line 598: SEMACE (the initials before its parentheses do not spell it)
- Body, line 599: JFCE (the initials before its parentheses do not spell it)

| Scope | Line | Rule | Acronym | Uses |
|---|---|---|---|---|
| Body | 3 | Not defined | LaTeX | 1 |
| Body | 3 | Not defined | PPGEco | 1 |
| Body | 3 | Not defined | UFES | 1 |
| Body | 139 | Not defined | PL | 1 |
| Body | 145 | Not defined | ADI | 1 |
| Body | 320 | Not defined | ATT | 2 |
| Body | 495 | Not defined | VPP | 1 |
| Body | 586 | Not defined | SINASC | 2 |
| Body | 587 | Not defined | SIM | 2 |
| Body | 588 | Not defined | SINAN | 2 |
| Body | 589 | Not defined | PAM | 2 |
| Body | 593 | Not defined | FAO | 1 |
| Body | 593 | Not defined | GAEZ | 1 |
| Body | 596 | Not defined | CE | 1 |
| Body | 596 | Not defined | RN | 1 |
| Body | 640 | Not defined | CEP | 1 |
| Body | 640 | Not defined | CONEP | 1 |
