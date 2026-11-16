# Relatório de Verificação de Integridade Acadêmica — rodada 21, Estágio 2.5, verificação 3 (última)

Agente: `integrity_verification_agent` (ARS v3.24.2). Data: 2026-11-16.
Objeto: `paper/projeto/`, versão projeto_v9. O hash `content_hash_v9` do passport
(`sha256:899a55d9…`) foi reproduzido por mim sobre os arquivos em disco: o texto julgado é o v9.
PDF de 30 páginas, gerado às 00:50:08, depois da última edição dos `.tex` (00:49:43) e do `.bib`
(00:47:29). O agente não editou o manuscrito, não rodou script de análise e não tocou em `data/`.
Não viu as correções serem feitas; julgou o texto como está.

## Modo de verificação
Mode 1 (pré-revisão), reverificação após correção, 3ª e última rodada do laço. Escopo: itens
corrigidos, entradas novas da bibliografia, a checagem C2 inteira (a correção mexeu na regra de
decisão e houve cortes para caber em 15 páginas) e o checklist dos 7 modos.

## Veredito
**PASS WITH NOTES** — 0 SERIOUS, 0 MEDIUM, 8 MINOR (5 resíduos de achados antigos, 3 novos), mais notas.

Não há referência fabricada, MAJOR_DISTORTION nem UNVERIFIABLE. Os dois MEDIUM da rodada 2 caíram
para resíduo MINOR. Duas classificações são julgamento meu na fronteira MINOR/MEDIUM e estão
marcadas como tal (resíduos de IL2-MEDIUM-1 e de IL-MEDIUM-1); numa leitura mais dura de qualquer
uma delas o veredito seria FAIL, e a decisão de aceitar a minha leitura é do pesquisador.

**Fora do veredito, e ainda travando o pipeline:** o checklist dos 7 modos segue em **bloqueio**,
com os Modos 3 e 6 SUSPECTED apenas pela regra formal. O veredito PASS WITH NOTES não libera o
Estágio 3 enquanto o pesquisador não responder a esse bloqueio (seção própria).

No Estágio 4.5 qualquer MINOR bloqueia: os oito abaixo terão de estar fechados até lá.

## Destino dos achados da rodada 2

