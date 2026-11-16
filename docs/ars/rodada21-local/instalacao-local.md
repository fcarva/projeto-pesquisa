# Instalação local (Windows)

Comandos conferidos na documentação do Claude Code em 2026-11-16
(code.claude.com/docs). Eles mudam; se algo falhar, a documentação vale mais
que este arquivo.

## Windows nativo ou WSL 2
A documentação não recomenda um dos dois. A diferença que importa aqui: o
isolamento (sandbox) só existe no WSL 2. No Windows nativo, a regra que nega
`data/` vale para leitura e edição de arquivo, mas um comando de terminal pode
contorná-la. Para o laço autônomo, WSL 2 é o caminho mais seguro.

## Passos
1. **Claude Code.** PowerShell: `irm https://claude.ai/install.ps1 | iex`.
   No WSL: `curl -fsSL https://claude.ai/install.sh | bash`. Conferir com
   `claude --version` e `claude doctor`. No nativo, instalar o Git for Windows.
2. **Repositório.** Na pasta do projeto: `git fetch origin
   claude/gifted-maxwell-ryr7yk`, `git checkout claude/gifted-maxwell-ryr7yk`,
   `git pull`.
3. **Plugin ARS.** Dentro do Claude Code:
   `/plugin marketplace add Imbad0202/academic-research-skills` e depois
   `/plugin install academic-research-skills --marketplace Imbad0202/academic-research-skills`.
   ⚠️ A forma sem o marketplace, que está no `CLAUDE.md`, não aparece na
   documentação atual.
4. **R.** R 4.x com Rtools (no nativo). Da raiz: `Rscript -e "renv::restore()"`.
   Para as provas bastam `fixest` e `data.table`; o restante do `renv.lock`
   (arrow, CVXR, contdid) é do pipeline de estimação e demora a compilar.
5. **Python.** `pip install -r requirements.txt`.
6. **LaTeX.** TeX Live ou MiKTeX com `abntex2` e `latexmk`.
7. **Conferir.** `make teste`, `make projeto` (15 páginas textuais: Introdução
   na 5, Referências na 20) e `make provas REPS=5` (cerca de um minuto).

`make` no Windows nativo vem com o Rtools ou com o Git Bash; no WSL, do
`build-essential`.
