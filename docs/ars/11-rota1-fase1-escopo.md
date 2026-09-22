# Rota 1 — Fase 1 (escopo): o desenho de fronteira CE × vizinho

*ARS `deep-research`, modo `full`, Fase 1 de 6. Oversight: alto — a Fase 2 não
abre sem confirmação. 2026-09-22.*

> **Estado: AGUARDANDO CONFIRMAÇÃO.** A Fase 1 devolveu três achados que mudam a
> Rota 1 como ela foi escrita em `auditoria-mensuracao-do-tratamento.md` §4.
> Um deles **corrige uma afirmação minha** e outro **pode inviabilizar a rota na
> forma proposta**. Registrar isso antes de investigar é o ponto da fase.

---

## 1. RQ Brief

### Pergunta candidata

> **O banimento estadual da pulverização aérea no Ceará (Lei 16.820/2019) alterou
> desfechos perinatais nos municípios da Chapada do Apodi cearense, relativamente
> aos municípios potiguares do mesmo complexo de fruticultura irrigada, que
> permaneceram sob o regime anterior?**

### Subperguntas

1. O complexo agrícola da Chapada do Apodi é, de fato, contínuo através da
   fronteira CE–RN — em cultura, em aptidão e em prática de aplicação?
2. A diferença que a fronteira cria em 2019 é **a pulverização aérea**, ou é a
   pulverização aérea **somada** a tudo mais que difere entre dois estados?
3. O ban deslocou operação aeroagrícola para o outro lado da linha?

### FINER

| critério | avaliação |
|---|---|
| **F**easible | ⚠️ **é o critério em risco** — ver §3. O pipeline já aceita multi-UF (§4), mas a viabilidade depende de um fato ainda não verificado sobre o RN |
| **I**nteresting | ✅ alto. Um ban de método avaliado em fronteira é desenho raro |
| **N**ovel | ✅ a busca não devolveu nenhuma avaliação causal do ban cearense por desenho de fronteira |
| **E**thical | ✅ dado secundário agregado; microdado não sai de `data/` |
| **R**elevant | ✅ dez estados discutem normas análogas; o STF já validou a cearense |

### Fronteiras de escopo

**Dentro:** desfechos SINASC/SIM em municípios de CE e da(s) UF(s) de comparação,
2015–2024; identificação por fronteira estadual; ameaças de *compound treatment*
e de spillover.

**Fora:** o canal-água (SISAGUA suspenso, razão declarada); submunicipal
(vedado na pré-especificação §7); o Ensaio 2.

---

## 2. Blueprint de metodologia

| dimensão | escolha | razão |
|---|---|---|
| Paradigma | positivista / inferência causal | idioma da banca |
| Desenho | **difference-in-discontinuities geográfico** | ver abaixo |
| Unidade | município × ano-mês | mantém a pré-especificação |
| Dados | secundários (SINASC, SIM, PAM, GAEZ, Censo Agro) | já mapeados |
| Comparação | municípios da UF vizinha na faixa de fronteira | a decidir — §3 |

### Por que diff-in-disc e não RD geográfico puro

O RD de fronteira administrativa tem crítica conhecida: **múltiplos tratamentos
mudam no mesmo corte**. Atravessar a linha CE–RN não muda só a pulverização
aérea — muda secretaria de saúde, financiamento SUS estadual, política agrícola
estadual e capacidade fiscal. Um RD puro atribuiria tudo isso ao ban.

> **Cunningham, J. (2021).** *Geographic Difference-in-Discontinuities.*
> **arXiv:2109.07406** — estende o arcabouço de Grembi, Nannicini & Troiano
> (2016) ao caso geográfico e formaliza as hipóteses que permitem **remover
> sorting invariante no tempo e tratamentos compostos**, à maneira do DiD.
> ⚠️ *working paper*, conferido no arXiv em 2026-09-22.

A lógica é a que este projeto precisa: a descontinuidade na fronteira **antes**
de 2019 mede tudo que difere entre os dois estados e não é o ban; a diferença
entre a descontinuidade pós e a pré isola o ban, **desde que** o resto não mude
em 2019.