| ID | Destino | Texto atual (arquivo:linha) | Observação |
|---|---|---|---|
| IL2-MEDIUM-1 (regra de decisão) | **PARCIAL** — parte (1) resolvida; parte (2) em parte. Resíduo **MINOR** | `05-metodologia.tex:250-253`: "O efeito plausível é o da especificação principal do análogo equatoriano, cerca de 80 gramas, multiplicado pela fração de nascimentos exposta, para uma grade de frações fixada no plano de análise; decide o valor central da grade." | (1) O ponto do efeito está fixado e é o da fonte: Tabela 3, coluna 2, "a birth weight deficit of 80 grams". "Grade de frações" agora coincide com o Apêndice B (`apendices.tex:60`). Coerente com o quadro da regra (`05:266-269`; Quadro 1 no PDF), com a Seção 3.2 (`03:32-33`, mesmos 80 g; "O valor serve de referência, e não de limite", `03:37`) e com a diluição (`07:26-27`). (2) A divulgação pedida entrou (`05:310-311`: "calculou efeito detectável com o período inteiro"), e não contradiz `05:295-297` (o cálculo que vale para a regra usa só referência e seca). **Resíduo:** a grade, que é componente da regra declarada inalterável (`05:303-305`), continua "fixada no plano de análise", isto é, depois de a rodada de novembro ter mostrado efeitos detectáveis; o "Por isso" de `05:311-312` cobre municípios tratados e estação, não a grade. Julgo MINOR, e não MEDIUM, porque o limiar já tem forma fechada (80 g × fração central), a escolha em aberto está divulgada e só inverteria a linha do quadro com uma grade centrada em fração implausivelmente alta. É julgamento. Pequeno: "cerca de 80 gramas" dentro de uma regra; a fonte dá 80. |
| IL-MEDIUM-1 (resíduo: três fatos sem fonte) | **PARCIAL** — 2 de 3 resolvidos. Resíduo **MINOR** | Ação civil pública: `02-contexto.tex:66-67` e `05:200-201` (`mpt2011apodi`). Seca: `apendices.tex:134` (`rebello2018seca`). **Sem fonte, de propósito:** a notícia de proibição de março de 2011 em `02:65-66`, `05:139` e `apendices.tex:133` | Ver "Nota de 11/03/2011" abaixo. |
| IL-MINOR-3 (resíduo) | **RESOLVIDO** | `05:227-229`: "a versão binária da comparação identificaria, sob as hipóteses do resultado citado," | — |
| IL2-MINOR-1 (atribuição do intervalo) | **RESOLVIDO** | `03-referencial.tex:32-36`: "déficit de cerca de 80 gramas na especificação principal, e de até 150 conforme a exposição, para mães que moravam a até 150 metros do perímetro de um bananal e tiveram três meses ou mais de fumigação intensiva na gestação" | Fiel ao manuscrito de 03/2023, relido nesta rodada: 80 g na especificação principal (seção 5); "between 80 and 150 grams, with an impact that depends on the number of months of exposure" (conclusão); "the total effect depends on the trimesters during which newborns are exposed" (seção 5); limiar de 5 galões, 104,3 g (seção 6.4); exposição = até 150 m e ao menos três meses acima de 4 galões/ha/mês. "Conforme a exposição" é genérico, mas não atribui a causa errada. |
| IL2-MINOR-2 (divulgação das rodadas) | **PARCIAL** — (a) resolvido; (b) em parte; (c) não | `05:305-314` | Ver "Divulgação das rodadas exploratórias" abaixo. |
| IL2-MINOR-3 (cinco leis municipais) | **NÃO RESOLVIDO** | `03:76-79`: "cinco foram conferidas, com datas de 2009 a 2017, mas não a vigência" | Texto idêntico ao da rodada 2. A fonte citada (`lavor2019antes`) não dá número nem data de lei; o leitor não sabe quais cinco nem onde foram conferidas. |
| IL2-MINOR-4 (Dossiê sem página e sem data do relato) | **PARCIAL** | `02:38-39`: `\cite[p.~69 e 152]{carneiro2015dossie}`; `07-ameacas.tex:32-33` segue sem página | Página entrou em um dos dois usos. Não entrou a data do relato (estudo de 2011, em pretérito: "eram realizadas"), que importa porque o texto o põe ao lado de um relato de 2021. |
| IL2-MINOR-5 (caixa inconsistente) | **RESOLVIDO**, com nota de formato | `referencias-projeto.bib` (`stf2025adi7794`, `ceara2018nascer`, `mpt2011apodi`); PDF p. 20-21 | Todas as entradas institucionais saem agora em caixa mista ("Brasil. Supremo Tribunal Federal", 2023 e 2025; "Ceará. …"). A inconsistência acabou. Nota: uniformizou-se no sentido contrário ao da NBR 6023 (jurisdição em maiúsculas), e os autores pessoais seguem em maiúsculas; é formato, para o Estágio 5. |

### Regra de decisão: resposta direta às perguntas do despacho
- **Sem ambiguidade?** Quanto ao efeito, sim: um número, o da especificação principal. Quanto à fração, a regra remete a uma grade ainda não fixada (resíduo acima).
- **Coerente com o resto?** Sim: quadro da regra, Apêndice B, Seção 3.2, Seção 7 e a frase "não o período de referência nem a regra de decisão" não se contradizem. A tensão que resta é a grade ser parte de uma regra inalterável e ainda estar por fixar.
- **A frase da Seção 3.2 é fiel ao artigo?** Sim, conferida no manuscrito de 03/2023 (não na versão tipografada; ver "Não conferido").

### Divulgação das rodadas exploratórias (`05:305-314`)
Texto: "A de novembro estimou o desenho de calendário sobre os nascimentos de 2005 a 2024, com
classificação e estação provisórias e sem a chuva, em variantes de limiar, de grupo tratado e de
comparação, incluída a potiguar, e calculou efeito detectável com o período inteiro: a exposição
sazonal já foi cruzada com o desfecho do pós-lei."

