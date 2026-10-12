# Apêndice A — Estratégias de busca

*Protocolo PRISMA-P, `protocolo.md`. Strings **congeladas** em 2026-10-12, a partir da calibração (`calibracao/<bloco>.json`) e da revisão PRESS 2015 de cada bloco (`calibracao/<bloco>-press.json`). As strings abaixo são as `recommended_final_query` da PRESS, **copiadas por script, sem redigitação**. Contagens são instantâneos da data indicada; o OpenAlex muda com o tempo.*

> ⚠️ **O que não foi feito, e por quê.** A rodada de finalização que mediria o recall num conjunto de validação totalmente novo (V4) falhou nos quatro blocos por limite de gasto da organização (2026-10-12). O recall reportado abaixo mistura itens de ajuste (sementes) e itens que **a PRESS** encontrou depois da calibração. Estes são independentes da string calibrada, mas não da string revisada. Fica como pendência registrada, e não como recall independente.

## Notas de sintaxe (valem para todos os blocos)

- OpenAlex title_and_abstract.search honours uppercase AND, OR and NOT, parentheses and quoted phrases. Set algebra checks out exactly: pesticide = 316,429; "birth weight" = 174,496; AND = 458; OR = 490,467 = A + B - A∧B; A NOT B = 315,971 = A - A∧B. The OQL echo in meta.x_query confirms how each query was parsed.
- Lowercase 'and' is not an operator: it is parsed as a search term and, as a stopword, leaves the count unchanged. Space-separated terms are implicitly ANDed.
- Stemming is always on: 'pesticide' and 'pesticides' give the same count, and quoted phrases are matched as 'stemmed' phrases. A '*' wildcard returns HTTP 400. The title_and_abstract.search.no_stem filter returns HTTP 400 in the current API.
- Multiple filters are ANDed with commas, and negation works on facets (type:!paratext etc.). group_by cannot be combined with select (HTTP 400) but works without it.
- Known-item recall works by prefixing doi:<DOI1>|<DOI2>|... to the search filter. Up to 26 DOIs in one pipe list worked, and URLs of about 4,200 characters were accepted.
- Elsevier records return abstract_inverted_index = null yet are still matched on abstract words by title_and_abstract.search.
- PubMed E-utilities ([tiab], truncation *, [mh], [doi]) is reachable through Parallel web_fetch. Unknown DOIs come back in warninglist.quotedphrasesnotfound, which shows directly which seeds are not indexed.
- Parallel `web_fetch` pode devolver *cache* para URLs longas quase idênticas: toda contagem confere o eco `meta.x_query` (PRESS SQ1).
- GET com string muito longa falha no PubMed (HTTP 414 a ~5.400 caracteres): usar o *history server* do E-utilities (`usehistory=y`) e combinar as linhas `#n`.


---

## SQ1 — revisão sistemática principal, literatura internacional

**Veredito PRESS:** revision required. Mudanças incorporadas na string abaixo.

### Estratégia congelada (OpenAlex e, quando indicado, PubMed/SciELO/LILACS)

```text
((pesticide OR herbicide OR insecticide OR fungicide OR glyphosate OR atrazine OR organophosphate OR agrochemical OR agrichemical OR fumigation OR fumigant OR "aerial spraying" OR "crop dusting" OR chlorpyrifos OR paraquat OR "plant protection products") OR (agrotoxic OR agrotoxics OR plaguicide OR plaguicides OR nematicide OR carbamate OR pyrethroid OR neonicotinoid OR mancozeb OR malathion OR naled OR dibromochloropropane OR "methyl bromide" OR "aerial application" OR "aerial spray" OR "spray drift" OR "pesticide drift" OR "crop spraying" OR Roundup OR "agricultural chemicals") OR ("drinking water contaminant" OR "drinking water contamination" OR "water contaminants") OR (procymidone OR carbaryl OR carbofuran OR fenitrothion OR dithiocarbamate OR dithiocarbamates OR chlordecone OR kepone OR "crop protection")) AND ((("birth weight" OR birthweight OR preterm OR "premature birth" OR "gestational age" OR "gestational length" OR "fetal growth" OR "intrauterine growth" OR stillbirth OR "fetal death" OR "fetal loss" OR miscarriage OR "spontaneous abortion" OR "infant mortality" OR "neonatal mortality" OR "perinatal mortality" OR "infant death" OR "birth defects" OR "congenital anomalies" OR "congenital malformations" OR "neural tube defects" OR hypospadias OR cryptorchidism OR gastroschisis OR "orofacial clefts" OR "birth outcomes" OR "pregnancy outcomes" OR "perinatal health" OR "newborn health" OR "infant health" OR "neonatal health" OR "reproductive outcomes") OR ("pregnancy loss" OR "foetal death" OR "fetal mortality" OR "perinatal outcomes" OR "neonatal outcomes" OR "congenital defects" OR "congenital heart defects" OR "spina bifida" OR anencephaly OR "cleft lip" OR "limb reduction") OR ("child mortality" OR "child health" OR "infant and child" OR "under-five mortality" OR "infant outcomes")) OR ("neonatal death" OR "perinatal death" OR "length of gestation" OR "gestation length" OR "gestational duration" OR "shortened gestation" OR "oral clefts" OR "cleft palate" OR anophthalmia OR microphthalmia OR Apgar OR "head circumference" OR "birth length" OR "congenital cardiac" OR "congenital heart" OR "birth malformations" OR "congenital abnormalities" OR "birth anomalies" OR "fetal malformations" OR "foetal growth" OR "premature delivery" OR "premature infants" OR "abdominal wall defects")) NOT (rats OR rat OR mice OR mouse OR "in vitro" OR zebrafish OR rabbits OR "animal model") NOT ("bed nets" OR bednets OR "bed net" OR "insecticide-treated nets" OR "insecticide-treated bed" OR "treated nets" OR "mosquito nets" OR "insecticidal nets")

[Run as an OpenAlex filter=title_and_abstract.search:<URL-encoded string>, with ,type:!paratext,type:!erratum,type:!book-review,type:!software appended.]

Count: 3385 (2026-10-12, before type exclusions).

Recall: 13/13 tested in-scope items — the 9 seeds, Kadhel 2014, Herve 2016, Rouget 2019, and ISA 2024 (10.1097/ee9.0000000000000290).

Precise variant QR1: the same string AND (agricultural OR agriculture OR farm OR farming OR crop OR crops OR plantation OR orchard OR vineyard OR residential OR residence OR proximity OR near OR living OR ambient OR drift OR aerial OR spraying OR sprayed OR fumigation OR "drinking water" OR "surface water" OR groundwater OR rural OR county OR counties OR municipality OR municipalities OR district OR region OR regions OR geographic OR spatial OR ecological OR community OR communities OR "genetically modified" OR transgenic OR ban OR policy OR banana OR bananas OR "natural experiment" OR "difference-in-differences" OR "instrumental variable" OR "quasi-experimental" OR "regression discontinuity" OR "event study" OR village OR villages OR "zip code" OR "census tract" OR geocoded OR GIS OR buffer OR "land use" OR corn OR maize OR soybean OR cotton OR sugarcane OR "well water" OR "water supply" OR prohibition OR chlordecone). QR1 = 1962 records and misses ISA; use it as screening tier 1.

PubMed companion: the original adapted string plus the MeSH, text-word and bed-net additions listed under subject headings and text words = 717 records, retrieving all 10 PubMed-indexed known items.
```

