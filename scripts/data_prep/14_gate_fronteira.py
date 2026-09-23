"""E14 — O gate da Rota 1: o desenho de fronteira CE × vizinho é viável?

POR QUE ESTE SCRIPT EXISTE
--------------------------

A Rota 1 (`docs/auditoria-mensuracao-do-tratamento.md` §4) propõe trocar o grupo
de comparação — de "município cearense com área zero" para "município do estado
vizinho, no mesmo complexo agrícola, sob o regime anterior". Se ela procede, a
flag 7 (diluição do tratamento) **sai do desenho principal** em vez de ser
limitada, porque o tratamento passa a ser `estado × período`, medido sem erro.

⚠️ E A FASE 1 ACHOU O QUE PODE DERRUBAR A ROTA
-----------------------------------------------

O SINDAG conta **293 aeronaves agrícolas no Nordeste em SEIS estados** — BA 173,
MA 63, PI 41, AL 14, PE 5, SE 1. Os três **sem frota** são **Ceará, Rio Grande
do Norte e Paraíba**.

Se o RN não tinha pulverização aérea, a comparação deixa de ser entre *iguais
sob regimes diferentes* e vira *quem perdeu* contra *quem nunca teve* — e o
`d = 0` que a rota prometia eliminar reaparece do outro lado da fronteira, com
outro nome.

**Mas o número do SINDAG não decide**, por três razões: é de 2025 e não do
pré-ban; registra por **base do operador**, não por onde a aeronave voa; e conta
empresas do sindicato, não cadastro regulatório. Este script roda a verificação
que decide — a mesma tabela que já respondeu a pergunta para o Ceará.

AS TRÊS PERGUNTAS DO GATE
-------------------------

**G1 — o vizinho tinha aeronave no pré-ban?**
Censo Agropecuário, tabela SIDRA 1008 (equipamento de aplicação, categoria
"Por aeronave"), agora para a UF vizinha. O Ceará devolveu 36 estabelecimentos
em 7 municípios. Se o vizinho devolver ~0, a Rota 1 na forma proposta cai.

**G2 — o suporte de melão fecha em CE+vizinho?**
O Gate 1 encerrou o melão como âncora por ter só **10** municípios com área
positiva — **no Ceará**. Esse encerramento é condicional à amostra: o cinturão
do melão está do lado potiguar. Este gate recontará o suporte no painel
ampliado. ⚠️ Isso **não troca a âncora**; devolve a decisão ao dado.

**G3 — o registro é comparável?**
Se o SINASC do vizinho tem cobertura ou preenchimento de peso diferentes, um DiD
sobre peso ao nascer compara **prática de registro**, não saúde. Mede-se
cobertura, `%` de peso ausente, peso médio e massa por célula.

⚠️ O QUE ESTE SCRIPT NÃO FAZ
-----------------------------

- **Não decide a rota.** Emite veredito por pergunta e um veredito agregado; a
  escolha entre as três saídas da Fase 1 é do pesquisador.
- **Não troca a âncora nem a estratégia de identificação.** Ambas exigem
  conversa com o orientador (CLAUDE.md, "Perguntar antes de").
- **Não trata ausência como reprovação.** Sem dado, o veredito é `ausente`, que
  é diferente de `✘`. "Não verificado" e "verificado e falhou" pedem ações
  opostas, e confundi-los foi erro real na linhagem deste repositório.

Uso:
    python scripts/data_prep/14_gate_fronteira.py --vizinho 24     # CE x RN
    python scripts/data_prep/14_gate_fronteira.py --vizinho 22     # CE x PI
    python scripts/data_prep/14_gate_fronteira.py --pular-censo    # só G2 e G3

Saída: `data/processed/gate_fronteira__uf23-<vizinho>.csv` (gitignored).
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from datetime import date
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
OUT_DIR = RAIZ / "data" / "processed"

UF_CEARA = "23"
# Ceará, Censo Agropecuário 2006 (script 13, rodado em 2026-09-22): 36
# estabelecimentos com aeronave em 7 municípios. É a régua de G1 — o vizinho é
# comparável se estiver na mesma ordem de grandeza, não se for idêntico.
AERONAVES_CE_2006 = 36
MUNICIPIOS_COM_AERONAVE_CE_2006 = 7
# Suporte mínimo para a curva não-paramétrica (sieve CCK). Abaixo disto o
# próprio CGS manda descer o degrau da escada — ver `recomenda_especificacao`
# no script 01, que é quem manda; este número está aqui só para o relatório.
SUPORTE_MINIMO_CURVA = 30


def _carrega_script(nome: str, sub: str = "data_prep"):
    """Scripts numerados não são importáveis por `import` — carrega por caminho."""
    caminho = RAIZ / "scripts" / sub / nome
    spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


# --------------------------------------------------------------------------
# G1 — o vizinho tinha aeronave?
# --------------------------------------------------------------------------

def gate_aeronave(vizinho: str, chunk: int = 25) -> dict:
    """Censo Agro 1008 para a UF vizinha. Devolve veredito + contagens.

    ⚠️ `ausente` quando a rede não responde. Sem isto, bloqueio de rede viraria
    "o vizinho não tinha aeronave", que é exatamente a conclusão errada — e é a
    classe de erro que este repositório já cometeu (a truncagem do bucket GAEZ).
    """
    censo = _carrega_script("13_censo_agro_equipamento.py")
    try:
        ids = censo.municipios_da_uf(vizinho)
        tabela = censo.baixa(ids, chunk=chunk)
    except Exception as erro:  # noqa: BLE001
        return {
            "gate": "G1_aeronave", "veredito": "ausente",
            "detalhe": f"{type(erro).__name__}: {erro}",
        }
    if tabela.empty:
        return {"gate": "G1_aeronave", "veredito": "ausente",
                "detalhe": "SIDRA respondeu vazio"}

    aeronaves = float(tabela["aeronave"].sum())
    com_aeronave = int((tabela["aeronave"] > 0).sum())
    # ✔ = o vizinho tinha pulverização aérea em ordem de grandeza comparável à
    # do Ceará, logo há o que comparar. ✘ = não tinha, e a Rota 1 na forma
    # proposta não se sustenta (as saídas B e C da Fase 1 continuam abertas).
    veredito = "✔" if aeronaves >= 0.25 * AERONAVES_CE_2006 else "✘"
    return {
        "gate": "G1_aeronave", "veredito": veredito,
        "aeronaves_vizinho": aeronaves,
        "municipios_com_aeronave_vizinho": com_aeronave,
        "aeronaves_ce": float(AERONAVES_CE_2006),
        "municipios_com_aeronave_ce": float(MUNICIPIOS_COM_AERONAVE_CE_2006),
        "detalhe": (f"{aeronaves:.0f} estabelecimentos com aeronave em "
                    f"{com_aeronave} municípios (Censo 2006), contra "
                    f"{AERONAVES_CE_2006} em {MUNICIPIOS_COM_AERONAVE_CE_2006} no CE"),
    }


# --------------------------------------------------------------------------
# G2 — o suporte de melão fecha no painel ampliado?
# --------------------------------------------------------------------------

# O parquet agregado do script 01 chama a coluna `area_ha_media` — a média da
# janela pré-ban. Só o formato longo, ano a ano, tem `area_ha`. Aceitar os dois
# evita depender de qual dos dois arquivos chega pelo `--pam`; o que não pode
# é falhar com KeyError cru, que foi exatamente o que escondeu esta divergência
# (os testes usavam `area_ha`, o script 01 grava `area_ha_media`).
COLUNAS_DE_AREA = ("area_ha_media", "area_ha")


def coluna_de_area(df: pd.DataFrame) -> str:
    for col in COLUNAS_DE_AREA:
        if col in df.columns:
            return col
    raise KeyError(
        f"PAM sem coluna de área: esperava uma de {COLUNAS_DE_AREA}, "
        f"veio {list(df.columns)}"
    )


def suporte_por_cultura(medias: pd.DataFrame, ufs) -> pd.DataFrame:
    """Municípios com área > 0 por cultura, dentro e fora do Ceará."""
    df = medias.copy()
    df["cod_ibge"] = df["cod_ibge"].astype(str)
    df = df[df["cod_ibge"].str.startswith(tuple(ufs))]
    df = df[df[coluna_de_area(df)] > 0]
    df["uf"] = df["cod_ibge"].str[:2]
    tabela = (df.groupby(["cultura", "uf"])["cod_ibge"].nunique()
                .unstack(fill_value=0))
    tabela["total"] = tabela.sum(axis=1)
    return tabela.sort_values("total", ascending=False)


def gate_melao(medias: pd.DataFrame | None, vizinho: str) -> dict:
    """Recontagem do suporte do melão em CE+vizinho.

    ⚠️ Isto NÃO troca a cultura-âncora. A banana está ratificada na
    pré-especificação §3, e trocá-la depois de ver resultado é exatamente o que
    aquele documento existe para impedir. O que o gate faz é registrar se o
    encerramento empírico do melão — 10 municípios, *no Ceará* — sobrevive à
    ampliação da amostra. Se não sobreviver, vira pergunta para o ciclo
    seguinte, pré-especificada antes do dado.
    """
    if medias is None or medias.empty:
        return {"gate": "G2_melao", "veredito": "ausente",
                "detalhe": "PAM indisponível"}
    tabela = suporte_por_cultura(medias, (UF_CEARA, vizinho))
    linha = tabela[tabela.index.str.contains("melão", case=False, na=False)]
    if linha.empty:
        return {"gate": "G2_melao", "veredito": "ausente",
                "detalhe": "melão não apareceu nos rótulos do PAM"}
    so_ce = float(linha.get(UF_CEARA, pd.Series([0])).iloc[0])
    total = float(linha["total"].iloc[0])
    veredito = "✔" if total >= SUPORTE_MINIMO_CURVA else "✘"
    return {
        "gate": "G2_melao", "veredito": veredito,
        "municipios_melao_ce": so_ce,
        "municipios_melao_total": total,
        "detalhe": (f"melão: {so_ce:.0f} municípios no CE, {total:.0f} em "
                    f"CE+{vizinho} (mínimo para a curva: {SUPORTE_MINIMO_CURVA})"),
    }


# --------------------------------------------------------------------------
# G3 — o registro é comparável?
# --------------------------------------------------------------------------

def comparabilidade_registro(painel: pd.DataFrame, ufs) -> pd.DataFrame:
    """Descritivas de registro por UF, sobre o painel município × ano-mês."""
    df = painel.copy()
    coluna = "cod_ibge6" if "cod_ibge6" in df.columns else "cod_ibge"
    df[coluna] = df[coluna].astype(str)
    df = df[df[coluna].str.startswith(tuple(ufs))]
    df["uf"] = df[coluna].str[:2]
    agg = {"n_nascimentos": "sum"}
    for candidata in ("peso_medio", "baixo_peso", "prematuridade"):
        if candidata in df.columns:
            agg[candidata] = "mean"
    fora = df.groupby("uf").agg(agg)
    fora["municipios"] = df.groupby("uf")[coluna].nunique()
    fora["celulas"] = df.groupby("uf").size()
    if "celula_pequena" in df.columns:
        fora["frac_celula_pequena"] = df.groupby("uf")["celula_pequena"].mean()
    return fora


def gate_registro(painel: pd.DataFrame | None, vizinho: str,
                  tolerancia_g: float = 50.0) -> dict:
    """Compara peso médio entre as UFs.

    A régua é deliberadamente frouxa: o gate pergunta se as duas UFs são
    *comparáveis*, não se são iguais. ⚠️ Uma diferença de nível **não** invalida
    o DiD — o que invalidaria é diferença de *tendência*, que este gate não
    mede. Ele é triagem, não teste de identificação, e dizer isso aqui impede
    que um ✔ vire licença.
    """
    if painel is None or painel.empty:
        return {"gate": "G3_registro", "veredito": "ausente",
                "detalhe": "painel de nascimentos indisponível"}
    fora = comparabilidade_registro(painel, (UF_CEARA, vizinho))
    if UF_CEARA not in fora.index or vizinho not in fora.index:
        return {"gate": "G3_registro", "veredito": "ausente",
                "detalhe": f"painel não tem as duas UFs (tem: {list(fora.index)})"}
    if "peso_medio" not in fora.columns:
        return {"gate": "G3_registro", "veredito": "ausente",
                "detalhe": "painel sem coluna peso_medio"}
    delta = float(fora.loc[UF_CEARA, "peso_medio"] - fora.loc[vizinho, "peso_medio"])
    veredito = "✔" if abs(delta) <= tolerancia_g else "✘"
    return {
        "gate": "G3_registro", "veredito": veredito,
        "peso_medio_ce": float(fora.loc[UF_CEARA, "peso_medio"]),
        "peso_medio_vizinho": float(fora.loc[vizinho, "peso_medio"]),
        "delta_peso_g": delta,
        "municipios_vizinho": float(fora.loc[vizinho, "municipios"]),
        "detalhe": (f"peso médio CE {fora.loc[UF_CEARA, 'peso_medio']:.0f} g vs "
                    f"UF {vizinho} {fora.loc[vizinho, 'peso_medio']:.0f} g "
                    f"(Δ {delta:+.0f} g; tolerância ±{tolerancia_g:.0f} g)"),
    }


# --------------------------------------------------------------------------
# Veredito agregado
# --------------------------------------------------------------------------

def veredito_agregado(resultados: list[dict]) -> str:
    """`ausente` domina: sem G1 não há veredito, porque é ele que decide a rota.

    ⚠️ A ordem importa e não é estética. G1 é a pergunta que a Fase 1 abriu; G2 e
    G3 são condições de qualidade. Um ✔ em G2 e G3 com G1 ausente NÃO é
    aprovação — é ignorância sobre a única coisa que estava em dúvida.
    """
    por_gate = {r["gate"]: r["veredito"] for r in resultados}
    if por_gate.get("G1_aeronave") == "ausente":
        return "ausente"
    if por_gate.get("G1_aeronave") == "✘":
        return "✘ rota 1 na forma proposta"
    if any(v == "✘" for v in por_gate.values()):
        return "⚠ com ressalva"
    if any(v == "ausente" for v in por_gate.values()):
        return "⚠ parcial"
    return "✔"


def imprime(resultados: list[dict], vizinho: str, agregado: str) -> None:
    barra = "=" * 84
    print(barra)
    print(f"GATE DA ROTA 1 — desenho de fronteira CE (23) × UF {vizinho}")
    print(barra)
    for r in resultados:
        print(f"  [{r['veredito']:>7}] {r['gate']:<14} {r.get('detalhe', '')}")
    print(barra)
    print(f"  VEREDITO AGREGADO: {agregado}")
    if agregado == "ausente":
        print("  ⚠️ 'ausente' NÃO é reprovação. O G1 não rodou — tipicamente rede")
        print("     bloqueada. Rodar de novo com acesso ao servicodados.ibge.gov.br.")
    elif agregado.startswith("✘"):
        print("  ⚠️ O vizinho não tinha pulverização aérea em escala comparável.")
        print("     A Rota 1 como proposta (comparação entre iguais) não se sustenta.")
        print("     As saídas B (ITT de fronteira) e C (trocar o vizinho) seguem abertas —")
        print("     ver docs/ars/11-rota1-fase1-escopo.md §6.")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--vizinho", default="24", metavar="COD",
                   help="Código IBGE da UF de comparação (24=RN, 22=PI, 26=PE).")
    p.add_argument("--painel", type=Path, default=None,
                   help="Painel de nascimentos multi-UF (parquet). Omitir pula o G3.")
    p.add_argument("--pam", type=Path, default=None,
                   help="PAM município×cultura multi-UF (parquet). Omitir pula o G2.")
    p.add_argument("--pular-censo", action="store_true",
                   help="Pula o G1 (que é o que exige rede).")
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    p.add_argument("--chunk", type=int, default=25)
    args = p.parse_args(argv)

    if args.vizinho == UF_CEARA:
        print("[erro] --vizinho não pode ser 23: o Ceará é o grupo tratado.")
        return 1

    resultados = []
    if args.pular_censo:
        resultados.append({"gate": "G1_aeronave", "veredito": "ausente",
                           "detalhe": "pulado por --pular-censo"})
    else:
        resultados.append(gate_aeronave(args.vizinho, chunk=args.chunk))

    def _le(caminho):
        if caminho is None or not caminho.exists():
            return None
        try:
            return pd.read_parquet(caminho)
        except Exception as erro:  # noqa: BLE001
            print(f"[aviso] não li {caminho}: {type(erro).__name__}: {erro}")
            return None

    resultados.append(gate_melao(_le(args.pam), args.vizinho))
    resultados.append(gate_registro(_le(args.painel), args.vizinho))

    agregado = veredito_agregado(resultados)
    imprime(resultados, args.vizinho, agregado)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    destino = args.out_dir / f"gate_fronteira__uf{UF_CEARA}-{args.vizinho}.csv"
    saida = pd.DataFrame(resultados)
    # Proveniência viaja DENTRO do arquivo, não só no nome — um CSV desgarrado
    # do nome já foi lido como se fosse real uma vez neste projeto.
    saida["vizinho"] = args.vizinho
    saida["veredito_agregado"] = agregado
    saida["extraido_em"] = date.today().isoformat()
    saida.to_csv(destino, index=False, encoding="utf-8")
    print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
