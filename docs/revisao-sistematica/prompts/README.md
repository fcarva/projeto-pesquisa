# Prompts da revisão sistemática (PRISMA-trAIce M6)

Cada arquivo é o script de *workflow* executado **verbatim**: os prompts dos
agentes estão no próprio código. Parâmetros de amostragem não são expostos pela
plataforma (Claude Code) e ficam no padrão dela.

| arquivo | etapa | data | argumentos |
|---|---|---|---|
| `00-conferencia-referencias-protocolo.js` | conferência no Crossref das referências metodológicas do protocolo | 2026-10-11 | `["10.1136/bmj.n71","10.1136/bmj.g7647","10.1016/j.jclinepi.2016.01.021","10.1016/j.envint.2024.108602","10.1136/bmj.l6890","10.1136/bmj.39489.470347.AD","10.2196/80247","10.1136/bmj.i4919"]` |
| `01-calibracao-busca.js` | calibração das strings (desenvolvimento da estratégia, PRISMA-P) e revisão PRESS | 2026-10-11 (retomado após o limite de uso, com os agentes concluídos vindos do cache) | — |
| `02-finalizacao-busca.js` | aplicação das revisões PRESS, congelamento das strings em linhas numeradas e recall em validação independente | 2026-10-12 | — |
| `03-leapspace-busca-complementar-sq1.md` | busca complementar da SQ1 no LeapSpace (Elsevier, via CAPES), colada pelo pesquisador; a resposta volta para conferência no Crossref e para a deduplicação | 2026-10-13 | — |
| `04-triagem-titulo-resumo-sq1.md` | triagem por título e resumo da SQ1 (dois triadores de IA independentes, mesmo texto; o lote entra em `{{LOTE}}`) | 2026-10-13, **aguardando aprovação** | lote de `ferramentas/prepara_triagem.py` |
