# Prompts de inicialização — Claude Code

Cole no Claude Code, na raiz do repositório (com `CLAUDE.md` presente). Ordem recomendada: **Tarefa 1 antes da Tarefa 2** — se não houver variação de dose entre municípios, o desenho de tratamento contínuo inteiro cai, então a restrição que amarra é checada primeiro.

---

## Tarefa 0 (opcional) — Bootstrap do repositório
Se preferir que o Claude Code monte o scaffold em vez de rodar `setup.sh`:

> Monte o scaffold do repositório da minha tese conforme o `CLAUDE.md`. Crie a árvore `data/{raw,processed,geo}`, `notebooks/`, `scripts/{data_prep,build_panel,estimate,figures}`, `paper/{tables,figures}`, `docs/`; um `.gitignore` que ignore todo microdado sob `data/` e os binários `.dbc/.dbf/.shp/.tif`; `requirements.txt` com o stack Python-first; e um `setup_r.R` que inicialize um `renv` com `did` e `contdid`. Não commite nada em `data/`. Faça o commit inicial só com código e docs.

---

## Tarefa 1 — Verificar a cultura-âncora e a variação de dose (fazer primeiro)

> Antes de fixar a variável de tratamento, preciso testar se existe **variação de dose** utilizável entre municípios do Ceará. Escreva `scripts/data_prep/01_check_dose_variation.py` que:
>
> 1. Baixe (via `sidrapy`, PAM/IBGE) a área plantada/colhida por cultura, por município do Ceará, 2015–2018. Se o acesso não estiver configurado, gere um DataFrame **simulado** com o mesmo esquema (`cod_ibge` do município, `ano`, `cultura`, `area_ha`) e deixe a fonte real como troca de uma linha.
> 2. Para culturas candidatas de alta pulverização (melão, outras frutas irrigadas da Chapada do Apodi, algodão), calcule a **média 2015–2018** por município e a **dispersão entre municípios**: coeficiente de variação, razão p90/p10 e nº de municípios com área > 0.
> 3. Reporte uma tabela por cultura ordenada por dispersão, sinalizando quais têm massa suficiente para servir de dose. **Não** hard-code uma cultura como escolhida — o output é diagnóstico. Salve em `data/processed/` (não commitar) e imprima o resumo no console.
>
> Trate como hipótese a checar, não fato: algodão pode ter área fina pós-bicudo (ver flags em `CLAUDE.md`).

---

## Tarefa 2 — Limpar e colapsar nascimentos (SINASC)

> Escreva `scripts/data_prep/02_clean_births.py` que:
>
> 1. Carregue microdados de nascimentos SINASC com os **nomes reais das colunas do DATASUS**: `CODMUNRES` (município de residência, 6 dígitos IBGE), `DTNASC` (data no formato DDMMAAAA), `PESO` (gramas), `SEMAGESTAC` (semanas de gestação) e, como fallback, `GESTACAO` (categórica), além de `IDADEMAE`, `ESCMAE`, `CONSULTAS`. Se o acesso real (via `pysus` ou Base dos Dados) não estiver configurado, gere um DataFrame **simulado** com essas mesmas colunas e distribuições plausíveis (`PESO` ~ N(3200, 500) com ~9% < 2500; `SEMAGESTAC` com ~11% < 37), e deixe a fonte real como troca de uma linha.
> 2. Filtre municípios do Ceará (UF 23 — os `CODMUNRES` que começam com "23"). Derive: baixo peso = `PESO < 2500`; prematuridade = `SEMAGESTAC < 37` (ou, quando `SEMAGESTAC` faltar, mapeie as categorias de `GESTACAO` para < 37 semanas — categorias 1 a 4). Extraia `ano` e `mes` de `DTNASC`.
> 3. Colapse a **`CODMUNRES` × `ano` × `mes`**: nº de nascimentos, peso médio, taxa de baixo peso, taxa de prematuridade.
> 4. Salve o painel limpo em `data/processed/nascimentos_ce_muni_mes.parquet` (**não commitar**).
>
> Use funções pequenas e testáveis. Comente o descasamento tratamento-aéreo/molécula onde for relevante para a interpretação.

---

## Depois (esboço das próximas tarefas)

- `scripts/build_panel/` — juntar nascimentos + dose (PAM) + instrumento (GAEZ) + bacias (ANA) num painel município×mês.
- `scripts/estimate/03_contdid.R` — estimar a curva dose-resposta com `contdid`, lendo o parquet do painel e gravando um CSV *tidy* de resultados.
- `scripts/estimate/04_robustness.py` — SDID, PSM+DiD, inferência Conley–Taber / wild bootstrap.
- `scripts/figures/` — curva dose-resposta e event-study a partir do CSV de resultados.
- Redação: mudar para o plugin ARS (`/ars-plan`, `/ars-lit-review`) com os resultados já verificados.
