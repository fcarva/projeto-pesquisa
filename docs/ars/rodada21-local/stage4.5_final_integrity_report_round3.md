# Relatório de verificação de integridade — Estágio 4.5 (final), rodada 21, verificação 3 (última do laço)

Data da execução: 2026-11-16. Agente: `integrity_verification_agent` (ARS v3.24.2), Mode 2 (final-check), terceira verificação, depois da segunda rodada de correção (três correções).

Objeto: `paper/projeto/` na versão projeto_v14. O hash recalculado sobre `projeto.tex`, `secoes/*`, `referencias-projeto.bib` e `../referencias.bib` confere com `content_hash_v14` do passport (`c5f1c6c7…0d89ec`). `projeto.pdf`, `.bbl`, `.log`, `.blg` e `.toc` são de 02h54, posteriores a todos os `.tex` e `.bib`. O manuscrito não foi editado.

Alcance: destino dos três achados da rodada 2; erros novos; checagens formais do zero; leitura do Apêndice F.6 contra os roteiros 21, 22 e 23 (somente leitura; nenhum dado nem saída aberto; nada executado); checklist dos 7 modos e C4/D7 com a justificativa registrada. As Fases A, B, D e E não foram refeitas (ver "Não conferido").

## Veredito

**FAIL formal, por uma única causa: C4/D7, condição 4.** Fora dela, o texto está limpo.

- **Zero SERIOUS, zero MEDIUM, zero MINOR.** Os três achados da rodada 2 estão resolvidos e as correções não introduziram erro.
- **Checklist dos 7 modos: não bloqueia.** Modos 3 e 6 ficam OVERRIDDEN (justificativa registrada no ledger); os demais, CLEAR ou aviso.
- **C4/D7, condição 4: FAIL formal, mantido.** A declaração do passport continua `no_experiments_declared` ("Não reporta") e o texto continua relatando o sentido de um resultado próprio. O protocolo não prevê override dentro do veredito para condição do D7; a saída é a do laço esgotado: decisão explícita e registrada do pesquisador sobre os itens abertos listados ao fim. O laço de três rodadas se esgota aqui.

## Resumo

| Categoria | Resultado |
|---|---|
| Achados da rodada 2 | 3 de 3 RESOLVIDO |
| Achados novos | nenhum no manuscrito; 2 notas; 1 defeito no registro do processo (passport) |
| Citações e `\ref` | 58 chaves citadas, 58 `\bibitem`, conjuntos idênticos; 23 `\ref`, nenhum sem `\label`; nenhum `??` no PDF; nenhum aviso de LaTeX no `.log` |
| BibTeX | zero avisos (`warning$ -- 0`; nenhuma linha `Warning--`) |
| `.log` | nenhum `Overfull`; 20 `Underfull` (células de quadro) |
| Páginas | PDF de 40 páginas; Introdução na p. 5, cronograma na p. 19, Referências na p. 20 (`projeto.toc` e PDF): 15 páginas textuais |
| Número de estimativa própria | nenhum em corpo, resumo, quadros e apêndices |
| C4 / D7 | condições 1, 2, 3 e 5 passam; **condição 4: FAIL formal** |
| Modos | 1 CLEAR; 2 CLEAR; 3 OVERRIDDEN; 4 CLEAR; 5 CLEAR; 6 OVERRIDDEN; 7 INSUFFICIENT EVIDENCE (aviso) |

## Destino dos três achados da rodada 2

| ID | Destino | Onde | O que está lá |
|---|---|---|---|
| F2-MINOR-1 | **RESOLVIDO** | `apendices.tex:536-539`; p. 38 (folha 39 do PDF) | "O limiar de exposição alta não foi variado; a exclusão de 2012 e 2019 valeu para a diferença tripla, e os estudos de evento trazem coeficiente também para esses dois anos; o início do pós-lei foi deslocado pela variante sem 2020 e 2021." Fiel aos roteiros (seção seguinte). |
| F2-MINOR-2 | **RESOLVIDO** | `referencias-projeto.bib:14` e `:320`; `projeto.bbl:266` e `:399`; p. 22 e 23 | `{arXiv}` protegido nos dois campos. No PDF: "arXiv:2207.11890, versão 3, de 2026" e "arXiv:2505.09942, versão 3". Nenhum "ArXiv" resta em `.bib`, `.bbl` ou PDF. |
| F2-MINOR-3 | **RESOLVIDO** | `referencias-projeto.bib:194` e `:330`; `projeto.bbl:432` e `:155`; p. 24 e 21 | No PDF: "RIGOTTO, R. M.; SILVA, A. M. C. da; …" e "CARNEIRO, F. F.; AUGUSTO, L. G. da S.; RIGOTTO, R. M.; …". Os dois alvos atingidos. Ver nota N3-1 sobre o modo. |

