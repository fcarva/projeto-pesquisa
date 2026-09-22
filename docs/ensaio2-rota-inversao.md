# Ensaio 2 pela inversão — o que falta, e de onde vem

*Rota escolhida em 2026-09-22, entre as três que a §7.2 do paper expõe. Este
documento é o plano de execução: o que a inversão precisa, o que já existe, e o
que tem de ser buscado fora.*

---

## 1. A decisão, e por que ela não é consolo

O Ensaio 1 não entregou a âncora que a §3 do paper prometeu. As três saídas eram
adiar o Ensaio 2, trocar o ponto por limites, ou **inverter a pergunta**.

Escolhida a terceira. Ela não finge que o dado diz o que não diz — diz com
exatidão o que teria de ser verdade para a conclusão de política virar, e quanto
falta para saber. É o que se faz em análise de política com desenho imperfeito.

⚠️ **E ela já produziu um resultado, antes de qualquer calibração.** Ver §3.

---

## 2. A regra, e o mapeamento dos objetos

Weitzman (1974), aproximação linear-quadrática, choque aditivo no custo marginal:

```
Delta = E[W_preço] − E[W_quantidade] = (sigma² / 2c²) · (c − beta)

  beta = |B''|  inclinação do benefício marginal do abatimento
  c    =  C''   inclinação do custo marginal
  sigma         desvio-padrão do choque de custo

  Delta > 0  →  taxa domina        ⟺  c > beta
  Delta < 0  →  proibição domina   ⟺  beta > c
```

**O limiar é `beta = c`.** E note o que `sigma` faz e não faz: escala a
**magnitude** da vantagem e **nunca troca o lado dela**. A intuição de que "mais
incerteza favorece o instrumento X" é falsa, e o script tem teste para isso.

### ⚠️ O mapeamento revela um erro de alvo na §3 do paper

```
B(q)   = benefício de abater q     = |ATT(q|q)|    ← o Ensaio 1 estima
B'(q)  = benefício MARGINAL        = |ACR(q)|      ← o Ensaio 1 mira
B''(q) = inclinação do marginal    = ACR'(q)       ← WEITZMAN USA ESTA
```

A §3 diz que "o Ensaio 2 consome a derivada". Erra por uma ordem: o `ACR` **já
é** a derivada, e a regra precisa da inclinação **dele**.

O que salva parcialmente a formulação é que ter a **curva** inteira de `ACR` — e
não um ponto — entrega o `ACR'` de imediato. Era por isso que a curva era o
alvo, e a justificativa correta do alvo é essa, não a que está escrita.

✅ Corrigido no paper: §3 ganhou o parágrafo da imprecisão, §7.2 traz o
mapeamento completo.

---

## 3. O resultado que a inversão já deu

`make weitzman` roda sem calibração nenhuma e devolve **indeterminado em toda a
grade**. Isso não é falha — é medida.

> **O Ensaio 1 não restringe `beta` nem um pouco.** Ele estima o `ACR` com
> intervalo que cobre zero com folga em todas as faixas de dose, e a derivada de
> uma curva não identificada não é identificada.

⚠️ **E a inversão localiza o gargalo, que é o valor real dela.** Os dois lados da
regra não estão igualmente vazios:

| lado | estado | como se resolve |
|---|---|---|
| **custo** (`c`) | ⬜ vazio mas **calibrável** | fonte secundária: custo aéreo vs terrestre por hectare, perda de rendimento na substituição. Não depende deste desenho |
| **benefício** (`beta`) | 🔴 **vazio e travado** | exige curvatura identificada. ⚠️ **Não se resolve encorpando o grupo tratado na margem** — o objeto que falta é uma curvatura, não um nível |

Essa assimetria é informação de planejamento: investir no lado do custo é barato
e não destrava a conclusão; destravar o benefício é o problema difícil.

---

## 4. O que buscar, em ordem

### 4.1 O lado do custo — ✅ BUSCADO em 2026-09-22

⭐ **A Conab tem item de linha próprio para avião.** A planilha de custos de
produção da banana (`serie-historica-custos-banana-2008-a-2025.xlsx`) traz
**"2 - Operação com Avião"**, separado de "3.1 - Tratores e Colheitadeiras".
Órgão oficial, 88 sistemas, 2008–2025, cinco UFs.

`scripts/data_prep/12_clean_conab_custos.py` · `make custo-conab`

| grandeza | valor |
|---|---|
| custo de operação com avião | **R$ 280 a 520/ha** (mediana R$ 460) |
| como % do custo total | **1,55%** (máx 1,70%) |
| custo total da banana | ~R$ 28.000/ha |
| sistemas com avião | 4 de 88 |
| sistemas com trator | 9 de 88 |
| **sistemas com ambos** | **0** |

#### ⭐ Dois achados que valem mais que o preço

