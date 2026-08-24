# Roteiro até a qualificação — Ensaio 1

*Alvo: documento de projeto defensável. Identificação fechada, dose verificada,
descritivas preliminares, ameaças mapeadas. **Não** resultado estimado.*

Cada etapa tem um **gate falsificável**: a pergunta cuja resposta negativa manda
voltar, não seguir. Etapa sem gate é etapa decorativa.

Duas trilhas correm em paralelo — a decisão de escopo cheio foi tomada
justamente para que a aquisição não espere o gate. A regra que protege o
investimento: **cada fonte tem uso declarado que sobrevive a um gate negativo.**

```
TRILHA DO GATE                          TRILHA DE AQUISIÇÃO
──────────────                          ───────────────────
E0  antecipação: PL de 2015 +  ⚠️        A1  SINASC + SIM (pysus / BD)
    bans municipais < 2019
E1  data e janela  ✅                    A2  FAO-GAEZ (raster)
E1.5 DP das tendências (SINASC) ⚠️       A3  ANA ottobacias + SISAGUA
E2  01_check_dose --fonte sidra         A4  MapBiomas + INMET/FUNCEME
E3  escolha de especificação            A5  SIH + CAGED/RAIS + PIB agro
E4  d = 0 e contaminação                A6  cadastro aeroagrícola + SEMACE
        │                                          │
        └──────────►  E5  build_panel  ◄───────────┘
                            │
                    E6  03_contdid.R
                            │
                    E7  04_robustness.py
                            │
                    E8  paper/ (qualificação)
```

---

## Trilha do gate

### E1 — Data, janela e antecipação ✅ resolvida
**Feito:** texto oficial obtido (`docs/legislacao/`). Sanção **08/01/2019**,
publicação e vigência **09/01/2019**. Janela 2015 → 19/12/2024; 2019 como ano de
transição; antecipação a partir de **18/12/2018** (aprovação na ALECE).
**Gate residual:** a data do DOE bate com a do portal da AL-CE? A própria fonte
avisa que não substitui o Diário Oficial.
**Se não:** todas as janelas se deslocam. Refazer E2 em diante.
**Pendência aberta que E1 revelou:** bans municipais anteriores a 2019 (ver o fim
deste arquivo). Essa é mais grave que a data.

### E1.5 — Dispersão das tendências municipais ⚠️ **roda antes do Gate 1**
**Faz:** `python scripts/data_prep/02_clean_births.py` contra o SINASC real, e ler
a DP das variações municipais de peso ao nascer no pré-período (o script 01 já a
reporta como `sd_tendencia_g` quando recebe `--nascimentos`).
**Por quê antes:** Reynier & Rubin acham 23–32 g. Com DP de tendências ≈ 10 g,
dois ou três municípios de dose alta bastam para detectar isso. Com DP ≈ 40 g,
seriam necessários de 14 a 28 — e Rigotto et al. trabalham com **três**. O
parâmetro que decide o Ensaio 1 é essa DP, não a dispersão de dose no PAM, e ela
sai só do SINASC. Ver `05-integracao-estado-da-arte.md` §1.
**Gate:** essa DP permite detectar 23–32 g com a ordem de grandeza de municípios
de dose alta que se espera (3 a 15)?
**Se não:** trocar o desfecho primário — taxa de baixo peso, prematuridade ou
mortalidade (SIM) têm estruturas de variância diferentes — ou trocar a unidade.
Melhor saber antes de montar treze fontes.

### E2 — Variação de dose (o gate que amarra tudo)
**Faz:** `python scripts/data_prep/01_check_dose_variation.py --fonte sidra`
(roda na sua máquina — a rede da sessão remota bloqueia `apisidra.ibge.gov.br`).
Com `--nascimentos data/processed/nascimentos_ce_muni_mes.parquet`, junta pelo
`cod_ibge6` e acrescenta o MDE.

**Colunas que o script já emite** (versão de 2026-08-24): `n_muni_positivo`,
`n_muni_zero`, `n_dose_distintas`, `n_muni_acima_mediana`,
`n_muni_decil_superior`, `share_area_decil_superior`, `gini_dose`, `cv_todos`,
`cv_positivos`, `p90_p10_positivos`, `especificacao`, `motivo` e — com a flag —
`n_nascimentos_dose_alta`, `mde_ingenuo_g`, `mde_agrupado_g`. O CSV se
identifica por dentro: cabeçalho com fonte, seed e data, e coluna `fonte` em
toda linha.

