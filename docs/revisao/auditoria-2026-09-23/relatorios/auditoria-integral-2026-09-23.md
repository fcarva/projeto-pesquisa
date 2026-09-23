# Auditoria integral do projeto: hipóteses, identificação e evidência

**23 de setembro de 2026 · Ensaio 1 e ponte com o Ensaio 2**

**Veredito:** revisão maior. O material atual não sustenta uma conclusão estabelecida sobre o efeito causal da retirada da pulverização aérea nem sobre a superioridade da proibição. Há uma pergunta científica defensável, fontes administrativas adicionais e correções executáveis. O problema ultrapassa falta de poder: mensuração, estimandos, inferência e documentação ainda não formam uma cadeia coerente.

## Resumo

Esta auditoria reexaminou as hipóteses substantivas e de identificação da dissertação sobre a proibição da pulverização aérea no Ceará, confrontando manuscrito, código, legislação e literatura original. Foram clonados os dois repositórios solicitados, aplicados os protocolos de pesquisa aprofundada e revisão do Academic Research Skills, e mobilizadas três frentes de auditoria configuradas explicitamente com GPT-6 Astra. As verificações confirmaram a revogação da proibição municipal de 2009, identificaram registros municipais potencialmente úteis e preservaram a incerteza sobre aplicação efetiva em 2015–2018. A revisão econométrica mostrou que o cálculo de poder usa grupo de comparação diferente das estimações, que a correção de multiplicidade testa outro parâmetro e que o diagnóstico proposto para tendências paralelas fortes é inválido. Testes adicionais reproduziram preenchimento de mortalidade fetal com zero fora da cobertura e conversão de valor-p indefinido em número finito. A planilha original da Conab revelou perdas extensas de extração. Esses achados não demonstram ausência de benefício sanitário, presença de dano causado pela lei ou inviabilidade definitiva do projeto. Delimitam quais resultados podem ser descritos, quais interpretações devem ser suspensas e quais registros e correções são necessários antes de nova estimação causal.

## 1. Escopo e método

Pergunta da auditoria: **cada hipótese enunciada pelo projeto tem um objeto bem definido, evidência apropriada e implementação que permite avaliá-la?** A análise cobre as seis predições explícitas do referencial teórico, pressupostos de identificação, mensuração e inferência, os principais resultados narrados e a ponte de bem-estar com o Ensaio 2. Afirmações históricas, normativas e propostas exploratórias recebem estatutos próprios; uma hipótese não demonstrada não é automaticamente falsa.

O projeto foi examinado no commit `8d3a31ea2680e530d4ea3cee6134531be0d853fe`, de 23/09/2026. O ARS foi lido no commit `86b8d8b180a6ed2d9e0e517ba5245af15b45bdc1`. A cópia é um clone raso do HEAD disponível, não uma reconstrução da sessão anterior. O commit `9830a71` mencionado no histórico fornecido não é a base auditada; não se pressupõe que suas alterações tenham sido incorporadas. O README presente continua com formulações antigas.

