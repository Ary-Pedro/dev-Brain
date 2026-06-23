---
type: note
scope: meudinheiro-v2
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: graphify
status: active
confidence: high
last_verified: 2026-06-19
token_policy: summary-first
tags: [graph, code, meudinheiro-v2]
aliases: [meudinheiro-v2-graph]
---

# meudinheiro-v2 — grafo de código

> Estrutura real do código (graphify, AST). **622 nós · 1301 arestas · 35 módulos**.
> Mapa do projeto: [[meudinheiro-v2]] · relatório bruto: `graph/meudinheiro-v2/GRAPH_REPORT.md` · grafo: `graph/meudinheiro-v2/graph.json`.

## Módulos (comunidades, nomeadas pela pasta dominante)

| Módulo | Nós | Pastas | Exemplos |
|--------|-----|--------|----------|
| **modules** | 121 | modules (52), components (42), app (22) | `page.tsx`, `page.tsx`, `page.tsx`, `page.tsx` |
| **app** | 73 | app (57), lib (9), server (7) | `executeRoute()`, `auth.ts`, `http.ts`, `getCurrentUserFromHeaders()` |
| **modules** | 50 | modules (50) | `InvestmentsRepository`, `InvestmentsService`, `investments-service.ts`, `InvestmentsController` |
| **modules** | 30 | modules (27), server (3) | `simulations.ts`, `SimulationsService`, `simulations-service.ts`, `SimulationsRepository` |
| **package.json** | 28 | package.json (28) | `dependencies`, `next`, `react`, `react-dom` |
| **modules** | 25 | modules (25) | `CategoriesRepository`, `categories-service.ts`, `CategoriesService`, `categories-controller.ts` |
| **modules** | 23 | modules (12), app (11) | `page.tsx`, `dashboard.ts`, `sankey-section.tsx`, `ExchangeRates` |
| **modules** | 23 | modules (18), server (3), lib (2) | `auth-service.ts`, `auth.ts`, `auth-controller.ts`, `AuthService` |
| **tsconfig.json** | 20 | tsconfig.json (20) | `compilerOptions`, `tsconfig.json`, `paths`, `target` |
| **components** | 19 | components (14), app (5) | `use-toast.ts`, `layout.tsx`, `toaster.tsx`, `providers.tsx` |
| **components.json** | 18 | components.json (18) | `components.json`, `tailwind`, `aliases`, `$schema` |
| **modules** | 18 | modules (18) | `transfers-service.ts`, `TransfersRepository`, `TransfersService`, `transfers-controller.ts` |
| **modules** | 17 | modules (17) | `accounts-service.ts`, `AccountsService`, `accounts-controller.ts`, `AccountsController` |
| **server** | 16 | server (10), modules (6) | `finance.ts`, `dashboard-controller.ts`, `DashboardService`, `DashboardController` |
| **modules** | 16 | modules (16) | `dashboard-service.ts`, `resolvePeriods()`, `previousPeriodFor()`, `dashboard.dto.ts` |

## Hubs (god nodes — maior conectividade)

| Símbolo | Grau | Arquivo |
|---------|------|---------|
| `executeRoute()` | 52 | `src/lib/http.ts` |
| `finance.ts` | 47 | `src/server/composition/finance.ts` |
| `page.tsx` | 34 | `src/app/(app)/dashboard/page.tsx` |
| `page.tsx` | 34 | `src/app/(app)/finance/transactions/page.tsx` |
| `page.tsx` | 32 | `src/app/(app)/investments/page.tsx` |
| `page.tsx` | 31 | `src/app/(app)/finance/accounts/page.tsx` |
| `auth.ts` | 31 | `src/lib/auth.ts` |
| `page.tsx` | 30 | `src/app/(app)/finance/transfers/page.tsx` |
| `http.ts` | 30 | `src/lib/http.ts` |
| `utils.ts` | 29 | `src/lib/utils.ts` |
| `dependencies` | 28 | `package.json` |
| `page.tsx` | 26 | `src/app/(app)/finance/categories/page.tsx` |

