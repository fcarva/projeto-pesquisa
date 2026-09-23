# Parecer sobre mecanismos, custos e escolha de instrumento

Data: 23/09/2026. Auditoria do commit `8d3a31ea2680e530d4ea3cee6134531be0d853fe`. Este parecer registra verificações e deduções da auditoria; não altera a dissertação nem estima efeitos do banimento.

## 1. A ponte entre os ensaios precisa de um modelo adicional

O manuscrito, `paper/secoes/07-conclusao.tex`, escreve `B(q)=|ATT(q|q)|`, `B'(q)=|ACR(q)|` e `B''(q)=ACR'(q)`. As identidades não decorrem dos estimandos utilizados. A dose implementada é a área média de banana normalizada pelo máximo municipal, o desfecho é peso em gramas e o contraste é uma mudança de regime legal. Nenhum desses objetos é, por definição, benefício social monetário em função de abatimento físico. A nota `docs/ars/17`, §2.1, reconhece o problema, mas ele persiste no manuscrito e no script 11.

Uma reconstrução possível, explicitamente proposta por esta auditoria, começa por definir `a` como abatimento de uma exposição física e `e(a)` como exposição residual. Se um componente do benefício fosse `B(a)=v N [m(e(a))−m(e(0))]`, com valor marginal constante `v`, população fixa `N` e resposta de saúde `m`, então:

`B''(a)=v N {m''(e(a))[e'(a)]² + m'(e(a))e''(a)}`.

Até nessa simplificação, curvatura sanitária isolada não basta. Faltam a transformação exposição–abatimento, população relevante, monetização e os demais desfechos. Valor marginal não constante, composição populacional e danos não perinatais acrescentam termos. A derivada de `ATT(d|d)` entre grupos também mistura composição com resposta, salvo hipóteses adicionais. Tomar módulo apaga sinais e não resolve essas diferenças. Esta é uma demonstração algébrica da auditoria, não uma fórmula estimada para o Ceará.

## 2. Weitzman não fornece automaticamente um ranking entre taxa e proibição total

