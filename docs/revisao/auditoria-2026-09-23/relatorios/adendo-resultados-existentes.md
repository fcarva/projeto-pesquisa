# Adendo quantitativo: reconciliação dos resultados existentes

**23/09/2026 — auditoria assistida por IA.** Fonte: repositório fornecido pelo usuário em `C:/Users/DELL/Documents/projeto-pesquisa/projeto-pesquisa`, HEAD **4ab2c93971fa64d03393405428f6518950c9dada**. Esta é uma versão distinta do clone da auditoria bibliográfica. Os arquivos originais foram apenas lidos. As reconstruções deste adendo usam Python, médias explícitas e funções isoladas dos scripts 13/14; **não executei R nem a replicação geral dos scripts 04/09**. A nova inferência produzida pelo coordenador deve ser consultada em seu relatório próprio.

**Resultado principal:** o −36,19 g foi reproduzido como contraste **169 municípios com dose positiva contra 14 controles filtrados por GAEZ**, pré jan/2015–dez/2018 e pós out/2019–dez/2022. O MDE 33,4 g não corresponde a essa amostra nem à amostra 17×14 dos estimadores binários. O calendário salvo usa CE+RN, com **7×344**, e não a comparação interna do Ceará. Os CSV de placebo SPT não podem ser usados como placebos exclusivamente pré-ban, por falha de filtragem temporal confirmada no código.

## 1. Painel, tratamento e filtros efetivamente encontrados

O painel principal tem **17.664 células**, **184 municípios**, **96 meses**, de janeiro/2015 a dezembro/2022; soma **1.001.709 nascimentos**. Dez células não têm peso médio observado. Todas as linhas trazem `fonte=real`. Esse rótulo, sozinho, não substitui a auditoria da aquisição, que não é objeto deste adendo.

Há **169** municípios de dose positiva, **15** de dose zero e **17** no decil superior entre produtores. O percentil 75 estadual de aptidão é **0,4825389551**. A definição 4 exclui do zero o município **230523**, de aptidão **0,540605**: restam **14** controles. Não se trata de incorporar ao controle todos os municípios de baixa aptidão; é retirar um município do grupo inicialmente definido por área zero.

O código de `03_contdid.R` faz média simples dos pesos médios mensais dentro de cada município/período. Depois, o agregado usa pesos municipais iguais. Portanto ele não é a média individual de efeito sobre bebês e tampouco usa peso proporcional ao número de nascimentos. A variável `share_gestacao_pos_ban` aparece no rótulo de saída, mas o contraste colapsado é implementado por **cortes de calendário**, não pela regressão nessa fração.

No contraste principal, descartam-se janeiro–setembro/2019: nove meses, **1.656 células** do painel original. O pós tem **39 meses**, dos quais **24 pertencem a 2020–2021**. Assim, os anos pandêmicos compõem **61,5% dos meses pós**. Não há exclusão da pandemia na execução codificada.

## 2. Reconstrução exata do nível reportado

Reconstruí `Δ_i = média pós_i − média pré_i` e então `média(Δ_i|dose>0) − média(Δ_i|controle)`. Os resultados são:

| Construção | Tratados × controles | Contraste reconstruído |
|---|---:|---:|
| Área zero, pós out/2019 | 169×15 | **−35,329099 g** |
| Área zero + filtro GAEZ, pós out/2019 | 169×14 | **−36,192369 g** |
| Decil superior + filtro GAEZ, pós out/2019 | 17×14 | −24,213715 g |
| Decil superior + filtro GAEZ, pós jan/2019 | 17×14 | **−21,851818 g** |

Os dois primeiros reproduzem os valores −35,33 e −36,19 do manuscrito. O último reproduz o DiD simples salvo em `synthdid__peso_medio.csv`. A diferença entre −24,21 e −21,85 vem da inclusão das coortes de transição em 2019, mantidos os mesmos grupos. Assim, o DiD simples reportado ao lado de SDID não usa a mesma janela gestacional do agregado CGS.

