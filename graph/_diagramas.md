---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: human
status: stable
tags: [meta, graph, diagramas]
---

# _diagramas — abrir as visualizações

> Índice das visões gráficas (HTML). Pra TEU olho — a IA usa os `.md`/`graph.json`, não estes HTML.
> Abrir: clica no link (se o Obsidian abrir externo) ou cola o caminho no browser do Windows:
> `file://\\wsl.localhost\Ubuntu\home\pedroczar\devSpace\dev-Brain\graph\<arquivo>`

## Estrutura de código (graphify tree)

| Projeto | Diagrama |
|---------|----------|
| global devSpace | `devspace_tree.html` |
| mailerweb-panel-v2 | `mailerweb-panel-v2/mailerweb-panel-v2_tree.html` |
| mailerweb-portal | `mailerweb-portal/mailerweb-portal_tree.html` |
| prontuario | `prontuario/prontuario_tree.html` |
| faculdade-alessandro | `faculdade-alessandro/faculdade-alessandro_tree.html` |
| meudinheiro-v2 | `meudinheiro-v2/meudinheiro-v2_tree.html` |

## Semântico (vector map)

| Vault | Mapa | Missing-links |
|-------|------|---------------|
| dev-Brain | `dev-brain_vector_map.html` | [[dev-brain_missing-links]] |
| mailerweb-brain | `mailerweb_vector_map.html` | [[mailerweb_missing-links]] |

> No vector map: **cor = pasta**, símbolo = cluster, rótulo = nome. Proximidade 2D é APROXIMADA — relações reais nos `*_missing-links.md` (cosseno verdadeiro).

## Texto (pra IA e humano)

- [[00-graph-index]] — resumo por repo · [[hybrid-views]] — as 3 visões explicadas

Rebuild tudo: `bash graph/build-all.sh` · resumos: `python graph/summarize.py` · vetor: `python graph/vector-map.py <vault> <base>`.
