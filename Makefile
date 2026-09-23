# Ordem de execução do pipeline do Ensaio 1.
#
# Catorze scripts com dependência entre si e sem alvo único que os rode na ordem é
# convite a estimar com painel velho. Este arquivo é o achado de
# reprodutibilidade da revisão metodológica (docs/ars/09) virando alvo.
#
#   make simulado   # pipeline inteiro com dado simulado (valida o código)
#   make real       # exige pré-especificação preenchida; roda contra dado real
#   make teste      # a suíte
#   make varredura  # bans municipais < 2019 (rede pesada; produto commitado)
#   make gaez       # aptidão FAO-GAEZ (exige rasters em data/geo/)
#
# ⚠️ `make real` é bloqueado de propósito enquanto docs/pre-especificacao.md
# estiver com "Status: ⬜ não preenchido". Ver o achado M1 da revisão: 31 séries
# candidatas a desfecho e poder curto pedem plano ANTES do dado.
#
# ⚠️ AUDITORIA 2026-09-21: este arquivo tinha ficado para trás do pipeline —
# conhecia sete scripts quando já eram onze, e por isso `make real` montava o
# painel SEM bans municipais, SEM SINAN, SEM população e SEM GAEZ. Era
# exatamente o "estimar com painel velho" que ele existe para impedir. Um
# orquestrador desatualizado é pior que nenhum: ele dá a impressão de que a
# ordem está garantida.

PY      := python

# ⚠️ ARMADILHA DE WINDOWS, achada rodando em 2026-09-21. O `make` que vem com o
# Rtools é MSYS e **não repassa `APPDATA`**. Sem ela o Python resolve o user
# site-packages para o literal `~\Python\Python313\site-packages` e não enxerga
# NENHUM pacote instalado pelo usuário: `make simulado` morre em
# `ModuleNotFoundError: No module named 'dateutil'` enquanto o mesmo comando,
# rodado à mão, funciona. O sintoma aponta para o pacote; a causa é a variável.
# `USERPROFILE` também é removida; só `HOME` sobrevive, e em forma MSYS
# (`/c/Users/...`). `cygpath -w` a converte para a forma que o Python entende.
ifeq ($(APPDATA),)
export APPDATA := $(shell cygpath -w "$(HOME)" 2>/dev/null)\AppData\Roaming
endif

# ⚠️ Conserto de sintoma, não de causa. A causa é o projeto usar o Python do
# sistema com pacotes em user site-packages. O gates doc §1.3 já recomenda um
# `.venv` — instalar o `pysus` rebaixou o pandas global de 3.0.0 para 2.3.3 e
# quebrou um pacote não relacionado. Com `PY := .venv/Scripts/python` esta
# armadilha inteira desaparece, junto com aquela.

# ⚠️ SEM DEFAULT, e isso conserta um bug real. Era `CULTURA ?= Melão`. O Gate 1
# contra dado real descartou o melão — 10 municípios com área positiva, curva
# abandonada. Rodar com o default montava o painel na cultura que o dado já
# tinha eliminado, e NÃO falhava: só produzia resultado errado em silêncio.
# Exigir a escolha não hard-coda âncora nenhuma (o CLAUDE.md proíbe): recusa
# escolher, que é o que o repositório manda o script 05 fazer.
CULTURA ?=
DESFECHO?= peso_medio
MDE     ?=

# Construção do d = 0 da §5.3. A pré-especificação de 2026-09-21 ratificou a
# **definição 4** (baixa aptidão FAO-GAEZ), que só passou a ser possível depois
# que o GAEZ foi adquirido. `D_ZERO=1` roda a definição base como sensibilidade,
# e o nome do arquivo de saída carrega a construção — duas rodadas não se
# apagam. ⚠️ Trocar o primário aqui exige entrada na tabela de desvios da §8.
D_ZERO  ?= 4

.PHONY: teste simulado real limpar prespec-ok cultura-ok varredura gaez ajuda

