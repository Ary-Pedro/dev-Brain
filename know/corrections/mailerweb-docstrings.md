---
type: correction
scope: mailerweb
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: active
confidence: high
last_verified: 2026-06-24
token_policy: full
tags: [know, corrections, mailerweb, docs, docstrings]
aliases: [mailerweb-docstrings, mailerweb-docstring-standard]
---

# MailerWeb — padrão de docstring/comentário (refina o universal)

- **Onde:** `mailerweb.panel.v2` (e `mailerweb-portal`) — todo Python.
- **Viola/refina:** [[docstrings]] e [[comments]] (universais). MailerWeb **adiciona** regras; onde houver choque, vale o item abaixo **só dentro do MailerWeb**.
- **Status:** ativo. Vício recorrente da IA: docstring sem `Note` p/ except capturado; comentário inline verboso/jargão; assumir linha 79.

## O que o MailerWeb exige além do universal

1. **Resumo em 3ª pessoa do singular, indicativo** — "Retorna o valor…", "Gera a mensagem…", "Resolve o adapter…". (Não imperativo "Retorne".)
2. **Corpo obrigatório quando a lógica não é trivial** — regra de negócio, fluxo alternativo, como o erro é tratado internamente. Vem depois do resumo, antes de `Args`.
3. **`Note:` é OBRIGATÓRIO quando a função captura exceção internamente** — documentar a captura silenciosa, side effects e dependências externas. Isto é o que mais esquecemos. Diferente de `Raises:` (exceção *lançada* p/ o caller).
4. **Privada com lógica não-trivial também leva docstring** (o universal dispensa privado autoexplicativo; MailerWeb é mais estrito).
5. **Tipos** em `Args`/`Returns`/`Yields`. `Yields:` só em generator.
6. Toda função **pública** leva docstring, sempre.

## Ordem fixa das seções

`Resumo (1 linha)` → `Corpo` → `Args` → `Returns` → `Yields` (se gerador) → `Note` (se captura except / side effect / dep externa).

```python
def send_single_transaction(tx_id):
    """Envia uma transação de mensagem pelo adapter do provider da instância.

    Reatribui a instância quando a designada está doente (mesma campanha →
    qualquer instância conectada do tenant) antes de marcar FAILED. Provider
    desconhecido resolve para None e a transação falha explicitamente.

    Args:
        tx_id (str): UUID da MessageTransaction a processar.

    Returns:
        bool: True se aceita pelo provider; False se falhou após retries.

    Note:
        Captura todas as exceções do adapter e converte em FAILED + retry —
        nunca propaga p/ o worker Celery. Faz I/O de rede (Meta/Green API).
    """
```

## Estilo / PEP 8 no MailerWeb (realidade, não o doc genérico)

- **Linha = 120 colunas** (ruff `line-length = 120`, `E501` ignorado em `pyproject.toml`). **NÃO** é 79 — o doc de onboarding cita o default PEP 8, mas o painel sobrescreve. Não reformatar p/ 79.
- ruff `select = E,F,W,I,N,UP,S,B,A,C4,SIM,TCH`; alvo `py312`. Aspas/format = o que o ruff aceita.
- Nomes descritivos em inglês; comentários de código em inglês; commit em PT (ver [[git-commits]]).

## Comentário inline (vício a cortar)

Comentário explica **porquê**, curto. Vício detectado: comentário-de-campo com 3 linhas, travessões e jargão empilhado. Ruim:

```python
# WABA approved template (SOA "Soft FK" — denormalized, no cross-app ORM FK).
# Cold / out-of-24h-window WhatsApp sends MUST use an approved template;
# dispatch calls adapter.send_template with the stored name + language.
```

Bom — uma linha, o porquê essencial; o resto vira docstring de quem usa:

```python
# Soft FK: nome/idioma do template aprovado (sem ORM FK cross-app).
# Obrigatório p/ envio fora da janela de 24h (Meta bloqueia texto livre).
```

Ver [[comments]]: se o nome resolve, renomeia; nada de código comentado "por garantia".

Relacionado: [[docstrings]] · [[comments]] · [[python-django]] · [[code-style]] · [[git-commits]].
