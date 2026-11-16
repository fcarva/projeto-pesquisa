# Laço autônomo — regras

O laço propõe uma mudança, roda a bateria, mede e guarda ou descarta. Ele só
existe sobre **dado simulado**. Sobre o desfecho real, tentar especificações
até melhorar é busca de especificação e destrói a hipótese confirmatória.

## Objetivo
Achar uma inferência para o coeficiente de município com avião × exposição
alta × pós-lei que tenha tamanho de teste correto com poucos municípios
tratados e de porte diferente da comparação. Primeira tarefa: implementar o
procedimento que o projeto declara principal, Ferman e Pinto (2019), que hoje
falta em `scripts/simulacao/02_estimadores.R`.

## Métrica (linha `METRICA` no fim de `make provas`)
1. `erro_tamanho_max`: maior distância entre a taxa de rejeição a 5% sob
   efeito zero e 0,05, nos cenários de tamanho. Vem primeiro.
2. `emd80_7trat`: efeito mínimo detectável. Só se compara entre procedimentos
   cujo tamanho esteja dentro de dois erros-padrão de Monte Carlo.

Com 200 repetições o erro-padrão de Monte Carlo é 0,015: diferença menor que
0,03 no tamanho é ruído. Decisão de guardar exige `REPS=1000`.

## O que o laço pode e não pode tocar
| arquivo | regra |
|---|---|
| `scripts/simulacao/02_estimadores.R` | editável; `estimar(d)` continua devolvendo `beta` e o vetor `p` |
| `scripts/simulacao/01_gerador_painel.R` | travado: é o mundo |
| `scripts/simulacao/03_bateria.R` | travado: é a régua |
| `data/`, `paper/`, `docs/`, `Makefile`, `CLAUDE.md` | travados |

Acrescentar um procedimento novo é acrescentar um nome ao vetor `p`; não se
remove nem se renomeia procedimento existente, para a comparação continuar
possível.

## Como rodar
- Cópia de trabalho com ramo próprio: `claude --worktree provas-inferencia`.
- Negar `data/` em `.claude/settings.json` (o pesquisador grava; o laço não
  edita configuração):
  ```json
  { "permissions": { "deny": ["Read(./data/**)", "Edit(./data/**)"] } }
  ```
- Raciocínio alto para esta tarefa: `/effort high`.
- Interativo: `/loop` com o pedido abaixo. Sem interação:
  `claude -p "<pedido>" --max-turns 40 --allowedTools "Read,Edit,Bash(Rscript *),Bash(make provas*),Bash(git add *),Bash(git commit *)"`.
- Limite: 10 experimentos por rodada. Um commit por experimento, com a linha
  `METRICA` antes e depois na mensagem. Experimento que piora é revertido, e a
  tentativa fica anotada em `docs/ars/rodada21-local/experimentos.tsv`
  (única exceção ao travamento de `docs/`).

## Pedido
> Leia `docs/ars/rodada21-local/laco-autonomo.md` e siga as regras. Rode
> `make provas` para ter a linha de base. Proponha uma mudança em
> `scripts/simulacao/02_estimadores.R`, rode de novo, compare a métrica,
> guarde ou reverta, registre. Pare em 10 experimentos ou quando o erro de
> tamanho estiver dentro do ruído de Monte Carlo com `REPS=1000`.

## Linha de base (teste de fumaça de 2026-11-16, 20 repetições)
Com 20 repetições o erro-padrão de Monte Carlo é 0,049, então os números só
dizem a direção: o erro-padrão agrupado por município rejeitou demais sob
efeito zero (pior com 2 tratados), e a permutação simples rejeitou de menos.
Nenhum dos dois serve como está. Parâmetros do gerador são hipotéticos.

## O que sai daqui
A inferência escolhida e a tabela de poder vão para o plano de análise, que o
orientador ratifica. Só depois o código roda, uma vez, sobre o dado real.
