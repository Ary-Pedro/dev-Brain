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
tags: [lesson, frontend, react, api-client]
keywords: [apiRequest, fetch, axios, data, params, body, json-stringify, query-string, instance_id-required, empty-body]
aliases: [apirequest-fetch-vs-axios]
---

# Cliente API fetch-style ignora `data`/`params` (estilo axios)

**Contexto:** chamada à API do front "some" no backend — body vazio ou filtro ignorado.
**Sintoma:** backend responde `... is required` (campo do body ausente) ou lista retorna sem filtrar, mesmo passando `{ data: {...} }` / `{ params: {...} }`.
**Causa:** o helper `apiRequest(endpoint, options)` repassa `options` direto pro `fetch` — só lê `options.body` e a URL. `data`/`params` (convenção axios) são **ignorados** por `fetch`.
**Solução:** POST → `apiRequest(url, { method:'POST', body: JSON.stringify(payload) })`; GET filtro → `apiRequest('/x/?' + new URLSearchParams(params))`. (Ou usar os helpers de conveniência `api.post(url,data)` que já fazem `JSON.stringify`.)
**Evitar futuro:** ao escrever um módulo de API novo, copie o contrato do `client.js` (fetch: `body`+URL), não presuma axios.
**Relacionado:** [[typescript-next]] · [[code-style]] (copiar contrato do client existente).

**Visto em:** [[daily/2026-06-19]]
