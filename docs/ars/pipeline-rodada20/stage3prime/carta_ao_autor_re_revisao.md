[LEGACY-NO-CONTRACT]

# Carta ao autor — re-revisão do projeto (16/11/2026)

Felipe,

Esta é a conferência da segunda versão do projeto contra os 59 itens da rodada 1. O resultado é **revisão menor**: os dois bloqueios caíram, nenhum item obrigatório ficou sem resposta, e o que resta se resolve com frases, sem dado novo e sem mexer no desenho.

Uma ressalva antes do conteúdo. Quem conferiu é um modelo da mesma família dos pareceristas e de quem ajudou na revisão. Erros que o painel não viu podem ter passado de novo, e um reparo escrito ao gosto desse leitor tende a ser aceito por ele. A leitura do Renato é a única conferência independente.

## O que ficou resolvido

- O diagnóstico do pré-período não decide mais nada. O período de referência está fixado no texto, a regra de decisão não usa o desfecho, e a frase sobre graus de liberdade saiu (itens 12 e 43).
- A pergunta é a mesma nos capítulos 1, 4, 5 e 8, o tratamento é a lei (intenção de tratar), e o grupo tratado tem definição que não fica vazia se a seca suspendeu os voos (itens 1, 10 e 17).
- Rocha e Soares entrou e mudou o desenho: a chuva é controle, e o texto admite que não separa por completo a lei do retorno das chuvas (itens 21 e 45).
- O óbito fetal deixou de ser hipótese confirmatória, e há uma só hipótese confirmatória (item 22, em parte; ver abaixo).
- A medida dos voos passou a ser condicional, o cronograma tem data-limite e prioridades, e as alegações de ineditismo sem apoio saíram.

Contagem: dos 15 obrigatórios, 7 atendidos e 8 em parte; dos 11 sugeridos, 6 atendidos e 5 em parte; dos 33 opcionais, 18 atendidos, 11 em parte e 4 não atendidos.

## O que falta, em ordem de importância

**1. O contrafactual da volta dos voos (item 44; também o Quadro 2, item 13).** Se houve voo em 2007–2011 e não houve em 2012–2018, o coeficiente principal só é efeito da lei se os voos tivessem voltado sem ela. O texto diz que a lei "teria impedido a sua volta", mas não diz que isso é uma hipótese nem como será examinada. Se a prática acabou depois de 2011 por outro motivo, o coeficiente sai positivo sem a lei ter feito nada. Você já pediu os dados que ajudam: os relatórios de 2017–2018 (houve retomada antes da lei?), os do Rio Grande do Norte (os voos voltaram onde não havia proibição?) e a comparação entre o coeficiente do pós-lei e o do período de seca. Faltam duas ou três frases dizendo isso e como se lê o resultado se os dois coeficientes forem parecidos.

Classifiquei esse resto como sugerido, e é isso que separa revisão menor de revisão maior. Se o Renato entender que essa frase é condição para a qualificação, a decisão passa a revisão maior. Vale conferir com ele primeiro.

**2. O período de referência (achado novo; também os itens 46 e 57).** Ele é a peça central do reparo e você o declarou imutável, então precisa estar certo agora. Há quatro pontos:

- a Eq. (2) só tem indicadores para a seca e para o pós-lei, de modo que as coortes de 2005–2006 e as de fronteira (2011/2012 e 2018/2019) caem na categoria de referência, a menos que saiam da amostra, o que o texto não diz;
- 2007 não tem justificativa e fica fora dos relatórios pedidos, que começam em 2008;
- 2011 é o ano da notícia de proibição na Chapada, do PL nº 134 e da ação civil pública, todos no seu Quadro 1; o Apêndice B diz que a referência é "anterior aos projetos de lei", e não é;
- a §5.2 chama 2007–2011 de "anos para os quais há registro de voos", e a §5.4 diz que não se sabe se os relatórios foram preservados.

Ou você justifica a janela como está, ou adota uma coberta pelos pedidos e anterior a 2011. A escolha é sua; o que não pode é ficar para o plano de análise.

**3. O estudo de evento (item 14).** Com 2007–2011 agrupado como base, todos os coeficientes são posteriores à referência, e os de 2012–2018 são justamente os anos em que o tratamento pode ter mudado. Não sobra nenhum coeficiente que teste a tendência prévia. Um ano-base único e coeficientes para os anos anteriores a 2012 resolvem.

