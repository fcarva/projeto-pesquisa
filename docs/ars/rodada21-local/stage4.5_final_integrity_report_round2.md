# Relatório de verificação de integridade — Estágio 4.5 (final), rodada 21, verificação 2

Data da execução: 2026-11-16. Agente: `integrity_verification_agent` (ARS v3.24.2), Mode 2 (final-check), segunda verificação, depois de uma rodada de correção (treze substituições de texto).

Objeto: `paper/projeto/` na versão projeto_v13 (`projeto.tex`, `secoes/01` a `08`, `secoes/apendices.tex`, `referencias-projeto.bib`, `../referencias.bib`; `projeto.pdf`, `.toc`, `.bbl`, `.log` de 16/11/2026, 02h45, posteriores a todos os `.tex` e `.bib`). O manuscrito não foi editado.

Alcance desta rodada: reverificação dos doze achados da rodada 1, busca de erros novos, checagens formais do zero, e evidência para o Modo 1 a partir de quatro arquivos de saída agregada e dos quatro roteiros exploratórios (somente leitura; nada foi executado). A Fase A não foi refeita por inteiro nesta rodada: valem as 58 conferências da rodada 1, e reabri só as fontes das entradas e frases alteradas.

## Veredito

**FAIL.**

- Zero SERIOUS, zero MEDIUM, **3 MINOR** (um de conteúdo, dois de formatação da lista de referências). No Estágio 4.5 qualquer MINOR reprova.
- **C4, condição 4 do anti-skip (D7): FAIL formal, mantido.** O passport segue com `no_experiments_declared` ("Não reporta") e o texto segue relatando, em primeira pessoa, o sentido de um resultado próprio (`05-metodologia.tex:280-283`; `apendices.tex:417-428`). Nenhuma das treze substituições toca nisso, e não cabe ao verificador tocar.
- **Checklist dos 7 modos:** o Modo 1 sai do bloqueio (CLEAR, com ressalvas registradas). Os Modos 3 e 6 seguem SUSPECTED **só pela regra formal** e bloqueiam até resposta do pesquisador.

Dos doze achados da rodada 1, **doze resolvidos**. Nenhuma referência fabricada, nenhuma distorção de fonte, nenhum número de estimativa própria no texto, nenhuma citação ou remissão indefinida.

## Resumo

| Categoria | Resultado |
|---|---|
| Achados da rodada 1 | 12 de 12 RESOLVIDO |
| Achados novos | 3 MINOR (F2-MINOR-1 a 3); nenhum foi introduzido pelas treze substituições |
| Citações e `\ref` | 58 chaves citadas, 58 na lista; 0 órfãs, 0 penduradas; 0 `\ref` sem `\label`; nenhum `??` no PDF; nenhum aviso de indefinição no `.log` |
| Páginas | PDF de 40 páginas; parte textual da p. 5 à p. 19 (15 páginas); Referências na p. 20 (`projeto.toc` e PDF) |
| `.log` e BibTeX | nenhum `Overfull`; só `Underfull` em células de quadro; BibTeX com zero avisos |
| Número de estimativa própria | nenhum. Os únicos decimais do texto são a grade (frações e produtos de desenho) |
| C4 / D7 | condições 1, 2, 3 e 5 passam; **condição 4: FAIL formal** |
| Modos | 1 CLEAR; 2 CLEAR; 3 SUSPECTED (formal); 4 CLEAR; 5 CLEAR; 6 SUSPECTED (formal); 7 INSUFFICIENT EVIDENCE (aviso) |

## Destino dos doze achados da rodada 1

