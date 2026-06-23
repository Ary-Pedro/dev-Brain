---
type: note
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: stable
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [know, git]
---

# git-commits — Commits e branches

> PADRÃO universal de histórico Git no devSpace. Vale para qualquer stack: Python/Django, Java/Spring, TypeScript/Next. Ver também [[_principles]], [[naming]], [[testing]].

Um histórico Git é documentação executável. Commit ruim apaga o "porquê" e custa caro no `git blame` seis meses depois. Aqui não se negocia.

## Conventional Commits (obrigatório)

Formato:

```
<tipo>(<escopo opcional>): <subject>

<body opcional>

<footer obrigatório neste workspace>
```

Tipos permitidos:

| Tipo | Quando usar |
|------|-------------|
| `feat` | Nova funcionalidade visível ao usuário/API |
| `fix` | Correção de bug |
| `chore` | Build, deps, config, tarefas sem efeito em runtime |
| `refactor` | Mudança de código sem alterar comportamento |
| `docs` | Só documentação |
| `test` | Só testes (adiciona/ajusta, sem mudar produção) |

Regra: se a mudança muda comportamento, é `feat` ou `fix` — nunca `refactor`/`chore`.

## Regras do subject

- **<= 50 caracteres.**
- **Imperativo presente**: "adiciona", "corrige", "remove" (não "adicionado", "adicionando", "adiciona X e foi testado").
- Sem ponto final.
- Minúscula depois do `:`.
- Escopo entre parênteses quando ajuda a localizar (`feat(auth):`, `fix(billing):`).

```text
# BOM
feat(auth): adiciona login via magic link
fix(billing): corrige arredondamento de imposto
refactor(api): extrai validação de payload

# RUIM
feat: Adicionado novo login e ajustes gerais no projeto.   # passado, ponto final, vago, >50
update                                                       # sem tipo, sem informação
fix: bug                                                     # diz nada
```

## Regras do body

- O subject diz **o quê**. O body explica **o porquê** — a razão da mudança, o trade-off, o contexto que o diff não mostra.
- Não reescreva o diff em prosa. Quem lê o body já vê o `git diff`.
- Linha em branco separando subject do body. Quebre linhas ~72 chars.
- Body é opcional quando o "porquê" é óbvio pelo subject (ex.: bump de versão).

```text
# BOM (o porquê não está no diff)
fix(cache): invalida cache de tenant ao trocar plano

O plano define limites de envio. Sem invalidar, o tenant
continuava com o limite antigo até o TTL expirar (15min),
liberando envios acima da cota recém-reduzida.

# RUIM (body só repete o diff)
fix(cache): invalida cache

Mudei a função para chamar cache.delete() na linha 42.
```

## Commit atômico

Um commit = uma mudança lógica coesa. Deve poder ser revertido sozinho sem quebrar nada nem deixar lixo.

- Nada de "WIP" ou "ajustes" no histórico final.
- Não misture refactor com feature no mesmo commit. Separe.
- Se o subject precisa de "e" para descrever o commit, provavelmente são dois commits.

```text
# RUIM — um commit, três assuntos
feat: adiciona export CSV, corrige typo no header e atualiza lib X

# BOM — três commits atômicos
feat(report): adiciona export CSV
docs(report): corrige typo no header da tabela
chore(deps): atualiza lib X para 2.1.0
```

## Branch por feature

- Uma branch por unidade de trabalho (feature, fix, chore). Nunca commitar direto na branch padrão (`main`/`master`).
- Nomeie por tipo + descrição curta em kebab-case, alinhado a [[naming]]:

```text
feat/magic-link-login
fix/billing-tax-rounding
chore/bump-django-5.1
```

- Branch curta e focada. Abriu PR, mergeou, deletou. Branch longa = conflito garantido.

## Footer obrigatório deste workspace

**Toda mensagem de commit DEVE terminar com este trailer:**

```text
Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

Exemplo completo de commit válido no devSpace:

```text
feat(auth): adiciona login via magic link

Substitui senha por token de uso único enviado por e-mail.
Reduz superfície de ataque (sem hash de senha em repouso) e
elimina o fluxo de reset de senha.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

## Checklist antes de commitar

- [ ] Tipo correto (`feat`/`fix`/`chore`/`refactor`/`docs`/`test`)?
- [ ] Subject <= 50 chars, imperativo, sem ponto final?
- [ ] Body explica o **porquê** (ou é óbvio)?
- [ ] Commit é atômico (uma mudança lógica)?
- [ ] Está numa branch de feature, não na default?
- [ ] Trailer `Co-Authored-By` presente?
