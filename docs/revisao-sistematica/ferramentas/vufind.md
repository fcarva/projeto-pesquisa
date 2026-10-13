## SQ1 — OASISBR e LA Referencia (emendas v1.1 e v1.2)

*Gerado por `ferramentas/coleta_vufind.py` em 2026-10-13. Consulta = blocos SQ1-AL #1 (exposição, 58 termos) AND #2 (desfecho, 78 termos) da seção "SQ1 — braço América Latina", lidos dos JSON congelados, **sem o #3 (geografia)**, porque as fontes já são brasileira e latino-americana. API VuFind, `type=AllFields`. Teses e dissertações (emenda v1.1) e TCCs de graduação (emenda v1.2) entram.*

| linha | base | contagem | descrição |
|---|---|---:|---|
| OASISBR #1 | OASISBR (API VuFind) | 878 | #1 AND #2, em 192 fatias (soma bruta 2.493; união por `id`). Sem chamada única possível (a API recusa consulta booleana com ~10 termos ou mais (HTTP 403, regra de firewall, não tamanho de URL) e depois bloqueia o IP por um tempo; 5 termos de cada lado passam). Equivalência do fatiamento: as mesmas fatias, rodadas na LA Referencia, dão 544/544 (união das fatias / chamada única). Cobertura dos registros brasileiros (`BR_`) da LA Referencia na união: 289/337; dos faltantes, 40/48 estão indexados no OASISBR, mas o motor dele não os casa com a string (mesmo título e resumo; a LA Referencia casa por outros campos ou radicalização). Eles entram no conjunto da SQ1 pela LA Referencia. Com resumo: 838; com DOI: 78. Formatos: masterThesis 317, article 254, doctoralThesis 153, bachelorThesis 71, ? 52, conferenceObject 17, other 9, book 2, report 1, bookPart 1, dataset 1. |
| LA Referencia #1 | LA Referencia (API VuFind) | 544 | #1 AND #2, em 6 fatias (soma bruta 887; união por `id`). Chamada única: 544, igual à união. Com resumo: 537; com DOI: 89. Formatos: article 251, masterThesis 167, doctoralThesis 125, bookPart 1. |

**String exata** (2026-10-13; a mesma em todas as fontes VuFind):

```text
(agrotóxicos OR agrotóxico OR agrotoxicos OR agrotoxico OR plaguicidas OR pesticidas OR praguicidas OR pesticides OR herbicides OR fungicides OR insecticides OR glyphosate OR glifosato OR agroquímicos OR agroquimicos OR fumigaciones OR "aerial spraying" OR "aerial fumigation" OR "aerial application" OR "crop dusting" OR "pulverização aérea" OR "fumigación aérea" OR "aspersión aérea" OR "aspersiones aéreas" OR "defensivos agrícolas" OR fumigation OR fumigations OR fumigação OR fumigación OR "aerial spray" OR "aerially sprayed" OR agrochemicals OR agrochemical OR "agricultural chemicals" OR agroquímico OR agroquimico OR mancozeb OR chlorpyrifos OR clorpirifós OR organophosphate OR organophosphates OR organofosforados OR paraquat OR atrazine OR procymidone OR procimidona OR chlordecone OR "pesticide drift" OR "spray drift" OR "pulverizações aéreas" OR "aplicação aérea" OR "aviação agrícola" OR DDE OR DDT OR organochlorine OR organochlorines OR organoclorados OR dichlorodiphenyldichloroethylene) AND ("birth weight" OR "low birth weight" OR preterm OR prematurity OR "gestational age" OR "congenital anomalies" OR "congenital malformations" OR "birth defects" OR hypospadias OR cryptorchidism OR stillbirth OR "fetal death" OR miscarriage OR "spontaneous abortion" OR "infant mortality" OR "neonatal mortality" OR "birth outcomes" OR "pregnancy outcomes" OR perinatal OR newborns OR "peso ao nascer" OR "baixo peso" OR prematuridade OR "malformações congênitas" OR "anomalias congênitas" OR "defeitos congênitos" OR "óbito fetal" OR "aborto espontâneo" OR "mortalidade infantil" OR "mortalidade neonatal" OR "recém-nascidos" OR "nascidos vivos" OR "desfechos gestacionais" OR "peso al nacer" OR "bajo peso" OR prematurez OR "malformaciones congénitas" OR "anomalías congénitas" OR "aborto espontáneo" OR "mortalidad infantil" OR "mortalidad neonatal" OR "recién nacidos" OR birthweight OR "infant health" OR "newborn health" OR "neonatal outcomes" OR "fetal growth" OR "gestational length" OR "small for gestational age" OR "saúde infantil" OR "salud infantil" OR "fetal mortality" OR "mortalidade fetal" OR "mortalidad fetal" OR "muerte fetal" OR natimortos OR mortinatos OR "óbitos fetais" OR prematuridad OR "parto prematuro" OR "parto pretérmino" OR "pré-termo" OR "defectos congénitos" OR "neural tube defects" OR "obstetric outcomes" OR "desfechos obstétricos" OR "abortos espontâneos" OR "abortamentos espontâneos" OR "sex ratio at birth" OR "congenital abnormalities" OR "orofacial clefts" OR "cleft lip" OR "cleft palate" OR neonates OR neonate OR "birth length" OR "head circumference" OR "birth size")
```

