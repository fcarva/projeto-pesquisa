# Relatório de Verificação de Integridade Acadêmica — rodada 21, Estágio 2.5

Agente: `integrity_verification_agent` (ARS v3.24.2). Data: 2026-11-16.
Objeto: `paper/projeto/` (projeto_v7; commit `b63069c` nos arquivos do projeto, sem
alteração local em `paper/`), PDF de 29 páginas, 15 textuais (numeradas 5–19, conferido).
O agente não editou o manuscrito, não rodou script de análise e não tocou em `data/`.

## Modo de verificação
Verificação inicial (Mode 1, pré-revisão), com a lista mínima do `LEIA-PRIMEIRO.md`.

## Veredito
**FAIL** — 2 SERIOUS, 1 MEDIUM, 9 MINOR, mais notas.

Nenhuma referência é fabricada: as 51 citadas existem e os metadados conferem. As duas
falhas graves são de afirmação, não de referência, e coincidem com as duas decisões que o
pesquisador deixou em "Decido depois". O portão registra; a escolha de como corrigir é dele.

Fora do veredito (regra do protocolo): o checklist dos 7 modos dá **bloqueio** por Modos 3
e 6 SUSPECTED, que só o pesquisador destrava (ver seção própria).

## Cobertura (denominadores)

| Categoria | Total | Sem problema | Com achado |
|---|---|---|---|
| Referências citadas no projeto (chaves `\cite`/`\citeonline` distintas) | 51 | — | — |
| Existência (Fase A1) | 51 | 51 | 0 |
| Exatidão bibliográfica (A2) | 51 | 46 | 5 (todos MINOR: 1 desatualizada, 4 de detalhe) |
| Citação pendente (no texto, fora da lista) | 0 | — | 0 |
| Entradas órfãs nos `.bib` | 29 de 80 | não são impressas (bibtex só lista as citadas) | 0 |
| Ocorrências de citação no texto (Fase B) | 82 | 82 conferidas contra a fonte ou o resumo | 3 |
| Números e datas do texto (Fase C) | todos os localizados | ver C1 | 0 erro de número |
| Número de estimativa própria | 0 encontrado | — | 0 |
| Afirmações registradas (Fase E, registro abaixo) | 58 | 51 VERIFIED (três com ressalva: linhas 16, 21 e 28) | 2 MAJOR_DISTORTION, 3 MINOR_DISTORTION, 2 verdadeiras mas sem fonte na lista (uma terceira está dentro da linha 8); 1 UNVERIFIABLE_ACCESS como nota |
| Originalidade D1 (busca de frases na web) | — | **não executada** (ver "Não conferido") | — |

Como cada referência foi conferida:

| Via | Quantas | Quais |
|---|---|---|
| Metadados por Crossref (`api.crossref.org/works/<DOI>`), campo a campo | 30 | os 29 artigos com DOI e o NBER WP 32117 |
| Metadados por arXiv (PDF baixado) | 2 | Denteh e Kédagni; Ortiz-Villavicencio e Sant'Anna |
| Fonte oficial aberta e lida | 12 | Leis 16.820, 12.228, 19.135; PL 134/2011; PL 18/2015; Lei municipal 1.511 (PDF local, p. 65–67); IN MAPA 2/2008; Portaria MAPA 298/2021; Decreto 4.074; Res. CNS 510; ADI 6137; Consolidação SINASC 2011 |
| Dado público consultado na API do IBGE | 3 | SIDRA 1008, 1612/1613, 6955 |
| Página de imprensa aberta e lida | 4 | Agência Brasil 2016; Globo Rural 2021; Agência Pública 2019; nota de 26/03/2018 |
| **Conteúdo conferido no texto integral** (versão aberta) | 26 | Baker et al. (arXiv v3); Callaway e Sant'Anna (arXiv v4); de Chaisemartin e D'Haultfœuille (arXiv v7); Goodman-Bacon (NBER WP 25018); Callaway, Goodman-Bacon e Sant'Anna (arXiv v8); Ortiz e Sant'Anna (arXiv v3); Denteh e Kédagni (arXiv v3); Calzada et al. (manuscrito mar/2023); Reynier e Rubin (PNAS); Rigotto et al. (SciELO); Olden e Møen (OUP, aberto); Larsen et al. (PMC); Buckles e Hungerman (PMC); Pereira e Cuellar (SciELO); Weitzman (PDF); mais as 12 fontes oficiais, menos a ADI (trechos do acórdão) |
| Conteúdo conferido só por resumo do editor | 14 | Dias et al.; Rocha e Soares; Brainerd e Menon; Currie e Schwandt; Jones; Ferman e Pinto; MacKinnon e Webb; Hagemann; Canay et al.; Chernozhukov et al.; Böcker et al.; Lichtenberg et al.; Helfand e House; Arkhangelsky et al. |
| Só metadados, afirmação genérica ao nível do título | 3 | Coase; Conley e Taber; Camacho e Mejía |
| Versão citada inacessível | 1 | Calzada et al., texto tipografado do JAERE (HTTP 403) |

## Lista de achados

### SERIOUS (corrigir antes do Estágio 3)

