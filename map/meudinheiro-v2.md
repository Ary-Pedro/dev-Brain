---
type: note
scope: meudinheiro-v2
repo_path: ~/devSpace/projeto/meuDinheiroNaMaoV2
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: active
confidence: high
last_verified: 2026-06-19
token_policy: summary-first
tags: [map, projeto, typescript-next]
---

# meudinheiro-v2 — mapa do projeto

> App fullstack de gestão financeira pessoal. Projeto **independente** (sem domínio MailerWeb).
> Localização: `~/devSpace/projeto/meuDinheiroNaMaoV2`. Tem `CLAUDE.md` próprio na raiz — leia antes de codar.

## Stack

- **Framework:** Next.js 16 (App Router) + React 19 — fullstack (UI + API routes no mesmo projeto).
- **Linguagem:** TypeScript 5 (`strict`, alias `@/*` → `./src/*`).
- **ORM/DB:** Prisma 6 + PostgreSQL.
- **Auth:** JWT em cookie (`jose`) + `bcryptjs`; verificação em `src/proxy.ts` (convenção de proxy do Next 16), injeta headers `x-user-id`/`x-user-email`/`x-user-name`.
- **Validação:** Zod (em DTOs, chamados nos controllers).
- **UI:** Tailwind CSS 4 + Radix UI + shadcn (`components.json`), `lucide-react`, `recharts`/`highcharts` para gráficos.
- **Data:** `@tanstack/react-query`, `date-fns`.
- **Infra:** Docker + docker-compose (app + Postgres, profile `public` adiciona Cloudflare Quick Tunnel).

## Estrutura

| Dir | Papel |
|-----|-------|
| `src/app/(auth)` | Rotas/UI de autenticação (login, etc.). |
| `src/app/(app)` | UI autenticada (dashboards das telas). |
| `src/app/api` | API routes — importam objeto de composição e chamam controllers. |
| `src/server/composition` | Injeção de dependência manual (wires repos → services → controllers). |
| `src/modules/finance` | Domínio Finanças (contas, categorias, transações, transferências). |
| `src/modules/investments` | Domínio Investimentos (ativos, operações, posições). |
| `src/modules/simulations` | Domínio Simulações (cenários DRAFT→CALCULATED→ARCHIVED). |
| `src/modules/auth` | Domínio de autenticação. |
| `src/lib` | Infra compartilhada (`http.ts` com `executeRoute()`, helpers de auth). |
| `src/components/ui` | Componentes base (Radix/shadcn). |
| `src/components/layout` | Layout/shell da aplicação. |
| `prisma` | `schema.prisma`, `migrations/`, `seed.ts`. |

**Arquitetura em camadas (nunca pular camada):**
`app/ (UI + API) → Controller → Service → Repository → Prisma → PostgreSQL`.
Regras de domínio: Finance, Investments e Simulations são **estritamente isolados** (sem acesso cruzado); Prisma só em repositories; Zod só em controllers.

## Entrypoints

- **App/UI + API:** `src/app/` (App Router; `route.ts` para endpoints, layouts/pages para UI).
- **Auth/middleware:** `src/proxy.ts` — verifica JWT e injeta headers de usuário.
- **DI raiz:** `src/server/composition/*` (ex.: `finance.ts` exporta `financeComposition`).
- **Error mapping central:** `src/lib/http.ts` → `executeRoute()` (AppError→status, ZodError→400, Prisma P2002→409, P2025→404).
- **Schema de dados:** `prisma/schema.prisma`.

## Como rodar (comandos)

```bash
# Setup
npm install
cp .env.example .env            # DATABASE_URL + JWT_SECRET

# DB (Prisma)
npm run prisma:migrate:dev      # cria + aplica migração (dev)
npm run prisma:migrate          # aplica migrações pendentes (prod)
npm run prisma:generate         # regenera client após mudar schema
npm run prisma:seed             # popula usuário/dados demo
npm run prisma:studio           # editor visual

# Dev / build
npm run dev                     # dev server em 0.0.0.0:3000
npm run build                   # build de produção
npm run start                   # serve build
npm run lint                    # ESLint

# Docker (app + PostgreSQL)
npm run start:docker            # docker compose up --build -d
docker compose --profile public up -d   # + Cloudflare Quick Tunnel
```

> Nota: o projeto não tem suíte de testes configurada no `package.json` (sem script `test`). Ao adicionar testes, seguir [[testing]].

## Padrões aplicáveis

Governança universal (`know/`): [[_principles]] · [[code-style]] · [[naming]] · [[docstrings]] · [[comments]] · [[error-handling]] · [[security]] · [[performance]] · [[git-commits]] · [[testing]].

Por stack: [[typescript-next]] — padrões de TypeScript/Next (App Router, server/client components, route handlers, Prisma).

## Roteamento

Projeto **independente** → consultar **somente dev-Brain**. Não citar apps, fluxos ou regras do MailerWeb (anti-alucinação). Regra completa em [[routing]].

Precedência: `know/` (padrão de engenharia, inviolável) > `CLAUDE.md` da raiz do projeto (regras locais: camadas, isolamento de domínio, Zod em controllers).

---
Voltar ao [[00-index]].
