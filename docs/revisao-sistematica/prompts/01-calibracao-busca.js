export const meta = {
  name: 'sr-search-calibration',
  description: 'PRISMA-P search-strategy calibration: per-block search strings, hit counts and known-item recall across OpenAlex, PubMed index, Scholar Gateway, SciELO/LILACS',
  phases: [
    { title: 'Calibrate', detail: 'one agent per review block tests and refines search strings' },
    { title: 'PRESS', detail: 'independent PRESS-style peer review of each final strategy' },
  ],
}

const COMMON = `
You are calibrating the SEARCH STRATEGY for a systematic review protocol (PRISMA-P stage). You are NOT screening or selecting studies; you only design and test search strings and report hit counts and known-item recall.

Context: a Brazilian economics master's dissertation (PPGEco/UFES) evaluates the 2019 state ban on AERIAL pesticide spraying in Ceará, Brazil (Lei 16.820/2019), as a negative externality. Essay 1: causal effect of the ban on birth outcomes (SINASC), continuous-dose DiD (Callaway, Goodman-Bacon & Sant'Anna 2024). Exposure dose = pre-ban banana area (fungicides like procymidone applied by airplane). Essay 2: instrument choice (ban vs tax vs buffer zones) under Weitzman prices-vs-quantities.

TOOLS AND HOW TO USE THEM (direct curl/bash network access is BLOCKED; use MCP tools, load them with ToolSearch first):
- OpenAlex REST API through Firecrawl: call mcp__Firecrawl__firecrawl_scrape with url like
  https://api.openalex.org/works?filter=title_and_abstract.search:<URL-encoded boolean query>&per-page=5&select=id,doi,title,publication_year
  and formats ["markdown"]. The JSON "meta.count" is the hit count. OpenAlex supports uppercase AND/OR/NOT, parentheses and "quoted phrases" in .search filters; verify the syntax actually behaves as expected (e.g. compare counts of A, B, A AND B). You can add filters separated by commas, e.g. publication_year:1990-2026, type:article|preprint.
- KNOWN-ITEM RECALL in OpenAlex: add a doi filter with pipe-separated DOIs, e.g. filter=doi:10.1038/s41467-017-00349-2|10.1086/725349,title_and_abstract.search:<query>. The DOIs returned are the seeds your string retrieves; seeds missing are misses. First check each seed DOI is indexed at all (filter=doi:<all seeds> alone) so you separate "not indexed" from "missed by the string".
- PubMed/medRxiv/arXiv index: mcp__Firecrawl__firecrawl_research_search_papers (ranked, no total counts; use k up to 100 to check whether seeds appear in top-k for your natural-language framing).
- Wiley full-text index: mcp__Scholar_Gateway__semanticSearch (ranked passages).
- Web/grey literature: mcp__Firecrawl__firecrawl_search or mcp__Parallel_Search__web_search (e.g. site:nber.org, site:ideas.repec.org, site:ssrn.com, site:iza.org).
- Crossref API also works via firecrawl_scrape (https://api.crossref.org/works?query.bibliographic=...&rows=5) if useful.
Be economical but thorough: iterate strings until recall of indexed seeds is maximized while total volume stays screenable (state the trade-off explicitly). Record EVERY query you ran with its count, in order, so the log is reproducible. Do not invent counts: report only what the tools returned. If a tool fails, say so.
Return your result through the structured output.`

