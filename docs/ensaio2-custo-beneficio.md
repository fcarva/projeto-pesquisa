# Ensaio 2 — o ban valeu o que custou, e era o instrumento certo?

*2026-11-16. Plano do segundo ensaio, na forma que o `framework-dissertacao.md`
§8 propõe. Substitui, como plano, o `ensaio2-rota-inversao.md`, que fica como
registro. ⬜ **Depende de decisão do orientador**: trocar a calibração de
Weitzman por custo-benefício é mudança de escopo.*

---

## 1. A pergunta

O Ensaio 1 mede o que a lei fez. O Ensaio 2 pergunta duas coisas sobre esses
números:

1. **Custo-benefício.** O benefício em saúde do banimento supera o custo em
   produção?
2. **Instrumento.** Uma taxa ou uma zona-tampão teriam chegado a um resultado
   melhor do que a proibição?

A primeira é empírica e se responde com os resultados do Ensaio 1. A segunda é
argumentativa: usa a teoria (Weitzman 1974; Lichtenberg, Parker & Zilberman
1988) para organizar o que os números permitem dizer, sem estimar o que o
desenho não identifica.

**Por que não a calibração de Weitzman.** A regra compara a inclinação do
benefício marginal com a do custo marginal. O Ensaio 1, binário, entrega um
nível de efeito, não uma inclinação; e o parecer de 22/09 já havia mostrado que
a ponte entre a curva dose-resposta e a regra não se sustentava. Insistir seria
repetir no Ensaio 2 o que desandou no Ensaio 1.

---

## 2. Estrutura do custo-benefício

No formato da disciplina (TIP1, s.22): benefício líquido = benefício total −
custo total, por ano, para os municípios tratados.

### 2.1 Benefícios

| componente | quantidade (do Ensaio 1) | preço | fonte do preço |
|---|---|---|---|
| Saúde ao nascer | ATT sobre peso ao nascer (g) e sobre baixo peso (p.p.) × nascimentos nos tratados | valor de um grama a mais ao nascer, ou custo evitado por caso de baixo peso | ⬜ a escolher e verificar: literatura de retornos ao peso ao nascer; custo hospitalar neonatal do SIH |
| Óbito fetal e infantil | ATT × nascimentos, se houver efeito | valor estatístico da vida usado para o Brasil | Dias, Rocha & Soares (2023) valoram assim a externalidade do glifosato; ⬜ localizar a fonte do VSL que eles usam |
| Intoxicação aguda | ATT sobre casos notificados (pode ser **negativo**: ver §2.3) | **reestimar com o SIH do Ceará e do RN**: valor médio da internação e dias de permanência nos códigos de intoxicação por agrotóxico, mais a diária rural local | os valores publicados são do Paraná em 1998/99 e servem de método e ordem de grandeza: US$ 787,97 por caso hospitalizado (Soares & Porto 2009, lido); cenários de US$ 260 a US$ 1.098 (Soares & Porto 2012, lido) |

A decomposição de Harrington & Portney (1987), que Rodrigues (2022) usa,
organiza a conta: disposição a pagar = dano à saúde + gasto preventivo + gasto
de remediação. O projeto observa só o primeiro e parte do terceiro (SIH), e
deve dizer que o benefício calculado é um **piso**.

### 2.2 Custos

| componente | quantidade | fonte |
|---|---|---|
| Produção perdida | ATT sobre área colhida, produção e valor da banana (PAM) | Ensaio 1 |
| Custo adicional de controle | diferença de custo entre aplicação aérea e terrestre, por hectare | planilha da Conab (`12_clean_conab_custos.py`): a operação aérea é ~1,5% do custo total da banana; em 2009 o voo custava R$ 135/ha ao produtor parceiro (Marinho et al. 2011, p. 171); depoimentos de produtores (25 L/ha por avião contra 250–300 L/ha manual) |
| Emprego | ATT sobre vínculos formais na agricultura (RAIS/CAGED) | Ensaio 1. O sinal é ambíguo: a aplicação manual emprega mais gente |

