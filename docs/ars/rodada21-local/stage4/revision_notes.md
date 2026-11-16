# Notas de revisão — rodada 21, Estágio 4 (16/11/2026)

Acompanha `response_to_reviewers.md`. Trata de três coisas: o que foi cortado ou movido para o corpo caber em 15 páginas, o que foi feito com cada pendência do verificador de integridade, e o que ficou sem resolver.

## 1. Estado da compilação

Compilado com `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, a partir de `paper/projeto`.

| Conferência | Resultado |
|---|---|
| Página das Referências (`projeto.toc`) | 20 |
| Páginas textuais | 5 a 19; a página 19 tem cerca de seis linhas de folga |
| Erros no `projeto.log` | nenhum |
| Citações ou referências indefinidas | nenhuma |
| "??" no PDF | nenhum |
| `Overfull \hbox` | nenhum |
| `Float too large` | nenhum (apareceram dois nos Apêndices B e C e foram resolvidos dividindo os quadros) |
| Número de estimativa própria no texto | nenhum |
| Codificação e fim de linha dos `.tex` e do `.bib` | UTF-8 sem BOM, LF (o `04-objetivos.tex` estava em CRLF e foi convertido) |
| Total de páginas do PDF | 38 |

Os números que aparecem no texto são de desenho ou da literatura: nível de 5%, poder de 80%, magnitudes de 40, 80 e 150 gramas, frações de 0,05 a 0,50 e os produtos do Quadro da grade. O Quadro diz que são produtos de desenho, não estimativas.

## 2. Cortes e deslocamentos

A primeira versão revisada passou o limite em cerca de uma página e meia. O que segue trouxe o corpo de volta às 15 páginas.

### Deslocamentos para apêndice

| O que saiu do corpo | Destino | Ressalva preservada? |
|---|---|---|
| Figura 1, diagrama causal (Seção 5.2) | Apêndice E, antes do quadro que a explica. O corpo remete ao apêndice. | Sim, inteira. É o maior ganho de espaço (cerca de 17 linhas). **Decisão que o pesquisador pode querer reverter.** |
| Detalhe do portão de poder: grade, valor que decide, definição do efeito detectável | Apêndice F, Seção F.3 | Sim; o corpo guarda a faixa, a célula que decide (80 gramas e fração de 0,25) e a remissão. |
| Casos sem linha, critério de pico, regra de A_m, completude | Apêndice F, Seções F.1 e F.2 | Sim. |
| Lista de variantes das rodadas exploratórias e a separação entre escolhas anteriores e posteriores | Apêndice F, Seção F.6 | Sim. O corpo guarda o fato central (o desfecho do pós-lei já foi cruzado) e os três compromissos. |
| Estatística de inferência e tratamento da contiguidade | Apêndice F, Seção F.4; o corpo guarda duas frases | Sim. |
| Argumento de suficiência por linha (REV-01) | Apêndice F, Seção F.5 | Sim. Fica menos visível para a banca do que no corpo. |
| "Um hiato achado por acaso no pré-período regrediria no pós-lei" (antiga Seção 5.3) | Apêndice B, linha "Hiato sazonal achado por acaso" | Sim. |
| Parágrafo "A diluição" do Cap. 7 | Apêndice B, linha "Diluição dentro do município", com o texto ampliado. O Cap. 7 passou a comentar três ameaças, não quatro. | Sim. A lógica da diluição continua no corpo, na segunda regularidade do Cap. 3. |
| "O registro de óbito fetal tem subnotificação e contagens quase sempre de zero ou um" (Cap. 7) | Apêndice B, linha "Seleção para o nascimento vivo" | Sim, com a redação "zero ou um". |
| "Outras fontes de sazonalidade do peso só ameaçam se diferirem entre os grupos" (Cap. 7) | Apêndice B, linha própria | Sim. |
| "Avaliações preliminares do monitoramento da água e do mapeamento por satélite" (Cap. 6) | Apêndice A, última linha | Sim. |
| Citações das fontes complementares (Lei 12.228, Decreto 4.074, notícia da ação) na Seção 5.3 | Apêndice A, nas linhas correspondentes | Sim; as três entradas continuam citadas. |
| Versão saturada e versão linear de P_t (Seção 5.2) | Já estavam no Apêndice C; a frase do corpo saiu | Sim. |
| Convenções de P_t, da chuva e dos vizinhos | Apêndice C, parágrafo "Convenções" (texto novo) | — |

### Cortes sem destino (redundância)

| Trecho cortado | Onde a informação continua |
|---|---|
| Equação θ = VPP × ATT e sua explicação (REV-34) | Uma frase na Seção 5.5, com a citação de Denteh e Kédagni |
| Frase sobre Larsen e coautores na Introdução | Cap. 3, segunda regularidade |
| "Concentrada na cauda inferior" (Reynier e Rubin, Introdução) | Cap. 3, segunda regularidade |
| "A comparação entre proibir e taxar é antiga" com três citações (Introdução) | Cap. 3, Seção 3.1, com as mesmas citações |
| Constitucionalidade e replicabilidade repetidas na Contribuição | Justificativa, com a citação do julgamento |
| "Não há variação de timing" na Contribuição | Cap. 3, Seção 3.3 |
| Abertura da Seção 3.1 (quem paga e quem arca) | Cap. 1, segundo parágrafo; a Seção 3.1 remete a ele |
| Callaway e Sant'Anna "vale, com uma única data, nas comparações com outros estados" (Seção 3.3) | **Não continua.** Era observação, não ressalva. A entrada segue citada na mesma seção. |
| "Cinco [leis municipais] foram conferidas, com datas de 2009 a 2017, mas não a vigência" (Seção 3.3) | **Não continua.** Pendência do verificador: a oração não dizia quais. |
| Parágrafo final da Seção 3.3 sobre inferência com poucos grupos | Seção 5.7, com as mesmas citações |
| Rigotto e coautores: "mais internações por neoplasias" | **Não continua.** Fica o resultado sobre óbitos fetais, que é o que toca o projeto. |
| "A população é de coortes, e não de municípios" (Seção 5.1) | **Não continua** como frase; a definição de τ por coorte a contém. |
| Regressão de efeitos fixos "não é em geral válida na diferença tripla" (parágrafo do grupo de comparação) | Seção 3.3, terceiro resultado |
| "Há uma única hipótese confirmatória" (Seção 5.7) | Cap. 4, parágrafo de hipóteses |
| "Se os registros não chegarem até o fim do terceiro, segue-se com a classificação provisória" (Cap. 8) | Linha 6 do Quadro da regra |
| Linha "Início do segundo ensaio" do cronograma | Fora do escopo declarado (REV-06) |
| Título de seção "Diagnóstico descritivo do pré-período" | Virou parágrafo com título em negrito na Seção 5.2. A numeração das seções do Cap. 5 mudou: são sete, não oito. |
| Notícia de proibição de março de 2011 (Cap. 2 e Cap. 5) | Ver pendência 6 abaixo |

## 3. Pendências do verificador de integridade (rodada 3)

| Pendência | O que foi feito |
|---|---|
| 1. Grade de frações ainda "a fixar no plano" | Fixada no projeto: `apendices.tex`, Seção F.3 e Quadro da grade. O texto diz que os valores não têm fonte. |
| 2. Alcance do "Por isso" na divulgação das rodadas | Os parâmetros abertos passam a ser fixados "por critério escrito sem uso do desfecho" (`05:289-291`). O Apêndice F diz quais foram variados em novembro (grupo tratado, limiar de agricultura familiar, comparação potiguar) e registra o roteiro de estudo de evento com bases em 2014 e 2018. |
| 3. Plano de setembro sem menção | Mencionado no corpo (`05:285-286`) e no Apêndice F: plano fechado em 21 de setembro de 2026, alvo revisto no dia seguinte. |
| 4. "Cinco leis municipais" sem dizer quais | Oração cortada. Fica a citação da reportagem e a extensão possível. |
| 5. Página do Dossiê no Cap. 7 e data do relato | `07:24-25`: "relato, de 2011 e no pretérito", com a página 152. |
| 6. Nota de 11/03/2011 sem fonte | Retirada do corpo (Cap. 2 e Cap. 5). A citação do Ministério Público do Trabalho cobre agora só a ação civil pública. A sensibilidade com 2008 a 2010 apoia-se no projeto de lei de maio de 2011 e na ação de julho. No Apêndice D a nota fica registrada como "pista a conferir nos autos, e não como fato". Não tentei reabrir a reprodução. |
| Nota: seca de 2012 a 2017 sem fonte no Cap. 5 | Citação acrescentada (`05:32`). |
| Nota: "julho" é a data da notícia, não do ajuizamento | Dito na fonte do Quadro da cronologia. |
| IL3-MINOR-1 (óbito fetal, "quase sempre nulas") | Já estava corrigido; a redação "zero ou um" foi para o Apêndice B. |
| IL3-MINOR-2 (endereço que ultrapassa a margem) | Já estava resolvido; a compilação não acusa `Overfull`. |
| IL3-MINOR-3 (remissão colada às arboviroses) | Já estava corrigida; o papel das arboviroses foi explicitado (`06:27-28`). |
| Itens 1, 2, 9 e 10 da lista "em aberto" (bloqueio dos modos, aceitação das classificações, perguntas do passport, versão publicada de Calzada) | Não são matéria desta revisão. Continuam com o pesquisador. |

## 4. Decisões que tomei e que o pesquisador deve conferir

Além dos cinco pontos provisórios do orquestrador, a carta exigia valores e regras que ninguém havia fixado. Escolhi a opção mais simples em cada caso e marquei no texto o que não tem fonte.

1. **Célula decisória do portão: 80 gramas e fração de 0,25.** Ao escolher, eu já tinha lido os valores de efeito detectável da rodada de novembro em `mapa-de-lacunas-e-exploratorio.md`. Com aqueles valores (calculados com o período inteiro e por outro procedimento), o portão fica fechado na célula escolhida e em todas as células de 40 e de 80 gramas; só a célula de 150 gramas e 0,50 o abriria, e apenas para o grupo de sete municípios. A escolha não é, portanto, pivotal em relação ao que já foi visto, mas não foi feita às cegas. O Apêndice F declara que os critérios foram escritos por quem conhecia os resultados.
2. **Linha 5 definida por 2018.** A seca vai até 2017 no texto, de modo que 2018 é o único ano entre o fim da seca e a lei. A ausência de voo num único ano é evidência fraca de que a prática cessou, e o Apêndice F o diz: ela impede a atribuição à lei, mas não demonstra que os voos não voltariam.
3. **Rótulo de reestimação.** Se municípios e estação medidos coincidirem com uma variante já estimada, o resultado deixa de ser chamado de confirmatório. É a sugestão do parecer de metodologia (W1, item iv). É o compromisso mais custoso da revisão: os sete municípios do Censo de 2006 e os dois da Chapada já foram estimados.
4. **Chuva indexada pela quadra de exposição.** Para as coortes nascidas em janeiro e fevereiro, a chuva passa a ser a do ano anterior. A notação mudou de `C_{m,a(t)}` para `C_{m,q(t)}`. Afeta só o controle das coortes intermediárias. É precisão, mas altera a regressão em relação ao que o roteiro exploratório faria.
5. **Vizinhos imediatos fora do grupo de comparação.** O texto dizia "três grupos" sem dizer onde os vizinhos ficam na especificação principal. Escrevi que ficam fora. É a minha leitura.
6. **Relação de operadores registrados.** O critério de completude depende dela. As minutas de pedido de acesso em `docs/legislacao/` precisam recebê-la; não as alterei.
7. **Horários no Apêndice F.** Os horários das versões vêm do `git log` (convertidos para o horário de Brasília). Os dos roteiros exploratórios vêm da data de modificação dos arquivos em `scripts/exploratorio/`, que não estão no repositório. É evidência fraca, e o texto diz que o intervalo é de horas.
8. **Rodada de setembro.** A descrição das variantes de setembro no Apêndice F é genérica. Baseia-se no `CLAUDE.md` e em `docs/pre-especificacao.md`, não numa leitura dos roteiros. O pesquisador deve completá-la antes do depósito.
9. **Contagem de páginas.** Há cerca de seis linhas de folga na página 19. Qualquer acréscimo acima disso empurra as Referências para a página 21.

## 5. O que não foi resolvido

- **REV-17**: protocolo e data da busca bibliográfica. Não os encontrei nesta ramificação.
- **REV-18 e REV-23**: página do Dossiê para a tabela de análises de água.
- **REV-19 e REV-22**: estimativas por trimestre e localizadores dos 150 gramas e da faixa de 23 a 32 gramas. A versão publicada de Calzada e coautores continua sem ser aberta; o localizador dos 80 gramas é do manuscrito de 2023.
- **REV-28**: se houve dispersão aérea contra vetores no Ceará antes de 2019.
- **REV-29**: limiar de supressão, nível de agregação e guarda dos documentos; conferência ética para registros identificados.
- **REV-31**: tramitação oficial da votação de 2018; séries de precipitação para datar a seca; número da ação de 2011. Da lei municipal de 2009 li número, data e ementa na página oficial; não abri o PDF do texto integral.
- **REV-33**: o valor do efeito mínimo detectável, por restrição do pesquisador.
- **Depósito público** do plano e do material exploratório: é compromisso no texto, não fato.
- **Protocolo de *patch* do modo `revision`**: não executado. Não há *sidecar* de adjudicação, relatório de aplicação nem pacote de evidência. O passport e o livro-razão da rodada não foram atualizados.
- **`CLAUDE.md`** e as minutas de pedido de acesso não foram atualizados para refletir a regra nova.
- **Comentário de cabeçalho** de `projeto.tex` ainda manda compilar com `make projeto`, que não funciona.
- O texto revisado ainda não passou pela reverificação do Estágio 3'.

## 6. Referências

| Entrada | Situação | Como foi conferida |
|---|---|---|
| `rambachan2023credible` | Já estava em `paper/referencias.bib`; passou a ser citada (Seção 5.2 e Apêndice F) | Crossref, DOI 10.1093/restud/rdad018: título, autores, periódico, volume 90, número 5, páginas 2555 a 2591 |
| `limoeiro2009lei1478` | Nova, em `referencias-projeto.bib` | Página oficial `camaralimoeirodonorte.ce.gov.br/leis/549`, aberta em 16/11/2026: número 1478, data 20/11/2009, ementa. O PDF do texto integral não foi aberto. |

Nenhuma das quatro referências sugeridas pelo parecer de domínio entrou.

## 7. Adendo da segunda revisão (Estágio 4', 16/11/2026)

Os resíduos da re-revisão foram aplicados; o registro está em `response_to_residuals.md`. As Referências continuam na página 20 e a página 19 ficou cheia: não há mais folga. As siglas saíram da nota do Quadro de fontes e viraram um parágrafo no início do Apêndice A, porque a nota alongada empurrava o quadro para uma página sozinha. A afirmação da resposta de que a revisão "não muda o grupo de comparação" valia só para o conceito: os vizinhos imediatos saíram da comparação principal, e a resposta agora o diz.
