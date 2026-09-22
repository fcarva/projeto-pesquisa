#!/usr/bin/env Rscript
# E7-quater — Synthetic DiD (Arkhangelsky, Athey, Hirshberg, Imbens & Wager 2021).
#
# ══════════════════════════════════════════════════════════════════════════════
# ⚠️ ESTE NÃO É O SDID QUE O CLAUDE.md PEDE — e a diferença importa
# ══════════════════════════════════════════════════════════════════════════════
# O `CLAUDE.md` registra: *"Synthetic DiD (Arkhangelsky et al. 2021) para o
# agregado ESTADUAL."* Isto é, **Ceará contra um Ceará sintético** montado com
# outros estados — o desenho em que o SDID brilha, porque aguenta uma única
# unidade tratada.
#
# ⚠️ **Esse desenho não roda com o que existe no repositório.** O painel tem
# apenas municípios do Ceará; o SINASC dos outros 26 estados não foi adquirido.
# Montar o doador exigiria baixar a série nacional — viável pelo `pysus`, mas
# fora do escopo de aquisição declarado.
#
# O que este script faz é a versão **INTRAESTADUAL**: municípios de dose alta
# contra um sintético montado com os municípios `d = 0`. É legítimo e é
# informativo, mas é OUTRO desenho:
#
# | | SDID estadual (o do CLAUDE.md) | SDID intraestadual (este) |
# |---|---|---|
# | unidade tratada | Ceará (1) | 17 municípios do decil superior |
# | doadores | outros estados | 14 municípios de `d = 0` |
# | ameaça principal | choque estadual concorrente | contaminação do `d = 0` (flag 5) |
#
# ⚠️ E a segunda ameaça é a que este projeto já conhece: se o `d = 0` está
# contaminado por controle vetorial aéreo (§2º do art. 28-B), o sintético é
# montado com unidades parcialmente tratadas — e o SDID não conserta isso, só o
# herda.
#
# ══════════════════════════════════════════════════════════════════════════════
# POR QUE TRÊS ESTIMADORES, E NÃO UM
# ══════════════════════════════════════════════════════════════════════════════
# O pacote entrega `synthdid`, `sc` (controle sintético puro) e `did` (DiD
# simples) sobre a MESMA matriz. Rodar os três é o mesmo princípio do
# `04_robustness.py`: **o informativo é a distância entre eles.** Se o SC puro e
# o DiD simples divergem muito, o peso das unidades está fazendo trabalho
# pesado, e isso é uma propriedade do dado que o leitor precisa ver.
#
# ⚠️ **O erro-padrão por placebo NÃO roda aqui**, e o motivo é uma propriedade
# do desenho, não do código: o pacote exige mais controles que tratados, e este
# desenho tem **17 tratados para 14 controles**. Um grupo de comparação menor
# que o grupo tratado é incomum e vale dizer em voz alta — o sintético é montado
# com 14 doadores apenas. Ficam `jackknife` e `bootstrap`.
#
# USO
#   Rscript scripts/estimate/08_synthdid.R --desfecho peso_medio

suppressPackageStartupMessages({
  library(arrow); library(data.table); library(synthdid)
})

args <- commandArgs(trailingOnly = TRUE)
CONHECIDOS <- c("--painel", "--desfecho", "--saida", "--seed", "--aptidao-p",
                "--fracao-decil", "--ano-ban")
if ("--help" %in% args || "-h" %in% args) {
  cat("E7-quater — Synthetic DiD (versão INTRAESTADUAL)\n\n")
  cat("  --painel        parquet do painel [data/processed/painel_ensaio1.parquet]\n")
  cat("  --desfecho      coluna do desfecho [peso_medio]\n")
  cat("  --fracao-decil  fração do topo que é 'tratado' [0.10]\n")
  cat("  --aptidao-p     percentil de aptidão que define o zero crível [0.75]\n")
  cat("  --ano-ban       primeiro ano tratado [2019]\n")
  cat("  --seed          semente [20190613]\n\n")
  cat("⚠️ NÃO é o SDID estadual que o CLAUDE.md pede — ver o cabeçalho.\n")
  quit(status = 0)
}
desconhecidas <- setdiff(grep("^--", args, value = TRUE), CONHECIDOS)
if (length(desconhecidas) > 0) {
  cat("[erro] opção desconhecida:", paste(desconhecidas, collapse = ", "), "\n")
  quit(status = 2)
}
le <- function(n, d) { i <- which(args == n); if (length(i) == 0) d else args[i + 1] }
caminho <- le("--painel", "data/processed/painel_ensaio1.parquet")
desfecho <- le("--desfecho", "peso_medio")
saida <- le("--saida", "data/processed")
fracao <- as.numeric(le("--fracao-decil", "0.10"))
aptidao_p <- as.numeric(le("--aptidao-p", "0.75"))
ano_ban <- as.integer(le("--ano-ban", "2019"))
semente <- as.integer(le("--seed", "20190613"))
set.seed(semente)

