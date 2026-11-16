[LEGACY-NO-CONTRACT]

# Verification Review Report — rodada 21, Estágio 3' (re-revisão)

Data: 2026-11-16. Modo legado de passagem única, por opção do pesquisador: a revisão foi feita por edição direta dos `.tex`, sem protocolo de *patch*, sem *sidecar* e sem relatório de aplicação. Não há pré-compromisso de critérios nem verificação mecânica; a decisão abaixo é juízo do verificador contra os critérios de aceitação da carta da rodada 1.

## Judge Record

- **Verification judge**: Claude (claude-fable-5-2), sessão única.
- **Round-1 panel provenance**: artefato tipado ausente na rodada 1 (estado `invalid`, razão `absent`); todos os eixos `unknown`.
- **Blind cross-model pass**: `not_configured`.
- **Pre-committed criteria**: none (legacy — no contract). Usei os *Acceptance criteria* da carta (itens obrigatórios) e a coluna "O que se pede" do roteiro (demais).
- **Prompt/rubric surfaces**: `re_review_mode_protocol.md` (§ Legacy Mode, § Decision Derivation como referência, § Re-Review Output Format); `editorial_decision_standards.md` (linha `re-review`).
- **Reviewer configuration**: cartões da rodada 1 não relidos; o padrão aplicado é o da carta.
- **Apply-report chain**: `not_run_no_reports`.
- **Evidence seen by the judge**: `stage3/editorial_decision.md` (inteiro); listas de Minor Issues dos quatro pareceres; `stage3/manuscript.txt` (por diferença contra o revisado); `stage3prime/manuscript_revised.txt` (inteiro); `stage4/response_to_reviewers.md` e `stage4/revision_notes.md` (inteiros, abertos só depois de formado o juízo item a item). Nenhum outro arquivo do projeto foi aberto. Sem busca na web.
- **Ordem**: evidência antes de persuasão. Três vereditos mudaram depois da leitura da resposta e das notas (REV-06, REV-07, REV-23), todos para baixo ou para a posição do próprio autor; estão marcados.

Esta rodada de verificação rodou na mesma família de modelo que conduziu a revisão; é possível sobre-otimização aos vieses latentes deste juiz.

## Decision

**Minor Revision.**

Os nove itens obrigatórios têm resposta no texto e nenhum ficou sem atendimento. Seis estão atendidos e três atendidos em parte, com resíduo que se corrige trocando palavras ou acrescentando uma frase em apêndice. O CRITICAL C1 (REV-32) está atendido nos três critérios da carta. Não é Accept porque (i) três obrigatórios têm resíduo, (ii) menos de 80% dos itens `should_fix` estão atendidos por inteiro (9 de 20) e (iii) a revisão introduziu incoerências entre o corpo, o Quadro da regra e o Apêndice F. Não é Major porque nenhum resíduo pede reescrita de seção, dado novo ou mudança de desenho, e nenhum obrigatório piorou.

Um aviso de leitura: o resíduo RES-01 é o único que classifico como `major`. Trato-o como resíduo de REV-03 e REV-33, e não como regressão, porque a matéria (a viabilidade do ramo confirmatório) já estava no roteiro. Pela tabela mecânica do contrato, uma regressão `major` levaria a Major Revision. Se o pesquisador recusar a correção, a verificação de integridade deve tratá-lo como achado próprio.

## Revision Response Checklist

Estados: `ADDRESSED`, `PARTIALLY_ADDRESSED`, `NOT_ADDRESSED`, `DECLINED_WITH_REASON`. Arquivos: `05` = `secoes/05-metodologia.tex`; `ap` = `secoes/apendices.tex`; Ap. F = "Regra de decisão: definições, critérios e variantes exploradas".

### must_fix (9)

