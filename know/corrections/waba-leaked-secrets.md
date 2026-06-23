---
type: correction
scope: mailerweb
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: active
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [know, corrections, security, urgent]
keywords: [secret, token, leak, vazamento, app-secret, access-token, waba, meta, rotation]
aliases: [waba-leaked-secrets]
---

# 🔴 Credenciais Meta/WABA expostas no chat — ROTACIONAR

- **Onde:** App Secret + access token da integração Meta/WABA foram colados/expostos durante a sessão WABA (ver [[daily/2026-06-19]], Pendências).
- **Viola:** [[security]] (segredos nunca em chat/log/repo; rotação após exposição).
- **Risco:** quem tiver o token envia mensagens, lê webhooks e acessa a WABA em nome da conta até a rotação.
- **Ação (fazer já):**
  1. **App Secret** → Meta App Dashboard → Configurações → Básico → *Redefinir chave secreta do app*.
  2. **Access token** → gerar novo (System User token de longa duração) e revogar o antigo.
  3. Atualizar os segredos **só** via env/secret manager (nunca no código/chat). Ver [[security]].
  4. Conferir histórico/transcript e remover onde apareceram.
- **Status:** ✅ RESOLVIDO (2026-06-19) — tokens descontinuados pelo usuário; sem exposição ativa. Mantido como registro + lição preventiva.
- **Evitar futuro:** ao depurar API, mascarar token (`Bearer ****`); nunca colar credencial crua no chat.

Visto em [[daily/2026-06-19]] · ver [[security]] · [[meta-webhook-setup-gotchas]].
