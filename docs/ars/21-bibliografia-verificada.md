# 21 — Bibliografia verificada (rodada de 2026-11-10)

*ARS Stage 1. Complementa o doc 20. **Não reivindica cobertura da
literatura**: a forma de revisão (sistemática, de escopo, narrativa) é decisão
do pesquisador e está em aberto.*

## Como ler

- **Status.** ✅ Crossref = autores, título, periódico, volume e páginas
  conferidos em `api.crossref.org/works/<DOI>`. ✅ arXiv = conferido na API do
  arXiv. ⬜ = não verificada; **não citar**.
- **Leitura.** [TC] texto completo; [TP] trechos extensos; [R] só resumo;
  [M] só metadados — nas [M], a descrição do método **não** vem de leitura
  nesta rodada; conferir antes de citar detalhe técnico.
- Nada daqui foi incluído em `paper/referencias.bib`.

## 1. Mudanças de status de referências que o projeto já usa

| referência | o que mudou |
|---|---|
| Callaway, Goodman-Bacon & Sant'Anna, *DiD with a Continuous Treatment* | **"forthcoming" na *AER***. DOI `10.1257/aer.20240137` consta na página da AEA mas ainda não resolve no Crossref. Citar "AER, forthcoming" + arXiv:2107.02637 (última versão 31/12/2025) |
| Baker, Callaway, Cunningham, Goodman-Bacon & Sant'Anna | *JEL* 64(2):498–557, jun/2026, `10.1257/jel.20251650` ✅ |
| Bilinski & Hatfield | publicado: *Statistics in Medicine* 45(3-5):e70296, fev/2026, `10.1002/sim.70296`. Título final: "Nothing to See Here? A Non-Inferiority Approach to Parallel Trends" ✅ |
| "Cunningham, arXiv:2109.07406" (doc 11) | **O autor é Kyle Butts**, não Cunningham. *Geographic difference-in-discontinuities*, *Applied Economics Letters* 30(5):615–619, `10.1080/13504851.2021.2005236` ✅. ⬜ Corrigir no doc 11 |
| Denteh & Kédagni, arXiv:2207.11890 | Corolário 1 confere textualmente na v3 (30/04/2026): sem falso negativo, `θ_DID = P(ε=0\|D=1)·ATT`. Continua working paper. ⬜ Ler o enunciado da "Assumption 1" de que depende |
| Borusyak, Hull & Jaravel (2025) — "qual dos dois" | São dois artigos, ambos ✅: (i) *A Practical Guide to Shift-Share Instruments*, *JEP* 39(1):181–204, `10.1257/jep.20231370`; (ii) *Design-based identification with formula instruments: a review*, *Econometrics Journal* 28(1):83–108, `10.1093/ectj/utae003`. Para GAEZ × pós, o (ii) |
| Helfand (1991) | *Standards versus Standards: The Effects of Different Pollution Restrictions*, *AER* 81(3):622–634. Sem DOI; JSTOR 2006524 ✅ [M] |
| Calzada et al. (2023) — "80–150 g" | Pelo texto: −80 g (≥ 3 meses intensivos); −74 g e −75 g por trimestre. Ver doc 20 §4 |

## 2. Agrotóxicos e desfechos de nascimento