| ID | Estado | Trecho do revisado que sustenta | O que falta |
|---|---|---|---|
| REV-01 | ADDRESSED | `ap`, Quadro "Produto mínimo de cada linha": linha 3 "Não basta sozinha como avaliação de impacto. Completam-na o controle sintético e a comparação de fronteira"; linha 6 "Excede as rodadas exploratórias pela chuva, pela inferência, pelo poder calculado sem o pós-lei". `08`: "o Apêndice diz, linha a linha, o produto mínimo e por que ele basta, ou não". | As linhas 4 e 5 dizem "é de medida, e não de impacto" sem dizer se basta. O Cap. 8 nomeia só a linha 6 como insuficiente; o apêndice também declara a 3 (RES-10). |
| REV-03 | PARTIALLY_ADDRESSED | `ap`, F.3: "ao nível de 5%, unilateral", "probabilidade de 80%", "decide o maior dos dois"; três magnitudes (40, 80, 150 g); grade de 0,05 a 0,50; "Decide a célula de 80 gramas e fração de 0,25, valor deliberadamente favorável ao teste". | (c) e (b) atendidos. Em (a), a carta pede justificativa independente do desfecho. O texto admite que fração, desconto e 0,25 não têm fonte, e a declaração de que a célula foi fixada por quem conhecia o efeito detectável exploratório é genérica (RES-01). O corpo chama a célula de "central", e ela não é (RES-02). |
| REV-04 | ADDRESSED | `ap`, F.1: "A expressão ausência de voos só é usada para anos completos"; "A_m = 1 se os relatórios registram aplicação aérea [...] em ao menos um ano completo de 2008 a 2011"; "quatro meses consecutivos concentram metade ou mais da área". Quadro "Casos que o Quadro não nomeia": parciais, só eletrônicos, só anuais, tardios. `05`: "31 de maio de 2027". | A linha 6 do Quadro do corpo diz "ou incompletos", e o apêndice manda os parciais com dois ou mais anos completos para as linhas 1 a 5 (RES-07). |
| REV-05 | ADDRESSED | `05`: τ como diferença de duas médias (H_t contra R_t); "hipótese mantida, não testável: a de que a exposição tardia não beneficia o feto". `01`, `04` e resumo nomeiam "aplicação aérea documentada entre 2007 e 2011" e o contraste. "Onde a prática existia" não aparece. | Nada. Título inalterado (era opcional). |
| REV-06 | PARTIALLY_ADDRESSED (ajustado depois da resposta) | Preâmbulo: "Projeto de pesquisa do primeiro ensaio da dissertação". `01`: "o segundo [...] é apenas mencionado e será apresentado à parte". `03`: "ou, nos cenários sem estimativa, a medida do alcance da lei e o efeito mínimo detectável". `08`: "cobre apenas o primeiro ensaio; a defesa segue o calendário do programa". | O critério pede que o texto indique onde o segundo ensaio será apresentado. "À parte" não diz onde nem quando; o próprio autor o reconhece (RES-04). Provisório, a ratificar. |
| REV-07 | PARTIALLY_ADDRESSED (ajustado depois das notas) | `05`: parágrafo "Rodadas exploratórias e plano de análise", com três compromissos; "rotulado como reestimação em dados já examinados"; depósito "com data verificável por terceiros, antes da análise confirmatória". `ap`, F.6: variantes de setembro e de novembro; "O que estava fixado antes", com horários. `01` e resumo com uma linha. | Na leitura do texto, atendido. As notas mostram que o texto afirma mais do que a evidência dá: "A ordem é verificável pelas versões registradas", mas os roteiros de novembro não estão no repositório e o horário deles é data de arquivo; a lista de setembro é por categoria e não saiu da leitura dos roteiros (RES-03). "Nenhum é função do desfecho do pós-lei" é verdadeiro na forma e convive mal com RES-01. |
| REV-10 | ADDRESSED | `ap`, F.4 (a): "Cada município é reduzido à diferença, entre o pós-lei e o período de referência, da média dos resíduos das coortes de exposição alta menos a das coortes de referência"; (b): "A conclusão confirmatória exige que os dois rejeitem a hipótese nula; se só o principal rejeita, β é reportado com as duas inferências, sem conclusão confirmatória". | Nada essencial. Falta o caso inverso (só o de agregado único rejeita); cabe em RES-08. |
| REV-11 | ADDRESSED | `05`: "a conclusão confirmatória exige que a especificação principal e a que deixa o efeito diferir por grupo concordem em sinal e em ordem de grandeza [...] e, se divergirem, β é reportado como resultado não separado do retorno das chuvas". `ap`, F.4 (c): razão "entre um meio e dois"; comparabilidade da chuva. | Nada. A faixa não tem fonte, e o texto o diz. |
| REV-32 | ADDRESSED | Ver seção própria abaixo. | Refinamentos em RES-05 e RES-06, fora dos critérios da carta. |