Foram aplicadas as funções das seis fases do [ARS deep-research](https://github.com/imbad0202/academic-research-skills/blob/86b8d8b180a6ed2d9e0e517ba5245af15b45bdc1/deep-research/SKILL.md): delimitação; investigação e verificação; síntese; redação; revisão crítica; consolidação. O escopo já estava dado pela solicitação de reauditoria. Usou-se também a restrição de revisão em documentos separados do [academic-paper-reviewer](https://github.com/imbad0202/academic-research-skills/blob/86b8d8b180a6ed2d9e0e517ba5245af15b45bdc1/academic-paper-reviewer/SKILL.md). A execução foi adaptada às ferramentas do Codex: protocolos lidos diretamente, três agentes especializados mais síntese e revisão; não uma instalação do plugin Claude nem execução de treze agentes. Não se reivindica painel calibrado ou validação independente por famílias distintas de modelo.

As buscas foram orientadas por alegações, em português e inglês, com prioridade para legislação oficial, artigos originais, repositórios institucionais, código dos autores e bases oficiais. Foram incluídas evidências contrárias e versões discordantes. Não é revisão sistemática PRISMA, busca exaustiva de toda a literatura nem reprodução das regressões dos artigos citados. Os registros de busca e acesso estão nos pareceres anexos.

Verifiquei os metadados dos **47 DOIs da bibliografia** via Crossref: todos retornaram registros com títulos compatíveis após repetir três respostas temporárias 429. Semantic Scholar retornou indisponibilidade, registrada no arquivo de auditoria. Isso confirma correspondência bibliográfica, **não** que cada citação sustente a frase em que foi utilizada. Datas online e impressa diferentes foram preservadas. Não foi certificada ausência de retratação ou de conflitos de interesse para todas as fontes.

As três frentes especializadas não leram os pareceres umas das outras antes de entregá-los. Compartilharam escopo e, em um caso, uma URL primária. A síntese resolve sobreposições e qualifica pontos ainda não reproduzidos. Essa separação de trabalho reduz algumas omissões; não torna os erros estatisticamente independentes.

## 2. O que mudou em relação à auditoria anterior

### A. O problema de mensuração permanece, mas já existe uma nova rota concreta

O art. 212 da Lei municipal 1.511/2010 revoga expressamente a Lei 1.478/2009. O texto foi recuperado e lido, encerrando a pendência documental sobre a existência da revogação. A Lei 2.054/2018 mantém substancialmente condições anteriores de aplicação; não se identificou ali novo ban municipal geral. Seus avisos prévios e comunicações de produtos oferecem uma rota para localizar aplicações antes de 2019. A existência da obrigação não garante que os arquivos existam ou estejam completos. [Lei 1.511, PDF, p. 65](https://www.camaralimoeirodonorte.ce.gov.br/arquivos/581/Leis_1511_2010_0000001.pdf); [Lei 2.054, PDF, pp. 62–64](https://immab.limoeirodonorte.ce.gov.br/arquivos/3/Leis%20Municipais_2054_2018_0000001.pdf).

A alegação de interrupção regional em 2011 não foi confirmada por decisão judicial operativa e comportamento posterior. Também não se pode afirmar cessação total: foi localizado relato contemporâneo de avião pulverizando em 2018. A aplicação municipal mensal permanece desconhecida. Portanto, nem “o ban de 2019 não tratou ninguém” nem “o Censo comprova os tratados de 2019” é conclusão autorizada. Veja as fontes e a distinção entre relato, pedido judicial e decisão no parecer de fontes primárias.

Os relatórios MAPA podem registrar município, cultura, área trabalhada e produto comercial; não prometem quantidade de ingrediente ativo ou mapa universal. A entrega à SFA de destino para operador de outra UF está no art. 12, VI; o relatório mensal e a declaração de ausência de atividade, no art. 14. Ausência documental precisa permanecer diferente de atividade nula declarada. [IN MAPA 2/2008 consolidada, arts. 9, 12 e 14](https://www.gov.br/agricultura/pt-br/assuntos/insumos-agropecuarios/aviacao-agricola/legislacao/3-in-2-de-03-de-janeiro-de-2008-com-alteracoes-da-in-37-2020.pdf).

### B. O poder foi calculado para outra comparação

O MDE de 33,4 g usa decil superior contra todos os demais: **17×167**. HonestDiD e SDID usam decil contra dose zero, com aproximadamente **14–15 controles**. O agregado usa todos os produtores contra zeros: **169×14/15**. Além dos tamanhos, mudam pesos, janelas e alvos. Assim, o MDE não pode ser transportado de uma linha para outra.

Somente como demonstração aritmética, mantendo o DP antigo, substituir 17×167 por 17×15 elevaria 33,4 para 46,48 g; com 14, para 47,35 g. **Esses valores não são novos MDEs empíricos.** A reestimação exige os dados e o procedimento de cada contraste. A calibração de poder que reutiliza 33,4 fica suspensa. Evidência: scripts `01_check_dose_variation.py`, `07_honestdid.R`, `08_synthdid.R` e `12_erro_de_classificacao.py`, localizados nos pareceres de código e identificação.

MDE é uma propriedade de planejamento. Uma estimativa abaixo dele pode rejeitar zero; uma acima dele não corrige viés. Sob aproximação normal, `MDE≈2,80 SE`, enquanto significância bilateral de 5% começa em `1,96 SE`. Comparar MDE previsto a meia-largura realizada também compara objetos diferentes. Esse erro deve ser corrigido por emenda datada, não preservado como compromisso científico.

### C. A família confirmatória não testa o ATT anunciado como principal

O `09_holm.py` aplica testes a uma inclinação OLS de variação do desfecho sobre dose. Não testa o ATT agregado promovido a principal, não testa a curva não paramétrica inteira e não usa o mesmo filtro GAEZ. Num exemplo sintético, a diferença binária foi −45 e a inclinação +34,98. O exemplo não é resultado do Ceará: demonstra que nem o sinal é necessariamente compartilhado.

Logo, “nenhum confirmatório rejeita após Holm” não resume o ATT principal. É necessário preservar a família original, registrar a mudança pós-estimação e apresentar uma família coerente para a análise revisada. Chamar a nova escolha de prospectivamente confirmatória apagaria a cronologia que o próprio projeto registra.

O rótulo de exposição também precisa corresponder à execução: em `03_contdid.R`, `--exposicao` é usado como metadado, enquanto o contraste é determinado pelos cortes de coortes. Trocar o argumento não troca a regressão. HonestDiD/SDID incluem 2019 inteiro no pós, mas o contdid exclui janeiro–setembro. Essas linhas avaliam exposições temporais diferentes; não são apenas três métodos de inferência para o mesmo efeito.

### D. Um intervalo que exclui zero foi descrito como compatível com zero

O manuscrito reporta −36,19 g e IC [−66,51; −5,87]. Esse intervalo exclui zero. A crítica cabível é avaliar sua validade, o tratamento medido e a inferência com poucos controles; não alterar a leitura aritmética do intervalo. **Não concluí que a lei piorou a saúde:** os números são transcritos do manuscrito, não reproduzidos nesta cópia.

O critério “meia-largura menor que 15 g” também não testa, isoladamente, exclusão de benefício de 15 g. IC [20,30] tem meia-largura 5 e não exclui benefícios acima de 15. Para testar benefício mínimo ou equivalência, definir hipótese direcional/margens e usar o intervalo ou teste correspondente. Ver `03_contdid.R:556–562` e parecer de código.

### E. Há falhas de dados que uma suíte verde não detectou

Uma junção de SINASC até 2024 com SIM somente até 2022 produz taxa fetal zero em 2023–2024. O teste adicional reproduziu o defeito: falta da fonte virou ausência de óbitos. Outra verificação reproduziu `Holm([NaN,0,04])→[0,08;0,08]`; um teste indefinido ganha valor-p finito.

O alvo `make real` ainda permite que a preparação do SIM caia em simulação. **Nuance:** o arquivo simulado recebe sufixo próprio e não é automaticamente incorporado ao painel real. O risco confirmado é prosseguir com componente ausente ou antigo; em outra rota, a origem interna do componente é descartada e o painel recebe rótulo pela PAM. Não há evidência de que isso tenha contaminado as estimativas históricas, pois seus dados e logs não estão no clone.

### F. A conclusão de custos está apoiada em extração incompleta

A reexecução do extrator na planilha oficial deixou 72/88 custos aéreos, 69/88 custos de tratores e 57/88 custos totais ausentes. Mudanças de rótulos explicam parte da perda. Os quatro custos aéreos positivos são do mesmo sistema/localidade em 2021–2024. Não encontrar avião e trator simultaneamente nessa extração não demonstra exclusividade tecnológica. [Conab, planilha original](https://www.gov.br/conab/pt-br/atuacao/informacoes-agropecuarias/custos-de-producao/arquivos-custo-de-producao/agricolas/serie-historica-custos-banana-2008-a-2025.xlsx/view); resultados em `auditoria-conab.json`.

## 3. Matriz de hipóteses reavaliadas

“Mantida” significa condição necessária ainda dependente de argumento/evidência, não condição comprovada. “Refutada” abaixo se refere à inferência ou implementação indicada, não à hipótese de que agrotóxicos possam causar dano.

| ID | Hipótese ou afirmação do projeto | Resultado da auditoria | Decisão |
|---|---|---|---|
| H01 | Lei estadual começa na sanção de 08/01/2019 | Vigência em 09/01, pela publicação | Usar data jurídica correta |
| H02 | Ban de 2009 em Limoeiro contamina todo pré-2019 | Revogação expressa confirmada em lei de 2010 | Remover esse argumento; auditar fiscalização posterior |
| H03 | Ban regional de 2011 encerrou aplicação | Não demonstrado; há evidência parcial contrária à cessação total | Recuperar processo e registros operacionais |
| H04 | Aplicação aérea existia nos municípios tratados em 2015–2018 | Parcial em relatos, sem painel validado | Mensurar antes de interpretar retirada efetiva |
| H05 | Banana é medida de aplicação aérea | Área agrícola não identifica modalidade | Manter proxy explicitamente |
| H06 | Dose mede intensidade per capita/territorial | Código normaliza hectares pelo máximo | Definir unidade e alvo; não chamar exposição individual |
| H07 | Censo 2006 mede frota | Mede estabelecimentos com uso por aeronave | Corrigir unidade; não inferir número de aviões |
| H08 | Zero em 2006 valida zero em 2018 | Extrapolação temporal não sustentada | Verificar controles contemporâneos e outras vias |
| H09 | VPP 2/17 ou 7/169 é conhecido para 2019 | Apenas calibração histórica condicional | Incorporar incerteza; não usar correção pontual validada |
| H10 | Corolário 1 permite atenuação com erro diferencial unilateral | Teorema confirmado sob suas premissas | Manter como cenário; verificar premissas na política |
| H11 | PT do grupo observado basta para contraste agregado | Condição teórica pertinente, aplicação não demonstrada | Placebo e sensibilidade no mesmo estimando |
| H12 | Gradiente entre ATT(d|d) é resposta causal à dose | Seleção entre doses impede leitura automática | Separar heterogeneidade observada de ACR |
| H13 | ATT versus ATE é teste de SPT | Mesma expressão observada sob hipóteses distintas | Retirar falso teste; level versus slope tampouco serve |
| H14 | Pré-teste não significativo valida SPT/PT | Não; apenas não rejeita restrição examinada | Reportar poder e sensibilidade sem linguagem de prova |
| H15 | Dose 2015–2018 é livre de antecipação | Janela sucede notícia legislativa de 2015 | Examinar janela anterior com desenho explícito |
| H16 | Controles não recebem efeitos indiretos | Deriva, água, renda e controle vetorial permanecem possíveis | Explicitar interferência e efeito comum eliminado pelo DiD |
| H17 | GAEZ é IV validado para método aéreo | Relevância de plantio não prova exclusão; pipeline não estima esse IV | Rebaixar promessa; justificar novo desenho se proposto |
| H18 | Mais área implica maior ganho perinatal da lei | Condicional a uso, cumprimento, substituição e composição | Predição plausível, não resultado estabelecido |
| H19 | SIM nulo elimina seleção de nascidos vivos | Poder e perdas precoces impedem conclusão | Tratar SIM como diagnóstico, após corrigir cobertura |
| H20 | 33,4 g é MDE de todas as estimações | Comparações diferentes | Recalcular por estimando/amostra/tempo/peso |
| H21 | Coeficiente abaixo de MDE vira limite superior | Inferência estatística inválida | Separar planejamento, IC e relevância econômica |
| H22 | Meia-largura abaixo de 15 falsifica benefício ≥15 | Critério ignora centro do intervalo | Implementar teste correto |
| H23 | Holm valida não rejeição do ATT principal | Testa inclinação diferente; NaN tratado incorretamente | Refazer família e regra para ausência |
| H24 | Bootstrap/permutação resolve 14–15 controles | Não há garantia universal; intercambiabilidade não demonstrada | Auditar influência, dependência e tamanho efetivo |
| H25 | Conley–Taber invertido resolve escassez de controles | Requer modelo de choques e heterogeneidade | Não promover inversão de rótulo a método validado |
| H26 | Efeitos hídricos podem ser estimados no SISAGUA atual | Projeto suspendeu canal por registro; não reproduzido aqui | Preservar hipótese, suspender conclusão causal |
| H27 | Vento dominante separa canal-ar da geografia | Coerência espacial pode confundir direção com localização | Exigir variação apropriada e localização de fontes |
| H28 | Substituição terrestre necessariamente aumenta intoxicação ocupacional | Sinal não necessário | Tornar predição condicional; não usar como teste único |
| H29 | Intoxicação autoprovocada é controle negativo garantido | Disponibilidade, estoque e renda podem responder | Justificar exclusões causais adicionais |
| H30 | Calendário de Calzada pode ser importado | Estudo usa aplicação mensal local medida | Medir calendário CE antes dos desfechos |
| H31 | DDD sazonal estima efeito total da proibição | Em geral estima diferença pico menos fora do pico | Nomear novo estimando e pré-especificar |
| H32 | DDD elimina diluição e poucos clusters | Não em geral | Simular desenho real; medir mistura intramunicipal |
| H33 | 80–150 g é teto transferível para CE | Contraste/população/química diferentes | Usar cenário, não bound causal |
| H34 | ATT/ACR em gramas é benefício/curvatura de Weitzman | Falta mapeamento físico, agregação e monetização | Construir modelo adicional |
| H35 | Quantidade ótima equivale à proibição total | Solução de canto não demonstrada | Separar instrumentos e conjunto factível |
| H36 | Conab demonstra tecnologias exclusivas e substituição barata | Extração incompleta e categorias não comparáveis | Corrigir leitura; retirar conclusão setorial |
| H37 | Custo homogêneo decide proibição por c→0 | Extrapolação local pode sair do domínio | Usar problema com limites e cenários explícitos |
| H38 | Dados até 2024 respeitam automaticamente corte legal | Código mensal preserva dezembro inteiro; defaults acabam em 2022 | Fixar janela comum e recorte antes do colapso |
| H39 | Januzzi é evidência nacional unívoca de nulo | Dissertação e ENABER têm resultados diferentes | Identificar versão e reconciliar especificação |
| H40 | Testes passam, logo efeitos estão reproduzidos | Suíte passou; bases/resultados não estão no clone | Distinguir software testado de resultado reproduzido |

Fundamentos externos dessa matriz: [CGS, versão 2024, Apêndice C](https://arxiv.org/html/2107.02637v4#A3), [Denteh–Kédagni, Corolário 1](https://arxiv.org/html/2207.11890v3), [Olden–Møen, §5](https://academic.oup.com/ectj/article-pdf/25/3/531/45842047/utac010.pdf), [Calzada et al., texto original](https://diposit.ub.edu/bitstreams/73f71bc2-9e61-4f15-a2de-a58cb08d43ac/download). Locatores legais, unidades IBGE e versões de Januzzi estão detalhados no parecer de fontes. As críticas de implementação são sustentadas por arquivos e contraexemplos nos pareceres, não atribuídas aos artigos.

## 4. Arquitetura de análise recomendada

### Ficha de estimando obrigatória

Cada linha de resultado deve carregar: pergunta, população, unidade, definição de tratamento, variável observada, pesos, janela, comparação, hipótese identificadora e método de inferência. Isso evita que robustez aparente mude silenciosamente a pergunta.

| Objeto | O que pode representar | Limite decisivo |
|---|---|---|
| Nível agregado, produtores versus zero | Mudança diferencial média entre grupos definidos pela proxy | Efeito da lei só sob hipóteses; retirada de aplicação requer validação adicional |
| ATT(d|d) por dose | Efeito para o grupo de dose d sob PT apropriada | Comparar grupos d distintos não isola resposta à dose |
| ACR/curva estrutural | Resposta sob hipóteses mais fortes e dose substantiva bem definida | SPT e mensuração não são validadas por rodar sieve |
| Decil versus zero | Efeito em outra subpopulação | Não é alternativa de inferência do agregado 169×zero |
| DDD sazonal | Efeito relativo em coortes de pico versus demais | Pode ser zero mesmo com benefício em ambas |
| Custos/bem-estar | Cenários condicionais de política | Sem ponte estrutural, não importar ATT como B(q) |

Outra decisão importante: ponderar nascimentos **dentro** de município-período é diferente de ponderar **entre** municípios. Média simples de médias mensais dá o mesmo peso a mês com um nascimento e mês com cem. É possível usar pesos válidos internamente e depois agregar municípios igualmente. A ficha precisa dizer se o alvo é município típico, mês típico ou criança típica.

### Sequência para o próximo ciclo

1. **Reparar falhas determinísticas.** Cobertura SIM; NaN no Holm; fonte e vintage por componente; falha explícita de estimação; invalidação de artefatos antigos; leitura Conab; cortes temporais; filtro GAEZ completo. Remover ou implementar o argumento inoperante `--exposicao`, descrevendo o contraste realmente usado. Harmonizar as coortes de 2019 entre métodos ou rotular cada janela como alvo diferente. Testes novos devem reproduzir os contraexemplos, não apenas espelhar implementação.
2. **Reconciliar resultados existentes.** Escolher a ficha do agregado, preservar a análise originalmente planejada e declarar alterações pós-resultado. Gerar IC, multiplicidade e diagnóstico de poder sobre o mesmo objeto. O valor negativo não deve ser apagado nem transformado em dano causal sem identificação.
3. **Medir aplicação e cobertura.** Solicitar registros MAPA/SFA, ADAGRI e municipais, juntando aplicação, declarações nulas, cobertura e fiscalização. A nova fonte municipal deve entrar ao lado das minutas já existentes. A auditoria não enviou pedidos ou mensagens.
4. **Examinar identificação antes de escolher a nova curva.** Verificar controles, tendências agrícolas, exposição indireta, antecipação, registros de nascimento e perdas. A confirmação de alguns voos não encerra esses problemas.
5. **Avaliar calendário somente com calendário externo.** Congelar picos com informação operacional anterior ao ban; definir coortes, diferença de efeitos, janela pandêmica e inferência. Simular poder sob esse estimando com municípios efetivos, pesos, correlação e diluição.
6. **Reformular o Ensaio 2.** Separar aplicação aérea de exposição ambiental, cota ótima de proibição e custo contábil de custo de abatimento. Até existir ponte, oferecer análise de cenários/condições, com parâmetros explicitamente externos e sem ranking empírico.

Critério de saída: se a atividade pré-ban ou a resposta efetiva à lei não puder ser mensurada, a contribuição pode ser uma avaliação transparente dos limites de identificação e um contraste reduzido condicionado às premissas. Isso não deve ser escolhido antecipadamente como resultado desejado; é a conclusão que dependerá dos documentos e diagnósticos.

## 5. Revisão crítica da própria auditoria

**Contestação mais forte:** estamos exigindo mensuração perfeita quando políticas podem ser avaliadas por intenção de tratar. Resposta: a perfeição não é exigida. Um efeito da regra legal pode ser identificado sem observar todos os voos, se houver contraste de política e hipóteses adequadas. Aqui a regra muda simultaneamente em todo o estado, a variação é uma proxy de intensidade e os resultados são narrados como retirada de aplicação. Essa ponte precisa ser explicitada. Um controle externo ou outro desenho pode responder a pergunta distinta, mas não se valida por existir.

**Outra contestação:** os erros encontrados podem não alterar o sinal real. Correto. Os testes sintéticos demonstram capacidade de falha, não que a execução histórica a sofreu. Sem painéis, logs e resultados agregados não se quantifica o impacto. A auditoria rejeita conclusões injustificadas; não fabrica coeficientes corrigidos.

**Contra o pessimismo excessivo:** a revogação municipal foi verificada; registros de aviso prévio e relatórios mensais oferecem caminhos plausíveis; o precedente Calzada mostra como observar calendário. São avanços concretos. Não há fundamento para declarar o Ensaio 1 impossível. Tampouco a multiplicação de estimadores ou agentes substitui dados de tratamento e pressupostos.

**Ética e autoria:** este é trabalho assistido por IA. Não foram coletados novos microdados individuais nem publicados dados pessoais, não foram enviados pedidos a órgãos e não se atribuiu a terceiros conclusão que depende de nossa inferência. A decisão científica e a redação autoral final pertencem ao pesquisador. Fontes de atores interessados foram atribuídas, e falhas de acesso não foram tratadas como evidência de inexistência.

**Checkpoint final:** um quarto agente GPT-6 Astra revisou a síntese, os pareceres e evidências pontuais. Encontrou dois refinamentos, ambos corrigidos: definição da dose e destaque para exposição/coortes divergentes. O veredito foi PASS quanto à coerência da auditoria, sem certificar identificação causal ou repetir a execução empírica. O registro completo acompanha os entregáveis.

## 6. Verificação executada e limitações materiais

- **274 testes existentes passaram**, com dois avisos, usando temporário no workspace. A primeira tentativa com runtime empacotado não tinha pytest; a execução concluída usou Python do sistema. Detalhes no parecer de código.
- Foram executados contraexemplos sintéticos para cobertura fetal, estimando do Holm, NaN, composição do MDE, corte de dezembro, proveniência e pesos. Nenhum deles é estimativa causal sobre o Ceará.
- O extrator original Conab foi executado sobre arquivo oficial recém-baixado. As contagens de campos ausentes foram verificadas e o arquivo recebeu hash.
- Todos os 47 DOIs foram recuperados no Crossref; não se certificou apoio de todas as frases, integridade integral dos estudos ou situação de retratação.
- Não foram reproduzidas as estimativas reais: o clone tem `.gitkeep` nas pastas de dados, não os painéis, curvas ou resultados históricos. Rscript e make não estavam disponíveis no PATH examinado.
- Situação atual da ADI 7.794 e desfecho operativo da ação de 2011 permanecem não certificados. Não se afirma lei suspensa ou julgamento pendente com base em notícia antiga.
- O possível problema de propagação da incerteza dos controles nas bandas CCK é **risco por inspeção**, descrito no parecer de identificação, não bug numericamente confirmado. Deve ser checado antes de entrar como acusação definitiva ao pacote.

## 7. Entregáveis e trilha de evidência

Este relatório deve ser lido com quatro pareceres separados: **identificação**, **código e reprodutibilidade**, **fontes primárias** e **teoria e custos**. Eles contêm caminhos/linhas do código, URLs, localizadores, demonstrações e limites de acesso. Os JSON de metadados e Conab preservam a conferência mecânica. O manuscrito e o código do repositório permaneceram intactos durante a auditoria.

- [Parecer de identificação e inferência](C:/Users/DELL/Documents/Codex/2026-09-23/prior-conversation-with-codex-conversation-role/outputs/parecer-identificacao.md)
- [Parecer de código e reprodutibilidade](C:/Users/DELL/Documents/Codex/2026-09-23/prior-conversation-with-codex-conversation-role/outputs/parecer-codigo-reprodutibilidade.md)
- [Parecer de fontes primárias](C:/Users/DELL/Documents/Codex/2026-09-23/prior-conversation-with-codex-conversation-role/outputs/parecer-fontes-primarias.md)
- [Parecer de teoria e custos](C:/Users/DELL/Documents/Codex/2026-09-23/prior-conversation-with-codex-conversation-role/outputs/parecer-teoria-custos.md)
- [Revisão adversarial final](C:/Users/DELL/Documents/Codex/2026-09-23/prior-conversation-with-codex-conversation-role/outputs/revisao-final-auditoria.md)
- [Metadados das 47 referências](C:/Users/DELL/Documents/Codex/2026-09-23/prior-conversation-with-codex-conversation-role/outputs/auditoria-metadados-referencias.json)
- [Verificação da extração Conab](C:/Users/DELL/Documents/Codex/2026-09-23/prior-conversation-with-codex-conversation-role/outputs/auditoria-conab.json)

O resultado utilizável hoje é uma agenda de reparo e aquisição de evidência, acompanhada de diagnósticos verificáveis. A conclusão científica sobre benefícios, danos ou ausência de efeito permanece aberta.
