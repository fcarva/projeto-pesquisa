#!/usr/bin/env Rscript
# E6 — estimação CGS de tratamento contínuo (Callaway, Goodman-Bacon & Sant'Anna).
#
# Lê o parquet do `scripts/build_panel/05_build_panel.py`, estima, e grava CSV
# *tidy* que o Python lê de volta para tabelas e figuras. A fronteira entre as
# linguagens é arquivo, nunca in-process — CLAUDE.md, "Convenções do repositório".
#
# ⚠️ A API abaixo foi CONFERIDA contra o código de `bcallaway11/contdid` v0.1.1
# (NAMESPACE e R/cont_did.R), não suposta. Mas **este script nunca foi executado**:
# não há R nesta sessão. O que está verificado são nomes de argumento e as
# restrições que o próprio pacote impõe; o que não está é a rodada.
#
# ══════════════════════════════════════════════════════════════════════════════
# TRÊS RESTRIÇÕES DO PACOTE QUE MUDAM O DESENHO, E QUE PRECISAM ESTAR AQUI
# ══════════════════════════════════════════════════════════════════════════════
#
# 1. ⚠️ **O sieve não-paramétrico (CCK) exige EXATAMENTE DOIS PERÍODOS.**
#    De R/cont_did.R:
#        if (length(unique(data[[tname]])) != 2)
#          stop("cck estimator not supported with more than two time periods.
#                consider averaging across pre and post treatment periods")
#    O painel mensal do E5 tem ~120 períodos. Ou seja: o estimador que entrega
#    **a curva** — que é o resultado principal da D1, e o que o Ensaio 2 precisa —
#    **não roda no painel mensal**. Ele precisa do painel colapsado em pré/pós.
#    Isso não é detalhe de implementação: é uma escolha de agregação que o
#    desenho tem de declarar.
#
# 2. ⚠️ **Com o sieve não há event study.**
#        if (aggregation != "dose") stop("event study not supported with cck")
#    Então os *leads* que testam paralelismo (A4) e a antecipação de 2015–2018
#    **não saem do mesmo estimador que a curva**. São duas rodadas, com
#    agregações diferentes, e o texto tem de dizer isso.
#
# 3. ⚠️ **Covariáveis não são suportadas.**
#        if (xformula != ~1) stop("covariates not currently supported")
#    Qualquer ajuste por características municipais tem de vir por outra via
#    (por exemplo, o PSM+DiD da camada de comunicação), não por dentro do CGS.
#
# ══════════════════════════════════════════════════════════════════════════════
# O QUE O SIEVE FAZ COM O GRUPO d = 0 — e por que a flag 5 vira mecânica
# ══════════════════════════════════════════════════════════════════════════════
# De R/cont_did.R, no bloco do cck:
#        dy <- post_data$.dy            # primeira diferença do desfecho
#        m0 <- mean(dy[dose == 0])      # média entre os de dose zero
#        dy_centered <- dy - m0         # a curva inteira é centrada nisso
#
# A curva é **centrada na variação média do grupo de dose zero**. Então
# contaminação do zero não acrescenta ruído: **desloca o nível da curva inteira**.
# A flag 5 do CLAUDE.md ("o d = 0 não é zero de tratamento" — controle vetorial
# aéreo pelo §2º do art. 28-B) deixa de ser ressalva de texto e vira aritmética
# do estimador. As quatro construções de zero da §5.3 têm de ser rodadas, e a
# dispersão entre elas é a incerteza sobre o nível.
#
# ══════════════════════════════════════════════════════════════════════════════
# O GATE DO TEOREMA C.1
# ══════════════════════════════════════════════════════════════════════════════
# `cont_did` tem `target_parameter = c("level", "slope")`:
#   "level" -> ATT(d|d), que sai sob paralelismo tradicional (Assumption 4)
#   "slope" -> ACRT(d|d)/ACR(d), que exige strong parallel trends (Assumption 5)
#
# O Teorema C.1 do CGS diz que A4 + A5 juntas implicam ATT(d|d) = ATE(d). Então
# rodar os dois e comparar É o diagnóstico. **Divergência é informação, não
# defeito:** se divergirem, o resultado principal migra para os limites da §5.1,
# conforme o compromisso já registrado em 03-modelagem-ensaio1.md §4.1. A decisão
# é do diagnóstico, não da estética do coeficiente.
#
# ⚠️ Este script **não decide** por você. Ele roda os dois, grava os dois, e
# imprime a comparação.
#
# USO
#   Rscript scripts/estimate/03_contdid.R \
#     --painel data/processed/painel_ensaio1.parquet \
#     --desfecho peso_medio \
#     --saida data/processed
#
#   --exposicao   share_gestacao_pos_ban (padrão) | share_tri3_pos_ban | ...
#   --corte-pre   último mês tratado como pré  (padrão: 2018-12)
#   --corte-pos   primeiro mês tratado como pós (padrão: 2019-10)

