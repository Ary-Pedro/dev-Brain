---
type: decision
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: active
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [decision, adr, dashboards, automation]
aliases: [ADR-0002]
---

# ADR-0002 — Dashboards gerados por script, não por plugin

- **Status:** aceita
- **Data:** 2026-06-19

## Contexto

Os `dashboards/*.md` usavam blocos `dataview`, mas o plugin Dataview não estava instalado — então não renderizavam nada. Vault AI-first deve ser legível no **filesystem puro** (a IA lê o `.md` direto, sem app Obsidian aberto).

## Decisão

Dashboards têm uma **tabela estática gerada por script** (`dashboards/build-dashboards.py`, lê o frontmatter de `projects/*.md`) entre marcadores `<!-- @generated -->`. O bloco `dataview` fica por cima como **enhancement opcional** para quem abrir o Obsidian com o plugin. A fonte canônica é a tabela gerada.

## Alternativas descartadas

- **Só Dataview** — quebra sem o plugin; invisível pra IA via filesystem; depende de código de terceiros.
- **Tabela 100% manual** — desatualiza; duplica o que já está no frontmatter dos cards.

## Consequências

- Funciona sem plugin e a IA lê direto; regenerável (`python3 dashboards/build-dashboards.py`).
- Marcadores `@generated`/`@user` preservam nota manual ao regenerar.
- Mesmo padrão dos `graph/*-grafo.md` (gerado de fonte). Plugin vira opcional, não dependência.

Ver [[projects-board]] · [[context-economist]] · [[hybrid-views]].
