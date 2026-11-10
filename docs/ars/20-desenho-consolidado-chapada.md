# 20 — Desenho consolidado: o que estou estimando, com que dado, contra que controle

*ARS `academic-pipeline` → Stage 1 (`deep-research`, modo `full`). Rodada de
pesquisa, sem estimação e sem edição do paper ou da pré-especificação.
2026-11-10. Documentos irmãos: `21-bibliografia-verificada.md` (referências e
URLs das fontes documentais, §7) e `22-avaliacao-de-politica-sutva-dags.md`.*

> **Cinco achados, em ordem de consequência.**
>
> 1. 🔴 **A ameaça ao tratamento mudou de forma: não é 2011, é a seca.** A
>    "proibição" de março/2011 não tem instrumento jurídico localizável e a ACP
>    de julho/2011 não tem desfecho conhecido — a prática não parou por ordem
>    legal. Mas duas fontes independentes de 2016 dizem que os voos **cessaram
>    na Chapada a partir de ~2012 por causa da seca** (a sigatoka-amarela
>    depende de umidade). A janela de dose 2015–2018 cai quase toda nesse
>    período: o contraste pré/pós 2019 pode ser "pouco avião → nenhum avião"
>    (§2).
> 2. ✅ **Lei 1.511/2010 de Limoeiro conferida no texto integral.** Art. 212:
>    "Fica revogada a Lei nº. 1.478, de 20 de novembro de 2.009." A lei também
>    **regula** a pulverização aérea (art. 214: 1.000 m de povoações, aviso de
>    cinco dias). A flag 0 passa a fonte primária (§2.1).
> 3. ⚠️ **A divisa CE×RN não é um experimento natural limpo.** Política
>    estadual de saúde materno-infantil coincidente (Nascer no Ceará,
>    26/03/2018); culturas diferentes dos dois lados (banana × melão); mesmas
>    empresas e fronteira agrícola em movimento no pré-período; aquífero
>    compartilhado no trecho central. Serve como **triangulação com diferença
>    tripla**, não como identificação única (§3).
> 4. ⚠️ **A diluição continua dentro do município tratado.** Em Calzada et al.
>    (2023) o efeito só existe para mães a até 150 m do bananal e com ≥ 3 meses
>    de fumigação intensiva. Com município de residência, os −80 g viram
>    −80 g × fração exposta — mesmo em Limoeiro e Quixeré (§4).
> 5. ✅ **Há um desenho que responde a 1, 3 e 4 ao mesmo tempo, e um
>    diagnóstico que o testa sem usar o pós.** Diferença tripla de calendário
>    (estação chuvosa × trimestre gestacional), com interação por chuva. O
>    gradiente sazonal no pré-ban é o "primeiro estágio" que o projeto nunca
>    teve (§5).

---

## 1. Respostas diretas às perguntas do pesquisador

**"O que eu estou fazendo em relação a tudo isso?"**
Hoje o projeto estima a **forma reduzida do ban segundo uma proxy**: compara,
dentro do Ceará, a variação do peso ao nascer (pós − pré) entre municípios com
mais e menos área de banana. Não estima o efeito da pulverização aérea, porque
não a mede. O resultado (`ATT(d|d)` = −36,19 g, EP 15,47; inclinação em dose
+6,81, p ≈ 0,74) é uma média sobre municípios dos quais só 2 de 17 tinham
avião em 2006.

**"A cultura da banana: como fazer o DiD com isso usando a PAM?"**
A PAM diz **onde há banana**, não onde há avião. Três usos legítimos, em
ordem de força:
1. *Delimitar* unidades e doadores (perfil de culturas) e conferir que o
   controle não muda de cultura no pós.
2. *Dose de forma reduzida* no desenho estadual, lida pelo Corolário 1 de
   Denteh & Kédagni (`θ = VPP·ATT`, atenuação pura).
