# O que o estado da arte muda no desenho

*Integração de `docs/estado-da-arte.md`, `docs/framework-dissertacao.md` e
`docs/lista-leitura.md` ao que a Etapa 2 já tinha estabelecido. 2026-08-24.*

Três documentos entraram no repositório. O que segue não os resume — registra as
quatro coisas que eles **mudam**.

---

## 1. O gate que decide o Ensaio 1 não é o Gate 1

Este é o achado. O estado da arte entrega o número que faltava no *commitment
gate* da Layer 3: **Reynier & Rubin (2025) acham redução de 23–32 g no peso ao
nascer e ~1 dia de gestação, na exposição média.** É a magnitude de referência
mais próxima que existe — mesmo desfecho, mesmo instrumento de aptidão GAEZ,
mesmo mecanismo químico, publicado em top-journal.

Cruzando com o efeito mínimo detectável do desenho cearense (184 municípios, DP
individual do peso 500 g, 80% de poder):

**Quantos municípios de dose alta são necessários para detectar um efeito de
tamanho X**

| Efeito | DP das tendências = 10 g | = 20 g | = 40 g |
|---|---|---|---|
| 20 g | 2 municípios | 9 | 41 |
| **23 g** | **2** | **7** | **28** |
| **32 g** | **2** | **4** | **14** |
| 50 g | 2 | 2 | 6 |

Rigotto et al. (2013) comparam **três** municípios expostos — Limoeiro do Norte,
Quixeré e Russas. Leia a tabela nessa linha:

- **DP das tendências ≈ 10 g** → três municípios bastam. O desenho passa.
- **DP ≈ 20 g** → três é marginal para 32 g e insuficiente para 23 g.
- **DP ≈ 40 g** → três é inviável. Precisaria de 14 a 28.

**A consequência que reordena o roteiro:** o parâmetro que decide se o Ensaio 1
tem chance **não é a dispersão de dose no PAM**. É a **dispersão das tendências
municipais de peso ao nascer** — e essa é estimável **hoje**, só com o SINASC,
antes de tocar em PAM, GAEZ, bacias ou vento.

O script 01 já a calcula (`sd_tendencia_g`, por um placebo que parte o
pré-período ao meio). O que muda é o *status*: de coluna informativa para
**gate**, e gate anterior ao Gate 1.

⚠️ Duas ressalvas antes de tratar 23–32 g como alvo. Reynier & Rubin medem o
efeito de **acrescentar** glifosato ao longo de duas décadas; o Ceará **remove**
aplicação aérea de todos os agrotóxicos por ~6 anos. Molécula, duração e dose
diferentes. E o efeito esperado aqui se concentra na cauda alta, então o efeito
no topo pode ser maior que a média deles. 23–32 g é âncora de ordem de grandeza,
não predição.

---

## 2. As duas citações não verificadas — uma resolvida, uma ainda não

**Larsen et al. (2017) — resolvida.** Referência completa:
Larsen, A. E., Gaines, S. D. & Deschênes, O. (2017), *Agricultural pesticide use
and adverse birth outcomes in the San Joaquin Valley of California*,
**Nature Communications 8: 302**, DOI 10.1038/s41467-017-00349-2. Mais de 500 mil
nascimentos (1997–2011), exposição residencial por trimestre e toxicidade;
efeitos adversos de 5–9% **apenas na cauda superior** (top 5%) da distribuição de
exposição. Sai da lista de pendências como referência; **continua não lida por
mim** — o corpus da sessão não a serve. Conferir contra o DOI ao baixar.

Ela reforça a hipótese de limiar registrada na L2 — e, junto com o item 1 acima,
aperta o problema: efeito só na cauda + suporte fino na cauda = a colisão já
declarada, agora com duas fontes.

**Marx-Stoelting et al. (2025) — continua não verificada.** É um *Technical
Comment* na *Science* sobre Frank (2024), e o próprio `docs/estado-da-arte.md`
a marca com *"(confirmar DOI ao baixar)"*. Ninguém confirmou. Permanece
sinalizada onde for citada.

---

## 3. HonestDiD não substitui os bounds do CGS — são camadas diferentes

`docs/estado-da-arte.md` acrescenta **Rambachan & Roth (2023)**, *A More Credible
Approach to Parallel Trends*, *ReStud* 90(5):2555–2591 (pacote `HonestDiD`), como
"munição defensiva" para o problema de tendências paralelas. Correto, e entra no
desenho — **com uma distinção que precisa ficar explícita para não virar erro**:

| Ferramenta | Sobre qual hipótese | O que entrega |
|---|---|---|
| Event study de leads | Assumption 4 (paralelismo em resultado **não tratado**) | evidência, não validação |
| **HonestDiD** | **Assumption 4** | sensibilidade: quão grande a violação teria de ser para derrubar o resultado |
| **Bounds §5.1 do CGS** | **Assumption 5 (strong PT)** | identificação parcial sob direção do viés |

HonestDiD formaliza a sensibilidade do paralelismo **tradicional**. Ele não toca
o *strong parallel trends*, porque a A5 restringe trajetórias sob doses não
recebidas — e não há pré-período que informe isso. As duas ferramentas são
**complementares**: HonestDiD blinda o ATT(d|d); os bounds da §5.1 blindam a
curva. Usar uma no lugar da outra é o erro a evitar.

---

## 4. A pendência §8.3.5 do framework está resolvida

