#!/usr/bin/env Rscript
# E7-ter — sensibilidade a violações de tendências paralelas (Rambachan & Roth).
#
# ══════════════════════════════════════════════════════════════════════════════
# ⚠️ POR QUE ESTE SCRIPT NÃO USA O ESTIMADOR PRINCIPAL, E O QUE ISSO CUSTA
# ══════════════════════════════════════════════════════════════════════════════
# `HonestDiD` exige coeficientes de event study **pré E pós**. O `contdid`, com
# coorte única — que é o caso de um ban simultâneo —, devolve `att_gt` com valor
# apenas para `t < g`: todos os 48 períodos pós saem NA (conferido em
# `03_contdid.R`). **Não há sobre o que aplicar o HonestDiD na curva.**
#
# A saída é produzir um event study que TENHA pós, de outro estimador, e dizer
# exatamente o que ele é. Três consequências, e nenhuma é detalhe:
#
# 1. ⚠️ **O tratamento aqui é BINÁRIO**, não a dose contínua. Tratado = decil
#    superior da cultura-âncora; controle = `d = 0` pela definição 4. É outro
#    estimando: ATT médio do grupo de dose alta, não `ACR(d)`. O texto tem de
#    dizer de qual objeto fala — a ressalva já registrada em
#    `docs/did-analysis-aderencia.md`.
#
# 2. ✅ **TWFE é legítimo AQUI**, e esse é o único caso em que é. O problema de
#    Goodman-Bacon vem de adoção **escalonada**, com unidades já tratadas
#    servindo de controle. O ban do Ceará é **simultâneo** e há grupo
#    nunca-tratado limpo: não existe comparação ruim a fazer. A cautela que o
#    `CLAUDE.md` e o `did-analysis-aderencia.md` registram contra ferramentas de
#    timing **não se aplica a este uso específico** — e é importante dizer isso,
#    porque a leitura apressada do repositório sugeriria o contrário.
#
# 3. ⚠️ **Só 3 períodos pré** depois da agregação anual (2015–2018, com −1 como
#    referência). O `Mbar` das magnitudes relativas é calibrado contra a MAIOR
#    violação pré observada — com três pontos, essa calibragem é frágil.
#
# ══════════════════════════════════════════════════════════════════════════════
# COMO LER O RESULTADO — e por que "valor de quebra" pode não existir
# ══════════════════════════════════════════════════════════════════════════════
# A pergunta usual do HonestDiD é: *até que tamanho de violação o resultado
# sobrevive?* Isso pressupõe que exista resultado a sobreviver. Se o IC original
# (Mbar = 0, paralelismo perfeito) **já cobre zero**, não há robustez a perder:
# o valor de quebra é 0, e a leitura correta não é "frágil" — é "nunca houve
# significância para ser destruída".
#
# É o que se espera num desenho cujo próprio MDE ex ante (33,4 g) supera o
# efeito procurado (15–25 g). O HonestDiD não conserta poder; ele mostra o
# preço da hipótese.
#
# USO
#   Rscript scripts/estimate/07_honestdid.R --desfecho peso_medio

suppressPackageStartupMessages({
  library(arrow); library(data.table); library(fixest); library(HonestDiD)
})

args <- commandArgs(trailingOnly = TRUE)
CONHECIDOS <- c("--painel", "--desfecho", "--saida", "--seed", "--aptidao-p",
                "--fracao-decil", "--ano-ban")
