"""E15 — A dose classifica bem? Sensibilidade, especificidade, VPP e o limite.

POR QUE ESTE SCRIPT EXISTE
--------------------------

A flag 7 do `CLAUDE.md` diz que a dose por área plantada atribui tratamento alto
a municípios sem pulverização aérea, e que isso atenua o ATT por construção. Até
aqui isso era **afirmação qualitativa** com duas ilustrações (15 dos 17 tratados
sem aplicação por aeronave; 27 dos 36 estabelecimentos no decil).

Este script transforma a afirmação em **três métricas padrão**, em **um limite
reportável** e numa **calibração de poder**. Nenhum deles exige dado novo: saem
do confronto entre a dose (PAM) e a medida direta (Censo Agro 2006, script 13).

⚠️ O QUE O CENSO MEDE — USO, NÃO POSSE
--------------------------------------

A tabela 1008 do SIDRA conta estabelecimentos por **"tipo de equipamento
utilizado na aplicação"**. É o estabelecimento que *recebeu* aplicação por
aeronave, no município onde ele está — contratada ou própria. A ressalva antiga
("prestador sediado em Limoeiro pulveriza lavoura em Quixeré, então 'não ter
aeronave' não é 'não receber pulverização'") estava mal posta: a lavoura de
Quixeré atendida por avião de fora entra **em Quixeré**. Ficam as ressalvas que
valem: o dado é de 2006, e é declaração do informante.

O QUE A LITERATURA DIZ SOBRE ESTA CONFIGURAÇÃO
----------------------------------------------

> Rull, R. P. & Ritz, B. (2003). *Historical pesticide exposure in California
> using pesticide use reports and land-use surveys: an assessment of
> misclassification error and bias.* **Environmental Health Perspectives**
> 111(13): 1582–1589. PMID 14527836.

Eles simulam exatamente a troca que este projeto faz — usar **proximidade a
cultura** no lugar de **registro de aplicação** — e o achado é:

> *se a misclassificação é não-diferencial e a **prevalência de exposição é
> baixa**, **pequenas reduções de especificidade** produzem **reduções
> substanciais** na estimativa de risco.*

⚠️ **As duas condições valem aqui, e com folga.** A prevalência do tratamento
verdadeiro é ~3,8% dos municípios (7 de 184 com aplicação por aeronave em 2006).
O número que decide é o **VPP**: a fração do grupo "tratado" que estava de fato
tratada. Com prevalência baixa, especificidade de 90% ainda produz VPP perto de
10%.

O RESULTADO QUE SE APLICA: COROLÁRIO 1, NÃO O 5
------------------------------------------------

Denteh & Kédagni (arXiv:2207.11890, v3), **Corolário 1**: sob a Hipótese 1 —
tendências paralelas no tratamento **observado** D, que é a hipótese que os
estimadores binários do paper já mantêm — e **sem falso negativo**,
`P(D*=1, ε=1) = 0`:

    θ_DID = P(ε=0 | D=1) · ATT          (atenuação pura)

e isso vale para misclassificação **arbitrária**, inclusive diferencial. O sinal
não inverte. A inversão da Proposição 1 vem inteira do termo de falso negativo,
`−ATT_{ε=1} · P(ε=1 | D=0)`, e aqui ele é zero: o grupo de comparação dos
scripts 07 e 08 é de dose ZERO, e nenhum município de dose zero tinha aplicação
por aeronave (flag 5).

Logo `ATT = θ / VPP`, e com `VPP ∈ [vpp_min, 1]`:

    min{θ, θ/vpp_min} ≤ ATT ≤ max{θ, θ/vpp_min}

É numericamente o Corolário 5 com `λ = 1 − vpp_min`. A diferença está nas
hipóteses: o Corolário 5 exige erro **não-diferencial** e monotonicidade; o 1
não. A ressalva "sob erro diferencial o sinal pode inverter", que este script
imprimia até 2026-09-22, **não se aplica a este desenho**.

⚠️ Corrigido em 2026-09-22 — o λ antigo somava os falsos negativos de TODOS os
167 municípios fora do decil (5/167). Mas os de dose intermediária não entram
no DiD binário; no grupo de comparação o falso negativo é zero, e `λ = 1 − VPP`.
A versão populacional continua na saída, rotulada, para a diferença ficar
visível.

⚠️ E NEGI & NEGI NÃO SE APLICAM
--------------------------------

Negi & Negi (2025, *JAE* 40(4):411–423) tratam o erro unilateral **oposto**:
`D = D*·S`, falso negativo permitido e falso positivo **excluído por
construção**. O erro daqui é só falso positivo. O estimador deles não resolve
este caso como formulado, e a busca por uma restrição de exclusão para ele
perde o objeto. Ver `docs/ars/16-diluicao-corolario1-limoeiro-calibracao.md` §3.

A CALIBRAÇÃO — QUANTO SINAL O DESENHO PODERIA VER
-------------------------------------------------

Pelo Corolário 1, `θ = VPP · ATT*`, e o ATT municipal de um município
genuinamente tratado não passa de `f · δ`: a fração dos nascimentos com
exposição alta vezes o efeito individual sob exposição alta. O análogo mais
próximo — fumigação aérea de fungicida em bananal, peso ao nascer — dá
`δ = 80–150 g` (Calzada, Gisbert & Moscoso 2023, pelo resumo). Com o VPP do
Censo, `θ` esperado fica abaixo de 9 g mesmo com `f = 0,5` e `δ = 150`, e o
poder contra o MDE de 33,4 g não passa de ~11%. Não é estimação: é aritmética
de insumos declarados, para dizer o que o desenho podia e não podia ver.

TRÊS RESSALVAS, E SÃO SÉRIAS
-----------------------------

1. São **limites de estimativa pontual**, não intervalos de confiança.
   Inferência sobre eles exige *intersection bounds* (Chernozhukov, Lee & Rosen).
2. O VPP vem de **2006**, treze anos antes do ban. Fora das serras, a aviação
   agrícola pode ter crescido até 2018; por isso a calibração tem um cenário de
   teto geográfico, não só o do Censo.
3. O Corolário 1 exige tendências paralelas no D **observado**. Se elas valem
   só no D* latente (a hipótese de Negi & Negi), falsos positivos com tendência
   própria enviesam θ em qualquer direção — mas isso é violação da hipótese que
   o desenho já mantém, e o pré-período a testa.

Uso:
    python scripts/estimate/12_erro_de_classificacao.py                # números da §5.4
    python scripts/estimate/12_erro_de_classificacao.py --theta -21.85
    python scripts/estimate/12_erro_de_classificacao.py \
        --censo data/processed/censo_agro_equipamento_ce.csv \
        --dose  data/processed/pam_ce_muni_cultura_media__sidra.parquet

Saídas (gitignored): `data/processed/erro_classificacao_dose.csv` e
`data/processed/calibracao_sinal_esperado.csv`.
"""

