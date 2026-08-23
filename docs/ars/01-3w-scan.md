# Mapa WHY / HOW / WHAT dos papers-base

*ARS `deep-research` — modo `three-way-scan`. Etapa 1 de 3 do começo de pesquisa.*
*Fonte: pasta do Drive `17ftiijOfJFyq0b06kHk1ZbCuQ78FUrKR`. Leitura em 2026-08-23.*

Este documento é **diagnóstico**, não decisório. Ele organiza o que os papers
fazem e o que transfere para o objeto cearense. Não escolhe pergunta de
pesquisa, rota de identificação nem cultura-âncora — isso é a Etapa 2.

## Nota de proveniência (leia antes de citar)

Toda afirmação abaixo vem do PDF correspondente na pasta. Três ressalvas que
mudam como citar:

1. **DRS — versão lida é o working paper, não o publicado.** O PDF na pasta é
   *LACEA Working Paper Series No. 0024, dezembro de 2020*. A referência da sua
   lista é *Review of Economic Studies* 90(6):2943–2981 (2023). Magnitudes e
   especificações podem ter mudado na revisão. **Conferir os números contra o
   publicado antes de citar qualquer coeficiente.**
2. **Reynier & Rubin — volume divergente.** O cabeçalho do PDF diz "PNAS 2025
   Vol. 121 No. 3 e2413013121"; a sua lista de leitura diz 122(3). O DOI
   (10.1073/pnas.2413013121) é o que manda. Conferir o volume antes da versão
   final.
3. **`2023_tese_lmgreges.pdf` — NÃO LIDO.** 54 MB, sem camada de texto
   (PDF digitalizado); a extração devolve string vazia. Não sei o que este
   documento contém e não vou adivinhar. Se importar, dá para rodar OCR — é
   caro, mas viável.

Os outros sete arquivos foram lidos. Do CGS, do Practitioner's Guide, do DRS e
do Reynier & Rubin li abstract, introdução e as seções de identificação, não o
paper inteiro; de Lichtenberg–Parker–Zilberman e da dissertação da Chapada do
Apodi li o texto completo disponível; da ADI li o texto integral da petição.

---

## Os papers, um a um

### 1. Dias, Rocha & Soares — *Down the River* (LACEA WP 0024, 2020; publicado ReStud 2023)

**WHY.** Regulação de agrotóxico é problema-livro de externalidade, mas a
externalidade é difícil de medir: adoção de tecnologia agrícola é endógena ao
desenvolvimento local, e a tecnologia mexe em renda por vários canais ao mesmo
tempo. O foco é a **toxicidade subclínica** — população que não é envenenada
diretamente, mas ingere resíduo pela água.

**HOW.** Quatro peças encaixadas: (i) a mudança regulatória que liberou semente
transgênica no Brasil; (ii) o ganho *potencial* de produtividade municipal com
soja TH (instrumento de aptidão, seguindo Bustos et al. 2016); (iii) a
complementaridade forte entre glifosato e semente TH; (iv) **a direção do fluxo
d'água dentro da bacia**. O instrumento é lido não como variação no próprio
município, mas como variação exógena no uso de glifosato *nas outras áreas que
compartilham a água*. Municípios 2000–2010, dados de nascimento e óbito do MS,
bacias da ANA.

**WHAT.** Deterioração dos desfechos a jusante, **nada a montante**. O aumento
médio de glifosato eleva a mortalidade infantil em 0,88 por mil (≈5% da média;
0,45 óbito/município/ano; 503 óbitos/ano no total). Também sobem prematuridade
e baixo peso. 75% do efeito vem de duas causas — afecções perinatais (56%) e
respiratórias (19%). Validações de mecanismo: efeito só aparece com chuva
suficiente na estação de aplicação e solo mais erodível; maior em municípios de
captação superficial; decai com a distância; **maior para nascimentos com
exposição intrauterina mais longa à estação de aplicação**. Falseamentos:
primeiro estágio com milho ≈ 0; event study pré-autorização ≈ 0.

**Transfere / não transfere.** Transfere: a estrutura montante/jusante, o
casamento com SINASC, o teste de mês de nascimento (é por isso que o painel do
repo é município × **mês**, não ano), e a bateria de mecanismo. **Não
transfere direto**: DRS estuda *molécula* (glifosato) chegando por *água*, com
uso de agrotóxico *aumentando*. No Ceará o objeto é *método* (aérea) sendo
*removido*, e o canal aéreo — deriva — não passa pela bacia. Além disso, a
contaminação documentada na Chapada do Apodi envolve o **Aquífero Jandaíra**
(subterrâneo), e a lógica montante/jusante é de água superficial.

