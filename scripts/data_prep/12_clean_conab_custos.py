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

🔴 CORRIGIDO EM 2026-09-23: A LEITURA PERDIA A MAIOR PARTE DA SÉRIE
------------------------------------------------------------------
A auditoria de 2026-09-23 reexecutou este extrator na planilha oficial (88 abas
região–UF–ano) e contou 72/88 custos de avião, 69/88 de trator e 57/88 custos
totais AUSENTES. Duas causas, as duas daqui:

1. **Rótulo casado por prefixo literal.** As abas antigas escrevem
   "1 - Operação com avião"; o código exigia "2 - Operação com Avião". Agora o
   rótulo é normalizado (sem numeração, sem acento, sem caixa) antes de casar.
2. **Ausente virava zero** (`fillna(0.0)`), e a contagem "avião e trator nunca
   aparecem juntos" era feita sobre esses zeros. A conclusão de que as duas
   tecnologias são "mutuamente exclusivas" e de que o trator é "a escolha da
   maioria" não se sustenta e saiu do relatório. Agora ausente fica ausente, e
   a contagem separa positivo, zero e ausente.

E o item de máquinas mudou de categoria entre os leiautes: as abas antigas têm
"Operação com máquinas próprias" e "Aluguel de máquinas/serviços", não
"Tratores e Colheitadeiras". Não são o mesmo item, e a coluna `leiaute` diz
qual é qual em vez de fingir série contínua.

Saída: `data/processed/conab_custo_aviao_banana.csv`
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimate"))
from importlib import import_module

_saida_utf8 = import_module("04_robustness")._saida_utf8

RAIZ = Path(__file__).resolve().parents[2]
BRUTO = RAIZ / "data" / "raw" / "conab" / "custos_banana_2008_2025.xlsx"
OUT_DIR = RAIZ / "data" / "processed"

# As linhas que importam, pelo início do rótulo NORMALIZADO (sem a numeração
# do item, sem acento, em minúsculas) na coluna DISCRIMINAÇÃO. A numeração muda
# entre leiautes ("1 - Operação com avião" nas abas antigas, "2 - Operação com
# Avião" nas novas); o texto, não.
ALVOS = {
    "custo_aviao": "operacao com aviao",
    "custo_tratores": "tratores e colheitade",
    "custo_agrotoxicos": "agrotoxicos",
    "custo_mao_obra": "mao de obra",
    "custo_total": "custo total",
}
# Marca do leiaute antigo, em que máquinas não é "Tratores e Colheitadeiras".
LEIAUTE_ANTIGO = "operacao com maquinas proprias"


def normaliza_rotulo(rotulo: str) -> str:
    """Sem acento, sem caixa, sem a numeração do item ("3.1 - "), sem hífen."""
    s = unicodedata.normalize("NFKD", str(rotulo)).encode("ascii", "ignore").decode()
    s = s.replace("\t", " ").strip().casefold()
    s = re.sub(r"^\d+(\.\d+)*\s*-\s*", "", s)
    return re.sub(r"\s+", " ", s.replace("-", " ")).strip()


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
    leiaute = "novo"
    for _, row in df.iterrows():
        rotulo = normaliza_rotulo(row.iloc[0]) if pd.notna(row.iloc[0]) else ""
        if rotulo.startswith(LEIAUTE_ANTIGO):
            leiaute = "antigo"
        for chave, prefixo in ALVOS.items():
            if chave in achados:
                continue
            if rotulo.startswith(prefixo):
                achados[chave] = _num(row.iloc[1])
    reg.update(achados)
    reg["leiaute"] = leiaute
    return reg


def contagem(tb: pd.DataFrame, coluna: str) -> dict:
    """Positivo, zero e AUSENTE, separados. Ausente não é zero."""
    serie = tb[coluna] if coluna in tb.columns else pd.Series(dtype=float)
    return {"positivo": int((serie > 0).sum()), "zero": int((serie == 0).sum()),
            "ausente": int(serie.isna().sum() + (len(tb) - len(serie)))}