3. *Refinar a proxy*: banana × (1 − participação da agricultura familiar),
   ou banana em área irrigada/empresarial. Ataca o VPP baixo, mas herda o
   problema de medir cultura e não método.

O que a PAM **não** faz: sustentar uma curva dose-resposta da pulverização.
A curva (`ACR(d)`) já foi abandonada na §8 da pré-especificação; falta
alinhar §4/§6 da pré-especificação e §4.1 do paper.

**"E o Rio Grande do Norte?"**
É grupo de comparação útil para absorver choques locais comuns à Chapada
(seca, safra, mercado de frutas), mas falha o segundo quesito do curso — "o
tratamento não pode afetar o grupo de comparação" — por três canais (deriva,
aquífero, realocação), e a divisa carrega tudo que é estadual. Detalhe em §3.

**"Agricultura familiar como controle?"**
Tem dado (Censo Agro 2017, tabelas SIDRA 6851/6852: uso de agrotóxico por
tipologia, nível municipal) e precedente no mesmo território (Rigotto et al.
2013: Limoeiro, Quixeré e Russas contra 12 municípios de agricultura familiar;
ecológico, não causal). Como **grupo de controle** não serve: familiar e
empresarial diferem em pobreza, programas sociais e aplicação costal, e
dentro do município o SINASC não os separa. Serve de três outras formas
(§6): placebo, estratificação e refinamento da dose. O trade-off "saúde ×
receita" é matéria do Ensaio 2.

**"O que falta para o nível mais alto?"** Lista priorizada em §8.

---

## 2. Pergunta A — o tratamento existiu em 2019?

**Veredito: indeterminado, com leitura mais provável "legal e regulado de
2010 a 2019; suspenso de fato pela seca entre ~2012 e ~2016/17; sem prova
datada de voo na Chapada em 2017–2018".**

### 2.1 O que está estabelecido

| fato | fonte | tipo |
|---|---|---|
| Lei 1.511, 26/05/2010, art. 212: revoga a Lei 1.478/2009 | PDF da Câmara, p. 65 (`camaralimoeirodonorte.ce.gov.br/arquivos/581/Leis_1511_2010_0000001.pdf`); página conferida nesta sessão | primária |
| A mesma lei regula a prática (art. 214): proibida a menos de 1.000 m de povoações e mananciais de abastecimento e 500 m de moradias isoladas; aviso com 5 dias; multa de R$ 10 mil a R$ 100 mil; art. 217 prevê convênio de fiscalização com o MAPA | idem, p. 65–68 (lidas pelo agente de pesquisa; a p. 65 conferida aqui) | primária |
| A numeração salta do art. 212 para o 214 | idem | primária |
| SINDAG (2018) descreve a 1.511 como a que "revoga a Lei 1.478/2009 [...] e estabelece várias normas de aplicação" | apresentação à Câmara Temática de Insumos/MAPA | setorial |
| A "proibição" de 11/03/2011 foi anúncio da Comissão Nacional de Combate à Violência no Campo (SDH), sem ato normativo, TAC ou decisão judicial localizados | texto da SDH reproduzido em Combate Racismo Ambiental, 12/03/2011; Mapa de Conflitos/Fiocruz | secundária |
| ACP de julho/2011 (MPF, MPT, MP-CE; 15ª Vara Federal) existiu; pedia a proibição | Fiocruz; Ferreira, *Rev. Direito Sanitário* 15(3) | secundária |
| Em jul–ago/2011 produtores ainda defendiam a prática e movimentos ainda pediam a proibição | MST, 14/07 e 23/08/2011 | secundária |

Consequência para a flag 0: `fonte = primaria`; ⬜ atualizar
`docs/legislacao/bans-municipais-ce.csv` e o README da legislação (fora do
escopo desta rodada).

### 2.2 O achado que muda o desenho: a seca

> "A partir de 2012, segundo a agricultura, não houve novas aplicações devido
> à baixa intensidade das chuvas nas últimas quadras invernosas." — moradora
> do Tomé, Agência Brasil, 16/07/2016.

