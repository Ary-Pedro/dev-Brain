---
type: note
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: active
last_verified: 2026-06-23
token_policy: full
tags: [meta, automation, toolbox, agents, skills]
---

# toolbox-guide — como usar/ativar agents & skills

> Guia curado de **quando e como** usar cada agent/skill. O inventário cru (auto-gerado a cada boot pelo hook `dev-brain-sync.js`) fica em [[_toolbox]]; aqui está o **how/when**. Roteamento geral: [[routing]] · loop: [[flow]].

## Como a ativação funciona (não precisa decorar)
- **Agents** (sub-agents) ativam pela `description` — o Claude despacha sozinho ao detectar a tarefa. Forçar: `@nome` ou "use o agent X". Sub-agent **não despacha** outro (lê domínio MailerWeb direto, read-only).
- **Skills** ativam por `/nome` ou auto-trigger pela `description` (gatilho na conversa). Corpo da skill só entra no contexto **quando invocada** (economia — ver camadas em [[flow]]).
- **Inventário** (`_toolbox.md`) e drift se atualizam **sozinhos no próximo SessionStart**. Nada manual.

## Agents (stack + papel)
| Agent | Quando usar | Lê |
|-------|-------------|-----|
| [[dev-django]] | codar/revisar Python/Django | know/ + `python-django` |
| [[dev-next]] | codar/revisar TS/Next | know/ + `typescript-next` |
| [[dev-spring]] | codar/revisar Java/Spring | know/ + `java-spring` |
| **dev-dba** | schema/migration/query/índice/N+1/EXPLAIN | know/ + `database` |
| **dev-uiux** | UI/UX, a11y/WCAG, design system, estados de tela | know/ + `frontend`+`typescript-next` |
| **dev-devops** | Docker/CI-CD/deploy/env/observabilidade | know/ (`security`/`performance`) |
| **project-watcher** | panorama: commits/peso/grafo/missing-links → cards/dashboards | git + graph/ + projects/ (escreve só dev-Brain) |
| [[mailerweb-bridge]] | domínio MailerWeb (onde/o quê/regra) | só `mailerweb-brain` (read-only) |
| [[context-economist]] | ANTES de contexto pesado: menor conjunto de fontes | projects/ token_weight + routing |
| [[brain-architect]] | saúde do vault: frontmatter, links, MOCs, missing-links | dev-Brain |
| **architect** | design de sistema/módulo, tradeoffs, ADR | `/architecture-modeling` `/backend-layering` `/design-patterns` |
| **qa-engineer** | gate de qualidade (read-only), go/no-go | `/qa-review` `/code-audit` `/release-readiness` |
| **data-analyst** | métrica/KPI/relatório com grão e validação | `/data-analysis` `/dba-*` |
| **process-analyst** | requisitos/casos de uso/fluxo antes de codar | `/process-modeling` |

> Plugins já cobrem papéis genéricos (ver [[_toolbox]]): `code-architect`, `security-auditor`, `code-reviewer`, `test-engineer`, `cavecrew-{investigator,builder,reviewer}`. Reviewer/auditor = use esses; não dupliquei. Mapa gatilho→agent/skill: [[keyword-routing]].

## Skills (procedimento sob demanda — 25)
Gatilho→skill detalhado em [[keyword-routing]]. Toda skill **lê o `know/` correspondente antes** (padrão = verdade; skill = procedimento) e tem workflow + guardrails + validação (smoke-test) + saída.

**Processo & arquitetura:** `/process-modeling` · `/architecture-modeling` · `/fullstack-feature` · `/prompt-library`
**Engenharia OO/clean:** `/solid` · `/poo` · `/design-patterns` · `/refactor` · `/python-clean`
**Backend & API:** `/backend-layering` · `/api-design` · `/infra-security`
**Dados/DB:** `/db-design` · `/dba-basic` · `/dba-mcp` (DB MCP) · `/data-analysis`
**Front & UX:** `/frontend-ui` · `/uiux-basic` · `/uiux-figma` (Figma MCP) · `/a11y` · `/javascript-platform`
**Entrega & QA:** `/devops-delivery` · `/code-audit` · `/qa-review` · `/release-readiness`
**Domínio & meta:** `/mailerweb-domain` (read-only) · `/graphify` · `/journal` · `/caveman` · `/cavecrew`

> Cobertura: QA, backend, frontend, dados, OO/arquitetura e domínio — nível sênior, cada skill com workflow + guardrails + validação. Inventário cru auto: [[_toolbox]].

## MCP (pontes)
- **Figma** — ✅ conectado (claude.ai). Skill `/uiux-figma`. Skill `/figma-use` antes de `use_figma`.
- **Database** — read-only, localhost, **draft** (você adiciona credencial). Skill `/dba-mcp`. Config em [[mcp-database]]. Sem ele → `/dba-basic`.
- **Obsidian** — adiado ([[0003-stack-e-fluxo-2026-06]]); vault via filesystem.

## Backlog (núcleo pronto; resto sob demanda)
Núcleo de skills/agents materializado. Próximos candidatos só **quando a dor aparecer** ([[_principles]]): `tdd` (red→green→refactor) · `observability` (logs/métricas/traces) · `caching` (+invalidação/prompt-cache) · `data-modeling` (DDD/agregados) · `dependency-audit` · `tech-writer` (docs/ADR). Antes de criar, checar plugin existente (ver [[_toolbox]]) — não duplicar.

Ver [[00-index]] · [[routing]] · [[flow]] · [[_toolbox]].
