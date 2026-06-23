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
# 📊 Projetos — dashboard

> Requer plugin **Dataview** (ver [[obsidian-plugins]]). Sem ele, ver cards em `projects/`.

```dataview
TABLE stack, token_weight AS "peso IA", status, brain_policy AS "domínio"
FROM "projects"
WHERE type = "project"
SORT token_weight ASC
```

<!-- @generated:start -->
## Tabela (gerada — sem plugin)

| Projeto | Peso IA | Status | Stack | Domínio | Nós grafo | Custo graph.json |
|---------|---------|--------|-------|---------|-----------|------------------|
| [[mailerweb-panel-v2-proj\|mailerweb-panel-v2]] | **crítico** | active | python, django, celery, react, mysql | mailerweb-brain | 20717 | 20753 KB |
| [[theds-panel-proj\|theds-panel]] | **crítico** | active | python, django, react, celery, mysql, redis | mailerweb-brain | 0 | — |
| [[mailerweb-portal-proj\|mailerweb-portal]] | **médio** | active | python, django-cms, mysql | mailerweb-brain | 799 | 801 KB |
| [[prontuario-proj\|prontuario]] | **médio** | active | java, spring-boot, maven, h2 | (nenhum) | 1648 | 1753 KB |
| [[wiks-proj\|wiks]] | **médio** | active | markdown, docs | mailerweb-brain | 0 | — |
| [[faculdade-alessandro-proj\|faculdade-alessandro]] | **baixo** | active | java, spring-boot, docker | (nenhum) | 379 | 419 KB |
| [[faculdade-atvdd-proj\|faculdade-atvdd]] | **baixo** | draft | typescript, vite, react | (nenhum) | 0 | — |
| [[meudinheiro-v2-proj\|meudinheiro-v2]] | **baixo** | active | typescript, nextjs, prisma, postgres | (nenhum) | 622 | 613 KB |

> Regra de peso (ver [[context-economist]]): `baixo`=resumo+2 notas · `médio`=digest+graphify query · `alto`=bridge/subagent · `crítico`=exigir plano, nunca abrir repo inteiro.
> Gerado de `projects/*.md` por `dashboards/build-dashboards.py`. 8 projetos.
<!-- @generated:end -->

<!-- @user:start -->
(observações manuais do Pedro)
<!-- @user:end -->

Regenerar: `python3 dashboards/build-dashboards.py`.
