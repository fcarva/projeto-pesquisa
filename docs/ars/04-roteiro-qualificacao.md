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
E1  data e janela                       A1  SINASC + SIM (pysus / BD)
E2  01_check_dose --fonte sidra         A2  FAO-GAEZ (raster)
E3  escolha de especificação            A3  ANA ottobacias + SISAGUA
E4  d = 0 e contaminação                A4  MapBiomas + INMET/FUNCEME
                                        A5  SIH + CAGED/RAIS + PIB agro
                                        A6  cadastro aeroagrícola (ANAC/MAPA/SINDAG)
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

### E1 — Data, janela e antecipação
**Faz:** confirmar 08/01/2019 contra o texto oficial da Lei 16.820/2019 (o
download da ADAGRI está pendente — ver `docs/legislacao/README.md`); fixar
janela 2015 → 19/12/2024; marcar 2019 como transição e 18/12/2018 como início da
antecipação.
**Gate:** a data oficial bate com a citada na ADI?
**Se não:** o `CLAUDE.md` volta a mudar e todas as janelas se deslocam. Refazer
E2 em diante.

### E2 — Variação de dose (o gate que amarra tudo)
**Faz:** `python scripts/data_prep/01_check_dose_variation.py --fonte sidra`
(roda na sua máquina — a rede da sessão remota bloqueia `apisidra.ibge.gov.br`).
**Passa a reportar**, além do que já reporta: número de valores distintos de dose
acima da mediana, contagem no decil superior, nascimentos acumulados no grupo de
dose alta, e o MDE implicado.
**Gate:** existe dispersão de dose utilizável, e a cultura-âncora se sustenta
empiricamente — banana, melão, ou outra?
**Se não:** o desenho de tratamento contínuo cai inteiro. Aí a rota volta a ser
controle sintético estadual ou o pareamento à la Rigotto, e a tese muda de
espinha. Melhor descobrir aqui do que no capítulo 6.

### E3 — Escolha de especificação
**Faz:** aplicar a escada do CGS ao resultado de E2 (ver a nota de poder em
`02-research-plan-summary.md`) — curva não-paramétrica, dose discreta em faixas,
ou binário sob Assumption 4-Agg.
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
| A6 | cadastro aeroagrícola | definição 3 de d = 0 — a única que mede o **método** |

**Verificações a fazer na aquisição, não a assumir:**
- MapBiomas separa banana e melão, ou só classes genéricas? (A4)
- Existe mapa público de vulnerabilidade cárstica do Jandaíra, CPRM/SGB? (A3)
- SINASC 2024 já está disponível na vintage necessária? (A1 — define se a janela
  fecha em 2024 ou 2023)
- O Censo Agropecuário separa algodão agroecológico de convencional com
  granularidade municipal? (matriz de falsificação — a PAM não separa)
- Cobertura do SISAGUA correlaciona com a dose? (A3 — se sim, a ausência é
  seletiva e o canal-água vira condicional)

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

## Antes de tudo — três pendências que não são etapa

1. **Verificar as duas citações** — Larsen et al. (2017) e Marx-Stoelting et al.
   (2025) sobre Frank (2024). Nenhuma foi conferida; nenhuma está na pasta.
2. **Baixar o texto oficial da Lei 16.820/2019** (links em
   `docs/legislacao/README.md`; bloqueados na sessão remota, livres na sua máquina).
3. **Decidir o controle vetorial** — exclusão do d = 0 ou parte do tratamento.

## E as camadas socráticas que faltam

L3, L4 e L5 continuam abertas em `02-research-plan-summary.md`. O roteiro acima
não depende delas para começar em E1 e E2 — mas **E3 depende da L3** (é lá que os
critérios de especificação viram compromisso seu) e **E7 depende da L4** (é lá
que as ameaças viram lista fechada). Rodar E2 antes de fechar a L3 é aceitável;
rodar E6 antes, não.