Há duas afirmações em conflito sobre o custo, e o Ensaio 1 arbitra entre elas:

- Os produtores, na ADI 6137 e na imprensa, dizem que sem o avião o controle da
  sigatoka fica "ruim e muito mais caro".
- A nota técnica de Cavalcante (2022, UFRN), lida na íntegra, mostra que
  produção, rendimento e exportação **subiram** depois de 2018. Os dados
  conferem com a PAM; a comparação parte do fundo de uma seca e não tem grupo
  de comparação (`leituras-segunda-rodada.md` §5).
- Há ainda um terceiro caso possível: se os voos já tinham parado em 2012, a
  lei não custou nada porque não removeu nada. Aí o custo-benefício relevante é
  o do fim dos voos em 2012, e o da lei é o de impedir a retomada.

Nenhuma das duas tem grupo de comparação. O DiD da PAM entre os dois lados da
Chapada é a primeira estimativa com contrafactual.

### 2.3 A substituição entra nos dois lados

Proibir o método não proíbe a molécula. Se o produtor troca o avião pelo
pulverizador costal, a exposição ambiental cai e a ocupacional pode subir: mais
calda, mais trabalhadores, e o costal é fator de risco de intoxicação
plausível, ainda que mal medido (Soares, Freitas & Coutinho 2005 têm 15 casos;
o argumento de mecanismo está em Valadares et al. 2020). O efeito
sobre intoxicação no SINAN pode, portanto, ser positivo. Nesse caso entra na
conta como **custo**, e é o achado mais informativo para a segunda pergunta.

### 2.4 Como reportar

Nenhum componente terá estimativa precisa. O resultado se apresenta como tabela
de cenários: para cada combinação de limites dos intervalos do Ensaio 1, o
sinal do benefício líquido. A pergunta útil é a inversa: **que efeito sobre o
peso ao nascer seria necessário para o ban se pagar, dado o custo estimado?** E
esse efeito está dentro ou fora do intervalo? É a mesma lógica de limiar do
plano anterior, aplicada a números que o desenho de fato produz.

---

## 3. A escolha do instrumento

### 3.1 O que a teoria organiza

- **Weitzman (1974):** sob incerteza sobre o custo de abatimento, quantidade
  (proibir) domina preço (taxar) quando o dano marginal cresce mais depressa
  que o custo marginal. Fica como referencial, com a aplicação restrita ao que
  se pode argumentar: dano concentrado em poucas comunidades vizinhas e custo
  de substituição baixo (~1,5% do custo de produção) apontam para a quantidade.
- **Poluição difusa:** a deriva não tem medidor. Uma taxa sobre deriva não é
  implementável; uma taxa sobre o voo ou sobre o produto é, e não distingue o
  bananal ao lado da escola do bananal isolado. A zona-tampão distingue.
- **Lichtenberg, Parker & Zilberman (1988):** a regulação de agrotóxico tem
  custo de bem-estar e efeitos distributivos que dependem de quem pode
  substituir. É a linhagem do orientador, e é onde a heterogeneidade familiar ×
  não familiar do Ensaio 1 conversa com o Ensaio 2: a lei atinge só quem usava
  avião.

### 3.2 O que os dados brasileiros acrescentam

