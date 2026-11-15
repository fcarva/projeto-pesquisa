# Academic Integrity Verification Report

*ARS v3.24.2 · `integrity_verification_agent` · Estágio 2.5 · **projeto_v2, rodada 1** · concluída em 2026-11-15T22:53Z (UTC).
Manuscrito no commit `5c6cac4` (`git diff bacd817 HEAD -- paper/`): seções 03, 04, 05 e 07 reescritas; 01, 02, 06 e 08 alteradas; 7 entradas novas de bibliografia. PDF `paper/projeto/projeto.pdf`: 21 páginas, 15 textuais.
Os relatórios da v1 (`stage2.5_integrity_report*.md`) não foram alterados e não valem para esta versão. Este agente não editou o manuscrito nem os `.bib`. Arquivos gravados: este relatório e a pasta `evidence/`, refeita por inteiro.*

## Verification Mode

Initial Verification (Mode 1, pre-review), passada completa sobre o projeto_v2. Reaproveitado da v1, sem refazer: a verificação das 36 referências que não mudaram e das afirmações cujo texto não mudou. Feito de novo: Fase A das 8 chaves novas na lista, Fases B, C e E sobre o texto atual, Fase D nos parágrafos novos, e os 7 modos.

## Verdict

**FAIL**

Uma issue SERIOUS e uma MEDIUM, as duas em afirmações novas que sustentam o desenho principal: a de que os municípios de banana familiar "não têm o avião" e a de que o análogo equatoriano não encontra efeito no terceiro trimestre. O restante confere ou tem só imprecisão. As 44 referências existem. Nenhum modo de falha abre bloqueio novo.

## Verification Summary

| Category | Total | Passed | Issues |
|----------|-------|--------|--------|
| Reference Existence | 44 (chaves citadas agora) | 44 | 0 |
| Bibliographic Accuracy | 44 | 41 | 3 MINOR (`ceara2018nascer`, `ibge2017censoagro`, `ibge2006censoagro`); mais 1 MINOR geral de completude |
| Ghost Citations | -- | -- | 0 órfãs na lista impressa / 0 pendentes (44 chaves, 44 itens no `projeto.bbl`, nenhuma referência indefinida). Saíram do texto `cameron2008wild`, `rambachan2023credible` e `roth2023trending`; entrou `canay2021wild`, que já estava em `referencias.bib` |
| Citation Context Accuracy | 44 de 44 chaves | 37 | 1 MEDIUM, 4 MINOR; 4 chaves com acesso limitado (notas) |
| Statistical Data Accuracy | 14 números ou fatos datados | 13 | 1 MINOR ("poucas centenas de metros") |
| Internal Consistency | -- | Fail | 3 inconsistências menores (MINOR) |
| Originality Check (D1) | 9 de 27 parágrafos novos ou reescritos (33%) | 9 | 0 (CLOSE_MATCH / VERBATIM) |
| Self-Plagiarism (D2) | não refeita | -- | -- |
| Claim Verification (E) | 61 de 65 registradas (Mode 1: HIGH-IMPACT: 47, RANDOM: 0, TOP-UP: 14; NOT-SELECTED: 4, só no E5; semantic extraction coverage: not_machine_detectable; candidate gaps: 1, falso positivo inspecionado) | 46 | 0 MAJOR_DISTORTION / 1 UNVERIFIABLE (5 MINOR_DISTORTION; 9 UNVERIFIABLE_ACCESS) |

Restrições do autor:

| Restrição | Resultado |
|---|---|
| Nenhum número de estimativa | Nenhum. Os valores presentes são da literatura (23 a 32 g; cerca de 80 g; 150 metros; três meses) ou de fonte pública (36 estabelecimentos, 7 e 184 municípios, 23 pontos de coleta). A rodada exploratória é mencionada sem número. |
| No máximo 15 páginas textuais | 15 (numeração impressa 3 a 17; referências a partir da 18). No limite, sem folga. |
| Só o Ensaio 1 | O Ensaio 2 aparece só como remissão (`03-referencial.tex:19-21`; `08-cronograma.tex:19-21`) e como linha do cronograma (`08-cronograma.tex:43`). |

O PDF é posterior aos fontes (22:45:05 contra 22:45:04), traz a Figura 1 e não tem referência indefinida. Não o recompilei.

## Os onze pontos pedidos pelo coordenador