suppressPackageStartupMessages({
  library(arrow)
  library(data.table)
  library(contdid)
})

# ── argumentos ───────────────────────────────────────────────────────────────

args <- commandArgs(trailingOnly = TRUE)
le <- function(nome, padrao) {
  i <- which(args == nome)
  if (length(i) == 0) padrao else args[i + 1]
}

caminho_painel <- le("--painel", "data/processed/painel_ensaio1.parquet")
desfecho <- le("--desfecho", "peso_medio")
exposicao <- le("--exposicao", "share_gestacao_pos_ban")
saida <- le("--saida", "data/processed")
corte_pre <- le("--corte-pre", "2018-12")
corte_pos <- le("--corte-pos", "2019-10")
biters <- as.integer(le("--biters", "1000"))

dir.create(saida, recursive = TRUE, showWarnings = FALSE)

barra <- strrep("=", 84)
cat(barra, "\n")
cat("E6 — CGS TRATAMENTO CONTÍNUO | desfecho:", desfecho, "\n")
cat(barra, "\n")

# ── painel ───────────────────────────────────────────────────────────────────

painel <- as.data.table(arrow::read_parquet(caminho_painel))
stopifnot(all(c("cod_ibge6", "ano", "mes", "dose", desfecho) %in% names(painel)))

painel[, id := as.integer(factor(cod_ibge6))]
painel[, t := ano * 12L + mes - 1L]
painel[, y := get(desfecho)]

cat("municípios:", uniqueN(painel$id),
    "| períodos:", uniqueN(painel$t),
    "| células:", nrow(painel), "\n")

if (painel[, sum(is.na(y))] > 0) {
  cat("[aviso]", painel[, sum(is.na(y))], "células com desfecho ausente.\n")
  cat("[aviso] O pacote NÃO aceita painel desbalanceado:\n")
  cat("[aviso]   if (allow_unbalanced_panel) stop('unbalanced panel not currently supported')\n")
  cat("[aviso] Células ausentes serão descartadas, e o painel rebalanceado.\n")
}

# ── colapso pré/pós, exigido pelo sieve ──────────────────────────────────────
#
# ⚠️ As coortes de transição — aquelas cuja gestação atravessa o ban, com
# `share_gestacao_pos_ban` estritamente entre 0 e 1 — não são nem pré nem pós.
# Aqui elas são **descartadas**, que é a escolha conservadora: incluí-las de
# qualquer lado embute atenuação conhecida (ver o E5 do roteiro). Os cortes são
# parâmetros justamente porque essa é decisão do pesquisador, não do script.

t_de <- function(txt) {
  partes <- as.integer(strsplit(txt, "-")[[1]])
  partes[1] * 12L + partes[2] - 1L
}
t_pre <- t_de(corte_pre)
t_pos <- t_de(corte_pos)

painel[, periodo := fifelse(t <= t_pre, 1L, fifelse(t >= t_pos, 2L, NA_integer_))]
n_transicao <- painel[is.na(periodo), .N]
cat("\ncoortes de transição descartadas:", n_transicao,
    sprintf("(%.1f%%)\n", 100 * n_transicao / nrow(painel)))
cat("  pré  <= ", corte_pre, " | pós >= ", corte_pos, "\n", sep = "")
cat("  ⚠️ São as coortes cuja gestação atravessa o ban. Descartar é a escolha\n")
cat("     conservadora; incluí-las embute atenuação. Ajuste com --corte-pre/pos.\n")

colapsado <- painel[!is.na(periodo) & !is.na(y),
                    .(y = mean(y, na.rm = TRUE), dose = first(dose)),
                    by = .(id, periodo)]
# o sieve exige painel balanceado nos dois períodos
completos <- colapsado[, .N, by = id][N == 2L, id]
colapsado <- colapsado[id %in% completos]
cat("  municípios com os dois períodos:", uniqueN(colapsado$id), "\n")

# ── 1. a curva, via sieve não-paramétrico (CCK) ──────────────────────────────

cat("\n", barra, "\n", sep = "")
cat("1. CURVA DOSE-RESPOSTA — sieve não-paramétrico (CCK), 2 períodos\n")
cat(barra, "\n")

grava_tidy <- function(obj, arquivo, extra = list()) {
  tidy <- tryCatch(as.data.table(broom::tidy(obj)), error = function(e) NULL)
  if (is.null(tidy)) {
    # `contdid` não expõe broom::tidy; extrai os campos do objeto direto
    tidy <- data.table(
      dose = tryCatch(obj$dose, error = function(e) NA_real_),
      estimativa = tryCatch(obj$att.d, error = function(e) NA_real_),
      erro_padrao = tryCatch(obj$att.d.se, error = function(e) NA_real_)
    )
  }
  for (nome in names(extra)) tidy[[nome]] <- extra[[nome]]
  caminho <- file.path(saida, arquivo)
  data.table::fwrite(tidy, caminho)
  cat("  [ok]", caminho, "\n")
  invisible(tidy)
}