**4. A frase "os termos de ordem inferior são absorvidos" (item 9).** Refiz a conta por posto de matriz (`conferencia_posto_eq2.py`, nesta pasta). Com efeito fixo por ano de nascimento e períodos definidos pela gestação, as interações do grupo tratado com a seca e com o pós-lei não são absorvidas, por causa das coortes de 2012 e 2019. Passam a ser se o ano do efeito fixo e os períodos usarem o mesmo índice. Os dois coeficientes de interesse são identificados nos dois casos. É uma definição a escrever: o que é `a(t)`.

**5. A regra de decisão (itens 13 e 31).** Faltam: a linha para "voos documentados sem pico sazonal", caso em que o próprio texto diz que o desenho não tem o que medir; qual fração da grade decide a comparação com o efeito plausível; e uma frase dizendo que passar no teste contra o teto equatoriano é condição necessária, não suficiente. Hoje os 80 gramas mudaram de nome, mas seguem sendo o único valor contra o qual o poder é julgado.

**6. O quadro de especificações (item 11).** Faltam a ponderação das células, os termos de ordem inferior da interação de H3, e uma linha para o óbito fetal, o desfecho composto e H5. A chuva como controle está descrita como "parte da especificação principal" numa linha, enquanto a linha principal remete à Eq. (2) sem ela.

**7. Calzada et al. (item 20).** O capítulo 7 ainda diz que o análogo "encontra efeito apenas para mães que moravam a até 150 metros". Era essa a frase apontada na rodada 1. O intervalo do próprio artigo também não aparece, e "entre 150 e 2.500 metros não há gradiente" é mais forte do que os autores escrevem.

**8. O teste de seleção (item 22).** O óbito fetal foi rebaixado, mas o teste que o parecer propunha no lugar (nascidos vivos por coorte de concepção e razão de sexo ao nascer) não entrou. É ele que alcança as perdas precoces, e sai do SINASC.

**9. A seca e a lavoura irrigada (item 35 e achado novo).** Pereira e Cuellar sustentam a restrição de água; não sustentam a retração da lavoura. Pela leitura que consegui fazer, o artigo relata aumento da produção dos perímetros até 2013–2014 e corte pequeno para a fruticultura. O capítulo 7 diz "pode ter alterado"; o Apêndice B dá a retração como fato. Basta alinhar.

Miúdos: com que estação o diagnóstico roda, se o plano é do 2º bimestre e os registros podem chegar até o 3º (item 3); a tendência crescente de óbito fetal em Rigotto et al., que a frase nova omite (item 23); contiguidade dos tratados e intervalos na inferência (item 16); a frase das "duas aplicações aéreas por ano" sem citação junto dela; o nó da Figura 1 que ainda diz "coorte que deixa de receber o voo".

## Sobre o que você recusou

Os itens 19, 58 e 59 (recusados), 42 (recusado em parte) e 30, 40, 55, 56 e 57 (tratados como limitação) são todos opcionais. Nenhum pesa na decisão, e ela seria a mesma se fossem contados como atendidos. Um detalhe: o item 30, dos precedentes de restrição do método em outros países, aparece na resposta como "limitação", mas o texto não o menciona. Uma frase resolve.

## Restrições

Cumpridas: 15 páginas textuais (páginas 5 a 19 do PDF), nenhum número de estimativa seu, só o Ensaio 1. Duas observações. A conta de 15 páginas depende de apêndices ficarem fora; se a norma do programa os contar, o total passa. E, com os três quadros nos apêndices, a banca precisa abri-los para avaliar o desenho, porque parte da especificação principal só está no Apêndice C.

Aviso de leitura: H2 mudou de sentido entre as versões. Era o óbito fetal; agora é o hiato sazonal no período de seca. Quem comparar esta carta com a da rodada 1 deve ter isso em mente.

## O que não consegui conferir

A reportagem do Globo Rural não abriu; a doença, as duas aplicações por ano e os voos no Cariri até 2018 ficam apoiados na leitura do parecer da rodada 1. As tabelas de Calzada et al. na versão do periódico e o texto integral de Jones (2020) não foram abertos. O texto integral de Pereira e Cuellar foi lido por extração automática, não por leitura completa; confira a passagem antes de mudar a frase. O plano versionado de setembro e a afirmação de que a exposição sazonal não foi cruzada com os desfechos não são verificáveis pelo texto.

O relatório completo, com a tabela item a item e a comparação por critério, está em `re_review_report.md`, nesta pasta.
