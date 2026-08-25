#!/usr/bin/env Rscript
# Exporta SINASC, SIM e SIH do DATASUS via datazoom.saude para arquivo.
#
# POR QUE ISTO EXISTE, E POR QUE É R
# ----------------------------------
# `datazoom.saude` (datazoompuc, PUC-Rio) é pacote **R**. O CLAUDE.md já fixa a
# regra para esse caso: a fronteira entre linguagens é **I/O de arquivo**, nunca
# in-process — a mesma regra que vale para o `contdid`. Então este script é o
# passo `Rscript` que grava, e os scripts 02/03 (Python) leem com `--caminho`.
#
# ⚠️ ISTO NÃO CONTORNA O BLOQUEIO DE REDE. Verificado no código do pacote: ele
# baixa de `ftp://ftp.datasus.gov.br`, exatamente o host que a política de rede
# da sessão remota barra. Rode na SUA máquina; traga o arquivo.
#
# O QUE A LÍNGUA MUDA
# -------------------
# `language = "pt"` aqui não é estética: os scripts 02 e 03 têm tabela de alias
# para as DUAS convenções do pacote, conferida contra o `R/dictionary.R` dele.
# "pt" está fixado abaixo para que o arquivo gravado seja sempre o mesmo,
# independente de o padrão do pacote ("eng") mudar de versão.
#
# USO
#   Rscript scripts/data_prep/00_export_datazoom.R --anos 2015:2022 --saida data/raw
#   Rscript scripts/data_prep/00_export_datazoom.R --bases sinasc,fetal
#
# SAÍDA (em data/raw/, que é gitignored — microdado nunca vai para o repositório)
#   sinasc_ce_<ano>.csv.gz     -> scripts/data_prep/02_clean_births.py --caminho
#   sim_dofet_ce_<ano>.csv.gz  -> scripts/data_prep/03_clean_fetal_deaths.py --caminho --ja-fetal
#   sih_rd_ce_<ano>.csv.gz     -> canal de intoxicação aguda (A5 do roteiro)

suppressPackageStartupMessages({
  library(datazoom.saude)
  library(data.table)
})

# --- parâmetros -------------------------------------------------------------

UF <- "CE"
LINGUA <- "pt"  # fixado: ver nota acima. O padrão do pacote é "eng".

args <- commandArgs(trailingOnly = TRUE)
le_arg <- function(nome, padrao) {
  i <- which(args == nome)
  if (length(i) == 0) padrao else args[i + 1]
}

anos_txt <- le_arg("--anos", "2015:2022")
anos <- eval(parse(text = anos_txt))
saida <- le_arg("--saida", "data/raw")
bases <- strsplit(le_arg("--bases", "sinasc,fetal,sih"), ",")[[1]]

dir.create(saida, recursive = TRUE, showWarnings = FALSE)

cat(strrep("=", 78), "\n")
cat("EXPORTA DATAZOOM.SAUDE ->", saida, "\n")
cat("UF:", UF, "| anos:", paste(range(anos), collapse = "-"),
    "| língua:", LINGUA, "| bases:", paste(bases, collapse = ", "), "\n")
cat(strrep("=", 78), "\n")

grava <- function(dados, nome) {
  if (is.null(dados) || nrow(dados) == 0) {
    cat("  [aviso]", nome, "veio vazio — nada gravado.\n")
    return(invisible(NULL))
  }
  caminho <- file.path(saida, paste0(nome, ".csv.gz"))
  data.table::fwrite(dados, caminho)
  cat("  [ok]", caminho, "|", format(nrow(dados), big.mark = "."), "linhas\n")
}

# --- SINASC: o desfecho principal -------------------------------------------

if ("sinasc" %in% bases) {
  cat("\nSINASC (nascidos vivos)\n")
  for (ano in anos) {
    dados <- tryCatch(
      load_births(time_period = ano, states = UF, language = LINGUA),
      error = function(e) { cat("  [erro]", ano, ":", conditionMessage(e), "\n"); NULL }
    )
    grava(dados, sprintf("sinasc_ce_%d", ano))
  }
}

# --- SIM/DOFET: o teste de seleção ------------------------------------------
#
# ⚠️ Duas coisas que o script 03 precisa saber sobre esta saída:
#   1. DOFET **já é só óbito fetal** e pode não trazer TIPOBITO. Passe --ja-fetal
#      ao script 03, ou deixe que ele detecte (e anuncie) a ausência.
#   2. DOFET é **nacional**, não por UF. O `states` é ignorado aqui; o recorte
#      para o Ceará acontece do lado Python, em `filtra_ceara`.

if ("fetal" %in% bases) {
  cat("\nSIM / DOFET (óbito fetal) — base NACIONAL, recorte CE feito no Python\n")
  for (ano in anos) {
    dados <- tryCatch(
      load_mortality(dataset = "fetal", time_period = ano, language = LINGUA),
      error = function(e) { cat("  [erro]", ano, ":", conditionMessage(e), "\n"); NULL }
    )
    grava(dados, sprintf("sim_dofet_ce_%d", ano))
  }
}

# --- SIH: o canal de substituição aéreo -> terrestre (A5) --------------------
#
# Hipótese do canal: proibido o avião, a aplicação migra para trator e costal —
# o que APROXIMA o aplicador do veneno e pode AUMENTAR intoxicação aguda
# ocupacional, mesmo que a deriva sobre a população caia. Efeito de sinal oposto
# ao do desfecho perinatal, e por isso vale medir separado.
#
# O `reduced_aih` traz `cid_diagnostico_principal` (CID-10),
# `codigo_ibge_municipio_residencia` e `data_internacao` — o suficiente para
# montar o painel município × mês por causa. Os CID de interesse ficam do lado
# Python, para não enterrar decisão de escopo aqui dentro.

if ("sih" %in% bases) {
  cat("\nSIH / AIH reduzida (internações) — para o canal de intoxicação aguda\n")
  for (ano in anos) {
    dados <- tryCatch(
      load_hospital_admissions(dataset = "reduced_aih", time_period = ano,
                               states = UF, language = LINGUA),
      error = function(e) { cat("  [erro]", ano, ":", conditionMessage(e), "\n"); NULL }
    )
    grava(dados, sprintf("sih_rd_ce_%d", ano))
  }
}

cat("\n", strrep("=", 78), "\n", sep = "")
cat("Próximo passo, do lado Python:\n")
cat("  python scripts/data_prep/02_clean_births.py --fonte arquivos \\\n")
cat("      --caminho", file.path(saida, "sinasc_ce_*.csv.gz"), "\n")
cat("  python scripts/data_prep/03_clean_fetal_deaths.py --fonte arquivos --ja-fetal \\\n")
cat("      --caminho", file.path(saida, "sim_dofet_ce_*.csv.gz"), "\n")
cat("\n⚠️ data/raw/ é gitignored. Microdado não vai para o repositório.\n")
cat("⚠️ Anote a data desta extração em docs/fontes-e-vintages.md.\n")
cat(strrep("=", 78), "\n")
