# Inferência com poucos tratados e um só estado tratado — nota de leitura

Data: 2026-11-17. Escopo: leitura metodológica para a seção 4.6 do projeto. Não altera o desenho nem a pré-especificação; a escolha do procedimento é do pesquisador. Toda afirmação sobre um artigo traz localização na versão lida (§6 diz qual versão). O que é dedução minha, e não texto do artigo, está marcado **[dedução]**.

## 1. O problema, em uma tela

A unidade é o município: 2 tratados (3 na versão ampla), todos no Ceará, uma coorte (2019T1); 21 controles, todos no Rio Grande do Norte; 36 trimestres antes (2010–2018) e 24 depois (2019–2024). Escreva o erro do desfecho não tratado como

`u_it = a_{s(i),t} + e_it`, com `s(i) ∈ {CE, RN}`.

O contraste de DiD entre médias de tratados e controles, de um período-base `b` para `t`, carrega

`[Δa_CE,t − Δa_RN,t] + [média_tratados(Δe_it) − média_controles(Δe_it)]`.

São duas camadas de incerteza. A segunda (idiossincrática municipal) tem 2 realizações do lado tratado e 21, não independentes, do lado controle. A primeira (choque estadual diferencial) tem **uma** realização por período, porque há um estado de cada lado. Qualquer estatística calculada só entre municípios potiguares elimina `a_RN,t` (é comum a todos) e nunca vê `a_CE,t`: placebos dentro do RN medem a segunda camada e são mudos sobre a primeira, mesmo com tendências paralelas em expectativa (`E[Δa_CE − Δa_RN] = 0`). É o ponto (a) do parecer, e ele está correto.

## 2. Método × exigência × o que admite

Legenda das colunas de dependência: H = heterocedasticidade; S = dependência serial; E = dependência espacial entre municípios; C = choque comum aos tratados (estadual).

| Método | O que exige | H | S | E | C | Compatível com CS-DR ponderado por nascimentos e covariáveis? | Fonte e nível de leitura |
|---|---|---|---|---|---|---|---|
| Bootstrap multiplicador e bandas simultâneas de Callaway & Sant'Anna | Amostra iid entre unidades (Hip. 2); fração positiva da população tratada, `P(G_g=1) > ε` (Hip. 6); `n → ∞`, `T` fixo (§4.1); com agrupamento, número de clusters "grande" (Obs. 10) | sim | sim (Hip. 2 não restringe a série) | não | não | É o procedimento nativo, mas fora das condições: 2 tratados, 2 estados | CS 2021, integral (arXiv v4) |
| Conley & Taber (2011) | `N0 → ∞`, `N1` e `T` fixos; erros dos tratados com a mesma distribuição dos controles (Hip. 2: iid entre grupos, independentes de `d` e `X`) | só a paramétrica do apêndice (variância função da população) | sim, arbitrária | só com processo estacionário no espaço e métrica de distância observada (apêndice A.3) | não **[dedução]** | Formulado para MQO com efeitos fixos; extensão ao CS "fora do escopo" segundo os próprios CS (nota 16) | CT 2011, corpo integral (cópia do autor, OCR ruim) + apêndice web A.3 |
| Ferman & Pinto (2019), correção transversal | `N0 → ∞`; `W_j` independente entre `j`; `W_j \| X_j` igual entre tratados e controles a menos de escala (hip. 1–5, §2.3) | sim, a estimável por observáveis (tamanho do grupo: `A + B/M_j`) | sim, sem especificar | não ("uncorrelated across groups", §2) | não | Covariáveis de grupo e individuais entram (§2.3); pesos amostrais só para microdado (ap. A.4); nada sobre CS/DR | FP, versão de trabalho out/2017 (MPRA 81988), integral; **texto publicado não conferido** |
| Alvarez & Ferman, correlação espacial | Hip. 4.1: distribuição marginal comum (a menos de escala) e lei dos grandes números nos controles | sim (como FP) | sim | sim, fraca nos controles, arbitrária entre tratados; com `N1 > 1`, só os testes conservadores da §5 | não **[dedução]**: a marginal dos tratados deixa de ser recuperável dos controles | DiD simples; não trata CS/DR | arXiv 2006.16997v8, §§1, 4, 5.1, 7 lidas |
| Via série temporal: Ferman & Pinto §4 (teste de Andrews); Chernozhukov, Wüthrich & Zhu (2021) | `T0` grande; série do contraste tratados − controles estacionária e fracamente dependente (CWZ, Hip. 2); efeito sem heterogeneidade estocástica; CWZ pensa `T*` curto frente a `T0` | sim, no corte transversal | sim, se estacionária e mixing (permutação em blocos móveis) | sim | **sim**, se `a_CE,t − a_RN,t` for estacionário | Aplica-se a uma série de contraste; nada demonstrado para ATT(g,t) DR ponderado | FP §4 (versão 2017); CWZ arXiv v10, §§1, 2.1–2.3, Hip. 1–2 lidas |
| Hagemann, teste de rearranjo | Poucos clusters grandes, **independentes entre si**, um tratado; cota para a variância relativa; pelo menos dez controles para os níveis usuais | sim | sim (dentro do cluster) | não entre clusters | só se o cluster for o estado, e aí há um controle | Não se aplica: municípios não são independentes; estados são 1 × 1 | arXiv 2010.04076v1, introdução e §3 lidas; versão publicada não conferida |
| Permutação / inferência por aleatorização | Atribuição aleatória (ou permutabilidade); hipótese nula forte | sim | sim | não, se a atribuição é por estado | não | Estatística livre, mas a atribuição aqui é estadual: há 2 permutações de estado | Roth et al. §5.1 (arXiv v3); MacKinnon & Webb (2020), **só resumo** |
| Rambachan & Roth (2023) | `β̂` assintoticamente normal com variância consistentemente estimável (§2.2, §2.5) | herda da inferência de base | idem | idem | trata o choque como **viés** limitado, não como variância | Aceita coeficientes de CS como `β̂`; não conserta a inferência de base | RR 2023, texto publicado, §§2.2 e 2.5 lidas |

