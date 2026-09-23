# 19 — Medir o método: Fase 2 (investigação) e matriz de decisão

*ARS `deep-research`, modo `full`, Fase 2 de 6, aberta pelo pesquisador na
opção A do doc 18. A matriz de decisão (§5) e o checkpoint 2 (§6) adiantam a
Fase 3, como a opção A previa. 2026-09-23.*

> **Quatro achados, em ordem de consequência.**
>
> 1. 🔴 **Uma ameaça nova ao grupo tratado, anterior ao ban.** Em 11/03/2011, a
>    Secretaria Especial de Direitos Humanos noticiou que as empresas de
>    fruticultura da Chapada do Apodi estavam "proibidas de utilizar aeronaves
>    para pulverizar os pomares". Em julho de 2011, MPF, MPT e MP estadual
>    ajuizaram ação civil pública pedindo a proibição. O desfecho de uma e de
>    outra é desconhecido. Se a pulverização aérea parou em 2011, o Censo 2006
>    superestima o tratamento de 2018 justamente nos dois municípios que o
>    projeto trata como genuinamente tratados (§2.3).
> 2. ✅ **O relatório mensal do MAPA traz o município.** O Anexo V da IN 2/2008
>    tem as colunas UF, Município, Tipo de Serviço, Cultura, Área (ha) e
>    Produtos. É o que o Pedido D precisa, e agora ele responde também ao
>    achado 1: mostra se houve aplicação aérea na Chapada entre 2011 e 2018
>    (§2.1).
> 3. ✅ **O desenho de calendário tem precedentes diretos.** Calzada et al.
>    (estação chuvosa, sigatoka), Brainerd & Menon (mês da concepção × estação
>    do fertilizante), Winchester et al. (mês da última menstruação × herbicida
>    na água). Camacho & Mejía usam campanhas diárias de aspersão por município.
>    A diferença tripla exige uma única tendência paralela (Olden & Møen 2022)
>    (§§3–4).
> 4. ⚠️ **O gargalo muda de lugar, não some.** O script novo
>    (`14_mde_calendario.py`) mostra, em dado sintético, que o calendário
>    cancela a heterogeneidade entre municípios que infla o MDE do nível. Mas
>    os dois desenhos passam a depender da **fração de nascimentos expostos
>    dentro do município**, e o SINASC municipal não tem como aumentá-la. O
>    número real sai do `make mde-calendario` (§5).

---

## 1. Estratégia de busca

| item | como foi feito |
|---|---|
| ferramentas | busca web com índice (Firecrawl), texto integral Wiley (Scholar Gateway), listagens RePEc/IDEAS, arXiv e PubMed pelo índice |
| bloqueios | gov.br, planalto, portais legislativos, MPT, SINAIT, Fiocruz, academia.edu e o repositório da UB estão bloqueados no proxy. **Textos normativos e notícias foram lidos só pelos trechos do índice**, e cada um vem marcado assim |
| F1, termos | "Instrução Normativa MAPA 2/2008", "relatório mensal", "Anexo V", "relatório operacional", "RBAC 137", "frota aeroagrícola Ceará", "pulverização aérea Chapada do Apodi", "ação civil pública", "liminar" |
| F2, termos | aerial fumigation × birth weight, pesticide use × birth outcomes, month of conception × agrichemicals, season of birth |
| F3, termos | few treated clusters, wild bootstrap, conformal inference synthetic control, triple difference |
| inclusão | F1: normas e registros oficiais sobre aplicação aérea no Brasil. F2: estudos que medem exposição a agrotóxico agrícola ou aéreo com desfecho de saúde **e** estratégia de identificação declarada. F3: métodos publicados ou *working papers* estabelecidos |
| exclusão | opinião sem dado; estudo de exposição sem identificação, salvo toxicologia de mecanismo |

---

## 2. F1 — Registros da aplicação aérea no pré-período

### 2.1 O que existe, quem guarda e como se chega

