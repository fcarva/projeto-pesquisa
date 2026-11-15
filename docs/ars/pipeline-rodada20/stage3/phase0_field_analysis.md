# Field Analysis Report

Estágio 3 (REVIEW) do academic-pipeline, rodada 20 — Fase 0 do `academic-paper-reviewer`, modo `full`.
Agente: `field_analyst_agent` (ARS v3.24.2). Data: 2026-11-15.
Este relatório configura o painel. Não avalia mérito, não despacha parecerista e não altera o manuscrito.

## Cobertura da leitura

**Lido por inteiro (fonte `.tex`, inclusive comentários de cabeçalho):**

| Arquivo | Conteúdo |
|---|---|
| `paper/projeto/projeto.tex` | Preâmbulo, metadados (título, autor, orientador, programa), capa, ordem das seções |
| `secoes/01-introducao.tex` | Cap. 1: abertura, pergunta, Antecedentes, Justificativa, Contribuição |
| `secoes/02-contexto.tex` | Cap. 2: a lei, a Chapada/cultura/químico, "O que se sabe sobre onde havia avião" |
| `secoes/03-referencial.tex` | Cap. 3: externalidade, agrotóxicos e saúde ao nascer, avaliação de política simultânea |
| `secoes/04-objetivos.tex` | Cap. 4: objetivo geral, quatro específicos, H1–H4 |
| `secoes/05-metodologia.tex` | Cap. 5: parâmetro-alvo, estágios 1–3, regra de decisão, inferência e poder |
| `secoes/06-dados.tex` | Cap. 6: unidade, fontes, desfechos, exposição, escopo, reprodutibilidade, ética |
| `secoes/07-ameacas.tex` | Cap. 7: quadro de ameaças e três comentários |
| `secoes/08-cronograma.tex` | Cap. 8: resultados esperados e cronograma |

**Quadros lidos (5, todos):** Quadro 1, cronologia legal (`qua:cronologia`, cap. 2); Quadro 2, regra de decisão entre estágios (`qua:regra`, cap. 5); Quadro 3, fontes de dados (`qua:fontes`, cap. 6); Quadro 4, ameaças e respostas (`qua:ameacas`, cap. 7); Quadro 5, cronograma por bimestre (`qua:cronograma`, cap. 8). A numeração 1–5 é a ordem de aparição na fonte; não a conferi no PDF.

**Equações lidas (4, todas no cap. 5):** (1) definição do `ATT` condicionado a `A_m = 1`; (2) `θ = VPP × ATT` (`eq:atenuacao`); (3) tendências paralelas em `ΔY(0)` por dose; (4) especificação da diferença tripla (`eq:ddd`). Não há figuras nem tabelas numéricas.

**Bibliografia:** li por inteiro `paper/projeto/referencias-projeto.bib` (19 entradas) e `paper/referencias.bib` (47 entradas). O texto cita 39 chaves distintas (conferido contra `projeto.bbl`, 39 `\bibitem`): as 19 do arquivo do projeto e 20 do arquivo geral. As outras 27 entradas de `referencias.bib` não são citadas no projeto e não aparecem na lista de referências.

**Não lido / não feito:**
- Não li o PDF compilado página a página; usei-o só para contar páginas (21) e palavras. Paginação, quebras de quadro e aparência final não foram examinadas.
- Não abri nenhuma das obras citadas nem conferi DOI, autores ou conteúdo: a correspondência entre o que o texto atribui a cada fonte e o que a fonte diz não foi verificada aqui.
- Não li `paper/main.tex` (qualificação), `docs/ars/20-projeto-de-pesquisa-desenho.md`, os relatórios do Estágio 2.5, o plano de análise versionado, scripts ou dados. O que o manuscrito diz sobre eles ("plano escrito em setembro de 2026", "rodada exploratória já executada") está registrado como afirmação do texto, não como fato conferido.
- Não li `references/top_journals_by_field.md`: o arquivo de agente não o exige e não há alvo a resolver.
- Não conheço as normas do PPGEco/UFES para projeto de pesquisa (extensão, seções obrigatórias, resumo). Nenhum cartão pode tratar essas normas como conhecidas.

