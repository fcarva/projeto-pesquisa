# O gate da Rota 1, completo — e o vizinho certo não é o que a Fase 1 supunha

*2026-09-22. Primeira sessão na máquina do pesquisador, continuando
`docs/ars/14-continuacao-local.md`. O que a sessão remota não podia fazer era a
rede; é o que esta fez. Quem chegar aqui depois começa pelo §8.*

> ⚠️ **Complemento da sessão remota, no mesmo dia**
> (`docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md` §8-bis). Duas
> leituras deste documento mudam. **(1)** A lei de Limoeiro de 2009 foi
> **revogada em 20/05/2010**, então a flag 0 não "fica exatamente como está":
> os dois tratados da divisa, Limoeiro e Quixeré, são tratamento genuíno em
> 2019. **(2)** A frase "a partir de λ = 0,5 o efeito implicado continua a
> ultrapassar o MDE" (§5) compara o limite do ATT com o MDE do estimando θ, e
> essa comparação não serve. E o G1 reprovado talvez não derrube a Rota 1,
> leitura que fica para o orientador.

---

## 1. O gate, com os três vizinhos e os três portões

`14_gate_fronteira.py`, Censo Agropecuário 2006 (SIDRA 1008), PAM 2015–2018 e
painel SINASC 2015–2022:

| vizinho | G1 — tinha aeronave? | G2 — melão fecha? | G3 — registro comparável? | agregado |
|---|---|---|---|---|
| **RN (24)** | ✘ **5** estab. em **2** mun. | ✔ 34 (10 CE + 24 RN) | ✔ 3.215 g (Δ −7 g) | **✘** |
| **PI (22)** | ✔ **22** estab. em **10** mun. | ✘ 14 | ✔ 3.221 g (Δ −13 g) | ⚠ com ressalva |
| **PE (26)** | ✔ **40** estab. em **12** mun. | ✘ 23 | ✔ 3.225 g (Δ −17 g) | ⚠ com ressalva |

Referências do Ceará, mesmas fontes: **36 estabelecimentos em 7 municípios**;
peso médio **3.208 g**. O corte do G1 é 25% da frota cearense (9
estabelecimentos); o do G3 é ±50 g de diferença de nível.

**O RN reprova o G1.** Não tinha pulverização aérea a perder, e a Rota 1 na
forma proposta — comparação entre iguais sob regimes diferentes — não se
sustenta com ele.

⚠️ **O G3 passa nos três, e por isso não decide nada.** Ele era a triagem que
poderia ter eliminado um vizinho por prática de registro; não eliminou nenhum.
A escolha continua inteira entre G1 e G2 — entre o método e a cultura.

---

## 2. O trade-off da Fase 1 saiu de conjectura para medida

A tabela do §6 do doc 11 punha a escolha assim: um vizinho casa na **cultura**,
outro casa no **método**, nenhum nos dois. O gate mediu os dois eixos:

| | casa no **método** (G1) | casa na **cultura** (G2, melão) |
|---|---|---|
| RN | ✘ | ✔ **é o único que fecha** |
| PI | ✔ | ✘ |
| PE | ✔ | ✘ |

O trade-off **não se dissolveu**: confirmou-se, e agora com número. E ganhou
uma informação que a Fase 1 não tinha — **dois** vizinhos passam no método, não
um, e o que passa com folga é **Pernambuco**, que a Fase 1 sequer considerou
candidato.

⚠️ **O melão só fecha com o RN**, e fecha bem: 24 municípios potiguares contra
10 cearenses, total 34 contra o mínimo de 30. A hipótese de que "o cinturão do
melão está do lado potiguar" estava certa. Mas é o vizinho que reprova no
método.

---

## 3. ⚠️ O SINDAG não responde a esta pergunta — e o Censo mostra por quê

A Fase 1 apoiou-se no SINDAG 2025: 293 aeronaves no Nordeste em seis estados,
com **CE, RN e PB sem frota** e **PE com 5**. Contra o Censo Agropecuário 2006:

| UF | SINDAG 2025 (aeronaves) | Censo Agro 2006 (estabelecimentos que usam) |
|---|---:|---:|
| CE | **0** | **36**, em 7 municípios |
| PE | **5** | **40**, em 12 municípios |
| PI | 41 | 22, em 10 municípios |
| RN | **0** | 5, em 2 municípios |