Observações que a tabela não comporta:

- **CS dizem eles mesmos que o caso está fora.** Obs. 10 (p. 25 do arXiv): com poucos clusters "the application of the aforementioned bootstrap procedure is not warranted"; nota 16: nesses casos "one could use alternative procedures such as Conley and Taber (2011) and Ferman and Pinto (2019). Extending these proposals to our setup is beyond the scope of this paper". Karim, Nielsen, MacKinnon & Webb (arXiv 2602.12043, só resumo) relatam por simulação que a sobre-rejeição com poucos clusters tratados é "at least as severe for CSDID as for traditional DiD".
- **Pesos amostrais: o artigo de CS não os trata.** Nenhuma hipótese ou resultado menciona peso amostral; "peso" ali é peso de agregação dos ATT(g,t) (Tabela 1) e peso normalizado do estimador DR (§4). A ponderação por nascimentos é recurso de implementação; o que ela faz à teoria assintótica **não foi conferido**.
- **A robustez dupla não sobrevive a poucos tratados.** Alvarez & Ferman (arXiv 2302.03131, nota 3, p. 4): o estimador DR de CS "is not consistent in our setting" e "is not doubly robust in our setting with a few number of treated units"; a inferência deles vale "provided that the outcome model is correctly specified". Com 2 tratados não há escore de propensão estimável: na prática a identificação repousa no modelo de desfecho.
- **CT não exige independência, exige estacionariedade no corte.** p. 115–116 (paginação inferida do PDF): a Hip. 2 "is not necessary for our approach; it can be replaced by any model of cross-sectionally stationary data, with, for example, spatially correlated or conditionally heteroskedastic η_jt, that is, estimable given data from the controls". Um componente presente em todos os tratados e ausente dos controles viola exatamente isso **[dedução]**; CT não discutem nível acima do grupo.

## 3. Três objetos de inferência

1. **ATT(t) trimestral.** CT/FP e Alvarez & Ferman cobrem um contraste por vez, para a camada idiossincrática. Pela via temporal, cada trimestre pós é um teste de instabilidade de fim de amostra com `T* = 1`, e o p-valor mínimo é da ordem de `1/T` (levantamento de Alvarez, Ferman & Wüthrich, eq. 11).
2. **Efeito pós agregado.** Mesmos métodos sobre a combinação linear dos erros (`W_j` é pós menos pré em CT e FP). Pela via temporal, CWZ usam a estatística da média no pós com blocos móveis (§2.2); com 24 de 60 trimestres no pós, a premissa de `T*` curto está esticada, e o levantamento adverte (§4.3) que aproximações com muitos períodos pós têm problemas próprios (variância de longo prazo, não estacionariedade).
3. **Bandas simultâneas.** As de CS dependem do bootstrap multiplicador (Teorema 3, Corolário 1) e herdam suas condições. Com `N1` fixo, a única proposta localizada é Alvarez & Ferman (arXiv 2302.03131, §3: bandas uniformes para estudo de evento), sob independência entre unidades e a hipótese de distribuição comum; não cobre choque estadual. Bandas simultâneas pela via temporal: **não localizado**.