**Gate:** existe dispersão de dose utilizável, e a cultura-âncora se sustenta
empiricamente — banana, melão, ou outra?
**Se não:** o desenho de tratamento contínuo cai inteiro. Aí a rota volta a ser
controle sintético estadual ou o pareamento à la Rigotto, e a tese muda de
espinha. Melhor descobrir aqui do que no capítulo 6.

### E3 — Escolha de especificação
**Faz:** ler a coluna `especificacao`, que já aplica a escada do CGS —
≥40 municípios com suporte espalhado → curva não-paramétrica; 15 a 39 → faixas
discretas com indicadores múltiplos; <15 → binário sob Assumption 4-Agg. A
coluna `motivo` diz o que derrubou a curva quando ela cai: poucos valores
distintos de dose, ou cauda superior vazia. **A coluna recomenda; você ratifica.**
**Gate:** o número de municípios com dose positiva e o suporte no decil superior
sustentam a curva não-paramétrica?
**Se não:** desce um degrau na escada, e a mudança fica **registrada com a data**,
antes de qualquer estimação. Descer degrau não é fracasso; descer degrau sem
registrar é.

### E4 — Grupo d = 0
**Faz:** construir as quatro definições de zero (§5.3 da modelagem) e rodar o
teste de contaminação por aptidão GAEZ. Decidir — decisão do pesquisador — se
controle vetorial aéreo entra como exclusão ou como tratamento.
**Gate:** o zero é zero? Os municípios de alta aptidão com área zero se comportam
como os de baixa aptidão com área zero no pré-período?
**Se não:** o grupo de comparação está contaminado, e a magnitude da divergência
entra como correção declarada — não como nota de rodapé.

---

## Trilha de aquisição

Ordem por dependência, não por importância. Cada linha traz o uso que sobrevive
a um gate negativo em E2.

| # | Fonte | Sobrevive a gate negativo como |
|---|---|---|
| A1 | SINASC + SIM | painel de desfechos para qualquer desenho alternativo |
| A2 | FAO-GAEZ | instrumento **e** definição 4 de d = 0 **e** teste de contaminação |
| A3 | ANA + SISAGUA | canal-água, que independe do formato da curva |
| A4 | MapBiomas + INMET/FUNCEME | canal-ar; e os polígonos melhoram a própria medida de dose |
| A5 | SIH + CAGED/RAIS + PIB agro | canais de substituição e renda; insumo direto do Ensaio 2 |
| A6 | cadastro aeroagrícola (ANAC/MAPA/SINDAG) **+ registro SEMACE** | definição 3 de d = 0 — a única que mede o **método**. O art. 8º da Lei 12.228/1993 obriga prestadoras de serviço de aplicação a se registrarem na SEMACE: fonte estadual, provavelmente melhor |

**Verificações a fazer na aquisição, não a assumir:**
- MapBiomas separa banana e melão, ou só classes genéricas? (A4)
- Existe mapa público de vulnerabilidade cárstica do Jandaíra, CPRM/SGB? (A3)
- SINASC 2024 já está disponível na vintage necessária? (A1 — define se a janela
  fecha em 2024 ou 2023)
- O Censo Agropecuário separa algodão agroecológico de convencional com
  granularidade municipal? (matriz de falsificação — a PAM não separa)
- Cobertura do SISAGUA correlaciona com a dose? (A3 — se sim, a ausência é
  seletiva e o canal-água vira condicional)
- A PAM cobre 2010–2014 com comparabilidade equivalente, para uma janela
  pré-ban anterior ao PL de 2015? Houve mudança de metodologia ou de
  classificação de cultura? (E0)

---

## Encontro das trilhas