> "Atualmente, a pulverização aérea não tem acontecido na região em função da
> seca, porque a Sigatoka-amarela é uma doença fúngica, que acontece em
> função do grau de umidade." — Raquel Rigotto (Tramas/UFC), entrevista
> republicada pelo MST, 06/10/2016.

Duas fontes independentes, ambas secundárias, coerentes entre si e com o
mecanismo agronômico. Todas as evidências **datadas** de voo na Chapada que a
pesquisa encontrou são de 2007–2010.

### 2.3 A favor de tratamento real em 2019

- Produtor do **Cariri**: "até 2018, fazia duas aplicações aéreas anuais no
  seu bananal" (Globo Rural, 09/04/2021). Com data.
- Produtores da **Chapada** (Tropical Nordeste; 300 ha): comparam avião (4 h,
  25 L/ha) com costal (250 L/ha), sem datar o último voo (Globo Rural 2021;
  Agência Pública 15/02/2019).
- SINDAG, relatório de ago/2019: "quando a pulverização aérea era permitida,
  faziam-se, sobre os bananais do Cariri e da Chapada do Apodi, no máximo
  duas pulverizações por ano"; reunião de 05/08/2019 com "fotos e vídeos da
  destruição nos bananais".
- Abrafrutas: o prejuízo veio "no ano passado [2020] porque choveu muito e a
  sigatoka ficou sem controle".
- SINDAG (2023): "eram apenas quatro aeronaves no Estado". Nenhum operador
  aeroagrícola sediado no CE em dez/2018 — quem voava vinha de fora.

Todas são de parte interessada. Leitura conjunta: o avião era a tecnologia
disponível e usada **em anos chuvosos**; o ban morde quando a sigatoka volta.

### 2.4 O que isso faz com o desenho

1. **A dose 2015–2018 é medida num período de suspensão.** Soma-se à flag de
   antecipação (PL de 02/2015): a janela pré-ban é ruim por dois motivos
   independentes.
2. **O efeito do ban deve ser heterogêneo por chuva.** Interagir o pós com a
   precipitação da quadra chuvosa (fev–mai) é previsão falsificável: efeito
   em 2020 (chuvoso), pouco ou nada em anos secos.
3. **O Cariri entra no mapa.** É o único lugar com declaração datada de uso
   até 2018. ⬜ Identificar os municípios (o projeto conhece 7 municípios com
   aeronave em 2006; cruzar com a banana do Cariri).
4. **Divergência de frequência a registrar:** Tramas/Abrasco falam em 6–8
   aplicações/ano (base 2009–2010); o setor, em "no máximo duas".
5. **A fonte que fecha a questão é o relatório mensal ao MAPA** (IN 2/2008,
   Anexo V: UF, município, cultura, área). O Pedido D deve pedir
   **2012–2018, por município, incluindo operadores sediados fora do CE, e
   também o RN**.

### 2.5 Não confirmado

Número, liminar e sentença da ACP de 2011 (PJe/JFCE e TRF5 não consultados
diretamente; a notícia do MPT devolveu HTTP 500); qualquer voo datado na
Chapada em 2012–2018; parecer do Tramas de jun/2016; relatório de 2019 da
SEDET-CE citado na Nota Técnica MAPA 26/2025; uma "Lei 550/2011 (Limoeiro)"
citada numa dissertação da UFPR (pode ser erro).

---

## 3. Pergunta B — a Chapada é um experimento natural CE×RN?

### 3.1 O que sustenta a ideia

- A Chapada é uma unidade física cortada por uma divisa política; `Chapada`
  como confundidor comum some na diferença (DAG 3 do doc 22).
- Os dois únicos tratados com aeronave em 2006 (Limoeiro 18 estabelecimentos,
  Quixeré 9) tocam a divisa do RN.