O Ceará é a prova do problema: o SINDAG diz zero, e o Censo conta 36. **O zero
do SINDAG nunca significou "não há pulverização aérea"** — ele registra por
*base do operador*, não por onde a aeronave voa, e conta empresas
sindicalizadas, não uso declarado. Para a pergunta "o município tinha o que
perder em 2019", a fonte é o Censo, e a Fase 1 quase decidiu a rota pela fonte
errada.

⚠️ O Censo também tem suas ressalvas, e elas continuam de pé: é de **2006**,
conta **estabelecimentos** e não voos, e o Censo de 2017 não publicou o corte.

---

## 4. Três bugs que a rede expôs — e são todos da mesma família

Os scripts dos passos 2–4 estavam testados sem rede. Ao encontrar dado real,
quebraram nos pontos em que teste com fixture não alcança.

### 4.1 O painel de fronteira que só tinha o Ceará

`01_check_dose_variation.py --ufs 23 24` gravou
`pam_ce_muni_cultura_media__sidra__uf23-24.parquet` com **184 municípios, todos
cearenses**. Duas falhas encadeadas:

1. `carrega_pam_sidra` recebia `ufs` e chamava `_pam_via_sidrapy(anos)` **sem
   repassar** — os dois transportes caíam no default `("23",)`. O nome do
   arquivo, esse, vinha do argumento da CLI: **artefato rotulado de fronteira,
   conteúdo de uma UF só**.
2. Corrigido o repasse, a consulta passou a estourar o limite do SIDRA —
   **50.000 valores por requisição**, e CE+RN pedem 63.180. A resposta é
   **400**, não um resultado truncado. Agora vai **uma UF por consulta**
   (~31.600 cada), com a união conferida no fim.

⚠️ **E o gate acreditou no artefato.** Com o painel só-cearense, o G2 devolveu
`✘ melão: 10 no CE, 10 em CE+24` — leu a **ausência do RN** como achado
substantivo ("o RN não planta melão"), quando o veredito honesto era `ausente`.
É a mesma classe de erro da truncagem do bucket GAEZ, que este repositório já
cometeu uma vez: **silêncio de fonte virando resultado**. Com o dado certo, o
mesmo gate devolve `✔ 34`.

Foi acrescentada a guarda que faltava: `_confere_ufs` levanta se **qualquer** UF
pedida não voltar. Vazio total já gritava; faltar *uma* das UFs, não.

### 4.2 A coluna que os testes inventaram

`12_erro_de_classificacao.py` e `14_gate_fronteira.py` liam `area_ha` do parquet
agregado. O script 01 grava **`area_ha_media`** — só o formato longo, ano a ano,
tem `area_ha`. Os scripts 05, 07 e 08 já usavam o nome certo; 12 e 14 eram os
fora de padrão, **e os testes deles usavam fixtures com o nome errado**, de modo
que 194 testes passavam enquanto o artefato real quebrava com `KeyError`.

Os dois agora aceitam os dois nomes e **levantam erro nomeado** se não vier
nenhum. As fixtures passaram a usar o nome que o script 01 de fato grava, e
entrou teste para o caminho `metricas_de_artefatos`, que não tinha nenhum.

### 4.3 O Makefile montava o nome do artefato à mão — e errava só para o PI

`sufixo_das_ufs` (scripts 01 e 02) **ordena** as UFs antes de nomear: `--ufs 23
22` grava `__uf22-23`. O alvo `gate-fronteira` montava `"uf23-$(VIZINHO)"`, que
casa para 24 e 26 e **quebra para 22**.

⚠️ E o 22 não é um caso qualquer: é exatamente o vizinho que o doc 14 manda
tentar **quando o RN reprova no G1** — que foi o que aconteceu. O bug estava
escondido no único ramo que o gate ia tomar. Passei ao largo dele porque rodei
os comandos à mão com o nome certo; quem seguisse o `make fronteira VIZINHO=22`
do roteiro teria batido num arquivo inexistente.

