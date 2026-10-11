# Prompts da revisão sistemática (PRISMA-trAIce M6)

Cada arquivo é o script de *workflow* executado **verbatim**: os prompts dos
agentes estão no próprio código. Parâmetros de amostragem não são expostos pela
plataforma (Claude Code) e ficam no padrão dela.

| arquivo | etapa | data | argumentos |
|---|---|---|---|
| `00-conferencia-referencias-protocolo.js` | conferência no Crossref das referências metodológicas do protocolo | 2026-10-11 | `["10.1136/bmj.n71","10.1136/bmj.g7647","10.1016/j.jclinepi.2016.01.021","10.1016/j.envint.2024.108602","10.1136/bmj.l6890","10.1136/bmj.39489.470347.AD","10.2196/80247","10.1136/bmj.i4919"]` |
| `01-calibracao-busca.js` | calibração das strings (desenvolvimento da estratégia, PRISMA-P) e revisão PRESS | 2026-10-11 (retomado após o limite de uso, com os agentes concluídos vindos do cache) | — |
