---
tags: [lesson, git, workflow]
keywords: [pre-prod, staging, main, branch, referência, comparação]
aliases: [pre-prod-staging-nao-e-main]
---

# "Pre-prod" no contexto MailerWeb = staging com branch deployado, não main

**Contexto:** User pede para "manter igual ao pre-prod" e mostra screenshot de `staging.app.mailerweb.com.br`.

**Sintoma:** Claude compara com `git show main:arquivo` e não encontra o componente/comportamento mostrado no screenshot. Iteração inútil.

**Causa:** Staging tem o feature branch deployado. O user chama de "pre-prod" o estado que está em staging (branch), não o `main`. `main` é mais antigo e pode não ter os novos componentes.

**Solução:**
- Quando user mostra screenshot de staging e diz "pre-prod": a referência é o branch atual, estado funcional anterior às últimas mudanças
- Para achar a versão "pré-prod" real: `git log --oneline -- <arquivo>` → pegar commit anterior ao merge/rebase problemático
- Perguntar: "pre-prod = staging ou main?"

**Evitar futuro:** Ao ver screenshot de `staging.app.mailerweb.com.br`, assume que staging tem branch atual deployado. Não comparar com `main` diretamente.

**Visto em:** [[daily/2026-06-26]] · sessão feature/waba-integration
