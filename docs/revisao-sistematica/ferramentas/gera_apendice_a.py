"""Gera o Apêndice A (estratégias de busca) a partir dos JSON de calibração.

Para cada bloco, usa `calibracao/<bloco>-final.json` (rodada de finalização) quando
existe; senão, cai para a `recommended_final_query` da PRESS. As strings são
copiadas dos JSON, sem redigitação. Rodar da pasta docs/revisao-sistematica:

    python3 ferramentas/gera_apendice_a.py
"""
import json
import os

BLOCOS = [
    ("sq1-internacional", "SQ1 — revisão sistemática principal, literatura internacional"),
    ("sq1-america-latina", "SQ1 — braço América Latina (PT/ES/EN)"),
    ("sq2-metodo", "SQ2 — revisão estruturada complementar: método"),
    ("sq3-instrumento", "SQ3 — revisão estruturada complementar: escolha de instrumento"),
]
C = "calibracao/"


def carrega(nome):
    p = C + nome + ".json"
    return json.load(open(p)) if os.path.exists(p) else None


def bloco_final(w, fin):
    w("**Fonte:** rodada de finalização (`-final.json`), que aplica a PRESS e congela as linhas.\n")
    w("| linha | base | contagem | descrição |")
    w("|---|---|---:|---|")
    for ln in fin["numbered_lines"]:
        cnt = ln.get("count")
        cnt = f"{cnt:,}".replace(",", ".") if isinstance(cnt, int) else "—"
        desc = ln["description"].replace("|", "/").replace("\n", " ")
        w(f"| {ln['line']} | {ln['database'][:40]} | {cnt} | {desc} |")
    w("\n**Strings exatas, prontas para rodar:**\n")
    for ln in fin["numbered_lines"]:
        w(f"`{ln['line']}` ({ln['database'][:40]}, {ln.get('run_date', '')}):")
        w("```text\n" + ln["query"].strip() + "\n```")
    w("\n**O que entra na triagem:**\n")
    for s in fin["final_lines_to_screen"]:
        w(f"- {s}")
    if fin.get("screening_priority_rule"):
        w(f"\n**Ordem de triagem:** {fin['screening_priority_rule']}\n")
    w("**Recall, desenvolvimento** (itens usados no ajuste; otimista por construção):\n")
    w("> " + fin["recall_tuning_set"].replace("\n", "\n> ") + "\n")
    w("**Recall, validação independente** (itens escolhidos antes do teste):\n")
    w("> " + fin["recall_independent_validation"].replace("\n", "\n> ") + "\n")
    w(f"**Volume:** {fin['estimated_unique_volume']}\n")
    if fin.get("changes_not_applied"):
        w("**Mudanças da PRESS não aplicadas, e por quê:**\n")
        for c in fin["changes_not_applied"]:
            w(f"- *{c['change']}* — {c['why']}")
    if fin.get("issues"):
        w("\n**Problemas e limites registrados:**\n")
        for i in fin["issues"]:
            w(f"- {i}")


def bloco_press(w, cal, pr):
    w("⚠️ **Fonte:** recomendação da PRESS (`-press.json`). A rodada de finalização "
      "deste bloco ainda não terminou; ao terminar, rodar este script de novo.\n")
    w(f"**Veredito PRESS:** {pr['verdict']}.\n")
    w("```text\n" + pr["recommended_final_query"].strip() + "\n```\n")
    w(f"- Recall na calibração: {cal['known_item_recall'].get('recall_indexed', '')}")
    w(f"- Volume na calibração: {cal['volume_estimate_after_dedup']}")


def main():
    out = []
    w = out.append
    w("# Apêndice A — Estratégias de busca\n")
    w("*Protocolo PRISMA-P, `protocolo.md`. Gerado por `ferramentas/gera_apendice_a.py` a partir de "
      "`calibracao/`; as strings são copiadas dos JSON, sem redigitação. Contagens são instantâneos "
      "da data indicada em cada linha; o OpenAlex muda com o tempo.*\n")
    w("Cadeia de cada bloco: calibração (`<bloco>.json`) → revisão PRESS 2015 independente "
      "(`<bloco>-press.json`, as quatro pediram revisão obrigatória) → finalização, que aplica a "
      "PRESS, congela as linhas e mede recall em validação independente (`<bloco>-final.json`).\n")
    s1 = carrega("sq1-internacional")
    w("## Notas de sintaxe (valem para todos os blocos)\n")
    for f in s1.get("syntax_findings", []):
        w(f"- {f}")
    w("- Parallel `web_fetch` pode devolver *cache* para URLs longas quase idênticas: toda contagem confere o eco `meta.x_query`.")
    w("- GET longo falha no PubMed (HTTP 414 a ~5.400 caracteres): usar o *history server* do E-utilities (`usehistory=y`).\n")
    for nome, titulo in BLOCOS:
        w(f"\n---\n\n## {titulo}\n")
        fin = carrega(nome + "-final")
        if fin:
            bloco_final(w, fin)
        else:
            bloco_press(w, carrega(nome), carrega(nome + "-press"))
    w("\n---\n")
    w(open("ferramentas/scopus_wos.md").read())
    w("\n---\n")
    w(open("ferramentas/volume.md").read())
    open("apendice-a-estrategias.md", "w").write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
