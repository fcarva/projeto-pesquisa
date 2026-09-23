# Parecer independente: identificação, inferência e poder

**Data:** 23/09/2026. **Escopo:** projeto `work/projeto-pesquisa`, Ensaio 1. **Conclusão:** revisão metodológica maior. O contraste reduzido entre municípios classificados pela bananicultura pode continuar sendo reportado, condicionado às hipóteses; sua interpretação como efeito da retirada efetiva da pulverização aérea ainda não está demonstrada. A rota sazonal é uma hipótese de novo desenho, não uma solução validada.

Auditoria assistida por IA, orientada pelo protocolo ARS `deep-research` e pelas referências de argumentação e severidade. Li CLAUDE.md, docs/ars/03, 16, 17, 18, 19, pré-especificação, seção 04 do manuscrito, scripts de estimação 03, 04, 07, 08, 10, 12, 13, 14, o cálculo de MDE do script de dados 01 e renv.lock. Não li pareceres dos outros agentes. Recebi somente uma indicação de URL do PDF de Calzada, que abri e examinei independentemente. Não alterei manuscrito ou código. **Nenhum estimador foi reexecutado e nenhum resultado empírico foi reproduzido nesta auditoria.** Os cálculos novos abaixo são apenas aritmética explícita de números existentes nos documentos.

## 1. Achados prioritários

### P0 — O MDE de 33,4 g pertence a um contraste diferente do estimado

O código permite uma verificação direta, sem depender de parecer anterior:

- `scripts/data_prep/01_check_dose_variation.py:963–979`: define os municípios do topo e faz `g0 = dose.size - g1`. Para os números registrados no projeto, o contraste é **17 contra 167**.
- `scripts/estimate/07_honestdid.R:93–103` e `08_synthdid.R:93–98`: selecionam **17 do topo contra os de dose zero filtrados por GAEZ**, com 14 controles na configuração padrão documentada, não contra todos os outros 167.
- `scripts/estimate/03_contdid.R:319` e a rota `overall_att` do pacote: o agregado usa todos os positivos, **169 contra 14/15**.
- `scripts/estimate/12_erro_de_classificacao.py:137`: fixa `MDE_G = 33.4` para calibrar o poder que docs/ars/16 atribui ao contraste do decil estimado.

Portanto, “poder ≤11%” não é uma estimativa de poder validada para o DiD 17×14. Mantendo **somente para comparação aritmética** o mesmo DP de tendências de 46,86 g e o multiplicador 2,8 usados pelos documentos:

| Contraste | 2,8 × 46,86 × √(1/G1 + 1/G0) |
|---|---:|
| 17 × 167 | 33,40 g |
| 17 × 15 | 46,48 g |
| 17 × 14 | 47,35 g |
| 169 × 14 | 36,49 g |

Esses últimos números **não são MDEs reestimados**: a variância, os pesos, a janela, a composição e a dependência entre municípios também precisam mudar com o contraste. Demonstram apenas que a conta original não se transporta automaticamente. O próprio script 13 já contém instrumentos para separar desenhos; suas saídas precisam substituir as contas herdadas.

Há um segundo erro aritmético nos docs/ars/17 §§3 e 7.4: concordância entre “MDE previsto 33,4” e “meia-largura realizada 30,3” não valida diagnóstico amostral. Sob a aproximação usada, **33,4 de MDE implica 23,38 de meia-largura**, enquanto 30,32 de meia-largura implica MDE de aproximadamente 43,31. Ademais, foram produzidos por estimandos diferentes.

**Consequência:** suspender conclusões quantitativas de detectabilidade por desenho até haver uma tabela que associe cada estimando a sua amostra, variância, calendário, ponderação e teste. Isso pode agravar a baixa potência; não a elimina.

### P0 — “Comparar ATT e ATE para testar SPT” é um teste inexistente

