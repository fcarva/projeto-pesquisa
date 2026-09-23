# Auditoria empírica do Ensaio 1 com os painéis locais

**23/09/2026. Continuação da auditoria integral com Academic Research Skills e agentes GPT-6 Astra.** Esta etapa usou os dados que o pesquisador indicou em `C:/Users/DELL/Documents/projeto-pesquisa`. Os painéis estão no repositório aninhado `projeto-pesquisa/projeto-pesquisa`, HEAD `4ab2c93971fa64d03393405428f6518950c9dada`. A auditoria anterior, de fontes, teoria e código, permanece em [auditoria-integral-2026-09-23.md](auditoria-integral-2026-09-23.md); a limitação anterior de acesso aos painéis é superada por este adendo.

**Conclusão:** o coeficiente de −36,19 g é numericamente reproduzível. Isso não estabelece o efeito causal da proibição. A nova etapa encontrou um erro efetivo nos placebos, um canal SIH sem controles utilizáveis e uma correção de multiplicidade que se aplica a outro parâmetro. A definição do tratamento real continua sendo a principal lacuna de identificação.

## 1. O que foi efetivamente reproduzido

O painel tem **184 municípios × 96 meses, 2015–2022**, com 1.001.709 nascimentos agregados. Reconstruí seu conteúdo com os componentes atuais: todos os valores numéricos compartilhados coincidem. Há atualizações de metadados de legislação municipal, descritas no [parecer de integridade](adendo-integridade-paineis.md), sem efeito nas estimações reproduzidas. SINASC obtido por dois transportes, pysus e FTP, também coincide numericamente no recorte CE.

O clone da primeira auditoria tinha HEAD `8d3a31e`. Os 40 arquivos de código, testes e manuscrito comparados têm o mesmo conteúdo textual no HEAD auditado e na cópia aninhada fornecida; seis diferem apenas na representação de fim de linha. Assim, a diferença de commit não explica as discrepâncias econométricas encontradas.

Executei o código original com Python 3.13 e **R 4.6.1**, usando a biblioteca `renv` já disponível. `contdid` 0.1.1 está no SHA `5cfec81a82fc8cfeffb6b7b822a0eded5deafc91`; também foram carregados `ptetools`, `npiv`, `HonestDiD` e `synthdid`. Foi necessário ajustar somente a localidade UTF-8 no wrapper de execução. Os scripts originais e seus resultados salvos não foram sobrescritos.

| Resultado | Amostra e janela | Reprodução |
|---|---|---|
| CGS, ATT agregado do peso | 169 positivos × 14 controles; pré 2015–2018, pós out/2019–dez/2022 | **−36,19 g; SE 15,47; IC95% [−66,51;−5,87]** |
| CGS, ATT agregado fetal | Mesma construção de dose e janela | **+0,000176**, aproximadamente +0,176 por mil; IC95% do pacote [−0,00389;+0,00424] |
| Inclinação OLS do peso | 184 municípios, incluindo 15 zeros | **+6,8075** g por unidade da dose; p wild 0,757 |
| Synthetic DiD | 17 do decil × 14 doadores; anos 2015–2018 contra 2019–2022 | **−20,1629 g; IC jackknife [−56,4287;+16,1030]** |
| HonestDiD | Contraste anual do decil, 17×14 | IC original **[−72,9151;+24,9409]**; inclui zero antes da sensibilidade |
| Holm já existente | Duas inclinações OLS, 184 municípios | Valores reproduzidos; **não corrige a família de ATT agregados** |

Os CSV de peso CGS, event study, SDID, HonestDiD e Holm coincidem com os salvos, dentro de tolerância numérica de 1e−8 relativa e 1e−10 absoluta. A robustez reproduz os campos inferenciais antigos e acrescenta campos que o código atual já escreve; omiti o argumento MDE legado, portanto o campo de MDE fica vazio nesta execução.

No CGS fetal, **pontos e erros-padrão das curvas coincidem**, mas os críticos e as bandas bootstrap não coincidem com os arquivos históricos: crítico level **6,78690 → 6,27645**, slope **6,34803 → 6,32414**. Sem manifesto da chamada antiga, não atribuo a diferença a uma causa específica. A inferência histórica fetal não está integralmente reproduzida. Os logs, CSV e comparação automática acompanham o pacote.

## 2. Novo erro confirmado: os placebos usavam o pós-ban

Em `scripts/estimate/10_spt_pretrend.py`, o laço passa o painel inteiro a `primeira_diferenca`. Essa função calcula o pseudo-pós com `t >= corte`, sem impor dezembro/2018 como teto. O filtro subsequente exige apenas dose observada. Assim, cada placebo antigo inclui os **48 meses de 2019–2022**, apesar de seus cortes serem anteriores à lei.

O erro importa substantivamente. Para o **nível com os mesmos 14 controles do ATT principal**, a comparação é:

