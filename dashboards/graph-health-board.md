---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: ai
status: active
tags: [meta, dashboard]
---
# 🕸️ Saúde do grafo — dashboard

- Estrutura: [[00-graph-index]] · diagramas: [[_diagramas]]
- Missing-links (relações sem `[[ ]]`): [[dev-brain_missing-links]] · [[mailerweb_missing-links]]
- Rebuild: `bash graph/build-all.sh` → `python graph/summarize.py` → `python graph/vector-map.py <vault> <base>`

```dataview
TABLE graph_nodes AS nós, graph_edges AS arestas, token_weight AS peso
FROM "projects"
WHERE type = "project"
SORT graph_nodes DESC
```
