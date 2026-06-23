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
# 📚 Lições — dashboard

> Requer **Dataview**. Memória reutilizável; busca por keyword. Ver [[lessons]].

```dataview
TABLE keywords, tags
FROM "know/lessons"
WHERE contains(tags, "lesson")
SORT file.name ASC
```
