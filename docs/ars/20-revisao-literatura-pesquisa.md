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

**Confirmação (2026-10-12, sessão nova).** Perguntado se confirmava o protocolo
v1.0, o pesquisador respondeu **"Confirmo o v1.0"**. O commit que registra a
confirmação é o carimbo de tempo; a coleta definitiva vem depois dele (§8).

---

## 7. Retomada numa sessão nova (passagem de bastão, 2026-10-12)

*Por que uma sessão nova:* credenciais cadastradas no ambiente
(`OPENALEX_API_KEY`, `ELSEVIER_API_KEY`) só entram em sessões iniciadas
depois do cadastro. A rede está irrestrita desde 2026-10-12.

**Estado exato:**
- Branch `claude/confident-wozniak-1rae17`.
- Pipeline ARS `/ars-full`, **Estágio 1** (`deep-research`, modo `systematic-review`), **fim da Fase 1**. O ARS é seguido pelos arquivos do repositório `Imbad0202/academic-research-skills`, fixado no commit `d1e5171` (v3.23.0); clonar num diretório temporário se o plugin não estiver instalado.
- Protocolo: `docs/revisao-sistematica/protocolo.md` **v1.0, AGUARDANDO A CONFIRMAÇÃO EXPLÍCITA do pesquisador**. A busca definitiva não começa sem ela.
- Estratégias congeladas (4 blocos): `docs/revisao-sistematica/apendice-a-estrategias.md`, gerado por `ferramentas/gera_apendice_a.py` a partir de `calibracao/*-final.json`.
- Seção de revisão de literatura (pré-triagem, estilo Bellemare, 4 páginas): `paper/overleaf/revisao-literatura.tex`.

**Acesso:**
- PubMed (E-utilities), Crossref, arXiv e RePEc respondem direto, por script.
- OpenAlex exige `OPENALEX_API_KEY`: passar `api_key=` na URL.
- SciELO e BVS bloqueiam IP de datacenter, inclusive com navegador sem interface, então ficam como exportação do pesquisador. O Scopus também é exportação do pesquisador.

**Próximos passos, em ordem, depois da confirmação:**
1. Commit de fechamento do protocolo (o carimbo de tempo).
2. Coleta **por script**, sem agentes: OpenAlex (paginação com cursor, `per-page=200`, com `abstract_inverted_index` reconstruído em texto) e PubMed (`esearch` com *history* + `efetch`) para as linhas congeladas. Registros em `docs/revisao-sistematica/registros/` (CSV/JSONL), com data e contagem.
3. Importar as exportações de SciELO, LILACS e Scopus de `registros/importados/` e deduplicar por DOI, depois título + ano.
4. Piloto de 50 registros (dois triadores de IA) → κ → ajuste dos critérios.
5. Planilha cega de 50 registros (25/25) para a amostra de referência do pesquisador.
6. Triagem: SQ1 dupla; SQ2/SQ3 por relevância, com regra de parada e auditoria (protocolo, "Escala da triagem").

**Cuidados aprendidos:**
- o limite de gasto da organização derrubou rodadas de agentes duas vezes: coleta e deduplicação são script, e os agentes ficam só para a triagem;
- o Parallel `web_fetch` devolve *cache* para URLs quase idênticas;
- o OpenAlex não tem curinga e não junta acentos;
- GET longo no PubMed dá 414, então usar o *history server*.

---

## 8. Sessão de 2026-10-12 (branch `claude/admiring-carson-3l2d8h`)

**Feito:**
1. **Protocolo v1.0 confirmado** pelo pesquisador; o carimbo é o commit `1d12f10`.
2. **Coleta do PubMed concluída** (`ferramentas/coleta_pubmed.py`, commit `817f7d6`). As contagens batem com as congeladas: SQ1 #5 = 2.054 (camada 1 = 892, camada 2 = 1.162) e SQ3 P1 = 578. Os metadados e o SHA-256 do resumo ficam em `registros/`, e o log em `registros/coletas.jsonl`. O resumo fica fora do git, porque o repositório é público e o texto tem direito autoral do editor. Ele é reconstruído com `--reidratar`, que confere o hash.
3. **Coletor do OpenAlex escrito** (`ferramentas/coleta_openalex.py`), mas **não rodado**. Ele resolve os marcadores das linhas congeladas: na SQ1-AL, `(#1)`–`(#3)` e `#n-v0`, com as caudas de 6, 9 e 18 termos; na SQ2 #7, `<the #5 search string>`. O `--plano` valida as 28 linhas sem rede. **Conferência ao vivo:** a SQ1-AL #4-v0, a linha mais difícil de resolver, deu **604** pelo Parallel `web_fetch`, igual à congelada. O `meta.x_query` ecoou os três blocos.