**As duas tecnologias são mutuamente exclusivas, e ambas estão em uso
comercial.** Nenhum dos 88 sistemas usa avião e trator. E a maioria dos que a
Conab acompanha já usa trator. Ou seja: a aplicação terrestre não é apenas
*tecnicamente* viável (a Embrapa já dizia isso para o controle de sigatoka) —
ela é a **escolha corrente da maior parte do setor registrado**.

⚠️ Isso é insumo para o Ensaio 1 também, não só para o 2: a substituição que o
ban força já era praticada por parte do setor antes dele, o que torna o choque
de custo menor do que a retórica do contencioso judicial sugeria.

**A ordem de grandeza reenquadra o problema.** A aplicação aérea é ~1,5% do
custo de produção, contra ~45% de fertilizante. Mesmo dobrar esse item deixa o
efeito sobre o custo total abaixo do ruído anual de insumo.

#### ⚠️ E a armadilha que essa tabela arma

É tentador subtrair R$ 460 (avião) de R$ 1.003 (trator) e chamar de custo de
abatimento. **Não é**, por três razões independentes:

1. Os itens não são comparáveis: "Avião" é só pulverização; "Tratores e
   Colheitadeiras" é **toda** a operação tratorizada.
2. As amostras não se sobrepõem: avião só na BA, trator em ES/RS/SC, com
   produtividade mediana de 26.000 contra 30.000 kg/ha.
3. A escolha de tecnologia é **endógena** ao sistema.

O script imprime as três e se recusa a fazer a subtração.

#### ⚠️ E o que continua faltando: `c` não é o nível

A Conab dá o **nível** de custo por hectare. Weitzman compara **inclinações**. O
que decide `c` é a **heterogeneidade do custo de conversão entre produtores** —
terreno, porte do bananal, tamanho do talhão —, e a planilha, que reporta
sistema típico, não enxerga isso.

```
c ~ 0   (prêmio de conversão homogêneo)
        Delta -> -infinito se beta > 0
        => a QUANTIDADE domina, SEM precisar saber quanto vale beta
c >> 0  (conversão muito mais cara para alguns)
        volta a valer a comparação usual, e beta é indispensável
```

⭐ **O valor da busca foi encolher a pergunta.** O Ensaio 2 não precisa medir `c`
na escala certa — precisa saber se o prêmio de conversão é **homogêneo entre
produtores**. Isso é pergunta de levantamento setorial, não de econometria.

#### O que ainda falta no lado do custo

| item | onde |
|---|---|
| dispersão do custo de conversão entre produtores | ⚠️ **o que decide `c`** — levantamento setorial, SINDAG, cooperativas da Chapada do Apodi |
| perda de rendimento na substituição | literatura agronômica de banana; elo mais fraco |
| `sigma` do choque de custo | variância da série Conab já extraída |

### 4.2 O lado do benefício — o problema de verdade

Três rotas, nenhuma barata:

1. **Desenho com poder para a curvatura.** Exige muito mais variação de dose ou
   muito mais unidades. Fora do alcance do Ceará sozinho.
2. **Importar a curvatura da literatura.** ⚠️ Reynier & Rubin reportam
   concentração do efeito na cauda (75 g no decil inferior contra 6 g no
   superior), que é evidência de **convexidade em vulnerabilidade** — não em
   dose. Não é o `beta` que a regra pede, e usá-lo como se fosse seria repetir o
   erro de alvo da §3. Serve de **cenário**, não de estimativa.
3. **Abandonar a forma linear-quadrática.** Weitzman é aproximação de segunda
   ordem; com proibição total (cota em zero) a aproximação local é justamente
   onde ela é pior. Uma formulação global pediria a curva inteira — que é o que
   falta.

---

## 5. O que o Ensaio 2 pode escrever hoje

Sem nenhum dado novo:

- ✅ A regra, o mapeamento e o limiar `beta = c`.
- ✅ Que `sigma` escala e não vira o lado — resultado que contraria intuição
  comum e vale por si.
- ✅ A fronteira `(c, beta)` completa, como objeto teórico.
- ✅ **Que o Ensaio 1 não exclui nenhuma região dela**, e por quê.
- ✅ A assimetria de §3: custo calibrável, benefício travado.
- ✅ A camada de realismo de poluição difusa, que já está na §3 do paper
  (Helfand 1995: sob heterogeneidade, a taxa tende a ser mais eficiente e a
  regulação por quantidade gera maior lucro ao setor regulado) — ⚠️ observação
  com consequência distributiva, e que conversa com o fato de a proibição
  cearense ter sido contestada pelo setor, não por consumidores.

O que **não** se pode escrever é qual instrumento domina. E dizer isso
explicitamente é mais defensável do que escolher um e torcer.

---

## 6. Ferramenta

```bash
make weitzman                                  # fronteira, sem calibração
make weitzman BETA_MIN=40 BETA_MAX=55          # cenário calibrado
```

`scripts/estimate/11_weitzman_inversao.py` · saída em
`data/processed/weitzman_inversao.csv` · 4 testes, sendo o central o que garante
que **sem calibração o script não conclui**.
