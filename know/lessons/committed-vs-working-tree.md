---
tags: [lesson, git, debugging]
keywords: [git diff, working tree, HEAD, commits, imports quebrados, undefined]
aliases: [committed-vs-working-tree]
---

# Distinguir estado commitado vs working tree antes de diagnosticar

**Contexto:** Arquivo tem bugs (imports quebrados, variáveis undefined). Difícil saber se bug está no commit ou foi introduzido na sessão atual.

**Sintoma:** `git show HEAD:arquivo` mostra imports incorretos mas o working tree tem versão diferente. Claude fica confuso sobre qual versão está causando o bug.

**Causa:** Branch foi commitado com bugs de imports/lógica. Working tree tem fixes parciais não commitados. Diagnóstico baseado em HEAD sem checar working tree dá informação errada.

**Solução:**
```bash
# Estado commitado:
git show HEAD:caminho/arquivo.jsx | head -30

# Diff working tree vs commitado:
git diff HEAD -- caminho/arquivo.jsx

# Lista arquivos com mudanças não commitadas:
git diff HEAD --name-only
```

Sempre rodar os três antes de editar um arquivo suspeito.

**Evitar futuro:** Início de sessão e antes de diagnosticar bug visual: checar `git diff HEAD --name-only` para saber quais arquivos têm mudanças em voo.

**Visto em:** [[daily/2026-06-26]] · sessão feature/waba-integration