| ID | Destino | Local atual | Texto atual | Conferência |
|---|---|---|---|---|
| F-MEDIUM-1 | **RESOLVIDO** | `apendices.tex:534-536` | "Um roteiro de estudo de evento com bases em 2014 e 2018 e com a idade da mãe como desfecho foi escrito na mesma rodada, e só a primeira de suas seis estimações terminou." | `23_leads_lags_exploratorio.py:171-178` lista seis estimações (quatro com base 2018, duas com base 2014; uma com idade da mãe). Na pasta de saída há um único `expl_leads_lags__N.csv`, o de N = 1, e não há o arquivo de resumo que o roteiro grava ao fim (linha 194). Confere com `RETOMAR.md:27-28`. A que terminou é a dos sete municípios, base 2018, peso ao nascer; o texto não diz qual, e não precisa (nota N2-3). |
| F-MINOR-1 | **RESOLVIDO** | `apendices.tex:529-531` | "quatro definições do grupo de comparação, pela participação familiar nos estabelecimentos e pelo número mínimo de estabelecimentos com banana" | `21_calendario_exploratorio.py:132-133` (principal) e `:169` (três alternativas); quatro linhas correspondentes em `expl_calendario_especificacoes.csv`. |
| F-MINOR-2 | **RESOLVIDO** | `apendices.tex:542-544` | "datadas de 15 de novembro de 2026, entre 19h45 e 22h12, no horário de Brasília" | `git log` de `05-metodologia.tex`: `5c6cac4` às 22h45 UTC (19h45 em Brasília) e `1e71a72` à 01h12 UTC do dia 16 (22h12 do dia 15 em Brasília). |
| F-MINOR-3 | **RESOLVIDO** | `02-contexto.tex:20-21` | "a \emph{certeza} (aprovação unânime \cite{lavor2019antes}, em dezembro de 2018)" | A citação agora cobre só a unanimidade, e a data fica fora dela. Reabri a reportagem: ela diz "sem nenhum voto contrário" e, adiante, "aprovação por unanimidade"; não dá a data da votação. "Unânime" está sustentado. |
| F-MINOR-4 | **RESOLVIDO** | `07-ameacas.tex:13-14` | "Ela levou, desde 2014, ao racionamento da irrigação no Baixo Jaguaribe \cite{pereira2015conflitos}" | Reabri o artigo: "em meados de 2014 começa a ter necessidade de racionamento"; "Após a redução do nível dos reservatórios para 30%, em 2014, é que começou o racionamento". O artigo é de 2015 e só atesta o início; "desde" é lido como marco de início. |
| F-MINOR-5 | **RESOLVIDO** | `08-cronograma.tex:15-16` | "Nas linhas 3 e 6 o ensaio não basta sozinho, e na 6 a medida dos voos é parcial ou falta." | Coerente com o Quadro da regra, linha 6 ("medida parcial dos voos, se houver", `05:251`) e com `apendices.tex:504`. |
| F-MINOR-6 | **RESOLVIDO** | `05-metodologia.tex:64-65` | "o indicador das coortes nascidas de 2013 a 2018, cujo início de gestação cai, em geral, nos anos de seca" | Coerente com `apendices.tex:355-359`. |
| F-MINOR-7 | **RESOLVIDO** | `apendices.tex:151`; `05-metodologia.tex:110-111` | "Exclui, em Limoeiro do Norte, as coortes com alguma parte da gestação na estação de 2010 (nascidas de março de 2010 a fevereiro de 2011, sob a estação provisória; as de março a maio tiveram só o terceiro trimestre na estação)" | Aritmética refeita, abaixo. |
| F-MINOR-8 | **RESOLVIDO** | `../referencias.bib:47`; `projeto.bbl:140-142` | `Mej{\'i}a, Daniel`; na lista, "CAMACHO, A.; MEJ{\'I}A, D." | Caixa alta correta no `.bbl` e no PDF. |
| F-MINOR-9 | **RESOLVIDO** | `referencias-projeto.bib:258-265`; `projeto.bbl:443-450` | `author = {Silva, Eliane}`, `note = {Globo Rural, São Paulo, 9 abr. 2021}` | Página reaberta (por serviço de extração; o acesso direto foi recusado): linha de autoria "Eliane Silva", "09 Abr 2021 - 13h15", título idêntico. A chamada continua definida: a chave `globorural2021bananais` não mudou, as três chamadas (`02:36`, `02:41`, `02:75`) saem como "(SILVA, 2021)" e a entrada está na lista. A cidade "São Paulo" não aparece no trecho lido (ver "Não conferido"). |
| F-MINOR-10 | **RESOLVIDO** | `referencias-projeto.bib:295-302`; `projeto.bbl:66-75` | `note = {Brasília. Documento datado de 28 maio 2013}`, `year = {2013}` | A chamada em `06-dados.tex:19-20` sai com o ano de 2013, ao lado de "a troca do formulário de nascido vivo, em 2011": sem conflito, porque 2011 é o ano da troca e 2013 o do documento. |
| F-MINOR-11 | **RESOLVIDO** | `referencias-projeto.bib:157-164` e `10-17`; `projeto.bbl:318-324` e `263-269` | `ibgepam`: "Disponível em: … Acesso em: 25 ago. 2026."; `denteh2022misclassification`: "Acesso em: 16 nov. 2026." | As duas entradas no padrão das demais. |

