# Auditoria de código, estimandos e reprodutibilidade

Data: 23/09/2026. Escopo: inspeção independente de `work/projeto-pesquisa`, sem alteração de código ou manuscrito e sem aquisição de microdados. Foram usados os protocolos ARS `deep-research` e `academic-paper-reviewer` como apoio à revisão; os achados abaixo derivam dos arquivos e das verificações locais, não de pareceres anteriores. Relatório produzido com assistência de IA.

**Veredito: revisão maior antes de apresentar a conclusão empírica como estabelecida.** O projeto tem testes úteis e registra várias limitações honestamente. Entretanto, a cadeia hipótese → estimando → inferência → conclusão está interrompida: o Holm testa outra quantidade, o MDE pertence a outra comparação, e um intervalo que exclui zero é descrito como compatível com zero. Há ainda falhas de cobertura/proveniência que precisam ser corrigidas antes de nova estimação real.

Os caminhos nas referências abaixo são relativos a `C:/Users/DELL/Documents/Codex/2026-09-23/prior-conversation-with-codex-conversation-role/work/projeto-pesquisa`. As linhas referem-se à cópia inspecionada.

## 1. Achados prioritários

### C1 — Crítico para a conclusão: Holm não testa o estimando principal

**Evidência.** A mudança registrada em `docs/pre-especificacao.md:291` promove `level`/ATT a principal. Contudo, `scripts/estimate/09_holm.py:43`, `:107` e `:211–238` importam e aplicam `estima()` do script 04, uma inclinação OLS de ΔY sobre dose (`scripts/estimate/04_robustness.py:106–121`). Não usam `nivel()`, definido separadamente em `04_robustness.py:327–334`, nem os coeficientes/erros do sieve. Não aplicam o filtro GAEZ da definição 4. A tabela confirmatória continua declarando ACR, inclusive no plano (`docs/pre-especificacao.md:235–245`).

**Impacto.** Os valores-p ajustados não autorizam a frase “nenhuma hipótese confirmatória rejeita” sobre o ATT promovido a principal; tampouco são um teste da curva não paramétrica inteira. Trata-se de outro funcional com outra ponderação. Demonstração sintética executada: doses `[0,0,0.1,1]`, diferenças `[0,0,-100,10]` produzem ATT binário **−45** e inclinação usada pelo Holm **+34,9823**. Nem o sinal precisa coincidir.

**Correção necessária.** Fixar qual família permanece confirmatória após a troca, qual estimando entra em cada hipótese, qual amostra e qual procedimento produz seus valores-p. Reestimar e aplicar Holm a esses valores-p. Preservar a família original como originalmente especificada e classificar a mudança pós-resultado como tal.

### C2 — Crítico para a interpretação: meia-largura e MDE foram transformados em regra de evidência

**Evidência.** `03_contdid.R:556–562` declara “falsifica 15 g?” apenas se `1.96*SE <= 15`, ignorando a estimativa. `04_robustness.py:545–554` usa comparação entre `abs(beta)` e MDE para classificar achado. `paper/secoes/06-diagnostico-poder.tex:78–85` informa **−36,19**, IC **[−66,51; −5,87]**, mas o parágrafo seguinte afirma compatibilidade com zero. O IC exibido não contém zero. Além disso, −36,19 em módulo supera o MDE de 33,4 usado no texto, embora esse MDE não pertença ao estimando correspondente.

**Impacto.** Precisão planejada, significância observada, relevância econômica e equivalência são perguntas distintas. Largura isolada não testa nem efeito mínimo nem equivalência. Por exemplo, IC [20,30] tem meia-largura 5<15 e seria marcado “falsifica”, embora todos os seus valores excedam +15. IC [−66,51;−5,87] exclui +15, embora a rotina diga não por largura excessiva. Nenhum desses exemplos resolve validade causal ou inferência com poucos controles.

**Correção necessária.** Reportar estimativa, IC e limitações do procedimento que o gerou. Para refutar benefício ≥15 g, formular teste unilateral específico e usar o limite superior adequado; para equivalência, definir margens e procedimento próprio. Um limite causal de “até 60 g” não decorre de concordância aproximada de estimadores que usam populações diferentes. A crítica correta ao IC do contdid é sua validade sob as hipóteses e o número de controles, não dizer que ele inclui zero.

### C3 — Alto: MDE de 33,4 g não corresponde às comparações estimadas