ajuda:
	@echo "make teste     — 274 testes (3 exigem requirements-geo.txt)"
	@echo "make simulado  — pipeline completo, dado simulado"
	@echo "make real      — pipeline completo, dado real (exige pré-especificação)"
	@echo "make varredura — bans municipais < 2019 (rede pesada; produto commitado)"
	@echo "make gaez      — aptidão FAO-GAEZ (exige rasters em data/geo/)"
	@echo "make erro-classificacao — a flag 7 medida: VPP da dose + limite do ATT"
	@echo "make censo-demografico — Censo 2022 (censobr): água/esgoto CE x vizinho"
	@echo "make audita-sisagua — canal-água: o que quebra na série, e o que não"
	@echo "make fronteira-geografica — os tratados estão NA divisa? (geobr)"
	@echo "make mde-desenhos — quanto poder cada grupo tratado compra (só pré-período)"
	@echo "make mde-calendario — MDE do desenho de calendário (1º tri no pico) contra o do nível"
	@echo "                 (PICO=2,3,4,5 é HIPÓTESE; TRATADOS=cód,cód substitui o Censo 2006)"
	@echo "make fronteira — Rota 1: ingestão CE+vizinho e o GATE de viabilidade"
	@echo "                 (VIZINHO=24 RN padrão | 22 PI | 26 PE)"
	@echo "make limpar    — apaga data/processed/"
	@echo ""
	@echo "variáveis: CULTURA=<nome>  DESFECHO=<coluna>  MDE=<gramas>  D_ZERO=1|4"
	@echo ""
	@echo "D_ZERO=4 é o primário (aptidão GAEZ, ratificado na pré-especificação);"
	@echo "D_ZERO=1 roda a definição base como sensibilidade."
	@echo ""
	@echo "⚠️ CULTURA é obrigatória. O Gate 1 descartou melão e algodão;"
	@echo "   a banana sustenta a curva (169 municípios, Gini 0,86)."

teste:
	$(PY) -m pytest tests/ -q

# O segundo portão. O primeiro protege contra estimar sem plano; este, contra
# estimar na cultura errada.
cultura-ok:
	@test -n "$(CULTURA)" || { \
	  echo ""; \
	  echo "  BLOQUEADO: CULTURA não informada."; \
	  echo ""; \
	  echo "  Este Makefile não escolhe a cultura-âncora — o CLAUDE.md proíbe"; \
	  echo "  hard-codá-la, e o Gate 1 contra dado real já descartou"; \
	  echo "  empiricamente o melão (10 municípios) e o algodão (28)."; \
	  echo "  A banana sustenta a curva: 169 municípios, Gini 0,86."; \
	  echo ""; \
	  echo '  make real CULTURA="Banana (cacho)"'; \
	  echo ""; \
	  exit 1; \
	}

simulado: cultura-ok
	$(PY) scripts/data_prep/02_clean_births.py       --fonte simulado
	$(PY) scripts/data_prep/03_clean_fetal_deaths.py --fonte simulado \
	    --nascimentos data/processed/nascimentos_ce_muni_mes__simulado.parquet
	$(PY) scripts/data_prep/04_clean_poisoning.py    --fonte simulado
	$(PY) scripts/data_prep/10_clean_sinan_iexo.py   --fonte simulado
	$(PY) scripts/data_prep/11_clean_populacao.py    --fonte simulado
	$(PY) scripts/data_prep/01_check_dose_variation.py --fonte simulado \
	    --nascimentos data/processed/nascimentos_ce_muni_mes__simulado.parquet
	$(PY) scripts/build_panel/05_build_panel.py --cultura "$(CULTURA)" --fonte simulado
	$(PY) scripts/estimate/04_robustness.py --desfecho $(DESFECHO) $(if $(MDE),--mde $(MDE),)
	@echo ""
	@echo "⚠️ Tudo acima é SIMULADO. Nada é evidência sobre o Ceará."
	@echo "   O E6 e o passo Rscript scripts/estimate/03_contdid.R — R esta"
	@echo "   instalado desde 2026-09-21; ver setup_r.R e o renv.lock."

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

# ⚠️ NENHUM passo daqui pode cair para `simulado`. O alvo `real` existe para
# rodar contra dado real, e `--fonte auto` termina em simulado quando a rede
# falha — painel plausível e inventado, dentro do alvo cuja premissa é o
# oposto. Por isso `--fonte ftp` explícito nos scripts 02, 04 e 10: é o
# transporte que funciona (docs/ars/15 §6) e falha DURO quando não funciona.
# A linha do 10 já era explícita (`--fonte pysus`) pela mesma razão; só mudou
# qual transporte é o que está de pé.
real: prespec-ok cultura-ok
	$(PY) scripts/data_prep/02_clean_births.py       --fonte ftp
	$(PY) scripts/data_prep/03_clean_fetal_deaths.py --fonte auto \
	    --nascimentos data/processed/nascimentos_ce_muni_mes.parquet
	$(PY) scripts/data_prep/04_clean_poisoning.py    --fonte ftp
	$(PY) scripts/data_prep/10_clean_sinan_iexo.py   --fonte ftp
	$(PY) scripts/data_prep/11_clean_populacao.py    --fonte sidra
	$(PY) scripts/data_prep/01_check_dose_variation.py --verificar-codigos
	$(PY) scripts/data_prep/01_check_dose_variation.py --fonte sidra \
	    --nascimentos data/processed/nascimentos_ce_muni_mes.parquet
	$(PY) scripts/build_panel/05_build_panel.py --cultura "$(CULTURA)" --fonte real
	Rscript scripts/estimate/03_contdid.R --desfecho $(DESFECHO) --d-zero $(D_ZERO)
	$(PY) scripts/estimate/04_robustness.py --painel data/processed/painel_ensaio1.parquet \
	    --desfecho $(DESFECHO) $(if $(MDE),--mde $(MDE),)
	Rscript scripts/estimate/06_pretrends.R --desfecho $(DESFECHO)
	Rscript scripts/estimate/07_honestdid.R --desfecho $(DESFECHO)
	Rscript scripts/estimate/08_synthdid.R --desfecho $(DESFECHO)