### REV-32 (CRITICAL C1), critério a critério

1. **Premissa entre as hipóteses de identificação, com a evidência que a sustentaria.** Atendido. `05`, Parâmetro-alvo: "Essa escolha exige uma hipótese de identificação adicional, não verificada: sem a lei, os voos teriam voltado ao padrão da referência depois da seca. [...] Os relatórios de 2008 a 2024 e o relato de voo até 2018 são a evidência que a examina". `ap`, Quadro do Apêndice E, linha "Retorno dos voos". Resumo: "ler o resultado como efeito da lei supõe que, sem ela, os voos teriam voltado depois da seca". `07`: "que eles voltariam é hipótese, não fato".
2. **Linha ou enquadramento para cessação anterior à lei, com entrega declarada.** Atendido. `05`, Quadro da regra, linha 5: "Voos na referência e nenhum em 2018 (série completa): a prática cessou antes da lei [...] β só descritivo". `ap`, F.1 (e) e linha 5 do Quadro de suficiência ("Datação da cessação dos voos e das causas candidatas").
3. **Coeficiente positivo não distingue a lei do fim da prática.** Atendido. `05`: "se os voos cessaram antes da lei por outra causa, um coeficiente positivo não distingue o efeito da lei do fim da prática".

A revisão da "quarta versão do tratamento" também foi feita (`05`: "Não voar desde antes da lei não é uma quarta versão"). A numeração está coerente: todas as remissões à "linha 5" (corpo, Apêndices B, E e F) apontam para a cessação, e a antiga linha 5 é a 6 em todos os lugares. A separação entre as linhas 4 e 5 é clara.

O que a linha nova deixa aberto, sem tirar o atendimento: (i) com cessação parcial, o grupo inteiro segue no teste confirmatório e a estimativa restrita vira sensibilidade, embora o corpo diga que, onde os voos cessaram, "β atribuiria a ela o que tem outra causa"; (ii) com a série de 2018 incompleta, o teste segue confirmatório com a hipótese "não verificada"; (iii) 2018 é chamado "primeiro ano depois da seca", mas as coortes nascidas em 2018 continuam em `Seca_t`. Ver RES-05 e RES-06.

### should_fix (20)