---

### 2. Reynier & Rubin — *Glyphosate exposure and GM seed rollout unequally reduced perinatal health* (PNAS, DOI 10.1073/pnas.2413013121)

**WHY.** Glifosato é o herbicida mais usado do mundo e o efeito sobre saúde
humana segue em disputa regulatória. Ciência e política não fecharam.

**HOW.** Duas abordagens complementares: DiD reduzida (alta vs. baixa aptidão,
antes vs. depois de 1996) e 2SLS instrumentando intensidade de glifosato por
**aptidão × dummies de ano**. A construção do instrumento importa e é o que o
`CLAUDE.md` empresta: percentil de *attainable yield* = **diferença de
rendimento atingível entre os cenários de alto e de baixo insumo** do FAO-GAEZ,
para milho, soja e algodão; reescala cada cultura a percentil nacional, toma o
**máximo** entre as três, reescala de novo, normaliza em [0,1]. Amostra
restrita a *condados rurais*. Pré-período 1990–1995, pós 2005–2010, **jogando
fora a fase de transição**.

**WHAT.** Introdução de semente TH + glifosato reduziu peso ao nascer e duração
gestacional. Efeito ao longo de toda a distribuição, mas **12 vezes maior no
decil de menor peso esperado** que no maior.

**Transfere / não transfere.** Transfere: a receita GAEZ (e note — é a
*diferença alto-menos-baixo insumo*, não o rendimento atingível puro), o event
study com aptidão × ano, a heterogeneidade na cauda baixa, e a disciplina de
descartar a fase de transição. **Não transfere**: a aptidão GAEZ resolve a
endogeneidade de *onde se planta a cultura*; ela não diz nada sobre *como se
aplica o agrotóxico*. No Ceará o tratamento é o método de aplicação — o
instrumento cobre metade do problema, e essa é uma lacuna a declarar, não a
esconder.

---

### 3. Callaway, Goodman-Bacon & Sant'Anna — *Difference-in-Differences with a Continuous Treatment* (draft de 26/01/2024)

**WHY.** DiD com dose é comum e conceitualmente útil, mas a econometria
disponível dava pouca orientação fora de casos específicos.

**HOW e WHAT (é paper de método — o "achado" são os resultados de identificação).**
Quatro coisas que mudam o desenho do Ensaio 1:

1. **Dois parâmetros diferentes, não um.** *Level treatment effect* = efeito de
   receber a dose *d* versus não receber. *Causal response* (ACR) = efeito de um
   aumento marginal da dose. Com tratamento binário coincidem; com dose contínua,
   **não**. E exigem hipóteses diferentes.
2. **A curva dose-resposta custa mais caro que o nível.** ATT(d) é identificado
   sob paralelismo padrão, igual ao caso binário. Mas comparar *entre* doses —
   que é exatamente o que uma curva dose-resposta faz — exige **strong parallel
   trends**: a trajetória dos municípios de dose baixa tem que representar como
   os de dose alta teriam evoluído se tivessem recebido a dose baixa. Sem isso,
   a comparação entre doses vem contaminada por um termo que os autores chamam
   de **viés de seleção**.
3. **TWFE com `D_i × Post_t` não tem interpretação limpa** — nem com dois
   períodos. Na decomposição em efeitos de nível os pesos **somam zero** (logo
   não é média de efeito), com peso negativo nos municípios de dose abaixo da
   média. Na decomposição em ACR os pesos somam um e são não-negativos, mas
   entra o termo de viés de seleção, e os pesos não seguem a distribuição da
   dose.
4. **O resumo seguro é binário.** Para sumarizar efeitos de nível entre tratados,
   os autores mostram que basta comparar a variação média dos tratados (qualquer
   dose positiva) com a dos não tratados — ou seja, **um DiD binário com dummy
   de dose > 0**. Resumir ACR exige derivada média com pesos da densidade da dose.

Na aplicação a Acemoglu–Finkelstein (1983, Medicare) eles acham ACR
**negativo** para a maior parte das doses positivas e leem isso como suspeita
sobre o strong parallel trends — ou sobre o modelo, ou ambos.

