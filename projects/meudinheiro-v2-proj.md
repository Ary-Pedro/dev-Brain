---
type: project
project: meudinheiro-v2
scope: meudinheiro-v2
repo_path: ~/devSpace/projeto/meuDinheiroNaMaoV2
stack: [typescript, nextjs, prisma, postgres]
brain_policy: dev-brain
write_policy: dev-brain-only
domain_brain: (nenhum)
status: active
token_weight: baixo
token_policy: summary-first
graph_nodes: 622
graph_edges: 1301
source: human+graphify
audience: ai
tags: [project]
---

# meudinheiro-v2 — card vivo

> Camada operacional p/ o agente decidir contexto antes de codar. Não é doc humana — é onde a IA descobre o que abrir e como rotear. Detalhe estrutural fica no mapa [[meudinheiro-v2]] e no grafo [[meudinheiro-v2-grafo]].

<!-- @generated:start -->
## Objetivo

App fullstack de gestão financeira pessoal (Next.js 16 App Router + React 19 + Prisma 6 + PostgreSQL). Projeto **independente**, sem domínio MailerWeb. Arquitetura em camadas estritas: `app/ (UI + API) → Controller → Service → Repository → Prisma → PostgreSQL`. Três domínios isolados sem acesso cruzado: Finance, Investments, Simulations (+ Auth). Prisma só em repositories; Zod só em controllers; error mapping central em `executeRoute()` (`src/lib/http.ts`).

## Como consultar

1. **Domínio** (regra de negócio, fluxo, isolamento de módulos) → **somente dev-Brain**. `domain_brain` é nenhum; nunca citar MailerWeb (anti-alucinação). Ver [[routing]].
2. **Padrão** (engenharia: estilo, naming, erros, segurança, testes) → `know/` via `/know`. Por stack: [[typescript-next]].
3. **Estrutura** (onde mora algo, árvore de dirs, entrypoints) → [[meudinheiro-v2-grafo]] / mapa [[meudinheiro-v2]].
4. **Relação** (quem chama quem, impacto de mudança, god nodes) → `graphify query` no grafo `meudinheiro-v2` (622 nós / 1301 arestas, 35 comunidades).

## Peso p/ IA

`token_weight=baixo` → para uma tarefa típica pode abrir **resumo + ~2 notas** sem estourar contexto. Sequência recomendada: este card → mapa [[meudinheiro-v2]] → (se preciso) grafo [[meudinheiro-v2-grafo]] ou uma nota `know/`. Não carregar os 622 nós de uma vez — usar `graphify query` direcionado.

Âncoras de alto grau (god nodes — começar por aqui ao investigar):
- `executeRoute()` — `src/lib/http.ts` (degree 52, error mapping central).
- `finance.ts` — `src/server/composition/finance.ts` (degree 47, DI do domínio Finance).
- `auth.ts` / `getCurrentUserFromHeaders()` — `src/lib/auth.ts` (auth via headers injetados pelo proxy).
- Páginas-hub: `dashboard`, `finance/transactions`, `investments`, `finance/accounts`, `finance/transfers`.

## Próxima ação

Sem ação em aberto registrada. Ao abrir tarefa neste projeto: ler `CLAUDE.md` da raiz do repo (regras locais de camadas/isolamento/Zod) antes de codar. Sem suíte de testes configurada (`package.json` não tem script `test`) — se for adicionar testes, seguir [[testing]].
<!-- @generated:end -->

<!-- @user:start -->
(observações manuais do Pedro)
<!-- @user:end -->

---
Relacionados: [[meudinheiro-v2]] (mapa) · [[meudinheiro-v2-grafo]] · [[routing]].
