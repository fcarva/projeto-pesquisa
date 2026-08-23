# Ensaio 1 — modelagem teórica e empírica

*Lógica de forward engineering: parâmetro-alvo → hipóteses de identificação →
estimação. Escrito **antes** de qualquer estimação, de propósito: implicação
testável fixada depois do resultado é racionalização.*

---

## 1. Arco teórico

### 1.1 A externalidade

A deriva da pulverização aérea é o caso de manual de externalidade negativa: o
custo recai sobre quem não participa da transação nem da decisão. A repartição
física está documentada (Pignati/EMBRAPA, citada na dissertação da Chapada do
Apodi): **32%** da calda fica na planta, **19% se dispersa pelo ar** atingindo o
entorno, **49% fica no solo** e escoa. Os dois canais do Ensaio 1 são,
literalmente, esses 19% e esses 49%.

### 1.2 O ban como instrumento

A Lei 16.820/2019 é uma **cota fixada em zero sobre um método**, não sobre uma
molécula. Três consequências que amarram o modelo:

1. **O tratamento não é o químico.** Nenhum princípio ativo é nomeado no art.
   28-B. Quem continuar aplicando por trator não é alcançado. O efeito
   detectável se restringe à parcela da exposição que dependia do avião.
2. **O tratamento não é só agrícola.** O §2º proíbe também dispersão aérea para
   controle vetorial. Isso contamina o grupo de dose agrícola nula (§4.3).
3. **A reversão de 2024 é troca de instrumento, não revogação.** A Lei
   19.135/2024 substitui a cota zero por regulação de desempenho com zona-tampão
   de 30 m. O Ceará rodou sozinho a comparação que o Ensaio 2 propõe.

### 1.3 A predição testável que liga os dois ensaios

Se o dano marginal é crescente na intensidade de exposição, a remoção do método
produz melhora **crescente na dose**. É essa inclinação — e não o efeito médio —
que o Ensaio 2 precisa para calibrar Weitzman: a regra preço-vs-quantidade
depende das inclinações relativas de benefício e custo marginais, e a inclinação
do benefício marginal é exatamente o que o Ensaio 1 estima. Daí a curva ser o
alvo declarado, e não uma extensão.

Do lado do custo, Lichtenberg, Parker & Zilberman (1988) dão três predições
testáveis que o Ensaio 2 herda e que o Ensaio 1 pode começar a medir: quem **não**
pulverizava ganha com a proibição (24–32% das perdas dos usuários no caso-base
deles, até 80–90% com demanda inelástica); o consumidor carrega a maior parte da
perda de excedente; e em cultura de exportação — melão e banana do Ceará —
**o consumidor estrangeiro** carrega parte relevante.

---

## 2. Parâmetro-alvo

Notação de Callaway, Goodman-Bacon & Sant'Anna (rascunho de 26/01/2024; primeiro
no arXiv em 06/07/2021; NBER WP 32117).

### 2.1 A inversão de sinal que este caso exige

No CGS as unidades saem de não tratadas para uma dose `d`: o tratamento **liga**.
No Ceará ele **desliga**. Mapeamento explícito, porque errar aqui inverte a
leitura de todos os coeficientes:

- `D_i` = **intensidade pré-ban** de pulverização aérea no município `i`.
- O evento é a **remoção** dessa intensidade em 08/01/2019.
- `Y_{t}(d)` = desfecho sob remoção de uma dose `d` de exposição.
- Dose 0 = município que não tinha o que perder — o grupo de comparação.

Consequência: onde DRS e Reynier & Rubin estimam **piora** com o aumento do
químico, aqui se espera **melhora** com a remoção. Sinal esperado positivo para
peso ao nascer, negativo para prematuridade e baixo peso.

### 2.2 Os quatro parâmetros

Com dois períodos, `t = 1` pré e `t = 2` pós:

```
ATT(d|d′) = E[ Y₂(d) − Y₂(0) | D = d′ ]      efeito de nível
ATE(d)    = E[ Y₂(d) − Y₂(0) ]                efeito de nível, população inteira
ACRT(d|d′) = ∂ ATT(l|d′) / ∂l  em l = d       resposta causal nos tratados
ACR(d)     = ∂ ATE(d) / ∂d                    resposta causal populacional
```