| # | Ponto | Resultado |
|---|---|---|
| 1 | Calzada et al. | Li o manuscrito de março de 2023, depositado no repositório da Universidade de Barcelona sob o registro do artigo (o aceite é de 22/03/2023). Não é a versão publicada. **Confere:** 80 g na especificação principal; exposição definida por mãe a até 150 m do perímetro e pelo menos três meses em célula com mais de 4 galões por hectare; gradientes semelhantes entre 150 e 2.500 m; efeito no primeiro e no segundo trimestres; fumigação mais intensa na estação chuvosa. **Não confere:** "nenhum no terceiro". O manuscrito diz que o termo do terceiro trimestre é "negative and non-significant" e relata déficit no terceiro trimestre para meninos e numa análise de robustez. IL-MEDIUM-1 |
| 2 | Rigotto et al. (2013) | Confere. Estudo ecológico, 2000 a 2010; grupo caso Limoeiro do Norte, Quixeré e Russas; grupo controle de 12 municípios "onde se desenvolve apenas a agricultura familiar tradicional do semiárido"; internações por neoplasia 1,76 vez maiores; tendência crescente de óbitos fetais. Título e autores conferem no Crossref |
| 3 | Jones (2020) | Confere no resumo: estimativas separadas para inseticida e fungicida. "Entre os poucos" não é verificável em fonte; é juízo do texto |
| 4 | Lei municipal 1.511/2010 | **Confere, em fonte primária.** Baixei o PDF da Câmara (68 páginas digitalizadas) e li as páginas 1, 65 e 66: lei de 26 de maio de 2010; art. 212 revoga a Lei 1.478, de 20 de novembro de 2009; art. 214, II, proíbe a aplicação aérea a menos de mil metros de povoações e de mananciais de captação e a menos de quinhentos metros de mananciais, moradias isoladas e agrupamentos de animais. O endereço na entrada funciona |
| 5 | Seca | O título da entrada confere ("Ceará pode proibir pulverização aérea de agrotóxicos", Agência Brasil, 16/07/2016, repórter Edwirges Nogueira). O conteúdo é o relato de uma agricultora sobre a comunidade do Tomé: "A partir de 2012 [...] não houve novas aplicações devido à baixa intensidade das chuvas". A generalização para "a Chapada" e a explicação pela doença fúngica vêm da entrevista de Raquel Rigotto (MST, 06/10/2016), que li e que o texto não cita. IL-MINOR-1. A frase sobre o setor produtivo está sem citação e diz mais do que as declarações que li. IL-MINOR-2 |
| 6 | `ceara2018nascer` | Título e data conferem ("Ceará lança programa para reduzir mortes maternas e neonatais", 26 de março de 2018). O sítio é o do Hospital Geral Dr. César Cals, não o da Secretaria da Saúde; o programa é o Nascer no Ceará, apresentado pelo Governo do Ceará. IL-MINOR-7 |
| 7 | `ibge2017censoagro` | 2019 confere (o IBGE divulgou os resultados definitivos em 25/10/2019; a publicação é "Censo agropec., Rio de Janeiro, v. 8, 2019"). As tabelas 6851 e 6852 existem e cruzam tipologia com uso de agrotóxicos. Elas não identificam a banana; as que cruzam produtos da lavoura permanente com tipologia são a 6955 e a 6956. IL-MINOR-7 |
| 8 | "Não têm o avião" | **Sem base na fonte citada e com indício contrário no Censo de 2006.** IL-SERIOUS-1 |
| 9 | Inferência | MacKinnon e Webb (2018): confere no resumo ("is known to fail when the number of treated clusters is very small"). Hagemann (2025): confere (um único cluster tratado). Canay, Santos e Shaikh (2021): o resumo não diz que o resultado depende de variação interna ao cluster; texto não lido (nota). Achei também uma imprecisão antiga: Conley e Taber não admitem heterocedasticidade por tamanho de grupo; quem a trata é Ferman e Pinto. IL-MINOR-4 |
| 10 | Restrições | Cumpridas; ver tabela acima |
| 11 | Modos de falha | Nada muda; ver a seção do checklist |

## Phase A: Reference Verification Results

Das 44 chaves, 36 foram verificadas nas rodadas da v1 e não mudaram. As oito restantes:

| Chave | Existência | Campo a campo | Fonte |
|---|---|---|---|
| jones2020invasive | VERIFIED | Autor, título, *Land Economics*, v. 96, n. 2, p. 149-170, 2020: tudo confere | Crossref |
| rigotto2013trends | VERIFIED | Cinco autores, título, *Revista Brasileira de Epidemiologia*, v. 16, n. 3, p. 763-773, 2013: tudo confere | Crossref; SciELO |
| hagemann2025single | VERIFIED | Autor, título, *Review of Economic Studies*, v. 92, n. 6, p. 3968-3994, 2025: tudo confere | Crossref |
| canay2021wild | VERIFIED | Três autores, título, *Review of Economics and Statistics*, v. 103, n. 2, p. 346-363, 2021: tudo confere | Crossref |
| limoeiro2010lei1511 | VERIFIED | Número, data e ementa conferem com a página 1 do PDF. O endereço responde (HTTP 200) | PDF da Câmara Municipal, lido |
| agenciabrasil2016ceara | VERIFIED | Título e data conferem. Falta a autoria da reportagem (Edwirges Nogueira) | Página da Agência Brasil, lida |
| ceara2018nascer | VERIFIED | Título e data conferem. Autoria imprecisa: a página é do Hospital Geral Dr. César Cals | Página `hgcc.ce.gov.br`, lida |
| ibge2017censoagro | VERIFIED | Título e ano conferem. As tabelas citadas existem, mas não são as que identificam a banana por tipologia | API do SIDRA; publicação do IBGE |

**A0.** Não refiz o lote no Semantic Scholar para as quatro com DOI; usei Crossref e OpenAlex, que responderam.

## Phase B: Citation Context Verification Results

Contextos novos ou alterados:

| Chave | Local | O que o texto atribui | Resultado |
|---|---|---|---|
| calzada2023bananas | `01-introducao.tex:52-55` | déficit entre filhos de mães que moravam junto às plantações, expostas a fumigação intensa | Confere (resumo publicado e manuscrito) |
| calzada2023bananas | `01-introducao.tex:55-56` | "mesma classe de produto" | Nota: o manuscrito lista clorpirifós (inseticida) ao lado de ditiocarbamatos e triazóis (fungicidas) |
| calzada2023bananas | `02-contexto.tex:57-58` | aplicações se intensificam na estação chuvosa | Confere no manuscrito |
| calzada2023bananas | `03-referencial.tex:31-34` | cerca de 80 g; até 150 m; três meses ou mais; sem gradiente mais longe | Confere no manuscrito. O resumo publicado dá a faixa de 80 a 150 g; "cerca de 80" é a especificação principal |
| calzada2023bananas | `03-referencial.tex:49-51`; `05-metodologia.tex:104-105` | efeito nos dois primeiros trimestres e "nenhum no terceiro" | **Não confere na segunda parte.** IL-MEDIUM-1 |
| calzada2023bananas (implícita) | `07-ameacas.tex:58-59` | efeito "apenas a poucas centenas de metros" | Impreciso: 150 metros. IL-MINOR-5 |
| rigotto2013trends | `03-referencial.tex:35-37` | fruticultura irrigada contra agricultura familiar; piores indicadores; ecológico | Confere |
| jones2020invasive | `03-referencial.tex:41-42` | isola fungicidas | Confere no resumo |
| lichtenberg1988, helfand1995, skevas2012 | `03-referencial.tex:18-19` | "dimensão distributiva" | Skevas et al. não trata de distribuição. IL-MINOR-3 |
| conley2011, ferman2019inference | `05-metodologia.tex:236-238` | "admitem heterocedasticidade por tamanho de município" | Vale para Ferman e Pinto, não para Conley e Taber. IL-MINOR-4 |
| mackinnon2018wild | `05-metodologia.tex:235-236` | wild cluster bootstrap falha com poucos tratados | Confere no resumo |
| hagemann2025single | `05-metodologia.tex:239-240`; `03-referencial.tex:72` | caso-limite | Confere no resumo |
| canay2021wild | `05-metodologia.tex:240-241` | aplica-se à diferença tripla, com variação interna ao município | Acesso limitado: o resumo não diz isso |
| limoeiro2010lei1511 | `02-contexto.tex:82-85`; `06-dados.tex:59-60` | revoga e regula, com distâncias mínimas | Confere em fonte primária |
| agenciabrasil2016ceara | `02-contexto.tex:88-91` | voos cessaram na Chapada a partir de cerca de 2012 | Confere em parte. IL-MINOR-1 |
| ceara2018nascer | `02-contexto.tex:40` | programa estadual em 03/2018 | Confere |
| ibge2017censoagro | `05-metodologia.tex:107-111` | classificação por agricultura familiar; "não o avião" | A segunda parte não está na fonte. IL-SERIOUS-1 |
| denteh2022misclassification, callaway2024continuous, olden2022triple, arkhangelsky2021sdid, mapa2008in2, brasil2002decreto4074, ceara1993lei12228, ibge2006censoagro, ibgepam | `05-metodologia.tex`, vários | usos mantidos da v1, em frases reescritas | Conferem |

