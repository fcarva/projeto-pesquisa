# 18 — Medir o método, não a cultura: Fase 1 (escopo)

*ARS `deep-research`, modo `full`, Fase 1 de 6. Oversight: alto — a Fase 2 não
abre sem confirmação. 2026-09-23. Pedido do pesquisador: "voltar ao academic
research e buscar uma forma de tentar resolver os problemas dessa pesquisa".*

> **Estado: AGUARDANDO CONFIRMAÇÃO.** A sondagem da Fase 1 trouxe três achados.
> O primeiro abre uma fonte que o projeto não tinha considerado. O segundo
> muda onde procurar poder. O terceiro diz por que o primeiro, sozinho, não
> basta.
>
> 1. **Há um registro federal da aplicação aérea no pré-período que o projeto
>    nunca pediu.** A IN MAPA nº 2/2008 obriga toda empresa de aviação agrícola
>    a entregar um **relatório mensal de atividades** à Superintendência
>    Federal de Agricultura (SFA). O projeto concluiu que "o MAPA não tem
>    profundidade histórica" olhando só o SIPEAGRO, que começa em 2021 (§3.1).
> 2. **O análogo mais próximo identifica pelo calendário, não pelo corte
>    transversal.** Calzada et al. estimam o efeito principal com bebês cujo
>    primeiro trimestre coincidiu com os meses de fumigação intensa. O poder
>    pode vir da variação no tempo dentro do mesmo município, onde a diluição
>    entre municípios não o destrói (§3.2).
> 3. **Medir o tratamento corrige o viés, mas não compra poder no corte
>    transversal.** Com os 7 municípios que tinham avião em 2006, o efeito
>    mínimo detectável da comparação entre municípios fica na ordem de 50 g
>    (§4.1). A medida precisa vir junto com o desenho de calendário.

---

## 0. O problema, em uma frase

A dose mede intensidade da bananicultura, não pulverização aérea. Pela
classificação de 2006, 15 dos 17 municípios do decil e 162 dos 169 com área
positiva não tinham aplicação por aeronave (flag 7; doc 17 §1.3, que trata isso
como calibração condicional). Dessa diferença saem os cinco problemas abertos:

| problema | onde está documentado |
|---|---|
| atenuação: \(\theta = VPP\cdot ATT\) sob as hipóteses do Corolário 1 | doc 16 §4 |
| poder ≤ 11% para os efeitos do análogo | doc 16 §7 |
| o nível agregado depende de 15 controles | doc 17 §1.1 |
| a fronteira CE × RN tem poucos tratados e controle que ganha drone em 2021 | doc 15; doc 16 §8 |
| o Ensaio 2 não recebe curvatura do Ensaio 1 | doc 17 §6 |

Os quatro primeiros têm a mesma raiz. Resolver a medida do tratamento é
condição para qualquer um deles, e é por isso que esta rodada começa por ela.

---

## 1. RQ Brief

### Pergunta candidata

> **Que dado e que desenho permitem estimar o efeito da retirada da
> pulverização aérea sobre desfechos perinatais no Ceará, com o tratamento
> medido pelo método e não pela cultura, e com poder para os efeitos que a
> literatura documenta, de 30 a 150 g sob exposição alta?**

### Subperguntas

1. **Medida.** Existe registro administrativo da aplicação aérea no Ceará antes
   de 2019, por município e mês? Onde, com quais campos e por qual acesso?
2. **Desenho.** Com essa medida, ou sem ela, que desenho entrega poder com
   poucos municípios genuinamente tratados? São três candidatos. (a) O
   calendário: 1º trimestre × meses de pulverização × antes e depois do ban,
   dentro do município. (b) Poucos tratados contra doadores de fora do Ceará.
   (c) A fronteira.
3. **Poder e plausibilidade.** Que efeito mínimo detectável cada desenho
   entrega, contra os 80–150 g da versão publicada de Calzada et al. e os
   38–89 g da versão de trabalho? E que VPP e que fração de nascimentos
   expostos cada desenho exige?

### FINER

| critério | avaliação |
|---|---|
| **F**easible | ⚠️ **é o critério em risco.** A subpergunta 1 depende de LAI (prazo federal de 20 + 10 dias), e o dado pode não ter sido guardado. As subperguntas 2 e 3 são factíveis com o que o projeto já tem |
| **I**nteresting | ✅ alto. Resolve a crítica central do parecer (comentários 5 e 7; bloco geral 1) |
| **N**ovel | ✅ a busca não achou avaliação de pulverização aérea no Brasil com registro de aplicação. Os análogos que mediram aplicação são de Califórnia, Colômbia e Equador (doc 13) |
| **E**thical | ✅ dado agregado. ⚠️ Relatórios e receitas trazem nome e CPF de pilotos, agrônomos e produtores: os pedidos pedem supressão (Lei 12.527, art. 7º, §2º) |
| **R**elevant | ✅ dez estados discutem normas análogas; o STF validou a cearense |

