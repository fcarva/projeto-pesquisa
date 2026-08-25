#!/usr/bin/env bash
set -euo pipefail

# setup.sh — scaffold do repositório da tese (pulverização aérea / Ceará)
# Uso: bash setup.sh
# Seguro: usa mkdir -p e NÃO sobrescreve arquivos existentes (CLAUDE.md,
# README.md, .gitignore, requirements.txt, setup_r.R).

# Se já estamos na raiz do repositório da tese (CLAUDE.md presente), monta a
# árvore aqui mesmo em vez de criar um subdiretório aninhado.
if [ -f CLAUDE.md ]; then
  ROOT="."
  echo "==> CLAUDE.md encontrado: montando/conferindo a estrutura no diretório atual."
else
  ROOT="tese-agrotoxicos-ceara"
  echo "==> Criando estrutura em ./$ROOT"
fi

mkdir -p "$ROOT"/{data/raw,data/processed,data/geo,notebooks,scripts/data_prep,scripts/build_panel,scripts/estimate,scripts/figures,paper/tables,paper/figures,docs,tests}
cd "$ROOT"

# .gitkeep para versionar diretórios (senão o Git ignora pastas vazias)
find data notebooks scripts paper docs -type d -exec touch {}/.gitkeep \;

# .gitignore — microdado nunca vai para o Git
if [ ! -f .gitignore ]; then
cat > .gitignore <<'EOF'
# --- Dados sensíveis: microdado só vive em data/, e data/ não é versionado ---
# Padrão "dir/*" (e não "dir/"): o Git desce no diretório, então a exceção do
# .gitkeep abaixo funciona.
data/raw/*
data/processed/*
data/geo/*
!data/raw/.gitkeep
!data/processed/.gitkeep
!data/geo/.gitkeep

# --- Binários de microdado/geo em qualquer lugar (defesa em profundidade) ---
*.dbc
*.dbf
*.shp
*.shx
*.prj
*.cpg
*.tif
*.tiff
*.parquet

# --- Ambientes ---
.venv/
venv/
__pycache__/
*.pyc
.pytest_cache/
.Rproj.user/
renv/library/
renv/staging/
.Renviron
.Rhistory

# --- Sistema / editores ---
.DS_Store
.ipynb_checkpoints/
.vscode/
EOF
fi

# requirements.txt (Python-first)
if [ ! -f requirements.txt ]; then
cat > requirements.txt <<'EOF'
pandas
numpy
pyarrow
pyfixest
sidrapy
pysus==2.10.0
geopandas
matplotlib
pytest
EOF
fi

# Base dos Dados é opcional: sua versão atual exige uma faixa de loguru
# incompatível com o PySUS 2.10.0. Instale-a em ambiente separado quando
# consultas ao BigQuery forem necessárias.
if [ ! -f requirements-basedosdados.txt ]; then
cat > requirements-basedosdados.txt <<'EOF'
basedosdados==2.0.3
EOF
fi

# Bootstrap mínimo do R (só para o estimador de tratamento contínuo)
if [ ! -f scripts/estimate/setup_r.R ]; then
cat > scripts/estimate/setup_r.R <<'EOF'
# Ambiente R isolado para o estimador CGS de tratamento contínuo.
# Rodar uma vez: Rscript scripts/estimate/setup_r.R
install.packages("renv")
renv::init(bare = TRUE)
renv::install(c("did", "data.table", "fixest"))
renv::install("bcallaway11/contdid")  # contdid: fonte GitHub, ver comentário no arquivo
renv::snapshot()
EOF
fi

# Stubs (NÃO sobrescreve se você já colocou os arquivos fornecidos)
[ -f README.md ] || printf '# tese-agrotoxicos-ceara\n\n> Substituir por README.md fornecido.\n' > README.md
[ -f CLAUDE.md ] || printf '# CLAUDE.md\n\n> Substituir por CLAUDE.md fornecido.\n' > CLAUDE.md

# Git
if [ ! -d .git ]; then
  git init -q
  git add -A
  echo "==> Repositório Git inicializado (commit ainda não feito)."
fi

cat <<'EOF'

==> Pronto. Próximos passos:
  1. Confira que CLAUDE.md e README.md estão na raiz e prompts.md em docs/.
  2. python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
      # Base dos Dados/BigQuery: use um ambiente separado e requirements-basedosdados.txt
  3. Rscript scripts/estimate/setup_r.R          # uma vez, para o R
  4. python scripts/data_prep/01_check_dose_variation.py   # Tarefa 1: variação de dose
  5. python scripts/data_prep/02_clean_births.py           # Tarefa 2: SINASC
  6. git add -A && git commit -m "scaffold inicial da tese"
EOF