Agora o Makefile deriva o sufixo com `$(sort 23 $(VIZINHO))`. Como não há `make`
nesta máquina, o contrato entrou como **teste**: ele recalcula o que o `$(sort)`
produziria e compara com `sufixo_das_ufs` para 22, 24 e 26 — os dois lados
travados juntos.

E o mesmo alvo passou a usar `--fonte ftp` em vez de `--fonte pysus` (§6.1):
o alvo termina num **gate**, e queda silenciosa para simulado ali produziria
veredito sobre microdado inventado. Também virou teste.

> **A lição das três:** fixture escrita a partir do código testa o código contra
> si mesmo. As três quebras estavam em **contratos** — entre scripts (4.1, 4.2)
> e entre o Makefile e os scripts (4.3) —, que é exatamente onde a fixture não
> olha.

---

## 5. 17 × 19 — resolvido, e eram dois números, não um

Reproduzido dos artefatos: a banana tem **169** municípios com área positiva, e
a convenção do Gate 1 tira o decil **sobre os positivos** — 169/10 ≈ **17**. O
19 vinha de dividir os 184 municípios do estado, que não é o corte da
pré-especificação.

| | decil | com aeronave | **sem** aeronave | VPP | λ teto |
|---|---:|---:|---:|---:|---:|
| **correto** | **17** | 2 | **15** | **11,8%** | 0,912 |
| superado | 19 | 2 | 17 | 10,5% | 0,925 |

Os 2 com aeronave são **Limoeiro do Norte (18) e Quixeré (9)** — as 27 aeronaves
do decil. Limoeiro é o 6º de 17, o que mantém a flag 0 exatamente como está.

⚠️ **A correção mexeu em dois números.** Onde se lia "dos **19**, **17** sem
aeronave", o certo é "dos **17**, **15** sem aeronave": o numeral 17 aparecia
nos dois papéis, e trocar só o 19 teria deixado o texto pior do que estava.
Corrigidos: `CLAUDE.md` (flag 7), `paper/secoes/05-dados.tex` §5.4,
`paper/secoes/06-diagnostico-poder.tex`, `scripts/data_prep/13`,
`docs/legislacao/lai-semace-minuta.md`,
`docs/auditoria-mensuracao-do-tratamento.md` e os testes do script 12.

Na auditoria, o **λ ingênuo** também muda — era 17/19 = 0,895, é 15/17 =
**0,882** — e a última coluna da tabela do §3 foi recalculada
(−171,4 / −294,4 / −185,7 / −307,7 g). **A leitura não muda:** o MDE é 33,4 g, e
a partir de λ = 0,5 o efeito implicado continua a ultrapassá-lo.

---

## 6. ⚠️ O diagnóstico de rede que eu errei — e o que ele rendeu

**Registro do erro primeiro, porque ele quase virou conclusão.** A primeira
versão deste documento dizia que o DATASUS estava bloqueado nesta máquina, com
"timeout de conexão", e dava o G3 por perdido. **Estava errado: eu testei as
portas erradas.**

`ftp.datasus.gov.br` não serve HTTP. Testei 443 (e depois 80), que estão
fechados porque **não há serviço ali** — e li isso como bloqueio. A porta 21
responde em **0,4 s** e lista o diretório inteiro.

| destino | porta | estado |
|---|---|---|
| `ftp.datasus.gov.br` | **21 (FTP)** | ✅ **aberta, 0,4 s** |
| `ftp.datasus.gov.br` | 80, 443 | ✘ fechadas — não há serviço |
| `nbg1.your-objectstorage.com` (espelho DuckLake do pysus) | 443 | ⚠️ TCP conecta, **sessão HTTPS morre** |
| SIDRA, censobr, Crossref, servicodados, Ceará Transparente, Planalto | 443 | ✅ respondem |

> **O que estava fora do ar não era a fonte — era um transporte até ela.** O
> pysus 2.10 **não lê o FTP**: baixa do espelho DuckLake por HTTPS. Com esse
> espelho inacessível, `--fonte pysus` falha inteiro, e a fonte original ao lado
> respondendo.

### 6.1 O transporte que faltava: `--fonte ftp`