#	09 e 10 fecham a auditoria de 2026-09-22. O 09 é o cumprimento do Holm que a
#	§6 da pré-especificação mandava e que não existia; o 10 é a sonda do SPT que
#	o CGS §6.3 propõe — a única hipótese que o alvo primário precisava e que
#	nenhum outro passo deste alvo tocava. Nenhum dos dois usa R.
	$(PY) scripts/estimate/09_holm.py --painel data/processed/painel_ensaio1.parquet
	$(PY) scripts/estimate/10_spt_pretrend.py --painel data/processed/painel_ensaio1.parquet \
	    --desfecho $(DESFECHO)

# ⚠️ FORA de `real` DE PROPÓSITO. A varredura é dezenas de requisições a portais
# de câmara, e o produto — docs/legislacao/bans-municipais-ce.csv — é COMMITADO.
# Repeti-la a cada estimação gastaria rede para reproduzir um arquivo que já
# está no git. O script 05 LÊ o CSV; este alvo o ATUALIZA.
varredura:
	$(PY) scripts/data_prep/08_alvos_legislativos.py
	$(PY) scripts/data_prep/09_varre_camaras.py --prioridade 1

# ⚠️ FORA de `real` porque exige rasters em data/geo/, que são gitignored e
# pesam ~5 MB cada. Baixar a cada rodada é desperdício, e sem eles o script
# falha alto — que é o comportamento certo. As URLs do bucket do GAEZ estão em
# docs/gates-resultados-dados-reais.md §7-quater.
gaez:
	$(PY) scripts/data_prep/06_build_gaez.py \
	    --culturas banana coco \
	    --raster-alto  data/geo/gaez_yx_alto_banana.tif data/geo/gaez_yx_alto_coco.tif \
	    --raster-baixo data/geo/gaez_yx_baixo_banana.tif data/geo/gaez_yx_baixo_coco.tif \
	    --municipios data/geo/municipios_br.geojson --campo-id codarea \
	    --uf 23 --all-touched