| ID | # | Categoria | Local | O que o texto diz | O que a fonte diz | Fonte consultada | Correção sugerida |
|---|---|---|---|---|---|---|---|
| IL-SERIOUS-1 | 1 | Afirmação sobre o próprio processo (MAJOR_DISTORTION; contradita por registro do repositório) | `05-metodologia.tex:301-306`; repercute em `05:170-171`, `05:292-293`, `05:297-299`, `08-cronograma.tex:22` | "o desenho de calendário foi adotado como principal depois dela, sem que a exposição sazonal tenha sido cruzada com os desfechos". E, como compromisso: "Antes de qualquer contato com os desfechos do pós-lei, descreve-se o hiato"; o efeito mínimo detectável "é calculado apenas com dados do período de referência e do período de seca"; parâmetros "fixados em plano de análise versionado antes de qualquer cruzamento com os desfechos do pós-lei"; "O plano de análise é escrito antes do diagnóstico". | Em 2026-11-15 a especificação do projeto (sem os termos de chuva) foi estimada sobre o SINASC real de 2005–2024, com coeficientes do pós-lei, do período de seca, estudo de evento, tratamento falso, permutação e efeito mínimo detectável, em sete variantes para o Ceará e cinco para CE × RN. O próprio documento declara: "o desenho de calendário já foi cruzado com o desfecho do pós-lei". A frase do texto deixou de ser verdadeira, e os quatro compromissos de ordem (plano antes do contato) já não podem ser cumpridos como escritos. | `docs/ars/rodada21-local/mapa-de-lacunas-e-exploratorio.md` (cabeçalho e §3–4); `passport.yaml` (comentário da declaração). Não li os scripts `exploratorio/20–22` nem os dados. | Decisão do pesquisador ("Decido depois"). O que o portão exige é que o texto não afirme o contrário do que ocorreu. Caminhos: (a) declarar a rodada de 15/11 como a de setembro foi declarada (sem número, dizendo o que foi cruzado e que não é reportada), e reescrever os quatro compromissos de ordem como "a análise confirmatória será refeita a partir das bases originais, com plano ratificado antes"; (b) além disso, registrar no plano de análise quais parâmetros a rodada pode ter informado (limiar familiar, estação, `A_m` de 7 ou de 2 municípios), porque escolhê-los agora já é escolha com o desfecho à vista. Remover a frase sem declarar a rodada não resolve: `05:297-299` e `08:22` continuariam falsos. |
| IL-SERIOUS-2 | 2 | Afirmação factual e crítica para o método (MAJOR_DISTORTION) | `03-referencial.tex:36-37`; `01-introducao.tex:57-58`; `05-metodologia.tex:247-249`; ligadas: `02-contexto.tex:36-39`, `07-ameacas.tex:33-34` | "Como o único relato disponível para o Ceará indica aplicações menos frequentes [...], esse valor [cerca de 80 g] é tomado como teto." Na regra de decisão: "O efeito plausível é o do análogo equatoriano, tomado como teto". | Três problemas. (1) **Não é o único relato.** O Dossiê Abrasco registra, para a Chapada do Apodi, pulverização aérea na banana "realizada seis a oito vezes por ano, em áreas de cerca de 2.950 hectares" e "no mínimo seis pulverizações durante a quadra chuvosa". O PL 18/2015, que o projeto cita, remete a esse mesmo trecho (Abrasco 2012, p. 38–39). Há ainda um terceiro relato, do setor: em 2011 a Frutacor disse que as pulverizações eram "realizadas poucas vezes no ano". (2) **80 g é o piso do intervalo do próprio artigo, não o teto.** O resumo publicado diz "birth weight deficit of between 80 and 150 grams"; com limiar de 5 galões/ha a estimativa é 104,3 g; para meninos, 95,9 g. (3) **A comparação de frequência com o Equador continua valendo, mas com outra margem**: Calzada et al. descrevem de 20 ciclos por ano a quase um por semana; seis a oito no Ceará ainda é menos, porém concentrados em cerca de quatro meses, e o tratamento do artigo é "três meses ou mais acima de 4 galões/ha/mês". A unidade não foi convertida (o Dossiê dá cerca de 25 L de calda por hectare por aplicação, não ingrediente ativo). | Dossiê Abrasco, ed. 2012, p. 38–39 (trecho lido em `mprs.mp.br/media/areas/ambiente/arquivos/agrotoxicos/dossie_abrasco_agrotoxico.pdf`); ed. 2015, p. 69 e 152 (conferidas na sessão local, `conferencia-local-fontes.md`; não reabri o PDF de 628 p.); corroboração do total anual de 442,5 mil L em `portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=508087`; PL 18/2015 em `www2.al.ce.gov.br/legislativo/tramit2015/pl18_15.htm`; Diário do Nordeste via `mst.org.br/2011/07/14/...`; Calzada et al., manuscrito de 20/03/2023, seções 2, 4.1, 6.4 (`diposit.ub.edu/.../73f71bc2-.../content`) e resumo em `journals.uchicago.edu/doi/10.1086/725349`. | Decisão do pesquisador ("Decido depois"). Mínimo: retirar "o único relato disponível" e citar os dois relatos (duas por ano no Cariri; seis a oito na Chapada), dizendo que são regiões e fontes diferentes. Sobre o teto, escolher e justificar: (a) manter 80 g, declarando que é a estimativa central e não o máximo do artigo, e que a intensidade cearense não foi convertida; (b) usar o intervalo 80–150 g na grade de poder; ou (c) tratar o valor como referência, não como teto. `02:38-39` e `07:33-34` deveriam registrar que já há relato de concentração na quadra chuvosa (Dossiê; Agência Brasil 2016, já citada, descreve os voos nas quadras de 2008 e 2009; na Globo Rural 2021, já citada, um produtor da Chapada diz que a pulverização "é necessária apenas quando chove"), e que o que falta é registro administrativo. |

### MEDIUM (corrigir)

| ID | # | Categoria | Local | Problema | Informação correta | Fonte |
|---|---|---|---|---|---|---|
| IL-MEDIUM-1 | 1 | Afirmações factuais sem fonte na lista de referências | `02-contexto.tex:65-68`; `05-metodologia.tex:138` e `199`; `apendices.tex:133` (2011). Também `apendices.tex:27` ("segundo o setor"), `apendices.tex:134` e `projeto.tex:91` (seca 2012–2017), `01-introducao.tex:74-75` (nova ação no STF), `02-contexto.tex:20-21` (aprovação unânime) | O texto sustenta decisões de desenho (sensibilidade 2008–2010, pedido dos autos, janela da seca) em fatos que não têm citação. O Apêndice D diz só "fontes secundárias". Conferi todos: **são verdadeiros**. Falta a fonte. | (i) Notícia de 11/03/2011 da Secretaria de Direitos Humanos: empresas de fruticultura da Chapada "proibidas de utilizar aeronaves", resultado de missão da Comissão Nacional de Combate à Violência no Campo; não é ato normativo. (ii) Ação civil pública de MPF, MPT-CE e MP-CE, 15ª Vara Federal, Limoeiro do Norte, noticiada em 07/07/2011, contra Fapija, Del Monte, Frutacor, Tropical Nordeste e Agrícola Famosa; desfecho não localizado. (iii) Envio eletrônico dos relatórios pelo SIPEAGRO desde junho de 2021; antes, papel, "nunca processado"; em 2023 passou ao SEI. (iv) Seca de 2012 a 2017: seis anos seguidos abaixo da média (Inmet). (v) ADI 7794, PSOL, março de 2025, rel. Min. Luiz Fux. (vi) Aprovação em 18/12/2018, sem voto contrário. | (i) `sinait.org.br/noticia/2874/...` (reproduz a nota da SDH); `mapadeconflitos.ensp.fiocruz.br/conflito/ce-uso-indiscriminado-de-agrotoxicos-...`. (ii) `prt7.mpt.mp.br/informe-se/noticias-do-mpt-ce/534-...`; idem Fiocruz. (iii) `sindag.org.br/setor-ganha-plataforma-digital-para-envio-de-relatorios-ao-mapa`; `sindag.org.br/mapa-redireciona-envio-de-relatorios-mensais-das-aeroagricolas`. (iv) `noticias.uol.com.br/meio-ambiente/ultimas-noticias/redacao/2018/03/03/seca-de-2012-a-2017-no-semiarido-foi-a-mais-longa-da-historia.htm`. (v) `noticias.stf.jus.br/postsnoticias/partido-questiona-lei-do-ceara-que-autoriza-pulverizacao-de-agrotoxicos-por-drones/`. (vi) `brasildefato.com.br/2018/12/19/...`; `apublica.org/2019/02/antes-do-ceara-...`. |

