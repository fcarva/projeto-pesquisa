# Rota 1, rodada 3 — o análogo que faltava, a dissertação que o trouxe, e o Censo

*ARS `deep-research`, modo `full`, continuação da Fase 2. Material recebido do
pesquisador em 2026-09-22: a dissertação de Januzzi (UFV, 2025), o pacote
`censobr` (IPEA) e três repositórios de Sidney Bissoli. 2026-09-22.*

---

## 0. O que chegou, e o que cada peça rendeu

| peça | o que rendeu | peso |
|---|---|---|
| Januzzi (2025), dissertação UFV | **a referência Calzada, Gisbert & Moscoso (2023)**, que o projeto não tinha; a rota INDEA/receituário; um nulo nacional | ⭐⭐⭐ pelo que cita, não pelo que acha |
| `censobr` (IPEA) | uma rota de dados que **passa pelo proxy** (GitHub Releases) e a triagem estrutural CE × RN, rodada | ⭐⭐ |
| `healthbR`, `sih-br-mcp`, `ibge-br-mcp` | nenhuma rota nova para os desfechos do Ensaio 1 — ver §5 | ⭐ |

A ordem das seções segue o peso, não a ordem de chegada.

---

## 1. ⭐ Calzada, Gisbert & Moscoso (2023) — o análogo mais próximo do mundo, ausente do projeto

> **Calzada, J., Gisbert, M. & Moscoso, B. (2023).** *The Hidden Cost of
> Bananas: The Effects of Pesticides on Newborns' Health.* **Journal of the
> Association of Environmental and Resource Economists** 10(6): 1623–1663.
> `doi:10.1086/725349`. Versão de trabalho: SSRN 3786643.

**Verificação:** ✅ confirmada por quatro fontes independentes — página do
periódico (vol. 10, nº 6), RePEc, portal da UAB e SSRN — e coincide com a
entrada da lista de referências de Januzzi. ⚠️ **Crossref pendente** (bloqueado
nesta sessão) e **texto completo não lido**: tudo abaixo é do resumo e do
resumo de Januzzi. Rodar a conferência Crossref localmente antes do `.bib`.

### O que é, pelo resumo

Fumigação **aérea** de **bananais** no **Equador**, 2015–2017. Exposição medida
por **endereço da mãe, perímetro das plantações e quantidade de agrotóxico**.
Diferenças-em-diferenças que explora a **variação sazonal** do uso de
agrotóxico. Recém-nascidos com exposição alta na gestação têm **déficit de 80 a
150 g** no peso ao nascer, e maior probabilidade de baixo peso e de prematuridade.
Januzzi acrescenta, do texto: o efeito aparece quando o **primeiro trimestre
coincide com períodos de fumigação intensa**, com baixo peso +0,35 p.p. e Apgar
baixo no 1º minuto +0,33 p.p.

### Por que é o análogo, e os outros três não eram

| | Reynier & Rubin (2025) | Dias, Rocha & Soares (2023) | Camacho & Mejía (2017) | **Calzada et al. (2023)** |
|---|---|---|---|---|
| cultura | milho/soja/algodão GM | soja | coca | **banana** |
| método | aplicação geral | aplicação geral | **aéreo** | **aéreo** |
| química | glifosato | glifosato | glifosato | **fungicidas de bananal** |
| desfecho | peso, gestação | mortalidade infantil | consultas, aborto | **peso, baixo peso, prematuridade** |
| exposição | cultura × GAEZ | cultura a montante | **registro de pulverização** | **quantidade + perímetro + endereço** |

Os três já citados casam em **uma ou duas** dimensões. Calzada casa em **todas as
cinco** — e a flag 2 do `CLAUDE.md` (o químico não é o glifosato) deixa de ser
limite de transporte para virar razão de preferência.

### 1.1 Magnitude: a conta que liga 80–150 g ao piso de 15 g

Calzada mede efeito **individual** sob exposição **alta** (mãe perto da
plantação). O `ATT(d|d)` deste trabalho é **municipal**: é o efeito individual
vezes a fração dos nascimentos do município que estava de fato exposta.

| fração dos nascimentos exposta | 80 g | 150 g |
|---:|---:|---:|
| 10% | 8 g | 15 g |
| 20% | 16 g | 30 g |
| 30% | 24 g | 45 g |

Com 10–20% dos nascimentos de um município bananeiro morando perto de plantação
pulverizada, a magnitude municipal esperada fica em **8 a 30 g** — o intervalo
que contém o piso de 15 g.