| registro | quem guarda | campos | período | acesso | estado |
|---|---|---|---|---|---|
| **Relatório mensal** (IN MAPA 2/2008, art. 14, Anexo V) | SFA do estado onde a empresa atuou | cabeçalho: empresa, mês, ano, endereço, registro no MAPA. Colunas: **UF, Município, Tipo de Serviço, Cultura, Área (ha), Produtos Utilizados** | desde 2008; por SEI desde abr/2023 | **LAI federal (Pedido D)** | ✅ colunas por trechos do PDF oficial (gov.br) e do LegisWeb, pelo índice; ⬜ guarda do período |
| **Relatório operacional** (art. 9º, Anexo I) | a empresa, por no mínimo 2 anos | Município, UF, CNPJ/CPF, Tipo de serviço, Produto, Formulação, Dosagem, Classe toxicológica, Adjuvante, Cultura, Área (ha), Volume; mapa DGPS | por operação | só o que o MAPA tiver recolhido em fiscalização | ✅ campos pelo índice; os de 2015–2018 provavelmente descartados |
| **Informação prévia de atuação**: uma lista da IN pede "município e período de atuação", "tipo de serviço a realizar e cultura a ser tratada" e o pátio de descontaminação | SFA | município, período, serviço, cultura | desde 2008 | LAI federal: entra como item do Pedido D | ⬜ o artigo exato não foi lido; pelo contexto, é a comunicação de empresa que vai operar fora da sede |
| Receituário agronômico (Decreto 4.074/2002, art. 66) | ADAGRI | modalidade de aplicação, obrigatória se aérea | a verificar | LAI estadual (Pedido C) | já minutado |
| Cadastro estadual (Lei 12.228/1993, art. 8º) | SEMACE | método de aplicação | desde 1993 | LAI estadual (Pedidos A/B) | já minutado |
| Diário de bordo da aeronave | o operador | registro das operações em campo | — | privado; fora de alcance | Guia de boas práticas da ANAC, pelo índice |
| RAB (ANAC) | ANAC | aeronave, operador, base | retrato atual | aberto | diz quem podia, não onde aplicou |
| SIPEAGRO | MAPA | registro e autorizações | 2021 em diante | aberto | já baixado; sem pré-período |
| Relatórios de gestão da SFA-CE | MAPA | ⬜ talvez a área aplicada por aviação no estado, por ano | 2007–2018 | público no gov.br | **download local** (§7) |

### 2.2 O que isto muda no Pedido D

A minuta ganhou um item para a informação prévia de atuação. O Pedido D passa a
ter duas finalidades. A primeira é **medir o tratamento**: município, cultura e
área aplicada por mês, de 2008 a 2018. A segunda é **datar o fim da prática**:
se não houver relatório de aplicação aérea na Chapada depois de 2011, o achado
2.3 se confirma pelo registro federal.

### 2.3 🔴 2011: proibição anunciada e ação civil pública

| data | fato | fonte | estado |
|---|---|---|---|
| 11/03/2011 | *"Pulverização de agrotóxicos com aeronaves está proibida na região da CHAPADA DO APODI, no CEARÁ. As empresas produtoras de frutas instaladas na região da Chapada de Apodi, no Ceará, estão proibidas de utilizar aeronaves para pulverizar os pomares com agrotóxicos."* | matéria da Secretaria Especial de Direitos Humanos, reproduzida pelo SINAIT em 15/03/2011 | trecho literal pelo índice. ⬜ **quem proibiu, por qual instrumento, com que alcance e por quanto tempo** |
| jul/2011 | MPF, MPT e MP estadual ajuízam ação civil pública na 15ª Vara Federal (Limoeiro do Norte) contra a FAPIJA e quatro empresas: Del Monte Fresh, Frutacor, Tropical Nordeste e Agrícola Famosa. Pedem a proibição da pulverização aérea na Chapada e a revisão dos licenciamentos pela SEMACE | MPT-CE; EcoDebate, 08/07/2011; trechos pelo índice. A vara e as rés vêm de resumo de buscador | ✅ existência. ⬜ vara, número do processo, liminar e sentença |
| 2015 | A justificativa do PL 18/2015 descreve a pulverização aérea na banana do Baixo Jaguaribe com **dados de 2010**: 2.600 ha, 66.300 litros por pulverização | `docs/legislacao/pl-18-2015.md` | ✅ não prova prática em curso em 2015 |

⚠️ **Uma correção feita durante a busca.** Um resumo automático atribuiu à ação
da Chapada uma liminar que proíbe pulverização perto das comunidades Carranca e
Araçá. As duas ficam em **Buriti, no Maranhão** (incidente de 2021). A liminar
não é deste caso.

