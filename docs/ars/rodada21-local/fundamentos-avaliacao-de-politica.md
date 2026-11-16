# Fundamentos de avaliação de política pública aplicados ao Ensaio 1 (2026-11-15)

**Origem do material.** Só o que trata de avaliação de política, da disciplina
PECO 5046-6046 — Avaliação de Políticas Públicas (PPGEco/UFES, 2026/2; Ana
Carolina Giuberti e Renato Nunes de Lima Seixas), em
`C:/Users/DELL/Documents/aval-pol/disciplina/txt/`. **Nada do artigo sobre a lei
de incentivo à cultura** (`aval-pol/analise`, `aval-pol/artigo`, `aval-pol/dados`,
e todo o `licc.gov`, que é o aplicativo daquele artigo) foi lido para conteúdo nem
trazido para cá. Os arquivos da disciplina **não foram copiados**: são livros e
slides de terceiros; este documento só os cita.

**O que li por inteiro:** os slides de Modelo de Resultados Potenciais (02/09),
Validade Interna e Externa (09/09), Amostragem e Poder Estatístico (16/09, até o
exemplo) e a apresentação do curso. **Só localizei por busca, não li:** Gertler
et al., *Avaliação de Impacto na Prática* (2ª ed.); *Avaliação Econômica de
Projetos Sociais* (Itaú Social, 3ª ed.); Magenta Book; White e Raitzer (guia do
ADB); volumes do SiMAPP/IJSN; Williams (2020); guias de poder. **Não está na
pasta:** as aulas de Diferenças em Diferenças (21/10 e 04/11) — o material de
leads e lags veio do capítulo 9 de Cunningham, lido online
(`mixtape.scunning.com`), que os slides citam como Cunningham (2021).

## 1. Do curso ao desenho
| conceito do curso | como aparece no Ensaio 1 | o que os dados locais mostraram |
|---|---|---|
| **Contrafactual válido** — três quesitos: características médias iguais; o tratamento não afeta o grupo de comparação; os grupos reagem igual, "ou, ao menos, apresentam a mesma tendência" | o desenho só reivindica o terceiro, na forma fraca: mesma tendência do **hiato sazonal** | banana familiar difere em nível (sequeiro × irrigado); o RN é mais parecido em nível, mas tem outra cultura dominante |
| **EMPT (ATT)** × EMP | o parâmetro é o efeito sobre as coortes expostas dos municípios com avião, em **intenção de tratar** | nos 7 municípios do Censo 2006, 5 quase não têm banana: o grupo "tratado" mistura populações |
| **Viés de seleção** e **viés de efeitos heterogêneos** (decomposição da diferença simples) | a diferença tripla remove seleção fixa no tempo e choques município-ano; efeitos heterogêneos ficam — por isso a exposição entra em grupos, não contínua | sinal oposto entre a Chapada e os de fora: heterogeneidade ou ruído, indistinguíveis com 7 unidades |
| **Diferenças em diferenças** "controla características não observáveis constantes no tempo" | idem, com a terceira diferença tirando também o que varia por município-ano | — |
| **SUTVA, 1ª parte — ausência de interferência** (transbordamento, equilíbrio geral) | deriva e aquífero comuns (atenuam); migração do serviço aéreo para o RN (infla) | o RN só serve de controle se o serviço aéreo não migrou; não há dado |
| **SUTVA, 2ª parte — sem variação oculta do tratamento** (dose uniforme) | "versões do tratamento" (Apêndice E) | três versões documentadas hoje: Limoeiro esteve sob **zona-tampão municipal** de 2010 a 2018 (Lei 1.511, art. 214); frequência de voo de 2/ano (Cariri) a 6–8/ano (Chapada); seca |
| **Ameaças à validade interna** — eventos externos, variável de confusão, instrumentação, transbordamento, tamanho da amostra | seca (evento externo), chuva (confusão), mudança do campo de gestação no SINASC (instrumentação) | chuva municipal **ausente**; a variável de semanas de gestação não existe nos arquivos mais antigos (32,6% da prematuridade do painel vem do campo em faixas) — o peso ao nascer não é afetado |
| **Poder e efeito mínimo detectável (EMD)** — passo 3: "qual é o nível mínimo de impacto que justificaria o investimento?"; 80% e α = 5% | regra de decisão (Quadro 2): compara o EMD com o efeito plausível | EMD por permutação: ≈ 49 g (7 municípios), ≈ 99 g (Chapada), ≈ 129 g (Chapada × RN). Com poucos conglomerados tratados, mais anos não ajudam |
| **Programa implementado em conglomerados?** (passo 1 do cálculo de poder) | sim: a lei é estadual e a exposição é municipal | o número efetivo de conglomerados tratados é 2 a 7 — é isso que fixa o poder, não os 2,5 milhões de nascimentos |
| **Teoria da mudança / cadeia de resultados** — cada elo precisa ocorrer | lei → cumprimento → havia voo a suspender → menor exposição (sem substituição terrestre) → peso | elos 2 e 3 sem medida (LAI não protocolada); o fechamento do hiato na seca é compatível com voos já suspensos |
| **Validade externa** — ampliação × transposição; mapeamento de mecanismo (Williams 2020) | usar Calzada et al. (Equador) como referência de magnitude é **transposição** | elos que diferem: regime de fumigação (o ano inteiro lá, quadra chuvosa aqui), frequência, contraste (intensiva × habitual lá; voo × nenhum voo aqui) — "teto" não se sustenta |
| **Falsificações** (Cunningham, cap. 9): mesmo desfecho em outro grupo; mesmo grupo, outro desfecho | tratamento falso (banana familiar × sem banana); idade da mãe | o primeiro passa (−5 g, erro-padrão 5); o segundo em `23_leads_lags_exploratorio.py` |
| **Leads e lags** (Cunningham, cap. 9): omitir t = −1; leads = tendência diferencial pré; "parallel trends cannot be tested" | estudo de evento A × H × ano, bases 2018 e 2014 | resultados na seção 7 do mapa de lacunas |
| **Inferência com poucos tratados** — agrupamento falha; aleatorização (Buchmueller, DiNardo e Valletta 2011) | o projeto promete Ferman e Pinto; aqui, permutação | com 7 tratados, agrupado (18,6 g) e permutação (17,5 g) coincidem; com 2 tratados o agrupado dá 11 g onde a permutação dá 35 g (Chapada) e 46 g (fronteira): três a quatro vezes otimista |