## Apêndice F.6 contra os roteiros 21, 22 e 23

A frase nova é **fiel**, nas duas metades.

- **"a exclusão de 2012 e 2019 valeu para a diferença tripla".** `21:87-88` (`amostra`) mantém só células com `Ref + Seca + Pos == 1`, e os períodos são 2007–2011, 2013–2018 e 2020–2024 (`21:41`): 2012 e 2019 ficam fora. Todas as estimações da diferença tripla passam por esse filtro: os três grupos tratados e as duas variantes de período (`21:150-161`), o tratamento falso (`21:164`, mesmo filtro escrito por extenso), as três definições alternativas do grupo de comparação (`21:169-172`), a permutação (`21:181-183`, sobre as mesmas amostras) e as cinco estimações potiguares (`22:78`).
- **"os estudos de evento trazem coeficiente também para esses dois anos".** O estudo de evento do roteiro 21 usa todos os anos do painel dos tratados e do grupo de comparação, sem o filtro de período, e cria um termo por ano diferente de 2011 (`21:194-203`; o próprio comentário diz "inclui 2005–2006, 2012, 2019"). O roteiro 23 monta as amostras sem o filtro (`23:149-152`) e a função `evento` cria um termo por ano diferente da base (`23:59-62`); na única estimação que terminou, de base 2018, isso inclui 2012 e 2019. Conferido só pelos roteiros; a presença das duas linhas no arquivo de saída é da rodada 2.
- **Resto da lista.** Relida contra os roteiros, sem divergência: três grupos tratados, referência 2008–2010, pós-lei sem 2020 e 2021, quatro definições do grupo de comparação (a principal e três), tratamento falso, cinco grupos potiguares (`22:86-109`), estudo de evento com base 2011, permutação com o período inteiro, e seis estimações previstas no roteiro 23 (`23:171-178`), com bases 2014 e 2018 e a idade da mãe.

Coerência interna: a frase concorda com a abertura do parágrafo ("as coortes de 2012 e 2019 excluídas", `ap:526`), com "O que estava fixado antes" (`ap:541-542`) e com o corpo ("sobre os nascimentos de 2005 a 2024", `05:292-293`).

## Achados novos

Nenhum SERIOUS, MEDIUM ou MINOR.

### Notas (não são problemas do manuscrito)

| ID | Local | Nota |
|---|---|---|
| N3-1 | `referencias-projeto.bib:330` | Em `carneiro2015dossie` a partícula foi obtida com `{\relax da~S}ilva` dentro do nome. A renderização está certa no `.bbl` e no PDF, mas o campo deixou de ser um nome limpo: outro estilo ou um exportador de referências leria o sobrenome de forma diferente. Em `rigotto2013trends` a solução é a comum (`da Silva, Ageo …`). Só importa se o `.bib` for reaproveitado fora deste estilo. |
| N3-2 | `apendices.tex:536-539` | Os estudos de evento incluem também 2005 e 2006, que a diferença tripla não usa (ficam fora da referência de 2007 a 2011). O texto não diz isso nesta frase, e não precisa: o corpo já dá o intervalo de 2005 a 2024. |
| Mantidas | — | N-1 (a frase qualitativa, lida com a célula em negrito, dá limite numérico implícito), N-2 (Calzada et al., versão diagramada não aberta), N2-3, N2-4, ADV-E5-1 e ADV-E5-2: sem mudança desde a rodada 2. ADV-E6-1: ver item aberto 2. |

### Defeito no registro do processo (não é do manuscrito)