**Ferramental conferido:** `rd2d` (arXiv:2505.07989 — R, Python e Stata, para
*boundary discontinuity designs* com escore bivariado) e a síntese de
Cattaneo et al. sobre BD designs (arXiv:2511.06474, ~80 aplicações). Ambos
*working papers*.

---

## 3. ⚠️ Devil's Advocate — Checkpoint 1: **REVISE**

Três achados. O primeiro favorece a rota, o segundo a ameaça e o terceiro
corrige a auditoria anterior.

### 3.1 ✅ A "mesma Chapada" não é inferência minha — tem delimitação oficial

O **PLP 98/07** (dep. Betinho Rosado, RN), aprovado na Comissão da Amazônia e
Desenvolvimento Regional da Câmara, autoriza criar a **Região Administrativa
Integrada de Desenvolvimento (RIDE) da Chapada do Apodi**, formada por **21
municípios do RN e 9 do Ceará**. Os 21 potiguares são: Afonso Bezerra, Alto do
Rodrigues, Apodi, Areia Branca, Assu, Baraúna, Caraúbas, Carnaubais, Felipe
Guerra, Galinhos, Governador Dix-Sept Rosado, Grossos, Guamaré, Ipanguaçu,
Macau, Mossoró, Pendências, Porto do Mangue, Serra do Mel, Tibau e Upanema.

**Por que importa para a identificação:** é um recorte **externo, anterior e
independente do desfecho**. Escolher o grupo de comparação por delimitação
administrativa preexistente é muito mais defensável do que escolhê-lo por
parecer semelhante depois de olhar o dado.

⚠️ É **projeto de lei complementar aprovado em comissão**, não RIDE instituída.
Serve como delimitação documentada, não como entidade jurídica. Confirmar o
desfecho da tramitação antes de citar.

### 3.2 🔴 O achado que ameaça a rota: o RN pode não ter tido o que perder

Dados do **SINDAG** sobre a frota aeroagrícola do Nordeste: **293 aeronaves em
seis estados** — Bahia 173, Maranhão 63, Piauí 41, Alagoas 14, Pernambuco 5,
Sergipe 1. Os três estados nordestinos **sem frota** são **Ceará, Rio Grande do
Norte e Paraíba**.

> **Se o Rio Grande do Norte não tem aviação agrícola, a frase que escrevi na
> auditoria — *"município potiguar com banana e aeronave, do outro lado da
> linha"* — descreve uma unidade que pode não existir.**

E isso desmonta a razão pela qual a rota parecia forte: a comparação deixaria de
ser entre **iguais sob regimes diferentes** e passaria a ser entre quem *perdeu*
a pulverização aérea e quem *nunca a teve*. O `d = 0` que a rota prometia
eliminar reapareceria do outro lado da fronteira, com outro nome.

**Três ressalvas que impedem de encerrar a rota agora:**

1. O número é **de 2025**, não de 2015–2018. Frota atual não é frota pré-ban.
2. Registro é por **base do operador**, não por onde a aeronave voa. Aviação
   agrícola é ativo móvel: uma empresa sediada em Pernambuco atende contrato no
   RN sem constar do RN.
3. É contagem de **empresas do sindicato**, não cadastro regulatório completo.

**O teste que decide** é o mesmo que o projeto já rodou para o Ceará:
Censo Agropecuário, tabela SIDRA **1008** (equipamento de aplicação, categoria
aeronave), agora para a **UF 24**. O script `13_censo_agro_equipamento.py` já
existe. Falta rede — ver §5.

### 3.3 🔴 Correção de uma afirmação minha da auditoria

Escrevi em `auditoria-mensuracao-do-tratamento.md` §4, Rota 1:

> *"O viés é de contaminação do controle, isto é, **atenuante** — conservador, e
> é a direção certa de errar."*

