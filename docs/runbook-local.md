# Runbook — rodar o pipeline na sua máquina

*Como sair de "nada rodou contra dado real" com o mínimo de passos, e na ordem
certa. Escrito em 2026-09-21, contra o código em `72c074a`.*

> ⚠️ **Nada neste documento foi executado.** A sessão remota bloqueia
> `apisidra.ibge.gov.br` e `ftp.datasus.gov.br`; os comandos abaixo foram
> extraídos do `--help` de cada script, não supostos, mas a primeira rodada real
> é sua. Onde eu sei que há risco, está marcado.

---

## 0. Identificadores

```bash
git clone https://github.com/fcarva/projeto-pesquisa
cd projeto-pesquisa
git checkout claude/new-session-fmif38
git log -1 --format='%H %s'   # 72c074a... Justificativa: o argumento de mérito
```

| | |
|---|---|
| Repositório | `fcarva/projeto-pesquisa` |
| Branch de trabalho | `claude/new-session-fmif38` |
| Commit | `72c074ad2591f8610862619861ce03cb65fadf90` |
| Sessão que produziu | https://claude.ai/code/session_0163avxXFMJviKB43SZc37Kv |

---

## 1. A ordem não é a ordem do pipeline

O instinto é rodar `make real` e ver o coeficiente. Esse é exatamente o caminho
que o repositório foi construído para bloquear, e o bloqueio é deliberado: `make
real` falha enquanto `docs/pre-especificacao.md` não trouxer o marcador
`PRESPEC_STATUS: FECHADA` (hoje está `ABERTA`).

A razão é que **duas decisões dependem de números que ainda não existem**, e as
duas vêm antes de qualquer estimação:

| Número | Sai de | Decide |
|---|---|---|
| DP das tendências municipais de peso ao nascer no pré-período | **SINASC** (script 02) | se o efeito de 15–25 g é detectável — E1.5 |
| Nº de municípios com dose alta, e a cultura-âncora | **PAM/SIDRA** (script 01) | se a curva dose-resposta se sustenta — Gate 1 |

Enquanto eles não existirem, boa parte do que parece questão metodológica é
questão empírica esperando dado. Por isso a ordem é: **aquisição → os dois
números → a pré-especificação → estimação.**

⚠️ **Os scripts individuais não estão travados** — só o alvo `make real` está. Os
passos 2 a 5 abaixo rodam hoje, sem tocar na pré-especificação. É de propósito:
o portão protege a *estimação*, não o *diagnóstico*.

---

## 2. Passo 0 — ambiente

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make teste          # 92 testes, ~25 s. Se não passar, pare aqui.
make simulado       # o pipeline inteiro com dado sintético — valida a fiação
```

`make simulado` não é evidência sobre nada; serve para provar que o código roda
na sua máquina antes de você gastar banda com microdado.

**R só é necessário no passo 6** (e no passo 4, se o `pysus` falhar). Não instale
agora.

---

## 3. Passo 1 — PAM/SIDRA: o mais barato, e é o Gate 1

API HTTP pura, sem FTP, sem microdado. Comece por aqui.

```bash
# preflight: confere os códigos contra a API de metadados. NÃO baixa dado.
python scripts/data_prep/01_check_dose_variation.py --verificar-codigos

# o download de verdade
python scripts/data_prep/01_check_dose_variation.py --fonte sidra
```

⚠️ **Por que o preflight existe.** Um código de variável ou classificação errado
no SIDRA devolve **vazio, não erro** — o script falharia silenciosamente com um
"não há variação de dose" que seria artefato. As tabelas usadas são a **1612**
(lavoura temporária, variável 109, classificação 81) e a **1613** (permanente,
variável 2313, classificação 82).

**Se a API não responder**, baixe as duas tabelas pelo portal do SIDRA e use:

```bash
python scripts/data_prep/01_check_dose_variation.py --fonte arquivo \
    --caminho ~/Downloads/tabela1612.csv ~/Downloads/tabela1613.csv
```

O parser detecta a linha de rótulo em vez de pular um número fixo de linhas —
formato de portal varia, e isso já mordeu uma vez.

**O que ler na saída:** `n_muni_positivo`, `n_muni_decil_superior`,
`especificacao` e `motivo`. A coluna `especificacao` aplica a escada do CGS
(≥40 municípios → curva não-paramétrica; 15–39 → faixas; 12–14 → faixas com
suporte fino; <12 → binário, curva abandonada). **A coluna recomenda; você
ratifica.**

---

## 4. Passo 2 — SINASC e SIM: o número que decide o ensaio

Duas rotas. Tente o Python primeiro — evita instalar R agora.

```bash
python scripts/data_prep/02_clean_births.py --fonte pysus --anos 2015 2016 2017 2018 2019 2020 2021 2022
python scripts/data_prep/03_clean_fetal_deaths.py --fonte pysus \
    --nascimentos data/processed/nascimentos_ce_muni_mes.parquet