**Evidência.** `scripts/data_prep/01_check_dose_variation.py:967–980` define tratados pelo decil positivo e controles como **todos os demais municípios** (`g0=dose.size-g1`): 17×167 no cenário documentado. Já `07_honestdid.R:93–98` e `08_synthdid.R:93–100` usam decil versus área zero com filtro GAEZ: aproximadamente **17×14**, ou 17×15 sem filtro. O ATT agregado do script 04 compara todos os positivos versus zeros: **169×15**, novamente outro alvo.

**Impacto quantitativo.** Mantendo, apenas para ilustração, o mesmo DP de tendências, trocar 17×167 por 17×15 aumenta MDE pelo fator **1,3915**; 33,4 vira **46,48 g**. Para 17×14 o fator é **1,4176**, dando **47,35 g**. Não são novos MDE estimados: mudam apenas o termo amostral da fórmula antiga; dispersões, janelas e pesos também precisam ser recalculados.

**Correção necessária.** Fazer diagnóstico de poder específico para cada estimando, usando os municípios, períodos e pesos efetivamente incluídos. Não comparar o coeficiente de inclinação (gramas por unidade da dose normalizada) com um MDE de diferença binária em gramas sem um contraste substantivo comum.

### C4 — Alto, reproduzido: meses/anos sem SIM viram mortalidade fetal zero

**Evidência.** `scripts/data_prep/03_clean_fetal_deaths.py:410–424` faz junção externa com SINASC e preenche todas as contagens fetais ausentes com zero, sem verificar cobertura de SIM. Seu padrão continua 2015–2022 (`:82`). SINASC pode ser estendido até 2024 por argumento, mas o Makefile não sincroniza janelas entre fontes.

**Reprodução.** Fonte fetal com dois óbitos em janeiro/2022; SINASC com cem nascimentos em janeiro/2022, janeiro/2023 e janeiro/2024. A função devolve taxas **0,019608; 0; 0**, todas com `sem_denominador=False`. Os últimos dois valores deveriam ser ausentes por falta da fonte, não zeros observados.

**Impacto.** Uma atualização apenas do SINASC fabricaria queda pós-ban no segundo desfecho confirmatório e poderia produzir uma falsa narrativa de seleção para nascimento vivo. O painel já contém tratamento mais cuidadoso para a cobertura do SINAN (`05_build_panel.py:371–383`); isso não foi estendido ao SIM.

**Correção necessária.** Usar manifesto de cobertura por fonte/UF/ano ou mês; preencher zeros apenas dentro de cobertura comprovada. Se não houver nascidos vivos observados para um município-mês com óbito fetal, não transformar ausência do denominador em taxa um sem excluir/marcar essa observação na estimação.

### C5 — Alto: o alvo `real` ainda pode executar SIM simulado ou reutilizar SIM antigo

**Evidência.** `Makefile:154` usa `03_clean_fetal_deaths.py --fonte auto`; esse dispatcher cai em simulação se os transportes falharem (`03_clean_fetal_deaths.py:733–742`). A fonte simulada grava sufixo separado (`:882–888`), mas o painel real procura o nome sem sufixo (`05_build_panel.py:646–650`). Ausência fetal é tolerada (`:202–205`), e um arquivo real antigo, se presente, continua sendo lido. `09_holm.py:208–210` pula desfecho ausente e reduz a família (`:238–243`).

**Nuance importante.** O fluxo canônico não insere automaticamente o arquivo `__simulado` no painel real: o sufixo impede isso. O defeito concreto é executar simulação dentro do alvo real e seguir com fetal ausente ou antigo; não há garantia de que todas as fontes sejam da rodada atual. Em paralelo, a junção remove a coluna interna `fonte` (`05_build_panel.py:208`), e o rótulo final é deduzido do nome do arquivo PAM (`:666–667`), não da proveniência de cada componente. Com um componente mal nomeado, sua origem simulada seria apagada e o painel seria rotulado real.

**Correção necessária.** Transporte explícito e falha dura no SIM; manifesto de entradas com hash, cobertura, origem e extração; validação interna antes da junção; bloquear família incompleta. O teste `test_makefile_alvo_real_nunca_cai_no_simulado` (`tests/test_data_prep.py:360`) passa apesar dessa exceção.

### C6 — Alto: comparação ATT versus derivada não é teste de ATT=ATE/SPT