| fato | fonte | o que diz sobre o instrumento |
|---|---|---|
| Já existia zona-tampão: 500 m de povoações e 250 m de mananciais | IN MAPA 2/2008, art. 10 | a alternativa "regular em vez de proibir" foi tentada. A literatura da Chapada descreve descumprimento sistemático (Marinho 2010; parecer do Tramas 2016). A proibição é mais barata de fiscalizar: avião no ar é infração |
| O instrumento-preço opera com sinal trocado: R$ 9,86 bilhões de desoneração em 2017, R$ 6,22 bilhões de ICMS. **Ceará: R$ 7,6 milhões; RN: R$ 12,5 milhões**, os dois com isenção nas operações internas | Cunha & Soares (2020), Tabs. 2 e 3, lido | antes de discutir taxa pigouviana, há um subsídio a retirar. É a matéria da ADI 5553 (`docs/legislacao/adi-5553-7755-tributacao.md`). Os próprios autores reconhecem que a demanda responde pouco a preço no curto prazo, o que pesa contra a taxa como substituto da proibição |
| No Nordeste o real marginal de agrotóxico rende R$ 1,35; no Sul, R$ 0,10 | Rodrigues (2022), cap. 3 | uma taxa uniforme custaria produção no Nordeste e quase nada no Sul. Instrumento nacional de preço é mal calibrado para a região do estudo. ⚠️ Média de municípios de sequeiro; não descreve a fruticultura irrigada |
| Crédito rural aumenta o sobreuso | Rodrigues (2022), cap. 3; Rodrigues, Fortini & Neves (2023) | há um terceiro instrumento, o condicionamento do crédito, que a discussão proibir × taxar ignora |
| Controle biológico eleva a eficiência no país e não no Nordeste, onde 0,51% dos estabelecimentos adotam | Rodrigues, Fortini & Neves (2023) | a substituição tecnológica "limpa" não está disponível na região no curto prazo; o substituto real do avião é o costal |
| A Lei 19.135/2024 reabriu a aplicação aérea por drone | `docs/legislacao/` | o legislador moveu-se da proibição para a regulação do método. É o experimento seguinte, fora da janela |

### 3.3 O que o ensaio conclui, em cada cenário do Ensaio 1

| se o Ensaio 1 achar | leitura para o instrumento |
|---|---|
| melhora ao nascer, sem perda de produção | a proibição foi barata e funcionou; a taxa teria deixado voar quem podia pagar, ao lado das mesmas comunidades |
| melhora ao nascer, com perda de produção | custo-benefício decide; zona-tampão com fiscalização efetiva seria o candidato a dominar |
| nenhum efeito detectável ao nascer, intoxicação sobe | a proibição trocou um risco difuso por um ocupacional; o problema era a molécula e a prática, não o método |
| nenhum efeito detectável em nada | com ~1.000 ha, a lei mudou pouco no mundo; seu valor é de precedente (ADI 6137), e o ensaio discute o que o desenho não consegue ver |

Escrever a tabela **antes** de estimar é o que impede o texto de racionalizar o
resultado depois.

---

## 4. O que falta

| # | o quê | tipo |
|---|---|---|
| 1 | Decisão do orientador sobre o escopo | humano |
| 2 | Ensaio 1 estimado: os ATT e seus intervalos | depende do painel |
| 3 | Preço do peso ao nascer: escolher a literatura e conferir DOIs | leitura |
| 4 | Soares & Porto (2012) e (2009) no original; atualizar valores | leitura |
| 5 | Nota técnica UFRN (2022) | busca |
| 6 | Custo de substituição: revisar a leitura da planilha da Conab à luz do parecer de 22/09 (custo contábil de quem escolheu cada tecnologia não é custo contrafactual de conversão) | análise |
| 7 | Ingestor RAIS/CAGED | código |

---

## 5. Referências deste plano

Todas no `paper/referencias.bib`, conferidas no Crossref em 2026-11-16, salvo
as marcadas ⬜ no texto: Weitzman (1974); Lichtenberg, Parker & Zilberman
(1988); Lichtenberg & Zilberman (1986); Soares & Porto (2009, 2012); Cunha &
Soares (2020); Rodrigues (2022); Rodrigues, Fortini & Neves (2023); Dias, Rocha
& Soares (2023); Reges (2023). Harrington & Portney (1987) e Soares, Freitas &
Coutinho (2005) são conhecidas só pela citação em Rodrigues (2022) e **não**
estão no `.bib`.
