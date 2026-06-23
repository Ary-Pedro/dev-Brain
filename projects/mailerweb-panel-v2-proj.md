---
type: project
project: mailerweb-panel-v2
scope: mailerweb
repo_path: ~/devSpace/mailerWeb/mailerweb.panel.v2
stack: [python, django, celery, react, mysql]
brain_policy: read-domain-from-mailerweb-brain
write_policy: dev-brain-only
domain_brain: mailerweb-brain
status: active
token_weight: crítico
token_policy: summary-first
graph_nodes: 20717
graph_edges: 38682
source: human+graphify
audience: ai
tags: [project, mailerweb]
---

# mailerweb-panel-v2 — CARD VIVO

> Camada operacional para o agente decidir **qual contexto abrir** antes de tocar o repo. Não é doc de arquitetura — para estrutura ver [[mailerweb-panel-v2]] (mapa) e [[mailerweb-panel-v2-grafo]].

<!-- @generated:start -->
## Objetivo

Painel multi-tenant da MailerWeb (SaaS de atendimento/WhatsApp), reescrita Django 5 autoritativa do legado `mailerweb.panel` (Django 1.11). Monolito SOA (Strangler Fig): camadas `services.py` → `clients/` → `EventBus`, sem JOIN/import cross-app de models, isolamento de tenant via `TenantBaseModel`. Backend Django 5 + DRF + Channels + Celery (MySQL/Redis); frontend React 19 + Vite + Tailwind 4. Tudo roda em Docker.

## Como consultar

Ordem de resolução para não abrir o repo às cegas:

1. **Domínio / regra de negócio / fluxo** → ponte `[[mailerweb-bridge]]` (aponta p/ vault `mailerweb-brain`, somente leitura).
2. **Padrão de engenharia** (estilo, testes, segurança, commits) → `know/` do dev-Brain ([[_principles]], [[code-style]], [[testing]], [[python-django]], [[typescript-next]]).
3. **Estrutura / onde algo vive / entrypoints** → [[mailerweb-panel-v2-grafo]] e o mapa [[mailerweb-panel-v2]].
4. **Relação entre símbolos / quem chama quem / impacto de mudança** → `graphify query` sobre o grafo (20717 nós / 38682 arestas).

## Peso p/ IA

`token_weight = crítico`. Regras duras:

- **NUNCA** abrir o repo inteiro nem ler diretórios em massa — estoura contexto sem retorno.
- **Exigir plano antes de editar**: dizer qual app/arquivo, qual camada (service/client/event), e por quê.
- **Usar digest + bridge primeiro**: resolver a dúvida pelo `mailerweb-panel-v2.digest.json` (god nodes + comunidades) e por `[[mailerweb-bridge]]` antes de tocar código.
- **God nodes** (alto fan-out — mudar = onda): `EventBus` (`apps/core/event_bus.py`), `Tenant` (`apps/tenants/models.py`), `TenantBaseModel` (`apps/core/models.py`), `Contact` (`apps/contacts/models.py`), `AutomationEngine` (`apps/automations/engine.py`), `User` (`apps/accounts/models/user.py`), `Instance` (`apps/messaging/models.py`), `TenantFactory()` (`apps/core/tests/factories.py`), frontend `api`/`index.js` (`frontend/src/services/api/`), `useToast()`, `useAuth()`.
- **Hubs por comunidade**: billing, integrations (Asaas/Kiwify/Hotmart adapters), affiliates, contacts (+CSV import), accounts, campaigns, igaming. Tocar um hub → checar dependentes via `graphify query` antes.
- **Domínio é só-leitura**: `mailerweb-brain` é git da empresa. Toda saída/anotação vai **só** em dev-Brain (`write_policy: dev-brain-only`). Em conflito de padrão, dev-Brain vence e aponta correção no domínio.

## Próxima ação

- Manter god nodes / comunidades sincronizados quando o grafo for re-gerado (graphify) — fonte: digest.
- Antes de qualquer task: rodar passo 1–4 de "Como consultar" e produzir plano explícito (app + camada + arquivo).
<!-- @generated:end -->

<!-- @user:start -->
(observações manuais do Pedro)
<!-- @user:end -->

---

Relacionados: [[mailerweb-panel-v2]] · [[mailerweb-panel-v2-grafo]] · [[mailerweb-bridge]] · [[routing]]