A média dos 169 valores de `estimativa` no CSV da curva de nível também coincide numericamente com −36,192369. Isso confirma o ponto, mas **não recupera o erro-padrão do agregado**: os pontos da curva são correlacionados, e sua média de erros-padrão não é o erro-padrão da média. O script 03 imprime o agregado e sua inferência; os CSV fornecidos preservam as curvas e não uma linha autônoma com todos os campos do agregado. O erro-padrão 15,47 e IC [−66,51;−5,87] estavam no texto, mas sua reprodução pelo bootstrap de R cabe à execução separada do coordenador.

Como verificação aritmética independente, um contraste de médias com variância de Welch dá **SE 15,4068** para 169×14 e IC t de Welch **[−69,1504;−3,2343]**. Para 169×15, SE **14,4239** e IC **[−65,9473;−4,7109]**. Esses são diagnósticos sob independência entre municípios, não correção da identificação ou garantia contra dependência espacial. Mostram, contudo, que o intervalo negativo do manuscrito não é automaticamente anulado pelo critério de MDE.

### Sensibilidades de calendário e agregação — novas, exploratórias

Estas contas foram explicitamente reconstruídas e **não existiam como resultados confirmatórios**:

| Variante do agregado 169×14 | Estimativa | SE de Welch | IC t de Welch |
|---|---:|---:|---:|
| Pós desde out/2019, original | −36,1924 | 15,4068 | [−69,1504;−3,2343] |
| Pós desde jan/2019 | −33,7163 | 15,2814 | [−66,4348;−0,9978] |
| Pós out/2019, excluindo 2020 e 2021 | −36,1278 | 22,2524 | [−83,8528;+11,5972] |
| Médias por bebê dentro do município/período, municípios igualmente ponderados | −36,5512 | 15,4769 | [−69,6878;−3,4147] |

Excluir a pandemia quase não altera o ponto do agregado, mas deixa apenas out–dez/2019 e 2022 no pós e aumenta bastante a incerteza. Não é evidência de ausência de confusão pandêmica: a seleção de meses também muda sazonalidade e precisão. A última linha pondera meses dentro de município; **não** passa a ponderar municípios por população.

## 3. Curvas CGS: nível e derivada contam histórias estatísticas distintas

| CSV existente | Média das estimativas | Pontos com banda abaixo de zero | Pontos com banda acima de zero |
|---|---:|---:|---:|
| Level, peso, d0-1 | −35,329099 | 132/169 | 0 |
| Level, peso, d0-4 | −36,192369 | **133/169** | 0 |
| Slope, peso, d0-1 | −2.946,760531 | 0/169 | 0 |
| Slope, peso, d0-4 | −2.946,760531 | **0/169** | 0 |
| Level, óbito fetal, d0-4 | aproximadamente +0,000176 | 1/169 | 0 |
| Slope, óbito fetal, d0-4 | −0,520877 | 0/169 | 0 |

O crítico uniforme gravado para nível/peso/d0-4 é **4,384405**; para slope/peso/d0-4, **4,344838**. A banda do nível fica negativa em 133 pontos, entre doses aproximadamente 0,000419 e 0,667365. A frase “nenhum dos 169 pontos exclui zero” é correta para a **derivada**, não para a curva de nível. Tampouco a faixa de nível é literalmente plana: no d0-4 as estimativas variam de **−59,0923 a −11,3361 g**.

Esse quadro não transforma as bandas em inferência validada. Permanece a questão técnica da propagação da incerteza do grupo zero na rota CCK, apontada no parecer de identificação. Os números acima auditam **o conteúdo dos arquivos**, não a validade final do procedimento.

## 4. SDID, HonestDiD, OLS e Holm não são confirmações do mesmo parâmetro

### Resultados binários existentes

O arquivo SDID usa **17 tratados, 14 doadores, quatro anos pré e quatro pós**. O código colapsa por município×ano e trata 2019 inteiro como pós:

| Estimador | Estimativa g | SE jackknife | SE bootstrap | IC gravado |
|---|---:|---:|---:|---:|
| Synthetic DiD | −20,1629 | 18,5030 | 21,1617 | [−56,4287;+16,1030] |
| Controle sintético | −34,6405 | 16,7298 | 23,2728 | **[−67,4310;−1,8501]** |
| DiD simples | −21,8518 | 19,2287 | 19,4605 | [−59,5400;+15,8364] |

