# 20 — Revisão de literatura e Metodologia: Estágio 1 (RESEARCH)

*ARS `academic-pipeline` (`/ars-full`), Estágio 1 = `deep-research`, modo `full`
na Fase 1 e, a partir da escolha do pesquisador (§5), modo `systematic-review`.
2026-10-11.*

> **Estado do pipeline.** Estágio 1 · RQ Brief confirmado; forma da revisão
> escolhida (sistemática, §5); protocolo PRISMA-P em preparação. Nada foi escrito
> em `paper/` ainda.
>
> **Como o pipeline está rodando, e por que isso fica registrado.** O plugin ARS
> não está instalado na sessão remota. O orquestrador é executado seguindo os
> `SKILL.md` e os arquivos de agente do repositório `Imbad0202/academic-research-skills`,
> **fixado no commit `d1e5171` (v3.23.0, 2026-10-03)**, e não a versão que estiver
> instalada na máquina local. O Crossref e o OpenAlex devolvem 403 no proxy da
> sessão; a conferência de DOI na Fase 2 usa outras rotas e registra qual foi
> usada, como em `docs/referencias-verificadas.md` §8. Os gates opcionais que
> mandam conteúdo a modelo externo (`ARS_AUDIT_ARTIFACT_GATE`, `ARS_CROSS_MODEL`)
> ficam **desligados**.
>
> **Decisões do pesquisador que valem para o pipeline inteiro (2026-10-11):**
> pipeline completo; capítulo **novo** de revisão de literatura e o
> `04-identificacao.tex` **reescrito como Metodologia**; revisão cobrindo os
> **Ensaios 1 e 2**.

---

## 1. Research Question Brief

### Área
Externalidade negativa da pulverização aérea de agrotóxicos: dano à saúde
perinatal (Ensaio 1) e escolha do instrumento que a regula (Ensaio 2), a partir
do banimento estadual do Ceará (Lei 16.820/2019).

### Pergunta principal da revisão
**Em que medida a literatura existente permite quantificar o dano perinatal da
pulverização aérea de agrotóxicos com a precisão que a escolha entre proibir,
taxar e zonear o método exigiria?**

Ela é deliberadamente uma pergunta **sobre a literatura**, não a pergunta da
tese (essa está fixada: CLAUDE.md, `docs/pre-especificacao.md`). O que ela
decide é o que o capítulo de revisão tem de sustentar: o Ensaio 1 só se
justifica se a resposta for "não o suficiente", e o Ensaio 2 só tem âncora se
houver algum parâmetro de dano que a literatura, ou o Ensaio 1, entregue.

### Avaliação FINER

| critério | nota | justificativa |
|---|---|---|
| Feasible | 5/5 | corpus semente já existe (47 entradas no `.bib`, `estado-da-arte.md`, `lista-leitura.md`, docs ARS 01/05/13/19); busca complementar alcançável pelas ferramentas da sessão |
| Interesting | 4/5 | a tensão é real: a literatura causal mais forte é sobre **molécula** (glifosato, culturas GM), e o ban proíbe **método**; os análogos de método (Camacho & Mejía; Calzada et al.) são de outro contexto |
| Novel | 3/5 | revisão não produz evidência nova; a novidade está em cruzar a literatura de dano com a de instrumento e em mostrar que o parâmetro que Weitzman pede não está estimado para o método |
| Ethical | 5/5 | revisão de fontes publicadas; sem sujeitos |
| Relevant | 5/5 | ADI 7794 e sucessoras, projetos análogos em outros estados, ADI 5553/7755 (instrumento-preço) |
| **Média** | **4,4/5** | acima do limiar (≥ 3,0, nenhum critério < 2) |

### Limites de escopo

**Dentro:**
- estudos causais e quase-experimentais, em economia e epidemiologia, sobre exposição agrícola a agrotóxicos e desfechos ao nascer (peso, prematuridade, óbito fetal e infantil), com prioridade para os que identificam pelo **método de aplicação** ou pela **deriva**;
- o cânone de regulação ambiental → saúde infantil, só no que ele ensina sobre desenho;
- literatura de método que o desenho usa: DiD com tratamento contínuo, choque simultâneo, inferência com poucos clusters, erro de classificação do tratamento, controle sintético, instrumento de aptidão agroclimática;
- escolha de instrumento aplicada a agrotóxicos: taxação, proibição, zonas-tampão, poluição difusa;
- literatura brasileira e cearense sobre a Chapada do Apodi e o uso de agrotóxicos, tratada como contexto e evidência descritiva.

