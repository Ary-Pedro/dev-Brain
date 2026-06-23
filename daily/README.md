---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: human
status: stable
tags: [meta, daily]
---

# daily — diário de sessões

> Uma nota `YYYY-MM-DD.md` por dia. Cada sessão vira um bloco.
> Equivalente ao **Daily Notes** do Obsidian, mas alimentado por Claude.

## Dois mecanismos

1. **Hook SessionEnd** (`dev-brain-journal.js`) → breadcrumb automático: tópicos (prompts) + arquivos tocados. Sempre roda, sem LLM.
2. **Skill `/journal`** → resumo rico (problema→solução, decisões, keywords) + extrai [[lessons/README|lições]] reutilizáveis. Rodar ao fim da sessão.

## Fluxo recomendado

Fim de sessão → `/journal` (resumo completo). Se esquecer, o hook já deixou o breadcrumb.

Ver [[00-index]] · lições em `know/lessons/`.