| citação | DOI/ID | status | o que diz | uso |
|---|---|---|---|---|
| Calzada, J.; Gisbert, M.; Moscoso, B. (2023). The Hidden Cost of Bananas: The Effects of Pesticides on Newborns' Health. *JAERE* 10(6):1623–1663 | `10.1086/725349` | ✅ Crossref [TC do manuscrito aceito; §2.3, tabelas e apêndice não] | Equador, 2015–17; exposição = ≤ 150 m do bananal e ≥ 3 meses de fumigação intensiva; −80 g; some com limiar de 3 galões/ha | análogo químico e de desenho (calendário) |
| Camacho, A.; Mejía, D. (2017). The health consequences of aerial spraying illicit crops: The case of Colombia. *J. Health Economics* 54:147–160 | `10.1016/j.jhealeco.2017.04.005` | ✅ Crossref [R] | painel individual; glifosato aéreo; consultas dermatológicas, respiratórias e abortos. ⬜ magnitude de abortos só no WP, truncada | aspersão aérea; perda gestacional (flag 6) |
| Dias, M.; Rocha, R.; Soares, R. R. (2023). Down the River: Glyphosate Use in Agriculture and Birth Outcomes of Surrounding Populations. *REStud* 90(6):2943–2981 | `10.1093/restud/rdad011` | ✅ Crossref [R] | soja GM × GAEZ × direção do rio; mortalidade infantil +5% a jusante | template do canal-água; não transfere quimicamente |
| Reynier, E.; Rubin, E. (2025). Glyphosate exposure and GM seed rollout unequally reduced perinatal health. *PNAS* 122(3):e2413013121 | `10.1073/pnas.2413013121` | ✅ Crossref [TP] | −29,8 g na intensidade média de 2012; −75 g no 1º decil de peso previsto contra −6 g no 10º | receita GAEZ; heterogeneidade por peso previsto |
| Larsen, A. E.; Gaines, S. D.; Deschênes, O. (2017). Agricultural pesticide use and adverse birth outcomes in the San Joaquin Valley of California. *Nature Communications* 8:302 | `10.1038/s41467-017-00349-2` | ✅ Crossref [R] | efeito de 5–9% só no topo de 5% da exposição | efeito na cauda → diluição |
| Jones, B. A. (2020). Invasive Species Control, Agricultural Pesticide Use, and Infant Health Outcomes. *Land Economics* 96(2):149–170 | `10.3368/le.96.2.149` | ✅ Crossref [R] | IV por praga invasora; +10% de fungicida → prematuridade +0,15 p.p. | único que isola **fungicida** |
| Brainerd, E.; Menon, N. (2014). Seasonal effects of water quality: The hidden costs of the Green Revolution to infant and child health in India. *JDE* 107:49–64 | `10.1016/j.jdeveco.2013.11.004` | ✅ Crossref [R; números do WP] | sazonalidade da aplicação × mês de concepção | precedente do desenho de calendário |
| Frank, E. G. (2024). The economic impacts of ecosystem disruptions: Costs from substituting biological pest control. *Science* 385(6713):eadg0344 | `10.1126/science.adg0344` | ✅ Crossref [R] | inseticida +31,1%; mortalidade infantil +7,9% | choque na demanda de pesticida |
| Skidmore, M. E.; Sims, K. M.; Gibbs, H. K. (2023). Agricultural intensification and childhood cancer in Brazil. *PNAS* 120(45):e2306003120 | `10.1073/pnas.2306003120` | ✅ Crossref [R] | soja → leucemia pediátrica, via água | Brasil; canal-água |
| Taylor, C. A. Cicadian Rhythm: Insecticides, Infant Health and Long-term Outcomes. CEEP Working Paper 9, Columbia (2020; versões 2021–22) | — | ✅ só como working paper [R] | cigarras → inseticida → mortalidade infantil | **não há publicação em periódico localizada**; citar como WP |
| Rigotto, R. M.; Silva, A. M. C.; Ferreira, M. J. M.; Rosa, I. F.; Aguiar, A. C. P. (2013). *Rev. Bras. Epidemiol.* 16(3):763–773 | `10.1590/S1415-790X2013000300019` | ✅ PubMed 24896288 / SciELO [R] | Limoeiro, Quixeré, Russas × 12 municípios de agricultura familiar; internações por neoplasia 1,76×; tendência crescente de óbitos fetais | precedente local da comparação com agricultura familiar; ecológico. ⬜ título completo a transcrever da fonte |
| Maertens, R. "Biofueling Poor Fetal Health?" | — | ⬜ **não verificada** | só citações secundárias | não citar |

## 3. Inferência com poucos clusters tratados

Todas [M], salvo indicação.