limpar:
	rm -rf data/processed/*.parquet data/processed/*.csv

# A inversao de Weitzman e material do ENSAIO 2, nao do pipeline do Ensaio 1:
# nao le painel, consome as constantes ja estimadas. Alvo proprio, de proposito.
.PHONY: weitzman custo-conab equipamento erro-classificacao
custo-conab:
	$(PY) scripts/data_prep/12_clean_conab_custos.py

# ⚠️ Saiu da busca pelo lado do custo do Ensaio 2 e achou coisa do Ensaio 1:
# quem de fato pulverizava por aviao no CE. Rede leve; alvo proprio.
equipamento:
	$(PY) scripts/data_prep/13_censo_agro_equipamento.py

# ⚠️ A flag 7, MEDIDA: sensibilidade, especificidade e VPP da dose contra a
# medida direta de metodo, mais o limite do ATT sob misclassificacao. Roda sem
# rede a partir dos numeros da secao 5.4; com --censo/--dose recalcula.
erro-classificacao:
	$(PY) scripts/estimate/12_erro_de_classificacao.py

weitzman: custo-conab
	$(PY) scripts/estimate/11_weitzman_inversao.py $(if $(BETA_MIN),--beta-min $(BETA_MIN) --beta-max $(BETA_MAX),)

# --- Rota 1: desenho de fronteira CE x vizinho -----------------------------
# ⚠️ GATE, nao estimacao. Decide se a Rota 1 e viavel ANTES de investir nela:
# o vizinho tinha pulverizacao aerea no pre-ban? (SINDAG diz que o RN nao tem
# frota; o Censo Agro e quem decide.) Ver docs/ars/11-rota1-fase1-escopo.md.
# VIZINHO=24 (RN, padrao) | 22 (PI) | 26 (PE)
.PHONY: gate-fronteira equipamento-vizinho fronteira censo-demografico fronteira-geografica mde-desenhos mde-calendario
VIZINHO ?= 24
# ⚠️ `sufixo_das_ufs` (scripts 01 e 02) ORDENA as UFs antes de montar o nome:
# --ufs 23 22 grava `__uf22-23`, nao `__uf23-22`. Montar o sufixo a mao como
# "uf23-$(VIZINHO)" funcionava para 24 e 26 e QUEBRAVA para 22 — justamente o
# vizinho que o gate manda tentar quando o RN reprova no G1. `$(sort ...)` e
# lexical, e com codigos de dois digitos isso coincide com a ordem numerica.
UFS_ORDENADAS := $(sort 23 $(VIZINHO))
SUFIXO_UF := uf$(word 1,$(UFS_ORDENADAS))-$(word 2,$(UFS_ORDENADAS))

# Censo 2022 por setor via censobr (GitHub Releases do IPEA). Triagem ESTRUTURAL
# (agua, esgoto, poco) entre os dois lados da linha. Niveis, nao tendencias.
censo-demografico:
	$(PY) scripts/data_prep/15_censo_demografico.py --ufs 23 $(VIZINHO) --verificar-dicionario

equipamento-vizinho:
	$(PY) scripts/data_prep/13_censo_agro_equipamento.py --uf $(VIZINHO)

# Canal-água. ⚠️ AUDITORIA, não ingestão: mede a fonte, não o efeito. O §1-ter
# de docs/lacunas-de-dados.md suspendeu o canal, e este alvo diz exatamente o
# que quebra — e o que NUNCA funcionou, que é a parte pior.
.PHONY: audita-sisagua
audita-sisagua:
	$(PY) scripts/data_prep/17_audita_sisagua.py

# ⚠️ Dimensão que o gate NÃO mede: um vizinho pode passar nos três portões e
# não servir, porque o grupo tratado está a 300 km da divisa. Exige geobr
# (requirements-geo.txt) e rede. Ver docs/ars/15 §7.
# O preço de cada desenho candidato: MDE do decil (benchmark dos 33,4 g), da
# Chapada (Limoeiro + Quixeré contra o RN) e da Rota 3 (tratado pelo método).
# ⚠️ So pre-periodo, nada estimado; e o painel tem de ter o RN (make fronteira).
# Ver docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md §11.
mde-desenhos:
	$(PY) scripts/estimate/13_mde_desenhos.py \
	  --painel data/processed/nascimentos_ce_muni_mes__$(SUFIXO_UF).parquet

# ⚠️ Só o pré-período, como o mde-desenhos. O calendário do pico é HIPÓTESE
# (quadra chuvosa, por analogia com Calzada et al.) até os relatórios mensais
# do MAPA chegarem — docs/ars/19-medida-e-desenho-fase2-investigacao.md.
# Os tratados padrão são os do Censo 2006.
PICO ?= 2,3,4,5
mde-calendario:
	$(PY) scripts/estimate/14_mde_calendario.py \
	  --painel data/processed/nascimentos_ce_muni_mes.parquet \
	  --censo data/processed/censo_agro_equipamento_ce.csv \
	  --meses-pico $(PICO) $(if $(TRATADOS),--tratados $(TRATADOS),)

fronteira-geografica:
	$(PY) scripts/data_prep/16_fronteira_geografica.py --vizinhos 24 22 26

gate-fronteira:
	$(PY) scripts/data_prep/14_gate_fronteira.py --vizinho $(VIZINHO) \
	  --pam data/processed/pam_ce_muni_cultura_media__sidra__$(SUFIXO_UF).parquet \
	  --painel data/processed/nascimentos_ce_muni_mes__$(SUFIXO_UF).parquet

# Ingestao multi-UF + gate, na ordem. ⚠️ Nao monta painel nem estima: a
# estrategia de identificacao nao muda sem o orientador (CLAUDE.md).
# ⚠️ O script 02 vai de `--fonte ftp`, nao `pysus`: o pysus passa pelo espelho
# DuckLake em HTTPS, que caiu em 2026-09-22 enquanto o FTP do DATASUS — a fonte
# original — respondia em 0,4 s. E aqui nao pode haver queda silenciosa para
# simulado, porque o que vem depois e um GATE. Ver docs/ars/15 §6.
fronteira:
	$(PY) scripts/data_prep/01_check_dose_variation.py --fonte sidra --ufs 23 $(VIZINHO)
	$(PY) scripts/data_prep/02_clean_births.py --fonte ftp --ufs 23 $(VIZINHO)
	$(MAKE) censo-demografico VIZINHO=$(VIZINHO)
	$(MAKE) gate-fronteira VIZINHO=$(VIZINHO)
