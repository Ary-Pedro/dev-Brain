---
type: meta
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: ai
status: active
token_policy: summary-first
tags: [meta, toolbox]
---

# _toolbox — skills, agents, plugins disponíveis

> Gerado automaticamente pelo hook `dev-brain-sync.js` a cada SessionStart.
> NÃO editar à mão — reescrito toda sessão. Drift registrado em `.sync/changelog.md`.
>
> dev-Brain usa esta lista para **sugerir** skill/plugin/agent certo por tarefa. Ver [[routing]].

Última sync: 2026-06-25T17:38:18.862Z

## Skills (29)

| Skill | Descrição | Origem |
|-------|-----------|--------|
| `a11y` | Auditoria e aplicação de acessibilidade (WCAG) em UI — HTML semântico, teclado, foco, contraste, for | user |
| `agent-workbench` |  | user |
| `api-design` | Desenho de API/contrato — recursos REST, verbos/status corretos, formato de erro consistente, idempo | user |
| `architecture-modeling` | Converte pedido ambíguo de arquitetura/modelagem em guia de design conceitual, lógico e físico — fro | user |
| `backend-layering` | Revisa/modela backend em camadas com fronteiras explícitas — transport (controller), domínio (servic | user |
| `code-audit` | Audita plano, diff ou branch em 6 dimensões — correção, segurança, concorrência, performance, observ | user |
| `data-analysis` | Estrutura coleta de dados, métricas, gráficos e interpretação quantitativa com grão (grain) explícit | user |
| `db-design` | Desenha schema e plano de migration a partir de processo de negócio, atores e padrões de acesso (sem | user |
| `dba-basic` | Revisa entidades, chaves, índices e decisões de SQL quando NÃO há acesso a banco vivo — análise está | user |
| `dba-mcp` | Inspeciona schema de banco VIVO via MCP de banco de dados (read-only) e transforma os achados em gui | user |
| `design-patterns` | Catálogo de padrões de projeto aplicado — quando USAR e quando EVITAR (GoF + arquiteturais como Repo | user |
| `devops-delivery` | Modela/revisa CI/CD, containers, ambientes, secrets, rollout, rollback, observabilidade e validação  | user |
| `frontend-ui` | Implementa/revisa fluxos de UI com atenção a acessibilidade, responsividade, os 4 estados, copy, tip | user |
| `fullstack-feature` | Estrutura ou revisa uma feature que cruza UI, backend, contratos, dados, validação e rollout — pra i | user |
| `graphify` | Use for any question about a codebase, its architecture, file relationships, or project content — es | user |
| `infra-security` | Revisa backend/integração quanto a fronteiras de protocolo, controle de acesso, fronteiras de confia | user |
| `javascript-platform` | Revisa/modela trabalho em JavaScript/TypeScript de plataforma — browser, Node.js, PWA, React Native, | user |
| `journal` | Resume a sessão atual no dev-Brain — cria/atualiza a daily note (problema→solução, decisões, keyword | user |
| `mailerweb-domain` | Aplica as regras de domínio MailerWeb — consentimento/opt-in, quotas/rate, webhooks, deliverability  | user |
| `poo` | Modelagem orientada a objetos de qualidade — encapsulamento, composição sobre herança, coesão/acopla | user |
| `process-modeling` | Transforma ambiguidade de processo de negócio em artefatos — documento de visão, mapa de stakeholder | user |
| `prompt-library` | Transforma pedido vago em prompt curto e reutilizável com as skills certas, agents, testes e critéri | user |
| `python-clean` | Implementa/refatora serviços Python com contratos fortes, funções pequenas, erros explícitos, type h | user |
| `qa-review` | Gate de QA padronizado (ISO/IEC 25010) — valida prontidão de entrega nas 6 dimensões de qualidade (a | user |
| `refactor` | Workflow de refatoração SEGURA — rede de testes de caracterização, passos pequenos reversíveis, verd | user |
| `release-readiness` | Avalia se uma mudança está REALMENTE pronta p/ merge/release/deploy — cobertura de escopo, evidência | user |
| `solid` | Aplica e audita os 5 princípios SOLID em código OO (Python/Java/TypeScript). Use ao projetar uma cla | user |
| `uiux-basic` | Análise de UX/UI sem ferramenta externa — qualidade de fluxo, avaliação heurística, carga cognitiva, | user |
| `uiux-figma` | Extrai guia de UX/UI do Figma via MCP quando o arquivo de design é a fonte de verdade — tokens, layo | user |

## Agents (17)

| Agent | Descrição | Origem |
|-------|-----------|--------|
| `architect` | Arquiteto de software. Use ao desenhar sistema/módulo/feature complexa, decidir estrutura, avaliar t | user |
| `brain-architect` | Mantém a saúde do dev-Brain: frontmatter padrão ([[_frontmatter]]), links/MOCs, triagem de missing-l | user |
| `cavecrew-builder` | Surgical 1-2 file edit. Typo fixes, single-function rewrites, mechanical | plugin |
| `cavecrew-investigator` | Read-only code locator. Returns file:line table for "where is X defined", | plugin |
| `cavecrew-reviewer` | Diff/branch/file reviewer. One line per finding, severity-tagged, no praise, | plugin |
| `context-economist` | <Decide o MENOR conjunto de fontes p/ responder uma tarefa no devSpace, minimizando tokens. Use ANTE | user |
| `data-analyst` | Analista de dados. Use ao definir/validar métrica ou KPI, montar relatório/dashboard de dados, inter | user |
| `dev-dba` | DBA / engenheiro de dados sênior. Use quando a tarefa for modelar schema, escrever/otimizar query, c | user |
| `dev-devops` | Engenheiro DevOps/infra sênior. Use quando a tarefa for Docker/Compose, CI/CD (GitLab/GitHub Actions | user |
| `dev-django` | Dev sênior Python/Django. Use quando a tarefa for codar/revisar/refatorar Python/Django (projetos: m | user |
| `dev-next` | Dev sênior TypeScript/Next.js. Use quando a tarefa for codar, revisar ou refatorar TypeScript/Next.j | user |
| `dev-spring` | Dev sênior Java/Spring Boot. Use quando a tarefa for codar, revisar ou refatorar Java/Spring Boot —  | user |
| `dev-uiux` | Dev de UI/UX & front craft sênior. Use quando a tarefa tocar interface, acessibilidade (WCAG/a11y),  | user |
| `mailerweb-bridge` | Ponte read-only para o domínio MailerWeb. Responde "onde está X", "o que é o fluxo Y", "qual a regra | user |
| `process-analyst` | Analista de processo/requisitos (BPM + engenharia de requisitos). Use ANTES de codar feature nova/am | user |
| `project-watcher` | Observador de projetos ativos (monitor) do devSpace. Use para gerar um panorama do que está acontece | user |
| `qa-engineer` | Engenheiro de QA / gate de qualidade. Use para validar prontidão de uma entrega antes de merge/relea | user |

## Plugins (1)

- `caveman@caveman`

## Commands (0)

_nenhum_
