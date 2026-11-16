# A literatura brasileira de agrotóxicos, passada pelo filtro do desenho

> ⚠️ **Três afirmações desta página foram corrigidas pela segunda rodada**
> (`leituras-segunda-rodada.md` §6): o pulverizador costal não é fator de risco
> "documentado" (15 casos, +16% bruto); Paumgartten (2020) não foi lido por
> ninguém do projeto e não sustenta a frase de lacuna; Jones (2020) não separa
> fungicida de inseticida. E a linha do tempo do §4.1 tem versão corrigida no
> §3 daquele documento: o produtor que voou "até 2018" é do Cariri.

*2026-11-16. Leitura das três peças de Viçosa (UFV/PPGEA), das suas listas de
referências, e de três textos sobre a Chapada do Apodi e a legislação. O filtro
é o desenho do `docs/framework-dissertacao.md`: DiD binário na Chapada do Apodi,
lado cearense (proibido em 2019) contra lado potiguar, Callaway & Sant'Anna
(2021).*

**Como ler as marcas.** ✅ lido na íntegra; ◐ lido em parte (o trecho está
dito); 🔎 conhecido só pela citação de quem leu. Todo DOI desta página foi
conferido no registro do Crossref em 2026-11-16, e as entradas correspondentes
do `paper/referencias.bib` foram geradas do registro, não digitadas.

---

## 1. O que esta leitura muda no projeto

1. **Ninguém, nesta literatura, usa diferenças em diferenças sobre agrotóxico.**
   Nas bibliografias da tese de Rodrigues (2022) e da dissertação de Januzzi
   (2025) não há um único estudo de DiD, nem Callaway–Sant'Anna, nem
   Goodman-Bacon. A economia brasileira de agrotóxicos identifica por proxy de
   uso (despesa por hectare, índice por cultura) com efeito fixo ou instrumento
   climático. O projeto entra por outra porta: um choque de política com data e
   fronteira.
2. **As duas proxies nacionais são cegas para o caso do Ceará.** O índice de
   Januzzi cobre sete culturas de Mato Grosso e exclui, por regra, as que não
   são comuns lá; banana e melão caem nessa exclusão. A despesa por hectare de
   Rodrigues não distingue método de aplicação. Nenhuma das duas menciona
   pulverização aérea como objeto, nem o Ceará, nem o Rio Grande do Norte.
3. **O resultado nacional sobre nascimentos é nulo, e a razão é de desenho.**
   Com efeitos fixos de município e de ano, Januzzi acha 0,74 caso de baixo
   peso por mil nascidos por kg/ha, com erro-padrão de 0,67. O "+1,2, p < 0,10"
   da versão de congresso é a especificação **sem efeito de ano**, numa janela
   (2019–2022) que contém a pandemia. Lição direta para o Ensaio 1: nesse
   período, o que separa efeito de artefato é ter um grupo de comparação
   contemporâneo. É o que o lado potiguar dá.
4. **O SINAN mede notificação, e notificar depende de infraestrutura.** Em
   Rodrigues, o número de municípios que notificam quase triplica entre 2006 e
   2017, e os que notificam têm mais hospital, mais vigilância e mais renda.
   Para o desfecho de intoxicação do Ensaio 1, isso obriga a conferir se a
   capacidade de notificação evoluiu igual nos dois lados da divisa.
5. **Óbito por intoxicação não tem poder; suicídio é a maior parte.** Dos
   3.491 óbitos por agrotóxico no país em 2006–2017, 3.039 são suicídios; os
   não intencionais foram 24 em 2006 e 54 em 2017. No município, esse desfecho
   não existe. Fica o caso notificado não intencional, com a tentativa de
   suicídio como placebo.
6. **O pulverizador costal como fator de risco é hipótese, não achado.**
   Soares, Freitas & Coutinho (2005), lido depois no original, tem 15 casos e
   um aumento bruto de 16%, sem intervalo. O que sustenta a hipótese de
   substituição do framework (§2) é o argumento de mecanismo de Valadares et
   al. (2020): o risco agudo ocupacional é da aplicação manual.
7. **No Nordeste, na média, não há sobreuso.** Rodrigues estima que o real
   marginal gasto com agrotóxico rende R$ 1,35 no Nordeste (IC 1,19–1,51),
   contra R$ 0,10 no Sul. Para o Ensaio 2, restringir uso no Nordeste custa
   produção na margem. Ressalva: é média de 1.659 municípios, quase todos de
   sequeiro, e não descreve a fruticultura irrigada da Chapada.
