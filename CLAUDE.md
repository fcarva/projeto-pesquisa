# CLAUDE.md — Tese: externalidade da pulverização aérea no Ceará

Instruções de projeto para o Claude Code. Este arquivo é lido automaticamente no início de cada sessão. Mantê-lo curto, correto e atualizado.

## O que é este repositório
Dissertação de mestrado (PPGEco/UFES) em **dois ensaios** sobre o banimento estadual da pulverização aérea de agrotóxicos no Ceará (Lei Estadual nº 16.820/2019, "Lei Zé Maria do Tomé"), tratado como **externalidade negativa**.

- **Ensaio 1 — avaliação de impacto causal.** Efeito do ban sobre desfechos de nascimento (SINASC) e, como canal, qualidade da água (SISAGUA). Idioma "Berkeley": inferência causal aplicada (orientador: Prof. Renato Seixas, PhD ARE/Berkeley).
- **Ensaio 2 — escolha de instrumento.** Proibição vs. taxação vs. zonas-tampão, sob Weitzman (1974) preço-vs-quantidade, ancorado na curva dose-resposta estimada no Ensaio 1.

Idioma: **português** na prosa da dissertação; código e comentários podem ser em inglês. Prosa enxuta, lógica de *forward engineering* (parâmetro-alvo → hipóteses de identificação → estimação).

## Estratégia de identificação (forward engineering)
**Parâmetro-alvo.** ATT dose-resposta: como o efeito do ban varia com a **intensidade pré-ban de exposição** à pulverização aérea entre municípios. O tratamento é **contínuo (dose)**, não binário.
- ⚠️ **A curva custa mais caro que o nível.** CGS separam dois parâmetros: `ATT(d|d)` (nível) sai sob paralelismo tradicional; a **curva** — `ATE(d)`/`ACR(d)` — exige **strong parallel trends** (Assumption SPT), que exclui *selection-on-gains*. ⚠️ **Corrigido em 2026-09-22:** o placebo pré-tratamento **não isola** o SPT — passar não valida, porque a implicação é comum ao PT e ao SPT —, **mas pode falsificá-lo**, e o CGS §6.3 propõe e roda exatamente essa verificação (rejeitando, na aplicação deles). O teste está em `scripts/estimate/10_spt_pretrend.py`. ⚠️ **E a decisão mudou:** desde 2026-09-22 o resultado principal é o `ATT(d|d)`, não a curva — a derivada agregada não é interpretável (§8 da pré-especificação, linha de 2026-09-22). Ver `docs/ars/03-modelagem-ensaio1.md` e `docs/auditoria-pre-especificacao.md`.
- **Janela principal:** 2015 → 19/12/2024, cortada na Lei 19.135/2024 (exceção de drones) para preservar a cota zero. O segundo evento também é estadual e simultâneo — não é adoção escalonada.

**Estimador primário.** Callaway, Goodman-Bacon & Sant'Anna (2024, NBER WP 32117 / arXiv:2107.02637) — DiD com **tratamento contínuo**.
- ⚠️ **Não** é DiD escalonado. O ban é **estadual e simultâneo** (Lei 16.820/2019, art. 28-B; sanção **08/01/2019**, publicação e vigência **09/01/2019**): não há variação de *timing*. **Três marcos de antecipação, não um:** o PL 18/2015 foi **apresentado em 24/02/2015** (notícia), aprovado por unanimidade em **18/12/2018** (certeza) e entrou em vigor em 09/01/2019 (obrigação). ⚠️ A janela pré-ban 2015–2018 começa **depois** do marco de notícia — a dose medida pode já estar respondendo à expectativa. Isso morde a variável de tratamento, não só o desfecho. Ver `docs/ars/06-quimico-e-antecipacao.md`. Fonte: texto oficial das leis 16.820/2019 e 12.228/1993 (consolidada) em `docs/legislacao/`. Callaway–Sant'Anna (2021), de Chaisemartin–D'Haultfœuille (2020) e Goodman-Bacon (2021) tratam variação de *timing*, não de dose — são referência conceitual, **não** os estimadores principais.

**Variável de dose.** Intensidade agrícola pré-ban (PAM/IBGE, média 2015–2018) de culturas dependentes de pulverização. ⚠️ **A cultura-âncora ainda não está fixada — ver "Flags de auditoria".** Não hard-codar "algodão" nem "fruticultura" antes de verificar a dispersão empírica.

**Instrumento para exposição endógena.** Aptidão agroclimática **FAO-GAEZ** (percentil de *attainable yield*), seguindo Reynier & Rubin (2025, *PNAS* 122(3):e2413013121 — análogo dos EUA: glifosato + GAEZ + saúde perinatal) e a lógica de Dias, Rocha & Soares (2023, *ReStud*). Endereça a endogeneidade de *onde* culturas de alta pulverização são plantadas.

