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
tags: [lesson, waba, whatsapp-cloud-api, webhook]
keywords: [meta, webhook, callback-url, append-slash, subscribed_apps, app-domains, embedded-signup, config_id, js-sdk, trycloudflare, verify-token, hub.challenge]
aliases: [meta-webhook-setup-gotchas]
---

# Meta WABA webhook + Embedded Signup: lista de gotchas

**Contexto:** configurar inbound/status (webhook) e/ou Embedded Signup; eventos não chegam ou popup falha.
**Sintoma/Causa → Fix:**
- Callback URL com `https://` **duplicado** → corrigir a URL.
- URL **sem barra final** (`/inbound` vs `/inbound/`) → `POST 500 RuntimeError APPEND_SLASH` (Django não redireciona POST). Use a barra.
- Webhook "verde" mas **não chega evento** → `subscribed_apps` vazio: `POST /{waba_id}/subscribed_apps`.
- Popup *"domínio não incluído nos domínios do app"* → **App → Configurações → Básico → App Domains** = domínio bare (sem http/path).
- Popup *"A opção JSSDK não está ativada"* → Facebook Login for Business → Settings → **Login com SDK JavaScript = Sim** + domínios JS SDK.
- `config_id` inválido → é o **Configuration ID** do Facebook Login for Business, **≠ WABA id**.
- App Domains (config do app) **≠** verificação de domínio do negócio (Business Settings → Domínios, meta-tag no `<head>`).
- Túnel `*.trycloudflare.com` é **efêmero** → muda a cada restart e re-quebra tudo acima; use domínio fixo (staging/prod / ngrok `--domain`).
**Verificar:** GET de verificação responde `hub.challenge` 200 quando `hub.verify_token` casa a instância; `GET /{app_id}/subscriptions` (app token `app_id|app_secret`) mostra `callback_url`+`fields` ativos.
**Relacionado:** [[security]] · domínio → mailerweb-brain `apps/webhooks.md`, `apps/integrations.md` (via [[mailerweb-bridge]]).

**Visto em:** [[daily/2026-06-19]]
