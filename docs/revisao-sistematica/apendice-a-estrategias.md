# Apêndice A — Estratégias de busca

*Protocolo PRISMA-P, `protocolo.md`. Gerado por `ferramentas/gera_apendice_a.py` a partir de `calibracao/`; as strings são copiadas dos JSON, sem redigitação. Contagens são instantâneos da data indicada em cada linha; o OpenAlex muda com o tempo.*

Cadeia de cada bloco: calibração (`<bloco>.json`) → revisão PRESS 2015 independente (`<bloco>-press.json`, as quatro pediram revisão obrigatória) → finalização, que aplica a PRESS, congela as linhas e mede recall em validação independente (`<bloco>-final.json`).

## Notas de sintaxe (valem para todos os blocos)

- OpenAlex title_and_abstract.search honours uppercase AND, OR and NOT, parentheses and quoted phrases. Set algebra checks out exactly: pesticide = 316,429; "birth weight" = 174,496; AND = 458; OR = 490,467 = A + B - A∧B; A NOT B = 315,971 = A - A∧B. The OQL echo in meta.x_query confirms how each query was parsed.
- Lowercase 'and' is not an operator: it is parsed as a search term and, as a stopword, leaves the count unchanged. Space-separated terms are implicitly ANDed.
- Stemming is always on: 'pesticide' and 'pesticides' give the same count, and quoted phrases are matched as 'stemmed' phrases. A '*' wildcard returns HTTP 400. The title_and_abstract.search.no_stem filter returns HTTP 400 in the current API.
- Multiple filters are ANDed with commas, and negation works on facets (type:!paratext etc.). group_by cannot be combined with select (HTTP 400) but works without it.
- Known-item recall works by prefixing doi:<DOI1>|<DOI2>|... to the search filter. Up to 26 DOIs in one pipe list worked, and URLs of about 4,200 characters were accepted.
- Elsevier records return abstract_inverted_index = null yet are still matched on abstract words by title_and_abstract.search.
- PubMed E-utilities ([tiab], truncation *, [mh], [doi]) is reachable through Parallel web_fetch. Unknown DOIs come back in warninglist.quotedphrasesnotfound, which shows directly which seeds are not indexed.
- Parallel `web_fetch` pode devolver *cache* para URLs longas quase idênticas: toda contagem confere o eco `meta.x_query`.
- GET longo falha no PubMed (HTTP 414 a ~5.400 caracteres): usar o *history server* do E-utilities (`usehistory=y`).


---

## SQ1 — revisão sistemática principal, literatura internacional

**Fonte:** rodada de finalização (`-final.json`), que aplica a PRESS e congela as linhas.

| linha | base | contagem | descrição |
|---|---|---:|---|
| #1 | OpenAlex | 892.695 | Exposure block (agent). PRESS additions included: chlordecone, kepone, Ceará actives (procymidone, carbaryl, carbofuran, fenitrothion, dithiocarbamate/dithiocarbamates) and "crop protection". OpenAlex has no wildcards; it stems inflections only. |
| #2 | OpenAlex | 1.278.696 | Outcome block. The 4th group of specific phrases from PRESS is included. Deliberately absent: prematurity, bare congenital/malformation (PRESS showed these add noise). |
| #3 | OpenAlex | 12.641 | Bed-net NOT block (malaria-in-pregnancy noise). Kept as PRESS recommended. Applied as NOT inside title_and_abstract.search. |
| #4 | OpenAlex | — | Animal/in-vitro NOT at TITLE level only, written as 8 separate negated title filters. These are appended to the filter of #5 and are not a standalone search, so no standalone count was run. The OQL echo of #5 shows 'title has (NOT ... AND NOT ...)'. |
| #5 | OpenAlex | 3.774 | QS-prime = #1 AND #2 NOT #3 NOT #4, before type exclusions. Run with group_by=type on 2026-10-12: total 3,774 = article 2,805, book-chapter 200, conference-abstract 198, dissertation 123, other 88, preprint 76, review 76, conference-paper 41, editorial 36, paratext 22, reference-entry 20, dataset 19, book 18, book-review 13, letter 12, report 12, erratum 8, peer-review 4, data-paper 1, retraction 1, software 1. With the abstract-level animal NOT, PRESS QS' gave 3,385, so the title-level NOT keeps 389 more records. |
| #6 | OpenAlex | 3.730 | SCREENING SET = #5 with ,type:!paratext,type:!erratum,type:!book-review,type:!software appended. type:!dataset is deliberately not used (PRESS: it drops the Calzada replication dataset). The count is #5 minus the 44 records of the 4 excluded types (22+8+13+1) from the exact group_by partition of #5. The same filter, ANDed with the development DOI list, ran with a matching OQL echo ('type is not ...'). |
| #7 | OpenAlex | — | Context block = SCREENING-PRIORITY FLAG ONLY, never a filter. It is the PRESS-extended version: setting, crops incl. banana, design, spatial-unit and policy terms. It is used only to split #6 into tiers #8 and #9, so no standalone count was run. |
| #8 | OpenAlex | 2.128 | TIER 1 (screen first) = #6 AND #7. |
| #9 | OpenAlex | 1.602 | TIER 2 (screen after tier 1, never dropped) = #6 NOT #7. The count is derived as #6 minus #8 (3,730 − 2,128). The query was not run separately, but OpenAlex set algebra is exact (calibration syntax findings). |
| #1 | PubMed (E-utilities esearch, db=pubmed) | 272.526 | Exposure. The original adaptation plus PRESS additions: Agrochemicals[mh], "Pesticide Residues"[mh], chlordecone, kepone, Ceará actives, "crop protection", plus OpenAlex terms not ported before (naled, Roundup, agrotoxic*, plaguicide*, nematicide*, carbamate*, dibromochloropropane, "aerial spray*", "pesticide drift", "crop spraying", "plant protection product*", water-contaminant phrases). Querytranslation checked. |
| #2 | PubMed (E-utilities esearch, db=pubmed) | 1.317.186 | Outcome. The original adaptation plus PRESS MeSH (Birth Weight, Gestational Age, Fetal Growth Retardation, Infant Small for Gestational Age, Fetal Death, Abortion Spontaneous, Perinatal Death, Infant Mortality) and the tiab phrases of the OpenAlex outcome groups. In the as-run sequence this was query_key=1 (WebEnv MCID_6acc31ff316c767392068878). Querytranslation checked. |
| #3 | PubMed (E-utilities esearch, db=pubmed) | — | Bed-net NOT block, ported from OpenAlex as PRESS recommended. Not counted standalone; it appears verbatim in the querytranslation of #5. |
| #4 | PubMed (E-utilities esearch, db=pubmed) | — | Animal-only NOT block (keeps records indexed for both animals and humans). Not counted standalone; checked in the querytranslation of #5. |
| #5 | PubMed (E-utilities esearch, db=pubmed) | 2.054 | PUBMED SCREENING SET = #1 AND #2 NOT #4 NOT #3. The expanded string below can be pasted into PubMed Advanced Search. Over E-utilities a single GET returns HTTP 414 (failed at 4,636 characters), so the as-run sequence used the history server. Step A: esearch usehistory=y term=<#2> gives WebEnv and query_key 1. Step B: same WebEnv, usehistory=y, term=<#1> AND #1 NOT (animals[mh] NOT humans[mh]) NOT <#3>, giving query_key 2 with count 2,054. Querytranslation checked. |
| #6 | PubMed (E-utilities esearch, db=pubmed) | — | Context block = SCREENING-PRIORITY FLAG ONLY, never a filter. It mirrors OpenAlex #7 plus the PRESS setting MeSH: Agriculture, Rural Population, Drinking Water, Water Pollutants Chemical. Not counted standalone. |
| #7 | PubMed (E-utilities esearch, db=pubmed) | 892 | TIER 1 (screen first) = #5 AND #6. As run: term=#2 AND <#6 string> with the same WebEnv and usehistory=y, giving query_key 3. Querytranslation checked. |
| #8 | PubMed (E-utilities esearch, db=pubmed) | 1.162 | TIER 2 (screen after tier 1, never dropped) = #5 NOT #6. The count is derived as 2,054 − 892; this line was not run separately. |

**Strings exatas, prontas para rodar:**