**Fatias, OASISBR** (192 chamadas; no máximo 5 termos de cada lado, pausa de 3 s; `--plano` reproduz e confere que cobrem exatamente os blocos):

- E1: termos de #1 de `agrotóxicos` a `plaguicidas` (5)
- E2: termos de #1 de `pesticidas` a `fungicides` (5)
- E3: termos de #1 de `insecticides` a `agroquimicos` (5)
- E4: termos de #1 de `fumigaciones` a `"crop dusting"` (5)
- E5: termos de #1 de `"pulverização aérea"` a `"defensivos agrícolas"` (5)
- E6: termos de #1 de `fumigation` a `"aerial spray"` (5)
- E7: termos de #1 de `"aerially sprayed"` a `agroquímico` (5)
- E8: termos de #1 de `agroquimico` a `organophosphate` (5)
- E9: termos de #1 de `organophosphates` a `procymidone` (5)
- E10: termos de #1 de `procimidona` a `"pulverizações aéreas"` (5)
- E11: termos de #1 de `"aplicação aérea"` a `organochlorine` (5)
- E12: termos de #1 de `organochlorines` a `dichlorodiphenyldichloroethylene` (3)
- O1: termos de #2 de `"birth weight"` a `"gestational age"` (5)
- O2: termos de #2 de `"congenital anomalies"` a `cryptorchidism` (5)
- O3: termos de #2 de `stillbirth` a `"infant mortality"` (5)
- O4: termos de #2 de `"neonatal mortality"` a `newborns` (5)
- O5: termos de #2 de `"peso ao nascer"` a `"anomalias congênitas"` (5)
- O6: termos de #2 de `"defeitos congênitos"` a `"mortalidade neonatal"` (5)
- O7: termos de #2 de `"recém-nascidos"` a `"bajo peso"` (5)
- O8: termos de #2 de `prematurez` a `"mortalidad infantil"` (5)
- O9: termos de #2 de `"mortalidad neonatal"` a `"newborn health"` (5)
- O10: termos de #2 de `"neonatal outcomes"` a `"saúde infantil"` (5)
- O11: termos de #2 de `"salud infantil"` a `"muerte fetal"` (5)
- O12: termos de #2 de `natimortos` a `"parto prematuro"` (5)
- O13: termos de #2 de `"parto pretérmino"` a `"obstetric outcomes"` (5)
- O14: termos de #2 de `"desfechos obstétricos"` a `"congenital abnormalities"` (5)
- O15: termos de #2 de `"orofacial clefts"` a `neonate` (5)
- O16: termos de #2 de `"birth length"` a `"birth size"` (3)

**Fatias, LA Referencia** (6 chamadas; URL < 1800 caracteres; `--plano` reproduz e confere que cobrem exatamente os blocos):

- E1: termos de #1 de `agrotóxicos` a `"crop dusting"` (20)
- E2: termos de #1 de `"pulverização aérea"` a `organophosphate` (20)
- E3: termos de #1 de `organophosphates` a `dichlorodiphenyldichloroethylene` (18)
- O1: termos de #2 de `"birth weight"` a `"mortalidad neonatal"` (41)
- O2: termos de #2 de `"recién nacidos"` a `"birth size"` (37)

**Recall dos itens conhecidos** (DOIs da calibração SQ1-AL; conferência por DOI e, na falta, por título normalizado; "BR" = algum autor com afiliação brasileira no OpenAlex):

