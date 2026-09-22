# Documentos legais

Fonte primária da cronologia e do texto do ban. **Obtidos** — os arquivos vieram
do portal da Assembleia Legislativa do Ceará (`www2.al.ce.gov.br`), fornecidos
pelo pesquisador em 2026-08-23, porque a sessão remota tem o domínio bloqueado
no proxy.

| Arquivo | O que é |
|---|---|
| `lei-16820-2019.md` | Lei 16.820/2019 — o ban. Texto integral. |
| `lei-12228-1993-consolidada.md` | Lei 12.228/1993 **consolidada**, com o art. 28-B nas duas redações e o histórico de alteração. É a peça mais útil das duas. |
| `pl-18-2015.md` | Projeto de Lei 18/2015 — o texto original e a **justificativa**, que reproduz a tabela do Dossiê ABRASCO com 24 amostras de água da Chapada do Apodi. Ver `docs/ars/06-quimico-e-antecipacao.md`. |

⚠️ Ambos trazem a ressalva de praxe: *"O texto desta Lei não substitui o
publicado no Diário Oficial."* Para citação em texto final, conferir o DOE.

Ainda não obtidos: acórdão da ADI 6137/STF; petição da ADI 7794 está na pasta do
Drive, não no repositório.

## Cronologia

| Data | Evento |
|---|---|
| **09/12/1993** | Lei 12.228/1993 — norma-mãe sobre agrotóxicos no Ceará (D.O. 14.12.93). |
| **20/11/2009** | ✅ **CONFERIDO.** Limoeiro do Norte proíbe a pulverização aérea pela **Lei Municipal 1.478/2009** — *"dispõe sobre a proibição do uso de aeronaves nas pulverizações de lavouras no município de Limoeiro do Norte"*. Fonte primária: `camaralimoeirodonorte.ce.gov.br/leis/549` (consulta 2026-09-21). O art. 29 da lei estadual autoriza o município a legislar supletivamente. ⚠️ Ver a ameaça abaixo — ela agora tem número. |
| **24/02/2015** | **PL 18/2015 apresentado** por Renato Roseno. ⚠️ **Marco de notícia** — a janela pré-ban 2015–2018 começa *depois* disto. |
| **18/12/2018** | ALECE aprova por unanimidade, após 4 anos de tramitação. **Marco de certeza.** |
| **08/01/2019** | Lei 16.820/2019 sancionada por Camilo Sobreira de Santana. |
| **09/01/2019** | Publicação no D.O. O art. 2º diz "entra em vigor na data de sua publicação" — **é esta a data de vigência**. |
| **mai/2023** | STF julga a lei constitucional (ADI 6137, rel. min. Cármen Lúcia, unânime). |
| **19/12/2024** | Lei 19.135/2024 dá nova redação ao art. 28-B: exceção para drones. |
| **2025** | ADI 7794 (PSOL) contra a Lei 19.135/2024, rel. min. Luiz Fux. Pendente. |

**Precisão da data.** Sanção em 08/01, publicação e vigência em 09/01. Num painel
mensal a distinção não muda nada — ambas caem em janeiro de 2019 —, mas o texto
da dissertação deve dizer 09/01/2019 quando falar de vigência e 08/01/2019 quando
falar de sanção.

**Três marcos, não um.** Notícia (24/02/2015), certeza (18/12/2018), obrigação (09/01/2019). O primeiro morde a variável de tratamento, não só o desfecho — ver `docs/ars/06-quimico-e-antecipacao.md` §1.

**Iniciativa.** O PL 18/2015 e o texto oficial da Lei 16.820/2019 registram apenas
**Deputado Renato Roseno**. O esboço atribui a autoria a três deputados (Roseno,
Joaquim Noronha e Elmano de Freitas) — provavelmente coautoria no PL, não na lei
sancionada. Conferir na tramitação do PL 18/2015 antes de afirmar.

## Duas descobertas que mudam o desenho

### 1. ⚠️ Bans municipais anteriores contaminam o pré-período — **confirmado**

