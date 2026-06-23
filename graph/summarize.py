#!/usr/bin/env python3
"""
summarize.py — gera, por repo, um DIGEST compacto + nota-texto Obsidian a partir do graph.json.
Comunidades são NOMEADAS pela pasta/módulo dominante (não "Community N").
Saída: graph/<slug>.digest.json  e  graph/<slug>.md
Uso:   ~/.local/share/graphify-venv/bin/python summarize.py
"""
import json, collections, pathlib, re, datetime

GRAPH = pathlib.Path(__file__).parent
REPOS = ["prontuario", "faculdade-alessandro", "meudinheiro-v2", "mailerweb-portal", "mailerweb-panel-v2"]
MAILERWEB = {"mailerweb-portal", "mailerweb-panel-v2"}
TODAY = datetime.date.today().isoformat()

def scope_of(slug):
    """scope canônico (ver [[_frontmatter]]): mailerweb p/ repos do universo, senão o slug."""
    return "mailerweb" if slug in MAILERWEB else slug

def top_dir(src, repo_aware=False):
    if not src:
        return "(raiz)"
    parts = src.replace("\\", "/").split("/")
    # se prefixado por repo (grafo merged): repo::path
    if repo_aware and "::" in src:
        return src.split("::", 1)[0]
    # mantém apps/<x> ou src/main/java/<x> compacto
    if parts[0] in ("apps", "src") and len(parts) > 1:
        if parts[0] == "src":
            # src/main/java/<pkg> -> <pkg>; src/<x> -> <x>
            for i, p in enumerate(parts):
                if p in ("java", "kotlin", "resources") and i + 1 < len(parts):
                    return parts[i + 1]
            return parts[1] if len(parts) > 1 else parts[0]
        return parts[0] + "/" + parts[1]
    return parts[0] if len(parts) > 1 else (parts[0] or "(raiz)")

def name_community(nodes):
    dirs = collections.Counter(top_dir(n.get("source_file", "")) for n in nodes)
    return dirs.most_common(1)[0][0], dict(dirs.most_common(5))

def summarize(slug):
    p = GRAPH / slug / "graph.json"
    if not p.exists():
        return None
    g = json.loads(p.read_text())
    nodes = g["nodes"]
    links = g.get("links") or g.get("edges") or []
    deg = collections.Counter()
    for e in links:
        deg[e["source"]] += 1
        deg[e["target"]] += 1
    by_id = {n["id"]: n for n in nodes}
    # comunidades
    comm = collections.defaultdict(list)
    for n in nodes:
        comm[n.get("community", -1)].append(n)
    comms = []
    for cid, members in comm.items():
        label, dirs = name_community(members)
        members_sorted = sorted(members, key=lambda m: -deg[m["id"]])
        comms.append({
            "id": cid, "label": label, "size": len(members), "dirs": dirs,
            "samples": [m["label"] for m in members_sorted[:6]],
        })
    comms.sort(key=lambda c: -c["size"])
    # god nodes
    gods = []
    for nid, d in deg.most_common(20):
        n = by_id.get(nid, {})
        gods.append({"label": n.get("label", nid), "degree": d, "file": n.get("source_file", "")})
    digest = {
        "slug": slug, "n_nodes": len(nodes), "n_edges": len(links),
        "n_comms": len(comm), "top_comms": comms[:15], "gods": gods,
    }
    (GRAPH / f"{slug}.digest.json").write_text(json.dumps(digest, ensure_ascii=False, indent=2))
    write_note(digest)
    return digest

def write_note(d):
    slug = d["slug"]
    lines = [
        "---",
        "type: note",
        f"scope: {scope_of(slug)}",
        "brain_policy: dev-brain",
        "write_policy: dev-brain-only",
        "audience: ai",
        "source: graphify",
        "status: active",
        "confidence: high",
        f"last_verified: {TODAY}",
        "token_policy: summary-first",
        f"tags: [graph, code, {slug}]",
        f"aliases: [{slug}-graph]",
        "---", "",
        f"# {slug} — grafo de código",
        "",
        f"> Estrutura real do código (graphify, AST). **{d['n_nodes']} nós · {d['n_edges']} arestas · {d['n_comms']} módulos**.",
        f"> Mapa do projeto: [[{slug}]] · relatório bruto: `graph/{slug}/GRAPH_REPORT.md` · grafo: `graph/{slug}/graph.json`.",
        "",
        "## Módulos (comunidades, nomeadas pela pasta dominante)", "",
        "| Módulo | Nós | Pastas | Exemplos |",
        "|--------|-----|--------|----------|",
    ]
    for c in d["top_comms"]:
        dirs = ", ".join(f"{k} ({v})" for k, v in list(c["dirs"].items())[:3])
        samp = ", ".join(f"`{s}`" for s in c["samples"][:4])
        lines.append(f"| **{c['label']}** | {c['size']} | {dirs} | {samp} |")
    lines += ["", "## Hubs (god nodes — maior conectividade)", "",
              "| Símbolo | Grau | Arquivo |", "|---------|------|---------|"]
    for gd in d["gods"][:12]:
        lines.append(f"| `{gd['label']}` | {gd['degree']} | `{gd['file']}` |")
    lines += ["", "> Hub com grau muito alto + nome genérico = candidato a quebrar em peças menores (ver [[_strategy]])."]
    out = "\n".join(lines)
    # preserva bloco @user (ex.: "🧠 Leitura arquitetural" feita por agente) entre reruns
    dest = GRAPH / f"{slug}-grafo.md"   # nome -grafo evita colisão com map/<slug>.md
    user_block = ""
    if dest.exists():
        m = re.search(r"<!-- @user:start -->[\s\S]*?<!-- @user:end -->", dest.read_text())
        if m:
            user_block = "\n\n" + m.group(0)
    out += user_block + "\n\nVer [[00-graph-index]] · padrões em [[routing]]."
    dest.write_text(out)

def write_index(digests):
    lines = ["---",
             "type: moc", "scope: global", "brain_policy: dev-brain", "write_policy: dev-brain-only",
             "audience: both", "source: graphify", "status: active",
             f"last_verified: {TODAY}", "token_policy: summary-first", "tags: [meta, graph, moc]",
             "---", "", "# 00-graph-index — grafos de código",
             "", "> Visão-texto dos grafos graphify. Um nó-resumo por repo + o grafo global.", "",
             "| Repo | Nós | Arestas | Módulos | Nota |", "|------|-----|---------|---------|------|"]
    for d in digests:
        lines.append(f"| {d['slug']} | {d['n_nodes']} | {d['n_edges']} | {d['n_comms']} | [[{d['slug']}-grafo\\|{d['slug']}]] |")
    lines += ["", "**Grafo global cross-repo:** `graph/devspace-merged.json` (merge dos 5).",
              "", "Rebuild grafos: `bash graph/build-all.sh` · resumos: `python graph/summarize.py`.",
              "", "Camada semântica (embeddings): ver [[hybrid-views]]. Estratégia: [[_strategy]]."]
    (GRAPH / "00-graph-index.md").write_text("\n".join(lines))

if __name__ == "__main__":
    digs = [d for d in (summarize(s) for s in REPOS) if d]
    write_index(digs)
    for d in digs:
        print(f"{d['slug']}: {d['n_nodes']} nós, {d['n_comms']} módulos -> {d['slug']}.md")
    print("00-graph-index.md gerado")