from __future__ import annotations

import argparse
import math
from datetime import date
from pathlib import Path
from statistics import NormalDist

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
OUT_DIR = RAIZ / "data" / "processed"

# MDE do desenho (§6 do paper): 80% de poder, teste bilateral a 5%.
MDE_G = 33.4
ALFA = 0.05
PODER_NO_MDE = 0.80

# Números da §5.4 do paper, usados quando não há artefatos. ⚠️ Fonte: Censo
# Agropecuário 2006, tabela SIDRA 1008, rodado pelo script 13 em 2026-09-22.
PUBLICADOS = {
    "n_municipios": 184,
    "municipios_com_aeronave": 7,
    # Limoeiro do Norte (18 estab.) e Quixeré (9): ranks 6 e 13 de 169 na
    # banana, logo DENTRO dos 17 e dos 19.
    "municipios_decil_com_aeronave": 2,
    # Nenhum dos 7 tem dose zero (flag 5): o grupo de comparação não tem
    # falso negativo.
    "falso_negativo_no_controle": 0,
}
# ✅ Divergência 17 × 19 RESOLVIDA em 2026-09-22, contra os artefatos: a banana
# tem 169 municípios com área positiva, e o decil da convenção do Gate 1 é
# sobre os positivos — 169/10 ≈ 17. O 19 vinha do denominador errado (184
# municípios do CE, ceil = 19), que não é o corte que a pré-especificação usa.
# Com 17: 2 com aeronave (Limoeiro 18, Quixeré 9), 15 sem, VPP 11,8%.
# O 19 é a conta do script 13 (`confronta`: quantil 0,9 sobre os 184,
# zeros incluídos) — os mesmos 17 mais o 18º e o 19º. Não entra mais aqui.
FRACAO_DECIL = 0.10
TAMANHO_DECIL_CANONICO = 17
TAMANHOS_DECIL = (17,)

