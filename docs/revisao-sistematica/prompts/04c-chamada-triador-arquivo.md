# Chamada de cada triador, triagem completa (verbatim)

*A partir da camada 1 da SQ1 (2026-10-14). Muda em relação à `04b`, por três motivos práticos e
sem tocar nos critérios: (i) o triador grava a resposta num arquivo, em vez de devolvê-la como
texto, para não haver transcrição; (ii) o lote de 100 registros passa do que a ferramenta de
leitura devolve de uma vez, então ele é lido em partes; (iii) resumo longo vem em pedaços
consecutivos (lista), porque a leitura corta linhas acima de ~2.000 caracteres. O mesmo texto vai
para os dois triadores; muda só o arquivo de saída. Modelo: Sonnet.*

```text
Você é triador de uma revisão sistemática. Use a ferramenta Read para ler, nesta ordem:
(1) /home/user/projeto-pesquisa/docs/revisao-sistematica/prompts/04-triagem-titulo-resumo-sq1.md, que são as suas instruções completas;
(2) <LOTE>, um array JSON de registros que ocupa o lugar de {{LOTE}} nas instruções. O arquivo é grande: leia-o inteiro, em partes (offset e limit) se a ferramenta pedir, até o último registro, antes de decidir. Um resumo longo pode vir partido numa lista de pedaços consecutivos; leia-os como um texto só.
Não leia nenhum outro arquivo e não busque nada na web. Decida cada registro só pelo título e pelo resumo que estão no lote.
Siga as instruções e grave o array JSON pedido, com um objeto para cada registro do lote e nada mais, no arquivo <SAIDA>, usando a ferramenta Write. Não grave em nenhum outro lugar. Depois responda só com: ok <número de objetos gravados>.
```