### F-MINOR-7: a aritmética

- Convenção do Apêndice C: janela de gestação de t−9 a t−1; dois primeiros trimestres de t−9 a t−4; estação provisória de fevereiro a maio.
- A coorte t tem alguma parte da gestação na estação de 2010 se t−1 ≥ fevereiro de 2010 e t−9 ≤ maio de 2010, isto é, **de março de 2010 a fevereiro de 2011**. Confere com o texto.
- Nascidas em março, abril e maio de 2010: os dois primeiros trimestres terminam em novembro de 2009, dezembro de 2009 e janeiro de 2010; só o terceiro trimestre toca a estação (um, dois e três meses). Confere com "as de março a maio tiveram só o terceiro trimestre na estação".
- Nascidas de junho a dezembro de 2010 e em janeiro e fevereiro de 2011: P = 1/6, 2/6, 3/6, 4/6, 4/6, 4/6, 3/6, 2/6, 1/6, todas positivas. Nascidas em fevereiro de 2010 (janela de maio de 2009 a janeiro de 2010) e em março de 2011 (janela de junho de 2010 a fevereiro de 2011) não tocam a estação de 2010. Os limites estão certos.
- Vigência da proibição municipal: de 20/11/2009 a 26/05/2010. A estação de 2010 cai inteira dentro dela, salvo os cinco últimos dias de maio; os meses de vigência fora da estação (novembro de 2009 a janeiro de 2010) não contam como exposição no desenho. A exclusão cobre, portanto, todas as coortes cuja exposição à estação a proibição pode ter alterado, que é o que o corpo promete ("a exclusão das coortes de Limoeiro afetadas").

## Achados novos

Nenhum foi introduzido pelas treze substituições. O primeiro apareceu ao ler as saídas, que a rodada 1 não abriu; os outros dois já estavam na lista de referências e escaparam à rodada 1.

### SERIOUS e MEDIUM

Nenhum.

### MINOR

| ID | Local | O que o texto diz | O que o registro mostra | Correção de uma linha |
|---|---|---|---|---|
| F2-MINOR-1 | `apendices.tex:536-537` | "O limiar de exposição alta e a exclusão de 2012 e 2019 não foram variados" | Vale para as estimações da diferença tripla. Os dois estudos de evento da rodada não excluem esses anos: o do roteiro 21 traz um coeficiente por ano, "inclui 2005–2006, 2012, 2019" (`21_calendario_exploratorio.py:194-203`), e a estimação que terminou no roteiro 23 também (`23_…py:149-152`; `expl_leads_lags__1.csv` tem linhas para 2012 e 2019). O hiato sazonal das coortes de 2019 nos tratados já foi, portanto, estimado. | "O limiar de exposição alta não foi variado; a exclusão de 2012 e 2019 valeu para a diferença tripla, e os estudos de evento trazem coeficiente também para esses dois anos". |
| F2-MINOR-2 | `referencias-projeto.bib:14` e `:320`; `projeto.bbl:266` e `:399`; lista, p. 21 e 23 | "ArXiv:2207.11890" e "ArXiv:2505.09942" | O estilo põe em maiúscula a inicial do campo; o nome do repositório é "arXiv". Caixa quebrada. | Proteger a inicial: `howpublished = {{arXiv}:2207.11890, …}` e `{{arXiv}:2505.09942, …}`; conferir no `.bbl`. |
| F2-MINOR-3 | `referencias-projeto.bib:194` e `:330`; `projeto.bbl` (entradas `rigotto2013trends` e `carneiro2015dossie`) | "SILVA, A. M. C. d." e "AUGUSTO, L. G. d. S." | A partícula "da" dos nomes (Ageo Mário Cândido da Silva; Lia Giraldo da Silva Augusto) sai abreviada como "d.". O esperado é "SILVA, A. M. C. da" e "AUGUSTO, L. G. da S.". | Ajustar os dois campos de autoria para que a partícula não seja abreviada (alvo de renderização acima) e conferir no `.bbl`. |

### Notas (não são problemas)