Continuam com acesso limitado: `weitzman1974` e `coase1960` (texto não lido) e `brainerd2014seasonal` (conferido na v1 por trechos; não baixado de novo).

## Phase C: Data Verification Results

### C1. Números e fatos datados do texto atual

| # | Afirmação | Local | Resultado | Fonte e tipo |
|---|---|---|---|---|
| 1 | 184 municípios | `02-contexto.tex:16`; `06-dados.tex:7-8` | Confere | primária (SIDRA, v1) |
| 2 | 36 estabelecimentos em 7 dos 184 municípios (Censo 2006) | `02-contexto.tex:75-77` | Confere | primária (SIDRA 1008, v1) |
| 3 | bananicultura na maior parte do estado; maioria sem registro de avião | `02-contexto.tex:78-80` | Confere | primária (169 de 184; 162 de 169) |
| 4 | tabela do PL 18/2015: 23 pontos; todos, todos, 18, 16, 4 | `02-contexto.tex:62-66` | Confere | primária para o PL (v1) |
| 5 | 23 a 32 g (Reynier e Rubin) | `03-referencial.tex:29-31` | Confere | primária, texto completo (v1) |
| 6 | cerca de 80 g; 150 m; três meses (Calzada et al.) | `03-referencial.tex:31-34` | Confere no manuscrito de março de 2023 | manuscrito, não a versão publicada |
| 7 | "poucas centenas de metros" | `07-ameacas.tex:58-59` | Não confere com o item 6 | idem |
| 8 | datas das leis estaduais, do PL 18/2015, da ADI 6137 | `02-contexto.tex:9-25`, `:35-45` | Conferem | primárias (v1) |
| 9 | PL nº 134, maio de 2011 | `02-contexto.tex:38` | Confere | primária (ALECE, v1) |
| 10 | Lei municipal 1.478, 20/11/2009; Lei 1.511, maio de 2010, revoga e regula | `02-contexto.tex:36-37`, `:82-85` | Confere | **primária, lida nesta rodada** |
| 11 | 2012-2017: seca; relatos de suspensão dos voos | `02-contexto.tex:39`, `:88-91` | Confere, com a ressalva do IL-MINOR-1 | secundária externa (Agência Brasil; MST) |
| 12 | 03/2018: programa estadual de saúde materna e neonatal | `02-contexto.tex:40` | Confere | primária (página do governo estadual) |
| 13 | relatórios do MAPA "de 2012 a 2018", CE e RN | `05-metodologia.tex:151-154` | É pedido a fazer, não fato; o conteúdo do relatório confere com a IN (v1) | -- |
| 14 | plano de setembro de 2026; rodada exploratória; alvo revisto da curva para o nível | `05-metodologia.tex:254-257` | Confere | secundária interna (`docs/pre-especificacao.md` §0, §4 e §8) |

### C2. Consistência interna

1. **Distância.** `03-referencial.tex:32` diz "a até 150 metros"; `07-ameacas.tex:58-59` diz "a poucas centenas de metros". IL-MINOR-5.
2. **Ordem do Quadro 1.** A linha "03/2018" (`02-contexto.tex:40`) vem antes da linha "24/02/2015" (`:41`). IL-MINOR-6.
3. **"Antes de qualquer contato com os desfechos do pós-lei"** (`05-metodologia.tex:130`; `:251-253`), ao lado da divulgação de que uma rodada exploratória da forma reduzida, que usa o pós-lei, já foi executada (`:254-257`). As frases se referem ao desenho de calendário, e o texto não diz que a troca de desenho principal veio depois dessa rodada. IL-MINOR-9.

O restante bate entre capítulos: desenho principal de calendário (`01:89-93`; `04:16-17`; `05:36-44`; `08:14-16`); dois primeiros trimestres (`05:41-42`, `:87`); terceiro trimestre como contraste (`04:29-30`; `05:104-105`; `07:26`); banana familiar como comparação e como tratamento falso (`04:16-17`, `:30-31`; `05:107-118`; `07:26`); painel a partir de 2005 (`06:9`; `08:37`).

**Para os pareceristas, não como issue:** o documento de 10/11 que serve de base ao projeto recomenda a agricultura familiar como tratamento falso, refinamento da dose e estratificação, e diz "Não usar como controle direto" (§6). O projeto a usa como grupo de comparação dentro da diferença tripla e justifica a diferença (`05-metodologia.tex:111-116`). É decisão do pesquisador; registro a divergência entre o documento-base e o texto.

### C3. Figure/Table Caption Fidelity

