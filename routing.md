---
type: meta
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: stable
last_verified: 2026-06-19
token_policy: full
tags: [meta, routing]
---

# routing — qual brain consultar

> Regra que o Claude segue **antes** de codar no devSpace.

## Árvore de decisão

```
O alvo está em ~/devSpace/mailerWeb/ ?
├── SIM
│   ├── pergunta de DOMÍNIO (onde está regra X, qual app, fluxo auth/billing)?
│   │     → mailerweb-brain PRIMEIRO, via agent [[mailerweb-bridge]] (task/domain memory)
│   ├── pergunta de PADRÃO (naming, testes, segurança, cross-repo)?
│   │     → dev-Brain know/ (policy/architecture memory)
│   ├── NÃO duplicar domínio MailerWeb aqui — delegar ao bridge (economia de contexto)
│   └── conflito de padrão? dev-Brain VENCE. Vício → nota em [[corrections]].
└── NÃO → SÓ dev-Brain. NÃO citar apps/fluxos/regras MailerWeb. (anti-alucinação)
```

> Por que essa ordem: dev-Brain = **policy + architecture** (geral, prescritivo, coerência cross-projeto). mailerweb-brain = **task + domain** (curado, operacional, menos latência/tokens). Detalhe em [[_strategy]].

> 🔒 **mailerweb-brain é SOMENTE LEITURA** — consultar, nunca gravar (git da empresa). dev-Brain só toca em si mesmo, 100% mantido pelo Claude. Regra dura em [[_mailerweb-access]].

> Skills/agents/plugins disponíveis para sugerir: ver [[_toolbox]] (mantido pelo hook `dev-brain-sync.js` a cada sessão).

## Sempre (qualquer projeto)

Aplicar `know/`:
- [[_principles]] — como pensar antes de escrever
- [[code-style]], [[naming]], [[docstrings]]
- [[git-commits]], [[testing]], [[error-handling]], [[security]]

## Por stack detectada

| Stack | Nota de padrão | Projetos |
|-------|---------------|----------|
| Python / Django | [[python-django]] | mailerweb.panel.v2 |
| Java / Spring | [[java-spring]] | prontuario, faculdade_alessandro |
| TypeScript / Next | [[typescript-next]] | meuDinheiroNaMaoV2 |

Ver inventário completo em [[00-index]] e detalhe por projeto em `map/`.

## Precedência de conflitos

1. **dev-Brain `know/`** — padrão de engenharia. Inviolável.
2. **CLAUDE.md do projeto** — regras locais que não conflitam com (1).
3. **mailerweb-brain** — domínio/localização. Nunca sobrepõe padrão.

Se mailerweb-brain documenta um anti-padrão (ex.: docstring fora do estilo), dev-Brain **marca para correção** — não copia o vício.