| ID | Local | Nota |
|---|---|---|
| N-1 (mantida) | `apendices.tex:420-424` com o Quadro da grade | A frase qualitativa, lida com a célula em negrito, continua dando um limite inferior numérico ao efeito detectável exploratório, nos dois recortes. Decisão do pesquisador diante da restrição "nenhum número de estimativa no texto". |
| N-2 (mantida) | `03-referencial.tex:32-33` | Tabela 3, coluna 2, de Calzada et al. conferida na rodada 1 no manuscrito de 2023; versão diagramada não aberta. UNVERIFIABLE_ACCESS, como o próprio texto declara. |
| N2-3 | `apendices.tex:534-536` | A estimação que terminou no roteiro 23 é a dos sete municípios, com base 2018 e peso ao nascer. O texto não a identifica; dizer qual é melhora o registro, mas a frase atual não é falsa. |
| N2-4 | `apendices.tex:531-534` | O roteiro 22 também calcula uma permutação no lado potiguar (`22_…py:110-120`), só impressa, não gravada. A lista do apêndice fala em "efeito mínimo detectável por permutação" sem distinguir; não é omissão que mude o sentido. |
| ADV-E5-1, ADV-E5-2 (mantidas) | `01-introducao.tex:22-23` e `:60-61` | Afirmações de novidade limitadas à busca, sem protocolo nem data de busca: `UNRESOLVED`, consultivo. |
| ADV-E6-1 (mantida) | `05-metodologia.tex:279-284` | Mudança de força autorizada por item marcado "provisório, a ratificar pelo autor". Continua pedindo a disposição do autor (`restore`, `authorize_with_reason` ou `pause`). As treze substituições não trazem deriva nova: as duas que mudam força ("em geral", `05:65`; "levou, desde 2014, ao racionamento", `07:13`) foram pedidas pela rodada 1. |

## Evidência para o Modo 1

Arquivos abertos, somente leitura: `expl_calendario_permutacao.csv`, `expl_calendario_especificacoes.csv`, `expl_fronteira_rn.csv`, `expl_leads_lags__1.csv`; roteiros `20_` a `23_` em `scripts/exploratorio/`. Nenhum outro arquivo de dados foi aberto; da pasta de saída só li a listagem de nomes e datas. Nada foi executado. Este relatório não reproduz valor de estimativa.

### (a) A frase do corpo é fiel à saída gravada?

**Sim, nos dois recortes.**

- A frase: "A rodada exploratória de novembro, com classificação e estação provisórias, indicou efeito detectável acima do plausível na célula que decide" (`05:280-282`), com a célula de 80 gramas e fração 0,25, isto é, 20 gramas (`05:226-227`; Quadro da grade).
- O que está gravado: `expl_calendario_permutacao.csv` tem duas linhas, "principal" (7 tratados) e "Chapada" (2 tratados), cada uma com o desvio-padrão da distribuição de placebos e o número de repetições. O efeito detectável **não é coluna do arquivo**: o roteiro o imprime na tela como um múltiplo fixo desse desvio (`21_…py:191`) e não grava a saída de tela. Refiz o produto à mão.
- Resultado: o efeito detectável fica **acima** dos 20 gramas no recorte de sete municípios e **acima** no da Chapada, com folga nos dois.
- O multiplicador do roteiro é o do teste bilateral; o projeto define o teste como unilateral (`05:276-277`), cujo multiplicador é menor. Refeito com o unilateral: **acima** nos dois recortes. A diferença não muda o lado.
- Conferência cruzada: usando, no lugar do desvio dos placebos, o erro-padrão agrupado gravado em `expl_calendario_especificacoes.csv` (que o próprio roteiro chama de otimista), o resultado segue **acima** nos dois recortes.
- "A escolha de 0,25, e não de fração menor, não muda o lado" (`ap:424-425`): verdadeiro por construção, porque fração menor só reduz o efeito plausível.
- "tanto com os sete municípios do Censo de 2006 quanto só com os dois da Chapada do Apodi" (`ap:421-422`): as contagens de tratados gravadas são 7 e 2, e o roteiro as impõe por `assert` (`21_…py:184`).
- "calculado por permutação, com o período inteiro" (`ap:419`): a função `permuta` sorteia tratados falsos entre os municípios de comparação e usa o coeficiente do pós-lei, na amostra com referência, seca e pós-lei (`21_…py:87-108`). Confere.

### (b) A lista de variantes do Apêndice F.6 corresponde aos roteiros?

