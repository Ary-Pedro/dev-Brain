---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: ai
status: active
tags: [meta, tasks, dashboard]
---

# ✅ Tarefas abertas — vault inteiro

> Requer plugin **Tasks**. Agrega todo `- [ ]` do vault. Board visual: [[tasks-board]].

## Pendentes (por prioridade)

```tasks
not done
sort by priority
sort by due
```

## Vencendo / atrasadas

```tasks
not done
(due before in 7 days) OR (is overdue)
sort by due
```

---

## Convenção (a IA segue ao criar/atualizar tarefa)

Tarefa = linha `- [ ]` em qualquer nota. Sintaxe Tasks (emoji opcional):

```text
- [ ] Texto da tarefa #projeto/mailerweb-panel-v2 🔼 📅 2026-06-25
```

- `#projeto/<slug>` — vincula ao card de projeto.
- `🔼`/`⏫`/`🔽` — prioridade (alta/urgente/baixa).
- `📅 YYYY-MM-DD` — data limite. `✅ YYYY-MM-DD` é posto ao concluir.
- IA usa isto como **checklist de uma tarefa** (quebra o trabalho em `- [ ]` no daily/sessão) e o humano marca `[x]` ou edita no board [[tasks-board]] (Kanban).

Ver [[pending-board]] · [[projects-board]].
