# CLAUDE.md — Tese: externalidade da pulverização aérea no Ceará

Instruções de projeto para o Claude Code. Este arquivo é lido automaticamente no início de cada sessão. Mantê-lo curto, correto e atualizado.

## O que é este repositório
Dissertação de mestrado (PPGEco/UFES) em **dois ensaios** sobre o banimento estadual da pulverização aérea de agrotóxicos no Ceará (Lei Estadual nº 16.820/2019, "Lei Zé Maria do Tomé"), tratado como **externalidade negativa**.

- **Ensaio 1 — avaliação de impacto causal.** Efeito do ban sobre desfechos de nascimento (SINASC) e, como canal, qualidade da água (SISAGUA). Idioma "Berkeley": inferência causal aplicada (orientador: Prof. Renato Seixas, PhD ARE/Berkeley).
- **Ensaio 2 — escolha de instrumento.** Proibição vs. taxação vs. zonas-tampão, sob Weitzman (1974) preço-vs-quantidade, ancorado na curva dose-resposta estimada no Ensaio 1.

Idioma: **português** na prosa da dissertação; código e comentários podem ser em inglês. Prosa enxuta, lógica de *forward engineering* (parâmetro-alvo → hipóteses de identificação → estimação).

## Estratégia de identificação (forward engineering)
**Parâmetro-alvo.** ATT dose-resposta: como o efeito do ban varia com a **intensidade pré-ban de exposição** à pulverização aérea entre municípios. O tratamento é **contínuo (dose)**, não binário.
- ⚠️ **A curva custa mais caro que o nível.** CGS separam dois parâmetros: `ATT(d|d)` (nível) sai sob paralelismo tradicional; a **curva** — `ATE(d)`/`ACR(d)` — exige **strong parallel trends** (Assumption 5), que exclui *selection-on-gains*. Placebo pré-tratamento **não testa** essa hipótese. Decisão tomada: a curva é o resultado principal, **acompanhada dos limites da §5.1** sob hipótese de direção do viés. Ver `docs/ars/03-modelagem-ensaio1.md`.
- **Janela principal:** 2015 → 19/12/2024, cortada na Lei 19.135/2024 (exceção de drones) para preservar a cota zero. O segundo evento também é estadual e simultâneo — não é adoção escalonada.

**Estimador primário.** Callaway, Goodman-Bacon & Sant'Anna (2024, NBER WP 32117 / arXiv:2107.02637) — DiD com **tratamento contínuo**.
- ⚠️ **Não** é DiD escalonado. O ban é **estadual e simultâneo** (Lei 16.820/2019, art. 28-B; sanção **08/01/2019**, publicação e vigência **09/01/2019**): não há variação de *timing*. **Marco de antecipação:** a ALECE aprovou o PL 18/2015 por unanimidade em **18/12/2018**, após quatro anos de tramitação — é aí, não na sanção, que o resultado deixa de ser incerto para o produtor, e os *leads* do event study precisam cobrir esse ponto. Fonte: texto oficial das leis 16.820/2019 e 12.228/1993 (consolidada) em `docs/legislacao/`. Callaway–Sant'Anna (2021), de Chaisemartin–D'Haultfœuille (2020) e Goodman-Bacon (2021) tratam variação de *timing*, não de dose — são referência conceitual, **não** os estimadores principais.

**Variável de dose.** Intensidade agrícola pré-ban (PAM/IBGE, média 2015–2018) de culturas dependentes de pulverização. ⚠️ **A cultura-âncora ainda não está fixada — ver "Flags de auditoria".** Não hard-codar "algodão" nem "fruticultura" antes de verificar a dispersão empírica.

**Instrumento para exposição endógena.** Aptidão agroclimática **FAO-GAEZ** (percentil de *attainable yield*), seguindo Reynier & Rubin (2025, *PNAS* 122(3):e2413013121 — análogo dos EUA: glifosato + GAEZ + saúde perinatal) e a lógica de Dias, Rocha & Soares (2023, *ReStud*). Endereça a endogeneidade de *onde* culturas de alta pulverização são plantadas.