### Fronteiras de escopo

**Dentro:** o Ensaio 1; janela 2010–2024, incluindo o período anterior ao
marco de notícia de 2015; unidade município × mês; fontes de medida; desenhos;
poder.

**Fora:** o Ensaio 2, salvo consequências; o canal-água (SISAGUA suspenso);
drones depois de 19/12/2024; geocodificação submunicipal. Esta última é vedada
pela §7 da pré-especificação e, de todo modo, o SINASC público só traz o
município.

---

## 2. Blueprint de metodologia (da pesquisa desta rodada)

| dimensão | escolha | razão |
|---|---|---|
| Paradigma | pragmatista, a serviço de inferência causal | a pergunta é "o que funciona", com critério de identificação |
| Método | revisão estruturada de **dados e desenho**, em três frentes | ver abaixo |
| Dados | secundários: normas, literatura e o que o projeto já tem. Pedidos LAI saem redigidos, não protocolados | a ARS não roda experimento (CLAUDE.md) |
| Quadro analítico | **matriz de decisão**: para cada rota, ganho de VPP, efeito mínimo detectável, hipótese de identificação, tempo até o dado e compatibilidade com a pré-especificação | torna comparável o que hoje está espalhado em seis documentos |
| Validade | conferência na fonte primária (texto normativo, DOI) e os três checkpoints do *devil's advocate* | regra da casa: referência não conferida não entra |

**As três frentes da Fase 2:**

| frente | o que procurar | fontes |
|---|---|---|
| F1 — registros | todo registro legal da aplicação aérea no pré-período: quem guarda, campos, prazo de guarda, acesso | IN MAPA 2/2008 e IN 37/2020; Portaria MAPA 298/2021; Decreto 4.074/2002, art. 66; Lei CE 12.228/1993, art. 8º; RBAC 137 (ANAC); relatórios de gestão da SFA-CE |
| F2 — medida e identificação na literatura | como os estudos que mediram aplicação aérea identificaram o efeito, sobretudo por calendário | Calzada et al. (texto integral, pendente desde o doc 13); Camacho & Mejía (2017); Larsen et al. (2017); Rull & Ritz (2003); Dias et al. (2023); sazonalidade no nascimento, como Currie & Schwandt (2013) ⬜ |
| F3 — inferência com poucos tratados e erro de classificação | procedimentos para 2 a 7 tratados contra muitos doadores | Conley & Taber (2011); Ferman & Pinto (2019); controle sintético com inferência conformal (Chernozhukov, Wüthrich & Zhu, 2021) ⬜; Denteh & Kédagni (Corolário 1) |

⬜ = a conferir na Fase 2. ⚠️ O proxy da sessão remota bloqueia gov.br,
planalto, Crossref e a maioria das fontes legislativas. A F1 depende da
máquina local para os textos integrais (§5).

---

## 3. O que a sondagem da Fase 1 encontrou

### 3.1 🟢 Os relatórios mensais da IN MAPA nº 2/2008

| elemento | o que se sabe | estado |
|---|---|---|
| **Art. 9º:** cada operação gera um **relatório operacional** (Anexo I) | localização da lavoura, mapa DGPS de cada faixa aplicada, produto, área tratada, meteorologia, profissionais responsáveis. A redação anterior à IN 37/2020 incluía cópia do receituário agronômico | trecho da IN pelo índice de busca, e resumo de buscador; ⬜ texto integral |
| guarda do relatório operacional | **mínimo de 2 anos**, pela empresa | resumo de buscador ⬜. Consequência: os de 2015–2018 provavelmente já não existem nas empresas |
| **Art. 14:** **relatório mensal** de atividades (Anexo V), entregue à SFA | trecho literal: *"As empresas de aviação agrícola, pessoa física ou jurídica, deverão apresentar o relatório mensal [...] Anexo V, com informações [...]"*. Prazo: até o 15º dia do mês seguinte; empresa de outra UF entrega à SFA **do estado onde atuou** | trecho do gov.br pelo índice de busca; ⬜ campos do Anexo V e redação vigente em 2010–2018 |
| o MAPA de fato recebia e contava esses relatórios | o relatório de gestão de 2012 da SFA-SP traz um indicador de "Recebimento de Relatórios Mensais (Irrav)" e comenta a "declaração de área aplicada, por aviação agrícola" | trecho pelo índice de busca; é indício de prática, não prova para o Ceará |
| o canal existe até hoje | desde abril de 2023 o envio é por peticionamento no SEI; a página do MAPA mantém planilha-modelo (versão 2026) | página "Relatórios mensais" do MAPA e SINDAG, pelo índice de busca |

