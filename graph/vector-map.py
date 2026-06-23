#!/usr/bin/env python3
"""
vector-map.py — mapa vetorial semântico de um vault Obsidian.
3ª visão (semântica) ao lado de links (Obsidian) e estrutura (graphify).
Também emite <base>_missing-links.md: notas próximas SEM link explícito.

Metodologia (corrigida):
- embedding por nota (MiniLM multilingual, 384-dim, L2-normalizado).
- CLUSTER nos embeddings ORIGINAIS (HDBSCAN), não nas coords 2D — 2D é só layout.
- UMAP só para desenhar.
- cor = PASTA (âncora semântica interpretável); símbolo = cluster; rótulo = nome do arquivo.
- hover limpo (pasta · cluster · 1ª frase), sem tabela crua.

Uso:
  ~/.local/share/vecmap-venv/bin/python vector-map.py <vault_path> [saida_basename]
"""
import sys, re, pathlib, datetime
import numpy as np
import pandas as pd
import plotly.express as px
from sentence_transformers import SentenceTransformer
import umap, hdbscan

_args = [a for a in sys.argv[1:] if not a.startswith("--")]
_flags = {a for a in sys.argv[1:] if a.startswith("--")}
VAULT = pathlib.Path(_args[0]).expanduser()
BASE = _args[1] if len(_args) > 1 else VAULT.name
COLOR_BY = "domain" if "--domain" in _flags else "pasta"   # M2: cor por tag de domínio (além de pasta)
OUT_DIR = pathlib.Path(__file__).parent
DOMAIN_TAGS = {"core-infra", "comms", "ai", "biz", "marketing"}

