---
type: note
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: active
last_verified: 2026-06-23
token_policy: summary-first
tags: [meta, routing, skills, agents]
---

# keyword-routing — gatilho → skill/agent

> Mapa de ativação por palavra-chave. Agents despacham pela `description`; skills por `/nome` ou auto-trigger. Guia completo: [[toolbox-guide]]. Roteamento de cérebro: [[routing]].

## Por intenção
| Gatilho (pt/en) | Skill | Agent |
|---|---|---|
| requisito, fluxo, regra de negócio, caso de uso, levantar | `/process-modeling` | process-analyst |
| arquitetura, como estruturar, design, tradeoff | `/architecture-modeling` `/design-patterns` | architect |
| feature completa, do front ao banco, end-to-end | `/fullstack-feature` | architect → devs |
| backend, endpoint, controller, service, repository, DTO | `/backend-layering` `/api-design` | dev-django · dev-spring |
| python, refatorar serviço, clean | `/python-clean` `/refactor` | dev-django |
| SOLID, acoplamento, responsabilidade | `/solid` | architect · reviewer |
| POO, herança vs composição, modelo de domínio | `/poo` | architect |
| schema, modelar dados, migration (conceitual) | `/db-design` | dev-dba |
| revisar SQL/migration/query (estático) | `/dba-basic` | dev-dba |
| schema vivo, banco real, drift | `/dba-mcp` (MCP) | dev-dba |
| UI, tela, componente, layout | `/frontend-ui` | dev-uiux · dev-next |
| UX, usabilidade, fluxo de tela | `/uiux-basic` | dev-uiux |
| Figma, implementar design, design-to-code | `/uiux-figma` (Figma MCP) | dev-uiux |
| acessibilidade, a11y, WCAG, teclado, leitor | `/a11y` | dev-uiux |
| browser vs server, runtime JS, edge, RN, bundle | `/javascript-platform` | dev-next |
| Docker, CI/CD, deploy, pipeline, rollout | `/devops-delivery` | dev-devops |
| segurança, authz, webhook, segredo, CORS, trust | `/infra-security` | dev-devops · security-auditor |
| auditar, code audit, revisar PR a fundo | `/code-audit` | qa-engineer · code-reviewer |
| QA, qualidade, critério de aceite, teste | `/qa-review` | qa-engineer |
| pronto?, go/no-go, release, deploy | `/release-readiness` | qa-engineer |
| métrica, KPI, analisar dados, gráfico | `/data-analysis` | data-analyst |
| domínio MailerWeb, consentimento, quota, deliverability | `/mailerweb-domain` | mailerweb-bridge |
| montar prompt, padronizar pedido pra IA | `/prompt-library` | context-economist |
| grafo de código, quem chama quem | `/graphify` | context-economist |
| fim de sessão, registrar aprendizado | `/journal` | — |
| comprimir saída / subagent cirúrgico | `/caveman` `/cavecrew` | cavecrew-* |

> Regra: **1 tarefa → 1 agent dono**; agent puxa as skills da coluna. Não rodar todos os agents sempre (custo). Antes de contexto pesado → [[context-economist]]. Domínio MailerWeb sempre read-only ([[_mailerweb-access]]).

Ver [[toolbox-guide]] · [[routing]] · [[flow]] · [[_toolbox]].
