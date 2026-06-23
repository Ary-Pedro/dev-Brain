---
type: note
scope: mailerweb
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

# mailerweb-portal

Site público da MailerWeb: landing page de marketing, blog, central de ajuda e páginas de produto. Projeto **separado** do painel (`mailerweb.panel.v2`) — codebase, deploy e banco distintos. Construído sobre **django CMS 4**, deploy em **AWS Lambda via SAM**.

> Esta nota é um MAPA de engenharia (dev-Brain): stack, estrutura e como rodar. Regras de domínio/negócio do produto pertencem ao vault `mailerweb-brain` — ver [[#Roteamento]].

## Stack

- **Linguagem:** Python 3 · **Framework:** Django 5.2.3 + **django CMS 5.0.1** (CMS 4 line)
- **DB:** MySQL 8.0 (`mysqlclient`) — dev via docker-compose, prod gerenciado
- **CMS stack:** `djangocms-versioning`, `djangocms-alias`, `djangocms-frontend`, `djangocms-text`, `djangocms-link`, `django-filer`, `django-parler` (i18n), `django-cms-blog` (fork interno via tarball do GitHub)
- **Servidor:** `gunicorn` (prod) · `whitenoise` (estáticos) · `django-storages[s3]` (mídia em S3)
- **Integrações:** Pipedrive (`portal/pipedrive_service.py`), gatekeeper de onboarding (`portal/gatekeeper_service.py`)
- **Observabilidade:** `sentry-sdk[django]`
- **Testes:** `pytest` + `pytest-django`, `Faker`
- **Deploy/infra:** AWS SAM (`template.yaml`, `samconfig.toml`), Docker, GitLab CI (`.gitlab-ci.yml`)

Manifesto-fonte: `requirements.txt` (sem pyproject/poetry; pip flat-pinned).

## Estrutura

| Diretório | Papel |
|-----------|-------|
| `portal/` | App núcleo: views (`views.py`, 42KB), forms, `urls.py`, settings, serviços (Pipedrive, gatekeeper), middleware, sitemaps, templates |
| `portal/settings/` | Settings por ambiente: `base.py`, `local.py`, `staging.py`, `production.py`, `amazon.py`, `storages.py` |
| `blog/` | App de blog (models/views/urls + templates) |
| `helpcenter/` | Central de ajuda (`/ajuda/`) |
| `landing_page/` | Landing pages com plugins CMS (`cms_plugins.py`) |
| `products/` | Páginas de produto + integração CMS (`cms_app.py`, `cms_plugins.py`, `tasks.py`) |
| `configuration/` | Configuração global do site (models, admin, management commands, `tasks.py`) |
| `tests/` | Suíte separada da raiz: `unit/`, `integration/`, `end2end/` |
| `configuration/` + apps | Cada app tem `migrations/`, `templates/`, `static/` conforme necessário |

Raiz contém: `manage.py`, `Dockerfile.{local,prod,stag}`, `docker-compose.yml`, `deploy.sh`, `template.yaml`, `samconfig.toml`, `.env.example`.

## Entrypoints

- **WSGI:** `portal/wsgi.py` · **ASGI:** `portal/asgi.py`
- **CLI:** `manage.py` → `DJANGO_SETTINGS_MODULE=portal.settings` (default; sobrescrito por ambiente)
- **Roteamento HTTP:** `portal/urls.py` — inclui `cms.urls` no final (catch-all do CMS), `admin/`, `filer/`, `blog/`, `ajuda/` (helpcenter), `lp` (landing_page), `taggit_autosuggest/`, `sitemap.xml`, `robots.txt`, `health`, `sentry-debug/`. Rotas de negócio em PT-BR (`/planos`, `/cadastro`, `/pagamento`, `/registro`, `/fale-com-vendas`...).
- **Health check:** `GET /health` (`HealthView`)

## Como rodar

```bash
# Dev local (Docker — recomendado): sobe MySQL 8 + app em :8002
docker-compose up
# DJANGO_SETTINGS_MODULE=portal.settings.local, debugpy em :5678 se DEBUG_MODE=True

# Dev local (sem Docker)
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
./manage.py runserver            # usa portal.settings (default)

# Testes (pytest, como na CI)
pytest --maxfail=1
pytest --maxfail=1 --disable-warnings -q

# Estáticos por ambiente
python manage.py collectstatic --noinput --settings=portal.settings.<staging|production>
```

**Deploy (CI/CD):** stages `tests → build → {staging,production}_deploy` no `.gitlab-ci.yml`, via `sam deploy`. Fallback manual (`README.md`): `./deploy.sh` (build + push imagem ECR) → sincronizar `COMMIT_HASH` em `ImageTag` no `samconfig.toml` → `sam deploy --config-env <env>` → `collectstatic`.

## Padrões aplicáveis

Projeto Python/Django — aplicar as notas de `know/` por stack:

- [[python-django]] — convenções de framework (se a nota existir; senão usar padrões Django gerais)
- [[code-style]] · [[naming]] · [[comments]] · [[docstrings]]
- [[testing]] — suíte `pytest`/`pytest-django`; espelhar layout `tests/{unit,integration,end2end}`
- [[error-handling]] · [[security]] (atenção a chaves de integração Pipedrive/gatekeeper e settings por ambiente)
- [[performance]] · [[git-commits]] · [[_principles]]

## Roteamento

Este projeto pertence ao **UNIVERSO MailerWeb**. Regras de domínio, fluxos de negócio (onboarding/gatekeeper, planos, cadastro, integração Pipedrive) e decisões de produto ficam no vault **`mailerweb-brain`** — **NÃO duplicar aqui**. O dev-Brain só registra o padrão de engenharia transversal.

Ver [[routing]] para o mapa de qual vault responde a quê. Voltar ao índice: [[00-index]].