**Fora:**
- toxicologia e mecanismo biológico além do que o Background já usa (o `02-background.tex` cobre a deriva e o químico);
- saúde ocupacional de adultos, exceto como canal (SIH/SINAN);
- canal-água como evidência principal: o SISAGUA está suspenso (CLAUDE.md), e a literatura de água entra só como desenho (DRS 2023, Sorensen 2025);
- teoria de externalidade e Weitzman em si: já estão no `03-teoria.tex`. A revisão cobre a literatura **aplicada** que usa essa teoria, sem repetir a derivação.

**Domínio:** economia ambiental e da saúde aplicada; econometria de avaliação de impacto.
**Período:** literatura de 1960 (Coase) a 2026; estudos empíricos de exposição concentrados em 2000–2026.
**Geografia:** global, com prioridade para América Latina e Brasil.
**População:** gestantes e nascidos vivos (Ensaio 1); produtores rurais e reguladores (Ensaio 2).

**Hipóteses de que a revisão parte:**
- o desenho da tese está fixado e a revisão **não** o reabre (CLAUDE.md, "Perguntar antes de mudar a estratégia de identificação");
- desde 2026-09-22 o resultado principal é o `ATT(d|d)`, e a curva é secundária (`pre-especificacao.md` §8). A revisão não pode prometer ao Ensaio 2 uma curva que o Ensaio 1 não entrega.

### Sub-perguntas

1. **(Ensaio 1, evidência)** O que os desenhos causais publicados estimam sobre a exposição agrícola a agrotóxicos e os desfechos ao nascer, e quanto cada estimativa se transfere ao caso cearense, que tem método aéreo, fungicida em banana e cultura não-GM?
2. **(Método)** Que estimadores e hipóteses a literatura de diferenças-em-diferenças oferece para um choque simultâneo com intensidade contínua, tratamento mal classificado e poucos controles?
3. **(Ensaio 2)** Que forma da função de dano a literatura de escolha de instrumento para agrotóxicos supõe, e qual parâmetro empírico ela exige para ordenar proibição, taxação e zonas-tampão?

### Vínculos das sub-perguntas (#547)
1. herda: domínio = economia ambiental/saúde aplicada; população = gestantes e nascidos vivos; geografia = global, prioridade América Latina/Brasil; período = 2000–2026. Desvios: nenhum.
2. herda: domínio = econometria de avaliação de impacto; período = literatura de método até 2026. Desvio: **sem restrição de população nem de geografia**, porque a literatura de método não é de domínio. ⬜ Desvio a aprovar pelo pesquisador neste checkpoint.
3. herda: domínio = economia ambiental; população = produtores e reguladores; geografia = global. Desvios: nenhum.

### Perguntas candidatas consideradas

| # | candidata | FINER | por que não |
|---|---|---|---|
| 1 | *a selecionada* | 4,4 | selecionada |
| 2 | "Qual é o efeito da exposição a agrotóxicos sobre o peso ao nascer?" | 3,6 | é pergunta de meta-análise; não conversa com o Ensaio 2 nem com o método |
| 3 | "O que a literatura diz sobre a Lei Zé Maria do Tomé?" | 2,8 | quase não há literatura econômica sobre ela; é Background, não revisão |
| 4 | "Proibição ou taxação: o que a literatura recomenda para agrotóxicos?" | 3,8 | deixa o Ensaio 1 sem justificativa e pressupõe que a literatura recomende algo |

---

## 2. Methodology Blueprint

Duas camadas, porque o pipeline produz dois capítulos: (a) **o método da revisão**
e (b) **o método da tese**, que o capítulo de Metodologia vai reorganizar sem
alterar.