**Bloqueado: as credenciais continuam sem funcionar nesta sessão.**
- **OpenAlex:** a credencial foi cadastrada no ambiente com o host `*.example.com` e o caminho `/api.openalex.org/works`. O proxy nunca a injeta em `api.openalex.org`, e sem chave a cota do IP compartilhado está esgotada. **Correção:** host `api.openalex.org`; caminho `/works`, ou sem restrição, para o `cites:` e a reidratação. O coletor também aceita `OPENALEX_API_KEY` como variável de ambiente.
- **Elsevier:** o host está certo, mas a API responde "Invalid API Key". A chave pode estar sendo injetada num cabeçalho que a Elsevier não lê, porque ela espera `X-ELS-APIKey`, ou pode estar inválida. De qualquer forma, o protocolo prevê o Scopus como **exportação do pesquisador** pela CAPES: a API não é rota do v1.0, e fora de IP institucional ela não devolve o Scopus completo.
- O Firecrawl está sem créditos.

**Próximos passos, depois de corrigir a credencial e abrir uma sessão nova:**
1. `python3 ferramentas/coleta_openalex.py --conferir`: compara as contagens de hoje com as congeladas, linha a linha;
2. `python3 ferramentas/coleta_openalex.py`: coleta tudo;
3. deduplicação (script ainda a escrever): DOI → PMID/ID OpenAlex → título normalizado + ano. Pools separados por SQ, com a pertença cruzada registrada. Para a SQ1, exclusão automática por metadado (ano < 1990, idioma fora de en/pt/es), contada no PRISMA. Para a SQ3, exclusão de *paratext* e retratados;
4. importar as exportações de SciELO, LILACS e Scopus de `registros/importados/` (RIS de preferência);
5. piloto de 50 registros da SQ1 com os dois triadores → κ. A amostra de referência de 50 (25/25) **depende do consenso da IA**, então só sai depois que a triagem da SQ1 tiver ao menos 25 inclusões de consenso.

---

## 9. Plano de execução (2026-10-13)

O roteiro das próximas sessões está em `docs/revisao-sistematica/plano-execucao.md`:
as tarefas do pesquisador (chaves como variáveis de ambiente; exportação de Scopus,
SciELO e LILACS pela CAPES) e cinco etapas no Claude Code, cada uma com prompt pronto.
As etapas são: (1) emenda v1.1 + OASISBR/LA Referencia; (2) OpenAlex + Scopus API;
(3) importação + deduplicação; (4) PRISMA 2020 completo; (5) piloto + triagem.
Decisões do pesquisador nesta data: teses e dissertações entram na SQ1; Scopus por API
(visão reduzida) + exportação pela CAPES.

**Emenda v1.1 do protocolo (2026-10-13).** As duas decisões entraram no
`protocolo.md` (tabelas *Emendas* e *Histórico de versões*), num commit isolado,
anterior às coletas novas:
- *Status* (SQ1): tese ou dissertação com dado original é elegível; "vale o publicado" vale também para tese → artigo; a exclusão "teses e dissertações, por viabilidade" saiu;
- *Fontes de informação*: OASISBR e LA Referencia (API VuFind, por script) e Scopus por API (visão reduzida, só identificação; resumo hidratado por DOI via OpenAlex/Crossref), além da exportação pela CAPES;
- a consulta nas duas fontes VuFind é SQ1-AL #1 AND #2, **sem o #3 (geografia)**, porque as fontes já são brasileira e latino-americana;
- *Uso de IA*, M2: as fontes novas entram na lista de ferramentas.
O motivo é a lacuna de literatura brasileira: das 544 respostas da LA Referencia à
string #1 AND #2 (teste de 2026-10-13), 292 são teses e dissertações.

**Coleta da LA Referencia (2026-10-13, depois da emenda).** `ferramentas/coleta_vufind.py`,
6 fatias, união = **544**, igual à chamada única: 251 artigos, 167 dissertações, 125 teses
e 1 capítulo; 537 com resumo e 89 com DOI. Dos 43 itens conhecidos da calibração SQ1-AL,
só 6 estão na fonte, e a string recupera 3. Os 3 perdidos são itens de **contexto** (Rocha
2017, Dossiê ABRASCO em espanhol, artigo jurídico sobre a pulverização aérea), que nenhuma
linha de efeito recupera. O **OASISBR não foi coletado**: o 403 não vem do tamanho da URL,
como se supunha, mas de uma regra que recusa consultas booleanas com ~10 termos ou mais e
depois bloqueia o IP. Detalhes no Apêndice A.

