#!/usr/bin/env python3
"""
build-dashboards.py — gera tabelas estáticas (SEM plugin) a partir do frontmatter
dos project cards em projects/*.md. Substitui só o bloco entre <!-- @generated --> ,
preservando o bloco Dataview (pra quem tiver o plugin) e o bloco @user.

Por quê: dashboards/*.md usam Dataview, que não está instalado — então não renderizam.
Esta tabela funciona no filesystem puro (e a IA lê direto). Reexecutável.

Uso: python3 ~/devSpace/dev-Brain/dashboards/build-dashboards.py
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROJ = ROOT / "projects"
WEIGHT_ORDER = {"crítico": 0, "critico": 0, "alto": 1, "médio": 2, "medio": 2, "baixo": 3}


def fm(text):
    m = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    d = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"([a-z_]+):\s*(.*)", line)
        if mm:
            d[mm.group(1)] = mm.group(2).strip()
    return d


def graph_kb(slug):
    """Tamanho do graph.json do projeto, em KB (proxy de custo de leitura crua)."""
    gj = ROOT / "graph" / slug / "graph.json"
    return gj.stat().st_size // 1024 if gj.exists() else 0


def collect():
    rows = []
    for p in sorted(PROJ.glob("*.md")):
        d = fm(p.read_text(encoding="utf-8"))
        if d.get("type") != "project":
            continue
        slug = p.stem.replace("-proj", "")
        kb = graph_kb(slug)
        rows.append({
            "slug": slug,
            "stack": d.get("stack", "").strip("[]"),
            "weight": d.get("token_weight", "?"),
            "status": d.get("status", "?"),
            "domain": d.get("domain_brain", "—"),
            "nodes": d.get("graph_nodes", "0"),
            "cost": f"{kb} KB" if kb else "—",
        })
    rows.sort(key=lambda r: WEIGHT_ORDER.get(r["weight"], 9))
    return rows


def render(rows):
    out = ["<!-- @generated:start -->",
           "## Tabela (gerada — sem plugin)", "",
           "| Projeto | Peso IA | Status | Stack | Domínio | Nós grafo | Custo graph.json |",
           "|---------|---------|--------|-------|---------|-----------|------------------|"]
    for r in rows:
        link = f"[[{r['slug']}-proj\\|{r['slug']}]]"
        out.append(f"| {link} | **{r['weight']}** | {r['status']} | {r['stack']} | {r['domain']} | {r['nodes']} | {r['cost']} |")
    out += ["",
            "> Regra de peso (ver [[context-economist]]): "
            "`baixo`=resumo+2 notas · `médio`=digest+graphify query · "
            "`alto`=bridge/subagent · `crítico`=exigir plano, nunca abrir repo inteiro.",
            f"> Gerado de `projects/*.md` por `dashboards/build-dashboards.py`. {len(rows)} projetos.",
            "<!-- @generated:end -->"]
    return "\n".join(out)


def main():
    board = ROOT / "dashboards" / "projects-board.md"
    text = board.read_text(encoding="utf-8")
    block = render(collect())
    if "<!-- @generated:start -->" in text:
        text = re.sub(r"<!-- @generated:start -->.*?<!-- @generated:end -->",
                      block, text, count=1, flags=re.DOTALL)
    else:
        # insere após o bloco dataview (primeira cerca ``` fechando) ou no fim
        text = text.rstrip() + "\n\n" + block + "\n"
    board.write_text(text, encoding="utf-8")
    print(f"projects-board.md atualizado ({len(collect())} projetos).")


if __name__ == "__main__":
    main()