barra <- strrep("=", 84)
cat(barra, "\n")
cat("E7-quater — SYNTHETIC DiD (INTRAESTADUAL) |", desfecho, "\n")
cat(barra, "\n")
cat("⚠️ NÃO é o SDID estadual do CLAUDE.md: aquele precisa de outros estados,\n")
cat("   e o SINASC nacional não foi adquirido. Este é município × município.\n\n")

painel <- as.data.table(read_parquet(caminho))
painel <- painel[!is.na(get(desfecho))]
por_muni <- unique(painel[, .(cod_ibge6, dose_ha, aptidao_gaez)])
k <- ceiling(nrow(por_muni[dose_ha > 0]) * fracao)
tratados <- por_muni[dose_ha > 0][order(-dose_ha)][1:k, cod_ibge6]
corte <- as.numeric(quantile(por_muni$aptidao_gaez, aptidao_p, na.rm = TRUE))
controles <- por_muni[dose_ha == 0 & aptidao_gaez <= corte, cod_ibge6]

amostra <- painel[cod_ibge6 %in% c(tratados, controles)]
anual <- amostra[, .(y = mean(get(desfecho), na.rm = TRUE)), by = .(cod_ibge6, ano)]
anual[, tratamento := as.integer(cod_ibge6 %in% tratados & ano >= ano_ban)]
setorder(anual, cod_ibge6, ano)

# ⚠️ `panel.matrices` EXIGE painel balanceado e falha de forma pouco legível se
# não estiver. Conferir aqui é mais barato que depurar a mensagem dele.
n_esperado <- uniqueN(anual$cod_ibge6) * uniqueN(anual$ano)
if (nrow(anual) != n_esperado) {
  stop("painel desbalanceado: ", nrow(anual), " células para ",
       n_esperado, " esperadas. O `panel.matrices` exige balanceado.")
}

pm <- panel.matrices(as.data.frame(anual), unit = "cod_ibge6", time = "ano",
                     outcome = "y", treatment = "tratamento")
n1 <- nrow(pm$Y) - pm$N0
n_pos <- ncol(pm$Y) - pm$T0
cat("doadores (d = 0):", pm$N0, "| tratados:", n1, "\n")
cat("períodos pré:", pm$T0, "| pós:", n_pos, "\n")
if (n1 >= pm$N0) {
  cat("\n⚠️ MAIS TRATADOS QUE DOADORES (", n1, " contra ", pm$N0, ").\n", sep = "")
  cat("   O sintético é montado com um conjunto pequeno, e o erro-padrão por\n")
  cat("   PLACEBO fica indisponível — o pacote exige mais controles que tratados.\n")
}