**Evidência.** `03_contdid.R:576–592` propõe comparar os arquivos `level` e `slope` como diagnóstico da igualdade ATT(d|d)=ATE(d), chegando a afirmar que divergência significa que SPT não se sustenta. Porém, o script extrai `att.d` para um e `acrt.d` para o outro (`:425–443`): nível e derivada, com dimensões diferentes. Nenhuma estimativa separada de ATE(d) é produzida nesse bloco.

**Impacto.** Divergência entre valor de uma função e sua derivada não testa a igualdade entre duas funções de nível, nem identifica selection-on-gains. O desenho pode sondar implicações de pré-tendências, mas o código anunciado não executa esse teste de identificação.

**Correção necessária.** Remover esse diagnóstico e distinguir estimação sob hipóteses de testes de suas implicações observáveis. A execução de `10_spt_pretrend.py` permanece útil como sonda de uma restrição pré-tratamento, não valida SPT.

## 2. Outros problemas materiais

| Gravidade | Achado e evidência | Implicação |
|---|---|---|
| Alto | `--exposicao` em `03_contdid.R` é lido em `:160` e gravado como metadado em `:484–485`, mas o colapso usa só datas (`:302–328`) e dose. Não se exige que a coluna exista. | Trocar gestação inteira por trimestre não muda a estimação, apenas seu rótulo. É legítimo estimar contraste de coortes inteiramente expostas, mas isso precisa ser descrito e o argumento inoperante deve ser removido ou implementado. |
| Alto | `07_honestdid.R:108–110` e `08_synthdid.R:99–100` agregam o ano de 2019 inteiro como pós; `03_contdid.R` exclui janeiro–setembro/2019. | Sensibilidades mudam simultaneamente grupo, estimando e exposição. Não são somente alternativas de inferência para o resultado principal. |
| Alto | Corte superior diário de 19/12/2024 não é implementado: `02_clean_births.py:285–298` conserva apenas ano/mês no filtro; `05_build_panel.py:81`, `:346–351` aceita dezembro/2024 inteiro. Os padrões dos scripts de nascimento e SIM terminam em 2022. | O pipeline padrão é 2015–2022; se estendido, inclui nascimentos após o marco de drones dentro de dezembro. A data exata exige corte anterior ao colapso ou exclusão conservadora do mês. Não foi demonstrado que esse bug afetou estimativas históricas, pois seus dados não estão nesta cópia. |
| Alto | `03_contdid.R:246–263` verifica existência, mas não completude de GAEZ; o montador cria a coluna inteiramente NaN quando a base não existe (`05_build_panel.py:416–419`). | `--d-zero 4` pode manter os zeros sem aptidão por não satisfazerem `aptidao>corte`, rotulando-os como definição 4. Já 07/08 exigem `aptidao<=corte` e os excluem: amostras divergentes sob missingness. |
| Alto | `09_holm.py:86–94` não trata NaN. Reproduzido: `holm([NaN,0.04])` retorna `[0.08,0.08]`. | Um teste indefinido ganha valor-p finito. Deve preservar ausência e não declarar família válida. |
| Moderado | `03_contdid.R:468` e `:630` capturam erros e seguem, sem saída não-zero ao falhar estimação. CSV antigos não são invalidados. | `make` pode continuar e artefatos anteriores parecerem resultados da rodada nova. |
| Moderado | `04_robustness.py:447–471` anuncia sensibilidade ao nível mas chama `estima()` da inclinação; a inferência adicional de nível (`:662`) usa a definição base, sem reestimar a definição 4. | A implementação nova reconhece 15 controles, mas não completa a inferência do ATT primário sob seu zero ratificado. |
| Moderado | `04_robustness.py:382` chama `p_welch` à cauda normal, sem graus de liberdade de Welch–Satterthwaite. | O rótulo pode ser lido como teste t de Welch finito-amostral; na verdade é aproximação normal usando sua fórmula de variância, como parte dos comentários reconhece. |
| Moderado | Saídas `robustez_inferencia.csv`, `robustez_perfil_dose.csv` e `holm_confirmatorios.csv` têm nome fixo; os CSV do contdid separam desfecho/zero, mas não janela, exposição, fonte ou seed. | Rodadas distintas sobrescrevem sensibilidades e simulados podem ocupar nomes de resultados; coluna interna de origem não substitui separação e manifesto. |
| Moderado | `03_contdid.R:324–329`, `04_robustness.py:93–102` fazem média dos meses disponíveis, exigindo apenas algum pré e algum pós. | Ausência seletiva muda suporte temporal e peso implícito por município. Para event study, contar linhas máximas (`03_contdid.R:613`) não garante meses idênticos se houver lacunas diferentes. |