def clean_markdown(text):
    text = re.sub(r"---[\s\S]*?---", "", text, count=1)   # frontmatter
    text = re.sub(r"```[\s\S]*?```", " ", text)            # code fences
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[\[([^\]|#]+).*?\]\]", r"\1", text)
    text = re.sub(r"[|#>*`]", " ", text)                   # mata pipes/markup -> hover limpo
    return re.sub(r"\s+", " ", text).strip()

def wikilinks(text):
    return set(m.split("|")[0].split("#")[0].strip().lower()
               for m in re.findall(r"\[\[([^\]]+)\]\]", text))

def embed_text(raw, cleaned):
    """Sinal FOCADO p/ o vetor: título + tags + keywords (peso 2x) + cabeça do corpo.
    Evita que menção incidental no corpo (ex.: 'docker compose' num app financeiro)
    arraste o centroide. O 'sobre o quê' manda mais que cada token."""
    title = (re.search(r"^#\s+(.+)", raw, re.M) or [None, ""])[1].strip()
    fm = (re.search(r"^---\n([\s\S]*?)\n---", raw) or [None, ""])[1]
    tags = (re.search(r"tags:\s*\[([^\]]*)\]", fm) or [None, ""])[1]
    kw = (re.search(r"keywords:\s*\[([^\]]*)\]", fm) or [None, ""])[1]
    head = cleaned[:1000]
    focus = f"{title}. {tags} {kw}. "          # título+tags+keywords
    return (focus * 2) + head                   # peso 2x no foco vs corpo

def folder(rel):
    parts = pathlib.Path(rel).parts
    return parts[0] if len(parts) > 1 else "(raiz)"

def domain_of(raw):
    """Bucket de domínio (tags do frontmatter): core-infra/comms/ai/biz/marketing.
    Sem match -> 'outros'. Usado só no modo --domain (M2)."""
    fm = (re.search(r"^---\n([\s\S]*?)\n---", raw) or [None, ""])[1]
    tags = (re.search(r"tags:\s*\[([^\]]*)\]", fm) or [None, ""])[1]
    toks = {t.strip().lower() for t in tags.split(",")}
    hit = toks & DOMAIN_TAGS
    return sorted(hit)[0] if hit else "outros"

files, texts, links, folders, firsts, domains = [], [], [], [], [], []
for path in VAULT.rglob("*.md"):
    if ".obsidian" in path.parts or ".sync" in path.parts or "templates" in path.parts:
        continue
    if "GRAPH_REPORT" in path.name or path.name.endswith("_missing-links.md"):
        continue
    # IA não consome tudo: pula meta/navegação humana e notas marcadas audience: human
    if "daily" in path.parts or path.name == "README.md" \
       or path.name.startswith("00-") or path.name == "_toolbox.md":
        continue
    raw = path.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"^audience:\s*human\b", raw, re.M):
        continue
    cleaned = clean_markdown(raw)
    if len(cleaned) < 80:
        continue
    rel = str(path.relative_to(VAULT))
    files.append(rel)
    texts.append(embed_text(raw, cleaned))     # sinal focado, não nota inteira
    links.append(wikilinks(raw))
    folders.append(folder(rel))
    domains.append(domain_of(raw))
    firsts.append((cleaned[:160] + "…") if len(cleaned) > 160 else cleaned)

N = len(files)
if N < 3:
    print(f"poucas notas ({N}) em {VAULT} — abortando"); sys.exit(1)

print(f"{N} notas. Embedding...")
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
emb = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)

# CLUSTER nos embeddings originais (normalizado → euclidean ~ cosine). 2D é só layout.
mcs = max(2, N // 12)
clusters = hdbscan.HDBSCAN(min_cluster_size=mcs, min_samples=1, metric="euclidean").fit_predict(emb)
xy = umap.UMAP(n_neighbors=min(12, N - 1), min_dist=0.1, metric="cosine", random_state=42).fit_transform(emb)

stems = [pathlib.Path(f).stem for f in files]
df = pd.DataFrame({
    "file": files, "nota": stems, "pasta": folders, "domínio": domains,
    "x": xy[:, 0], "y": xy[:, 1],
    "cluster": [("ruído" if c == -1 else f"c{c}") for c in clusters],
    "resumo": firsts,
})
color_col = "domínio" if COLOR_BY == "domain" else "pasta"
fig = px.scatter(
    df, x="x", y="y", color=color_col, symbol="cluster", text="nota",
    hover_data={"x": False, "y": False, "pasta": True, "domínio": True, "cluster": True, "resumo": True, "nota": False},
    title=f"Mapa vetorial — {BASE} ({N} notas · cor={color_col} · proximidade 2D é APROXIMADA; relações reais em {BASE}_missing-links.md)",
)
fig.update_traces(textposition="top center", textfont_size=9, marker=dict(size=11, opacity=0.8))
fig.update_layout(legend_title_text=color_col)
suffix = "_domain" if COLOR_BY == "domain" else ""
out_html = OUT_DIR / f"{BASE}_vector_map{suffix}.html"
fig.write_html(out_html)
print(f"Gerado: {out_html}  (cor={color_col}, clusters: {len(set(clusters) - {-1})}, ruído: {(clusters==-1).sum()})")

# missing-links só no modo padrão (cor=pasta); modo --domain não reescreve p/ não clobberar
if COLOR_BY == "domain":
    sys.exit(0)

# missing-links: pares cos >= THRESH SEM link explícito entre si
print("Calculando missing-links...")
slug = [s.lower() for s in stems]
sim = emb @ emb.T
THRESH = 0.55
pairs = []
for i in range(N):
    for j in range(i + 1, N):
        s = float(sim[i, j])
        if s < THRESH:
            continue
        if slug[j] in links[i] or slug[i] in links[j]:
            continue
        pairs.append((s, files[i], files[j]))
pairs.sort(reverse=True)
md = ["---",
      "type: note", "scope: global", "brain_policy: dev-brain", "write_policy: dev-brain-only",
      "audience: ai", "source: vector", "status: active",
      f"last_verified: {datetime.date.today().isoformat()}", "token_policy: summary-first",
      "tags: [meta, graph, missing-links]",
      "---", "",
      f"# missing-links — {BASE}", "",
      f"> Notas com similaridade cosseno ≥ {THRESH} **sem** link `[[ ]]` entre si. Candidatas a `Relacionado:`.",
      f"> Calculado nos embeddings originais (não no layout 2D). {len(pairs)} pares.", "",
      "| Sim | Nota A | Nota B |", "|-----|--------|--------|"]
for s, a, b in pairs[:60]:
    md.append(f"| {s:.2f} | `{a}` | `{b}` |")
md += ["", "Ação: relação real → `Relacionado: [[B]]` em A. Ver [[_strategy]] (matriz link×vetor×graphify)."]
(OUT_DIR / f"{BASE}_missing-links.md").write_text("\n".join(md))
print(f"Gerado: {BASE}_missing-links.md ({len(pairs)} pares)")