Com tratamento binário, nível e resposta coincidem. Com dose contínua, **não** —
e exigem hipóteses diferentes. É a distinção que organiza tudo abaixo.

**Alvo declarado do Ensaio 1: a curva** — `ACR(d)` / `ATE(d)` — acompanhada dos
limites da §5.1. O nível `ATT(d|d)` entra como o degrau barato, sempre reportado.

---

## 3. Hipóteses de identificação

### 3.1 Assumption 4 — paralelismo tradicional

Trajetórias de resultado potencial **não tratado** paralelas entre grupos de
dose. Identifica `ATT(d|d)`.

O que ela **não** entrega: a comparação entre doses. CGS §3.2.2: *"average causal
responses are not identified under a traditional parallel trends assumption"*,
porque *"the selection bias is not identified as we do not observe Y₂(d) for
units that experienced dose d′. Such a result precludes a causal interpretation
of ATT differences across doses."*

Versão agregada, verbatim (Assumption 4-Agg), que é o degrau mais seguro:

```
E[Y₂(0) − Y₁(0) | D > 0] = E[Y₂(0) − Y₁(0) | D = 0]
```

Isto é: binarizar o tratamento e assumir paralelismo sobre o binário.

### 3.2 Assumption 5 — strong parallel trends

Verbatim: *para todo d ∈ D,*

```
E[Y₂(d) − Y₁(0)] = E[Y₂(d) − Y₁(0) | D = d]
```

A evolução média de toda a população, se todos tivessem recebido a dose `d`,
igual à evolução que o grupo de dose `d` de fato experimentou. Identifica
`ATE(d)` e `ACR(d)`.

**O que ela proíbe.** Pelo Teorema C.1, mantida a A4, a A5 equivale a
`ATT(d|d) = ATE(d)` para toda dose. CGS: *"While this condition does not impose
full treatment effect homogeneity, it does rule out selection-on-gains into a
particular dose group."* Ou seja: municípios não escolheram sua intensidade de
pulverização **em função do ganho que teriam** com a política. Substantivamente,
no caso cearense: a intensidade pré-ban foi determinada por aptidão agroclimática
e estrutura fundiária, não por antecipação do benefício de saúde de um ban que
ainda não existia. Essa é a defesa, e ela é razoável — o ban de 2019 não estava
no horizonte de quem decidiu plantar em 2005.

### 3.3 Por que o placebo pré-tratamento não testa a A5

Placebo restringe trajetórias de resultado potencial **não tratado** — evidência
sobre a A4. A A5 envolve `Y₂(d)`: trajetórias sob doses que a unidade **não
recebeu**. No pré-período ninguém é tratado, logo não existe análogo pré-período
da A5. Nenhum event study de leads testa a A5, por mais limpo que saia.

Corolários: (i) placebo limpo apoia a A4, não a A5; (ii) não rejeitar não é
validar; (iii) com antecipação desde 18/12/2018, um placebo em 2017 deixa apenas
2015–2016 como pré-período — dois anos.

---

## 4. Defesa do strong parallel trends — implicações fixadas antes do dado

### 4.1 Diagnóstico 1 — as duas curvas lado a lado (Teorema C.1)

Estimar e plotar **`ATT(d|d)`** (identificada sob A4) contra **`ATE(d)`**
(identificada sob A5). Pelo Teorema C.1, se A4 e A5 valem, as duas coincidem.

- **Convergem** → a seleção-nos-ganhos é desprezível; a curva sob A5 fica de pé.
- **Divergem** → a A5 é rejeitada; o resultado principal migra para os bounds da
  §5.1, e a magnitude da divergência estima o tamanho da seleção.

Compromisso registrado: **a decisão entre curva pontual e bounds é tomada por
este diagnóstico, não por qual dos dois dá o resultado mais bonito.**

### 4.2 Diagnóstico 2 — sinal patológico da ACR