# Coeficientes já reportados na §6 do paper, em gramas.
COEFICIENTES_PAPER = {
    "synthdid": -20.16,
    "controle_sintetico": -34.64,
    "did_simples": -21.85,
}

# --- Calibração --------------------------------------------------------------
# δ — efeito individual sob exposição ALTA no análogo mais próximo (bananal,
#     fumigação aérea de fungicida, peso ao nascer): Calzada, Gisbert &
#     Moscoso (2023), JAERE 10(6):1623–1663, doi 10.1086/725349.
#     ⚠️ 80–150 g pelo RESUMO; o texto completo não foi lido.
EFEITOS_INDIVIDUAIS_G = (80.0, 150.0)
# f — fração dos nascimentos de um município genuinamente tratado com exposição
#     comparável à "alta" de Calzada. ⚠️ DESCONHECIDA: é grade, não estimativa.
#     0,5 já é generoso para municípios de 15 a 70 mil habitantes.
FRACOES_EXPOSTAS = (0.10, 0.25, 0.50)
# VPP — fração dos 17 tratados genuinamente tratada em 2019.
CENARIOS_VPP = {
    # Censo 2006: Limoeiro + Quixeré. A lei de Limoeiro (2009) foi revogada
    # em 20/05/2010 (fontes secundárias) — os dois contam.
    "censo2006": 2 / 17,
    # Se a revogação de 2010 NÃO se confirmar na fonte primária: só Quixeré.
    "censo2006_sem_limoeiro": 1 / 17,
    # Tudo o que não é serra: Limoeiro, Quixeré, Russas, Varjota, Itapipoca
    # (misto) e Missão Velha (vale do Cariri). Teto generoso — doc 16 §6.
    "teto_geografico": 6 / 17,
    # A leitura de "falta de poder": dose é tratamento.
    "dose_e_tratamento": 1.0,
}


def metricas_classificacao(n_municipios: int, com_aeronave: int,
                           tamanho_decil: int, decil_com_aeronave: int,
                           fn_controle: int = 0,
                           n_controle: int | None = None) -> dict:
    """Matriz de confusão da dose contra a medida direta de método.

    `D = 1` é "está no decil superior da dose"; `D* = 1` é "algum
    estabelecimento aplicou por aeronave".

    Dois λ, e só um serve:
      - `lambda_amostra` — o do DiD binário: falsos positivos no decil mais
        falsos negativos no GRUPO DE COMPARAÇÃO (`fn_controle / n_controle`).
        É o λ da Hipótese 6 de Denteh & Kédagni para a amostra que se estima.
      - `lambda_populacao` — a versão antiga, que contava como falso negativo
        todo município com aeronave fora do decil, inclusive os de dose
        intermediária, que não entram no DiD binário. Fica na saída, rotulada.
    """
    if decil_com_aeronave > min(com_aeronave, tamanho_decil):
        raise ValueError("decil_com_aeronave não pode exceder com_aeronave nem o decil")
    if tamanho_decil >= n_municipios or com_aeronave >= n_municipios:
        raise ValueError("decil e com_aeronave têm de ser menores que n_municipios")

    vp = decil_com_aeronave
    fp = tamanho_decil - vp
    fn = com_aeronave - vp
    vn = n_municipios - tamanho_decil - fn
    if not 0 <= fn_controle <= fn:
        raise ValueError("fn_controle tem de estar entre 0 e os falsos negativos totais")
    if fn_controle and not n_controle:
        raise ValueError("com falso negativo no controle, n_controle é obrigatório")

    vpp = vp / tamanho_decil
    taxa_fn_controle = fn_controle / n_controle if fn_controle else 0.0
    return {
        "tamanho_decil": tamanho_decil,
        "vp": vp, "fp": fp, "fn": fn, "vn": vn,
        "prevalencia": com_aeronave / n_municipios,
        "sensibilidade": vp / com_aeronave,
        "especificidade": vn / (n_municipios - com_aeronave),
        "vpp": vpp,
        "fn_controle": fn_controle,
        "lambda_amostra": (1 - vpp) + taxa_fn_controle,
        "lambda_populacao": (1 - vpp) + fn / (n_municipios - tamanho_decil),
        # Sem falso negativo no controle vale o Corolário 1 (erro arbitrário);
        # com ele, só o 5 (exige erro não-diferencial).
        "corolario": 1 if fn_controle == 0 else 5,
    }


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