- **Fiel?** Sim, ponto a ponto, ao `mapa-de-lacunas-e-exploratorio.md` §3-4: painel 2005-2024; Censo 2006 e fevereiro a maio provisórios; sem os termos de chuva; limiar 0,5 e 0,75; grupos de 7, 2 e 5 municípios; comparações com o Rio Grande do Norte; efeito mínimo detectável por permutação sobre o coeficiente do pós-lei. Nenhum número entrou no texto.
- **Suficiente?** Para o que o portão exige, sim: o fato que importa (o desfecho do pós-lei já foi visto, em várias variantes, inclusive com cálculo de poder) está dito. Faltam três coisas, todas MINOR:
  1. O "Por isso" (`05:311-313`) tira consequência só para municípios tratados e estação. O **limiar de agricultura familiar**, o **grupo de comparação** (com ou sem a potiguar) e a **grade de frações** também foram variados ou informados pelo desfecho e seguem "a fixar no plano", sem a cláusula de que o critério não usa o desfecho.
  2. O estudo de evento com bases 2018 e 2014, diferentes da base 2011 do projeto (`scripts/exploratorio/23_leads_lags_exploratorio.py`, cabeçalho), não aparece. "Estimou o desenho de calendário" cobre o estudo de evento em geral, não a troca de base.
  3. Continua sem menção o plano da forma reduzida fechado em 21/09/2026 (`docs/pre-especificacao.md:3`). "Duas rodadas exploratórias antecedem o plano" ainda sugere que não havia plano, e "Os planos são versionados" (`05:313`) segue sem antecedente no plural.

### Nota de 11/03/2011 (Secretaria de Direitos Humanos), sem citação: gravidade
**MINOR**, por julgamento, com o seguinte na balança:
- A favor de MINOR: o fato foi conferido na rodada 2 em duas reproduções; o texto é cauteloso ("noticiou-se", "não se localizou instrumento jurídico", `02:65-68`); a fonte do Apêndice D avisa que os eventos de 2011 a 2017 vêm de fontes secundárias (`apendices.tex:143`); a omissão é declarada, não disfarçada.
- A favor de MEDIUM: é afirmação factual que o leitor não consegue rastrear, e ela sustenta uma escolha de desenho (a sensibilidade com referência 2008-2010, `05:139-140`).
- **Agravante novo, de redação:** em `02:65-67` a citação `\cite{mpt2011apodi}` fecha a frase coordenada ("noticiou-se uma proibição [...] e o Ministério Público ajuizou ação civil pública com esse pedido \cite{...}") e pode ser lida como fonte dos dois fatos. Abri a página do MPT nesta rodada: ela **não menciona** proibição anterior, março de 2011, a Secretaria nem a Comissão Nacional de Combate à Violência no Campo.
- **Nesta rodada não consegui reabrir nenhuma fonte da nota:** SINAIT, tempo esgotado duas vezes; a ficha do Mapa de Conflitos da Fiocruz, no endereço registrado na rodada 2, devolveu 404; duas buscas não trouxeram a nota. O fato apoia-se, portanto, só na leitura por extrato feita na rodada 2.
- Correções possíveis, em ordem de custo: (a) deslocar a citação do MPT para junto de "ação civil pública", de modo que não cubra a notícia; (b) abrir a página do SINAIT no navegador e citá-la como reprodução (apud SDH), com data de acesso; (c) se não abrir, retirar a notícia de `02:65-66`, `05:139` e `apendices.tex:133` e apoiar a sensibilidade 2008-2010 no que tem fonte: o projeto de lei de maio de 2011 (`ceara2011pl134`) e a ação de julho de 2011 (`mpt2011apodi`).

## Achados novos

Nenhum SERIOUS. Nenhum MEDIUM.

### MINOR

