---
type: note
scope: mailerweb
repo_path: /home/pedroczar/devSpace/mailerWeb/theds_panel
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: active
confidence: high
last_verified: 2026-06-19
token_policy: summary-first
tags: [map, mailerweb, python-django]
---

# theds_panel

`/home/pedroczar/devSpace/mailerWeb/theds_panel` **não é um projeto** — é uma pasta-guarda-chuva com três checkouts paralelos do painel MailerWeb (provavelmente worktrees/clones de sessão "theds"). Não trate a raiz como repo: cada subpasta tem seu próprio `.git`, stack e regras.

| Checkout | Projeto interno | Stack | Status |
|----------|-----------------|-------|--------|
| `theds01/mailerweb.panel.v2` | painel v2 | Django 5.1 + React 19 | rewrite atual |
| `theds3/mailerweb.panel.v2`  | painel v2 | Django 5.1 + React 19 | rewrite atual (clone mais recente) |
| `theds02/mailerweb.panel`    | painel v1 | **Django 1.11 + Python 2.7** | **LEGADO** — referência apenas |

Regra de ouro: **quando v1 e v2 conflitam, v2 vence.** Qualquer doc que descreva o Django 1.11 está obsoleto. Trabalho novo entra no `mailerweb.panel.v2`.

## Stack

**v2 (`theds01` / `theds3` — autoritativo):**
- Backend: Django 5.1 + DRF + Channels (ASGI) + Celery 5 + MySQL 8 + Redis 7, Python 3.12+. Settings em `config/settings/{base,development,test,production}.py`, env via `python-decouple`.
- Frontend: React 19 + Vite + Tailwind CSS 4 + `react-i18next` (i18n obrigatório em 3 locales: pt-BR/en-US/es-ES). Em `frontend/`.
- Auth: `simplejwt` + OAuth/SAML por domínio (resellers). Multi-tenant via `TenantBaseModel` + middleware.
- Async/realtime: Celery worker + celery-beat (`DatabaseScheduler`), broker Redis; Channels em `/ws/`.

**v1 (`theds02` — legado):** Django 1.11.29, Celery 4.4, Python 2.7, MySQL + MongoDB (`mongoengine`/`tastypie`) + RabbitMQ broker. Não modernizar — só consultar.

## Estrutura

Dirs-chave do **v2** (idênticos em `theds01` e `theds3`):

| Dir / arquivo | Papel |
|---------------|-------|
| `apps/` | 30 Django apps (SOA monolith): `core`, `tenants`, `accounts`, `api`, `infrastructure`, `messaging`, `message_queue`, `campaigns`, `billing`, `crm`, `ai_engine`, `webhooks`, etc. |
| `config/` | `settings/`, `urls.py`, `asgi.py`, `wsgi.py`, `celery.py` |
| `frontend/` | app Vite/React 19 (`src/`, `design-system/`, `e2e/`, `package.json`, `vite.config.js`) |
| `manage.py` | entrypoint Django |
| `pyproject.toml` / `pytest.ini` / `conftest.py` | tooling Python: ruff, mypy, pytest (`fail_under=70`, AGENTS pede 85% no módulo tocado) |
| `importlinter.ini` | contratos SOA — `lint-imports` falha se cruzar fronteiras |
| `docker-compose.yml` + `.docker/` + `Dockerfile{,.prod}` | runtime obrigatório (interpretador local proibido) |
| `scripts/` | `onboarding.py` (wizard), `audit_cross_imports.py`, `verify_sprint.sh` |
| `deploy/` + `.gitlab-ci.yml` | CI/CD GitLab |
| `CLAUDE.md` / `AGENTS.md` / `README.md` | regras de engenharia do repo |

Legado `theds02` usa layout próprio: código em `src/`, lib custom em `core/`, `fabfile.py`, `supervisor-conf/`, `celery.conf`.

## Entrypoints

- **Backend (v2):** `manage.py` → Django; `config/wsgi.py` / `config/asgi.py`; `config/celery.py` (workers/beat); API em `/api/v1/`, WS em `/ws/`.
- **Frontend (v2):** `frontend/index.html` + `frontend/src/` via Vite (`npm run dev`).
- **Legado (v1):** `manage.py` (Django 1.11), `fabfile.py`, configs em `supervisor-conf/` + `celery.conf`.

## Como rodar

Tudo em Docker — interpretador local é **proibido** (AGENTS §1.8). Comandos abaixo no v2:

```bash
# subir stack (repo já bootstrapado)
docker compose up -d

# clone novo: NÃO rode up direto (placeholders de .env.example quebram o web)
python3 scripts/onboarding.py        # gera SECRET_KEY/FIELD_ENCRYPTION_KEY, migrate, setup_system

# Django
docker compose exec -T web python manage.py {check,migrate,makemigrations,shell}

# testes
docker compose exec -T web python manage.py test --settings=config.settings.test
docker compose exec -T web pytest apps/<app>/tests/test_x.py::test_name
./run_all_tests.sh

# qualidade
docker compose exec -T web ruff check .
docker compose exec -T web mypy apps
docker compose exec -T web lint-imports          # fronteiras SOA

# frontend (DEVE passar antes de declarar UI pronta)
docker compose exec -T frontend npx vite build --mode development
docker compose exec -T frontend npx vitest run --reporter=verbose
docker compose exec -T frontend npm run lint
```

Portas reais (do `docker-compose.yml`, README é stale): db MySQL **3308**, redis **6379**, web Django **8000** (`/api/v1/`, `/api/docs/`), frontend Vite **3001**, smtp-proxy **587**.

## Padrões aplicáveis

Projeto Python/Django + frontend TS/React. Aplicar os padrões do vault:

- [[python-django]] — backend (não existe ainda em `know/`; criar quando for o caso)
- [[typescript-next]] — referência de frontend TS/React (idem)
- [[code-style]] · [[testing]] · [[naming]] · [[comments]] · [[docstrings]]
- [[error-handling]] · [[security]] · [[performance]] · [[git-commits]]
- [[_principles]]

Convenções fortes deste repo (alinham com o vault): commits Conventional **em PT-BR**, comentários de código **em inglês**, TDD red→green→refactor não-opcional, sem stubs/`TODO`, i18n com edição simultânea dos 3 locales.

## Roteamento

Este projeto é do **UNIVERSO MailerWeb**. Domínio, fluxos de negócio, regras de multi-tenancy, catálogo de eventos do EventBus e arquitetura específica das apps **vivem no vault `mailerweb-brain`** — NÃO duplicar aqui. O dev-Brain só aplica padrão de engenharia transversal (estilo, testes, segurança, etc.).

- Detalhes de domínio/arquitetura → `mailerweb-brain` (`arquitetura.md`, `apps/<app>.md`, `patterns.md`, `eventos/catalogo-de-eventos.md`, `security.md`, `commands.md`).
- Padrão de engenharia → este vault. Ver [[routing]].

[[00-index]]
