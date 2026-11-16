# Rodada 21 — estado em 2026-11-16 (todos os estágios executados)

Os Estágios 2.5, 3, 4, 3', 4', 4.5, 5 e 6 foram executados. O pipeline **não está
marcado como concluído**: falta o reconhecimento terminal do pesquisador (ledger, seq 31).
Estado em `passport.yaml`; registro em `stage6/registro_do_processo.md`.

## Entregável
- `paper/projeto/projeto.pdf` — projeto_v14, 40 páginas, 15 textuais (5–19), Referências na
  p. 20, Apêndices A a F, 58 referências. Hashes no passport.
- Compilar: `pdflatex` → `bibtex` → `pdflatex` ×2, em `paper/projeto` (não há `make` nem
  `latexmk` nesta máquina).
- **Nada foi commitado.** ⚠️ O PDF da Lei 1.511 em `docs/legislacao/` tem 28 MB.

## Resultado dos portões
- 2.5: PASS WITH NOTES (3 rodadas). 3: Major Revision (34 itens; painel cego imperfeito).
- 4 e 4': revisão e resíduos aplicados. 3': Minor Revision, em modo legado (sem contrato).
- 4.5: texto com zero achados na terceira rodada; **FAIL formal** de C4/D7 condição 4,
  aceito pelo pesquisador (seq 27). Modos 3 e 6 afastados com justificativa (seq 24).

## O que o pesquisador ainda precisa fazer
1. Ler `stage6/registro_do_processo.md` e `stage3/carta_ao_autor.md`; dar o reconhecimento
   terminal ou pedir correção.
2. Ratificar ou vetar, com o orientador, as decisões tomadas por delegação (lista no
   registro): célula 80 g × 0,25 do portão de poder; critérios dos registros e data-limite
   31/05/2027; concordâncias exigidas; vizinhos fora da comparação; chuva por quadra de
   exposição; diagrama causal no Apêndice E; divulgação qualitativa do resultado exploratório;
   linha 5 da regra (prática cessou antes da lei); compromisso de depósito público do plano.
3. Responder ao que ficou aberto: o desenho principal continua o mesmo, sabendo que a
   indicação exploratória é a linha 2 (sem teste)? Grupo tratado provisório: 7 municípios ou
   só a Chapada? RN como segunda comparação?
4. Fatos que só ele tem: data de defesa e prazo do programa; descrição da rodada de setembro
   (Apêndice F está genérico).
5. Decidir o commit.

## Pendências fora do pipeline
- Chuva municipal (FUNCEME/EMPARN) e voos por município e mês (LAI ao MAPA e à ADAGRI,
  minutas não protocoladas).
- Estudo de evento com leads e lags (`scripts/exploratorio/23_...py`): 1 de 6 estimações;
  fora do Makefile.
- Ação civil pública de 2011: número e desfecho. Nota de 11/03/2011: fonte não abriu.
- Calzada et al., versão publicada do JAERE: acesso pago.
- Três correções de uma linha da v10 e os documentos de apoio desta rodada não passaram por
  verificação independente.
