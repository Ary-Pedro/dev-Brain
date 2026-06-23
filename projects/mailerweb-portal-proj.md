---
type: project
project: mailerweb-portal
scope: mailerweb
repo_path: ~/devSpace/mailerWeb/mailerweb-portal
stack: [python, django-cms, mysql]
brain_policy: read-domain-from-mailerweb-brain
write_policy: dev-brain-only
domain_brain: mailerweb-brain
status: active
token_weight: médio
token_policy: summary-first
graph_nodes: 799
graph_edges: 1691
source: human+graphify
audience: ai
tags: [project, mailerweb]
---

# mailerweb-portal (card vivo)

<!-- @generated:start -->
## Objetivo

Site público da MailerWeb (landing/marketing, blog, central de ajuda `/ajuda/`, páginas de produto, fluxos de cadastro/pagamento/planos). Projeto **separado** do painel (`mailerweb.panel.v2`) — codebase, deploy e DB distintos. Stack: **Django 5.2 + django CMS 5 (linha CMS 4)** sobre **MySQL 8**, deploy **AWS Lambda via SAM**.

Núcleo: app `portal/` (views 42KB, forms com ~7 god-forms, serviços de integração). Integrações-chave: **Pipedrive** (`pipedrive_service.py`), **Gatekeeper** de onboarding (`gatekeeper_service.py`), **Nazgul** (`services.py`).

## Como consultar

1. **Domínio/negócio** (onboarding, gatekeeper, planos, regras Pipedrive, decisões de produto) → ponte [[mailerweb-bridge]] → vault **mailerweb-brain** (SOMENTE LEITURA). NÃO duplicar regra de negócio aqui.
2. **Padrão de engenharia** (style, naming, testing, security, error-handling) → `know/` por stack: [[python-django]] · [[testing]] · [[security]] · [[error-handling]] · [[_principles]].
3. **Estrutura/stack/como rodar** → mapa [[mailerweb-portal-grafo]] (camada de mapa em `map/`).
4. **Relação entre arquivos/símbolos** (quem chama quem, god nodes, comunidades) → `graphify query` sobre o grafo (799 nós / 1691 arestas / 94 comunidades).

## Peso p/ IA (token_weight=médio)

Médio → **não** carregar codebase inteiro. Fluxo: ler **digest** (`graph/mailerweb-portal.digest.json`) para mapa mental, depois **`graphify query`** para alvos específicos. God nodes prováveis pontos de entrada: `SignupForm` (deg 102, `portal/forms.py`), `views.py` (deg 68), `PreSignUpForm` (51), `PipedriveSender` (50), `GatekeeperService` (44), `NazgulService` (41), `PipedriveClient` (37). Comunidades-âncora: `portal` (cadastro/forms/serviços), `helpcenter`, `landing_page`, `products`, `blog`, `tests/{unit,integration,end2end}`.

## Próxima ação

- Confirmar existência da nota de mapa [[mailerweb-portal-grafo]] em `map/` (atual: `map/mailerweb-portal.md`) e alinhar o wikilink.
- Validar a ponte de domínio [[mailerweb-bridge]] → mailerweb-brain (read-only) antes de responder qualquer questão de negócio.
- Ao tocar fluxo de cadastro/pagamento: entrar por `portal/forms.py` (SignupForm) e `portal/views.py`, espelhar testes em `tests/unit`.
<!-- @generated:end -->

<!-- @user:start -->
(observações manuais do Pedro)
<!-- @user:end -->

---
Ver também: [[mailerweb-portal-grafo]] · [[routing]] · [[mailerweb-bridge]]
