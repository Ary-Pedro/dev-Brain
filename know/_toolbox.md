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

Última sync: 2026-06-23T19:01:13.443Z

## Skills (3)

| Skill | Descrição | Origem |
|-------|-----------|--------|
| `agent-workbench` |  | user |
| `graphify` | Use for any question about a codebase, its architecture, file relationships, or project content — es | user |
| `journal` | Resume a sessão atual no dev-Brain — cria/atualiza a daily note (problema→solução, decisões, keyword | user |

## Agents (9)

| Agent | Descrição | Origem |
|-------|-----------|--------|
| `brain-architect` | Mantém a saúde do dev-Brain: frontmatter padrão ([[_frontmatter]]), links/MOCs, triagem de missing-l | user |
| `cavecrew-builder` | Surgical 1-2 file edit. Typo fixes, single-function rewrites, mechanical | plugin |
| `cavecrew-investigator` | Read-only code locator. Returns file:line table for "where is X defined", | plugin |
| `cavecrew-reviewer` | Diff/branch/file reviewer. One line per finding, severity-tagged, no praise, | plugin |
| `context-economist` | <Decide o MENOR conjunto de fontes p/ responder uma tarefa no devSpace, minimizando tokens. Use ANTE | user |
| `dev-django` | Dev sênior Python/Django. Use quando a tarefa for codar/revisar/refatorar Python/Django (projetos: m | user |
| `dev-next` | Dev sênior TypeScript/Next.js. Use quando a tarefa for codar, revisar ou refatorar TypeScript/Next.j | user |
| `dev-spring` | Dev sênior Java/Spring Boot. Use quando a tarefa for codar, revisar ou refatorar Java/Spring Boot —  | user |
| `mailerweb-bridge` | Ponte read-only para o domínio MailerWeb. Responde "onde está X", "o que é o fluxo Y", "qual a regra | user |

## Plugins (1)

- `caveman@caveman`

## Commands (0)

_nenhum_