### Fontes ranqueadas e literatura cinzenta (da calibração)

- **PubMed/medRxiv/arXiv index (firecrawl_research_search_papers, ranked)**: `F1: 'effect of residential or community exposure to agricultural pesticide spraying during pregnancy on birth weight, preterm birth, birth defects and infant mortality' | F2: 'natural experiment difference-in-differences: aerial spraying, glyphosate or pesticide use shocks and newborn health, birth weight, gestational length, infant mortality' | F3: 'agricultural chemicals atrazine herbicides in drinking water or surface water and birth defects, low birth weight and preterm birth' | F4: 'aerial pesticide spraying or aerial fumigation of crops or plantations and pregnancy outcomes, birth weight, congenital anomalies in nearby communities'` — k=100 for F1-F3, k=40 for F4. Ranked results only; this source gives no totals.
- **Wiley Scholar Gateway (full-text passages, ranked)**: `S1: 'Does residential or community exposure to agricultural pesticide applications during pregnancy affect birth weight, preterm birth, birth defects or fetal death?' | S2: 'Are agricultural chemical contaminants such as atrazine and other pesticides in surface water or drinking water associated with birth defects, low birth weight or preterm birth?'` — topN=20 passages per query
- **Grey literature (NBER, IZA, SSRN, RePEc, author pages)**: `site:nber.org pesticide birth outcomes; site:nber.org pesticides infant health; site:nber.org glyphosate birth weight; site:nber.org insecticide infant mortality; site:iza.org pesticides birth weight; site:ssrn.com pesticide exposure birth outcomes; site:ideas.repec.org pesticides infant health; site:ideas.repec.org aerial spraying birth weight; "Cicadian Rhythm" Taylor working paper; Maertens atrazine Renewable Fuel Standard infant mortality; pesticide ban effect infant health natural experiment; neonicotinoid infant health economics working paper` — Web search (Parallel). Plan to export the first 20-30 hits per query.

### Recall de itens conhecidos

- Calibração: OpenAlex, final string: 9/9 indexed DOI seeds (100%). Beyond the seeds, two extra checks: validation set 1 retrieved 15/17, both misses having outcomes outside SQ1 (Lai 2017 JEEM, adult health; Fletcher & Noghanibehambari 2023 JEEM, later-life mortality); validation set 2 retrieved 20/20. That makes 44/46 known items overall and 44/44 of the in-scope ones. PubMed native adapted string: 7/7 of the seeds PubMed indexes. Firecrawl research index (union of 4 framings, top 40-100): 7/9. Scholar Gateway: 3/3 Wiley seeds.
- PRESS (translation of question): Marginal yield of the extra context terms: A AND C AND T3b NOT B2 NOT animal NOT bed-net = 23 records. They included the Calzada replication dataset (10.7910/dvn/z1dgdb), the three chlordecone papers above, and 'Reproductive performance in population exposed to pesticides in cotton fields in India' (1991, 10.1016/s0013-9351(05)80168-9).

A broader T3 that also had state/states/province/regulation added 187 records, with the top 30 by citations dominated by DDE/PCB biomonitoring.

