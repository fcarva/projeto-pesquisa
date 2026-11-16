# Bateria fixa de provas do desenho principal, sobre dado SIMULADO.
#
# ⚠️ TRAVADO para o laço autônomo: este arquivo é a métrica. Um laço que
# pudesse editar a régua "melhoraria" mudando a régua.
#
# Uso (da raiz):  Rscript scripts/simulacao/03_bateria.R [REPS] [SEMENTE]
# Saída: output/simulacao/bateria.csv (tidy) e resumo no terminal.
#
# O que mede:
#   1. recuperação : viés de beta com efeito plantado, sem falhas
#   2. tamanho     : taxa de rejeição a 5% com efeito zero (alvo: 0,05)
#   3. poder       : taxa de rejeição por tamanho de efeito e nº de tratados
#   4. falhas      : viés e rejeição sob chuva diferencial, antecipação,
#                    seleção e ruído no hiato, uma de cada vez
# Métrica do laço (última linha): erro de tamanho e efeito mínimo detectável.

args <- commandArgs(trailingOnly = TRUE)
REPS <- if (length(args) >= 1) as.integer(args[1]) else 200L
SEM <- if (length(args) >= 2) as.integer(args[2]) else 20261116L
raiz <- "scripts/simulacao"
source(file.path(raiz, "01_gerador_painel.R"))
source(file.path(raiz, "02_estimadores.R"))

cenario <- function(nome, bloco, ...) {
  p <- parametros_padrao(); mud <- list(...)
  p[names(mud)] <- mud
  list(nome = nome, bloco = bloco, par = p)
}
cen <- list(
  cenario("efeito 20 g, 7 tratados", "recuperacao", beta_H = 20),
  cenario("nulo, 7 tratados", "tamanho"),
  cenario("nulo, 2 tratados", "tamanho", n_trat = 2L),
  cenario("nulo, 7 tratados, portes iguais", "tamanho", nasc_trat = 30),
  cenario("nulo, 7 tratados, tratados 10x maiores", "tamanho", nasc_trat = 300)
)
for (nt in c(2L, 7L)) for (b in c(10, 20, 40))
  cen[[length(cen) + 1]] <- cenario(sprintf("efeito %d g, %d tratados", b, nt),
                                    "poder", beta_H = b, n_trat = nt)
cen <- c(cen, list(
  cenario("chuva diferencial + pós mais chuvoso", "falha",
          theta_dif = 10, chuva_pos = 1),
  cenario("antecipação: efeito inteiro já em 2011", "falha",
          beta_H = 20, antecipa = 1),
  cenario("seleção: -10 g por nascimentos marginais", "falha",
          beta_H = 20, selecao = 10),
  cenario("ruído no hiato por município-ano (dp 15 g)", "falha", dp_hiato = 15)
))

linhas <- list()
for (i in seq_along(cen)) {
  cc <- cen[[i]]
  r <- lapply(seq_len(REPS), function(k) {
    set.seed(SEM + 1000L * i + k)
    e <- estimar(gerar_painel(cc$par, semente = SEM + 1000L * i + k))
    c(beta = e$beta, e$p)
  })
  r <- do.call(rbind, r)
  proc <- setdiff(colnames(r), "beta")
  for (pr in proc) linhas[[length(linhas) + 1]] <- data.frame(
    bloco = cc$bloco, cenario = cc$nome, n_trat = cc$par$n_trat,
    beta_plantado = cc$par$beta_H, inferencia = pr, reps = REPS,
    beta_medio = mean(r[, "beta"]), dp_beta = sd(r[, "beta"]),
    vies = mean(r[, "beta"]) - cc$par$beta_H,
    rejeicao_5 = mean(r[, pr] < 0.05))
  cat(sprintf("[%2d/%d] %s\n", i, length(cen), cc$nome))
}
res <- do.call(rbind, linhas)
dir.create("output/simulacao", recursive = TRUE, showWarnings = FALSE)
write.csv(res, "output/simulacao/bateria.csv", row.names = FALSE)

fmt <- res
fmt[c("beta_medio", "dp_beta", "vies")] <- round(fmt[c("beta_medio", "dp_beta", "vies")], 1)
fmt$rejeicao_5 <- round(fmt$rejeicao_5, 3)
print(fmt[, c("bloco", "cenario", "inferencia", "beta_plantado", "beta_medio",
              "dp_beta", "rejeicao_5")], row.names = FALSE)

# --- métrica do laço ---
ep_mc <- sqrt(0.05 * 0.95 / REPS)
cat(sprintf("\nErro-padrão de Monte Carlo da taxa de rejeição a 5%%: %.3f (REPS = %d)\n",
            ep_mc, REPS))
for (pr in unique(res$inferencia)) {
  tm <- res[res$bloco == "tamanho" & res$inferencia == pr, ]
  erro <- max(abs(tm$rejeicao_5 - 0.05))
  # EMD a 80% com 7 tratados: 2,8 x dp de beta no cenário nulo (aproximação
  # normal; só vale se o tamanho do teste estiver certo)
  dp0 <- res$dp_beta[res$cenario == "nulo, 7 tratados" & res$inferencia == pr]
  cat(sprintf("METRICA inferencia=%s erro_tamanho_max=%.3f emd80_7trat=%.1f\n",
              pr, erro, 2.8 * dp0))
}
cat("⚠️ Dado simulado, parâmetros hipotéticos: estes números não são estimativa e não entram no projeto.\n")
