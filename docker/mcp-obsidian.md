---
type: note
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: active
last_verified: 2026-06-19
token_policy: full
tags: [meta, mcp, obsidian]
---

# MCP Obsidian — acesso vivo Claude ↔ vault

## Objetivo

Claude lê e escreve o vault **em tempo real** via plugin **Local REST API** do Obsidian. Sem isso, Claude só enxerga o que está montado no filesystem; com o MCP, ele opera sobre o Obsidian rodando (busca, edição, append, dataview), respeitando o estado vivo do app.

## Passos

1. **No Obsidian** → Settings → Community Plugins → instalar **"Local REST API"** → ativar → copiar a **API key** → habilitar **HTTPS** (porta padrão **27124**).
2. **No Claude Code** → adicionar o MCP server com o bloco de config abaixo.

## Config EXATA

```json
{
  "mcpServers": {
    "obsidian": {
      "type": "http",
      "url": "https://127.0.0.1:27124/mcp/",
      "headers": { "Authorization": "Bearer <API_KEY>" }
    }
  }
}
```

Trocar `<API_KEY>` pela key copiada no passo 1.

## Pendência: expor a porta no Docker

O container roda o Obsidian. A porta **27124** do plugin precisa ser **exposta no `docker-compose`** para o Claude no host alcançar o endpoint:

```yaml
ports:
  - "27124:27124"
```

> [!todo] Passo pendente
> Mapear `27124:27124` no `docker-compose` do serviço Obsidian. Sem isso, `https://127.0.0.1:27124/mcp/` não responde do host.

## Roteamento p/ CLAUDE.md

- **Domínio MailerWeb** → `mailerweb-brain` primeiro.
- **Padrões / cross-repo** → `dev-Brain`.

Relacionado: [[obsidian-plugins]] — shortlist de plugins; o Local REST API exigido aqui é o pré-requisito deste MCP.

Ver [[_strategy]] e [[routing]].