Tanto `docs/framework-dissertacao.md` (§8.3, item 5) quanto
`docs/estado-da-arte.md` (§5, "A achar") registram como pendente o estudo citado
pela petição do PSOL comparando saúde entre municípios com pulverização aérea e
municípios de agricultura familiar. O estado da arte anota que ele *"não apareceu
nas buscas acadêmicas (pode ser relatório técnico/tese, não indexado)"*.

**Ele está na própria petição, nota de rodapé 22:** Rigotto, R. M. et al. (2013),
*Trends of chronic health effects associated to pesticide use in fruit farming
regions in the state of Ceará, Brazil*, *Revista Brasileira de Epidemiologia*
16:763–773 — mortalidade por neoplasia **38% maior** em Limoeiro do Norte,
Quixeré e Russas contra **12 municípios de população similar** onde predomina
agricultura familiar, dados secundários **2000–2010**.

Ou seja: era o item [3] da própria lista de leitura. Duas consequências:

- O desenho dele — 3 expostos contra 12 pareados — é o ancestral direto do
  PSM+DiD, e o número "3" é a origem do problema de poder do item 1 acima.
- ⚠️ **O período 2000–2010 atravessa o ban municipal de Limoeiro do Norte (2009).**
  Isso afeta como aquele antecedente deve ser lido, e reforça a pendência E0 do
  roteiro.

---

## 5. Referências novas a incorporar

Do `docs/estado-da-arte.md`, por função. **Nenhuma foi lida por mim** — os DOIs
vêm do documento do pesquisador e precisam de conferência.

**Magnitude e mecanismo (Ensaio 1):** Frank (2024, *Science* 385:eadg0344) —
choque exógeno sobre quantidade de inseticida → +31,1% de uso, +7,9% de
mortalidade infantil; é o desenho de substituição de insumo com o sinal
invertido em relação ao ban. Frank & Sudarshan (2025, *AER*) — externalidade
ecológica → saúde via água. Sorensen Montoya (2025, *JEEM*) — nitrato em água de
consumo → prematuridade, **abaixo do limite regulatório**; é o molde para casar
SISAGUA com SINASC.

**Instrumento (Ensaio 2):** Böcker, Britz, Möhring & Finger (2020, *ERAE*
47(2):371–402) — avaliação ex-ante de um ban de glifosato, o contraponto europeu
direto. Finger (2024, *Ag. Economics* 55(2):265–269) — **a tese adversária**:
taxação por risco dá flexibilidade que proibição não dá. Engajar de frente.

**Método:** Roth, Sant'Anna, Bilinski & Poe (2023, *J. Econometrics*
235(2):2218–2244) — a revisão-guarda-chuva. Rambachan & Roth (2023) — ver §3.

**Idioma ag-econ:** Henningsen et al. (2025, *J. Agricultural Economics*
77(2):356–382, open access) — guia de causalidade escrito para essa plateia.
Bravo-Ureta et al. (2020, *AJAE*) — PSM+DiD em programa agroambiental.
Chatzimichael, Genius & Tzouvelekas (2021, *AJAE*) — agrotóxico como tratamento
**contínuo e endógeno**, precedente direto da escolha metodológica.

---

## O que isto muda no roteiro

Entra uma etapa antes do Gate 1:

> **E1.5 — Dispersão das tendências municipais.** Rodar o script 02 contra o
> SINASC real e medir a DP das variações municipais de peso ao nascer no
> pré-período. **Gate:** dado o número plausível de municípios de dose alta,
> essa DP permite detectar 23–32 g?
> **Se não:** ver §6 — a saída **não** é trocar o desfecho.

---

## 6. ⚠️ Correção: trocar o desfecho é a saída errada

A versão anterior desta nota dizia que, se o poder não fechasse, o desfecho
primário deveria migrar para baixo peso, prematuridade ou mortalidade, "que têm
estruturas de variância diferentes". Têm — **e são piores**. O erro era meu.

Calculando o piso amostral do ruído de tendência municipal (município de 800
nascimentos/ano, meia-janela de 2 anos, n = 1.600):

| Desfecho | Ruído relativo | Efeito na literatura | Razão efeito/ruído |
|---|---|---|---|
| **Peso médio** | 0,55% | 23–32 g (Reynier & Rubin) | **1,30 – 1,81** |
| Baixo peso (<2500 g) | 11,2% | 5–9% relativo (Larsen) | 0,44 – 0,80 |
| Prematuridade (<37 sem) | 10,1% | ~5% relativo | 0,50 |
| Mortalidade infantil | 28,7% | 5% relativo (DRS) | 0,17 |

Média contínua sobre todos os nascimentos bate evento raro por um fator de duas
a oito vezes. A escolha da Layer 1 estava certa por uma razão que o diálogo não
tinha articulado: peso médio não é só o desfecho mais defensável
conceitualmente, é **o único com razão efeito/ruído acima de 1**.

**O número que muda o cenário base.** Esse piso dá **DP de tendência ≈ 17,7 g** —
sem nenhuma heterogeneidade real, só amostragem. A linha "DP = 20 g" da tabela do
§1 é portanto aproximadamente o **melhor caso**, não o caso médio. Com três
municípios tratados, o MDE de 33 g é otimista, e o efeito esperado pelo
pesquisador é de 15–25 g.

Não é cenário de risco: é o cenário base. E a saída correta não é trocar de
desfecho — é **encorpar o grupo tratado**, o que devolve a decisão ao Gate 1.
Ver a Layer 3 em `02-research-plan-summary.md`.

Isso não contradiz a decisão de escopo cheio: a aquisição continua em paralelo.
Muda qual número se olha primeiro.
