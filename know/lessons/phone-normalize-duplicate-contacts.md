---
type: lesson
scope: mailerweb
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: ai
status: active
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [lesson, whatsapp, contacts, normalization]
keywords: [telefone, phone, normalize, e164, wa_id, country-code, ddd, 55, duplicate-contact, find_or_create, phonenumbers]
aliases: [phone-normalize-duplicate-contacts]
---

# Telefone sem código de país duplica contato/sessão

**Contexto:** WhatsApp — inbound chega como `wa_id` E.164 (`5521995897270`), mas atendente digita sem o 55 (`21995897270`).
**Sintoma:** mesmo cliente vira 2 contatos + 2 sessões; `find_or_create` por telefone não casa.
**Causa:** telefone não normalizado antes do `find_or_create` → formatos diferentes = registros diferentes.
**Solução:** normalizar p/ o formato do `wa_id` (dígitos E.164, sem `+`) com `phonenumbers.parse(raw, "BR")` → `format_number(..., E164).lstrip("+")`, com fallback pros dígitos crus. Aplicar no caminho manual (criar atendimento) — o inbound já vem normalizado.
**Evitar futuro:** todo ponto que aceita telefone do usuário deve normalizar antes de buscar/criar contato.
**Relacionado:** [[python-django]] · domínio → mailerweb-brain `apps/contacts.md`, `apps/sessions.md` (via [[mailerweb-bridge]]).

**Visto em:** [[daily/2026-06-19]]
