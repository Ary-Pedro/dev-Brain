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
tags: [lesson, waba, message-queue, campanha]
keywords: [campanha, message-queue, fan_out_campaign, send_single_transaction, _send_via_adapter, waba-template, content_type, cold-contact, MessageTransaction, soft-fk]
aliases: [campaign-message-queue-waba-template]
---

# Campanha não entrega template a contato frio (rota da fila ignora WABA template)

**Contexto:** campanha WABA com template aprovado; envio direto funciona, mas pela UI o contato frio não recebe.
**Sintoma:** `start_campaign` cria `MessageTransaction` com `body=''`, `content_type='text'`, sem template → fila manda texto vazio → Meta bloqueia cold.
**Causa:** há DUAS rotas de dispatch — a direta (`tasks._send_message`→`send_waba_template`) e a real da UI (`start_campaign`→fila `fan_out_campaign`→`send_single_transaction`→`_send_via_adapter`). A da fila só montava `campaign.template`/`message_template` (inline), **ignorando** `Campaign.waba_template_name` (soft FK).
**Solução:**
- `fan_out_campaign`: quando `campaign.waba_template_name`, montar tx `content_type='template'`, `body=nome`, `subject=idioma`, `buttons=[params já renderizados por contato]`.
- `_send_via_adapter`: branch `content_type=='template'` → `adapter.send_template(name, language, components)`.
**Evitar futuro:** ao adicionar um campo de envio na campanha, propague-o em AMBAS as rotas (direta + fila/MessageTransaction); a UI usa a fila.
**Relacionado:** [[python-django]] · domínio → mailerweb-brain `apps/campaigns.md`, `apps/message_queue.md` (via [[mailerweb-bridge]]).

**Visto em:** [[daily/2026-06-19]]
