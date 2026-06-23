---
type: project
project: theds-panel
repo_path: ~/devSpace/mailerWeb/theds_panel
scope: mailerweb
stack: [python, django, react, celery, mysql, redis]
brain_policy: read-domain-from-mailerweb-brain
write_policy: dev-brain-only
domain_brain: mailerweb-brain
status: active
token_weight: crítico
graph_nodes: 0
graph_edges: 0
source: human
audience: ai
confidence: med
last_verified: 2026-06-19
token_policy: summary-first
tags: [project, mailerweb, python-django]
---

# theds-panel — card vivo

> Camada operacional p/ o agente decidir contexto antes de codar. Não é doc humana — é onde a IA descobre o que abrir e como rotear. Estrutura detalhada no mapa [[theds-panel]]; grafo de código → use o de [[mailerweb-panel-v2-grafo]] (mesma base v2).

<!-- @generated:start -->
## Objetivo

**Workspace de trabalho multitarefa no universo MailerWeb**, não um repo único. `~/devSpace/mailerWeb/theds_panel` é guarda-chuva com 3 checkouts paralelos do painel (sessões "theds"): `theds01/` e `theds3/` = `mailerweb.panel.v2` (Django 5.1 + React 19, **autoritativo**); `theds02/` = `mailerweb.panel` v1 (Django 1.11 / Py2.7, **legado — só referência**). Uso típico: abrir 2-3 chats em paralelo, resolver uma problemática focada, revisar um MR. **Regra de ouro: v2 vence v1.**

## Como consultar

1. **Domínio** (regra de negócio, fluxo, multi-tenancy, EventBus) → **mailerweb-brain via [[mailerweb-bridge]]** (read-only). NÃO varrer o monolito nem duplicar domínio aqui.
2. **Padrão** (engenharia: estilo, naming, erros, segurança, testes) → `know/`. Por stack: [[python-django]] (backend) · [[typescript-next]] (frontend TS/React).
3. **Estrutura / onde mora algo** → mapa [[theds-panel]].
4. **Relação / impacto** (quem chama quem, god nodes) → `graphify query` no grafo [[mailerweb-panel-v2-grafo]] (o código v2 é o mesmo de [[mailerweb-panel-v2]]).

## Peso p/ IA

`token_weight=crítico` → os checkouts v2 SÃO o codebase de [[mailerweb-panel-v2]] (~20.7k nós). **NUNCA abrir repo inteiro nem `graph.json` cru.** Exigir plano (via [[context-economist]]) antes de leitura pesada: domínio no bridge → digest `graph/mailerweb-panel-v2.digest.json` → `graphify query` dirigida → arquivo único só após identificar candidato. Foco da sessão é pequeno; o codebase não é.

## Próxima ação

Ao abrir tarefa: confirmar QUAL checkout (theds01/theds3 = v2 atual; theds02 = legado, não modernizar) e ler o `CLAUDE.md`/`AGENTS.md` do checkout (Docker obrigatório, interpretador local proibido, TDD red→green→refactor, commits Conventional em PT-BR, comentários em inglês, i18n nos 3 locales). Convenções fortes alinham com o vault.
<!-- @generated:end -->

<!-- @user:start -->
(observações manuais do Pedro)
<!-- @user:end -->

---
Relacionados: [[theds-panel]] (mapa) · [[mailerweb-panel-v2]] (mesmo código v2) · [[mailerweb-bridge]] · [[context-economist]] · [[routing]].