**Canal água.** SISAGUA; DiD montante/jusante dentro de bacia hidrográfica (shapefiles ANA). Template: DRS (2023).

**Robustez e comunicação.**
- Synthetic DiD (Arkhangelsky et al. 2021) para o agregado estadual.
- **PSM+DiD** como camada de comunicação para o orientador (idioma do Renato).
- Inferência com poucos clusters tratados e desfechos raros: Conley–Taber (2011) / wild-cluster bootstrap. Não superestimar precisão.

**Desfechos (SINASC).** Peso ao nascer (`PESO`), baixo peso (<2500 g), prematuridade (<37 semanas), colapsados a **município × ano-mês**.

## Fontes de dados e acesso

> **Status em 2026-09-21** — leia antes de sair caçando fonte. Detalhes e
> proveniência em `docs/lacunas-de-dados.md` e `docs/gates-resultados-dados-reais.md`.
>
> | fonte | estado |
> |---|---|
> | PAM/SIDRA, SINASC, SIM, SIH | ✅ adquiridas e no painel |
> | **SINAN/IEXO** | ✅ adquirida — canal A5, 1.217 notificações de agrotóxico agrícola |
> | **População (SIDRA)** | ✅ adquirida — denominador. ⚠️ 2022 vem do Censo, não de estimativa |
> | **FAO-GAEZ** | ✅ adquirida — 184/184 municípios, primeiro estágio confere |
> | **Bans municipais < 2019** | ✅ varridos — só Limoeiro do Norte (Lei 1.478, 20/11/2009) |
> | **MapBiomas** | ✘ **DESCARTADO**: só classes genéricas, banana cai em "Outras culturas perenes". Não melhora a dose — não escrever ingestor |
> | **SISAGUA** | ⏸️ adquirido e **suspenso**: quebra de registro no CE a partir de 2020 produziria efeito espúrio |
> | **ANA (ottobacias)** | ⏸️ **bloqueada pelo SISAGUA**, não por disponibilidade — o montante/jusante precisa de coordenada que o SISAGUA não tem |
> | **INMET / FUNCEME** | ⏸️ adquirível e bom, mas os alísios dão coerência 0,96 entre estações: "a favor do vento" vira "a oeste", que é geografia |
> | **Censo 2022 (censobr)** | ✅ adquirido 2026-09-22 — domicílios por setor via GitHub Releases do IPEA; passa pelo proxy remoto. Triagem estrutural CE×RN em `15_censo_demografico.py` |
> | **ADAGRI (receituário)** | ⬜ **LAI a protocolar** — a receita registra a modalidade de aplicação (Dec. 4.074/2002, art. 66). Única rota para medir o **método** no pré-período. Ver `docs/legislacao/lai-adagri-minuta.md` |
> | **SEMACE / ANAC / MAPA** | ⚠️ o MAPA é **dado aberto** (a LAI era desnecessária), mas não tem profundidade histórica. A LAI à SEMACE é a única rota para o pré-período |

- **SINASC** (nascimentos), **SIM** (óbitos) — DATASUS, via `pysus` ou Base dos Dados (BigQuery). **Microdado sensível → nunca commitar.**
- **SISAGUA** (qualidade da água) — Base dos Dados / MS.
- **PAM/IBGE** (área/produção por cultura) — `sidrapy` ou Base dos Dados.
- **FAO-GAEZ** (aptidão agroclimática) — raster → `data/geo/`.
- **ANA** (bacias) — shapefiles → `data/geo/`.
- **IBAMA** (vendas de agrotóxicos) — contexto.
- **SIH/DATASUS** (internações por intoxicação aguda) — canal de substituição aéreo→terrestre.
- **CAGED/RAIS** e **PIB agropecuário municipal** (IBGE) — canal de renda; insumo do Ensaio 2.
- **MapBiomas** (polígonos de cultivo) — fonte da deriva no canal-ar. ⚠️ Verificar se separa banana/melão ou só classes genéricas.
- **INMET / FUNCEME** (vento diário) — vetor a favor/contra no canal-ar.
- **CPRM/SGB** (vulnerabilidade cárstica, Aquífero Jandaíra) — heterogeneidade do canal-água. ⚠️ Confirmar se o mapa é público.
- **ANAC / MAPA / SINDAG** (cadastro aeroagrícola e pistas) — define o `d = 0` que mede o **método**, não a cultura.
- Documentos legais → `docs/legislacao/`: Lei 16.820/2019 e Lei 12.228/1993 consolidada (**obtidos**); ADI 6137/STF; Lei 19.135/2024 (exceção drones); ADI 7794. **ADI 5553 / ADI 7755** (desoneração tributária de agrotóxicos, rel. Fachin) — o STF decidindo o instrumento-**preço** enquanto já validou o instrumento-**quantidade**; matéria do Ensaio 2. A audiência pública da ADI 5553 é acervo técnico público.

