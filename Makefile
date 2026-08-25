# Ordem de execução do pipeline do Ensaio 1.
#
# Sete scripts com dependência entre si e sem alvo único que os rode na ordem é
# convite a estimar com painel velho. Este arquivo é o achado de
# reprodutibilidade da revisão metodológica (docs/ars/09) virando alvo.
#
#   make simulado   # pipeline inteiro com dado simulado (valida o código)
#   make real       # exige pré-especificação preenchida; roda contra dado real
#   make teste      # a suíte
#
# ⚠️ `make real` é bloqueado de propósito enquanto docs/pre-especificacao.md
# estiver com "Status: ⬜ não preenchido". Ver o achado M1 da revisão: 31 séries
# candidatas a desfecho e poder curto pedem plano ANTES do dado.

PY      := python
CULTURA ?= Melão
DESFECHO?= peso_medio
MDE     ?=

.PHONY: teste simulado real limpar prespec-ok ajuda

ajuda:
	@echo "make teste     — 85 testes"
	@echo "make simulado  — pipeline completo, dado simulado"
	@echo "make real      — pipeline completo, dado real (exige pré-especificação)"
	@echo "make limpar    — apaga data/processed/"
	@echo ""
	@echo "variáveis: CULTURA=<nome>  DESFECHO=<coluna>  MDE=<gramas>"

teste:
	$(PY) -m pytest tests/ -q

simulado:
	$(PY) scripts/data_prep/02_clean_births.py       --fonte simulado
	$(PY) scripts/data_prep/03_clean_fetal_deaths.py --fonte simulado \
	    --nascimentos data/processed/nascimentos_ce_muni_mes__simulado.parquet
	$(PY) scripts/data_prep/04_clean_poisoning.py    --fonte simulado
	$(PY) scripts/data_prep/01_check_dose_variation.py --fonte simulado \
	    --nascimentos data/processed/nascimentos_ce_muni_mes__simulado.parquet
	$(PY) scripts/build_panel/05_build_panel.py --cultura "$(CULTURA)" --fonte simulado
	$(PY) scripts/estimate/04_robustness.py --desfecho $(DESFECHO) $(if $(MDE),--mde $(MDE),)
	@echo ""
	@echo "⚠️ Tudo acima é SIMULADO. Nada é evidência sobre o Ceará."
	@echo "   O E6 (Rscript scripts/estimate/03_contdid.R) exige R — ver setup_r.R."

# O portão: sem plano escrito, não roda contra dado real.
# Fail-CLOSED de propósito: só passa com o marcador explícito de FECHADA.
# Marcador ausente, arquivo apagado ou renomeado => bloqueia. Um portão que
# libera quando não encontra o que procura não é portão.
prespec-ok:
	@grep -q "PRESPEC_STATUS: FECHADA" docs/pre-especificacao.md 2>/dev/null || { \
	  echo ""; \
	  echo "  BLOQUEADO: docs/pre-especificacao.md não está fechada."; \
	  echo ""; \
	  echo "  O pipeline produz 31 séries candidatas a desfecho e o poder é curto."; \
	  echo "  Rodar contra dado real sem plano escrito é o caminho mais curto para"; \
	  echo "  um achado espúrio com aparência de rigor — achado M1 da revisão em"; \
	  echo "  docs/ars/09-revisao-metodologica.md."; \
	  echo ""; \
	  echo "  Preencha, date, assine e COMMITE. O commit é o carimbo de tempo:"; \
	  echo "  o histórico do git prova que o plano é anterior ao dado."; \
	  echo ""; \
	  exit 1; \
	}
	@echo "  [ok] pré-especificação FECHADA — pode rodar contra dado real."

real: prespec-ok
	$(PY) scripts/data_prep/02_clean_births.py       --fonte auto
	$(PY) scripts/data_prep/03_clean_fetal_deaths.py --fonte auto \
	    --nascimentos data/processed/nascimentos_ce_muni_mes.parquet
	$(PY) scripts/data_prep/04_clean_poisoning.py    --fonte auto
	$(PY) scripts/data_prep/01_check_dose_variation.py --verificar-codigos
	$(PY) scripts/data_prep/01_check_dose_variation.py --fonte sidra \
	    --nascimentos data/processed/nascimentos_ce_muni_mes.parquet
	$(PY) scripts/build_panel/05_build_panel.py --cultura "$(CULTURA)" --fonte real
	Rscript scripts/estimate/03_contdid.R --desfecho $(DESFECHO)
	$(PY) scripts/estimate/04_robustness.py --painel data/processed/painel_ensaio1.parquet \
	    --desfecho $(DESFECHO) $(if $(MDE),--mde $(MDE),)

limpar:
	rm -rf data/processed/*.parquet data/processed/*.csv