⚠️ **O piso não muda.** A pré-especificação fixou 15 g antes do dado e registra
que trocar o piso depois de ver o IC inverte o sentido do teste. O que muda é a
**justificativa**: hoje ele desce de Reynier & Rubin com "ajuste para baixo por
juízo"; com Calzada ele passa a ter derivação — efeito individual do análogo
exato vezes diluição espacial. Entra como **adendo** à proveniência da §5 da
pré-especificação, com o valor intacto. Usar Calzada para **subir** o piso seria
exatamente a prática que aquele documento proíbe.

⚠️ E a conta tem um insumo que o projeto não mediu: a fração exposta. Ela é a
diluição espacial da Fase 2 (§4.3) com número — e é **estimável** com o Censo
por setor (§4 abaixo: população rural por setor em município bananeiro), o que
fica como tarefa, não como resultado.

### 1.2 Identificação: a sazonalidade é a variação que este desenho não usa

O desenho atual compara municípios (dose) antes e depois. Calzada compara
**gestações dentro do mesmo lugar** conforme a janela sensível caia ou não no
pico de fumigação. Transposto para o Ceará:

> **dose × pós-ban × (primeiro trimestre no pico de pulverização)**

O que isso compraria:

1. **Contraste dentro do município** — confundidores municipais (renda, sistema
   de saúde, porte) não variam com o mês de concepção.
2. **Teste de mecanismo** — gestações com janela sensível **fora** do pico são
   placebo natural: o ban não deveria movê-las.
3. **Poder** — a variação sai de coortes dentro do município-ano, não só de
   184 municípios.

⚠️ **Três condições antes de qualquer coisa:**

- **Não é resultado nem análise feita.** É candidata à pré-especificação do
  ciclo seguinte — o mesmo estatuto da hipótese de cauda da §6.8.
- **Falta o calendário de pulverização do Ceará.** A hipótese de que a
  Sigatoka (o alvo do fungicida em banana) segue a quadra chuvosa é plausível e
  **não verificada** — e a Chapada é irrigada, o que pode achatar a
  sazonalidade. A fonte seria ADAGRI/EMBRAPA, ou o próprio receituário (§2).
- **Sazonalidade de concepção é seletiva.** Características maternas variam com
  o mês de concepção; o desenho precisa dos efeitos principais de estação e de
  pré-tendência dose × estação. Literatura de *season of birth* a levantar e
  conferir antes de citar.

### 1.3 Medida: o terceiro análogo com registro de aplicação

Calzada tinha **quantidade de agrotóxico** e **perímetro de plantação**. Soma-se
à Califórnia (PUR) e à Colômbia (hectares pulverizados): os três análogos com
identificação causal mediram a **aplicação**; este trabalho mede a **cultura**.
Isso reforça a conclusão da Fase 2 §4.2 — a distância é de infraestrutura de
dados — e aumenta o valor da rota da §2.

### 1.4 Posicionamento

A novidade declarada do projeto **sobrevive**: Calzada estima efeito de
**exposição**, não de uma **proibição de método**. Mas a revisão de literatura
sem Calzada seria apanhada por qualquer parecerista de economia ambiental —
*JAERE* é o periódico de campo da área. Entra na justificativa, no background e
na §6.

E há um aglomerado correlato, conferido só por resumo, a ler: o estudo ISA na
Costa Rica, onde *"mancozeb is aerially sprayed at large-scale banana
plantations on a weekly basis"*, com metabólito urinário em gestantes
(PMC4256696); e um estudo recente de associação espacial entre exposição a
agrotóxico e baixo peso no Equador (PMID 41962821).

---

## 2. A pista do receituário: o registro brasileiro de aplicação pode existir

A dissertação de Januzzi constrói exposição com dados do **INDEA-MT**: o
*Relatório Consolidado de Comércio de Agrotóxicos*, compilado das **receitas
agronômicas** do Mato Grosso, com volume por município, cultura e ingrediente
ativo. Seguindo o fio:

| elo | norma | verificação |
|---|---|---|
| venda de agrotóxico agrícola exige receituário | Lei Estadual nº 12.228/1993, **art. 16** | ✅ texto consolidado no repositório |
| a receita contém a **modalidade de aplicação**, com anotação **obrigatória** quando aérea | Decreto nº 4.074/2002, **art. 66** | ⚠️ confirmado por dois agregadores de legislação; verbatim pendente |
| fiscalizar o receituário é da defesa agropecuária estadual | Lei nº 12.228/1993, **art. 30, IV** (SEARA, 1993); hoje a **ADAGRI** executa o Sistema de Defesa Agropecuária | ✅ / ⚠️ sucessão a conferir |