### 2a. Método da revisão
- **Paradigma:** positivista/pragmático. A revisão serve a uma estratégia causal.
- **Desenho:** a forma da revisão (sistemática, de escopo, narrativa/integrativa, rápida ou nenhuma formal) é **escolha do pesquisador**, e o ARS a pergunta logo depois da confirmação deste brief.
- **Dados:** secundários. Corpus semente = `paper/referencias.bib` (47 entradas, 25 citadas no texto hoje), `docs/estado-da-arte.md` (blocos A′–D′, E–G), `docs/lista-leitura.md`, `docs/ars/01-3w-scan.md`, `05`, `13` e `19` §§3–4. A Fase 2 complementa por busca documentada.
- **Quadro analítico:** síntese temática em cinco blocos, um por sub-pergunta e contexto:
  A. agrotóxicos/deriva → saúde perinatal (SQ1);
  B. regulação ambiental → saúde infantil, pelo desenho (SQ1);
  C. Brasil/Ceará: Chapada do Apodi, ABRASCO, Rigotto (SQ1, contexto);
  D. método (SQ2);
  E. escolha de instrumento para agrotóxicos (SQ3).
  Para cada estudo: o que identifica (molécula, método, cultura, distância), como identifica, magnitude e **transferibilidade** ao Ceará.
- **Validade:** busca e critérios de inclusão escritos antes de olhar resultados; registro de resultados nulos e contrários (ver DA, item M2); toda referência citada conferida contra fonte primária ou índice, com a rota registrada.

### 2b. Método da tese (mapa para o capítulo de Metodologia; **nada aqui muda o desenho**)

| componente | o que está fixado | fonte |
|---|---|---|
| Paradigma | positivista; inferência causal com dado observacional | CLAUDE.md |
| Método | quase-experimento: choque estadual **simultâneo** (vigência em 09/01/2019), intensidade **contínua** de exposição pré-ban | CLAUDE.md; `04-identificacao.tex` |
| Estimando primário | `ATT(d\|d)` (nível), desde 2026-09-22; a curva `ACR(d)` fica secundária e exige SPT | `pre-especificacao.md` §8 |
| Estimador | Callaway, Goodman-Bacon & Sant'Anna (2024), via `contdid` em `Rscript` isolado | CLAUDE.md |
| Dose | área de banana (PAM, média 2015–2018), janela 2010–2014 como sensibilidade | `pre-especificacao.md` §§3–4 |
| Zero | definição 4 (baixa aptidão GAEZ) primária, definição 2 sensibilidade | `pre-especificacao.md` §4 e §8 |
| Desfecho | peso médio, município × ano-mês; óbito fetal confirmatório | `pre-especificacao.md` §§1, 6 |
| Exposição | `share_gestacao_pos_ban`; corte das coortes que atravessam o ban | `pre-especificacao.md` §§2, 4 |
| Antecipação | três marcos: 24/02/2015, 18/12/2018, 09/01/2019 | `docs/ars/06` |
| Inferência | poucos clusters; o grupo escasso é o de **controle** (15 com área nula); jackknife, wild bootstrap, Conley–Taber | CLAUDE.md flag 4; `04_robustness.py` |
| Medida do tratamento | diluição: VPP 2/17 (Censo Agro 2006); Corolário 1 de Denteh & Kédagni; 🔴 nó de 2011 aberto | CLAUDE.md flag 7; `docs/ars/16`, `19` §2.3 |
| Robustez | SDiD; PSM+DiD como camada de comunicação; placebo SPT (`10_spt_pretrend.py`); Holm (`09_holm.py`) | CLAUDE.md; `pre-especificacao.md` §8 |
| Falsificação | piso de 15 g | `pre-especificacao.md` §5 |

**Validade (tese):**

| critério | estratégia |
|---|---|
| Validade interna | PT no D observado; placebo SPT; antecipação com três marcos; janela de dose recuada |
| Validade de construto do tratamento | Censo Agro 2006 (flag 5 testada; flag 7 aberta); LAI à ADAGRI e ao MAPA pendentes |
| Validade estatística | MDE *ex ante*; inferência que respeita os 15 controles; Holm na família confirmatória |
| Validade externa | o efeito é do **método** num estado de fruticultura irrigada não-GM; não se transfere a glifosato/soja sem argumento |

