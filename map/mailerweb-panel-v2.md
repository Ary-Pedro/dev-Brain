---
type: note
scope: mailerweb
repo_path: ~/devSpace/mailerWeb/mailerweb.panel.v2
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: active
confidence: high
last_verified: 2026-06-19
token_policy: summary-first
tags: [map, mailerweb, python-django, typescript-next]
---

# mailerweb.panel.v2 — MAPA

> Painel de controle multi-tenant da MailerWeb (SaaS de atendimento/WhatsApp).
> Caminho: `~/devSpace/mailerWeb/mailerweb.panel.v2`. Reescrita Django 5 do legado `mailerweb.panel` (Django 1.11) — esta versão é a autoritativa.

Pertence ao **universo MailerWeb**: domínio, fluxos e regras de negócio vivem no vault `mailerweb-brain`. Aqui o dev-Brain só aplica padrão de engenharia — ver [[routing]].

## Stack

- **Backend**: Django 5.1 + DRF 3.15 + Channels (ASGI/WebSocket) + Celery 5 + `django-celery-beat`. Python 3.12+. MySQL 8, Redis 7.
- **Settings**: `config/settings/{base,development,test,production}.py`, env via `python-decouple`. Default `config.settings.development`.
- **Auth**: `djangorestframework-simplejwt` (access+refresh) + OAuth/SAML por domínio para resellers.
- **Multi-tenant**: todo model de domínio herda `TenantBaseModel`; isolamento por middleware. Nunca escrever query que ignore o tenant.
- **AI/LLM**: `openai`, `anthropic`, `langchain`, `litellm`.
- **Frontend**: React 19 + Vite + Tailwind CSS 4 + `react-i18next` (pt-BR/en-US/es-ES). Editor visual `@craftjs/core`, `framer-motion`, `lucide-react`, Radix UI. Testes Vitest + Playwright.
- **Obs/Sec**: `structlog`, `sentry-sdk`, `django-encrypted-model-fields` (Fernet via `FIELD_ENCRYPTION_KEY`).
- **Qualidade**: `ruff`, `mypy` (+django/drf stubs), `import-linter` (contratos SOA), `mutmut` (mutation), cobertura `fail_under=70` (AGENTS.md exige 85% no módulo tocado).

## Estrutura

| Dir | Papel |
|-----|-------|
| `apps/` | 30 apps Django (core, tenants, accounts, messaging, message_queue, ai_engine, billing, campaigns, contacts, crm, webhooks, etc.). Cada app: `models/services/views/serializers/clients/tasks/tests`. |
| `config/` | Projeto Django: `settings/`, `urls.py`, `asgi.py`, `wsgi.py`, `celery.py`. |
| `frontend/` | App React 19 + Vite. Código em `frontend/src/`; design system, e2e (Playwright), i18n. |
| `deploy/` | Artefatos de deploy. |
| `scripts/` | Onboarding e auditorias (`onboarding.py`, `audit_cross_imports.py`, `verify_sprint.sh`). |
| `docs/` | Documentação (ex.: `waba-guia.md`). |
| `locale/` | Traduções Django. |
| `manage.py` | Entrypoint CLI (valida segredos de boot antes do Django). |

Manifestos: `pyproject.toml` (pkg `greenapi-saas`, deps + ruff/mypy/pytest/coverage), `requirements.txt`, `frontend/package.json` (`mailerweb-frontend`), `Dockerfile` / `Dockerfile.prod`, `docker-compose*.yml`.

## Entrypoints

- **CLI / admin**: `manage.py` → `config.settings.development`. Chama `enforce_bootstrap_secrets()` antes de carregar o Django.
- **WSGI**: `config/wsgi.py` (HTTP sync).
- **ASGI**: `config/asgi.py` (Channels, WebSocket em `/ws/`).
- **Celery**: `config/celery.py` (worker + beat, broker Redis).
- **API HTTP**: base `/api/v1/` (`config/urls.py`). Swagger em `/api/docs/`, `/api/docs/reseller/`, `/api/docs/internal/`.
- **Frontend**: `frontend/index.html` + Vite (`frontend/vite.config.js`).

## Como rodar (comandos)

Tudo roda **em Docker** (interpretador local proibido — AGENTS.md §1.8).

```bash
# Clone novo: usar o wizard (gera chaves reais, migrate + setup_system)
python3 scripts/onboarding.py

# Repo já configurado: subir a stack
docker compose up -d

# Django (web em :8000, db MySQL :3308, redis :6379, frontend Vite :3001)
docker compose exec -T web python manage.py check
docker compose exec -T web python manage.py migrate
docker compose exec -T web python manage.py shell

# Testes (stack dedicada docker-compose.test.yml — SQLite memória, Celery eager)
scripts/run_full_tests.sh --stop-dev
docker compose -f docker-compose.test.yml exec -T tests python manage.py test apps.<app>

# Lint / typing / arquitetura
docker compose exec -T web ruff check .
docker compose exec -T web mypy apps
docker compose exec -T web lint-imports

# Frontend (build DEVE passar antes de dar UI por concluída)
docker compose exec -T frontend npx vite build --mode development
docker compose exec -T frontend npx vitest run
docker compose exec -T frontend npm run lint
```

> Confira sempre `docker-compose.yml` / `.env` antes de assumir porta — o README é stale (AGENTS.md §1.10).

## Padrões aplicáveis

Governança universal de [[00-index]] / `know/`:

- [[_principles]] — pensar antes de codar
- [[code-style]] · [[naming]] · [[docstrings]] · [[comments]]
- [[testing]] · [[error-handling]] · [[security]] · [[performance]] · [[git-commits]]

Por stack:

- Backend → [[python-django]]
- Frontend → [[typescript-next]]

Regras locais fortes (no `CLAUDE.md`/`AGENTS.md` do projeto, não duplicar): monolito SOA (Strangler Fig) com camadas `services.py` → `clients/` → `EventBus`, sem JOIN/import cross-app de models; isolamento de tenant; isolamento de addon (modelos separados via `OneToOneField`); TDD red→green→refactor; commits Convencionais em PT-BR, comentários em inglês; i18n obrigatório (3 idiomas simultâneos). Em conflito de padrão, **dev-Brain vence** e aponta correção no domínio.

## Roteamento

Projeto do **universo MailerWeb**. O dev-Brain aplica apenas padrão de engenharia (`know/` + notas de stack). Domínio, apps, fluxos e regras de negócio **não são duplicados aqui** — vivem no vault `mailerweb-brain` (e narrativa/intenção em `wiks/`). Decisão de qual brain consultar: [[routing]]. Voltar ao índice: [[00-index]].