> **Se a ADAGRI guarda as receitas de 2015–2018, o filtro "modalidade = aérea"
> por município, ano e cultura é, para o tratamento deste trabalho, o que o PUR é
> para a Califórnia.** Nenhuma das rotas pendentes chega perto: a SEMACE diz
> quem **podia** pulverizar; o Censo Agro 2006 diz quem **tinha** aeronave; a
> receita diria **onde, quanto e em que cultura** se prescreveu aplicação aérea,
> no pré-período exato.

⚠️ **Ressalvas:** receita é **prescrição**, não execução; a digitalização em
2015–2018 é desconhecida (portarias da ADAGRI de 2022, 2024 e 2025 sobre envio
eletrônico apareceram em busca, objeto **não conferido**); e a receita tem dado
pessoal, o que o pedido trata por supressão.

**Minuta pronta:** `docs/legislacao/lai-adagri-minuta.md` (Pedido C), no padrão
da minuta da SEMACE, com checklist do que conferir antes de protocolar e tabela
do que fazer com cada resposta.

---

## 3. Januzzi (2025) — leitura crítica

> **Januzzi, S. B. (2025).** *Impacts of Pesticide Exposure on Birth Outcomes
> and Child Health in Brazil.* Dissertação (Mestrado em Economia Aplicada) —
> Universidade Federal de Viçosa. Orientador: L. C. B. Cardoso. Aprovada em
> 15/09/2025.

5.510 municípios, 2019–2022, painel com efeitos fixos. Exposição por índice
*shift-share*: intensidade de uso no Mato Grosso por cultura (INDEA-MT) ×
área plantada no município (PAM) ÷ área municipal, sete culturas. **Resultado:
nenhum efeito significativo** sobre baixo peso, prematuridade, mortalidade
infantil ou câncer infantil nos modelos com efeitos fixos; associações positivas
no *pooled* desaparecem com os efeitos fixos.

> ⚠️ **ERRATA de 2026-09-23 — há duas versões, com resultados diferentes.** O
> artigo apresentado no ENABER 2025 (Januzzi, Cardoso e Rodrigues), com o mesmo
> universo, reporta que *"each additional kilogram of pesticide applied per
> hectare increases the incidence of low birth weight by 1.2 cases per 1,000
> live births"* (resumo pelo índice do Semantic Scholar; PDF nos anais da BRSA,
> bloqueado pelo proxy). O "nulo" acima é o da **dissertação**. Citar a versão, e
> não "o nulo de Januzzi". Achado da auditoria de 2026-09-23 (doc 20 §4).

### 3.1 O índice não enxerga o Ceará

As sete culturas são soja, algodão, milho, cana, café, arroz e feijão — as que o
INDEA-MT cobre. **Banana e melão não entram.** A pergunta previsível da banca —
*"por que não usar o índice de Pignati, como Januzzi e DRS?"* — tem resposta
direta: ele é cego para as culturas que o avião pulverizava aqui, e mede volume
total, quando o ban remove um **método**.

### 3.2 O nulo diz mais sobre o desenho que sobre o efeito

- **O *shift* não varia no tempo.** A §3.1 da dissertação calcula a intensidade
  do Mato Grosso como **média do período** "para minimizar erro de medida"; a
  §3.2 descreve os *shifts* como "time-varying". As duas não podem valer. Pela
  construção efetiva, com efeito fixo de município a variação identificadora é
  só a **mudança de área plantada em quatro anos** — pequena por natureza.
- **Sete *shifts* não sustentam o argumento de exogeneidade.** O arcabouço de
  choques de Borusyak, Hull & Jaravel exige **muitos** choques
  aproximadamente aleatórios; com sete culturas, a identificação recai sobre a
  exogeneidade das **participações** (Goldsmith-Pinkham, Sorkin & Swift), e a
  composição de culturas de um município não é exógena. A afirmação de que o
  *shift-share* "por construção" endereça a endogeneidade não se sustenta.