| ID | Local | Texto | Problema | Fonte | Correção sugerida |
|---|---|---|---|---|---|
| IL3-MINOR-1 | `07-ameacas.tex:43-44` | "O registro de óbito fetal tem subnotificação e contagens quase sempre nulas por município e mês" | O corte mudou o sentido de uma afirmação sobre os dados: antes, "quase sempre zero ou um"; agora, "quase sempre nulas". Nenhuma das duas tem fonte, e a nova é mais forte. Para os municípios maiores do grupo tratado, "zero ou um" é a descrição mais plausível. Não conferi nos dados (fora do mandato). | `git diff -- paper/projeto/secoes/07-ameacas.tex` | Voltar a "quase sempre zero ou um" ou escrever "contagens muito baixas por município e mês". |
| IL3-MINOR-2 | Lista de referências, PDF p. 20; `referencias-projeto.bib` (`mpt2011apodi`) | URL da entrada do MPT | O endereço não quebra e ultrapassa a margem em 135 pt (`projeto.log:1396`, "Overfull \hbox"): sai da página, e o final ("…licenciamentos-ambientais") não é legível no impresso. Introduzido pela entrada nova. | `projeto.log`; texto extraído do PDF | Usar o endereço curto, que a rodada 2 registrou como válido (`…/noticias-do-mpt-ce/534-`), ou permitir quebra de URL em hífen. Conferir o endereço curto no navegador antes. |
| IL3-MINOR-3 | `06-dados.tex:21-23` | "…e as de arboviroses, como controle (Apêndice~\ref{ap:espec})." | A remissão nova resolve (`ap:espec` existe) e entrega as intoxicações (linha $H_5$, `apendices.tex:111`, com a ressalva das intencionais preservada). Mas fica colada às arboviroses, e o Apêndice C não tem especificação alguma com arboviroses como controle. A lacuna é anterior; a remissão passou a prometer o que o apêndice não traz. | `apendices.tex:96-111` | Mover a remissão para depois de "canal de substituição", ou acrescentar ao Apêndice C a linha das arboviroses. |

### Cortes e deslocamentos: resultado da conferência
| Corte | Removeu ressalva substantiva? | Quebrou remissão? |
|---|---|---|
| `07`: "As fontes da suspensão dos voos são de imprensa e de parte interessada" → "sem registro administrativo" | Não: a natureza das fontes continua em `02:68-74` (moradora, produtor; "Nenhuma delas vem de registro administrativo"). Perdeu-se só a expressão "parte interessada". | Não |
| `07`: "este projeto diz de antemão qual efeito consegue detectar" | Não: está em `08-cronograma.tex:10-11` (item ii) e no resumo (`projeto.tex:94-95`). | Não |
| `07`: outras fontes de sazonalidade | Não: sentido equivalente. | Não |
| `07`: óbito fetal | **Sim, em parte**: IL3-MINOR-1. | Não |
| `06`: intoxicações intencionais para o Apêndice C | Não: frase e ressalva estão em `apendices.tex:111`. | Remissão imprecisa: IL3-MINOR-3 |
| `06`: remissão ao Apêndice A encurtada | Não. | Não |
| `02`: "Trata-se de fungicida e inseticida sobre fruta irrigada." | Não: a frase anterior já nomeia "o fungicida procimidona e o inseticida carbaril" (`02:45-46`). | Não |
| `05`: rodada de setembro encurtada | Não cria erro; mantém aberto o item (c) do IL2-MINOR-2. | Não |

Todas as 14 remissões (`\ref`) têm rótulo definido; zero "??" no PDF; nenhum aviso de referência no `.log`.

### Notas (não contam no veredito)
- `05:23` e o resumo citam a seca de 2012-2017 sem fonte; a citação está só no Apêndice D. Basta repetir `\cite{rebello2018seca}` em `05:23`.
- `mpt2011apodi`: a página não traz local na assinatura ("Escrito por ASCOM"); "Fortaleza" é a sede da Procuradoria. Também não traz a data do ajuizamento: "julho" (`apendices.tex:133`) é a data da notícia. Não traz número de processo, que a consulta prevista no cronograma vai exigir.
- Deriva de força das afirmações nesta leva (E6, feita à mão): nenhuma afirmação ficou mais forte que a fonte, salvo IL3-MINOR-1. Os artefatos formais do E6 (arquivo de achados e de disposição) não foram gerados.
- Calzada et al.: todas as conferências são contra o manuscrito de 03/2023; a entrada cita a versão do JAERE. Formalmente UNVERIFIABLE_ACCESS para a versão citada (nota, não bloqueia).

## Bibliografia: entradas novas

| Chave | Metadados | Uso no texto | Veredito |
|---|---|---|---|
| `mpt2011apodi` | **Abri diretamente nesta rodada.** Título confere, palavra por palavra; "Escrito por ASCOM", 07 de julho de 2011; sítio da PRT da 7ª Região. | `02:66-67` ("o Ministério Público ajuizou ação civil pública com esse pedido") e `05:200-201`. Sustentado: MPF, MPT e MP estadual, "ação civil pública" contra a Fapija e quatro empresas, 15ª Vara da Justiça Federal em Limoeiro do Norte; pede a proibição da pulverização aérea na Chapada. Não sustenta a notícia de março (ver acima). | VERIFIED; IL3-MINOR-2 (URL) |
| `rebello2018seca` | Autor, título ("na história do Brasil") e data (3 mar. 2018) iguais aos conferidos na rodada 2 por extrato de serviço de busca. **Nesta rodada não abriu:** UOL bloqueado, Internet Archive bloqueado, busca pelo título sem retorno. | `apendices.tex:134` ("Seca no semiárido", 2012-2017). Sustentado pelo trecho lido na rodada 2. Fonte jornalística para fato climático: aceitável em quadro de cronologia. | VERIFIED por herança da rodada 2; abrir no navegador antes de gravar a data de acesso |