**Etapa 2 (2026-10-13).** *Scopus pela API* (`ferramentas/coleta_scopus.py`): **4.945**
registros da string de `scopus_wos.md`, lida do arquivo; visão STANDARD (sem resumo), 4.276
com DOI, e as 3 sementes do arquivo recuperadas. Sem assinatura, a Elsevier recusa o
`cursor`; a paginação é por `start` (teto de 5.000) com ordem fixa `-coverDate`, porque a
ordem padrão repetiu registros entre páginas (o coletor parou sem gravar na primeira
tentativa). *OpenAlex*: o `--conferir` deu contagens de hoje menores que as congeladas em
quase todas as linhas; só a SQ2 #11 passa do limite de 5% (27 × 29). **Decisão do
pesquisador: aceitar as contagens de hoje** (todas as linhas caíram na mesma direção, o que
sugere limpeza do índice). Coleta completa das 28 linhas, cada uma com os distintos iguais à
contagem de hoje. Achado de método: o cursor do OpenAlex não é determinístico; numa passada
ele repete umas obras e pula outras (SQ2 #5: 3.716 distintos de 3.719). O coletor une
passadas por ID até fechar o total, refaz a ordem pelo `relevance_score` de cada obra (que
importa para a regra de parada da SQ2/SQ3) e registra no log as passadas e as repetições.

**Emenda v1.2 (2026-10-13, sessão na nuvem, antes da coleta do OASISBR).** Num teste com
duas consultas curtas e idênticas, a LA Referencia saiu **subconjunto** do OASISBR (zero
registros só nela). O OASISBR trouxe 30 de 45 e 23 de 47 registros a mais, entre eles
dissertações centrais para a SQ1 e TCCs de graduação. Decisões do pesquisador:
(i) **TCC com dado original entra na SQ1**, e TCC → artigo segue "vale o publicado";
(ii) o OASISBR é coletado em **fatias de ≤ 5 + 5 termos**, com pausa de 3 s e parada no
primeiro 403, porque a API recusa consultas com ~10 termos ou mais. O texto da emenda
foi aprovado pelo pesquisador antes do commit.

**Coleta do OASISBR (2026-10-13, depois da emenda v1.2).** 192 fatias de ≤ 5 + 5 termos,
pausa de 3 s, sem nenhum 403: **878 registros** (317 dissertações, 254 artigos, 153 teses,
71 TCCs, 52 sem formato), 838 com resumo e 78 com DOI. Recall: 7/43 itens conhecidos estão
no OASISBR, e a string recupera 4/7 (os 3 perdidos são os mesmos itens de contexto da LA
Referencia).
- **Conferência planejada que falhou, e por quê.** O critério de parada era a cobertura dos registros `BR_` da LA Referencia na união do OASISBR (≥ 95%), porque o acervo dela está contido no dele. Deu 289/337 (85,8%), e a coleta parou sem gravar. Diagnóstico: dos 48 faltantes, 40 estão indexados no OASISBR com o **mesmo título e resumo**, mas o motor do OASISBR não os casa com a string, e o da LA Referencia casa por outros campos ou radicalização. Acervo contido não implica resultado de busca contido. Boa parte desses 48 é ruído (*Spodoptera*, *Bacillus thuringiensis*, amamentação), e todos já entram na SQ1 pela LA Referencia.
- **Critério que substituiu o anterior** (equivalência do fatiamento): as mesmas 192 fatias, rodadas na LA Referencia, reproduzem a chamada única dela (**544 = 544**). A cobertura continua reportada, mas não é mais critério de parada.
- **Recall reprodutível:** a lista dos 43 itens conhecidos foi congelada em `calibracao/itens-conhecidos-sq1-al.json`, porque a cota gratuita do OpenAlex do IP compartilhado se esgotou no meio da execução.

**Etapa 3 (2026-10-13): deduplicação.** `deduplica.py` une, por *union-find*, os registros
com o mesmo DOI, PMID, ID OpenAlex, EID, ID VuFind ou título normalizado + ano (este com
≥ 30 caracteres). O representante é a versão publicada ("vale o publicado").
- **Resultado:** SQ1 = 14.200 brutos → 9.416 únicos → **8.593 a triar** (693 excluídos por período e 130 por idioma). SQ2 = 4.132 → **3.920**; o OpenAlex tem obras duplicadas com IDs diferentes (198). SQ3 = 6.373 → 6.029 → **6.016** (7 paratext, 6 retratados).
- **Achados de método:**
  - o **Scopus (API)** traz sozinho 2.561 registros a triar na SQ1, a busca TITLE-ABS-KEY também casa palavras-chave indexadas, e ele vem sem resumo;
  - **teses e artigos não se fundem pelo título**: são 38 pares para conferência, a maioria a mesma dissertação aparecendo como `dissertation` no OpenAlex e sem formato nas fontes VuFind;
  - o **push protection do GitHub** confunde os IDs `ES_<hash>` da LA Referencia com chaves do hCaptcha, então as saídas gravam `PAÍS/<hash>`.
- **Hidratação dos resumos:** 4.668 DOIs sem resumo; o Crossref trouxe 932. O OpenAlex fica para uma sessão com a chave.

**Etapa 4 (2026-10-13): PRISMA 2020.**
- `ferramentas/prisma.py` gera os fluxogramas das três SQs em TikZ (`paper/overleaf/prisma-sq*.tex`, compilação testada) e em Markdown (`prisma-fluxo.md`).
- O script confere as identidades. Na SQ1: 13.456 registros distintos nas bases − 4.040 duplicatas − 823 por regra de metadado = 8.593 a triar.
- A sobreposição entre linhas de uma mesma base (744) fica fora dos "distintos" e é declarada em nota.
- As exclusões por período e idioma entram na caixa "marcados como inelegíveis por ferramenta automática", com a regra escrita na própria caixa.
- Checklists PRISMA 2020 e PRISMA-S, item a item, com onde cada um está documentado ou "pendente".

**LeapSpace (2026-10-13): conferência externa de recall, não fonte de identificação.** O
pesquisador colou o prompt `prompts/03-leapspace-busca-complementar-sq1.md` no LeapSpace
(Elsevier, via CAPES).
- **Formato:** o LeapSpace não seguiu as tabelas pedidas. Devolveu uma síntese narrativa e 14 referências, transcritas em `registros/importados/leapspace-sq1-2026-10-13.md`.
- **Conferência** (`ferramentas/confere_referencias_ia.py` → `registros/leapspace-sq1-2026-10-13-conferencia.csv`): as **14 existem** no Crossref, com título conferido, e **13 já estavam no conjunto** (uma, Roan 1984, sai na regra de período).
- **A única nova**, Rull & Ritz (2003, *EHP*), é sobre o erro de classificação na medida de exposição e não tem desfecho ao nascer. Não é elegível na SQ1; serve de referência de fundo para a SQ2 (erro de classificação).
- **Uso:** o resultado não entra no fluxograma como fonte e não pede emenda. Fica registrado como uma conferência independente de que a busca por script captura a literatura que um assistente com acesso ao Scopus e ao ScienceDirect devolve. Ele não trouxe nenhum estudo brasileiro além de Siqueira et al. (2010), que já estava no conjunto.

**LeapSpace, tabelas comparativas (2026-10-13).** O pesquisador exportou duas *compare tables*
do LeapSpace, com DOI, EID, data e resumo do Scopus. Elas estão em
`data/raw/revisao-sistematica/leapspace/`, fora do git, porque o resumo é conteúdo do Scopus. A
conferência por DOI, EID e título (`ferramentas/confere_referencias_ia.py`, agora também para esse
CSV) deu:
- **tabela 1**: as mesmas 13 referências da síntese, todas reais; 12 já estavam no conjunto, e a nova é de novo Rull & Ritz 2003, não elegível;
- **tabela 2**: resposta ao pedido de estudos latino-americanos, com 7 estudos, **todos já no conjunto**: Calzada 2023; ISA 2024; Siqueira 2010; Boccolini et al. 2013, *IJHEH*; Oliveira et al. 2014, *Ciênc Saúde Coletiva*, Mato Grosso (autores conferidos no Crossref); um estudo do Rio Grande do Sul de 2021 sem DOI, casado pelo EID com o registro do Scopus pela API; e o de malatião aplicado por avião na Califórnia, 1987, *AJPH*, fora pela regra de período.

Conclusão: nas duas rodadas, o LeapSpace não trouxe nenhum estudo elegível que a busca por
script tivesse perdido. O resultado fica registrado como conferência externa de recall.

**Etapa 5, piloto (2026-10-14).** O pesquisador aprovou o prompt de triagem
(`prompts/04-triagem-titulo-resumo-sq1.md`) e escolheu **Sonnet** para os triadores. Os dois
triadores leram o prompt e o lote direto dos arquivos, com chamadas idênticas
(`prompts/04b-chamada-triador.md`), em instâncias paralelas.
- **Concordância** nos 50 registros do piloto: **κ = 0,91** (49/50), com 6 inclusões e 43 exclusões em comum.
- **Divergência:** só uma (coorte de piretroides × metabolismo lipídico neonatal), adjudicada como exclusão por desfecho intermediário.
- **Qualidade das saídas:** citação literal em 99/100 (a falha é um acento acrescentado); os 11 registros sem resumo foram excluídos pelo título, todos claramente fora do tema.
- **Consumo:** cerca de 132 mil tokens por chamada de 50 registros e 77 mil numa chamada de adjudicação com 1 registro, ou seja, uns 75 mil de sobrecarga fixa por chamada e uns 1,1 mil por registro.
- **Ajuste de redação:** os motivos divergiram em 3 de 43 exclusões em comum (editorial: `desenho` × `tipo_documento`; texto jurídico: `desenho` × `fora_do_tema`). Isso não afeta a decisão nem o fluxograma, que só reporta motivos no texto completo, então o prompt fica como foi validado.