CGS, na aplicação a Acemoglu–Finkelstein, encontram ACR **negativa** na maior
parte das doses positivas e leem isso como suspeita contra a A5 (ou contra o
modelo, ou ambos).

Tradução para este caso: a hipótese registrada é melhora **crescente** na dose.
ACR de sinal invertido em faixa relevante da distribuição é, por default,
**evidência contra a A5** — não achado biológico. Para ser lida como achado
precisa de mecanismo independente que a sustente, e o candidato já está nomeado:
substituição aéreo→terrestre elevando exposição em dose média. Esse mecanismo
tem teste próprio (SIH, §6.1). **Sem confirmação no SIH, ACR invertida é
diagnóstico de hipótese quebrada.**

### 4.3 Identificação parcial — bounds da §5.1

CGS §5.1 oferece o meio-termo: assumida a **direção** do viés de seleção, saem
limites possivelmente informativos. A hipótese direcional, por extenso:

> Para toda dose `d` e para quaisquer grupos de dose `l < h`:
> `ATT(d|l) ≤ ATT(d|h)`
> — grupos de dose mais alta teriam efeito de tratamento maior em qualquer valor
> da dose.

Justificativa substantiva no caso cearense: quem operava o pacote de aviação
agrícola da Chapada do Apodi é quem tinha mais a ganhar com a remoção da deriva,
porque é onde a exposição populacional era maior por unidade de área. A direção
é defensável; o tamanho não é assumido.

Isso entrega identificação parcial sem a premissa heroica e sem depender de um
teste que não existe.

---

## 5. A dose e o grupo d = 0

### 5.1 Construção da dose

Intensidade agrícola pré-ban (PAM/IBGE, média 2015–2018) da cultura-âncora.
**A cultura-âncora não está fixada** e não será fixada aqui — é o Gate 1. Três
fontes independentes convergem para **banana** como a cultura efetivamente
pulverizada por via aérea na Chapada do Apodi (dissertação da UFC: "fungicidas de
classes toxicológicas 1 e 2 nos extensos cultivos de banana"; ADI 7794:
"amplamente utilizada na produção de banana"; Cavalcante 2023 sobre a banana
pós-ban). Convergência é hipótese forte, não escolha.

Usa-se área **plantada**, não colhida: 2012–2017 foi seca severa no semiárido, e
área colhida responde à quebra de safra — endógena ao clima, que é o canal que o
instrumento GAEZ tenta isolar.

### 5.2 O instrumento GAEZ e o que ele não resolve

Receita do Reynier & Rubin: percentil de *attainable yield* = **diferença de
rendimento atingível entre os cenários de alto e de baixo insumo** do FAO-GAEZ
(não o rendimento puro), reescalado a percentil nacional, máximo entre as
culturas relevantes, reescalado de novo, normalizado em [0,1].

**O que resolve:** a endogeneidade de *onde* a cultura de alta pulverização é
plantada.
**O que não resolve:** a endogeneidade de *como* se aplica. O tratamento aqui é
o método, e aptidão agroclimática não prediz escolha de veículo de aplicação. O
instrumento cobre metade do problema. Declarar, não esconder.

### 5.3 O grupo d = 0 — quatro construções, todas reportadas

O zero produzido pela PAM é zero de **proxy** (área nula da cultura), não zero de
tratamento. E há um contaminante com direção: o §2º do art. 28-B alcança
dispersão aérea para **controle vetorial**, de modo que um município sem
agricultura pulverizada mas com controle aéreo de dengue **é tratado** — e esses
tendem a ser os maiores, logo a contaminação correlaciona com porte, que
correlaciona com desfecho perinatal.

| # | Definição | Fonte | O que corrige |
|---|---|---|---|
| 1 | Área nula da cultura-âncora, PAM 2015–2018 | PAM | nada — é a linha de base |
| 2 | Área nula de **qualquer** cultura candidata a aplicação aérea | PAM | falso zero de quem trocou de cultura |
| 3 | (2) + sem operador aeroagrícola e sem pista agrícola registrados | ANAC / MAPA / SINDAG | mede o **método**, não a cultura |
| 4 | Baixa aptidão GAEZ para a cultura-âncora | FAO-GAEZ | não depende de registro administrativo estar completo |

