# Graph Report - .  (2026-06-19)

## Corpus Check
- Corpus is ~31,683 words - fits in a single context window. You may not need a graph.

## Summary
- 622 nodes · 1301 edges · 35 communities (26 shown, 9 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.8)
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
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]

## God Nodes (most connected - your core abstractions)
1. `executeRoute()` - 52 edges
2. `formatCurrency()` - 25 edges
3. `getCurrentUserFromHeaders()` - 19 edges
4. `InvestmentsRepository` - 19 edges
5. `Button` - 18 edges
6. `AccountsRepository` - 18 edges
7. `cn()` - 16 edges
8. `InvestmentsService` - 16 edges
9. `compilerOptions` - 16 edges
10. `CategoriesRepository` - 15 edges

## Surprising Connections (you probably didn't know these)
- `PUT()` --calls--> `executeRoute()`  [INFERRED]
  src/app/api/finance/accounts/[id]/route.ts → src/lib/http.ts
- `DELETE()` --calls--> `executeRoute()`  [INFERRED]
  src/app/api/finance/accounts/[id]/route.ts → src/lib/http.ts
- `PUT()` --calls--> `executeRoute()`  [INFERRED]
  src/app/api/finance/categories/[id]/route.ts → src/lib/http.ts
- `DELETE()` --calls--> `executeRoute()`  [INFERRED]
  src/app/api/finance/categories/[id]/route.ts → src/lib/http.ts
- `PUT()` --calls--> `executeRoute()`  [INFERRED]
  src/app/api/finance/transactions/[id]/route.ts → src/lib/http.ts

## Import Cycles
- None detected.

## Communities (35 total, 9 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (88): AccountsPage(), emptyForm(), isInvestmentType(), CategoriesPage(), COLORS, empty(), AccountCard(), AccountCardProps (+80 more)

### Community 1 - "Community 1"
Cohesion: 0.07
Nodes (45): GET(), POST(), GET(), POST(), GET(), POST(), POST(), GET() (+37 more)

### Community 2 - "Community 2"
Cohesion: 0.06
Nodes (9): InvestmentsController, CreateAccountInvestmentDto, CreateAssetDto, CreateOperationDto, UpdateAccountInvestmentDto, UpdateAssetDto, UpdatePositionDto, InvestmentsRepository (+1 more)

### Community 3 - "Community 3"
Cohesion: 0.11
Nodes (7): simulationsRepo, simulationsService, SimulationsController, CreateSimulationDto, UpdateSimulationDto, SimulationsRepository, SimulationsService

### Community 4 - "Community 4"
Cohesion: 0.07
Nodes (28): dependencies, bcryptjs, class-variance-authority, clsx, date-fns, highcharts, highcharts-react-official, jose (+20 more)

### Community 5 - "Community 5"
Cohesion: 0.11
Nodes (5): CategoriesController, CreateCategoryDto, UpdateCategoryDto, CategoriesRepository, CategoriesService

### Community 6 - "Community 6"
Cohesion: 0.13
Nodes (16): BarTooltip(), BarTooltipProps, ExchangeRatesWidget(), HighchartsReact, SankeySection(), SankeySectionProps, addDays(), DashboardPage() (+8 more)

### Community 7 - "Community 7"
Cohesion: 0.17
Nodes (9): authRepo, authService, AuthController, LoginDto, RegisterDto, JwtPayload, signToken(), AuthRepository (+1 more)

### Community 8 - "Community 8"
Cohesion: 0.10
Nodes (19): compilerOptions, allowJs, esModuleInterop, incremental, isolatedModules, jsx, lib, module (+11 more)

### Community 9 - "Community 9"
Cohesion: 0.13
Nodes (14): manrope, metadata, spaceGrotesk, Providers(), Toaster(), Action, dispatch(), genId() (+6 more)

### Community 10 - "Community 10"
Cohesion: 0.11
Nodes (17): aliases, components, hooks, lib, ui, utils, iconLibrary, rsc (+9 more)

### Community 11 - "Community 11"
Cohesion: 0.18
Nodes (4): CreateTransferDto, UpdateTransferDto, TransfersRepository, TransfersService

### Community 12 - "Community 12"
Cohesion: 0.18
Nodes (4): AccountsController, CreateAccountDto, UpdateAccountDto, AccountsService

### Community 13 - "Community 13"
Cohesion: 0.15
Nodes (11): accountsRepo, accountsService, categoriesRepo, categoriesService, dashboardService, transactionsRepo, transactionsService, transfersRepo (+3 more)

### Community 14 - "Community 14"
Cohesion: 0.23
Nodes (13): DashboardSummaryDto, dateOnly, addDays(), DashboardPeriod, diffDaysInclusive(), formatShortDate(), parseDateOnly(), presetChartLabel() (+5 more)

### Community 15 - "Community 15"
Cohesion: 0.15
Nodes (13): devDependencies, eslint, eslint-config-next, @eslint/eslintrc, prisma, tailwindcss, @tailwindcss/postcss, tsx (+5 more)

### Community 16 - "Community 16"
Cohesion: 0.15
Nodes (13): scripts, build, dev, lint, prisma:generate, prisma:migrate, prisma:migrate:dev, prisma:seed (+5 more)

### Community 17 - "Community 17"
Cohesion: 0.26
Nodes (9): INPUT_LABELS, RESULT_LABELS, SimulationCard(), SimulationCardProps, SimFormState, SimulationForm(), SimulationScenario, emptyForm() (+1 more)

### Community 18 - "Community 18"
Cohesion: 0.33
Nodes (4): CreateTransactionDto, ListTransactionsDto, UpdateTransactionDto, TransactionsService

### Community 21 - "Community 21"
Cohesion: 0.38
Nodes (6): config, isApiPath(), proxy(), PUBLIC_PATHS, secret, unauthorizedResponse()

### Community 25 - "Community 25"
Cohesion: 0.47
Nodes (5): main(), md(), prisma, TxInput, vary()

### Community 27 - "Community 27"
Cohesion: 0.40
Nodes (4): compat, __dirname, eslintConfig, __filename

### Community 28 - "Community 28"
Cohesion: 0.50
Nodes (3): name, private, version

## Knowledge Gaps
- **154 isolated node(s):** `$schema`, `style`, `rsc`, `tsx`, `config` (+149 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AppError` connect `Community 1` to `Community 2`, `Community 3`, `Community 5`, `Community 7`, `Community 11`, `Community 12`, `Community 18`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Why does `InvestmentsRepository` connect `Community 2` to `Community 24`, `Community 1`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Are the 14 inferred relationships involving `executeRoute()` (e.g. with `DELETE()` and `PUT()`) actually correct?**
  _`executeRoute()` has 14 INFERRED edges - model-reasoned connections that need verification._
- **What connects `$schema`, `style`, `rsc` to the rest of the system?**
  _154 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.0559228650137741 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.07039573820395738 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.05877551020408163 - nodes in this community are weakly interconnected._