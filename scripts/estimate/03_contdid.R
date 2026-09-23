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
#    Então os *leads* que testam paralelismo (PT) e a antecipação de 2015–2018
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
# LEVEL E SLOPE NÃO SÃO ATT E ATE — corrigido em 2026-09-23
# ══════════════════════════════════════════════════════════════════════════════
# `cont_did` tem `target_parameter = c("level", "slope")`:
#   "level" -> a curva de nível, E[ΔY|D=d] − E[ΔY|D=0]
#   "slope" -> a DERIVADA dessa curva em d
#
# ⚠️ Até 2026-09-23 este cabeçalho dizia que rodar os dois e comparar era o
# diagnóstico do Teorema C.1 (ATT(d|d) = ATE(d)). É falso, e a auditoria de
# 2026-09-23 mostrou por quê, lendo o próprio teorema (CGS, v4, Apêndice C):
# sob PT a expressão E[ΔY|D=d] − E[ΔY|D=0] identifica ATT(d|d); sob SPT, a
# MESMA expressão identifica ATE(d). Não existem duas curvas estimadas de forma
# independente para comparar: é um objeto, lido sob duas hipóteses. E "level"
# contra "slope" compara uma função com a derivada dela, em unidades
# diferentes. A divergência entre os dois arquivos não diz nada sobre o SPT.
#
# O que existe de testável é a implicação pré-tratamento, comum a PT e SPT:
# está no 10_spt_pretrend.py, e pode falsificar, não validar.
#
# USO
#   Rscript scripts/estimate/03_contdid.R \
#     --painel data/processed/painel_ensaio1.parquet \
#     --desfecho peso_medio \
#     --saida data/processed
#
#   --corte-pre   último mês tratado como pré  (padrão: 2018-12)
#   --corte-pos   primeiro mês tratado como pós (padrão: 2019-10)
#
# ⚠️ `--exposicao` FOI REMOVIDO em 2026-09-23. Era lido e gravado como metadado,
# mas o colapso usa só os cortes de calendário: trocar de
# `share_gestacao_pos_ban` para `share_tri3_pos_ban` mudava o rótulo do CSV e
# não a regressão (auditoria de 2026-09-23). O contraste é o dos cortes, e é
# isso que a coluna `contraste` das saídas diz. Passar a opção agora é erro.

suppressPackageStartupMessages({
  library(arrow)
  library(data.table)
  library(contdid)
})

# ── argumentos ───────────────────────────────────────────────────────────────

args <- commandArgs(trailingOnly = TRUE)

CONHECIDOS <- c("--painel", "--desfecho", "--saida",
                "--corte-pre", "--corte-pos", "--biters", "--control-group",
                "--d-zero", "--aptidao-p", "--seed")

