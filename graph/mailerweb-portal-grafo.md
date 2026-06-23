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
tags: [graph, code, mailerweb-portal]
aliases: [mailerweb-portal-graph]
---

# mailerweb-portal — grafo de código

> Estrutura real do código (graphify, AST). **831 nós · 1731 arestas · 95 módulos**.
> Mapa do projeto: [[mailerweb-portal]] · relatório bruto: `graph/mailerweb-portal/GRAPH_REPORT.md` · grafo: `graph/mailerweb-portal/graph.json`.

## Módulos (comunidades, nomeadas pela pasta dominante)

| Módulo | Nós | Pastas | Exemplos |
|--------|-----|--------|----------|
| **portal** | 91 | portal (84), (raiz) (3), landing_page (2) | `views.py`, `PreSignUpForm`, `PipedriveSender`, `GatekeeperService` |
| **portal** | 55 | portal (34), tests (21) | `.get()`, `validate_form_generic()`, `services.py`, `test_validate_form_generic.py` |
| **portal** | 53 | portal (53) | `$()`, `ee()`, `V()`, `I()` |
| **helpcenter** | 40 | helpcenter (22), portal (15), (raiz) (3) | `HelpPost`, `HelpCategory`, `sitemaps.py`, `views.py` |
| **landing_page** | 36 | landing_page (25), products (8), (raiz) (2) | `views.py`, `BaseLandingPagePlansView`, `BaseLandingPageView`, `.process_lead()` |
| **portal** | 31 | portal (31) | `SignupForm`, `._only_digits()`, `.clean_cnpj()`, `.clean_phone()` |
| **.gitlab-ci.yml** | 31 | .gitlab-ci.yml (17), README.md (6), deploy.sh (5) | `Manual deploy fallback procedure`, `deploy.sh (manual ECR image deployer)`, `Job: build_staging (docker build/push ECR)`, `Job: build_production (docker build/push ECR)` |
| **products** | 24 | products (24) | `.handle()`, `Command`, `._sync_prices()`, `upsert_category()` |
| **tests** | 24 | tests (24) | `_base_pf_data()`, `TestCleanPersonName`, `.test_valid_full_name()`, `.test_empty_name_rejected()` |
| **configuration** | 23 | configuration (13), portal (5), products (4) | `get_plans_price.py`, `tasks.py`, `get_objects()`, `tasks.py` |
| **portal** | 23 | portal (23) | `utils.py`, `check_exists()`, `create_object()`, `.clean_username()` |
| **products** | 22 | products (21), (raiz) (1) | `admin.py`, `forms.py`, `ProductPrice`, `ProductResource` |
| **portal** | 21 | portal (10), tests (10), (raiz) (1) | `test_gatekeeper_onboarding.py`, `GatekeeperOnboardingError`, `gatekeeper_service.py`, `.build_portal_signup_onboarding_payload()` |
| **portal** | 21 | portal (21) | `payment.js`, `toggleLoading()`, `handleRegisterPaymentMethod()`, `requestByPaymentMethod()` |
| **products** | 21 | products (20), (raiz) (1) | `Product`, `Category`, `views.py`, `.save()` |

## Hubs (god nodes — maior conectividade)

| Símbolo | Grau | Arquivo |
|---------|------|---------|
| `SignupForm` | 102 | `portal/forms.py` |
| `views.py` | 68 | `portal/views.py` |
| `$()` | 57 | `portal/static/js/jquery-3.7.1.min.js` |
| `PreSignUpForm` | 51 | `portal/forms.py` |
| `PipedriveSender` | 50 | `portal/pipedrive_service.py` |
| `GatekeeperService` | 44 | `portal/gatekeeper_service.py` |
| `NazgulService` | 41 | `portal/services.py` |
| `PipedriveClient` | 37 | `portal/pipedrive_service.py` |
| `utils.py` | 36 | `portal/utils.py` |
| `urls.py` | 35 | `portal/urls.py` |
| `_base_pf_data()` | 34 | `tests/unit/test_signup_form_validation.py` |
| `MixFreeEmailForm` | 33 | `portal/forms.py` |

> Hub com grau muito alto + nome genérico = candidato a quebrar em peças menores (ver [[_strategy]]).

<!-- @user:start -->
## 🧠 Leitura arquitetural

Os módulos dominantes confirmam um monolito Django CMS centrado no app `portal/`: sete das quinze maiores comunidades têm `portal` como pasta principal, e as três primeiras (94, 70, 56 nós) giram em torno de `views.py`, `forms.py` e `services.py`. Não há separação clara de bounded contexts — `portal` absorve cadastro/signup, integração Pipedrive (`pipedrive_service.py`), onboarding (`gatekeeper_service.py`), serviços de domínio (`NazgulService` em `services.py`) e até assets estáticos (a comunidade de 53 nós é só o `jquery-3.7.1.min.js` poluindo o grafo). Os apps satélite — `helpcenter/`, `landing_page/`, `products/`, `blog/` — formam comunidades coesas e bem delimitadas, o que é saudável; o problema de concentração está no núcleo, não nas bordas.

Entre os hubs de maior grau, há dois perfis distintos. `SignupForm` (grau 102), `PreSignUpForm` (51), `MixFreeEmailForm`/`ReportAbuseForm`/`SupportForm`/`PaymentForm`/`RCSStartForm` — todos em `portal/forms.py` — são god-objects a quebrar: um único módulo de forms concentra a maior densidade de conexões do projeto inteiro. `SignupForm` com grau 102 sozinho, somado aos métodos de validação (`.clean_cnpj()`, `.clean_phone()`, `.clean_cpf()` na comunidade de 31 nós), sinaliza que regras de validação de PF/PJ deveriam virar validators/serviços reutilizáveis fora da classe Form. Já `views.py` (68) e `urls.py` (35) têm grau alto por natureza de roteador Django — coesão esperada, não patologia, embora `views.py` com 42KB mereça split por feature.

Os serviços de integração — `PipedriveSender` (50), `GatekeeperService` (44), `NazgulService` (41), `PipedriveClient` (37) — são pontos de acoplamento externo concentrados em poucos arquivos. Isso é, na verdade, um padrão correto (anti-corruption layer isolando APIs de terceiros), mas o grau elevado indica que muitas views chamam esses serviços diretamente. O risco real está na fronteira `forms.py` ↔ `services.py` ↔ `pipedrive_service.py`/`gatekeeper_service.py`: o fluxo de signup atravessa todas elas, e a comunidade de testes de onboarding (20 nós: `test_gatekeeper_onboarding.py`, `.sync_portal_signup()`) confirma que esse é o caminho crítico de negócio.

Ações concretas:
- **Quebrar `portal/forms.py`**: extrair as validações de `SignupForm`/`PreSignUpForm` (CNPJ/CPF/telefone/CEP) em validators ou um service de validação, e separar os forms por feature (signup, payment, support, RCS). Aplicar [[python-django]] (forms/validators) e [[code-style]].
- **Aliviar `portal/views.py` (42KB, grau 68)**: dividir em módulos por área (signup, pagamento, vendas) e manter as chamadas a `PipedriveSender`/`GatekeeperService` atrás de uma camada de serviço fina, reduzindo o acoplamento direto view→integração. Ver [[performance]] (custo de imports/carga do módulo) e [[python-django]].
<!-- @user:end -->

Ver [[00-graph-index]] · padrões em [[routing]].