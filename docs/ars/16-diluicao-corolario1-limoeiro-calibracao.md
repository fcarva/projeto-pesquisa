# 16 — O que a diluição de fato implica: Corolário 1, a revogação de Limoeiro e a calibração de poder

*2026-09-22, sessão remota. Continua `12-rota1-fase2-medida.md` e
`auditoria-mensuracao-do-tratamento.md`, e **corrige os dois em quatro
pontos**. Foi escrito em paralelo ao `15-gate-rota1-resultado.md` da máquina
local, que chegou ao GitHub durante esta rodada e foi mesclado; o §8-bis diz
como os dois se encaixam.*

---

## 0. Cinco achados, em ordem de consequência

1. **A lei municipal de Limoeiro do Norte foi revogada em maio de 2010**, um
   mês depois do assassinato de Zé Maria do Tomé, por um artigo da **Lei 1.511,
   de 26/05/2010** (política ambiental). A contaminação da flag 0 **não
   alcança a janela do estudo**, e os 27 estabelecimentos com aplicação por
   aeronave do grupo tratado (Limoeiro 18, Quixeré 9) são **todos** tratamento
   genuíno em 2019. ⚠️ A revogadora está identificada, mas o texto integral
   dela ainda não foi lido (§5).
2. **Negi & Negi (2025) não se aplicam.** O erro unilateral deles é o
   **inverso** do nosso: admite só falso negativo e exclui o falso positivo por
   construção. A flag 7 encaixou o estimador deles no sentido errado (§3).
3. **O resultado certo é o Corolário 1 de Denteh & Kédagni, e é notícia
   boa.** Sem falso negativo, a diluição **só atenua**, mesmo que o erro seja
   diferencial. O sinal não inverte, e a coerência de sinal entre estimadores
   volta a valer como evidência contra esta ameaça (§4).
4. **17 × 19 resolvido.** 17 é o grupo que se estima; 19 é outra conta. Dentro
   dos 17, **15 não tinham aplicação por aeronave**, e o VPP é 2/17 = 11,8% (§1).
5. **A calibração redimensiona o problema.** Com esse VPP, o sinal esperado no
   melhor análogo publicado é de **no máximo ~9 g**, e o poder **não passa de
   11%**. "Falta de poder" e "erro de medida" **não são leituras rivais**: a
   diluição é o *mecanismo* da falta de poder. E o θ̂ de −22 g **não pode ser
   lido como sinal diluído**, salvo no canto mais generoso da grade (§7).

---

## 1. 17 × 19: duas contas de "decil superior"

| conta | onde | universo | regra | resultado |
|---|---|---|---|---|
| **canônica** | estimadores `07_honestdid.R` e `08_synthdid.R`, Gate 1 (`01_*`), varredura legislativa (`08_alvos_*`) | os **169** produtores de banana | `ceil(0,10 × 169)` maiores por área | **17** |
| a do script 13 | `13_censo_agro_equipamento.py`, função `confronta` | os **184** municípios, zeros incluídos | `dose ≥ quantil(0,9)` | **19** |

A dose do script 13 é `dose_ha / máximo`, transformação monótona da área: o
ordenamento é o mesmo, e os 19 são os 17 **mais** os 18º e 19º colocados. Os
dois municípios com aplicação por aeronave têm ranks **6** (Limoeiro) e **13**
(Quixeré) de 169: estão nos dois conjuntos. Logo, **no grupo que se estima:**

> **15 dos 17 tratados** não tinham nenhum estabelecimento com aplicação por
> aeronave em 2006. **VPP = 2/17 = 11,8%.**

O "17 de 19" da flag 7, do §5.4 do paper e da §6 fala de um grupo que nenhum
estimador usa. Os arquivos foram corrigidos (§9).

⚠️ E um defeito latente, também corrigido: o script 12 calculava o decil com
`round(n/10)`, os estimadores com `ceil`. Com 169 produtores dá o mesmo; com
163 daria 16 contra 17.