**Canal água.** SISAGUA; DiD montante/jusante dentro de bacia hidrográfica (shapefiles ANA). Template: DRS (2023).

**Robustez e comunicação.**
- Synthetic DiD (Arkhangelsky et al. 2021) para o agregado estadual.
- **PSM+DiD** como camada de comunicação para o orientador (idioma do Renato).
- Inferência com poucos clusters tratados e desfechos raros: Conley–Taber (2011) / wild-cluster bootstrap. Não superestimar precisão.

**Desfechos (SINASC).** Peso ao nascer (`PESO`), baixo peso (<2500 g), prematuridade (<37 semanas), colapsados a **município × ano-mês**.

## Fontes de dados e acesso
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
- Pipeline em scripts numerados: `scripts/data_prep/01_*`, `02_*` → `scripts/build_panel/` → `scripts/estimate/` → `scripts/figures/`.
- **Python-first** (pandas, `pyfixest`, `sidrapy`, `pysus`, `geopandas`). **R apenas para o estimador CGS de tratamento contínuo** (pacotes `contdid`/`did`), chamado como passo `Rscript` isolado. **A fronteira entre linguagens é I/O de arquivo** (parquet/CSV), nunca in-process: Python prepara o painel → grava parquet → `Rscript` estima → grava CSV *tidy* → Python lê de volta para tabelas/figuras. Isso mantém a reprodutibilidade.
- Reprodutibilidade: `requirements.txt` (Python) + `renv.lock` (R). Fixar seeds. Documentar a *vintage* de cada base (data de extração).
- **Nunca commitar** `data/raw`, `data/processed`, nem microdado. Commitar só código, docs e tabelas agregadas/derivadas seguras. Ver `.gitignore`.

## Flags de auditoria (tratar como incertezas vivas, não fatos)
Ao escrever código de análise, **explicitar estas como hipóteses a checar**, não como verdades assentadas:
0. **Bans municipais anteriores.** O art. 29 da Lei 12.228/1993 autoriza municípios a legislar supletivamente, e Limoeiro do Norte teria proibido a pulverização aérea já em **2009**. Se procede, há municípios **já tratados** dentro do grupo de dose alta, e 2015–2018 não é pré-tratamento para todos. Levantar as leis municipais antes de montar o painel. Ver `docs/legislacao/README.md`.
1. **Cultura-âncora não verificada.** Área de algodão pode ser fina no pós-bicudo; o agronegócio da Chapada do Apodi é fruta/melão, não algodão. **Verificar a variação de dose no PAM antes de fixar a cultura.**
2. **Descasamento tratamento/químico.** O ban proíbe o **método aéreo**, não moléculas; glifosato é frequentemente terrestre. O efeito detectável pode se restringir a químicos/culturas de aplicação aérea.
3. **Lacuna de *enforcement*.** Proibir método ≠ proibir molécula.
4. **Poder estatístico.** Poucos municípios tratados + desfechos raros → usar Conley–Taber / wild bootstrap; não exagerar precisão.
5. **O `d = 0` não é zero de tratamento.** Área nula na PAM é zero de *proxy*. E o §2º do art. 28-B alcança **dispersão aérea para controle vetorial**: município sem agricultura pulverizada mas com controle aéreo de dengue **é tratado** — e esses tendem a ser os maiores, então a contaminação correlaciona com porte, que correlaciona com desfecho. Quatro construções de zero em `docs/ars/03-modelagem-ensaio1.md` §5.3.
6. **Seleção para nascimento vivo.** Se o ban reduz óbito fetal, fetos marginais passam a nascer e entram na cauda de baixo peso — o efeito sobre peso médio vem atenuado ou invertido. Por isso o **SIM** é fonte de primeira linha, não acessório.

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