**Transfere / não transfere.** Transfere inteiro: é o estimador primário do repo
e o desenho é exatamente "todo mundo tratado ao mesmo tempo, o que varia é a
dose". **A tensão a resolver**: o `CLAUDE.md` fixa como parâmetro-alvo "como o
efeito do ban varia com a intensidade" — isto é, a **curva**, que é o objeto que
exige a hipótese mais forte. E o strong parallel trends *restringe
heterogeneidade de efeito*, que é justamente o que um estudo de dose-resposta
quer documentar. Não é contradição fatal, mas é uma escolha que precisa ser
feita com os olhos abertos e defendida na banca.

---

### 4. Baker, Callaway, Cunningham, Goodman-Bacon & Sant'Anna — *Difference-in-Differences Designs: A Practitioner's Guide* (JEL 2026, 64(2):498–557)

**WHY.** DiD virou o desenho mais comum das ciências sociais, mas a prática fora
do 2×2 é ad hoc, e regressão simples pode dar magnitude enganosa e até **sinal
errado**.

**HOW.** Propõe um enquadramento único: todo DiD complexo é agregação de
comparações **2×2** entre um conjunto cuja exposição muda e outro cuja não muda.
Estime cada bloco 2×2, depois agregue. Identificação vem do paralelismo simples
exigido por cada bloco.

**WHAT.** O termo que organiza tudo é **forward engineering**: fixe o
parâmetro-alvo, derive a técnica — em oposição ao *reverse engineering*, que
parte de uma especificação familiar e depois pergunta sob que hipóteses ela tem
interpretação causal. A vantagem prática: duas estimativas passam a ser
distinguíveis pelas hipóteses de identificação, não por "robustez".

**Transfere / não transfere.** Transfere como **vocabulário e grade de
diagnóstico** — e vale notar que a lógica de *forward engineering* que já está no
`CLAUDE.md` vem daqui. **Não transfere como estimador**: o paper foca pesos,
covariáveis e *timing* escalonado; tratamento contínuo/multivalorado está no
apêndice suplementar. Para o Ceará ele é a régua, não a ferramenta.

---

### 5. Lichtenberg, Parker & Zilberman — *Marginal Analysis of Welfare Costs of Environmental Policies: The Case of Pesticide Regulation* (AJAE 70(4), 1988)

**WHY.** Avaliação de política precisa de eficiência **e** distribuição, com
dados que existem de fato (preço, quantidade, elasticidades) e em prazo curto.

**HOW.** Análise marginal: dado o efeito da política sobre custo e/ou
produtividade (estimado por agrônomo, não por econometrista), diferencia o
sistema de equilíbrio e recupera mudanças em preço, quantidade e excedentes por
grupo. Aplicação: cancelar o registro do inseticida paration etílico em amêndoa,
ameixa e ameixa-seca.

**WHAT.** Três resultados com dentes:

- **Quem não usava o agrotóxico ganha com a proibição.** Os ganhos dos não-usuários
  somam 24–32% das perdas dos usuários no caso-base, e podem chegar a **80–90%**
  quando a demanda é inelástica.
- **O consumidor paga a maior parte.** ~40% da perda de excedente social nos
  casos de ameixa; pode chegar a **75–90%** com demanda inelástica.
- **Em cultura de exportação, o consumidor estrangeiro carrega boa parte do custo.**
  Em amêndoa, consumidores estrangeiros perdem 30% *mais* que os domésticos.

Sensibilidade: a elasticidade de **oferta** pesa ~1/3 mais que a de demanda na
razão ganho/perda, e ~40% mais na fatia do consumidor. E o *partial budgeting*
(a conta ingênua) superestima a perda dos usuários em 15–30%.

**Transfere / não transfere.** Transfere e é subestimado no seu esboço:
**melão e banana do Ceará são culturas de exportação**, então o resultado
"estrangeiro paga parte do custo" é diretamente aplicável e é um argumento
político forte. E o resultado "não-usuário ganha" é uma **predição testável com
o PAM**: municípios sem pulverização aérea deveriam ganhar com o ban por efeito
de preço. **Custo escondido**: o método exige elasticidades de oferta e demanda
— que **não estão** na lista de fontes do `CLAUDE.md`. Isso é uma dependência de
dados do Ensaio 2 ainda não provisionada.

---

