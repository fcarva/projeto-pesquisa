# projeto/ — projeto de dissertação (entrega 27/11/2026)

Documento ABNT (NBR 15287, projeto de pesquisa) na classe `abntex2`. É uma
condensação de `paper/` (versão longa do Ensaio 1) e dos documentos de decisão
em `docs/`, já na posição corrigida pelo parecer de 22/09/2026.

## Compilar

```bash
make projeto
```

Gera `projeto/main.pdf` (não versionado). Exige TeX Live com `abntex2` e
`latexmk`. No Overleaf: enviar a pasta `projeto/` e `paper/referencias.bib`,
mantendo o caminho relativo `../paper/referencias`.

## Rascunho × versão final

Em `main.tex`:

- `\rascunhotrue` — mostra `[Decisão Dn: ...]` (vermelho) e `[A informar: ...]`
  (azul).
- `\rascunhofalse` — esconde as duas marcas. Usar na entrega.

As decisões D1–D7 estão em `docs/pauta-orientador-2026-11.md`.

## Estado por seção (2026-11-10)

| Arquivo | Conteúdo | Estado |
|---|---|---|
| `main.tex` | Preâmbulo, capa, folha de rosto, siglas, sumário | pronto; título e orientador a confirmar |
| `secoes/01-introducao.tex` | Tema, problema, hipóteses, objetivos, justificativa | primeira versão completa |
| `secoes/02-contexto.tex` | Lei, cronologia, química, deriva, registros | primeira versão completa |
| `secoes/03-referencial.tex` | Externalidade, instrumento, evidência, método | primeira versão completa |
| `secoes/04-metodologia.tex` | Estimando, dose, comparação, dados, inferência, ameaças | primeira versão completa; D1–D5 |
| `secoes/05-resultados-preliminares.tex` | Nível, inclinação, robustez, diluição, síntese | primeira versão completa |
| `secoes/06-ensaio2.tex` | Proposta do Ensaio 2 | primeira versão completa; D6 |
| `secoes/07-plano-de-trabalho.tex` | Atividades, riscos, reprodutibilidade | primeira versão completa; D7 |
| `secoes/08-cronograma.tex` | Quadro mensal | **horizonte suposto** (dez/2026–jul/2027) |
| `secoes/apendice-a-preespecificacao.tex` | Plano de análise e desvios | pronto |
| `secoes/apendice-b-proveniencia.tex` | Script de origem de cada resultado | pronto |

## Regras deste documento

- **Nenhum número novo.** Todo resultado vem de `paper/secoes/06-diagnostico-poder.tex`
  e dos docs 16 e 17, que por sua vez vêm da execução real de 21–22/09/2026.
  Número novo só entra com o CSV que o sustenta.
- **Bibliografia única.** `paper/referencias.bib`. Entrada nova só com DOI
  conferido no Crossref (ou exceção declarada no cabeçalho do bloco).
- **Citações.** `\citet{}` e `\citep{}` funcionam (ponte para `abntex2cite`),
  de modo que trechos de `paper/` migram sem reescrita.
- **Frases que o parecer derrubou não entram:** "compatível com efeito nulo",
  permutação "exata", "identificação fechada", placebo que "exclui".

## Pendências para a versão final

- [ ] Decisões D1–D7 do orientador.
- [ ] Data de defesa → ajustar o Quadro do Capítulo 8.
- [ ] Título definitivo, linha de pesquisa, nome completo do orientador.
- [ ] Comitê de ética: confirmar dispensa (Seção 7.3).
- [ ] Conferir o texto da IN MAPA nº 2/2008 (citada nas Seções 2.4 e 7.1.1).
- [ ] Conferir a edição vigente da NBR 15287 e o guia da Biblioteca Central da
      UFES (a 2ª ed. de 2015 é a localizada; o texto da norma está no GEDWeb).
- [ ] Opcional: números do `make real` (jackknife dos 15 controles, perfil por
      dose, IC por inversão) e uma figura.
- [ ] `\rascunhofalse` e leitura final.
