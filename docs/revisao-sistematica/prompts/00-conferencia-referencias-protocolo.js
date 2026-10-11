export const meta = {
  name: 'verify-protocol-refs',
  description: 'Verify the methodological references cited in the SR protocol against Crossref (via Firecrawl)',
  phases: [{ title: 'Verify', detail: 'one Crossref lookup per DOI' }],
}
const DOIS = args
const SCHEMA = {
  type: 'object',
  properties: {
    doi: { type: 'string' },
    resolved: { type: 'boolean' },
    title: { type: 'string' },
    authors_first3: { type: 'string' },
    container: { type: 'string' },
    year_issued: { type: 'string' },
    volume_pages: { type: 'string' },
    note: { type: 'string' },
  },
  required: ['doi', 'resolved', 'note'],
}
const out = await parallel(DOIS.map(d => () => agent(
  `Look up DOI ${d} in the Crossref REST API. Direct network is blocked: load mcp__Firecrawl__firecrawl_scrape with ToolSearch and scrape https://api.crossref.org/works/${d} (formats ["markdown"]). Report exactly what Crossref returns: title, first three authors (family, given initial), container-title, issued year, volume/issue/pages or article number. If it does not resolve, say so. Do not fill anything from memory.`,
  { label: `crossref:${d}`, schema: SCHEMA, effort: 'low' })))
return out.filter(Boolean)