## 2. O Censo mede uso, não posse

A tabela 1008 do SIDRA conta estabelecimentos por **"tipo de equipamento
utilizado na aplicação"**; o título está no docstring do próprio script 13. É o
estabelecimento que **recebeu** aplicação por aeronave, contratada ou própria,
no município onde ele fica.

A ressalva que a auditoria (§3, ressalva 2) e o script 12 usavam para
desqualificar o λ medido estava **mal posta**: *"um prestador sediado em Limoeiro
pulveriza lavoura em Quixeré — 'não ter aeronave' não é 'não receber
pulverização'"*. A lavoura de Quixeré atendida por avião de Limoeiro entra **em
Quixeré**. Ficam as ressalvas que valem: o dado é de **2006**, é declaração do
informante sobre prática regulada, e a deriva atravessa divisa municipal.

## 3. Negi & Negi: a direção do erro

Lido pelo **texto completo** em 2026-09-22 (Scholar Gateway, acervo Wiley;
*open access*). A formulação deles, eq. (5):

> *"D = D\* · S, where S is a binary indicator for correct classification. This
> is a one-sided error formulation because D = 1 implies D\* = 1 [...] In other
> words, **false negatives/errors of exclusion are permitted whereas false
> positives/errors of inclusion are ruled out**. An extension to correct for
> two-sided misclassification is not straightforward and would likely require
> an additional exclusion restriction."*

E as tendências paralelas deles são no tratamento **latente** D\*, não no
observado.

**O erro deste projeto é o espelho:** só falso positivo (dose alta sem
aeronave), nenhum falso negativo (flag 5). A flag 7 dizia *"o erro daqui é
unilateral, já provado → Negi & Negi identificam pontualmente"*. O fato está
certo e a conclusão não: é unilateral **do outro lado**. O estimador em duas
etapas deles não resolve este caso como formulado.

**Consequência prática:** a busca por uma restrição de exclusão (a auditoria
sugeria *distância a pista aeroagrícola*) perde o objeto que tinha. A
variável pode ter outros usos, mas não é mais condição de identificação de nada.

## 4. Denteh & Kédagni: o Corolário 1 é o nosso caso

Conferido contra o texto do arXiv, **v3**, atualizada em 2026-05-01. A
numeração do Corolário 5 e a fórmula que o projeto usa **não mudaram**. Mas o
artigo tem um resultado anterior, na §2.1 (misclassificação **arbitrária**),
que o projeto não tinha usado:

> ***Corollary 1.*** *Suppose that Assumption 1 holds, and there are no false
> negatives, i.e., ℙ(D\*=1, ε=1) = 0. Then, θ_DID = ℙ(ε=0|D=1)·ATT (attenuation
> bias).*
>
> *"[It] shows that even when misclassification is arbitrary, its consequence
> for DID estimation is less severe when the misclassification is one-sided."*

A **Hipótese 1** é *"parallel trends with the observed treatment D"*:
`E[Y₁(0) − Y₀(0) | D=1] = E[Y₁(0) − Y₀(0) | D=0]`. É exatamente a hipótese que
os estimadores binários do paper já mantêm e cujo pré-período já testam. O
Lema 1 dá condições suficientes: tendências paralelas em D\* e, dentro de cada
braço verdadeiro, entre bem e mal classificados.

**Por que o sinal não inverte aqui.** Pela Proposição 1,

    θ_DID = ATT_{ε=0} · P(ε=0|D=1)  −  ATT_{ε=1} · P(ε=1|D=0)

e a inversão vem **inteira do segundo termo**, o do falso negativo no grupo de
comparação. O grupo de comparação dos scripts 07 e 08 é de dose **zero**, e
nenhum município de dose zero tinha aplicação por aeronave. O termo é zero.

**O que muda:**

