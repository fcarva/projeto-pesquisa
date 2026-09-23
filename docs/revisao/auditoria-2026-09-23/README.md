# Auditoria externa de 2026-09-23 — arquivo

*Arquivado em 2026-09-23 a partir do pacote que o pesquisador enviou à sessão
remota (`auditoria-completa-com-paineis-2026-09-23.zip`, SHA-256
`883df950c328b3235d9b587d8a3ec30fcda9e810a99ea5be63ff38be99558675`). A resposta,
achado por achado, está em `docs/ars/20-resposta-a-auditoria-2026-09-23.md`.*

**O que é.** Auditoria feita por outro assistente de IA, com subagentes, sobre o
commit `8d3a31e` (o `4ab2c93` desta branch mais o merge do PR #1 e a remoção de
`docs/programa-pesquisa.md`). Teve duas etapas:

1. **Auditoria integral** (`relatorios/auditoria-integral-2026-09-23.md`), com
   quatro pareceres separados: identificação, código, fontes primárias e
   teoria/custos. Foi feita sem os painéis.
2. **Auditoria empírica** (`relatorios/auditoria-empirica-2026-09-23.md`), feita
   com os painéis da máquina do pesquisador. Rodou o código original (Python 3.13,
   R 4.6.1, `renv` do projeto) e reproduziu o −36,19 g.

**O que não é.** Não é texto nosso, e nada aqui foi editado: os arquivos estão
como vieram. Os links internos apontam para caminhos do Windows da máquina do
pesquisador (`C:/Users/DELL/...`). Afirmações factuais daqui só entram no projeto
depois de conferidas (doc 20 §§2–5).

**O que não está aqui.** Nenhum painel Parquet e nenhum microdado. O pacote não os
trazia, e `data/` continua fora do git. Os CSV de `resultados/` são agregados:
contrastes, curvas por ponto de dose, estimativas sem cada controle e p-valores.
É o tipo de tabela que o `CLAUDE.md` permite versionar, e a auditoria pediu que o
projeto passasse a versionar.

| pasta | conteúdo |
|---|---|
| `relatorios/` | os 7 relatórios em Markdown, os manifestos, a conferência Crossref dos 47 DOIs (`auditoria-metadados-referencias.json`), a da Conab, a integridade dos painéis (metadados e hashes, sem células) e o patch dos placebos |
| `resultados/` | as saídas reproduzidas: CGS de peso e fetal, robustez, Holm, HonestDiD, SDID, placebos antes e depois da correção, jackknife dos controles, auditoria do nível |
| `resultados/reconciliacao/` | contrastes reconstruídos (janelas, pesos, 169×15, 169×14, 17×14), MDE recalculados, calendário CE e CE+RN |
| `resultados/logs/` | saída de console das rodadas e comparação com os CSV salvos |
| `codigo/` | os scripts que a auditoria usou para reconstruir e comparar |

⚠️ Os scripts de `codigo/` são do auditor, não do pipeline: não entram no
`Makefile` nem nos testes.