**Teste de contaminação do zero.** Dentro do grupo `d = 0`, quebrar por aptidão
GAEZ. Se os de **alta** aptidão com área zero se comportam como os de **baixa**
aptidão com área zero, o zero é real. Se divergem, o zero é medida — e a
divergência estima a contaminação.

⚠️ **Decisão em aberto, do pesquisador:** controle vetorial entra como exclusão
do `d = 0` ou como parte do tratamento? O ban é de método, e dispersão sanitária
é método aéreo. As duas leituras são defensáveis e dão estimandos diferentes.

---

## 6. Canais

### 6.1 Canal-ar — deriva

Fonte de emissão: **borda dos polígonos de cultivo intensivo** (MapBiomas), não
o centroide municipal — o desenho de Rangel & Vogl precisa de fonte pontual, e a
pulverização aérea é difusa no talhão. Para cada sede/distrito, vetor de
distância e ângulo até o polígono mais próximo, cruzado com direção
predominante do vento (INMET/FUNCEME) na janela de aplicação.

⚠️ **Dois pontos a verificar antes de prometer o teste.** (a) As coleções
recentes do MapBiomas trazem camadas específicas para soja, cana, algodão, café,
cítricos e arroz; **banana e melão provavelmente caem em classes genéricas**
("lavoura perene", "mosaico de usos"). Se for o caso, a alternativa é ponderar o
polígono genérico pela área municipal da PAM. (b) A **janela de aplicação depende
da cultura-âncora**, que não está fixada: outubro–março é calendário de melão
exportação; sigatoka em banana se pulveriza quase o ano todo. A janela de vento
não fecha antes do Gate 1.

Contra-teste do mesmo canal: **SIH/DATASUS**, internações por intoxicação aguda.
Se o produtor migrou para aplicação terrestre, a exposição pontual sobe nos meses
de aplicação pós-ban, mesmo com a exposição difusa caindo. É o teste que
distingue "ACR invertida = achado" de "ACR invertida = A5 quebrada" (§4.2).

### 6.2 Canal-água

Estrutura montante/jusante em ottobacias (ANA), template do DRS, cruzada com
tipo de captação no SISAGUA.

⚠️ **A ressalva estrutural.** O DRS funciona para água **superficial** — eles
mesmos acham efeito maior onde a captação é superficial. Na Chapada do Apodi o
vetor documentado inclui o **Aquífero Jandaíra**, carbonático/cárstico: fraturas
e sumidouros conectam superfície e lençol sem a filtragem lenta de meio arenoso.
Onde o carste manda, a posição na bacia superficial identifica pouco. Daí o
cruzamento com mapa de vulnerabilidade cárstica (CPRM/SGB) — **cuja existência e
disponibilidade pública precisam ser confirmadas antes de o teste ser prometido.**

⚠️ **SISAGUA tem dois usos com coberturas muito diferentes**: tipo de captação
(superficial/subterrânea) é razoavelmente completo; **detecção de ingrediente
ativo** é onde mora a lacuna massiva. Separar. E a falha é provavelmente
**seletiva** — municípios pequenos, vigilância fraca — o que significa ausência
correlacionada com a dose, não ruído.

---

## 7. Ameaças à identificação

