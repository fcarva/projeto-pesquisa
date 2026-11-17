# Resposta ao parecer do refine.ink (2026-11-17)

Parecer: cinco blocos de comentário geral e um comentário detalhado ("Major")
sobre inferência. Decisão do pesquisador: mudar o **alcance das conclusões**,
sem alterar o desenho principal, H1–H4 ou o caminho-alvo. O detalhe novo foi
para o Apêndice B (plano de análise), fora das 15 páginas.

| # | Comentário | Resposta | Local | Status |
|---|---|---|---|---|
| 1 | Zero verdadeiro × ausência de registro; intermitência; lacunas | Critérios de cobertura fixados antes; classificação voo / sem voo / sem registro; função de cada fonte; etapa de viabilidade | 2.1 (último parágrafo); 4.4 "Primeiro estágio"; B.1 | atendido |
| 2 | Deslocar o contraste para 2012 muda o objeto; seca não é choque simétrico | 2019 é a única avaliação da lei e estima o efeito total municipal; cessação anterior documentada significa que não havia aplicação em curso para a lei interromper; a interrupção pode motivar estudo complementar com identificação própria | 2.1; 4.4; B.1 (fim); `docs/pre-especificacao-v2.md` linha 8 | atendido |
| 3 | Controle definido por recorte institucional | Lista da região integrada como ponto de partida; lista final por critérios territoriais e produtivos; sensibilidade restrita à fruticultura irrigada; tabela de equilíbrio | 4.3; B.2 | atendido como plano; os critérios numéricos ficam para a pré-especificação |
| 4 | Tripla não fecha choque setorial; calendário precisa de hipótese sazonal; contaminação não é só atenuação | Ressalva na tripla; hipótese sazonal enunciada; "direção do viés não garantida" | 4.4; Tabela 2 | atendido |
| 5 | Qual contraste sustenta a conclusão causal | Fronteira é o primário; os demais são secundários e não substituem o seu intervalo | 4.2 | atendido |
| 6 | Inferência: permutabilidade, dependência, choque estadual residual (comentário detalhado) | Seção reescrita: procedimento a definir após verificar aplicabilidade; placebos potiguares não reproduzem choque diferencial entre estados; intervalos condicionais | 4.6; B.3; cap. 5 (limitações); `docs/inferencia-poucos-tratados.md` | **limitação explicitada no corpo; procedimento investigado, não justificado** (ver abaixo) |
| 7 | τ = 0 não informa a precisão dos intervalos | Poder dos parâmetros efetivamente estimados por simulação no pré-período, preservando porte e choques comuns | 4.5 (último parágrafo); B.3 | atendido como plano |
| 8 | Não rejeitar ≠ excluir caminho concorrente | Mecanismos como evidência de implementação e de compatibilidade, com intervalos; sem decomposição | 3.2; 4.4 "Mecanismos" | atendido |
| 9 | 1–2 g não é teto; 150 m não é fronteira universal | "Cenário de referência"; grade de cenários; fração exposta local é objeto de medida | 4.5; 1.3; resumo; B.4 | atendido |
| 10 | Custo-benefício: ligação monetária com o peso; dupla contagem; perspectiva, horizonte, contrafactual | Avaliação parcial; desfechos diretamente valoráveis; limiar em gramas só com a função peso → consequência clínica → custo evitado; produção e emprego como efeitos distributivos | 4.7; B.5 | atendido como estrutura; a calibração é trabalho do segundo ensaio |
| 11 | Comparação de instrumentos é condicional | Condicional a fiscalização, substituição e dano marginal; o efeito da lei não identifica os outros instrumentos | 4.7 | atendido |
| 12 | Tabela 4: a coluna de um ano não é o EMD do ATT periódico (A1) | As duas colunas são contrastes agregados; o poder do ATT trimestral é avaliado à parte | 4.5 | atendido |

## Item 6: o que a investigação entregou e o que não entregou

A leitura (`docs/inferencia-poucos-tratados.md`) confirma os três pontos do
parecer. Em resumo:

- Callaway e Sant'Anna supõem amostra iid de unidades e, para o bootstrap por
  conglomerado, número "grande" de conglomerados; o artigo declara que o
  procedimento não se justifica com poucos e remete a Conley–Taber e
  Ferman–Pinto sem estendê-los ao seu estimador.
- Conley–Taber e Ferman–Pinto recuperam a distribuição do erro dos tratados a
  partir dos controles. Nenhum representa um choque diferencial entre dois
  estados quando há um estado de cada lado (dedução da nota, não frase dos
  artigos).
- Duas saídas com restrição explícita: via série temporal do contraste (exige
  estacionariedade do choque diferencial) ou condicionar nos choques estaduais
  e tratá-los na sensibilidade a tendências paralelas.
- **Não demonstrado:** validade de qualquer método de poucos tratados para o
  ATT duplamente robusto, com covariáveis e ponderado por nascimentos.

Nenhum procedimento principal foi levado ao texto. Ficam para decisão do
pesquisador e do orientador: (i) qual das duas saídas propor; (ii) o alerta, em
Alvarez e Ferman, de que a versão duplamente robusta perde essa propriedade com
poucos tratados, o que toca a especificação fixada; (iii) citar ou não as
referências novas (só entram depois de registro + conteúdo no padrão do
projeto).