Os ICs gravados usam o **SE jackknife** multiplicado por 1,96. Há um estimador cuja banda exclui zero: o controle sintético. Não é correto resumir os três como unanimemente nulos. Se fosse usado o SE bootstrap do próprio CSV para construir o intervalo normal, o controle sintético incluiria zero; isso reforça a necessidade de declarar a regra inferencial, não escolher retrospectivamente a mais conveniente.

O arquivo HonestDiD também usa **17×14**; registra três coeficientes pré e quatro pós. O intervalo original é **[−72,9151;+24,9409]**, centrado em cerca de **−23,9871 g**. Com `Mbar=0`, o intervalo robusto é [−72,4673;+24,4889]; com `Mbar=0,5`, [−130,4411;+79,4641]. São intervalos do contraste anual do decil, não do agregado de todos os 169 produtores e não da derivada contínua.

### Robustez e multiplicidade existentes

`robustez_inferencia.csv` reporta **+6,807527**, SE **20,204426**, `p_ingenuo=0,736168`, `p_wcb=0,757`, `p_aleatorizacao=0,7935`, IC **[−46,4544;+57,8450]**, N=184 e MDE rotulado 33,4. Esse coeficiente é a **inclinação OLS sobre a dose**, não o nível −36,19. A unidade é gramas por unidade da dose normalizada, não diretamente gramas de efeito médio do ban.

`holm_confirmatorios.csv` corrige as duas inclinações OLS em 184 municípios:

| Desfecho | Inclinação | p unilateral salvo | p unilateral Holm | p permutação Holm | p WCB Holm |
|---|---:|---:|---:|---:|---:|
| Peso | +6,807527 | 0,3940 | 0,4270 | 0,8660 | 0,7570 |
| Óbito fetal | −0,00243536 | 0,2135 | 0,4270 | 0,8660 | 0,3800 |

Nenhuma rejeita; porém essa correção **não é a família de níveis CGS** após a mudança do alvo primário. A troca para nível não converte a correção de inclinações em correção do novo alvo. Note-se inclusive que a média da curva de nível fetal é positiva, ao passo que a inclinação OLS usada por Holm é negativa: são objetos diferentes, não um erro de sinal automaticamente demonstrado.

## 5. Pré-tendências: separar três objetos e retirar os falsos placebos pré-ban

O CSV do event study mensal tem 47 linhas pré e 48 pós. **Uma linha pré tem banda simultânea excluindo zero**:

| Tempo de evento | Estimativa g | SE | Banda simultânea |
|---|---:|---:|---:|
| **−1** | **+100,806373** | 32,859690 | **[+5,356170;+196,256576]** |

O código usa janeiro/2019 como mês do evento; e=−1 é dezembro/2018. Não se deve confundir esse ponto, cuja construção depende da base temporal do pacote, com o teste conjunto de todos os leads. **As 48 linhas pós têm estimativas ausentes (`NA`); portanto não constituem evidência de ausência de efeito dinâmico.** O arquivo `pretrends_poder` tem 46 leads e inclinações de 0,238187 g/mês para poder 80% e 0,429003 para 90%; são outros cálculos, não o número de rejeições pontuais da tabela acima.

Os três cortes em `spt_pretrend__peso_medio.csv` contêm inclinações 25,757640; 31,072709; 12,963551 e valores-p 0,3705; 0,2385; 0,6080. O arquivo fetal tem valores-p 0,8640; 0,8520; 0,9585. **Essas não rejeições não são evidência válida de placebos exclusivamente anteriores à lei.**

Confirmei por inspeção o problema identificado pelo coordenador: em `10_spt_pretrend.py`, o laço passa **o painel completo** a `primeira_diferenca(painel, desfecho, a, b)`. Essa função, em `04_robustness.py`, constrói o pseudo-pós com apenas `t >= b`, sem teto em dezembro/2018. O filtro seguinte `dose.notna()` não restringe datas. Assim, para cortes em 2016/2017, o cálculo incorpora também 2019–2022. O comentário “só o pré-período” não corresponde à operação executada.