| ID | Estado | Sustentação e o que falta |
|---|---|---|
| REV-02 | ADDRESSED | `08`: "Na linha 6 não há medida dos voos". `01`: "ela depende de os registros serem obtidos"; "o teste depende de haver voos documentados e poder". Linha 6: "o parâmetro deste capítulo não é o alvo". |
| REV-08 | PARTIALLY_ADDRESSED | `01` define estação e período de referência. Siglas só na nota do Apêndice A, e não todas (FUNCEME, INMET, FAO-GAEZ, DATASUS, IBGE, CEP/CONEP). "Hiato sazonal" aparece no Cap. 4 antes da definição (RES-16). |
| REV-12 | ADDRESSED | `05`: "fora da referência cobre só 2005 e 2006, com pouco poder"; "relatados junto a β, e não como portão". Falta dizer o que conta como "desfavorável" (RES-15). Provisório. |
| REV-13 | ADDRESSED | `ap`, Convenções do Apêndice C: janela de $t-9$ a $t-1$; meses de nascimento por grupo; chuva por quadra de exposição; estação única; vizinhos; dezembro de 2024. Refiz a conta dos meses e a das coortes de Limoeiro: conferem. |
| REV-14 | ADDRESSED | `05`: "A comparação entre as análises é descritiva, sem rótulo de concordância". |
| REV-16 | PARTIALLY_ADDRESSED | Estimando por nascimento; linhas "Ponderação" e "Um tratado por vez". Os pesos da referência entram só como sensibilidade (recusa parcial, com razão). |
| REV-17 | PARTIALLY_ADDRESSED | Formulações uniformizadas ("Entre os trabalhos localizados, nenhum avalia"). Sem protocolo nem data da busca. |
| REV-18 | PARTIALLY_ADDRESSED | `02`: "A tabela mostra contaminação da água na região, e não o que o avião aplicava". Sem fonte primária com página. |
| REV-19 | PARTIALLY_ADDRESSED | `03`: "vem, portanto, de um único estudo, e não de mecanismo estabelecido". Sem as estimativas por trimestre e sem a declaração de que não se achou referência. |
| REV-20 | ADDRESSED | `06`: "A média é o desfecho confirmatório porque é nela que o análogo mede o efeito [...]". |
| REV-21 | ADDRESSED | `05`: "Como o análogo equatoriano não encontra efeito além de 150 metros". |
| REV-22 | PARTIALLY_ADDRESSED | Localizador só para os 80 g, e de um "manuscrito de 2023", enquanto a lista traz o artigo publicado (RES-13). |
| REV-23 | PARTIALLY_ADDRESSED (alinhado ao autor) | Afirmação enfraquecida até o que a fonte sustenta ("presença de agrotóxicos na água"). Sem página. |
| REV-24 | ADDRESSED | `05`: "Reportam-se a referência restrita a 2008--2010 e a exclusão das coortes de Limoeiro afetadas"; linha "Sem Limoeiro em 2010". |
| REV-25 | ADDRESSED | Apêndice A (SINAN) e linha Substituição; nota do Quadro do Apêndice E ("Dois elos da cadeia causal ficam sem medida direta"). |
| REV-28 | PARTIALLY_ADDRESSED | `06`: "não se verificou se ela ocorreu no Ceará antes de 2019". Limitação declarada; a consulta pedida não foi feita. Papel das arboviroses explicitado. |
| REV-29 | PARTIALLY_ADDRESSED | `06`: risco reconhecido; "agregação, limiar de supressão e guarda dos documentos são fixados no plano de análise". Nada fixado; sem palavra sobre o enquadramento ético dos registros identificados. |
| REV-30 | ADDRESSED | `01`: "o ensaio informa um desfecho, por uma via, em nível municipal". |
| REV-31 | PARTIALLY_ADDRESSED | Lei nº 1.478/2009 na lista e citada. Faltam a tramitação oficial de 2018, a datação da seca por série de chuva e o número da ação. |
| REV-33 | DECLINED_WITH_REASON | `05`: "Este projeto não traz o seu valor, o que é uma limitação". Razão: restrição do pesquisador. A frase seguinte, "não se sabe ainda qual linha [...] é a provável", diz menos do que o autor sabe (RES-01). Provisório. |

### consider (5)

| ID | Estado | Nota |
|---|---|---|
| REV-09 | PARTIALLY_ADDRESSED | Feitos os cinco exemplos da carta e mais quatro. Não feitos: nome da doença equatoriana, resultado de Camacho e Mejía, Rigotto fora de lugar, "ao menos seis na quadra chuvosa", nome dos órgãos estaduais. |
| REV-15 | PARTIALLY_ADDRESSED | Hipótese condicional declarada; número mínimo de tratados não fixado. |
| REV-26 | ADDRESSED | Apêndice B, linha "Exposição defasada", com o sinal. |
| REV-27 | ADDRESSED | Apêndice C, linha Seleção. |
| REV-34 | ADDRESSED | Equação retirada; a ressalva sobrevive em uma frase com a citação. |

### Contagem

| Obrigação | ADDRESSED | PARTIALLY | NOT_ADDRESSED | DECLINED |
|---|---|---|---|---|
| must_fix (9) | 6 (01, 04, 05, 10, 11, 32) | 3 (03, 06, 07) | 0 | 0 |
| should_fix (20) | 9 | 10 | 0 | 1 (33) |
| consider (5) | 3 | 2 | 0 | 0 |
| Total (34) | 18 | 15 | 0 | 1 |

## New Issues (introduzidos ou tornados visíveis pela revisão)