Entrou no script 02 um segundo transporte para a **mesma** fonte: baixa
`DN{SIGLA}{ano}.dbc` do FTP do DATASUS, com cache em `data/raw/sinasc/`.

- **Escreve em `.parte` e só então renomeia.** Interrupção no meio deixaria um
  `.dbc` truncado no cache, que a rodada seguinte leria como arquivo bom —
  falha silenciosa, de novo.
- **Ano pedido e ausente é erro**, não janela curta e silenciosa.
- **É fetcher, não leitor:** baixa e delega ao caminho por arquivo, que já
  processa um DBC por vez e não segura a janela toda em memória. Só a
  proveniência gravada continua sendo `ftp`.
- **O `auto` virou pysus → FTP → simulado.** Antes era pysus → simulado: com o
  espelho fora do ar, a segunda opção era microdado **simulado**, que não é
  evidência. O simulado passou a ser último recurso, não segundo.

Validado ponta a ponta: `DNCE2015.dbc` → 132.516 registros lidos por
`pyreaddbc` no Windows. Os três painéis de fronteira foram montados por esta
rota.

### 6.2 ✅ E o FTP tem 2023 e 2024 — a premissa do desvio ao BigQuery era falsa

`docs/lacunas-de-dados.md` e `gates-resultados-dados-reais.md` §7-bis.4 diziam
"**2013–2022** no FTP do DATASUS", e foi isso que motivou toda a rota
alternativa pela Base dos Dados, com a credencial de BigQuery que ela pede.
Listando o diretório da série **consolidada**
(`/dissemin/publicos/SINASC/1996_/Dados/DNRES`, que tem uma pasta `PRELIM` irmã
e separada):

| UF | anos disponíveis |
|---|---|
| CE | 2007–**2024** |
| RN, PI, PE | 2005–**2024** |

**A janela pode fechar em 19/12/2024 pelo próprio DATASUS**, sem BigQuery e sem
credencial nova. Os dois documentos foram corrigidos.

⚠️ **Mas isso é disponibilidade, não decisão.** Ampliar o pós-ban de 2019–2022
para 2019–2024 muda `ANOS_PADRAO` do script 02 e obriga a refazer o painel — e
é decisão de desenho, que passa pelo orientador. O painel corrente segue em
**2015–2022**. E 2024 entraria **truncado** em 19/12, para preservar a cota zero
contra a Lei 19.135/2024.

### 6.3 O que os três repositórios do Sidney Bissoli renderam

| repositório | o que resolveu aqui |
|---|---|
| **healthbR** | Fechou o item 8 do doc 14: o espelho R2 cobre **SIH e SI-PNI, não SINASC** — o módulo SINASC dele lê `ftp://ftp.datasus.gov.br`. Foi essa linha que levou ao teste da porta 21 |
| **sih-br-mcp** | Cubos agregados do SIH (1992–2025, município × mês × CID) em Parquet HTTPS, `data.sidneybissoli.com`, manifest respondendo. ⬜ **Terceira rota, não usada ainda** — candidata para a pendência do canal A5 |
| **ibge-br-mcp** | SIDRA já funciona por `sidrapy` neste pipeline; valor marginal aqui |

### 6.4 ✅ O `--fonte ftp` estendido aos scripts 04 (SIH) e 10 (SINAN)

Os dois dependiam **só** do transporte que caiu. Os artefatos já existiam, então
nada estava bloqueado — mas a próxima rodada limpa quebraria. Agora os dois têm
o segundo transporte, e o `auto` dos dois virou **pysus → FTP → simulado**.

**Script 04 (SIH)** — `RD{UF}{AA}{MM}.dbc` em
`/dissemin/publicos/SIHSUS/200801_/Dados`:

- O SIH é **mensal**: a janela são **96** arquivos, não 8. Uma conexão FTP
  reaproveitada, portanto — o script 03, que já usava FTP, abre um `curl` por
  arquivo, o que aqui seriam 96 processos.
- **O grupo vem do NOME** (`RD`), como no caminho do pysus: `ER`, `RJ` e `SP`
  moram no mesmo diretório e são rejeição e serviços profissionais — entrariam
  como internação que não houve.
- ⚠️ **Mês ausente é erro.** Um ano com 11 meses produziria queda de internações
  que o texto leria como efeito.
