export const meta = {
  name: 'sr-search-finalize',
  description: 'Apply PRESS revisions, freeze line-numbered search strategies, final counts and validation recall per block',
  phases: [{ title: 'Finalize', detail: 'one agent per block applies PRESS changes and freezes the strategy' }],
}

const BLOCKS = [
  { key: 'sq1-internacional', extra: 'Primary SR. Use the PRESS-recommended sensitive string without the context block as the PRIMARY OpenAlex search (QS-prime), with the animal NOT applied at TITLE level only and the bed-net NOT kept; include chlordecone/kepone, Ceará actives (procymidone, carbaryl, carbofuran, fenitrothion, dithiocarbamate) and "crop protection". Also freeze the augmented PubMed (E-utilities) string with the MeSH additions and the bed-net NOT. Define the context block only as a SCREENING-PRIORITY flag, not as a filter.' },
  { key: 'sq1-america-latina', extra: 'Collapse OA-1/OA-2 into one effect branch with the expanded geography block G4 (Brazilian states, demonyms, SINASC/DATASUS, Caribbean incl. French Antilles); add the agrochemical/molecule terms recommended; rebuild the context arm as recommended including unaccented variants; add the legal/policy arm if PRESS recommended it (drop the bare "16.820" token); SciELO S1-prime and LILACS L1-prime (with the DeCS line) as recommended. Drop the language branch as primary device.' },
  { key: 'sq2-metodo', extra: 'Adopt A2, B_v2, C_v3-lean and D3 as recommended, keep the (e) arms (formula/shift-share string, GAEZ keyword string and the citation-chasing arm), and run the union. Run the filtered strings a second time with topics.id:T10845 in place of the subfield filter if PRESS recommended it, and report the union count by OpenAlex ID (you may report the two counts and an overlap computed via NOT if a single call is impossible).' },
  { key: 'sq3-instrumento', extra: 'Apply the S3-double-prime rewrite, add the X block to S1, add NEW synonyms to the title block, add S4b, S9 (drift, liability, compensation) and S10 (elasticity / abatement cost), add the fumigant terms to S2 and the Pigovian/fee terms to S1-I if they test well. Report exact increments with within-field NOT as PRESS described.' },
]

const SCHEMA = {
  type: 'object',
  properties: {
    block: { type: 'string' },
    numbered_lines: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          line: { type: 'string', description: 'e.g. #1' },
          database: { type: 'string' },
          description: { type: 'string' },
          query: { type: 'string', description: 'exact query or URL filter, ready to run' },
          count: { type: ['integer', 'null'] },
          run_date: { type: 'string' },
          oql_or_echo_checked: { type: 'boolean' },
        },
        required: ['line', 'database', 'description', 'query'],
      },
    },
    final_lines_to_screen: { type: 'array', items: { type: 'string' }, description: 'which numbered lines produce the screening set, per database' },
    screening_priority_rule: { type: 'string' },
    recall_tuning_set: { type: 'string', description: 'recall on seeds + development items used in calibration/PRESS (development-set recall)' },
    recall_independent_validation: { type: 'string', description: 'recall on a FRESH validation set not used in tuning: list each item (DOI), how you selected it, indexed or not, retrieved or not' },
    estimated_unique_volume: { type: 'string' },
    changes_applied: { type: 'array', items: { type: 'string' } },
    changes_not_applied: { type: 'array', items: { type: 'object', properties: { change: { type: 'string' }, why: { type: 'string' } }, required: ['change', 'why'] } },
    issues: { type: 'array', items: { type: 'string' } },
  },
  required: ['block', 'numbered_lines', 'final_lines_to_screen', 'recall_tuning_set', 'recall_independent_validation', 'estimated_unique_volume', 'changes_applied'],
}

const results = await parallel(BLOCKS.map(b => () => agent(
`You are FINALIZING (freezing) the search strategy for one block of a systematic review protocol (PRISMA-P stage; no screening). Work from the repository files (read them first):
- docs/revisao-sistematica/calibracao/${b.key}.json  (calibration: query log, final strategies, recall, syntax findings)
- docs/revisao-sistematica/calibracao/${b.key}-press.json  (independent PRESS 2015 review: verdict "revision required", per-element suggested changes with the queries it tested, and recommended_final_query)
- docs/revisao-sistematica/protocolo.md (eligibility criteria; do not edit it)

Task: apply the PRESS revisions (block-specific notes: ${b.extra}), then FREEZE the strategy as line-numbered search lines per database (#1 exposure/concept, #2 outcome, ..., combination lines), each ready to run verbatim, with today's count. Accept a PRESS change unless testing shows it harms recall or explodes volume with noise; record every change applied and every change not applied with the reason.

Then measure recall twice: (1) development-set recall on the seeds and validation items already used in calibration/PRESS; (2) INDEPENDENT validation: assemble 5-10 fresh relevant items NOT used in calibration or PRESS (e.g. from the reference list of a recent review on the topic found via the research index or Scholar Gateway, or via OpenAlex citing works of a seed), state how each was selected BEFORE testing it, check it is indexed, then test retrieval. Report honestly, including misses and why.

Tools (direct curl is blocked; load via ToolSearch): mcp__Parallel_Search__web_fetch reaches https://api.openalex.org/works?filter=... and PubMed E-utilities (https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...&rettype=count) WITHOUT the Firecrawl rate limit — prefer it. mcp__Firecrawl__firecrawl_scrape (rate-limited ~13/min shared) for SciELO (search.scielo.org) and BVS/LILACS (pesquisa.bvsalud.org), and as fallback. Known pitfalls from calibration: OpenAlex has no wildcards, no accent folding, stems inflections only; Parallel web_fetch can return a CACHED answer for near-duplicate long URLs — check that meta.x_query (OQL echo) matches your query and add a harmless cache-busting parameter (e.g. &mailto=revisao.sistematica.ufes@example.org or a distinct per-page value) when re-running similar URLs. Commas inside a search value must be avoided.
Be efficient: do not re-explore what calibration/PRESS already settled; aim for roughly 15-30 tool calls. Never invent counts. Return via structured output.`,
  { label: `finalize:${b.key}`, schema: SCHEMA })))
return results