| # | Severidade | Local | Descrição |
|---|---|---|---|
| NEW-1 | major | `05`, Inferência; `ap`, F.3 | O texto diz "não se sabe ainda qual linha do Quadro é a provável" e chama a célula decisória de "deliberadamente favorável ao teste". O Apêndice F lista, entre as variantes de novembro, "o efeito mínimo detectável por permutação, com o período inteiro", e diz que os critérios foram escritos "por quem conhecia os resultados". As notas de revisão confirmam que a célula foi escolhida com esses valores à vista e que, sob eles, o portão fica fechado na célula decisória. A declaração do Apêndice F é genérica: não liga o conhecimento ao portão nem diz de que lado a célula cai. Resíduo de REV-03 e REV-33. |
| NEW-2 | minor | `05`, Regra de decisão; `ap`, F.3 | O corpo diz "decide a célula central". A grade tem quatro frações (0,05; 0,10; 0,25; 0,50), sem centro; a célula que decide é a de 0,25, que o apêndice chama de favorável. |
| NEW-3 | minor | `ap`, F.1 (e); `05`, Eq. e definição de `Seca_t`; F.3 | O Apêndice F trata 2018 como "primeiro ano depois da seca" e usa os voos de 2018 como exame do retorno. As coortes nascidas em 2018 estão em `Seca_t`, e as de exposição alta nascidas de agosto a dezembro de 2018 foram expostas à quadra de 2018. O efeito detectável por placebo usa o "período de seca" até 2018 como pós falso. Se os voos voltaram em 2018 (o que a linha 1 supõe), essas coortes não são de seca. |
| NEW-4 | minor | `05`, Quadro da regra | As linhas não são mutuamente exclusivas e a precedência não está escrita: a condição da linha 5 pode valer junto com a das linhas 1 a 3. A linha 1 diz "confirmatório" sem remeter às quatro condições que o texto agora exige (voo em 2018; dois procedimentos rejeitam; chuva concorda; não coincide com variante já estimada). |
| NEW-5 | minor | `05`, Quadro, linha 6; `ap`, Quadro de casos | "Registros não obtidos, ou incompletos" (linha 6) contra "parciais, com dois ou mais anos completos: linhas 1 a 5". |
| NEW-6 | minor | `ap`, F.1 (e) | Cessação parcial: o grupo inteiro segue no teste e a estimativa restrita é sensibilidade, em tensão com `05` ("β atribuiria a ela o que tem outra causa"). Série de 2018 incompleta: o teste segue confirmatório. |
| NEW-7 | minor | `ap`, F.6 | "A ordem é verificável pelas versões registradas": só as escolhas estão em versão; os roteiros de novembro, não. A lista de setembro é por categoria. |
| NEW-8 | minor | `ap`, F.6 | "O início do pós-lei não [foi variado]" contra "Foram estimados: [...] o pós-lei sem 2020 e 2021". |
| NEW-9 | minor | `08`; `ap`, F.5 | O Cap. 8 declara insuficiente só a linha 6; o apêndice, também a 3. |
| NEW-10 | minor | `05`, Inferência; `ap`, F | "A ratificação com o orientador não altera [...] a regra de decisão." Não está dito se isso alcança os limiares do Apêndice F, vários deles "sem fonte" e marcados pelo autor como provisórios. Como está, o texto os congela. |
| NEW-11 | minor | `05`, Inferência; `08`, cronograma | O efeito detectável "é reportado no plano de análise" (bimestre 2), mas depende do número de tratados, que a medição pode só dar no bimestre 3. |
| NEW-12 | minor | `ap`, F.1 (b) e (d) | Classificação e pico medidos "em qualquer cultura". Na Chapada há banana e melão; o pico agregado pode não ser o da banana, que é o que a cadeia causal descreve. Falta desempate quando mais de uma janela de quatro meses passa do limiar. |
| NEW-13 | minor | `ap`, F.4 (d) | "Se desfavoráveis" sem critério. |
| NEW-14 | minor | `03` | "Tabela 3, coluna 2, do manuscrito de 2023": o localizador é de versão diferente da que está na lista de referências. |
| NEW-15 | minor | `ap`, Convenções do Apêndice C | A revisão fixou duas escolhas da especificação principal que o original deixava abertas (chuva pela quadra de exposição; vizinhos imediatos fora do grupo de comparação). Não mudam a estratégia, mas mudam a regressão em relação aos roteiros exploratórios. São do agente de revisão e pedem confirmação do pesquisador. |

### O que conferi e não achei