### 6. Aguiar, A. C. P. — *Más-formações congênitas, puberdade precoce e agrotóxicos: uma herança maldita do agronegócio para a Chapada do Apodi (CE)* (dissertação, Mestrado em Saúde Pública, UFC, 2017; orientação Raquel Rigotto)

**WHY.** Moradores da comunidade de **Tomé** (Chapada do Apodi) denunciavam
aumento de más-formações congênitas e puberdade precoce nas crianças. É a
comunidade do Zé Maria do Tomé.

**HOW.** Estudo de casos múltiplos, 8 famílias (5 más-formações, 3 puberdade
precoce): história clínica, exame físico, caracterização da exposição ambiental
e ocupacional, exames toxicológicos em sangue e urina, e análise da água de
consumo dos domicílios.

**WHAT.** Organoclorados detectados em 11 de 19 amostras de sangue; metabólitos
de piretroides em 7 de 17 amostras de urina; **em 6 de 7 domicílios a água de
consumo tinha ao menos um ingrediente ativo de agrotóxico**. Dois dados de
mecanismo que valem para o desenho:

- **A pulverização aérea local era em banana, com fungicidas.** Literalmente:
  "a prática da pulverização aérea com **fungicidas de classes toxicológicas 1 e
  2 nos extensos cultivos de banana** inseridos entre as comunidades rurais".
- **A física da deriva.** Citando Pignati/EMBRAPA: só **32%** do que se
  pulveriza fica na planta; **19% se dispersa pelo ar** atingindo o entorno; e
  **49% fica no solo**. É a repartição quantitativa dos dois canais.
- Escala: ~4 milhões de litros de calda "extremamente tóxica ou muito tóxica"
  em 2000–2010 na região, **só por pulverização aérea** (Teixeira 2011).

**Transfere / não transfere.** Transfere como **evidência de mecanismo e como
fixador de desfecho**. E entrega um desafio ao enquadramento do esboço: o
esboço trata glifosato como "caso central", mas a evidência local aponta
**fungicidas, organoclorados e piretroides** — não glifosato. Se o ban de método
morde onde a aplicação era aérea, e a aplicação aérea local era de fungicida em
banana, então o "químico emblemático" do Ensaio 1 talvez não seja o glifosato.
**Não transfere** como identificação: n=8, sem contrafactual. É o tipo de
evidência correlacional que o seu desenho existe para melhorar.

---

### 7. ADI do PSOL contra a Lei 19.135/2024 (ADI 7794 conforme o esboço) — petição inicial

**WHY.** Contestar a exceção de drones como inconstitucionalidade formal
(competência da União sobre navegação aérea) e material (meio ambiente, saúde,
precaução, não-retrocesso).

**HOW.** Peça jurídica, não estudo. Vale como **fonte primária de cronologia e
de parâmetros** — e como bibliografia comentada do lado da saúde.

**WHAT** (o que ela estabelece factualmente):

- **A data do ban é 08 de janeiro de 2019.** "Em 08 de janeiro de 2019, foi
  acrescentado à referida norma o artigo 28-B, pela Lei nº 16.820/2019", com
  link para a fonte oficial (ADAGRI-CE). **Isso contradiz o `CLAUDE.md`, que
  hoje diz "jun/2019".**
- **Aprovação na ALECE em 18 de dezembro de 2018**, por unanimidade, após 4 anos
  de tramitação do PL 18/2015. Relevante para antecipação.
- **O ban não é só agrícola**: o §2º proíbe também dispersão aérea para controle
  vetorial, inclusive de doenças virais.
- **Texto integral da Lei 19.135/2024**: drones permitidos, mas com orientação
  técnica de agrônomo e ART; **até 2 m acima da copa**; **vento < 10 km/h**;
  **30 m de escolas, hospitais, praças, APA e APP**; multa de 15 mil UFIRCEs.
  Vigência na data da publicação (19/12/2024).
- **Banana de novo**: "Em período anterior à vigência da lei, a pulverização
  aérea foi **amplamente utilizada na produção de banana**", com contaminação da
  água consumida (24 amostras, todas com resíduo de ingredientes ativos) e do
  **Aquífero Jandaíra**.
- FUNCEME sobre regime de ventos do Ceará — insumo para um desenho à la Rangel
  & Vogl.

