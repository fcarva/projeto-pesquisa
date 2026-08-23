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

# `contdid` (implementação do estimador de tratamento contínuo) é distribuído
# pelo GitHub do autor, não pelo CRAN — instalar como "contdid" puro falha com
# "package not available". Se em algum momento ele for publicado no CRAN, a
# linha abaixo continua funcionando; conferir em https://github.com/bcallaway11/contdid
renv::install("bcallaway11/contdid")

renv::snapshot()

cat("\n== Ambiente R pronto. Confira renv.lock. ==\n")