| Corte pré / início pseudo-pós | Nível antigo, incluindo 2019–2022 | Nível restrito a 2015–2018 | p bilateral de Welch, correção nova |
|---|---:|---:|---:|
| jan/2016 / nov/2016 | −6,47 g | **+20,09 g** | 0,392 |
| jul/2016 / mai/2017 | −6,89 g | **+28,13 g** | 0,169 |
| jan/2017 / nov/2017 | −12,85 g | **+21,55 g** | 0,367 |

São diagnósticos novos do nível, com inferência de Welch sob independência entre municípios, não resultados confirmatórios retrospectivos. Ajustar esses três testes por Holm tampouco gera rejeição a 5%. Os placebos corrigidos não demonstram tendências paralelas: permanecem imprecisos, e seus níveis economicamente relevantes têm de ser considerados junto com os intervalos.

Também reexecutei o script corrigido mantendo sua amostra padrão de **169×15** e seu procedimento de permutação das inclinações: p do peso **0,303; 0,259; 0,519**; p fetal **0,557; 0,461; 0,732**. Esses p-valores dependem da hipótese de permutabilidade da dose; não são testes exatos garantidos para área de banana observacional. Não se devem misturar seus valores com a tabela de níveis 169×14 acima.

**Correção concreta:** em uma cópia isolada, restrinjo as observações entre `--inicio` e `--corte-pre` antes de formar cada placebo e rejeito janelas pré que alcancem janeiro/2019. Não alterei o estimador primário nem a especificação histórica no repositório do pesquisador. O patch de duas fronteiras temporais e seus testes acompanham esta entrega.

Os dois testes perturbam apenas desfechos fora da janela permitida, um antes de seu início e outro depois do fim. Ambos falham com o código original e passam com a correção. A suíte completa passou: **276 testes, dois avisos; `git diff --check` sem erros**.

## 3. O sinal negativo não é um resultado unanimemente nulo

O −36,1924 g decompõe-se em mudança média de **−16,7364 g** nos 169 municípios positivos menos **+19,4559 g** nos 14 controles. Cerca de **95,0% da variância de Welch** desse contraste vem da média dos controles. Esse é o motivo quantitativo para tratar o lado de controle como o lado escasso.

O IC original do CGS exclui zero; não pode ser descrito como “compatível com zero” apenas porque a estimativa é menor que algum MDE. MDE é característica de poder de um desenho sob alternativas e hipóteses, não um segundo teste de significância do coeficiente observado.

Ao mesmo tempo, o nível negativo não demonstra que a proibição piorou a saúde. Dose agrícola não é aplicação aérea observada, e a política atingiu o estado inteiro; a comparação depende de controles válidos e tendências adequadas. Trocar o procedimento inferencial não resolve esses pressupostos.

Para auditar a família de **níveis**, calculei uma sensibilidade transparente com estatística **t de Welch e graus de liberdade estimados**, pois `p_welch` do script original usa uma cauda normal. Esta é uma análise nova; não substitui retroativamente a regra confirmatória:

| Nível, definição 4 | Estimativa | IC95% t de Welch | p bilateral | p bilateral Holm, família de dois |
|---|---:|---:|---:|---:|
| Peso | −36,1924 g | [−69,1504;−3,2343] g | 0,03357 | **0,06713** |
| Óbito fetal | +0,000176 | [−0,004284;+0,004637] | 0,93360 | **0,93360** |

Nenhum dos dois rejeita a 5% **nesta sensibilidade de multiplicidade**. Isso não prova efeito zero nem torna essa escolha inferencial o novo protocolo. Os testes unilaterais nas direções substantivas esperadas, aumento do peso e redução da taxa fetal, tampouco rejeitam; seus p ajustados são 1. O nível do peso vai na direção oposta à expectativa de benefício.

A inferência de nível já implementada no script, aplicada aos 14 controles, dá p wild **0,0375** e p de permutação studentizada **0,0340**, ambos sem ajuste pela família. A retirada de um controle de cada vez move o ponto entre **−43,12 e −29,30 g**, mantendo o sinal. Esses diagnósticos não validam a atribuição da dose nem substituem inferência apropriada sob dependência espacial.

## 4. Pré-tendências, pandemia e poder

O event study mensal reproduzido contém um lead com banda simultânea acima de zero: **e=−1**, correspondente a dezembro/2018, estimativa **+100,81 g**, banda **[+5,36;+196,26]**. A construção depende da base temporal do pacote; não o interpreto automaticamente como antecipação causal, nem como teste conjunto de todos os leads. É suficiente, porém, para retirar a afirmação de que todos os leads passam.

**As 48 estimativas pós do event study são `NA`.** Esse arquivo não fornece a trajetória dinâmica depois do ban; a ausência de estimativas não é evidência de efeito nulo. O CGS de dois períodos e seu ATT agregado foram executados por outra rota.

No pós principal, 24 dos 39 meses são de 2020–2021. A sensibilidade exploratória que os exclui deixa o ponto quase igual, **−36,13 g**, mas alarga o IC de Welch para **[−83,85;+11,60]**. Não escolhemos essa variante como primária; ela mostra que estabilidade do ponto e precisão são questões diferentes.

