# Resposta aos comentários do autor no PDF (2026-11-20)

Versão comentada: `paper/` no commit `0e159e3` (PDF `main_edição.pdf`, 28 p., 37 comentários).
Roteiro feito no modo *revision* do ARS (`academic-paper`), com os comentários do autor como parecer.
⚠️ O protocolo de *patch* do ARS (ancoragem de blocos, aplicação determinística) é para rascunho em
Markdown e **não foi rodado**: o projeto é LaTeX em vários arquivos, e as mudanças foram aplicadas
direto nos `.tex`. O registro de autorização é este arquivo mais as quatro decisões abaixo.

Resultado: 29 páginas, **14 da Introdução ao Cronograma** (limite 15), 34 referências, zero citação
indefinida, zero *overfull*.

## Decisões do autor nesta rodada

| tema | decisão |
|---|---|
| Agricultura familiar | segundo contraste declarado (municípios cearenses de agricultura familiar sem avião); CE × RN na Chapada segue principal |
| Poder estatístico | sai do corpo por inteiro; vai ao Apêndice B.5 |
| Drones (Lei 19.135/2024) | segundo evento do desenho |
| Páginas | manter 15, compensando com cortes |

## Três fatos que mudaram o texto

1. **A transcrição do STF no repositório é da ADI 5553/7755 (benefícios fiscais), não da ADI 6137.** É
   automática e não citável. E o registro do repositório estava desatualizado: o julgamento **terminou em
   18/12/2025**, improcedente por maioria (benefícios mantidos; vencidos Fachin e Cármen Lúcia, pela
   procedência, e Mendonça e Dino, pela procedência parcial com gradação por toxicidade). O texto cita só
   as notícias oficiais do STF (30/05/2023 e 18/12/2025). ⬜ Atualizar `docs/legislacao/adi-5553-7755-tributacao.md`.
2. **Toda fonte primária registra avião só em banana.** "Fruticultura irrigada de exportação" entrou como
   o cenário; o avião continua atribuído à banana.
3. **O "documento da UFES" para as declarações é a Portaria Normativa nº 310/2026** (23/10/2026, art. 19):
   declaração de uso de IA com ferramenta, versão, finalidade e forma de contribuição, em apêndice.

## Comentário a comentário