A fonte original resolve a questão: CGS, versão janeiro/2024, Teorema C.1(b)–(d), identifica `ATT(d|d)` sob PT e `ATE(d)` sob SPT **pela mesma expressão observável**, `E[ΔY|D=d]−E[ΔY|D=0]`. PT e SPT são não aninhadas, embora a segunda costume ser substantivamente mais exigente. [CGS, v4, Apêndice C](https://arxiv.org/html/2107.02637v4#A3).

**Dedução para este projeto:** o diagnóstico proposto em docs/ars/03 §4.1 — convergência validaria seleção desprezível, divergência rejeitaria SPT e mediria seleção — não é operacional. Não existem duas curvas identificadas de maneira independente para fazer essa comparação. Sob hipóteses distintas, o mesmo objeto estatístico recebe interpretações distintas. O cabeçalho do `03_contdid.R:55–70` ainda reproduz o erro. Rodar `target_parameter="level"` e `"slope"` compara um nível com sua derivada, em unidades diferentes; não estima ATT versus ATE.

Também não basta dizer que produtores escolheram a cultura antes de preverem o ban. A exclusão de seleção em ganhos é restrição sobre heterogeneidade de efeitos e composição dos grupos, não sobre consciência ou intenção dos produtores. Exemplo lógico próprio: altitude pode determinar banana e simultaneamente a dispersão do produto e o benefício sanitário por hectare. A escolha anteceder a lei não desfaz essa correlação.

O alvo agregado `ATTᵒ` deve ser distinguido de uma curva `ATT(d|d)`: PT agregada pode bastar para o primeiro sem identificar cada dose. Há ainda diferença de notação entre versões: a v4 usa ATE(d) populacional; versões posteriores usam parâmetros globais entre tratados. Fixar a versão e a população-alvo na dissertação evita colar definições de rascunhos diferentes. [Histórico de versões CGS](https://arxiv.org/abs/2107.02637), [v6, Teorema C.1](https://arxiv.org/html/2107.02637v6).

### P0 — Corolário 1 correto; “ausência de falso negativo verificada” incorreta

Denteh–Kédagni realmente estabelecem, no Corolário 1, `θ_DID = P(ε=0|D=1) × ATT` sob tendências paralelas no **tratamento observado** e ausência de falsos negativos. O resultado admite erro diferencial. A Proposição 1 mostra os termos positivo e negativo que antecedem a simplificação. O modelo também supõe ausência de antecipação e define tratamento verdadeiro ocorrendo entre os dois períodos. [Denteh–Kédagni, v3, §2, Assumption 1, Proposition 1 e Corollary 1](https://arxiv.org/html/2207.11890v3).

**Aplicação própria ao projeto:** o teorema está bem citado, mas sua premissa empírica não foi demonstrada para 2019. Ausência de estabelecimento com uso aéreo em 2006 não implica ausência de aplicação agrícola, sanitária ou exposição recebida em 2018. Nem garante que aplicação registrada em 2006 continuasse imediatamente antes do ban. As questões de 2011 tornam o segundo problema especialmente concreto.

Além da data, falta definir precisamente `D*`: município onde havia aplicação em 2018; município cujo uso caiu por causa da lei; ou município cuja população teve exposição reduzida? São objetos diferentes. Para ler os demais produtores como “falsos positivos sem efeito”, é preciso excluir efeitos do ban sobre eles via deriva, renda, preços, migração ou substituição. Se esses caminhos existem, classificá-los como `D*=0` e aplicar a fórmula já impõe uma exclusão substantiva adicional.

Para a amostra restrita decil versus zero, o ATT corrigido refere-se aos verdadeiros tratados **nessa amostra**, não aos sete municípios históricos nem ao estado. O VPP deve corresponder aos mesmos pesos do estimando: a fração municipal 2/17 não corrige automaticamente estimadores reponderados como SDID. Na presença de pesos, seria necessário derivar o alvo e a mistura ponderada. A concordância de sinal entre resultados que compartilham controles não equivale a replicação independente.

**Recomendação:** manter `θ/VPP` como sensibilidade condicional, com denominador contemporâneo desconhecido; nunca como correção empírica já identificada. Reportar incerteza sobre VPP e sobre θ. O Corolário não torna transportável o VPP histórico nem corrige PT violada.

Negi–Negi, na versão integral acessível de 2022, modelam o caso unilateral de exclusão: tratados verdadeiros classificados como controles. Isso confirma que seu procedimento não pode ser importado diretamente para a configuração de falsos positivos descrita pelo projeto. Uma recodificação dos braços exigiria rederivar estimando e hipóteses; não é uma solução automática. O texto publicado de 2025 não abriu nesta rodada. [Negi–Negi, §§1 e 6](https://arxiv.org/pdf/2208.02412), DOI publicado registrado no projeto: [10.1002/jae.3116](https://doi.org/10.1002/jae.3116).

### P1 — O MDE não é um limiar posterior de validade científica

O manuscrito, §4, `04_robustness.py:46–50` e pré-especificação §§5 e 7 transformam “coeficiente abaixo do MDE” em “não é achado; é limite superior”. Isso confunde uma propriedade prospectiva do teste com inferência sobre uma realização amostral.

**Demonstração própria:** em teste normal bilateral de 5%, MDE para potência de 80% é aproximadamente `2,80×SE`; significância ocorre a partir de `1,96×SE`. Uma estimativa de `2,20×SE` está abaixo do MDE e rejeita zero. Isso é matematicamente possível e não contradiz a definição de poder. Um limite superior exige uma construção de intervalo ou teste direcional, não nasce da desigualdade `|estimativa|<MDE`.

Do mesmo modo, `meia_largura < 15` é medida de precisão **em torno de uma estimativa próxima de zero**, não teste geral que exclui efeito +15. O script 03 imprime “falsifica 15 g?” usando apenas `1.96*ag_se <=15` (`03_contdid.R:560–562`): pode dizer sim quando todo o IC está acima de +15. Para excluir um ganho ≥15, deve-se comparar a borda superior apropriada com +15; para equivalência em ±15, requer-se teste/intervalo de equivalência. A hipótese, a direção e o nível precisam ser explícitos.

Preservar o compromisso original datado é correto. Preservar um erro lógico como se fosse regra estatística não é necessário: registrar emenda metodológica, mantendo resultados e rotulando a mudança pós-estimação. O piso 15 continua sendo uma escolha substantiva analógica, não uma constante da literatura.

### P1 — Os 14/15 controles importam; nenhum procedimento oferecido garante solução

A identidade do agregado binarizado é corroborada pelo caminho `overall_att_res <- ptetools::pte_default(...)` do `contdid` fixado no lockfile; o nível por dose é produzido por outra rota. O pacote documenta limitações de CCK a dois períodos e ausência de covariáveis. [Código fixado, linhas 176–317](https://raw.githubusercontent.com/bcallaway11/contdid/5cfec81a82fc8cfeffb6b7b822a0eded5deafc91/R/cont_did.R), [documentação oficial](https://bcallaway11.github.io/contdid/reference/cont_did.html).

**Aplicação própria:** distinguir número total de clusters, número de controles, concentração de influência e correlação espacial. Quinze não torna automaticamente todo bootstrap otimista; é fator de risco que precisa de diagnóstico. Não existe garantia universal de que a permutação forneça o resultado mais conservador. A população de municípios é observacional e a dose segue aptidão e geografia; permutação global não é aleatorização real. Estratificar por GAEZ reduz a exigência, mas não prova intercambiabilidade dentro dos estratos.

Conley–Taber aprendem a distribuição de choques com muitas unidades não tratadas; no texto integral aberto, Assumption 2 exige vetores de choques i.i.d. entre grupos e independência de tratamento/covariáveis. Isso é mais forte que PT das médias. Não é simplesmente “permutar a dose”. [Manuscrito dos autores, pp. 9–12](https://www.ssc.wisc.edu/~ctaber/Papers/taber-conley.pdf), [publicação DOI 10.1162/REST_a_00049](https://doi.org/10.1162/REST_a_00049).

**Dedução própria:** inverter a codificação dos braços produz equivalência algébrica em modelo aditivo homogêneo; não garante que os resíduos dos 169 produtores informem choques contrafactuais dos 15 controles. Nos 169, efeitos heterogêneos da política podem entrar no resíduo. Portanto a proposta “Conley–Taber/Ferman–Pinto invertido” precisa de justificativa específica, não só troca de rótulos. Ferman–Pinto tratam explicitamente heterocedasticidade com poucos tratados e muitos controles; a página oficial confirma escopo, mas o artigo integral não abriu aqui. [Registro editorial e DOI 10.1162/rest_a_00759](https://direct.mit.edu/rest/article-pdf/101/3/452/1916793/rest_a_00759.pdf).

**Risco adicional por inspeção:** na rota CCK, o pacote centra o desfecho por `m0` estimado nos controles, ajusta `npiv` apenas nos tratados e extrai `att.d_se` diretamente do ajuste. Não aparece nesse bloco parcela que propague a incerteza de `m0` às bandas de nível por dose. Já o agregado usa outra rotina. Essa leitura merece auditoria técnica e simulação dirigida antes de usar bandas por dose; não afirmo que executei ou confirmei numericamente um bug.

### P1 — Calzada é precedente próximo, não teto biológico nem réplica do calendário proposto

Abri o PDF de março/2023 no repositório institucional. Ele combina residência materna, perímetro agrícola e aplicação mensal; define exposição sazonal em células de 5×5 km, com limiar de quatro galões por hectare e meses gestacionais expostos. A versão examina trimestres, não apenas o primeiro. O intervalo de 80–150 g consta do resumo e da conclusão; a Tabela 3 refere-se à **intensificação sazonal**. Os autores também mostram sensibilidade a limiares e escolhem a classificação geográfica examinando gradientes de desfecho. [Calzada, Gisbert e Moscoso, PDF, pp. 4, 18–20, 25–27 e Tabela 3](https://diposit.ub.edu/bitstreams/73f71bc2-9e61-4f15-a2de-a58cb08d43ac/download), [DOI 10.1086/725349](https://doi.org/10.1086/725349).

**Implicações próprias:** converter esse contraste em efeito da remoção de todo uso aéreo requer hipóteses sobre dose, química, população, exposição basal, substituição e reversibilidade. Não se demonstrou que 150 g seja teto do efeito no Ceará. Consequentemente, expressões “não passa de”, “impossível” e “θ̂ não é sinal diluído” extrapolam a calibração. O exercício pode dizer que uma estimativa é difícil de reconciliar com **essa grade**, não impossível no mundo.

O produto `VPP×f×δ` é um cenário simplificado: com heterogeneidade, o efeito médio contém médias ponderadas de `f_i δ_i`, e não necessariamente produto de médias. Não se deve multiplicar novamente por frações já embutidas no estimando importado. Um efeito negativo do ban também não vira versão diluída de um benefício positivo: a comparação em módulo descarta a restrição de sinal.

“Aumentar N sem aumentar VPP não resolve” é falso como regra geral: com VPP constante e positivo, mais informação reduz SE. Neste estado e com estas unidades, pode ser impraticável; isso é uma restrição de viabilidade. Adicionar municípios menos expostos muda simultaneamente mistura, precisão e estimando. A direção líquida precisa de cálculo, não decorre apenas do VPP.

### P1 — A DDD sazonal identifica diferença de efeitos e conserva ameaças relevantes

Olden–Møen, §5, eqs. (5.2)–(5.4), apresentam PT para o diferencial entre categorias; o resultado exige uma condição de tendências relativas, não duas PT separadas. A §7 mantém os problemas de correlação serial e de grupo. [Artigo publicado, pp. 536–539](https://academic.oup.com/ectj/article-pdf/25/3/531/45842047/utac010.pdf).

**Derivação própria para o projeto:** escreva `H_it = média peso(coortes de pico) − média peso(coortes fora do pico)`. Uma DDD é o DiD de H entre municípios com/sem aplicação. Se o ban afeta ambos os conjuntos de coortes, seu parâmetro é `ATT_pico − ATT_fora`, não o ATT anual ou o efeito total da retirada. Docs/ars/19 reconhece esse ponto; deve permanecer no desenho final. Zero pode significar efeitos iguais nos dois grupos, não ausência de benefício.

O script 14 é diagnóstico de variância pré-tratamento, não demonstração de identificação ou poder realizado. Sua grade usa pico hipotético fev–mai, janela fixa, exclusão das coortes com exposição 1/3 e aproximação normal. Isso é transparente, mas ainda precisa de:

1. Calendário independente dos desfechos e medido antes da política; chuva sozinha não reproduz Calzada.
2. Quantificação da diluição dentro do município, que DDD não remove.
3. Estrutura de correlação temporal e espacial e teste adequado ao número efetivo de municípios.
4. Sensibilidade a erro na atribuição gestacional. Janela fixa evita usar duração gestacional afetada pelo tratamento, mas misclassifica o trimestre de prematuros; é trade-off, não solução perfeita.
5. Tendências do hiato sob mudanças climáticas, composição materna, pandemia, atendimento pré-natal e substituição terrestre.

Na frase de docs/ars/19 §6, a mudança de sigatoka com o fim da seca **não é automaticamente parte do tratamento**. Substituição causada pelo ban é mecanismo; clima que mudaria aplicação e saúde mesmo sem ban é confundidor. É preciso separar causalmente as duas coisas.

O script 14 permite nova comparação 7×177 em vez de 17×14, pois redefine quem é tratado. Portanto os 15 controles podem deixar de limitar por uma mudança de classificação/amostra; comparar dentro do município, isoladamente, não cria novas unidades independentes. A hipótese pós-ban não é “testável” em sentido literal: placebos examinam implicações anteriores e podem aumentar ou reduzir credibilidade.

## 2. Matriz de hipóteses e estatuto

| Hipótese/afirmação | Estatuto nesta auditoria | Implicação operacional |
|---|---|---|
| PT agregada para 169 produtores vs zero | Mantida, não demonstrada | Sustenta causalidade do agregado; pode falhar com tendências agrícolas próprias |
| PT por dose identifica ATT(d|d) | Teorema verificado; aplicação não verificada | Não transforma diferenças entre doses em resposta causal |
| SPT elimina seleção relevante em ganhos | Teorema verificado na versão citada | Requer defesa substantiva além de ausência de antecipação |
| ATT e ATE podem ser estimados separadamente para testar SPT | Refutada | Remover o diagnóstico e comentários correspondentes |
| Placebos não distinguem PT de SPT | Verificada | O script linear é sonda parcial, não teste omnibus nem validação |
| Corolário 1 vale com erro diferencial e só falsos positivos | Verificada | Correção apenas condicional às premissas |
| Zero em 2006 prova ausência de falso negativo em 2018 | Não verificada; inferência inválida | Exigir medida contemporânea e cobertura de outras vias |
| 2/17 e 7/169 são VPP causal de 2019 | Não verificada | Tratar como cenários históricos |
| Fração municipal corrige SDID ponderado | Não demonstrada | Derivar mistura sob os pesos do estimador |
| MDE 33,4 mede poder dos estimadores do decil | Refutada por leitura de código | Recalcular para 17×14/15 e para cada estimador |
| Coeficiente abaixo do MDE é só limite superior | Refutada algebricamente | Separar planejamento, teste e intervalo |
| Meia-largura menor que 15 falsifica efeito +15 | Refutada em geral | Usar borda de IC ou teste apropriado |
| Permutação é exata/conservadora sem assintótico | Não sustentada | Declarar atribuição hipotética e alvo do teste |
| Inverter Conley–Taber resolve poucos controles | Não demonstrada | Requer modelo de choques e efeitos |
| 80–150 g de Calzada é teto transportável | Não sustentada | Usar grade de sensibilidade, não bound empírico |
| DDD elimina diluição e poucos clusters | Refutada em geral | Pode melhorar razão sinal/ruído, sujeito a diagnóstico |
| Uma PT do hiato basta no DDD canônico | Teorema verificado | Estimando diferencial; condicionamento e interferência precisam de tratamento próprio |
| Não rejeitar óbito fetal encerra seleção para nascido vivo | Não sustentada | Considerar poder e perdas gestacionais não medidas |
| Mudança para level permanece confirmatória | Mudança registrada depois de resultados | Reportar cronologia e natureza adaptativa, preservar alvo original |

## 3. O que fica defensável e o que fazer primeiro

O acerto principal do projeto é reconhecer que o método de aplicação é mal medido e preservar a história das mudanças. O contraste observado deve ser apresentado como **variação diferencial de peso médio entre grupos definidos pela proxy agrícola**; a expressão “efeito causal do ban segundo a proxy” continua condicionada a PT, não antecipação, composição e ausência de vias que contaminem o controle.

A sequência útil é: (i) congelar uma ficha de estimando para cada resultado, incluindo pesos e amostra; (ii) corrigir o MDE e a lógica de equivalência sem alterar retrospectivamente o piso; (iii) retirar o falso teste ATT–ATE; (iv) buscar medida de aplicação imediatamente pré-2019; (v) pré-especificar o estimando sazonal como diferença entre efeitos e só então avaliar sua detectabilidade. Os resultados atuais devem ser preservados, com a escolha pós-estimação do nível claramente rotulada.

Não é necessário escolher novo estimador primário nesta auditoria. Nenhuma das referências metodológicas transforma ausência de medida em identificação. A prioridade é resolver o vínculo entre tratamento substantivo, classificação observada e contraste estimado.

## 4. Registro de fontes, buscas e limites

Busca focal de verificação, não revisão sistemática exaustiva. Incluí fontes originais, documentação dos autores e código fixado; excluí resumos de terceiros como suporte de proposições formais. Pesquisei em 23/09/2026: `Olden Moen 2022 triple difference estimator pdf`; `Calzada Gisbert Moscoso 2023 80 150 birth weight pdf`; `Conley Taber 2011 inference small number policy changes paper`; `MacKinnon Webb few treated clusters wild bootstrap`; `Negi Negi 2025 misclassification false negatives 3116`; `Ferman Pinto 2019 heteroskedasticity pdf`. Abri diretamente arXiv e documentação oficial contdid, depois versões específicas e o raw GitHub conforme renv.lock.

| Fonte primária | Verificação efetuada | Limite |
|---|---|---|
| CGS arXiv 2107.02637 v4 | Texto integral, §3 e Teorema C.1 | A referência 2024 precisa permanecer vinculada a esta versão |
| CGS v5, v6, v8 e histórico | Mudança de notação/população global; discussão de pré-tendências | Não substituí automaticamente a versão teórica do projeto |
| Denteh–Kédagni v3 | Texto integral, modelo, Assumption 1, Proposition 1, Corollary 1 | Working paper; HTML mostra datas internas distintas, fixar PDF/hash na bibliografia |
| Negi–Negi arXiv 2208.02412 | Texto integral de 2022, direção unilateral | DOI 2025 não abriu; comparação de redação publicada pendente |
| contdid SHA 5cfec81 | Fonte original integral, CCK e overall_att | Não executei R/npiv; erro de bandas é risco por inspeção |
| Olden–Møen 2022 | PDF publicado, §5 equações e §7 | Não valida pressupostos empíricos do calendário CE |
| Calzada et al., março/2023 | PDF institucional integral disponível, passagens de métodos e Tabela 3 | Não reexecutei estudo nem examinei integralmente todos os apêndices externos |
| Conley–Taber | Manuscrito integral hospedado por autor e DOI editorial | Condições verificadas no manuscrito, não comparação linha a linha com versão publicada |
| Ferman–Pinto | Registro editorial e resumo originais | PDF integral bloqueado; não alego método rederivado |
| MacKinnon–Webb | Busca localizou PDF de autor e DOI 10.1111/ectj.12107 | Abertura do PDF falhou; não utilizado para sustentar nova proposição detalhada |

Falharam inicialmente páginas HTML da OUP, Wiley, DOI Chicago e a URL antiga do DSpace UB. O PDF publicado de Olden abriu por link `article-pdf`; o de Calzada abriu por UUID `bitstreams`. A rota raw de `ptetools/attgt_functions.R` falhou; a rota `overall_att` em contdid e a implementação local da diferença de médias foram verificadas, mas não alego auditoria completa de toda a cadeia DRDID.

Não conferi nesta auditoria o processo judicial de 2011, os microdados, a veracidade dos totais municipais do Censo ou a vigência das normas. Esses são **insumos não validados aqui**, mesmo quando usados como números condicionais. Os achados de código referem-se a esta cópia do repositório. A correção das falhas conceituais e de compatibilidade não autoriza afirmar qual seria o efeito empírico corrigido.