### MINOR (recomendado agora; obrigatório no Estágio 4.5)

| ID | # | Categoria | Local | Problema | Sugestão |
|---|---|---|---|---|---|
| IL-MINOR-1 | 1 | Referência desatualizada | `../referencias.bib:98` (`callaway2024continuous`) | A entrada é o NBER WP 32117 (2024), que existe e confere. O artigo está aceito na *American Economic Review*, "Forthcoming", DOI 10.1257/aer.20240137 (página da AEA abre; o DOI ainda devolve 404 no Crossref e em doi.org). | Acrescentar nota "no prelo, American Economic Review"; trocar a entrada quando houver volume. |
| IL-MINOR-2 | 2 | Paráfrase imprecisa (MINOR_DISTORTION) | `03-referencial.tex:35-36` | "os autores não detectam gradiente de distância entre 150 e 2.500 metros". O artigo diz que, nessa faixa, os gradientes dos gestados dentro e fora dos períodos de fumigação intensiva "are quite similar", e que a diferença aparece a menos de 150 m. É figura descritiva (regressão polinomial local), não estimativa. | "não observam, além de 150 metros, diferença entre os gestados dentro e fora dos períodos de fumigação intensiva". Nuance não mencionada em `03:53-54`: na subamostra de meninos o terceiro trimestre é significativo (75,6 g). |
| IL-MINOR-3 | 3 | Condições omitidas (MINOR_DISTORTION) | `05-metodologia.tex:225-232` | "se não produzisse falsos negativos, a forma reduzida identificaria θ = VPP × ATT". O Corolário 1 de Denteh e Kédagni vale para o DiD canônico de dois grupos e dois períodos, com tratamento binário, e sob a Hipótese 1 (tendências paralelas e independência condicional do erro). A forma reduzida do projeto é de dose contínua. | Dizer "na versão binária da comparação e sob as hipóteses do Corolário 1". A ressalva de que a condição não vale exatamente está certa: Quixeramobim tem 1 estabelecimento com aeronave no Censo de 2006 e área de banana nula em 2015–2017 (PAM, tabela 1613). |
| IL-MINOR-4 | 4 | Consistência interna | `05-metodologia.tex:247` × `05:292-293` | "Nenhum critério usa o desfecho", mas o efeito detectável é calculado com o peso ao nascer do período de referência e da seca. | "Nenhum critério usa o desfecho do pós-lei". |
| IL-MINOR-5 | 5 | Consistência interna | `08-cronograma.tex:41-42` × `08:16-17` | No bimestre 6 estão "Início do segundo ensaio" e "Revisão final e defesa". Se a dissertação tem dois ensaios, a defesa não cabe no bimestre em que o segundo começa; o texto diz que o segundo ensaio "tem cronograma próprio". | Dizer o que se defende no bimestre 6 (o primeiro ensaio? a qualificação já está nos bimestres 4–5) ou trocar "defesa" por "versão final do ensaio". |
| IL-MINOR-6 | 6 | Simplificação (MINOR_DISTORTION) | `01-introducao.tex:72`; `apendices.tex:139` | "declarada constitucional"; "julga a lei constitucional". O STF conheceu a ação em parte e declarou constitucionais o caput e o § 1º do art. 28-B. O § 2º (controle vetorial por aeronave), que o projeto descreve em `02:12-13`, não foi examinado. Julgamento virtual de 19 a 26/05/2023; acórdão datado de 29/05/2023. | "julga constitucional a vedação (caput e § 1º do art. 28-B)". |
| IL-MINOR-7 | 7 | Texto superado pela conferência | `03-referencial.tex:76-77` | "essas leis não foram conferidas". Conferi cinco: Nova Venécia/ES, Lei 3.121, de 04/11/2011 (texto oficial reproduzido); Vila Valério/ES, Lei 550, de 05/08/2011; Boa Esperança/ES, Lei 1.649, de 19/12/2017 (ADPF 529 arquivada); Luz/MG, Lei 1.764, de 08/09/2009; Campo Magro/PR, Lei 1.011, de 13/12/2017. As datas diferem (2009 a 2017), que é a condição que o texto põe para o desenho escalonado. | Trocar por "cinco delas foram conferidas, com datas de 2009 a 2017; a vigência não foi" (a de Uchoa/SP foi suspensa por liminar, e há ação no STF contra várias delas). A reportagem não dá número de lei: dá os oito municípios num mapa embutido (Vila Valério, Nova Venécia, Boa Esperança, Pratânia, Uchoa, Luz, Campo Magro, Quitandinha). |
| IL-MINOR-8 | 8 | Detalhe de entrada bibliográfica | `referencias-projeto.bib:10`, `148`, `229`, `304` | (a) `ortiz2025triple` sem versão (lida: v3, 18/07/2025). (b) `denteh2022misclassification`: ano 2022 com "versão 3", que é de 30/04/2026. (c) `ibge2006censoagro`: "segunda apuração", 2012 — o metadado da tabela 1008 diz só "Censo Agropecuário, 2006"; o rótulo não foi confirmado. (d) `ceara2018nascer`: autor "Hospital Geral Dr. César Cals" para nota do Governo do Ceará hospedada no site do hospital; na lista sai em caixa baixa, ao contrário de "IBGE". | (a) e (b) indicar versão e data; (c) confirmar na página da tabela ou tirar "segunda apuração"; (d) autoria "CEARÁ. Governo do Estado". |
| IL-MINOR-9 | 9 | Definição não explicada | `05-metodologia.tex:95-96`, `112`; `04-objetivos.tex:33` × `apendices.tex:134` | A seca é de 2012–2017, mas $Seca_t$ são as coortes nascidas de 2013 a 2018, com 2012 e 2019 como transição. A defasagem é coerente (quem nasce em 2018 teve o início da gestação em 2017), mas o texto não a explica. | Uma frase: as coortes são datadas pelo nascimento, e o início da gestação cai no ano anterior. |

