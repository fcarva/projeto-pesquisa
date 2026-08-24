# Layer 4 — as três perguntas abertas, equipadas

*Estado: **aberta**. A rodada 1 foi respondida com "não sei" — resposta legítima,
registrada como tal. Este documento não responde por ninguém; ele converte três
perguntas paralisantes em três tarefas com endereço. 2026-08-24.*

Eu perguntei as três de uma vez sem marcar que **não são do mesmo tipo**. Uma é
lógica e se resolve com uma conta. Uma é empírica e se resolve com uma consulta
barata. Uma é administrativa e se resolve com um ofício. Nenhuma exige inventar
método.

---

## Pergunta 2 — a falsificação. **Destravada: era pergunta de poder disfarçada.**

Eu apresentei como dilema filosófico: se efeito positivo confirma o ban e nulo é
ilegível, nenhum resultado falsifica. Estava mal colocado.

Um nulo é inconclusivo **só se o intervalo de confiança for largo**. Se a
estimativa vier zero com um IC estreito que **exclui 15 g** — o piso do efeito
esperado —, isso *é* evidência de que o ban não produziu o efeito que a
literatura levaria a esperar. O desenho falsifica.

Então "que resultado te faria concluir que o ban não funcionou?" tem resposta
mecânica: **um IC que exclua o efeito esperado.** E se esse IC é alcançável já é
a pergunta de poder da E1.5. As duas perguntas eram a mesma.

**Se a estimativa vier zero, o IC de 95% exclui 15 g?**

| Municípios tratados | DP tend. 10 g | 18 g | 20 g | 30 g | 40 g |
|---|---|---|---|---|---|
| 3 | ±11,4 ✔ | ±20,5 ✘ | ±22,8 ✘ | ±34,2 ✘ | ±45,6 ✘ |
| 5 | ±8,9 ✔ | ±16,0 ✘ | ±17,8 ✘ | ±26,7 ✘ | ±35,5 ✘ |
| **10** | ±6,4 ✔ | **±11,5 ✔** | ±12,7 ✔ | ±19,1 ✘ | ±25,5 ✘ |
| 15 | ±5,3 ✔ | ±9,5 ✔ | ±10,6 ✔ | ±15,8 ✘ | ±21,1 ✘ |
| 20 | ±4,6 ✔ | ±8,4 ✔ | ±9,3 ✔ | ±13,9 ✔ | ±18,6 ✘ |
| 40 | ±3,5 ✔ | ±6,3 ✔ | ±7,0 ✔ | ±10,5 ✔ | ±14,0 ✔ |

✔ = o IC exclui 15 g; um nulo **falsifica**. ✘ = o IC contém 15 g; um nulo é
ilegível.

**A linha que importa.** No piso amostral (DP ≈ 18 g), o desenho passa a
falsificar a partir de **~10 municípios tratados**. Com três, não. Isso dá um
alvo numérico para a decisão que a L3 já tomou — "baixar o corte de dose para
encorpar o grupo tratado": **o alvo é dez.**

**Regra de bolso:** a meia-largura do IC é 0,70 × MDE. O desenho falsifica 15 g
sempre que o **MDE ficar abaixo de 21,4 g**.

**Próxima ação:** nenhuma decisão pendente aqui. O gate da E1.5 já cobre —
acrescentar à saída do script a coluna "o IC exclui o efeito esperado?", que é o
MDE multiplicado por 0,70 comparado ao piso de 15 g.

⚠️ **O que continua sendo pergunta sua, e que eu não respondo:** o piso de 15 g é
o *seu* efeito esperado. Se você mudar de ideia sobre a magnitude, a tabela muda
de leitura. E a pergunta substantiva — **que resultado você aceitaria como
evidência de que o ban não melhorou saúde perinatal** — continua sua. Eu mostrei
que ela é computável; o número é seu.

---

## Pergunta 1 — a seleção para nascimento vivo. **Destravada: há um teste barato antes da escolha difícil.**

O problema: se o ban reduz óbito fetal, fetos marginais passam a nascer vivos e
entram pela cauda de baixo peso, puxando a média para baixo — na direção oposta
ao efeito esperado, e competindo pelo mesmo espaço de magnitude.

Eu perguntei "como você separa os dois?" como se exigisse decisão imediata. Não
exige. **Antes de escolher qualquer correção, verifique se o problema existe.**

**O teste barato:** rodar a série de óbito fetal do SIM contra a dose, com o
mesmo desenho. Se óbito fetal **não se move** com a dose, a seleção é problema
teórico e não atual — a discussão acaba num parágrafo da seção de limitações,
com o teste como evidência. Se **se move**, aí a escolha difícil se torna
necessária, e só aí.

