#!/usr/bin/env Rscript
# E7-bis — PODER do teste de pré-tendências (Roth 2022, pacote `pretrends`).
#
# ══════════════════════════════════════════════════════════════════════════════
# POR QUE ESTE SCRIPT EXISTE
# ══════════════════════════════════════════════════════════════════════════════
# `docs/did-analysis-aderencia.md` registra, ao adotar o `pretrends`:
#
#   "Este desenho tem poder curto por admissão própria. Num desenho assim, um
#    teste de pré-tendências que 'passa' pode não informar nada: ele passa
#    porque não tem poder para detectar a violação, não porque a violação não
#    existe. A D1 inteira se apoia na credibilidade desse placebo. Medir o poder
#    dele deixa de ser refinamento e vira pré-requisito."
#
# O `03_contdid.R` reporta quantos leads ficam fora da banda. Isso NÃO é o
# poder — é o resultado do teste. Este script responde a outra pergunta: **que
# violação o teste conseguiria ver?**
#
# ⚠️ E a resposta corrige uma conta de guardanapo que é fácil de fazer errado.
# Olhar a meia-largura de um lead isolado (~86 g aqui) e compará-la ao efeito
# procurado (15 g) sugere que o teste é inútil — razão de 5,7×. **Está errado.**
# O teste de tendência usa os 46 leads CONJUNTAMENTE para detectar uma
# inclinação linear, e o teste conjunto é muito mais potente que qualquer lead
# sozinho. É exatamente por isso que o `pretrends` existe, e por que a conta à
# mão não substitui rodá-lo.
#
# ══════════════════════════════════════════════════════════════════════════════
# O QUE ESTE SCRIPT NÃO RESOLVE
# ══════════════════════════════════════════════════════════════════════════════
# ⚠️ **`pretrends` opera sobre coeficientes de EVENT STUDY**, e o sieve do
# `contdid` não faz event study — a curva sai de outro estimador. Então o poder
# medido aqui é sobre o **objeto vizinho**, não sobre a curva que é o resultado
# principal. O texto tem de dizer de qual objeto fala. Ver
# `docs/did-analysis-aderencia.md`, seção "A ressalva que não dá para omitir".
#
# ⚠️ **O `sigma` é analítico, construído da função de influência**
# (`crossprod(IF)/n^2`), enquanto os erros-padrão reportados pelo `03_contdid.R`
# vêm do bootstrap multiplicador. Os dois concordam em ordem de grandeza — 31,0
# contra 35,1 no primeiro lead, 26,6 contra 24,2 no segundo — mas não são o
# mesmo objeto. É aproximação declarada, não identidade.
#
# ⚠️ **`slope_for_power` falha abaixo de 80% de poder** neste desenho: o
# root-finder retorna "valores f() nas extremidades não têm sinais opostos". Não
# é erro de uso — é a função de poder não cruzando o alvo dentro do intervalo de
# busca. Os pontos de 50% a 70% ficam sem resposta, e fingir que existem seria
# inventar.
#
# USO
#   Rscript scripts/estimate/06_pretrends.R --desfecho peso_medio

suppressPackageStartupMessages({
  library(arrow); library(data.table); library(contdid); library(pretrends)
})

args <- commandArgs(trailingOnly = TRUE)
CONHECIDOS <- c("--painel", "--desfecho", "--saida", "--seed", "--biters",
                "--referencia", "--meses-pos")
if ("--help" %in% args || "-h" %in% args) {
  cat("E7-bis — poder do teste de pré-tendências\n\n")
  cat("  --painel      parquet do painel [data/processed/painel_ensaio1.parquet]\n")
  cat("  --desfecho    coluna do desfecho [peso_medio]\n")
  cat("  --referencia  período de referência do event study [-1]\n")
  cat("  --meses-pos   janela pós para traduzir inclinação em viés [48]\n")
  cat("  --seed        semente [20190613]\n")
  quit(status = 0)
}
desconhecidas <- setdiff(grep("^--", args, value = TRUE), CONHECIDOS)
if (length(desconhecidas) > 0) {
  cat("[erro] opção desconhecida:", paste(desconhecidas, collapse = ", "), "\n")
  quit(status = 2)
}
le <- function(nome, padrao) {
  i <- which(args == nome); if (length(i) == 0) padrao else args[i + 1]
}
caminho <- le("--painel", "data/processed/painel_ensaio1.parquet")
desfecho <- le("--desfecho", "peso_medio")
saida <- le("--saida", "data/processed")
ref <- as.integer(le("--referencia", "-1"))
meses_pos <- as.integer(le("--meses-pos", "48"))
biters <- as.integer(le("--biters", "200"))
set.seed(as.integer(le("--seed", "20190613")))

barra <- strrep("=", 84)
cat(barra, "\n")
cat("E7-bis — PODER DO TESTE DE PRÉ-TENDÊNCIAS |", desfecho, "\n")
cat(barra, "\n")