## Lista mínima (tabela "O que rechecar" do LEIA-PRIMEIRO)

| Item | Estado | Evidência |
|---|---|---|
| Lei municipal 1.511/2010 | **Conferido na fonte primária** | PDF local, p. 65: "Art. 212. Fica revogada a Lei nº. 1.478, de 20 de novembro de 2.009."; art. 214 (1.000 m e 500 m, aviso de cinco dias, multa); p. 67: "em 26 de maio de 2010", João Dilmar da Silva. O texto do projeto (`02:62-65`, `06:31-35`, Apêndice D) confere. Não conferido: se a 1.511 foi alterada entre 2010 e 2018 ("legal e regulada até a lei estadual" depende disso; o texto promete a conferência de vigência). |
| Calzada, Gisbert e Moscoso (JAERE) | **Conferido no manuscrito de 20/03/2023 e no resumo publicado; versão tipografada não conferida (403)** — UNVERIFIABLE_ACCESS | −80,02 g (erro-padrão 30,81) para "Banana Exposure × Intensive Fumigation"; exposição = mãe a até 150 m e índice de área fumigada acima de 6.000; intensiva = três meses ou mais em célula com mais de 4 galões/ha/mês; 3 galões: sem efeito; 5 galões: 104,3 g; 1º e 2º trimestres significativos, 3º não (4,9 e −43,2, imprecisos); fumigação o ano inteiro, mais intensa na estação chuvosa. Metadados Crossref: 10(6), 1623–1663, nov/2023. Ver IL-SERIOUS-2 e IL-MINOR-2. |
| Seção 3.3: Baker et al. | **Conferido no texto integral (arXiv v3, jun/2025)**; versão do JEL não aberta | Seção 5: "When treatment can happen only at one point in time [...]"; 5.1 "Simple event studies (2 × T)", com grupo não tratado; 5.2.3 estimadores de Callaway e Sant'Anna; 5.3 limites do TWFE. Crossref: JEL 64(2), 498–557, jun/2026. |
| Seção 3.3: Callaway e Sant'Anna 2021 | **Conferido no texto integral (arXiv v4, dez/2020)** | Efeitos médios por grupo e período; comparação com nunca tratados ou ainda não tratados; caso canônico de dois grupos e dois períodos como caso particular. Sustenta `03:67-73`. |
| Seção 3.3: Goodman-Bacon 2021 | **Conferido no texto integral do NBER WP 25018** (não a versão do periódico) | O estimador de efeitos fixos é "a weighted average of all possible two-group/two-period DD estimators" que comparam grupos de datas diferentes. Sustenta "decomposições que exploram essa variação". |
| Seção 3.3: de Chaisemartin e D'Haultfœuille 2020 | **Conferido no texto integral (arXiv v7, mar/2020)** | "weighted sums of the average treatment effects (ATE) in each group and period, with weights that may be negative". Sustenta "misturam efeitos heterogêneos". Segue valendo a nota da rodada 20: o artigo trata tratamento binário; a frase do projeto continua com o caso contínuo, que é de Callaway, Goodman-Bacon e Sant'Anna. |
| Ortiz-Villavicencio e Sant'Anna | **Conferido no texto integral (arXiv v3)** | Resumo e seções 3–4: a diferença entre dois DiD e a regressão de três efeitos fixos "are generally invalid when identification requires conditioning on covariates"; estimadores por regressão, ponderação e duplamente robusto; covariáveis anteriores ao tratamento e fixas no tempo; pacote `triplediff`. Sustenta `03:83-86`, `05:154-158` e a linha do Apêndice C. Não testei o pacote. |
| Callaway, Goodman-Bacon e Sant'Anna | **Conferido no texto integral (arXiv v8, 31/12/2025)**; aceitação na AER confirmada | Parâmetros de nível identificados sob tendências paralelas análogas ao caso binário; comparações entre doses exigem "strong parallel trends"; decomposições do TWFE. Página da AEA: "American Economic Review (Forthcoming)". Entrada do `.bib`: IL-MINOR-1. |
| Suspensão dos voos na seca | **Conferido em duas fontes independentes, nenhuma administrativa** | Agência Brasil, 16/07/2016 (citada): agricultora do Tomé, "a partir de 2012 [...] não houve novas aplicações devido à baixa intensidade das chuvas". Entrevista de Raquel Rigotto ao IHU, 06/10/2016 (não citada): "a pulverização aérea não tem acontecido na região em função da seca". O texto trata como hipótese (`07:19-20`). |
| Ação civil pública de 2011 | **Ajuizamento conferido; número do processo e desfecho não conferidos** | Nota do MPT-CE de 07/07/2011 e ficha da Fiocruz. Consulta processual na JFCE/TRF5 não tentada. O texto diz o mesmo, sem citar fonte: IL-MEDIUM-1. |
| Sigatoka-amarela e frequência | **Conferido; contradiz o texto** | Sigatoka-amarela: Agência Brasil 2016 e Globo Rural 2021 (ambas citadas), IHU 2016. Frequência: IL-SERIOUS-2. Fonte técnica da Embrapa não aberta. |
| Proibições municipais em outros estados | **Conferido (cinco leis)** | IL-MINOR-7. Fontes: `contraosagrotoxicos.org/wp-content/uploads/2019/10/nova-venecia.pdf` (cópia do texto do site da Câmara); `portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=384212`; `seculodiario.com.br/...stf-arquiva-acao...`; `acervo.socioambiental.org/sites/default/files/documents/t1d00115.pdf`; nota técnica 05/2023 da Defensoria do Paraná. |
| Censo Agropecuário 2006 (SIDRA 1008) | **Refeito por mim na API do IBGE; confere** | 184 municípios consultados; "Por aeronave": Limoeiro do Norte 18, Quixeré 9, Aiuaba 5, Jaguaruana 1, Mauriti 1, Quiterianópolis 1, Quixeramobim 1 = 36 em 7. O texto (`02:56`) diz 36 em 7 de 184. |
| Rocha e Soares 2015 | Conferido por resumo e destaques do editor | Chuva na gestação afeta mortalidade, peso e duração da gestação no semiárido; canal de água potável. |
| Reynier e Rubin 2025 | Conferido no texto (PNAS, aberto) | "reduced average birthweight by 23 to 32 g"; efeito doze vezes maior no decil inferior de peso esperado; aptidão para culturas transgênicas como instrumento. |
| Rigotto et al. 2013 | Conferido no texto (SciELO) | Estudo ecológico, 2000–2010; internações por neoplasias 1,76 vez maiores; óbito fetal com tendência crescente (p < 0,05) e razão de taxas não significante (0,77; p = 0,258). |
| Olden e Møen 2022 | Conferido no texto (OUP) | "does not require two parallel trend assumptions"; uma só, sobre a diferença entre os dois grupos. |
| Ferman e Pinto; MacKinnon e Webb; Conley e Taber | Resumo (os dois primeiros); só título (o terceiro) | Ferman e Pinto: poucos tratados e heterocedasticidade por tamanho de grupo. MacKinnon e Webb: o bootstrap selvagem agrupado "is known to fail when the number of treated clusters is very small". |
| Denteh e Kédagni | Conferido no texto (arXiv v3) | Corolário 1: sem falsos negativos, DID = P(ε = 0 \| D = 1) × ATT. Ver IL-MINOR-3. |
| Arkhangelsky et al. 2021 | Resumo (arXiv v4) | Uso genérico: o estimador é o citado. |

