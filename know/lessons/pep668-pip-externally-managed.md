---
type: lesson
scope: cross-repo
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: ai
status: active
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [lesson, python, env]
keywords: [pip, pep668, externally-managed, venv, wsl, debian]
aliases: [pep668-pip-externally-managed]
---

# pip falha: externally-managed-environment (PEP 668)

## Contexto
Tentativa de `pip install <pacote>` usando o Python do sistema no Debian/Ubuntu/WSL.

## Sintoma
```
error: externally-managed-environment
```

## Causa
PEP 668 protege o Python do sistema: instalar pacotes globalmente com pip pode quebrar dependências gerenciadas pelo apt.

## Solução
Criar um venv dedicado e instalar lá:
```bash
python3 -m venv ~/.local/share/<tool>-venv
~/.local/share/<tool>-venv/bin/pip install <pacote>
```
Alternativa: usar `pipx` para ferramentas CLI.

NUNCA usar `--break-system-packages`.

## Evitar futuro
- Sempre isolar ferramentas Python em venv dedicado (ou pipx).
- Ex. real: `graphify` e `embeddings` instalados em venvs próprios.

Visto em: [[daily/2026-06-19]]