8. **Sobre 2012–2018 na Chapada, a literatura acadêmica se cala.** O período
   documentado da pulverização aérea é 2000–2010. Depois disso há relatos de
   entrevista em Aguiar (2017), o parecer do Tramas (2016) e imprensa. A LAI ao
   MAPA continua sendo o que fecha a premissa.
9. **Sobre o Rio Grande do Norte, nenhum dos textos lidos traz norma,
   projeto ou decisão judicial.** Reges (2023) lista dez estados com projetos
   inspirados na lei cearense, e o RN não está entre eles. É ausência em três
   textos, não prova de ausência: ⬜ conferir na Assembleia do RN.

---

## 2. Viçosa (UFV, Programa de Pós-Graduação em Economia Aplicada)

O grupo: José Gustavo Féres orientou Loredany Rodrigues (2022), que coorientou
Stela Januzzi (2025) com Leonardo Cardoso. São as duas pontas da mesma agenda:
intoxicação aguda e produtividade de um lado, saúde infantil do outro.

### 2.1 Rodrigues (2022), tese ✅

*Impactos socioeconômicos do uso de agrotóxicos no Brasil*, UFV,
`10.47328/ufvbbt.2022.752`, 117 f. Dois ensaios. (A capa diz "do uso de
agrotóxicos"; o resumo e o registro do repositório, "dos agrotóxicos". Citar
pela ficha.)

**Ensaio sobre intoxicação (cap. 2).**

| | |
|---|---|
| pergunta | mais intensidade de uso → mais intoxicação e morte por agrotóxico? |
| dados | painel municipal de dois pontos, 2006 e 2017; SINAN; 5.328 municípios |
| exposição | despesa com agrotóxico (Censo Agro) ÷ área de lavoura, em R$/ha; média 215 |
| identificação | Poisson com efeitos fixos e função de controle; instrumentos: média e desvio-padrão da temperatura anual |
| resultado | +R$ 10/ha → +13,1% nos casos por 100 mil (coef. 0,0130, EP 0,0049; Tab. 2, p. 41). Rural: +16,7%. Sem unidade de vigilância: +22,8% |
| óbitos | nada significativo; só 78 municípios tiveram óbito não intencional |
| monetização | ≈ 2.539 casos adicionais → até US$ 2,8 milhões por +R$ 10/ha, com os custos unitários de Soares & Porto (2012) |

*Pelo filtro.*
- **Serve ao Ensaio 1:** a anatomia do SINAN (itens 4 e 5 da §1); os controles
  de capacidade de notificação (unidade de vigilância em saúde e hospital, do
  CNES); a separação intencional × não intencional.
- **Não serve como calibração.** O estimador com instrumento dá um efeito nove
  vezes maior que o sem instrumento (elasticidade ≈ 2,8 contra ≈ 0,3); o
  primeiro estágio tem sinal oposto ao da motivação (temperatura mais alta
  **reduz** a despesa) e a tese não reporta estatística F; a amostra efetiva
  são os 1.641 municípios que notificam. E mede gasto por hectare, não método
  de aplicação.
- **Fraqueza de desenho:** dois períodos. Não há pré-tendência a testar nem
  estudo de evento. A variação que identifica é a mudança de temperatura dentro
  da UF entre 2006 e 2016, e o calor afeta também o uso de EPI (a própria tese
  diz que o equipamento é quente), a volatilização e o mix de culturas.

**Ensaio sobre produtividade (cap. 3).**

| | |
|---|---|
| pergunta | o agrotóxico marginal paga o que custa? |
| método | controle de danos de Lichtenberg & Zilberman (1986), especificação Weibull, contra Cobb-Douglas; Censos 2006 e 2017; sem efeito fixo de município e sem instrumento |
| resultado | receita marginal por real gasto: Brasil 0,77; **Nordeste 1,35**; Sudeste 0,71; Centro-Oeste 0,36; Sul 0,10 (Tab. 3, p. 92). Uso excessivo em 4.432 de 5.171 municípios em 2017 |
| determinantes | crédito rural aumenta o sobreuso; agricultura orgânica e cooperativa reduzem |

*Pelo filtro.*
- **Serve ao Ensaio 2:** dá o lado do custo em linguagem de livro-texto. Onde a
  receita marginal é menor que 1, reduzir uso é ganho privado além de social;
  onde é maior, há custo de produção a pesar. O Nordeste está no segundo caso.
