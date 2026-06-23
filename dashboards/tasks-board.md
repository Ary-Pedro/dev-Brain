---
kanban-plugin: basic
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: human
status: active
tags: [meta, kanban, board]
---

## Backlog

- [ ] Local REST API + bloco MCP (porta 27124 no docker) #dev-brain @P2
- [ ] PostCommit hook `graphify --update` nos repos de código #automation
- [ ] graphify semântico em `prontuario` + `mailerweb-portal` #graph
- [ ] geradores (`summarize.py`/`vector-map.py`) emitirem frontmatter canônico #graph
- [ ] re-triar `dev-brain_missing-links.md` (72 pares) via [[brain-architect]] #brain


## Doing


## Done

**Complete**
- [x] 3 proj cards faltantes + `token_weight`
- [x] frontmatter normalizado (69 notas, schema [[_frontmatter]])
- [x] `decisions/` (ADR) + ADR-0001/0002
- [x] dashboard plugin-free + coluna de custo
- [x] plugins: Dataview, Linter, Iconize, Kanban, Tasks, Templater, Recent Files, Day Planner


%% kanban:settings
```
{"kanban-plugin":"basic","show-checkboxes":true}
```
%%