## Fase C — dados

C1, números e datas conferidos na fonte: sanção em 08/01/2019 e D.O. de 09/01/2019; caput e § 2º do
art. 28-B (citação literal confere); Lei 12.228 de 09/12/1993 (D.O. 14/12/1993), art. 29 (municípios
legislam supletivamente); PL 134 de 31/05/2011 (mesmo art. 28-B); PL 18 de 24/02/2015; aprovação
em 18/12/2018; Lei 19.135 de 19/12/2024 (D.O. do mesmo dia); assassinato em 21/04/2010; Lei 1.478
de 20/11/2009; Lei 1.511 de 26/05/2010; ADI 6137 (Cármen Lúcia, sessão virtual de 19 a 26/05/2023,
DJe 14/06/2023); IN 2 de 03/01/2008 (D.O.U. 08/01/2008), art. 14 (relatório mensal com UF,
município, tipo de serviço, cultura, área, produtos); Portaria 298 de 22/09/2021 (D.O.U.
24/09/2021, seção 1, p. 14); Decreto 4.074 (D.O.U. 08/01/2002, p. 1), art. 66, IV, d (modalidade de
aplicação na receita); Res. CNS 510 (D.O.U. 24/05/2016, seção 1, p. 44), art. 1º, parágrafo único,
II e V; formulário de nascido vivo trocado em 2011; programa estadual de 26/03/2018; 184 municípios;
36 estabelecimentos em 7 municípios; banana em 162 a 167 dos 184 municípios (PAM 2015 e 2018).

Tabela do PL 18/2015 recontada linha a linha: 23 pontos de coleta; procimidona em 23, carbaril em
23, carbofurano em 18, fenitrotiona em 16, glifosato em 4. Confere com `02-contexto.tex:44-46`.

Magnitudes da literatura: 23 a 32 g (confere); cerca de 80 g, 150 m, três meses, 2.500 m (conferem
no manuscrito; ver IL-SERIOUS-2 sobre o uso).

**Número de estimativa própria: nenhum.** Varredura de todos os algarismos com unidade nas nove
seções e no resumo, e do PDF por padrões de coeficiente, erro-padrão, valor-p e intervalo.

C2, consistência interna: períodos (referência 2007–2011; 2005–2006 só no estudo de evento;
transição 2012 e 2019; seca 2013–2018 por nascimento; pós 2020 em diante; sensibilidades 2008–2010
e sem 2020–2021) coincidem entre a Seção 5, os objetivos e os Apêndices B, C e E. A lista de testes
de seleção é a mesma em quatro lugares. Hipóteses H1 a H5 batem com o Apêndice C. Uma só hipótese
confirmatória em todos os lugares. Achados: IL-MINOR-4, 5 e 9.

C3, figuras e tabelas: uma figura (diagrama) e seis quadros, todos de elaboração própria e sem dado;
não há pacote de figuras nem `figure_table_trace[]`. Sem verificação de legenda a fazer.

C4, proveniência de experimentos: o passport traz `experiment_intake_declaration`
(`no_experiments_declared`, `declared_by`, `declared_at`); sem `repro_lock`, é tratado como
posterior à #260; não há `experiment_provenance[]`. Das cinco condições de FAIL, nenhuma se
verifica: a nº 4 pede manifesto com alegação empírica ou frase de seção de Resultados com
resultado próprio, e o projeto não tem nem uma nem outra. Nenhuma linha de
`experiment_alignment_results[]` foi emitida. Nota: o texto menciona análises próprias já
executadas, sem resultado; isso pesa no checklist dos 7 modos, não aqui.
"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the
experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

## Fase D — originalidade

D1 por busca de frases na web: **não executada.** A instrução do despacho proíbe enviar conteúdo do
projeto a buscadores além de títulos, autores e DOIs, e o projeto é inédito. O que fiz no lugar:
comparei com as fontes abertas os sete parágrafos que parafraseiam literatura (1.1, 3.2 e 3.3).
Resultado: PARAPHRASE com citação em todos; nenhum trecho de 20 palavras idênticas. A frase de
`03:83-86` segue de perto o resumo de Ortiz-Villavicencio e Sant'Anna, com citação. Cobertura real
de D1: cerca de 9% dos parágrafos, abaixo dos 30% do protocolo.

D2 (autoplágio): não executada (exigiria buscar pelo nome do autor). Os comentários do `.tex` dizem
que as seções 1 e 2 condensam `paper/secoes/`, texto do próprio autor e inédito.

## Fase E — registro de afirmações

Faixa de risco: todas as afirmações numéricas, causais e críticas para o método foram verificadas
(HIGH-IMPACT, 100%); o restante também, porque o total é pequeno.