**Texto dirigido ao painel:** não encontrei no manuscrito nenhuma instrução dirigida a pareceristas (identidade, leniência, decisão). Os comentários `%` da fonte são notas do autor para si (por exemplo, no cap. 8: as datas do cronograma são "uma PROPOSTA", a ajustar aos prazos do programa). Esses comentários não aparecem no PDF que a banca lê; os pareceristas devem avaliar o texto renderizado e tratar os comentários como contexto.

## Paper Basic Information

- **Title**: Proibição da pulverização aérea de agrotóxicos no Ceará: efeitos sobre a saúde ao nascer
- **Tipo de documento**: projeto de pesquisa de mestrado (PPGEco/UFES), em português, abnTeX2. Plano de pesquisa com elementos de plano de pré-análise; sem resultados.
- **Abstract length**: não há resumo nem abstract no documento (0 palavras).
- **Full text length**: cerca de 5.600 palavras de corpo na fonte (contagem aproximada, sem comandos LaTeX); cerca de 7.500 palavras no PDF de 21 páginas, incluídos capa, sumário e referências.
- **Number of references**: 39 citadas (27 artigos, working papers ou preprints; 12 fontes normativas, judiciais e estatísticas).

## Field Analysis

| Dimension | Analysis Result |
|-----------|----------------|
| Primary Discipline | Economia aplicada: avaliação de impacto causal de política pública (microeconometria aplicada), na interseção de economia ambiental e economia da saúde |
| Secondary Disciplines | Economia agrícola e dos recursos naturais (regulação de agrotóxicos, escolha de instrumento); epidemiologia ambiental e perinatal (exposição gestacional, peso ao nascer, óbito fetal); direito e administração pública (regulação estadual, registros administrativos, acesso à informação) |
| Research Paradigm | Quantitative Research (desenho observacional com dados administrativos secundários; estágio de plano, sem estimativas) |
| Methodology Type | Experimental / Quasi-experimental (quase-experimental: diferenças-em-diferenças com tratamento contínuo, diferença tripla de calendário gestacional, controle sintético/SDiD como robustez), com componente de Policy Analysis e uma etapa de medição documental do tratamento |
| Target Journal Tier | `criteria_binding_unavailable`. Não há periódico nem outro alvo confirmado pelo autor; o destinatário é o orientador e a banca do programa. Nenhum tier é atribuído. Observação de campo, sem vínculo a veículo: o texto usa o vocabulário e as referências correntes da microeconometria aplicada recente (parâmetro-alvo antes do estimador, hipóteses de identificação nomeadas, inferência com poucos grupos, poder calculado antes da estimação). |
| Paper Maturity | Pre-submission, entendido como "versão para entrega à banca", com ressalvas. Base (só estrutura, citação e acabamento, não mérito): oito capítulos completos e encadeados, cinco quadros com fonte, quatro equações numeradas, citações em formato ABNT resolvidas no `.bbl`, linguagem acabada. Ressalvas visíveis: não há resumo; o texto declara vários fatos "a conferir" (eventos de 2009–2011, vigência de leis municipais, persistência da prática); as datas do cronograma estão marcadas na fonte como proposta. |

## Recommended Target Journals (Top 3)

Não se aplica. O manuscrito é um projeto de pesquisa de mestrado, não um artigo; o autor não confirmou periódico nem outro alvo; e a instrução de despacho veda nomear alvos. Nenhum periódico é recomendado, e nenhum critério de veículo deve ser inferido pelos pareceristas.

## Reviewer Configuration Cards

Os quatro cartões abaixo cobrem os assentos configuráveis. O quinto assento, Devil's Advocate, é fixo e não recebe cartão. Os cartões dizem o que checar e onde; não antecipam conclusões.

Divisão de território, para evitar sobreposição:
- **Cartão 1**: o documento como projeto (pergunta, coerência interna, escopo, viabilidade no prazo, completude formal).
- **Cartão 2**: identificação, estimação, inferência e poder (cap. 5, eqs. 1–4, Quadro 2, parte econométrica do cap. 7).
- **Cartão 3**: literatura, enquadramento econômico, desfechos e dados de saúde (caps. 1, 3, 4, 6).
- **Cartão 4**: a medida física e administrativa do tratamento (caps. 2 e 5.3, Quadros 1 e 3, linhas de fonte do cronograma).

### Reviewer Configuration Card #1