**Limitações de desenho:** diluição do tratamento (o mecanismo da falta de poder); exposição omitida no controle (controle vetorial aéreo, §2º do art. 28-B); seleção para nascimento vivo (flag 6).

**Ética e status de sujeitos humanos:** dado secundário administrativo (SINASC, SIM, SIH, SINAN), microdado nunca commitado e agregado a município × mês. ⚠️ Se a pesquisa precisa de apreciação por CEP, quem determina é a instituição (UFES/CEP), não o ARS. Este blueprint **não** declara dispensa.

**Padrão de reporte:** economia não adota checklist formal; os itens STROBE aplicáveis a desenho observacional servem de lista de conferência interna.

**Pré-registro:** **não há**, e o texto não pode sugerir que haja. O que existe é um *plano pré-estimação* (`pre-especificacao.md` §0), fechado em 2026-09-21, com tabela de desvios datada.

---

## 3. Devil's Advocate — Checkpoint 1

### Veredito: **PASS** (nenhum crítico; três maiores a endereçar na Fase 2)

### Problemas críticos
Nenhum identificado.

### Problemas maiores

**M1. A pergunta pode prometer ao Ensaio 2 o que o Ensaio 1 já não entrega.**
- *Tipo:* escopo / *bait-and-switch*.
- *Onde:* pergunta principal e SQ3.
- *Problema:* a pergunta é sobre "a precisão que a escolha de instrumento exigiria". Desde 2026-09-22 a tese não tem curva interpretável, e o `07-conclusao.tex` já tem uma subseção chamada "A âncora que o Ensaio 2 esperava, e que não veio". Uma revisão que termina em "a literatura não estima a curva, logo a tese a estima" seria falsa.
- *Recomendação:* a lacuna tem de ser escrita em dois tempos: o que falta na literatura e o que a tese consegue entregar (nível, limite superior, diagnóstico de desenho). Essa formulação entra no esboço do Estágio 2.

**M2. O corpus semente foi curado para o desenho, e isso é viés de confirmação estrutural.**
- *Tipo:* viés de seleção.
- *Onde:* §2a, dados.
- *Problema:* as 47 entradas do `.bib` e os blocos do `estado-da-arte.md` foram escolhidos em sessões que já defendiam este desenho. Estudos que não acham associação entre agrotóxico e peso ao nascer, ou que acham só na cauda (o próprio Larsen et al. 2017 não acha nada na média), tendem a ficar de fora.
- *Recomendação:* na Fase 2, busca com strings escritas antes, critérios de inclusão explícitos e uma coluna "resultado" na matriz que registre nulos e efeitos só na cauda; o relatório reporta quantos nulos entraram.

**M3. A transferibilidade é a questão central, e não pode virar nota de rodapé.**
- *Tipo:* validade externa.
- *Onde:* SQ1.
- *Problema:* a evidência causal mais forte é de glifosato/culturas GM (DRS 2023; Reynier & Rubin 2025) ou de herbicida sobre coca (Camacho & Mejía 2017). O análogo de cultura e método, Calzada et al. (2023), ainda **não teve o texto integral conferido** (doc 19 §3). Uma revisão que empilha magnitudes de contextos diferentes como se medissem a mesma coisa produz um "efeito esperado" sem fundamento.
- *Recomendação:* a matriz da Fase 2 classifica cada estudo por molécula × método × cultura × medida de exposição, e o texto compara só dentro de cada célula. Conferir o texto integral de Calzada et al. vira tarefa da Fase 2.

### Problemas menores
- O Bloco E pode duplicar o `03-teoria.tex`. Quando o esboço for montado, cada referência de E deve ser marcada como "nova" ou "já em teoria".
- Denteh & Kédagni (arXiv:2207.11890) sustentam a flag 7 e não estão no `.bib`. Exigem entrada como *working paper*, com a ressalva de `referencias-verificadas.md` §9.3.
- Reescrever o `04` é onde o desenho pode mudar sem querer. Recomendação: no Estágio 2.5, conferir item a item o texto novo contra a tabela §2b.