**Isso está errado como afirmação geral, e a literatura de fronteira mostra por
quê.** Há dois canais de spillover com **sinais opostos**:

| canal | efeito sobre o controle | efeito sobre a estimativa |
|---|---|---|
| **Deriva** atravessa a linha | RN recebe parte do benefício do ban | **atenua** — conservador |
| **Realocação** da operação aérea | RN recebe MAIS pulverização que antes | **infla** o benefício aparente |

O segundo canal não é hipotético: é o resultado central do caso canônico de
desenho de fronteira com deslocamento.

> **Geographic Spillover Effects of Prescription Drug Monitoring Programs**,
> **arXiv:2107.04925** — *"reduces a state's opioid sales but **increases**
> opioid sales in neighboring counties on the other side of the state border"*,
> e ainda *"systematic differences in opioid sales and mortality between border
> counties and interior counties"*. ⚠️ *working paper*, lido pelo resumo.

Ou seja: a fronteira tem **duas** falhas conhecidas, e este desenho está exposto
às duas. A direção líquida do viés é **ambígua**, não conservadora. E a segunda
linha da citação é uma terceira ameaça: municípios de fronteira não são como os
do interior — nem do lado tratado.

⚠️ E há um agravante específico daqui: a busca registra que a pressão social
contra a aviação agrícola **fez empresas deixarem a região**. Se essa pressão
atravessou a fronteira junto com o debate público do ban, o "controle" potiguar
foi parcialmente tratado pelo próprio movimento que produziu a lei.

### 3.4 Uma correção factual de rota menor, mas que evita erro no texto

Uma busca intermediária sugeriu que **a Paraíba tem lei** proibindo pulverização
aérea. **Conferindo, é Projeto de Lei apresentado em 30/06/2023** — não lei
sancionada. O documento que a busca encontrou é o PL, não a norma.
**O Ceará segue sendo o único ban estadual em vigor na janela deste trabalho.**
Registrado para que não entre no paper como fato.

### 3.5 ✅ E um achado que abre porta em vez de fechar

O polo irrigado RN–CE é caracterizado por **melão e melancia**, com cerca de
**20 mil hectares** por safra. O Gate 1 encerrou o melão como âncora por falta
de suporte — **10** municípios com área positiva **no Ceará**.

> Esse encerramento é **condicional à amostra só-Ceará**. O cinturão do melão
> está do lado potiguar. Um painel CE+RN pode devolver ao melão o suporte que
> lhe faltava — e o melão casa melhor com a química do Dossiê que a banana.

Isso não reabre a decisão sozinho, mas a torna **empírica de novo** em vez de
encerrada. Entra como subpergunta, não como troca de âncora.

---

## 4. O que já foi construído (não depende da confirmação)

As três opções da §5 exigem ingestão multi-UF. Ela existe agora, testada.

| arquivo | mudança |
|---|---|
| `01_check_dose_variation.py` | `UFS_PADRAO`, `territorio_sidra()`, `sufixo_das_ufs()`, `--ufs`; `ufs` atravessa `carrega_pam` → `_pam_via_sidrapy` / `_pam_via_rest` / `_finaliza_pam` |
| `02_clean_births.py` | `UFS_PADRAO`, `SIGLA_POR_UF`, `filtra_ufs()`, `_sigla_da_uf()`, `sufixo_das_ufs()`, `--ufs`; `ufs` atravessa `carrega_nascimentos` → `carrega_de_pysus` |
| `tests/test_data_prep.py` | **9 testes novos**; suíte de 157 → **166, todos passando** |

**O padrão não mudou:** sem `--ufs`, tudo se comporta exatamente como antes —
`territorio_sidra(("23",))` devolve a constante antiga e `filtra_ceara` virou
caso particular de `filtra_ufs`, com teste que trava a equivalência.

**A guarda que mais importa** é o sufixo de arquivo. Verificado rodando:

```
nascimentos_ce_muni_mes__simulado.parquet            # --fonte simulado
nascimentos_ce_muni_mes__uf23-24__simulado.parquet   # --ufs 23 24
```

