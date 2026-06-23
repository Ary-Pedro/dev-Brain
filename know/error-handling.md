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
tags: [know, errors]
---

# error-handling — tratamento de erro

> Padrão universal do devSpace. Aplica antes de qualquer stack. Conflito? esta nota VENCE. Base de pensamento: [[_principles]].

## Princípios (invioláveis)

1. **Fail-fast.** Erro detectado = erro lançado **agora**, na borda. Não propague estado inválido. Quanto mais perto da origem, mais barato o diagnóstico.
2. **Exceção específica, nunca genérica.** `catch (Exception)` / `except Exception` / `catch (e)` largo é proibido fora do *boundary* global (handler de request, `main`, worker). Capture o tipo que você sabe tratar.
3. **Nunca engula exceção.** `catch` vazio, `except: pass`, `.catch(() => {})` são bug. Se não trata, **não captura** — deixa subir. Se captura, **loga ou relança** (idealmente encadeando a causa).
4. **Logging estruturado com contexto.** Log é dado, não prosa. Inclua identificadores (`tenant_id`, `user_id`, `request_id`, recurso afetado) em campos, não interpolados na string. Nível certo: `error` = ação humana; `warning` = degradou mas seguiu; `info` = fluxo normal.
5. **Mensagem acionável.** Diga **o quê** falhou, **com qual valor** e **o que fazer**. "Erro ao processar" é inútil. Erro de usuário ≠ erro de sistema: usuário recebe orientação, log recebe stack + contexto.
6. **Validação na borda.** Valide input no ponto de entrada (controller/view/handler). O núcleo do domínio assume dados já válidos — não revalida defensivamente em toda função.

## Anti-padrões (não fazer)

- Capturar amplo só para relogar e relançar sem agregar contexto (ruído).
- Usar exceção como controle de fluxo esperado (ex.: "registro não existe" em caminho normal).
- Engolir e retornar `null`/`None`/valor default silencioso — esconde a falha.
- Mensagem com PII/segredo no log. Ver [[security]].
- `try` gigante envolvendo 50 linhas: não dá pra saber o que falhou.

## Por stack

### Python / Django — ver [[python-django]]

```python
# RUIM
try:
    user = User.objects.get(pk=pk)
    process(user)
except Exception:          # genérico, engole tudo
    pass                   # falha some

# BOM
try:
    user = User.objects.get(pk=pk)
except User.DoesNotExist:
    raise Http404(f"User {pk} não encontrado")  # acionável, borda
process(user)              # núcleo assume user válido

# logging estruturado
logger.error("falha ao cobrar fatura", extra={
    "tenant_id": tenant.id, "invoice_id": inv.id, "amount": inv.amount,
})  # NÃO: logger.error(f"erro {e}")
```

- Valide na borda com DRF serializers / Forms — não no model manager.
- `raise X from e` para preservar a causa.

### Java / Spring — ver [[java-spring]]

```java
// RUIM
try { repo.save(x); }
catch (Exception e) { log.error("erro"); }   // genérico + sem contexto + engole

// BOM
try {
    repo.save(x);
} catch (DataIntegrityViolationException e) {
    throw new InvoiceConflictException(
        "Fatura %s duplicada para tenant %s".formatted(x.getId(), tenantId), e);
}
```

- Checked vs unchecked: lance unchecked específica (`@ResponseStatus` ou `@ControllerAdvice` mapeia para HTTP). Não declare `throws Exception`.
- `@ControllerAdvice` global = único lugar com captura ampla; traduz exceção → resposta.
- Bean Validation (`@Valid` + `@NotNull`/`@Size`) na borda do controller.
- Use SLF4J com argumentos parametrizados e MDC para contexto: `log.error("falha cobrança invoice={} tenant={}", id, tenantId, e);`

### TypeScript / Next — ver [[typescript-next]]

```ts
// RUIM
try { await charge(id); }
catch { /* silêncio */ }              // engole; e some

// BOM
try {
  await charge(id);
} catch (err) {
  if (err instanceof PaymentDeclinedError) {
    logger.error("cobrança recusada", { invoiceId: id, tenantId, cause: err });
    throw new ActionableError("Cartão recusado. Verifique os dados e tente de novo.");
  }
  throw err;                          // não sei tratar → sobe
}
```

- Tipe o `catch` (`catch (err: unknown)`) e faça *narrowing* com `instanceof`.
- Valide input na borda do route handler / Server Action com Zod (`schema.parse`) — falha cedo, mensagem do Zod já é acionável.
- Error boundaries no React para o que escapa; nunca `.catch(() => {})`.

## Checklist de PR

- [ ] Nenhum `catch`/`except` genérico fora do boundary global.
- [ ] Nenhuma exceção engolida (vazio / `pass` / default silencioso).
- [ ] Toda mensagem de erro diz o quê + valor + ação.
- [ ] Logs têm contexto estruturado (ids), sem PII/segredo.
- [ ] Input validado na borda; núcleo confia nos dados.
- [ ] Causa encadeada (`raise from` / `throw new X(..., e)` / `{ cause }`).

Relacionadas: [[_principles]] · [[testing]] · [[security]] · [[code-style]]
