---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: ai
status: active
tags: [know, corrections]
aliases: [corrections]
---

# corrections — vícios detectados, correções a aplicar

> Registro de anti-padrões achados no código/brain do devSpace que violam o `know/`.
> A correção mora aqui (dev-Brain = padrão); é aplicada no projeto/contexto certo por quem coda.

## De onde vêm

- `mailerweb-bridge` (seção `## ⚠️ correções p/ dev-Brain`) → vícios no universo MailerWeb.
- Recon de `map/` → ex.: [[faculdade-alessandro]] tem `Models/` na raiz fora de convenção ([[java-spring]]).
- Code review manual.

## Convenção de arquivo

`corrections/<escopo>-<slug>.md` — ex.: `mailerweb-docstring-services.md`, `faculdade-package-naming.md`.

Frontmatter: `tags: [know, corrections, <escopo>]`. Corpo:

```
# <vício curto>
- **Onde:** <projeto/app/arquivo>
- **Viola:** [[know/<nota>]]
- **Correção:** <o que fazer>
- **Status:** aberto | aplicado
```

## Abertas

- [[mailerweb-docstrings]] — padrão de docstring/comentário do MailerWeb (refina [[docstrings]]/[[comments]]): `Note:` obrigatório p/ except capturado, corpo p/ lógica não-trivial, linha **120** (não 79), comentário inline curto. Vício recorrente da IA.

Ver [[routing]] · [[mailerweb-bridge]].
