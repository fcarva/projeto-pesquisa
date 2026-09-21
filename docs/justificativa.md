# Justificativa

> **Nota de uso — não integra o texto do projeto.** Redação no padrão ABNT para
> projeto de pesquisa (NBR 15287): prosa contínua, impessoal, sem subdivisão
> interna, com citações autor-data (NBR 10520); as referências completas entram
> na seção própria do projeto (NBR 6023) quando o `.bib` for conferido contra
> DOI. Extensão de cerca de duas páginas e meia (893 palavras, ante 1.714 da
> versão anterior). Hipóteses de identificação, limites e ressalvas de escopo
> ficaram fora: na NBR 15287 são metodologia, e já estão em
> `paper/secoes/04-identificacao.tex`. A versão longa de trabalho permanece no
> histórico do repositório (commit `72c074a`). O quadro de proveniência ao final
> é controle interno do repositório e também não integra o projeto entregue.

---

A pulverização aérea de agrotóxicos retém 32% do produto no alvo, deposita 49%
no solo e dispersa 19% para fora da área de aplicação — conta atribuída à
Embrapa na justificativa do Projeto de Lei nº 18/2015 da Assembleia Legislativa
do Ceará. Quase um quinto do que sai da aeronave recai sobre quintal, poço,
escola e casa de quem não contratou a aplicação: é externalidade negativa em
sentido estrito, com a diferença de que aqui ela tem endereço. O endereço é a
Chapada do Apodi, no Baixo Jaguaribe, onde a fruticultura irrigada de exportação
convive com agricultura familiar e assentamentos, e onde análises de 23 pontos
de coleta reproduzidas no mesmo projeto de lei, oriundas do Dossiê ABRASCO,
encontraram procimidona e carbaril em todas as amostras, carbofurano em 18 e
fenitrotiona em 16 — e glifosato em apenas 4. Em 2010, o líder comunitário José
Maria Filho, o Zé Maria do Tomé, foi assassinado após denunciar essa
pulverização, e a lei que nove anos mais tarde proibiu o método em todo o estado
recebeu o seu nome: a proibição respondeu a um conflito distributivo, não a um
ajuste técnico. O Ceará foi o primeiro estado brasileiro a adotá-la e, até o
momento, não há estimativa de seu efeito.

A literatura causal sobre agrotóxicos e saúde ao nascer mediu três objetos, e
nenhum deles é este. Dias, Rocha e Soares (2023) exploram a expansão da soja
transgênica no Brasil comparando populações a jusante e a montante da mesma
bacia: medem uma substância pelo canal-água. Reynier e Rubin (2025), sobre mais
de dez milhões de nascimentos no rural norte-americano e com aptidão
agroclimática da FAO-GAEZ, estimam redução de 23 a 32 gramas no peso ao nascer
no nível médio de exposição: medem a difusão de uma tecnologia por produtores
privados. Camacho e Mejía (2017) estudam a fumigação aérea de cultivos ilícitos
na Colômbia: medem um método, porém operado como programa estatal, cuja variação
vem da intensidade com que o Estado pulveriza, não de uma regra que proíbe
pulverizar. Duas contribuições delimitam o que se pode esperar: Larsen, Gaines e
Deschênes (2017) encontram efeitos adversos apenas no topo 5% da distribuição de
exposição, o que sustenta a rota dose-resposta e adverte que o suporte útil é
estreito; e Greenstone e Hanna (2014) encontram efeito nas regulações ambientais
indianas de ar e nenhum nas de água — regular no papel não equivale a reduzir
exposição no corpo, e é isso que impede que a pergunta aqui proposta seja
retórica.

O que não foi avaliado é um banimento de método, com data, texto legal e
reversão parcial. O tratamento examinado não é a adoção de uma tecnologia nem a
intensidade de um programa estatal, e sim um interruptor regulatório: o art.
28-B, inserido na Lei estadual nº 12.228/1993 pela Lei nº 16.820, sancionada em
8 de janeiro de 2019 e vigente desde o dia 9, não nomeia princípio ativo algum — proíbe o *como*,
não o *quê*. O caso é ainda quimicamente distinto de seus antecedentes, pois o
problema da Chapada é de fungicida e carbamato sobre banana e melão: os desenhos
citados transferem metodologicamente, não quimicamente. Duas rotas independentes
de busca, ao corpus internacional e aos periódicos brasileiros de economia, não
retornaram avaliação causal de banimento de método de aplicação — a forma honesta
do enunciado é que a busca não encontrou, não que não exista.