| # | Local | Afirmação (resumida) | Fonte | Veredito |
|---|---|---|---|---|
| 1 | 01:38-40 | Dias et al.: soja transgênica, direção da água, piora a jusante | resumo ReStud | VERIFIED |
| 2 | 01:40-43; 03:29-32; 03:44-45 | Reynier e Rubin: aptidão; peso e gestação; 23–32 g; cauda inferior | PNAS | VERIFIED |
| 3 | 01:44-47; 03:43-44 | Larsen et al.: efeito só no topo da exposição | PMC | VERIFIED |
| 4 | 01:50-51 | Camacho e Mejía: aspersão aérea de herbicida na Colômbia | título; resumo de terceiros | VERIFIED (nível do título) |
| 5 | 01:52-55 | Calzada et al.: déficit entre expostas à fumigação intensa junto às plantações | manuscrito | VERIFIED |
| 6 | 01:55-58; 03:36-37; 05:247-249 | relato único; frequência menor; 80 g como teto | Dossiê Abrasco; Calzada | **MAJOR_DISTORTION** (IL-SERIOUS-2) |
| 7 | 01:62-64 | Weitzman; Lichtenberg et al.; Helfand e House; Böcker et al. (simulação) | resumos | VERIFIED |
| 8 | 01:71-75; ap:139 | STF declarou a lei constitucional; drones em 2024; nova ação | STF | MINOR_DISTORTION (IL-MINOR-6); sem fonte para a nova ação (IL-MEDIUM-1) |
| 9 | 02:9-16 | datas, caput, § 2º, 184 municípios | AL-CE | VERIFIED |
| 10 | 02:19-25 | PL 2015, PL 2011, aprovação unânime, Lei 19.135 | AL-CE; imprensa | VERIFIED |
| 11 | 02:33-35 | reportagens nomeiam a sigatoka-amarela | Agência Brasil; Globo Rural | VERIFIED |
| 12 | 02:36-37 | Equador: fumigação o ano inteiro, mais intensa na chuva | manuscrito, 4.1 | VERIFIED |
| 13 | 02:37-38 | produtor do Cariri: duas aplicações por ano | Globo Rural | VERIFIED |
| 14 | 02:42-46 | tabela do PL 18/2015: 23; 23; 23; 18; 16; 4 | PL 18/2015 | VERIFIED (recontado) |
| 15 | 02:54-60 | Censo 2006: 36 em 7 de 184; banana na maior parte do estado | SIDRA 1008 e 1613 | VERIFIED |
| 16 | 02:62-65 | Lei 1.511 revogou e passou a regular | PDF | VERIFIED; "até a lei estadual" não conferido |
| 17 | 02:65-68 | notícia de proibição e ação civil pública em 2011 | SDH; MPT-CE | verdadeira, **sem fonte** (IL-MEDIUM-1) |
| 18 | 02:68-70 | moradora: sem aplicações desde 2012 | Agência Brasil | VERIFIED |
| 19 | 02:71-73 | produtor: aplicações até 2018 | Globo Rural | VERIFIED |
| 20 | 03:13 | Coase: custos de transação | — | VERIFIED (nível do título) |
| 21 | 03:32-35 | 80 g; 150 m; três meses; varia com o limiar | manuscrito | VERIFIED; versão tipografada UNVERIFIABLE_ACCESS |
| 22 | 03:35-36 | sem gradiente entre 150 e 2.500 m | manuscrito, fig. 3 | MINOR_DISTORTION (IL-MINOR-2) |
| 23 | 03:38-41 | Rigotto et al. | SciELO | VERIFIED |
| 24 | 03:45-46 | Jones: fungicidas na variação explorada | resumo | VERIFIED; "dos poucos" é ADV-E5-3 |
| 25 | 03:53-56 | efeito nos dois primeiros trimestres; Brainerd e Menon | manuscrito; resumo | VERIFIED |
| 26 | 03:56-61 | Buckles e Hungerman; Currie e Schwandt; Rocha e Soares | PMC; PNAS; resumo | VERIFIED |
| 27 | 03:65-73 | Baker et al.; Callaway e Sant'Anna; Goodman-Bacon | textos integrais | VERIFIED |
| 28 | 03:73-77 | proibições municipais; leis não conferidas | Agência Pública | VERIFIED; superado (IL-MINOR-7) |
| 29 | 03:77-80 | de Chaisemartin; Callaway, Goodman-Bacon e Sant'Anna | textos integrais | VERIFIED |
| 30 | 03:81-86 | Olden e Møen; Ortiz e Sant'Anna | textos integrais | VERIFIED |
| 31 | 03:88-90; 05:280-288 | inferência com poucos tratados (seis referências) | resumos | VERIFIED |
| 32 | 05:121-124 | exposição contínua exige hipótese mais forte, por analogia | arXiv v8 | VERIFIED |
| 33 | 05:160-162; 07:15 | chuva afeta o peso por vias próprias | Rocha e Soares | VERIFIED |
| 34 | 05:189-194 | relatórios mensais; drones desde 2021 | IN 2/2008; Portaria 298 | VERIFIED |
| 35 | 05:196-199 | cadastro estadual; receituário registra prescrição | Lei 12.228; Decreto 4.074 | VERIFIED |
| 36 | 05:225-232 | θ = VPP × ATT | arXiv v3 | MINOR_DISTORTION (IL-MINOR-3) |
| 37 | 05:234-236 | diferenças-em-diferenças sintético | arXiv v4 | VERIFIED |
| 38 | 05:301-306 e ligadas | exposição sazonal não cruzada com os desfechos | registro do repositório | **MAJOR_DISTORTION** (IL-SERIOUS-1) |
| 39 | 06:16-19 | troca de formulário em 2011 | Consolidação SINASC 2011 | VERIFIED |
| 40 | 06:31-35 | Lei 12.228 autoriza municípios; Limoeiro 2009 e 2010 | AL-CE; PDF | VERIFIED |
| 41 | 06:47-50 | Res. 510/2016 | D.O.U. | VERIFIED |
| 42 | 07:12-14 | seca restringiu a água de irrigação | Pereira e Cuellar | VERIFIED (a irrigação caiu de 83% para 47% da vazão; a mesma tabela mostra produção de Limoeiro subindo em 2012–2014, o que o "a verificar" do texto cobre) |
| 43 | 07:23-24 | análogo estima para mães a até 150 m | manuscrito | VERIFIED |
| 44 | ap:27 | envio eletrônico desde 2021, segundo o setor | Sindag | verdadeira, **sem fonte** (IL-MEDIUM-1) |
| 45 | ap:130-140 | cronologia | várias | VERIFIED, salvo IL-MINOR-6 |
| 46–58 | diversas | datas e identificadores de normas (Fase C1) | fontes oficiais | VERIFIED |

