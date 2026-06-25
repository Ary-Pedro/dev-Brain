---
type: note
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: draft
confidence: med
last_verified: 2026-06-23
token_policy: full
tags: [meta, mcp, database]
---

# MCP database — schema vivo p/ a skill /dba-mcp

> Ponte read-only entre Claude e o banco, p/ a skill `/dba-mcp` inspecionar schema REAL. Alinhado [[0003-stack-e-fluxo-2026-06|ADR-0003]]: **só localhost, read-only, sem expor porta**. Status: **draft** — ativar quando precisar (exige credencial, que você adiciona).

## Princípio
A skill `/dba-mcp` **só lê** schema (tabelas/constraints/índices). NUNCA roda DDL/DML nem toca dado prod sem autorização explícita. Sem MCP configurado → cai pra `/dba-basic` (análise estática).

## Config (você adiciona com a credencial — não versionar)
Em `~/.claude/settings.json`, bloco `mcpServers` (use um MCP de Postgres/MySQL read-only; ex. `@modelcontextprotocol/server-postgres` ou equivalente):

```json
{
  "mcpServers": {
    "db-dev": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://READONLY_USER:***@127.0.0.1:5432/app_dev"]
    }
  }
}
```

Regras duras:
- Usuário **read-only** no banco (GRANT SELECT apenas). Nunca o user de escrita/admin.
- Apontar p/ **dev/staging**, nunca prod (salvo tarefa que autorize explicitamente).
- Connection string com segredo **fora do git** (`settings.json` é versionado — use `settings.local.json`, que é gitignored, ou env).
- `127.0.0.1` only. Não expor porta no Docker.

## Figma MCP (já conectado)
A skill `/uiux-figma` usa o **Figma MCP** (já ativo nesta sessão via claude.ai). Tools: `get_design_context`, `get_screenshot`, `get_variable_defs`, `get_code_connect_map`. Skill `/figma-use` antes de `use_figma`. Nada a configurar.

Ver [[mcp-obsidian]] (outro MCP, adiado) · [[obsidian-plugins]] · [[toolbox-guide]].
