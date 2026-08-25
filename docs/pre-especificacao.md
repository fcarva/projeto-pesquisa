# Pré-especificação — Ensaio 1

*Preencher e datar **antes** do primeiro contato com dado real. Depois disso, o
documento não vale mais para o que ele existe: um plano escrito depois de ver o
coeficiente não é plano, é racionalização com data.*

**Status:** ⬜ não preenchido · **Data de fechamento:** ______ · **Assinatura:** ______

<!-- PRESPEC_STATUS: ABERTA -->
*(o `make real` lê a linha acima. Troque `ABERTA` por `FECHADA` só depois de
preencher, datar e assinar — e commite a troca: o commit é o carimbo de tempo.)*

⚠️ Este arquivo é resposta ao achado **M1** de `docs/ars/09-revisao-metodologica.md`:
o pipeline produz **31 séries candidatas a desfecho**, e o desenho já sabe que o
poder é curto. Poder curto mais espaço de busca grande é a combinação que produz
achado espúrio com aparência de rigor. As seções abaixo fecham essa porta —
**ou declaram, explicitamente, que ficou aberta.**

A janela para escrever isto ainda está aberta justamente porque a rede está
bloqueada e nenhuma fonte real foi tocada. Ela fecha na primeira rodada com dado.

---

## 1. Desfecho primário

**Escolha:** ______________________

*O que já está argumentado, e que o pesquisador só precisa ratificar ou recusar:*
`peso_medio` é o único dos quatro candidatos com razão efeito/ruído acima de 1
(1,30–1,81, contra 0,44–0,80 para baixo peso, 0,50 para prematuridade e 0,17 para
mortalidade infantil — ver `05-integracao-estado-da-arte.md` §6). Média contínua
sobre todos os nascimentos bate evento raro por um fator de duas a oito vezes.

⚠️ Se a escolha for outra, o cálculo de poder do script 01 tem de ser refeito com
o desvio-padrão daquele desfecho — o `SD_PESO_G = 500.0` é do peso.

## 2. Exposição primária

**Escolha:** ⬜ `share_gestacao_pos_ban` · ⬜ `share_tri1` · ⬜ `share_tri2` ·
⬜ `share_tri3` · ⬜ outra: ______

*Contexto:* Larsen et al. (2017) acham efeito concentrado na cauda alta de
exposição; a literatura perinatal costuma separar por trimestre. Fixar um como
primário e reportar os outros como exploratórios é diferente de rodar os quatro e
contar o que se move.

## 3. Cultura-âncora

**Escolha:** ______________________

*Contexto:* três fontes independentes convergem para **banana** (dissertação da
UFC; ADI 7794; Cavalcante 2023). Convergência é hipótese forte, não escolha — o
Gate 1 decide se ela se sustenta empiricamente. ⚠️ Se o Gate 1 derrubar a
escolha, **a troca tem de ser registrada com data**, e a curva original também
reportada.

## 4. Especificação

- Degrau da escada do CGS: ______  *(a coluna `especificacao` do script 01
  recomenda; o pesquisador ratifica — E3 do roteiro)*
- Parâmetro-alvo primário: ⬜ `slope` (ACR — a curva, o que o Ensaio 2 precisa) ·
  ⬜ `level` (ATT(d|d))
- Construção de `d = 0` primária: ⬜ 1 · ⬜ 2 · ⬜ 3 · ⬜ 4  *(§5.3 de
  `03-modelagem-ensaio1.md`)*
- Cortes do colapso pré/pós: `--corte-pre` ______ · `--corte-pos` ______

## 5. Critério de falsificação

**Piso de efeito esperado:** ______ g

*Já registrado como 15–25 g pelo pesquisador na Layer 3.* O script 01 emite
`falsifica` comparando a meia-largura do IC contra esse piso. ⚠️ Trocar o piso
**depois** de ver o IC inverte o sentido do teste.

**O que se escreve se o desenho não falsificar:** ______________________
*(o compromisso já registrado é "limite superior informativo" — E7)*

## 6. Multiplicidade — o núcleo do M1

**Confirmatório** (declarar aqui; tudo que não estiver nesta lista é exploratório):

| # | Desfecho | Exposição | Hipótese e direção esperada |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Correção de família:** ⬜ nenhuma (e justificar) · ⬜ Bonferroni ·
⬜ Holm · ⬜ Benjamini–Hochberg · ⬜ outra: ______

**Exploratório declarado:** tudo o mais — inclusive os 19 recortes do canal de
intoxicação e as séries de óbito fetal. Reportar como exploratório é legítimo;
reportar exploratório como confirmatório não é.

⚠️ **O placebo não conta como desfecho.** A série X68 (intoxicação autoprovocada)
entra como **falsificação**, não como resultado: a hipótese prevê que ela **não**
se mova. Declarar isso aqui é o que impede que um movimento nela seja
reinterpretado como achado depois.

## 7. O que NÃO será feito

- ⬜ Não trocar o desfecho primário se o poder não fechar. *(A saída ratificada é
  encorpar o grupo tratado baixando o corte de dose — E1.5.)*
- ⬜ Não descer de unidade geográfica. *(O registro de residência materna do
  DATASUS não aguenta escala submunicipal — decisão da L3.)*
- ⬜ Não reportar coeficiente abaixo do MDE do próprio desenho como achado.
- ⬜ Outros: ______________________

## 8. Desvios

Qualquer desvio do acima entra nesta tabela, **com data e motivo**, e o texto
final reporta as duas versões.

| Data | O que mudou | Por quê | Resultado original preservado em |
|---|---|---|---|
| | | | |

---

## Como usar

1. Preencher com o orientador — as escolhas de 1 a 6 são as **D1–D7** do
   `docs/ars/08-briefing-orientador.md`.
2. Datar, assinar, **commitar**. O commit é o carimbo de tempo: o histórico do
   git prova que o plano é anterior ao dado.
3. Só então rodar `make pipeline` contra fonte real.