**Role**: EIC
**Display role**: Journal-Fit Reviewer
**Identity Description**: Professor de pós-graduação em Economia com experiência em bancas de projeto e de qualificação de mestrado em economia aplicada, leitor generalista de avaliação de políticas públicas (não especialista em agrotóxicos nem em DiD contínuo). Como não há veículo confirmado (`criteria_binding_unavailable`), o "fit" avaliado é o de um projeto de mestrado perante orientador e banca, em termos gerais de campo; este assento não escolhe periódico substituto nem presume normas específicas do PPGEco/UFES.
**Review Focus**:
  1. Clareza e delimitação da pergunta: conferir se a pergunta em negrito do cap. 1, o objetivo geral e os quatro objetivos específicos do cap. 4, as hipóteses H1–H4 e os "resultados esperados" (i)–(iv) do cap. 8 dizem a mesma coisa, com a mesma população ("municípios onde a prática existia") e os mesmos desfechos.
  2. Rastreabilidade objetivo → hipótese → estágio → dado → atividade: para cada objetivo específico, localizar o estágio do cap. 5 que o atende, a linha do Quadro 3 que o alimenta e a linha do Quadro 5 que o agenda; registrar qualquer elo ausente (inclusive H2 e H4, e a robustez com doadores de outros estados mencionada na seção 5.4).
  3. Viabilidade e escopo no prazo: ler o Quadro 5 contra o Quadro 2. Checar se o cronograma de seis bimestres comporta os quatro cenários da regra de decisão, o que acontece com o estágio 3 se os pedidos de acesso não retornarem a tempo, e se o segundo ensaio (bimestres 5–6), declarado fora do projeto no cap. 3, cabe no mesmo calendário.
  4. Contribuição e significância declaradas: checar se as três camadas da seção "Contribuição" (objeto, medida, identificação) e a Justificativa são sustentadas pelo que os caps. 2–5 efetivamente prometem, e se a contribuição sobrevive em cada linha do Quadro 2, inclusive nas duas últimas.
  5. Completude formal como projeto: ausência de resumo; ausência de seção de orçamento/recursos; adequação do título ao conteúdo (o título promete "efeitos sobre a saúde ao nascer"; o texto admite cenários sem estimativa de efeito). Registrar como pontos a confirmar com as normas do programa, que este assento não conhece.
**Will particularly care about**: Se um membro de banca que lê só os caps. 1, 4 e 8 entende o que será entregue em cada cenário e quando. Se o documento distingue com clareza o que é desenho, o que é fato conferido e o que está "a conferir".
**Possible blind spots**: Não tem como julgar se as hipóteses de identificação são suficientes nem se os estimadores estão bem aplicados (Cartão 2). Tende a aceitar a caracterização da literatura como dada (Cartão 3) e a tomar a obtenção dos registros administrativos como questão só de prazo, não de conteúdo (Cartão 4). Pode confundir acabamento de redação com solidez do desenho.

### Reviewer Configuration Card #2