def tamanho_do_decil(n_positivos: int, fracao: float = FRACAO_DECIL) -> int:
    """A mesma conta dos scripts 07 e 08: `ceil`, não `round`.

    ⚠️ Corrigido em 2026-09-22: este script usava `round(n/10)`, que diverge do
    `ceil` dos estimadores sempre que a parte fracionária é < 0,5 (163
    produtores: 16 aqui, 17 lá). O decil daqui tem de ser o grupo que se estima.
    """
    return max(1, math.ceil(n_positivos * fracao))


def metricas_de_artefatos(censo_csv: Path, dose_parquet: Path, cultura: str,
                         tamanho_decil: int | None = None) -> dict:
    """Recalcula as métricas a partir dos artefatos, em vez dos números da §5.4.

    `censo_csv` sai do script 13 (`censo_agro_equipamento_ce.csv`) e traz
    `cod_ibge6` e `aeronave`; `dose_parquet` sai do script 01
    (`pam_ce_muni_cultura_media__*.parquet`) e traz `cod_ibge`, `cultura`,
    `area_ha_media`.

    ⚠️ O decil é calculado sobre os municípios com área POSITIVA da cultura —
    a convenção dos estimadores e do Gate 1 (169 para a banana), não sobre os
    184. O grupo de comparação é o de área zero, e é nele que o falso negativo
    é contado.
    """
    censo = pd.read_csv(censo_csv, dtype={"cod_ibge6": str})
    dose = pd.read_parquet(dose_parquet)
    dose["cod_ibge"] = dose["cod_ibge"].astype(str).str[:6]
    dose = dose[dose["cultura"].str.contains(cultura, case=False, na=False)]
    col_area = coluna_de_area(dose)
    dose = dose[dose[col_area] > 0]
    if dose.empty:
        raise ValueError(f"nenhum município com área positiva de {cultura!r}")

    positivos = set(dose["cod_ibge"])
    k = tamanho_decil or tamanho_do_decil(len(positivos))
    decil = set(dose.nlargest(k, col_area)["cod_ibge"])

    universo = set(censo["cod_ibge6"])
    com_aeronave = set(censo.loc[censo["aeronave"] > 0, "cod_ibge6"])
    controles = universo - positivos
    return metricas_classificacao(
        n_municipios=len(universo),
        com_aeronave=len(com_aeronave),
        tamanho_decil=len(decil),
        decil_com_aeronave=len(decil & com_aeronave),
        fn_controle=len(controles & com_aeronave),
        n_controle=len(controles),
    )


def limite_corolario1(theta: float, vpp_min: float) -> tuple[float, float]:
    """Limites do ATT sem falso negativo (Corolário 1 de Denteh & Kédagni).

    `θ = VPP · ATT` sob tendências paralelas no D observado, para erro
    arbitrário. Com `VPP ∈ [vpp_min, 1]`, o ATT fica entre θ e θ/vpp_min — e
    com o MESMO sinal de θ, que é o que o Corolário 5 não garante.
    """
    if not 0 < vpp_min <= 1:
        raise ValueError(f"vpp_min tem de estar em (0, 1]; recebido {vpp_min:.3f}")
    escalado = theta / vpp_min
    return (min(escalado, theta), max(escalado, theta))


