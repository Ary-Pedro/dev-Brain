---
tags: [meta, agent, typescript]
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

# dev-next

## O que é

Stack-agent dispatchável de dev sênior **TypeScript/Next.js**. É a persona que o Claude assume para escrever, revisar e refatorar código TS/Next.js de produção, aplicando o padrão do dev-Brain com precedência sobre vício local e entregando o menor diff possível.

O agent real (system prompt + frontmatter) vive em `~/.claude/agents/dev-next.md`. Esta nota é só a spec/documentação dele no vault.

## Quando o Claude usa

- Tarefa de **codar / revisar / refatorar TypeScript ou Next.js**.
- Projetos cobertos: [[meudinheiro-v2]] (meuDinheiroNaMaoV2).
- Tópicos típicos: App Router (server vs client components), server actions, tipos estritos, Zod na borda, Prisma sem N+1, boundaries `error.tsx`/`loading.tsx`, testes com Vitest + Testing Library.

## O que ele lê (ANTES de codar)

1. [[routing]] — `dev-Brain/routing.md`, o mapa de roteamento que diz onde achar cada coisa.
2. Notas **universais** em `know/`: [[_principles]], [[code-style]], [[naming]], [[docstrings]], [[testing]], [[error-handling]], [[security]], [[performance]].
3. A nota da própria stack: [[typescript-next]] (`know/typescript-next`).

O padrão do dev-Brain tem **precedência** sobre o vício local — o agent imita o padrão já existente no repo e faz o diff mínimo.

## Como trata o domínio MailerWeb

Um subagent **não pode despachar outro subagent**. Então, quando a tarefa toca o domínio MailerWeb, o dev-next lê **direto** o `~/devSpace/mailerWeb/mailerweb-brain/` (`apps/<x>.md`, `eventos/`) para descobrir regra de negócio, fluxo de evento ou localização de código — em vez de varrer o monolito inteiro. Ver [[mailerweb-bridge]].

Fora do mailerWeb, o agent não cita MailerWeb (anti-alucinação). Vício consolidado achado no domínio é registrado em `know/corrections/`, não copiado.

## Links

- [[typescript-next]] — nota de padrão da stack
- [[meudinheiro-v2]] — projeto coberto
- [[routing]] — mapa de roteamento lido antes de codar
- [[mailerweb-bridge]] — como acessar o domínio MailerWeb
- [[dev-django]] · [[dev-spring]] — stack-agents irmãos (mesma persona, stacks diferentes)
- [[00-index]] — índice do vault