const BLOCKS = [
  {
    key: 'SQ1-intl',
    prompt: `${COMMON}

BLOCK: SQ1 (primary systematic review, PECOS). Question: effect of ENVIRONMENTAL/COMMUNITY exposure to AGRICULTURAL pesticides (residential proximity, area-level agricultural use, aerial spraying/fumigation campaigns, spray drift, agricultural pesticide contamination of drinking water, policy shocks such as bans/approvals/GM seed adoption) during pregnancy on birth outcomes: birth weight, low birth weight, preterm birth, small for gestational age, fetal death/stillbirth, neonatal/infant mortality, congenital anomalies. Designs: quasi-experimental (DiD, IV, RD, event study, natural experiment), cohort, case-control, ecological/panel with spatial exposure. Intended exclusions (do not optimize for these): purely occupational exposure, household/indoor pesticide use, biomonitoring-only studies without agricultural source, animal/in vitro.
Languages: English (this agent). Databases to calibrate: OpenAlex (primary, give counts), PubMed index (firecrawl research), Scholar Gateway, and grey literature in economics (NBER, IZA, SSRN, RePEc) via web search.
SEED SET for known-item recall (all should be retrieved):
10.1038/s41467-017-00349-2 (Larsen, Gaines & Deschenes 2017, Nat Commun)
10.1086/725349 (Calzada, Gisbert & Moscoso 2023, JAERE, banana fumigation Ecuador)
10.1016/j.jhealeco.2017.04.005 (Camacho & Mejia 2017, aerial spraying Colombia, J Health Econ)
10.1093/restud/rdad011 (Dias, Rocha & Soares 2023, glyphosate downstream birth outcomes Brazil, ReStud)
10.1073/pnas.2413013121 (Reynier & Rubin 2025, glyphosate + GM seed, perinatal health, PNAS)
10.1111/j.1365-3016.2010.01165.x (Shirangi et al. 2011, living near agricultural pesticide applications, Paediatr Perinat Epidemiol)
10.1111/j.1651-2227.2008.01207.x (Winchester, Huskins & Ying 2009, agrichemicals in surface water and birth defects)
10.1002/pam.22558 (DiSalvo & Hill 2023, drinking water contaminants incl. atrazine and birth outcomes)
10.3390/toxics6030041 (Ling et al. 2018, ambient pesticides, preterm birth, California)
Also try to find (no DOI known): Charles A. Taylor, "Cicadian Rhythm: Insecticides, Infant Health, and Long-term Outcomes" (working paper).
Deliver: final boolean string(s) for OpenAlex with count and recall; natural-language framings for the ranked indexes with which seeds appeared; grey-literature query set. Also list any NEW highly relevant studies you incidentally noticed (title, year, DOI if shown) — as a list only, they are not screened.`,
  },
  {
    key: 'SQ1-latam',
    prompt: `${COMMON}

BLOCK: SQ1 Brazil / Latin America sub-strategy (Portuguese and Spanish, plus English-language studies set in Latin America). Same PECOS as the main SQ1: environmental/community exposure to agricultural pesticides (agrotóxicos/plaguicidas), including aerial spraying (pulverização aérea / fumigación aérea / aspersión aérea), on birth outcomes (peso ao nascer, baixo peso, prematuridade, malformações congênitas, óbito fetal, mortalidade infantil; peso al nacer, bajo peso, prematurez, malformaciones). Also context studies on Chapada do Apodi / Ceará / Limoeiro do Norte / Baixo Jaguaribe agrotóxicos e saúde (Rigotto group, Dossiê ABRASCO) — flag these as "context" if they are not effect studies.
Databases to calibrate: SciELO (via firecrawl_scrape of https://search.scielo.org/?q=<query>&lang=pt&count=50 — figure out the boolean syntax that works; a naive phrase query returned 0), LILACS via BVS portal (https://pesquisa.bvsalud.org/portal/?q=<query> or the LILACS-specific filter; test what works through firecrawl_scrape), OpenAlex with Portuguese/Spanish terms (counts), and web search for Brazilian economics working papers (e.g. ANPEC, IPEA, FGV) on agrotóxicos and saúde infantil.
SEED SET: 10.1590/0103-11042017s206 (Rocha et al. 2017, Saúde em Debate, women workers in agribusiness, Chapada do Apodi — context); 10.1093/restud/rdad011 (Dias, Rocha & Soares 2023, Brazil); 10.1086/725349 (Calzada et al. 2023, Ecuador); 10.1016/j.jhealeco.2017.04.005 (Camacho & Mejia 2017, Colombia). Also try to locate (and report DOI if found): Brazilian studies associating municipal pesticide use/soy expansion with birth defects or low birth weight (e.g. studies in Mato Grosso, Paraná, Rio Grande do Sul), and the 'Dossiê ABRASCO' itself.
Deliver: working query strings per database with counts, recall, and a list of incidentally noticed highly relevant studies (not screened).`,
  },
  {
    key: 'SQ2-method',
    prompt: `${COMMON}

BLOCK: SQ2 (companion structured review, methods). Question: what estimators and identifying assumptions does the econometrics/statistics literature offer for a SIMULTANEOUS (non-staggered) policy shock with CONTINUOUS treatment intensity (dose), MISCLASSIFIED treatment (false positives in the treated group), and FEW CONTROL (or few treated) clusters? Sub-topics: (a) DiD with continuous / multi-valued treatment and dose-response (CGS 2024, de Chaisemartin & D'Haultfoeuille et al.), (b) DiD/treatment effects with misclassified or mismeasured treatment, (c) inference with few treated or few control clusters (Conley-Taber, wild cluster bootstrap, randomization inference, Ferman-Pinto, conformal), (d) synthetic control / synthetic DiD with few units, (e) agro-climatic suitability (FAO-GAEZ) as instrument or exposure predictor, shift-share / formula instruments.
No population or geography restriction (approved deviation). Databases: OpenAlex (counts; consider restricting to concepts/fields economics/statistics if it helps, e.g. via primary_topic or concepts filters — report what you used), arXiv via firecrawl research search (econ.EM, stat.ME), NBER/SSRN/RePEc via web search.
SEED SET: 10.3386/w32117 (Callaway, Goodman-Bacon & Sant'Anna, DiD with continuous treatment, NBER WP); arXiv 2107.02637 (same paper, arXiv); 10.1002/jae.3116 (Negi & Negi 2025, DiD with misclassified treatment); arXiv 2207.11890 (Denteh & Kedagni, misclassification in DiD); 10.1162/rest_a_00049 (Conley & Taber 2011); 10.1162/rest_a_00887 (Canay, Santos & Shaikh 2021 wild bootstrap few clusters); 10.1257/aer.20190159 (Arkhangelsky et al. 2021 SDID); 10.1111/ectj.12107 (MacKinnon & Webb 2018); 10.1162/rest.90.3.414 (Cameron, Gelbach & Miller 2008); 10.1093/ectj/utae003 (Borusyak & Hull, formula instruments review); 10.1093/restud/rdad011 (Dias, Rocha & Soares 2023 — uses suitability-based exposure). Also locate Ferman & Pinto (2019, REStat) "Inference in differences-in-differences with few treated groups and heteroskedasticity" and de Chaisemartin, D'Haultfoeuille et al. on continuous treatments (report identifiers).
Methods literature is unbounded; design strings that are sensitive for the five sub-topics with a screenable volume (state volume per sub-topic). Deliver strings, counts, recall, and incidentally noticed key papers (not screened).`,
  },
  {
    key: 'SQ3-instrument',
    prompt: `${COMMON}

BLOCK: SQ3 (companion structured review, Essay 2). Question: what form of the damage function does the literature on INSTRUMENT CHOICE for agricultural pesticides assume, and which empirical parameter does it require to rank bans, taxes and buffer zones? Include: economic analyses (theoretical, simulation, empirical) of pesticide taxes/levies, bans/prohibitions/withdrawals of active ingredients or application methods (incl. aerial application restrictions), buffer zones/setbacks/no-spray zones, quotas, information instruments; ex post evaluations of pesticide bans or restrictions on use, yields, health (e.g. paraquat/highly hazardous pesticide bans and suicide in Sri Lanka, Korea, etc.; Danish/Norwegian/Swedish/French pesticide taxes; EU neonicotinoid restrictions; glyphosate ban assessments); and nonpoint-source pollution instrument choice applied to pesticides. Weitzman-style prices vs quantities applications to agrochemicals are of special interest.
Databases: OpenAlex (counts), AgEcon Search / RePEc / web search (grey literature in agricultural economics), Scholar Gateway.
SEED SET: 10.2307/1241928 (Lichtenberg & Zilberman 1988? 'Marginal analysis of welfare costs of environmental policies: the case of pesticide regulation', AJAE); 10.2307/1243825 (Helfand & House 1995, nonpoint source pollution heterogeneous conditions); 10.1111/j.1574-0862.2012.00581.x (Skevas, Stefanou & Oude Lansink 2012, pesticide taxes); 10.1093/erae/jby050 (Böcker & Finger, glyphosate ban assessment); 10.1111/agec.12817 (Finger et al. 2024, Europe pesticide policy); 10.2307/1350002 (Fernandez-Cornejo et al. 1998, economics of pesticide use review); 10.1111/ajae.12266 (Voica 2021?); 10.1111/ajae.12244 (Chatzimichael et al. 2021); 10.2307/2296698 (Weitzman 1974). Also try to locate: Gunnell et al. (2007) on pesticide regulation and suicide in Sri Lanka; Finger, Möhring et al. on pesticide taxes in Europe (e.g. Denmark); any study on buffer zones / setbacks for pesticide spraying (e.g. California school buffer zones) with an economic evaluation.
Deliver strings, counts, recall, and incidentally noticed key papers (not screened).`,
  },
]