`#1` (OpenAlex, 2026-10-12):
```text
https://api.openalex.org/works?mailto=revisao.sistematica.ufes@example.org&filter=title_and_abstract.search:((pesticide OR herbicide OR insecticide OR fungicide OR glyphosate OR atrazine OR organophosphate OR agrochemical OR agrichemical OR fumigation OR fumigant OR "aerial spraying" OR "crop dusting" OR chlorpyrifos OR paraquat OR "plant protection products") OR (agrotoxic OR agrotoxics OR plaguicide OR plaguicides OR nematicide OR carbamate OR pyrethroid OR neonicotinoid OR mancozeb OR malathion OR naled OR dibromochloropropane OR "methyl bromide" OR "aerial application" OR "aerial spray" OR "spray drift" OR "pesticide drift" OR "crop spraying" OR Roundup OR "agricultural chemicals") OR ("drinking water contaminant" OR "drinking water contamination" OR "water contaminants") OR (procymidone OR carbaryl OR carbofuran OR fenitrothion OR dithiocarbamate OR dithiocarbamates OR chlordecone OR kepone OR "crop protection"))
```
`#2` (OpenAlex, 2026-10-12):
```text
https://api.openalex.org/works?mailto=revisao.sistematica.ufes@example.org&filter=title_and_abstract.search:((("birth weight" OR birthweight OR preterm OR "premature birth" OR "gestational age" OR "gestational length" OR "fetal growth" OR "intrauterine growth" OR stillbirth OR "fetal death" OR "fetal loss" OR miscarriage OR "spontaneous abortion" OR "infant mortality" OR "neonatal mortality" OR "perinatal mortality" OR "infant death" OR "birth defects" OR "congenital anomalies" OR "congenital malformations" OR "neural tube defects" OR hypospadias OR cryptorchidism OR gastroschisis OR "orofacial clefts" OR "birth outcomes" OR "pregnancy outcomes" OR "perinatal health" OR "newborn health" OR "infant health" OR "neonatal health" OR "reproductive outcomes") OR ("pregnancy loss" OR "foetal death" OR "fetal mortality" OR "perinatal outcomes" OR "neonatal outcomes" OR "congenital defects" OR "congenital heart defects" OR "spina bifida" OR anencephaly OR "cleft lip" OR "limb reduction") OR ("child mortality" OR "child health" OR "infant and child" OR "under-five mortality" OR "infant outcomes")) OR ("neonatal death" OR "perinatal death" OR "length of gestation" OR "gestation length" OR "gestational duration" OR "shortened gestation" OR "oral clefts" OR "cleft palate" OR anophthalmia OR microphthalmia OR Apgar OR "head circumference" OR "birth length" OR "congenital cardiac" OR "congenital heart" OR "birth malformations" OR "congenital abnormalities" OR "birth anomalies" OR "fetal malformations" OR "foetal growth" OR "premature delivery" OR "premature infants" OR "abdominal wall defects"))
```
`#3` (OpenAlex, 2026-10-12):
```text
https://api.openalex.org/works?mailto=revisao.sistematica.ufes@example.org&filter=title_and_abstract.search:("bed nets" OR bednets OR "bed net" OR "insecticide-treated nets" OR "insecticide-treated bed" OR "treated nets" OR "mosquito nets" OR "insecticidal nets")
```
`#4` (OpenAlex, 2026-10-12):
```text
title.search:!rats,title.search:!rat,title.search:!mice,title.search:!mouse,title.search:!"in vitro",title.search:!zebrafish,title.search:!rabbits,title.search:!"animal model"
```
`#5` (OpenAlex, 2026-10-12):
```text
https://api.openalex.org/works?mailto=revisao.sistematica.ufes@example.org&filter=title_and_abstract.search:((pesticide OR herbicide OR insecticide OR fungicide OR glyphosate OR atrazine OR organophosphate OR agrochemical OR agrichemical OR fumigation OR fumigant OR "aerial spraying" OR "crop dusting" OR chlorpyrifos OR paraquat OR "plant protection products") OR (agrotoxic OR agrotoxics OR plaguicide OR plaguicides OR nematicide OR carbamate OR pyrethroid OR neonicotinoid OR mancozeb OR malathion OR naled OR dibromochloropropane OR "methyl bromide" OR "aerial application" OR "aerial spray" OR "spray drift" OR "pesticide drift" OR "crop spraying" OR Roundup OR "agricultural chemicals") OR ("drinking water contaminant" OR "drinking water contamination" OR "water contaminants") OR (procymidone OR carbaryl OR carbofuran OR fenitrothion OR dithiocarbamate OR dithiocarbamates OR chlordecone OR kepone OR "crop protection")) AND ((("birth weight" OR birthweight OR preterm OR "premature birth" OR "gestational age" OR "gestational length" OR "fetal growth" OR "intrauterine growth" OR stillbirth OR "fetal death" OR "fetal loss" OR miscarriage OR "spontaneous abortion" OR "infant mortality" OR "neonatal mortality" OR "perinatal mortality" OR "infant death" OR "birth defects" OR "congenital anomalies" OR "congenital malformations" OR "neural tube defects" OR hypospadias OR cryptorchidism OR gastroschisis OR "orofacial clefts" OR "birth outcomes" OR "pregnancy outcomes" OR "perinatal health" OR "newborn health" OR "infant health" OR "neonatal health" OR "reproductive outcomes") OR ("pregnancy loss" OR "foetal death" OR "fetal mortality" OR "perinatal outcomes" OR "neonatal outcomes" OR "congenital defects" OR "congenital heart defects" OR "spina bifida" OR anencephaly OR "cleft lip" OR "limb reduction") OR ("child mortality" OR "child health" OR "infant and child" OR "under-five mortality" OR "infant outcomes")) OR ("neonatal death" OR "perinatal death" OR "length of gestation" OR "gestation length" OR "gestational duration" OR "shortened gestation" OR "oral clefts" OR "cleft palate" OR anophthalmia OR microphthalmia OR Apgar OR "head circumference" OR "birth length" OR "congenital cardiac" OR "congenital heart" OR "birth malformations" OR "congenital abnormalities" OR "birth anomalies" OR "fetal malformations" OR "foetal growth" OR "premature delivery" OR "premature infants" OR "abdominal wall defects")) NOT ("bed nets" OR bednets OR "bed net" OR "insecticide-treated nets" OR "insecticide-treated bed" OR "treated nets" OR "mosquito nets" OR "insecticidal nets"),title.search:!rats,title.search:!rat,title.search:!mice,title.search:!mouse,title.search:!"in vitro",title.search:!zebrafish,title.search:!rabbits,title.search:!"animal model"
```
`#6` (OpenAlex, 2026-10-12):
```text
https://api.openalex.org/works?mailto=revisao.sistematica.ufes@example.org&filter=title_and_abstract.search:((pesticide OR herbicide OR insecticide OR fungicide OR glyphosate OR atrazine OR organophosphate OR agrochemical OR agrichemical OR fumigation OR fumigant OR "aerial spraying" OR "crop dusting" OR chlorpyrifos OR paraquat OR "plant protection products") OR (agrotoxic OR agrotoxics OR plaguicide OR plaguicides OR nematicide OR carbamate OR pyrethroid OR neonicotinoid OR mancozeb OR malathion OR naled OR dibromochloropropane OR "methyl bromide" OR "aerial application" OR "aerial spray" OR "spray drift" OR "pesticide drift" OR "crop spraying" OR Roundup OR "agricultural chemicals") OR ("drinking water contaminant" OR "drinking water contamination" OR "water contaminants") OR (procymidone OR carbaryl OR carbofuran OR fenitrothion OR dithiocarbamate OR dithiocarbamates OR chlordecone OR kepone OR "crop protection")) AND ((("birth weight" OR birthweight OR preterm OR "premature birth" OR "gestational age" OR "gestational length" OR "fetal growth" OR "intrauterine growth" OR stillbirth OR "fetal death" OR "fetal loss" OR miscarriage OR "spontaneous abortion" OR "infant mortality" OR "neonatal mortality" OR "perinatal mortality" OR "infant death" OR "birth defects" OR "congenital anomalies" OR "congenital malformations" OR "neural tube defects" OR hypospadias OR cryptorchidism OR gastroschisis OR "orofacial clefts" OR "birth outcomes" OR "pregnancy outcomes" OR "perinatal health" OR "newborn health" OR "infant health" OR "neonatal health" OR "reproductive outcomes") OR ("pregnancy loss" OR "foetal death" OR "fetal mortality" OR "perinatal outcomes" OR "neonatal outcomes" OR "congenital defects" OR "congenital heart defects" OR "spina bifida" OR anencephaly OR "cleft lip" OR "limb reduction") OR ("child mortality" OR "child health" OR "infant and child" OR "under-five mortality" OR "infant outcomes")) OR ("neonatal death" OR "perinatal death" OR "length of gestation" OR "gestation length" OR "gestational duration" OR "shortened gestation" OR "oral clefts" OR "cleft palate" OR anophthalmia OR microphthalmia OR Apgar OR "head circumference" OR "birth length" OR "congenital cardiac" OR "congenital heart" OR "birth malformations" OR "congenital abnormalities" OR "birth anomalies" OR "fetal malformations" OR "foetal growth" OR "premature delivery" OR "premature infants" OR "abdominal wall defects")) NOT ("bed nets" OR bednets OR "bed net" OR "insecticide-treated nets" OR "insecticide-treated bed" OR "treated nets" OR "mosquito nets" OR "insecticidal nets"),title.search:!rats,title.search:!rat,title.search:!mice,title.search:!mouse,title.search:!"in vitro",title.search:!zebrafish,title.search:!rabbits,title.search:!"animal model",type:!paratext,type:!erratum,type:!book-review,type:!software
```
`#7` (OpenAlex, 2026-10-12):
```text
https://api.openalex.org/works?mailto=revisao.sistematica.ufes@example.org&filter=title_and_abstract.search:(agricultural OR agriculture OR farm OR farming OR crop OR crops OR plantation OR orchard OR vineyard OR residential OR residence OR proximity OR near OR living OR ambient OR drift OR aerial OR spraying OR sprayed OR fumigation OR "drinking water" OR "surface water" OR groundwater OR rural OR county OR counties OR municipality OR municipalities OR district OR region OR regions OR geographic OR spatial OR ecological OR community OR communities OR "genetically modified" OR transgenic OR ban OR policy OR banana OR bananas OR "natural experiment" OR "difference-in-differences" OR "instrumental variable" OR "quasi-experimental" OR "regression discontinuity" OR "event study" OR village OR villages OR "zip code" OR "census tract" OR geocoded OR GIS OR buffer OR "land use" OR corn OR maize OR soybean OR cotton OR sugarcane OR "well water" OR "water supply" OR prohibition OR chlordecone)
```
`#8` (OpenAlex, 2026-10-12):
```text
https://api.openalex.org/works?mailto=revisao.sistematica.ufes@example.org&filter=title_and_abstract.search:((pesticide OR herbicide OR insecticide OR fungicide OR glyphosate OR atrazine OR organophosphate OR agrochemical OR agrichemical OR fumigation OR fumigant OR "aerial spraying" OR "crop dusting" OR chlorpyrifos OR paraquat OR "plant protection products") OR (agrotoxic OR agrotoxics OR plaguicide OR plaguicides OR nematicide OR carbamate OR pyrethroid OR neonicotinoid OR mancozeb OR malathion OR naled OR dibromochloropropane OR "methyl bromide" OR "aerial application" OR "aerial spray" OR "spray drift" OR "pesticide drift" OR "crop spraying" OR Roundup OR "agricultural chemicals") OR ("drinking water contaminant" OR "drinking water contamination" OR "water contaminants") OR (procymidone OR carbaryl OR carbofuran OR fenitrothion OR dithiocarbamate OR dithiocarbamates OR chlordecone OR kepone OR "crop protection")) AND ((("birth weight" OR birthweight OR preterm OR "premature birth" OR "gestational age" OR "gestational length" OR "fetal growth" OR "intrauterine growth" OR stillbirth OR "fetal death" OR "fetal loss" OR miscarriage OR "spontaneous abortion" OR "infant mortality" OR "neonatal mortality" OR "perinatal mortality" OR "infant death" OR "birth defects" OR "congenital anomalies" OR "congenital malformations" OR "neural tube defects" OR hypospadias OR cryptorchidism OR gastroschisis OR "orofacial clefts" OR "birth outcomes" OR "pregnancy outcomes" OR "perinatal health" OR "newborn health" OR "infant health" OR "neonatal health" OR "reproductive outcomes") OR ("pregnancy loss" OR "foetal death" OR "fetal mortality" OR "perinatal outcomes" OR "neonatal outcomes" OR "congenital defects" OR "congenital heart defects" OR "spina bifida" OR anencephaly OR "cleft lip" OR "limb reduction") OR ("child mortality" OR "child health" OR "infant and child" OR "under-five mortality" OR "infant outcomes")) OR ("neonatal death" OR "perinatal death" OR "length of gestation" OR "gestation length" OR "gestational duration" OR "shortened gestation" OR "oral clefts" OR "cleft palate" OR anophthalmia OR microphthalmia OR Apgar OR "head circumference" OR "birth length" OR "congenital cardiac" OR "congenital heart" OR "birth malformations" OR "congenital abnormalities" OR "birth anomalies" OR "fetal malformations" OR "foetal growth" OR "premature delivery" OR "premature infants" OR "abdominal wall defects")) AND (agricultural OR agriculture OR farm OR farming OR crop OR crops OR plantation OR orchard OR vineyard OR residential OR residence OR proximity OR near OR living OR ambient OR drift OR aerial OR spraying OR sprayed OR fumigation OR "drinking water" OR "surface water" OR groundwater OR rural OR county OR counties OR municipality OR municipalities OR district OR region OR regions OR geographic OR spatial OR ecological OR community OR communities OR "genetically modified" OR transgenic OR ban OR policy OR banana OR bananas OR "natural experiment" OR "difference-in-differences" OR "instrumental variable" OR "quasi-experimental" OR "regression discontinuity" OR "event study" OR village OR villages OR "zip code" OR "census tract" OR geocoded OR GIS OR buffer OR "land use" OR corn OR maize OR soybean OR cotton OR sugarcane OR "well water" OR "water supply" OR prohibition OR chlordecone) NOT ("bed nets" OR bednets OR "bed net" OR "insecticide-treated nets" OR "insecticide-treated bed" OR "treated nets" OR "mosquito nets" OR "insecticidal nets"),title.search:!rats,title.search:!rat,title.search:!mice,title.search:!mouse,title.search:!"in vitro",title.search:!zebrafish,title.search:!rabbits,title.search:!"animal model",type:!paratext,type:!erratum,type:!book-review,type:!software
```
`#9` (OpenAlex, 2026-10-12):
```text
https://api.openalex.org/works?mailto=revisao.sistematica.ufes@example.org&filter=title_and_abstract.search:((pesticide OR herbicide OR insecticide OR fungicide OR glyphosate OR atrazine OR organophosphate OR agrochemical OR agrichemical OR fumigation OR fumigant OR "aerial spraying" OR "crop dusting" OR chlorpyrifos OR paraquat OR "plant protection products") OR (agrotoxic OR agrotoxics OR plaguicide OR plaguicides OR nematicide OR carbamate OR pyrethroid OR neonicotinoid OR mancozeb OR malathion OR naled OR dibromochloropropane OR "methyl bromide" OR "aerial application" OR "aerial spray" OR "spray drift" OR "pesticide drift" OR "crop spraying" OR Roundup OR "agricultural chemicals") OR ("drinking water contaminant" OR "drinking water contamination" OR "water contaminants") OR (procymidone OR carbaryl OR carbofuran OR fenitrothion OR dithiocarbamate OR dithiocarbamates OR chlordecone OR kepone OR "crop protection")) AND ((("birth weight" OR birthweight OR preterm OR "premature birth" OR "gestational age" OR "gestational length" OR "fetal growth" OR "intrauterine growth" OR stillbirth OR "fetal death" OR "fetal loss" OR miscarriage OR "spontaneous abortion" OR "infant mortality" OR "neonatal mortality" OR "perinatal mortality" OR "infant death" OR "birth defects" OR "congenital anomalies" OR "congenital malformations" OR "neural tube defects" OR hypospadias OR cryptorchidism OR gastroschisis OR "orofacial clefts" OR "birth outcomes" OR "pregnancy outcomes" OR "perinatal health" OR "newborn health" OR "infant health" OR "neonatal health" OR "reproductive outcomes") OR ("pregnancy loss" OR "foetal death" OR "fetal mortality" OR "perinatal outcomes" OR "neonatal outcomes" OR "congenital defects" OR "congenital heart defects" OR "spina bifida" OR anencephaly OR "cleft lip" OR "limb reduction") OR ("child mortality" OR "child health" OR "infant and child" OR "under-five mortality" OR "infant outcomes")) OR ("neonatal death" OR "perinatal death" OR "length of gestation" OR "gestation length" OR "gestational duration" OR "shortened gestation" OR "oral clefts" OR "cleft palate" OR anophthalmia OR microphthalmia OR Apgar OR "head circumference" OR "birth length" OR "congenital cardiac" OR "congenital heart" OR "birth malformations" OR "congenital abnormalities" OR "birth anomalies" OR "fetal malformations" OR "foetal growth" OR "premature delivery" OR "premature infants" OR "abdominal wall defects")) NOT ("bed nets" OR bednets OR "bed net" OR "insecticide-treated nets" OR "insecticide-treated bed" OR "treated nets" OR "mosquito nets" OR "insecticidal nets") NOT (agricultural OR agriculture OR farm OR farming OR crop OR crops OR plantation OR orchard OR vineyard OR residential OR residence OR proximity OR near OR living OR ambient OR drift OR aerial OR spraying OR sprayed OR fumigation OR "drinking water" OR "surface water" OR groundwater OR rural OR county OR counties OR municipality OR municipalities OR district OR region OR regions OR geographic OR spatial OR ecological OR community OR communities OR "genetically modified" OR transgenic OR ban OR policy OR banana OR bananas OR "natural experiment" OR "difference-in-differences" OR "instrumental variable" OR "quasi-experimental" OR "regression discontinuity" OR "event study" OR village OR villages OR "zip code" OR "census tract" OR geocoded OR GIS OR buffer OR "land use" OR corn OR maize OR soybean OR cotton OR sugarcane OR "well water" OR "water supply" OR prohibition OR chlordecone),title.search:!rats,title.search:!rat,title.search:!mice,title.search:!mouse,title.search:!"in vitro",title.search:!zebrafish,title.search:!rabbits,title.search:!"animal model",type:!paratext,type:!erratum,type:!book-review,type:!software
```
`#1` (PubMed (E-utilities esearch, db=pubmed), 2026-10-12):
```text
(pesticide*[tiab] OR herbicide*[tiab] OR insecticide*[tiab] OR fungicide*[tiab] OR glyphosate[tiab] OR atrazine[tiab] OR organophosphate*[tiab] OR agrochemical*[tiab] OR agrichemical*[tiab] OR fumigat*[tiab] OR "aerial spraying"[tiab] OR "aerial application"[tiab] OR "aerial spray*"[tiab] OR "crop dusting"[tiab] OR "crop spraying"[tiab] OR chlorpyrifos[tiab] OR paraquat[tiab] OR malathion[tiab] OR naled[tiab] OR "methyl bromide"[tiab] OR dibromochloropropane[tiab] OR "spray drift"[tiab] OR "pesticide drift"[tiab] OR pyrethroid*[tiab] OR neonicotinoid*[tiab] OR carbamate*[tiab] OR nematicide*[tiab] OR mancozeb[tiab] OR Roundup[tiab] OR agrotoxic*[tiab] OR plaguicide*[tiab] OR "plant protection product*"[tiab] OR "crop protection"[tiab] OR "agricultural chemicals"[tiab] OR "drinking water contaminant*"[tiab] OR "drinking water contamination"[tiab] OR "water contaminants"[tiab] OR procymidone[tiab] OR carbaryl[tiab] OR carbofuran[tiab] OR fenitrothion[tiab] OR dithiocarbamate*[tiab] OR chlordecone[tiab] OR kepone[tiab] OR Pesticides[mh] OR Agrochemicals[mh] OR "Pesticide Residues"[mh])
```
`#2` (PubMed (E-utilities esearch, db=pubmed), 2026-10-12):
```text
("birth weight"[tiab] OR birthweight[tiab] OR preterm[tiab] OR "premature birth"[tiab] OR "premature deliver*"[tiab] OR "premature infant*"[tiab] OR "gestational age"[tiab] OR "gestational length"[tiab] OR "gestational duration"[tiab] OR "gestation length"[tiab] OR "length of gestation"[tiab] OR "shortened gestation"[tiab] OR "small for gestational age"[tiab] OR "fetal growth"[tiab] OR "foetal growth"[tiab] OR "intrauterine growth"[tiab] OR "head circumference"[tiab] OR "birth length"[tiab] OR Apgar[tiab] OR stillbirth*[tiab] OR "fetal death*"[tiab] OR "foetal death*"[tiab] OR "fetal loss"[tiab] OR "fetal mortality"[tiab] OR "pregnancy loss"[tiab] OR miscarriage*[tiab] OR "spontaneous abortion*"[tiab] OR "infant mortality"[tiab] OR "neonatal mortality"[tiab] OR "perinatal mortality"[tiab] OR "infant death*"[tiab] OR "neonatal death*"[tiab] OR "perinatal death*"[tiab] OR "child mortality"[tiab] OR "under-five mortality"[tiab] OR "birth defect*"[tiab] OR "congenital anomal*"[tiab] OR "congenital malformation*"[tiab] OR "congenital abnormalit*"[tiab] OR "congenital defect*"[tiab] OR "congenital heart"[tiab] OR "congenital cardiac"[tiab] OR "birth malformation*"[tiab] OR "birth anomal*"[tiab] OR "fetal malformation*"[tiab] OR "neural tube defect*"[tiab] OR "spina bifida"[tiab] OR anencephaly[tiab] OR hypospadias[tiab] OR cryptorchidism[tiab] OR gastroschisis[tiab] OR "abdominal wall defect*"[tiab] OR "orofacial cleft*"[tiab] OR "oral cleft*"[tiab] OR "cleft lip"[tiab] OR "cleft palate"[tiab] OR "limb reduction"[tiab] OR anophthalmia[tiab] OR microphthalmia[tiab] OR "birth outcome*"[tiab] OR "pregnancy outcome*"[tiab] OR "perinatal outcome*"[tiab] OR "neonatal outcome*"[tiab] OR "perinatal health"[tiab] OR "newborn health"[tiab] OR "neonatal health"[tiab] OR "infant health"[tiab] OR "infant outcome*"[tiab] OR "child health"[tiab] OR "infant and child"[tiab] OR "reproductive outcome*"[tiab] OR "Pregnancy Outcome"[mh] OR "Birth Weight"[mh] OR "Infant, Low Birth Weight"[mh] OR "Premature Birth"[mh] OR "Gestational Age"[mh] OR "Fetal Growth Retardation"[mh] OR "Infant, Small for Gestational Age"[mh] OR "Fetal Death"[mh] OR "Abortion, Spontaneous"[mh] OR "Perinatal Death"[mh] OR "Infant Mortality"[mh] OR "Congenital Abnormalities"[mh])
```
`#3` (PubMed (E-utilities esearch, db=pubmed), 2026-10-12):
```text
("Insecticide-Treated Bednets"[mh] OR "bed net*"[tiab] OR bednet*[tiab] OR "mosquito net*"[tiab] OR "insecticide-treated net*"[tiab] OR "insecticidal net*"[tiab] OR "treated net*"[tiab])
```
`#4` (PubMed (E-utilities esearch, db=pubmed), 2026-10-12):
```text
(animals[mh] NOT humans[mh])
```
`#5` (PubMed (E-utilities esearch, db=pubmed), 2026-10-12):
```text
(pesticide*[tiab] OR herbicide*[tiab] OR insecticide*[tiab] OR fungicide*[tiab] OR glyphosate[tiab] OR atrazine[tiab] OR organophosphate*[tiab] OR agrochemical*[tiab] OR agrichemical*[tiab] OR fumigat*[tiab] OR "aerial spraying"[tiab] OR "aerial application"[tiab] OR "aerial spray*"[tiab] OR "crop dusting"[tiab] OR "crop spraying"[tiab] OR chlorpyrifos[tiab] OR paraquat[tiab] OR malathion[tiab] OR naled[tiab] OR "methyl bromide"[tiab] OR dibromochloropropane[tiab] OR "spray drift"[tiab] OR "pesticide drift"[tiab] OR pyrethroid*[tiab] OR neonicotinoid*[tiab] OR carbamate*[tiab] OR nematicide*[tiab] OR mancozeb[tiab] OR Roundup[tiab] OR agrotoxic*[tiab] OR plaguicide*[tiab] OR "plant protection product*"[tiab] OR "crop protection"[tiab] OR "agricultural chemicals"[tiab] OR "drinking water contaminant*"[tiab] OR "drinking water contamination"[tiab] OR "water contaminants"[tiab] OR procymidone[tiab] OR carbaryl[tiab] OR carbofuran[tiab] OR fenitrothion[tiab] OR dithiocarbamate*[tiab] OR chlordecone[tiab] OR kepone[tiab] OR Pesticides[mh] OR Agrochemicals[mh] OR "Pesticide Residues"[mh]) AND ("birth weight"[tiab] OR birthweight[tiab] OR preterm[tiab] OR "premature birth"[tiab] OR "premature deliver*"[tiab] OR "premature infant*"[tiab] OR "gestational age"[tiab] OR "gestational length"[tiab] OR "gestational duration"[tiab] OR "gestation length"[tiab] OR "length of gestation"[tiab] OR "shortened gestation"[tiab] OR "small for gestational age"[tiab] OR "fetal growth"[tiab] OR "foetal growth"[tiab] OR "intrauterine growth"[tiab] OR "head circumference"[tiab] OR "birth length"[tiab] OR Apgar[tiab] OR stillbirth*[tiab] OR "fetal death*"[tiab] OR "foetal death*"[tiab] OR "fetal loss"[tiab] OR "fetal mortality"[tiab] OR "pregnancy loss"[tiab] OR miscarriage*[tiab] OR "spontaneous abortion*"[tiab] OR "infant mortality"[tiab] OR "neonatal mortality"[tiab] OR "perinatal mortality"[tiab] OR "infant death*"[tiab] OR "neonatal death*"[tiab] OR "perinatal death*"[tiab] OR "child mortality"[tiab] OR "under-five mortality"[tiab] OR "birth defect*"[tiab] OR "congenital anomal*"[tiab] OR "congenital malformation*"[tiab] OR "congenital abnormalit*"[tiab] OR "congenital defect*"[tiab] OR "congenital heart"[tiab] OR "congenital cardiac"[tiab] OR "birth malformation*"[tiab] OR "birth anomal*"[tiab] OR "fetal malformation*"[tiab] OR "neural tube defect*"[tiab] OR "spina bifida"[tiab] OR anencephaly[tiab] OR hypospadias[tiab] OR cryptorchidism[tiab] OR gastroschisis[tiab] OR "abdominal wall defect*"[tiab] OR "orofacial cleft*"[tiab] OR "oral cleft*"[tiab] OR "cleft lip"[tiab] OR "cleft palate"[tiab] OR "limb reduction"[tiab] OR anophthalmia[tiab] OR microphthalmia[tiab] OR "birth outcome*"[tiab] OR "pregnancy outcome*"[tiab] OR "perinatal outcome*"[tiab] OR "neonatal outcome*"[tiab] OR "perinatal health"[tiab] OR "newborn health"[tiab] OR "neonatal health"[tiab] OR "infant health"[tiab] OR "infant outcome*"[tiab] OR "child health"[tiab] OR "infant and child"[tiab] OR "reproductive outcome*"[tiab] OR "Pregnancy Outcome"[mh] OR "Birth Weight"[mh] OR "Infant, Low Birth Weight"[mh] OR "Premature Birth"[mh] OR "Gestational Age"[mh] OR "Fetal Growth Retardation"[mh] OR "Infant, Small for Gestational Age"[mh] OR "Fetal Death"[mh] OR "Abortion, Spontaneous"[mh] OR "Perinatal Death"[mh] OR "Infant Mortality"[mh] OR "Congenital Abnormalities"[mh]) NOT (animals[mh] NOT humans[mh]) NOT ("Insecticide-Treated Bednets"[mh] OR "bed net*"[tiab] OR bednet*[tiab] OR "mosquito net*"[tiab] OR "insecticide-treated net*"[tiab] OR "insecticidal net*"[tiab] OR "treated net*"[tiab])
```
`#6` (PubMed (E-utilities esearch, db=pubmed), 2026-10-12):
```text
(agricultur*[tiab] OR farm*[tiab] OR crop*[tiab] OR plantation*[tiab] OR orchard*[tiab] OR vineyard*[tiab] OR residential[tiab] OR residence*[tiab] OR proximity[tiab] OR near[tiab] OR living[tiab] OR ambient[tiab] OR drift[tiab] OR aerial[tiab] OR spraying[tiab] OR sprayed[tiab] OR "drinking water"[tiab] OR "surface water"[tiab] OR groundwater[tiab] OR "well water"[tiab] OR "water supply"[tiab] OR rural[tiab] OR county[tiab] OR counties[tiab] OR municipal*[tiab] OR district*[tiab] OR region*[tiab] OR geographic*[tiab] OR spatial[tiab] OR ecological[tiab] OR communit*[tiab] OR village*[tiab] OR "zip code*"[tiab] OR "census tract*"[tiab] OR geocod*[tiab] OR GIS[tiab] OR buffer*[tiab] OR "land use"[tiab] OR "genetically modified"[tiab] OR transgenic[tiab] OR banana*[tiab] OR corn[tiab] OR maize[tiab] OR soybean*[tiab] OR cotton[tiab] OR sugarcane[tiab] OR ban[tiab] OR prohibition[tiab] OR policy[tiab] OR "natural experiment*"[tiab] OR "difference-in-difference*"[tiab] OR "instrumental variable*"[tiab] OR "quasi-experiment*"[tiab] OR "regression discontinuity"[tiab] OR "event study"[tiab] OR Agriculture[mh] OR "Rural Population"[mh] OR "Drinking Water"[mh] OR "Water Pollutants, Chemical"[mh])
```
`#7` (PubMed (E-utilities esearch, db=pubmed), 2026-10-12):
```text
#5 AND #6  [as run on the history server: #2 AND (agricultur*[tiab] OR farm*[tiab] OR ... OR "Water Pollutants, Chemical"[mh]) with the full #6 string above]
```
`#8` (PubMed (E-utilities esearch, db=pubmed), 2026-10-12):
```text
#5 NOT #6
```