- **Cuidado:** o veredito depende da forma funcional (Cobb-Douglas dá 1,61 para
  o Brasil, Weibull dá 0,77), e a tese não inclui o dano à saúde na conta, o
  que ela mesma deixa como agenda. É exatamente o que o Ensaio 2 pode fazer num
  caso só.
- **Não há heterogeneidade familiar × patronal.** A agricultura familiar
  aparece só como contexto. É espaço livre para o projeto.

### 2.2 Rodrigues & Féres (2022), *RESR* 🔎

`10.1590/1806-9479.2021.244491`. **Outro estudo, não o capítulo da tese:**
Censo Agro 2006, escore de propensão generalizado, dose-resposta entre
intensidade de uso e proporção de estabelecimentos com intoxicados. Interessa
por dois motivos. É o precedente brasileiro de dose-resposta em agrotóxico, e é
o método que o orientador já usou; cabe citar ao explicar por que o projeto
**saiu** da dose (framework §0). ⬜ Ler.

### 2.3 Januzzi (2025), dissertação ✅

*Impacts of Pesticide Exposure on Birth Outcomes and Child Health in Brazil*,
UFV, `10.47328/ufvbbt.2025.749`, 48 f. Versão de congresso: Januzzi, Cardoso &
Rodrigues, ENABER 2025 ✅.

| | |
|---|---|
| pergunta | morar em município de agricultura intensiva em agrotóxico piora baixo peso, prematuridade, mortalidade infantil e câncer infantil? |
| dados | 5.510 municípios, 2019–2022, anual; SINASC, SIM, Painel-Oncologia |
| exposição | Σ (kg de ingrediente ativo por ha da cultura em **Mato Grosso**, média 2019–22) × área da cultura no município ÷ área agrícola. Sete culturas: soja, algodão, milho, cana, café, arroz, feijão |
| especificação | efeitos fixos de município e ano, erro agrupado por município, sem peso |
| resultado | baixo peso 0,738 (EP 0,669); prematuridade 0,790 (0,938); mortalidade infantil −0,077 (0,257); câncer −0,15 (1,11). Nada significativo (Tabs. 5 e 6) |

**As duas versões, conferidas tabela a tabela.** Mesma amostra, mesmo
coeficiente com os dois efeitos fixos (0,738). O "+1,197, p < 0,10" que o
resumo do ENABER leva à manchete é a coluna **sem efeito fixo de ano**; a
dissertação traz o mesmo número, rotula a coluna de "pooled" e conclui pelo
nulo. O que se pode citar é o nulo. Fica corrigida a pendência que o framework
anotava.

*Pelo filtro.*
- **Por que o índice não enxerga a Chapada.** A regra de seleção exclui
  culturas "prevalent in other states but not commonly grown in Mato Grosso"
  (p. 24–25). No Ceará o índice vê milho e feijão de sequeiro com a intensidade
  mato-grossense, e, como divide pela área agrícola, dá ao sertão um valor
  parecido com a média nacional e ao polo bananeiro um valor baixo. Ordena o
  estado ao contrário do que interessa. A autora admite que o índice se apoia
  em "just seven crops".
- **Por que o nulo informa pouco.** Os "shifts" não variam no tempo, são sete e
  vêm de um estado só: com efeito fixo de município, o que identifica é a
  mudança de composição de área em quatro anos, que é pequena e é escolha do
  produtor. Não é o desenho de Borusyak, Hull & Jaravel que a dissertação
  invoca.
- **O que se aproveita:** as definições de desfecho (iguais às do projeto); a
  lista de controles maternos, dos quais gemelaridade e idade materna são os
  defensáveis (pré-natal e parto hospitalar podem responder ao tratamento, e
  baixo peso como controle da mortalidade é controlar por mediador); a
  constatação de que taxa municipal sem peso é dominada por município
  minúsculo.
- **Magnitude de referência:** baixo peso médio de 7,9% e prematuridade de
  11,4% no país. A dissertação não usa peso em gramas nem óbito fetal.
- **Calzada, dois números.** A dissertação cita 38–89 g; o resumo publicado
  diz 80–150 g. O repositório já tinha a explicação (doc 19): o primeiro é a
  estratégia de calendário do *working paper*, o segundo é o da exposição alta
  na versão publicada. ⬜ Confirmar no texto integral antes de calibrar.

### 2.4 Rodrigues, Fortini & Neves (2023), *IJEST* ✅