**Por que isto é sério.** O VPP de 2/17 do decil e de 7/169 do agregado vem do
Censo 2006. A proibição anunciada em 2011 e a ação do mesmo ano caem entre o
Censo e a janela 2015–2018, e **na Chapada**, onde estão Limoeiro e Quixeré,
os 27 estabelecimentos que o projeto trata como tratamento genuíno em 2019. ⬜
Se os estabelecimentos do Censo são as empresas da ação, não se sabe. Se a pulverização aérea parou em 2011, o ban de 2019 não removeu nada
ali. Nesse caso o nulo do Ensaio 1 não seria falta de poder: seria ausência de
tratamento.

**O que pesa contra essa leitura, e ainda não basta.** A ação de julho de 2011
pedia a proibição, o que sugere que a de março era parcial ou não pegou. E a
lei de 2019 foi aprovada contra uma prática descrita como corrente. Nenhuma das
duas coisas prova pulverização em 2015–2018. ⬜ **Dois passos locais decidem**
(§7): o processo na Justiça Federal e o Pedido D.

---

## 3. F2 — Como a literatura mediu e identificou

| referência | por quê (WHY) | como (HOW) | o quê (WHAT) | grau | verificação |
|---|---|---|---|---|---|
| Calzada, Gisbert & Moscoso (2023), *JAERE*, doi:10.1086/725349; WP UB 2021/405 | fumigação aérea de bananais e recém-nascidos, Equador 2015–17 | exposição pelo endereço da mãe e pelo perímetro das plantações; **1º trimestre × períodos de fumigação intensa**, que é a estação chuvosa, quando ataca a sigatoka-negra ("fumigated throughout the year, but the most intense fumigations occur during the rainy season") | −38 a −89 g na estratégia de calendário (WP); 80–150 g sob exposição alta (publicado, pelo resumo) | A | resumo do WP (RePEc), trecho da VoxDev; ⬜ texto integral |
| Camacho & Mejía (2017), *J Health Econ* 54:147–160, doi:10.1016/j.jhealeco.2017.04.005 | aspersão aérea de herbicida sobre cultivos ilícitos, Colômbia | **campanhas diárias de aspersão por município** + registros individuais de saúde, com efeitos fixos individuais | efeitos sobre saúde da exposição ao herbicida | A | conclusão pelo índice (ScienceDirect) |
| Larsen, Gaines & Deschênes (2017), *Nat Commun* 8:302, doi:10.1038/s41467-017-00349-2 | uso agrícola de agrotóxico e nascimento, Califórnia | Pesticide Use Report por seção e mês | *"for individuals in the top 5 percent of exposure, pesticide exposure led to 5–9% increases in adverse outcomes"*; nada na média | A | resumo literal (Nature) |
| Brainerd & Menon (2014), *J Dev Econ* 107:49–64 | fertilizante na água e saúde infantil, Índia | **mês da concepção** × estação de aplicação por cultura | *"fertilizer chemicals in water in the month of conception significantly increases the likelihood of infant mortality"* | A | resumo literal (autores, RePEc) |
| Winchester, Huskins & Ying (2009), *Acta Paediatrica*, doi:10.1111/j.1651-2227.2008.01207.x | agroquímicos na água e defeitos congênitos, EUA | **mês da última menstruação** × concentração sazonal na água | associação entre o mês da concepção e a estação dos agroquímicos na água; ⬜ meses e magnitudes a conferir no texto | B, ecológico | registro Wiley e PubMed |
| Currie & Schwandt (2013), *PNAS* 110(30):12265–12270, doi:10.1073/pnas.1307582110 | sazonalidade da saúde ao nascer | comparação dentro da mãe | separa a sazonalidade que vem de quem concebe quando (composição) da que vem da própria estação; ⬜ magnitudes a conferir | A | PubMed e PNAS |
| Buckles & Hungerman (2013), *REStat* 95(3):711–724 | estação de nascimento e resultados | características maternas por mês de concepção | a composição das mães varia com a estação | A | MIT Press e JSTOR |

**Síntese da F2.** Quando a exposição tem estação, o desenho estabelecido é o de
calendário: mês da concepção ou trimestre × estação de aplicação. A ameaça
conhecida é a composição sazonal das mães (Currie & Schwandt; Buckles &
Hungerman), e Winchester et al. é o exemplo do que acontece quando ela não é
controlada. A diferença tripla com municípios sem aplicação aérea remove a
sazonalidade estável de cada município. O que ela não remove é uma **mudança**
de sazonalidade em 2019 que seja diferente onde havia avião. E Larsen et al.
põem número no problema de fundo do projeto: sem medir a cauda de exposição,
não há efeito a ver.