**Por que isto importa mais que as outras rotas.** O SINDAG não lista frota
aeroagrícola sediada no Ceará (dado de 2025, doc 11 §3.2), e o SIPEAGRO
registra uma única aeronave convencional no estado, em Limoeiro (lacunas §1-bis).
A hipótese de trabalho é que as aplicações na Chapada eram feitas por empresas
de outras UFs ou por operadores privados. A regra do art. 14 manda o relatório
mensal para a SFA **do estado onde a empresa atuou**, então a SFA-CE é o lugar
onde a aplicação aérea no Ceará deveria estar registrada, mês a mês, desde
2008. Se o Anexo V trouxer município,
cultura e área, é a medida que falta. Ela daria o VPP de 2018, a intensidade
por município e o calendário.

**O que pode dar errado.** O arquivo pode não ter sido guardado: antes do SEI
os relatórios iam por e-mail ou papel. O Anexo V pode não trazer município. O
cumprimento pode ter sido parcial, e o próprio relatório da SFA-SP menciona
problema na declaração de área. E empresas de fora podem ter entregado à SFA de
origem. A minuta do pedido (§6) foi escrita para que cada uma dessas respostas
seja informativa.

### 3.2 🟢 O análogo identifica pelo calendário

Resumo da versão de trabalho (UB School of Economics WP 2021/405, pelo RePEc):
Calzada, Gisbert & Moscoso medem a exposição pelo endereço da mãe e pelo
perímetro das plantações. A **primeira** estratégia compara bebês cujo **primeiro
trimestre coincidiu com os períodos de fumigação intensiva**: redução de 38 a
89 g. A segunda compara plantações de banana fumigadas com outras culturas
fumigadas (29 a 76 g). A terceira usa efeitos fixos de mãe (346 g nas
meninas). A versão publicada (*JAERE*, doi:10.1086/725349) dá 80–150 g sob
exposição alta, pelo resumo que o projeto já tinha.

**O que isto muda.** O endereço não se transporta: o SINASC público só traz o
município. **O calendário se transporta.** O SINASC traz data de nascimento e
semanas de gestação, o que data o primeiro trimestre. O desenho vira uma
diferença tripla dentro do município. Compara bebês cujo 1º trimestre caiu nos
meses de pulverização com os demais, em municípios com e sem aplicação aérea,
antes e depois de 2019. O ban deveria apagar o hiato sazonal onde havia avião.
Isto é a "hipótese sazonal" que o projeto já tinha registrado para o próximo
ciclo (doc 13 §6; doc 14 §7). O que faltava era o calendário, e o relatório
mensal do §3.1 o daria por município.

### 3.3 🟡 O que a sondagem não achou

- **ANAC/RAB**: registro de aeronaves por operador. Diz quem podia aplicar e
  onde tem base, não onde aplicou. Continua sem mapeamento (auditoria de
  mensuração, §5).
- **Relatórios de gestão da SFA-CE**: existem (2007, 2009 e outros, no
  gov.br) e citam relatórios mensais do serviço de sanidade. ⬜ Não se sabe se
  trazem a área aplicada por aviação no estado. Se trouxerem, dariam a **série
  estadual 2010–2018** e responderiam à objeção da crítica ao doc 17: a aviação
  cresceu entre 2006 e 2018? São públicos e só precisam de download local.

---

## 4. ⚠️ Devil's Advocate — Checkpoint 1: **PASS com condições**

### 4.1 🔴 A medida sozinha não compra poder no corte transversal

O efeito mínimo detectável do decil, 33,4 g, vem de 2,8 × 46,86 × √(1/17 +
1/167). Com os 7 municípios que tinham avião em 2006 contra 177, a mesma conta
dá **≈ 50 g**. O efeito sobre a **média do município** é a fração de
nascimentos expostos vezes o efeito individual: com um quarto dos nascimentos
expostos e 115 g, ~29 g. Medir o tratamento elimina a atenuação, mas deixa o
desenho entre municípios abaixo do próprio limiar.

Duas ressalvas atenuam, e nenhuma resolve. Os municípios com avião são maiores
que a média (Limoeiro, Russas), e isso reduz o ruído da média municipal. E a
conta precisa ser refeita com o script 13 quando a lista existir.