## 4. O critério decisivo

**Pergunta:** algum procedimento representa a incerteza de `Δa_CE,t − Δa_RN,t` com um só estado tratado?

**Pelo corte transversal, nenhum.** Bootstrap de CS, CT, FP transversal, Alvarez & Ferman, Hagemann e permutação entre municípios aprendem a distribuição dos erros dos tratados a partir dos controles; os 21 potiguares não contêm informação sobre a diferença de choques estaduais. Os pontos (b) e (c) do parecer também procedem: Alvarez & Ferman mostram que CT e FP continuam válidos sob dependência fraca **só com `N1 = 1`** (Prop. 4.1, Cor. 4.1) e "may be invalid with more than one treated unit" (resumo; §4.2); e no exemplo deles — 14 condados de Massachusetts contra 513 condados de 45 estados — a saída é FP **no nível do estado** (§7, p. 29), o que aqui não existe: o controle também é um estado só.

**Pela série temporal, sim, sob restrição explícita.** A série do contraste CE − RN contém `a_CE,t − a_RN,t` em cada período; FP §4 (o procedimento "works even if we have as few as one treated and one control group") e CWZ usam os 36 trimestres pré para aprender sua distribuição. A restrição é que o choque diferencial seja **estacionário e fracamente dependente no tempo**, sem quebra de distribuição em 2019, e que o efeito não seja estocástico. Sazonalidade do peso ao nascer e mudança no número de nascimentos por célula violam a estacionariedade se não forem tratadas (FP §4 dá a segunda como exemplo). Um choque diferencial persistente é indistinguível de violação de tendências paralelas.

**A alternativa declarada na literatura é condicionar.** Roth et al. §5.1, com o exemplo de Card e Krueger (NJ × PA): tratar os dois estados como fixos e "view any state-level shocks between NJ and PA as a violation of the parallel trends assumption", explorando a sensibilidade à magnitude da violação, calibrada pelo pré-período. O levantamento (ap. A.1) acrescenta o custo: o alvo vira `τ + ω_1 − ω_2`, que "does not have a clear causal interpretation", e por isso a recomendação de acoplar limites à la Rambachan & Roth. Nessa leitura RR passa de complemento a peça central — mas RR pressupõe `β̂` aproximadamente normal com variância estimável, e é justamente isso que 2 municípios tratados não entregam para a camada idiossincrática.

Em suma: **não há procedimento que cubra as duas camadas ao mesmo tempo sem hipótese adicional.** É preciso escolher e declarar: (i) estacionariedade temporal do choque diferencial; ou (ii) condicionamento nos choques estaduais com cota de sensibilidade; ou (iii) restrição de desenho que elimine `a_{s,t}` — a diferença tripla e o contraste de calendário que o projeto já lista como robustez (a inferência desses não foi objeto desta leitura).

## 5. Recomendação condicional

O que a leitura sustenta propor ao pesquisador:

1. **Não apresentar o bootstrap de CS como a inferência do projeto**, nem as bandas simultâneas dele; os autores excluem o caso (Obs. 10, nota 16). Estimativas pontuais de ATT(g,t) continuam utilizáveis.
2. **Declarar no texto as duas camadas e dizer qual procedimento responde por qual.** Camada municipal: CT/FP com os controles potiguares, na forma conservadora de Alvarez & Ferman para `N1 > 1` (Método 1, sem restrição à dependência entre tratados), com a variância função do número de nascimentos. Camada estadual: via temporal (FP §4 ou CWZ) sobre a série do contraste, **ou** condicionamento com sensibilidade de RR — dizendo qual das duas restrições se assume.
3. **Reportar o conjunto, não o mais favorável.** O levantamento (§6) recomenda transparência sobre as hipóteses e lembra que o máximo dos p-valores entre métodos plausíveis controla o tamanho se ao menos um for válido, ao custo de poder.
4. **Rebaixar a linguagem sobre robustez dupla**: com 2 tratados a especificação depende do modelo de desfecho (item da §2). Isso toca a pré-especificação; fica como ponto a decidir, não como mudança feita.
5. **Placebos no pré-período como diagnóstico de calibração.** Pseudo-tratamentos em datas do pré medem a taxa de rejeição do procedimento temporal; placebos entre potiguares medem a camada municipal. Ferman (2023, Obs. 3) mostra que pré-testes também captam distorção por correlação espacial. Nenhum deles valida a hipótese sobre 2019 em diante.