| # | Ameaça | Por que morde aqui | Teste / abordagem |
|---|---|---|---|
| 1 | **Seleção para nascimento vivo** | Se o ban reduz óbito fetal, fetos marginais passam a nascer e entram na cauda de baixo peso — o efeito sobre peso médio vem atenuado ou com sinal invertido | Análise conjunta com **SIM** (óbito fetal e infantil); reportar peso condicional e não condicional; considerar limites de Lee |
| 2 | **SUTVA / spillover** | Deriva cruza fronteira estadual; água corre entre municípios. Medir o canal **não** conserta a premissa | Defasagem espacial da dose (exposição do vizinho) como regressor; exclusão de municípios de fronteira como robustez; sensibilidade da unidade (município / bacia / região imediata) |
| 3 | **Antecipação** | ALECE aprovou em 18/12/2018; quatro anos de tramitação pública antes | Leads cobrindo 2015–2018; 2019 como ano de transição, possivelmente descartado (Reynier & Rubin descartam a fase de transição) |
| 4 | **Erro de medida na dose** | Área plantada é proxy de intensidade agrícola, não de pulverização aérea. Atenua o efeito | Definições alternativas de dose; instrumentação por GAEZ; bounds; declarar a atenuação como direção conhecida do viés |
| 5 | **Falácia ecológica / agregação** | Exposição municipal inferindo desfecho individual | Seção própria de robustez; heterogeneidade por características maternas do próprio SINASC; sensibilidade à escala |
| 6 | **Contaminação do d = 0** | Controle vetorial aéreo alcança municípios de dose agrícola zero, e correlaciona com porte | Quatro definições de zero (§5.3) + teste de quebra por aptidão GAEZ |
| 7 | **Poucos clusters tratados** | O *n* efetivo é o de municípios, não o de bebês | **Conley–Taber**, wild-cluster bootstrap; reportar MDE junto do coeficiente |
| 8 | **Lacuna de enforcement** | Proibir método ≠ eliminar prática | Auto de infração / fiscalização estadual, se houver série; tratar como atenuação |
| 9 | **Substituição de método** | Terrestre ao nível do solo pode elevar exposição residencial | SIH (§6.1); PAM e PIB agropecuário para separar de canal de renda |
| 10 | **Segundo evento (2024)** | Lei 19.135/2024 troca cota zero por zona-tampão | Janela principal cortada em 19/12/2024; o pós-2024 vira objeto do Ensaio 2, **não** DiD escalonado — o evento é simultâneo |

---

## 8. Inferência

Poucos clusters intensamente tratados e desfecho de cauda: **Conley–Taber (2011)**
e wild-cluster bootstrap, não erro-padrão agrupado convencional. Todo coeficiente
publicado vem acompanhado do **efeito mínimo detectável** implicado pelo desenho
— ver a nota de poder em `02-research-plan-summary.md`, que mostra a distância
entre a conta ingênua (9,9 g com três municípios tratados) e a conta honesta
(16 a 65 g, conforme a dispersão das tendências municipais).

**A colisão a declarar em limitações:** a hipótese registrada é que o efeito se
concentra na cauda de alta exposição, que é exatamente onde o suporte é mais
fino. Quanto mais correta a hipótese sobre o formato, menos municípios carregam
o efeito e maior o MDE.

---

## 9. Referências e estado de verificação

**Lidos nesta sessão** (pasta do Drive): Callaway, Goodman-Bacon & Sant'Anna
(rascunho 26/01/2024); Baker, Callaway, Cunningham, Goodman-Bacon & Sant'Anna
(2026, *JEL* 64(2):498–557); Dias, Rocha & Soares (LACEA WP 0024, 2020 —
**conferir contra o publicado**, *ReStud* 90(6):2943–2981, 2023); Reynier & Rubin
(*PNAS*, DOI 10.1073/pnas.2413013121 — **volume divergente**, cabeçalho diz
121(3), lista de leitura diz 122(3)); Lichtenberg, Parker & Zilberman (1988,
*AJAE* 70(4):867–874); Aguiar (2017, dissertação UFC); ADI 7794 (petição PSOL).

**Não verificadas — não usar sem conferir contra DOI/Crossref:**
- Larsen et al. (2017) — pesticidas na Califórnia, efeito no topo da distribuição.
- Marx-Stoelting et al. (2025) — crítica a Frank (2024) sobre falácia ecológica.

**Não lido:** `2023_tese_lmgreges.pdf` (digitalizado, sem camada de texto).

**Citadas por terceiros, não lidas:** Rigotto et al. (2013); Barbosa et al.
(2019); Pignati, Machado & Cabral (2007); Teixeira (2011); Cavalcante (2023);
Chen, Christensen & Kankanala (2023); Conley & Taber (2011); Rangel & Vogl
(2019); Camacho & Mejía (2017); Weitzman (1974).
