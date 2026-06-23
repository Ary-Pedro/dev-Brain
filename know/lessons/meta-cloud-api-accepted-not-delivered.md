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
tags: [lesson, waba, whatsapp-cloud-api]
keywords: [meta, whatsapp, cloud-api, wamid, accepted, not-delivered, nao-entrega, payment, allowlist, 24h-window, template, test-number]
aliases: [meta-cloud-api-accepted-not-delivered]
---

# Meta Cloud API: aceita (wamid) mas não entrega

**Contexto:** `POST /messages` retorna 200 com `messages[].id` (wamid) mas a mensagem não chega no destino.
**Sintoma:** sucesso na API, status preso em `sent` (sem `delivered`), nada no celular destino.
**Causa (3 frentes):**
1. **Sem forma de pagamento** na WABA → Meta aceita mas não entrega msg iniciada pela empresa (banner "adicionar forma de pagamento").
2. **Número de TESTE** (+1 555 da Meta) → só entrega a destinos na **allowlist** (API Setup → "To" → manage list).
3. **Contato frio** (fora da janela 24h, 1º contato) → só recebe **template aprovado**; texto livre é bloqueado.
**Solução:** confirmar pagamento na WABA; adicionar destino na allowlist (se nº de teste); usar **template** p/ cold/1º contato (texto livre só dentro da janela 24h, aberta quando o cliente te escreve).
**Evitar futuro:** "aceito ≠ entregue". O status real só vem por **webhook** (`statuses[]` delivered/read/failed + `errors[]`); sem webhook configurado você fica cego.
**Relacionado:** [[meta-webhook-setup-gotchas]] · domínio → mailerweb-brain `apps/integrations.md`, `apps/campaigns.md` (via [[mailerweb-bridge]]).

**Visto em:** [[daily/2026-06-19]] · ver [[lessons/meta-webhook-setup-gotchas]]