```

⚠️ **O modo de falha mais perigoso do projeto inteiro está aqui.** O óbito fetal
já voltou **zero linhas em silêncio** numa rodada anterior — e um painel de óbito
fetal vazio **imita** um teste de seleção benigno. Confira a contagem antes de
seguir:

```bash
python -c "
import pandas as pd
d = pd.read_parquet('data/processed/obitos_fetais_ce_muni_mes.parquet')
print(d.shape, d.filter(like='obito').sum().to_dict())
"
```

Zero não é "não há problema de seleção"; é "o download falhou".

**Se o `pysus` falhar** (a API do DATASUS muda de forma sem aviso), a rota R:

```bash
Rscript scripts/data_prep/00_export_datazoom.R --anos 2015:2022 --saida data/raw
python scripts/data_prep/02_clean_births.py --fonte arquivos --caminho data/raw/sinasc_ce_*.csv.gz
python scripts/data_prep/03_clean_fetal_deaths.py --fonte arquivos --ja-fetal \
    --caminho data/raw/sim_dofet_ce_*.csv.gz \
    --nascimentos data/processed/nascimentos_ce_muni_mes.parquet
```

⚠️ `--ja-fetal` é obrigatório com o arquivo DOFET: ele **já é** só óbito fetal, e
aplicar o filtro `TIPOBITO==1` por cima zeraria o painel.

---

## 5. Passo 3 — SIH: só pela rota R

⚠️ **O script 04 não tem downloader Python** — aceita `{auto, arquivos,
simulado}`, sem `pysus`. Então o canal de intoxicação (e o placebo X48/X68 que
vem com ele) depende do `00_export_datazoom.R`.

```bash
Rscript scripts/data_prep/00_export_datazoom.R --bases sih --anos 2015:2022
python scripts/data_prep/04_clean_poisoning.py --fonte arquivos --caminho data/raw/sih_rd_ce_*.csv.gz
```

Expectativa realista: na rodada simulada, **100% das células município-mês
ficaram abaixo de 5 internações**. Intoxicação internada é evento raro. Se isso
se confirmar no dado real, o canal vira descritivo no texto, não estimativa — e
é assim que a Justificativa §5 já o declara.

---

## 6. Passo 4 — o MDE, e só então a D7

Agora os dois números existem. Junte-os:

```bash
python scripts/data_prep/01_check_dose_variation.py --fonte sidra \
    --nascimentos data/processed/nascimentos_ce_muni_mes.parquet \
    --efeito-esperado-g 15
```

Isso acrescenta `sd_tendencia_g`, `mde_ingenuo_g`, `mde_agrupado_g` e a coluna
`falsifica`. A regra: meia-largura do IC = **0,70 × MDE**, logo o desenho
falsifica 15 g quando o **MDE fica abaixo de 21,4 g**.

**Aqui para a máquina e começa a conversa com o orientador.** Com o MDE e o
número de municípios de dose alta na mão, preencha `docs/pre-especificacao.md`:
desfecho primário, exposição primária, o que é confirmatório, se há correção de
família, e que **X68 é falsificação, não desfecho**. Troque o marcador da linha 9
para `<!-- PRESPEC_STATUS: FECHADA -->`, date, e **commite**.

O commit é o carimbo de tempo: o histórico do git prova que o plano é anterior ao
dado. É a única coisa desta lista que fica impossível de fazer depois.

---

## 7. Passo 5 — GAEZ (a lacuna mais cara)

Depois do E6, o GAEZ deixou de ser "o instrumento" e virou **mecânico**: o sieve
do `contdid` centra a curva inteira em `mean(dy[dose == 0])`, então quem está no
grupo de dose zero **desloca o nível da curva**, não apenas acrescenta ruído.

```bash
pip install -r requirements-geo.txt     # rasterio, geopandas, shapely, pyproj, rasterstats
```

Baixe à mão, do portal da FAO-GAEZ, os GeoTIFF de *attainable yield* em **dois
cenários de insumo** (alto e baixo) para cada cultura relevante, mais a malha
municipal do IBGE. Depois:

```bash
python scripts/data_prep/06_build_gaez.py \
    --culturas banana melao \
    --raster-alto  data/geo/banana_alto.tif data/geo/melao_alto.tif \
    --raster-baixo data/geo/banana_baixo.tif data/geo/melao_baixo.tif \
    --municipios   data/geo/malha_municipal_ce.gpkg