| citação | DOI/ID | status | nota de aplicação (2 tratados) |
|---|---|---|---|
| Conley, T. G.; Taber, C. R. (2011). *REStat* 93(1):113–125 | `10.1162/REST_a_00049` | ✅ | supõe mesma distribuição de erro em tratados e controles; falha se a variância depende do tamanho |
| Ferman, B.; Pinto, C. (2019). Inference in Differences-in-Differences with Few Treated Groups and Heteroskedasticity. *REStat* 101(3):452–467 | `10.1162/rest_a_00759` | ✅ | modela a variância no nº de nascimentos; a mais adequada ao caso |
| MacKinnon, J. G.; Webb, M. D. (2017). Wild Bootstrap Inference for Wildly Different Cluster Sizes. *J. Applied Econometrics* 32(2):233–254 | `10.1002/jae.2508` | ✅ | wild cluster bootstrap falha com poucos tratados |
| MacKinnon, J. G.; Webb, M. D. (2018). The wild bootstrap for few (treated) clusters. *Econometrics Journal* 21(2):114–135 | `10.1111/ectj.12107` | ✅ | wild em nível mais fino; sensibilidade |
| MacKinnon, J. G.; Webb, M. D. (2020). Randomization inference for difference-in-differences with few treated clusters. *J. Econometrics* 218(2):435–450 | `10.1016/j.jeconom.2020.04.024` | ✅ | permutação; preferir estatística t |
| Roodman, D. et al. (2019). Fast and wild: Bootstrap inference in Stata using boottest. *Stata Journal* 19(1):4–60 | `10.1177/1536867X19830877` | ✅ | implementação |
| Canay, I. A.; Santos, A.; Shaikh, A. M. (2021). The Wild Bootstrap with a "Small" Number of "Large" Clusters. *REStat* 103(2):346–363 | `10.1162/rest_a_00887` | ✅ | cobre a diferença tripla (variação dentro do cluster) |
| Canay, I. A.; Romano, J. P.; Shaikh, A. M. (2017). Randomization Tests Under an Approximate Symmetry Assumption. *Econometrica* 85(3):1013–1030 | `10.3982/ecta13081` | ✅ | base dos testes por cluster |
| Hagemann, A. (2025). Inference with a Single Treated Cluster. *REStud* 92(6):3968–3994 | `10.1093/restud/rdaf002` | ✅ | desenhado para 1 tratado |
| Alvarez, L.; Ferman, B.; Wüthrich, K. Inference with few treated units | arXiv:2504.19841 | ✅ arXiv | ⬜ ler; parece panorama |
| Alvarez, L.; Ferman, B. Inference in DiD with Few Treated Units and Spatial Correlation | arXiv:2006.16997 | ✅ arXiv | controles vizinhos são espacialmente correlacionados |

## 4. Controle sintético

| citação | DOI | status |
|---|---|---|
| Abadie, A.; Diamond, A.; Hainmueller, J. (2010). *JASA* 105(490):493–505 | `10.1198/jasa.2009.ap08746` | ✅ [M] |
| Abadie, A. (2021). Using Synthetic Controls. *JEL* 59(2):391–425 | `10.1257/jel.20191450` | ✅ [M] |
| Arkhangelsky, D. et al. (2021). Synthetic Difference-in-Differences. *AER* 111(12):4088–4118 | `10.1257/aer.20190159` | ✅ [M] |
| Ben-Michael, E.; Feller, A.; Rothstein, J. (2021). The Augmented Synthetic Control Method. *JASA* 116(536):1789–1803 | `10.1080/01621459.2021.1929245` | ✅ [M] |
| Chernozhukov, V.; Wüthrich, K.; Zhu, Y. (2021). An Exact and Robust Conformal Inference Method for Counterfactual and Synthetic Controls. *JASA* 116(536):1849–1864 | `10.1080/01621459.2021.1920957` | ✅ [M] |
| Abadie, A.; L'Hour, J. (2021). A Penalized Synthetic Control Estimator for Disaggregated Data. *JASA* 116(536):1817–1834 | `10.1080/01621459.2021.1971535` | ✅ [M] |
| Chernozhukov, Wüthrich & Zhu, "t-test for synthetic controls" | — | ⬜ não verificada |

