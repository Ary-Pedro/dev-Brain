---
tags: [meta, agent, python]
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

# agent: dev-django

> Spec do stack-agent Python/Django. Agent real (dispatchável) em `~/.claude/agents/dev-django.md`.

## O que é

Dev sênior Python/Django. Coda, revisa e refatora Python/Django aplicando o padrão da casa: apps coesos, fat models com invariantes, `selectors` (leitura) / `services` (escrita), `serializers` DRF, views finas, Celery em `tasks`, ORM sem N+1, multi-tenancy, migrations seguras e testes (pytest / Django `TestCase`).

## Quando o Claude usa

- Tarefa for **codar / revisar / refatorar Python/Django**.
- Projetos: [[mailerweb-panel-v2]] (Django 5 multi-tenant + DRF + Celery) e mailerweb-portal.
- Não usar para pergunta de domínio pura (onde está X, qual a regra Y) — isso é a ponte de domínio, ver [[mailerweb-bridge]].

Ver a árvore de decisão em [[routing]].

## O que ele lê (antes de codar)

1. [[routing]] — qual brain consultar.
2. Universais em `know/`: [[_principles]], [[code-style]], [[naming]], [[docstrings]], [[testing]], [[error-handling]], [[security]], [[performance]].
3. A nota de stack: [[python-django]].

Padrão do dev-Brain **vence** vício local. Imita o padrão já no repo. Menor diff possível.

## Como trata o domínio MailerWeb

Subagent **não despacha** outro subagent — logo o `dev-django` **não** chama a ponte. Quando a tarefa está em `~/devSpace/mailerWeb/` e precisa de domínio, ele lê **direto** `~/devSpace/mailerWeb/mailerweb-brain/` (`apps/<x>.md`, `eventos/`). Nunca varre o monolito inteiro. A racional da separação padrão↔domínio está em [[mailerweb-bridge]].

Fora do mailerWeb: não cita MailerWeb (anti-alucinação). Vício achado no domínio → nota em [[corrections]], não copiado.

## Entrega

Diff mínimo + 1 linha citando a nota de padrão aplicada (ex.: `[[python-django]] + [[performance]]`).

Relacionado: [[dev-next]] · [[dev-spring]] — stack-agents irmãos (mesma persona, stacks diferentes, leem o mesmo `know/`).

Ver [[python-django]] · [[mailerweb-panel-v2]] · [[routing]] · [[00-index]].