- O RN regula e não proíbe a aplicação aérea (Decreto RN 26.594/2017). Não se
  encontrou PL estadual nem lei municipal potiguar de proibição (ausência em
  busca, não `ausente_conferido`).

### 3.2 O que a derruba como identificação única

| problema | evidência | efeito no contraste CE−RN |
|---|---|---|
| **Política estadual coincidente** | Nascer no Ceará, lançado em 26/03/2018 (pré-natal de alto risco, redução de morte neonatal); Mais Infância Ceará desde 08/2015 | confunde: melhora o CE no pós por outra via |
| **Chikungunya assimétrica no pré** | CE: 1.149/100 mil em 2017, 73,9% dos casos do país | pré-período do CE deprimido → recuperação espúria |
| **Culturas diferentes** | CE: banana; RN contíguo: melão, melancia, mamão. Banana potiguar está no Vale do Açu, fora da Chapada | o controle não tem a cultura do avião; não se achou aviação agrícola operando no RN |
| **Fronteira agrícola em movimento** | Agrícola Famosa, Bessa e UGBP avançam sobre Apodi/Felipe Guerra em 2015–2018 (inclusive banana "na divisa do RN-CE") | tendência diferencial no controle dentro do pré |
| **Mesmas firmas** | Agrícola Famosa e Del Monte nos dois estados | risco de realocação (não há evidência de que ocorreu) |
| **Aquífero** | ANA (2010): Jandaíra e Açu "possuem fluxos interestaduais", mas só na sub-bacia Mata Fresca; a oeste drena para o Jaguaribe, a leste para o Apodi-Mossoró | interferência restrita a Quixeré–Jaguaruana–Baraúna |
| **Água de beber heterogênea** | sedes de Mossoró e Baraúna: aquífero Açu (confinado); Chapada de Limoeiro: canal do perímetro; rural: Jandaíra | a via água não é municipal |
| **Inferência** | a lei é atribuída no nível do estado: 1 cluster tratado | p-valor municipal não é definitivo |

Dois canais atenuam (deriva e água melhoram o RN) e um infla (realocação
piora o RN). **O sinal líquido do viés de interferência não é assinável a
priori** — o que o doc 11 §3.3 já dizia, agora com a hidrogeologia.

### 3.3 Delimitação

- A **RIDE nunca foi instituída** (PLP 98/2007 apenas "autoriza"; só existem
  três RIDEs no país). A lista do PLP — 21 municípios do RN, usada em
  `RIDE_CHAPADA_RN` — é política e muito mais larga que a Chapada (inclui o
  Vale do Açu e o litoral salineiro).
- **Recorte mais defensável: o hidrogeológico da ANA (2010)** — Baraúna
  (30% da área), Mossoró (24%), Quixeré (21%), Jaguaruana (11%), Limoeiro do
  Norte (10%), Tabuleiro do Norte; Russas, Aracati e Dix-Sept Rosado somam 1%.
- ⚠️ Com esse recorte o controle potiguar cai para **2 municípios**
  (Baraúna e Mossoró), e Mossoró é polo urbano. O `mde-desenhos` com 21
  doadores superestima o que a Chapada estrita oferece.
- Qualquer lista precisa ser pré-especificada **antes** de cruzar com o
  desfecho.

### 3.4 Veredito

A fronteira entra como **uma das diferenças** de um desenho que tem outra
fonte de variação (calendário, §5), e como base de doadores para um sintético
(§5.3). Sozinha, não identifica. Três grupos, como o material do curso pede:
Chapada-CE (tratado), Chapada-RN (não tratado **exposto**), e um terceiro
distante e agroclimaticamente parecido (não tratado **não exposto**).

---

## 4. Pergunta C — o que a literatura análoga implica para o tamanho do efeito

Calzada, Gisbert & Moscoso (2023), lido no manuscrito aceito:

- Exposição = mãe a **até 150 m** do perímetro do bananal **e** ≥ 3 meses de
  fumigação intensiva (> 4 galões/ha) na gestação. Controle: mães entre 150 m
  e 2,5 km. A distância sozinha não mostra gradiente.
- −80 g com ≥ 3 meses intensivos; −74 g (1º trimestre) e −75 g (2º); 3º não
  significativo. Efeito fixo materno: −327 g.
- Frágil ao limiar: com 3 galões/ha o efeito some; com exposição "qualquer
  dose" cai para −18 a −30 g.
- Intensidade vem da estação chuvosa (sigatoka) — **o mesmo mecanismo do
  §2.2**.

Implicações:

1. **Diluição intramunicipal.** Efeito municipal esperado ≈ −80 g × fração
   dos nascimentos do município a ≤ 150 m de bananal pulverizado. Se a fração
   for 10%, são ~8 g. ⚠️ Ordem de grandeza ilustrativa; os insumos são
   suposições, não dados do SINASC.
2. **O estimando deles não é o nosso.** Eles medem exposição intensa; o ban
   mede a *retirada do método*, com substituição por terrestre.
3. **A correção de calibração da flag 7 muda.** O "80–150 g" do CLAUDE.md
   vinha do resumo; o texto dá −80 g (agregado) e ~−75 g por trimestre. O
   teto de ~9 g de θ esperado **cai**, não sobe, quando se soma a diluição
   intramunicipal.

Outros análogos (referências no doc 21): Larsen et al. (2017) — efeito só no
topo de 5% da exposição; Reynier & Rubin (2025) — −75 g no 1º decil de peso
previsto contra −6 g no 10º; Jones (2020) — único que isola fungicida.
Padrão comum: **efeito concentrado na cauda**, diluído na média.

---

## 5. Blueprint metodológico

### 5.1 Parâmetro-alvo (a decidir com o orientador; aqui a recomendação)

> Efeito da **retirada da aplicação aérea de fungicida em bananais** sobre o
> peso ao nascer de gestações que coincidiriam com a estação de pulverização,
> nos municípios cearenses onde a prática existia.

É um EMPT (ATT) sobre *coortes expostas*, não sobre municípios-ano. Declara o
que a dose-resposta municipal nunca pôde declarar: **quem** é tratado.

Consequência honesta: **curva dose-resposta municipal não é estimável** com 2
(ou poucos) municípios genuinamente tratados. "Dose" passa a ser temporal
(meses de gestação na estação intensiva) e climática (chuva da quadra).

### 5.2 Desenho primário candidato: diferença tripla de calendário

```
Y_imt = β · (CE_i × Pós_t × Estação_m) + interações de 2ª ordem
        + EF município + EF mês-ano + ε
```

- `Estação_m`: gestação com trimestre(s) dentro da estação de pulverização.
- Variação da terceira diferença é **dentro do município, entre coortes
  mensais** — remove choques município-ano (Nascer no Ceará, chikungunya,
  seca agregada) comuns às coortes.
- Hipótese de identificação (uma só, Olden & Møen 2022): o hiato sazonal
  evoluiria igual no tratado e no controle sem o ban.
- Extensão: `× Chuva_t` (quadra chuvosa), previsão do §2.4.
- Já codificado em parte: `scripts/estimate/14_mde_calendario.py` (pico 2–5
  como HIPÓTESE). ⬜ Nunca rodou com dado real.

**O que ele exige e o projeto não tem:** o calendário real de aplicação na
Chapada (banana **irrigada** — a sazonalidade pode ser mais fraca que no
Equador). É a LAI ao MAPA/ADAGRI.

**O que ele não resolve:** a diluição espacial (§4). Concentra o contraste
nas coortes expostas, não nas mães expostas.

### 5.3 Triangulação