if ("--help" %in% args || "-h" %in% args) {
  cat("E7-ter — sensibilidade HonestDiD (Rambachan & Roth)\n\n")
  cat("  --painel        parquet do painel [data/processed/painel_ensaio1.parquet]\n")
  cat("  --desfecho      coluna do desfecho [peso_medio]\n")
  cat("  --fracao-decil  fração do topo que é 'tratado' [0.10]\n")
  cat("  --aptidao-p     percentil de aptidão que define o zero crível [0.75]\n")
  cat("  --ano-ban       ano de vigência [2019]\n")
  cat("  --seed          semente [20190613]\n\n")
  cat("⚠️ Tratamento BINÁRIO, não a dose contínua. Ver o cabeçalho.\n")
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
cat("E7-ter — HONESTDID |", desfecho, "\n")
cat(barra, "\n")
cat("⚠️ Tratamento BINÁRIO (decil superior), não a dose contínua. Outro estimando\n")
cat("   que a curva do E6 — ver o cabeçalho deste script.\n\n")

painel <- as.data.table(read_parquet(caminho))
painel <- painel[!is.na(get(desfecho))]
por_muni <- unique(painel[, .(cod_ibge6, dose_ha, aptidao_gaez)])

k <- ceiling(nrow(por_muni[dose_ha > 0]) * fracao)
tratados <- por_muni[dose_ha > 0][order(-dose_ha)][1:k, cod_ibge6]
corte <- as.numeric(quantile(por_muni$aptidao_gaez, aptidao_p, na.rm = TRUE))
controles <- por_muni[dose_ha == 0 & aptidao_gaez <= corte, cod_ibge6]
cat("tratados (decil superior):", length(tratados),
    "| controles (d=0 def. 4):", length(controles), "\n")
if (length(controles) < 5) {
  cat("⚠️ MENOS DE 5 CONTROLES — o IC não terá precisão utilizável.\n")
}

amostra <- painel[cod_ibge6 %in% c(tratados, controles)]
amostra[, tratado := as.integer(cod_ibge6 %in% tratados)]
# ⚠️ Agregação ANUAL de propósito. Com 96 meses o HonestDiD faria busca em grade
# sobre 48 períodos pós — caro e sem ganho: a exposição é gestacional, e o
# desenho já colapsa pré/pós no E6.
anual <- amostra[, .(y = mean(get(desfecho), na.rm = TRUE)),
                 by = .(cod_ibge6, ano, tratado)]
anual[, rel := ano - ano_ban]

modelo <- feols(y ~ i(rel, tratado, ref = -1) | cod_ibge6 + ano,
                data = anual, cluster = ~cod_ibge6)
rels <- sort(unique(anual$rel)); rels <- rels[rels != -1]
nomes <- sprintf("rel::%d:tratado", rels)
nomes <- nomes[nomes %in% names(coef(modelo))]
b <- coef(modelo)[nomes]
V <- vcov(modelo)[nomes, nomes]
n_pre <- sum(as.integer(sub("rel::(-?\\d+):tratado", "\\1", nomes)) < 0)
n_pos <- length(nomes) - n_pre
cat("períodos: ", n_pre, " pré + ", n_pos, " pós (referência: -1)\n", sep = "")
cat("betahat:", paste(round(b, 2), collapse = " "), "\n")
if (n_pre < 2) stop("HonestDiD precisa de ao menos 2 períodos pré para calibrar Mbar.")

l_vec <- rep(1 / n_pos, n_pos)   # alvo = média dos períodos pós
orig <- constructOriginalCS(betahat = b, sigma = V,
                            numPrePeriods = n_pre, numPostPeriods = n_pos,
                            l_vec = l_vec)
cat("\n", barra, "\n", sep = "")
cat("IC ORIGINAL (média dos", n_pos, "períodos pós, paralelismo PERFEITO)\n")
cat(barra, "\n")
cat(sprintf("  [%.2f ; %.2f]\n", orig$lb, orig$ub))
cobre_zero <- orig$lb <= 0 && orig$ub >= 0
if (cobre_zero) {
  cat("  ⚠️ JÁ COBRE ZERO sob paralelismo perfeito. O valor de quebra é 0, e a\n")
  cat("     leitura correta NÃO é 'o resultado é frágil' — é que nunca houve\n")
  cat("     significância para ser destruída. O HonestDiD não conserta poder.\n")
}

cat("\n", barra, "\n", sep = "")
cat("SENSIBILIDADE — magnitudes relativas (Rambachan & Roth)\n")
cat(barra, "\n")
cat("Mbar = quão grande pode ser a violação PÓS em relação à MAIOR violação PRÉ\n")
cat("observada. Mbar = 1 significa 'tão grande quanto o pior desvio pré'.\n\n")
mbar <- c(0, 0.25, 0.5, 0.75, 1, 1.5, 2)
rm_ <- createSensitivityResults_relativeMagnitudes(
  betahat = b, sigma = V, numPrePeriods = n_pre, numPostPeriods = n_pos,
  l_vec = l_vec, Mbarvec = mbar, seed = semente)
tab <- as.data.table(rm_)[, .(Mbar, lb, ub)]
tab[, largura := ub - lb]
for (i in seq_len(nrow(tab))) {
  cat(sprintf("  Mbar = %.2f : [%9.2f ; %9.2f]   largura %8.2f g\n",
              tab$Mbar[i], tab$lb[i], tab$ub[i], tab$largura[i]))
}

cat("\n", barra, "\n", sep = "")
cat("COMO LER — e o que este script NÃO diz\n")
cat(barra, "\n")
cat("  • ⚠️ Isto NÃO é a curva. É ATT binário do decil superior, de um\n")
cat("    estimador diferente do E6. O texto tem de dizer de qual objeto fala.\n")
cat("  • ✅ TWFE é válido aqui porque a adoção é SIMULTÂNEA e há nunca-tratado\n")
cat("    limpo — não há a comparação ruim de Goodman-Bacon a fazer.\n")
cat("  • ⚠️ Com", n_pre, "períodos pré, a calibragem de Mbar é frágil: ela se\n")
cat("    ancora na maior violação pré OBSERVADA, e com poucos pontos essa\n")
cat("    referência é ela mesma ruidosa.\n")
cat("  • A largura crescendo rápido com Mbar é o preço da hipótese de\n")
cat("    paralelismo. Se o intervalo já é vazio de informação em Mbar baixo,\n")
cat("    o desenho só fala sob hipótese quase perfeita — e isso é resultado.\n")
cat(barra, "\n")

dir.create(saida, recursive = TRUE, showWarnings = FALSE)
tab[, `:=`(desfecho = desfecho, n_tratados = length(tratados),
           n_controles = length(controles), n_pre = n_pre, n_pos = n_pos,
           ic_orig_lb = orig$lb, ic_orig_ub = orig$ub)]
destino <- file.path(saida, sprintf("honestdid__%s.csv", desfecho))
fwrite(tab, destino)
cat("\n[ok]", destino, "\n")