resultados <- list()
for (alvo in c("level", "slope")) {
  cat("\n  target_parameter =", alvo,
      if (alvo == "level") "  -> ATT(d|d), sob Assumption 4"
      else "  -> ACR(d), exige Assumption 5 (NÃO testável)", "\n")
  res <- tryCatch(
    cont_did(
      yname = "y", dname = "dose", tname = "periodo", idname = "id",
      data = as.data.frame(colapsado),
      target_parameter = alvo,
      aggregation = "dose",
      treatment_type = "continuous",
      dose_est_method = "cck",
      biters = biters,
      cband = TRUE
    ),
    error = function(e) { cat("  [erro]", conditionMessage(e), "\n"); NULL }
  )
  resultados[[alvo]] <- res
  if (!is.null(res)) {
    grava_tidy(res, sprintf("cgs_curva_%s.csv", alvo),
               extra = list(alvo = alvo, desfecho = desfecho, exposicao = exposicao))
  }
}

# ── 2. o gate do Teorema C.1 ─────────────────────────────────────────────────

cat("\n", barra, "\n", sep = "")
cat("2. DIAGNÓSTICO DO TEOREMA C.1 — ATT(d|d) converge com ATE(d)?\n")
cat(barra, "\n")
cat("A4 + A5 juntas implicam ATT(d|d) = ATE(d). Divergência é INFORMAÇÃO:\n")
cat("quer dizer que a A5 (strong parallel trends) não se sustenta, e o\n")
cat("resultado principal migra para os limites da §5.1 — compromisso já\n")
cat("registrado em docs/ars/03-modelagem-ensaio1.md §4.1.\n\n")

if (!is.null(resultados$level) && !is.null(resultados$slope)) {
  cat("Os dois rodaram. Compare `cgs_curva_level.csv` com `cgs_curva_slope.csv`.\n")
  cat("⚠️ Este script NÃO decide se convergem — a leitura é sua, e o critério\n")
  cat("   tem de estar escrito ANTES de olhar o coeficiente.\n")
} else {
  cat("⚠️ Ao menos um dos dois não rodou. Sem os dois, não há diagnóstico —\n")
  cat("   e sem diagnóstico não se escolhe entre curva e limites.\n")
}

# ── 3. event study (parametrico, painel mensal) ──────────────────────────────
#
# ⚠️ Rodada SEPARADA de propósito: o sieve não faz event study
# (`stop("event study not supported with cck estimator yet")`). Então os leads
# que dão evidência sobre a A4 saem de outro estimador que a curva — e o texto
# tem de dizer isso, em vez de deixar parecer que é tudo a mesma rodada.
#
# Os leads precisam alcançar 2018: os três marcos de antecipação são
# 24/02/2015 (notícia), 18/12/2018 (certeza) e 09/01/2019 (obrigação).

cat("\n", barra, "\n", sep = "")
cat("3. EVENT STUDY — paramétrico, painel mensal (rodada SEPARADA da curva)\n")
cat(barra, "\n")

mensal <- painel[!is.na(y), .(id, t, y, dose)]
completos_m <- mensal[, .N, by = id][N == max(N), id]
mensal <- mensal[id %in% completos_m]
cat("  painel balanceado:", uniqueN(mensal$id), "municípios ×",
    uniqueN(mensal$t), "meses\n")

es <- tryCatch(
  cont_did(
    yname = "y", dname = "dose", tname = "t", idname = "id",
    data = as.data.frame(mensal),
    target_parameter = "level",
    aggregation = "eventstudy",
    treatment_type = "continuous",
    dose_est_method = "parametric",
    biters = biters,
    cband = TRUE
  ),
  error = function(e) { cat("  [erro]", conditionMessage(e), "\n"); NULL }
)
if (!is.null(es)) {
  grava_tidy(es, "cgs_eventstudy.csv",
             extra = list(desfecho = desfecho, exposicao = exposicao))
}

cat("\n", barra, "\n", sep = "")
cat("O QUE LEVAR PARA O TEXTO\n")
cat(barra, "\n")
cat("• A curva e o event study vêm de estimadores DIFERENTES (sieve vs.\n")
cat("  paramétrico) e de agregações diferentes. Não é uma rodada só.\n")
cat("• ⚠️ O sieve centra a curva na variação média do grupo dose = 0\n")
cat("  (`m0 <- mean(dy[dose == 0])`). Contaminação do zero DESLOCA o nível da\n")
cat("  curva inteira — não é ruído. Rode as quatro construções de zero da\n")
cat("  §5.3 e reporte a dispersão entre elas.\n")
cat("• ⚠️ Covariáveis não entram no CGS. Ajuste municipal só por outra via.\n")
cat("• O próximo passo é a robustez: Conley–Taber e wild-cluster bootstrap,\n")
cat("  porque poucos clusters tratados + desfecho raro não perdoam inferência\n")
cat("  assintótica. Ver scripts/estimate/04_robustness.py.\n")
cat(barra, "\n")
