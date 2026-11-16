# Gerador do painel SIMULADO do desenho principal (diferença tripla de
# calendário). Nenhum dado real entra aqui.
#
# ⚠️ TRAVADO para o laço autônomo: este arquivo define o "mundo" contra o qual
# os estimadores são medidos. Mudar o gerador muda a pergunta. Só o
# pesquisador altera (docs/ars/rodada21-local/laco-autonomo.md).
#
# ⚠️ Todo parâmetro abaixo é HIPÓTESE, não calibração: desvio-padrão do peso,
# nascimentos por município, variâncias dos choques, meses da estação. A
# calibração com o pré-período é decisão do pesquisador e fica para depois.
#
# Desenho (paper/projeto/secoes/05-metodologia.tex, eq. principal):
#   unidade: município m × mês de nascimento t
#   A_m    : município com aplicação aérea documentada
#   P_t    : fração dos dois primeiros trimestres (meses t-9..t-4) na estação
#   H_t    : P_t >= 1/2 ; I_t : 0 < P_t < 1/2 ; referência: P_t = 0
#   Ref    : nascidos 2007-2011 ; Seca: 2013-2018 ; Pos: 2020 em diante
#   2012 e 2019 excluídos; 2005-2006 só entram no estudo de evento.

parametros_padrao <- function() {
  list(
    n_trat = 7L,            # municípios com avião (Censo 2006 tem 7; hipótese)
    n_comp = 40L,           # municípios de comparação (banana familiar)
    ano_ini = 2007L, ano_fim = 2024L,
    estacao = 2:5,          # meses da estação de pulverização (HIPÓTESE)
    nasc_trat = 60,         # nascimentos médios por mês, tratados
    nasc_comp = 30,         # idem, comparação
    cv_nasc = 0.6,          # dispersão do porte entre municípios
    dp_peso = 500,          # desvio-padrão individual do peso ao nascer (g)
    dp_mun_mes = 30,        # alpha_{m,s}: sazonalidade de base por município
    dp_mun_ano = 15,        # mu_{m,a}: choque município-ano
    dp_coorte = 10,         # gamma_t
    dp_hiato = 0,           # choque no hiato sazonal por município-ano (ruído
                            #   que os efeitos fixos NÃO absorvem)
    beta_H = 0,             # efeito plantado: A x H x Pos (g, média municipal)
    razao_I = 0.5,          # efeito nas coortes intermediárias = razao * beta_H
    beta_S = 0,             # A x H x Seca (voos suspensos na seca)
    theta = 5,              # efeito direto da chuva sobre o hiato (g por dp)
    # --- falhas plantadas (0 = desligada) ---
    theta_dif = 0,          # efeito da chuva sobre o hiato difere nos tratados
    chuva_pos = 0,          # deslocamento médio da chuva no pós-lei (dp)
    antecipa = 0,           # fração do efeito já presente em 2011
    selecao = 0             # queda do peso médio por entrada de nascimentos
                            #   marginais, tratados x H x Pos (g)
  )
}

exposicao <- function(mes_nasc, estacao) {
  # janela fixa: meses t-9 .. t-4 (dois primeiros trimestres)
  sapply(mes_nasc, function(b) {
    jan <- ((b - 9:4 - 1) %% 12) + 1
    mean(jan %in% estacao)
  })
}

gerar_painel <- function(par = parametros_padrao(), semente = 1L) {
  set.seed(semente)
  M <- par$n_trat + par$n_comp
  mun <- data.frame(
    m = seq_len(M),
    A = as.integer(seq_len(M) <= par$n_trat)
  )
  base <- ifelse(mun$A == 1, par$nasc_trat, par$nasc_comp)
  sdlog <- sqrt(log(1 + par$cv_nasc^2))
  mun$porte <- base * rlnorm(M, meanlog = -sdlog^2 / 2, sdlog = sdlog)

  anos <- par$ano_ini:par$ano_fim
  d <- expand.grid(m = mun$m, ano = anos, mes = 1:12)
  d <- merge(d, mun, by = "m")
  d$t <- (d$ano - par$ano_ini) * 12L + d$mes
  d$P <- exposicao(d$mes, par$estacao)
  d$H <- as.integer(d$P >= 0.5)
  d$I <- as.integer(d$P > 0 & d$P < 0.5)
  d$Ref <- as.integer(d$ano >= 2007 & d$ano <= 2011)
  d$Seca <- as.integer(d$ano >= 2013 & d$ano <= 2018)
  d$Pos <- as.integer(d$ano >= 2020)
  d$n <- pmax(rpois(nrow(d), d$porte), 1L)

  # efeitos fixos verdadeiros
  a_ms <- matrix(rnorm(M * 12, 0, par$dp_mun_mes), M, 12)
  mu_ma <- matrix(rnorm(M * length(anos), 0, par$dp_mun_ano), M, length(anos))
  g_t <- rnorm(max(d$t), 0, par$dp_coorte)
  ia <- d$ano - par$ano_ini + 1L

  # chuva da quadra por município-ano: componente comum + idiossincrático
  ch_ano <- rnorm(length(anos)) + par$chuva_pos * (anos >= 2020)
  ch <- matrix(0.7 * rep(ch_ano, each = M) + 0.7 * rnorm(M * length(anos)),
               M, length(anos))
  d$C <- ch[cbind(d$m, ia)]

  # choque no hiato por município-ano (não absorvido)
  hi <- matrix(rnorm(M * length(anos), 0, par$dp_hiato), M, length(anos))

  k <- d$H + par$razao_I * d$I            # intensidade da coorte
  efeito <- par$beta_H * d$A * k * d$Pos +
            par$beta_S * d$A * k * d$Seca +
            par$antecipa * par$beta_H * d$A * k * (d$ano == 2011)
  chuva <- (par$theta + par$theta_dif * d$A) * k * d$C
  selec <- -par$selecao * d$A * d$H * d$Pos

  d$Y <- 3200 + a_ms[cbind(d$m, d$mes)] + mu_ma[cbind(d$m, ia)] + g_t[d$t] +
    efeito + chuva + selec + hi[cbind(d$m, ia)] * d$H +
    rnorm(nrow(d), 0, par$dp_peso / sqrt(d$n))

  d <- d[d$Ref == 1 | d$Seca == 1 | d$Pos == 1, ]
  d[order(d$m, d$t), c("m", "A", "ano", "mes", "t", "n", "P", "H", "I",
                       "Ref", "Seca", "Pos", "C", "Y")]
}

# Rodado como script: grava um painel de exemplo (gitignorado).
if (sys.nframe() == 0L) {
  dir.create("data/processed/simulado", recursive = TRUE, showWarnings = FALSE)
  p <- parametros_padrao(); p$beta_H <- 20
  d <- gerar_painel(p, semente = 20261116L)
  arq <- "data/processed/simulado/painel_calendario_exemplo.csv"
  write.csv(d, arq, row.names = FALSE)
  cat(sprintf("painel simulado: %d linhas, %d municípios (%d tratados) -> %s\n",
              nrow(d), length(unique(d$m)), sum(tapply(d$A, d$m, max)), arq))
  print(table(H = d$H[d$m == 1 & d$ano == 2007], I = d$I[d$m == 1 & d$ano == 2007]))
}
