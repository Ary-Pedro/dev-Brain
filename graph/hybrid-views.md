---
type: meta
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: stable
token_policy: full
tags: [meta, graph, hybrid]
---

# hybrid-views — as 3 visões do conhecimento + ferramentas

> Nenhuma visão sozinha basta. Links dizem o que **você** ligou; código diz o que **importa** o quê; vetores dizem o que **fala parecido**. A interseção é onde mora o insight. Estratégia: [[_strategy]] · grafos de código: [[00-graph-index]] · roteamento: [[routing]].

## As 3 visões

### 1. Obsidian Graph — links manuais (intenção)
O grafo que você desenhou à mão com `[[ ]]`. Mostra a estrutura **deliberada** do vault.
- **Filtros** (barra do graph): `path:know`, `path:map`, `tag:#mailerweb` para isolar uma camada por vez. Combine (`path:know tag:#testing`).
- **Liga** sempre: `Existing files only` (mata fantasmas), `Arrows` (vê direção), `Tags`.
- **Local Graph** com depth **2-3** ao abrir uma nota — é a vizinhança real, sem o ruído do grafo global.
- Para quê: achar órfãs, hubs intencionais (MOCs), e onde a estrutura está rasa.

### 2. graphify `graph.html` — estrutura de código (realidade)
Grafo de import/chamada extraído dos repos. Não é opinião sua, é o que o código faz.
- Um nó-resumo por repo + grafo global cross-repo (`devspace-merged.json`). Detalhe em [[00-graph-index]].
- Para quê: god nodes, módulos acoplados, comunidades reais vs. organização que você *acha* que tem.

### 3. vector map — similaridade semântica (descoberta)
Embeddings das notas projetados em 2D (UMAP) + clusters (HDBSCAN). Mostra o que está **próximo no significado** mesmo sem link.

## Como rodar o vector map

```bash
~/.local/share/vecmap-venv/bin/python graph/vector-map.py <vault> <base>
```
Gera **`<base>_vector_map.html`** (mapa interativo) + **`<base>_missing-links.md`** (pares próximos sem link).

Exemplos:
```bash
~/.local/share/vecmap-venv/bin/python graph/vector-map.py ~/devSpace/dev-Brain dev-brain
~/.local/share/vecmap-venv/bin/python graph/vector-map.py ~/devSpace/mailerWeb/mailerweb-brain mailerweb
```
Deps (já no `vecmap-venv`): `sentence-transformers`, `umap-learn`, `hdbscan`, `plotly`. Modelo: `paraphrase-multilingual-MiniLM-L12-v2` (PT-BR ok). Threshold de missing-link: cos ≥ 0.55.

## O que procurar no mapa

- **Clusters bons** = sinal de saúde: billing / tenant / auth / setup aparecem **separados**. Se separa sozinho, a nota tem identidade clara.
- **Notas próximas SEM link = ouro.** É o caso de uso principal. Abra o `<base>_missing-links.md`, valide cada par, e se a relação for real adicione `Relacionado: [[B]]` na nota A. Bidirecional só se fizer sentido nos dois sentidos.
- **Clusters misturados** (billing colado em tenant colado em setup) = suas notas estão **genéricas demais**. Sinal pra quebrar em notas mais específicas.
- **Hubs falsos no centro** (nota que cai no meio de tudo) = nota guarda-chuva sem foco. **Quebrar** em peças menores e bem-tituladas.

## Plugins / ferramentas

- **Smart Connections** — embeddings locais **dentro** do Obsidian. Descobre relacionadas sem termo exato, direto na sidebar enquanto você escreve. Complemento ao vector map (interativo vs. batch).
- **TensorBoard Embedding Projector** — explorar os embeddings em 3D (PCA/t-SNE/UMAP), bom pra inspecionar clusters à mão.
- **Gephi / Cytoscape** — layout e métricas de grafo (centralidade, comunidades) sobre o grafo de links ou de código exportado.
- **Neo4j Bloom** — query visual se você carregar o grafo num Neo4j.
- **graphify `--mcp`** — servidor MCP do grafo de código: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`. Útil pra perguntar a estrutura sem abrir o HTML.

---

**Fluxo recomendado:** rode o vector map → triagem do `*_missing-links.md` → adicione `Relacionado:` nos pares reais → re-rode pra ver clusters limpando. Cruze com [[00-graph-index]] (código) quando uma proximidade semântica não casar com a estrutura real. Regras de quando usar cada visão: [[_strategy]]. Antes de codar: [[routing]].