| antes | agora |
|---|---|
| "sob erro diferencial o sinal pode inverter — a coerência de sinal entre estimadores perde valor probatório" | Sem falso negativo, o erro diferencial **não inverte o sinal**. A coerência de sinal volta a valer contra *esta* ameaça. Não vale contra as outras, como tendência diferencial ou seleção para nascimento vivo |
| limite pelo Corolário 5, exige erro não-diferencial e monotonicidade | limite pelo Corolário 1: **mesmos números** com `λ = 1 − VPP`, sob hipóteses mais fracas |
| `λ` teto = 0,912 (falsos negativos contados nos 167 fora do decil) | `λ` da amostra = **0,882**: os de dose intermediária não entram no DiD binário, e no grupo de comparação o falso negativo é zero |
| identificação pontual exigiria Negi & Negi + restrição de exclusão | `ATT = θ / VPP`: **pontual dado o VPP**. Toda a incerteza da diluição mora num número só, e ele é medível (§8) |

## 5. Limoeiro: a lei de 2009 foi revogada em 2010

| fonte | o que diz | estado |
|---|---|---|
| CPT, 23/04/2014, reproduzida pela Terra de Direitos ([link](https://terradedireitos.org.br/noticias/noticias/quatro-anos-do-assassinato-de-ze-maria-uma-luta-contra-os-agrotoxicos-e-por-justica/14217); original em [cptnacional.org.br](https://cptnacional.org.br/2014/04/23/quatro-anos-do-assassinato-de-ze-maria-uma-luta-contra-os-agrotoxicos-e-por-justica/)) | *"A lei que proibia a pulverização aérea foi revogada em dia 20 de maio de 2010, um mês após o assassinato de Zé Maria."* | ✅ trecho literal, via índice de busca |
| MST, 16/01/2019 ([link](https://mst.org.br/2019/01/16/proibicao-da-pulverizacao-aerea-de-agrotoxicos-no-ceara-direito-e-conquista-dos-povos-do-campo/)) | cerca de um mês após a morte de Zé Maria, a lei municipal foi revertida e a pulverização voltou a ser permitida | ⚠️ lido pelo resumo do buscador, não pelo texto integral |
| Agência Pública / Repórter Brasil, 02/2019 | lista 8 municípios com proibição anterior à lei estadual; pela auditoria, todos no Centro-Oeste, Sul e Sudeste | ✅ consistente: Limoeiro não está na lista |
| **lei revogadora, no acervo da Câmara** | Lei **1.511, de 26/05/2010**, *"Dispõe sobre a política ambiental do município"* (`/leis/581`) | ✅ identificada (atualização abaixo); ⬜ texto integral a ler |

> **Atualização, 2026-09-22 (fim do dia).** A sessão local procurou a
> revogadora no acervo completo (2.692 leis) e não achou lei citando a 1.478
> nem datada de 20/05/2010, então contestou a revogação. A revogadora existe:
> é a **Lei 1.511, de 26/05/2010**, de política ambiental, e a revogação está
> num **artigo do corpo**. A ementa não diz nada disso, e por isso nenhuma
> busca a pegou. O *Diário do Nordeste* (abr/2010) noticiou que o projeto "tem
> em um de seus artigos a revogação da lei anterior, que proíbe a pulverização
> aérea". O G1 (31/10/2024) diz que a Câmara "votou a lei 1.511" em maio de
> 2010. O 20/05 da CPT é, provavelmente, a data da votação. Registro,
> `CLAUDE.md` e paper usam 26/05/2010. Evidência completa e pendências em
> `docs/legislacao/README.md` (bloco RESOLVIDO).

O ban municipal durou **seis meses** (20/11/2009 a maio de 2010). As
consequências, agora que a revogadora está identificada:

- **Flag 0:** a contaminação do pré-período **não existe na janela do estudo**.
  Em 2015–2018 Limoeiro pulverizava como os vizinhos.
- **Flag 7:** o "descontado Limoeiro, sobram 9 aeronaves em Quixeré" cai. Os 27
  estabelecimentos do grupo tratado são tratamento genuíno em 2019, e o VPP é
  **2/17**, não 1/17. A calibração mantém 1/17 como cenário para o caso de a
  revogação não se confirmar.
- **Pipeline:** a varredura (script 09) grava só a **primeira** lei que acha e
  nunca procura a que a revoga, cuja ementa ("Revoga a Lei nº…") não casa com
  nenhum termo de busca. ⚠️ E o caso real era pior do que este pressuposto: a
  ementa da revogadora não diz "revoga" **nem** cita o número. O `--revogacao`
  passou a marcar leis-quadro ambientais posteriores (`lei_quadro`) como
  candidatas a ler. O registro ganhou as colunas `data_revogacao` e
  `fonte_revogacao`. O painel ganhou `ban_municipal_revogado_em` e
  `ban_vigente_em()`, e o relatório passou a dizer quantos bans estavam
  **vigentes** em 2015.

**Para fechar, na máquina local:** abrir o anexo da Lei 1.511 em
`camaralimoeirodonorte.ce.gov.br/leis/581`, copiar o artigo revogatório para
`docs/legislacao/README.md` e trocar "secundaria" por "primaria" em
`fonte_revogacao`. Se o artigo tiver caído na votação, a revogação volta a ser
questão aberta, e a flag 0 com ela.

## 6. A geografia do grupo tratado

Os 17, na ordem da área de banana (ranks do registro em
`docs/legislacao/bans-municipais-ce.csv`):

| rank | município | região (natural ou de planejamento) | relevo | aplicação aérea 2006 |
|---:|---|---|---|---:|
| 1 | Itapajé | Serra de Uruburetama | serra | 0 |
| 2 | Uruburetama | Serra de Uruburetama | serra | 0 |
| 3 | Redenção | Maciço de Baturité | ⚠️ pé de serra | 0 |
| 4 | Itapipoca | Litoral Oeste / Serra de Uruburetama | ⚠️ misto | 0 |
| 5 | Pacoti | Maciço de Baturité | serra | 0 |
| 6 | **Limoeiro do Norte** | Vale do Jaguaribe (Chapada do Apodi) | planície irrigada | **18** |
| 7 | Missão Velha | Cariri | ⚠️ vale | 0 |
| 8 | Aratuba | Maciço de Baturité | serra | 0 |
| 9 | Mulungu | Maciço de Baturité | serra | 0 |
| 10 | Baturité | Maciço de Baturité | serra | 0 |
| 11 | Palmácia | Maciço de Baturité | serra | 0 |
| 12 | Russas | Vale do Jaguaribe | planície irrigada | 0 |
| 13 | **Quixeré** | Vale do Jaguaribe (Chapada do Apodi) | planície irrigada | **9** |
| 14 | Tianguá | Serra da Ibiapaba | serra | 0 |
| 15 | Varjota | Vale do Acaraú | planície irrigada | 0 |
| 16 | Guaraciaba do Norte | Serra da Ibiapaba | serra | 0 |
| 17 | Capistrano | Maciço de Baturité | ⚠️ pé de serra | 0 |

**Onze dos dezessete são banana de serra**: sete do Maciço de Baturité, dois
da Ibiapaba e dois da Serra de Uruburetama. Mais Itapipoca, que é mista, e
Missão Velha, no vale do Cariri. Só **quatro** estão em planície irrigada. É
na serra que a dose por área é mais alta, e é onde a pulverização aérea é
menos plausível: encosta, propriedade pequena, nenhum estabelecimento com
aplicação aérea em 2006. ⚠️ A coluna "relevo" é
classificação desta sessão, apoiada nas regiões de planejamento do IPECE e no
relevo conhecido; conferir. Ela não entra em nenhum número além do cenário de
**teto geográfico** (§7), que conta como possivelmente tratado tudo o que não é
serra: **6/17 = 0,35**. Se Redenção e Capistrano, de pé de serra, também
entrassem, o teto iria a 8/17 = 0,47, e a leitura do §7 não mudaria: o θ̂ só
vira sinal nos cantos generosos da grade.

## 7. A calibração: quanto sinal este desenho podia ver

Pelo Corolário 1, `θ = VPP · ATT*`. O ATT municipal de um município
genuinamente tratado não passa de `f · δ`: a fração `f` dos nascimentos com
exposição alta vezes o efeito individual `δ` sob exposição alta. Insumos:

- `δ = 80–150 g` — Calzada, Gisbert & Moscoso (2023): fumigação aérea de
  fungicida em bananal e peso ao nascer. ⚠️ Números **do resumo**.
- `f ∈ {0,10; 0,25; 0,50}` — **desconhecido**; é grade. 0,5 já é generoso para
  municípios de 15 a 70 mil habitantes.
- `VPP` — Censo 2006 (2/17), sem Limoeiro (1/17), teto geográfico (6/17) e
  "dose é tratamento" (1).
- MDE de 33,4 g (80% de poder, 5% bilateral), o que implica erro-padrão de
  **11,9 g**.

Saída de `make erro-classificacao` (θ esperado em gramas, poder aproximado):

| cenário | VPP | f | δ = 80 | poder | δ = 150 | poder |
|---|---:|---:|---:|---:|---:|---:|
| Censo 2006 | 0,12 | 0,10 | 0,9 | 5% | 1,8 | 5% |
| Censo 2006 | 0,12 | 0,25 | 2,4 | 5% | 4,4 | 7% |
| Censo 2006 | 0,12 | 0,50 | 4,7 | 7% | 8,8 | **11%** |
| teto geográfico | 0,35 | 0,25 | 7,1 | 9% | 13,2 | 20% |
| teto geográfico | 0,35 | 0,50 | 14,1 | 22% | 26,5 | 60% |
| dose é tratamento | 1,00 | 0,25 | 20,0 | 39% | 37,5 | 88% |
| dose é tratamento | 1,00 | 0,50 | 40,0 | 92% | 75,0 | 100% |

**VPP de equilíbrio**, o VPP que faria o θ̂ observado ser sinal diluído puro
(`|θ̂| / (f·δ)`):

| estimador | θ̂ | f=0,25, δ=80 | f=0,25, δ=150 | f=0,5, δ=80 | f=0,5, δ=150 |
|---|---:|---:|---:|---:|---:|
| DiD simples | −21,9 | 1,09 ✘ | 0,58 | 0,55 | **0,29** |
| Synthetic DiD | −20,2 | 1,01 ✘ | 0,54 | 0,50 | **0,27** |

✘ = acima de 1, impossível.

**Três leituras, e nenhuma é estimação:**

1. **Sob o VPP do Censo, o desenho não tinha como ver o efeito.** O poder fica
   em 11% no máximo, mesmo com metade dos nascimentos expostos e o teto do
   análogo. Para detectar 8,8 g com 80% de poder, o erro-padrão teria de cair
   de 11,9 para ~3,1 g, ou seja, **~14 vezes mais informação**. O Ceará não tem
   14 vezes mais produtores de banana.
2. **O θ̂ de −22 g não é sinal diluído.** Só no canto mais generoso da grade
   (teto geográfico, `f = 0,5`, `δ = 150`) o sinal esperado alcança o θ̂. No
   resto, θ̂ está dentro do ruído: é 1,8 erro-padrão de zero. Ler o θ̂ como
   "efeito atenuado de algo grande" exigiria de cinco a dez dos 17 municípios
   genuinamente tratados, ou mais do que todos com `f = 0,25` e `δ = 80`. O
   Censo diz dois, e a geografia diz no máximo seis a oito.
3. **As duas leituras da §6.8 não são rivais.** A diluição é o *mecanismo* da
   falta de poder, e a consequência prática é forte: **aumentar N sem aumentar
   o VPP não resolve.** Baixar o corte de dose, a via que a §6 declara, traz o
   18º, o 19º e os seguintes, mais serra e mais sertão, e **reduz** o VPP. O
   "encorpar o grupo tratado pioraria" da flag 7 estava certo, e a calibração
   diz quanto.

⚠️ **E o que a calibração não autoriza:** mudar o piso de 15 g, reescrever o
MDE ou tratar `f` como estimado. É aritmética de insumos declarados, útil para
dizer o que o desenho podia ver. Não diz o que o mundo é.

## 8. O que isso muda nas rotas

A alavanca é o **VPP**, não o N. Reordenando o que já existe:

| rota | o que faz com o VPP | estado |
|---|---|---|
| **LAI à ADAGRI** (receituário com modalidade aérea) | **mede** o VPP de 2015–2018 por município, e com ele o ATT sai pontual (`θ/VPP`) | ⬜ minuta pronta; é a de maior valor por esforço agora |
| **Rota 1, Chapada** (CE × RN) | concentra o grupo tratado onde a aplicação aérea existia. Com a revogação, a Chapada cearense tem **dois** municípios genuinamente tratados, e não um — e são justamente os dois que tocam a divisa do RN (doc 15 §8) | ✅ gate rodado (doc 15); ver §8-bis. O poder com dois tratados **precisa ser calculado** antes de investir |
| **Heterogeneidade planície × serra**, dentro do Ceará | previsão falseável: sob a leitura de diluição, o efeito se concentra nos 4 a 6 municípios de planície | 🆕 candidata a **pré-especificação exploratória**. Muda a análise: decisão do orientador |
| **Rota 2** (eCIC, caudas) | **não** mexe no VPP: a distribuição do grupo "tratado" também é mistura. Ganha sinal na cauda, e a diluição continua | inalterada |
| baixar o corte de dose | **reduz** o VPP | ✘ desaconselhada pela calibração |

## 8-bis. Como isto se encaixa no gate da máquina local (doc 15)

O `15-gate-rota1-resultado.md` foi escrito sem os achados deste documento, e
este sem o gate. Juntos, quatro coisas mudam de lugar.

1. **Os dois genuinamente tratados são os dois da divisa.** O script 16 mostrou
   que Limoeiro do Norte e Quixeré, os únicos do grupo com aplicação aérea,
   estão em cima da linha potiguar. O doc 15 lia Limoeiro como "banido desde
   2009", mantendo a flag 0 "exatamente como está". Com a revogação de 2010,
   **os dois são tratados em 2019**. Na Chapada cearense o VPP é ~1, e no
   estado é 2/17.
2. **O G1 reprovado talvez não derrube a Rota 1.** Ele foi desenhado para
   garantir *comparação entre iguais sob regimes diferentes* (doc 11 §3.2): o
   vizinho também pulverizaria por avião, e só o Ceará perderia. Com o RN sem
   aviação, o contraste vira **"aéreo → terrestre" (CE) contra "sempre
   terrestre" (RN)**. Isso é DiD padrão com grupo nunca-tratado, e o regime do
   RN é exatamente o que o Ceará adota depois do ban. O que o DiD exige são
   tendências paralelas, não exposição igual no pré-período. Há duas vantagens
   que o G1 não enxergava:
   - **Pelo Corolário 1, o lado do controle não gera erro de classificação.** O
     município potiguar não é "falso negativo": não foi banido, e pulverizar ou
     não por avião é o estado não tratado dele.
   - **A deriva pós-ban não contamina.** Se o RN seguisse pulverizando por avião
     depois de 2019, a deriva sobre a divisa exporia comunidades cearenses no
     pós-período e atenuaria o efeito. Sem aviação potiguar, isso não acontece.
     A contaminação que resta é a do pré-período: deriva cearense sobre o RN,
     que atenua. É a ressalva de SUTVA já registrada.

   ⚠️ **Isto é leitura para o orientador, não decisão.** Muda o que a Rota 1
   promete: ela deixa de ser "comparação entre iguais" e vira "o Ceará converge
   ao regime do vizinho". E não resolve o poder. São **dois** tratados, e o MDE
   de um desenho com dois clusters tratados precisa ser calculado antes de
   qualquer investimento.
3. **O λ ingênuo do doc 15 (0,882) é o λ da amostra deste documento.** São o
   mesmo número por razões diferentes. 15/17 é a fração do grupo sem aeronave;
   1 − VPP é o λ quando o controle não tem falso negativo. O "λ teto 0,912"
   do doc 15 §5 é a conta populacional que este documento aposenta (§4).
4. **A frase "a partir de λ = 0,5 o efeito implicado continua a ultrapassar o
   MDE" (doc 15 §5) é a leitura que o §7 corrige.** O número está certo, mas a
   comparação não serve: o MDE é do estimando θ, que é o mesmo nas duas
   leituras.

## 9. Arquivos alterados nesta rodada

| arquivo | o quê |
|---|---|
| `scripts/estimate/12_erro_de_classificacao.py` | Corolário 1; λ na amostra (0,882); decil com `ceil`; calibração (`sinal_esperado`, `poder_aproximado`, `vpp_de_equilibrio`, `tabela_calibracao`); nova saída `calibracao_sinal_esperado.csv`; sem a comparação limite × MDE |
| `scripts/data_prep/08_alvos_legislativos.py` | colunas `data_revogacao` e `fonte_revogacao`, preservadas na mescla; semente de Limoeiro com a revogação |
| `scripts/data_prep/09_varre_camaras.py` | aviso: lei achada ≠ lei vigente |
| `scripts/build_panel/05_build_panel.py` | `ban_municipal_revogado_em`, `ban_vigente_em()`, relatório com bans vigentes em 2015 |
| `docs/legislacao/bans-municipais-ce.csv` | as duas colunas; linha de Limoeiro preenchida |
| `tests/test_data_prep.py` | +13 testes desta rodada; com os commits locais, **232** (3 exigem `requirements-geo.txt`) |
| `CLAUDE.md` | flags 0 e 7 |
| `paper/secoes/02`, `04`, `05`, `06` | 17/15 no lugar de 19/17; revogação de Limoeiro. **A argumentação da §6 não foi reescrita** (§10) |
| `docs/auditoria-mensuracao-do-tratamento.md`, `docs/ars/12-*.md` | notas de correção datadas, sem apagar o texto original |
| `docs/legislacao/README.md`, `docs/referencias-verificadas.md`, `docs/ars/14-*.md` | registros |

## 10. O que falta, e de quem é

**Da máquina local:**

1. `git pull origin claude/exciting-noether-17cl74` antes de continuar: esta
   rodada foi mesclada **sobre** os cinco commits locais. Os conflitos, em
   `CLAUDE.md`, no script 12, nos testes, no paper e em três documentos, foram
   resolvidos preservando os dois lados: `area_ha_media`, `--fonte ftp` e o
   sufixo das UFs, e também o Corolário 1, o λ da amostra e a revogação.
2. **Localizar a lei revogadora de Limoeiro** (§5): `python
   scripts/data_prep/09_varre_camaras.py --revogacao` (§11.2).
3. **O poder de um desenho com dois tratados** (Limoeiro e Quixeré contra a
   Chapada potiguar), antes de qualquer investimento na Rota 1 (§8-bis):
   `make mde-desenhos` (§11.1).

**Do orientador:**

1. Aceitar a releitura da §6.8: a diluição é o mecanismo da falta de poder, e
   a via "baixar o corte" sai. Isso muda a argumentação do paper; não reescrevi.
2. Pré-especificar, ou não, a heterogeneidade planície × serra como
   exploratória.
3. Decidir o que o Ensaio 1 reporta como resultado principal: o nulo com os
   limites do Corolário 1 e a calibração, em vez de "desenho sem poder".

## 11. As duas ferramentas para a máquina local

*Acrescentado na mesma noite, depois dos commits locais do Crossref e do DOFET.*

### 11.1 `make mde-desenhos` — quanto poder cada grupo tratado compra

`scripts/estimate/13_mde_desenhos.py` calcula o MDE de seis desenhos
candidatos com **só o pré-período** (2015–2018). Nada é estimado, e o pós-ban
não entra: um teste trava isso.

| desenho | tratados | controles | VPP |
|---|---|---|---|
| `decil17_vs_ce_outros` | decil da banana (17) | resto do CE | 2/17 — **benchmark** |
| `decil17_vs_ce_dose_zero` | decil (17) | CE de dose zero (07/08) | 2/17 |
| `chapada2_vs_ride_rn` | Limoeiro + Quixeré | RIDE potiguar (21) | ~1 |
| `chapada2_vs_rn` | Limoeiro + Quixeré | todo o RN | ~1 |
| `quixere_vs_ride_rn` | só Quixeré | RIDE potiguar | ~1 |
| `aeronave_ce_vs_ce_sem` | os 7 com aplicação aérea | CE sem | ~1 (Rota 3) |

Duas contas por desenho. A **agrupada** é a do script 01, a que deu os 33,4 g.
A **por unidade** dá a cada município a própria variância, `σ²(1/N_ini +
1/N_fim) + τ²`. Com σ estimado da variação mês a mês e τ pelo método do script
07, é a que vale com poucos tratados. O poder sai contra `θ = VPP · f · δ`, a
calibração do §7.

**Como ler, em ordem:**

1. **O benchmark primeiro.** A coluna agrupada de `decil17_vs_ce_outros` tem de
   reproduzir ~33,4 g. Se não reproduzir, pare: o painel difere do que gerou o
   MDE do paper, e os outros números não são comparáveis.
2. **Depois `chapada2_vs_ride_rn`**, contra o sinal de `f · δ`. É o número que
   decide se a Rota 1 concentrada vale o investimento.
3. **`aeronave_ce_vs_ce_sem`** mostra o que a Rota 3 compraria dentro do
   próprio estado, tratando pelo método e não pela cultura.

⚠️ Num painel **sintético** com a forma do real (184 + 167 municípios, σ ≈ 550
g, τ ≈ 15 g), a ordem foi: o decil diluído com poder de no máximo ~14%; a
Chapada com dois tratados entre 13% e 86%; os 7 pelo método entre 26% e 100%,
conforme `f` e `δ`. **Não é resultado**, é a mecânica: com VPP ≈ 1, até dois
tratados podem comprar mais poder que dezessete diluídos. Os números reais
saem do painel `__uf23-24`. E escolher desenho continua sendo decisão do
orientador.

⚠️ É a aproximação normal. Com 1 ou 2 tratados, a inferência de verdade seria
Conley–Taber, com a distribuição tirada dos controles.

### 11.2 `09_varre_camaras.py --revogacao` — a lei revogadora de Limoeiro

Para cada `confirmado` do registro, procura as leis **posteriores** que citam
o número da lei achada (as duas grafias, "1.478" e "1478") ou que revogam algo
do tema. Na plataforma A, busca `REVOGA` e variantes mais o próprio número; na
B, lê o acervo inteiro, sem o filtro de tema e de ano que a varredura aplica.

```powershell
python scripts/data_prep/09_varre_camaras.py --revogacao                    # só relata
python scripts/data_prep/09_varre_camaras.py --revogacao --gravar-revogacao
```

Só grava a candidata **inequívoca**, a única que cita o número E fala em
revogar, e troca `fonte_revogacao` de "secundaria" para "primaria". "Altera a
Lei nº 1.478" cita e não revoga; duas candidatas fortes não são escolhidas.
Nesses casos o relatório lista as candidatas para conferência à mão.

Se a busca não achar nada, a alternativa manual é o **export do acervo** da
Câmara: `camaralimoeirodonorte.ce.gov.br/leis/export` (CSV, JSON ou XLS). Aí
basta procurar "1.478" nas leis de 2010.