> Hub com grau muito alto + nome genérico = candidato a quebrar em peças menores (ver [[_strategy]]).

<!-- @user:start -->
## 🧠 Leitura arquitetural

Os módulos dominantes confirmam uma arquitetura em camadas **por domínio**, replicada quase idêntica em cada feature. As três maiores comunidades fora da UI são tríades `Repository → Service → Controller` completas: `InvestmentsRepository/InvestmentsService/InvestmentsController` (50 nós, 100% em `src/modules`), `SimulationsService/SimulationsRepository/SimulationsController` (30 nós) e `CategoriesRepository/CategoriesService/CategoriesController` (25 nós), com `transfers` e `accounts` repetindo o mesmo molde menor (18 e 17 nós). É um sinal saudável: o isolamento de domínio prometido no [[meudinheiro-v2|mapa]] aparece no grafo — cada domínio é uma comunidade fechada, sem nós cruzando para outro domínio. A maior comunidade (121 nós) mistura `modules` (52) + `components` (42) + `app` (22): é a camada de apresentação por feature, onde vivem os vários `page.tsx`.

O acoplamento real está concentrado na infra compartilhada, não nos domínios. Os dois maiores hubs — `executeRoute()` (grau 52, `src/lib/http.ts`) e `finance.ts` (grau 47, `src/server/composition/finance.ts`) — são pontos de entrada legítimos, mas merecem leituras opostas:

- **`executeRoute()` / `http.ts` (grau 52/30):** coesão saudável. É o wrapper central de error-mapping (AppError→status, ZodError→400, Prisma P2002/P2025) que toda `route.ts` consome. Grau alto é esperado num utilitário de borda; quebrá-lo só fragmentaria o tratamento de erro. Manter, seguindo [[error-handling]].
- **`finance.ts` (grau 47):** este é o candidato a god-object. O container de DI manual `financeComposition` está fazendo o wiring de contas, categorias, transações, transferências **e** dashboard num só arquivo — daí o grau quase idêntico ao do `executeRoute()`. Conforme o domínio Finance cresce, esse arquivo vira ponto único de mudança e merge-conflict. Vale dividir a composição por sub-domínio (`accounts.ts`, `categories.ts`, `transfers.ts`, `dashboard.ts`) e reagrupar num índice. Ver [[typescript-next]] (composição/DI) e [[_strategy]].
- **`utils.ts` (grau 29) + `formatCurrency()` (grau 25):** grab-bag clássico. `utils.ts` agrega helpers heterogêneos; `formatCurrency` sozinho é puxado por 25 nós. Considerar extrair formatadores de moeda/data para um módulo dedicado em vez de um `utils` genérico — ver [[code-style]].

Risco de acoplamento entre módulos é **baixo** — não há domínio vazando para outro no grafo. O ponto de pressão é vertical: tudo converge em `lib/` (http, auth, utils) e em `server/composition`. Os `page.tsx` de grau alto (dashboard 34, transactions 34, investments 32, accounts 31, transfers 30) são telas densas que combinam react-query + forms + charts; o cluster de `operation-form.tsx`/`asset-form.tsx`/`account-investment-form.tsx` (grau 22 cada) em `modules/investments/components` sugere lógica de formulário duplicada que poderia compartilhar um form-builder.

**Ações concretas:**
- Quebrar `src/server/composition/finance.ts` em composições por sub-domínio para reduzir o grau do hub e isolar mudanças — [[typescript-next]] · [[_strategy]].
- Extrair formatadores (`formatCurrency` e afins) de `src/lib/utils.ts` para um módulo de formatação coeso e consolidar os `*-form.tsx` de investments num componente base reaproveitável — [[code-style]].
<!-- @user:end -->

Ver [[00-graph-index]] · padrões em [[routing]].