def limite_corolario5(theta: float, lambda_: float) -> tuple[float, float]:
    """Limites do ATT sob misclassificação não-diferencial (Corolário 5).

    Só é o resultado certo quando HÁ falso negativo no grupo de comparação.
    Sem ele, use `limite_corolario1`, que dá o mesmo número sob hipóteses
    mais fracas.

    ⚠️ `lambda_ >= 1` não tem limite: o corolário exige λ < 1, e λ = 1 significa
    que a classificação não carrega informação alguma. Levanta em vez de
    devolver infinito, porque um infinito silencioso viraria número em tabela.
    """
    if not 0 <= lambda_ < 1:
        raise ValueError(f"λ tem de estar em [0, 1); recebido {lambda_:.3f}")
    escalado = theta / (1 - lambda_)
    return (min(escalado, theta), max(escalado, theta))


def tabela_limites(theta: float, lambdas, rotulo: str) -> pd.DataFrame:
    """Limites do ATT para uma faixa de λ (sem falso negativo, `VPP = 1 − λ`).

    ⚠️ Não compara o limite com o MDE. Até 2026-09-22 comparava, e lia "passou
    do MDE" como "o desenho teria tido poder" — mas o MDE é do estimando θ
    deste desenho, com 17 tratados, e θ é o mesmo nas duas leituras. Quem diz
    o que o desenho podia ver é `tabela_calibracao`.
    """
    linhas = []
    for lam in lambdas:
        inf, sup = limite_corolario1(theta, 1 - lam)
        linhas.append({
            "estimador": rotulo, "theta_g": theta, "lambda": lam,
            "vpp": 1 - lam,
            "limite_inferior_g": inf, "limite_superior_g": sup,
        })
    return pd.DataFrame(linhas)


# --- Calibração --------------------------------------------------------------

def _z(p: float) -> float:
    return NormalDist().inv_cdf(p)


def erro_padrao_do_mde(mde: float = MDE_G, alfa: float = ALFA,
                       poder: float = PODER_NO_MDE) -> float:
    """O erro-padrão que o MDE implica: `MDE = (z_{1−α/2} + z_{poder}) · ep`."""
    return mde / (_z(1 - alfa / 2) + _z(poder))


def poder_aproximado(theta: float, mde: float = MDE_G, alfa: float = ALFA,
                     poder_no_mde: float = PODER_NO_MDE) -> float:
    """Poder bilateral de um teste z contra um efeito verdadeiro `theta`.

    Usa o erro-padrão implícito no MDE, então `poder_aproximado(MDE) = 0,80`
    e `poder_aproximado(0) = α` por construção. É aproximação de ordem de
    grandeza — a inferência do paper é por Conley–Taber / bootstrap.
    """
    ep = erro_padrao_do_mde(mde, alfa, poder_no_mde)
    z = _z(1 - alfa / 2)
    t = abs(theta) / ep
    return NormalDist().cdf(t - z) + NormalDist().cdf(-t - z)


def sinal_esperado(vpp: float, fracao_exposta: float,
                   efeito_individual_g: float) -> float:
    """`θ = VPP · f · δ`, em gramas de déficit (magnitude).

    Supõe efeito zero fora da exposição alta — o que puxa θ para baixo; se a
    exposição moderada também pesa, θ sobe. É o insumo, não a conclusão.
    """
    for nome, v in (("vpp", vpp), ("fracao_exposta", fracao_exposta)):
        if not 0 <= v <= 1:
            raise ValueError(f"{nome} tem de estar em [0, 1]; recebido {v}")
    if efeito_individual_g < 0:
        raise ValueError("efeito_individual_g é magnitude (≥ 0)")
    return vpp * fracao_exposta * efeito_individual_g