## Convenções do repositório
- Estrutura: `data/{raw,processed,geo}`, `notebooks/`, `scripts/`, `paper/`, `docs/`.
- Pipeline em scripts numerados: `scripts/data_prep/01_*` a `11_*` → `scripts/build_panel/` → `scripts/estimate/` → `scripts/figures/`. **O `Makefile` é a ordem canônica** — `make simulado` / `make real` / `make varredura` / `make gaez`. ⚠️ Script novo que não entra no Makefile é script que não roda no pipeline.
- **Python-first** (pandas, `pyfixest`, `sidrapy`, `pysus`, `geopandas`). **R apenas para o estimador CGS de tratamento contínuo** (pacotes `contdid`/`did`), chamado como passo `Rscript` isolado. **A fronteira entre linguagens é I/O de arquivo** (parquet/CSV), nunca in-process: Python prepara o painel → grava parquet → `Rscript` estima → grava CSV *tidy* → Python lê de volta para tabelas/figuras. Isso mantém a reprodutibilidade.
- Reprodutibilidade: `requirements.txt` (Python) + `renv.lock` (R). Fixar seeds. Documentar a *vintage* de cada base (data de extração).
- **Nunca commitar** `data/raw`, `data/processed`, nem microdado. Commitar só código, docs e tabelas agregadas/derivadas seguras. Ver `.gitignore`.