| O texto (`ap:524-538`) | Roteiro | Saída | Resultado |
|---|---|---|---|
| estação de fevereiro a maio; limiar de metade; referência 2007–2011; 2012 e 2019 excluídas; sem a chuva | `21:40-41`, `:64-68`, `:88`; cabeçalho `:16-17` | — | confere |
| três grupos tratados (sete; dois da Chapada; cinco restantes) | `21:150-157` | três primeiras linhas de `expl_calendario_especificacoes.csv`, com 7, 2 e 5 tratados | confere |
| referência restrita a 2008–2010 | `21:158-159` | linha própria | confere |
| pós-lei sem 2020 e 2021 | `21:160-161` | linha própria | confere |
| quatro definições do grupo de comparação | `21:132-133` e `:169` | a principal e três linhas de limiar | confere |
| tratamento falso | `21:163-166` | linha própria | confere |
| cinco grupos de comparação potiguares para os dois municípios da Chapada | `22:86-109` | `expl_fronteira_rn.csv` tem cinco linhas, todas com 2 tratados | confere |
| estudo de evento com 2011 como base | `21:194-209` | `expl_calendario_evento.csv` existe (listagem; não aberto) | confere pelo roteiro |
| efeito mínimo detectável por permutação, com o período inteiro | `21:178-192` | `expl_calendario_permutacao.csv` | confere |
| roteiro com bases em 2014 e 2018 e idade da mãe; só a primeira de seis estimações terminou | `23:171-178` | só `expl_leads_lags__1.csv`; sem arquivo de resumo | confere |
| "a exclusão de 2012 e 2019 não [foi variada]" | `21:194-203`; `23:149-152` | `expl_leads_lags__1.csv` tem 2012 e 2019 | **impreciso: F2-MINOR-1** |

O arquivo de especificações tem nove linhas, e as nove estão na lista do apêndice.

### (c) Sinais de erro de implementação que comprometam a frase do corpo

Não encontrei nenhum que mude o lado. O que li:

- **Exposição.** `exposicao` (`21:45-48`) toma os meses de t−9 a t−4 e devolve a fração na estação; refiz os doze meses e ela reproduz a classificação do Apêndice C (alta de agosto a dezembro; intermediária em janeiro, fevereiro, junho e julho; referência de março a maio).
- **Especificação.** Efeitos fixos de município por mês, município por ano e coorte; interações de tratado com exposição alta e intermediária, por período; ponderação por nascimentos (`21:73-84`). É a Equação do projeto sem os termos de chuva, como o texto diz. Os termos de ordem inferior são de fato absorvidos pelos efeitos fixos.
- **Permutação.** As 999 repetições pedidas estão todas gravadas nos dois recortes: o `try/except` que engoliria falhas (`21:104-107`) não descartou nenhuma.
- **Execução.** O roteiro grava os três arquivos `expl_calendario_*` no último passo (`21:211-215`), depois do estudo de evento; os três existem, com data de 23:39:15, posterior à gravação do roteiro (23:32:36). A execução chegou ao fim sem exceção. Os números não são redondos nem repetidos entre recortes.
- **Porte.** Os placebos são sorteados entre municípios de comparação. Se os tratados fossem muito maiores, o desvio dos placebos superestimaria o efeito detectável. Pela coluna de nascimentos das saídas, o porte médio dos tratados é da mesma ordem do dos municípios de comparação, e não maior. Esse viés não explica o lado.

Ressalvas, que não mudam o lado e ficam registradas:

1. **Não há registro da saída de tela nem código de saída gravado.** O término sem erro é inferido da existência e da data dos arquivos.
2. **Os avisos foram silenciados** (`warnings.filterwarnings("ignore")`, `21:38`). Não é possível atestar "zero avisos"; avisos do estimador sobre observações descartadas ou colinearidade, se houve, não ficaram em lugar nenhum.
3. **O efeito detectável é aproximação** (múltiplo do desvio dos placebos, com multiplicador bilateral), não o procedimento de Ferman e Pinto nem o de agregado único que o projeto pré-especifica; e usa o pós-lei. O texto diz as duas coisas (`ap:417-420`, `:426-428`).
4. **Roteiro 22.** Não remove duplicatas do arquivo de nascimentos dos dois estados, ao passo que o roteiro 23 o faz (`23:156`). Se há duplicatas, as estimativas de fronteira estão afetadas. A frase do corpo não depende delas (vem só do roteiro 21 e do arquivo cearense), e o texto só afirma que os cinco grupos foram estimados. Fica como aviso para o depósito.