E1.1: a extração é semântica; a completude não é garantida. E4 (escopo): as restrições
permanentes "só o Ensaio 1", "até 15 páginas textuais" e "nenhum número de estimativa" estão
respeitadas; o segundo ensaio aparece só como destino do insumo. Sem linha `SCOPE-BROADENED`.
E6: `[E6-SKIPPED: no revision evidence]` (primeira passagem desta rodada).

E5, alegações de ausência de literatura (consultivas, não contam no veredito):

| ID | Local | Texto | Classificação |
|---|---|---|---|
| ADV-E5-1 | 01:22-23 | "não se localizou, na literatura consultada, avaliação causal dos efeitos dessa resposta" | UNRESOLVED: redação limitada à busca, mas sem estratégia de busca documentada nem data |
| ADV-E5-2 | 01:75 | "não se conhece estimativa causal do que a proibição de fato produziu" | UNRESOLVED: redação absoluta |
| ADV-E5-3 | 03:45-46 | Jones "é dos poucos estudos em que fungicidas têm peso na variação explorada" | UNRESOLVED: sem busca documentada |

## Checklist dos 7 modos de falha de pesquisa com IA

Regra aplicada: a declaração é `no_experiments_declared` ("Não reporta"). O protocolo manda
verificar se o texto, mesmo assim, apresenta análises de dados como executadas pelo autor. Apresenta,
sem número: "uma rodada exploratória dessa análise já foi executada e levou a rever seu alvo, da
curva para o nível" (`05:302-303`); "um levantamento preliminar encontrou uma proibição"
(`06:33`); "Uma avaliação preliminar do monitoramento da água e do mapeamento de uso da terra por
satélite indicou limitações" (`06:40-41`). Pela letra da regra, declaração e texto discordam:
nenhum dos Modos 1, 3, 5 e 6 é NOT APPLICABLE, e os Modos 3 e 6 ficam SUSPECTED.

| Modo | Resultado | Evidência | Bloqueia? |
|---|---|---|---|
| 1. Erro de implementação que passa na autorrevisão | CLEAR | O texto não traz nenhum resultado numérico próprio; as perguntas de detecção não têm sobre o que incidir. Ressalva: não vi registro de execução das rodadas de setembro e de 15/11, e esta última corrigiu dois defeitos em `02_clean_births.py`. | não |
| 2. Citação alucinada | CLEAR | 51 de 51 referências existem; 30 por Crossref campo a campo, 2 por arXiv, 19 por fonte oficial, dado público ou página aberta. Nenhum DOI trocado, nenhum autor ou periódico errado. As distorções achadas são de afirmação (Fase E). | não |
| 3. Resultado experimental alucinado | **SUSPECTED** (por aplicação da regra) | Declaração "Não reporta" contra três frases que apresentam análises próprias como feitas. Substância fraca: não há número; a única consequência narrada é a troca de alvo, e o "levantamento preliminar" de Limoeiro eu conferi na fonte primária. O pesquisador pode confirmar ou afastar com justificativa. | **sim** |
| 4. Atalho | CLEAR | Não há resultado. O desenho prevê tratamento falso, placebo de composição materna e estudo de evento. Só sinaliza neste estágio. | não |
| 5. Erro reapresentado como achado novo | CLEAR | Nenhuma ocorrência de "surpreendente", "inesperado", "ao contrário do esperado" ou equivalente nas seções. | não |
| 6. Fabricação de metodologia | **SUSPECTED** (substantivo) | A Metodologia descreve um processo que não é o que ocorreu: "sem que a exposição sazonal tenha sido cruzada com os desfechos", contra a rodada de 15/11 sobre dado real. É o IL-SERIOUS-1. | **sim** |
| 7. Travamento de enquadramento | INSUFFICIENT EVIDENCE | O documento da rodada de 15/11 devolve ao pesquisador escolhas que mexem no enquadramento: `A_m` com os 7 municípios do Censo ou só os 2 da Chapada (Aiuaba tem 5 estabelecimentos com aeronave e 4 a 9 ha de banana na PAM); RN como segunda comparação; efeito detectável acima do plausível. O projeto tem regra de decisão que prevê o cenário sem poder, o que pesa contra o travamento. Depende de resposta dele. | não (aviso; rever no 4.5) |

Condição de bloqueio: qualquer modo SUSPECTED, exceto o 4. Há dois. O pipeline não avança para o
Estágio 3 até o pesquisador responder, por modo: confirmar e voltar ao texto; afastar com
justificativa registrada; ou revisar a passagem e repetir a checagem.

## Não conferido (com o motivo)

1. **Calzada et al., versão tipografada do JAERE** — `journals.uchicago.edu` devolve 403 (acesso pago). Conferidos o resumo publicado e o manuscrito de 20/03/2023.
2. **Baker et al., versão do JEL** — não aberta; conferido o arXiv v3 (jun/2025), anterior à publicação.
3. **Goodman-Bacon, versão do Journal of Econometrics** — conferido o NBER WP 25018 (2018).
4. **Callaway e Sant'Anna; de Chaisemartin e D'Haultfœuille, versões dos periódicos** — conferidas as do arXiv (v4 e v7).
5. **Catorze artigos só por resumo e três só por título** (lista na tabela de cobertura): as afirmações atribuídas são genéricas e batem, mas o texto integral não foi lido.
6. **Dossiê Abrasco 2015, p. 69 e 152** — não reabri o PDF; li o trecho equivalente da edição de 2012 e confio na conferência local de 15/11 para a paginação de 2015.
7. **Ação civil pública de 2011** — número do processo, andamento e decisão: consulta à JFCE/TRF5 não tentada.
8. **Nota original da SDH de 11/03/2011** — lida em reprodução do SINAIT, não no sítio do governo.
9. **Vigência da Lei 1.511/2010 entre 2010 e 2018** e das leis municipais de outros estados.
10. **Rótulo "segunda apuração" (2012) da tabela SIDRA 1008** — o metadado da API não o traz.
11. **Página do Censo Agropecuário 2017 no SIDRA** (URL da entrada `ibge2017censoagro`) — 403 para acesso automático; a tabela 6955 existe na API.
12. **Fonte técnica (Embrapa, ADAGRI) sobre frequência de aplicações** — não buscada.
13. **Scripts `scripts/exploratorio/20–22`, registros de execução e dados** — fora do mandato; o IL-SERIOUS-1 apoia-se no documento do repositório.
14. **Pacote `triplediff`** — não testado.
15. **Originalidade D1 por busca na web e D2** — não executadas (restrição do despacho).
16. **Semantic Scholar (A0)** — não usado; a verificação foi por Crossref, arXiv e fonte primária.

