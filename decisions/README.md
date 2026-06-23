---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: human
status: active
tags: [meta, decisions, adr, moc]
aliases: [decisions, adr]
---

# decisions — ADRs (Architecture Decision Records)

> Decisões arquiteturais **datadas e imutáveis**. Diferente de [[lessons]] (problema→solução técnica reaproveitável) e de [[corrections]] (vício de domínio a corrigir): aqui registra-se **POR QUÊ** uma escolha estrutural foi feita, com alternativas descartadas.

## Regras

- **Imutável.** Um ADR não se edita após `status: accepted`. Mudou de ideia? Cria um novo ADR que **supersede** o antigo (`status: superseded` no velho, link recíproco).
- **Numeração sequencial:** `NNNN-slug-curto.md` (ex.: `0001-dois-cerebros.md`).
- **Frontmatter:** `type: decision`. Corpo segue `_template.md`.
- **Quando criar:** escolha que afeta estrutura/política do vault ou dos projetos e que alguém (humano ou IA) questionaria depois ("por que é assim?").

## Índice

- [[0001-dois-cerebros-mailerweb-readonly]] — dois brains; mailerweb-brain read-only
- [[0002-dashboards-plugin-free]] — dashboards gerados por script, não por Dataview
- [[0003-stack-e-fluxo-2026-06]] — extensões, MCP localhost-only, hooks passivos, context-packet, panel-v2 skip

Template: [[_template]]. Ver [[routing]] · [[_strategy]] · [[00-index]].