| DOI | ano | BR | OASISBR | LA Referencia | título |
|---|---|---|---|---|---|
| 10.1590/0103-11042017s206 | 2017 | sim | ✗ indexado, não recuperado | ✗ indexado, não recuperado | Produção de vulnerabilidades em saúde: o trabalho das mulheres em empresas agrícolas da Ch |
| 10.1093/restud/rdad011 | 2023 | sim | fora da fonte | fora da fonte | Down the River: Glyphosate Use in Agriculture and Birth Outcomes of Surrounding Population |
| 10.1086/725349 | 2023 | não | fora da fonte | ✓ titulo | The Hidden Cost of Bananas: The Effects of Pesticides on Newborns’ Health |
| 10.1016/j.jhealeco.2017.04.005 | 2017 | não | fora da fonte | fora da fonte | The health consequences of aerial spraying illicit crops: The case of Colombia |
| 10.1590/s1415-790x2013000300019 | 2013 | sim | ✓ titulo | fora da fonte | Trends of chronic health effects associated to pesticide use in fruit farming regions in t |
| 10.1590/s0124-00642008000100008 | 2008 | não | fora da fonte | ✓ titulo | A Preliminary Statistical Study of Whether Pesticide use Could be Related to birth defects |
| 10.47328/ufvbbt.2025.749 | 2025 | não | ✓ doi | fora da fonte | Impacts of pesticide exposure on birth outcomes and child health in Brazil |
| 10.1590/1413-812320141910.08512014 | 2014 | sim | ✓ titulo | fora da fonte | Malformações congênitas em municípios de grande utilização de agrotóxicos em Mato Grosso,  |
| 10.1590/s0102-311x2012000700005 | 2012 | sim | ✓ doi | ✓ doi | Exposição a agrotóxicos e eventos adversos na gravidez no Sul do Brasil, 1996-2000 |
| 10.1016/j.ijheh.2012.08.006 | 2012 | sim | fora da fonte | fora da fonte | Pesticide exposure and low birth weight prevalence in Brazil |
| 10.1007/s00128-010-0027-8 | 2010 | sim | fora da fonte | fora da fonte | Correlation Between Pesticide Use in Agriculture and Adverse Birth Outcomes in Brazil: An  |
| 10.11606/issn.2176-7262.v50i5p285-296 | 2017 | sim | fora da fonte | fora da fonte | Malformações congênitas em regiões de monocultivo no estado de Minas Gerais, Brasil |
| 10.1590/0103-1104201912108 | 2019 | sim | fora da fonte | fora da fonte | Tendência de malformações congênitas e utilização de agrotóxicos em commodities: um estudo |
| 10.2478/s13382-014-0269-5 | 2014 | sim | fora da fonte | fora da fonte | Pesticide consumption, central nervous system and cardiovascular congenital malformations  |
| 10.1186/s12887-016-0667-x | 2016 | sim | fora da fonte | fora da fonte | Parenteral exposure to pesticides and occurence of congenital malformations: hospital-base |
| 10.1097/ee9.0000000000000290 | 2024 | não | fora da fonte | fora da fonte | Pesticide exposure, birth size, and gestational age in the ISA birth cohort, Costa Rica |
| 10.1016/j.envpol.2026.128090 | 2026 | não | fora da fonte | fora da fonte | Agricultural pesticide exposures in Ecuador and their spatial association with low birth w |
| 10.1007/s11356-021-14574-2 | 2021 | não | fora da fonte | fora da fonte | Residential proximity to pesticide applications in Argentine Patagonia: impact on pregnanc |
| 10.1016/j.socscimed.2025.118285 | 2025 | não | fora da fonte | fora da fonte | Armed conflict and birthweight: The role of organized violence and anti-coca fumigation in |
| 10.5271/sjweh.1790 | 1990 | não | fora da fonte | fora da fonte | Prevalence of adverse reproductive outcomes in a population occupationally exposed to pest |
| 10.3390/healthcare12202052 | 2024 | não | fora da fonte | fora da fonte | Aerial Spraying and Its Impacts on Human Health in Banana-Growing Areas of Ecuador |
| 10.18472/sustdeb.v9n1.2018.29594 | 2018 | sim | ✗ indexado, não recuperado | ✗ indexado, não recuperado | Versão em espanhol do Dossiê ABRASCO sobre o impacto dos agrotóxicos na saúde: |
| 10.1289/ehp.1307679 | 2014 | não | fora da fonte | fora da fonte | Aerial Application of Mancozeb and Urinary Ethylene Thiourea (ETU) Concentrations among Pr |
| 10.1289/jhp1043 | 2024 | sim | fora da fonte | fora da fonte | Pesticide Exposures during Pregnancy and Health Outcomes in Latin America and the Caribbea |
| 10.1289/ehp9934 | 2022 | sim | fora da fonte | fora da fonte | Health Effects of Pesticide Exposure in Latin American and the Caribbean Populations: A Sc |
| 10.1515/reveh.2011.007 | 2011 | não | fora da fonte | fora da fonte | Baseline determination in social, health, and genetic areas in communities affected by gly |
| 10.21680/2447-3359.2021v7n2id24607 | 2021 | sim | fora da fonte | fora da fonte | VALE DO JAGUARIBE: UM OÁSIS EM PERIGO NO SEMIÁRIDO BRASILEIRO – REVISÃO SISTEMÁTICA SOBRE  |
| 10.1007/s11368-016-1597-9 | 2016 | sim | fora da fonte | fora da fonte | Occurrence, distribution, and fate of pesticides in an intensive farming region in the Bra |
| 10.26668/indexlawjournals/2526-0081/2023.v9i2.10012 | 2024 | sim | ✗ indexado, não recuperado | ✗ indexado, não recuperado | MEIO AMBIENTE DO TRABALHO RURAL E PULVERIZAÇÃO AÉREA DE AGROTÓXICOS NA AGRICULTURA: O CASO |
| 10.22533/at.ed.92920110213 | 2020 | não | fora da fonte | fora da fonte | FATORES DE RISCO RELACIONADOS AO CÂNCER INFANTOJUVENIL: COMUNIDADES EXPOSTAS A AGROTÓXICOS |
| 10.54033/cadpedv22n7-345 | 2025 | sim | fora da fonte | fora da fonte | O conflito federativo e a justiça ambiental: a trajetória normativa e judicial sobre a pul |
| 10.18174/442443 | 2018 | não | fora da fonte | fora da fonte | The general ban on aerial spraying of pesticides of the European Union: the policy-making  |
| 10.1289/ehp7295 | 2021 | não | fora da fonte | fora da fonte | Prenatal Exposure to Glyphosate and Its Environmental Degradate, Aminomethylphosphonic Aci |
| 10.1097/scs.0000000000009539 | 2023 | não | fora da fonte | fora da fonte | A Retrospective and Prospective Cohort Study Comparing Pediatric Patients With Cleft Lip a |
| 10.1016/j.chemosphere.2023.138790 | 2023 | não | fora da fonte | fora da fonte | Pesticides exposure in pregnant Argentinian women: Potential relations with the residence  |
| 10.24875/rmn.22000067 | 2023 | não | fora da fonte | fora da fonte | Incidence of congenital malformations of the central nervous system in newborns in Chiapas |
| 10.1097/jom.0000000000002689 | 2022 | sim | fora da fonte | fora da fonte | Environmental Factors at the Periconceptional Period and the Occurrence of Cleft Lip and P |
| 10.1017/s2040174422000277 | 2022 | não | fora da fonte | fora da fonte | Exposure to p,p´-DDE during early pregnancy, anthropometry, and gestational age at birth, |
| 10.35563/rmp.v5i2.63 | 2019 | não | fora da fonte | fora da fonte | Prevalencia y riesgo de malformación congénita en mujeres gestantes expuestas a plaguicida |
| 10.31698/ped.45012018002 | 2018 | não | fora da fonte | fora da fonte | Factores de riesgo prenatales y su asociación a malformaciones congénitas en un Hospital U |
| 10.1016/j.envres.2016.08.008 | 2016 | não | fora da fonte | fora da fonte | Associations of maternal o,p′-DDT and p,p′-DDE levels with birth outcomes in a Bolivian co |
| 10.1289/isee.2015.2015-2920 | 2015 | sim | fora da fonte | fora da fonte | The Impact Of Agricultural Pesticide Use On The Prevalence Of Perinatal Outcomes In Brazil |
| 10.1016/j.scitotenv.2013.01.034 | 2013 | não | fora da fonte | fora da fonte | Association between PON1 genetic polymorphisms and miscarriage in Mexican women exposed to |

- OASISBR: 7/43 itens conhecidos estão na fonte; a string recupera 4/7 deles. Perdidos, mas indexados: `10.1590/0103-11042017s206`; `10.18472/sustdeb.v9n1.2018.29594`; `10.26668/indexlawjournals/2526-0081/2023.v9i2.10012`.

- LA Referencia: 6/43 itens conhecidos estão na fonte; a string recupera 3/6 deles. Perdidos, mas indexados: `10.1590/0103-11042017s206`; `10.18472/sustdeb.v9n1.2018.29594`; `10.26668/indexlawjournals/2526-0081/2023.v9i2.10012`.

O recall que conta é o **sobre os itens indexados**: os itens conhecidos são, na maioria, artigos em periódicos internacionais, que repositórios institucionais não precisam ter. O papel destas fontes é trazer teses, dissertações, TCCs e periódicos brasileiros que as bases indexadas não cobrem. "Fora da fonte" = a busca pelo título (8 primeiras palavras, campo Title) não achou o item; um título traduzido pode dar falso "fora da fonte". Os itens de **contexto** (sem termo de desfecho ao nascer: Rocha 2017, Dossiê ABRASCO, textos jurídicos) não são alvo de #1 AND #2: na calibração, só os braços de contexto os recuperam.
