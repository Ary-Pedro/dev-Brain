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
tags: [lesson, django, drf, frontend]
keywords: [django, uuid, primary-key, drf, serializer, IntegerField, UUIDField, Number, NaN, foreignkey-not-linked]
aliases: [django-uuid-pk-vs-integerfield]
---

# UUID PK + serializer IntegerField + Number() no front = links zerados

**Contexto:** payload cria o objeto (201) mas FKs/M2M (template, instância, lista) vêm vazios.
**Sintoma:** registro criado sem nenhum vínculo; nenhum erro de validação.
**Causa:** PKs são `UUIDField` (BaseModel), mas (a) o serializer DRF declarava os `*_id` como `IntegerField`/`ListField(child=IntegerField())` e (b) o front fazia `Number(uuid)` → `NaN` → filtrado → lista vazia / `undefined`. O IntegerField aceitava `[]` sem erro → 201 silencioso.
**Solução:** serializer → `UUIDField` (e `ListField(child=UUIDField())`); front → **não** `Number()` em id (UUID é string); passar como string.
**Evitar futuro:** em projeto com UUID PK, nunca coage id pra número no front; serializers de id sempre `UUIDField`.
**Relacionado:** [[python-django]] · [[code-style]].

**Visto em:** [[daily/2026-06-19]]