Weitzman compara instrumentos ótimos dentro de um modelo local com benefícios e custos em unidades compatíveis. A expressão `Δ=σ²(c−β)/(2c²)` é coerente com choque aditivo de custo, `c>0`, curvaturas fixas e a versão sem correlação relevante entre choques de custos e benefícios. A nota de rodapé da p. 485 trata a correlação. A regra não transforma qualquer quantidade escolhida em quantidade ótima. [Weitzman, 1974, pp. 479–485, DOI](https://doi.org/10.2307/2296698); [texto original indexado na página do autor, p. 485](https://scholar.harvard.edu/files/weitzman/files/prices_vs_quantities.pdf).

Aplicação ao projeto: no eixo de emissões, proibição é emissão zero; no eixo de abatimento, é o extremo de abatimento máximo. Demonstrar vantagem de uma cota ótima sobre uma taxa ótima não demonstra vantagem desse extremo. Além disso, proibir aplicação aérea não equivale a zerar exposição química quando existe aplicação terrestre, transporte hídrico ou descumprimento.

O limite `c→0` usado pelo script 12 da Conab merece retirada da conclusão aplicada. A expressão local pode divergir porque a resposta não restringida da quantidade ao choque cresce como `1/c`. Isso pode sair da região de aproximação e do conjunto fisicamente possível. Como contraexemplo matemático, se o abatimento está em `[0,Q]`, as funções são contínuas e os choques têm esperança apropriada finita, a diferença de bem-estar permanece finita. Portanto a divergência da aproximação não prova uma vantagem infinita nem decide a proibição cearense.

Há também um erro verificável por inspeção no `11_weitzman_inversao.py`: para `sigma=0`, `vantagem_preco` retorna zero, mas `fronteira` continua classificando por `beta>c` ou `beta<c`. Nesse modelo os instrumentos empatam em certeza; o rótulo de dominância não acompanha a própria fórmula. É necessário tratar esse caso ao corrigir o script. Não executei esse módulo para alegar um resultado empírico.

## 3. A auditoria da planilha Conab encontrou perdas de leitura

Baixei a [planilha oficial de banana 2008–2025](https://www.gov.br/conab/pt-br/atuacao/informacoes-agropecuarias/custos-de-producao/arquivos-custo-de-producao/agricolas/serie-historica-custos-banana-2008-a-2025.xlsx/view), atualizada no portal em 24/07/2025. Executei o extrator original `scripts/data_prep/12_clean_conab_custos.py`, sem modificar seu código, e contei positivos, zeros e valores ausentes separadamente. Registro completo em `auditoria-conab.json`; SHA-256 do arquivo: `ec690b88b91a8314d6562aca099e5b727bf29bd23aeef11b8778cbf4a1f7cfe9`.

| Campo extraído | Positivo | Zero | Ausente na extração | Total de registros |
|---|---:|---:|---:|---:|
| Operação com avião | 4 | 12 | 72 | 88 |
| Tratores e colheitadeiras | 9 | 10 | 69 | 88 |
| Custo total | 31 | 0 | 57 | 88 |

O arquivo contém 89 abas; 88 passam pelo filtro de nome região–UF–ano. Nos exemplos antigos de Bom Jesus da Lapa, o rótulo de avião começa com `1`, enquanto o código exige o prefixo `2 - Operação com Avião`. A categoria de máquinas também muda. Isso comprova falta de harmonização, sem supor que todos os ausentes tenham a mesma causa. Valores ausentes não são zeros.

Os quatro positivos de avião extraídos são **banana-prata, Bom Jesus da Lapa/BA, 2021–2024**, com R$ 280, 400, 520 e 520 por hectare. A mediana de R$ 460 é reproduzível nesse subconjunto. São observações repetidas de um sistema/localidade, não quatro tecnologias independentes. Sua extrapolação a Ceará, a 2018 ou ao setor nacional não foi validada.

Não encontrar ambas as linhas positivas na extração incompleta não estabelece exclusividade tecnológica. Trator/colheitadeira tampouco significa pulverização terrestre: agrega outras operações, limitação que o próprio script reconhece. Mesmo uma tabela completa de custos típicos não é amostra probabilística de produtores.

Consequência: retirar as afirmações sobre exclusividade, adoção majoritária e choque pequeno demonstrado. O peso contábil de uma operação não limita a perda de rendimento, o custo de capital, a escassez de substitutos ou o custo marginal de abater exposição. A série nominal de custo por hectare também não mede diretamente a variância do choque estrutural `σ` de Weitzman. Corrigir primeiro dicionário de rótulos/colunas, cobertura, unidade monetária e estrutura longitudinal.

## 4. A literatura citada contém resultados de contexto, não uma ordem universal

O resumo original de Helfand e House descreve uma aplicação a alface em dois solos do Salinas Valley. O contraste entre eficiência e lucro é resultado daquele exercício sobre instrumentos uniformes, não teorema geral de que impostos dominam toda regulação por quantidade. [Helfand & House, 1995, resumo editorial](https://academic.oup.com/ajae/article-abstract/77/4/1024/51470).

Baixei a tese original de Skevas no repositório da Wageningen. O capítulo 4 identifica o texto aceito em *Agricultural Economics*. Seu modelo simula impostos, subsídios e cotas em agricultura holandesa. As cotas reduzem mais o uso nos cenários considerados, mas as conclusões defendem combinação de instrumentos; eficácia na redução física não é automaticamente dominância de bem-estar. [Skevas, 2012, capítulo 4, §§4.5–4.7](https://edepot.wur.nl/201500); [artigo, DOI](https://doi.org/10.1111/j.1574-0862.2012.00581.x).

Proibição, taxa sobre molécula, taxa sobre método, limite de emissão e zona de proteção regulam margens diferentes. Uma comparação útil precisa declarar o que cada instrumento controla, fiscalização, resposta do produtor e quem recebe benefícios e custos. A opção normativa por proteção mínima ou restrição de direitos pode ser estudada como critério explícito, mas não é um resultado econométrico nem deve ser atribuída automaticamente a uma intenção legislativa não documentada.

## 5. Reavaliação das seis predições explícitas do manuscrito

| Predição em `03-teoria.tex` | Veredito da auditoria | Condição que falta |
|---|---|---|
| Ban melhora saúde; melhora cresce com dose | Plausível, condicional, não confirmada | Uso aéreo real, redução causada pela lei, exposição populacional e composição dos nascimentos; monotonicidade em área de banana não é garantida |
| Melhora maior a jusante | Hipótese de mecanismo | Rede de captação e fluxo, local/tempo de aplicação, persistência química e registro estável; dados SISAGUA do projeto estão suspensos |
| Melhora maior a favor do vento | Hipótese de mecanismo | Variação meteorológica que separe vento de posição geográfica e fonte emissora; vento médio persistente não resolve seleção espacial |
| Aplicação terrestre aumenta intoxicação ocupacional | Sinal não necessário | Exposição dos trabalhadores depende de volume, equipamento, proteção, formulação e substituição; ausência de aumento não refuta toda substituição |
| Intoxicação autoprovocada deve ficar invariável | Controle negativo candidato | Lei pode alterar compra, estoque, renda e acesso; não proibir molécula não garante esses caminhos constantes |
| Ban impõe custo privado | Restrição plausível sob condições fixas | Custo realizado depende da alternativa, produtividade, adaptação, cumprimento e tendências; diferença contábil entre sistemas não é efeito causal |

O princípio de controle negativo exige que ele não seja causado pela exposição de interesse e compartilhe fontes relevantes de viés. Aplicação ao caso: a invariância da intoxicação autoprovocada é uma hipótese adicional a defender; movimento conjunto de duas séries não identifica sozinho a causa do movimento. [Lipsitch, Tchetgen Tchetgen & Cohen, 2010, seção “Choice of negative controls”](https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/).

Uma DAG a desenvolver deve incluir lei → aplicação aérea/terrestre → exposição ambiental e ocupacional; lei → custos/renda/migração; exposição → perda fetal e saúde entre sobreviventes; e condições agrícolas/clima → aplicações e saúde. A inclusão de óbito fetal ajuda a interpretar seleção, mas não observa todas as concepções ou perdas precoces. Uma evidência nula imprecisa não elimina essa via.

## 6. Proveniência e limites

O trabalho combinou inspeção do manuscrito e scripts, reexecução do extrator Conab, conferência bibliográfica e leitura de fontes originais. O arquivo PDF de Skevas foi lido por extração textual; não dependi de leitura de gráficos. Weitzman e Helfand tiveram trechos/resumo primários recuperados pela busca, mas downloads integrais foram bloqueados nesta sessão. O texto do controle negativo foi recuperado no índice de PMC; a abertura direta encontrou CAPTCHA. Esses limites não são tratados como inexistência das fontes. Não fiz revisão sistemática PRISMA, avaliação clínica individual, estimação de custo causal ou ranking empírico de políticas.

As deduções algébricas e críticas de aplicação estão identificadas como análise desta auditoria. Ferramentas de IA participaram da pesquisa e redação. A conclusão é **reformular a ponte entre ensaios e reparar a extração antes de calibrar**, preservando as questões científicas e as estimativas históricas com seus rótulos adequados.
