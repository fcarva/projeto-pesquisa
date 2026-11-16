# Estimação e inferência do desenho principal, sobre painel no formato de
# 01_gerador_painel.R.
#
# ✎ EDITÁVEL pelo laço autônomo: é aqui que se melhora a inferência com poucos
# municípios tratados. Contrato que não muda: `estimar(d)` devolve uma lista
# com `beta` (estimativa de A x H x Pos) e `p` (vetor nomeado de p-valores
# bilaterais, um por procedimento de inferência).
#
# Estado atual (ponto de partida, não chegada):
#   p["cluster"]   : erro-padrão agrupado por município, t com G-1 graus
#   p["permuta"]   : permutação do rótulo de tratado entre municípios, sobre
#                    as estimativas por município (dois passos, à la
#                    Conley-Taber)
# ⚠️ FALTA o procedimento que o projeto declara principal: Ferman e Pinto
# (2019), que corrige a permutação pela heterocedasticidade de porte. Sem ele,
# a permutação pode ter tamanho errado quando tratados e comparação diferem em
# número de nascimentos. É a primeira tarefa do laço.

suppressPackageStartupMessages(library(fixest))
setFixest_notes(FALSE)

estimar <- function(d, n_perm = 499L) {
  # --- especificação do projeto, agrupada ---
  d$HC <- d$H * d$C; d$IC <- d$I * d$C
  d$AHSeca <- d$A * d$H * d$Seca; d$AISeca <- d$A * d$I * d$Seca
  d$AHPos <- d$A * d$H * d$Pos; d$AIPos <- d$A * d$I * d$Pos
  f <- Y ~ HC + IC + AHSeca + AISeca + AHPos + AIPos | m^mes + m^ano + t
  aj <- feols(f, data = d, weights = ~n, cluster = ~m)
  b <- coef(aj)[["AHPos"]]
  ep <- se(aj)[["AHPos"]]
  G <- length(unique(d$m))
  p_cluster <- 2 * pt(-abs(b / ep), df = G - 1)

  # --- dois passos: um coeficiente H x Pos por município ---
  # Um município de referência é absorvido pelo efeito fixo de coorte; a
  # diferença de médias entre grupos não depende de qual.
  f2 <- Y ~ HC + IC + i(m, H_Pos) + i(m, I_Pos) + i(m, H_Seca) + i(m, I_Seca) |
    m^mes + m^ano + t
  d$H_Pos <- d$H * d$Pos; d$I_Pos <- d$I * d$Pos
  d$H_Seca <- d$H * d$Seca; d$I_Seca <- d$I * d$Seca
  aj2 <- feols(f2, data = d, weights = ~n, warn = FALSE)
  cf <- coef(aj2)
  nm <- grep("^m::[0-9]+:H_Pos$", names(cf), value = TRUE)
  bm <- setNames(rep(0, G), sort(unique(d$m)))       # referência = 0
  bm[sub("^m::([0-9]+):H_Pos$", "\\1", nm)] <- cf[nm]
  A <- tapply(d$A, d$m, max)[names(bm)]
  est <- function(a) mean(bm[a == 1]) - mean(bm[a == 0])
  obs <- est(A)
  perm <- replicate(n_perm, est(sample(A)))
  p_perm <- (1 + sum(abs(perm) >= abs(obs))) / (n_perm + 1)

  list(beta = b, beta_2p = obs, p = c(cluster = p_cluster, permuta = p_perm))
}