- `carrega_de_arquivos` passou a aceitar `.dbc` (antes, só parquet e csv), e o
  recorte de colunas é feito arquivo a arquivo — a RD tem ~110 colunas.

**Script 10 (SINAN/IEXO)** — e aqui apareceu uma decisão que os outros não
tinham. O IEXO mora em **dois diretórios**:

| diretório | anos em 2026-09-22 |
|---|---|
| `SINAN/DADOS/FINAIS` | 2006–**2022** |
| `SINAN/DADOS/PRELIM` | **2023**–2026 |

> **Dado preliminar ainda é revisado pelo SINAN.** Misturá-lo com final sem
> dizer produziria uma série cuja quebra vem do estágio de consolidação, não do
> mundo — e a janela deste projeto cruza exatamente 2022/2023.

Por isso: procura em FINAIS primeiro; ano que só existe em PRELIM **levanta
erro** nomeando o ano e o diretório; com `--aceitar-preliminar` ele entra, é
cacheado com prefixo `prelim_` e a proveniência gravada no painel vira
**`ftp_preliminar`**, não `ftp`. Para a janela atual (2015–2022) tudo cai em
FINAIS, então nada muda hoje — é a guarda para quando a janela esticar.

#### Validação: o FTP reproduz o pysus exatamente, nos dois canais

Os dois painéis foram refeitos pelo FTP e comparados, célula a célula, com os
artefatos que o `pysus` havia gerado antes:

| painel | linhas | índice `cod_ibge6 × ano × mês` | diferença |
|---|---:|---|---|
| **SINAN/IEXO** (script 10) | 4.382 nos dois | idêntico | **0** nas 9 colunas de contagem |
| **SIH** (script 04) | 46 nos dois | idêntico | **0** nas 20 colunas (`DataFrame.equals` verdadeiro) |

Não é argumento de que "o FTP deveria dar o mesmo": é a comparação rodada. Os
dois transportes leem o mesmo arquivo do mesmo servidor, e agora está medido.

⚠️ **Uma assimetria deixada de propósito:** o script 10 acumula os blocos
**nacionais** antes de recortar o Ceará (~5% das linhas), igual ao caminho do
pysus. O script 03 recorta antes de acumular e gasta ~20× menos memória. É
melhoria disponível, não correção — e manter os dois transportes simétricos
vale mais aqui do que a memória.

---

## 7. O que o `02_clean_births.py` faz certo (e um aviso operacional)

Ele **falha como deve**: sai com código **1** e não grava painel nenhum quando
a rede cai. Numa primeira medição pareceu sair com 0 — era o código de saída do
`tail` no pipe, não o do Python.

⚠️ Fica o aviso: `cmd | tail` mascara o código de saída, e neste repositório
isso importa mais do que o normal, porque metade das guardas é justamente sobre
falha silenciosa.

---

## 8. Para o orientador — e eu parei aqui de propósito

⚠️ **Não montei painel de fronteira nem estimei nada.** Trocar o vizinho é
**mudança de identificação**, e o `CLAUDE.md` põe isso em "perguntar antes de".
O gate informa a decisão; não a toma.

1. **O vizinho — e a geometria corrige a leitura do gate.** O gate descarta o
   RN pelo método e aponta PI e PE. **O mapa desmente parte disso.** Um desenho
   de fronteira é, antes de tudo, uma afirmação geométrica: as unidades tratadas
   têm de estar *na linha*. Rodando `16_fronteira_geografica.py` sobre a malha
   do IBGE (geobr, geometria completa):

   | vizinho | mun. CE na divisa | **tratados** na divisa | dist. média dos 17 |
   |---|---:|---:|---:|
   | RN (24) | 12 | **2** | 169 km |
   | PI (22) | 20 | **2** | 188 km |
   | PE (26) | 10 | **0** | **323 km** |

   ⚠️ **Pernambuco é geograficamente inviável para este desenho.** Passou o G1
   com folga — 40 estabelecimentos contra 36 do Ceará —, e **nenhum** dos 17
   tratados toca a divisa dele. O mais próximo é Missão Velha, a 19 km, sem
   aeronave. Um desenho de fronteira com PE não teria unidade tratada na
   fronteira, que é a condição mínima.

   ✅ **E os dois únicos tratados COM aeronave tocam a divisa do RN.** Limoeiro
   do Norte (18 aeronaves) e Quixeré (9) — as 27 do decil — estão *em cima* da
   linha potiguar. A Chapada do Apodi é fronteira. Pelo Piauí tocam Tianguá e
   Guaraciaba do Norte (Ibiapaba), nenhum dos dois com aeronave em 2006.

   Isso não reabilita o RN no G1 nem reprova o PE no seu: é **outra dimensão**,
   e entra junto com as outras. Mas inverte o custo relativo das saídas — a (C)
   com PE deixa de ser uma opção, e a (B) com o RN ganha o argumento de que as
   unidades genuinamente tratadas são justamente as da linha.