**O estudo que o PSOL cita — achado.** O seu esboço pedia para localizar "um
estudo que já comparou efeitos à saúde entre cidades com pulverização aérea e
cidades de agricultura familiar no interior do Ceará". Na petição é a nota 22:
mortalidade por neoplasia **38% maior** em **Limoeiro do Norte, Quixeré e
Russas** frente a **12 municípios de população similar onde predomina
agricultura familiar tradicional**, com dados secundários de **2000–2010** →
**Rigotto, R. M. et al. (2013), *Rev. Bras. Epidemiologia* 16:763–773**. É o
item [3] da sua própria lista de leitura. O desenho dele — 3 municípios
expostos contra 12 pareados por população — é o ancestral direto de um
PSM+DiD.

---

## Síntese cruzada

### WHY comum

Os cinco papers empíricos partem do mesmo lugar: **a externalidade do agrotóxico
sobre quem não decide nada** — não o trabalhador que aplica, mas a população do
entorno, e em particular o feto. Todos escolhem desfecho de nascimento pela
mesma razão: a janela de exposição é datável e o feto é sensível. Isso é a
convergência mais forte do conjunto, e legitima o desfecho primário do repo.

### HOW divergente

A divergência não é de estimador — é de **onde mora a variação exógena**:

| Paper | Variação vem de | Canal isolado |
|---|---|---|
| DRS | aptidão × mudança regulatória × **fluxo d'água** | água superficial |
| Reynier & Rubin | aptidão GAEZ × **timing** da semente TH | ambiente (não separa) |
| Rigotto et al. 2013 | **pareamento** de municípios por população | nenhum (comparação bruta) |
| CGS / Ceará | **dose pré-ban**, sem variação de timing | nenhum ainda |

O Ceará é o único caso em que **não há variação de timing** — a lei é estadual e
simultânea. Isso mata os desenhos escalonados como estimador principal e joga
todo o peso na dose. É a restrição que amarra, e é por isso que a Tarefa 1 do
repo vem antes de tudo.

### WHAT mais forte

O achado mais robusto do conjunto, e o mais transferível, é **DRS**: efeito a
jusante, zero a montante, com bateria de mecanismo (chuva, erodibilidade,
captação superficial, distância, timing gestacional) e falseamento (milho, event
study pré-autorização). É forte porque o placebo é interno ao desenho — a
mesma variação, aplicada rio acima, não produz efeito. **Reynier & Rubin** vem
logo atrás e entrega o que DRS não tem: heterogeneidade explícita ao longo da
distribuição do desfecho (12× no decil inferior).

### Lacuna não resolvida

**Ninguém avaliou um banimento de método de aplicação com identificação causal.**
DRS e Reynier & Rubin avaliam a *expansão* de uma molécula. Camacho & Mejía
(citado no esboço, não na pasta) avalia um *programa* de pulverização aérea, não
sua proibição. Rigotto et al. avaliam *estado do mundo*, sem política. A
literatura de instrumento (LPZ, Weitzman) modela o cancelamento de registro de
**substância**.

O caso cearense é: **remoção de um método, mantendo as moléculas legais**. Isso
é a lacuna, e é onde está o valor da tese. É também, honestamente, onde está o
risco: o efeito só aparece se a substituição aéreo→terrestre mudar de fato a
exposição da população — e não há paper na pasta que estabeleça isso.

---

## Tensões com o desenho que está hoje no `CLAUDE.md`

Quatro, em ordem de quanto machucam:

1. **A data do ban está errada no `CLAUDE.md`.** Está "jun/2019"; a ADI
   estabelece **08/01/2019**, com aprovação na ALECE em 18/12/2018. Muda o corte
   do event study, a janela pré-ban do PAM e a retroprojeção gestacional (uma
   criança nascida em out/2019 foi concebida *antes* da lei). Correção pendente
   da sua aprovação.
2. **O parâmetro-alvo é o mais caro dos dois.** O `CLAUDE.md` mira a *curva*
   dose-resposta; CGS mostram que a curva exige **strong parallel trends** e que
   o nível — DiD binário com dummy de dose > 0 — sai sob paralelismo comum. Há
   uma escada aqui: nível primeiro, curva depois, cada degrau com sua hipótese
   declarada.
3. **A cultura-âncora tem três fontes convergindo, e não é a que o `CLAUDE.md`
   antecipa.** A dissertação da Chapada do Apodi diz que a aérea local era
   **fungicida em banana**; a ADI diz que a aérea foi "amplamente utilizada na
   produção de banana"; e a nota técnica de Cavalcante (2023, item [4] da lista)
   diz que a banana **cresceu** depois do ban. O flag 1 do `CLAUDE.md` alertava
   contra hard-codar algodão ou "fruticultura" — o alerta continua valendo, e
   agora tem um candidato específico a testar no PAM. Continua hipótese, não
   escolha.