## 5. Fronteira, transbordamento, tendências paralelas

| citação | DOI/ID | status |
|---|---|---|
| Dube, A.; Lester, T. W.; Reich, M. (2010). Minimum Wage Effects Across State Borders. *REStat* 92(4):945–964 | `10.1162/REST_a_00039` | ✅ [M] |
| Holmes, T. J. (1998). The Effect of State Policies on the Location of Manufacturing. *JPE* 106(4):667–705 | `10.1086/250026` | ✅ [M] |
| Keele, L. J.; Titiunik, R. (2015). Geographic Boundaries as Regression Discontinuities. *Political Analysis* 23(1):127–155 | `10.1093/pan/mpu014` | ✅ [M] |
| Butts, K. (2023). Geographic difference-in-discontinuities. *Applied Economics Letters* 30(5):615–619 | `10.1080/13504851.2021.2005236` | ✅ [R] |
| Butts, K. Difference-in-Differences Estimation with Spatial Spillovers | arXiv:2105.03737 | ✅ arXiv [R]; working paper |
| Clarke, D. (2017). Estimating Difference-in-Differences in the Presence of Spillovers. MPRA Paper 81604 | — | ✅ página do MPRA [R] |
| Huber, M.; Steinmayr, A. (2021). *JBES* 39(2):422–436 | `10.1080/07350015.2019.1668795` | ✅ [M]; encaixe fraco |
| Olden, A.; Møen, J. (2022). The triple difference estimator. *Econometrics Journal* 25(3):531–553 | `10.1093/ectj/utac010` | ✅ [M] |
| Rambachan, A.; Roth, J. (2023). A More Credible Approach to Parallel Trends. *REStud* 90(5):2555–2591 | `10.1093/restud/rdad018` | ✅ [M] |
| Roth, J. (2022). Pretest with Caution. *AER: Insights* 4(3):305–322 | `10.1257/aeri.20210236` | ✅ [M] |
| Negi, A.; Negi, D. S. (2025). *J. Applied Econometrics* 40(4):411–423 | `10.1002/jae.3116` | ✅ [M] |
| Grembi, Nannicini & Troiano (2016), diff-in-disc | — | ⬜ referência do periódico não conferida |

## 6. Avaliação de políticas (doc 22)

| citação | status |
|---|---|
| Cunningham, S. (2021). *Causal Inference: The Mixtape*. Yale University Press | lido na versão web da **1ª edição** (`mixtape-1ed.netlify.app`); cap. 3 inteiro, demais parcialmente. ⚠️ `mixtape.scunning.com` hoje serve a 2ª edição, em construção — não citar trechos dela como "Cunningham (2021)" |
| Gertler, P. J. et al. (2018). *Avaliação de impacto na prática*, 2. ed. BID/Banco Mundial | via nota `aval-pol/notas/disciplina/03-gertler.md`; livro não reaberto. O DOI impresso não resolve (registrado na nota) |
| Slides PECO 5046-6046 (Giuberti; Seixas), UFES 2026/2 | via nota `01-slides-e-guias.md`; PDFs não vistos |
| Itaú Social (2017); Magenta Book (HM Treasury); White & Raitzer (ADB, 2017) | via nota `04-itau-magenta-adb.md` (declara-se gerada por IA) |
| Bucher & Seixas (2026), *Ecological Economics* 242 | ⬜ **não lido** — artigo de DiD do orientador, citado no cronograma do curso; DOI não conferido. Ler: é o "idioma do Renato" |

## 7. Fontes documentais do doc 20 (não bibliográficas)

Acesso em 2026-11-10. (P) primária; (S) secundária; (I) parte interessada.

- (P) Lei 1.511/2010, Limoeiro do Norte:
  `https://www.camaralimoeirodonorte.ce.gov.br/arquivos/581/Leis_1511_2010_0000001.pdf`
