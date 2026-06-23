---
tags: [meta, agent]
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

# agent: context-economist

> Spec do economista de contexto. Agent real (dispatchável) em `~/.claude/agents/context-economist.md`.

## O que é

Camada operacional que decide o **menor conjunto de fontes** para responder uma tarefa no devSpace, minimizando tokens. Roda **antes** de carregar contexto pesado. Não coda, não responde a tarefa — entrega um **plano de leitura** + estimativa de peso. Tools: `Read`, `Grep`, `Glob` (leitura pura).

## Por que existe

A janela de contexto é o recurso escasso. Sem um porteiro, o Claude tende a abrir repo inteiro, `graph.json` cru ou notas demais. O `context-economist` corta isso na entrada: lê o `token_weight` do projeto e o [[routing]], e devolve só o estritamente necessário. Casa com a divisão de dois cérebros de [[_strategy]] — economiza latência + tokens sem duplicar domínio.

## Quando o Claude usa

- **Antes** de qualquer tarefa que possa puxar contexto pesado (varredura de repo, grafo, vários projetos).
- Quando não está claro **quais** fontes abrir nem **quanto** custam.
- Especialmente em projetos de `token_weight` alto/crítico (ex.: [[mailerweb-panel-v2]]).

Árvore de decisão de roteamento em [[routing]].

## Regra de tiers (por token_weight)

Lê o `token_weight` da nota do projeto (em `dev-Brain/projects/<slug>.md`; hoje os mapas vivem em `map/<slug>.md`) e aplica:

| Tier | Plano |
|------|-------|
| **baixo** | resumo + no máx. **2 notas** específicas |
| **médio** | **digest** (`graph/<slug>.digest.json`) + **graphify query** dirigida |
| **alto** | **não abrir tudo** → delegar a [[mailerweb-bridge]] / stack-subagent; só notas pontuais |
| **crítico** | **exigir plano antes de ler mais**; NUNCA abrir repo inteiro |

## Preferências duras

- Sempre **digest** (`graph/<slug>.digest.json`) em vez de `graph.json` cru.
- **graphify query** > leitura sequencial para perguntas de relação ("onde/como").
- 🔒 **mailerweb-brain é SOMENTE LEITURA** — só consultar, nunca gravar.
- Toda saída/escrita só em **dev-Brain**.

## Entrega

1. Lista mínima de fontes (caminhos exatos, em ordem).
2. Estimativa de peso (tier + ordem de grandeza).
3. Se cabível: delegar a [[mailerweb-bridge]] ou stack-subagent em vez de abrir contexto pesado.

## Projetos governados

[[mailerweb-panel-v2]] · [[mailerweb-portal]] · [[meudinheiro-v2]] · [[prontuario]] · [[faculdade-alessandro]] · [[faculdade-atvdd]] · [[theds-panel]] · [[wiks]]

Relacionado: [[brain-architect]] — camada operacional irmã (porteiro de contexto vs curadoria do vault).

Ver [[routing]] · [[_strategy]] · [[00-index]].
