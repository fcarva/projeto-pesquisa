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
> | **Bans municipais < 2019** | ✅ varridos — só Limoeiro do Norte (Lei 1.478, 20/11/2009), **revogada pela Lei 1.511, de 26/05/2010** (política ambiental; a revogação está num artigo do corpo, não na ementa — por isso a busca no acervo não a achou). ⬜ Texto integral a conferir. Ver `docs/legislacao/README.md` |
> | **MapBiomas** | ✘ **DESCARTADO**: só classes genéricas, banana cai em "Outras culturas perenes". Não melhora a dose — não escrever ingestor |
> | **SISAGUA** | ⏸️ adquirido e **suspenso**: quebra de registro no CE a partir de 2020 produziria efeito espúrio |
> | **ANA (ottobacias)** | ⏸️ **bloqueada pelo SISAGUA**, não por disponibilidade — o montante/jusante precisa de coordenada que o SISAGUA não tem |
> | **INMET / FUNCEME** | ⏸️ adquirível e bom, mas os alísios dão coerência 0,96 entre estações: "a favor do vento" vira "a oeste", que é geografia |
> | **Censo 2022 (censobr)** | ✅ adquirido 2026-09-22 — domicílios por setor via GitHub Releases do IPEA; passa pelo proxy remoto. Triagem estrutural CE×RN em `15_censo_demografico.py` |
> | **ADAGRI (receituário)** | ⬜ **LAI a protocolar** — a receita registra a modalidade de aplicação (Dec. 4.074/2002, art. 66). Única rota para medir o **método** no pré-período. Ver `docs/legislacao/lai-adagri-minuta.md` |
> | **SEMACE / ANAC / MAPA** | ⚠️ o MAPA é **dado aberto** (a LAI era desnecessária), mas não tem profundidade histórica. A LAI à SEMACE é a única rota para o pré-período |