A Figura 1 (`05-metodologia.tex:46-85`) é nova e não tem Figure Package nem entrada de rastreio: nota *trace-unavailable* (consultiva). A legenda ("Diagrama causal do desenho de calendário") não afirma nada sobre dados. O documento de 10/11 registra que os diagramas não foram executados em ferramenta de verificação de grafos. Cinco quadros avulsos, como antes.

### C4. Experiment Provenance & Claim Alignment

"This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

D7 com a declaração `no_experiments_declared` e sem `experiment_provenance[]`: condições 1, 2, 3 e 5 não acionadas. Condição 4: como na rodada 4 da v1, limítrofe e, pela letra, não acionada (não há seção de Resultados nem métrica própria; a rodada exploratória é dita "não reportada"). Nenhuma linha de `experiment_alignment_results[]`.

## Phase D: Originality Verification Results

Nove sondagens de frase exata, uma por parágrafo, nos parágrafos novos ou reescritos de 02, 03, 04, 05 e 07 (9 de 27, 33%). Os parágrafos que não mudaram foram sondados na v1.

| Grade | Paragraph Count | Proportion |
|-------|----------------|-----------|
| ORIGINAL | 8 | 89% |
| COMMON_KNOWLEDGE | 1 | 11% |
| PARAPHRASE | 0 | 0% |
| CLOSE_MATCH | 0 | 0% |
| VERBATIM | 0 | 0% |

O COMMON_KNOWLEDGE é a distinção entre falha de implementação e falha do mecanismo, corrente em avaliação de políticas. O texto novo condensa o documento de 10/11, que é material do próprio projeto; não comparei os dois por sequências de palavras.

## Phase E: Claim Verification Results