const RESULT_SCHEMA = {
  type: 'object',
  properties: {
    block: { type: 'string' },
    query_log: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          order: { type: 'integer' },
          source: { type: 'string' },
          query: { type: 'string' },
          url_or_call: { type: 'string' },
          count: { type: ['integer', 'null'] },
          note: { type: 'string' },
        },
        required: ['order', 'source', 'query', 'note'],
      },
    },
    final_strategies: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          source: { type: 'string' },
          query: { type: 'string' },
          filters: { type: 'string' },
          count: { type: ['integer', 'null'] },
          rationale: { type: 'string' },
        },
        required: ['source', 'query', 'rationale'],
      },
    },
    known_item_recall: {
      type: 'object',
      properties: {
        seeds_tested: { type: 'array', items: { type: 'string' } },
        seeds_not_indexed: { type: 'array', items: { type: 'string' } },
        seeds_retrieved: { type: 'array', items: { type: 'string' } },
        seeds_missed: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, why: { type: 'string' } }, required: ['id', 'why'] } },
        recall_indexed: { type: 'string' },
      },
      required: ['seeds_tested', 'seeds_retrieved', 'seeds_missed', 'recall_indexed'],
    },
    volume_estimate_after_dedup: { type: 'string' },
    syntax_findings: { type: 'array', items: { type: 'string' } },
    incidental_relevant_studies: {
      type: 'array',
      items: { type: 'object', properties: { title: { type: 'string' }, year: { type: 'string' }, id: { type: 'string' }, why: { type: 'string' } }, required: ['title', 'why'] },
    },
    issues_and_limits: { type: 'array', items: { type: 'string' } },
  },
  required: ['block', 'query_log', 'final_strategies', 'known_item_recall', 'volume_estimate_after_dedup', 'issues_and_limits'],
}