**O que entra na triagem:**

- OpenAlex: line #6 (3,730 records). Screen tier 1 = #8 (2,128) first, then tier 2 = #9 (1,602). #7 is a flag only.
- PubMed: line #5 (2,054 records), deduplicated against OpenAlex #6 by DOI/PMID. Tier 1 = #7 (892), tier 2 = #8 (1,162). #6 is a flag only.
- Supplementary sources, unchanged from calibration and outside the numbered Boolean lines: ranked framings F1-F4 on the PubMed/medRxiv/arXiv index and Scholar Gateway S1-S2; the grey-literature query set plus the PRESS addition site:ideas.repec.org "aerial fumigation"; forward and backward citation chasing (OpenAlex cites:/cited_by:) from the seeds, the ISA and chlordecone cohort papers and all included studies.

**Ordem de triagem:** Every record in OpenAlex #6 ∪ PubMed #5 (after deduplication) is screened; the context block never excludes anything. Order:
1. Tier 1: records matching the context flag (OpenAlex #8 ∪ PubMed #7).
2. Tier 2: the rest (OpenAlex #9 ∪ PubMed #8).

Within each tier, records can be sorted by OpenAlex relevance or citation count to speed up early discovery. The tier membership of every included study is recorded, so that the flag's sensitivity can be reported afterwards; ISA 2024 is a known tier-2 relevant item.

Reviews (76 in #5) are not eligible, but go to the citation-chasing list.

**Recall, desenvolvimento** (itens usados no ajuste; otimista por construção):

> Development set: the 9 calibration seeds, the 6 PRESS-found items that have DOIs, and the 20 calibration validation items whose DOIs are recorded in sq1-internacional.json (incidental_relevant_studies). Total 35 DOIs.
> 
> OpenAlex, line #6 (2026-10-12; OQL echo matched): 35/35 retrieved, 100% (Wilson 95% CI 0.90–1.00).
> - Seeds 9/9: 10.1038/s41467-017-00349-2, 10.1086/725349, 10.1016/j.jhealeco.2017.04.005, 10.1093/restud/rdad011, 10.1073/pnas.2413013121, 10.1111/j.1365-3016.2010.01165.x, 10.1111/j.1651-2227.2008.01207.x, 10.1002/pam.22558, 10.3390/toxics6030041.
> - PRESS items 6/6: Kadhel 2014 (10.1093/aje/kwt313), Herve 2016 (10.1016/j.envres.2016.08.004), Rouget 2019 (10.1007/s11356-019-06031-y), ISA 2024 (10.1097/ee9.0000000000000290), the 2016 review (10.1007/s40572-016-0085-0), and the 1991 India cotton-field study (10.1016/s0013-9351(05)80168-9).
> - Calibration validation items 20/20, including Brainerd & Menon 2014 (borderline: fertilizer).
> 
> PubMed, line #5 (history server): 32/32 PubMed-indexed development items retrieved. Three development items are not in PubMed (warninglist 'quoted phrase not found'): Calzada 2023, Dias 2023 and Brainerd 2014.
> 
> Not re-tested: the PRESS items 'Agricultural Pesticide Exposure and Congenital Abnormalities in Mexico: A Systematic Review' (2019) and the ISEE 2024 Apgar abstract, because the PRESS file does not record their DOIs. PRESS found both in QR2. #5 is a logical superset of QR2 (the same string without the context AND), so both remain retrieved unless OpenAlex types them as paratext, erratum, book-review or software.
> 
> The out-of-scope calibration items (Lai 2017 and Fletcher & Noghanibehambari 2023, adult and later-life outcomes) were excluded from the denominator, as in calibration.
> 
> These items informed the string design, so this is development-set recall, not an independent estimate.

**Recall, validação independente** (itens escolhidos antes do teste):

> How the items were selected, fixed BEFORE any retrieval test. Two routes, both independent of the Boolean terms:
> - R1, forward citations: OpenAlex filter cites:W2743540986|W2036103866|W3124792110|W2117778701|W4406357681|W4362575627 (Larsen 2017, Gemmill 2013, Dias 2023, Kadhel 2014, Reynier 2025, Calzada 2023), from_publication_date:2024-01-01, type:article|preprint. This returned 123 works.
> - R2, backward references: the reference list of a recent review that calibration and PRESS never used, 'Pesticide Exposures during Pregnancy and Health Outcomes in Latin America and the Caribbean: A Scoping Review' (Environ Health Perspect 2024, 10.1289/jhp1043, W4401700389), fetched with OpenAlex cited_by:W4401700389. This returned 156 references.
> 
> Inclusion rule, applied to titles only:
> - primary study (not a review);
> - the title indicates environmental, residential, area-level or exclusively-agricultural-source pesticide or agrochemical exposure (not occupational-only);
> - the title indicates an SQ1 outcome;
> - not among the 35 development items, and not named anywhere in calibracao/*.json for any block. This was checked with grep before testing, and it moved 3 Brazilian items to tier B.
> 
> Items that failed only the 'unused' condition (tier B) or whose eligibility was doubtful (tier C) were tested too, but are reported separately. All items come from OpenAlex, so all are indexed there. PubMed indexing was checked with a DOI-only esearch (warninglist). Retrieval was tested with a single OpenAlex call (openalex:<ids> AND line #6) and with PubMed #5 AND (<DOIs>)[doi].
> 
> TIER A — fresh for every block (the independent estimate):
> - A1 Maternal residential exposure to agricultural pesticides and birth defects, North Carolina 2016 (10.1002/bdra.23479; R2): OpenAlex retrieved; PubMed indexed and retrieved.
> - A2 Pesticides exposure in pregnant Argentinian women: residence areas and anthropometric neonate parameters, Chemosphere 2023 (10.1016/j.chemosphere.2023.138790; R2): OpenAlex MISSED; PubMed (PMID 37142107) indexed and MISSED.
> - A3 Neonatal, placental and umbilical cord blood parameters in pregnant women residing in areas with intensive pesticide application, ESPR 2017 (10.1007/s11356-017-9642-9; R2): OpenAlex MISSED; PubMed (PMID 28718019) indexed and MISSED.
> - A4 High prevalence of micropenis in newborns from an intensive-use pesticide area of Northeastern Brazil, 2012 (10.1111/j.1365-2605.2011.01241.x; R2): retrieved in both.
> - A5 Exposure to pesticides and cryptorchidism: geographical evidence, EHP 1996 (10.1289/ehp.104-1469503; R2): retrieved in both.
> - A6 Glyphosate Use, Water Contamination, and Neonatal Health in the United States, 2025 (10.1086/740157; R1): OpenAlex retrieved; not in PubMed.
> - A7 The health effects of prenatal pesticide exposure by marital status, 2026 (10.1186/s12982-026-01469-1; R1): OpenAlex retrieved; not in PubMed.
> 
> Tier A result:
> - OpenAlex 5/7 = 71% (Wilson 95% CI 0.36–0.92).
> - PubMed 3/5 indexed.
> - Union of both databases 5/7. Both misses are missed by both databases.
> 
> Why the misses happened (diagnosed after testing):
> - In OpenAlex, both records have abstract_inverted_index = null (Elsevier and Springer). The titles say 'anthropometric neonate parameters' and 'Neonatal, placental, and umbilical cord blood parameters', and no outcome-block phrase matches them.
> - PubMed holds both abstracts ('Has Abstract', MEDLINE-indexed) and still misses them. So the abstracts also lack every outcome phrase in the block and carry no outcome MeSH. This is an outcome-vocabulary gap for anthropometric or 'neonatal parameter' reporting, not only a missing-abstract problem.
> - A broad patch was tested afterwards: (neonatal OR neonate(s) OR newborn(s) OR anthropometric OR anthropometry OR "placental weight") AND exposure NOT outcome. It added 2,223 OpenAlex records whose top-cited hits were noise, so it was not adopted.
> 
> TIER B — fresh for this block's string, but used as test items in the Latin America arm's calibration: 5/5 retrieved in OpenAlex.
> - Cremonese 2012 (10.1590/s0102-311x2012000700005): also PubMed indexed and retrieved.
> - Pesticide consumption and CNS/cardiovascular malformations, Brazil 2014 (10.2478/s13382-014-0269-5): also PubMed indexed and retrieved.
> - Malformações congênitas em regiões de monocultivo, Minas Gerais 2017 (10.11606/issn.2176-7262.v50i5p285-296): not in PubMed.
> - Agrochemicals and obstetric outcomes, Uruguay 2024, English version (10.1590/1809-4422asoc00761vu27l3oa): not in PubMed.
> - Congenital defects and exposure to pesticides in the São Francisco Valley, 2011 (W1746831501, no DOI): retrieved by its OpenAlex ID.
> Tiers A+B together: OpenAlex 10/12 = 83% (95% CI 0.55–0.95).
> 
> TIER C — eligibility doubtful (DA-1b multi-source biomonitoring, or exposure unclear); reported but not counted. 5/6 retrieved in OpenAlex, and every PubMed-indexed one was retrieved.
> - Glyphosate/AMPA and birth outcomes, Midwest 2025 (10.1016/j.ijheh.2025.114733): retrieved in both.
> - PROTECT glyphosate and preterm birth, 2021 (10.1289/ehp7295): retrieved in both.
> - The health effects of GM crops, 2026 (10.1016/j.jdeveco.2026.103930): OpenAlex retrieved; not in PubMed.
> - Gestational disorders, intensive-application areas, 2019 (10.1016/j.etap.2019.103280): retrieved in both.
> - Chihuahua placental maturity and newborn weight, 2009 (10.1177/0960327109107045): retrieved in both.
> - MISSED: Clusters of prenatally detected fetal defects, San Joaquin Valley, 2026 (10.1177/87564793261428863). Its abstract measures no exposure and mentions only 'agricultural/industrial chemicals' as future research. The slash breaks the phrase "agricultural chemicals", so the record does not match. It is not eligible, so this is a correct non-retrieval.
> 
> Caveat: selection was title-based, and titles share vocabulary with the search, so recall is probably overstated. Even so, the test exposed a real outcome-vocabulary gap.

**Volume:** Estimate only; no deduplication was run. About 3,900–4,200 unique records for title/abstract screening:
- OpenAlex #6: 3,730.
- PubMed #5: 2,054, which overlaps OpenAlex heavily. Expect roughly 150–350 PubMed-only records, added mainly through MeSH.
- Ranked supplements and grey literature: about 20–50.
- Citation chasing: additional.

Tier 1 is about 2,200–2,350 unique (OpenAlex #8 = 2,128 plus the PubMed-only part of PubMed #7 = 892). Tier 2 is about 1,700–1,850.

Expect the set to shrink:
- internal OpenAlex duplicates (preprint/published pairs);
- 198 conference abstracts and 123 dissertations in #5, which the protocol excludes at screening (abstracts without full text; theses);
- records published before 1990, which are ineligible by period. This share was not measured.

This is more than calibration's QF3 (1,859) and PRESS QR1 (1,962). That is the cost of dropping the context filter and moving the animal NOT to the title. In return, the strategy retrieves ISA 2024 and the 2016 review.

**Mudanças da PRESS não aplicadas, e por quê:**

- *PubMed proximity searching for key pairs (e.g. "pesticide exposure"[tiab:~3])* — PRESS marked it untested. The phrase and MeSH coverage already retrieves 32/32 indexed development items. It was not tested here because the Parallel transport was rate-limited and Firecrawl credits were low.
- *Add organophosphorus and triazine as exposure terms* — PRESS advised against them: they bring flame-retardant and melamine noise. Organophosphate and atrazine are already present.
- *Add prematurity, bare congenital, malformation or teratogenic as outcome terms* — PRESS showed noise: 856 marginal records driven by premature*, and 1,301 from bare congenital/malformation. The specific phrase group was added instead.
- *Add a vector-control/aircraft exposure block (mosquito control, vector control, adulticide, aircraft, airplane)* — PRESS measured 264 marginal records, mostly aircraft noise and IRS/malaria. Aerial vector control is eligible under the protocol, and the existing terms (naled, malathion, aerial spraying/application/spray) plus citation chasing cover the known studies (the Medfly malathion studies are retrieved).
- *Add 2,4-D / 2,4,5-T* — Not required by PRESS (it only gave encoding advice), and commas inside a search value must be avoided. 'herbicide' and the citation chasing cover the Agent Orange/2,4,5-T literature: the 1981 aerial 2,4,5-T study is retrieved.
- *Post-validation outcome patch (neonatal OR neonate OR neonates OR newborn OR newborns OR anthropometric OR anthropometry OR "placental weight") to recover the two independent misses* — Tested on 2026-10-12: it adds 2,223 OpenAlex records (exposure AND patch NOT #2 NOT #3, title-NOT and types), and the top 25 by citations are essentially all noise (melatonin, saliva, ARDS, chlorpyrifos mechanisms). That is about +60% volume, mostly noise. It was also derived from the independent misses, so adopting it would contaminate the validation estimate. Recommended instead: citation chasing of included Latin American studies and the LatAm arm; a narrower phrase patch can be considered in a documented protocol amendment.
- *Citation chasing (OpenAlex cites:/referenced_works from the seeds, the ISA and chlordecone cohort papers) and site:ideas.repec.org "aerial fumigation"* — These are not Boolean database lines, so they are not frozen here. They stay in the supplementary search plan to run at the search stage. The forward-chasing syntax was verified in this run (cites: on 6 anchors returned 123 works from 2024 onward).
- *Optional type:!dissertation filter (123 records in #5)* — Not a PRESS change. The protocol excludes theses, but they are kept in the export so that exclusions are counted at screening (PRISMA transparency).

**Problemas e limites registrados:**

- Transport: Parallel web_fetch returned 'Too Many Requests' on every attempt (6 tries), and direct curl to api.openalex.org is blocked by the proxy (CONNECT 403). All 25 counts went through Firecrawl scrape at maxAge=0, and every response carried a 'low on credits' warning. The user should add Firecrawl credits before the export or search stage.
- Some line counts are null: OpenAlex #4 and #7, PubMed #3, #4 and #6. These are NOT/flag blocks that are not meaningful alone, and they were not run separately to save credits. Their syntax was verified inside the combination echoes. OpenAlex #9 and PubMed #8 are derived by subtraction.
- Independent recall is 5/7 (71%, CI 0.36–0.92). Both misses are Argentine residential-exposure studies that report 'neonatal/anthropometric parameters' with no phrase from the outcome block. In OpenAlex their abstracts are also null (Elsevier, Springer), which contradicts the calibration's general claim that Elsevier abstracts are searchable even when hidden. Expect other studies that report newborn anthropometry or neonatal parameters to be missed. Mitigations: citation chasing, the LatAm arm, and possibly a narrow phrase amendment.
- The development set was reconstructed from the DOIs recorded in calibracao/sq1-internacional.json. Calibration validation sets 1 and 2 (37 items) are not fully enumerated there, so about 10 of them could not be re-tested. To keep the independent set clean, its candidates were checked against every calibracao/*.json file before testing.
- The PRESS items Mexico CA review (2019) and the ISEE 2024 Apgar abstract were not re-tested because their DOIs are not recorded. Logically they are retrieved (#5 is a superset of PRESS QR2), unless OpenAlex types them as one of the 4 excluded types.
- The protocol limits the period to 1990–2026-10-11, but no date filter was applied, following PRESS. Pre-1990 records (e.g. aerial 2,4,5-T 1981, Medfly malathion 1987) are excluded at screening. Their share in #6 was not measured.
- #5 contains 198 conference abstracts, 123 dissertations, 200 book chapters and 76 reviews. The protocol excludes conference abstracts without full text and theses, and reviews go to citation chasing. Screening workload is lower than the raw 3,730 suggests.
- OpenAlex has no wildcards (it stems inflections only) and no proximity operator, so spelling variants were added by hand. PubMed truncation inside phrases ("aerial spray*", "congenital anomal*") was accepted, as the querytranslation shows.
- Volume more than doubled compared with calibration QF3 (1,859 → 3,730) and PRESS QR1 (1,962). The tiered order keeps the context-matching records first, but every record must be screened.
- OpenAlex counts are snapshots and change over time. A re-run should record the date and compare against these counts. The PubMed WebEnv used (MCID_6acc31ff316c767392068878) expires; re-run the history sequence instead of reusing it.

---

## SQ1 — braço América Latina (PT/ES/EN)

**Fonte:** rodada de finalização (`-final.json`), que aplica a PRESS e congela as linhas.

| linha | base | contagem | descrição |
|---|---|---:|---|
| OA #1 | OpenAlex | — | Final exposure block E. This is PRESS E4 plus six organochlorine terms added after validation (DDE OR DDT OR organochlorine OR organochlorines OR organoclorados OR dichlorodiphenyldichloroethylene). #1-v0 is the same string without those six terms; it is the PRESS E4 used in the independent validation. Bare fungicidas/herbicidas/insecticidas/fitosanitarios are deliberately excluded. Used only as a component, so no standalone count was run. |
| OA #2 | OpenAlex | — | Final outcome block O. This is PRESS O4 (the targeted additions only) plus nine terms added after validation ("congenital abnormalities" through "birth size"). #2-v0 is the same string without those nine terms; it is the PRESS O4. Used only as a component. |
| OA #3 | OpenAlex | — | Final geography block G. This is PRESS G4 (Brazilian states, demonyms, SINASC/DATASUS, the Caribbean including the French Antilles, Puerto Rico) plus 18 terms added after validation, from Ceara onward: unaccented state names, RN/PI/MA/TO/ES, América del Sur/do Sul, Sudamérica, Latinoamérica, Sul do Brasil/Sur de Brasil. #3-v0 is the same string without those 18 terms; it is the PRESS G4. Used only as a component. |
| OA #4-v0 | OpenAlex | 604 | PRESS single effect branch: #1-v0 AND #2-v0 AND #3-v0 (OA-1 and OA-2 collapsed; no language filter). This is the version measured by the independent validation. Today's count matches PRESS T19 exactly (604). For screening it is superseded by #4, which contains it. |
| OA #4 | OpenAlex | 797 | Final effect line: #1 AND #2 AND #3. It adds 193 records to #4-v0. Measured deltas, each run with the other two blocks fixed at v0: G additions NOT G4 = +1; O additions NOT O4 = +122; E additions NOT E4 = +62. A direct DOI test confirmed it retrieves 4/4 of the independent-validation misses. Those four are therefore development items for this line. |
| OA #5 | OpenAlex | 292 | Supplementary safety net (language), demoted from primary branch: #1-v0 AND #2-v0 AND language:pt/es. The part not in #4-v0 (#1-v0 AND (#2-v0 NOT #3-v0) AND language:pt/es) is 149 records. It is kept because it recovers PT/ES records whose abstracts carry no Latin American place term (independent item I7 is one). Expect Spain and Portugal noise. |
| OA #6 | OpenAlex | 170 | Aerial-spraying arm, any health outcome: calibration OA-3 first block plus the PRESS additions ("pulverizações aéreas", aeroagrícola, "aerial spraying ban") and the unaccented aeroagricola, AND the health/exposure block AND #3. With #3-v0 the count was 169; calibration OA-3 was 146. |
| OA #7a | OpenAlex | 316 | Context arm A, flagged 'context': the calibration OA-4 place phrases plus "Chapada de Apodi" and the unaccented variants (Quixere, "Ze Maria do Tome", "Dossie ABRASCO"), AND the original OA-4 co-term block. It contains OA-4 (311 in calibration). |
| OA #7b | OpenAlex | 236 | Context arm B, flagged 'context': the new place names from PRESS CTX3 AND a pesticide/agribusiness co-term only, with no generic health term. PRESS T6 showed that generic health co-terms bring in Limoeiro-PE and Staraya Russa noise. This arm retrieves Rigotto 2013, which OA-4 missed. |
| OA #8 | OpenAlex | 277 | Ceará arm, flagged 'context': state-level pesticide and aerial-spraying literature. |
| OA #9 | OpenAlex | 33 | Legal/policy arm, flagged 'context / Essay 2', with the bare token "16.820" dropped. The PRESS-tested version with "16.820" gave 63, so that token accounted for about 30 unrelated records. |
| OA #7-9 union | OpenAlex | 657 | #7a OR #7b OR #8 OR #9, run as one nested search value. The raw sum is 862, so about 205 records overlap. A direct DOI test retrieves 8/8 development context items. |
| OA #10 | OpenAlex | 1.591 | Union of every OpenAlex line except #5, run as one nested search value (URL about 9,000 characters, accepted): #4 OR #6 OR #7a OR #7b OR #8 OR #9. The geography block is factored out, so #3 is shared by #4 and #6. |
| OA #11 | OpenAlex | — | Final OpenAlex screening set: #10 OR #5. It cannot be counted in one call because a language filter cannot be ORed with a search filter. Bounds: 1,591 to 1,740 (#10 plus at most the 149 #5 records outside #3-v0). Deduplicate by OpenAlex ID after export. |
| SciELO #1 (S1') | SciELO (search.scielo.org, all indices,  | 187 | Effect line. It is calibration S1 plus agrochem* and fumigat* in the exposure block, and pretermin*, "mortalidade fetal", "mortalidad fetal", natimort*, mortinat* and obstetric* in the outcome block. pulveriz* was not added. The portal echoed the query. Calibration S1 was 175, so the additions give +12. The count is record-level, with the same article repeated across collections. |
| SciELO #2 (S2') | SciELO | 157 | Context line: S2 plus Russas* and Jaguaruana*. Calibration S2 was 135. A Russian distance-education record appeared in the sample, a quirk of truncated-token matching, so expect a little noise. |
| SciELO #3 (S2b) | SciELO | 47 | Ceará line, flagged 'context'. |
| SciELO #4 (S3) | SciELO | 67 | Aerial-spraying arm, unchanged from calibration. Today's count equals the calibration count. |
| SciELO #5 | SciELO | — | Screening set: #1 OR #2 OR #3 OR #4. The raw sum is 458. It was not counted as a single query; deduplicate across collections by PID or DOI. |
| LILACS #1 (L1') | LILACS via BVS portal (filter[db][]=LILA | 418 | Effect line: L1 free text OR the DeCS line. The count was read from the LILACS facet. Calibration L1 was 416, so the DeCS line adds 2, which matches PRESS T15. |
| LILACS #2 (L2'') | LILACS via BVS portal | 125 | Context and aerial line: L2 plus Russas* and Jaguaruana*. Ceara* is not in the place block because adding it there gave 3,067 (see changes not applied). Calibration L2 was 107. |
| LILACS #3 (L2b) | LILACS via BVS portal | 24 | Ceará line, flagged 'context'. It mirrors SciELO S2b and replaces PRESS's Ceara* addition to L2. |
| LILACS #4 | LILACS via BVS portal | — | Screening set: #1 OR #2 OR #3. The raw sum is 567. It was not counted as a single query. |

**Strings exatas, prontas para rodar:**

`OA #1` (OpenAlex, 2026-10-12):
```text
title_and_abstract.search:(agrotóxicos OR agrotóxico OR agrotoxicos OR agrotoxico OR plaguicidas OR pesticidas OR praguicidas OR pesticides OR herbicides OR fungicides OR insecticides OR glyphosate OR glifosato OR agroquímicos OR agroquimicos OR fumigaciones OR "aerial spraying" OR "aerial fumigation" OR "aerial application" OR "crop dusting" OR "pulverização aérea" OR "fumigación aérea" OR "aspersión aérea" OR "aspersiones aéreas" OR "defensivos agrícolas" OR fumigation OR fumigations OR fumigação OR fumigación OR "aerial spray" OR "aerially sprayed" OR agrochemicals OR agrochemical OR "agricultural chemicals" OR agroquímico OR agroquimico OR mancozeb OR chlorpyrifos OR clorpirifós OR organophosphate OR organophosphates OR organofosforados OR paraquat OR atrazine OR procymidone OR procimidona OR chlordecone OR "pesticide drift" OR "spray drift" OR "pulverizações aéreas" OR "aplicação aérea" OR "aviação agrícola" OR DDE OR DDT OR organochlorine OR organochlorines OR organoclorados OR dichlorodiphenyldichloroethylene)
```
`OA #2` (OpenAlex, 2026-10-12):
```text
title_and_abstract.search:("birth weight" OR "low birth weight" OR preterm OR prematurity OR "gestational age" OR "congenital anomalies" OR "congenital malformations" OR "birth defects" OR hypospadias OR cryptorchidism OR stillbirth OR "fetal death" OR miscarriage OR "spontaneous abortion" OR "infant mortality" OR "neonatal mortality" OR "birth outcomes" OR "pregnancy outcomes" OR perinatal OR newborns OR "peso ao nascer" OR "baixo peso" OR prematuridade OR "malformações congênitas" OR "anomalias congênitas" OR "defeitos congênitos" OR "óbito fetal" OR "aborto espontâneo" OR "mortalidade infantil" OR "mortalidade neonatal" OR "recém-nascidos" OR "nascidos vivos" OR "desfechos gestacionais" OR "peso al nacer" OR "bajo peso" OR prematurez OR "malformaciones congénitas" OR "anomalías congénitas" OR "aborto espontáneo" OR "mortalidad infantil" OR "mortalidad neonatal" OR "recién nacidos" OR birthweight OR "infant health" OR "newborn health" OR "neonatal outcomes" OR "fetal growth" OR "gestational length" OR "small for gestational age" OR "saúde infantil" OR "salud infantil" OR "fetal mortality" OR "mortalidade fetal" OR "mortalidad fetal" OR "muerte fetal" OR natimortos OR mortinatos OR "óbitos fetais" OR prematuridad OR "parto prematuro" OR "parto pretérmino" OR "pré-termo" OR "defectos congénitos" OR "neural tube defects" OR "obstetric outcomes" OR "desfechos obstétricos" OR "abortos espontâneos" OR "abortamentos espontâneos" OR "sex ratio at birth" OR "congenital abnormalities" OR "orofacial clefts" OR "cleft lip" OR "cleft palate" OR neonates OR neonate OR "birth length" OR "head circumference" OR "birth size")
```
`OA #3` (OpenAlex, 2026-10-12):
```text
title_and_abstract.search:(Brazil OR Brasil OR Brazilian OR "Latin America" OR "América Latina" OR Ecuador OR Colombia OR Argentina OR Mexico OR México OR Paraguay OR Peru OR Perú OR Chile OR "Costa Rica" OR Nicaragua OR Guatemala OR Honduras OR Uruguay OR Bolivia OR Venezuela OR Panama OR Panamá OR "El Salvador" OR Cuba OR "Dominican Republic" OR "Latin American" OR "South America" OR "Central America" OR Caribbean OR Caribe OR Guadeloupe OR Martinique OR Antilles OR "French West Indies" OR "Puerto Rico" OR Haiti OR Jamaica OR Guyana OR Suriname OR Belize OR Ecuadorian OR Colombian OR Argentine OR Argentinian OR "Costa Rican" OR Chilean OR Peruvian OR Paraguayan OR Uruguayan OR Bolivian OR Venezuelan OR Nicaraguan OR Guatemalan OR brasileiros OR brasileira OR brasileiro OR brasileiras OR brasileños OR SINASC OR DATASUS OR "Mato Grosso" OR Paraná OR "Rio Grande do Sul" OR Ceará OR "Santa Catarina" OR Goiás OR Bahia OR Pernambuco OR "Minas Gerais" OR "São Paulo" OR Nordeste OR "Northeast Brazil" OR Ceara OR Parana OR Goias OR "Sao Paulo" OR "Rio Grande do Norte" OR Piauí OR Piaui OR Maranhão OR Maranhao OR Tocantins OR "Espírito Santo" OR "América del Sur" OR "América do Sul" OR Sudamérica OR Latinoamérica OR Latinoamerica OR "Sul do Brasil" OR "Sur de Brasil")
```
`OA #4-v0` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:(#1-v0),title_and_abstract.search:(#2-v0),title_and_abstract.search:(#3-v0)   [#n-v0 = the #n string with its post-validation tail removed, as described in #1–#3]
```
`OA #4` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:(#1),title_and_abstract.search:(#2),title_and_abstract.search:(#3)
```
`OA #5` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:(#1-v0),title_and_abstract.search:(#2-v0),language:pt|es
```
`OA #6` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:("aerial spraying" OR "aerial fumigation" OR "aerial application" OR "aerial spray" OR "aerially sprayed" OR "crop dusting" OR "pulverização aérea" OR "aplicação aérea" OR "fumigación aérea" OR "fumigaciones aéreas" OR "aspersión aérea" OR "aspersiones aéreas" OR "aviação agrícola" OR "pulverizações aéreas" OR aeroagrícola OR aeroagricola OR "aerial spraying ban"),title_and_abstract.search:(health OR saúde OR salud OR exposure OR exposição OR exposición OR intoxication OR intoxicação OR intoxicación OR poisoning),title_and_abstract.search:(#3)
```
`OA #7a` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:("Chapada do Apodi" OR "Limoeiro do Norte" OR "Baixo Jaguaribe" OR Quixeré OR "Zé Maria do Tomé" OR "Dossiê ABRASCO" OR "Jaguaribe-Apodi" OR "Jaguaribe Apodi" OR "Chapada de Apodi" OR Quixere OR "Ze Maria do Tome" OR "Dossie ABRASCO"),title_and_abstract.search:(saúde OR health OR salud OR agrotóxicos OR agrotóxico OR agrotoxicos OR pesticides OR plaguicidas OR pesticidas OR agronegócio OR agribusiness OR fruticultura OR "pulverização aérea" OR adoecimento OR câncer OR cancer)
```
`OA #7b` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:(Apodi OR "Lower Jaguaribe" OR "Jaguaribe Valley" OR "Vale do Jaguaribe" OR "Tabuleiro de Russas" OR Russas OR Jaguaruana),title_and_abstract.search:(agrotóxicos OR agrotóxico OR agrotoxicos OR agrotoxico OR pesticides OR pesticidas OR plaguicidas OR agrochemicals OR agribusiness OR agronegócio OR agronegocio OR fruticultura OR "fruit farming" OR "fruit growing" OR "pulverização aérea" OR "perímetro irrigado" OR "perímetros irrigados" OR "irrigated perimeter")
```
`OA #8` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:(Ceará OR Ceara),title_and_abstract.search:(agrotóxicos OR agrotóxico OR agrotoxicos OR agrotoxico OR pesticides OR plaguicidas OR pesticidas OR "pulverização aérea" OR "aerial spraying" OR agrochemicals OR glyphosate OR glifosato OR fungicides)
```
`OA #9` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:("ADI 6137" OR "Zé Maria do Tomé" OR "Ze Maria do Tome" OR "proibição da pulverização aérea" OR "vedação da pulverização aérea" OR "aerial spraying ban" OR "ban on aerial spraying" OR "prohibition of aerial spraying" OR "aerial spraying prohibition" OR "prohibición de la fumigación aérea" OR "prohibición de las fumigaciones aéreas")
```
`OA #7-9 union` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:(((#7a block1) AND (#7a block2)) OR ((#7b block1) AND (#7b block2)) OR ((Ceará OR Ceara) AND (#8 block2)) OR (#9 block))
```
`OA #10` (OpenAlex, 2026-10-12):
```text
filter=title_and_abstract.search:(((#3) AND (((#1) AND (#2)) OR ((#6 aerial block) AND (#6 health block)))) OR (((#7a block1) AND (#7a block2)) OR ((#7b block1) AND (#7b block2)) OR ((Ceará OR Ceara) AND (#8 block2)) OR (#9 block)))
```
`OA #11` (OpenAlex, 2026-10-12):
```text
#10 OR #5 (export both and deduplicate by OpenAlex ID)
```
`SciELO #1 (S1')` (SciELO (search.scielo.org, all indices, , 2026-10-12):
```text
https://search.scielo.org/?q=(agrot* OR pesticid* OR plaguicid* OR praguicid* OR herbicid* OR fungicid* OR inseticid* OR insecticid* OR glifosato OR glyphosate OR agroquimic* OR agrochem* OR fumigacion* OR fumigat* OR "pulverização aérea" OR "aerial spraying") AND (nascer OR nacer OR birth* OR prematur* OR preterm OR pretermin* OR congenit* OR congênit* OR malforma* OR fetal OR fetais OR perinata* OR neonata* OR newborn* OR "recém-nascido*" OR "recién nacido*" OR "mortalidade infantil" OR "mortalidad infantil" OR "infant mortality" OR "mortalidade fetal" OR "mortalidad fetal" OR natimort* OR mortinat* OR obstetric* OR miscarriage* OR "aborto espontâneo" OR "aborto espontáneo" OR "spontaneous abortion")&lang=pt&count=50&output=site&format=summary  [URL-encode q]
```
`SciELO #2 (S2')` (SciELO, 2026-10-12):
```text
https://search.scielo.org/?q=(Apodi* OR Jaguaribe* OR Quixer* OR Russas* OR Jaguaruana*) AND (saúde* OR saude* OR health* OR salud* OR agrot* OR pesticid* OR agroneg* OR agribusiness* OR trabalh* OR fruticultura* OR mulheres*)&lang=pt&count=50&output=site&format=summary
```
`SciELO #3 (S2b)` (SciELO, 2026-10-12):
```text
https://search.scielo.org/?q=Ceara* AND (agrot* OR pesticid* OR plaguicid* OR "pulverização aérea")&lang=pt&count=50&output=site&format=summary
```
`SciELO #4 (S3)` (SciELO, 2026-10-12):
```text
https://search.scielo.org/?q=("pulverização aérea" OR "aplicação aérea" OR "aviação agrícola" OR "aerial spraying" OR "aerial application" OR "aerial fumigation" OR "fumigación aérea" OR "fumigaciones aéreas" OR "aspersión aérea" OR "aspersiones aéreas")&lang=pt&count=50&output=site&format=summary
```
`SciELO #5` (SciELO, 2026-10-12):
```text
#1 OR #2 OR #3 OR #4
```
`LILACS #1 (L1')` (LILACS via BVS portal (filter[db][]=LILA, 2026-10-12):
```text
https://pesquisa.bvsalud.org/portal/?lang=pt&q=((agrot* OR pesticid* OR plaguicid* OR praguicid* OR herbicid* OR fungicid* OR inseticid* OR insecticid* OR glifosato OR glyphosate OR agroquimic* OR fumiga*) AND (nascer OR nacer OR birth* OR prematur* OR preterm OR congenit* OR malforma* OR fetal OR perinata* OR neonata* OR newborn* OR "mortalidade infantil" OR "mortalidad infantil" OR "infant mortality" OR miscarriage* OR "aborto espontâneo" OR "aborto espontáneo")) OR ((mh:"Pesticides" OR mh:"Agrochemicals" OR mh:"Herbicides" OR mh:"Insecticides" OR mh:"Fungicides, Industrial" OR mh:"Agricultural Workers' Diseases") AND (mh:"Pregnancy Outcome" OR mh:"Infant, Low Birth Weight" OR mh:"Premature Birth" OR mh:"Congenital Abnormalities" OR mh:"Fetal Death" OR mh:"Abortion, Spontaneous" OR mh:"Infant Mortality" OR mh:"Stillbirth" OR mh:"Prenatal Exposure Delayed Effects"))&filter[db][]=LILACS  [URL-encode q]
```
`LILACS #2 (L2'')` (LILACS via BVS portal, 2026-10-12):
```text
https://pesquisa.bvsalud.org/portal/?lang=pt&q=(Apodi* OR Jaguaribe* OR Quixer* OR Russas* OR Jaguaruana* OR "Limoeiro do Norte" OR "pulverização aérea" OR "fumigación aérea" OR "aspersión aérea" OR "aerial spraying") AND (agrot* OR pesticid* OR plaguicid* OR saúde OR salud OR health OR trabalh*)&filter[db][]=LILACS
```
`LILACS #3 (L2b)` (LILACS via BVS portal, 2026-10-12):
```text
https://pesquisa.bvsalud.org/portal/?lang=pt&q=Ceara* AND (agrot* OR pesticid* OR plaguicid* OR "pulverização aérea")&filter[db][]=LILACS
```
`LILACS #4` (LILACS via BVS portal, 2026-10-12):
```text
#1 OR #2 OR #3
```

**O que entra na triagem:**

- OpenAlex: #11 = #10 (#4 OR #6 OR #7a OR #7b OR #8 OR #9; 1,591) OR #5 (language safety net, at most 149 extra). Total bounded at 1,591 to 1,740; deduplicate by OpenAlex ID.
- SciELO: #5 = S1' OR S2' OR S2b OR S3 (raw 187 + 157 + 47 + 67 = 458, with records repeated across collections).
- LILACS: #4 = L1' OR L2'' OR L2b (raw 418 + 125 + 24 = 567).
- Records from #7a, #7b, #8, #9, S2', S2b, L2'' and L2b carry the flag 'context'. #9 additionally carries 'Essay 2 (legal/policy)'. Records found only by #5 carry the flag 'language safety net'.

**Ordem de triagem:** Tier 1, full SQ1 eligibility screening first: any record in OpenAlex #4 or #6, SciELO S1' or S3, or LILACS L1'. These are effect and aerial-method records. Tier 2: records found only by OpenAlex #5 (PT/ES records with no Latin American place term). Screen titles quickly, because many will be studies from Spain or Portugal; screen the rest normally. Tier 3: records found only by the context lines (#7a, #7b, #8, #9, S2', S2b, L2'', L2b). Screen them against SQ1 eligibility as well, since some are effect studies (Rigotto 2013 is in both), but tag the remainder 'context' for Essay 1 background. #9 records are tagged 'Essay 2 legal/policy' whatever their SQ1 decision. Within each tier, deduplicate across databases before screening, giving priority to DOI, then OpenAlex ID, then title and year.

**Recall, desenvolvimento** (itens usados no ajuste; otimista por construção):

> Development-set recall uses items already seen in calibration or PRESS (optimistic by construction).
> 
> OpenAlex, tested by direct DOI filters on 2026-10-12:
> (a) #4-v0 (604), against 35 effect-type development items. These are the 3 effect seeds (Dias 2023, Calzada 2023, Camacho & Mejía 2017), the 7 calibration V items, the 9 calibration X items, Januzzi 2025, the 8 PRESS T16 items, and 7 more relevant PRESS T4/T10 items (Hervé 2016, Rouget 2019, Mato Grosso 2022, Mato Grosso 2024, Javeriana 2019, Mexico floriculture 2009, Paraná 2008 sex ratio). Result: 34/35. The only miss is Healthcare 2024 (10.3390/healthcare12202052), whose outcome is general health rather than a birth outcome. #6 retrieves it by set logic: #6 ⊇ calibration OA-3, which retrieved it in calibration row 96. It was not re-tested by DOI today. Dutra & Ferreira 2019 is now retrieved by #4-v0 through G4, where calibration needed the language branch.
> (b) Context union #7a ∪ #7b ∪ #8 ∪ #9, against 8 context development items: 8/8 by DOI test. They are Rocha 2017 (seed), Rigotto 2013, the Vale do Jaguaribe review (10.21680/2447-3359.2021v7n2id24607), Jaguaribe river pesticide fate (10.1007/s11368-016-1597-9), the ADI 6137 paper (10.26668/indexlawjournals/2526-0081/2023.v9i2.10012), childhood cancer in Ceará (10.22533/at.ed.92920110213), 10.54033/cadpedv22n7-345 and 10.18174/442443.
> (c) Overall: 4/4 orchestrator seeds and 42/42 distinct development items in the OpenAlex union (41 by direct DOI test, 1 by monotonicity). #4 (797) contains #4-v0, so these results carry over to it.
> 
> SciELO and LILACS were not re-tested today, to save Firecrawl credits. Every revised line contains its calibration line (S1' ⊇ S1, S2' ⊇ S2, L1' ⊇ L1, L2'' ⊇ L2), so the earlier retrievals carry over by monotonicity: SciELO had Dutra 2019, Oliveira 2014, Rigotto 2013, Cremonese 2012 (via pid), Venezuela 2008, Uruguay 2024 (PRESS T13) and Rocha 2017; LILACS had Rocha 2017 and Rigotto 2013.

**Recall, validação independente** (itens escolhidos antes do teste):

> Source and rule, fixed before any retrieval test. The fresh set came from the reference list of a recent review that neither calibration nor PRESS had mined: 'Pesticide Exposures during Pregnancy and Health Outcomes in Latin America and the Caribbean: A Scoping Review of Human Observational Studies' (10.1289/JHP1043, 2024, OpenAlex W4401700389). Its 156 OpenAlex-indexed references were pulled with filter=cited_by:W4401700389, titles only, sorted by year descending. The inclusion rule was applied to titles alone:
> (i) a primary human study;
> (ii) a Latin American or Caribbean setting evident from the title, or a Spanish/Portuguese title;
> (iii) a protocol primary or secondary outcome in the title (birth weight, size or anthropometry, gestational age or preterm birth, fetal loss or miscarriage, congenital anomalies);
> (iv) not explicitly occupational-only;
> (v) not already used in calibration or PRESS.
> The first 10 qualifying items, newest first, were taken. Honest caveat: the rule was written after seeing that titles-only list, but before any search test. Exclusions under (v) were the ISA birth cohort, Argentine Patagonia, Camacho, Rouget, Hervé, Kadhel and the Minas Gerais monoculture study (already development items), and the PROTECT glyphosate preterm study (10.1289/ehp7295), dropped because PRESS discussed it while revising G4.
> 
> Indexing: all 10 resolve by DOI in OpenAlex. One (I2) has abstract_inverted_index = null.
> 
> Results against the frozen PRESS-revised strategy (#4-v0, plus #5, #6 and the context arms):
> - I1. 10.1097/scs.0000000000009539 (cleft lip/palate, US vs Guatemala, 2023): MISSED. The abstract says 'congenital abnormalities' and 'orofacial clefts', which are not in O4. Pesticides appear only as 'agricultural chemical exposure' among several risk factors.
> - I2. 10.1016/j.chemosphere.2023.138790 (pregnant Argentinian women, 'anthropometric neonate parameters', 2023): MISSED. There is no O4 term ('neonate'/'anthropometric') and no abstract text in OpenAlex.
> - I3. 10.24875/rmn.22000067 (central nervous system malformations, Chiapas, 2023): retrieved.
> - I4. 10.1097/jom.0000000000002689 (periconceptional factors and cleft, Midwest Brazil, 2022): retrieved.
> - I5. 10.1017/s2040174422000277 (p,p'-DDE and birth anthropometry/gestational age, flower-growing region of Mexico, 2022): MISSED. Exposure is named only as 'p,p'-DDE'/'dichlorodiphenyldichloroethylene', which is not in E4. Under protocol rule (b), eligibility is doubtful because DDE has more than one source.
> - I6. 10.35563/rmp.v5i2.63 (congenital malformation in pesticide-exposed pregnant women, Ica, Peru, 2019): retrieved.
> - I7. 10.31698/ped.45012018002 (prenatal risk factors for malformations, Paraguayan hospital, 2018): MISSED by #4-v0, because the only geography term is 'América del Sur'. It is RETRIEVED by #5. This was inferred, not DOI-tested in #5: the record is language es, contains 'plaguicidas'/'agroquímicos' and 'malformaciones congénitas', and the geography delta (+1) is consistent with it.
> - I8. 10.1016/j.envres.2016.08.008 (maternal DDT/DDE and birth outcomes, Bolivia, 2016): retrieved.
> - I9. 10.1289/isee.2015.2015-2920 (pesticide use and perinatal outcomes, Brazil, ISEE 2015 abstract): retrieved. It is a conference abstract, which the protocol's status rule excludes.
> - I10. 10.1016/j.scitotenv.2013.01.034 (PON1 and miscarriage in pesticide-exposed Mexican women, 2013): retrieved. The exposure may be occupational.
> 
> Independent recall:
> - #4-v0 alone: 6/10.
> - Frozen PRESS-revised OpenAlex union (#4-v0 ∪ #5 ∪ #6 ∪ context arms): 7/10.
> - Among the 6 items with no evident eligibility doubt (I2, I3, I4, I6, I7, I8): 4/6 for #4-v0 and 5/6 for the union.
> 
> The misses come from three vocabulary gaps (anomaly wording, neonatal anthropometry, organochlorine names) and one geography gap. I closed them after validation (E, O and G additions, which turn #4-v0 into #4: +193 records, 797 in total). A direct DOI test showed #4 retrieves 4/4 of the misses. That 10/10 figure is development recall, not independent, because the additions were chosen from these misses. A new fresh set would be needed to validate #4 itself. SciELO and LILACS were not tested against this set.

**Volume:** Counted on 2026-10-12. OpenAlex: #10 = 1,591 unique, plus up to 149 from #5, so 1,591 to 1,740. SciELO: 458 raw records, which shrinks to roughly 250–320 once the same article is collapsed across collections (the calibration observed 1.5–2x duplication). LILACS: 567 raw. The cross-database total is my estimate, not a count: SciELO and LILACS overlap OpenAlex heavily for PT/ES effect studies, but S1' and L1' have no geography restriction, and LILACS holds grey literature that OpenAlex lacks. I expect about 2,000–2,300 unique records after deduplication. About 650–800 of them are context-flagged (OpenAlex context union 657, plus S2'/S2b/L2''/L2b) and about 1,300–1,500 come from the effect and aerial lines. This is above PRESS's OpenAlex estimate of 1,300–1,600. The difference is mainly the +193 post-validation additions and #5. At title/abstract stage it should take roughly 15–20 reviewer-hours.

**Mudanças da PRESS não aplicadas, e por quê:**

- *PRESS #7 as one string: all new place names (including bare Russas and Apodi) AND a co-term block that also contains generic 'saúde OR health OR mulheres'.* — PRESS's own T6 showed that generic health co-terms on the new place names give 481 delta records, with Limoeiro-PE and Staraya Russa noise; the pesticide-anchored version (T7) gave 88. The arm was therefore split: #7a keeps the OA-4 co-terms for the established Chapada/Baixo Jaguaribe phrases, and #7b uses pesticide/agribusiness co-terms for the new names. Both Rocha 2017 and Rigotto 2013 are retrieved.
- *PRESS LILACS L2' = L2 with Ceara* added to the place-name block.* — Tested on 2026-10-12: 3,067 LILACS records, because Ceara* AND (saúde OR health OR ...) catches the whole Ceará health literature. It was replaced by L2'' (Russas* and Jaguaruana* only, 125) plus L2b = Ceara* AND pesticide terms (24), which mirrors SciELO S2b.
- *'16.820' in the legal/policy arm.* — Dropped as PRESS recommended. It added about 30 unrelated chemistry and numeric records (63 with it against 33 without).
- *Bare fungicidas/herbicidas/insecticidas/fitosanitarios in the OpenAlex exposure block.* — PRESS T2 showed agronomy noise from these terms, and PRESS itself advised against them.
- *Broad outcome terms: 'prenatal exposure', 'in utero', 'maternal exposure', 'child health', 'reproductive health', 'malformaciones'.* — PRESS T3 found 151 records, mostly off-target (neurodevelopment, leukaemia, sperm, rat studies). Rejected by PRESS.
- *pulveriz* in SciELO S1'.* — PRESS T12 found it pulls in Ciência Rural and veterinary agronomy noise.
- *Language branch (OA-2) as a primary recall device.* — OpenAlex language metadata is incomplete (null for some PT records; multilingual SciELO records are tagged 'en'). G4 now carries the geography. The branch survives only as the supplementary line #5.
- *Optional PRESS sensitivity lines: the SciELO kw: author-keyword field and an OpenAlex topics/concepts filter.* — Not tested. Parallel web_fetch returned HTTP 429 on every attempt, and Firecrawl credits are low, so they were left out rather than frozen untested.
- *Carrying the post-validation E, O and G additions over to SciELO S1' and LILACS L1' (organoclor*, DDT, DDE, neonat*, cleft*).* — Not tested in those portals, for the same credit and rate-limit reasons, so they were not frozen there. S1' and L1' already cover congenit*, malforma* and neonata*; the organochlorine names are the real gap. This is a recommended next amendment.

**Problemas e limites registrados:**

- Tooling: Parallel web_fetch returned HTTP 429 on every one of the 5 attempts, so all OpenAlex, SciELO and BVS calls went through Firecrawl scrape (about 40 credits). Firecrawl reports that the account is low on credits; the user should add credits before the main search run.
- Independent validation exposed real vocabulary gaps (6/10 for #4-v0; 7/10 with the language safety net). The amended #4 recovers all four misses, but that was not independently validated. A second fresh set, for example from the reference list of 10.1289/ehp9934 (313 references, not used here), is needed to estimate the recall of #4 without bias.
- The independent-set rule was applied to titles after seeing the titles-only reference list, though before any retrieval test. 3–4 of the 10 items have doubtful eligibility under the protocol (DDE biomonitoring, possibly occupational exposure, a conference abstract).
- The OpenAlex blocks #1–#3 were not counted on their own. #11 (#10 OR #5) cannot be counted in one OpenAlex call because a language filter cannot be ORed with a search filter; it is given as the bound 1,591–1,740.
- Healthcare 2024 counts as retrieved by #6 by monotonicity (#6 ⊇ calibration OA-3). It was not DOI-tested today. SciELO and LILACS development recall rests on monotonicity, and the independent items were not tested there.
- LILACS counts were read from the LILACS facet on the BVS results page, with no parsed query echo. SciELO counts are record-level and include the same article in several collections.
- The OpenAlex PT/ES terms are accented only (for example 'malformações congênitas', 'óbito fetal', 'recém-nascidos'). OpenAlex does not fold accents, so abstracts written without accents could be missed. Unaccented outcome variants were not proposed by PRESS and were not tested.
- #5 (language safety net) will bring in Spain and Portugal studies (149 records outside G4). The screening rule assigns them to a fast-title tier.
- Every count is a 2026-10-12 snapshot and OpenAlex changes over time. For audit, the PRESS T19 count (604) was reproduced exactly today.
- docs/revisao-sistematica/apendice-a-estrategias.md still shows the PRESS recommended_final_query as the frozen SQ1-AL strategy. It should be updated to these numbered lines, with the context arm split, L2' replaced by L2''/L2b and the post-validation #4 noted. I did not edit the appendix or protocolo.md.

---

## SQ2 — revisão estruturada complementar: método

**Fonte:** rodada de finalização (`-final.json`), que aplica a PRESS e congela as linhas.

| linha | base | contagem | descrição |
|---|---|---:|---|
| #1 | OpenAlex (/works) | 356 | (a) Continuous or multi-valued DiD and dose-response: PRESS string A2, subfield-filtered. Re-run in this session. The OQL echo matched: 6 DiD terms AND 16 dose terms, all stemmed phrases. |
| #2 | OpenAlex (/works) | 447 | (b) Misclassified or mismeasured treatment: PRESS string B_v2, subfield-filtered. The count comes from PRESS call R5 on the same date and was not re-run alone here. Its parse was verified inside the #5/#6 OQL echo. |
| #3 | OpenAlex (/works) | 1.933 | (c) Inference with few treated or control clusters: PRESS string C_v3-lean, subfield-filtered. The count comes from PRESS call R11 on the same date and was not re-run alone here. Its parse was verified inside the #5/#6 OQL echo. |
| #4 | OpenAlex (/works) | 1.244 | (d) Synthetic control, SDID and factor/matrix-completion counterfactual estimators with few units: PRESS string D3, subfield-filtered. The count comes from PRESS call R18 on the same date and was not re-run alone here. Its parse was verified inside the #5/#6 OQL echo. |
| #5 | OpenAlex (/works) | 3.840 | #1 OR #2 OR #3 OR #4 in one call, subfield-filtered. Re-run in this session as the unfiltered union with group_by=primary_topic.subfield.id&per-page=200. The four subfields give 2613: 1,988; 2002: 1,395; 2000: 300; 1804: 157; total 3,840. This equals the PRESS single-call R21. For context, the same string unfiltered returns 18,159. |
| #6 | OpenAlex (/works) | 1.824 | PRESS second run: the same search string as #5, with topics.id:T10845 (Advanced Causal Inference Techniques, among any of a work's topics) in place of the subfield filter. Run in this session with group_by=primary_topic.subfield.id. Total 1,824 across 50 subfield groups, and the groups sum exactly to 1,824, so no record lacks a primary topic. 1,663 fall in 2613, 2002, 1804 or 2000 (1,509 + 140 + 12 + 2). Because the search string is the same, those 1,663 are already in #5. |
| #7 | OpenAlex (/works) | 161 | #6 NOT #5: the T10845-run records whose primary subfield is outside 2002, 2613, 2000 and 1804. These are the only records the second run adds. The count 161 = 1,824 - 1,663 comes from the #6 group_by. This verbatim negation-filter query was prepared but NOT executed directly, because the tools were blocked. Largest groups: Sociology & Political Science 23, Epidemiology 15, Safety/Risk 13, AI 9, Management Science 8, General Health Professions 8, Health Information Management 8. |
| #8 | OpenAlex | 4.001 | #5 OR #6, unioned by OpenAlex ID: 4,001 = 3,840 + 161. This is exact set algebra: the search string is identical, so #5 ∩ #6 is the set of #6 records with a primary subfield in the four-subfield filter. The T10845 run adds 4.2%. One filter value cannot express subfield OR topic, so export #5 and #7 and concatenate them; no further deduplication is needed between the two. |
| #9 | OpenAlex (/works) | 108 | (e) Formula and shift-share instruments: calibration string E6, restricted to topics.id:T10845, unchanged. Count from calibration order 60. A re-run today was blocked (Firecrawl had no credits; Parallel returned 429). |
| #10 | OpenAlex (/works) | 119 | (e) Citation-chasing arm, unchanged: forward citations of 5 GAEZ/suitability design anchors (Nunn-Qian 2011, Bustos et al. 2016, Costinot et al. 2016, DRS 2023, Reynier-Rubin 2025), intersected with suitability/GM vocabulary. All forward citations together number 1,709. Count from calibration order 69; re-run blocked. |
| #11 | OpenAlex (/works) | 29 | (e) GAEZ keyword arm, unchanged and unfiltered. A small, precise complement. Count from calibration order 52; re-run blocked. |
| #12 | OpenAlex (/works) | 8 | Known items forced in, as PRESS recommended plus two backstops. AKM 2019 is missed by E6 because it has no T10845 tag. DRS 2023 has no suitability vocabulary in its abstract, has primary subfield 1110, and is a #10 anchor that cannot cite itself. The other four #10 anchors are included for the same reason. Kreider et al. 2012 sits in subfield 3600 and is lost by #2 (its T10845 tag was not verified). Imbens-Kolesár 2016 is the only (c) miss of C_v3-lean. Each DOI was confirmed indexed in calibration or PRESS (orders 61 and 68; PRESS R1 and R22) but was not re-checked today. |
| #13 | OpenAlex | — | FINAL OpenAlex set: #8 OR #9 OR #10 OR #11 OR #12, unioned by OpenAlex ID. The gross upper bound is 4,001 + 108 + 119 + 29 + 8 = 4,265. The exact overlap among the (e) arms, the known items and #8 was NOT measured, because the tools were blocked. Calibration found that the (e) arms overlap little with (a)-(d). Deduplicate by OpenAlex ID, then collapse preprint, SSRN, NBER and journal versions. |
| #14 | arXiv/PubMed research index (firecrawl_r | — | Preprint supplement, unchanged from calibration. Ranked top-k lists with no totals. Recovers arXiv-only items that OpenAlex lacks, such as 2507.20415. |
| #15 | Wiley Scholar Gateway | 25 | Full-text passage supplement for Wiley journals (JAE, Econometrics Journal before 2019, CJE). Unchanged. The count is 25 passages, not records. |
| #16 | Web (Parallel search: NBER/SSRN/RePEc/IZ | — | Grey-literature supplement, unchanged. Screen the top results only. |

**Strings exatas, prontas para rodar:**

`#1` (OpenAlex (/works), 2026-10-12):
```text
filter=primary_topic.subfield.id:2002|2613|2000|1804,title_and_abstract.search:("difference in differences" OR "event study" OR "two-way fixed effects" OR "parallel trends" OR "changes in changes" OR TWFE) AND ("continuous treatment" OR "treatment intensity" OR "intensity of treatment" OR "dose-response" OR dosage OR "multi-valued treatment" OR "multivalued treatment" OR "non-binary treatment" OR "heterogeneous adoption" OR "treatment dose" OR stayers OR fuzzy OR "treatment rate" OR "continuously distributed" OR "exposure intensity" OR "continuous exposure")
```
`#2` (OpenAlex (/works), 2026-10-12 (PRESS R5)):
```text
filter=primary_topic.subfield.id:2002|2613|2000|1804,title_and_abstract.search:(("difference in differences" OR "parallel trends" OR "event study" OR "treatment effect" OR "treatment effects" OR "causal effect" OR "policy evaluation" OR "program evaluation" OR "binary regressor" OR "treatment status" OR "treatment indicator" OR "program participation") AND (misclassification OR misclassified OR misreporting OR misreported OR "mismeasured treatment" OR "mismeasured binary" OR "measurement error in treatment" OR "treatment measurement error")) OR (("difference in differences" OR "parallel trends" OR "event study" OR "binary regressor" OR "treatment status" OR "treatment indicator") AND ("measurement error" OR "errors in variables" OR mismeasured OR mismeasurement))
```
`#3` (OpenAlex (/works), 2026-10-12 (PRESS R11)):
```text
filter=primary_topic.subfield.id:2002|2613|2000|1804,title_and_abstract.search:(("few clusters" OR "few treated" OR "few control" OR "few untreated" OR "few groups" OR "small number of clusters" OR "small number of groups" OR "small number of treated" OR "small number of control" OR "small number of policy changes" OR "finite number of clusters" OR "single treated" OR "one treated" OR "unbalanced clusters" OR "clustered errors" OR "cluster bootstrap" OR "wild cluster bootstrap" OR "wild bootstrap" OR "randomization inference" OR "permutation inference" OR "conformal inference" OR "cluster-robust" OR "heterogeneous clusters" OR "randomization tests" OR "clustered standard errors") AND ("difference in differences" OR cluster OR clusters OR clustered OR "policy change" OR "policy changes" OR "few treated" OR "synthetic control")) OR (("number of clusters" OR "number of groups" OR "number of states") AND ("difference in differences" OR "standard errors" OR "t-statistic" OR "cluster-robust"))
```
`#4` (OpenAlex (/works), 2026-10-12 (PRESS R18)):
```text
filter=primary_topic.subfield.id:2002|2613|2000|1804,title_and_abstract.search:(("synthetic control" OR "synthetic controls" OR "synthetic difference in differences" OR "synthetic DiD") AND (inference OR estimator OR estimators OR estimation OR "few treated" OR "single treated" OR "small number" OR permutation OR placebo OR conformal OR "bias correction" OR identification OR "research design")) OR (("panel data approach" OR "panel data method" OR "matrix completion" OR "interactive fixed effects") AND (counterfactual OR counterfactuals OR "program evaluation" OR "policy evaluation" OR "treatment effect" OR "treatment effects" OR "causal effect"))
```
`#5` (OpenAlex (/works), 2026-10-12):
```text
filter=primary_topic.subfield.id:2002|2613|2000|1804,title_and_abstract.search:(("difference in differences" OR "event study" OR "two-way fixed effects" OR "parallel trends" OR "changes in changes" OR TWFE) AND ("continuous treatment" OR "treatment intensity" OR "intensity of treatment" OR "dose-response" OR dosage OR "multi-valued treatment" OR "multivalued treatment" OR "non-binary treatment" OR "heterogeneous adoption" OR "treatment dose" OR stayers OR fuzzy OR "treatment rate" OR "continuously distributed" OR "exposure intensity" OR "continuous exposure")) OR ((("difference in differences" OR "parallel trends" OR "event study" OR "treatment effect" OR "treatment effects" OR "causal effect" OR "policy evaluation" OR "program evaluation" OR "binary regressor" OR "treatment status" OR "treatment indicator" OR "program participation") AND (misclassification OR misclassified OR misreporting OR misreported OR "mismeasured treatment" OR "mismeasured binary" OR "measurement error in treatment" OR "treatment measurement error")) OR (("difference in differences" OR "parallel trends" OR "event study" OR "binary regressor" OR "treatment status" OR "treatment indicator") AND ("measurement error" OR "errors in variables" OR mismeasured OR mismeasurement))) OR ((("few clusters" OR "few treated" OR "few control" OR "few untreated" OR "few groups" OR "small number of clusters" OR "small number of groups" OR "small number of treated" OR "small number of control" OR "small number of policy changes" OR "finite number of clusters" OR "single treated" OR "one treated" OR "unbalanced clusters" OR "clustered errors" OR "cluster bootstrap" OR "wild cluster bootstrap" OR "wild bootstrap" OR "randomization inference" OR "permutation inference" OR "conformal inference" OR "cluster-robust" OR "heterogeneous clusters" OR "randomization tests" OR "clustered standard errors") AND ("difference in differences" OR cluster OR clusters OR clustered OR "policy change" OR "policy changes" OR "few treated" OR "synthetic control")) OR (("number of clusters" OR "number of groups" OR "number of states") AND ("difference in differences" OR "standard errors" OR "t-statistic" OR "cluster-robust"))) OR ((("synthetic control" OR "synthetic controls" OR "synthetic difference in differences" OR "synthetic DiD") AND (inference OR estimator OR estimators OR estimation OR "few treated" OR "single treated" OR "small number" OR permutation OR placebo OR conformal OR "bias correction" OR identification OR "research design")) OR (("panel data approach" OR "panel data method" OR "matrix completion" OR "interactive fixed effects") AND (counterfactual OR counterfactuals OR "program evaluation" OR "policy evaluation" OR "treatment effect" OR "treatment effects" OR "causal effect")))
```
`#6` (OpenAlex (/works), 2026-10-12):
```text
filter=topics.id:T10845,title_and_abstract.search:(("difference in differences" OR "event study" OR "two-way fixed effects" OR "parallel trends" OR "changes in changes" OR TWFE) AND ("continuous treatment" OR "treatment intensity" OR "intensity of treatment" OR "dose-response" OR dosage OR "multi-valued treatment" OR "multivalued treatment" OR "non-binary treatment" OR "heterogeneous adoption" OR "treatment dose" OR stayers OR fuzzy OR "treatment rate" OR "continuously distributed" OR "exposure intensity" OR "continuous exposure")) OR ((("difference in differences" OR "parallel trends" OR "event study" OR "treatment effect" OR "treatment effects" OR "causal effect" OR "policy evaluation" OR "program evaluation" OR "binary regressor" OR "treatment status" OR "treatment indicator" OR "program participation") AND (misclassification OR misclassified OR misreporting OR misreported OR "mismeasured treatment" OR "mismeasured binary" OR "measurement error in treatment" OR "treatment measurement error")) OR (("difference in differences" OR "parallel trends" OR "event study" OR "binary regressor" OR "treatment status" OR "treatment indicator") AND ("measurement error" OR "errors in variables" OR mismeasured OR mismeasurement))) OR ((("few clusters" OR "few treated" OR "few control" OR "few untreated" OR "few groups" OR "small number of clusters" OR "small number of groups" OR "small number of treated" OR "small number of control" OR "small number of policy changes" OR "finite number of clusters" OR "single treated" OR "one treated" OR "unbalanced clusters" OR "clustered errors" OR "cluster bootstrap" OR "wild cluster bootstrap" OR "wild bootstrap" OR "randomization inference" OR "permutation inference" OR "conformal inference" OR "cluster-robust" OR "heterogeneous clusters" OR "randomization tests" OR "clustered standard errors") AND ("difference in differences" OR cluster OR clusters OR clustered OR "policy change" OR "policy changes" OR "few treated" OR "synthetic control")) OR (("number of clusters" OR "number of groups" OR "number of states") AND ("difference in differences" OR "standard errors" OR "t-statistic" OR "cluster-robust"))) OR ((("synthetic control" OR "synthetic controls" OR "synthetic difference in differences" OR "synthetic DiD") AND (inference OR estimator OR estimators OR estimation OR "few treated" OR "single treated" OR "small number" OR permutation OR placebo OR conformal OR "bias correction" OR identification OR "research design")) OR (("panel data approach" OR "panel data method" OR "matrix completion" OR "interactive fixed effects") AND (counterfactual OR counterfactuals OR "program evaluation" OR "policy evaluation" OR "treatment effect" OR "treatment effects" OR "causal effect")))
```
`#7` (OpenAlex (/works), 2026-10-12 (derived from #6 group_by)):
```text
filter=topics.id:T10845,primary_topic.subfield.id:!2002,primary_topic.subfield.id:!2613,primary_topic.subfield.id:!2000,primary_topic.subfield.id:!1804,title_and_abstract.search:<the #5 search string, verbatim>
```
`#8` (OpenAlex, 2026-10-12):
```text
#5 ∪ #7 (export both calls; concatenate)
```
`#9` (OpenAlex (/works), 2026-10-11 (calibration; not re-run)):
```text
filter=topics.id:T10845,title_and_abstract.search:("shift-share" OR "shift share" OR "Bartik" OR "formula instrument" OR "formula instruments" OR "known formula" OR "simulated instrument" OR "simulated instruments" OR "exposure design" OR "exposure designs" OR "recentered instrument" OR "recentering" OR "exogenous shocks") AND ("instrumental variable" OR "instrumental variables" OR "instrument" OR "instruments" OR "inference" OR "standard errors" OR "research design" OR "research designs" OR "regression designs" OR "design-based")
```
`#10` (OpenAlex (/works), 2026-10-11 (calibration; not re-run)):
```text
filter=cites:W2166670725|W3122076865|W2299445035|W3124792110|W4406357681,title_and_abstract.search:suitability OR suitable OR "GAEZ" OR "potential yield" OR "potential yields" OR "attainable yield" OR "agro-ecological" OR agroclimatic OR "agro-climatic" OR "genetically modified" OR "genetically engineered"
```
`#11` (OpenAlex (/works), 2026-10-11 (calibration; not re-run)):
```text
filter=title_and_abstract.search:("GAEZ" OR "Global Agro-Ecological Zones" OR "agroclimatic suitability" OR "agro-climatic suitability" OR "crop suitability" OR "potential yield" OR "potential yields" OR "attainable yield" OR "soil suitability" OR "agricultural suitability") AND ("instrumental variable" OR "instrumental variables" OR "exogenous variation" OR "difference in differences" OR "identification strategy" OR "causal effect" OR "shift-share")
```
`#12` (OpenAlex (/works), 2026-10-12 (list fixed; indexing per calibration/PRESS)):
```text
filter=doi:10.1093/qje/qjz025|10.1093/restud/rdad011|10.1093/qje/qjr009|10.1257/aer.20131061|10.1086/684719|10.1073/pnas.2413013121|10.1080/01621459.2012.682828|10.1162/rest_a_00552
```
`#13` (OpenAlex, 2026-10-12):
```text
#5 ∪ #7 ∪ #9 ∪ #10 ∪ #11 ∪ #12 (dedupe by OpenAlex ID)
```
`#14` (arXiv/PubMed research index (firecrawl_r, 2026-10-11 (calibration)):
```text
4 natural-language framings: continuous-treatment DiD [econ.EM, k=100]; misclassified treatment in DiD [econ.EM, k=60]; few treated or control clusters inference [k=60]; SC/SDID with few units [econ.EM, k=50]
```
`#15` (Wiley Scholar Gateway, 2026-10-11 (calibration)):
```text
misclassified DiD (topN 15); few-cluster wild bootstrap and RI (topN 10)
```
`#16` (Web (Parallel search: NBER/SSRN/RePEc/IZ, 2026-10-11 (calibration)):
```text
site:nber.org | site:ideas.repec.org | site:ssrn.com | site:iza.org with continuous-treatment DiD, misclassification DiD, few treated clusters, and GAEZ instrument terms (3 calls, 12 queries)
```

**O que entra na triagem:**

- OpenAlex: #13 = #5 ∪ #7 ∪ #9 ∪ #10 ∪ #11 ∪ #12, deduplicated by OpenAlex ID and then by version. Lines #1-#4 are per-arm audit lines and #6 is the T10845 run before differencing; none of these is screened separately.
- arXiv/PubMed research index: #14, the top-k lists, deduplicated against #13.
- Wiley Scholar Gateway: #15, articles behind the 25 passages, deduplicated against #13.
- Web grey literature: #16, top results only, deduplicated against #13.

**Ordem de triagem:** This follows the protocol for SQ2: one AI screener, OpenAlex relevance order, stopping after 200 consecutive exclusions once at least 30% of the set is screened, with 10% double-screening and a 5% tail audit. Because #13 is a union of separate calls, relevance scores are not comparable across lines. Proposed order:
(1) the #12 known items, always screened in full;
(2) the (e) arms #9, #10 and #11 (256 records, small and heterogeneous), screened in full;
(3) #7, the 161 T10845-only records outside the economics and statistics subfields, screened in full;
(4) #5 exported with sort=relevance_score:desc, with the stopping rule applied only within #5 and its 30% floor computed on #5 (3,840, so at least 1,152);
(5) the arXiv (#14), Wiley (#15) and web (#16) supplements, screened in their own rank order after deduplication.
The 5% tail audit samples the unscreened part of #5. Steps (2) and (3) are a proposal consistent with protocolo.md, not a protocol change, and the researcher should confirm them.

**Recall, desenvolvimento** (itens usados no ajuste; otimista por construção):

> This is development-set (tuning) recall. It is circular, because these items shaped or revised the strings. It could NOT be re-verified by a DOI call today: OpenAlex became unreachable after 4 calls. The figures are PRESS's results for exactly the adopted strings, run on 2026-10-12.
> 
> (a), A2: 5/7. The misses are dCDH AER 2020 (10.1257/aer.20181169) and the dCDH survey (10.1093/ectj/utac017). Both are binary-treatment heterogeneity papers, recorded as out of scope for (a) by decision (CLAUDE.md classes them as conceptual references). In-scope recall is 5/5: CGS NBER and arXiv, dCDH 2201.06898, Fuzzy DiD rdx049 and DHS JoE.
> 
> (b), B_v2: 7/8. The miss is Kreider et al. 2012 (10.1080/01621459.2012.682828), whose primary subfield is 3600 and so falls outside the filter. Whether the T10845 run (#7) recovers it was not verified. It is now forced in as a known item (#12).
> 
> (c), C_v3-lean: 14/15. The miss is Imbens-Kolesár 2016 (10.1162/rest_a_00552), whose abstract has only 'robust standard errors' and 'clusters'. It is now a known item (#12).
> 
> (d), D3: 8/8.
> 
> Union (a)-(d), search only: at least 34/38 = 89%, or 34/36 = 94% in scope. With the #12 known items, in-scope coverage is 36/36.
> 
> Calibration seeds: 11/11 for (a)-(d). This holds by monotonicity, not by a re-run. Each revised arm only adds OR terms to the calibrated arm, and C_v2's 'cluster-robust inference' and D2's 'single treated unit' are subsumed by 'cluster-robust' and 'single treated'. With the same filter, the revised union is therefore a superset of the calibrated union of 2,416.
> 
> (e): E6 retrieves 4/5 shift-share anchors (Borusyak-Hull review utae003, BHJ rdab030, GPSS aer.20181047, BH ecta19367). AKM was missed and is now a #12 known item. The GAEZ application anchors are 0/5 by keyword (calibration). They enter only as #10 cites anchors or #12 known items, by construction, and that is not search recall. DRS 2023 is a #12 known item.

**Recall, validação independente** (itens escolhidos antes do teste):

> Selection rule, stated and applied before any testing. Items come from the reference lists, or the citers, of three sources in the Firecrawl research index's citation graph:
> (i) the references of Roth, Sant'Anna, Bilinski & Poe 2023, 'What's trending in difference-in-differences?' (arXiv 2201.01194; JoE 10.1016/j.jeconom.2023.03.008), with 35 indexed references;
> (ii) the references of Negi & Negi (arXiv 2208.02412), with 5 indexed references;
> (iii) the citers of Borusyak, Hull & Jaravel (arXiv 1806.01221), with 23 indexed citers.
> From these I kept every item whose title and abstract make it a methods contribution under SQ2 (a)-(e), and dropped any item that appears anywhere in sq2-metodo.json or sq2-metodo-press.json, which I checked by grep. Ranking intents were generic for (i) and (ii) and topical for (iii). For (b), the citers of Denteh-Kédagni returned only non-eligible items.
> 
> The 9 items selected:
> 1. (a) dCDH, 'DiD Estimators of Intertemporal Treatment Effects', arXiv 2007.04267.
> 2. (c) MacKinnon, Nielsen & Webb, 'Cluster-Robust Inference: A Guide to Empirical Practice', arXiv 2205.03285 (JoE 10.1016/j.jeconom.2022.04.001).
> 3. (c) 'Randomization Tests in Observational Studies with Staggered Adoption of Treatment', arXiv 1912.10610. This one is borderline for (c).
> 4. (d) Liu, Wang & Xu, 'A Practical Guide to Counterfactual Estimators for TSCS Data', arXiv 2107.00856.
> 5. (b) 'Heterogeneous Treatment Effects with Mismeasured Endogenous Treatment', arXiv 1511.04162.
> 6. (b) 'Identifying the effect of a mis-classified, binary, endogenous regressor', arXiv 2011.07272.
> 7. (e) 'Randomization Inference Tests for Shift-Share Designs', arXiv 2206.00999.
> 8. (e) 'Estimating Demand with Recentered Instruments', arXiv 2504.04056.
> 9. (e) 'On the Use of Design-Based Simulations', arXiv 2603.11381.
> Excluded at selection: 1907.01049 and 2010.04076 (already in the calibration file), 1710.02926 (whether to cluster, not few clusters), 2512.14616 (a misclassified dependent variable), staggered binary-timing papers, and pretest or sensitivity papers outside (a)-(e).
> 
> Indexing check: NOT DONE. The OpenAlex DOI call for these 11 DOIs (arXiv plus 2 journal DOIs) failed with HTTP 429 three times, so indexing is unknown. Arxiv-only items can be absent from OpenAlex; 2507.20415 is an example.
> 
> Retrieval test in OpenAlex: NOT DONE, for the same reason. As a substitute I ran an OFFLINE EMULATION, explicitly not OpenAlex retrieval. The emulator applies the exact boolean strings to each item's arXiv title and abstract from the research index, with lower-casing, hyphen treated as space, and light inflectional stemming only. It reproduced three known PRESS outcomes: the D2 vs D3 'estimation' miss and hit, Imbens-Kolesár missed by C3, and Ibragimov-Müller hit via 'heterogeneous clusters'.
> 
> Emulated string-match result: 7/9 (78%).
> - Matches: item 1 by #1 ('treatment dose', 'parallel trends' and 'event study'); item 2 by #3 ('cluster-robust'); item 3 by #3 and #4 ('randomization tests' plus 'synthetic control'); item 4 by #4 ('interactive fixed effects' plus 'counterfactual'); items 7-9 by #9 ('shift-share' or 'recentered instruments' plus inference or instrumental variables).
> - MISSES, both in (b), so (b) is 0/2. Item 5 says 'binary treatment is mismeasured' and 'mismeasured endogenous treatment'. The single word mismeasured sits only in B_v2's second arm, which requires DiD, binary-regressor or treatment-status context, and 'treatment effect' appears only in the first arm. Item 6 uses the hyphenated 'mis-classified', which tokenises to 'mis classified' and does not match misclassified. Its phrase 'binary, endogenous regressor' also breaks 'binary regressor'.
> 
> Caveats: true OpenAlex recall is at most this figure. Retrieval also needs (1) OpenAlex indexing; (2) for items 1-6, a primary subfield in the four or a T10845 tag; for items 7-9, a T10845 tag, which #9 requires and which the 2026 preprint may lack; and (3) an OpenAlex abstract that matches the arXiv version.
> 
> The (b) gap confirms PRESS's concern about the misclassification vocabulary. An amendment was derived but NOT adopted, because adopting it would contaminate this validation and its volume is untested. It would add to B_v2's first-arm error block: mismeasured OR "mis-classified" OR "mis-classification" OR "mis-measured" OR "mis-reported"; and to its context block: "endogenous regressor" OR "binary treatment". Offline, it catches both items.

**Volume:** OpenAlex gross: #8 = 4,001, an exact by-ID union verified today (3,840 subfield-filtered plus 161 T10845-only). Adding the (e) arms at 256 (calibration counts 108 + 119 + 29) and 8 known items gives an upper bound of 4,265 before overlap. Overlap between (e), the known items and #8 is small but unmeasured.

After version deduplication I expect roughly 3,400-3,800 unique works for title/abstract screening. The calibration showed heavy preprint, SSRN, NBER and journal duplication: CGS has 3 records, MacKinnon-Webb RI has 4, and 627 of the earlier 2,416 were dated 2026. Applying the calibration's ratio of about 0.79-0.90 to 4,265 gives about 3,370-3,840.

Add about 100-200 new items from the arXiv top-k lists (#14) and a few dozen grey-literature records (#16).

Compared with the pre-PRESS strategy (about 2,670 gross), this is about +60%. Most of the increase comes from (c): 1,933 against 1,025. Under the protocol's stopping rule (200 consecutive exclusions after at least 30% screened), at least about 1,100-1,300 records will actually be screened.

**Mudanças da PRESS não aplicadas, e por quê:**

- *An optional (f) arm for parallel-trends pretesting, sensitivity and anticipation, for example ("parallel trends" OR "pre-trends" OR "pretrends" OR "pre-trend") AND (test OR testing OR sensitivity OR "no anticipation" OR anticipation).* — Eligibility for SQ2 is fixed to (a)-(e) in protocolo.md, which this task may not edit, and PRESS left the count untested. Following PRESS's alternative, this literature (for example Rambachan & Roth 2023, 10.1093/restud/rdad018, and Roth's pretest paper) is left to known-item and citation chasing. Whether to add (f) is flagged for the researcher, because the project's SPT pre-trend test and its three anticipation dates depend on it.
- *C_v3-broad: add "robust standard errors", "permutation test(s)" and "randomization test" to the first (c) arm, and "hypothesis testing" and "panel data" to the second.* — It costs +467 records (2,400 against 1,933) to recover one validation item, Imbens-Kolesár 2016, which #12 now recovers at no volume cost. The task specified C_v3-lean.
- *Adding AKM 2019 as a cites: anchor in the (e) citation-chasing arm.* — PRESS offered 'anchor or known item'. That arm filters on suitability and GM vocabulary, which has nothing to do with shift-share inference, so AKM's citers would match mostly by chance. The known-item option guarantees the paper itself. Not tested.
- *Re-running the per-arm counts for #2-#4 and the (e) arms #9-#11 today, plus a direct run of the #7 negation-filter query.* — Blocked. Firecrawl reported insufficient credits after 4 successful OpenAlex calls; the account is out of credits and the user should add more. Parallel web_fetch returned HTTP 429 on about 10 attempts spaced over about 25 minutes. WebFetch has no DNS for api.openalex.org, and direct curl got a proxy 403. So #2-#4 carry PRESS counts from the same date, #9-#11 carry calibration counts from 2026-10-11, and #7 is derived exactly from the #6 group_by.
- *An exact by-ID union of the (e) arms and known items with #8 (the final #13 count).* — Same blocker. Reported as an upper bound of 4,265 before overlap.
- *Per-arm T10845 counts for #1-#4.* — Not needed for the by-ID union, which only requires the union-level T10845 run that was done, and blocked anyway.
- *A B-arm amendment from the independent validation: hyphenated mis- forms ('mis-classified', 'mis-measured', 'mis-reported', 'mis-classification'), the single word mismeasured in the treatment-effect arm, and 'endogenous regressor' or 'binary treatment' as context.* — It was derived from the independent validation set, so adopting it now would contaminate that validation, and its volume is untested because OpenAlex was unreachable. It is recommended for a researcher decision and a count before the strategy is registered.

**Problemas e limites registrados:**

- TOOLING: OpenAlex was reachable for only 4 calls this session, all through Firecrawl: #1, the unfiltered union grouped by subfield, and #6 grouped by subfield. After that, Firecrawl reported 'Insufficient credits'; tell the user to add Firecrawl credits. Parallel web_fetch returned 'Too Many Requests' on every attempt, including after waits of 90, 180, 240 and 300 seconds, even though Parallel web_search worked. WebFetch fails DNS for api.openalex.org and export.arxiv.org. Direct curl gets 'CONNECT tunnel failed, response 403'. The Firecrawl research-index tools still worked and were used to select the independent validation items.
- COUNT PROVENANCE: re-run today with the OQL echo checked are #1 (356), #5 (3,840, via the group_by sum, identical to PRESS R21), #6 (1,824) and the unfiltered union (18,159). Derived exactly today: #7 (161) and #8 (4,001). From PRESS on the same date: #2 (447), #3 (1,933) and #4 (1,244). From calibration on 2026-10-11: #9 (108), #10 (119) and #11 (29). #13 is only an upper bound.
- INDEPENDENT VALIDATION is an offline emulation on arXiv titles and abstracts, NOT an OpenAlex retrieval test. Neither OpenAlex indexing of the 9 items nor their subfield and T10845 tags were checked. The emulated 7/9 is an upper bound, and the (b) arm is 0/2 on fresh items. Before registration, re-run the 11 DOIs in the scratchpad batch against #5, #6 and #9.
- The (b) misclassification vocabulary remains the weakest arm. It now fails on hyphenated spellings ('mis-classified', 'mis-measured') and on 'mismeasured treatment' in a non-DiD treatment-effects context. PRESS showed the same for the pre-PRESS string on 5 of 6 items. The amendment is recorded but not applied.
- #13 is a union across several calls, so OpenAlex relevance scores are not comparable across lines. The protocol's relevance-ordered stopping rule can only apply within #5, and a screening order is proposed for confirmation.
- The (e) arm #9 depends on the T10845 topic tag. AKM shows that methods papers outside T10845 are lost, and new 2025-2026 shift-share preprints may not yet carry the tag. Only known-item and citation chasing guard against this.
- Kreider et al. 2012 may or may not carry T10845 among its topics, which was not verified. It is guaranteed only by the #12 known item.
- Year metadata drift (Conley-Taber 2010/2011, Ferman-Pinto 2018/2019) still applies. No date limits are used.
- Scratchpad artefacts with the exact URLs, ready to re-run, are in /tmp/claude-0/-home-user-projeto-pesquisa/7eb0b49f-b23b-5db5-b71e-5e4f90cc4ac1/scratchpad/ (q.py, lines.json, batch.json, urlsDev.json, indep.json, emu.py). No repository files were modified.

---

## SQ3 — revisão estruturada complementar: escolha de instrumento

⚠️ **Fonte:** recomendação da PRESS (`-press.json`). A rodada de finalização deste bloco ainda não terminou; ao terminar, rodar este script de novo.

**Veredito PRESS:** revision required.

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

- Recall na calibração: Primary: 9/9 indexed. Final union retrieves 8/9 (88.9%), and 9/9 with the hand-added anchor. S1 alone retrieves 7/9. Supplementary validation set S-1 (10 items found by OpenAlex title lookups during calibration, so NOT independent of the vocabulary): 10/10. It contains Gunnell 2007, the Danish tax ex post 2023, Norway 2020, the buffer-zone CBA 2009, Finger 2017, Böcker & Finger 2016 (x2), Möhring 2020, EST 2000 and the EU aerial ban 2018. Validation set V2 (12 items found outside the OpenAlex strings, via PubMed index, Scholar Gateway and web): 12/12 across the final union; S1 alone gets 7/12, and S2 (A4), S6, S7 and S8 add the other five.
- Volume na calibração: OpenAlex counts as of 2026-10-11/12. Core set (S1 1,545 + S2 689 + S3 174 + S4 227 + S5 108 = 2,743 gross; S1∩S2 measured at 30; the other overlaps, among S3/S2-A8b/S5 and S4/S1, were not measured and should be small): about 2,600–2,700 unique. Extended arms add, after measured overlaps with S1: S6 about +570, S7 about +143, S8 +391 at most (overlap with S1 not measured). Total about 3,600–3,800 OpenAlex records. Removing duplicate versions (AgEcon conference vs journal, SSRN vs journal, duplicate DOIs such as Soares & Porto, two records each for 'Spatial heterogeneity and the choice of instruments' 1996/2001 and 'Regulation of nitrogen pollution: taxes versus quotas' 1995) should bring this to roughly 3,300–3,500. The ranked sources add mostly duplicates; grey literature adds about 20–40 agency reports. Trade-off: a title+abstract-only design returns 6,380 and keeps the same 8/9 seeds, but its tail precision is about 0/15. The title-restricted design gets the same recall at less than half the volume. If volume must be cut further, S6 (regulatory cost) is the first candidate to screen with AI prioritization only; it was nonetheless the only arm that found Mace et al.

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

| bloco | linhas | registros | fonte da contagem |
|---|---|---:|---|
| SQ1 internacional | OpenAlex #6 (camadas 1 e 2) | 3.730 | finalização, 2026-10-12 |
| SQ1 internacional | PubMed #5 | 2.054 | finalização, 2026-10-12 (grande sobreposição com o OpenAlex; ~150–350 só no PubMed) |
| SQ1 América Latina | OpenAlex #11 | 1.591–1.740 | finalização, 2026-10-12 |
| SQ1 América Latina | SciELO #5 + LILACS #4 | 458 + 567 (brutos) | finalização; o SciELO repete o artigo entre coleções |
| SQ1 Scopus | — | ⬜ | exportação do pesquisador |
| **SQ1, únicos estimados** | | **~5.000–5.500** | estimativa; o braço AL sobrepõe pouco ao internacional fora dos estudos em inglês |
| SQ2 método | OpenAlex #13 | ≤ 4.265 (≈3.400–3.800 após versões) | finalização, 2026-10-12 |
| SQ3 instrumento | OpenAlex S1′–S10 | ~5.000–5.500 | PRESS (soma de partes); finalização em curso |

⚠️ **Recall em validação independente (finalização):**
- **SQ1 internacional: 5/7 (71%; IC 95% de Wilson 0,36–0,92).** As duas perdas são estudos argentinos que reportam "parâmetros neonatais/antropométricos". Os registros não têm resumo no OpenAlex, e o resumo no PubMed não traz nenhuma frase do bloco de desfecho. Um remendo amplo traria 2.223 registros de ruído e não foi adotado. **Mitigação prevista no protocolo:** busca de citações a partir das revisões relevantes. As duas perdas estão na lista de referências da revisão de escopo da EHP 2024 (10.1289/JHP1043), e o braço América Latina emendado recupera uma delas.
- **SQ1 América Latina: 7/10** na estratégia PRESS; a emenda pós-validação (#4) fecha as quatro perdas, mas essa emenda não foi validada de forma independente.
- **SQ2:** a validação foi emulada fora do OpenAlex, em títulos e resumos do arXiv, depois que as ferramentas esgotaram. Não é teste de recuperação.