Não refiz os p-valores corretivos, pois essa execução ficou com o coordenador. Os valores antigos devem ser preservados para proveniência e **retirados da argumentação de validação** até substituição explícita por placebos com truncamento correto. Além disso, o CSV salvo não contém a coluna `nivel` que o código atual escreve, mostrando que pelo menos esse arquivo antecede a versão atual do script.

## 6. MDE recalculado para as amostras efetivas

Usei somente 2015–2018. Reexecutei as **funções de diagnóstico** dos scripts 13/14 de forma isolada, com gravação exclusivamente na pasta de trabalho desta auditoria. Não estimei causalidade com essas funções.

### O 33,4 do texto é também uma versão numérica anterior

`dose_variacao_diagnostico__sidra.csv` fornecido registra DP **47,46**, MDE agrupado da banana **33,828631 g** e meia-largura **23,680041 g**. Portanto o 33,4/46,86 dos documentos é valor anterior aos arquivos entregues. A diferença é pequena perto do problema principal: esse benchmark usa **17×167**.

### Contas do script 13, grupos reconciliados

A coluna “agrupado” usa médias mensais simples e DP comum dentro da amostra selecionada. A coluna “por unidade” usa médias de período ponderadas pelos nascimentos e o modelo `σ²/N + τ²`. São aproximações diferentes; a segunda não é a mesma ponderação temporal do CGS.

| Contraste | N | MDE agrupado g | MDE por unidade, σ/τ calibrados no CE | MDE por unidade, σ/τ calibrados no CE+RN |
|---|---:|---:|---:|---:|
| Decil × resto CE | 17×167 | 33,8286 | 30,4722 | 34,3511 |
| Decil × zero PAM | 17×15 | 53,1630 | 50,2253 | **54,6567** |
| Decil × zero GAEZ | **17×14** | **54,9947** | **52,3214** | **56,7125** |
| Todos positivos × zero PAM | 169×15 | 35,7996 | 42,3895 | 45,3367 |
| Todos positivos × zero GAEZ | **169×14** | **37,0555** | **44,8533** | **47,7950** |
| Aeronave histórica × demais CE | 7×177 | 51,2073 | 43,5444 | **49,7925** |

Os valores destacados de 54,6567 e 49,7925 reproduzem o CSV existente. Esse arquivo usa variâncias calibradas no painel **CE+RN**, mesmo nas linhas cuja comparação é apenas CE. A diferença é material: σ estimado é **597,109 g** e τ **24,942 g** usando CE; passa a σ **587,948 g**, τ **33,966 g** com CE+RN. Incluir doadores potiguares no arquivo altera a calibração da variância dos desenhos internos, mesmo quando os grupos do contraste não mudam.

Sob a grade `VPP=2/17`, `f=0,5`, `δ=150`, o sinal é 8,823529 g. Para **17×14**, o poder normal aproximado recalculado é **7,59%** com σ/τ do CE e **7,20%** com σ/τ de CE+RN. O “até 11%” do documento corresponde à conta do benchmark com 167 controles; é otimista para o contraste efetivamente usado. Esses poderes continuam condicionais ao VPP histórico e ao transporte de δ, não fatos estimados sobre a retirada efetiva de exposição.

### Diagnóstico adicional com exatamente os mesmos pesos mensais do nível

Para evitar misturar a ponderação de nascimentos do script 13 com o CGS, calculei `Δ_i = média simples mensal 2017–2018 − média simples mensal 2015–2016` e SE de Welch para cada grupo. Multiplicar por 2,8 produz:

| Contraste | SE do contraste placebo | MDE normal 80%, mesmos pesos mensais |
|---|---:|---:|
| Decil × zero GAEZ, 17×14 | 21,0922 | **59,0582 g** |
| Positivos × zero GAEZ, 169×14 | 19,9644 | **55,9004 g** |
| Positivos × zero PAM, 169×15 | 18,7007 | **52,3620 g** |

