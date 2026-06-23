# Graph Report - .  (2026-06-19)

## Corpus Check
- 230 files · ~486,830 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 831 nodes · 1731 edges · 95 communities (67 shown, 28 thin omitted)
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 384 edges (avg confidence: 0.53)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 86|Community 86]]

## God Nodes (most connected - your core abstractions)
1. `SignupForm` - 102 edges
2. `$()` - 57 edges
3. `PreSignUpForm` - 51 edges
4. `PipedriveSender` - 50 edges
5. `GatekeeperService` - 44 edges
6. `NazgulService` - 41 edges
7. `PipedriveClient` - 37 edges
8. `_base_pf_data()` - 34 edges
9. `MixFreeEmailForm` - 33 edges
10. `ReportAbuseForm` - 33 edges

## Surprising Connections (you probably didn't know these)
- `portal.settings.local` --semantically_similar_to--> `Dockerfile.<env> selection`  [INFERRED] [semantically similar]
  docker-compose.yml → deploy.sh
- `deploy.sh (manual ECR image deployer)` --conceptually_related_to--> `GitLab CI/CD pipeline`  [INFERRED]
  deploy.sh → .gitlab-ci.yml
- `LeadFormMixin` --uses--> `PipedriveSender`  [INFERRED]
  landing_page/views.py → portal/pipedrive_service.py
- `BaseLandingPagePlansView` --uses--> `PipedriveSender`  [INFERRED]
  landing_page/views.py → portal/pipedrive_service.py
- `BaseLandingPageView` --uses--> `PipedriveSender`  [INFERRED]
  landing_page/views.py → portal/pipedrive_service.py

## Import Cycles
- 1-file cycle: `products/management/commands/get_plans_price.py -> products/management/commands/get_plans_price.py`
- 2-file cycle: `configuration/tasks.py -> products/management/commands/get_plans_price.py -> configuration/tasks.py`
- 2-file cycle: `portal/utils.py -> products/management/commands/get_plans_price.py -> portal/utils.py`
- 3-file cycle: `configuration/tasks.py -> portal/utils.py -> products/management/commands/get_plans_price.py -> configuration/tasks.py`
- 3-file cycle: `portal/utils.py -> products/management/commands/get_plans_price.py -> products/models.py -> portal/utils.py`

## Hyperedges (group relationships)
- **GitLab CI pipeline stages** — mailerweb_portal_gitlabci_stage_build, mailerweb_portal_gitlabci_stage_tests, mailerweb_portal_gitlabci_stage_staging_deploy [EXTRACTED 1.00]
- **Local dev stack (web + mysql + settings.local)** — mailerweb_portal_dockercompose_web, mailerweb_portal_dockercompose_mysql, mailerweb_portal_dockercompose_settings_local [EXTRACTED 1.00]
- **Manual deploy steps (build/push, samconfig, sam deploy)** — mailerweb_portal_deploy_script, mailerweb_portal_readme_samconfig, mailerweb_portal_readme_sam_deploy [EXTRACTED 1.00]