```

⚠️ `--culturas` é **obrigatório e sem padrão**, de propósito: a receita do
Reynier & Rubin é construída sobre culturas **transgênicas** (milho, soja,
algodão), e banana não é. Fixar a lista é decisão sua, não do script. E a ordem
da receita importa — é a **diferença** alto-menos-baixo insumo, depois percentil
nacional, depois **máximo entre culturas *após* o percentil**.

---

## 8. Passo 6 — R, e a estimação

```bash
Rscript scripts/estimate/setup_r.R
```

⚠️ **`renv.lock` ainda não existe no repositório** — este script é que o cria.
E a ordem de instalação dentro dele é carregada: `contdid` depende de `ptetools`,
que é **GitHub-only** e **não aparece no campo `Remotes:`** do `contdid`, então
instalar `contdid` direto falha na dependência. O script instala `ptetools`
antes. Depois de rodar, **commite o `renv.lock`**.

```bash
make real CULTURA="Melão" DESFECHO=peso_medio MDE=<o mde_agrupado_g do passo 4>
```

Ou, passo a passo:

```bash
Rscript scripts/estimate/03_contdid.R --desfecho peso_medio \
    --exposicao share_gestacao_pos_ban --corte-pre 2018-12 --corte-pos 2019-10
python scripts/estimate/04_robustness.py --painel data/processed/painel_ensaio1.parquet \
    --desfecho peso_medio --mde <mde_agrupado_g>
```

⚠️ **`03_contdid.R` nunca foi executado** — não há R nesta sessão. Os nomes de
argumento foram conferidos contra `R/cont_did.R` do repositório do autor (v0.1.1);
a rodada, não. Espere atrito na primeira vez.

**O que ler na saída do E7:** não o p-valor, e sim **a distância entre os três
procedimentos de inferência**. Se o cluster-robusto ingênuo der p = 0,01 e a
inferência por aleatorização der p = 0,31, o resultado não é "significante" — é
"o desenho não distingue". O script avisa quando a razão passa de 3×.

---

## 9. O que não fazer

- **Não commitar nada de `data/`.** O `.gitignore` já bloqueia `*.parquet`,
  `*.dbc`, `*.dbf`, `*.shp` e `*.tif` em qualquer lugar, mas a regra é sua, não
  do arquivo.
- **Não rodar `make real` antes de fechar a pré-especificação.** Se você se pegar
  querendo editar o Makefile para destravar, é exatamente o momento em que o
  portão está funcionando.
- **Não trocar o desfecho porque o poder não fechou.** Peso médio é o único com
  razão efeito/ruído acima de 1 (1,30–1,81, contra 0,44–0,80 para baixo peso e
  0,17 para mortalidade). A saída é **baixar o corte de dose** para encorpar o
  grupo tratado, e registrar que baixou.
- **Não ler saída com `__simulado` no nome do arquivo como resultado.** Os nomes
  carregam a fonte justamente para isso.

---

## 10. Prompts para a sessão local do Claude Code

Cole um por vez, na raiz do repositório:

> Rode `make teste` e `make simulado` e me diga se algo falha na minha máquina.
> Não toque em `data/` nem commite nada ainda.

> Rode o preflight do script 01 (`--verificar-codigos`) e depois `--fonte sidra`.
> Me mostre `n_muni_positivo`, `n_muni_decil_superior`, `especificacao` e
> `motivo`, e diga qual degrau da escada de especificação o dado sustenta.

> Baixe SINASC e SIM pelo `pysus` para 2015–2022 e rode os scripts 02 e 03.
> **Antes de seguir, confira que o painel de óbito fetal não voltou vazio** — zero
> linhas imita um teste de seleção benigno. Se o `pysus` falhar, use a rota R do
> `00_export_datazoom.R`.

> Rode o script 01 de novo com `--nascimentos` e me dê `sd_tendencia_g`,
> `mde_agrupado_g` e a coluna `falsifica`. Compare o MDE com 21,4 g e me diga se
> um nulo seria informativo neste desenho.

> Com esses números, me ajude a preencher `docs/pre-especificacao.md`. Não escolha
> por mim: me apresente as opções de desfecho primário e exposição primária com o
> custo de cada uma. Não altere o marcador `PRESPEC_STATUS` sem eu confirmar.

⚠️ **Um prompt que não vale a pena dar:** "rode o pipeline inteiro e me diga o
resultado". Ele pula os dois gates, e o repositório inteiro foi organizado para
que isso não aconteça por acidente.