### Observações
- O 🔴 nó de 2011 (flag 7) é fato jurídico-administrativo, não literatura. A revisão não o resolve, e a Metodologia tem de declará-lo como ameaça aberta.
- A ADI 5553/7755 (instrumento-preço no STF) é a ponte mais original do Bloco E e quase não tem literatura econômica. Fica como lacuna a reportar, não a preencher.

### O contra-argumento mais forte
"A revisão é uma justificativa *post hoc* de um desenho que já falhou em ter poder: escolhe a literatura que explica por que o nulo é informativo, em vez de perguntar se o desenho deveria ter sido outro."
Resposta disponível: o projeto declarou o MDE *ex ante* (`pre-especificacao.md` §5; `06-diagnostico-poder.tex`), e a revisão vai incluir as rotas alternativas que a literatura sugere (calendário, poucos tratados contra doadores externos; doc 19 §5) **como literatura**, sem adotá-las como desenho.

### O que falta
- Evidência sobre **deriva medida** (distância × concentração) para aplicação aérea em banana no semiárido.
- Literatura de **substituição** aéreo → terrestre depois de proibições (o canal SIH).
- Literatura empírica sobre **zonas-tampão** como instrumento, não só como recomendação técnica.

### Testes de estresse

| teste | resultado |
|---|---|
| Sem a fonte mais forte (DRS 2023), o argumento se sustenta? | Sim: Calzada et al. e Camacho & Mejía sustentam o canal de método; DRS sustenta o desenho de água |
| Inverter a pergunta ("a literatura já basta"): a visão oposta é crível? | Parcialmente: para glifosato/GM há magnitudes; para método aéreo em cultura não-GM, não |
| Aplicar a outro contexto: generaliza? | O argumento da revisão sim; as magnitudes não |
| "E daí?": a relevância se justifica? | Sim: STF, assembleias estaduais, MAPA/ANVISA |

---

## 4. Checkpoint do pesquisador (obrigatório antes da Fase 2)

Para seguir, preciso de:
1. **Confirmação do RQ Brief** (§1): pergunta principal e as três sub-perguntas.
2. **Aprovação do desvio de escopo da SQ2** (§1, vínculos): literatura de método sem restrição de população nem de geografia.
3. Ciência dos três problemas maiores do DA (M1–M3). Eles entram como requisitos da Fase 2, e não como mudança de desenho.

Depois da confirmação, o ARS mostra a nota sobre a **forma da revisão** e espera a resposta antes de iniciar a busca.

---

## 5. Registro do checkpoint (2026-10-11)