`10.1007/s13762-022-04032-y`. Controle biológico e eficiência técnica, Censo
2006, balanceamento por entropia e fronteira estocástica. Municípios intensivos
em controle biológico são mais eficientes (0,863 contra 0,823), **menos no
Nordeste**, onde a relação se inverte (0,752 contra 0,808) e só 0,51% dos
estabelecimentos adotam. Para o Ensaio 2: a alternativa tecnológica ao químico
existe no país e praticamente não existe na região do estudo.

---

## 3. O que as referências de Viçosa apontam

Triagem das duas bibliografias. Entram as que passam pelo filtro.

### 3.1 Agrotóxico e saúde, Brasil

| referência | o que é | uso no projeto |
|---|---|---|
| Dias, Rocha & Soares (2023), *REStud*, `10.1093/restud/rdad011` | glifosato, soja, montante/jusante; +0,88 óbito infantil por mil; externalidade de US$ 583 milhões/ano | o padrão de identificação no país; **outro químico e outro canal** |
| Skidmore, Sims & Gibbs (2023), *PNAS*, `10.1073/pnas.2306003120` | expansão da soja e leucemia infantil | os próprios autores evitam linguagem causal; citar como associação |
| Pignati et al. (2017), *Ciênc. Saúde Colet.* 22(10), `10.1590/1413-812320172210.17742017`; Pignati, Oliveira & Silva (2014), `10.1590/1413-812320141912.12762014` | imputação de uso por cultura a partir do receituário de MT | é a base do índice de Januzzi; explica a cegueira para a fruticultura |
| Oliveira et al. (2014), *Ciênc. Saúde Colet.* 19(10), `10.1590/1413-812320141910.08512014` | malformação congênita em municípios de alto uso, MT | antecedente epidemiológico de desfecho ao nascer |
| Siqueira et al. (2010), `10.1007/s00128-010-0027-8` | ecológico nacional: uso × prematuridade, baixo peso, malformação | idem |
| Paumgartten (2020), `10.1016/j.cotox.2020.01.003` | revisão: os estudos brasileiros são ecológicos, transversais ou caso-controle, com exposição imprecisa | **a frase de lacuna** para a introdução |
| Moraes (2019), Ipea TD 2506 | padrões de uso e regulação; soja, milho e cana são 76% das vendas | contexto; e por que o caso da banana é atípico |
| Valadares, Alves & Galiza (2020), Ipea 🔎 | Censo Agro 2017: uso de agrotóxico por agricultura familiar e não familiar | **fonte candidata para a heterogeneidade** do framework §4.3. ⬜ ler |
| Carneiro et al. (2015), Dossiê Abrasco 🔎 | razão de subnotificação de 1:50, atribuída à OMS | citar com a ressalva de que é número de segunda mão |

### 3.2 Custo social e instrumentos

| referência | o que é | uso no projeto |
|---|---|---|
| Soares & Porto (2009), *Ecol. Econ.* 68, `10.1016/j.ecolecon.2009.05.008` | custo da intoxicação aguda no Paraná: de 8% a 64% do benefício de herbicidas e inseticidas no milho | o molde brasileiro de custo-benefício |
| Soares & Porto (2012), *Rev. Saúde Pública* 46(2), `10.1590/S0034-89102012005000006` | custos unitários por caso: hospitalar US$ 129–740; dias parados US$ 131–358 | **os preços** para valorar o ATT sobre intoxicação |
| Cunha & Soares (2020), *Cad. Saúde Pública* 36(10), `10.1590/0102-311X00225919` | desoneração de R$ 9,8 bilhões em 2017, R$ 6,2 bilhões de ICMS | o instrumento-preço brasileiro tem o sinal trocado |
| Lichtenberg & Zilberman (1986), *AJAE* 68(2), `10.2307/1241427` | econometria do controle de danos | base de Rodrigues cap. 3; linhagem do orientador |
| Maumbe & Swinton (2003), `10.1016/S0277-9536(03)00016-9` | custo de saúde oculto: 45–83% do gasto com pesticida, Zimbábue | ordem de grandeza internacional |
| Harrington & Portney (1987), *J. Urban Econ.* 🔎 | disposição a pagar = dano + gasto preventivo + gasto de remediação | esqueleto da valoração |

### 3.3 Identificação causal, outros países