Citações: 56 chaves citadas, 56 itens no `.bbl`, nenhuma indefinida, nenhuma órfã, `projeto.blg` sem aviso.
As outras 54 entradas não foram reverificadas (protocolo de reverificação).

## Fase C — reverificação

**Número de estimativa própria: nenhum.** Varredura dos `.tex` e do texto do PDF. Números com
unidade: 23 a 32 g e 80 g/150 g (literatura); 2.500 g, 37 semanas e 150 m (definição). A divulgação
das rodadas exploratórias não traz número.

Consistência interna (C2):
- Períodos e coortes: referência 2007-2011; transição 2012 e 2019 fora; seca = nascidos de 2013 a 2018; pós = nascidos a partir de 2020; janela até 19/12/2024; estudo de evento com base 2011 e 2005-2010 como pré-tendência; sensibilidades 2008-2010 e sem 2020-2021. Coincidem entre o resumo, as Seções 4, 5 e 6 e os Apêndices B, C, D e E.
- O que é confirmatório: uma hipótese, peso ao nascer (`04:27-31`, `05:297-299`, `06:13-15`, Apêndice C linha $H_1$). A última linha do quadro da regra ("declarado exploratório") é coerente com a rodada de novembro já ter rodado essa especificação.
- Listas de testes: seleção (óbito fetal, desfecho composto, nascidos vivos por coorte, razão de sexo) idêntica em `07:42-43`, Apêndice B, C e E. Falsificação (tratamento falso, composição materna, sem 2020-2021) coerente entre `05:152-155` e os apêndices.
- Regra de decisão: coerente; resíduo sobre a grade.

Páginas: 30 no PDF; textuais de 5 a 19 (**15 páginas**, sem folga); **Referências começam na p. 20**
(`projeto.toc` e PDF); apêndices de 25 a 29.

C4: passport com `experiment_intake_declaration` completo; nenhuma das cinco condições de FAIL se
verifica (não há manifesto, seção de resultados nem métrica própria reportada). O que o texto
divulga pesa no checklist, abaixo.
"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the
experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

Restrições do passport: "só o Ensaio 1", "até 15 páginas textuais" e "nenhum número de estimativa" respeitadas.

## Checklist dos 7 modos de falha de pesquisa com IA

Regra aplicada: a declaração é `no_experiments_declared` ("Não reporta"). Se o texto, ainda assim,
apresenta análises de dados como feitas pelo autor, declaração e texto discordam: nenhum dos Modos
1, 3, 5 e 6 é NOT APPLICABLE, e os Modos 3 e 6 ficam SUSPECTED. O texto apresenta: "A de setembro
de 2026 estimou a forma reduzida estadual"; "A de novembro estimou o desenho de calendário [...] e
calculou efeito detectável" (`05:306-311`); "um levantamento preliminar encontrou uma proibição"
(`06:30`); "Avaliações preliminares [...] indicaram limitações" (`06:37-38`). A regra dispara.

