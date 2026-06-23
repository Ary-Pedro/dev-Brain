---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: human
status: active
tags: [meta, docker, readme]
---

# dev-Brain · Obsidian no Docker

Roda o Obsidian (desktop) dentro de container, acessível pelo **browser** (KasmVNC). Pra visualizar o vault `dev-Brain` — graph view, links, tags.

## Subir

```bash
cd ~/devSpace/dev-Brain/docker
docker compose up -d
```

Primeira vez baixa a imagem `lscr.io/linuxserver/obsidian` (~1.5 GB).

## Acessar

- http://localhost:3838  (ou https://localhost:3839) — portas 3000/3001 ficaram pro mailerweb frontend
- No WSL2: o `localhost` do Windows alcança a porta. Se não, use o IP do WSL: `hostname -I`.

## Abrir o vault (1ª vez)

Na UI do Obsidian → **Open folder as vault** → navegue até **`/config/dev-Brain`** → Open.
Depois: **Graph view** (ícone de grafo / `Ctrl+G`) — nós coloridos por domínio (know / map / mailerweb / meta).

> Plugin de grafo nativo já vem. As cores estão em `dev-Brain/.obsidian/graph.json`.

## Comandos

```bash
docker compose logs -f          # ver logs
docker compose stop             # parar (mantém estado)
docker compose down             # remover container (volume obsidian_config fica)
docker compose down -v          # remover tudo, inclusive settings do Obsidian
```

## Notas

- O vault é **bind-mount read-write**: edições no Obsidian gravam direto em `~/devSpace/dev-Brain`.
- `obsidian_config` (named volume) guarda só o estado/UI do Obsidian, não o vault.
- Grafo de **código** (graphify) é outra coisa: `dev-Brain/graph/*/GRAPH_REPORT.md` + `graph.json` (ver `graph/README.md`).