painel <- as.data.table(read_parquet(caminho))
painel[, id := as.integer(factor(cod_ibge6))]
painel[, y := get(desfecho)]
painel[, t := ano * 12L + mes - 1L]
mensal <- painel[!is.na(y), .(id, t, y, dose)]
mensal <- mensal[id %in% mensal[, .N, by = id][N == max(N), id]]
mensal[, g := fifelse(dose > 0, 2019L * 12L, 0L)]
cat("painel balanceado:", uniqueN(mensal$id), "municípios ×", uniqueN(mensal$t), "meses\n")

es <- suppressWarnings(cont_did(
  yname = "y", dname = "dose", gname = "g", tname = "t", idname = "id",
  data = as.data.frame(mensal), target_parameter = "level",
  aggregation = "eventstudy", treatment_type = "continuous",
  dose_est_method = "parametric", control_group = "nevertreated",
  biters = biters, cband = TRUE))

ev <- es$event_study
IF <- ev$inf.function$dynamic.inf.func.e
if (is.null(IF)) stop("event_study sem `inf.function$dynamic.inf.func.e` — API mudou.")
sigma_full <- crossprod(IF) / nrow(IF)^2

ok <- which(!is.na(ev$att.egt) & is.finite(ev$att.egt))
beta <- ev$att.egt[ok]; sg <- sigma_full[ok, ok]; tv <- ev$egt[ok]
pre_idx <- which(tv < ref)
cat("tempos de evento com estimativa:", length(ok),
    "| faixa:", min(tv), "a", max(tv), "\n")
cat("referência:", ref, "| leads usados no teste conjunto:", length(pre_idx), "\n")

# ⚠️ Concordância entre o sigma analítico e o erro-padrão do bootstrap. Se
# divergirem muito, o poder calculado aqui não descreve o teste que o
# 03_contdid.R roda — e a comparação tem de aparecer, não ficar implícita.
cat("\nsigma analítico vs. ep do bootstrap (4 primeiros leads):\n")
cat("  analítico:", paste(round(sqrt(diag(sg))[1:4], 1), collapse = " "), "\n")
cat("  bootstrap:", paste(round(ev$se.egt[ok][1:4], 1), collapse = " "), "\n")

cat("\n", barra, "\n", sep = "")
cat("QUE VIOLAÇÃO O TESTE CONSEGUIRIA VER?\n")
cat(barra, "\n")
linhas <- list()
for (pw in c(0.5, 0.6, 0.7, 0.8, 0.9)) {
  s <- tryCatch(slope_for_power(sigma = sg, targetPower = pw, tVec = tv,
                                referencePeriod = ref, prePeriodIndices = pre_idx),
                error = function(e) NA_real_)
  if (is.na(s)) {
    cat(sprintf("  poder %2.0f%%: — (root-finder não converge neste desenho)\n", pw * 100))
  } else {
    cat(sprintf("  poder %2.0f%%: %.4f g/mês  →  viés de %.2f g em %d meses de pós\n",
                pw * 100, s, s * meses_pos, meses_pos))
    linhas[[length(linhas) + 1]] <- data.table(
      poder = pw, inclinacao_g_mes = s, vies_acumulado_g = s * meses_pos,
      meses_pos = meses_pos, desfecho = desfecho, n_leads = length(pre_idx))
  }
}

cat("\n", barra, "\n", sep = "")
cat("COMO LER — e o que este script NÃO diz\n")
cat(barra, "\n")
cat("  • A tabela é sobre PODER, não sobre resultado. Ela diz que violação o\n")
cat("    teste veria, não se há violação.\n")
cat("  • ⚠️ A comparação que importa é com o EFEITO PROCURADO: o piso da §5 da\n")
cat("    pré-especificação é 15 g. Uma tendência que gere menos viés que isso\n")
cat("    passa despercebida, e o placebo não a exclui.\n")
cat("  • ⚠️ Isto mede o poder do EVENT STUDY, que é outro estimador que a curva.\n")
cat("    O texto tem de dizer de qual objeto fala.\n")
cat("  • ⚠️ Leads dentro do zero nunca provam paralelismo. Com esta tabela na\n")
cat("    mão, a frase honesta é 'o teste exclui tendências acima de X, não\n")
cat("    exclui abaixo' — e X está aí.\n")
cat(barra, "\n")

if (length(linhas) > 0) {
  tabela <- rbindlist(linhas)
  dir.create(saida, recursive = TRUE, showWarnings = FALSE)
  destino <- file.path(saida, sprintf("pretrends_poder__%s.csv", desfecho))
  fwrite(tabela, destino)
  cat("\n[ok]", destino, "\n")
} else {
  cat("\n⚠️ Nenhum ponto de poder convergiu — nada gravado.\n")
}