| Modo | Resultado | Regra formal ou mérito | Evidência | Bloqueia? |
|---|---|---|---|---|
| 1. Erro de implementação que passa na autorrevisão | CLEAR | mérito | Nenhum resultado numérico próprio no texto; as perguntas de detecção não têm objeto. Não vi registros de execução. | não |
| 2. Citação alucinada | CLEAR | mérito | 56 de 56 referências existem (54 por rodadas anteriores, 2 novas nesta). | não |
| 3. Resultado experimental alucinado | **SUSPECTED** | **só regra formal** | Declaração "Não reporta" contra frases que apresentam análises próprias como feitas. No mérito, nada a suspeitar: nenhum número; o que se narra confere com o registro do repositório. | **sim** |
| 4. Atalho | CLEAR | mérito | Não há resultado; o desenho prevê tratamento falso, placebo de composição e estudo de evento. | não |
| 5. Erro reapresentado como achado novo | CLEAR | mérito | Nenhuma ocorrência de "surpreendente", "inesperado" ou equivalente. | não |
| 6. Fabricação de metodologia | **SUSPECTED** | **só regra formal** | A Metodologia descreve as rodadas como o `mapa-de-lacunas-e-exploratorio.md` as descreve; o que falta é omissão menor (itens 1 a 3 da divulgação), não fabricação. Não vi configuração nem registro de execução; no mérito, o máximo que afirmo é "sem contradição conhecida". | **sim** |
| 7. Travamento de enquadramento | INSUFFICIENT EVIDENCE | mérito | Seguem abertas as escolhas que a rodada de novembro devolveu (7 ou 2 municípios tratados; Rio Grande do Norte como segunda comparação). A regra de decisão prevê o cenário sem poder, o que pesa contra o travamento. Depende de resposta do pesquisador. | não (aviso; rever no 4.5) |

**Estado: bloqueio, por dois modos, ambos só pela regra formal.** Não é achado das Fases A a E e
não muda o veredito. Só o pesquisador destrava, modo a modo. O protocolo dá três opções:

1. **Confirmar o sinal** e voltar ao Estágio 2 (ou antes) para corrigir. Não se aplica no mérito: não há resultado alucinado nem método fabricado a corrigir.
2. **Afastar com justificativa registrada.** O pesquisador declara por que o sinal é falso positivo, e a justificativa vai para o registro do Estágio 6. Justificativa disponível: as duas rodadas existem, estão divulgadas no texto, nenhum resultado delas é reportado (que é o sentido de "Não reporta"), e a divulgação foi posta ali para corrigir o IL-SERIOUS-1.
3. **Revisar a passagem e repetir a checagem.** Só silencia a regra se o texto deixar de apresentar análises como feitas, o que exigiria retirar a divulgação e recriaria o IL-SERIOUS-1. Não recomendo.

Consequências a conhecer: (i) enquanto o texto divulgar as rodadas e a declaração for
`no_experiments_declared`, a regra dispara de novo em qualquer reverificação, inclusive no 4.5,
onde um modo SUSPECTED no 2.5 só fecha como CLEAR, NOT APPLICABLE ou afastado com justificativa: a
opção 2 terá de ser registrada. (ii) Trocar a declaração para `experiments_declared` não está
entre as três opções; faria os Modos 1, 3, 5 e 6 dependerem de registros de execução e abriria a
checagem de proveniência (C4) sobre rodadas que o projeto, de propósito, não reporta.

## Não conferido (com o motivo)

1. **Nota da SDH de 11/03/2011** — nem o original nem as reproduções abriram nesta rodada (SINAIT: tempo esgotado, duas tentativas; ficha da Fiocruz no endereço da rodada 2: 404; duas buscas sem retorno). Vale só a leitura por extrato da rodada 2.
2. **Reportagem do UOL (`rebello2018seca`)** — acesso direto e Internet Archive bloqueados; busca pelo título sem retorno. Vale a leitura por extrato da rodada 2.
3. **Calzada et al., versão tipografada do JAERE** — não aberta; conferido o manuscrito de 03/2023 (PDF do repositório da Universidade de Barcelona, texto extraído e lido). Apêndice online não aberto.
4. **Ação civil pública de 2011** — número, andamento e desfecho: consulta processual não tentada.
5. **Cinco leis municipais de outros estados** (`03:76-79`) — não reconferidas; apoio na rodada 1.
6. **Rodada de setembro de 2026** — "estimou a forma reduzida estadual, cujo alvo foi revisto, da curva para o nível" não foi conferido contra registro de execução; só a existência e a data de `docs/pre-especificacao.md`.
7. **Scripts `scripts/exploratorio/20-23`, registros de execução e dados** — fora do mandato; do script 23 li só o cabeçalho. A fidelidade da divulgação foi medida contra o `mapa-de-lacunas-e-exploratorio.md`, não contra as saídas.
8. **Contagens de óbito fetal por município e mês** (IL3-MINOR-1) — não conferidas nos dados.
9. **As 54 referências não tocadas** — não reverificadas; valem os resultados e as lacunas da rodada 1.
10. **Originalidade (D1 por busca na web, D2)** — não executadas, como nas rodadas anteriores. Os trechos novos são paráfrases com citação.
11. **Semantic Scholar (A0), registro de afirmações e linhas de evidência persistidas (E1, E1.1, E3.1), artefatos do E6** — não gerados; verificação feita por leitura direta de fonte primária.
12. **Endereço curto do MPT** sugerido em IL3-MINOR-2 — não aberto nesta rodada.