O que **continua não demonstrado**: validade de qualquer método de `N1` fixo para o ATT de CS com ajuste DR, covariáveis e ponderação por nascimentos; desempenho da via temporal com 36 pré e 24 pós trimestres; bandas simultâneas que incluam o choque estadual; estacionariedade do choque diferencial CE − RN (hipótese, não fato verificável com uma realização); poder de qualquer dessas opções para um efeito de 1–2 g.

## 6. Fontes

Registros conferidos em `api.crossref.org/works/<doi>` ou na API do arXiv em 2026-11-17.

| Referência | Identificador | O que foi lido |
|---|---|---|
| Callaway & Sant'Anna (2021), *J. Econometrics* 225(2):200–230 | DOI 10.1016/j.jeconom.2020.12.001; arXiv 1803.09015 | arXiv v4, integral nos trechos de hipóteses e inferência (§2.1, §4.1, Obs. 10–13, notas 15–16). Paginação é a do arXiv. |
| Conley & Taber (2011), *REStat* 93(1):113–125 | DOI 10.1162/REST_a_00049 | Texto publicado (cópia na página de C. Taber, digitalização com OCR defeituoso): §§I–III, Hip. 1–2, Prop. 1–2. Apêndice web, §A.3, íntegro. Fórmulas não conferidas símbolo a símbolo. |
| Ferman & Pinto (2019), *REStat* 101(3):452–467 | DOI 10.1162/rest_a_00759 | Versão de trabalho de out/2017 (MPRA 81988): §§1–4, ap. A.4. **Numeração e redação da versão publicada não conferidas.** |
| Alvarez, Ferman & Wüthrich, "Inference with few treated units" | arXiv 2504.19841 (v3); sem DOI localizado | §§3.1, 4.1.1–4.1.3, 4.3, 6, 7 (início), ap. A.1–A.2. §4.2 e §5 não lidas. |
| Roth, Sant'Anna, Bilinski & Poe (2023), *J. Econometrics* 235(2):2218–2244 | DOI 10.1016/j.jeconom.2023.03.008; arXiv 2201.01194 | arXiv v3, §5.1 inteira. |
| Alvarez & Ferman, "…Few Treated Units and Spatial Correlation" | arXiv 2006.16997 (v8, jun/2026); sem DOI localizado | Resumo, §1, §4, §5 (Tabela 1, Método 1), §7. Métodos 2–4 só pela tabela. |
| Alvarez & Ferman, "Extensions for Inference in DiD with Few Treated Clusters" | arXiv 2302.03131 (v1); sem DOI localizado | Resumo, nota 3, §3 (Hip. 3 e entorno). |
| Ferman (2023), *J. Applied Econometrics* 38 | DOI 10.1002/jae.2955; arXiv 1909.01782 | arXiv v7: resumo, trecho da §2, Obs. 3, §4. |
| Chernozhukov, Wüthrich & Zhu (2021), *JASA* 116(536):1849–1864 | DOI 10.1080/01621459.2021.1920957; arXiv 1712.09089 | arXiv v10: §1, §2.1–2.3, Hip. 1–2. Teoremas não lidos. |
| Hagemann (2025), *REStud* 92 | DOI 10.1093/restud/rdaf002; arXiv 2010.04076 | arXiv v1 (2020): resumo, §1, início da §3, §4 (Ex. 4.1). Versão publicada não conferida. |
| MacKinnon & Webb (2020), *J. Econometrics* 218(2):435–450 | DOI 10.1016/j.jeconom.2020.04.024 | **Só resumo** (RePEc). |
| Karim, Nielsen, MacKinnon & Webb, "Improved Inference for CSDID Using the Cluster Jackknife" | arXiv 2602.12043 (v1, fev/2026) | **Só resumo.** |
| Rambachan & Roth (2023), *REStud* 90(5):2555–2591 | DOI 10.1093/restud/rdad018 | Texto publicado: §2.2 (normalidade assintótica de `β̂`, Hip. 1), §2.5 (eq. 9–11). |
| Sant'Anna & Zhao (2020), *J. Econometrics* 219 | DOI 10.1016/j.jeconom.2020.06.003 | Só o registro; não lido. |

**Não conferido:** a documentação do pacote `did` sobre pesos; o texto final de Ferman & Pinto na *REStat*; Hagemann publicado; MacKinnon & Webb na íntegra; os métodos de permutação de Canay, Romano & Shaikh e de Ibragimov & Müller, citados só por intermédio de Roth et al.; Alvarez & Ferman (2025) sobre intervalos de predição; qualquer simulação com o painel do projeto (vedada na fase atual).
