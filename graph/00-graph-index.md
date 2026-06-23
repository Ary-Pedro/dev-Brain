---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: graphify
status: active
last_verified: 2026-06-19
token_policy: summary-first
tags: [meta, graph, moc]
---

# 00-graph-index — grafos de código

> Visão-texto dos grafos graphify. Um nó-resumo por repo + o grafo global.

| Repo | Nós | Arestas | Módulos | Nota |
|------|-----|---------|---------|------|
| prontuario | 1668 | 3113 | 89 | [[prontuario-grafo\|prontuario]] |
| faculdade-alessandro | 379 | 793 | 23 | [[faculdade-alessandro-grafo\|faculdade-alessandro]] |
| meudinheiro-v2 | 622 | 1301 | 35 | [[meudinheiro-v2-grafo\|meudinheiro-v2]] |
| mailerweb-portal | 831 | 1731 | 95 | [[mailerweb-portal-grafo\|mailerweb-portal]] |
| mailerweb-panel-v2 | 20746 | 38750 | 1095 | [[mailerweb-panel-v2-grafo\|mailerweb-panel-v2]] |

**Grafo global cross-repo:** `graph/devspace-merged.json` (merge dos 5).

Rebuild grafos: `bash graph/build-all.sh` · resumos: `python graph/summarize.py`.

Camada semântica (embeddings): ver [[hybrid-views]]. Estratégia: [[_strategy]].