## Checagens formais e de consistência

- **Citações e remissões.** 58 chaves citadas nos `.tex` (comentários excluídos) e 58 `\bibitem`; conjuntos idênticos. Nenhum `\ref` sem `\label`. Nenhum `??` no texto do PDF. Nenhum aviso de citação ou referência indefinida no `.log`. BibTeX: zero avisos.
- **Páginas.** 40 no PDF. Introdução na p. 5; último texto na p. 19 (cronograma); Referências na p. 20. Quinze páginas textuais. A célula alongada do Quadro de especificações (F-MINOR-7) e a frase alongada do Apêndice F estão nos apêndices e não mexem na contagem.
- **Número de estimativa própria.** Nenhum em corpo, resumo, quadros e apêndices. Os valores em gramas são 40, 80, 150 (magnitudes da literatura e desconto declarado), 32 (literatura) e 2.500 (limiar de baixo peso); os decimais são as frações e os produtos da grade.
- **Resumo e corpo.** O resumo afirma só o que o corpo afirma; não traz o sentido do resultado exploratório, e não precisa.
- **Consistência das substituições entre si.** "na 6 a medida dos voos é parcial ou falta" (`08:15-16`) concorda com o Quadro da regra e com o quadro de suficiência; "em geral" (`05:65`) concorda com `ap:355-359`; a exclusão de Limoeiro (`ap:151`) concorda com `05:109-111` e com a cronologia (`ap:193-194`); "19h45" (`ap:543`) concorda com N-4 da rodada 1.
- **Lista de referências.** Lida inteira no `.bbl`. Fora F2-MINOR-2 e F2-MINOR-3, nenhuma entrada com campo ou caixa quebrados.

## C4 — proveniência de experimentos

"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

D7: declaração presente (`no_experiments_declared`, `declared_by: scholar`, `declared_at`, `scholar_answer: "Não reporta"`); `experiment_provenance[]` ausente. Condições 1, 2, 3 e 5 passam. **Condição 4: FAIL formal**, pelo mesmo sinal da rodada 1: frase de resultado próprio, em primeira pessoa, sem marcador de referência (`05:280-283`; `ap:420-424`). Nenhuma linha de `experiment_alignment_results[]` foi emitida, porque não há manifesto de afirmações com `planned_experiment_ids`.

O que é regra formal e o que é mérito:

- **Regra formal.** A condição 4 compara um rótulo com o texto. O rótulo diz que o manuscrito não reporta experimento próprio; o texto reporta o sentido de um. A condição é heurística e foi escrita para seção de Resultados, que um projeto não tem; ainda assim o sinal mínimo ("resultado de execução própria, sem marcador") está presente. O rótulo era exato na v7 e deixou de ser quando a divulgação entrou.
- **Mérito.** Não há problema de mérito. A divulgação é fiel à saída gravada (seção anterior), é desfavorável ao teste e foi pedida pela revisão (NEW-1).

Opções do pesquisador, todas dele:

1. **Trocar a declaração** para `experiments_declared` e registrar `experiment_provenance[]` para as duas rodadas. Cada entrada pede `experiment_id`, `title`, `repro_lock` (pode ser nulo, com o motivo), `planned_vs_executed[]` (no roteiro 23, cinco de seis com `executed: false` e `skip_reason`), `negative_results[]` e `known_limitations[]`. É a saída que deixa rótulo e texto de acordo. Com ela a condição 4 passa, a condição 2 passa, e a regra que força os Modos 3 e 6 a SUSPECTED deixa de disparar: os dois passam a ser julgados só no mérito. Para a linha de alinhamento ser emitida falta ainda um manifesto que ligue a frase ao experimento.
2. **Retirar a frase** do corpo e o parágrafo do apêndice. Zera o sinal da condição 4, mas reabre NEW-1, e o texto continuaria dizendo que as rodadas foram estimadas, de modo que os Modos 3 e 6 seguiriam disparando pela regra.
3. **Manter tudo e registrar decisão explícita** sobre o item, que é a saída que o protocolo dá depois do laço de três rodadas de FAIL do Estágio 4.5 (esta é a segunda).

## Checklist dos 7 modos