## Flags de auditoria (tratar como incertezas vivas, não fatos)
Ao escrever código de análise, **explicitar estas como hipóteses a checar**, não como verdades assentadas:
0. ⚠️ **Bans municipais anteriores — NÃO é mais hipótese: confirmado em 2026-09-21.** Limoeiro do Norte proibiu a pulverização aérea pela **Lei Municipal 1.478, de 20/11/2009** (fonte primária: `camaralimoeirodonorte.ce.gov.br/leis/549`), nove anos antes da lei estadual, ao amparo do art. 29 da Lei 12.228/1993. **E ele está dentro do grupo tratado:** 6º de 169 na banana, no decil superior de 17 municípios. Ou seja, ~6% do grupo tratado da cultura-âncora candidata está tratado desde 2009, não desde 2019 — a dose medida em 2015–2018 para essa unidade já vem suprimida, e o efeito estimado é de uma remoção que já ocorrera. ✅ **E a varredura dos 17 tratados está COMPLETA**: 1 confirmado, 16 `ausente_conferido`, zero inconclusivos. A contaminação é exatamente Limoeiro e não cresce — Quixeré (21.289 leis no acervo) e Russas (6.901) não têm norma anterior a 2019. A fase 2 (os 184) segue aberta como verificação de completude, e não bloqueia nada. Ver `docs/legislacao/README.md` §1.
1. **Cultura-âncora não verificada.** Área de algodão pode ser fina no pós-bicudo; o agronegócio da Chapada do Apodi é fruta/melão, não algodão. **Verificar a variação de dose no PAM antes de fixar a cultura.**
2. **Descasamento tratamento/químico — e o químico não é o glifosato.** O ban proíbe o **método aéreo**, não moléculas. E a tabela do Dossiê ABRASCO reproduzida no PL 18/2015 (23 pontos de coleta, Chapada do Apodi, 2009) mostra **procimidona e carbaril em 23/23, carbofurano em 18/23, fenitrotiona em 16/23 — e glifosato em 4/23**. Fungicida em banana, por avião. Consequência: o template DRS não transfere quimicamente (lá é soja TH + glifosato), e a receita GAEZ do Reynier & Rubin é construída sobre culturas **GM** (milho, soja, algodão) — banana não é. Ver `docs/ars/06-quimico-e-antecipacao.md`. ⚠️ **E o análogo químico existe:** Calzada, Gisbert & Moscoso (2023, *JAERE*, `10.1086/725349`) — fumigação aérea de bananais no Equador, déficit de 80–150 g no peso sob exposição alta. Faltava no projeto até 2026-09-22; ver `docs/ars/13-rota1-calzada-januzzi-censo.md`.
3. **Lacuna de *enforcement*.** Proibir método ≠ proibir molécula.
4. **Poder estatístico.** Poucos municípios tratados + desfechos raros → usar Conley–Taber / wild bootstrap; não exagerar precisão.
5. ✅ **O `d = 0` não é zero de tratamento — TESTADO em 2026-09-22, e passou.** O Censo Agropecuário (tabela SIDRA 1008, equipamento de aplicação) mostra que **nenhum** município de dose zero no Ceará tinha aeronave: as 36 do estado estão em 7 municípios, todos com dose > 0. É a verificação mais direta desta flag que o projeto conseguiu. ⚠️ Ressalvas: dado de **2006** (o Censo 2017 não publicou o corte), conta estabelecimentos e não voos. ⚠️ **E o mesmo dado abriu uma ameaça MAIOR — ver flag 7.** Texto original: **O `d = 0` não é zero de tratamento.** Área nula na PAM é zero de *proxy*. E o §2º do art. 28-B alcança **dispersão aérea para controle vetorial**: município sem agricultura pulverizada mas com controle aéreo de dengue **é tratado** — e esses tendem a ser os maiores, então a contaminação correlaciona com porte, que correlaciona com desfecho. Quatro construções de zero em `docs/ars/03-modelagem-ensaio1.md` §5.3.
6. **Seleção para nascimento vivo.** Se o ban reduz óbito fetal, fetos marginais passam a nascer e entram na cauda de baixo peso — o efeito sobre peso médio vem atenuado ou invertido. Por isso o **SIM** é fonte de primeira linha, não acessório.
7. ⚠️ **DILUIÇÃO DO TRATAMENTO — aberta em 2026-09-22, e é a mais séria.** Dos 17 municípios do decil superior da banana, **15 não tinham aeronave alguma** em 2006. A dose por área plantada atribui tratamento alto a quem não tinha pulverização aérea a perder, o que atenua o ATT **por construção**. Isso concorre com a leitura de 'desenho sem poder' da §6 do paper, e os remédios são OPOSTOS: falta de poder pede mais unidades tratadas; erro de medida pede outra variável de dose — e encorpar o grupo tratado **pioraria**. ⚠️ Compõe com a flag 0: das 27 aeronaves no decil, 18 são de Limoeiro do Norte, banido desde 2009; sobra **Quixeré, 9 aeronaves**. A LAI à SEMACE (cadastro aeroagrícola) deixa de ser conveniência e vira prioridade. Ver `scripts/data_prep/13_censo_agro_equipamento.py` e §5 do paper. ⚠️ **Atualizado em 2026-09-22: a flag tem nome, literatura e estimador — e as duas leituras NÃO são indecidíveis.** O objeto é *misclassification / mistargeting* do tratamento em DiD. Negi & Negi (2025, *J. Applied Econometrics* 40(4), `doi:10.1002/jae.3116`, open access) identificam pontualmente sob erro **unilateral** e **diferencial** — e o erro daqui **é unilateral, já provado**: a flag 5 mostrou que nenhum `d = 0` tinha aeronave, isto é, não há falso negativo. Denteh & Kédagni (arXiv:2207.11890, *working paper*) dão limites sem exigir instrumento, e alertam que sob erro **diferencial** o sinal pode **inverter** — o que retira valor probatório da coerência de sinal entre estimadores (§6.8 do paper), porque todos correm sobre a mesma dose mal medida. ⚠️ E a conta importa: aplicando o limite deles aos coeficientes já reportados, a partir de `λ = 0,5` o efeito implicado sobre os genuinamente tratados **ultrapassa o MDE de 33,4 g** — sob a leitura de erro de medida, o desenho teria tido poder. Ver `docs/auditoria-mensuracao-do-tratamento.md`.

## Plugin ARS (repositório separado)
O suite **Academic Research Skills** (fork `Imbad0202/academic-research-skills`) é instalado como plugin do Claude Code:
```
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```
**Divisão de trabalho:** este repositório = o projeto empírico (dados/código/paper); ARS = motor de metodologia para **redigir e auto-revisar**. Fluxo: resultados verificados aqui → ARS Stage 2 (WRITE). ARS **nunca** roda os experimentos; este repositório roda. Usar `/ars-plan` (estrutura socrática), `/ars-lit-review`, modos de revisão. Human-in-the-loop: o agente faz o trabalho braçal; o pesquisador decide pergunta, método e interpretação. Os *integrity gates* do ARS pegam referências fabricadas — útil, dada a exigência de proveniência da tese.

## O que o Claude Code deve / não deve fazer aqui
**Fazer:** escrever/refatorar scripts de pipeline, montar painéis, rodar checagens descritivas, produzir figuras/tabelas, redigir seções LaTeX quando pedido.
**Perguntar antes de:** commitar qualquer coisa em `data/`; mudar a estratégia de identificação; introduzir um novo estimador como "primário".
**Não fazer:** inventar referências (verificar contra DOI/Crossref); hard-codar a cultura-âncora; fabricar resultados; commitar microdado.
