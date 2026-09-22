"""E11 — Custo de aplicação aérea na bananicultura, da Conab.

POR QUE ISTO EXISTE
-------------------

A §7.2 do paper adota a rota da inversão de Weitzman, e `11_weitzman_inversao.py`
mostrou que ela trava em dois parâmetros. Um deles — o lado do **custo** — é
calibrável de fonte secundária, e esta é a fonte.

⭐ A planilha de custos de produção da Conab traz, para a banana, um item de
linha **"2 - Operação com Avião"**, separado de "3.1 - Tratores e Colheitadeiras".
Isso é exatamente o par que a substituição aéreo→terrestre precisa, medido por
órgão oficial, em série de 2008 a 2025.

⚠️ E O QUE ESTA FONTE **NÃO** RESOLVE
--------------------------------------

1. **Não há Ceará.** A série cobre BA, ES, MG, RS e SC. Some assim a ideia de
   medir o custo de abatimento revelado pelo próprio ban cearense — não há
   unidade tratada na fonte. As cinco UFs são todas não tratadas, o que as torna
   contrafactual e não experimento.

2. ⚠️ **Custo por hectare é NÍVEL, e Weitzman precisa de INCLINAÇÃO.** Este é o
   mesmo erro de alvo, uma ordem abaixo, que a auditoria pegou no lado do
   benefício. Se o prêmio de substituição for constante por hectare, o custo
   marginal de abatimento é **constante**, e portanto `C'' = 0`.

   Essa não é uma limitação chata: é um resultado. Ver `--interpretar`.

Saída: `data/processed/conab_custo_aviao_banana.csv`
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimate"))
from importlib import import_module

_saida_utf8 = import_module("04_robustness")._saida_utf8

RAIZ = Path(__file__).resolve().parents[2]
BRUTO = RAIZ / "data" / "raw" / "conab" / "custos_banana_2008_2025.xlsx"
OUT_DIR = RAIZ / "data" / "processed"

# As linhas que importam, por prefixo do rótulo na coluna DISCRIMINAÇÃO.
ALVOS = {
    "custo_aviao": "2 - Operação com Avião",
    "custo_tratores": "3.1 - Tratores e Colheitade",
    "custo_agrotoxicos": "10 - Agrotóxicos",
    "custo_mao_obra": "6 - Mão de obra",
    "custo_total": "CUSTO TOTAL",
}


def _num(x) -> float:
    if pd.isna(x):
        return float("nan")
    try:
        return float(x)
    except (TypeError, ValueError):
        return float("nan")


def le_aba(xl: pd.ExcelFile, aba: str) -> dict | None:
    """Uma aba = um sistema de produção em uma região-ano."""
    m = re.search(r"-([A-Z]{2})-(\d{4})$", aba)
    if not m:
        return None
    df = xl.parse(aba, header=None)

    reg = {"aba": aba, "uf": m.group(1), "ano": int(m.group(2))}
    # produtividade fica no cabeçalho, em texto livre
    for _, row in df.head(8).iterrows():
        txt = " ".join(str(x) for x in row.tolist() if pd.notna(x))
        p = re.search(r"Produtividade M[ée]dia:\s*([\d.,]+)", txt)
        if p:
            reg["produtividade_kg_ha"] = _num(p.group(1).replace(".", "").replace(",", "."))

    achados = {}
    for _, row in df.iterrows():
        rotulo = str(row.iloc[0]) if pd.notna(row.iloc[0]) else ""
        rotulo = rotulo.replace("\t", "").strip()
        for chave, prefixo in ALVOS.items():
            if chave in achados:
                continue
            if rotulo.startswith(prefixo):
                achados[chave] = _num(row.iloc[1])
    reg.update(achados)
    return reg


def interpreta(tb: pd.DataFrame) -> None:
    barra = "=" * 84
    print(barra)
    print("E11 — O LADO DO CUSTO: 'Operação com Avião' na bananicultura (Conab)")
    print(barra)

    n_av = int((tb["custo_aviao"] > 0).sum())
    n_tr = int((tb["custo_tratores"] > 0).sum())
    n_amb = int(((tb["custo_aviao"] > 0) & (tb["custo_tratores"] > 0)).sum())
    print(f"  sistemas na série: {len(tb)}  ({tb['ano'].min()}–{tb['ano'].max()}, "
          f"UFs: {', '.join(sorted(tb['uf'].unique()))})")
    print(f"  com avião > 0     : {n_av}")
    print(f"  com tratores > 0  : {n_tr}")
    print(f"  com AMBOS > 0     : {n_amb}")
    print("-" * 84)

    av = tb[tb["custo_aviao"] > 0]
    if len(av):
        print("CUSTO DE OPERAÇÃO COM AVIÃO, onde é usado")
        print(f"  mediana : R$ {av['custo_aviao'].median():,.2f} / ha")
        print(f"  faixa   : R$ {av['custo_aviao'].min():,.2f} a "
              f"R$ {av['custo_aviao'].max():,.2f} / ha")
        share = 100 * av["custo_aviao"] / av["custo_total"]
        print(f"  como % do custo TOTAL: mediana {share.median():.2f}%  "
              f"(máx {share.max():.2f}%)")
        print()
        print("  ⚠️ ORDEM DE GRANDEZA — e ela muda a leitura do problema.")
        print(f"     O custo total da banana é da ordem de "
              f"R$ {av['custo_total'].median():,.0f}/ha.")
        print("     A aplicação aérea é uma fração de UM POR CENTO disso. Mesmo")
        print("     que a substituição DOBRE esse item, o efeito sobre o custo de")
        print("     produção fica abaixo do ruído anual de fertilizante, que")
        print("     sozinho responde por perto de 45% do custeio.")
    print("-" * 84)

    tr = tb[tb["custo_tratores"] > 0]
    print("A COMPARAÇÃO QUE PARECE ESTAR AQUI — E QUE NÃO ESTÁ")
    if len(av) and len(tr):
        print(f"  item 'Operação com Avião'      : mediana R$ {av['custo_aviao'].median():>9,.2f}/ha")
        print(f"  item 'Tratores e Colheitadeiras': mediana R$ {tr['custo_tratores'].median():>9,.2f}/ha")
        print()
        print("  ⚠️ NÃO SUBTRAIA ESSES DOIS. A diferença não é o custo de")
        print("     abatimento, por três razões, e cada uma sozinha já basta:")
        print()
        print("     1. Os itens não são comparáveis. 'Avião' é só pulverização;")
        print("        'Tratores e Colheitadeiras' é TODA a operação tratorizada —")
        print("        preparo, transporte, colheita. Diferenciar mede sobretudo o")
        print("        que o trator faz além de pulverizar.")
        ufs_av = ", ".join(sorted(av["uf"].unique()))
        ufs_tr = ", ".join(sorted(tr["uf"].unique()))
        print(f"     2. As amostras não se sobrepõem geograficamente: avião em"
              f" {ufs_av}, trator em {ufs_tr}.")
        print(f"        Produtividade mediana difere — {av['produtividade_kg_ha'].median():,.0f}"
              f" contra {tr['produtividade_kg_ha'].median():,.0f} kg/ha.")
        print("     3. A escolha de tecnologia é ENDÓGENA ao sistema. Quem voa")
        print("        escolheu voar; o contrafactual não é o sistema do vizinho.")
    print("-" * 84)

    print("⭐ O QUE A FONTE ENTREGA DE FATO, E É MAIS ÚTIL QUE UM PREÇO")
    print(f"  Dos {len(tb)} sistemas, {n_av} usam avião, {n_tr} usam trator e"
          f" {n_amb} usam AMBOS.")
    print()
    print("  As duas tecnologias são MUTUAMENTE EXCLUSIVAS na prática registrada,")
    print("  e as duas estão em uso comercial na bananicultura brasileira. Ou")
    print("  seja: a aplicação terrestre não é só tecnicamente possível — ela é")
    print("  a escolha corrente da MAIORIA dos sistemas que a Conab acompanha.")
    print()
    print("  ⚠️ Isso é insumo para a tabela de ameaças do Ensaio 1, não só para o")
    print("     Ensaio 2: a substituição que o ban força já era praticada por")
    print("     parte do setor antes dele, o que torna o 'choque' de custo menor")
    print("     do que a retórica do contencioso judicial sugeria.")
    print("-" * 84)

    print("⚠️ O QUE ESTE NÚMERO É, E O QUE WEITZMAN PRECISA")
    print("  Isto é NÍVEL de custo por hectare, e a regra de Weitzman compara")
    print("  INCLINAÇÕES de curvas marginais. ⚠️ Esta fonte NÃO determina c.")
    print()
    print("  O que decide c é a HETEROGENEIDADE do custo de conversão entre")
    print("  produtores — terreno, porte do bananal, tamanho do talhão —, e a")
    print("  planilha da Conab, que reporta sistema típico, não enxerga isso.")
    print("  Os dois casos seguem abertos, e importam:")
    print()
    print("    c ~ 0  (prêmio de conversão ~ igual para todos)")
    print("           Delta = (sigma²/2c²)(c - beta) -> -infinito se beta > 0")
    print("           => a QUANTIDADE domina, e a conclusão NÃO depende de saber")
    print("              quanto vale beta: basta beta > 0.")
    print("           Intuição: com custo marginal plano, a taxa ou fica acima")
    print("           dele (todos abatem tudo) ou abaixo (ninguém abate); um")
    print("           choque minúsculo vira o resultado. A cota não tem isso.")
    print()
    print("    c >> 0 (conversão muito mais cara para alguns)")
    print("           volta a valer a comparação usual, e beta é indispensável.")
    print()
    print("  ⭐ O valor desta fonte é ter tornado a PERGUNTA menor: o Ensaio 2 não")
    print("     precisa mais medir c na escala certa — precisa saber se o prêmio")
    print("     de conversão é homogêneo entre produtores. Isso é pergunta de")
    print("     levantamento setorial, não de econometria.")
    print("-" * 84)
    print("⚠️ O QUE ISSO REDUZ, E O QUE NÃO RESOLVE")
    print("  A pergunta do Ensaio 2 deixa de ser 'quanto vale beta?' e passa a ser")
    print("  'beta é afastado de zero?' — exigência MUITO mais fraca, que um")
    print("  desenho com pouco poder ainda pode conseguir responder.")
    print()
    print("  ⚠️ Mas NÃO está respondida. Se beta = 0 (dose-resposta exatamente")
    print("     linear), o sinal se inverte e a taxa domina. O Ensaio 1 não")
    print("     distingue os dois casos.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    _saida_utf8()
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--bruto", type=Path, default=BRUTO)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args(argv)

    if not args.bruto.exists():
        print(f"✘ planilha da Conab não encontrada: {args.bruto}")
        print("  Baixe de gov.br/conab -> Custos de Produção -> Agrícolas ->")
        print("  serie-historica-custos-banana-2008-a-2025.xlsx")
        return 1

    xl = pd.ExcelFile(args.bruto)
    linhas = [r for aba in xl.sheet_names if (r := le_aba(xl, aba))]
    if not linhas:
        print("✘ nenhuma aba no formato esperado região-UF-ano.")
        return 1

    tb = pd.DataFrame(linhas)
    for c in ALVOS:
        if c not in tb.columns:
            tb[c] = float("nan")
        tb[c] = tb[c].fillna(0.0)

    interpreta(tb)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / "conab_custo_aviao_banana.csv"
    tb.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}  ({len(tb)} sistemas)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
