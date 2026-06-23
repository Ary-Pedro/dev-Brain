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
tags: [know, docs]
---

# Docstrings

Docstring documenta o **contrato** de uma unidade de código (função, classe, módulo) — _o quê_, _entradas_, _saídas_, _falhas_. É diferente de [[comments]]: comentário explica o _porquê_ de uma linha; docstring descreve a _interface_ para quem chama sem ler a implementação.

Regra de governança: **toda API pública leva docstring.** Privado/interno só quando o nome não basta.

---

## Quando documentar

- Funções/métodos **públicos** (exportados, endpoints, serviços, utils compartilhados).
- Comportamento **não óbvio**: efeitos colaterais, exceções lançadas, unidades, formatos, limites.
- Parâmetros com semântica especial (ex.: `timeout` em segundos, `None` = sem limite).
- Classes/módulos que outros vão consumir.

## Quando NÃO documentar

- Getters/setters triviais, código privado autoexplicativo.
- Repetir o que o nome e os _types_ já dizem (`def get_user_id() -> int` não precisa de "Retorna o id do usuário").
- Docstring que duplica a implementação — vira mentira no primeiro refactor.

> Type hints / generics fazem metade do trabalho. Docstring cobre o que o tipo **não** expressa: semântica, erros, contrato.

---

## Python — Google style

Args / Returns / Raises. Sem repetir tipos que já estão na assinatura.

```python
# BOM
def charge_customer(customer_id: str, amount: int, *, idempotency_key: str) -> Charge:
    """Cobra o cliente e retorna a cobrança confirmada.

    Args:
        customer_id: ID do cliente no gateway.
        amount: Valor em centavos (inteiro, nunca float).
        idempotency_key: Garante que reenvios não dupliquem a cobrança.

    Returns:
        A Charge persistida com status atualizado.

    Raises:
        PaymentDeclined: Quando o gateway recusa o cartão.
        GatewayTimeout: Quando o gateway não responde a tempo.
    """
```

```python
# RUIM — repete o nome, não diz nada do contrato
def charge_customer(customer_id, amount, idempotency_key):
    """Função que cobra o cliente."""  # e os erros? a unidade de amount?
```

---

## Java — Javadoc

`@param`, `@return`, `@throws`. Primeira frase é o resumo (vai no índice).

```java
// BOM
/**
 * Cobra o cliente e retorna a cobrança confirmada.
 *
 * @param customerId     ID do cliente no gateway.
 * @param amountCents    Valor em centavos; nunca negativo.
 * @param idempotencyKey Evita cobranças duplicadas em reenvios.
 * @return a {@link Charge} persistida com status atualizado.
 * @throws PaymentDeclinedException se o gateway recusar o cartão.
 * @throws GatewayTimeoutException  se o gateway não responder a tempo.
 */
public Charge chargeCustomer(String customerId, long amountCents, String idempotencyKey) {
```

```java
// RUIM
/** charge customer */
public Charge chargeCustomer(String customerId, long amountCents, String idempotencyKey) {
```

---

## TypeScript — TSDoc

Bloco `/** */` acima do símbolo. `@param`, `@returns`, `@throws`. Não anote o tipo no `@param` — o TS já tem.

```typescript
// BOM
/**
 * Cobra o cliente e retorna a cobrança confirmada.
 *
 * @param customerId - ID do cliente no gateway.
 * @param amountCents - Valor em centavos (inteiro, nunca float).
 * @param idempotencyKey - Evita cobranças duplicadas em reenvios.
 * @returns A cobrança persistida com status atualizado.
 * @throws {PaymentDeclinedError} Quando o gateway recusa o cartão.
 */
async function chargeCustomer(
  customerId: string,
  amountCents: number,
  idempotencyKey: string,
): Promise<Charge> {
```

```typescript
// RUIM — comentário de linha solto, sem contrato, não vira tooltip no editor
// cobra o cliente
async function chargeCustomer(customerId: string, amountCents: number, key: string) {}
```

---

## Checklist

- [ ] Resumo em uma frase, no imperativo ("Cobra...", "Retorna...").
- [ ] Toda exceção/erro relevante documentado (`Raises`/`@throws`).
- [ ] Unidades e formatos explícitos (centavos, segundos, ISO-8601).
- [ ] Sem repetir o que tipo/nome já dizem.
- [ ] Atualizada junto com a assinatura — docstring desatualizada é bug.

---

Relacionado: [[comments]] · [[code-style]] · ver também [[_principles]], [[naming]].