O **art. 29** da Lei 12.228/1993 estabelece: *"Compete aos municípios legislarem
supletivamente sobre o uso e o armazenamento dos agrotóxicos"*. O esboço
registrava que Limoeiro do Norte teria proibido a pulverização aérea em 2009.

✅ **Procede.** Lei Municipal **1.478, de 20/11/2009**, conferida no acervo da
Câmara Municipal em 2026-09-21. Não é hipótese de esboço: é lei, com número e
data, **nove anos e sete semanas antes** da vigência estadual.

#### ⚠️ E a contaminação está dentro do grupo tratado

Conferido contra `data/processed/pam_ce_muni_cultura_media__sidra.parquet`:

| | |
|---|---|
| Limoeiro do Norte | `cod_ibge6 = 230760` |
| Banana (cacho), área média 2015–18 | **1.857,5 ha** |
| Posição entre os 169 com área positiva | **6º** |
| Decil superior da banana (o grupo tratado) | 17 municípios — **Limoeiro está nele** |

O grupo tratado que sustenta o MDE da banana em `gates-resultados-dados-reais.md`
§6 tem **17 unidades**, e **uma delas está tratada desde 2009**. É ~6% do grupo,
e é a 6ª maior dose — não é unidade de borda.

⚠️ **Isto não é mais uma ameaça a verificar; é um defeito a tratar.** As
consequências que o esboço antecipava, agora com sujeito conhecido:

- a dose pré-ban medida em 2015–2018 para Limoeiro do Norte já vem suprimida pelo
  ban municipal, subestimando a exposição histórica;
- o efeito estimado para esse município é o de uma remoção que já havia
  acontecido em parte — atenuação, não efeito nulo;
- e a comparação de Rigotto (2000–2010) atravessa o ban municipal, o que também
  afeta como aquele antecedente deve ser lido.

### ✅ Varredura da fase 1 concluída em 2026-09-21 — e a contaminação é **só** Limoeiro

Os 17 municípios do decil superior da banana — o grupo tratado que sustenta o
MDE — foram varridos um a um:

| resultado | n | significado |
|---|---|---|
| **confirmado** | **1** | Limoeiro do Norte, Lei 1.478/2009 |
| `ausente_conferido` | **16** | acervo publicado conferido, **não há** lei do tema |
| `inconclusivo` | **0** | — |

✅ **Os 17 estão resolvidos.** Itapajé caiu depois: o host `cmitapaje.ce.gov.br`
responde com um stub de 3 KB — parece site, não é acervo — e as leis do
município moram em **`itapaje.ce.gov.br`, o portal da PREFEITURA**, que é
plataforma A. ⚠️ O varredor desistia no primeiro host que respondesse; agora
testa os três padrões (`camara<slug>`, `cm<slug>`, `<slug>`) antes de declarar
inconclusivo. Um "inconclusivo" é trabalho que nunca será feito porque parece
impossível — e este era só um prefixo de host.

**A contaminação está limitada a ~6% do grupo tratado, e não cresce.** A
hipótese de que a Chapada do Apodi tivesse legislado em bloco **não procede**:
Quixeré (21.289 leis no acervo), Russas (6.901) e Tabuleiro do Norte não têm
norma anterior a 2019 sobre pulverização aérea. Limoeiro foi isolado, não
pioneiro de uma onda.

⚠️ **O que "ausente_conferido" não diz.** Conferiu-se o **acervo publicado** de
cada câmara. Câmara que não digitalizou 2009 devolve vazio legitimamente — e
Uruburetama (151 leis) e Aratuba (80) têm acervos pequenos demais para serem
completos. A §8 da pré-especificação recebe isso como ameaça declarada.

**A fazer:** resolver Itapajé, e rodar a fase 2 (os 184) como verificação de
completude — nenhum dos dois bloqueia a estimação.

Escopo em duas fases, por custo-benefício: um ban em município de dose **zero**
quase não enviesa — ele já entra como não tratado. O que morde é ban em município
de **dose alta**.

