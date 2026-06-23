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

# comments — comentar o PORQUÊ, nunca o QUÊ

> Padrão universal do devSpace. Vale para Python/Django, Java/Spring e TypeScript/Next. Pensa antes em [[_principles]].

## Regra de ouro

O código já diz **o quê** ele faz. Comentário existe pra contar **o porquê**: a decisão, o trade-off, a regra de negócio obscura, o bug que você está contornando. Se o comentário só repete o que a linha abaixo faz, ele é dívida — vai dessincronizar e mentir.

## Sem comentário óbvio/redundante

```python
# RUIM — narra o que o código já grita
i = i + 1  # incrementa i
user.save()  # salva o usuário
# loop sobre os items
for item in items:
    ...
```

```python
# BOM — explica o porquê não-óbvio
# Stripe arredonda pra cima; somamos 1 centavo pra bater com a fatura deles.
total = ceil(total) + 1
# Reprocessa só os falhos: o batch inteiro já custou caro na 1ª passada.
for item in failed_items:
    ...
```

Se o nome resolve, **renomeie em vez de comentar** — ver [[naming]].

```typescript
// RUIM — comentário compensando nome ruim
const d = 86400; // segundos em um dia

// BOM — o nome é o comentário
const SECONDS_PER_DAY = 86400;
```

## TODO / FIXME com contexto

Marcador solto é lixo: ninguém sabe quem, por quê, nem quando. Sempre **autor + motivo + gatilho de remoção** (ticket, data ou condição).

```java
// RUIM
// TODO arrumar isso depois

// BOM
// FIXME(pedro, 2026-06): N+1 ao carregar faturas — bloqueado por MW-1423.
// Remover após migrar pra fetch join.
```

- `TODO` — melhoria planejada que ainda não dói.
- `FIXME` — defeito conhecido que já dói; rastreie num issue.

## Remover código morto — não comentar

Código comentado "pra não perder" é ruído: o git já é seu histórico. Apague.

```python
# RUIM
# old_price = calc_legacy(cart)   # deixa aqui caso precise
new_price = calc(cart)

# BOM
new_price = calc(cart)   # versão legada está no git (commit a1b2c3d)
```

## Docstring é outra coisa

Comentário inline ≠ docstring/Javadoc/JSDoc de contrato público de função, classe ou módulo. Para isso, siga [[docstrings]] — lá o "o quê" da assinatura é esperado.

## Checklist

- [ ] O comentário explica **porquê**, não **o quê**?
- [ ] Um rename eliminaria o comentário? Se sim, renomeie.
- [ ] Todo `TODO`/`FIXME` tem autor, motivo e gatilho de remoção?
- [ ] Zero código comentado "por garantia" — apaguei e confio no git ([[git-commits]]).
- [ ] O comentário ainda será verdade daqui a 6 meses? Se não, reescreva o código.
