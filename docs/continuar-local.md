# Continuar na máquina local

*2026-11-16. A sessão em nuvem escreve código e texto, mas não enxerga os
microdados: `data/` não é versionado. O que depende de dado roda aí.*

## 1. Trazer o trabalho da nuvem

```
git fetch origin
git checkout ccr-f547e31b-4vr6he
```

(ou faça o merge desse ramo no seu ramo de trabalho).

## 2. Conferir o que já foi baixado

```
python scripts/data_prep/19_inventario_local.py --conferir-ftp --salvar
```

- Varre `data/raw` e `data/processed`. Se os arquivos estiverem em outro lugar,
  acrescente `--pasta "C:/caminho/da/pasta"` (pode repetir).
- Mostra, arquivo por arquivo, o que o desenho de fronteira pede: SINASC do
  Ceará e do Rio Grande do Norte e o DOFET nacional, de 2005 a 2024.
- Situações possíveis: `ok`, `FALTA`, `INCOMPLETO` (download interrompido ou
  arquivo vazio), `TAMANHO DIFERE DO FTP`, `NAO EXISTE NO FTP`.
- No fim imprime os comandos para baixar só o que falta.
- `--salvar` grava `docs/inventario-local.md`, que tem apenas nomes e tamanhos.
  Se você fizer commit e push desse arquivo, a sessão em nuvem passa a saber o
  que existe aí.

Sem `make`? O comando acima é o mesmo que `make inventario`.

## 3. Duas coisas que o inventário pode revelar

- **`DO{UF}{ano}` não serve para óbito fetal.** O registro geral de óbitos por
  estado não traz os fetais. O arquivo certo é o `DOFET{AA}`, que é nacional.
- **O FTP pode não ter os anos mais antigos do Ceará no mesmo diretório.** Na
  conferência de setembro, o SINASC cearense começava em 2007 e o potiguar em
  2005. Se aparecer `NAO EXISTE NO FTP`, a janela começa no primeiro ano comum.

## 4. Rodar com o Claude Code na sua máquina

Abra o Claude Code na pasta do repositório (aplicativo de desktop ou terminal).
O `CLAUDE.md` já aponta para os documentos que mandam. Um começo de conversa
que funciona:

> Leia `docs/pre-especificacao-v2.md`, `docs/dag-identificacao.md` e
> `docs/inventario-local.md`. Baixe o que falta de SINASC e DOFET, estenda o
> script 03 para recortar também o Rio Grande do Norte, monte o painel CE + RN
> e rode `make mde-desenhos` e `make mde-calendario` só com o pré-período. Não
> estime nada pós-2019 antes de a pré-especificação estar assinada.

## 5. O que ainda só existe na nuvem até você puxar

- `paper/main.tex` e `paper/secoes/`: o texto consolidado do projeto.
- `scripts/data_prep/18_censo_agro_familiar.py`: avião por tipo de agricultura.
- `scripts/data_prep/19_inventario_local.py`: este inventário.