- (P) ANA/PROÁGUA (2010), aquíferos da Chapada do Apodi — Vol. III
  (hidrogeologia) e Vol. V (gestão), em
  `https://metadados.snirh.gov.br/geonetwork/srv/api/records/8d3286b3-4dac-46dd-b266-98e23b1e0468`;
  Vol. I em `https://portal.cogerh.com.br/wp-content/uploads/2018/10/Volume-I-Aspectos-Gerais.pdf`
- (P) Lei CE 19.135/2024: `https://www2.al.ce.gov.br/legislativo/legislacao5/leis2024/19135.htm`
- (P) Portaria MAPA 298/2021:
  `https://www.in.gov.br/web/dou/-/portaria-mapa-n-298-de-22-de-setembro-de-2021-347039095`
- (P) Nascer no Ceará, 26/03/2018:
  `https://www.hgcc.ce.gov.br/2018/03/26/ceara-lanca-programa-para-reduzir-mortes-maternas-e-neonatais`
- (P) Justificativa do PL 18/2015: `https://www2.al.ce.gov.br/legislativo/tramit2015/pl18_15.htm`
- (P) SIDRA, Censo Agro 2017, resultados definitivos:
  `https://sidra.ibge.gov.br/pesquisa/censo-agropecuario/censo-agropecuario-2017/resultados-definitivos`
- (S) Agência Brasil, 16/07/2016:
  `https://agenciabrasil.ebc.com.br/geral/noticia/2016-07/ceara-pode-proibir-pulverizacao-aerea-de-agrotoxicos`
- (S) Entrevista de Raquel Rigotto, MST, 06/10/2016:
  `https://mst.org.br/2016/10/06/88-mil-litros-de-calda-toxica-sao-utilizados-todas-as-noites-no-cultivo-de-fruticultura-no-ceara`
- (S) SDH, 11/03/2011, reproduzido em
  `https://acervo.racismoambiental.net.br/2011/03/12/pulverizacao-de-agrotoxicos-com-aeronaves-esta-proibida-na-regiao-da-chapada-do-apodi-no-ceara/`
- (S) Mapa de Conflitos/Fiocruz (ACP de 2011):
  `https://mapadeconflitos.ensp.fiocruz.br/conflito/ce-uso-indiscriminado-de-agrotoxicos-contamina-recursos-hidricos-e-e-a-provavel-razao-da-forte-incidencia-de-cancer-em-populacoes-trabalhadoras-e-moradoras-do-vale-do-jaguaribe`
- (S) Chikungunya no CE 2016–17:
  `http://scielo.iec.gov.br/scielo.php?script=sci_arttext&pid=S1679-49742019000300048`
- (S) PLP 98/2007, Agência Câmara, 18/12/2007:
  `https://www.camara.leg.br/noticias/112031-CHAPADA-DO-APODI-PODERA-TER-REGIAO-ADMINISTRATIVA`
- (S) Fronteira agrícola em Apodi, 29/04/2018:
  `https://blogcarlossantos.com.br/nova-fronteira-agricola-para-a-economia-do-rn`
- (I) Globo Rural, 09/04/2021:
  `https://globorural.globo.com/Noticias/Agricultura/noticia/2021/04/pulverizacao-aerea-de-bananais-no-ce-e-alvo-de-acao-no-stf.html`
- (I) Agência Pública, 15/02/2019 (declarações do setor):
  `https://apublica.org/2019/02/antes-do-ceara-8-municipios-ja-haviam-proibido-fumigacao-aerea-de-agrotoxicos/`
- (I) SINDAG, relatório de ago/2019:
  `https://sindag.org.br/wp-content/uploads/2025/10/Relatorio-de-Atividades-Agosto-2019-2.pdf`
- (I) SINDAG, 26/07/2023:
  `https://sindag.org.br/aviacao-agricola-seguranca-e-importancia-x-fatos-e-mitos-2`
- (I) SINDAG, operadores por UF, dez/2018:
  `https://sindag.org.br/wp-content/uploads/2025/10/Empresas-SAE-e-Operadores-Privados-TPP-2018.pdf`
