---
type: decision
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: active
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [decision, adr, architecture, mailerweb]
aliases: [ADR-0001]
---

# ADR-0001 — Dois cérebros; mailerweb-brain read-only

- **Status:** aceita
- **Data:** 2026-06-19

## Contexto

Existem dois vaults: `dev-Brain` (mantido 100% pelo Claude) e `mailerweb-brain` (git da empresa, gerado do código). Misturar padrão de engenharia com domínio MailerWeb num só lugar gera duplicação, alucinação fora do contexto MailerWeb e custo de token (reler monólito ~200k).

## Decisão

Separar em dois cérebros com papéis fixos: **dev-Brain = policy + architecture** (o COMO, escrevível); **mailerweb-brain = domínio** (o ONDE/QUÊ, **read-only**). Domínio MailerWeb é consultado via agent [[mailerweb-bridge]], nunca duplicado no dev-Brain. Padrão de engenharia (dev-Brain) **vence** em conflito.

## Alternativas descartadas

- **Um vault único** — vira hub falso, recall ruim, mistura política com domínio.
- **IA escreve no mailerweb-brain** — é produto da empresa; risco de alterar doc sensível. Inaceitável.

## Consequências

- Economia de token: agente consulta o mapa certo, não relê o monólito.
- Anti-alucinação: fora do mailerWeb, não citar apps/fluxos MailerWeb.
- Custo: exige disciplina de roteamento ([[routing]]) e o porteiro [[context-economist]].

Ver [[_strategy]] · [[_mailerweb-access]] · [[routing]].
