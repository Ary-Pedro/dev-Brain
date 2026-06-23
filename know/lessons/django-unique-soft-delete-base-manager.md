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
tags: [lesson, django, soft-delete]
keywords: [django, unique, soft-delete, is_deleted, duplicate-entry, 1062, sequence, protocol_number, base_manager, default-manager]
aliases: [django-unique-soft-delete-base-manager]
---

# Campo unique reusado após soft-delete (gerador de sequência)

**Contexto:** model com campo unique gerado por sequência (ex.: `protocol_number = GD-YYYY-NNNNN`) + soft-delete (`is_deleted`).
**Sintoma:** criar novo registro após soft-deletar → `(1062, "Duplicate entry 'GD-2026-00001' for key '...'")`.
**Causa:** o gerador calcula o próximo número via o **manager padrão** (que esconde `is_deleted=True`) → não vê os soft-deletados → regenera um número que **ainda existe** na tabela (a unique constraint do banco vê todas as linhas).
**Solução:** calcular o `max`/próxima sequência pelo **`_base_manager`** (não filtrado): `type(self)._base_manager.filter(...).order_by("-campo").first()`.
**Evitar futuro:** sequência/unicidade que coexiste com soft-delete deve consultar TODAS as linhas (`_base_manager`/`all_objects`), nunca o manager filtrado.
**Relacionado:** [[python-django]].

**Visto em:** [[daily/2026-06-19]]