4. **O poder estatístico pode ser pior do que o flag 4 supõe.** O estudo do
   PSOL compara **3 municípios** contra 12. Se a pulverização aérea estava
   concentrada em três municípios de 184, a dose alta tem suporte
   quase inexistente, e `share_top5_muni` no script 01 vira o número que decide
   o destino do desenho — não `cv_positivos`.

E uma nota de método que não é tensão, é oportunidade: **LPZ prevê que quem não
pulverizava ganha com o ban**, por efeito de preço. Isso é testável no PAM, é o
espelho econômico do efeito de saúde, e amarra o Ensaio 1 ao Ensaio 2 por dentro
em vez de por transição retórica.

---

## O que fica em aberto para a Etapa 2 (diálogo socrático)

Registro sem responder — a Etapa 2 é socrática estrita, e estas são suas de
responder, não minhas:

- A pergunta do esboço tem três desfechos (saúde, água, atividade agrícola).
  Uma tese de dois ensaios aguenta os três no Ensaio 1?
- Das quatro rotas (A sintético, B dose-resposta, C montante/jusante, D drones
  2024), qual é espinha e quais são robustez?
- Nível ou curva? (CGS §2 acima — é escolha de parâmetro-alvo, com preço de
  hipótese.)
- Se o canal local é aéreo e o aquífero é subterrâneo, o que sobra do template
  montante/jusante do DRS?
- Se a aérea local era fungicida, o glifosato continua sendo o "caso central" do
  Ensaio 1?
- Que resultado no PAM te faria abandonar o desenho de dose?

---

## Referências desta pasta

- Aguiar, A. C. P. (2017). *Más-formações congênitas, puberdade precoce e agrotóxicos: uma herança maldita do agronegócio para a Chapada do Apodi (CE)*. Dissertação, Mestrado em Saúde Pública, UFC.
- Baker, A., Callaway, B., Cunningham, S., Goodman-Bacon, A. & Sant'Anna, P. H. C. (2026). Difference-in-Differences Designs: A Practitioner's Guide. *Journal of Economic Literature* 64(2):498–557. DOI 10.1257/jel.20251650.
- Callaway, B., Goodman-Bacon, A. & Sant'Anna, P. H. C. (2024). *Difference-in-Differences with a Continuous Treatment*. Draft de 26/01/2024 (primeiro no arXiv em 06/07/2021).
- Dias, M., Rocha, R. & Soares, R. R. (2020). *Down the River: Glyphosate Use in Agriculture and Birth Outcomes of Surrounding Populations*. LACEA Working Paper Series No. 0024. [Publicado: *Review of Economic Studies* 90(6):2943–2981, 2023 — conferir números contra o publicado.]
- Lichtenberg, E., Parker, D. D. & Zilberman, D. (1988). Marginal Analysis of Welfare Costs of Environmental Policies: The Case of Pesticide Regulation. *American Journal of Agricultural Economics* 70(4):867–874.
- PSOL. *Ação Direta de Inconstitucionalidade com pedido de medida cautelar* contra a Lei estadual do Ceará nº 19.135/2024. (ADI 7794 conforme o esboço.)
- Reynier, E. & Rubin, E. Glyphosate exposure and GM seed rollout unequally reduced perinatal health. *PNAS*. DOI 10.1073/pnas.2413013121. [Volume a conferir: cabeçalho do PDF diz 121(3); sua lista diz 122(3).]
- `2023_tese_lmgreges.pdf` — **não lido** (PDF sem camada de texto).

**Citada por terceiros, não lida por mim** (aparecem acima porque a ADI ou a
dissertação as citam; **verificar antes de usar**): Rigotto et al. (2013), *Rev.
Bras. Epidemiologia* 16:763–773; Barbosa et al. (2019), *Ciência & Saúde
Coletiva* 24:1563–1570; Pignati, Machado & Cabral (2007); Teixeira (2011); Vaz
de Moura & Vieira Cavalcante (2023), *Estudos Sociedade e Agricultura* 31(2);
Cavalcante (2023), nota técnica UFRN sobre banana; CNDH Resolução 24/2022.
