---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: human
status: stable
tags: [meta, graph]
---

# graph/ — grafos de código (graphify)

Visão em grafo do código do devSpace, gerada por [graphify](https://github.com/safishamsi/graphify).
Complementa o `know/` (COMO) e o `map/` (ONDE) com a **estrutura real** do código.

## O que tem aqui

```
graph/
├── build-all.sh          ← reconstrói tudo (AST-only, sem LLM, idempotente)
├── <slug>/graph.json     ← grafo por repo (nós + arestas + comunidades)
├── <slug>/GRAPH_REPORT.md← relatório legível (god nodes, conexões surpresa)
└── devspace-merged.json  ← grafo GLOBAL cross-repo do devSpace
```

## Rebuild

```bash
bash ~/devSpace/dev-Brain/graph/build-all.sh
```

Determinístico, local (tree-sitter, 36 langs), **zero token de LLM** — só estrutura de código.

## Repos incluídos

prontuario · faculdade-alessandro · meudinheiro-v2 · mailerweb-portal · mailerweb-panel-v2

**Fora** (de propósito): `wiks` (só docs Markdown, sem código) · `faculdade-atvdd` (diretório vazio) · `theds_panel` (3 checkouts aninhados, inclui legado Python 2.7).

## Extração semântica (docs/PDF) — opcional, custa LLM

`build-all.sh` é AST-only. Para incluir docs/README/PDF no grafo, rode o skill:

```
/graphify ~/devSpace/projeto/meuDinheiroNaMaoV2
```

## Consultar o grafo

```bash
GR=~/devSpace/dev-Brain/graph
graphify query "como o auth conversa com o banco" --graph $GR/devspace-merged.json
graphify path "Controller" "Repository"            --graph $GR/prontuario/graph.json
graphify explain "CtrlPrograma"                    --graph $GR/prontuario/graph.json
```

> `graphify` = `~/.local/share/graphify-venv/bin/graphify` (ou symlink `~/.local/bin/graphify`).

Ver visão geral em [[00-index]] · padrões em [[routing]].