**Menu das rotas conhecidas — menu, não recomendação.** Se o teste acusar
movimento, estas são as opções que a literatura usa, com o custo de cada uma. A
escolha é sua:

| Rota | O que faz | Custo |
|---|---|---|
| **Reporte conjunto** | peso ao nascer e óbito fetal lado a lado, sem compor; o leitor integra | mais honesto, menos conclusivo; não entrega um número único |
| **Desfecho composto** | nascidos vivos + óbitos fetais como uma coorte só, com o óbito entrando como caso extremo | resolve a seleção por construção; exige justificar a composição, e o desfecho deixa de ser "peso ao nascer" |
| **Limites de seleção amostral** | estimar o intervalo que o efeito ocuparia sob os cenários extremos de quem entrou na amostra | não exige escolha substantiva; entrega faixa, não ponto, e some com a precisão que já é escassa |

**Próxima ação:** incluir óbito fetal do SIM na aquisição A1 e rodar o teste
junto do desfecho principal. Nada a decidir agora.

---

## Pergunta 3 — enforcement. **Destravada: é ofício, não decisão.**

Se o ban não foi fiscalizado, a dose pré-ban mede **intenção**, não exposição
removida, e a curva mede aderência voluntária. O estimando vira efeito de
intenção de tratar, e o parâmetro-alvo do `CLAUDE.md` deixa de descrever o que
está sendo estimado.

"Não sei" é a resposta correta aqui, porque ninguém sabe até perguntar.

**Base legal e endereço.** A fiscalização cabe a **SEMACE**, **SEARA** e
Secretaria da Saúde, pelos arts. 15 e 30 da Lei estadual 12.228/1993. O caminho é
a **Lei de Acesso à Informação (Lei 12.527/2011)**, que dá prazo legal de
resposta de 20 dias, prorrogáveis por 10.

**Minuta do pedido** (adaptar ao formulário do órgão):

> Com base na Lei nº 12.527/2011, solicito acesso às seguintes informações
> referentes à fiscalização do art. 28-B da Lei estadual nº 12.228/1993, incluído
> pela Lei nº 16.820/2019, que veda a pulverização aérea de agrotóxicos:
>
> 1. Número de autos de infração lavrados por descumprimento do art. 28-B, por
>    **município** e por **ano**, de 2019 a 2024.
> 2. Valor total de multas aplicadas e valor efetivamente arrecadado, no mesmo
>    recorte.
> 3. Número de ações fiscalizatórias (vistorias, denúncias apuradas) relacionadas
>    à pulverização aérea, no mesmo recorte.
> 4. Existindo cadastro de prestadoras de serviço de aplicação de agrotóxicos
>    registradas nos termos dos arts. 4º e 8º da Lei nº 12.228/1993, solicito a
>    relação por município, com data de registro e situação cadastral.
>
> Caso as informações estejam sob competência de outro órgão, solicito o
> encaminhamento nos termos do art. 11, §1º, III da Lei nº 12.527/2011.

O item 4 mata dois coelhos: serve ao enforcement **e** ao `d = 0` operacional
(definição 3 em `03-modelagem-ensaio1.md` §5.3).

**Próxima ação:** protocolar o pedido. É a única das três com prazo externo, e
por isso a que convém disparar primeiro — a resposta demora, o resto não.

**Se voltar vazio ou negativo:** o que se escreve é que a aderência não é
verificável com registro administrativo, que o estimando é portanto um efeito de
intenção de tratar, e que o parâmetro-alvo é renomeado de acordo. É uma
limitação declarável, não um impedimento — mas precisa estar declarada, e a
decisão de renomear é sua.

---

## Resumo do estado

| Pergunta | Estado | Próxima ação | Depende de decisão sua? |
|---|---|---|---|
| 2 — falsificação | **destravada por lógica** | coluna no script; alvo de ~10 municípios tratados | só o piso de 15 g, que já é seu |
| 1 — seleção | **destravada por teste barato** | rodar óbito fetal do SIM contra a dose | só **depois** do teste, se ele acusar |
| 3 — enforcement | **destravada por ofício** | protocolar LAI na SEMACE | não, até a resposta chegar |

A Layer 4 continua **aberta**. Ela fecha quando você responder o que sobrou de
substantivo: o piso de falsificação, a rota de seleção caso o teste acuse, e o
que escrever se o enforcement voltar vazio.