| referência | o que é | uso no projeto |
|---|---|---|
| Calzada, Gisbert & Moscoso (2023), *JAERE*, `10.1086/725349` | fumigação aérea de bananais, Equador | **o análogo**; fonte do efeito esperado |
| Camacho & Mejía (2017), `10.1016/j.jhealeco.2017.04.005` | aspersão aérea, Colômbia | método aéreo, outro químico |
| Larsen, Gaines & Deschênes (2017), `10.1038/s41467-017-00349-2` | efeito só na cauda de exposição | por que a média municipal dilui |
| Jones (2020), *Land Econ.* 96(2), `10.3368/le.96.2.149` | instrumento por praga invasora; +10% de **fungicida** → +0,15 p.p. de prematuridade e +0,08 p.p. de baixo peso | **novo no projeto**, e é o único com efeito de fungicida separado, que é a classe da banana |
| Regidor et al. (2004), `10.1136/oem.2003.009043` | exposição paterna e óbito fetal por causa | apoio para o óbito fetal como desfecho |
| Borusyak, Hull & Jaravel (2025), *JEP*, `10.1257/jep.20231370` | guia de *shift-share* | resolve a pendência do doc 15: é este o "2025" que Januzzi cita |

---

## 4. A Chapada do Apodi: o que os textos documentam

### 4.1 Linha do tempo da pulverização aérea, lado cearense

| período | o que se sabe | fonte | tipo |
|---|---|---|---|
| anos 2000 | começa com a chegada das empresas de fruticultura irrigada | Aguiar p. 31, 154 | secundária |
| 2000–2010 | cerca de 4 milhões de litros de calda por via aérea; difenoconazol, piraclostrobina + epoxiconazol, trifloxistrobina + tebuconazol, propiconazol | Aguiar p. 36, 154, citando Teixeira (2011) | secundária |
| 2003–2015 | cerca de 1.000 ha com aplicação aérea, 2,27% da banana do estado | nota de Zuza de Oliveira (2016), via parecer do Tramas | secundária, do lado dos produtores |
| 2008–2009 | 6 a 8 aplicações na quadra chuvosa, sobre ~2.950 ha | Marinho (2010), via Dossiê Abrasco e ADI 6137 | secundária |
| nov/2009–abr/2010 | a lei municipal não interrompeu os voos; avião fotografado em 22/03 e 19/04/2010 | Reges p. 63–69, citando o processo criminal | documental |
| 2010 | um produtor contratava o avião e cobrava dos demais por hectare | Reges p. 69, depoimento no processo | documental |
| 2010–2014 | "muitos episódios" presenciados por quem trabalhava a ~100 m do campo de pouso | Aguiar p. 108–109 | relato |
| 2012 em diante | "não houve novas aplicações [no Tomé] devido à baixa intensidade das chuvas" | Agência Brasil, 16/07/2016 | relato, imprensa |
| 2014 | bananal pulverizado, "inclusive por meio de pulverização aérea", a ~50 m de uma gestante | Aguiar p. 119 | relato |
| jun/2016 | Limoeiro, Quixeré e Russas são onde a pulverização aérea "ocorre" | parecer do Tramas | parecer técnico |
| jul/2017 | as empresas, "até alguns anos atrás, realizavam a pulverização aérea" | Aguiar p. 115 | relato |
| até 2018 | "fazia duas aplicações aéreas anuais" | produtor, Globo Rural, 09/04/2021 | relato, imprensa |

**Leitura.** A prática está bem documentada até 2010, tem testemunho até 2014 e
relatos que se contradizem para 2015–2018: uma moradora fala no passado em
2017, um produtor diz que voou até 2018. O mais provável é uma prática
rarefeita pela seca de 2012–2017 e localizada em poucas fazendas. Isso não muda
o desenho; muda a expectativa de efeito, e reforça que o resultado se reporta
como intervalo.

A fonte primária que falta ler é **Teixeira (2011)**, capítulo do livro de
Rigotto (p. 525–546): é de onde saem os 4 milhões de litros.

### 4.2 Aguiar (2017) ◐

Dissertação, UFC, orientação de Raquel Rigotto. Lidas na íntegra as p. 1–80 e
os trechos de resultados; o restante foi varrido por palavra-chave.

Estudo de casos múltiplos na comunidade do Tomé (≈ 2.500 habitantes), campo em
julho de 2017: 8 famílias, 11 crianças, 5 famílias com malformações e 3 com
puberdade precoce. Sete das oito famílias tiveram o nascimento ou o diagnóstico
depois de 2014. Sem grupo de comparação; a autora conclui por "fortes
evidências" por triangulação.