**Consequência para a Fase 2:** a subpergunta 2 não é acessória. O desenho de
calendário (§3.2) é o candidato a comprar poder, porque compara nascimentos do
mesmo município e absorve a heterogeneidade entre municípios que infla o
efeito mínimo detectável.

### 4.2 ⚠️ O dado pode não existir, e a resposta tem de ser útil mesmo assim

Guarda de 2 anos nas empresas; relatórios pré-SEI por e-mail ou papel;
cumprimento parcial. O pedido (§6) pede a regra de guarda e a unidade
detentora se o MAPA não tiver o período. "Não temos" fecha a rota com razão
registrada. É o mesmo desenho das minutas da ADAGRI e da SEMACE.

### 4.3 ⚠️ Pré-especificação

Medida nova ou desenho novo é **novo ciclo de análise**. O resultado atual
continua reportado como está. O desenho de calendário precisa ser
pré-especificado **antes** de cruzar a exposição nova com os desfechos. Sem
isso, o número de caminhos possíveis (meses de pico, trimestre, dose) vira
especificação escolhida depois de olhar. O caminho já está previsto: a hipótese
sazonal ficou registrada para o próximo ciclo (doc 14 §7).

### 4.4 ⚠️ O desenho de calendário tem ameaças próprias

- **Sazonalidade do nascimento.** Mães que concebem em estações diferentes
  diferem, e o peso ao nascer tem padrão sazonal próprio (Currie & Schwandt
  2013 ⬜). A diferença tripla remove a sazonalidade estável e a específica do
  município. Não remove uma mudança de sazonalidade em 2019 que seja diferente
  onde havia avião.
- **A estação chuvosa traz outras coisas**: arboviroses, oferta de alimento,
  trabalho sazonal na fruticultura. Tudo isso segue o calendário que,
  presumivelmente, rege a pulverização de fungicida na banana. O fungicida por
  avião está documentado (flag 2); a sazonalidade dele ⬜ é hipótese a
  confirmar na F2.
- **A seca de 2012–2017** muda o calendário agrícola dentro da própria janela
  pré.

A hipótese de identificação é que **o hiato sazonal entre municípios com e sem
aplicação aérea teria ficado estável na ausência do ban**. É testável no
pré-período, com placebos de data como os do script 10.

### 4.5 ✅ O que favorece

- O calendário só exige município e mês, e o SINASC público tem os dois.
- A fonte do §3.1 daria a exposição por município e mês, que é a forma do
  painel.
- Os 15 controles do nível (doc 17 §1.1) deixam de ser o gargalo: o contraste
  principal passa a ser dentro do município.

**Veredito:** PASS com condições. A Fase 2 pode abrir se: (a) a F1 trouxer o
texto integral da IN 2/2008 e do Anexo V, com a redação vigente em 2010–2018;
(b) a F2 ler Calzada et al. inteiro, com a fonte do calendário deles; (c) a
matriz de decisão incluir o efeito mínimo detectável do desenho de calendário.

---

## 5. O que depende da máquina local (proxy remoto bloqueia)

| passo | tempo | para quê |
|---|---|---|
| Baixar a IN MAPA 2/2008 consolidada (gov.br) e copiar os arts. 9º–14 e os Anexos I e V para `docs/legislacao/` | 15 min | confirma os campos do relatório mensal e o destino (SFA do estado onde atuou) antes de protocolar |
| Baixar os relatórios de gestão da SFA-CE 2010–2018 (gov.br, "prestação de contas") e procurar "aviação agrícola" | 30 min | série estadual da área aplicada, se houver: responde se a aviação cresceu depois de 2006 |
| Ler Calzada et al. (*JAERE*, 2023) inteiro | 1 h | de onde veio o calendário de fumigação, e como definiram "período intensivo" |

---

## 6. O que já foi construído (não depende da confirmação)

- **`docs/legislacao/lai-mapa-relatorios-mensais-minuta.md`**: Pedido D, ao
  MAPA pelo Fala.BR, dos relatórios mensais de aviação agrícola com operação no
  Ceará, 2010–2019. É o item com relógio mais longo, porque a LAI federal leva
  de 20 a 30 dias. Por isso vale protocolar antes de a Fase 2 terminar, depois
  do checklist da própria minuta.

---

## 7. Decisão pedida

| opção | o que acontece |
|---|---|
| **A — abrir a Fase 2 como está** (recomendada) | as três frentes, com matriz de decisão no fim |
| B — só a subpergunta 1 (dados) | mais rápida; deixa o desenho para depois de a LAI responder |
| C — voltar ao modo socrático | se a pergunta desta rodada não for a certa |

E, independentemente da opção: protocolar o Pedido D ao MAPA depois do
checklist da minuta.