const PRESS_SCHEMA = {
  type: 'object',
  properties: {
    block: { type: 'string' },
    verdict: { type: 'string', enum: ['no revision', 'revision suggested', 'revision required'] },
    press_items: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          element: { type: 'string', description: 'PRESS 2015 element: translation of question; boolean/proximity operators; subject headings; text word searching (free text); spelling, syntax, line numbers; limits and filters' },
          assessment: { type: 'string' },
          suggested_change: { type: 'string' },
          tested: { type: 'string', description: 'if you re-ran a modified query, the query and the count/recall you observed' },
        },
        required: ['element', 'assessment'],
      },
    },
    missing_concepts_or_synonyms: { type: 'array', items: { type: 'string' } },
    recommended_final_query: { type: 'string' },
  },
  required: ['block', 'verdict', 'press_items', 'recommended_final_query'],
}

const results = await pipeline(
  BLOCKS,
  b => agent(b.prompt, { label: `calibrate:${b.key}`, phase: 'Calibrate', schema: RESULT_SCHEMA }),
  (res, b) => res ? agent(`You are an independent search-strategy peer reviewer applying the PRESS 2015 guideline (McGowan et al.) to a systematic-review search strategy. Be adversarial: look for missing synonyms (e.g. agrochemical, plaguicide, fungicide, insecticide, herbicide, specific molecules such as glyphosate, atrazine, chlorpyrifos, mancozeb, procymidone; aerial application, crop dusting, aerial fumigation, drift), wrong operator logic, over-restrictive phrase quoting, and OpenAlex syntax pitfalls. You MAY re-run modified queries using the same tools (OpenAlex via mcp__Firecrawl__firecrawl_scrape, load with ToolSearch; direct network is blocked) to verify a suggestion improves recall without exploding volume; report what you ran and observed. Do not invent counts.

Original block instructions (for scope):\n${b.prompt}\n\nCalibration result to review (JSON):\n${JSON.stringify(res).slice(0, 60000)}`, { label: `press:${b.key}`, phase: 'PRESS', schema: PRESS_SCHEMA }).then(p => ({ calibration: res, press: p })) : null,
)

return results