⚠️ Referências de método a conferir no Crossref antes de entrar no `.bib`:
Borusyak, Hull & Jaravel (2022, *REStud*); Goldsmith-Pinkham, Sorkin & Swift
(2020, *AER*); e Borusyak, Hull & Jaravel (2025, *JEP* 39(1):181–204), que é a
que Januzzi cita.

### 3.3 O que o nulo **não** decide

Com 30 vezes mais municípios e nenhum efeito, é tentador ler Januzzi como
evidência de que "o problema não é N" — a favor da leitura de erro de medida da
§6.8. **Não é.** O nulo dela é compatível com as duas leituras e ainda com uma
terceira (variação identificadora quase nula). O que ele mostra é mais estreito:
**N grande não compensa exposição mal medida e variação fina** — o que é
consistente com a Fase 2, mas não a prova.

### 3.4 O que ela corrige no repositório

`docs/estado-da-arte.md` §5 dizia que a busca por avaliação econométrica
brasileira além do DRS devolvia só revisões. **Não é mais verdade**: há Januzzi
(2025). A afirmação que importa — *nenhum trabalho de economia avalia um ban de
método no Brasil* — **continua de pé**. Nota datada acrescentada lá.

---

## 4. O Censo 2022 via `censobr`: a triagem estrutural, rodada

O `censobr` hospeda o Censo por setor em **GitHub Releases**, que passam pelo
proxy desta sessão — quando SIDRA, DATASUS e servicodados não passam. Conferido:
HTTP 200, 115 MB, Parquet válido; o dicionário oficial também baixou, e os **17
códigos** de variável usados **conferem** com as descrições (a verificação é
passo do script, não afirmação).

`scripts/data_prep/15_censo_demografico.py`, `make censo-demografico`, 11 testes.

### O resultado — grupos definidos de fora (IBGE e PLP 98/07)

| grupo | mun. | rede geral | poço | poço (média munic.) | carro-pipa | esgoto adequado | fossa rudim. |
|---|---:|---:|---:|---:|---:|---:|---:|
| CE estado | 184 | 79,2% | 14,4% | 17,4% | 1,5% | 40,9% | 33,8% |
| RN estado | 167 | 84,9% | 8,5% | 12,9% | 3,4% | 32,4% | 35,5% |
| **CE: RI Russas–Limoeiro** | 15 | **83,2%** | 7,9% | **7,1%** | 4,4% | **26,2%** | 42,3% |
| **RN: RI Mossoró** | 17 | **82,4%** | 10,7% | **14,6%** | 3,7% | **35,4%** | 33,1% |
| RN: RIDE Chapada | 21 | 79,6% | 12,9% | 21,9% | 4,3% | 32,6% | 36,5% |
| CE: Limoeiro + Quixeré | 2 | 91,6% | 6,8% | 6,6% | 0,0% | 28,2% | 47,0% |

Fechamento das categorias no total de domicílios: água 99,2%, esgoto 99,1%.

### A leitura

1. **Abastecimento por rede e carro-pipa: praticamente iguais** dos dois lados
   da Chapada (83% × 82%; 4,4% × 3,7%).
2. **Esgoto: o lado cearense é ~9 p.p. pior** em esgoto adequado e ~9 p.p. mais
   dependente de fossa rudimentar.
3. ⚠️ **Poço: o lado potiguar depende duas a três vezes mais** na média
   municipal (14,6–21,9% contra 7,1%). Isso importa para o canal-água: a
   Chapada partilha o **Aquífero Jandaíra**. Se a exposição passa pelo lençol,
   o controle potiguar é **mais suscetível** — dimensão de heterogeneidade a
   pré-especificar, não detalhe.
4. ⚠️ **E o agregado estadual inverte o sinal**: o Ceará inteiro depende **mais**
   de poço que o RN inteiro (14,4% × 8,5%); na Chapada é o contrário. Comparar
   estados teria dado a resposta errada — é a razão empírica para os recortes
   locais.

### Por que não há veredito

O G3 do gate usa tolerância de 50 g no peso, fixada **antes** de haver dado. Aqui
os números já foram vistos: qualquer tolerância escolhida agora seria ajustada a
eles. Por isso o script **não emite ✔/✘** e não entrou no veredito agregado do
gate. É informação, e é assim que deve ser lida.

⚠️ **Níveis, não tendências** (o efeito fixo absorve nível); e **2022 é
pós-ban**. O corte limpo é o Censo 2010, pendente porque os códigos de 2010 são
outros e o dicionário é PDF.

---

