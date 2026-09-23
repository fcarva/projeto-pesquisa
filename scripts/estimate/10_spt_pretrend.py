"""E9 — Teste de inclinação em dose no pré-período (a sonda do strong parallel trends).

POR QUE ESTE SCRIPT EXISTE
--------------------------

O repositório afirmava, em quatro lugares, que *"nenhum event study de leads
testa a SPT, por mais limpo que saia"*. A auditoria de 2026-09-22
(`docs/auditoria-pre-especificacao.md`, achado 3) mostrou que a afirmação é forte
demais, lendo o CGS §6.3:

> *"Another indirect way to assess the plausibility of SPT [...] is to compute
> ACRT^es_glob(e) [...] prior to treatment [...] both Assumptions PT and SPT have
> the same implication: that the average relationship between outcome changes for
> adjacent dose groups should be zero. **Our estimates of these pre-trends reject
> this in 1981, which is a pre-treatment period.**"*

Ou seja: existe implicação pré-tratamento, ela é testável, e na aplicação dos
próprios autores ela **rejeita**.

A formulação correta é mais estreita do que a que o repositório usava: o placebo
**não isola** o SPT — passar não o valida, porque a implicação é comum ao PT e ao
SPT. **Mas pode falsificá-lo.** "Não distingue" e "não testa" são coisas
diferentes.

⚠️ E O QUE FOI TESTADO ATÉ AQUI NÃO É ISTO
-------------------------------------------

`06_pretrends.R` e `07_honestdid.R` rodam sobre o event study **binário** do
TWFE, em **níveis** — falam do PT. O teste que o CGS descreve é sobre a
**inclinação em dose**: se a relação entre *variação* do desfecho e dose é plana
antes do ban. São objetos diferentes, e o segundo nunca havia sido computado.

Isso importa porque o alvo que a pré-especificação declarou **primário** — a
curva `ACR(d)` — é justamente o que precisa do SPT.

COMO O TESTE É CONSTRUÍDO
-------------------------

Placebo puro: finge-se que o ban ocorreu numa data do pré-período, e roda-se
EXATAMENTE a mesma forma reduzida do `04_robustness.py` — `dy ~ dose`, centrada
no grupo de dose zero. Se a inclinação for diferente de zero antes de existir
tratamento, a implicação comum a PT e SPT está violada.

A estrutura de janelas espelha a do desenho real (mesmo intervalo entre corte pré
e corte pós), para que o placebo seja comparável e não mais fácil por construção.

⚠️ Este script NÃO usa o `contdid` e portanto não esbarra na limitação do sieve
CCK, que não faz event study. É aritmética sobre o painel que já existe.

⚠️ E O NÍVEL ENTRA JUNTO (2026-09-23). O comentário 4 do parecer de 2026-09-22
pede inferência sobre o próprio ATT(d|d) agregado, e não só sobre a
inclinação. Cada corte placebo grava também o nível (`nivel`: média de dy dos
de dose > 0 menos a dos de dose = 0), e o relatório compara o nível real com
os placebos. É a pergunta que o −36 g da §6.2 tem de responder.

Saída: `data/processed/spt_pretrend__<desfecho>.csv`
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from importlib import import_module

_rb = import_module("04_robustness")
primeira_diferenca = _rb.primeira_diferenca
estima = _rb.estima
erro_padrao_ingenuo = _rb.erro_padrao_ingenuo
inferencia_aleatorizacao = _rb.inferencia_aleatorizacao
nivel = _rb.nivel
_saida_utf8 = _rb._saida_utf8
N_BOOT = _rb.N_BOOT
SEED = _rb.SEED

RAIZ = Path(__file__).resolve().parents[2]
PAINEL = RAIZ / "data" / "processed" / "painel_ensaio1.parquet"
OUT_DIR = RAIZ / "data" / "processed"

BAN_T = 2019 * 12 + 1 - 1  # 2019-01, vigência em 09/01/2019


def _t(aamm: str) -> int:
    a, m = (int(x) for x in aamm.split("-"))
    return a * 12 + m - 1


def _rotulo(t: int) -> str:
    return f"{t // 12}-{t % 12 + 1:02d}"


def placebos(t_inicio: int, t_fim: int, gap: int,
             largura_min: int) -> list[tuple[int, int]]:
    """Cortes placebo dentro do pré-período, espelhando o gap do desenho real.

    Cada corte devolve (t_pre, t_pos) tal que ambas as janelas cabem inteiras
    antes do ban. Exige `largura_min` meses de cada lado para que a média não
    seja de dois ou três pontos.
    """
    saida = []
    corte = t_inicio + largura_min
    while corte + gap + largura_min <= t_fim:
        saida.append((corte, corte + gap))
        corte += 6  # de seis em seis meses
    return saida


def imprime(res: pd.DataFrame, desfecho: str, real: dict | None,
            alfa: float) -> None:
    barra = "=" * 84
    print(barra)
    print(f"E9 — INCLINAÇÃO EM DOSE NO PRÉ-PERÍODO (sonda do SPT) | {desfecho}")
    print(barra)
    print("Implicação comum ao PT e ao SPT (CGS §6.3): antes do tratamento, a")
    print("relação entre VARIAÇÃO do desfecho e dose deve ser zero.")
    print()
    print("⚠️ Passar NÃO valida o SPT — a implicação é comum às duas hipóteses.")
    print("   Rejeitar, sim, é evidência CONTRA ele, e contra a leitura causal")
    print("   da curva ACR(d), que a pré-especificação declarou alvo primário.")
    print("-" * 84)

    print(f"  {'corte placebo':<18} {'n':>4} {'inclinação':>13} {'p (aleat.)':>11}  ")
    print("  " + "-" * 56)
    for _, r in res.iterrows():
        marca = "  ⚠️ REJEITA" if r["p"] < alfa else ""
        print(f"  {r['corte']:<18} {int(r['n_municipios']):>4} "
              f"{r['beta']:>13.5f} {r['p']:>11.4f}{marca}")

    n_rej = int((res["p"] < alfa).sum())
    n_tot = len(res)
    print("-" * 84)

    if n_rej == 0:
        print(f"✔  NENHUM dos {n_tot} cortes placebo rejeita a {alfa:.0%}.")
        print("   A implicação pré-tratamento comum a PT e SPT NÃO é violada onde")
        print("   se consegue olhar. Isso é evidência a favor, e é o mais forte")
        print("   que este teste consegue ser — ele não valida o SPT.")
    else:
        print(f"⚠️  {n_rej} de {n_tot} cortes placebo REJEITAM a {alfa:.0%}.")
        print("   Sob o nulo esperava-se cerca de "
              f"{alfa * n_tot:.1f}. Isto é evidência CONTRA a implicação comum,")
        print("   e portanto contra a interpretação causal da curva ACR(d).")
        print()
        print("   ⚠️ CONSEQUÊNCIA PARA O TEXTO: se isto rejeitar, a decisão de")
        print("      reportar o ATT(d|d) em vez do ACR(d) deixa de ser escolha")
        print("      do pesquisador e passa a ser EXIGIDA pelo dado — o que é")
        print("      defesa muito mais forte na banca.")

    if real is not None:
        print("-" * 84)
        print("PARA COMPARAR — a mesma forma reduzida no desenho de verdade:")
        print(f"  inclinação {real['beta']:+.5f}   p = {real['p']:.4f}")
        maior = (res["beta"].abs() >= abs(real["beta"])).sum()
        print(f"  cortes placebo com inclinação ao menos tão grande em módulo: "
              f"{maior} de {n_tot}")
        if maior > n_tot * 0.5:
            print("  ⚠️ A maioria dos placebos produz inclinação tão grande quanto a")
            print("     real. O desenho não separa o efeito do ruído de pré-período.")
        if "nivel" in res.columns and not np.isnan(real.get("nivel", np.nan)):
            print("-" * 84)
            print("E O NÍVEL — o ATT(d|d) agregado, que é o número da §6.2:")
            print(f"  real {real['nivel']:+.3f}   placebos: "
                  + ", ".join(f"{v:+.3f}" for v in res["nivel"]))
            maior_n = (res["nivel"].abs() >= abs(real["nivel"])).sum()
            print(f"  cortes placebo com nível ao menos tão grande em módulo: "
                  f"{maior_n} de {n_tot}")
            print("  ⚠️ Com poucos cortes, isto não é p-valor. É a pergunta que o")
            print("     parecer faz ao −36 g: ele está fora do ruído de pré-período?")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--painel", type=Path, default=PAINEL)
    parser.add_argument("--desfecho", default="peso_medio")
    parser.add_argument("--inicio", default="2015-01",
                        help="início do pré-período")
    parser.add_argument("--corte-pre", default="2018-12",
                        help="fim do pré-período do desenho real")
    parser.add_argument("--corte-pos", default="2019-10",
                        help="início do pós do desenho real; define o gap")
    parser.add_argument("--largura-min", type=int, default=12,
                        help="meses mínimos de cada lado do corte placebo")
    parser.add_argument("--alfa", type=float, default=0.05)
    parser.add_argument("--n-boot", type=int, default=N_BOOT)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    if not args.painel.exists():
        print(f"✘ painel não encontrado: {args.painel}")
        return 1

    painel = pd.read_parquet(args.painel)
    if args.desfecho not in painel.columns:
        print(f"✘ desfecho ausente no painel: {args.desfecho}")
        return 1

    t_ini, t_pre, t_pos = _t(args.inicio), _t(args.corte_pre), _t(args.corte_pos)
    gap = t_pos - t_pre

    cortes = placebos(t_ini, t_pre, gap, args.largura_min)
    if not cortes:
        print("✘ pré-período curto demais para qualquer corte placebo com")
        print(f"   largura mínima de {args.largura_min} meses e gap de {gap}.")
        print("   Baixe --largura-min ou amplie a janela com --inicio.")
        return 1

    print(f"pré-período: {args.inicio} .. {args.corte_pre}  "
          f"(gap do desenho real: {gap} meses)")
    print(f"cortes placebo construídos: {len(cortes)}\n")

    linhas = []
    for a, b in cortes:
        dados = primeira_diferenca(painel, args.desfecho, a, b)
        # só o pré-período: nada depois do ban pode entrar
        dados = dados[dados["dose"].notna()]
        if len(dados) < 10:
            continue
        beta = estima(dados)
        rnd = inferencia_aleatorizacao(dados, args.n_boot, args.seed)
        linhas.append({
            "corte": f"{_rotulo(a)} / {_rotulo(b)}",
            "t_pre": a,
            "t_pos": b,
            "n_municipios": len(dados),
            "beta": beta,
            "ep_ingenuo": erro_padrao_ingenuo(dados),
            "p": rnd["p"],
            "ic_baixo": rnd["ic_baixo"],
            "ic_alto": rnd["ic_alto"],
            # o nível, que é o ATT(d|d) agregado: comentário 4 do parecer
            "nivel": nivel(dados),
        })

    if not linhas:
        print("✘ nenhum corte placebo produziu amostra utilizável.")
        return 1

    res = pd.DataFrame(linhas)

    # o desenho real, para comparação
    reais = primeira_diferenca(painel, args.desfecho, t_pre, t_pos)
    real = {"beta": estima(reais),
            "p": inferencia_aleatorizacao(reais, args.n_boot, args.seed)["p"],
            "nivel": nivel(reais)}

    imprime(res, args.desfecho, real, args.alfa)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / f"spt_pretrend__{args.desfecho}.csv"
    res.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