## 2. O que isto sugere para o texto do projeto (decisão do pesquisador)
1. **Dizer qual quesito do contrafactual o desenho reivindica.** Só o terceiro, na
   forma de tendência do hiato. É mais honesto e mais defensável que "grupo de
   comparação válido".
2. **Enunciar as duas partes do SUTVA em separado.** A interferência já está; a
   variação oculta do tratamento ganhou evidência nova (zona-tampão de Limoeiro).
3. **Tratar o uso de Calzada et al. como transposição**, com o mapeamento de elos,
   em vez de "teto".
4. **Leads e lags com duas bases** (2018 e 2014), porque a lei tem três marcos de
   antecipação.
5. **O poder é de conglomerados.** O texto já diz; os números locais dão a ordem
   de grandeza.

## 3. Referências (conferidas por DOI no Crossref em 2026-11-15, salvo nota)
- CUNNINGHAM, S. *Causal Inference: The Mixtape*. Yale University Press, 2021. DOI 10.12987/9780300255881. Lido na versão online (cap. 9), que hoje se intitula "The Remix"; não cotejada com a impressa.
- BUCHMUELLER, T.; DINARDO, J.; VALLETTA, R. *AEJ: Economic Policy* 3(4):25–51, 2011. DOI 10.1257/pol.3.4.25.
- MILLER, S.; JOHNSON, N.; WHERRY, L. *QJE* 136(3):1783–1829, 2021. DOI 10.1093/qje/qjab004.
- ROTH, J. *AER: Insights* 4(3):305–322, 2022. DOI 10.1257/aeri.20210236.
- WILLIAMS, M. J. *The World Bank Research Observer* 35(2):158–191, 2020. **Não conferida no Crossref**; dados como nos slides.
- GERTLER et al., *Avaliação de Impacto na Prática*, 2ª ed.; ITAÚ SOCIAL, *Avaliação Econômica de Projetos Sociais*, 3ª ed. **Não conferidas**; citadas como nos slides.
