# Busca complementar: agrotóxicos agrícolas e desfechos ao nascer (SQ1)

> **Para o LeapSpace (Elsevier, via Portal de Periódicos CAPES).** Copie tudo abaixo desta
> caixa como uma única mensagem. Responda **só** no formato da seção 5. Este texto faz parte de
> uma revisão sistemática registrada em repositório público e é guardado na íntegra (PRISMA-trAIce,
> item M6). Versão de 2026-10-13.

---

## 1. Contexto

Sou mestrando em economia (PPGEco/UFES). Faço uma revisão sistemática para uma dissertação
sobre a **proibição da pulverização aérea de agrotóxicos no Ceará** (Lei Estadual 16.820/2019,
"Lei Zé Maria do Tomé"). A lei proíbe o **método** de aplicação, não uma molécula. Na Chapada do
Apodi, o caso de referência, a aplicação aérea era sobretudo de **fungicidas em banana**.

**Pergunta da revisão:** qual é a evidência de que a exposição **ambiental ou comunitária** a
agrotóxicos de **uso agrícola**, com ênfase na **aplicação aérea**, afeta os **desfechos ao nascer**?

## 2. Critérios de elegibilidade

| critério | entra | não entra |
|---|---|---|
| Exposição | agrotóxico **agrícola** por via ambiental ou comunitária: proximidade residencial, deriva, água, uso no município, pulverização aérea (inclusive para controle de vetores); biomonitoramento só se o composto tem fonte **exclusivamente agrícola** no contexto (p. ex. clordecona nas Antilhas) | exposição medida **só pela ocupação** da mãe ou do pai; uso doméstico; biomonitoramento de composto com várias fontes (p. ex. metabólitos DAP na população geral); só fertilizante ou nitrato |
| Desfecho | **primários:** peso ao nascer, baixo peso (< 2.500 g), prematuridade (< 37 semanas); **secundários:** pequeno para a idade gestacional, óbito fetal ou natimorto, mortalidade neonatal ou infantil, anomalias congênitas, idade gestacional | só biomarcadores ou marcadores intermediários |
| Desenho | quase-experimental (DiD, RD, IV, evento); coorte; caso-controle; ecológico ou painel com exposição espaço-temporal; transversal com exposição individual atribuída | relato ou série de casos; revisão (mas **liste as revisões relevantes à parte**, para a busca de citações); editorial; estudo em animal ou *in vitro* |
| Tipo de documento | artigo revisado por pares; *working paper* (NBER, IZA, SSRN, RePEc, Banco Mundial, BID, IPEA); *preprint*; **tese, dissertação ou TCC com dado original** | resumo de congresso sem texto completo |
| Período e idioma | 1990 em diante; inglês, português ou espanhol | — |

## 3. O que já foi buscado (para você não repetir o óbvio)

Busca por script em 2026-10-12/13: OpenAlex (5.035 registros distintos), PubMed (2.054), Scopus
pela API (4.945, string `TITLE-ABS-KEY` com blocos de exposição e desfecho), OASISBR (878) e LA
Referencia (544). São 9.416 registros únicos depois da deduplicação. Os estudos centrais já
conhecidos incluem Calzada, Gisbert & Moscoso (2023, *JAERE*, banana no Equador); Dias, Rocha &
Soares (2023, *ReStud*, glifosato no Brasil); Camacho & Mejía (2017, *J Health Econ*, pulverização
aérea na Colômbia); Larsen, Gaines & Deschênes (2017, *Nat Commun*, Califórnia); Reynier & Rubin
(2025, *PNAS*); as coortes de clordecona de Guadalupe (Timoun); e o Dossiê ABRASCO.

**O que mais me interessa é o que uma busca booleana pode ter perdido:**
- estudos **brasileiros** e **latino-americanos**: Ceará, Chapada do Apodi, Baixo Jaguaribe, Mato Grosso, Paraná, Rio Grande do Sul, Pernambuco, zona da mata, regiões de fruticultura irrigada; Equador, Colômbia, Costa Rica, Argentina, México; Antilhas Francesas;
- estudos que avaliam **aplicação aérea** especificamente: aviação agrícola, fumigação aérea, deriva, proibição de pulverização aérea;
- estudos sobre **banana, fruticultura, cana, soja e algodão** e desfechos ao nascer;
- **avaliações de política** (proibição, restrição, zona-tampão) com desfecho de saúde perinatal;
- teses e dissertações brasileiras que viraram artigo, e artigos indexados só com palavras-chave em português.

## 4. Tarefas

1. **Identifique estudos elegíveis** (seção 2), priorizando os temas da seção 3. Use o Scopus e o ScienceDirect. Para cada um, informe os campos da seção 5.
2. **Liste à parte as revisões** (sistemáticas ou narrativas) sobre o tema, com DOI. Elas vão para a busca de citações.
3. Para cada estudo, diga se ele está indexado no Scopus e, se souber, o **EID** (`2-s2.0-…`).

**Regras, que valem para tudo:**
- **Só referências reais e verificáveis.** Não invente título, autor, DOI nem EID. Se não tiver certeza de um campo, deixe-o vazio e marque a confiança como "baixa". Cada DOI será conferido no Crossref, e referência inexistente é descartada e registrada como erro.
- Não resuma os estudos além do pedido na tabela.
- Prefira a versão **publicada** quando houver *working paper* e artigo.
- Se o resultado passar de 60 estudos, mande os 60 mais relevantes e diga quantos ficaram de fora.

## 5. Formato da resposta (obrigatório)

Responda **só** com as duas tabelas abaixo, em Markdown, sem texto antes ou depois, exceto uma
linha final "Fora da lista: N".

**Tabela A: estudos primários**

| n | primeiro_autor | ano | titulo | periodico_ou_tipo | doi | eid_scopus | pais | desenho | exposicao_e_metodo_de_aplicacao | desfecho | por_que_elegivel | confianca |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

- `doi`: só o DOI (`10.xxxx/...`), sem `https://doi.org/`;
- `exposicao_e_metodo_de_aplicacao`: diga se a aplicação é **aérea**, **terrestre**, **mista** ou **não especificada**;
- `confianca`: alta / média / baixa (sua confiança de que a referência existe e é elegível).

**Tabela B: revisões**

| n | primeiro_autor | ano | titulo | doi | tipo_de_revisao | confianca |
|---|---|---|---|---|---|---|