A declaração é `no_experiments_declared` e o texto apresenta análises próprias como feitas ("estimou a forma reduzida estadual", "estimou o desenho de calendário", "indicou efeito detectável acima do plausível", "Foram estimados: …"). Pela regra, declaração e texto discordam: nenhum dos Modos 1, 3, 5 e 6 é NOT APPLICABLE, e os Modos 3 e 6 ficam SUSPECTED. Os Modos 1 e 5 são julgados pela evidência.

| Modo | Resultado | Evidência | Bloqueia? |
|---|---|---|---|
| 1. Erro de implementação que passa pela autorrevisão | **CLEAR**, com ressalvas | A única afirmação de resultado do texto é de sentido. Vi a saída gravada, li o roteiro que a produz e refiz a conta: o lado se mantém nos dois recortes, com o multiplicador do roteiro, com o do projeto e com a medida de dispersão alternativa gravada. Execução concluída (arquivos gravados no último passo), repetições completas, sem número redondo. Ressalvas: sem registro de tela, avisos silenciados. | não |
| 2. Citação alucinada | CLEAR | 58 de 58 conferidas na rodada 1; nesta, reabertas as três fontes tocadas pelas correções; nenhum problema. Restam dois defeitos de formatação (F2-MINOR-2 e 3). | não |
| 3. Resultado experimental alucinado | **SUSPECTED só pela regra formal**; no mérito, limpo | A rodada 1 conferiu o resultado contra o mapa; esta, contra a saída bruta. Confere. A regra dispara pela discordância entre declaração e texto, não por dúvida sobre o resultado. | **sim** |
| 4. Atalho | CLEAR | Não há afirmação de efeito; o confundidor mais óbvio (chuva) é declarado como ausente na rodada e exigido na regra. | não |
| 5. Erro reenquadrado como achado | CLEAR | Nenhuma narrativa de surpresa; o resultado divulgado é desfavorável e não é tratado como descoberta. | não |
| 6. Fabricação de metodologia | **SUSPECTED só pela regra formal**; no mérito, resta uma imprecisão | As duas divergências da rodada 1 foram corrigidas e a lista de variantes confere com os roteiros e as saídas, linha a linha. Resta F2-MINOR-1 (os estudos de evento não excluíram 2012 e 2019). | **sim** |
| 7. Travamento de enquadramento | INSUFFICIENT EVIDENCE | Sem mudança desde a rodada 1. Pergunta ao pesquisador: sabendo que a indicação é a linha 2, o desenho principal continua o mesmo? | não (aviso) |

### Modos 1, 3 e 6: regra formal, mérito e opções

**Modo 1.** Não há regra formal em jogo; é só mérito, e o mérito está resolvido para o que o texto afirma. A rodada 1 não tinha visto saída nem roteiro executado; agora há os dois. As ressalvas (sem registro de tela; avisos silenciados) não bastam para manter o bloqueio, porque a afirmação é de lado e o lado resiste a todas as contas alternativas que a saída permite. Elas pesam para o depósito: convém refazer a rodada com os avisos ligados e a tela gravada.

**Modos 3 e 6.** O que é regra formal: quando a declaração diz que não há experimento e o texto apresenta análise própria como feita, os dois modos ficam SUSPECTED, qualquer que seja a qualidade do relato; e um modo que foi SUSPECTED no 2.5 precisa chegar ao 4.5 como CLEAR, NOT APPLICABLE ou com justificativa registrada, senão o pipeline volta a bloquear e não segue para a finalização. O que é mérito: no Modo 3, nada pendente; no Modo 6, uma frase a corrigir (F2-MINOR-1).

As opções que o protocolo dá ao pesquisador no bloqueio:

1. **Confirmar o aviso** e voltar à redação para corrigir.
2. **Justificar** (override com razão): dizer por que o aviso é falso positivo; a razão vai para o registro do Estágio 6.
3. **Revisar a passagem** e rodar a checagem de novo.

E, por fora do checklist, a opção 1 da seção C4 (trocar a declaração e registrar a proveniência), que faz a regra deixar de disparar e leva os dois modos a julgamento só de mérito: o Modo 3 ficaria CLEAR, e o Modo 6, CLEAR depois de F2-MINOR-1.

**A justificativa do 2.5 não pode ser só repetida.** Ela dizia: "Projeto, não resultado: É um projeto de pesquisa: descreve o que será feito. As duas rodadas exploratórias estão declaradas no texto, sem número, e serão refeitas a partir das bases originais." Foi dada sobre um texto que não dizia para que lado o resultado exploratório caiu. Hoje:

- "descreve o que será feito" já não é toda a verdade: o texto relata o sentido de um resultado e o usa para explicar por que a célula que decide não é pré-especificada em sentido estrito;
- "sem número" continua verdadeiro na letra, mas a frase, lida com a célula em negrito, dá um limite numérico implícito (N-1);
- "serão refeitas a partir das bases originais" continua valendo e está no texto (`05:299-302`).

Se a opção for justificar, a justificativa nova precisa cobrir expressamente a divulgação: que ela é deliberada, sem valor, fiel à saída gravada (o que esta verificação confirma) e que o valor que vale para a regra será recalculado como o Apêndice F descreve. O próprio passport registra que "a justificativa terá de ser registrada de novo". As palavras são do pesquisador; o verificador não as escreve.

## Não conferido

| Item | Motivo |
|---|---|
| Fase A do zero nesta rodada | Não refeita. Valem as 58 conferências da rodada 1; reabri só Globo Rural, Agência Pública e Pereira e Cuellar. As demais entradas da lista não mudaram de chave; não comparei os `.bib` com a v12 campo a campo (os arquivos não estão versionados nesse estado). |
| Cidade "São Paulo" em `globorural2021bananais` | O trecho lido da página traz autoria, data e título, não a cidade. O acesso direto à página foi recusado; a leitura foi por serviço de extração. |
| `expl_calendario_evento.csv` e os demais arquivos da pasta de saída | Fora da lista autorizada. Do estudo de evento com base 2011 conferi o roteiro e a existência do arquivo. |
| Registro de tela, código de saída e avisos das execuções | Não existem gravados. |
| Efeito de possíveis duplicatas no roteiro 22 | Exigiria abrir o arquivo de nascimentos. |
| Renderização exata das correções propostas em F2-MINOR-2 e 3 | Não compilei; a correção precisa ser conferida no `.bbl`. |
| Versão diagramada de Calzada et al.; data do DJe da ADI 6137; ano "2012" de `ibge2006censoagro`; página do SIDRA de `ibge2017censoagro`; texto integral das catorze referências conferidas só por metadados; Ferman e Pinto na versão publicada | Como na rodada 1; nada mudou. |
| Ausência de lei municipal de Limoeiro posterior a 2010; nota oficial de março de 2011 | Como na rodada 1. |
| Fase D (originalidade) | Não refeita. As treze substituições são trocas de palavras e de metadados, sem parágrafo novo. Cobertura da rodada 1: cerca de 10%, abaixo dos 50% do protocolo. D2 não executado. |
| Artefatos do protocolo: registro de afirmações (`claim-registry/1.0`), cobertura (#737), linhas de evidência (#656), contrato do E6, verificação entre modelos | Não executados, como na rodada 1. Estado `E1-COVERAGE-UNRESOLVED`; cobertura semântica `not_machine_detectable`; `[E4-SKIPPED: no scope context]`. |

## Trilha de auditoria (resumo)

- Manuscrito: leitura integral de `05-metodologia.tex`, `07-ameacas.tex`, `08-cronograma.tex` e de `apendices.tex` a partir da linha 100; `02-contexto.tex:10-77`; trechos de `01`, `06` e do resumo; `projeto.bbl` inteiro; `projeto.log`, `.blg`, `.toc`; texto extraído do PDF (páginas, `??`, decimais).
- Roteiro de conferência próprio (fora do repositório): conjunto de chaves citadas contra `\bibitem`; `\ref` contra `\label`; avisos do `.log`.
- Web: apublica.org (reportagem de 15/02/2019, redação sobre a votação); globorural.globo.com (autoria, data e título, por serviço de extração; acesso direto recusado); periodicos.usp.br (Pereira e Cuellar, 2015, trechos sobre o racionamento de 2014). Nenhum nome do pesquisador nem trecho do projeto foi enviado a buscador.
- Repositório: `git log` de `05-metodologia.tex` desde 15/11/2026; `RETOMAR.md:20-34`; `passport.yaml`; cabeçalho do registro de permutação em `mapa-de-lacunas-e-exploratorio.md` (só para confirmar que o mapa e a saída contam a mesma história).
- Exploratório: os quatro arquivos de saída autorizados; roteiros 20 a 23, lidos por inteiro; listagem de nomes e datas da pasta de saída e de `scripts/exploratorio/`.
