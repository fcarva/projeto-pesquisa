# Ambiente R isolado para o estimador CGS de tratamento contínuo
# (Callaway, Goodman-Bacon & Sant'Anna 2024).
#
# Rodar uma vez, da raiz do repositório:
#   Rscript scripts/estimate/setup_r.R
#
# A fronteira Python/R neste projeto é I/O de arquivo (parquet in, CSV tidy out),
# nunca chamada in-process — ver CLAUDE.md, "Convenções do repositório".

install.packages("renv", repos = "https://cloud.r-project.org")
renv::init(bare = TRUE)

# CRAN
renv::install(c("did", "data.table", "fixest", "arrow"))

# ⚠️ ORDEM IMPORTA AQUI, e o motivo não é óbvio.
#
# `contdid` depende de `ptetools (>= 1.0.1)`, que **não está no CRAN** — é
# GitHub-only (bcallaway11/ptetools, v1.0.2 quando isto foi escrito). E o
# DESCRIPTION do `contdid` **não traz campo `Remotes:`**, então o instalador não
# tem como descobrir onde achar `ptetools` sozinho: `renv::install("bcallaway11/contdid")`
# falha na dependência.
#
# Verificado clonando os dois repositórios em 2026-08-24. Instalar `ptetools`
# ANTES resolve. Se um dia ele for para o CRAN, esta linha continua funcionando.
renv::install("bcallaway11/ptetools")

# `contdid` (implementação do estimador de tratamento contínuo) também é
# distribuído pelo GitHub do autor, não pelo CRAN — instalar como "contdid" puro
# falha com "package not available".
# Conferir em https://github.com/bcallaway11/contdid
renv::install("bcallaway11/contdid")

renv::snapshot()

cat("\n== Ambiente R pronto. Confira renv.lock. ==\n")