## Aviso de limitação da ferramenta

> A checagem de originalidade (Fase D) deste relatório não usou busca de frases na web nem
> software de detecção de plágio (Turnitin, iThenticate). Limitou-se a comparar com as fontes
> abertas os parágrafos que parafraseiam literatura, cerca de 9% do texto, e há risco de omissão.
> Vale como triagem preliminar; recomenda-se ferramenta profissional antes da entrega formal.

Este relatório verifica as populações registradas acima. Não garante a completude da extração de
afirmações, a verdade do que está nas fontes, nem a correção de análises que não examinei.

## Trilha de auditoria

Referências com DOI (consulta `api.crossref.org/works/<DOI>`, 2026-11-15/16; confirmados autores,
título, periódico, volume, número, páginas e ano):
10.1257/aer.20190159; 10.1257/jel.20251650; 10.1093/erae/jby050 (volume e páginas pelo editor:
47(2), 371–402); 10.1016/j.jdeveco.2013.11.004; 10.1162/REST_a_00314; 10.1016/j.jeconom.2020.12.001;
10.3386/w32117; 10.1086/725349; 10.1016/j.jhealeco.2017.04.005; 10.1162/rest_a_00887;
10.1080/01621459.2021.1920957; 10.1086/466560; 10.1162/rest_a_00049; 10.1073/pnas.1307582110;
10.1257/aer.20181169; 10.1093/restud/rdad011; 10.1162/rest_a_00759; 10.1016/j.jeconom.2021.03.014;
10.1093/restud/rdaf002; 10.2307/1243825; 10.3368/le.96.2.149; 10.1038/s41467-017-00349-2;
10.2307/1241928; 10.1111/ectj.12107; 10.1093/ectj/utac010; 10.1590/S0103-40142015000200008;
10.1073/pnas.2413013121; 10.1590/S1415-790X2013000300019; 10.1016/j.jdeveco.2014.10.003;
10.2307/2296698 (páginas 477–491 pelo editor). 10.1257/aer.20240137: 404 no Crossref; página
`aeaweb.org/articles?id=10.1257/aer.20240137` abre e traz "Forthcoming".

Textos integrais baixados: `arxiv.org/pdf/2503.13323` (v3), `/1803.09015` (v4), `/1803.08807` (v7),
`/2107.02637` (v8), `/2505.09942` (v3), `/2207.11890` (v3), `/1812.09970` (v4);
`nber.org/system/files/working_papers/w25018/w25018.pdf`;
`diposit.ub.edu/server/api/core/bitstreams/73f71bc2-9e61-4f15-a2de-a58cb08d43ac/content`.

Páginas e documentos oficiais: `www2.al.ce.gov.br/legislativo/legislacao5/leis2018/16820.htm`;
`.../leis93/12228.htm`; `.../leis2024/19135.htm`; `.../tramit2011/pl134_11.htm`;
`.../tramit2015/pl18_15.htm`; `docs/legislacao/lei-municipal-limoeiro-1511-2010.pdf` (p. 65–67);
`gov.br/agricultura/.../3-in-2-de-03-de-janeiro-de-2008-com-alteracoes-da-in-37-2020.pdf`;
`in.gov.br/web/dou/-/portaria-mapa-n-298-de-22-de-setembro-de-2021-347039095`;
`planalto.gov.br/ccivil_03/decreto/2002/d4074.htm`;
`in.gov.br/web/dou/-/resolucao-n-510-de-7-de-abril-de-2016-22917558`;
`jurisprudencia.stf.jus.br/pages/search/sjur481679/false`;
`redir.stf.jus.br/paginadorpub/paginador.jsp?docID=768536164&docTP=TP`;
`tabnet.datasus.gov.br/cgi/sinasc/Consolida_Sinasc_2011.pdf`;
`servicodados.ibge.gov.br/api/v3/agregados/{1008,1612,1613,6955}/metadados`;
`apisidra.ibge.gov.br/values/t/1008/n6/in n3 23/v/2020/p/2006/c12596/113450/...`;
`apisidra.ibge.gov.br/values/t/1613/n6/in n3 23/v/2313/p/2015,2018/c82/2720`.

Imprensa e demais: `agenciabrasil.ebc.com.br/geral/noticia/2016-07/ceara-pode-proibir-pulverizacao-aerea-de-agrotoxicos`;
`globorural.globo.com/Noticias/Agricultura/noticia/2021/04/pulverizacao-aerea-de-bananais-no-ce-e-alvo-de-acao-no-stf.html`;
`apublica.org/2019/02/antes-do-ceara-8-municipios-ja-haviam-proibido-fumigacao-aerea-de-agrotoxicos/`
e o mapa embutido `public.flourish.studio/visualisation/220933/embed`;
`hgcc.ce.gov.br/2018/03/26/ceara-lanca-programa-para-reduzir-mortes-maternas-e-neonatais`;
`ihu.unisinos.br/560860-...entrevista-especial-com-raquel-rigotto`;
`g1.globo.com/ce/ceara/noticia/2024/10/31/ze-maria-do-tome-...`;
`pnas.org/doi/10.1073/pnas.2413013121`; `academic.oup.com/ectj/article/25/3/531/6545797`;
`doi.org/10.1590/S1415-790X2013000300019`; `le.uwpress.org/content/96/2/149`;
`pmc.ncbi.nlm.nih.gov/articles/PMC5575123`; `scielo.br/j/ea/a/Z3QqdD43cMrg3F78WKZ8VRC`.

Buscas feitas: só títulos, autores citados, DOIs, números de lei e nomes de municípios e de
órgãos. Nenhum nome de pesquisador nem trecho do projeto foi enviado a buscador.