uso <- function() {
  cat("E6 — CGS tratamento contínuo (Callaway, Goodman-Bacon & Sant'Anna)

")
  cat("  Rscript scripts/estimate/03_contdid.R [opções]

")
  cat("  --painel         parquet do painel   [data/processed/painel_ensaio1.parquet]
")
  cat("  --desfecho       coluna do desfecho  [peso_medio]
")
  cat("  --saida          pasta de saída      [data/processed]
")
  cat("  --corte-pre      último mês pré      [2018-12]
")
  cat("  --corte-pos      primeiro mês pós    [2019-10]
")
  cat("  --biters         réplicas bootstrap  [1000]
")
  cat("  --control-group  grupo de comparação [nevertreated]
")
  cat("  --d-zero         construção do d = 0: 1 (área nula) | 4 (aptidão GAEZ) [1]
")
  cat("  --aptidao-p      percentil de aptidão acima do qual o zero é SUSPEITO [0.75]
")
  cat("  --seed           semente do bootstrap [20190613]
")
  cat("  --help           esta mensagem

")
  cat("⚠️ Este script ESTIMA. Ele não é diagnóstico.
")
}

# ⚠️ Rejeitar flag desconhecida, e o motivo não é preciosismo. Antes disto,
# `le()` ignorava em silêncio o que não reconhecia: rodar com `--help` NÃO
# imprimia ajuda — ia direto estimar contra o painel real. Aconteceu em
# 2026-09-21. O portão do `make real` não protege contra isso, porque o script
# roda sozinho. Um estimador que estima ao receber flag errada é armadilha.
if ("--help" %in% args || "-h" %in% args) { uso(); quit(status = 0) }
if ("--exposicao" %in% args) {
  cat("[erro] --exposicao foi removido em 2026-09-23: o colapso usa só os cortes de\n")
  cat("       calendário, e a opção mudava o rótulo, não a regressão. Use\n")
  cat("       --corte-pre/--corte-pos para mudar o contraste.\n")
  quit(status = 2)
}
desconhecidas <- setdiff(grep("^--", args, value = TRUE), CONHECIDOS)
if (length(desconhecidas) > 0) {
  cat("[erro] opção desconhecida:", paste(desconhecidas, collapse = ", "), "

")
  uso()
  quit(status = 2)
}

le <- function(nome, padrao) {
  i <- which(args == nome)
  if (length(i) == 0) padrao else args[i + 1]
}

caminho_painel <- le("--painel", "data/processed/painel_ensaio1.parquet")
desfecho <- le("--desfecho", "peso_medio")
# O contraste, por extenso: é o que as saídas gravam no lugar de `exposicao`.
contraste <- NULL
saida <- le("--saida", "data/processed")
corte_pre <- le("--corte-pre", "2018-12")
corte_pos <- le("--corte-pos", "2019-10")
biters <- as.integer(le("--biters", "1000"))

# ⚠️ ESCOLHA DE IDENTIFICAÇÃO, não detalhe técnico. Decidida pelo pesquisador
# em 2026-09-21 e registrada aqui porque o CLAUDE.md manda perguntar antes de
# mexer em identificação.
#
# Duas coisas se somam aqui:
#
# 1. O default do `contdid` v0.1.1 é
#    `c("notyettreated","nevertreated","eventuallytreated")` — vetor de 3 —,
#    mas a asserção interna do pacote exige escalar atômico. **O default viola
#    a própria asserção**, então `cont_did` não roda sem este argumento
#    explícito. Conferido em `formals(contdid::cont_did)`.
# 2. O ban do Ceará é **simultâneo**: não existe "not yet treated" em sentido
#    de timing. A comparação é por dose, e o grupo de comparação é o `d = 0`.
#
# ⚠️ E é aqui que a flag 5 do CLAUDE.md morde: `"nevertreated"` são os `d = 0`,
# que a flag 5 diz NÃO serem zero de tratamento — o §2º do art. 28-B alcança
# controle vetorial aéreo, e área nula na PAM é zero de *proxy*. A escolha
# deste argumento e a construção do zero são a MESMA decisão. Qual das quatro
# construções de `d = 0` está em uso tem de estar declarado na §4 da
# pré-especificação junto com esta linha.
control_group <- le("--control-group", "nevertreated")

# ⚠️ CONSTRUÇÃO DO d = 0 — §5.3 de 03-modelagem-ensaio1.md, e a
# pré-especificação de 2026-09-21 ratificou a **definição 4**.
#
#   1 = área nula da cultura-âncora (PAM). É a linha de base.
#   4 = baixa aptidão GAEZ para a âncora. Não depende de registro
#       administrativo estar completo.
#
# A implementação da 4 é: dentro do grupo de área nula, DESCARTAR quem tem
# aptidão alta. O raciocínio é que um município que PODERIA plantar banana e
# não planta é zero suspeito — pode ter trocado de cultura, ou pulverizar
# outra coisa. Zero crível é área nula COM aptidão baixa.
#
# ⚠️ E isto quase não morde: no Ceará, dos 15 municípios de área nula, apenas
# UM tem aptidão acima do p75 estadual. Medido antes de implementar, não
# descoberto depois. O zero deste desenho já era quase todo de baixa aptidão —
# o que é boa notícia para a credibilidade do grupo de comparação, e torna a
# escolha entre 1 e 4 menos consequente do que a pré-especificação supunha.
#
# ⚠️ O corte é PARÂMETRO, não constante: p75 deixa 14 de 15 controles, p25
# deixa 5. Cortes apertados destroem o grupo de comparação, e um desenho sem
# controle não estima nada.
# ⚠️ SEMENTE FIXA, e o motivo apareceu rodando duas vezes. O `contdid` faz
# bootstrap multiplicador e SEM semente o valor crítico da banda muda entre
# rodadas: a mesma especificação deu 2 leads fora do zero numa execução e 0 na
# seguinte. Rejeições marginais que aparecem e somem não são resultado — e uma
# delas indo para a dissertação seria irreprodutível por quem a checasse.
# O CLAUDE.md já manda "fixar seeds"; o script R não fazia.
seed <- as.integer(le("--seed", "20190613"))
set.seed(seed)

d_zero <- le("--d-zero", "1")
aptidao_p <- as.numeric(le("--aptidao-p", "0.75"))

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

if (d_zero == "4") {
  if (!"aptidao_gaez" %in% names(painel)) {
    stop("--d-zero 4 exige a coluna `aptidao_gaez` no painel. Rode antes: make gaez")
  }
  por_muni <- unique(painel[, .(cod_ibge6, dose, aptidao_gaez)])
  # ⚠️ Zero sem aptidão é ERRO (auditoria de 2026-09-23). `NA > corte` não é
  # verdadeiro, e o município ficava como controle aqui, enquanto o 07/08, com
  # `aptidao_gaez <= corte`, o descartava: "definição 4" com duas amostras.
  sem_aptidao <- por_muni[dose == 0 & is.na(aptidao_gaez), cod_ibge6]
  if (length(sem_aptidao) > 0) {
    stop("município(s) de dose zero sem aptidão GAEZ: ",
         paste(sem_aptidao, collapse = ", "), ". A definição 4 não decide o lado deles.")
  }
  corte <- as.numeric(quantile(por_muni$aptidao_gaez, aptidao_p, na.rm = TRUE))
  suspeitos <- por_muni[dose == 0 & aptidao_gaez > corte, cod_ibge6]
  n_zero <- nrow(por_muni[dose == 0])
  cat("\nd = 0 pela DEFINIÇÃO 4 (aptidão GAEZ, §5.3) — ratificada na pré-especificação\n")
  cat("  corte de aptidão (p", format(aptidao_p * 100), "):", format(round(corte, 3)), "\n")
  cat("  zeros por área    :", n_zero, "\n")
  cat("  zeros SUSPEITOS descartados (área nula + aptidão alta):", length(suspeitos), "\n")
  cat("  controles restantes:", n_zero - length(suspeitos), "\n")
  if (n_zero - length(suspeitos) < 5) {
    cat("  ⚠️ MENOS DE 5 CONTROLES. O sieve centra a curva em mean(dy[dose==0]);\n")
    cat("     com grupo assim pequeno o nível fica sem precisão utilizável.\n")
  }
  painel <- painel[!cod_ibge6 %in% suspeitos]
} else {
  cat("\nd = 0 pela DEFINIÇÃO 1 (área nula da cultura-âncora).\n")
  cat("  ⚠️ A pré-especificação de 2026-09-21 ratificou a definição 4.\n")
  cat("     Rodar com 1 é SENSIBILIDADE — registre na §8 se virar primária.\n")
}

# ⚠️ Proveniência atravessa a fronteira R. Um painel simulado já foi lido como
# real uma vez neste projeto; o nome do arquivo sozinho não basta, e o CSV de
# saída tem de se identificar por dentro.
fonte_painel <- if ("fonte" %in% names(painel)) as.character(painel$fonte[1]) else "desconhecida"
cat("fonte do painel:", fonte_painel, "\n")
if (fonte_painel != "real") {
  cat("\n")
  cat("!! ============================================================ !!\n")
  cat("!! PAINEL NAO E REAL (fonte =", fonte_painel, ")\n")
  cat("!! Nada abaixo e evidencia sobre o Ceara. Os CSV de saida levam\n")
  cat("!! a coluna `fonte` para que isso nao se perca do arquivo.\n")
  cat("!! ============================================================ !!\n\n")
}

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
contraste <- sprintf("corte de calendário: pré <= %s, pós >= %s", corte_pre, corte_pos)

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

# ⚠️ `gname` É OBRIGATÓRIO, e a omissão dele era o SEGUNDO bug deste script.
# Sem ele o `cont_did` morre em "'by' deve unicamente especificar coluna
# válida" — erro de `data.table` vindo de dentro do pacote, que não diz
# qual argumento falta. Conferido rodando em 2026-09-21: com `gname`, os
# dois alvos rodam; sem, nenhum.
#
# `g` é o período em que a unidade passa a ser tratada, e 0 para nunca
# tratada. O ban é simultâneo: quem tem dose > 0 é tratado no período 2,
# e o grupo `d = 0` nunca é tratado — que é o mesmo grupo que
# `control_group = "nevertreated"` seleciona. As duas escolhas têm de
# concordar, senão o pacote compara com um conjunto e o texto descreve outro.
colapsado[, g := fifelse(dose > 0, 2L, 0L)]
cat("  g: tratados", uniqueN(colapsado[g == 2L]$id),
    "| nunca-tratados", uniqueN(colapsado[g == 0L]$id), "
")
cat("  municípios com os dois períodos:", uniqueN(colapsado$id), "\n")

# ── 1. a curva, via sieve não-paramétrico (CCK) ──────────────────────────────

cat("\n", barra, "\n", sep = "")
cat("1. CURVA DOSE-RESPOSTA — sieve não-paramétrico (CCK), 2 períodos\n")
cat(barra, "\n")

# ⚠️ TERCEIRO bug deste script, e o pior tipo: ele produzia saída PLAUSÍVEL e
# silenciosamente errada. Três defeitos somados, conferidos rodando em
# 2026-09-21 contra `names()` do objeto:
#
#   1. `broom::tidy` NÃO tem método para a classe `dose_obj` — erra sempre, e o
#      `tryCatch` mandava tudo para o fallback. O fallback era o caminho real,
#      não a exceção.
#   2. O fallback extraía `obj$att.d` para OS DOIS alvos. Resultado: os arquivos
#      `cgs_curva_level.csv` e `cgs_curva_slope.csv` saíam BYTE A BYTE IDÊNTICOS,
#      rotulados como parâmetros diferentes. ATT(d|d) e ACR(d) não são a mesma
#      coisa — o segundo é a derivada do primeiro.
#   3. Pedia `obj$att.d.se` (ponto); o campo é `att.d_se` (sublinhado). O erro
#      padrão sumia, e sem ele **não há critério de falsificação** — a §5 da
#      pré-especificação compara a meia-largura do IC contra o piso de 15 g.
#
# Os campos, conferidos: `att.d`/`att.d_se`/`att.d_crit.val` para o level,
# `acrt.d`/`acrt.d_se`/`acrt.d_crit.val` para o slope, mais os agregados
# `overall_att`/`overall_acrt` e seus erros.
# ⚠️ AS BANDAS DA CURVA DE NÍVEL NÃO LEVAM A INCERTEZA DO GRUPO ZERO — conferido
# em 2026-09-23 no código fixado (contdid 5cfec81, R/cont_did.R, l. 195–221),
# depois de a auditoria de 2026-09-23 apontar o risco por inspeção. O pacote faz
# `m0 <- mean(dy[dose == 0])`, centra `dy` nele, roda o `npiv` SÓ nos tratados e
# toma `att.d_se <- cck_res$asy.se`: m0 entra como constante conhecida. Com 14
# controles, a média deles tem EP da ordem de 15 g — é ela que faz 95% da
# variância do agregado. A banda por dose sai estreita demais, e "133 dos 169
# pontos excluem o zero" era artefato disso. O agregado (`overall_att`) não
# sofre: sai de outra rotina, que inclui os controles.
#
# Correção aproximada: m0 vem dos controles e o npiv dos tratados, amostras
# independentes, então Var(att.d) = asy.se² + EP(m0)². As colunas `ep_m0`,
# `ic_inf_m0` e `ic_sup_m0` usam isso com o mesmo valor crítico. Para a
# DERIVADA nada muda: deslocar a curva por uma constante não mexe na inclinação.
ep_do_m0 <- function(colapsado) {
  dy <- colapsado[, .(dy = y[periodo == 2L][1] - y[periodo == 1L][1], dose = dose[1]), by = id]
  z <- dy[dose == 0 & is.finite(dy), dy]
  if (length(z) < 2) return(NA_real_)
  sd(z) / sqrt(length(z))
}

grava_tidy <- function(obj, arquivo, alvo = "level", extra = list(), ep_m0 = NA_real_) {
  # ⚠️ DUAS CLASSES DE OBJETO, e confundi-las era o que quebrava o event study.
  # A curva (`aggregation = "dose"`) devolve `dose_obj`, com campos `att.d`.
  # O event study (`aggregation = "eventstudy"`) devolve `pte_results`, cuja
  # substância está em `obj$event_study` — um `aggte_obj` com `egt` (tempo de
  # evento), `att.egt`, `se.egt` e `crit.val.egt`. Procurar `att.d` nele dava
  # zero linhas, e o erro aparecia só depois, em `[[<-.data.frame`, apontando
  # para o lugar errado.
  if (inherits(obj, "pte_results") || !is.null(obj$event_study)) {
    ev <- obj$event_study
    if (is.null(ev$att.egt)) stop("pte_results sem `event_study$att.egt`.")
    crit <- if (is.null(ev$crit.val.egt)) NA_real_ else as.numeric(ev$crit.val.egt)[1]
    tidy <- data.table(
      tempo_evento = as.numeric(ev$egt),
      estimativa = as.numeric(ev$att.egt),
      erro_padrao = as.numeric(ev$se.egt),
      valor_critico = crit
    )
    tidy[, ic_inf := estimativa - valor_critico * erro_padrao]
    tidy[, ic_sup := estimativa + valor_critico * erro_padrao]
    tidy[, meia_largura := valor_critico * erro_padrao]
    tidy[, pre := tempo_evento < 0]
    for (nome in names(extra)) tidy[[nome]] <- extra[[nome]]
    caminho <- file.path(saida, arquivo)
    data.table::fwrite(tidy, caminho)
    cat("  [ok]", caminho, "
")
    # O teste de paralelismo é sobre os LEADS. Reportar aqui, não deixar para
    # quem abrir o CSV — é o número que decide se a PT se sustenta.
    # ⚠️ LIMITAÇÃO DO PACOTE, conferida rodando em 2026-09-21 e não suposta.
    # Com coorte ÚNICA — que é o caso de um ban simultâneo — o `cont_did` em
    # `aggregation = "eventstudy"` devolve `att_gt` com valor APENAS para
    # t < g. Todos os 48 períodos pós saem NA. Conferido em `es$att_gt`:
    # 47 não-NA, todos em t de 24181 a 24227; NA de 24228 a 24275.
    #
    # Consequência para o texto: **isto não é um event study, é um teste de
    # pré-tendências.** A trajetória dinâmica pós-ban não sai daqui, e prometê-la
    # seria prometer o que o estimador não entrega. O repositório já registrava
    # que "os leads saem de outro estimador que a curva"; agora sabe-se que os
    # LAGS não saem de nenhum dos dois.
    n_pos_na <- nrow(tidy[pre == FALSE & !is.finite(estimativa)])
    n_pos <- nrow(tidy[pre == FALSE])
    if (n_pos > 0 && n_pos_na == n_pos) {
      cat("  ⚠️ TODOS os", n_pos, "períodos PÓS saíram NA — limitação do pacote com
")
      cat("     coorte única. O que está no CSV é teste de PRÉ-TENDÊNCIAS, não
")
      cat("     event study. A trajetória dinâmica pós-ban não sai daqui.
")
    }

    pre <- tidy[pre == TRUE & is.finite(estimativa) & is.finite(erro_padrao)]
    if (nrow(pre) > 0) {
      fora <- pre[ic_inf > 0 | ic_sup < 0]
      cat(sprintf("       leads (t < 0): %d | fora do zero pela banda: %d (%.0f%%)
",
                  nrow(pre), nrow(fora), 100 * nrow(fora) / nrow(pre)))
      cat(sprintf("       |média dos leads|: %.2f | maior |lead|: %.2f
",
                  abs(mean(pre$estimativa)), max(abs(pre$estimativa))))
      # ⚠️ O NÚMERO QUE DECIDE não é quantos leads rejeitam — é a largura deles.
      mh <- median(pre$meia_largura, na.rm = TRUE)
      cat(sprintf("       meia-largura mediana dos leads: %.1f g
", mh))
      cat(sprintf("       ⚠️ contra o piso de 15 g da §5: %.1fx MAIOR
", mh / 15))
      cat("          Uma violação do tamanho que se procura seria INVISÍVEL.
")
      cat("          Leads dentro do zero não provam paralelismo — provam falta
")
      cat("          de poder para rejeitá-lo. É o que o `pretrends` quantifica.
")
    }
    return(invisible(tidy))
  }

  campo <- if (alvo == "slope") "acrt.d" else "att.d"
  est <- obj[[campo]]
  se <- obj[[paste0(campo, "_se")]]
  crit <- obj[[paste0(campo, "_crit.val")]]
  if (is.null(est) || is.null(se)) {
    stop("objeto do contdid sem `", campo, "` ou `", campo,
         "_se`. A API mudou — confira names(obj) antes de confiar na saída.")
  }
  # `cband = TRUE` devolve valor crítico de banda UNIFORME, não 1,96. Usar 1,96
  # aqui estreitaria a banda e inverteria o teste de falsificação.
  tidy <- data.table(
    dose = obj$dose,
    estimativa = est,
    erro_padrao = se,
    valor_critico = if (is.null(crit)) NA_real_ else as.numeric(crit)[1]
  )
  tidy[, ic_inf := estimativa - valor_critico * erro_padrao]
  tidy[, ic_sup := estimativa + valor_critico * erro_padrao]
  tidy[, meia_largura := valor_critico * erro_padrao]
  if (alvo == "level" && is.finite(ep_m0)) {
    tidy[, ep_m0 := ep_m0]
    tidy[, ic_inf_m0 := estimativa - valor_critico * sqrt(erro_padrao^2 + ep_m0^2)]
    tidy[, ic_sup_m0 := estimativa + valor_critico * sqrt(erro_padrao^2 + ep_m0^2)]
    fora_pacote <- tidy[ic_sup < 0 | ic_inf > 0, .N]
    fora_m0 <- tidy[ic_sup_m0 < 0 | ic_inf_m0 > 0, .N]
    cat(sprintf("       pontos cuja banda exclui o zero: %d de %d pela banda do pacote;\n",
                fora_pacote, nrow(tidy)))
    cat(sprintf("       %d de %d com o EP do grupo zero (%.2f) somado. Use a segunda.\n",
                fora_m0, nrow(tidy), ep_m0))
  }
  for (nome in names(extra)) tidy[[nome]] <- extra[[nome]]
  caminho <- file.path(saida, arquivo)
  data.table::fwrite(tidy, caminho)
  cat("  [ok]", caminho, "\n")
  invisible(tidy)
}

# ⚠️ FALHA DURA (auditoria de 2026-09-23). O `tryCatch` imprimia o erro e o
# script terminava com status 0: o `make` seguia, e um CSV de rodada anterior,
# com o mesmo nome, passava por resultado desta. Agora quem falha tem o CSV
# antigo removido, e o script sai com status 1 no fim.
falhas <- character(0)
remove_antigo <- function(arquivo) {
  caminho <- file.path(saida, arquivo)
  if (file.exists(caminho)) {
    file.remove(caminho)
    cat("  [removido] CSV de rodada anterior:", caminho, "\n")
  }
}

resultados <- list()
for (alvo in c("level", "slope")) {
  cat("\n  target_parameter =", alvo,
      if (alvo == "level") "  -> ATT(d|d), sob Assumption PT"
      else "  -> ACR(d), exige Assumption SPT (NÃO testável)", "\n")
  res <- tryCatch(
    cont_did(
      yname = "y", dname = "dose", gname = "g", tname = "periodo", idname = "id",
      data = as.data.frame(colapsado),
      target_parameter = alvo,
      aggregation = "dose",
      treatment_type = "continuous",
      dose_est_method = "cck",
      control_group = control_group,
      biters = biters,
      cband = TRUE
    ),
    error = function(e) { cat("  [erro]", conditionMessage(e), "\n"); NULL }
  )
  resultados[[alvo]] <- res
  if (is.null(res)) {
    falhas <- c(falhas, alvo)
    remove_antigo(sprintf("cgs_curva_%s__%s__d0-%s.csv", alvo, desfecho, d_zero))
  }
  if (!is.null(res)) {
    # ⚠️ O DESFECHO ENTRA NO NOME. Sem isso, rodar o confirmatório #2
    # (óbito fetal) SOBRESCREVIA os arquivos do #1 (peso), e o único sinal
    # era a coluna `desfecho` por dentro — que ninguém confere antes de ler
    # o CSV que acabou de ser gravado. Mesma classe do sufixo `__sidra` que
    # já quebrou o encontro das trilhas no E5.
    # ⚠️ E a construção do d = 0 TAMBÉM entra no nome. Sem ela, rodar a
    # sensibilidade `--d-zero 1` gravava por cima do primário `--d-zero 4`,
    # e o arquivo ficava com o rótulo certo e o conteúdo da outra rodada.
    # Duas rodadas que se apagam são pior que uma só: dão a impressão de
    # que a sensibilidade foi feita.
    grava_tidy(res, sprintf("cgs_curva_%s__%s__d0-%s.csv", alvo, desfecho, d_zero),
               alvo = alvo, ep_m0 = ep_do_m0(colapsado),
               extra = list(alvo = alvo, desfecho = desfecho, contraste = contraste,
                            fonte = fonte_painel))
    # O agregado — o número que vai para o texto. `overall_att` é o ATT médio
    # sobre os tratados; `overall_acrt`, o ACR médio.
    ag_est <- if (alvo == "slope") res$overall_acrt else res$overall_att
    ag_se  <- if (alvo == "slope") res$overall_acrt_se else res$overall_att_se

    # ⚠️⚠️ O `overall_acrt` NÃO É INTERPRETÁVEL COMO IMPRESSO, e isto foi
    # diagnosticado medindo, em 2026-09-22, ao resolver uma divergência de sinal
    # entre ele (-2.946,76) e a inclinação da forma reduzida do
    # `04_robustness.py` (+6,81). Os dois usam a MESMA coluna `dose` e a MESMA
    # forma reduzida — não era escala.
    #
    # A causa é que a derivada é fortemente NÃO LINEAR e o agregado é média
    # SIMPLES sobre os pontos de dose:
    #
    #   dose < 0,1%  (48 pontos): ACR ~ -9.138   ep/|est| = 1,3  <- não identificado
    #   0,1 a 1%     (68 pontos): ACR ~   -974   ep/|est| = 1,6  <- não identificado
    #   1 a 5%       (23 pontos): ACR ~   +233   ep/|est| = 0,5
    #   5 a 20%      (17 pontos): ACR ~   +119   ep/|est| = 0,6
    #   > 20%        (13 pontos): ACR ~    -41   ep/|est| = 1,0
    #
    # A média é dominada pelos 48 pontos de dose quase nula, onde o erro-padrão
    # SUPERA a estimativa. A inclinação OLS, sendo ponderada por variância, é
    # dominada pelos poucos pontos de dose alta. Os dois resumem a mesma curva
    # com pesos diferentes, e por isso divergem de sinal.
    #
    # ⚠️ E a magnitude é artefato de UNIDADE. Na faixa `< 0,1%` a dose varia de
    # 0,000052 a 0,000995 — amplitude de 0,000943. Uma derivada de -9.138 g
    # *por unidade de dose* aplicada a essa faixa implica **-8,6 g**. O número é
    # gigante porque o denominador é minúsculo, não porque o efeito seja.
    #
    # NENHUM ponto de NENHUMA faixa exclui zero.
    if (alvo == "slope") {
      cat("       ⚠️ ACR agregado é média SIMPLES de uma derivada NÃO LINEAR.\n")
      cat("          Não leve o número cru para o texto. A decomposição por\n")
      cat("          faixa de dose mostra por quê:\n\n")
      # ⚠️ Multiplicar o ACR agregado pela amplitude total de dose NÃO dá escala
      # interpretável: isso pressupõe linearidade, que é exatamente o que falha
      # aqui. O que informa é ver a derivada por faixa, com o erro-padrão ao
      # lado — é assim que se enxerga onde ela é identificada e onde não é.
      d <- res$dose; a <- res$acrt.d; e <- res$acrt.d_se
      cortes <- c(0, 0.001, 0.01, 0.05, 0.2, 1.0001)
      rot <- c("< 0,1%", "0,1 a 1%", "1 a 5%", "5 a 20%", "> 20%")
      cat("          faixa de dose      n      ACR        ep   ep/|ACR|\n")
      for (i in seq_len(length(cortes) - 1)) {
        sel <- d >= cortes[i] & d < cortes[i + 1] & is.finite(a)
        if (!any(sel)) next
        ac <- mean(a[sel]); ep <- mean(e[sel])
        cat(sprintf("          %-14s %4d %9.1f %9.1f %9.2f%s\n",
                    rot[i], sum(sel), ac, ep, ep / abs(ac),
                    if (ep / abs(ac) > 0.5) "  <- não identificado" else ""))
      }
      cat("\n          ⚠️ A média é dominada pelos pontos de dose quase nula, onde\n")
      cat("             o ep SUPERA a estimativa. E a magnitude ali é artefato de\n")
      cat("             UNIDADE: naquela faixa a dose varia ~0,0009, então -9.138 g\n")
      cat("             por unidade de dose implica cerca de -8,6 g de efeito real.\n")
      cat("          ⚠️ Use a curva ATT(d|d), que é estável entre as faixas.\n")
    }
    if (!is.null(ag_est) && !is.null(ag_se)) {
      # ⚠️ Precisão adaptativa: uma TAXA vive em 1e-3 e sairia como "0.00 g" com
      # duas casas — número real impresso como zero é o pior tipo de saída.
      casas <- if (abs(ag_est) < 1) 5 else 2
      unid <- if (desfecho == "peso_medio") " g" else ""
      cat(sprintf(paste0("       agregado: %.", casas, "f%s  (ep %.", casas,
                         "f)  IC95%% [%.", casas, "f ; %.", casas, "f]
"),
                  ag_est, unid, ag_se, ag_est - 1.96 * ag_se, ag_est + 1.96 * ag_se))
      # ⚠️ O piso de 15 g da §5 da pré-especificação é do PESO, em gramas. Ele
      # não significa nada para uma taxa. Aplicá-lo a `taxa_obito_fetal` daria
      # "falsifica SIM" trivialmente, porque a meia-largura de uma proporção é
      # sempre << 15. Falso conforto, e do tipo que passa despercebido.
      # ⚠️ CORRIGIDO EM 2026-09-23 (auditoria). Até esta data a pergunta
      # "falsifica 15 g?" olhava só a meia-largura (`1,96·EP <= 15`), que ignora
      # o centro: IC [20; 30] passava e IC [−66,5; −5,9] não, embora o segundo
      # exclua +15 e o primeiro não. O piso se testa como teste: benefício de
      # 15 g ou mais é rejeitado quando o limite superior do IC de 95% fica
      # abaixo de +15; equivalência a ±15 g é o IC de 90% dentro de (−15; +15).
      # Para o nível (ATT agregado, não a derivada), que está em gramas.
      if (desfecho == "peso_medio" && alvo == "level") {
        ic_sup <- ag_est + 1.96 * ag_se
        ic90 <- ag_est + c(-1, 1) * qnorm(0.95) * ag_se
        cat(sprintf("       piso de 15 g da §5 — limite superior do IC 95%%: %+.2f g
", ic_sup))
        cat(sprintf("       benefício >= 15 g rejeitado? %s
",
                    if (ic_sup < 15) "SIM — o IC fica abaixo de +15" else "NAO"))
        cat(sprintf("       equivalente a ±15 g (TOST, IC 90%% [%+.2f ; %+.2f])? %s
",
                    ic90[1], ic90[2], if (ic90[1] > -15 && ic90[2] < 15) "SIM" else "NAO"))
        cat("       ⚠️ Sob PT, com o EP do multiplicador (otimista com 14 controles;
")
        cat("          o 04_robustness.py refaz com t de Welch). E é o estimando
")
        cat("          diluído: não diz nada do efeito onde havia avião.
")
      } else if (desfecho == "peso_medio") {
        cat("       ⚠️ a derivada está em g por unidade de dose: o piso de 15 g
")
        cat("          (gramas de efeito) não se aplica a ela.
")
      } else {
        cat(sprintf("       meia-largura do IC: %.4f (unidade do desfecho)
",
                    1.96 * ag_se))
        cat("       ⚠️ o piso de 15 g é do PESO — não há piso pré-especificado
")
        cat("          para este desfecho, então NÃO há teste de falsificação aqui.
")
      }
    }
  }
}

# ── 2. o que level e slope NÃO testam ───────────────────────────────────────
# Até 2026-09-23 esta seção se chamava "diagnóstico do Teorema C.1" e mandava
# comparar os dois arquivos. Não há diagnóstico: ver o cabeçalho.

cat("\n", barra, "\n", sep = "")
cat("2. LEVEL E SLOPE NÃO SÃO ATT E ATE\n")
cat(barra, "\n")
cat("Sob PT, a curva de nível é ATT(d|d); sob SPT, a MESMA curva é ATE(d)\n")
cat("(CGS, Teorema C.1). Não há duas curvas para comparar, e o slope é a\n")
cat("derivada da curva de nível, em outra unidade. Comparar os dois arquivos\n")
cat("não testa o SPT. A implicação testável, comum a PT e SPT, é a do\n")
cat("pré-período: scripts/estimate/10_spt_pretrend.py (falsifica, não valida).\n")

# ── 3. event study (parametrico, painel mensal) ──────────────────────────────
#
# ⚠️ Rodada SEPARADA de propósito: o sieve não faz event study
# (`stop("event study not supported with cck estimator yet")`). Então os leads
# que dão evidência sobre a PT saem de outro estimador que a curva — e o texto
# tem de dizer isso, em vez de deixar parecer que é tudo a mesma rodada.
#
# Os leads precisam alcançar 2018: os três marcos de antecipação são
# 24/02/2015 (notícia), 18/12/2018 (certeza) e 09/01/2019 (obrigação).

cat("\n", barra, "\n", sep = "")
cat("3. EVENT STUDY — paramétrico, painel mensal (rodada SEPARADA da curva)\n")
cat(barra, "\n")

mensal <- painel[!is.na(y), .(id, t, y, dose)]
# Mesmo `gname`, agora no calendário mensal: o ban entra em vigor em
# 09/01/2019, que neste índice é 2019*12 + 0.
mensal[, g := fifelse(dose > 0, 2019L * 12L + 0L, 0L)]
completos_m <- mensal[, .N, by = id][N == max(N), id]
mensal <- mensal[id %in% completos_m]
cat("  painel balanceado:", uniqueN(mensal$id), "municípios ×",
    uniqueN(mensal$t), "meses\n")

es <- tryCatch(
  cont_did(
    yname = "y", dname = "dose", gname = "g", tname = "t", idname = "id",
    data = as.data.frame(mensal),
    target_parameter = "level",
    aggregation = "eventstudy",
    treatment_type = "continuous",
    dose_est_method = "parametric",
    control_group = control_group,
    biters = biters,
    cband = TRUE
  ),
  error = function(e) { cat("  [erro]", conditionMessage(e), "\n"); NULL }
)
if (is.null(es)) {
  falhas <- c(falhas, "eventstudy")
  remove_antigo(sprintf("cgs_eventstudy__%s__d0-%s.csv", desfecho, d_zero))
}
if (!is.null(es)) {
  grava_tidy(es, sprintf("cgs_eventstudy__%s__d0-%s.csv", desfecho, d_zero),
             extra = list(desfecho = desfecho, contraste = "event study mensal, g = 2019-01",
                          fonte = fonte_painel))
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

if (length(falhas) > 0) {
  cat("\n[erro] estimação falhou em:", paste(falhas, collapse = ", "),
      "— saindo com status 1.\n")
  quit(status = 1)
}