| # | p. | comentário (resumo) | o que foi feito | estado |
|---|---|---|---|---|
| 1 | 2 | título com cara de *working paper* | título **mantido** ("A proibição da pulverização aérea de agrotóxicos no Ceará: avaliação de impacto sobre a saúde ao nascer"), por decisão do autor: é o firmado com o orientador. Só o título conserva "saúde ao nascer"; o corpo usa "desfechos perinatais" | não aplicado, por decisão do autor |
| 2 | 3 | só bananais? prefiro fruticultura de exportação | "polo de fruticultura irrigada de exportação em que a banana era pulverizada por avião" | atendido em parte (as fontes só documentam banana) |
| 3 | 3 | por que não impactos perinatais? | "desfechos perinatais" em resumo, pergunta, objetivos, H1, palavras-chave | atendido |
| 4 | 3 | adjetivar só quando necessário ("na fronteira") | "diferenças em diferenças", sem adjetivo | atendido |
| 5 | 3 | economia agrícola mais funda no segundo ensaio | resumo: o avião como tecnologia de produção, ajuste dos produtores, comparação de instrumentos | atendido |
| 6 | 5 | gancho não é AER | abre pela externalidade de uma técnica (ganho do produtor, deriva para o vizinho); saem galinhas, varal e contagem de voos | atendido |
| 7 | 5 | gancho: fruticultura, Zé Maria liderança, ABRASCO | segundo parágrafo da introdução | atendido |
| 8 | 5 | STF "à la Weitzman" | parágrafo novo: quantidade validada (2023) e preço mantido como subsídio (2025); Weitzman | atendido, com fonte oficial e não com a transcrição |
| 9 | 5 | "a que custo agrícola" é insensível | pergunta: "como os produtores se ajustaram à retirada dessa tecnologia de aplicação?" | atendido |
| 10 | 5 | antecedentes por literatura, sem 1-2-3 | quatro literaturas: economia dos agrotóxicos; perinatal; Brasil; Chapada | atendido; a revisão sistemática fica declarada como não concluída (Apêndice A) |
| 11 | 6 | "caso que a literatura não cobre": necessária? | frase retirada | atendido |
| 12 | 6 | "perda fetal" → efeitos perinatais? | mecanismo reescrito; objetivo (c) diz "óbito fetal" | atendido |
| 13 | 6 | "delimita o que não promete": retórica | substituído por limites declarados (exposição não observada, ITT municipal, 2–3 tratados, premissa do primeiro estágio) | atendido |
| 14 | 6 | ajustar ao Mixtape; não mostrar o poder de cara | saiu a antecipação do resultado de poder; entra a lógica de projeto e a citação de Cunningham (2021) | atendido |
| 15 | 6 | Chapada como controle natural; agricultura familiar como controle | objetivo geral em linguagem de experimento natural; segundo contraste no objetivo (c) | atendido |
| 16 | 7 | fundamentar em economia agrícola (Seixas, ETH) | Seixas, Silveira & Ferrari (2022); Böcker & Finger (2016); Finger et al. (2017), na introdução, na revisão e na §4.6 | atendido |
| 17 | 7 | H1 em linguagem de DiD | H1 com grupo tratado e grupo de controle | atendido |
| 18 | 7 | H2 e o controle de agricultura familiar | H2 inclui "não aparece nos municípios de agricultura familiar" | atendido |
| 19 | 7 | H4 equivocada | H4: a retirada impôs custo de ajuste; área e produção do tratado caíram em relação ao controle | ⚠️ **redação minha — conferir** |
| 20 | 8 | adoção escalonada / Callaway–Sant'Anna | §4.2: DiD com estudo de evento; CS como implementação, com o porquê; drones como segundo evento (§4.4 e B.3) | atendido |
| 21 | 8 | situação do RN | regra federal (IN MAPA 2/2008: 500 m e 250 m), projeto de 2019 na Assembleia potiguar, Ceará único com lei | atendido |
| 22 | 8 | Chapada como elemento natural | abre o capítulo 2 | atendido em parte: sem fonte de geologia citável no repositório |
| 23 | 8 | explicar sigatoka | uma frase | atendido |
| 24 | 8 | glifosato: situar na literatura | "a literatura econômica mediu sobretudo herbicidas em grãos; aqui é fungicida em fruticultura perene" | atendido |
| 25 | 8 | Mixtape: indícios, não evidência causal (contrato) | "há um indício" | atendido |
| 26 | 8 | Mixtape (§2.1) | §2.1 abre pelo primeiro estágio (Cunningham); relatos "valem como indícios" | atendido |
| 27 | 9 | barra mal diagramada | figura refeita: faixas A–D com legenda na fonte, quatro regimes, rótulos sem sobreposição | atendido |
| 28 | 10 | explorar efeitos perinatais | bloco próprio "Agrotóxicos e desfechos perinatais" com magnitudes | atendido |
| 29 | 10 | Januzzi: o que encontra? | coeficientes positivos e imprecisos com EF de município e ano; associação a 10% só sem EF de ano | atendido |
| 30 | 11 | teoria da mudança: reconstruir pelo material | parte da justificativa do PL 18/2015, do parecer de 2016 e do julgamento de 2023 | atendido |
| 31 | 12 | "O que é aqui" | "Como aparece no caso" | atendido |
| 32 | 15 | rever o capítulo de poder | seção retirada do corpo; Apêndice B.5; uma frase nas limitações | atendido |
| 33 | 19 | qualificação no 1º semestre de 2027 | linha nova no cronograma (2027/1–2027/2) | atendido |
| 34 | 24 | declarações conforme a UFES | declaração de IA no formato do art. 19 da Portaria 310/2026 | ⬜ **falta a versão do modelo e o financiamento (autor)** |

(Os 37 comentários do PDF incluem três marcações repetidas sobre o mesmo trecho; estão agrupadas acima.)

## O que saiu do corpo para caber

Seção de poder (para B.5); contagem de voos, galinhas e varal; parágrafo "delimita o que não promete";
detalhes das teses de Viçosa; Soares & Porto na revisão (segue citado na §4.6); a repetição, na §2.1, do
que se faz se os voos tiverem cessado antes (está na §4.4).

## Abertos

- H4 (redação do autor); versão do modelo de IA e financiamento no Apêndice A.
- Referências que **não** entraram por falta de conteúdo conferido: Böcker et al. (2020, proibição do
  glifosato — o Crossref não tem resumo); Bucher & Seixas (2026); Terra de Direitos (2022); fonte de
  geologia da Chapada; estimador para tratamento não absorvente (drones).
- Inferência com 2–3 tratados: segue como estava (aberto desde 17/11).
