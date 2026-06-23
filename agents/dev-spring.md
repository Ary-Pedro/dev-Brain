---
tags: [meta, agent, java]
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

# dev-spring

## O que é

Stack-agent dispatchável de **Java / Spring Boot** — um dev sênior que coda, revisa e refatora código Spring Boot (camadas Controller/Service/Repository/Entity/DTO, JPA, REST, Bean Validation, JUnit/Mockito). O agent real vive em `~/.claude/agents/dev-spring.md`.

## Quando o Claude usa

Quando a tarefa for **codar, revisar ou refatorar Java/Spring Boot**, especialmente nos projetos [[prontuario]] e [[faculdade-alessandro]]. O Claude despacha este subagent ao detectar trabalho de backend Java/Spring.

## O que ele lê (antes de codar)

1. [[routing]] — `/home/pedroczar/devSpace/dev-Brain/routing.md`, para roteamento e contexto.
2. Notas **universais** de `know/`: [[_principles]] [[code-style]] [[naming]] [[docstrings]] [[testing]] [[error-handling]] [[security]] [[performance]].
3. Nota da stack: [[java-spring]].

O padrão do dev-Brain tem **precedência** sobre vício local; o agent imita o padrão já existente no repo e entrega o **menor diff possível**.

## Domínio MailerWeb

Um subagent **não pode despachar outro subagent**. Por isso, para regra/fluxo/localização do domínio MailerWeb, o dev-spring lê **direto** `~/devSpace/mailerWeb/mailerweb-brain/` (`apps/<x>.md`, `eventos/`) — nunca varre o monolito inteiro. Ver [[mailerweb-bridge]]. Fora do mailerWeb não cita MailerWeb (anti-alucinação). Vício achado no domínio é registrado em `know/corrections/`, não copiado.

## Entrega

Diff mínimo + 1 linha citando qual nota de padrão foi aplicada.

## Links

- [[java-spring]]
- [[prontuario]]
- [[faculdade-alessandro]]
- [[dev-django]] · [[dev-next]] — stack-agents irmãos (mesma persona, stacks diferentes)
- [[routing]]
- [[00-index]]