## 5. Os três repositórios de Sidney Bissoli

| repositório | o que é | de onde vem o dado | serve ao Ensaio 1? |
|---|---|---|---|
| `healthbR` | pacote **R** para SIM, SINASC, SIH, SIA, SINAN, CNES, SI-PNI e inquéritos | SINASC e SIM: **FTP do DATASUS** (o mesmo do `pysus`); SIH e SI-PNI: espelho Parquet em Cloudflare R2 | ✘ nenhuma rota nova para os desfechos — o próprio código diz que SIM e SINASC entram no espelho "quando seus backends chegarem" |
| `sih-br-mcp` | servidor MCP com cubos agregados do SIH 1992–2025 | espelho R2 do autor | ✘ o projeto já concluiu que o SIH **não é estimável** para o canal A5 (1 intoxicação acidental em 8 anos) |
| `ibge-br-mcp` | servidor MCP que consulta as APIs do IBGE ao vivo | `servicodados` e `sidra` do IBGE | ⚠️ localmente, dá acesso conversacional ao SIDRA — inclusive à tabela 1008 do Censo Agro para o RN. Mas os scripts do projeto já fazem isso; nesta sessão, bloqueado |

**Alcance nesta sessão:** os domínios do autor e o `r2.dev` estão bloqueados;
o endpoint S3 do R2 responde. Listar o bucket exigiria usar a chave de leitura
que o autor publica no código — tentativa **negada** pelo controle de permissões
desta sessão, e não contornada. Fica para decisão do pesquisador; o valor
esperado é baixo, dado que SINASC não está espelhado e que **na máquina local o
DATASUS responde** (`docs/fontes-e-vintages.md`).

O que o `healthbR` oferece de útil é outra coisa: a comparação publicada
*healthbR vs microdatasus* sobre os mesmos sistemas é um teste externo das
decisões de limpeza do SINASC — leitura, não ferramenta.

---

## 6. O que muda no plano

| # | ação | custo | por quê |
|---|---|---|---|
| 1 | **Ler Calzada et al. (2023) inteiro** e conferir no Crossref | ~1 dia | é o análogo exato; muda justificativa, background e §6 |
| 2 | **Rodar `make fronteira VIZINHO=24` localmente** | ~1 h | o gate está pronto; o bloqueio de rede é só desta sessão |
| 3 | Protocolar o **Pedido C (ADAGRI)** depois do checklist | ~2 h + prazo | é a única rota para medir o método no pré-período |
| 4 | Adendo à proveniência do piso (§1.1) na pré-especificação | ~30 min | justificativa melhor, valor intacto |
| 5 | Pré-especificar a hipótese sazonal (§1.2) para o próximo ciclo | ~meio dia | antes de olhar; exige calendário de pulverização |
| 6 | Estimar a fração exposta por setor censitário | ~1 dia | dá número ao insumo da conta da §1.1 |

---

## Referências desta rodada

```bibtex
@article{calzada2023bananas,
  author  = {Calzada, Joan and Gisbert, Meritxell and Moscoso, Bernard},
  title   = {The Hidden Cost of Bananas: The Effects of Pesticides on
             Newborns' Health},
  journal = {Journal of the Association of Environmental and Resource Economists},
  volume  = {10}, number = {6}, pages = {1623--1663}, year = {2023},
  doi     = {10.1086/725349},
  note    = {4 fontes independentes; Crossref pendente; texto completo nao lido}
}
@mastersthesis{januzzi2025pesticide,
  author = {Januzzi, Stela Barbosa},
  title  = {Impacts of Pesticide Exposure on Birth Outcomes and Child Health
            in Brazil},
  school = {Universidade Federal de Vi{\c{c}}osa},
  year   = {2025},
  type   = {Disserta{\c{c}}{\~a}o (Mestrado em Economia Aplicada)},
  note   = {texto completo lido (PDF fornecido pelo pesquisador)}
}
@manual{censobr,
  author = {Pereira, Rafael H. M. and Barbosa, Rog{\'e}rio J.},
  title  = {censobr: Download Data from {Brazil}'s Population Census},
  year   = {2023},
  doi    = {10.32614/CRAN.package.censobr},
  url    = {https://CRAN.R-project.org/package=censobr},
  note   = {citacao oficial do inst/CITATION do pacote, conferida no repositorio
            clonado. Dados: github.com/ipea/censobr\_prep\_data, release v1.0.0}
}
```