| desenho | estimando | hipótese | inferência | papel |
|---|---|---|---|---|
| **Sintético / SDID** do agregado tratado (Limoeiro+Quixeré; + Cariri se confirmado), doadores do RN e do CE não exposto, trimestral | ATT do agregado | pré-ajuste; doadores sem transbordamento | placebo no espaço + conformal no tempo (Chernozhukov et al. 2021) | complementar |
| **DiD de fronteira com microdado** (pares CE–RN) | ATT menos transbordamento | tendências paralelas + sem choque estadual | Ferman–Pinto (2019), com permutação, Conley–Taber e Hagemann (2025) ao lado | sensibilidade; só convence se as quatro concordam |
| **Estadual por dose de banana** (o atual) | `θ = VPP·ATT` | PT no D observado | já implementada no `04_robustness.py` | forma reduzida secundária |

Inferência: wild cluster bootstrap isolado **não é defensável** com poucos
tratados (MacKinnon & Webb 2017). O microdado não cria clusters.

### 5.4 O diagnóstico que vem antes de tudo

**Gradiente sazonal no pré-ban.** Em 2015–2018 — e, melhor, em 2007–2011,
quando há prova de voo —, coortes gestadas na estação intensiva em Limoeiro e
Quixeré têm peso menor que as demais, em relação ao controle?

- Se **sim em 2007–2011 e não em 2013–2017**: confirma a suspensão pela seca
  e dá o "bite" que o Mixtape exige antes do desfecho.
- Se **não em nenhum**: ou não havia exposição relevante, ou a diluição
  intramunicipal é total. Nos dois casos o DiD do ban não tem o que detectar.

Não usa o pós. Não gasta graus de liberdade da análise confirmatória. Exige
estender o SINASC para trás (o FTP tem a série desde 1996).

### 5.5 Seleção para nascimento vivo

SINASC condiciona em nascido vivo (colisor, DAG 1). Tratar com desfecho
composto (nascidos vivos + óbitos fetais do SIM no denominador) e com
características maternas como desfecho-placebo.

---

## 6. Pergunta E — agricultura familiar

- **Dado:** Censo Agro 2017, SIDRA 6851 e 6852 (estabelecimentos por
  tipologia × uso de agrotóxicos), 6753/6754/6769/6770 (número e área por
  tipologia), nível municipal confirmado na página do SIDRA. Conta
  estabelecimentos que usaram, não quantidade. ⬜ Categorias da 6851 não
  conferidas (a API do IBGE é bloqueada pelo proxy remoto).
- **Método de aplicação em 2017:** não se achou equivalente à tabela 1008 de
  2006. ⬜ Hipótese a conferir: a 6877 (veículos) teria "aeronaves" — seria
  *posse*, não *uso*.
- **Usos defensáveis, em ordem:**
  1. **Grupo de tratamento falso** (teste 2 do DD em Gertler): municípios de
     banana quase só familiar não deveriam reagir ao ban. É placebo, não
     controle — e é barato.
  2. **Refinar a dose:** banana × (1 − participação familiar). Ataca o VPP.
  3. **Estratificar/parear** por participação familiar.
- **Não usar como controle direto:** seleção em tipo de agricultura (DAG 4);
  agronegócio avançando sobre Apodi no pré; Acampamento Zé Maria do Tomé e
  assentamentos de Apodi ficam *dentro* dos municípios do agronegócio.
- **Ensaio 2:** produção de banana no CE teria crescido 20% em 2019 e seguido
  crescendo (IBGE via UFRN, fonte secundária — ⬜ conferir na PAM), contra o
  relato setorial de queda de 30%. É a evidência do lado do custo.

---

## 7. Contraprova (o que um parecerista hostil diria)

1. **"Vocês trocaram de desenho depois de ver um resultado ruim."** Verdade.
   Defesa possível: o desenho de calendário e o diagnóstico do §5.4 são
   pré-especificados **agora**, antes de cruzar exposição e desfecho; o
   resultado estadual fica reportado como está.
2. **"Sem primeiro estágio não há paper."** Procede. Sem o relatório do MAPA
   ou o gradiente sazonal pré-ban, o projeto não mostra que a política teve
   "bite".