| item | decisão do pesquisador | palavras dele |
|---|---|---|
| RQ Brief (§1) | ✅ confirmado | "confirmo" |
| Desvio de escopo da SQ2 | ✅ aprovado | "aprovo o desvio da SQ2" |
| DA M1–M3 | ✅ ciente; viram requisitos da busca | "pode seguir" |
| Amplitude da busca | máxima | "busque o máximo de artigos nesses sentido, usar firecrawl se necessário" |
| Nota sobre a forma da revisão (#921) | mostrada verbatim, sem recomendação; o pesquisador colou três formas e, perguntado qual, escolheu **revisão sistemática** | escolha: "Sistemática" |

**Consequência.** Pela regra do ARS (`deep-research/SKILL.md`, § Review-form note:
"Systematic review: offer `deep-research` `systematic-review` mode, and enter it
only when the author confirms"), o Estágio 1 sai do modo `full` e entra no modo
**`systematic-review`** (PRISMA 2020). Nesse modo a Fase 1 gera um **protocolo
PRISMA-P**, e não só o RQ Brief, e o protocolo exige confirmação do pesquisador
antes da busca (`references/systematic_review_protocol.md`, regra 2). O RQ Brief
e o blueprint acima continuam valendo como base do protocolo.

O protocolo fica em `docs/revisao-sistematica/protocolo.md`, e os registros de
busca e triagem, em `docs/revisao-sistematica/`. São metadados bibliográficos,
não microdado.

---

## 6. Fase 1 do modo `systematic-review`: protocolo e Devil's Advocate (checkpoint 1)

*2026-10-12.* Protocolo em `docs/revisao-sistematica/protocolo.md` (v0.9);
estratégias congeladas em `docs/revisao-sistematica/apendice-a-estrategias.md`;
logs em `docs/revisao-sistematica/calibracao/`; prompts verbatim em
`docs/revisao-sistematica/prompts/`.

**Como a estratégia foi construída.**
1. Calibração por bloco: 4 agentes, com recall de itens conhecidos.
2. Revisão PRESS 2015 independente: 4 agentes. **As quatro pediram revisão obrigatória**, com mudanças testadas.
3. Strings congeladas a partir das recomendações da PRESS, copiadas por script.

A rodada que mediria o recall num conjunto de validação totalmente novo falhou
por **limite de gasto da organização** e fica como pendência declarada.

### Devil's Advocate — Checkpoint 1 (protocolo)

**Veredito: PASS com condições.** Não há problema crítico. Dois problemas
maiores foram corrigidos no protocolo antes da confirmação, e dois dependem de
decisão do pesquisador.

**Maiores, corrigidos (emenda registrada no protocolo):**
- **M1. A regra de biomonitoramento excluiria as coortes de clordecona.** A PRESS da SQ1 mostrou que os estudos de Guadalupe (clordecona, inseticida usado só em bananais) são os mais próximos do caso cearense, e a exposição deles é medida no sangue materno. Correção: biomonitoramento é elegível quando o composto tem fonte exclusivamente agrícola no contexto.
- **M2. "Somente ocupacional" era ambíguo.** Em comunidades de *plantation*, a gestante muitas vezes também trabalha na lavoura. Correção: o critério é a **medida** de exposição. Se for residencial, espacial ou ambiental, o estudo é elegível mesmo com trabalhadoras na amostra.

**Maiores, que dependem do pesquisador:**
- **M3. Viabilidade (o F do FINER).** São ~15.000 registros brutos, ~4.000–4.500 só na SQ1. A triagem dupla por IA de tudo isso consome várias vezes o que a calibração consumiu, e a calibração já esgotou o limite de gasto da organização duas vezes. Um protocolo que não pode ser executado como escrito falha no PRISMA na hora do relatório. **Decisão de escala necessária.**
- **M4. A validação humana depende do tempo do pesquisador.** A amostra de referência de 100 registros (PRISMA-trAIce M9) leva de 2 a 3 horas de triagem cega. Sem ela, o item M9 é obrigatório e bloqueia o Estágio 2.5.

**Menores:**
- o recall em validação independente (V4) não foi medido; o relatório tem de chamá-lo de recall de desenvolvimento;
- as traduções para Scopus/WoS não foram testadas;
- a SQ3 depende de conferência manual de clássicos anteriores a 1990.

**Observação.** Sem Scopus/WoS, a cobertura de economia depende do OpenAlex,
de literatura cinzenta e de citações. Duas das nove sementes da SQ1 (Calzada,
JAERE; Dias, Rocha & Soares, ReStud) não estão no PubMed, e só o OpenAlex as
pega.

**Contra-argumento mais forte.** "Uma revisão 'sistemática' com triagem por IA
e um único humano não é sistemática no sentido Cochrane." Resposta disponível:
ela não se apresenta como Cochrane. Declara o uso de IA item a item
(PRISMA-trAIce), mede o desempenho da IA contra o humano e não esconde a falta
de um segundo revisor humano.

### Decisões do pesquisador no checkpoint do protocolo (2026-10-12)

| decisão | escolha |
|---|---|
| Escala da triagem | SQ1 com triagem dupla; SQ2/SQ3 com triador único, priorização por relevância, regra de parada e auditoria de 10% + 5% da cauda |
| Amostra de referência humana | 50 registros (25 incluídos / 25 excluídos), cega |
| Registro | sem registro externo; o carimbo é o commit |
| Scopus / WoS | Scopus, exportado pelo pesquisador pela CAPES; WoS não |

Incorporadas ao protocolo v1.0. **A busca só começa depois da confirmação
explícita do protocolo v1.0.**