---

## 4. F3 — Inferência com poucos tratados

| referência | o que resolve | uso aqui | verificação |
|---|---|---|---|
| Conley & Taber (2011) | poucos tratados, muitos controles; distribuição do erro tirada dos controles | 2 a 7 municípios com avião contra ~177 | já no `.bib` |
| Ferman & Pinto (2019), *REStat* 101(3):452–467 | o mesmo, com heterocedasticidade (tamanhos diferentes) | Limoeiro e Russas são maiores que a média: é o caso deles | MIT Press e RePEc |
| MacKinnon & Webb (2018), *Econometrics J* 21(2):114–135, doi:10.1111/ectj.12107 | wild bootstrap falha com pouquíssimos tratados; propõem o *subcluster* wild bootstrap, que exige clusters de tamanho parecido, *"not likely to hold for difference-in-differences"* | não usar o WCB sozinho com 2 a 7 tratados | resumo literal (RePEc) |
| Chernozhukov, Wüthrich & Zhu (2021), *JASA* 116(536):1849–1864, doi:10.1080/01621459.2021.1920957 | inferência conformal para controle sintético e DiD, por permutação no tempo, válida com uma unidade tratada | Limoeiro e Quixeré um a um | resumo (arXiv:1712.09089) |
| Olden & Møen (2022), *Econometrics J* 25(3):531–553 | a diferença tripla exige **uma** tendência paralela, a da diferença entre os dois DiDs | a hipótese do calendário é uma só: o hiato sazonal evoluiria igual nos dois grupos | resumo (Oxford Academic, RePEc) |
| Denteh & Kédagni, arXiv:2207.11890 | diluição sem falso negativo (Corolário 1) | o que resta de diluição dentro do grupo medido | já conferido |

---

## 5. Síntese: matriz de decisão (Fase 3, preliminar)

> ✅ **Atualizada em 2026-09-23 com os números reais:** `docs/ars/20-resposta-a-auditoria-2026-09-23.md` §6.
> A R3 foi calculada e **não tem poder** (δ mínimo de 165 g com f = 0,5, só
> Ceará). O "33,4 g" da R1 é do decil × resto, e não do contraste estimado. O nó
> de 2011 afrouxou, com indícios de aplicação em Limoeiro em 2018. E entrou uma
> R9: medir o tratamento em Limoeiro pelos avisos prévios municipais.

MDE em gramas sobre a média do grupo. "δ mínimo" é o efeito sobre o bebê exposto
que o desenho precisa para 80% de poder. Os números reais saem do painel local.

| rota | dado | tratamento | MDE | hipótese de identificação | ameaça principal | tempo até o dado | pré-especificação | veredito |
|---|---|---|---|---|---|---|---|---|
| R1 — nível, dose por área (status quo) | tem | VPP 2/17 no decil (calibração de 2006) | 33,4 g (decil) | PT entre produtores e não produtores | diluição; 15 controles; 2011 | 0 | a atual | **manter como forma reduzida reportada; não investir mais** |
| R2 — nível, tratados pelo avião (Censo 2006: 7) | tem | VPP ~1 **se** 2006 valer para 2018 | ~50 g (doc 18 §4.1) | PT | **2011**; f baixo | 0 | ciclo novo | subpotente, a não ser que f seja alto |
| R3 — calendário, tratados do Censo 2006, pico hipotético (fev–mai) | tem | idem | `make mde-calendario` | uma PT: o hiato sazonal (Olden & Møen) | 2011; mudança de sazonalidade em 2019; pandemia em 2020–21 | 0 | ciclo novo; a hipótese sazonal já está registrada (doc 14 §7) | **o mais promissor com o que existe: rodar o script 14 antes de decidir** |
| R4 — calendário com a medida do MAPA | Pedido D | municípios e meses medidos | script 14 com `--tratados` e `--meses-pico` do MAPA | idem R3 | o dado pode não existir | 20–30 dias, e pode falhar | ciclo novo | **o melhor, se o dado existir** |
| R5 — poucos tratados contra doadores de fora (sintético/SDID) | tem (SINASC multi-UF) | Limoeiro + Quixeré | script 13 (`chapada2_vs_ride_rn`) + Ferman–Pinto ou conformal | PT com doadores externos | 2011; drone nos vizinhos desde set/2021 | 0 | mudança de identificação: orientador | complementar; cortar o pós em set/2021 |
| R6 — fronteira CE × RN (Rota 1) | tem | poucos | doc 15 | diff-in-disc | G1 reprovado; drone em 2021 | — | orientador | despriorizar |
| R7 — identificação parcial com várias proxies | tem | limites | — | monotonicidade | limites largos | 0 | exploratório | secundário |
| R8 — Ensaio 1 como diagnóstico honesto | tem | — | — | — | — | 0 | — | sempre válido, e é o que o doc 17 já sustenta |