Não elejo essa conta como “MDE correto definitivo”: ela preserva os pesos e a heterocedasticidade amostral, mas se baseia em uma única divisão pré de dois anos contra dois, usa aproximação normal, ignora correlação espacial e não reproduz a duração 48 meses pré/39 pós. A dispersão entre métodos é a informação relevante. Não se sustenta uma afirmação única de poder assentada no benchmark 33,4.

## 7. Calendário: o resultado salvo é CE+RN, e o ganho é condicional

Reproduzi os números existentes e repeti a mesma função limitando o universo ao Ceará, sem mudar calendário ou lista histórica de tratados:

| Universo e contraste | Grupos | MDE agrupado | MDE por unidade | δ mínimo se f=0,25 | δ mínimo se f=0,50 |
|---|---:|---:|---:|---:|---:|
| CE+RN, nível sazonal | 7×344 | 67,8736 | 49,5202 | 621,4496 | 310,7248 |
| CE+RN, calendário | **7×344** | 124,6310 | **75,8991** | **303,5962** | **151,7981** |
| Somente CE, nível sazonal | 7×177 | 50,5943 | 43,5444 | 541,1541 | 270,5770 |
| Somente CE, calendário | **7×177** | 100,6972 | **82,4885** | **329,9540** | **164,9770** |

O pico hipotético é fevereiro–maio. A fração de nascimentos classificados como coorte alta no arquivo CE+RN é **0,318740**. O script escala o sinal do nível por essa fração e o do calendário por 1, supondo que somente coortes altas sejam afetadas. Isso explica como o calendário pode exigir δ menor, embora seu MDE bruto em gramas seja maior. Esse ganho depende justamente da concentração sazonal do efeito; não vale para um benefício semelhante ao longo do ano.

Ainda no cenário generoso f=0,5, o δ necessário fica em 151,8 g no painel misto e 165,0 g no CE. Portanto os números existentes **não demonstram poder confortável** para 80–150 g. Além disso, o resultado de 75,9 g não pode ser apresentado como teste de um desenho estritamente intraestadual. A escolha de RN como controle acrescenta pressupostos sobre comparabilidade e exposição, que o cálculo de variância não verifica.

## 8. Proveniência e limites do que foi demonstrado

As reconstruções foram executadas com Python 3.13 e pandas 2.3.3. O script de auditoria é `work/audit_existing_results.py`; suas tabelas intermediárias estão em `work/adendo_identificacao/`, incluindo contrastes, curvas, MDEs recalculados, calendário, metadados e SHA-256 dos oito principais insumos. `sys.dont_write_bytecode=True`/`python -B` impediram escrita de cache no repositório-fonte. As fontes não foram modificadas.

O que **foi** reexecutado aqui: médias e contrastes aritméticos do painel; variâncias de Welch descritivas; contagem de bandas dos CSV; funções de diagnóstico pré-período dos scripts 13 e 14. O que **não foi** reexecutado aqui: contdid/npiv/DRDID em R, SDID, HonestDiD, bootstrap de R, scripts gerais 04/09, correção dos placebos contaminados. Estes últimos estão separados no trabalho do coordenador; não os reivindico como validação deste adendo.

Os arquivos CGS, robustez e placebo têm metadados insuficientes para reconstruir integralmente a chamada histórica: em especial, as curvas não registram os cortes pré/pós, filtro GAEZ, data da execução e agregado com seu SE. Compatibilidade numérica com os padrões atuais é evidência forte da construção do ponto, não prova de todos os parâmetros da execução passada. Os resultados são restritos a 2015–2022, apesar de documentos discutirem expansão até 2024.

**Correções de interpretação exigidas pelos próprios números:** distinguir 169×14 de 17×14; distinguir nível de inclinação; declarar inclusão da transição em SDID/HonestDiD; retirar alegações de placebos exclusivamente pré-ban até corrigir o filtro; identificar CE+RN no calendário; e substituir o único MDE legado por uma tabela de diagnósticos coerente com amostra, pesos, horizonte e hipóteses. Nenhuma dessas reconciliações identifica, por si só, o efeito causal da proibição.
