---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: ai
status: active
tags: [know, lessons, moc]
aliases: [lessons]
---

# lessons — memória reutilizável (o "dev treinado")

> Problema → solução keyworded, extraído de sessões reais via `/journal`.
> Recall futuro: por tag, por keyword no frontmatter, ou busca semântica ([[hybrid-views]]).
> Antes de resolver um problema novo, **procure aqui** (e nas daily notes) por sintoma/keyword parecido.

## Como nasce

- `/journal` ao fim da sessão → daily note em `daily/` + 1 lição por problema reaproveitável aqui.
- Hook SessionEnd grava breadcrumb automático em `daily/<data>.md` (tópicos + arquivos); `/journal` enriquece.

## Convenção

`lessons/<slug>.md` · frontmatter `tags: [lesson, <tema>]` + `keywords: [...]`. Atualizar lição existente em vez de duplicar.

## Índice

| Lição | Keywords |
|-------|----------|
| [[montar-dev-brain-ai-operacional\|Como montar um dev-Brain AI-operacional]] | dev-brain, second-brain, ai-operational, vault, graphify, embeddings |
| [[claude-agents-load-on-boot\|Claude Code: agents/hooks novos não carregam na sessão atual]] | claude-code, agents, hooks, sessionstart, boot, registry |
| [[docker-port-already-allocated\|docker: Bind for 0.0.0.0:PORT failed: port is already allocated]] | docker, compose, porta, port-allocated, conflito |
| [[linuxserver-selkies-waiting-for-stream\|linuxserver/obsidian (Selkies) preso em "Waiting for stream"]] | selkies, webrtc, kasmvnc, obsidian, linuxserver, waiting-for-stream, stream |
| [[obsidian-basename-collision\|Obsidian: wikilink ambíguo por basename igual em pastas diferentes]] | obsidian, wikilink, basename, colisao, shortest-link, vault |
| [[pep668-pip-externally-managed\|pip falha: externally-managed-environment (PEP 668)]] | pip, pep668, externally-managed, venv, wsl, debian |
| [[apirequest-fetch-vs-axios\|Cliente API fetch-style ignora data/params (axios)]] | apiRequest, fetch, axios, data, params, body, query-string |
| [[campaign-message-queue-waba-template\|Campanha não entrega template a contato frio (fila ignora WABA template)]] | campanha, message-queue, fan_out, _send_via_adapter, waba-template, cold-contact |
| [[celery-result-backend-memory-url\|Celery: ModuleNotFoundError No module named 'memory']] | celery, result-backend, memory, broker, cache+memory, settings-test |
| [[django-unique-soft-delete-base-manager\|Campo unique reusado após soft-delete (base_manager)]] | django, unique, soft-delete, duplicate-entry, 1062, sequence, base_manager |
| [[django-uuid-pk-vs-integerfield\|UUID PK + serializer IntegerField + Number() = links zerados]] | django, uuid, drf, serializer, IntegerField, UUIDField, NaN |
| [[meta-cloud-api-accepted-not-delivered\|Meta Cloud API: aceita (wamid) mas não entrega]] | meta, whatsapp, cloud-api, wamid, payment, allowlist, 24h-window, template |
| [[meta-webhook-setup-gotchas\|Meta WABA webhook + Embedded Signup: gotchas]] | meta, webhook, callback-url, append-slash, subscribed_apps, app-domains, config_id, js-sdk |
| [[phone-normalize-duplicate-contacts\|Telefone sem código de país duplica contato/sessão]] | telefone, normalize, e164, wa_id, country-code, find_or_create, phonenumbers |
| [[waba-number-platform-type-cloud-api\|WABA: número não envia (ON_PREMISE / SMB)]] | waba, whatsapp, cloud-api, on-premise, platform_type, 133010, coexistence, register |


| [[route-antes-de-editar-componente\|Modal/tela errada: trace rota antes de editar componente]] | rota, componente errado, modal, URL, route, debugging, App.jsx |
| [[pre-prod-staging-nao-e-main\|"Pre-prod" no MailerWeb = staging com branch deployado, não main]] | pre-prod, staging, main, branch, referência, comparação |
| [[committed-vs-working-tree\|Distinguir estado commitado vs working tree antes de diagnosticar]] | git diff, working tree, HEAD, imports quebrados, undefined |

Ver [[routing]] · [[_strategy]] · daily em `daily/`.
