# Pauta para o orientador — projeto de dissertação (entrega 27/11/2026)

*2026-11-10. Acompanha o PDF do projeto (`projeto/main.pdf`, `make projeto`).
Sete decisões. Cada uma aparece marcada em vermelho no rascunho como
**[Decisão Dn]**, no ponto do texto que ela afeta. O texto já foi escrito com o
padrão indicado; se a decisão for outra, troca-se o trecho correspondente.*

Origem: parecer de 22/09/2026 (`docs/revisao/feedback-2026-09-22.md`) e a
resposta a ele (`docs/ars/17-resposta-ao-feedback-2026-09-22.md`, §5), mais a
matriz de rotas de `docs/ars/19-medida-e-desenho-fase2-investigacao.md`, §5.

## Contexto em quatro linhas

- A estimação do Ensaio 1 rodou com dados reais em setembro. O efeito no nível
  é −36,19 g (IC 95% [−66,51; −5,87]), sinal contrário ao esperado.
- O número não é tratado como achado: a meia-largura (30,3 g) é o dobro do piso
  pré-especificado (15 g), o agregado depende de 15 municípios de controle, e
  ele não é plausível como efeito diluído do ban.
- A variável de dose (área de banana) classifica mal o tratamento: pelo Censo
  Agropecuário de 2006, só 2 dos 17 municípios do decil superior e 7 dos 169
  com dose positiva tinham aplicação por aeronave.
- Risco aberto: notícia de proibição na Chapada em março de 2011 e ação civil
  pública em julho de 2011, com desfecho desconhecido.

## Decisões

| # | Decisão | Padrão adotado no texto | Alternativa | Onde no PDF |
|---|---|---|---|---|
| D1 | Estimando declarado | Efeito de forma reduzida do ban segundo a *proxy* de bananicultura; resultado principal é o `ATT(d\|d)` | Dose-resposta da pulverização aérea — exigiria o cadastro operacional pré-ban | Seção 4.1 |
| D2 | Papel do FAO-GAEZ | Construção do grupo de comparação e checagem de relevância; IV como extensão declarada | Estimar por IV já — exclusão frágil no semiárido (aptidão correlaciona com água) | Seção 4.4 |
| D3 | Janela da dose | 2015–2018 principal; 2010–2014 como sensibilidade | Promover 2010–2014 a principal — muda o plano de análise e ~24% do grupo tratado | Seção 4.2 |
| D4 | Vintage dos dados | Estender o SINASC até 19/12/2024, refazer painel e poder, congelar datas de extração | Manter 2015–2022 | Seção 4.5 |
| D5 | Inferência do nível | Procedimento que respeite os 15 controles (lógica Conley–Taber com papéis invertidos); jackknife dos controles reportado | Manter o bootstrap multiplicador como principal | Seção 4.6 |
| D6 | Enquadramento do Ensaio 2 | Suficiência informacional + padrão tecnológico (Helfand 1991) + objetivo do formulador (Hitzig 2020); sem ancorar em `ATT(d\|d)` | Adiar o Ensaio 2 até haver curvatura identificada | Seção 6.2 |
| D7 | Próximo desenho do Ensaio 1 | Desenho de calendário (hiato sazonal pico × entressafra onde havia aeronave), com plano de análise próprio fechado antes de estimar | Encerrar o Ensaio 1 como diagnóstico do desenho e da medida | Seção 7.1.3 |

D2, D3 e D7 mexem na estratégia de identificação. D7 é a de maior consequência
para o cronograma.

## O que preciso do orientador além das decisões

1. Título definitivo e dados de capa (linha de pesquisa, coorientação).
2. Data prevista de defesa — o cronograma do Capítulo 8 supõe julho de 2027.
3. Se o programa exige parecer de comitê de ética para dados públicos sem
   identificação.

## O que já está encaminhado, sem depender de decisão

- Minutas dos três pedidos de acesso à informação (MAPA, ADAGRI, SEMACE) em
  `docs/legislacao/`. Falta protocolar.
- Código da inferência sobre o nível, do perfil por dose e do MDE do desenho de
  calendário. Falta rodar com o painel real, na máquina local.
