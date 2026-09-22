"""E10 — A inversão de Weitzman: qual inclinação faria a proibição perder?

A ROTA ESCOLHIDA, E POR QUE ELA EXISTE
---------------------------------------

A §3 do paper prometeu que o Ensaio 1 entregaria a âncora empírica do Ensaio 2.
Não entregou: o agregado do `ACR(d)` não é interpretável (§6.2). A §7.2 põe três
rotas, e a escolhida é a terceira — **inverter a pergunta**. Em vez de estimar a
inclinação e alimentar a regra de Weitzman, perguntar qual inclinação seria
necessária para **inverter o ranking** entre proibir e taxar, e então confrontar
esse valor com o que o dado consegue excluir.

⚠️ E AO MONTAR A INVERSÃO APARECE UM PROBLEMA DE ALVO
------------------------------------------------------

A §3 diz que "o Ensaio 2 consome a derivada". Isso é impreciso, e a imprecisão
importa. Escrevendo o mapeamento:

    B(q)   = benefício de abater q de exposição  = |ATT(q|q)|
    B'(q)  = benefício MARGINAL do abatimento    = |ACR(q)|
    B''(q) = inclinação do benefício marginal    = ACR'(q)   <- Weitzman usa ESTA

Weitzman compara a inclinação do benefício marginal com a do custo marginal.
O `ACR` é o benefício marginal; a regra precisa da **inclinação dele**. Ou seja,
o Ensaio 2 consome a derivada SEGUNDA da dose-resposta, não a primeira.

O que salva parcialmente a formulação da §3 é que ter a **curva** inteira de
`ACR` — e não um ponto — dá o `ACR'` de imediato. Era por isso que a curva era o
alvo. Mas o objeto consumido é a inclinação dela.

⚠️ Consequência dura: o Ensaio 1 estima o `ACR` com erro-padrão que cobre zero em
todas as faixas. A derivada disso é ainda menos identificada. A inversão não
contorna esse fato — ela o torna **preciso**, dizendo exatamente o que teria de
ser verdade.

A REGRA, FORMALMENTE
--------------------

Weitzman (1974), aproximação linear-quadrática, com choque aditivo no custo
marginal de variância sigma²:

    Delta = E[W_preço] - E[W_quantidade] = (sigma² / (2c²)) * (c - beta)

onde  beta = |B''| >= 0  (inclinação do benefício marginal, em módulo)
      c    = C''    > 0  (inclinação do custo marginal)

    Delta > 0  ->  o PREÇO (taxa) domina     <=>  c > beta
    Delta < 0  ->  a QUANTIDADE (proibição) domina  <=>  beta > c

**O limiar é beta = c.** A proibição cearense é o caso-limite de cota em zero,
então a pergunta da inversão é: *quão inclinado teria de ser o benefício marginal
para que a proibição fosse a escolha certa?* Resposta: tão inclinado quanto o
custo marginal. O que a inversão acrescenta é o **confronto com a incerteza**.

⚠️ O QUE ESTE SCRIPT NÃO TEM, E NÃO FINGE TER
----------------------------------------------

O lado do CUSTO não vem do Ensaio 1 e **não existe neste repositório**. `c`
precisa de calibração externa: custo de aplicação aérea vs terrestre por hectare,
perda de rendimento na substituição, e a variância do choque de custo. Enquanto
não houver, este script devolve **fronteira**, não resposta — para cada `c`
plausível, o `beta` que inverte o ranking.

Isso é a forma honesta de fazer análise de política com desenho imperfeito: dizer
o que teria de ser verdade, e quão longe se está de saber.

Saída: `data/processed/weitzman_inversao.csv`
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
_saida_utf8 = _rb._saida_utf8

RAIZ = Path(__file__).resolve().parents[2]
OUT_DIR = RAIZ / "data" / "processed"

# Do Ensaio 1 (§6 do paper). Unidades: gramas de peso ao nascer por unidade de
# dose, onde a dose é normalizada em [0, 1].
ACR_PONTO = 6.81
ACR_IC = (-46.45, 57.85)      # inversão por aleatorização, 95%


# --------------------------------------------------------------------------
# A regra
# --------------------------------------------------------------------------

def vantagem_preco(beta: float, c: float, sigma: float) -> float:
    """Delta = E[W_preço] - E[W_quantidade]. Positivo => taxa domina."""
    if c <= 0:
        return float("nan")
    return (sigma ** 2 / (2.0 * c ** 2)) * (c - beta)


def limiar_beta(c: float) -> float:
    """O beta que zera a vantagem. Trivialmente igual a c — e é o ponto.

    A regra de Weitzman é uma comparação de inclinações; o limiar não depende de
    sigma. O que sigma controla é a MAGNITUDE da vantagem, não o lado dela.
    Registrar isso evita a leitura errada de que mais incerteza favoreceria um
    dos instrumentos.
    """
    return c


def fronteira(cs: np.ndarray, sigma: float,
              beta_faixa: tuple[float, float] | None) -> pd.DataFrame:
    """Para cada c, o limiar de beta e o que se consegue concluir.

    ⚠️ `beta_faixa` NÃO vem do Ensaio 1, e o script se recusa a fingir que vem.
    O Ensaio 1 estima o `ACR` (benefício marginal); Weitzman usa `ACR'`
    (a inclinação dele). Usar o IC do primeiro como se fosse do segundo seria
    exatamente o tipo de erro de alvo que a auditoria deste projeto pegou em
    outro lugar. Enquanto o pesquisador não fornecer faixa calibrada por
    `--beta-min/--beta-max`, a coluna de conclusão devolve `indeterminado`.
    """
    linhas = []
    for c in cs:
        if beta_faixa is None:
            conclusao, delta_lo, delta_hi = "indeterminado", np.nan, np.nan
        else:
            b_lo, b_hi = beta_faixa
            delta_lo = vantagem_preco(b_hi, c, sigma)   # beta alto -> Delta baixo
            delta_hi = vantagem_preco(b_lo, c, sigma)
            if b_lo > c:
                conclusao = "proibição"
            elif b_hi < c:
                conclusao = "taxa"
            else:
                conclusao = "indeterminado"
        linhas.append({
            "c": c,
            "limiar_beta": limiar_beta(c),
            "beta_min": beta_faixa[0] if beta_faixa else np.nan,
            "beta_max": beta_faixa[1] if beta_faixa else np.nan,
            "delta_min": delta_lo,
            "delta_max": delta_hi,
            "conclusao": conclusao,
        })
    return pd.DataFrame(linhas)


# --------------------------------------------------------------------------
# Relatório
# --------------------------------------------------------------------------

def imprime(fr: pd.DataFrame, sigma: float) -> None:
    barra = "=" * 84
    print(barra)
    print("E10 — INVERSÃO DE WEITZMAN: o que teria de ser verdade")
    print(barra)
    print("Regra:  Delta = (sigma²/2c²)(c - beta)   |   beta = |B''| ; c = C''")
    print("        Delta > 0 -> taxa domina         |   beta > c -> proibição domina")
    print()
    print("⚠️ ALVO: Weitzman usa a INCLINAÇÃO do benefício marginal, que é a")
    print("   derivada SEGUNDA da dose-resposta (ACR'), não o ACR. A §3 do paper")
    print("   diz 'consome a derivada' e é impreciso — ver o docstring.")
    print("-" * 84)

    print("O QUE O ENSAIO 1 ENTREGA — e é UM OBJETO ACIMA do que a regra pede")
    print(f"  ACR (benefício marginal): {ACR_PONTO:+.2f} g por unidade de dose")
    print(f"  IC 95% por aleatorização: [{ACR_IC[0]:+.2f} ; {ACR_IC[1]:+.2f}]")
    print("  ⚠️ Weitzman precisa da INCLINAÇÃO disto, e o IC acima cobre zero com")
    print("     folga. A derivada de uma curva não identificada não é")
    print("     identificada. Portanto o Ensaio 1 NÃO restringe beta — nem um")
    print("     pouco — e o script não vai fingir que restringe.")
    print("-" * 84)

    tem_beta = fr["conclusao"].ne("indeterminado").any()
    print(f"FRONTEIRA — para cada c, o beta que inverte o ranking (sigma = {sigma:g})")
    print()
    print(f"  {'c (custo marg.)':>16} {'limiar beta':>13} {'conclusão':>15}")
    print("  " + "-" * 47)
    for _, r in fr.iterrows():
        print(f"  {r['c']:>16.2f} {r['limiar_beta']:>13.2f} {r['conclusao']:>15}")

    print("-" * 84)
    if not tem_beta:
        print("⚠️  INDETERMINADO EM TODA A GRADE — e isto É o resultado.")
        print()
        print("    Nenhuma faixa de beta foi fornecida, porque nenhuma existe:")
        print("    o Ensaio 1 não identifica a curvatura da dose-resposta, e a")
        print("    literatura consultada não reporta esse objeto.")
        print()
        print("    A leitura correta NÃO é 'a inversão falhou'. É que a inversão")
        print("    localizou o gargalo com precisão: o que falta não é o lado do")
        print("    CUSTO, que é calibrável de fonte secundária — é o lado do")
        print("    BENEFÍCIO, e ele depende de um desenho com poder para a")
        print("    SEGUNDA derivada, que este não tem e não terá encorpando o")
        print("    grupo tratado na margem.")
        print()
        print("    ⚠️ Passe --beta-min/--beta-max para explorar cenários. Qualquer")
        print("       faixa assim é CALIBRAÇÃO declarada, jamais estimativa deste")
        print("       trabalho, e o texto tem de dizê-lo em cada uso.")
    else:
        n = int(fr["conclusao"].ne("indeterminado").sum())
        print(f"✔  A faixa de beta fornecida decide em {n} de {len(fr)} pontos.")
        print("   ⚠️ Sob CALIBRAÇÃO, não sob estimativa. Reportar como cenário.")
    print("-" * 84)
    print("O QUE FALTA PARA FECHAR — e não vem do Ensaio 1")
    print("  1. c  = inclinação do custo marginal de abatimento. Precisa de custo")
    print("         de aplicação aérea vs terrestre por hectare e perda de")
    print("         rendimento na substituição. NÃO existe neste repositório.")
    print("  2. sigma = desvio-padrão do choque de custo. Controla a MAGNITUDE da")
    print("         vantagem, nunca o lado dela.")
    print("  3. beta = ACR', que exige a curva identificada — o gargalo real.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--c-min", type=float, default=1.0)
    parser.add_argument("--c-max", type=float, default=60.0)
    parser.add_argument("--c-passos", type=int, default=9)
    parser.add_argument("--sigma", type=float, default=1.0,
                        help="DP do choque de custo; escala Delta, não o sinal")
    parser.add_argument("--beta-min", type=float, default=None,
                        help="⚠️ CALIBRAÇÃO, não estimativa deste trabalho")
    parser.add_argument("--beta-max", type=float, default=None)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    if (args.beta_min is None) != (args.beta_max is None):
        print("✘ --beta-min e --beta-max andam juntos ou nenhum dos dois.")
        return 2
    faixa = None if args.beta_min is None else (args.beta_min, args.beta_max)
    if faixa and faixa[0] > faixa[1]:
        print("✘ --beta-min maior que --beta-max."); return 2

    cs = np.linspace(args.c_min, args.c_max, args.c_passos)
    fr = fronteira(cs, args.sigma, faixa)
    imprime(fr, args.sigma)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / "weitzman_inversao.csv"
    fr.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
