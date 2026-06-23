---
tags: [meta, agent, mailerweb]
type: agent
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: stable
confidence: high
last_verified: 2026-06-19
token_policy: full
---

# agent: mailerweb-bridge

> Spec da ponte de domínio. Agent real em `~/.claude/agents/mailerweb-bridge.md` (dispatchável).

## Por que existe

dev-Brain governa o **COMO** (universal). Quando uma tarefa no mailerWeb precisa do **domínio** (apps, fluxos, eventos, regras), o dev-Brain **não absorve** esse contexto dentro de si — delega ao `mailerweb-bridge`, que lê só `mailerweb-brain` e devolve fato comprimido.

Ganho: janela de contexto do dev-Brain fica enxuta; sem duplicar o universo MailerWeb; sem alucinar.

## Quando o Claude usa

- Tarefa sob `~/devSpace/mailerWeb/` **e** precisa saber onde/o-que/regra.
- Em vez de varrer `mailerweb.panel.v2` (~200k tokens) ou copiar contexto pra cá.

Ver árvore de decisão em [[routing]].

## Fluxo de correção (vícios → dev-Brain)

```
mailerweb-bridge lê mailerweb-brain
   └── achou anti-padrão (docstring/naming/camada/...)?
         ├── NÃO conserta (read-only)
         └── reporta "## ⚠️ correções p/ dev-Brain"
                └── vira nota em know/corrections/  (ver [[corrections]])
                      └── aplicada depois, em contexto MailerWeb, por quem for codar lá
```

Correção mora no **dev-Brain** (padrão), aplicada no **mailerWeb** (domínio). Separação mantida.

## Stack-agents (ativos)

[[dev-django]] · [[dev-spring]] · [[dev-next]] — cada um lê [[python-django]]/[[java-spring]]/[[typescript-next]] + universais. Para domínio MailerWeb, lêem `mailerweb-brain` direto (subagent não despacha subagent).

Ver [[00-index]] · [[routing]].