def vpp_de_equilibrio(theta_obs: float, fracao_exposta: float,
                      efeito_individual_g: float) -> float:
    """O VPP que faria `theta_obs` ser sinal diluído puro: |θ| / (f · δ).

    Acima de 1 é impossível: nem com o grupo inteiro tratado o insumo gera θ.
    """
    if fracao_exposta <= 0 or efeito_individual_g <= 0:
        raise ValueError("fracao_exposta e efeito_individual_g têm de ser > 0")
    return abs(theta_obs) / (fracao_exposta * efeito_individual_g)


def tabela_calibracao(cenarios: dict[str, float] = CENARIOS_VPP,
                      fracoes=FRACOES_EXPOSTAS,
                      efeitos=EFEITOS_INDIVIDUAIS_G,
                      mde: float = MDE_G) -> pd.DataFrame:
    linhas = []
    for nome, vpp in cenarios.items():
        for f in fracoes:
            for d in efeitos:
                theta = sinal_esperado(vpp, f, d)
                linhas.append({
                    "cenario_vpp": nome, "vpp": vpp, "fracao_exposta": f,
                    "efeito_individual_g": d, "theta_esperado_g": theta,
                    "poder_aproximado": poder_aproximado(theta, mde),
                })
    return pd.DataFrame(linhas)