**Claim Registry coverage sidecar (#737)**

Os oito arquivos `.tex` mudaram; os oito registros e relatórios foram refeitos.

- Status: `completed` (8 de 8 com replay PASS)
- Registry: `claim-registry/1.0`
- Candidate scope: citation-bearing + quantitative sentences only
- Candidate-unregistered count: 1 (`05-metodologia.tex:87`, intervalo `[0,1]` lido como citação; inspecionado, não é afirmação)
- Semantic extraction coverage: `not_machine_detectable`

| Arquivo | Afirmações | Não registrados | SHA-256 do rascunho | SHA-256 do registro | SHA-256 da cobertura |
|---|---|---|---|---|---|
| 01-introducao | 14 | 0 | 051aac1ad4381d7eca6d3a82b2d606e061fc6b11da7fb789f121d4cde4630c5e | 44847215acaf53a92ff3b3a8d2244a2515db0983b943de08ccf06ec437573200 | 77b0697081c06e5d8f7ec8bb71fad08a41e969261a32bbc355c102b14b139540 |
| 02-contexto | 19 | 0 | 2fcba62a521342c472fc54b54240dcfcf7f40f8f3cb29a0d3511532e6fea4335 | c551788732c53e3bfac144cfe4e93222ed4507b03e3a6d5ef645f9efdea9a0d8 | 770306085cefb07848672d31f3689d5710f023555a026112c8d3cad44d6e76b6 |
| 03-referencial | 14 | 0 | 2bf7e59bd1345781874828d5af49845fcf081c0c3b5ff6746f1f30a92779495f | a52335ef9e862d3bc4470323cc93f79fe72d08a84d8c7334b7ea2b4368d71cba | 1bb4f432269387e2b3dfdfc4514c4be89256a8188be8d23bb1b346d1edb6f891 |
| 04-objetivos | 0 | 0 | 308becdfa5877dd2baeb9a1736ab17ec20c528442563e94ad477183e8d26b223 | 42d005b2713f18f68f5a6369dd3c5fc80cd2d10bc6632dc8294fae46cbc384d9 | 34f38dc94be7cde8c76c932c3a30a900302ca1362621290f48b65529ea0af7df |
| 05-metodologia | 12 | 1 | 17bc2ced0bfd9dd60427cf695680392bf5b84d4e287d43d643ee459b7c2fd0e1 | 4575f0436308a5ccaac058f0eadd2b72c7d875e86f8cbd5d4fd24341dcf27633 | 1e8b2f01dc4c7ad0932d2120a3f700f03311dcbabaa69aa161131d7354dc04ca |
| 06-dados | 4 | 0 | 6c4a07a4632742c8f663555bbe424f05967a8908acaf71ad5b9888f416b82613 | 7c094b44f9ff60e246eaec375093fcf95f6db1855c9a008c4274a6c584971990 | 29949e359ac2d20d569ed25466febb5a9e573978a90f822728ab69d3ca9fd1ad |
| 07-ameacas | 1 | 0 | 1d43b85bbcae468606ff4f4e6496bf3af3957dc4a6d55b87378ddab8b65531ac | f75167d1dd6ffd33bca8738665dd6a36e64c6726505d1a165586770af4e9342a | 55a4a14db7af267a72309fc403797b3ee287acac1020fbfac57e73a7e3da3f6a |
| 08-cronograma | 1 | 0 | b3862e24831a7ae5412e970a0e914c18a3848667beaa9137197e825cb03771d3 | 0210acae857d9611c2063ca85163be96f12a6384653cc648640aeb67179c0805 | 7a25821817ffcd74a8df1d29f4539e840a283b429e65cb6ec7826bd331c8eb9f |

O detector continua quase cego a `\cite{}` e a unidades em português; `completed` quer dizer que a ferramenta rodou e foi validada, não que a extração esteja completa. As seções 04 e 07 têm hipóteses e ameaças, que não registrei como afirmações factuais, salvo uma.

| Verdict | Claim Count | Proportion |
|---------|------------|-----------|
| VERIFIED | 46 | 75% |
| MINOR_DISTORTION | 5 | 8% |
| MAJOR_DISTORTION | 0 | 0% |
| UNVERIFIABLE | 1 | 2% |
| UNVERIFIABLE_ACCESS | 9 | 15% |

Critério, o mesmo da v1: VERIFIED quando o resumo da versão citada, o texto completo ou a fonte primária contém a afirmação. **Para Calzada et al., a versão citada é o artigo publicado, que não li.** As afirmações que só pude conferir no manuscrito de março de 2023 ficam como UNVERIFIABLE_ACCESS, com o que o manuscrito diz anotado em cada linha; não dei veredito de apoio com base nele. A issue IL-MEDIUM-1 também se apoia no manuscrito, e isso está dito nela.

Afirmações que não são VERIFIED:

| ID | Local | Afirmação (resumida) | Veredito | Motivo |
|---|---|---|---|---|
| H07 | `05-metodologia.tex:110-111` | banana familiar não tem o avião, "tecnologia da produção empresarial irrigada" | UNVERIFIABLE | A fonte citada não registra método de aplicação; indício contrário no Censo de 2006 |
| H03 | `02-contexto.tex:88-91` | relatos de 2016: voos cessaram na Chapada desde cerca de 2012 | MINOR_DISTORTION | A fonte citada fala da comunidade do Tomé; a segunda fonte não é citada |
| H04 | `02-contexto.tex:91-93` | setor produtivo: aplicações no Cariri e na Chapada até 2018, em anos chuvosos | MINOR_DISTORTION | Sem citação; só o Cariri tem data; "em anos chuvosos" não está nas declarações lidas |
| C12 | `03-referencial.tex:18-19` | dimensão distributiva | MINOR_DISTORTION | Skevas et al. não trata disso |
| H10 | `05-metodologia.tex:236-238` | Conley e Taber e Ferman e Pinto admitem heterocedasticidade | MINOR_DISTORTION | Só Ferman e Pinto |
| H14 | `07-ameacas.tex:58-59` | efeito a "poucas centenas de metros" | MINOR_DISTORTION | 150 metros |
| C06 | `01-introducao.tex:55-56` | mesma classe de produto | UNVERIFIABLE_ACCESS | manuscrito: inseticida e fungicidas |
| C08 | `02-contexto.tex:57-58` | estação chuvosa | UNVERIFIABLE_ACCESS | confere no manuscrito |
| C15 | `03-referencial.tex:31-34` | 80 g; 150 m; três meses | UNVERIFIABLE_ACCESS | confere no manuscrito |
| C18 | `03-referencial.tex:49-52` | dois primeiros trimestres; nenhum no terceiro | UNVERIFIABLE_ACCESS | primeira parte confere no manuscrito; a segunda, não |
| H08 | `05-metodologia.tex:104-105` | o análogo não encontra efeito no terceiro trimestre | UNVERIFIABLE_ACCESS | idem |
| H12 | `05-metodologia.tex:240-241` | Canay et al. na diferença tripla | UNVERIFIABLE_ACCESS | o resumo não basta |
| C07, C10, C11 | `01-introducao.tex:59-61`; `03-referencial.tex:13-14`, `:16-18` | Weitzman; Coase | UNVERIFIABLE_ACCESS | texto não lido |

**Persisted Phase E evidence rows (#656)**

- `docs/ars/pipeline-rodada20/evidence/evidence_rows.json` (SHA-256 `d9243ce749e43bf2e2834f8d5bb3d9c4872498d462c555e64b47d84504e55868`), com `checked: 61` e `verified: 46`.
- 76 linhas: 56 `agent_extracted`, 5 `access_failed`, 15 `anchorless`. `evidence_rows.py validate evidence_rows.json --source-dir sources`: "PASS: 76 evidence row(s)".
- `phases.E_claims.evidence_source_dir`: `docs/ars/pipeline-rodada20/evidence/sources`, com 39 arquivos. Removi `cameron2008wild.txt`, que eu mesmo havia gravado e que nenhuma linha referencia mais.
- `sources_manifest.json` (SHA-256 `ab9d83a7e37b211d9a4a8b55b13ac51c9505ca4f0a5af556b39bce4e56c5391e`) descreve cada fonte. Três merecem atenção: a de `calzada2023bananas` é o **manuscrito de março de 2023**, não o artigo publicado; a de `limoeiro2010lei1511` é uma **transcrição parcial minha**, feita das imagens das páginas 1, 65 e 66, porque o PDF não tem camada de texto; a de `ibgepam` é a resposta do SIDRA para a tabela 5457.
- A pasta contém texto integral de terceiros (o manuscrito de Calzada et al., o NBER WP 32117, o arXiv 2207.11890v3, o artigo de Reynier e Rubin). Direitos de redistribuição não avaliados.

**Scope-conformance advisory (#547)**: `[E4-SKIPPED: no scope context]`

| ID | Claim location | Effective scope | Drafted scope | Broadened axis |
|----|---------------|-----------------|---------------|----------------|
| -- | -- | -- | -- | -- |

**Novelty-claim classification (#548)** — advisory-only, not counted in verdicts or the gate decision:

| ID | Claim location | Claim wording | Classification | Nearest prior work / recommended bounded rewording |
|----|---------------|--------------|----------------|---------------------------------------------------|
| ADV-E5-1 | `01-introducao.tex:14-15` | "na primeira proibição estadual do gênero no Brasil" | UNRESOLVED | Citar a fonte, ou "apontada como a primeira" |
| ADV-E5-2 | `01-introducao.tex:23-24`; `:58-59` | "praticamente não há evidência causal no país"; "O que nenhum desses trabalhos oferece" | UNRESOLVED | "entre os trabalhos revisados" |
| ADV-E5-3 | `01-introducao.tex:86-87` | "registros administrativos nunca explorados para esse fim" | UNRESOLVED | "que não localizamos em uso para esse fim" |
| ADV-E5-4 | `08-cronograma.tex:9-11` | "a primeira medida municipal e mensal da aplicação aérea de agrotóxicos no Ceará antes da proibição" | UNRESOLVED; com "e mensal", o Censo de 2006 deixa de ser contraexemplo | "a primeira medida municipal e mensal de que temos notícia" |
| ADV-E5-5 | `03-referencial.tex:41-42` | "entre os poucos estudos que isolam fungicidas" | UNRESOLVED | "um dos estudos que isolam fungicidas" |

**Cache staleness advisory (#541)**: nenhuma linha servida de cache.

| ID | Citation key | Cache age (days) | Threshold | Re-verified live? |
|----|-------------|------------------|-----------|-------------------|
| -- | -- | -- | -- | -- |

**Claim-strength drift review (#569)**: `[E6-SKIPPED: no revision evidence]`. O projeto_v2 é reescrita, não rodada de revisão com bundle.

**Token-conservation advisory (#570)**: não executado.

## Issue List (Sorted by Severity)

IDs novos, deste relatório.

### SERIOUS (Must Fix)

| ID | # | Category | Location | Issue Description | Correct Information | Source |
|----|---|----------|----------|------------------|--------------------|----|
| IL-SERIOUS-1 | 1 | Claim (H07, UNVERIFIABLE) | `paper/projeto/secoes/05-metodologia.tex:107-111`; a mesma premissa em `01-introducao.tex:90-91`, `04-objetivos.tex:16-17` e `:30-31`, `05-metodologia.tex:117-118` | O texto afirma, logo depois de citar o Censo Agropecuário de 2017, que os municípios de banana predominantemente familiar "têm a cultura, o clima e o calendário agrícola, mas não o avião, que é tecnologia da produção empresarial irrigada". O Censo de 2017, nas tabelas citadas, não registra método de aplicação; o documento de 10/11 diz que não se achou em 2017 equivalente à tabela de 2006. No Censo de 2006, que o projeto usa, 5 dos 7 municípios com aplicação por aeronave estão fora dos polos irrigados: Aiuaba (5 estabelecimentos), Jaguaruana, Mauriti, Quiterianópolis e Quixeramobim (1 cada). Quiterianópolis é município controle, de agricultura familiar, em Rigotto et al. (2013) | Escrever como hipótese e dizer como será verificada: "supõe-se que não tenham aplicação aérea, o que se verifica nos relatórios do MAPA e no Censo de 2006; municípios com qualquer registro de aeronave são excluídos do grupo de comparação". Citar o Censo de 2006 para o que se sabe. Para classificar a banana por tipologia, citar as tabelas 6955 e 6956 | SIDRA, tabela 1008 (consulta da v1); SIDRA, tabelas 6851, 6852, 6955 e 6956 (cabeçalhos consultados nesta rodada); `docs/pdf/2026-11-10-desenho-consolidado-chapada-sutva-dags.pdf`, §6; SciELO, Rigotto et al., Tabela 1 |

### MEDIUM (Must Fix)

| ID | # | Category | Location | Issue Description | Correct Information | Source |
|----|---|----------|----------|------------------|--------------------|----|
| IL-MEDIUM-1 | 1 | Citation context (C18, H08) | `paper/projeto/secoes/03-referencial.tex:49-50`; `05-metodologia.tex:104-105`; reflete em `04-objetivos.tex:29-30` e `07-ameacas.tex:26` | "encontram efeito nos dois primeiros trimestres e nenhum no terceiro"; "o análogo equatoriano não encontra efeito". No manuscrito de março de 2023, o termo do terceiro trimestre na especificação conjunta é "negative and non-significant" (a tabela traz −43 g, erro-padrão 38); para meninos há déficit de 87,7 g e 75,6 g no segundo e no terceiro trimestres; uma análise de robustez dá 30,3 g e 17,7 g no segundo e no terceiro. O projeto usa o terceiro trimestre como contraste de falsificação. **Base: o manuscrito, não o artigo publicado** | "efeito no primeiro e no segundo trimestres; no terceiro, estimativa negativa e sem significância estatística na especificação principal". Rebaixar o terceiro trimestre de "falsificação" a contraste em que se espera efeito menor, ou justificar. Conferir no PDF publicado (JAERE 10(6), Tabela 3 e seção 5) antes de fechar | `https://diposit.ub.edu/server/api/core/bitstreams/73f71bc2-9e61-4f15-a2de-a58cb08d43ac/content`, seção 5 e Tabela 3 |

### MINOR (Recommended Fix at Stage 2.5; Must Fix at Stage 4.5)

| ID | # | Category | Location | Issue Description | Suggestion |
|----|---|----------|----------|------------------|----|
| IL-MINOR-1 | 1 | Citation context (H03) | `02-contexto.tex:88-91` | A fonte citada é o relato de uma agricultora sobre a comunidade do Tomé. "Na Chapada" e a explicação pela doença fúngica vêm da entrevista de Raquel Rigotto (MST, 06/10/2016), não citada | "relatos de 2016, de uma moradora do Tomé e de uma pesquisadora, afirmam [...]"; acrescentar a entrevista às referências |
| IL-MINOR-2 | 2 | Unsourced claim (H04) | `02-contexto.tex:91-93` | Sem citação. Na reportagem que li (Globo Rural, 09/04/2021), só o produtor do Cariri data o uso ("até 2018, fazia duas aplicações aéreas anuais"); o da Chapada descreve a prática sem data. "Em anos chuvosos" não está nas declarações | "um produtor do Cariri declara duas aplicações aéreas anuais até 2018; produtores da Chapada descrevem a prática sem datar o último voo"; citar a reportagem. O relatório do SINDAG de ago/2019 não foi lido por mim |
| IL-MINOR-3 | 3 | Citation context (C12) | `03-referencial.tex:18-19` | Skevas et al. citado para "dimensão distributiva"; o artigo trata da eficácia de instrumentos | Tirar `skevas2012` dessa citação ou devolver a frase da v1 ("a comparação, por simulação, entre cotas e taxas") |
| IL-MINOR-4 | 4 | Citation context (H10) | `05-metodologia.tex:236-238` | "que admitem heterocedasticidade por tamanho de município" atribuído a Conley e Taber e a Ferman e Pinto | "os procedimentos de Conley e Taber e, por admitir heterocedasticidade por tamanho de município, o de Ferman e Pinto" |
| IL-MINOR-5 | 5 | Data / consistency (H14) | `07-ameacas.tex:58-59` | "a poucas centenas de metros" contra "a até 150 metros" em `03-referencial.tex:32` | "a até 150 metros do bananal" |
| IL-MINOR-6 | 6 | Internal consistency | `02-contexto.tex:39-41` | Quadro 1 fora de ordem: "03/2018" antes de "24/02/2015" | Mover a linha de 03/2018 para depois da de 24/02/2015 |
| IL-MINOR-7 | 7 | Reference | `referencias-projeto.bib`: `ceara2018nascer`, `agenciabrasil2016ceara`, `ibge2017censoagro` | `ceara2018nascer`: a página é do Hospital Geral Dr. César Cals. `agenciabrasil2016ceara`: falta a autoria (Edwirges Nogueira). `ibge2017censoagro`: as tabelas 6851 e 6852 não identificam a banana por tipologia. As três sem data de acesso | Autor "Ceará. Hospital Geral Dr. César Cals" ou "Ceará. Governo do Estado"; "NOGUEIRA, Edwirges" na notícia; acrescentar as tabelas 6955 e 6956; "Acesso em" nas três |
| IL-MINOR-8 | 8 | Reference format (vem da v1) | `referencias-projeto.bib` | Dez entradas normativas e estatísticas sem endereço eletrônico e data de acesso; três sem data de publicação oficial; ano de publicação do Censo Agropecuário 2006 não conferido | Como nos relatórios das rodadas 3 e 4 da v1 |
| IL-MINOR-9 | 9 | Disclosure / consistency | `05-metodologia.tex:130`; `:251-257` | "Antes de qualquer contato com os desfechos do pós-lei" convive com a rodada exploratória da forma reduzida, que usou o pós-lei. O texto não diz que o desenho de calendário passou a principal depois dessa rodada; o documento de 10/11 admite isso (§7, item 1) | "Antes de qualquer contato do desenho de calendário com os desfechos do pós-lei"; e uma oração em `:254-257`: "o desenho de calendário passou a principal depois dessa rodada" |

## AI Research Failure Mode Checklist

Declaração no passport: `no_experiments_declared`, com a resposta de intake citada nos relatórios da v1. Na rodada 4 da v1, os Modos 1, 3 e 6 ficaram bloqueados pela regra da declaração, e o pesquisador anulou o bloqueio. O passport registra, em `failure_mode_overrides`, as palavras dele: "como é um projeto de pesquisa essa parte vai ser feita ao longo do ano, então é só o que eu vou fazer".

O que o texto novo apresenta como feito pelo autor é um subconjunto do que a v1 apresentava: o plano de setembro de 2026 e a rodada exploratória (`05-metodologia.tex:254-257`), o levantamento preliminar de leis municipais (`06-dados.tex:58-60`) e a avaliação preliminar de duas bases (`06-dados.tex:65-67`). Saíram o diagnóstico de dose e o cálculo preliminar de poder. Nada novo entra nessa categoria.

| Mode | Outcome (CLEAR / NOT APPLICABLE / SUSPECTED / INSUFFICIENT EVIDENCE) | Evidence | Blocks? |
|------|---------|----------|---------|
| 1. Implementation bug passing AI self-review | INSUFFICIENT EVIDENCE, coberto pelo override registrado | A regra da declaração retira o NOT APPLICABLE, como na v1. Sem logs nesta sessão. O texto não reporta número saído das análises preliminares; os números de fonte pública foram refeitos na v1 | no (override de 2026-11-15 em vigor; nada novo) |
| 2. Hallucinated citation | CLEAR | 44 de 44 referências existem; as oito novas na lista conferem campo a campo, com três imprecisões menores | no |
| 3. Hallucinated experimental result | SUSPECTED pela regra, coberto pelo override registrado | Mesma discordância entre declaração e rascunho. No mérito: nenhum resultado próprio é reportado, e as três menções conferem com documentos versionados | no (idem) |
| 4. Shortcut reliance | CLEAR (flag-only neste estágio) | O texto trata como ameaças a diluição, a seca e a possibilidade de o bananal irrigado não ter estação | no |
| 5. Implementation bug reframed as novel insight | CLEAR | Nenhuma linguagem de surpresa; nenhum achado anunciado | no |
| 6. Methodology fabrication | SUSPECTED pela regra, coberto pelo override registrado | Mesma discordância. No mérito: a divulgação da rodada exploratória e da revisão do alvo confere com `docs/pre-especificacao.md`; o desenho novo é descrito no futuro e nada no repositório indica que tenha sido rodado (o documento de 10/11 diz que `14_mde_calendario.py` "nunca rodou com dado real") | no (idem) |
| 7. Frame-lock at early pipeline stage | INSUFFICIENT EVIDENCE | O desenho mudou, o que pesa contra travamento. Mas o desenho novo apoia-se em três premissas que esta verificação não conseguiu confirmar: os municípios de banana familiar não terem avião (IL-SERIOUS-1); o terceiro trimestre servir de falsificação (IL-MEDIUM-1); o bananal irrigado do semiárido ter estação de pulverização (o próprio texto a trata como hipótese). E o documento-base desaconselha a agricultura familiar como controle direto | no (segue com aviso; reavaliar no 4.5) |

**Resultado do checklist:** nenhum bloqueio novo. O override dos Modos 1, 3 e 6 continua valendo porque o texto não acrescentou análise própria; deve ser reavaliado no Estágio 4.5 e relatado no Estágio 6.

Uma observação, sem reabrir o que foi decidido: as palavras do override ("essa parte vai ser feita ao longo do ano, então é só o que eu vou fazer") descrevem trabalho futuro, e o texto do projeto continua dizendo que uma rodada exploratória "já foi executada". As duas coisas convivem no registro.

## Tool Limitation Disclaimer

> This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 33% dos parágrafos novos ou reescritos, and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.

Limitações específicas:

1. **Calzada et al.** Li o manuscrito de março de 2023, não o artigo publicado no JAERE. As tabelas do apêndice online não foram lidas. A IL-MEDIUM-1 depende dessa leitura.
2. **Não lidos:** Weitzman (1974); Coase (1960); o texto completo de Canay, Santos e Shaikh (2021), de Hagemann (2025), de Jones (2020) e de MacKinnon e Webb (2018), dos quais li só o resumo; Brainerd e Menon (2014) nesta rodada.
3. **Lei 1.511/2010:** li as páginas 1, 65 e 66 de 68, como imagem. Não li as demais nem verifiquei alterações posteriores da lei; "legal e regulada até a lei estadual" (`02-contexto.tex:85`) supõe que não houve.
4. **Fontes do documento de 10/11 que não abri:** relatório do SINDAG de ago/2019; SINDAG de 2023 e lista de operadores de 2018; estudos da ANA sobre o aquífero; texto da SDH de 11/03/2011; artigo sobre chikungunya; Portaria MAPA 298/2021. A reportagem da Agência Pública foi baixada e não traz data de último voo.
5. **Censo de 2017:** conferi a existência e as dimensões das tabelas 6851, 6852, 6955 e 6956; não baixei dados municipais nem classifiquei municípios por participação familiar. Não sei quais municípios cairiam no grupo de comparação.
6. **As 36 referências antigas** não foram reverificadas do zero; as 29 entradas não citadas dos `.bib` seguem sem verificação.
7. **Fase D:** só parágrafos novos; D2 não refeita; sem comparação por sequências de palavras com o documento de 10/11.
8. **Documentos de 10/11:** li o de desenho consolidado quase inteiro (texto extraído); do de DAGs, só o que o primeiro reproduz. Não conferi a Figura 1 contra os DAGs do documento.
9. E4 e E6 pulados; conservação de tokens não rodada; sem verificação cruzada entre modelos; `content_hash_v2` do passport não conferido; PDF não recompilado.

## Verification Audit Trail

Projeto_v2, rodada 1, 2026-11-15, concluída às 22:53Z.

**Fase A.** `GET https://api.crossref.org/works/<doi>` e `https://api.openalex.org/works/doi:<doi>` para 10.3368/le.96.2.149, 10.1590/S1415-790X2013000300019, 10.1093/restud/rdaf002 e 10.1162/rest_a_00887: quatro respostas, campos iguais aos do `.bib`. Chaves citadas: 44; `\bibitem` em `projeto.bbl`: 44.

**Fontes documentais baixadas e lidas.**
- `https://www.camaralimoeirodonorte.ce.gov.br/arquivos/581/Leis_1511_2010_0000001.pdf`: HTTP 200, 28 MB, 68 páginas sem camada de texto; páginas 1, 65 e 66 convertidas em imagem e lidas.
- `https://agenciabrasil.ebc.com.br/geral/noticia/2016-07/ceara-pode-proibir-pulverizacao-aerea-de-agrotoxicos`: HTTP 200; título, data, repórter e o trecho sobre 2012.
- `https://www.hgcc.ce.gov.br/2018/03/26/ceara-lanca-programa-para-reduzir-mortes-maternas-e-neonatais`: HTTP 200; título, data, programa Nascer no Ceará.
- `https://globorural.globo.com/Noticias/Agricultura/noticia/2021/04/pulverizacao-aerea-de-bananais-no-ce-e-alvo-de-acao-no-stf.html`: HTTP 200; declarações dos produtores do Cariri e da Chapada.
- `https://mst.org.br/2016/10/06/88-mil-litros-de-calda-toxica-sao-utilizados-todas-as-noites-no-cultivo-de-fruticultura-no-ceara`: HTTP 200; trecho sobre a seca e a sigatoka-amarela.
- `https://apublica.org/2019/02/antes-do-ceara-8-municipios-ja-haviam-proibido-fumigacao-aerea-de-agrotoxicos/`: HTTP 200; declarações do setor, sem data de último voo.

**Calzada et al.** Busca "Hidden Cost of Bananas ... 150 meters three months intensive fumigation" devolveu o depósito da UB; `GET https://diposit.ub.edu/server/api/core/bitstreams/73f71bc2-9e61-4f15-a2de-a58cb08d43ac/content`, HTTP 200, PDF de 1,4 MB com a data "March 2023" na capa; `pdftotext`; leitura dirigida das passagens sobre 150 metros, três meses, galões por hectare, estação chuvosa, gradientes, trimestres e compostos químicos. A versão publicada no sítio da editora exige assinatura.

**Rigotto et al.** Resumo no Crossref; trechos do texto em `https://www.scielo.br/j/rbepid/a/hmYrvFwdY4WLb5ZNPR68cjv?lang=pt` devolvidos pela busca (objetivo, metodologia, Tabela 1). O acesso direto por `curl` ao SciELO devolveu 403.

**Censo de 2017.** `GET https://apisidra.ibge.gov.br/values/t/<tabela>/n3/23/v/all/p/all` para 6851, 6852, 6953 a 6957: dimensões lidas no cabeçalho. Ano de divulgação: `agenciadenoticias.ibge.gov.br` (25/10/2019) e a publicação "Censo agropec., Rio de Janeiro, v. 8, p. 1-105, 2019".

**Censo de 2006.** Resposta do SIDRA para a tabela 1008 guardada na v1: Aiuaba 5, Jaguaruana 1, Limoeiro do Norte 18, Mauriti 1, Quiterianópolis 1, Quixeramobim 1, Quixeré 9.

**Documentos de 10/11.** `pdftotext -layout` dos dois PDFs em `docs/pdf/`; leitura das seções 1 a 9 do documento 20, das seções 0 a 4 do documento 22 e da bibliografia (documento 21), incluída a lista de fontes documentais das páginas 27 e 28.

**Fase D.** Nove buscas de frase exata (WebSearch): `02-contexto` (1), `03-referencial` (1), `04-objetivos` (1), `05-metodologia` (5), `07-ameacas` (1). Nenhuma devolveu o trecho.

**Fase E.** Registro por arquivo com spans de bytes; `claim_registry_coverage.py` com `--output` e depois `--validate-report` (8 de 8 PASS); linhas com `evidence_rows.build(...)`; `evidence_rows.py validate evidence_rows.json --source-dir sources` (PASS, 76 linhas); 61 `claim_id` distintos, igual a `checked`; 46 VERIFIED, igual a `verified`; nenhuma linha para as 4 NOT-SELECTED.

**Páginas e números.** `pdfinfo` (21); `projeto.toc` (capítulo 1 na página 3; referências na 18); `pdftotext` nas páginas 17 a 19; busca por padrões de estimativa nos `.tex`.