## 3. Dose, zero, seleção e estado das hipóteses

**Dose implementada.** `05_build_panel.py:153–173` utiliza hectares médios divididos pelo maior valor municipal: não é área por residente, por área municipal, nem exposição individual. Portanto, pode refletir escala agrícola e tamanho municipal além de intensidade. O GAEZ não entra como instrumento numa estimação IV no código auditado: serve para construir/restringir controles. O alvo econômico deve ser definido como efeito reduzido do regime segundo essa proxy até existir mensuração de aplicação aérea. Relevância empírica de aptidão para plantio não verifica exclusão ou monotonicidade de um instrumento.

**Zero.** A comparação efetiva toma ausência de banana como ausência de tratamento. O Censo 2006 de equipamento não exclui aplicação por prestadores, mudança entre 2006 e 2018, deriva ou controle vetorial. Os próprios docs 18–19 reconhecem uma ameaça de cessação em 2011 e solicitam evidência de aplicação em 2015–2018. Assim, nem “zero validado” nem “tratados genuínos confirmados em 2019” decorrem do que o código mede. A ausência de dados atuais de aplicação é a lacuna central, não um problema que GAEZ ou bootstrap resolvam.

**Seleção.** Peso observado é entre nascidos vivos com peso válido (`02_clean_births.py:304–313`). Comparar SIM e SINASC é diagnóstico substantivamente adequado, mas não identifica efeito sobre uma população fixa de fetos ou sobreviventes. Óbito fetal não significativo não exclui seleção quando o teste é impreciso. As perdas precoces e alterações de registro não são captadas integralmente pelo denominador “coorte registrada”. O script usa janela fixa de nove meses também para o desfecho fetal, cujas idades de perda são heterogêneas: é preciso definir o calendário desse estimando separadamente. Contagens de peso/gestação válidos existem, mas não há auditoria causal de sua evolução por grupo incorporada na estimação.

**Pesos.** Média simples dos pesos médios mensais não é peso médio de todas as crianças de cada município-período. Demonstração: meses com 1 criança de 2500 g e 100 de 3500 g têm média de médias **3000 g**, contra **3490,10 g** por criança. Ponderar dentro do município-período pelo número de pesos válidos não obriga ponderar municípios pelo tamanho: são duas decisões distintas. A recusa genérica de ponderação na pré-especificação não resolve qual é o alvo dentro do município.

| Hipótese/compromisso | Estado da auditoria |
|---|---|
| H1: benefício no peso sob o ban | Não estabelecido. A família original é sobre ACR; a principal reportada passou a ATT depois de observar a curva. O Holm não testa esse ATT. |
| H2: redução do óbito fetal | Não estabelecida. A taxa tem bug de cobertura e a inferência confirmatória opera sobre inclinação OLS. Ausência de rejeição não elimina seleção. |
| Tendências paralelas | Suposição viva. Placebos e sensibilidades disponíveis, mas em estimandos/amostras/janelas diferentes. |
| Strong parallel trends | Não validada. O diagnóstico level×slope é inválido; placebos sondam implicações, não identificam a hipótese forte. |
| Ausência de antecipação | Não verificada. Janela PAM 2015–2018 sucede a notícia de 2015; a sensibilidade 2010–2014 não é rodada no `make real` canônico. |
| Proxy corresponde à aplicação removida | Não verificada. Censo 2006 é calibração histórica; ameaça 2011 e prática em 2018 permanecem abertas nos docs 18–19. |
| Controle sem tratamento/spillovers | Não verificado. Baixa aptidão e banana zero não provam ausência de aplicação/deriva ou controle vetorial. |
| Falsificação/equivalência ±15 g | Não executada corretamente. O código avalia largura/planejamento, não o teste correspondente. |
| Canal água | Suspenso nos documentos recentes por mensuração; README ainda o apresenta como componente ativo. |
| Calendário/poucos tratados propostos no doc 19 | Proposta exploratória, não efeito estimado. Sem painéis locais, não foi possível calcular seus MDE reais. |

## 4. Documentação e reprodutibilidade

O manuscrito está atrás das revisões internas. `paper/secoes/04-identificacao.tex` ainda declara a curva principal, quatro construções de zero “todas reportadas”, registro anterior ao contato com dado real e permutação como inferência particularmente conservadora. `docs/pre-especificacao.md:3–39` esclarece que é plano pré-estimação, não pré-registro; sua tabela de desvios altera o alvo (`:291`), mas o corpo e o rodapé mantêm frases de um estado anterior (`:105`, `:245`, `:307–308`). `README.md` continua prometendo GAEZ como instrumento, água, PSM e Conley–Taber; nem todos são implementados no pipeline executado.

