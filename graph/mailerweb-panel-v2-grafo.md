---
type: note
scope: mailerweb
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: graphify
status: active
confidence: high
last_verified: 2026-06-19
token_policy: summary-first
tags: [graph, code, mailerweb-panel-v2]
aliases: [mailerweb-panel-v2-graph]
---

# mailerweb-panel-v2 — grafo de código

> Estrutura real do código (graphify, AST). **20746 nós · 38750 arestas · 1095 módulos**.
> Mapa do projeto: [[mailerweb-panel-v2]] · relatório bruto: `graph/mailerweb-panel-v2/GRAPH_REPORT.md` · grafo: `graph/mailerweb-panel-v2/graph.json`.

## Módulos (comunidades, nomeadas pela pasta dominante)

| Módulo | Nós | Pastas | Exemplos |
|--------|-----|--------|----------|
| **apps/campaigns** | 380 | apps/campaigns (196), apps/metrics (38), apps/message_queue (31) | `TenantFactory()`, `AdminUserFactory()`, `Campaign`, `CampaignContact` |
| **apps/contacts** | 354 | apps/contacts (69), apps/chat (53), apps/tenants (32) | `Tenant`, `Contact`, `User`, `Instance` |
| **frontend** | 307 | frontend (307) | `useToast()`, `ToastProvider.jsx`, `useConfirm()`, `ConfirmDialog.jsx` |
| **apps/billing** | 301 | apps/billing (159), apps/core (49), apps/webhooks (47) | `TenantsClient`, `IsPlatformAdmin`, `MessagingClient`, `AsaasAdapter` |
| **apps/affiliates** | 242 | apps/affiliates (242) | `Affiliate`, `AffiliateProgram`, `Referral`, `Commission` |
| **apps/contacts** | 224 | apps/contacts (117), apps/igaming (22), apps/tenants (13) | `APITestCase`, `ContactViewSetMixin`, `ImportExecuteActionTest`, `TestCampaignReport` |
| **frontend** | 218 | frontend (218) | `api`, `client.js`, `CampaignWizard.jsx`, `campaigns.js` |
| **apps/metrics** | 206 | apps/metrics (95), apps/accounts (70), apps/community (15) | `urls.py`, `APIView`, `views.py`, `UnsubscribeService` |
| **apps/accounts** | 186 | apps/accounts (41), apps/core (38), apps/message_queue (30) | `UserFactory()`, `TestUserAPI`, `test_billing_settings_api.py`, `TestTransactionAPI` |
| **apps/resellers** | 177 | apps/resellers (171), apps/billing (2), apps/core (2) | `Reseller`, `__init__.py`, `tenant_management_service.py`, `config_gateway_service.py` |
| **apps/billing** | 174 | apps/billing (132), apps/metrics (11), apps/contacts (8) | `Plan`, `Subscription`, `models.py`, `serializers.py` |
| **frontend** | 151 | frontend (151) | `index.js`, `admin.js`, `adminApi`, `instancesApi` |
| **apps/core** | 149 | apps/core (43), apps/messaging (34), apps/contacts (17) | `EventBus`, `models.py`, `events.py`, `InstanceViewSetTestCase` |
| **apps/core** | 147 | apps/core (45), apps/automations (35), apps/chat (29) | `BaseModel`, `admin.py`, `sanitize_json_metadata()`, `models.py` |
| **frontend** | 137 | frontend (137) | `useAuth()`, `AuthContext.jsx`, `SessionsPage.jsx`, `AutomationBuilderPage.jsx` |

## Hubs (god nodes — maior conectividade)

| Símbolo | Grau | Arquivo |
|---------|------|---------|
| `TestCase` | 540 | `` |
| `TenantFactory()` | 418 | `apps/core/tests/factories.py` |
| `index.js` | 361 | `frontend/src/services/api/index.js` |
| `EventBus` | 330 | `apps/core/event_bus.py` |
| `Tenant` | 270 | `apps/tenants/models.py` |
| `AutomationEngine` | 197 | `apps/automations/engine.py` |
| `Contact` | 194 | `apps/contacts/models.py` |
| `useToast()` | 188 | `frontend/src/components/ui/ToastProvider.jsx` |
| `UserFactory()` | 167 | `apps/core/tests/factories.py` |
| `TenantsClient` | 151 | `apps/webhooks/clients/tenants.py` |
| `User` | 143 | `apps/accounts/models/user.py` |
| `TenantBaseModel` | 141 | `apps/core/models.py` |

> Hub com grau muito alto + nome genérico = candidato a quebrar em peças menores (ver [[_strategy]]).

<!-- @user:start -->
## 🧠 Leitura arquitetural

Os módulos dominantes confirmam o desenho **SOA-monolito** que o mapa promete, e mostram onde ele vaza. Os dois maiores módulos não são apps puros: `apps/billing` (341 nós) arrasta `apps/core`, `apps/webhooks` e `apps/campaigns` junto, e `apps/integrations` (323) mistura `apps/metrics` (94!) e `apps/accounts` (43). Isso é o efeito esperado da camada `clients/` — `MessagingClient`, `ContactsClient`, `TenantsClient`, `BillingClient` aparecem como pontes entre apps — mas a presença de `AsaasAdapter` simultaneamente em billing **e** integrations sugere adaptador de pagamento (Asaas/Kiwify/Hotmart) sem dono claro de fronteira. O frontend se fragmenta em quatro comunidades coerentes por feature (design-system `ToastProvider`/`Modal`, wizard de campanhas, auth/sessões, services/api), o que é saudável.

Sobre os hubs de maior grau: a maioria é **coesão saudável, não god-object**. `TestCase` (538) e `APITestCase` (107) são ruído de teste; `TenantFactory()` (416) e `UserFactory()` (167) são fixtures centrais — alto grau é natural e desejável. `EventBus` (330, `apps/core/event_bus.py`) é o ponto de desacoplamento por design do Strangler Fig — grau alto aqui é o objetivo, não o problema. `Tenant` (270) e `TenantBaseModel` (141) são a espinha multi-tenant; idem. Os candidatos reais a vigiar são **`apps/automations/engine.py::AutomationEngine`** (197) e **`frontend/src/services/api/index.js`** (361, reexport barrel) — grau alto + responsabilidade concentrada.

- **`AutomationEngine` (grau 197)** é o god-object mais provável: motor de regras costuma acumular parsing, avaliação de condições, execução de ações e agendamento. Vale fatiar em executor + registry de ações + avaliador de condições. Ver [[python-django]] (services finos) e [[performance]] (motor no hot-path de envio).
- **`frontend/src/services/api/index.js` (grau 361)** é barrel de reexport: grau inflado artificialmente, baixo risco semântico, mas vira gargalo de bundle/HMR. Considerar imports diretos por domínio. Ver [[typescript-next]].
- **Risco de acoplamento**: `apps/metrics` está espalhado entre integrations, billing e campaigns (94+16+16 nós) sem módulo próprio dominante — sintoma de leitura cross-app de métricas. Auditar com `scripts/audit_cross_imports.py` / `lint-imports` e garantir que métricas fluam via `EventBus`, não por import direto. Ver [[code-style]] e regra SOA local (sem import cross-app de models).
- **`apps/igaming`** já nasce acoplado a `core`, `message_queue`, `messaging` e `ai_engine` via `IGamingEventService` — confirmar que toda integração é por evento (`events.py`/`EventBus`), não JOIN.
<!-- @user:end -->

Ver [[00-graph-index]] · padrões em [[routing]].