**Leitura.** Todas as rotas que sobem o VPP passam pelo mesmo nó: **a
pulverização aérea continuou na Chapada depois de 2011?** Se não continuou, R2
a R5 perdem o grupo tratado, e sobra R8. Se continuou, R3 é o próximo passo com
o que já existe, e R4 o melhor com o Pedido D.

---

## 6. ⚠️ Devil's Advocate — Checkpoint 2: **PASS com condições**

| teste | resultado |
|---|---|
| **Seleção a dedo** | a busca procurou contra-evidência e achou: a proibição de 2011 (§2.3) enfraquece a premissa de todas as rotas novas, e está no topo. Winchester et al. entra como advertência, não como apoio |
| **Viés de confirmação** | o desenho de calendário foi promovido pela analogia com Calzada. Mas lá a fumigação é **o ano inteiro, com pico**. Aqui a diferença tripla mede só o diferencial do pico, e sem pico mede zero por construção |
| **Cadeia lógica** | relatório mensal → VPP e calendário → diferença tripla → poder. O elo fraco não é o método: é a existência do dado e a fração exposta *f* |
| **Explicações alternativas** | (i) a **pandemia de 2020–2021** muda sazonalidade de concepção e pré-natal, possivelmente de modo diferente em municípios agrícolas; (ii) o fim da seca de 2012–2017 muda a pressão de sigatoka e a pulverização terrestre na estação chuvosa. ⚠️ *Errata de 2026-09-23:* a versão anterior dizia que isso "é substituição, parte do efeito do ban e não confundidor". Só é, se for causado pelo ban. Clima que mudaria aplicação e saúde mesmo sem ban é **confundidor** do hiato (doc 20 §3.4) |
| **"E daí?"** | se a pulverização continuou e o script 14 der δ mínimo compatível com 38–89 g (⚠️ working paper; a versão publicada fala em 80–150 g, e as duas não se misturam) para *f* plausível, o projeto tem um desenho que responde à crítica central do parecer. Se não, R8 é a resposta, e agora com razão documentada |

**Condições para a Fase 3 final:**
1. rodar `make mde-calendario` e o script 13 no painel local;
2. descobrir o que foi a proibição de 11/03/2011 e o desfecho da ação de julho
   de 2011;
3. protocolar o Pedido D;
4. pré-especificar o calendário com o orientador **antes** de cruzar exposição
   e desfecho.

---

## 7. O que só a máquina local faz

| passo | tempo | decide |
|---|---|---|
| `make mde-calendario` (e `PICO=3,4,5,6` como sensibilidade) | 5 min | se R3 tem poder |
| Portal da Justiça Federal no Ceará: ação civil pública de 2011, 15ª Vara (Limoeiro do Norte), partes FAPIJA, Del Monte, Frutacor, Tropical Nordeste, Agrícola Famosa. Liminar? Sentença? | 30 min | o nó do §5 |
| A matéria da SEDH de 11/03/2011 (via SINAIT, 15/03/2011): quem proibiu, por qual instrumento, com que alcance | 15 min | idem |
| IN 2/2008 no gov.br: artigo da informação prévia de atuação; checklist do Pedido D; protocolo no Fala.BR | 30 min | R4 |
| Relatórios de gestão da SFA-CE 2010–2018: "aviação agrícola" | 30 min | série estadual da área aplicada |

---

## 8. Arquivos desta rodada

| arquivo | o quê |
|---|---|
| `scripts/estimate/14_mde_calendario.py` | MDE do hiato sazonal contra o do nível, só no pré-período; calendário e tratados como parâmetros |
| `Makefile` | alvo `mde-calendario` (`PICO`, `TRATADOS`) |
| `tests/test_data_prep.py` | 4 testes: janela do 1º trimestre, hiato plantado, cancelamento de τ, CLI |
| `docs/legislacao/lai-mapa-relatorios-mensais-minuta.md` | item da informação prévia; a segunda finalidade do pedido |
| este documento | a Fase 2 |