## Communities (95 total, 28 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.11
Nodes (52): FormView, test_pipedrive_get_persons(), LandingPageView, SuccessView, MixFreeEmailForm, PaymentForm, PreSignUpForm, A Django form for pre-signup user validation.     Fields:         username (Char (+44 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (28): Form, build_form_debug_message(), create_message_generic(), format_assunto_label(), get_mix_free_product_identifiers(), Any, Valida os dados de um formulário genérico.      Args:         raw_form (QueryDic, Monta uma mensagem HTML a partir dos dados validados e dos labels dos campos. (+20 more)

### Community 2 - "Community 2"
Cohesion: 0.09
Nodes (37): $(), A(), Ae(), B(), Be(), c(), $e(), ee() (+29 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (16): CMSSitemap, DetailView, HelpCategoryAdmin, HelpPostAdmin, HelpCategory, HelpPost, Meta, HelpCenterView (+8 more)

### Community 4 - "Community 4"
Cohesion: 0.08
Nodes (18): CMSPlugin, CMSPluginBase, HeroSection, HeroSectionPluginModel, LeadLandingPage, Meta, BaseLandingPagePlansView, BaseLandingPageView (+10 more)

### Community 5 - "Community 5"
Cohesion: 0.09
Nodes (31): AWS ECR (137899003623, us-east-2), COMMIT_HASH / image tag, Docker image mailerweb-portal-v2, Dockerfile.<env> selection, deploy.sh (manual ECR image deployer), Service: mysql-portal-v2 (MySQL 8.0), portal.settings.local, Service: web-portal-v2 (Django, Dockerfile.local) (+23 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (12): Formulário de registro completo (Pessoa Física ou Jurídica).      Valida os dado, Valida o nome completo para pessoa física.          Garante que o campo não está, Valida a data de nascimento para pessoa física.          Garante que a data é ob, Valida a razão social para pessoa jurídica.          Garante que o campo não est, Valida o nome fantasia para pessoa jurídica.          Garante que o campo não es, Valida o número de telefone.          Remove caracteres não numéricos e garante, Valida o CEP.          Remove caracteres não numéricos e garante que o CEP possu, Valida o endereço.          Garante que o campo não está vazio e possui pelo men (+4 more)

### Community 7 - "Community 7"
Cohesion: 0.13
Nodes (19): Category, Command, fetch_price_payloads(), Synchronise groups, products, categories, resources and prices with the remote p, Print a green-styled success message., Synchronise ProductPrice entries from the buffered payload., Synchronise Resource objects from the remote panel., Synchronise ProductResource mappings from the remote panel. (+11 more)

### Community 8 - "Community 8"
Cohesion: 0.12
Nodes (14): _base_pf_data(), Rejeita nome sem sobrenome., Rejeita nome contendo numeros., Rejeita nome contendo caracteres especiais invalidos., Aceita nome com acentos., Aceita nome com hifen., Rejeita parte do nome com menos de 2 caracteres., Remove espacos extras e normaliza o nome. (+6 more)

### Community 9 - "Community 9"
Cohesion: 0.21
Nodes (15): BaseCommand, Command, CurrencyAdmin, SiteAdmin, Currency, Meta, Site, get_sites_from_panel() (+7 more)

### Community 10 - "Community 10"
Cohesion: 0.13
Nodes (15): Valida o nome de usuário.          Garante que o username é obrigatório, possui, add_a_transaction_to_a_invoice(), add_months(), check_exists(), create_customer_on_panel(), create_invoice_from_transactions(), create_object(), create_service_discount_on_panel() (+7 more)

### Community 11 - "Community 11"
Cohesion: 0.12
Nodes (13): BaseInlineFormSet, Media, ProductPriceInline, ProductResourceInline, ProductTablePriceAdmin, ResourceAdmin, Meta, PageFormSet (+5 more)

### Community 12 - "Community 12"
Cohesion: 0.15
Nodes (15): cardCvcElement, cardExpiryElement, cardNumberElement, elements, getCardOwner(), handleRegisterPaymentMethod(), requestByPaymentMethod(), sendoToBackend() (+7 more)

### Community 13 - "Community 13"
Cohesion: 0.13
Nodes (10): GatekeeperOnboardingError, Raised when the secondary Gatekeeper onboarding call fails., RuntimeError, _attach_session(), _product_resource(), test_build_portal_signup_onboarding_payload_for_company(), test_build_portal_signup_onboarding_payload_for_person(), test_send_portal_signup_onboarding_raises_on_http_error() (+2 more)

### Community 14 - "Community 14"
Cohesion: 0.12
Nodes (6): ProductSelectForm, Category, Product, Site, Quantidade de parcelas (ex.: 12 para anual)., TranslatableModel

### Community 15 - "Community 15"
Cohesion: 0.13
Nodes (10): Lock, Any, Resolve email, person and deal context with MF/PP session fallback.          Arg, Execute an HTTP request to the Pipedrive API.          Args:             method:, Ensure a person exists in Pipedrive and return its ID.          Looks up by emai, Persist resolved person/deal data back into the session.          Only updates w, Create or update a person and deal in Pipedrive.          Resolves MF/PP session, Create or update a resource and return its ID.          Uses PUT when ``entity_i (+2 more)

### Community 16 - "Community 16"
Cohesion: 0.11
Nodes (8): normalize_date(), Helper func that returns the 1st of next month, if the supplied date does not ex, ConsumptionCycle, Group, Meta, ProductType, Resource, ResourceType

### Community 17 - "Community 17"
Cohesion: 0.14
Nodes (10): _base_pj_data(), Nao valida person_name quando aba ativa e juridica., Testes para SignupForm.clean_corporate_name., Aceita razao social valida., Rejeita razao social vazia para pessoa juridica., Rejeita razao social com menos de 2 caracteres., Nao valida corporate_name quando aba ativa e fisica., Nao valida birth_date quando aba ativa e juridica. (+2 more)

### Community 18 - "Community 18"
Cohesion: 0.21
Nodes (8): _BaseAddress, create_account(), Cria uma nova conta através de uma requisição POST para a API (LambdaFunction at, ClientIPResolver, get_client_ip(), Parse a textual token that may include ports, quotes, or hyphenated reverse DNS., Return True for globally routable addresses., Return the first public IP found in the provided header values.

### Community 19 - "Community 19"
Cohesion: 0.22
Nodes (7): CustomPost, Meta, CustomPostDetailView, CustomPostListView, Post, PostDetailView, PostListView

### Community 20 - "Community 20"
Cohesion: 0.23
Nodes (4): ManifestFilesMixin, S3Boto3Storage, ManifestS3BotoStorage, Storage S3 com Manifest para cache busting (para staging e/ou production).

### Community 21 - "Community 21"
Cohesion: 0.20
Nodes (6): Testes para SignupForm.clean_phone., Aceita telefone celular com 11 digitos., Aceita telefone fixo com 10 digitos., Rejeita telefone com menos de 10 digitos., Rejeita telefone vazio., TestCleanPhone

### Community 22 - "Community 22"
Cohesion: 0.20
Nodes (6): Testes para PreSignUpForm.clean_username., Aceita username alfanumerico valido., Rejeita username contendo espacos., Rejeita username contendo caracteres especiais invalidos., Aceita username com hifens e underscores., TestCleanUsername

### Community 23 - "Community 23"
Cohesion: 0.22
Nodes (8): cardHolderName, cardNameInput, cardNumber, cardNumberDisplay, cvvDisplay, cvvInput, displayValidity, validityInput

### Community 24 - "Community 24"
Cohesion: 0.25
Nodes (4): AppConfig, HelpcenterConfig, LandingPageConfig, PortalConfig

### Community 25 - "Community 25"
Cohesion: 0.32
Nodes (4): MiddlewareMixin, CustomErrorMiddleware, PartnerMiddleware, Middleware for generic HTTP error handling.     - 400 and 401: specific messages

### Community 26 - "Community 26"
Cohesion: 0.25
Nodes (5): Testes unitarios para validacoes do SignupForm e PreSignUpForm.  Cobre as valida, Testes para SignupForm.clean_city., Aceita cidade valida., Rejeita cidade com menos de 2 caracteres., TestCleanCity

### Community 27 - "Community 27"
Cohesion: 0.25
Nodes (5): Testes para SignupForm.clean_business_name., Aceita nome fantasia valido., Rejeita nome fantasia vazio para pessoa juridica., Nao valida business_name quando aba ativa e fisica., TestCleanBusinessName

### Community 28 - "Community 28"
Cohesion: 0.25
Nodes (5): Testes para SignupForm.clean_address., Aceita endereco valido., Rejeita endereco com menos de 3 caracteres., Rejeita endereco vazio., TestCleanAddress

### Community 29 - "Community 29"
Cohesion: 0.25
Nodes (5): Testes para SignupForm.clean_birth_date., Aceita data de nascimento valida., Rejeita data de nascimento vazia para pessoa fisica., Rejeita data em formato invalido., TestCleanBirthDate

### Community 30 - "Community 30"
Cohesion: 0.48
Nodes (6): generate_comece_agora_data(), generate_report_abuse_data(), generate_support_data(), run1(), run2(), Playwright

### Community 31 - "Community 31"
Cohesion: 0.29
Nodes (4): Testes para SignupForm.clean_zip_code., Aceita CEP valido com 8 digitos., Rejeita CEP com menos de 8 digitos., TestCleanZipCode

### Community 32 - "Community 32"
Cohesion: 0.29
Nodes (4): Testes para SignupForm.clean_state., Rejeita UF inexistente., Aceita UF em minusculas e converte para maiusculas., TestCleanState

### Community 33 - "Community 33"
Cohesion: 0.33
Nodes (3): CategoryAdmin, ProductAdmin, TranslatableAdmin

### Community 34 - "Community 34"
Cohesion: 0.33
Nodes (4): This file demonstrates writing tests using the unittest module. These will pass, Tests that 1 + 1 always equals 2., SimpleTest, TestCase

### Community 35 - "Community 35"
Cohesion: 0.33
Nodes (4): Testes para SignupForm.clean_neighborhood., Aceita bairro valido., Rejeita bairro com menos de 2 caracteres., TestCleanNeighborhood

## Knowledge Gaps
- **57 isolated node(s):** `Meta`, `CurrencyAdmin`, `SiteAdmin`, `Migration`, `Meta` (+52 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **28 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SignupForm` connect `Community 6` to `Community 0`, `Community 32`, `Community 35`, `Community 8`, `Community 17`, `Community 18`, `Community 21`, `Community 22`, `Community 26`, `Community 27`, `Community 28`, `Community 29`, `Community 31`?**
  _High betweenness centrality (0.171) - this node is a cross-community bridge._
- **Why does `PipedriveSender` connect `Community 0` to `Community 1`, `Community 18`, `Community 4`, `Community 15`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Why does `PreSignUpForm` connect `Community 0` to `Community 32`, `Community 1`, `Community 35`, `Community 8`, `Community 10`, `Community 17`, `Community 21`, `Community 22`, `Community 26`, `Community 27`, `Community 28`, `Community 29`, `Community 31`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `SignupForm` (e.g. with `RecaptchaV3Mixin` and `AboutMlsenderView`) actually correct?**
  _`SignupForm` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `$()` (e.g. with `toggleLoading()` and `togglePaymentButton()`) actually correct?**
  _`$()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 39 inferred relationships involving `PreSignUpForm` (e.g. with `RecaptchaV3Mixin` and `AboutMlsenderView`) actually correct?**
  _`PreSignUpForm` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 35 inferred relationships involving `PipedriveSender` (e.g. with `BaseLandingPagePlansView` and `BaseLandingPageView`) actually correct?**
  _`PipedriveSender` has 35 INFERRED edges - model-reasoned connections that need verification._