| Fase | Alvo | Por quê |
|---|---|---|
| 1 | união do decil superior entre as culturas candidatas (~30) | cobre exatamente onde o viés existe |
| 2 | os 184 | verificação de completude; não bloqueia nada |

Produto: **`docs/legislacao/bans-municipais-ce.csv`** — no repositório, não em
`data/`. É tabela derivada pequena e segura, e `data/` é gitignored: um arquivo
ali nunca chega às sessões remotas, que é a causa-raiz já paga duas vezes nesta
linhagem.

⚠️ **A coluna `confianca` não é enfeite.** Ausência de lei no site de uma câmara
**não é prova de ausência de lei** — muitas não publicam acervo histórico. O CSV
tem de separar "conferido, não há" de "não foi possível conferir", e a segunda
categoria entra na §8 da pré-especificação como ameaça declarada, não como zero.

### 2. O registro da SEMACE resolve o `d = 0` operacional

O **art. 8º** determina: *"Deverão ser registradas na SEMACE as Empresas
Prestadoras de Serviços, Empresas Agropecuárias e Empresas de Armazenamento e
Expurgos de sementes, que utilizam agrotóxicos, para fins fitossanitários"*. E o
art. 4º já obriga prestadoras de serviço de **aplicação** a se registrarem em
órgão estadual ou municipal.

Isso é uma fonte **estadual** para a definição 3 de `d = 0` (o zero que mede o
método, não a cultura) — provavelmente melhor e mais local que ANAC/MAPA/SINDAG,
porque cobre o prestador de serviço de aplicação no território cearense.
Fiscalização, pelos arts. 15 e 30, cabe a SEMACE, SEARA e Secretaria da Saúde —
possível fonte para a lacuna de *enforcement*.

**A fazer:** verificar se o cadastro da SEMACE é público e se tem série
histórica com município.

## Texto do art. 28-B nas duas redações

### 2019 — o ban (Lei 16.820/2019)

> **Art. 28-B.** É vedada a pulverização aérea de agrotóxicos na agricultura no
> Estado do Ceará.
> **§ 1º** A infração ao art. 1º sujeita o infrator ao pagamento de multa de 15
> mil (quinze mil) UFIRCEs.
> **§ 2º** Fica proibida a incorporação de mecanismos de controle vetorial por
> meio de dispersão por aeronave em todo o Estado do Ceará, inclusive para os
> casos de controle de doenças causadas por vírus.

Duas coisas que a redação estabelece: o ban é de **método**, não de molécula
(nenhum princípio ativo é nomeado), e **não é só agrícola** — o §2º alcança
controle vetorial aéreo, o que contamina o grupo de dose agrícola nula.

*(Nota de redação: o §1º pune "a infração ao art. 1º", que é o artigo que cria o
28-B, não a proibição em si. Erro de técnica legislativa sem efeito prático
aparente, mas vale saber que está lá.)*

### 2024 — a troca de instrumento (Lei 19.135/2024)

Nova redação: pulverização aérea vedada **"salvo se realizada por meio de
Aeronaves Remotamente Pilotadas – ARPs, Veículo Aéreo Não Tripulado – VANT ou
Drones"**, com orientação técnica de agrônomo e ART (§1º); **até 2 m acima da
copa e vento inferior a 10 km/h** (§2º); **30 m** de escolas, hospitais, praças,
APA e APP (§3º); apenas equipamento fabricado para pulverização, com piloto
habilitado ou empresa credenciada (§4º); multa de 15 mil UFIRCEs (§5º).

O §2º de 2019 — a proibição de controle vetorial aéreo — **foi revogado** pela
nova redação, que não o reproduz. Ou seja, a dispersão aérea sanitária volta a
ser possível a partir de 19/12/2024. Relevante para a janela: mais uma razão
para cortar em 19/12/2024.

Para o Ensaio 2: a lei de 2024 **não revoga o ban, substitui o instrumento** —
cota zero vira regulação de desempenho com zona-tampão. O Ceará rodou sozinho a
comparação que o Ensaio 2 propõe.