*Pelo filtro.* É a razão de existir do projeto, e não é evidência causal. Dois
usos: o *background* (o problema, na teoria da mudança), e o tamanho do funil.
Uma comunidade de 2.500 pessoas em municípios que somam ~160 mil dá a ordem de
grandeza da fração exposta, e ela é de poucos por cento. Não mede baixo peso,
prematuridade nem óbito fetal, e não traz número de nascimentos.

### 4.3 Reges (2023) ◐

Tese de doutorado em História, UFC (não dissertação, como o framework anotava).
Lidos os trechos sobre a cronologia; o resto foi varrido.

Serve ao *background* e traz o depoimento sobre a operação do avião em 2010.
**Não citar datas e números de lei por ela sem conferir:** a lei municipal
aparece com dois números (1.278 e 1478), a sanção da lei estadual aparece como
dezembro de 2019 e o assassinato com duas datas. O repositório já tem as fontes
primárias em `docs/legislacao/`.

Dois achados laterais, ambos a localizar:
- Uma **nota técnica do Grupo Territórios do Semiárido (UFRN, 2022)** afirma
  que produção e produtividade no Ceará **aumentaram** nos três anos após a
  lei (p. 178). É o primeiro texto que fala do custo econômico do ban, e é o
  oposto do que os produtores disseram ao STF. ⬜ Obter: é insumo direto do
  desfecho econômico do Ensaio 1 e do Ensaio 2.
- A Del Monte produzia banana em 900 ha no Rio Grande do Norte (nota 73,
  citando Freitas 2010), sem informar município nem método.

### 4.4 Olivete, Thomaz Junior & Barreto (2025) ✅

*Caderno Prudentino de Geografia* 47(1):226–246. Panorama legislativo. O Ceará
é o único estado com proibição total; os demais têm registro e fiscalização
(SP, SE) ou leis municipais (Glória de Dourados/MS, Caxias/MA, cem municípios
do Paraná). **Não menciona o Rio Grande do Norte** nem a Lei 19.135/2024.
Confirma que a fiscalização federal se faz pelo relatório mensal ao MAPA, o
mesmo documento que a LAI do projeto pede.

### 4.5 Parecer do Núcleo Tramas (2016) ✅

Já incorporado ao framework (§5.1): os três municípios e os 1.000 ha.

---

## 5. Onde o projeto se encaixa

Três frases para a introdução, cada uma sustentada por leitura feita:

1. A evidência brasileira sobre agrotóxico e saúde é, na avaliação de
   Paumgartten (2020), ecológica ou transversal, com exposição imprecisa; as
   exceções com identificação (Dias, Rocha & Soares 2023) tratam de glifosato
   em soja, por água.
2. As duas tentativas recentes de medir o efeito em escala nacional com dados
   municipais (Rodrigues 2022; Januzzi 2025) dependem de proxies de uso que não
   enxergam a fruticultura irrigada nem o método de aplicação, e a segunda não
   encontra efeito sobre nascimentos.
3. Nenhuma avalia uma **política**. O banimento cearense oferece o que falta a
   essa literatura: uma mudança datada no método de aplicação, numa região onde
   o dano está descrito há quinze anos (Rigotto et al. 2013; Aguiar 2017), com
   um vizinho na mesma chapada que não foi atingido pela lei.

O que o projeto **não** pode prometer, e a mesma literatura mostra por quê: a
exposição era pequena (cerca de 1.000 ha), o dado é municipal, e Larsen et al.
(2017) só acham efeito na cauda. O Ensaio 1 entrega um intervalo; o que esse
intervalo exclui é o resultado.

---

## 6. Pendências de leitura, por retorno

| # | o quê | por quê |
|---|---|---|
| 1 | Calzada, Gisbert & Moscoso (2023), na íntegra | o efeito de referência do cálculo de poder; resolver 38–89 g × 80–150 g |
| 2 | Nota técnica UFRN (2022), Grupo Territórios do Semiárido | único texto sobre o efeito econômico do ban |
| 3 | Teixeira (2011), em Rigotto (org.), p. 525–546 | fonte primária do volume pulverizado em 2000–2010 |
| 4 | Valadares, Alves & Galiza (2020), Ipea | agrotóxico por agricultura familiar × não familiar no Censo 2017 |
| 5 | Jones (2020), *Land Economics* | único efeito de fungicida sobre nascimento |
| 6 | Rodrigues & Féres (2022), *RESR* | precedente brasileiro de dose-resposta |
| 7 | Nota técnica de Zuza de Oliveira (2016) | fonte primária dos 1.000 ha |
| 8 | Aguiar (2017), p. 81–145, linha a linha | só foi varrida por palavra-chave |
