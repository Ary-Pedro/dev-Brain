---
type: lesson
scope: cross-repo
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: ai
status: active
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [lesson, claude-code]
keywords: [claude-code, agents, hooks, sessionstart, boot, registry]
aliases: [claude-agents-load-on-boot]
---

# Claude Code: agents/hooks novos não carregam na sessão atual

## Contexto
Criar um agent em `~/.claude/agents/` ou adicionar um hook no `settings.json` no MEIO de uma sessão ativa do Claude Code.

## Sintoma
```
Agent type X not found
```
O agent recém-criado (ou o hook recém-adicionado) não está disponível na sessão atual.

## Causa
O registry de agents + hooks é lido no `SessionStart`. Mudanças feitas depois do boot não são recarregadas durante a sessão.

## Solução
Reiniciar o Claude Code para que o registry seja relido no novo `SessionStart`.

## Evitar futuro
Antes de depender do novo agent/hook, validar:
- Frontmatter do agent válido: `name` / `description` / `tools`.
- Testar o hook manualmente: `echo JSON | node hook.js`.

Visto em: [[daily/2026-06-19]]