O [adendo de reconciliação](adendo-resultados-existentes.md) recalcula os diagnósticos de poder. Os resultados principais são:

* O benchmark de aproximadamente **33,4 g** vinha de **17×167**, não de 17×14 nem de 169×14. O CSV entregue traz uma versão próxima, **33,83 g**.
* No desenho **17×14**, o MDE agrupado recalculado é **54,99 g**. Modelos alternativos de variância produzem valores distintos, e calibrar com CE+RN muda os números até dos contrastes internos do CE.
* Para o agregado **169×14**, um diagnóstico pré-período com as mesmas médias mensais e variância de Welch produz MDE normal aproximado **55,90 g**. Não é um MDE definitivo: usa uma divisão pré de dois anos contra dois, distinta de 48 meses pré contra 39 pós, e ignora dependência espacial.
* O MDE de calendário salvo, **75,90 g**, usa **sete tratados históricos contra 344 controles no CE+RN**. Restrito ao CE, a mesma função entrega **82,49 g**, com 7×177. O pico fevereiro–maio e a validade do tratamento histórico ainda são hipóteses.

Não há fundamento para escolher um único desses números como “o verdadeiro MDE” sem fixar população, estimando, janela, pesos, variância e método de inferência. Nenhuma conta de poder comprova que os municípios realmente pulverizavam por aeronave em 2015–2018.

## 5. O canal SIH precisa ser reconstruído

O arquivo SIH integrado tem taxas observadas em apenas **46 de 17.664 células**; 17.618 ficaram ausentes. A saída agrega somente células com algum CID selecionado e não completa a grade dos meses sem evento. No contraste principal, sobram **três municípios positivos e zero controles** com pré e pós: não existe, nesse arquivo, a comparação necessária para estimar o canal SIH.

Há 96 arquivos RDCE mensais, todos não vazios, mas é preciso transformar esse inventário em cobertura verificável por calendário e residência antes de preencher zeros. Não fiz preenchimento indiscriminado. O SINAN dispõe de taxas na grade inteira e deve ser analisado separadamente; não corrige o problema de construção do SIH.

O risco de SIM preencher 2023–2024 com zeros sem fonte, demonstrado na primeira auditoria de código, **não se materializou nesta amostra**, que termina em 2022. Permanece como impedimento técnico a resolver antes de ampliar a janela.

## 6. Parecer atualizado e próximos passos determinados pela evidência

**Dados e reprodução:** o núcleo numérico de nascimento/peso é consistente e reproduzível. Isso permite corrigir afirmações concretas do manuscrito, sem especular sobre dados simulados ou painéis desatualizados.

**Código e inferência:** incorporar a correção dos placebos com seus testes; reconstruir o SIH com cobertura explícita; registrar chamada, seed, versão e agregado em cada saída; alinhar a família de testes ao estimando efetivamente escolhido. A seleção da regra confirmatória deve ser registrada com transparência sobre a mudança posterior à observação dos resultados.

**Identificação:** medir aplicação aérea real em 2015–2018 e sua mudança depois de 2019 continua necessário. O Censo de 2006 não valida o VPP de 2018 nem a ausência de falsos negativos contemporâneos. Os relatórios operacionais do MAPA e os registros municipais/estaduais identificados na [auditoria de fontes primárias](parecer-fontes-primarias.md) são as rotas documentais concretas. Nenhum pedido externo foi enviado nesta etapa.

**Ensaio 2:** esta reprodução não libera o uso do −36 g, da derivada agregada ou dos custos Conab como benefício marginal estrutural de reduzir pulverização. Permanecem a ausência de dose operacional, a passagem de efeito perinatal para benefício monetário e a identificação das curvaturas. As hipóteses teóricas continuam avaliadas no [parecer de teoria e custos](parecer-teoria-custos.md).

O resultado defensável hoje é **uma diferença negativa reproduzível na mudança do peso entre municípios com área de banana positiva e os controles selecionados de área zero**, acompanhada de limitações de identificação e inferência explicitadas. Isso é distinto da inclinação contínua sobre a dose, que nesta amostra é positiva e imprecisa. O conjunto atual não demonstra benefício causal da proibição, dano causal da proibição ou ausência de efeito.

## Arquivos e reprodução

* [Reconciliação de estimandos, janelas e poder](adendo-resultados-existentes.md).
* [Integridade, cobertura e proveniência dos painéis](adendo-integridade-paineis.md).
* [Comparação automática das saídas e viabilidade dos canais](reproducao-empirica-diagnosticos.json).
* `correcao-placebos-pre-periodo.patch`: alteração mínima e testes, aplicada somente na cópia isolada.
* `manifesto-reproducao-empirica.json`: hashes, versões, comandos e limites da reprodução.
* `auditoria-completa-com-paineis-2026-09-23.zip`: relatórios anteriores e atuais, tabelas agregadas, scripts e logs; não contém painéis Parquet nem microdados.