A demanda pelo resultado está declarada. O Supremo Tribunal Federal julgou a lei
constitucional em 2023, por unanimidade (ADI 6137); a Lei estadual nº
19.135/2024 abriu exceção para drones, revertendo parcialmente a proibição; e
nova ação segue pendente (ADI 7794). A política está viva, sendo contestada e
replicada, e a decisão de mantê-la, revogá-la ou substituí-la vem sendo tomada
sem estimativa de efeito. Daí decorre o segundo ensaio: como Weitzman (1974)
decide entre instrumento-preço e instrumento-quantidade pela inclinação relativa
do dano e do custo marginais, a escolha entre proibir, taxar ou impor
zonas-tampão consome a derivada que o primeiro estima — e é essa exigência que
fixa o parâmetro-alvo na curva dose-resposta, não no efeito em um ponto único.

A contribuição vem com preço declarado, e é o preço que sustenta a
justificativa sob incerteza. O parâmetro-alvo exige hipótese de identificação
mais forte do que a usual, e o poder estatístico é curto: contra efeito
esperado de 15 a 25 gramas, o piso amostral de ruído do desenho é de
aproximadamente 17,7 gramas. Daí que o entregável declarado inclua o resultado
nulo informativo — sobre política que está sendo replicada, um nulo cujo
intervalo exclua o efeito esperado é evidência publicável, desde que
pré-especificado, pois o pipeline produz 31 séries candidatas a desfecho e o
espaço de busca ultrapassa mil especificações. As hipóteses que sustentam o
parâmetro-alvo, os limites de identificação parcial que delas decorrem e o que
não se reivindica — o método e não a molécula, a dose como intenção de tratar,
a janela encerrada em dezembro de 2024 com a exceção para drones — são
desenvolvidos na seção de identificação.

A pesquisa é viável no prazo. O pipeline de estimação está completo e testado de
ponta a ponta, em oito etapas e 92 testes automatizados, a estratégia de
identificação está escrita e a legislação primária está obtida e transcrita; o
que falta é aquisição de dados — SINASC, SISAGUA, PAM/IBGE e FAO-GAEZ —, e o
cronograma até a qualificação está organizado em etapas com portão falsificável.

---

## Quadro de proveniência (controle interno — não integra o projeto)

**P** fonte primária no repositório · **V** citação verificada contra DOI/PMID ·
**C** a conferir no Portal CAPES · **D** aritmética do próprio desenho.
**Este documento não contém nenhum coeficiente estimado.**

| Afirmação | Classe | Fonte |
|---|---|---|
| Retenção 32% / solo 49% / dispersão 19% | **P** | `docs/legislacao/pl-18-2015.md` ⚠️ atribuição à Embrapa não conferida |
| Tabela ABRASCO, 23 pontos, 2009 | **P** | idem ⚠️ fonte primária do Dossiê não conferida |
| Art. 28-B; sanção 08/01, vigência 09/01/2019 | **P** | `docs/legislacao/lei-16820-2019.md` |
| Assassinato de Zé Maria do Tomé (2010); lei leva seu nome | **P** | `paper/secoes/02-background.tex` §2.1 |
| ADI 6137 (2023, unânime); Lei 19.135/2024; ADI 7794 | **P** | `docs/legislacao/README.md` |
| Reynier e Rubin (2025), PNAS; 23–32 g | **V** | `doi:10.1073/pnas.2413013121`, pmid 39808655 |
| Larsen, Gaines e Deschênes (2017), Nat. Commun.; topo 5% | **V** | `doi:10.1038/s41467-017-00349-2`, pmid 28851866 |
| Camacho e Mejía (2017), J. Health Econ. | **V** | `doi:10.1016/j.jhealeco.2017.04.005`, pmid 28570914 |
| Dias, Rocha e Soares (2023), REStud; Greenstone e Hanna (2014), AER; Weitzman (1974), REStud | **C** | fora do índice alcançável; conferir no CAPES |
| Efeito esperado de 15–25 g; piso amostral de ruído ≈ 17,7 g | **D** | `docs/ars/08-briefing-orientador.md` §D2 |
| 31 séries, > 1.000 especificações | **D** | idem §D7 |
| 8 etapas, 92 testes | **D** | `scripts/`, `tests/test_data_prep.py` |
| NBR 15287, NBR 10520, NBR 6023 (formato adotado) | **C** | conferir edição vigente das normas |

⚠️ **Nenhuma citação da classe C foi conferida.** O índice bibliográfico
alcançável desta sessão cobre PubMed/PMC e arXiv; periódicos de economia (AER,
QJE, REStud, JEEM, AJAE) ficam fora dele. Conferir antes da versão final, como
manda o `CLAUDE.md`.

*Quando a Introdução do Ensaio 1 for redigida — por último, pela fórmula de
Head —, os quatro primeiros parágrafos são promovidos a hook, antecedentes,
value added e pergunta; o quinto se distribui entre identificação e limitações;
o sexto permanece só na versão de projeto.*