Sem ele, `--ufs 23 24` gravaria por cima do painel canônico e o script 05
montaria o painel com o RN dentro **sem nada acusar** — a mesma classe de erro
que o `__sidra` já causou no E5. Dois testes travam isso, inclusive a
estabilidade à ordem (`--ufs 24 23` grava no mesmo lugar).

E a consulta que iria ao SIDRA, conferida:

```
CE     -> /t/1613/n6/in n3 23/v/2313/c82/all/p/2017
CE+RN  -> /t/1613/n6/in n3 23,24/v/2313/c82/all/p/2017
```

---

## 5. ⚠️ A rede continua bloqueada, e isso condiciona tudo

`apisidra.ibge.gov.br` e `ftp.datasus.gov.br` respondem **403 no CONNECT** do
proxy de egresso desta sessão (conferido em 2026-09-22, registro em
`__agentproxy/status`). **Nenhum dado do RN foi baixado, e nenhum número sobre o
RN aparece neste documento** — os três achados da §3 vêm de fonte documental e
de busca, não de painel.

Isso é o padrão do repositório: a instrumentação fica pronta, e roda no minuto
em que a rede voltar. O que **não** dá para fazer nesta sessão é o gate da §3.2.

---

## 6. A decisão que a Fase 1 devolve

O achado 3.2 põe um trade-off que não é meu para resolver:

| | casa na **cultura** | casa no **método** |
|---|---|---|
| **Rio Grande do Norte** | ✅ mesmo complexo, RIDE, fruticultura irrigada | ❓ zero aeronaves registradas (2025) |
| **Piauí** (41 aeronaves, faz fronteira com o CE) | ✘ grão/cerrado, outra química | ✅ tem aviação agrícola |

Um vizinho casa no que a dose mede; o outro, no que o ban proíbe. Nenhum nos
dois.

**As três saídas, e o que cada uma custa:**

- **(A) Travar o gate antes de investir.** Escrever o gate do Censo Agro para a
  UF 24 e as descritivas de comparabilidade, e só decidir com eles na mão. Custo:
  a Fase 2 espera a rede. Benefício: não se constrói desenho sobre fato não
  verificado — e é o que a §6 da auditoria já recomendava.
- **(B) Reenquadrar como ITT de fronteira.** Aceitar que o RN talvez nunca tenha
  tido pulverização aérea e estimar o efeito do **pacote** cearense na fronteira,
  com diff-in-disc geográfico removendo o composto invariante. Custo: **a dose
  sai do desenho**, e com ela a âncora que o Ensaio 2 pede.
- **(C) Trocar o controle por quem tinha o método.** Piauí e/ou Pernambuco.
  Custo: perde-se a comparabilidade de cultura e de química que é a razão de ser
  da Chapada do Apodi.

⚠️ **A Fase 2 não abre sem essa escolha**, porque ela determina o corpus a
levantar: (A) pede literatura de gate e de medida; (B) pede a literatura de
diff-in-disc e de *compound treatment*; (C) pede a de transporte de estimativa
entre contextos agronômicos distintos.

---

## Referências novas desta fase

⚠️ Todas conferidas no arXiv em 2026-09-22 e **todas *working papers***, exceto
onde indicado. Nenhuma entra no `.bib` do paper antes de checagem de versão
publicada.

| id | o que é |
|---|---|
| arXiv:2109.07406 | *Geographic Difference-in-Discontinuities* — o desenho da Rota 1 |
| arXiv:2107.04925 | *Geographic Spillover Effects of PDMPs* — as duas falhas de fronteira, com sinal |
| arXiv:2505.07989 | `rd2d` — software para BD designs (R/Python/Stata) |
| arXiv:2511.06474 | *Boundary Discontinuity Designs: Theory and Practice* — síntese de ~80 aplicações |

Fontes documentais: PLP 98/07 (Câmara dos Deputados, composição da RIDE);
SINDAG (frota aeroagrícola por estado); ALPB (PL de 30/06/2023).