- **Remissões.** Todas as `\ref` do revisado têm `\label`. `sec:diagnostico` ficou sem remissão (o rótulo está num parágrafo; inofensivo). As duas entradas novas citadas constam da lista.
- **Ressalvas que saíram do corpo.** O diagrama está inteiro no Apêndice E, com remissão no corpo. A diluição está no Apêndice B, ampliada, e a lógica segue no Cap. 3. A ressalva da equação de atenuação sobrevive em uma frase. O "hiato achado por acaso", as outras fontes de sazonalidade, a subnotificação do óbito fetal e as avaliações preliminares de água e satélite estão nos Apêndices A e B. O Cap. 7 diz "Três merecem comentário" e comenta três. Nenhuma ressalva sumiu.
- **Cortes sem destino.** Quatro (Callaway e Sant'Anna entre estados; "cinco leis conferidas"; internações por neoplasias; "a população é de coortes"). Nenhum era ressalva de identificação.
- **Número com cara de estimativa própria.** Nenhum. Os valores do Quadro da grade são produtos declarados como tais; os demais são contagens de variantes, datas e números da literatura ou do Censo.
- **Período de referência.** O Apêndice F não o altera. Classifica com 2008 a 2011 e declara a hipótese sobre 2007.
- **Numeração das linhas da regra.** Coerente em todo o texto.

## Onde a alegação do autor excede o texto

1. **REV-03, "atendido".** O critério pede justificativa independente do desfecho para a grade e a célula. O texto diz que não há fonte, e as notas dizem que a escolha "não foi feita às cegas". É atendimento em parte.
2. **REV-07, "atendido".** O texto afirma que a ordem das escolhas "é verificável pelas versões registradas"; as notas dizem que o horário dos roteiros vem da data de modificação de arquivos fora do repositório ("evidência fraca") e que a lista de setembro não saiu da leitura dos roteiros. Aqui é o texto que excede a evidência do autor.
3. **REV-06, "atendido".** A coluna de motivo admite que "à parte" não diz onde nem quando; o critério pedia isso.
4. **REV-01, "produto mínimo e razão de suficiência para cada linha".** As linhas 4 e 5 não dizem se bastam, e o Cap. 8 só reconhece a insuficiência da linha 6.
5. **Notas, "o corpo guarda a faixa, a célula central".** A célula não é central.
6. **Resumo das mudanças, "não muda [...] o grupo de comparação".** Os vizinhos imediatos passaram a ficar fora dele na especificação principal (NEW-15).
7. **`05`, "não se sabe ainda qual linha [...] é a provável".** As notas registram que, com os valores exploratórios, o portão fica fechado na célula decisória. O texto diz menos do que o autor sabe.

No sentido contrário, a resposta lista como não feita a nota sobre o ano da entrada `brasil2011sinasc`, e a lista de referências revisada já a traz.

## Decision Rationale

Nenhum obrigatório está `NOT_ADDRESSED` e nenhum piorou. Os três obrigatórios em parte têm resíduo de classe `should_fix`: uma frase de declaração (REV-03), uma frase reescrita (REV-07) e uma oração (REV-06). A taxa de `should_fix` atendidos por inteiro é de 45%, abaixo dos 80% que a tabela do contrato pede para Accept; os dez em parte são, quase todos, conferências de fonte que o autor declarou não ter feito. Usada como referência, a tabela do protocolo dá Minor Revision pela regra B5. O padrão qualitativo dá o mesmo: tudo se corrige sem nova rodada de pareceres.

## Residual Issues (corrigir antes da verificação final de integridade)

O corpo tem cerca de seis linhas de folga. As correções abaixo trocam palavras no corpo ou vão para apêndice.

| ID | Sev. | Local | Correção sugerida |
|---|---|---|---|
| RES-01 | major | `05`, Inferência (frase "não se sabe ainda"); `ap`, F.3 | Trocar a frase por "o valor pré-especificado ainda não foi calculado". Acrescentar em F.3 que a célula foi fixada por quem conhecia o efeito detectável exploratório de novembro (período inteiro, outro procedimento), de que lado dele a célula cai, e que o valor vai no material depositado. Não exige número. |
| RES-02 | minor | `05`, Regra de decisão | Trocar "decide a célula central" por "decide a célula de 80 gramas e fração de 0,25". |
| RES-03 | minor | `ap`, F.6 | Trocar "A ordem é verificável pelas versões registradas" por redação que diga que só as escolhas estão em versão e que o horário dos roteiros é data de arquivo, não conferível por terceiro. Dizer que a lista de setembro é por categoria e será completada no depósito. |
| RES-04 | minor | `01`, último parágrafo | Trocar "será apresentado à parte" por oração que diga onde (projeto próprio, qualificação ou outro). Decisão do pesquisador. |
| RES-05 | minor | `ap`, F.1 (e) ou Convenções do Apêndice C | Uma frase: as coortes de exposição alta nascidas de agosto a dezembro de 2018 foram expostas à quadra de 2018; β_S e o efeito detectável por placebo são reportados também sem as coortes de 2018. |
| RES-06 | minor | `ap`, F.1 (e) | Dizer o estatuto em dois casos: cessação parcial (sugestão: a conclusão confirmatória exige que a estimativa restrita aos municípios com voo em 2018 tenha o mesmo sinal) e série de 2018 incompleta sem voo registrado (sugestão: sem rótulo confirmatório). Decisão do pesquisador. |
| RES-07 | minor | `05`, Quadro da regra, linha 6 e nota de fonte | Trocar "ou incompletos" por "ou com menos de dois anos completos". Na nota: "A linha 4 prevalece sobre a 5, e a 5 sobre as linhas 1 a 3". |
| RES-08 | minor | `ap`, F.4 | Uma alínea que reúna as condições da conclusão confirmatória da linha 1 (voo em 2018; os dois procedimentos rejeitam; as duas especificações de chuva concordam; não coincide com variante já estimada) e diga o que ocorre se só o procedimento de agregado único rejeitar. |
| RES-09 | minor | `ap`, F.6 | Corrigir "o início do pós-lei não [foi variado]": a variante sem 2020 e 2021 o desloca. |
| RES-10 | minor | `08`; `ap`, F.5 | No Cap. 8, "Nas linhas 3 e 6 [...] não basta sozinho". Nas linhas 4 e 5 do Quadro de suficiência, dizer se basta como ensaio de medida. |
| RES-11 | minor | `05`, Inferência | Dizer se "a regra de decisão" que a ratificação não altera inclui os critérios do Apêndice F. O pesquisador precisa ratificar os valores sem fonte antes de essa frase ir à banca. |
| RES-12 | minor | `05`, Inferência | Trocar "O valor é reportado no plano de análise" por "no plano de análise ou em adendo datado, antes da análise confirmatória". |
| RES-13 | minor | `03` | Conferir o localizador dos 80 g na versão publicada, ou dizer que é de versão de trabalho não conferida contra a publicada. Os 150 g e a faixa de 23 a 32 g seguem sem localizador. |
| RES-14 | minor | `ap`, F.1 (d) | Dizer que a estação é a janela de quatro meses de maior concentração e reportar, como sensibilidade, o pico só da banana. |
| RES-15 | minor | `ap`, F.4 (d); `05` | Retirar "se desfavoráveis" (o intervalo de sensibilidade é sempre reportado) ou dar o critério. |
| RES-16 | minor | `ap`, nota do Quadro de fontes; `04` | Completar as siglas na nota (FUNCEME, INMET, FAO-GAEZ, DATASUS, IBGE, CEP/CONEP), sem custo no corpo. No objetivo (b), glosar "hiato sazonal" em poucas palavras ou remeter à Seção 5.2. |
| RES-17 | minor | vários | Pendências de fonte que o autor declarou e que a integridade vai reencontrar: protocolo e data da busca (REV-17); página do Dossiê (REV-18, REV-23); estimativas por trimestre (REV-19); dispersão contra vetores (REV-28); supressão, guarda e enquadramento ético (REV-29); tramitação de 2018, série de chuva e número da ação (REV-31). Resolver ou manter como limitação declarada. |
| RES-18 | minor | `ap`, Convenções do Apêndice C | Sem mudança de texto: o pesquisador confirma a chuva pela quadra de exposição e os vizinhos fora do grupo de comparação. |

Itens que continuam "provisórios, a ratificar": REV-06, REV-07, REV-12, REV-32, REV-33, e os valores e limiares de REV-03, REV-04, REV-10, REV-11 e REV-13. O depósito público do plano e do material exploratório é compromisso no texto, ainda não cumprido.