3. **"O sinal de −36 g é o Nascer no Ceará ao contrário, ou composição."**
   Não testado. A diferença tripla responde ao primeiro; o desfecho composto,
   ao segundo.
4. **"Banana irrigada não tem estação."** Possível. É a hipótese que mais
   ameaça o §5.2 e só o calendário real resolve.
5. **"Folde a mão."** O checklist da 2ª edição do Mixtape termina em "Don't
   Do Diff-in-Diff". Com 2 tratados, diluição intramunicipal e suspensão pela
   seca, um **paper de diagnóstico de poder e medida** — que é o que o
   `paper/` já é — pode ser o produto honesto do Ensaio 1, com o Ensaio 2
   carregando a contribuição. É decisão a levar ao orientador, não a evitar.

---

## 8. O que falta, em ordem

**Bloqueia tudo (ato do pesquisador):**
1. Protocolar a **LAI ao MAPA** (Fala.BR): relatórios mensais IN 2/2008,
   **2012–2018**, por município, **CE e RN**, incluindo operadores de outras
   UFs. Minuta: `docs/legislacao/lai-mapa-relatorios-mensais-minuta.md`
   (⬜ ampliar período e UF).
2. Localizar a **ACP de 2011**: consulta por parte no PJe/JFCE (FAPIJA, Del
   Monte, Frutacor, Tropical Nordeste) ou pedido à PRM de Limoeiro do Norte.

**Rodar na máquina local (dados não existem no contêiner):**
3. `make mde-calendario` e `make mde-desenhos` com dado real; repetir o
   segundo com o recorte ANA (Baraúna + Mossoró) no lugar da RIDE.
4. **Diagnóstico do §5.4**: SINASC 2005–2018 para Limoeiro, Quixeré e
   controles; gradiente sazonal por período. Script novo — ⬜ escrever só
   depois de pré-especificar a estação.
5. `make real` + `04_robustness.py` para fechar os `[·]` do doc 17 §7.
6. Chuva da quadra (FUNCEME/INMET) por município-ano; PAM de banana por
   município potiguar da divisa e no CE em 2018–2021.
7. SIDRA 6851/6852/6877 e tabela 1008 para o RN (fora do proxy).

**Decisões para o orientador (além das seis do doc 17 §5):**
8. Estimando: forma reduzida por proxy × retirada do método em coortes
   expostas (§5.1).
9. Desenho primário: calendário (§5.2) × manter o estadual × "foldar" (§7.5).
10. Delimitação da Chapada: ANA × RIDE × microrregião.
11. Incluir o Cariri no grupo tratado.
12. Pré-especificar estação, chuva e cauda antes de qualquer cruzamento.

**Coerência documental (rodada seguinte, com autorização):**
13. Alinhar pré-especificação §4/§6 e paper §4.1 ao estimando; aplicar o
    doc 17 §7; corrigir no CLAUDE.md a calibração "80–150 g".
14. `bans-municipais-ce.csv`: fonte da 1.511 → `primaria`.
15. `RIDE_CHAPADA_RN`: documentar que é lista de PLP não instituído.

---

## 9. Limites desta rodada

- Nenhuma estimativa nova. Todos os números de resultado vêm de
  `paper/secoes/06-diagnostico-poder.tex` e dos docs 16–19.
- Projetos **não commitados** da máquina do pesquisador não foram vistos.
- Fontes de imprensa e de parte interessada estão marcadas como tais; a
  conclusão do §2 é graduada por isso.
- Quatro agentes de pesquisa fizeram a coleta; a p. 65 da Lei 1.511 foi
  conferida diretamente. O restante das citações literais não foi reaberto
  uma a uma.
- A forma de revisão de literatura (sistemática, de escopo, narrativa…) é
  decisão do pesquisador e está em aberto; o doc 21 não reivindica cobertura.