## Em aberto para decisão do pesquisador (última rodada)

1. **Bloqueio dos Modos 3 e 6**: escolher entre as três opções; a que mantém a divulgação é afastar com justificativa registrada.
2. **Aceitar ou não as duas classificações de fronteira** (grade da regra de decisão; nota de março de 2011 sem fonte) como MINOR. Se não aceitar, o veredito é FAIL com dois MEDIUM e o laço de três rodadas se esgotou: a entrada no Estágio 3 dependeria de decisão explícita e registrada sobre esses itens.
3. **Grade de frações**: fixá-la já no projeto (uma oração) ou declarar que será fixada por critério que não usa o desfecho.
4. **Nota de 11/03/2011**: citar a reprodução depois de abri-la no navegador, deslocar a citação do MPT, ou retirar o fato.
5. **Divulgação**: estender o "Por isso" ao limiar de agricultura familiar e ao grupo de comparação; mencionar o plano de setembro.
6. **Cinco leis municipais** (`03:76-79`): nomear, citar fonte primária ou cortar a oração. Não foi tocado em duas rodadas.
7. **Dossiê**: página em `07:33` e data do relato.
8. **IL3-MINOR-1, 2 e 3**: três correções de uma linha. Qualquer acréscimo precisa caber em 15 páginas, hoje sem folga.
9. Do passport, ainda sem resposta: grupo tratado provisório (7 municípios ou 2), Rio Grande do Norte como segunda comparação, reconhecimento do Estágio 6 da rodada 20, painel cego no Estágio 3.
10. Versão publicada de Calzada et al.: obter o PDF por acesso institucional para fechar o UNVERIFIABLE_ACCESS antes do 4.5.

## Aviso de limitação da ferramenta

> A checagem de originalidade (Fase D) não usou busca de frases na web nem software de detecção
> de plágio (Turnitin, iThenticate). Vale como triagem preliminar; recomenda-se ferramenta
> profissional antes da entrega formal.

Este relatório verifica as populações registradas acima. Não garante a completude da extração de
afirmações, a verdade do que está nas fontes, nem a correção de análises que não examinei.

## Trilha de auditoria

Abertos diretamente nesta rodada:
`www.prt7.mpt.mp.br/informe-se/noticias-do-mpt-ce/534-agrotoxicos-no-apodi-mps-pedem-a-justica-o-fim-da-pulverizacao-aerea-e-revisao-de-licenciamentos-ambientais` (duas leituras: metadados e conteúdo);
`diposit.ub.edu/server/api/core/bitstreams/73f71bc2-9e61-4f15-a2de-a58cb08d43ac/content` (PDF baixado, texto extraído; resumo, seções 4.2, 5, 6.4 e 7 lidas).

Falharam: `sinait.org.br/noticia/2874/…` e a variante `?print` (tempo esgotado);
`mapadeconflitos.ensp.fiocruz.br/conflito/ce-uso-indiscriminado-…` (404);
`noticias.uol.com.br/…/seca-de-2012-a-2017-…` (bloqueado); `web.archive.org/web/20261019170109/…` (bloqueado).

Buscas (três): nome da região e dos órgãos da nota de 2011; título da reprodução do SINAIT; título
e autor da reportagem do UOL. Nenhuma trouxe o documento procurado. Nenhum nome de pesquisador nem
trecho do projeto foi enviado a buscador.

Locais: `git diff -- paper`; `projeto.pdf` (texto extraído), `projeto.toc`, `projeto.aux`,
`projeto.bbl`, `projeto.blg`, `projeto.log`; datas de arquivo; `passport.yaml` (hash v9
reproduzido); `mapa-de-lacunas-e-exploratorio.md`; `conferencia-local-fontes.md`; relatórios das
rodadas 1 e 2; cabeçalho de `scripts/exploratorio/23_leads_lags_exploratorio.py`;
`docs/pre-especificacao.md` (linhas 1-12).