### E5 — build_panel
**Faz:** `scripts/build_panel/` — junta desfechos, dose, instrumento, bacias,
vento, canais. Painel município × ano-mês, com a retroprojeção gestacional a
partir de `SEMAGESTAC` (é para isso que o script 02 colapsa por mês e não por
ano).
**Gate:** as chaves casam? PAM tem código IBGE de 7 dígitos, SINASC tem
`CODMUNRES` de 6 — o `cod_ibge6` já está nos dois scripts para isso. E a
cobertura por município-mês é suficiente, ou as células pequenas dominam?
**Se não:** agregar a bimestre ou trimestre, com o custo declarado na precisão da
janela gestacional.

### E6 — Estimação
**Faz:** `scripts/estimate/03_contdid.R` — lê parquet, grava CSV *tidy*. Produz
`ATT(d|d)`, `ATE(d)`, e os bounds da §5.1.
**Gate:** o diagnóstico do Teorema C.1 — `ATT(d|d)` e `ATE(d)` convergem?
**Se não:** o resultado principal migra para os bounds, conforme o compromisso
registrado em `03-modelagem-ensaio1.md` §4.1. A decisão é do diagnóstico, não da
estética do coeficiente.

### E7 — Robustez
**Faz:** `scripts/estimate/04_robustness.py` — Conley–Taber, wild-cluster
bootstrap, SDID agregado, PSM+DiD como camada de comunicação, event study de
leads cobrindo 2015–2018, exclusão de fronteira, defasagem espacial da dose.
**Gate:** o efeito estimado supera o MDE do próprio desenho?
**Se não:** o resultado é um **limite superior informativo**, e é assim que ele
tem que ser escrito. Reportar um coeficiente abaixo do próprio MDE como se fosse
achado é o erro que a banca pega.

### E8 — Texto
**Faz:** `paper/` — seções de identificação, dados, descritivas e ameaças. Aqui
entra o plugin ARS em modo de escrita (`academic-paper`), com os resultados já
verificados.
**Gate:** um leitor cético consegue reconstruir a decisão de especificação a
partir do texto, incluindo os degraus que **não** foram tomados?
**Se não:** falta o registro de E3 e E6 no texto.

---

## Antes de tudo — pendências que não são etapa

1. ⚠️ **A janela pré-ban começa depois da notícia do ban.** O PL 18/2015 foi
   apresentado em **24/02/2015**; a janela pré-ban é 2015–2018. A dose medida
   pode já estar respondendo à expectativa, e isso morde a variável de
   tratamento, não só o desfecho. Ver `06-quimico-e-antecipacao.md` §1. Decidir
   se o pré-período recua para 2010–2014 é pergunta da Layer 3.
2. ⚠️ **Levantar os bans municipais anteriores a 2019.** O art. 29 da Lei
   12.228/1993 autoriza município a legislar supletivamente, e Limoeiro do Norte
   teria proibido a pulverização aérea em **2009**. Se procede, há unidades **já
   tratadas** dentro do grupo de dose alta, e 2015–2018 deixa de ser
   pré-tratamento para todos. Isso é anterior a E2 em importância: contamina a
   própria medida de dose.
3. **Verificar a citação restante** — Larsen et al. (2017) e Marx-Stoelting et al.
   (2025) sobre Frank (2024). Nenhuma foi conferida; nenhuma está na pasta.
4. **Decidir o controle vetorial** — exclusão do d = 0 ou parte do tratamento.
   Nota: a redação de 2024 **não reproduz** o §2º de 2019, então a proibição de
   dispersão aérea sanitária caiu em 19/12/2024 — mais uma razão para o corte.
5. **Checar se o cadastro da SEMACE é público** (art. 8º da Lei 12.228/1993:
   prestadoras de serviço de aplicação de agrotóxico devem se registrar). É a
   fonte estadual para o `d = 0` operacional, provavelmente melhor que
   ANAC/MAPA/SINDAG.

~~Baixar o texto oficial da Lei 16.820/2019~~ — **feito**, em `docs/legislacao/`.

## E as camadas socráticas que faltam

L3, L4 e L5 continuam abertas em `02-research-plan-summary.md`. O roteiro acima
não depende delas para começar em E1 e E2 — mas **E3 depende da L3** (é lá que os
critérios de especificação viram compromisso seu) e **E7 depende da L4** (é lá
que as ameaças viram lista fechada). Rodar E2 antes de fechar a L3 é aceitável;
rodar E6 antes, não.