def imprime(metricas: list[dict], limites: pd.DataFrame,
            calibracao: pd.DataFrame, coeficientes: dict[str, float]) -> None:
    barra = "=" * 84
    print(barra)
    print("ERRO DE CLASSIFICAÇÃO DA DOSE — a flag 7, medida")
    print(barra)
    print("  A dose ('decil superior') contra a medida direta ('aplicou por aeronave'):")
    print()
    print(f"  {'decil':>6} {'sens.':>8} {'espec.':>8} {'VPP':>8} "
          f"{'λ amostra':>10} {'λ popul.':>9}")
    for m in metricas:
        canon = " ← canônico" if m["tamanho_decil"] == TAMANHO_DECIL_CANONICO else ""
        print(f"  {m['tamanho_decil']:>6} {m['sensibilidade']:>7.1%} "
              f"{m['especificidade']:>7.1%} {m['vpp']:>7.1%} "
              f"{m['lambda_amostra']:>10.3f} {m['lambda_populacao']:>9.3f}{canon}")
    print()
    print(f"  prevalência do tratamento verdadeiro: {metricas[0]['prevalencia']:.1%}")
    print(f"  falso negativo no grupo de comparação: {metricas[0]['fn_controle']}"
          f"  → vale o Corolário {metricas[0]['corolario']}")
    print("  ⚠️ O decil canônico é o dos estimadores (07/08): ceil(10% dos")
    print("     produtores). O 19 é o quantil 0,9 sobre os 184 (script 13).")
    print(barra)
    print("  LIMITES DO ATT (Corolário 1, Denteh & Kédagni) — pontuais, não IC:")
    print("  Sem falso negativo, θ = VPP·ATT para erro ARBITRÁRIO: o sinal não")
    print("  inverte, e o ATT fica entre θ e θ/VPP.")
    print()
    for est in limites["estimador"].unique():
        sub = limites[limites["estimador"] == est]
        print(f"  {est}:")
        for _, r in sub.iterrows():
            print(f"    VPP={r['vpp']:.2f} (λ={r['lambda']:.2f})  "
                  f"[{r['limite_inferior_g']:8.1f}; {r['limite_superior_g']:7.1f}] g")
    print(barra)
    print("  CALIBRAÇÃO — o sinal que o desenho poderia ver (θ = VPP · f · δ)")
    print("  δ = efeito individual sob exposição alta, Calzada et al. (2023, resumo);")
    print(f"  f = fração exposta (DESCONHECIDA, grade). MDE = {MDE_G} g, "
          f"ep implícito = {erro_padrao_do_mde():.1f} g.")
    print()
    print(f"  {'cenário':<24} {'VPP':>5} {'f':>5} "
          + "".join(f"{f'δ={d:.0f}':>9}{'poder':>7}" for d in EFEITOS_INDIVIDUAIS_G))
    for (nome, vpp, f), bloco in calibracao.groupby(
            ["cenario_vpp", "vpp", "fracao_exposta"], sort=False):
        celulas = "".join(f"{r['theta_esperado_g']:>9.1f}{r['poder_aproximado']:>7.0%}"
                          for _, r in bloco.iterrows())
        print(f"  {nome:<24} {vpp:>5.2f} {f:>5.2f} {celulas}")
    print()
    print("  VPP de equilíbrio — o que faria o θ observado ser sinal diluído puro:")
    for rotulo, theta in coeficientes.items():
        pares = ", ".join(
            f"f={f:.2f},δ={d:.0f}: {vpp_de_equilibrio(theta, f, d):.2f}"
            for f in FRACOES_EXPOSTAS[1:] for d in EFEITOS_INDIVIDUAIS_G)
        print(f"    {rotulo:<20} {pares}")
    print("  (acima de 1 = impossível; o Censo 2006 dá VPP = 0,12)")
    print(barra)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--theta", type=float, action="append", default=None,
                   help="Coeficiente em gramas. Repetível. Omitir usa os da §6.")
    p.add_argument("--lambdas", type=float, nargs="+",
                   default=[0.3, 0.5, 0.7],
                   help="Faixa de λ a reportar. O λ medido entra sempre.")
    p.add_argument("--censo", type=Path, default=None,
                   help="CSV do script 13. Com --dose, recalcula em vez de usar a §5.4.")
    p.add_argument("--dose", type=Path, default=None,
                   help="Parquet do script 01. Exige --censo.")
    p.add_argument("--cultura", default="banana",
                   help="Cultura-âncora para o decil (padrão: banana).")
    p.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = p.parse_args(argv)

    if (args.censo is None) != (args.dose is None):
        print("[erro] --censo e --dose andam juntos.")
        return 1
    if args.censo is not None:
        fonte = "artefatos"
        metricas = [metricas_de_artefatos(args.censo, args.dose, args.cultura)]
    else:
        # ⚠️ Sem artefatos, os números da §5.4, com o decil canônico (17).
        fonte = "publicados"
        metricas = [
            metricas_classificacao(
                PUBLICADOS["n_municipios"], PUBLICADOS["municipios_com_aeronave"],
                tamanho, PUBLICADOS["municipios_decil_com_aeronave"],
                fn_controle=PUBLICADOS["falso_negativo_no_controle"],
            )
            for tamanho in TAMANHOS_DECIL
        ]

    # O λ medido entra sempre: é ele que diz onde a faixa argumentada cai.
    lambdas = sorted(set(args.lambdas) | {round(m["lambda_amostra"], 3)
                                          for m in metricas})
    coeficientes = ({f"theta_{i}": t for i, t in enumerate(args.theta)}
                    if args.theta else COEFICIENTES_PAPER)
    limites = pd.concat(
        [tabela_limites(theta, lambdas, rotulo) for rotulo, theta in coeficientes.items()],
        ignore_index=True,
    )
    calibracao = tabela_calibracao()

    imprime(metricas, limites, calibracao, coeficientes)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    hoje = date.today().isoformat()
    destino = args.out_dir / "erro_classificacao_dose.csv"
    saida = limites.copy()
    for m in metricas:
        saida[f"lambda_amostra_decil{m['tamanho_decil']}"] = m["lambda_amostra"]
        saida[f"lambda_populacao_decil{m['tamanho_decil']}"] = m["lambda_populacao"]
        saida[f"vpp_decil{m['tamanho_decil']}"] = m["vpp"]
    saida["fonte"] = fonte
    saida["extraido_em"] = hoje
    saida.to_csv(destino, index=False, encoding="utf-8")
    destino_cal = args.out_dir / "calibracao_sinal_esperado.csv"
    calibracao.assign(extraido_em=hoje).to_csv(destino_cal, index=False,
                                               encoding="utf-8")
    print(f"gravado: {destino}")
    print(f"gravado: {destino_cal}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