**`passport.yaml` não é YAML válido.** O analisador para na linha 65: `round3:` aparece indentado depois de uma chave de primeiro nível (`content_hash_v9`), e o mesmo padrão se repete adiante. Consequência para esta rodada: o bloco `failure_mode_overrides` do Estágio 4.5 está escrito no arquivo, mas não é legível por máquina nem fica, de fato, dentro de `integrity_stage_4_5`. O registro válido da justificativa é o do ledger (`passport_run_ledger.yaml`, seq 23 e 24), que carrega sem erro e tem os elos `prev_hash` consistentes do início ao fim (não recalculei os hashes das entradas). O passport traz ainda dois campos desatualizados: `version_label: "projeto_v7"` e, em `open_decisions`, "divulgação da rodada exploratória de 2026-11-15 no texto: 'Decido depois'", que a decisão do seq 24 já resolveu.

## Checagens formais

- **Citações e remissões.** 58 chaves citadas (comentários excluídos) e 58 `\bibitem`, conjuntos idênticos. 23 remissões, todas com `\label`. Nenhum `??` no PDF. Nenhuma linha `LaTeX Warning` no `.log`.
- **BibTeX.** Zero avisos.
- **Caixas.** Nenhum `Overfull`. Vinte `Underfull`, como antes.
- **Páginas.** 40 no PDF; Referências na p. 20. A frase alongada está no Apêndice F e não toca a contagem.
- **Número de estimativa própria.** Nenhum. No PDF, os valores em gramas são 23 a 32, 80 e 150 (literatura), 40 (desconto declarado) e 2.500 (limiar); os decimais são só as frações e os produtos da grade (p. 16 e 37). A frase nova não traz número além dos anos.
- **Lista de referências.** Busquei no `.bbl` partícula abreviada ("d.") e caixa quebrada de "arXiv": nenhuma ocorrência. Não reli a lista inteira (a rodada 2 leu; mudaram quatro entradas).

## C4 — proveniência de experimentos

"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

D7 sem mudança: declaração presente (`no_experiments_declared`, `declared_by: scholar`, `scholar_answer: "Não reporta"`), `experiment_provenance[]` ausente. Condições 1, 2, 3 e 5 passam. **Condição 4: FAIL formal**, pelo mesmo sinal das rodadas 1 e 2 (`05-metodologia.tex:280-283`; `apendices.tex:417-428`). Nenhuma linha de `experiment_alignment_results[]` foi emitida: não há manifesto com `planned_experiment_ids`.

A justificativa registrada **não transforma a condição 4 em PASS**. Ela é uma condição de FAIL do verificador, que compara rótulo e texto, e os dois seguem em desacordo. O que a justificativa faz é servir de decisão registrada sobre o item, que é a porta que o protocolo dá para entrar no Estágio 5 depois do laço de três rodadas. No mérito não há pendência: a rodada 2 conferiu a divulgação contra a saída gravada, e ela é desfavorável ao teste.

## Checklist dos 7 modos

| Modo | Resultado | Evidência | Bloqueia? |
|---|---|---|---|
| 1. Erro de implementação | CLEAR, com as ressalvas da rodada 2 | Herdado da rodada 2 (saída vista, conta refeita, lado mantido). Nesta rodada não abri saída; a frase do corpo não mudou. A justificativa para o Modo 1 fica sem objeto. | não |
| 2. Citação alucinada | CLEAR | 58 de 58 da rodada 1; os dois defeitos de formatação da rodada 2 foram corrigidos. | não |
| 3. Resultado experimental alucinado | **OVERRIDDEN** (SUSPECTED só pela regra formal; no mérito, limpo) | A regra dispara porque declaração e texto discordam. Justificativa registrada no ledger, seq 24. | não |
| 4. Atalho | CLEAR | Sem afirmação de efeito; a ausência da chuva é declarada. | não |
| 5. Erro reenquadrado como achado | CLEAR | Nenhuma narrativa de surpresa. | não |
| 6. Fabricação de metodologia | **OVERRIDDEN** (SUSPECTED só pela regra formal; no mérito, limpo) | Com F2-MINOR-1 resolvido, a lista de variantes confere com os roteiros linha a linha. Justificativa registrada no ledger, seq 24. | não |
| 7. Travamento de enquadramento | INSUFFICIENT EVIDENCE | Sem mudança. Continua a pergunta ao pesquisador: sabendo que a indicação é a linha 2, o desenho principal segue o mesmo? | não (aviso) |

