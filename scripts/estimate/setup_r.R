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

# ══════════════════════════════════════════════════════════════════════════════
# CAMADA DE ROBUSTEZ — três lacunas que o roteiro já declarava em aberto
# ══════════════════════════════════════════════════════════════════════════════
#
# Vieram do registro de pacotes do skill `did-analysis`
# (github.com/zhangxiany-tamu/DID). ⚠️ O *workflow* daquele skill NÃO se aplica
# a este desenho — ele é organizado em torno de variação de timing, e o ban do
# Ceará é estadual e simultâneo. Ver docs/did-analysis-aderencia.md antes de
# rodar qualquer coisa de lá. Estes três pacotes, sim, encaixam.
#
# Fontes conferidas no DESCRIPTION de cada repositório, não supostas — o CRAN
# estava inalcançável da sessão que escreveu isto, então a rota verificada é a
# do GitHub. Se `install.packages()` achar no CRAN, tanto melhor.

# Poder do teste de pré-tendências (Roth). O projeto calcula o MDE do EFEITO e
# nada sobre o poder do próprio placebo — e a D1 depende da credibilidade dele.
# Um teste de pré-tendências que "passa" num desenho sem poder não informa nada.
# v0.1.0, GitHub-only. Imports leves: mvtnorm, tmvtnorm, dplyr, ggplot2.
renv::install("jonathandroth/pretrends")

# Rambachan & Roth (2023) — sensibilidade a violações de tendências paralelas.
# É o [N10] do docs/estado-da-arte.md, anotado lá como "munição defensiva de
# primeira" para o ponto fraco declarado deste desenho.
# ⚠️ v0.2.8 importa CVXR (>= 1.8) e ECOSolveR — otimização convexa, instalação
# pesada. Reserve tempo na primeira vez.
renv::install("asheshrambachan/HonestDiD")

# Synthetic DiD (Arkhangelsky, Athey, Hirshberg, Imbens & Wager) — o SDID
# agregado que o roteiro E7 marca como NÃO instrumentado e que o CLAUDE.md nomeia
# na camada de robustez. v0.0.9, GitHub-only, e leve: importa só mvtnorm.
# Aguenta uma única unidade tratada, que é o caso do Ceará.
renv::install("synth-inference/synthdid")

# ⚠️ `gsynth` NÃO entra, e a decisão é sua reverter isto. Dois motivos:
#   1. Ele é desenhado para MÚLTIPLAS unidades tratadas com efeitos fixos
#      interativos. O plano B da D5 é Ceará contra um Ceará sintético — uma
#      unidade tratada só. O `synthdid` acima já cobre esse caso.
#   2. Ele importa `fect (>= 2.0.0)` sem declarar `Remotes:` — a MESMA armadilha
#      do `ptetools` documentada acima. E `fect` importa Rcpp, ou seja, exige
#      toolchain C++ (Rtools no Windows).
# Se quiser mesmo assim, a ordem que funciona é esta:
# renv::install("xuyiqing/panelView")
# renv::install("xuyiqing/fect")
# renv::install("xuyiqing/gsynth")

renv::snapshot()

cat("\n== Ambiente R pronto. Confira renv.lock. ==\n")