Revised string with the context block (QR1) = 1962; without it (QS') = 3385.

Known-item recall:
- QF3: 0 of the 4 new in-scope items.
- QR1: 3 of 4 (misses ISA).
- QS': 4 of 4. QS' retrieved 13/13 of the 9 seeds pl
- PRESS (boolean/proximity operators): Records removed by the abstract-level animal NOT whose titles contain no animal/toxicology term: 145. They include 'Agricultural Compounds in Water and Birth Defects' (2016, 10.1007/s40572-016-0085-0), a relevant review that QR1 misses.

The title-level NOT variant of the revised string (QR2) = 2159, versus 1962 for QR1. QR2 retrieved 16/16 known items (9 seeds, the 3 chlordecone papers, the Mexico congenital-abnormality review, the Apgar ISEE abstract, the cotton-field study and the 2016 review), verified with Firecrawl at maxAge=0.

PubMed, through the history server: augmented blocks without the bed-net NOT = 901; with the bed-net NOT = 717, so the NOT removes 184 records.
- PRESS (subject headings): PubMed original string = 787. Ten known-item DOIs are all indexed in PubMed: the 7 PubMed seeds plus Kadhel 2014, Herve 2016 and Rouget 2019. The original string retrieves 7/10 and misses the 3 chlordecone papers (PMIDs 24401561, 27560981, 31376129).

The augmented string (MeSH and tiab additions plus the bed-net NOT, run as #1 AND #2 AND #4 NOT (animals[mh] NOT humans[mh]) NOT #3 on the E-utilities history server) = 717 and retrieves 10/10.

A single GET for the full augmented string failed with HTTP 414 at 5,436 characters.
- PRESS (limits and filters): Volume trade-off:
- QF3: 1859.
- QR1 (revised, with the extended context block): 1962.
- QR2 (revised, title-level animal NOT): 2159.
- QS' (revised, no context block): 3385.

Recall on the 13 tested in-scope items (9 seeds + 3 chlordecone + ISA): QF3 9/13, QR1 12/13, QS' 13/13.

The extra RePEc grey item came from web search: UB School of Economics Working Paper 2021/405, the Calzada et al. working-paper version.

### Volume estimado

- Calibração: About 1,850 to 2,100 unique records for title/abstract screening. This is an estimate: no deduplication was run. Basis: OpenAlex final string 1,821 after type exclusions (1,859 before); PubMed adapted string 787, expected to overlap OpenAlex heavily, adding perhaps 50-150 records through MeSH; ranked supplements (top 100 of the PubMed-index framings, Scholar Gateway) mostly duplicates; grey literature about 10-30 items. OpenAlex also holds internal duplicates (preprint plus published versions, Faculty Opinions records, conference abstracts; 115 conference abstracts in the set), so expect some shrinkage. The sensitive variant would raise the OpenAlex input to about 3,230.

### Sugestões da PRESS que não entraram, ou entraram sem teste

- boolean/proximity operators: 1. Apply the animal NOT to titles only. In OpenAlex, add separate negated filters (title.search:!rats, title.search:!mice, and so on) instead of NOT inside title_and_abstract.search; this syntax works.
2. Port the bed-net NOT to PubMed: ("Insecticide-Treated Bednets"[mh] OR "bed net*"[tiab] OR bednet*[tiab] OR "mosquito net*"[tiab] OR "insecticide-treated net*"[tiab] OR "insecticidal net*"[tiab]).
3. In PubMed, consider proximity searching for key pairs, e.g. "pesticide exposure"[tiab:~3] (not tested).
- limits and filters: 1. Use the sensitive revised string (QS') as the primary search and keep the paratext/erratum/book-review/software exclusions.
2. Use the context block only to prioritise screening order.
3. Add OpenAlex forward and backward citation chasing from the seeds and the ISA and chlordecone cohort papers (cites:W... filters; not tested here).
4. Add a site:ideas.repec.org query for "aerial fumigation" to the grey-literature set.

---

## SQ1 — braço América Latina (PT/ES/EN)

**Veredito PRESS:** revision required. Mudanças incorporadas na string abaixo.

### Estratégia congelada (OpenAlex e, quando indicado, PubMed/SciELO/LILACS)

```text
OPENALEX (title_and_abstract.search; one filter per line, comma-separated filters = AND)

#1 E4 = (agrotóxicos OR agrotóxico OR agrotoxicos OR agrotoxico OR plaguicidas OR pesticidas OR praguicidas OR pesticides OR herbicides OR fungicides OR insecticides OR glyphosate OR glifosato OR agroquímicos OR agroquimicos OR fumigaciones OR "aerial spraying" OR "aerial fumigation" OR "aerial application" OR "crop dusting" OR "pulverização aérea" OR "fumigación aérea" OR "aspersión aérea" OR "aspersiones aéreas" OR "defensivos agrícolas" OR fumigation OR fumigations OR fumigação OR fumigación OR "aerial spray" OR "aerially sprayed" OR agrochemicals OR agrochemical OR "agricultural chemicals" OR agroquímico OR agroquimico OR mancozeb OR chlorpyrifos OR clorpirifós OR organophosphate OR organophosphates OR organofosforados OR paraquat OR atrazine OR procymidone OR procimidona OR chlordecone OR "pesticide drift" OR "spray drift" OR "pulverizações aéreas" OR "aplicação aérea" OR "aviação agrícola")

#2 O4 = ("birth weight" OR "low birth weight" OR preterm OR prematurity OR "gestational age" OR "congenital anomalies" OR "congenital malformations" OR "birth defects" OR hypospadias OR cryptorchidism OR stillbirth OR "fetal death" OR miscarriage OR "spontaneous abortion" OR "infant mortality" OR "neonatal mortality" OR "birth outcomes" OR "pregnancy outcomes" OR perinatal OR newborns OR "peso ao nascer" OR "baixo peso" OR prematuridade OR "malformações congênitas" OR "anomalias congênitas" OR "defeitos congênitos" OR "óbito fetal" OR "aborto espontâneo" OR "mortalidade infantil" OR "mortalidade neonatal" OR "recém-nascidos" OR "nascidos vivos" OR "desfechos gestacionais" OR "peso al nacer" OR "bajo peso" OR prematurez OR "malformaciones congénitas" OR "anomalías congénitas" OR "aborto espontáneo" OR "mortalidad infantil" OR "mortalidad neonatal" OR "recién nacidos" OR birthweight OR "infant health" OR "newborn health" OR "neonatal outcomes" OR "fetal growth" OR "gestational length" OR "small for gestational age" OR "saúde infantil" OR "salud infantil" OR "fetal mortality" OR "mortalidade fetal" OR "mortalidad fetal" OR "muerte fetal" OR natimortos OR mortinatos OR "óbitos fetais" OR prematuridad OR "parto prematuro" OR "parto pretérmino" OR "pré-termo" OR "defectos congénitos" OR "neural tube defects" OR "obstetric outcomes" OR "desfechos obstétricos" OR "abortos espontâneos" OR "abortamentos espontâneos" OR "sex ratio at birth")

#3 G4 = (Brazil OR Brasil OR Brazilian OR "Latin America" OR "América Latina" OR Ecuador OR Colombia OR Argentina OR Mexico OR México OR Paraguay OR Peru OR Perú OR Chile OR "Costa Rica" OR Nicaragua OR Guatemala OR Honduras OR Uruguay OR Bolivia OR Venezuela OR Panama OR Panamá OR "El Salvador" OR Cuba OR "Dominican Republic" OR "Latin American" OR "South America" OR "Central America" OR Caribbean OR Caribe OR Guadeloupe OR Martinique OR Antilles OR "French West Indies" OR "Puerto Rico" OR Haiti OR Jamaica OR Guyana OR Suriname OR Belize OR Ecuadorian OR Colombian OR Argentine OR Argentinian OR "Costa Rican" OR Chilean OR Peruvian OR Paraguayan OR Uruguayan OR Bolivian OR Venezuelan OR Nicaraguan OR Guatemalan OR brasileiros OR brasileira OR brasileiro OR brasileiras OR brasileños OR SINASC OR DATASUS OR "Mato Grosso" OR Paraná OR "Rio Grande do Sul" OR Ceará OR "Santa Catarina" OR Goiás OR Bahia OR Pernambuco OR "Minas Gerais" OR "São Paulo" OR Nordeste OR "Northeast Brazil")

#4 = #1 AND #2 AND #3. Tested: 604 hits; 12/12 test DOIs (Dias 2023, Calzada 2023, Camacho & Mejía 2017, Dutra 2019, Uruguay 2024, ISA 2014, Kadhel 2014, Avila-Vazquez 2018, RS 2023, Pernambuco 2023, Mato Grosso 2026, Marialva-PR 2026).

#5 (optional safety net) = #1 AND #2, filter language:pt|es. Not re-counted.

#6 Aerial arm = OA-3 as in the calibration, adding "pulverizações aéreas" OR aeroagrícola OR "aerial spraying ban" to its first block. Not re-counted.

#7 Context arm (flag 'context') = (("Chapada do Apodi" OR "Chapada de Apodi" OR "Limoeiro do Norte" OR "Baixo Jaguaribe" OR Quixeré OR Quixere OR "Zé Maria do Tomé" OR "Ze Maria do Tome" OR "Dossiê ABRASCO" OR "Dossie ABRASCO" OR "Jaguaribe-Apodi" OR "Jaguaribe Apodi" OR Apodi OR "Lower Jaguaribe" OR "Jaguaribe Valley" OR "Vale do Jaguaribe" OR "Tabuleiro de Russas" OR Russas OR Jaguaruana) AND (agrotóxicos OR agrotóxico OR agrotoxicos OR agrotoxico OR pesticides OR pesticidas OR plaguicidas OR agrochemicals OR agribusiness OR agronegócio OR fruticultura OR "fruit farming" OR "fruit growing" OR "pulverização aérea" OR "perímetro irrigado" OR "perímetros irrigados" OR "irrigated perimeter" OR saúde OR health OR mulheres)). The original OA-4 (311) is kept in this arm. The new-term delta, run with a narrower second block, was 88.

#8 Ceará arm (flag 'context') = (Ceará OR Ceara) AND (agrotóxicos OR agrotóxico OR agrotoxicos OR agrotoxico OR pesticides OR plaguicidas OR pesticidas OR "pulverização aérea" OR "aerial spraying" OR agrochemicals OR glyphosate OR glifosato OR fungicides). 218 records not already in the original context arm.

#9 Legal/policy arm (flag 'context / Essay 2') = ("ADI 6137" OR "Zé Maria do Tomé" OR "Ze Maria do Tome" OR "proibição da pulverização aérea" OR "vedação da pulverização aérea" OR "aerial spraying ban" OR "ban on aerial spraying" OR "prohibition of aerial spraying" OR "aerial spraying prohibition" OR "prohibición de la fumigación aérea" OR "prohibición de las fumigaciones aéreas"). The tested version, which also contained "16.820", gave 63; drop "16.820".

Final OpenAlex set = #4 OR #5 OR #6 OR #7 OR #8 OR #9.

SCIELO (search.scielo.org, all indices)
S1' = (agrot* OR pesticid* OR plaguicid* OR praguicid* OR herbicid* OR fungicid* OR inseticid* OR insecticid* OR glifosato OR glyphosate OR agroquimic* OR agrochem* OR fumigacion* OR fumigat* OR "pulverização aérea" OR "aerial spraying") AND (nascer OR nacer OR birth* OR prematur* OR preterm OR pretermin* OR congenit* OR congênit* OR malforma* OR fetal OR fetais OR perinata* OR neonata* OR newborn* OR "recém-nascido*" OR "recién nacido*" OR "mortalidade infantil" OR "mortalidad infantil" OR "infant mortality" OR "mortalidade fetal" OR "mortalidad fetal" OR natimort* OR mortinat* OR obstetric* OR miscarriage* OR "aborto espontâneo" OR "aborto espontáneo" OR "spontaneous abortion"). Do not add pulveriz*: it adds agronomy noise.
S2' = (Apodi* OR Jaguaribe* OR Quixer* OR Russas* OR Jaguaruana*) AND (saúde* OR saude* OR health* OR salud* OR agrot* OR pesticid* OR agroneg* OR agribusiness* OR trabalh* OR fruticultura* OR mulheres*)
S2b = Ceara* AND (agrot* OR pesticid* OR plaguicid* OR "pulverização aérea")
S3 = aerial arm, as in the calibration.

LILACS (BVS portal, filter[db][]=LILACS)
L1' = L1 OR ((mh:"Pesticides" OR mh:"Agrochemicals" OR mh:"Herbicides" OR mh:"Insecticides" OR mh:"Fungicides, Industrial" OR mh:"Agricultural Workers' Diseases") AND (mh:"Pregnancy Outcome" OR mh:"Infant, Low Birth Weight" OR mh:"Premature Birth" OR mh:"Congenital Abnormalities" OR mh:"Fetal Death" OR mh:"Abortion, Spontaneous" OR mh:"Infant Mortality" OR mh:"Stillbirth" OR mh:"Prenatal Exposure Delayed Effects")). DeCS-only = 29; 2 of these are not in L1.
L2' = L2 with Russas* OR Jaguaruana* OR Ceara* added to the place-name block.
```

### Fontes ranqueadas e literatura cinzenta (da calibração)

- **Grey literature (web search; no counts)**: `site:anpec.org.br agrotóxicos ("peso ao nascer" OR "mortalidade infantil" OR "saúde infantil"); site:repositorio.ipea.gov.br agrotóxicos saúde; site:brsa.org.br agrotóxicos; "pesticides" "birth outcomes" Brazil working paper; site:ideas.repec.org pesticides Brazil infant` — Firecrawl web search / Parallel web_search

### Recall de itens conhecidos

- Calibração: OpenAlex: 4/4 seeds and 21/21 indexed known items retrieved by the 4-branch union (OA-1 alone: 18/21). SciELO: 1/1 indexed seed (Rocha 2017), and 5/5 SciELO-indexed effect validation items tested. LILACS: 1/1 seed tested (Rocha 2017, via L2); effect items verified only via a narrowed sub-query because of BVS 502/timeouts. Research index: generic framing 0/4 seeds in top 100 (2 seeds not indexed) and 5/7 V items in top 100.
- PRESS (boolean/proximity operators): T16. 8 new candidate items: 8/8 are indexed in OpenAlex.
T17. Original OA-1 retrieves 1/8 (Avila-Vazquez 2018, 10.4236/jep.2018.93016).
T18. Original OA-2 retrieves 2/8 (Pernambuco 2023, RS 2023). OA-1 ∪ OA-2 = 3/8.
T19. Revised single branch E4 AND O4 AND G4 = 604 hits (original OA-1 = 464; original OA-1 ∪ OA-2 = 625).
T20. The revised branch retrieves 12/12 of the 8 new items plus the 3 effect seeds (Dias 2023, Calzada 2023, Camacho & Mejía 2017) plus Dutra 2019. Caveat: the 8 items were found partly through the delta queries themselves (T2, T4, T10), so 12/12 shows the revisions work. It is not an unbiased recall estimate.
- PRESS (spelling, syntax, line numbers): T11. SciELO doi:"10.1590/1809-4422asoc00761vu27l3oa" = 1 (indexed).
T13. S1 AND that DOI = 1 (retrieved).
T12. SciELO exposure delta = 21, mostly noise.
T9. Legal arm = 63; '16.820' produces unrelated chemistry records.

### Volume estimado

- Calibração: Raw counts: OpenAlex OA-1 ∪ OA-2 = 625 (464 + 266 − 105). OA-3 = 146 and OA-4 = 311, so the OpenAlex upper bound is 1,082 before cross-branch overlap. SciELO: 175 + 135 + 67 = 377 records, including the same article listed in several collections (roughly 1.5–2x duplication in the samples seen). LILACS: 416 + 107 = 523. Raw total about 1,980. SciELO and LILACS records largely duplicate OpenAlex PT/ES records and each other. My estimate is about 1,100–1,400 unique records after deduplication: roughly 750–900 for the effect arms plus 350–450 context records, which should be flagged 'context'. Trade-off: dropping the generic outcome terms 'perinatal', 'newborns' and 'gestational age' and the OA-

### Sugestões da PRESS que não entraram, ou entraram sem teste

- subject headings: L1' = L1 OR (DeCS line above). Optional, untested: SciELO kw: field for author keywords; OpenAlex topics or concepts filter as an extra sensitivity line.

---

## SQ2 — revisão estruturada complementar: método

**Veredito PRESS:** revision required. Mudanças incorporadas na string abaixo.

### Estratégia congelada (OpenAlex e, quando indicado, PubMed/SciELO/LILACS)

```text
OpenAlex, one call, filter=primary_topic.subfield.id:2002|2613|2000|1804,title_and_abstract.search:
(("difference in differences" OR "event study" OR "two-way fixed effects" OR "parallel trends" OR "changes in changes" OR TWFE) AND ("continuous treatment" OR "treatment intensity" OR "intensity of treatment" OR "dose-response" OR dosage OR "multi-valued treatment" OR "multivalued treatment" OR "non-binary treatment" OR "heterogeneous adoption" OR "treatment dose" OR stayers OR fuzzy OR "treatment rate" OR "continuously distributed" OR "exposure intensity" OR "continuous exposure"))
OR ((("difference in differences" OR "parallel trends" OR "event study" OR "treatment effect" OR "treatment effects" OR "causal effect" OR "policy evaluation" OR "program evaluation" OR "binary regressor" OR "treatment status" OR "treatment indicator" OR "program participation") AND (misclassification OR misclassified OR misreporting OR misreported OR "mismeasured treatment" OR "mismeasured binary" OR "measurement error in treatment" OR "treatment measurement error")) OR (("difference in differences" OR "parallel trends" OR "event study" OR "binary regressor" OR "treatment status" OR "treatment indicator") AND ("measurement error" OR "errors in variables" OR mismeasured OR mismeasurement)))
OR ((("few clusters" OR "few treated" OR "few control" OR "few untreated" OR "few groups" OR "small number of clusters" OR "small number of groups" OR "small number of treated" OR "small number of control" OR "small number of policy changes" OR "finite number of clusters" OR "single treated" OR "one treated" OR "unbalanced clusters" OR "clustered errors" OR "cluster bootstrap" OR "wild cluster bootstrap" OR "wild bootstrap" OR "randomization inference" OR "permutation inference" OR "conformal inference" OR "cluster-robust" OR "heterogeneous clusters" OR "randomization tests" OR "clustered standard errors") AND ("difference in differences" OR cluster OR clusters OR clustered OR "policy change" OR "policy changes" OR "few treated" OR "synthetic control")) OR (("number of clusters" OR "number of groups" OR "number of states") AND ("difference in differences" OR "standard errors" OR "t-statistic" OR "cluster-robust")))
OR ((("synthetic control" OR "synthetic controls" OR "synthetic difference in differences" OR "synthetic DiD") AND (inference OR estimator OR estimators OR estimation OR "few treated" OR "single treated" OR "small number" OR permutation OR placebo OR conformal OR "bias correction" OR identification OR "research design")) OR (("panel data approach" OR "panel data method" OR "matrix completion" OR "interactive fixed effects") AND (counterfactual OR counterfactuals OR "program evaluation" OR "policy evaluation" OR "treatment effect" OR "treatment effects" OR "causal effect")))
[Result: 3,840 on 2026-10-12. Validation recall: (a) 5/7, where the 2 misses are binary-TWFE papers that are out of scope by decision; (b) 7/8, where the miss is lost to the subfield filter; (c) 14/15; (d) 8/8.]
Optional broad (c): add "robust standard errors" OR "permutation test" OR "permutation tests" OR "randomization test" to the first (c) arm, and "hypothesis testing" OR "panel data" to the second. The (c) arm then returns 2,400 alone with 15/15.
Plus a second run of the same string with topics.id:T10845 in place of the subfield filter, unioned by ID (not executed; recovers off-subfield methods papers such as Kreider et al. 2012).
Plus the (e) arms unchanged from the calibration: E6 shift-share/formula instruments (topics.id:T10845, 108), the cites: arm on 5 GAEZ anchors with suitability vocabulary (119; add AKM 10.1093/qje/qjz025 as an anchor or known item), and the 29-hit GAEZ keyword arm.
Plus the arXiv research-index, Wiley and NBER/SSRN/RePEc supplements as calibrated.
```

### Fontes ranqueadas e literatura cinzenta (da calibração)

- **arXiv/PubMed research index (firecrawl_research_search_papers)**: `4 natural-language framings: continuous-treatment DiD [econ.EM, k=100]; misclassified treatment in DiD [econ.EM, k=60]; few treated or control clusters inference [k=60]; SC/SDID with few units [econ.EM, k=50]` — categories econ.EM where noted
- **Wiley Scholar Gateway**: `misclassified DiD (topN 15); few-cluster wild bootstrap and RI (topN 10)` — none
- **Web (Parallel search: NBER/SSRN/RePEc/IZA)**: `site:nber.org | site:ideas.repec.org | site:ssrn.com | site:iza.org with continuous-treatment DiD, misclassification DiD, few treated clusters, and GAEZ instrument terms (3 calls, 12 queries)` — none

### Recall de itens conhecidos

- Calibração: 12/13 = 92% (all 13 seeds indexed in OpenAlex). By sub-topic: (a) 3/3; (b) 2/2; (c) 5/5, plus 3/3 extra validation items (MacKinnon-Webb JoE 2020, Rokicki et al. 2018, Hagemann single treated cluster); (d) 1/1; (e) 1/2 seeds (Borusyak-Hull review yes, DRS no). Extra (e) anchors: shift-share methods 4/5 by the E6 string (AKM missed); GAEZ-application anchors 0/5 by GAEZ keywords and 2/5 by a broad unfiltered suitability string (Reynier-Rubin, Nunn-Qian), which is why the citation-chasing arm was adopted.
- PRESS (Translation of the research question): Validation DOIs first checked for indexing (call R1: 14/14 indexed). Note: the DOI I guessed for Mahajan 2006, 10.1111/j.1468-0262.2006.00692.x, resolves to Pesaran 2006. The correct DOI is 10.1111/j.1468-0262.2006.00677.x, found by title search (R3).
- PRESS (Boolean and proximity operators): R7: C_v2 (filtered) plus 7 canonical few-cluster papers not used in tuning (BDM 2004 QJE, Donald-Lang 2007, Ibragimov-Müller 2016, Canay-Romano-Shaikh 2017 Ecta, Pustejovsky-Tipton 2018, Imbens-Kolesár 2016, Cameron-Miller 2015 JHR) returned 1/7, only Cameron-Miller. R11: C_v3-lean returned 1,933 (C_v2: 1,025). R22: C_v3-lean on all 15 (c) items returned 14/15; it missed Imbens-Kolesár, whose abstract has only 'robust standard errors' and 'clusters'. R9/R10: C_v3-broad, which adds "robust standard errors", "permutation test(s)", "randomization test", "hypothesis testing" and "panel data", returned 2,400 with 15/15. R4: B_final (filtered) plus 6 misclassification items returned 1/6, only Lewb
- PRESS (Text word searching (free text)): R12: A1 (filtered) on 7 items returned 4/7. It missed Fuzzy DiD, dCDH AER 2020 and the dCDH survey; it retrieved D'Haultfoeuille-Hoderlein-Sasaki JoE 10.1016/j.jeconom.2022.07.003 on its title. R14: A2 returned 356 (A1: 240). R15: A2 on the same 7 returned 5/7 and now includes Fuzzy DiD. R16: D2 (filtered) on 8 SC/SDID items returned 6/8; it missed Abadie 2021 JEL and Hsiao et al. 2012. R18: D3 returned 1,244 (D2: 934). R19: D3 on the same 8 returned 8/8, adding Abadie 2021, Hsiao et al. 2012, Athey et al. 2021 matrix completion, Xu 2017 GSC, ADH 2010, ASCM, SDID and Chernozhukov-Wüthrich-Zhu.
- PRESS (Spelling, syntax and line numbers): R17: the Abadie 2021 abstract contains 'estimation.' and 'estimates' but D2 did not retrieve it. R13: DHS JoE abstract_inverted_index null. R20: group_by=has_abstract on primary_topic.id:T10845 gave true for all 46,639 records and false for 0. R2: has_abstract:false over the 21 seed and validation DOIs returned 0.

### Volume estimado

- Calibração: By sub-topic in OpenAlex: (a) 240; (b) 323; (c) 1,025; (d) 934; (e) 108 formula/shift-share + 119 citation-chasing + 29 GAEZ keywords = 256. The single-string union for (a)-(d) is 2,416 (sum of parts 2,522, so about 106 overlap), and (a)-(e) together come to about 2,670 gross. The (e) arms overlap little with (a)-(d), so expect about 2,600 OpenAlex records. Preprint/SSRN/NBER/journal duplicates are common: CGS alone has 3 records and MacKinnon-Webb RI has 4, and 627 of the union records are dated 2026. Version deduplication should bring this to roughly 2,100-2,400 unique works for title/abstract screening, plus about 100-200 new items from the arXiv top-k lists and a few dozen grey-literatur

### Sugestões da PRESS que não entraram, ou entraram sem teste

- Translation of the research question: Add independent validation items that were not used for tuning, for every sub-topic. Optionally add an (f) arm for parallel-trends testing, sensitivity and anticipation, for example ("parallel trends" OR "pre-trends" OR "pretrends" OR "pre-trend") AND (test OR testing OR sensitivity OR "no anticipation" OR anticipation). The (f) arm was NOT tested here, so no count is claimed. Alternatively, record a protocol decision that this literature comes in by known-item and citation chasing.
- Subject headings (controlled vocabulary or cl: Run each filtered string a second time with topics.id:T10845 (any of a work's topics) in place of the subfield filter, and union the two runs by OpenAlex ID. One filter value cannot express subfield OR topic. That second run was not executed, so its added volume is unknown. Record in the protocol that health-services and political-methodology venues are covered only through the T10845 run and the arXiv/web supplements.

---

## SQ3 — revisão estruturada complementar: escolha de instrumento

**Veredito PRESS:** revision required. Mudanças incorporadas na string abaixo.

### Estratégia congelada (OpenAlex e, quando indicado, PubMed/SciELO/LILACS)

```text
Run every OpenAlex arm with no date or type limit. Keep S2, S5, S7 and S8 as calibrated. Change S1 and S3, promote S6 to core, and add S4b, S9 and S10.

Definitions:
- P++ = S1's title block as calibrated.
- NEW = "pest control" OR "pest management" OR "plant protection" OR agrichemical OR agrichemicals OR "agri-chemical" OR "agro-chemical" OR biocide OR nematicide OR acaricide OR mancozeb OR procymidone OR chlorothalonil OR carbofuran OR carbaryl OR dicamba OR aldicarb OR chlordecone OR parathion OR lindane OR fipronil OR imidacloprid OR clothianidin OR thiamethoxam OR "chemical input" OR "chemical inputs"
- I = S1's title_and_abstract block as calibrated.
- X = (incentive OR incentives OR "policy options" OR "policy mix") OR ((restrict OR restriction OR restrictions OR "restricted use") AND (tradeoff OR tradeoffs OR "trade-off" OR "social gains" OR "social benefits" OR welfare OR productivity OR profit OR "net returns"))

Arms:

S1' (about 2,292, the sum of disjoint measured parts 1,545 + 194 + 553):
filter=title.search:(P++ OR NEW),title_and_abstract.search:(I OR X)

S2 (689): unchanged. Add fumigant/fumigation/dichloropropene/chloropicrin to the A3b pesticide block (untested).

S3'' (531):
filter=title.search:(nonpoint OR "non-point" OR "diffuse pollution" OR "diffuse source" OR "agricultural pollution" OR "agricultural runoff" OR "agricultural source"),title_and_abstract.search:(instrument OR instruments OR incentive OR incentives OR tax OR taxes OR taxation OR "second-best" OR "least-cost" OR externality OR externalities OR "water quality trading" OR "pollution trading" OR "permit trading" OR "trading ratio" OR "ambient-based" OR "moral hazard" OR "asymmetric information" OR welfare)

S4 (227): unchanged.

S4b (290):
filter=title_and_abstract.search:(("aerial spraying" OR "aerial fumigation" OR "aerial eradication" OR "aerial spray" OR "aerial application" OR "aerial herbicide" OR "aerially sprayed" OR "aerially applied" OR "crop dusting" OR "pulverização aérea" OR "fumigación aérea" OR "aspersión aérea") AND (ban OR banned OR banning OR suspension OR suspended OR prohibition OR prohibited OR "buffer zone" OR "natural experiment" OR "quasi-experiment" OR "quasi-experimental" OR "difference-in-differences" OR "regression discontinuity" OR "exogenous variation" OR welfare OR externality OR externalities OR "cost-benefit"))

S5 (108): unchanged.
filter=cites:W1525260320,title_and_abstract.search:(<agricultural block>)

S6 (core, about 740): change the title block to (P++ OR NEW). Do not cut this arm.

S7 (189): change the first title block to (P++ OR NEW).

S8 (391): unchanged.

S9 (165; about 153 not in S1):
filter=title_and_abstract.search:(("spray drift" OR "pesticide drift" OR "herbicide drift" OR "dicamba drift" OR "drift damage" OR "drift injury" OR "drift complaints") AND (liability OR compensation OR economic OR economics OR welfare OR externality OR externalities OR "cost-benefit" OR lawsuit OR litigation OR "damage claims"))

S10 (about 170 beyond S1, measured with P++ title and bare 'elasticity'):
filter=title.search:(P++ OR NEW),title_and_abstract.search:("price elasticity" OR "demand elasticity" OR "elasticity of demand" OR "own-price" OR elasticities OR "price response" OR "price responsiveness" OR "demand for pesticides" OR "pesticide demand" OR "marginal abatement cost" OR "abatement cost")

Also:
- Hand-add Weitzman 1974 (W1525260320).
- Untested small additions: S1-I += Pigovian OR "tradeable permit" OR fee OR fees OR excise OR "pollution charge" OR redevance; title block += phytosanitaire OR phytosanitaires.
- Estimated volume: about 5,000–5,500 gross before deduplication; add type:!paratext and drop retracted records.
- Validate on a fresh set V4 before freezing, because V3 recall (18/18) is in-sample.
```

### Fontes ranqueadas e literatura cinzenta (da calibração)

- **Firecrawl research index (PubMed/medRxiv/arXiv), supplementary**: `(a) 'effect of national bans or regulations of highly hazardous pesticides such as paraquat on pesticide suicide rates and agricultural output' k=40; (b) 'pesticide tax or levy as an economic instrument to reduce pesticide use and environmental and health risks, ex post evaluation or simulation' k=25` — top-k only
- **Wiley Scholar Gateway, supplementary**: `(a) damage-function specification question; (b) Weitzman prices-vs-quantities for pesticides/nonpoint question (topN=15 each)` — top-15 passages
- **Grey literature / web (Parallel web_search plus agency hand-search)**: `site:ageconsearch.umn.edu, site:ideas.repec.org, site:nber.org on pesticide tax/ban/prices vs quantities; buffer zones/setbacks/schools; aerial spraying ban. Hand-search: CDFA-OPCA publications, CDPR rulemaking (DPR 24-001), EPA BEAD buffer impact analyses (regulations.gov EPA-HQ-OPP-2005-0128), EU SUD evaluation (Ramboll 2021, BiPRO 2004), EPRS 2022` — no counts

### Recall de itens conhecidos

- Calibração: Primary: 9/9 indexed. Final union retrieves 8/9 (88.9%), and 9/9 with the hand-added anchor. S1 alone retrieves 7/9. Supplementary validation set S-1 (10 items found by OpenAlex title lookups during calibration, so NOT independent of the vocabulary): 10/10. It contains Gunnell 2007, the Danish tax ex post 2023, Norway 2020, the buffer-zone CBA 2009, Finger 2017, Böcker & Finger 2016 (x2), Möhring 2020, EST 2000 and the EU aerial ban 2018. Validation set V2 (12 items found outside the OpenAlex strings, via PubMed index, Scholar Gateway and web): 12/12 across the final union; S1 alone gets 7/12, and S2 (A4), S6, S7 and S8 add the other five.
- PRESS (translation of question): Indexing check: doi:<22 candidate DOIs> returned 21. 10.1016/s0308-521x(00)00007-5 is not indexed. 3 DOIs resolved to unrelated works (10.2307/1242024, 10.2307/1243866, 10.1111/1477-9552.12008) and were dropped, leaving V3 = 18. Recall: doi:<V3> AND S1 = 9 (Kudsk & Mathiassen 2020; Lichtenberg-Spear-Zilberman 1993 reentry; Cropper et al. 1992; Jacquet 2011; Pedersen 2020; Travisi 2006; Sunding & Zivin 2000; Zilberman & Millock 1997; Florax 2005). doi:<9 missed> AND S6 = 2 (Kathage 2017; Brookes 2017). doi:<7 still missed> AND S3 = 0, AND S2 = 0, AND S5 = 0.
- PRESS (boolean/proximity operators): title.search:(P++ OR NEW),title_and_abstract.search:(X NOT I_S1) = 553 incremental records. doi:<Antle-Pingali, Lefebvre> on the same filter = 2/2. Top-12 about 7/12 relevant: IPM incentives review; 'High-Resolution Analysis of Pesticide Restrictions Highlights a Need to Balance Trade-offs' 2026; 'Atrazine and Water Quality: An Evaluation of Alternative Policy Options' 1996; 'The Case and Opportunity for Public-Supported Financial Incentives to Implement IPM' 2004. Noise: methyl bromide environmental fate; NAMs safety assessment.
- PRESS (text word searching (free text)): S4b = 290. doi:<Mejía 2015, Camacho & Mejía 2017, EU aerial ban 2018> AND S4b = 2 (Mejía; EU ban). Camacho & Mejía remains covered by S4. Top-10 about 5/10 relevant, including 'A 50 m Buffer Zone to Protect Humans and Ecosystems From Pesticide Aerial Spray Drift: Is It Enough?' (2006) and 'Buffer zone widths for honeybees from ground and aerial spraying' (1990). These are physical drift-distance damage relations, relevant to buffer width. Noise: AgDISP model, a 1939 spray-mixture note. S4b ∩ S4 was not measured.
- PRESS (text word searching (free text)): title.search:P++, ta:((elasticity OR elasticities OR "price response" OR "price responsiveness" OR "demand for pesticides" OR "pesticide demand" OR "marginal abatement cost" OR "abatement cost") NOT I_S1) = 170 incremental. Top-12 8/12 relevant (own-price elasticity meta-analysis and its dataset; 'Disaggregating the Demand for Pesticides' 2015; 'Farm Programs and Pesticide Demand' 1991; 'Estimation of price elasticities for components of fertilizers and pesticides' 2000). Noise: 2 records on the elasticity of apple flesh under methyl bromide. Damage-function arm: title.search:P++, ta:(("damage function(s)" OR "dose-response" OR "dose response" OR "marginal damage(s)" OR "exposure-response" O
- PRESS (text word searching (free text)): BUF variant: title.search:(P++ OR drift), ta:(("buffer strip(s)" OR setback(s) OR "buffer distance" OR "buffer width" OR "buffer zone" OR "no-spray" OR "spray-free" OR "pesticide-free zone") AND (cost-benefit/economic impact/compensation/welfare/WTP/net returns/profit...)) = 887. Top-12 about 4/12 relevant; noise is fungicide-profitability and drone-spraying papers. Rejected; keep S2's phrase-limited terms. The fumigant and spelling additions were not run.

### Volume estimado

- Calibração: OpenAlex counts as of 2026-10-11/12. Core set (S1 1,545 + S2 689 + S3 174 + S4 227 + S5 108 = 2,743 gross; S1∩S2 measured at 30; the other overlaps, among S3/S2-A8b/S5 and S4/S1, were not measured and should be small): about 2,600–2,700 unique. Extended arms add, after measured overlaps with S1: S6 about +570, S7 about +143, S8 +391 at most (overlap with S1 not measured). Total about 3,600–3,800 OpenAlex records. Removing duplicate versions (AgEcon conference vs journal, SSRN vs journal, duplicate DOIs such as Soares & Porto, two records each for 'Spatial heterogeneity and the choice of instruments' 1996/2001 and 'Regulation of nitrogen pollution: taxes versus quotas' 1995) should bring this

### Sugestões da PRESS que não entraram, ou entraram sem teste

- subject headings: If EconLit, CAB Abstracts or AgEcon full search becomes available, run the pesticide concept (P++ plus NEW) AND (JEL Q5* OR H23 OR K32). In PubMed: ("Pesticides"[Mesh] OR "Herbicides"[Mesh] OR "Insecticides"[Mesh]) AND ("Government Regulation"[Mesh] OR "Legislation as Topic"[Mesh] OR "Taxes"[Mesh]). Document that OpenAlex topic or keyword filters were not tested.
- text word searching (free text): Keep S4 and add S4b = title_and_abstract.search:(("aerial spraying" OR "aerial fumigation" OR "aerial eradication" OR "aerial spray" OR "aerial application" OR "aerial herbicide" OR "aerially sprayed" OR "aerially applied" OR "crop dusting" OR "pulverização aérea" OR "fumigación aérea" OR "aspersión aérea") AND (ban OR banned OR banning OR suspension OR suspended OR prohibition OR prohibited OR "buffer zone" OR "natural experiment" OR "quasi-experiment" OR "quasi-experimental" OR "difference-in-differences" OR "regression discontinuity" OR "exogenous variation" OR welfare OR externality OR ext
- text word searching (free text): S10 = title.search:(P++ OR NEW),title_and_abstract.search:("price elasticity" OR "demand elasticity" OR "elasticity of demand" OR "own-price" OR elasticities OR "price response" OR "price responsiveness" OR "demand for pesticides" OR "pesticide demand" OR "marginal abatement cost" OR "abatement cost"). Narrowing bare 'elasticity' to these phrases is untested. Do not add a standalone damage-function arm. Instead, tell screeners about the damage-control versus external-damage ambiguity.
- text word searching (free text): In S2-A3b's pesticide block add fumigant OR fumigants OR fumigation OR "methyl bromide" OR dichloropropene OR chloropicrin. In S1-I add Pigovian OR "tradeable permit" OR fee OR fees OR excise OR "pollution charge" OR redevance. In the title block add phytosanitaire OR phytosanitaires. All of these are untested and should be measured before adoption.
- limits and filters: Add type:!paratext and drop is_retracted:true records at deduplication (counts untested). Screen in this order: S1 core, S2, S3'', S6, S9, S4/S4b, S5, S7, S10, S8, then the S1 X-block increment, which is the costliest, about 1/3 noise in its top-12, and suits AI-prioritized screening. Validate on a fresh V4 set before freezing the protocol.

---

## Traduções para Scopus e Web of Science (SQ1; o pesquisador roda pelo Portal CAPES)

Tradução da string congelada da SQ1 (versão sensível, sem bloco de contexto).
Scopus e WoS aceitam truncamento (`*`), então as flexões viram um radical.
**Exportar todos os registros em RIS ou CSV com resumo** para
`registros/importados/`, com nome `scopus-sq1-AAAA-MM-DD.ris` /
`wos-sq1-AAAA-MM-DD.txt`. **Anotar a contagem e a data da busca.**

### Scopus (busca avançada)
```text
TITLE-ABS-KEY ( pesticid* OR herbicid* OR insecticid* OR fungicid* OR glyphosate OR atrazine OR organophosphat* OR agrochemical* OR agrichemical* OR fumigat* OR "aerial spray*" OR "aerial application" OR "crop dusting" OR "crop spraying" OR chlorpyrifos OR paraquat OR malathion OR naled OR mancozeb OR chlordecone OR kepone OR procymidone OR carbaryl OR carbofuran OR fenitrothion OR dithiocarbamate* OR "spray drift" OR "pesticide drift" OR "crop protection" OR "plant protection product*" OR "agricultural chemical*" OR plaguicid* OR agrotox* OR pyrethroid* OR neonicotinoid* OR carbamate* OR nematicid* OR "methyl bromide" OR dibromochloropropane OR roundup OR "drinking water contamina*" OR "water contaminant*" )
AND TITLE-ABS-KEY ( "birth weight" OR birthweight OR preterm OR "premature birth" OR "premature deliver*" OR "premature infant*" OR "gestational age" OR "gestational length" OR "length of gestation" OR "gestation length" OR "gestational duration" OR "fetal growth" OR "foetal growth" OR "intrauterine growth" OR stillbirth* OR "fetal death*" OR "foetal death*" OR "fetal loss" OR "fetal mortality" OR "pregnancy loss" OR miscarriage* OR "spontaneous abortion*" OR "infant mortality" OR "neonatal mortality" OR "perinatal mortality" OR "infant death*" OR "neonatal death*" OR "perinatal death*" OR "birth defect*" OR "congenital anomal*" OR "congenital malformation*" OR "congenital defect*" OR "congenital abnormalit*" OR "congenital heart" OR "congenital cardiac" OR "neural tube defect*" OR hypospadias OR cryptorchidism OR gastroschisis OR "abdominal wall defect*" OR "oral cleft*" OR "orofacial cleft*" OR "cleft lip" OR "cleft palate" OR "spina bifida" OR anencephaly OR "limb reduction" OR anophthalmia OR microphthalmia OR "birth outcome*" OR "pregnancy outcome*" OR "perinatal outcome*" OR "neonatal outcome*" OR "perinatal health" OR "newborn health" OR "infant health" OR "neonatal health" OR "child health" OR "child mortality" OR "under-five mortality" OR "infant outcome*" OR "infant and child" OR "reproductive outcome*" OR "head circumference" OR "birth length" OR apgar OR "birth malformation*" OR "birth anomal*" OR "fetal malformation*" )
AND NOT TITLE ( rat OR rats OR mice OR mouse OR zebrafish OR rabbit* OR "in vitro" OR "animal model" )
AND NOT TITLE-ABS-KEY ( "bed net*" OR bednet* OR "insecticide-treated net*" OR "treated net*" OR "mosquito net*" OR "insecticidal net*" )
```

### Web of Science Core Collection (busca avançada)
```text
TS=(pesticid* OR herbicid* OR insecticid* OR fungicid* OR glyphosate OR atrazine OR organophosphat* OR agrochemical* OR agrichemical* OR fumigat* OR "aerial spray*" OR "aerial application" OR "crop dusting" OR "crop spraying" OR chlorpyrifos OR paraquat OR malathion OR naled OR mancozeb OR chlordecone OR kepone OR procymidone OR carbaryl OR carbofuran OR fenitrothion OR dithiocarbamate* OR "spray drift" OR "pesticide drift" OR "crop protection" OR "plant protection product*" OR "agricultural chemical*" OR plaguicid* OR agrotox* OR pyrethroid* OR neonicotinoid* OR carbamate* OR nematicid* OR "methyl bromide" OR dibromochloropropane OR roundup OR "drinking water contamina*" OR "water contaminant*")
AND TS=("birth weight" OR birthweight OR preterm OR "premature birth" OR "premature deliver*" OR "premature infant*" OR "gestational age" OR "gestational length" OR "length of gestation" OR "gestation length" OR "gestational duration" OR "fetal growth" OR "foetal growth" OR "intrauterine growth" OR stillbirth* OR "fetal death*" OR "foetal death*" OR "fetal loss" OR "fetal mortality" OR "pregnancy loss" OR miscarriage* OR "spontaneous abortion*" OR "infant mortality" OR "neonatal mortality" OR "perinatal mortality" OR "infant death*" OR "neonatal death*" OR "perinatal death*" OR "birth defect*" OR "congenital anomal*" OR "congenital malformation*" OR "congenital defect*" OR "congenital abnormalit*" OR "congenital heart" OR "congenital cardiac" OR "neural tube defect*" OR hypospadias OR cryptorchidism OR gastroschisis OR "abdominal wall defect*" OR "oral cleft*" OR "orofacial cleft*" OR "cleft lip" OR "cleft palate" OR "spina bifida" OR anencephaly OR "limb reduction" OR anophthalmia OR microphthalmia OR "birth outcome*" OR "pregnancy outcome*" OR "perinatal outcome*" OR "neonatal outcome*" OR "perinatal health" OR "newborn health" OR "infant health" OR "neonatal health" OR "child health" OR "child mortality" OR "under-five mortality" OR "infant outcome*" OR "infant and child" OR "reproductive outcome*" OR "head circumference" OR "birth length" OR apgar OR "birth malformation*" OR "birth anomal*" OR "fetal malformation*")
NOT TI=(rat OR rats OR mice OR mouse OR zebrafish OR rabbit* OR "in vitro" OR "animal model")
NOT TS=("bed net*" OR bednet* OR "insecticide-treated net*" OR "treated net*" OR "mosquito net*" OR "insecticidal net*")
```
⚠️ Estas traduções **não foram testadas** (sem acesso a Scopus/WoS nesta
sessão). Antes de exportar, teste se os DOIs das sementes aparecem: no Scopus,
acrescente `AND DOI(10.1086/725349)` e confira se retorna 1; repita com
`10.1093/restud/rdad011` e `10.1038/s41467-017-00349-2`.

---

## Volume esperado para triagem (bruto, antes da deduplicação)

| bloco | linhas | registros brutos (aprox.) | fonte da contagem |
|---|---|---|---|
| SQ1 internacional | OpenAlex QS′ | 3.385 | PRESS, 2026-10-12 |
| SQ1 internacional | PubMed aumentado | 717 | PRESS, 2026-10-12 (grande sobreposição com o OpenAlex) |
| SQ1 América Latina | OpenAlex #4–#9 | ~1.400 | soma das partes medidas; união não recontada |
| SQ1 América Latina | SciELO S1′–S3, LILACS L1′–L2′ | ~900 | calibração + PRESS; duplicação entre coleções de 1,5 a 2× |
| SQ1 Scopus/WoS | — | ⬜ | exportação do pesquisador |
| **SQ1, únicos estimados** | | **~4.000–4.500** | estimativa |
| SQ2 método | OpenAlex união (a)–(d) + (e) | ~4.100 | PRESS (3.840) + braços (e) (~256) |
| SQ3 instrumento | OpenAlex S1′–S10 | ~5.000–5.500 | PRESS (soma de partes) |
| **Total bruto** | | **~15.000** | |