### A justificativa nova cobre a divulgação?

Texto registrado (ledger, seq 24, `checkpoint_id: stage4.5-failure-modes`, por seleção de opção): "É um projeto de pesquisa. O texto declara as rodadas exploratórias e o sentido do resultado do portão de poder, sem valor, para não dizer menos do que se sabe. Nada disso é teste confirmatório, e a análise será refeita a partir das bases originais."

| O que a rodada 2 pediu | Está na justificativa? |
|---|---|
| A divulgação do sentido do resultado é reconhecida | sim: "declara […] o sentido do resultado do portão de poder" |
| É deliberada | sim: "para não dizer menos do que se sabe" |
| Sem valor | sim: "sem valor" (vale a ressalva da nota N-1: com a célula em negrito há limite numérico implícito) |
| Não é teste confirmatório | sim, expressamente |
| Será refeita | sim: "a análise será refeita a partir das bases originais"; concorda com `05:299-302` |
| Fiel à saída gravada | não consta, e não cabe ao pesquisador atestar: é o que a rodada 2 verificou |

A justificativa não repete a do 2.5: aquela dizia que o projeto "descreve o que será feito" e não mencionava o sentido do resultado. Esta nomeia a divulgação e dá a razão. **Cobre expressamente.**

### O bloqueio fica destravado?

**Checklist: sim.** A regra é "any mode that was SUSPECTED at 2.5 must be resolved by 4.5 (CLEAR, NOT APPLICABLE […], or user-Overridden-with-reasoning)". Os Modos 3 e 6 estão na terceira saída, com razão registrada. O Modo 1 está CLEAR e o 7 só avisa.

Três ressalvas sobre o registro, para que ele não diga mais do que houve:

1. **Seleção de opção.** O protocolo pede que o usuário "explicitly states why the flag is a false positive". O ledger registra que o texto veio de uma opção escolhida, marcada "(Recomendado)", e não de palavras digitadas pelo pesquisador. O registro é honesto quanto a isso; o Estágio 6 tem de dizer o mesmo.
2. **Estado descrito na pergunta.** A pergunta do checkpoint (seq 23) descreve o estado da rodada 1 (Modo 1 INSUFFICIENT EVIDENCE, 1 MEDIUM e 11 MINOR), e o fechamento tem o mesmo horário do relatório da rodada 2 (05h53 UTC). O trecho divulgado não mudou entre a v12 e a v14, de modo que a justificativa vale para o texto atual; mas ela não foi dada à vista da lista desta rodada.
3. **Passport inválido.** A cópia no passport não é legível por máquina (acima). Vale o ledger.

**C4/D7, condição 4: não é destravada por override.** Fica como item aberto 1.

### O que tem de constar no registro do Estágio 6

No "Failure Mode Audit Log", para cada um dos 7 modos: estado final no 4.5, histórico e, se OVERRIDDEN, a razão do usuário.

- **Modo 1:** CLEAR. Histórico: INSUFFICIENT EVIDENCE na rodada 1 do 4.5 (bloqueou); CLEAR na rodada 2, depois de vistas a saída e o roteiro; ressalvas (sem registro de tela, avisos silenciados).
- **Modo 2:** CLEAR.
- **Modo 3:** OVERRIDDEN. Histórico: SUSPECTED no 2.5 (override com a justificativa "Projeto, não resultado"); SUSPECTED de novo nas três rodadas do 4.5, só pela regra formal. Razão: o texto integral do seq 24, com a menção de que foi dado por seleção de opção.
- **Modo 4:** CLEAR. **Modo 5:** CLEAR.
- **Modo 6:** OVERRIDDEN, com o mesmo histórico e a mesma razão do Modo 3, mais as divergências de mérito achadas e corrigidas (F-MEDIUM-1 e F-MINOR-1 na rodada 1; F2-MINOR-1 na rodada 2).
- **Modo 7:** INSUFFICIENT EVIDENCE no 2.5 e no 4.5; pergunta sem resposta registrada.
- **Fora do checklist:** C4/D7 condição 4 FAIL formal nas três rodadas, com a decisão registrada que a destravar; as duas justificativas (2.5 e 4.5), uma ao lado da outra, com a razão por que a primeira deixou de servir; a disposição de ADV-E6-1; os três vereditos do 4.5 (FAIL, FAIL, FAIL formal) e o que cada rodada corrigiu.