O paper também converte poder de 80% de um pré-teste em “o placebo exclui” tendências de 11 g (`06-diagnostico-poder.tex:178`), interpretação repetida em `06_pretrends.R:153`. Poder prospectivo não é limite de confiança sobre tendência após não rejeição. O mesmo texto ainda diz que diluição e falta de poder são leituras concorrentes e recomenda baixar corte para encorpar tratamento (`06-diagnostico-poder.tex:369–395`), enquanto os docs 17–19 reconhecem diluição como mecanismo e a escassez dos controles do estimando agregado.

**Artefatos disponíveis nesta cópia.** `data/raw`, `data/processed` e `data/geo` contêm apenas `.gitkeep`. Estão presentes scripts, documentação, leis em CSV, bibliografia, fontes LaTeX e um briefing PDF. Não estão presentes painel, curva estimada, Holm, resultados de robustez, arquivos GAEZ ou microdados. Isso é coerente com o gitignore e não prova inexistência na máquina original, mas impede verificar numericamente os efeitos, EP, contagens e MDE históricos. Ausência de artefatos agregados versionados, manifesto e geração automática de tabelas deixa o texto quantitativo desacoplado do código.

`requirements.txt` fixa `pysus==2.10.0`, mas deixa quase todas as demais dependências Python sem versão. Há `renv.lock` para R, o que é positivo. `Rscript` e `make` não foram localizados no PATH da sessão; não se executaram contdid, HonestDiD, pretrends ou synthdid. Esta auditoria não afirma ter validado internamente o pacote R fixado no lock: confirmou as chamadas e transformações do projeto.

## 5. Checagens executadas

1. Inventário de arquivos, leitura de CLAUDE, README, pré-especificação, docs ARS 17–19, identificação/resultados do paper, Makefile, rotinas centrais de preparação/estimação e testes; buscas por cobertura, fonte, cortes, zero, dose, multiplicidade e MDE.
2. Runtime Python empacotado do Codex: tentativa de pytest terminou imediatamente por **pytest ausente**; nada instalado.
3. Python do sistema: primeira tentativa de suíte teve **4 passes e 3 erros de setup** por acesso ao diretório temporário padrão, não por falha de função do projeto.
4. Retentativa com temporário exclusivo no workspace: `python -m pytest tests/test_data_prep.py -q --disable-warnings --maxfail=5 --basetemp <workspace>/work/auditoria-code-pytest` terminou com **274 passed, 2 warnings, 80,64 s**. Isso valida a suíte existente; não elimina os casos ausentes demonstrados neste relatório.
5. Script sintético independente `work/auditoria_code_checks.py` executado com sucesso, reproduzindo: zeros fetais fora da cobertura; divergência de sinal ATT×inclinação; fatores de MDE por composição de grupos; NaN convertido em p finito no Holm; perda de proveniência na junção; retenção de dezembro/2024 inteiro; distinção entre média mensal e por criança. Nenhum resultado desse script é evidência empírica sobre Ceará.

**Não executado:** aquisição de microdados; estimação real; reprodução dos números do artigo; restauração de ambiente R; testes de rede ou eficácia jurídica; apuração de processo de 2011; envio de LAI; alteração do manuscrito/código. Nenhuma dependência global foi instalada.

## 6. Ordem de correção recomendada

1. Congelar uma tabela de estimandos: parâmetro, unidade/população, dose, zero, janela, pesos, hipótese e inferência. Distinguir original pré-estimação, mudança pós-resultado e novo ciclo exploratório.
2. Corrigir cobertura SIM, proveniência, falha dura e tratamento de NaN; adicionar testes que reproduzam os contraexemplos acima.
3. Reconciliar ATT principal com Holm e com inferência em 14/15 controles; recalcular MDE na comparação efetiva. Reportar permutação como sensibilidade sob intercambiabilidade, não exatidão automática.
4. Gerar resultados e tabelas a partir de uma rodada identificada por manifesto; conservar agregados não sensíveis, cobertura e hashes suficientes à auditoria.
5. Atualizar o paper antes de inferir ausência de benefício, equivalência ou seleção. Só depois decidir o novo desenho de calendário, condicionado à mensuração de aplicação efetiva no pré-ban.