cat("\n", barra, "\n", sep = "")
cat("TRÊS ESTIMADORES SOBRE A MESMA MATRIZ — o informativo é a DISTÂNCIA\n")
cat(barra, "\n")
linhas <- list()
for (nome in c("synthdid_estimate", "sc_estimate", "did_estimate")) {
  est <- get(nome)(pm$Y, pm$N0, pm$T0)
  tau <- as.numeric(est)
  eps <- list()
  for (mt in c("jackknife", "bootstrap")) {
    v <- tryCatch(vcov(est, method = mt), error = function(e) NA_real_)
    eps[[mt]] <- if (is.na(v)) NA_real_ else sqrt(v)
  }
  ep <- eps[["jackknife"]]
  rot <- sub("_estimate", "", nome)
  if (is.na(ep)) {
    cat(sprintf("  %-10s tau = %8.2f g   (erro-padrão indisponível)\n", rot, tau))
  } else {
    cat(sprintf("  %-10s tau = %8.2f g   ep %6.2f (jack) / %6.2f (boot)   IC95%% [%8.2f ; %8.2f]\n",
                rot, tau, ep, eps[["bootstrap"]], tau - 1.96 * ep, tau + 1.96 * ep))
  }
  # ⚠️ `as.numeric` não é cosmético: `vcov()` devolve matriz 1x1, e sem isto a
  # coluna vira `ic_baixo.V1` — o `data.table` guarda a matriz como coluna-matriz
  # e o filtro por nome falha com "Objeto 'ic_baixo' não encontrado".
  linhas[[length(linhas) + 1]] <- data.table(
    estimador = rot, tau = as.numeric(tau),
    ep_jackknife = as.numeric(eps[["jackknife"]]),
    ep_bootstrap = as.numeric(eps[["bootstrap"]]),
    ic_baixo = as.numeric(tau - 1.96 * ep),
    ic_alto = as.numeric(tau + 1.96 * ep))
}
tab <- rbindlist(linhas)
amplitude <- max(tab$tau) - min(tab$tau)
cat(sprintf("\n  amplitude entre os três: %.2f g\n", amplitude))

# ⚠️ O ALARME QUE ESTE SCRIPT EXISTE PARA DAR. Se UM dos três exclui zero e os
# outros não, o candidato natural é reportar aquele — e isso é exatamente o
# achado M1 da revisão metodológica, que a pré-especificação fecha. Nenhum
# destes é confirmatório: a §6 declara a curva do `contdid` como confirmatório
# #1 e óbito fetal como #2. Tudo aqui é EXPLORATÓRIO.
exclui <- tab[!is.na(ic_baixo) & (ic_baixo > 0 | ic_alto < 0)]
if (nrow(exclui) > 0 && nrow(exclui) < nrow(tab)) {
  cat("\n")
  cat("  ⚠️⚠️ ATENÇÃO — ", nrow(exclui), " de ", nrow(tab),
      " estimadores excluem zero, e os outros não:\n", sep = "")
  for (i in seq_len(nrow(exclui))) {
    cat(sprintf("       %s: %.2f g, IC [%.2f ; %.2f]\n",
                exclui$estimador[i], exclui$tau[i],
                exclui$ic_baixo[i], exclui$ic_alto[i]))
  }
  cat("\n")
  cat("     Os três rodam sobre A MESMA MATRIZ. Divergirem quanto a excluir\n")
  cat("     zero não é evidência a favor do que exclui — é evidência de que o\n")
  cat("     resultado depende do estimador.\n")
  cat("\n")
  cat("     ⚠️ E NENHUM destes é confirmatório. Reportar um exploratório que\n")
  cat("        cruzou a linha como se fosse achado é o M1 acontecendo.\n")
}

cat("\n", barra, "\n", sep = "")
cat("COMO LER — e o que este script NÃO diz\n")
cat(barra, "\n")
cat("  • ⚠️ NÃO é o SDID estadual. Aquele responde 'o Ceará mudou em relação a\n")
cat("    um Ceará sintético'; este responde 'os municípios de dose alta mudaram\n")
cat("    em relação aos de dose zero'. Perguntas diferentes.\n")
cat("  • A distância entre `sc` e `did` mede quanto o RE-PESO das unidades está\n")
cat("    fazendo. Se for grande, o resultado depende de quem entra no sintético.\n")
cat("  • ⚠️ Se o `d = 0` está contaminado por controle vetorial aéreo (flag 5),\n")
cat("    o sintético é montado com unidades PARCIALMENTE TRATADAS. O SDID não\n")
cat("    conserta isso — ele herda.\n")
cat("  • ⚠️ O gate do E7 continua valendo: coeficiente abaixo do MDE do desenho\n")
cat("    NÃO é achado, por mais elegante que seja o estimador.\n")
cat(barra, "\n")

dir.create(saida, recursive = TRUE, showWarnings = FALSE)
tab[, `:=`(desfecho = desfecho, n_tratados = n1, n_doadores = pm$N0,
           t_pre = pm$T0, t_pos = n_pos, escopo = "intraestadual")]
destino <- file.path(saida, sprintf("synthdid__%s.csv", desfecho))
fwrite(tab, destino)
cat("\n[ok]", destino, "\n")