## Itens abertos para decisão registrada do pesquisador

1. **C4/D7, condição 4 (único bloqueio formal).** Três saídas, todas do pesquisador:
   - **(a)** Confirmar, depois desta rodada, a decisão já registrada no seq 24 ("manter a divulgação"), agora como decisão explícita sobre item não resolvido ao fim do laço. O seq 24 já nomeia a condição 4, mas foi registrado antes de o laço se esgotar e à vista da rodada 1; se ele basta ou se é preciso novo registro, não cabe ao verificador dizer.
   - **(b)** Trocar a declaração para `experiments_declared` e registrar `experiment_provenance[]` para as duas rodadas (campos na rodada 2, seção C4). É a única saída que põe rótulo e texto de acordo; com ela a condição 4 passa e os Modos 3 e 6 deixam de disparar pela regra.
   - **(c)** Retirar a frase do corpo e o parágrafo do apêndice. Reabre o achado NEW-1 da re-revisão.
2. **ADV-E6-1.** A divulgação entrou no Estágio 4' como item "provisório, a ratificar pelo autor" (RES-01), e a instrução de retomada manteve as decisões provisórias "por delegação (não ratificadas item a item)". O seq 24 trata do mesmo conteúdo e pode valer como `authorize_with_reason`, mas não está registrado como disposição do E6. Falta dizer que é.
3. **Modo 7.** Pergunta de enquadramento sem resposta registrada. Não bloqueia.

Para o orquestrador, sem decisão do pesquisador: consertar a estrutura do `passport.yaml` sem tocar nas palavras registradas, e atualizar `version_label` e `open_decisions`.

## Não conferido

| Item | Motivo |
|---|---|
| Arquivos de dados e de saída das rodadas exploratórias | Fora do alcance desta rodada, por instrução. A fidelidade da frase do corpo à saída gravada e a presença de 2012 e 2019 em `expl_leads_lags__1.csv` são da rodada 2. |
| Execução dos roteiros | Nada foi executado. |
| Fase A (58 referências), Fase B, Fase E | Não refeitas. Valem as rodadas 1 e 2. As correções desta rodada mexeram só em caixa e partícula de quatro entradas. |
| Comparação campo a campo dos `.bib` e dos `.tex` com a v13 | Não há versão anterior guardada nesse estado. Que só três correções foram feitas é o que o pedido informa; conferi o resultado, não a diferença. |
| Leitura integral da lista de referências no PDF | Só as quatro entradas tocadas e uma busca por padrões de defeito no `.bbl`. |
| Hashes das entradas do ledger | Conferi só o encadeamento `prev_hash`. |
| Fase D (originalidade), registro de afirmações (`claim-registry/1.0`), cobertura, contrato do E6, verificação entre modelos | Não executados, como nas rodadas 1 e 2. Estado `E1-COVERAGE-UNRESOLVED`; `[E4-SKIPPED: no scope context]`. |
| Pendências de acesso das rodadas anteriores (Calzada et al. diagramado; cidade em `globorural2021bananais`; DJe da ADI 6137; e as demais) | Sem mudança. |

## Trilha de auditoria (resumo)

- Protocolo: `integrity_verification_agent.md` (Mode 2, C4/D7, critérios de veredito, laço de correção) e `ai_research_failure_modes.md` (inteiro).
- Manuscrito: `apendices.tex:395-555`; `05-metodologia.tex:270-302`; `referencias-projeto.bib` (quatro entradas); `projeto.bbl` (quatro entradas e buscas); `projeto.log`, `.blg`, `.toc`; texto extraído do PDF (cabeçalhos de página, `??`, decimais, valores em gramas, as quatro referências, a frase do F.6).
- Roteiros: `21_`, `22_` e `23_` de `scripts/exploratorio/`, lidos por inteiro.
- Registro: `passport.yaml` (inteiro; tentativa de carga), `passport_run_ledger.yaml` (seq 17 a 25; carga e encadeamento), relatório da rodada 2 (inteiro), `stage4/response_to_residuals.md` (RES-01).
- Roteiros de conferência próprios, fora do repositório. Nenhuma consulta à web nesta rodada.
