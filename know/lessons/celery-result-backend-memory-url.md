---
type: lesson
scope: cross-repo
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: ai
status: active
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [lesson, celery, django, testing]
keywords: [celery, result-backend, memory, ModuleNotFoundError, no-module-named-memory, broker, cache+memory, by_url, settings-test]
aliases: [celery-result-backend-memory-url]
---

# Celery: `ModuleNotFoundError: No module named 'memory'`

**Contexto:** rodar testes/tasks com `CELERY_BROKER_URL=memory://`.
**Sintoma:** qualquer task quebra com `ModuleNotFoundError: No module named 'memory'` (de `celery.app.backends.by_url`).
**Causa:** `CELERY_RESULT_BACKEND` herdou `memory://` do broker. `memory://` é transporte de **broker** válido, mas **não** é um result backend → Celery tenta importar um backend chamado `memory`.
**Solução:** setar um result backend válido em memória: `CELERY_RESULT_BACKEND = "cache+memory://"` (ou `django-db`, ou desabilitar resultados).
**Evitar futuro:** broker e result backend são coisas distintas; ao trocar o broker p/ `memory://`, defina o result backend explicitamente.
**Relacionado:** [[python-django]] · [[testing]].

**Visto em:** [[daily/2026-06-19]]