def interpreta(tb: pd.DataFrame) -> None:
    barra = "=" * 84
    print(barra)
    print("E11 — O LADO DO CUSTO: 'Operação com Avião' na bananicultura (Conab)")
    print(barra)
    print(f"  sistemas na série: {len(tb)}  ({tb['ano'].min()}–{tb['ano'].max()}, "
          f"UFs: {', '.join(sorted(tb['uf'].unique()))})")
    n_antigo = int((tb.get("leiaute", pd.Series(dtype=str)) == "antigo").sum())
    print(f"  abas no leiaute antigo (máquinas ≠ 'Tratores e Colheitadeiras'): {n_antigo}")
    print()
    print(f"  {'item':<24} {'positivo':>9} {'zero':>6} {'ausente':>8}")
    for col, rot in (("custo_aviao", "operação com avião"),
                     ("custo_tratores", "tratores e colheitad."),
                     ("custo_total", "custo total")):
        c = contagem(tb, col)
        print(f"  {rot:<24} {c['positivo']:>9} {c['zero']:>6} {c['ausente']:>8}")
    print("  ⚠️ Ausente é rótulo não achado ou célula vazia, NÃO custo zero.")
    print("-" * 84)

    av = tb[tb["custo_aviao"] > 0]
    if len(av):
        sistemas = av["aba"].str.replace(r"-\d{4}$", "", regex=True).nunique()
        print("CUSTO DE OPERAÇÃO COM AVIÃO, onde a planilha o registra")
        print(f"  registros: {len(av)}  |  sistemas/localidades distintos: {sistemas}")
        print(f"  mediana : R$ {av['custo_aviao'].median():,.2f} / ha")
        print(f"  faixa   : R$ {av['custo_aviao'].min():,.2f} a "
              f"R$ {av['custo_aviao'].max():,.2f} / ha")
        share = 100 * av["custo_aviao"] / av["custo_total"]
        if share.notna().any():
            print(f"  como % do custo TOTAL: mediana {share.median():.2f}%  "
                  f"(máx {share.max():.2f}%)")
        print("  ⚠️ Poucos registros, e podem ser o MESMO sistema em anos seguidos:")
        print("     não são tecnologias independentes, nem amostra de produtores,")
        print("     nem Ceará, nem 2018. Custo contábil de uma operação também não")
        print("     é custo de abatimento: perda de rendimento, capital e escassez")
        print("     de substituto não aparecem nesta linha.")
    print("-" * 84)

    print("O QUE ESTA FONTE NÃO SUSTENTA (auditoria de 2026-09-23)")
    print("  • Que avião e trator sejam MUTUAMENTE EXCLUSIVOS: com a maior parte")
    print("    das células ausente, 'nunca aparecem juntos' não é evidência; e")
    print("    'Tratores e Colheitadeiras' é TODA a operação tratorizada, não a")
    print("    pulverização terrestre.")
    print("  • Que a aplicação terrestre seja 'a escolha da maioria' do setor.")
    print("  • Que o choque de custo do ban seja pequeno.")
    print("-" * 84)

    print("⚠️ NÍVEL NÃO É INCLINAÇÃO, E O CASO c → 0 NÃO DECIDE NADA SOZINHO")
    print("  Weitzman compara inclinações de curvas marginais; custo por hectare")
    print("  é nível. Com prêmio de conversão igual para todos, C'' = 0, e a")
    print("  fórmula local Δ = σ²(c − β)/(2c²) diverge quando c → 0.")
    print("  ⚠️ A divergência é da APROXIMAÇÃO LOCAL, não do bem-estar: com")
    print("     abatimento limitado a [0, Q] e choques de esperança finita, a")
    print("     diferença entre taxa e cota é finita. Não é vantagem infinita da")
    print("     quantidade. E proibir é o canto da cota, não a cota ótima do")
    print("     modelo: mostrar que a cota ótima vence a taxa ótima não mostra")
    print("     que a proibição total vence.")
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
        # ⚠️ sem fillna(0): ausente não é zero (auditoria de 2026-09-23)

    interpreta(tb)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / "conab_custo_aviao_banana.csv"
    tb.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}  ({len(tb)} sistemas)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