- **SINASC** (nascimentos), **SIM** (óbitos) — DATASUS. ⚠️ **Dois transportes para a mesma fonte, e isso é de propósito:** `--fonte ftp` (script 02) baixa o `.dbc` do **FTP do DATASUS, porta 21** — a fonte original —, e `--fonte pysus` passa pelo espelho DuckLake em HTTPS. Em 2026-09-22 o espelho ficou inalcançável (TCP abre, sessão morre) enquanto o FTP respondia em 0,4 s; o `auto` tenta pysus → FTP → simulado, **nessa ordem**, porque simulado não é evidência. O FTP tem a série consolidada **até 2024** (`/dissemin/publicos/SINASC/1996_/Dados/DNRES`, irmã da `PRELIM`) — a Base dos Dados/BigQuery deixou de ser rota necessária. **Microdado sensível → nunca commitar.**
- **SISAGUA** (qualidade da água) — Base dos Dados / MS.
- **PAM/IBGE** (área/produção por cultura) — `sidrapy` ou Base dos Dados.
- **FAO-GAEZ** (aptidão agroclimática) — raster → `data/geo/`.
- **ANA** (bacias) — shapefiles → `data/geo/`.
- **IBAMA** (vendas de agrotóxicos) — contexto.
- **SIH/DATASUS** (internações por intoxicação aguda) — canal de substituição aéreo→terrestre. `--fonte ftp` no script 04 (`RD{UF}{AA}{MM}.dbc`, **mensal**: a janela são 96 arquivos).
- **CAGED/RAIS** e **PIB agropecuário municipal** (IBGE) — canal de renda; insumo do Ensaio 2.
- **MapBiomas** (polígonos de cultivo) — fonte da deriva no canal-ar. ⚠️ Verificar se separa banana/melão ou só classes genéricas.
- **INMET / FUNCEME** (vento diário) — vetor a favor/contra no canal-ar.
- **SINAN/IEXO** (notificação de intoxicação exógena) — canal A5, script 10. ⚠️ **FINAIS e PRELIM são diretórios diferentes no FTP** (em 2026-09-22: finais até 2022, preliminares 2023–2026), e a janela do projeto cruza essa fronteira. Ano que só existe em PRELIM **não entra sozinho**: exige `--aceitar-preliminar`, e a proveniência gravada vira `ftp_preliminar`. Dado em revisão misturado com final produz quebra de série que vem da consolidação, não do mundo.
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
0. ✅ **Bans municipais anteriores — a lei de Limoeiro existiu e foi REVOGADA (revogadora identificada em 2026-09-22).** Limoeiro do Norte proibiu a pulverização aérea pela **Lei Municipal 1.478, de 20/11/2009** (fonte primária: `camaralimoeirodonorte.ce.gov.br/leis/549`), e o município está no grupo tratado (6º de 169 na banana). A lei foi revogada pela **Lei 1.511, de 26/05/2010** ("Dispõe sobre a política ambiental do município", `/leis/581`), um mês após o assassinato de Zé Maria do Tomé: a revogação está num **artigo do corpo**, não na ementa (*Diário do Nordeste*, abr/2010; G1, 31/10/2024). O "20/05/2010" da CPT é, provavelmente, a data da votação. ⚠️ Histórico: na mesma data a revogação chegou a ser **contestada** — o acervo completo da Câmara (2.692 leis) não tem lei citando a 1.478 nem datada de 20/05/2010, justamente porque a revogadora não diz isso na ementa. ⬜ **Texto integral da 1.511 a conferir** (anexo em `/leis/581`; o proxy remoto bloqueia): até lá a fonte fica `secundaria`. Na janela 2015–2018 Limoeiro **não** estava sob ban: a contaminação do pré-período é nula, e Limoeiro está no grupo genuinamente tratado. A varredura dos 17 tratados está completa (1 com lei, 16 `ausente_conferido`), mas ⚠️ **lei achada não é lei vigente**: todo `confirmado` exige conferência de revogação, registrada em `data_revogacao` (`docs/legislacao/bans-municipais-ce.csv`), e o `--revogacao` do script 09 marca leis-quadro ambientais posteriores como candidatas a ler. Ver `docs/legislacao/README.md` e `docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md` §5.
1. **Cultura-âncora não verificada.** Área de algodão pode ser fina no pós-bicudo; o agronegócio da Chapada do Apodi é fruta/melão, não algodão. **Verificar a variação de dose no PAM antes de fixar a cultura.**
2. **Descasamento tratamento/químico — e o químico não é o glifosato.** O ban proíbe o **método aéreo**, não moléculas. E a tabela do Dossiê ABRASCO reproduzida no PL 18/2015 (23 pontos de coleta, Chapada do Apodi, 2009) mostra **procimidona e carbaril em 23/23, carbofurano em 18/23, fenitrotiona em 16/23 — e glifosato em 4/23**. Fungicida em banana, por avião. Consequência: o template DRS não transfere quimicamente (lá é soja TH + glifosato), e a receita GAEZ do Reynier & Rubin é construída sobre culturas **GM** (milho, soja, algodão) — banana não é. Ver `docs/ars/06-quimico-e-antecipacao.md`. ⚠️ **E o análogo químico existe:** Calzada, Gisbert & Moscoso (2023, *JAERE*, `10.1086/725349`) — fumigação aérea de bananais no Equador, déficit de 80–150 g no peso sob exposição alta. Faltava no projeto até 2026-09-22; ver `docs/ars/13-rota1-calzada-januzzi-censo.md`.
3. **Lacuna de *enforcement*.** Proibir método ≠ proibir molécula.
4. **Poder estatístico.** Poucos municípios tratados + desfechos raros → usar Conley–Taber / wild bootstrap; não exagerar precisão. ⚠️ **E no agregado o grupo escasso é o de CONTROLE (2026-09-23):** o `ATT(d|d)` agregado é o DiD binarizado, 169 produtores contra 15 municípios de área nula, e todos os estimadores binários da §6 usam os mesmos 15 — coerência de sinal entre eles não é independência. Pela diluição (flag 7), o −36 g implicaria ≈ −870 g nos genuinamente tratados: não é efeito diluído do ban. O `04_robustness.py` reporta o nível com inferência que respeita os 15 (jackknife incluído). Ver `docs/ars/17-resposta-ao-feedback-2026-09-22.md` §1.
5. ✅ **O `d = 0` não é zero de tratamento — TESTADO em 2026-09-22, e passou.** O Censo Agropecuário (tabela SIDRA 1008, equipamento de aplicação) mostra que **nenhum** município de dose zero no Ceará tinha aeronave: as 36 do estado estão em 7 municípios, todos com dose > 0. É a verificação mais direta desta flag que o projeto conseguiu. ⚠️ Ressalvas: dado de **2006** (o Censo 2017 não publicou o corte), conta estabelecimentos e não voos. ⚠️ **E o mesmo dado abriu uma ameaça MAIOR — ver flag 7.** Texto original: **O `d = 0` não é zero de tratamento.** Área nula na PAM é zero de *proxy*. E o §2º do art. 28-B alcança **dispersão aérea para controle vetorial**: município sem agricultura pulverizada mas com controle aéreo de dengue **é tratado** — e esses tendem a ser os maiores, então a contaminação correlaciona com porte, que correlaciona com desfecho. Quatro construções de zero em `docs/ars/03-modelagem-ensaio1.md` §5.3.
6. **Seleção para nascimento vivo.** Se o ban reduz óbito fetal, fetos marginais passam a nascer e entram na cauda de baixo peso — o efeito sobre peso médio vem atenuado ou invertido. Por isso o **SIM** é fonte de primeira linha, não acessório.
7. ⚠️ **DILUIÇÃO DO TRATAMENTO — aberta em 2026-09-22, e é a mais séria.** Dos **17** tratados (decil superior da banana entre os 169 produtores — a conta dos estimadores 07/08), **15 não tinham nenhum estabelecimento com aplicação por aeronave** em 2006 (Censo Agro, tabela 1008 — conta *uso*, não posse). VPP = 2/17 = 11,8%. O "19" de documentos antigos é outra conta (quantil 0,9 sobre os 184). Com a revogação de Limoeiro (flag 0), os 27 estabelecimentos do grupo (Limoeiro 18, Quixeré 9) são tratamento genuíno em 2019. **O resultado que se aplica é o Corolário 1 de Denteh & Kédagni** (arXiv:2207.11890, v3): sob tendências paralelas no D *observado* — a hipótese que o paper já mantém — e sem falso negativo — verificado pela flag 5 —, `θ = VPP · ATT` para erro **arbitrário**, inclusive diferencial: atenuação pura, o sinal **não** inverte, e `ATT = θ/VPP` é pontual dado o VPP. ⚠️ **Corrigido em 2026-09-22:** (i) Negi & Negi (2025, *JAE* 40(4), `10.1002/jae.3116`) **não** se aplicam — o erro unilateral deles é só falso *negativo* (`D = D*·S`), o nosso é só falso *positivo*; (ii) o alerta "sob erro diferencial o sinal pode inverter" não vale aqui, e a coerência de sinal entre estimadores volta a contar contra esta ameaça; (iii) "a partir de λ = 0,5 o desenho teria tido poder" estava errado — o MDE é do estimando θ, que é o mesmo nas duas leituras. **A calibração** (`scripts/estimate/12_erro_de_classificacao.py`): com o VPP do Censo e o efeito do análogo mais próximo (Calzada et al. 2023: 80–150 g sob exposição alta, pelo resumo), o θ esperado é ≤ ~9 g e o poder ≤ 11%. A diluição é o **mecanismo** da falta de poder, não uma leitura rival: aumentar N sem aumentar o VPP não resolve, e baixar o corte de dose **piora** (os próximos da fila são serra e sertão). A alavanca é o VPP: medi-lo (LAI à ADAGRI) ou concentrar o grupo tratado onde havia avião (Rota 1, Chapada). Ver `docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md`.

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
