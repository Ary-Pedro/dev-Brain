---
type: meta
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: stable
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [know, meta, mailerweb, read-only]
aliases: [mailerweb-access, mailerweb-readonly]
---

# _mailerweb-access — mailerweb-brain é SOMENTE LEITURA

> Regra dura, sem exceção. Vale pra Claude, agents e qualquer skill/hook.

## A regra

`~/devSpace/mailerWeb/mailerweb-brain/` é um **sistema a ser CONSULTADO**, nunca gravado.

- ❌ **NUNCA** criar, editar, mover, renomear ou deletar arquivo em `mailerweb-brain/`.
- ❌ NUNCA rodar `git`/commit nele. É controlado pelo **git da empresa** — qualquer escrita local vira conflito/ruído no repo deles.
- ✅ **Só** ler: `Read`, `Grep`, `Glob` sobre `apps/*.md`, `eventos/`, etc.
- ✅ Toda **saída** (correção, nota, lição, mapa, link) vai pro **dev-Brain**, nunca pro mailerweb-brain.

## Por quê

- mailerweb-brain = **task/domain memory** da empresa, versionado por eles. Fonte externa.
- dev-Brain = **só toca em si mesmo**, 100% mantido pelo Claude (hooks + skills + agents).
- Achou vício/erro no domínio? Registra em [[corrections]] (dev-Brain), não conserta lá.

## Quem obedece

- [[mailerweb-bridge]] — já é read-only por design (`tools: Read, Grep, Glob`, sem Write).
- [[dev-django]] · [[dev-spring]] · [[dev-next]] — têm Write/Edit pra **código dos repos**, mas **proibidos** de escrever em `mailerweb-brain/`.
- Skill `/journal`, hooks de sync/journal — escrevem **só** em `dev-Brain/`.

Ver [[routing]] · [[_strategy]] · [[mailerweb-bridge]].
