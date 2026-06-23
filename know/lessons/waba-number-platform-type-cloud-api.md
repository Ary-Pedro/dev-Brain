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
keywords: [waba, whatsapp, cloud-api, on-premise, platform_type, 133010, account-not-registered, coexistence, register, smb]
aliases: [waba-number-platform-type-cloud-api]
---

# WABA: número não envia pela Cloud API (ON_PREMISE / SMB)

**Contexto:** integrar um número WhatsApp ao painel (Cloud API) e o envio falha.
**Sintoma:** `POST /{phone_number_id}/messages` → `(#133010) Account not registered`; e `POST /{phone_number_id}/register` → `(#100) Register endpoint is not available for SMB businesses`. `GET ?fields=platform_type` retorna `ON_PREMISE` (ou `NOT_APPLICABLE`/`PENDING`).
**Causa:** o número está preso ao **WhatsApp Business App / On-Premise**, não à **Cloud API**. As plataformas são mutuamente exclusivas (salvo coexistência). `/register` clássico é só p/ Cloud API puro.
**Solução:**
- **Número novo dedicado (simples):** WhatsApp Manager → Adicionar número → verificar por **SMS/ligação** → `POST /{pid}/register {messaging_product:whatsapp, pin:<6díg>}` → vira `CLOUD_API`/`CONNECTED`. (Não precisa Embedded Signup/domínio.)
- **Manter número no celular (coexistência):** Embedded Signup de um BSP + scan de QR no app (≥2.24.17, WABA ligada a Página FB). Exige domínio HTTPS fixo + App Review p/ produção.
**Evitar futuro:** antes de depurar envio, cheque `GET /{pid}?fields=platform_type,status` — só `CLOUD_API`+`CONNECTED` envia pelo painel.
**Relacionado:** [[meta-webhook-setup-gotchas]] · [[meta-cloud-api-accepted-not-delivered]] (trio Cloud API setup) · domínio MailerWeb → mailerweb-brain `apps/integrations.md`, `apps/chat.md` (via [[mailerweb-bridge]]).

**Visto em:** [[daily/2026-06-19]]