2. **Ou a saída (B).** Se o que importa é manter a comparabilidade agronômica,
   o RN volta como ITT de fronteira — e aí a dose sai do desenho, e com ela a
   âncora que o Ensaio 2 pede.
3. **O G3 não ajuda a escolher.** Passou nos três (Δ de −7 a −17 g, tolerância
   ±50 g). A prática de registro não elimina candidato algum.
4. **O melão vira pergunta real.** Fecha o suporte (34 municípios) **só com o
   RN**. Isso não troca a âncora — a banana está ratificada na
   pré-especificação §3 —, mas é subpergunta pré-especificável para o próximo
   ciclo.
5. **O SINDAG sai do argumento** como medida de frota pré-ban (§3). Onde o texto
   se apoiar nele para dizer "o vizinho não tinha aeronave", trocar pelo Censo.
6. **λ ingênuo 0,882** em vez de 0,895 — o valor muda, a leitura não.
7. **A janela até 2024 está disponível** (§6.2). Usar ou não é decisão de
   desenho.
8. ⚠️ **O `geobr` baixa sem verificar TLS** (`InsecureRequestWarning` em
   `github.com`). O conteúdo vem do GitHub Releases do IPEA, mas a cadeia não é
   verificada — e este repositório cobra proveniência por fonte. Registrado em
   `requirements-geo.txt` e no cabeçalho do script 16. ⚠️ E o `geobr` **não tem
   bacia hidrográfica**: conferido no pacote R e no Python, as ottobacias da ANA
   seguem sendo rota própria.

---

## 9. Pendente, em ordem

1. ~~**Passo 4 do doc 14 — Crossref.**~~ ✅ **Feito em 2026-09-22.** As sete
   resolvem e entraram no `.bib` (40 → 47), com os campos gerados do registro,
   não digitados. Detalhe em `docs/referencias-verificadas.md` §9. Três coisas
   que a passada produziu além do carimbo:
   - **Rull & Ritz ganhou DOI** (`10.1289/ehp.6118`); antes só havia PMID.
   - **Borusyak, Hull & Jaravel (2025) saiu de preprint**: *Econometrics
     Journal* 28(1):83–108.
   - ⬜ **Uma pendência nova, e é do pesquisador:** "(2025)" casa com DOIS
     artigos publicados do trio — a revisão do *EJ* (entrou) e *A Practical
     Guide to Shift-Share Instruments*, *JEP* 39(1):181–204. Qual o doc 14
     pretendia não está escrito, e adivinhar é o que o log proíbe.
2. **Leituras** (§5 do doc 14): Calzada et al. inteiro; Camacho & Mejía;
   calendário de pulverização da banana no CE.
3. **Alinhar o script 03 ao padrão**: ele baixa por `ftp://` com `curl` em
   subprocesso, um por arquivo, e exige `curl` no PATH. Os scripts 02, 04 e 10
   usam `ftplib`, sem binário externo e com a conexão reaproveitada.
4. **LAI** — fora do Claude Code. ADAGRI e SEMACE como no doc 14; o Planalto
   responde nesta máquina, então o art. 66 verbatim está desbloqueado.
5. **Canal A5**: avaliar os cubos do `sih-br-mcp` contra o SINAN/IEXO
   (2.914 eventos/ano × 4 no SIH) — item 7 do §8 do `gates-resultados`.
6. **Censo 2010** no script 15, para o corte pré-ban.