**Role**: Peer Reviewer 1
**Display role**: Peer Reviewer 1
**Identity Description**: Econometrista aplicado especializado em diferenças-em-diferenças com tratamento contínuo e intensidade de exposição (Callaway, Goodman-Bacon e Sant'Anna), em erro de classificação do tratamento e em inferência com poucos grupos tratados ou de controle (Conley–Taber, Ferman–Pinto, inferência conformal, wild cluster bootstrap), com prática em planos de pré-análise e cálculo de poder para desenhos observacionais de painel município × mês.
**Review Focus**:
  1. Coerência entre parâmetro-alvo e estimando: comparar a eq. (1) (ATT condicionado a `A_m = 1`, binário e não observado) com o alvo declarado do estágio 1 (`ATT(d|d)` agregado sobre a distribuição de doses, eq. 3) e com a eq. (2) (`θ = VPP × ATT`). Checar se o resultado de erro de classificação invocado, enunciado para tratamento binário, é transportado para uma dose contínua com justificativa; se as condições (tendências paralelas na classificação observada, ausência de falsos negativos) estão declaradas e onde o texto diz que serão verificadas (seção 5.1, cap. 7).
  2. Hipóteses de identificação do estágio 1 e sua testabilidade: eq. (3) e parágrafos "Janela da dose", "Exposição das coortes", "Grupo de comparação" e "Verificações". Checar o tratamento da dose possivelmente não predeterminada (2015–2018 contra 2010–2014), a definição operacional de pré e pós com exclusão das coortes de transição, o papel das quatro construções do grupo de dose nula, e o que o estudo de eventos consegue examinar dado que o painel começa em 2015 (leads, poder do teste de pré-tendência, intervalos de Rambachan–Roth, sonda da hipótese forte).
  3. Especificação da diferença tripla, eq. (4): conferir quais termos de ordem inferior estão incluídos ou absorvidos pelos efeitos fixos `α_{m,s(t)}` e `γ_t`; a definição de `P_t` e de `Pos_t`; o que identifica `β` e `λ`; se a hipótese única de identificação está enunciada de forma compatível com a especificação; e a consequência, para `β`, de `Â_m` ser estimado no estágio 2 e de a estação poder ser hipótese e não medida.
  4. Regra de decisão como pré-compromisso (Quadro 2): checar se as quatro linhas são mutuamente exclusivas e exaustivas, se os critérios que acionam cada linha são observáveis e estão definidos antes do dado (o que conta como "documentada", "nenhum registro novo", "cessou"), e se a regra evita que o resultado do estágio 1 influencie a classificação do estágio 2.
  5. Inferência, multiplicidade e poder (seção 5.6): adequação declarada de cada procedimento ao lado escasso de cada estágio (controles no 1, tratados no 3); a que estimativa e a que estágio se aplicam H1 e H2 sob a correção de Holm; como o efeito mínimo detectável será calculado e o que o texto promete fazer quando ele superar o efeito plausível; o estatuto do plano de análise (versionado, não público) e da rodada exploratória já executada, declarada no último parágrafo.
**Will particularly care about**: Se cada número que o projeto promete estimar tem um parâmetro causal nomeado e uma hipótese que o identifica, e se as decisões analíticas que restam em aberto estão amarradas antes do contato com os desfechos. Se o desenho distingue "teste" de "limite" de modo operacional.
**Possible blind spots**: Pode tratar a existência, o conteúdo e a granularidade dos registros de aplicação aérea como dados do problema (Cartão 4) e a plausibilidade biológica e a qualidade dos registros de nascimento e óbito como externas ao desenho (Cartão 3). Pode exigir de um projeto de mestrado o detalhamento de um plano de pré-análise completo; a proporcionalidade ao estágio é do Cartão 1 e do sintetizador.

### Reviewer Configuration Card #3

**Role**: Peer Reviewer 2
**Display role**: Peer Reviewer 2
**Identity Description**: Pesquisador sênior em economia ambiental e da saúde, com trabalhos sobre exposição a agrotóxicos e poluição e desfechos ao nascer em países de renda média, familiarizado com a literatura que o projeto mobiliza (soja transgênica e glifosato no Brasil, aspersão aérea na Colômbia, fumigação de bananais no Equador, estudos da Califórnia e dos EUA) e usuário dos registros do DATASUS (SINASC, SIM, SINAN) em painéis municipais.
**Review Focus**:
  1. Completude e fidelidade da revisão: nas seções "Antecedentes" (cap. 1) e "Agrotóxicos e saúde ao nascer" (cap. 3), checar se cada estudo é caracterizado corretamente quanto a desenho, população e resultado, em especial as magnitudes citadas (23–32 g; 80–150 g) e a base da afirmação de que o caso equatoriano é "o análogo mais próximo"; indicar literatura econômica e epidemiológica relevante que esteja ausente (por exemplo, outras avaliações de proibições ou restrições de agrotóxicos e a literatura brasileira sobre a Chapada do Apodi). Este assento deve abrir as fontes; a Fase 0 não abriu.
  2. A lacuna alegada: verificar a afirmação de que não existe avaliação ex post de uma proibição de método de aplicação (cap. 1, "O que nenhum desses trabalhos oferece") e a distinção entre substância e método que organiza o projeto.
  3. Enquadramento teórico e ligação com o segundo ensaio: seção 3.1 (externalidade, Coase, Weitzman, literatura de regulação de agrotóxicos). Checar se o referencial é proporcional ao que o projeto usa, e se a promessa de fornecer a "premissa empírica" do segundo ensaio é compatível com um parâmetro que o próprio texto descreve como intenção de tratar e, no estágio 1, atenuado.
  4. Desfechos e hipóteses de saúde: cap. 4 e parágrafo "Desfechos" do cap. 6. Checar a justificativa do peso médio e do óbito fetal como confirmatórios e de baixo peso e prematuridade como exploratórios; a janela gestacional sensível assumida em H3 (primeiro trimestre, segundo como sensibilidade) à luz da literatura citada; o duplo papel do óbito fetal (desfecho e teste de seleção) e a direção esperada em cada caso; o uso das intoxicações intencionais como placebo em H4.
  5. Qualidade e adequação dos registros de saúde: Quadro 3 e cap. 6. Checar o que o projeto diz, ou deixa de dizer, sobre cobertura e sub-registro do SIM para óbito fetal, município de residência contra de ocorrência, células pequenas em município × mês, mudanças de registro em 2020–2021, e mecanismos concorrentes no período (linha "Choques de 2020–2021" do Quadro 4; a seca de 2012–2017 mencionada no cap. 5).
**Will particularly care about**: Se a contribuição alegada é genuína frente ao que já existe, e se os desfechos escolhidos e os sinais esperados decorrem da literatura citada e não de conveniência dos dados. Se o projeto separa efeito populacional de efeito ocupacional ao falar de "saúde".
**Possible blind spots**: Pode avaliar o desenho por analogia com os estudos de referência e subestimar o que muda quando o tratamento é uma retirada estadual e simultânea (Cartão 2). Tende a supor que a cultura é boa proxy da exposição, que é justamente o que o projeto põe em dúvida (Cartão 4). Menos atento ao calendário e à forma do documento (Cartão 1).

### Reviewer Configuration Card #4

**Role**: Peer Reviewer 3
**Display role**: Peer Reviewer 3
**Identity Description**: Pesquisador de ciência da exposição e saúde ambiental com formação agronômica, especializado em tecnologia de aplicação de agrotóxicos (aviação agrícola, deriva, calendário fitossanitário da fruticultura irrigada do semiárido) e com experiência em reconstruir exposição histórica a partir de registros regulatórios e administrativos brasileiros (relatórios da aviação agrícola ao MAPA, receituário agronômico, cadastros estaduais, censos agropecuários, autos judiciais) obtidos por Lei de Acesso à Informação. Não é economista: lê o projeto perguntando se o "tratamento" descrito corresponde ao que acontecia no campo e ao que os arquivos públicos de fato guardam.
**Review Focus**:
  1. Validade de construto do tratamento: seções 2.2 e 2.3 e parágrafo "Dose" do cap. 5. Checar a premissa de que banana é a cultura associada à aplicação aérea no Ceará (e o lugar do melão e de outras culturas candidatas); se área plantada sobre área municipal mede algo próximo de exposição populacional à deriva; a hipótese de ausência de falsos negativos (avião sem a cultura), inclusive a dispersão aérea para controle vetorial alcançada pelo § 2º da lei, citada no cap. 2 e na linha "Grupo de comparação pequeno e contaminado" do Quadro 4.
  2. O que cada fonte do estágio 2 pode e não pode mostrar: seção 5.3 e Quadro 3, fonte por fonte. Para os relatórios mensais do MAPA, o receituário, o cadastro estadual, os autos de 2011 e o Censo Agropecuário de 2006: o que o projeto afirma que o registro contém, com que base normativa, para que anos, em que unidade (município, mês, estabelecimento), sob guarda de quem, e se o texto declara riscos de retenção, lacuna, sigilo ou negativa. Checar se a ordem de precedência entre fontes em caso de conflito está definida e como delas se chega a `Â_m` e ao `VPP`.
  3. Persistência da prática entre 2006 e 2018: Quadro 1 (linhas de 2009 a 2011, declaradas "a conferir"), seção 2.3 e comentário "A persistência da prática" do cap. 7. Checar se o projeto distingue fato conferido de notícia secundária em cada evento, e se o plano de conferência é capaz de decidir entre as linhas 3 e 4 do Quadro 2.
  4. Premissa agronômica do desenho de calendário: seções 2.2 e 5.4 e comentário "A sazonalidade" do cap. 7. Checar a base para supor pico sazonal de aplicação aérea em bananal irrigado no semiárido cearense, a transposição da estação chuvosa do caso equatoriano, e o que o texto prevê se a aplicação for uniforme ao longo do ano ou se o calendário não vier nos registros.
  5. Pós-proibição e alcance do escopo: o que o projeto prevê para medir cumprimento, fiscalização e substituição por aplicação terrestre ou por drones (Quadro 4, linhas "Substituição" e "Fiscalização desconhecida"; H4); a escolha de 19/12/2024 como fim da janela; a exclusão dos canais hídrico e atmosférico (cap. 6, "Escopo"); e a afirmação ética do cap. 6 à luz do tipo de dado que os pedidos de acesso podem devolver (registros com identificação de empresas, produtores ou responsáveis técnicos).
**Will particularly care about**: Se o projeto sabe, antes de pedir, o que os arquivos administrativos guardam e em que formato, e se a "cultura" e a "estação" usadas como substitutos têm base agronômica local e não apenas transposição de outro país. Se o município é uma unidade defensável para um fenômeno de deriva que opera em escala de quilômetros.
**Possible blind spots**: Não avalia identificação, estimação nem inferência (Cartão 2) e pode pedir uma precisão de medida de exposição que um desenho de forma reduzida não exige. Não julga a posição do projeto na literatura econômica (Cartão 3). Pode subestimar restrições de prazo e de escopo de um mestrado ao sugerir fontes adicionais (Cartão 1).

## Review Strategy Recommendations

- **É um plano, não um artigo com resultados.** Os critérios de `review_criteria_framework.md` § 2.1 se aplicam ao desenho prometido. "Statistical reporting completeness" e "Conclusion conservatism" não têm objeto no sentido usual: os pareceristas devem aplicá-los ao que o texto se compromete a reportar e a concluir (seção 5.6, cap. 8) ou marcar `NOT_ASSESSED`, sem cobrar estimativas. A ausência de números de estimativa é regra declarada do documento, não lacuna.
- **Sem alvo vinculante.** `criteria_binding_unavailable` vale para todos os assentos. Nenhum parecer deve invocar padrões de um periódico específico nem normas do PPGEco/UFES que não tenha lido; pontos formais (resumo, extensão, orçamento) entram como itens a confirmar pelo autor.
- **Afirmações do texto que nenhum assento pode conferir pelo manuscrito:** a existência e a data do plano de análise versionado, o conteúdo da rodada exploratória, os diagnósticos "preliminares" (dispersão da dose, poder do estágio 1, avaliação das fontes de água, vento e uso da terra). Os pareceristas devem tratá-las como declarações e dizer o que precisariam ver, não presumi-las verdadeiras nem falsas.
- **Fontes citadas não foram abertas na Fase 0.** A fidelidade das caracterizações da literatura cabe ao Cartão 3; a das bases normativas dos registros (instrução normativa da aviação agrícola, decreto do receituário, lei estadual) cabe ao Cartão 4.
- **Tensão esperada entre Cartões 2 e 4.** O Cartão 2 pode considerar a forma reduzida com atenuação declarada suficiente como resultado; o Cartão 4 pode considerar que, sem medida do método, o tratamento não está definido. O sintetizador deve manter a divergência visível, porque ela é a questão central que o próprio projeto declara (cap. 7, "A medida do tratamento").
- **Tensão esperada entre Cartões 1 e 2/4.** Exigências de detalhamento econométrico ou de novas fontes competem com o prazo de seis bimestres e com o escopo de um mestrado. Cabe distinguir, em cada achado, revisão necessária de sugestão opcional.
- **Fronteira com o Devil's Advocate.** Os quatro cartões cobrem o que o projeto declara. O assento fixo fica livre para atacar o que o projeto não declara, por exemplo o cenário em que nenhum dos três estágios produz evidência interpretável.
- **Idioma.** Pareceres em português, que é o idioma do manuscrito e dos destinatários.
- **Comentários da fonte.** Os comentários `%` dos arquivos `.tex` não aparecem no PDF. Servem de contexto ao painel, mas nenhum achado deve depender de informação que só exista neles sem dizer isso.

## Quality Gates

- [x] As 6 dimensões foram analisadas (a quinta, declarada `criteria_binding_unavailable`).
- [x] Os 4 cartões foram produzidos; nenhum quinto cartão foi emitido para o Devil's Advocate.
- [x] Os focos dos 4 assentos não se sobrepõem (territórios declarados antes dos cartões).
- [x] O Cartão 4 parte de outra disciplina (agronomia e ciência da exposição, registros regulatórios), não de uma versão "mais ampla" dos outros.
- [n/a] Periódicos-alvo recomendados: não se aplica, pelas razões da seção própria.
- [x] As descrições de identidade são específicas quanto a método, área e objeto.
