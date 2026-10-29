# Chamada do adjudicador, triagem completa (verbatim)

*A partir da camada 1 da SQ1 (2026-10-29). Muda em relação à `05b` pelos mesmos motivos práticos
da `04c`, sem tocar nas instruções (`05-adjudicacao-sq1.md`) nem nos critérios: (i) o adjudicador
grava a resposta num arquivo, em vez de devolvê-la como texto, para não haver transcrição; (ii) o
lote de divergências pode passar do que a ferramenta de leitura devolve de uma vez, então ele é
lido em partes; (iii) resumo longo vem em pedaços consecutivos (lista). Modelo: o desta sessão.
`<DIVERGENCIAS>` = lote gerado por `ferramentas/concordancia.py`; `<SAIDA>` =
`registros/triagem/<sq>-<modo>-adjudicacao.json`, que o `concordancia.py` lê.*

```text
Você é o adjudicador de uma revisão sistemática. Use a ferramenta Read para ler, nesta ordem:
(1) /home/user/projeto-pesquisa/docs/revisao-sistematica/prompts/05-adjudicacao-sq1.md, que são as suas instruções;
(2) o arquivo de critérios que essas instruções indicam;
(3) <DIVERGENCIAS>, o array JSON que ocupa o lugar de {{DIVERGENCIAS}}. Leia-o inteiro, em partes (offset e limit) se a ferramenta pedir, até o último registro, antes de decidir. Um resumo longo pode vir partido numa lista de pedaços consecutivos; leia-os como um texto só.
Não leia nenhum outro arquivo e não busque nada na web.
Siga as instruções e grave o array JSON pedido, com um objeto para cada registro do lote de divergências e nada mais, no arquivo <SAIDA>, usando a ferramenta Write. Não grave em nenhum outro lugar. Depois responda só com: ok <número de objetos gravados>.
```
