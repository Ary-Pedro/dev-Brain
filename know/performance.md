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
tags: [know, perf]
---

# Performance

Performance é **trade-off**, não virtude absoluta. A regra de governança: **primeiro correto e legível ([[code-style]], [[_principles]]), depois medido, só então otimizado.** Código rápido que ninguém entende custa mais no longo prazo do que latência marginal.

> "Premature optimization is the root of all evil." — Knuth. Mas isso **não** é desculpa para escolher o algoritmo O(n²) óbvio quando o O(n) é igual de simples, nem para deixar N+1 query no ORM. Burrice estrutural ≠ otimização. Evite as duas pontas.

---

## Disciplina (vale para toda stack)

1. **Não otimize no escuro.** Sem número, sem mudança. Profile/benchmark antes.
2. **Meça o que dói em produção**, não o que parece lento na sua cabeça. O gargalo quase nunca é o que você chuta — costuma ser I/O (DB, rede), não CPU.
3. **Otimize o caminho quente.** 95% do tempo está em 5% do código. Ataque esse.
4. **Re-meça depois.** "Otimização" sem antes/depois é fé, não engenharia.
5. **Documente o porquê** ([[comments]]) quando trocar clareza por velocidade — o próximo dev vai querer "simplificar" de volta.

```
# RUIM — micro-otimização cega que destrói legibilidade sem medir
total = reduce(lambda a, b: a + b.price * (1 - b.discount), items, 0)  # "é mais rápido"

# BOM — claro; se o profiler apontar AQUI, aí sim otimiza
total = sum(item.price * (1 - item.discount) for item in items)
```

---

## O inimigo nº 1: N+1 queries

O ORM esconde o custo. Um loop que acessa relação dispara **1 query + N queries** — explode com o volume. Quase sempre o maior ganho de performance num CRUD é matar N+1, não trocar de framework.

### Python / Django — `select_related` e `prefetch_related`

`select_related` = JOIN (relação ForeignKey/OneToOne, "para um"). `prefetch_related` = 2ª query + junção em memória (ManyToMany/reverse FK, "para muitos"). Ver [[python-django]].

```python
# RUIM — N+1: 1 query nos pedidos + 1 query por pedido para pegar o cliente
for order in Order.objects.all():
    print(order.customer.name)        # bate no banco a cada iteração

# BOM — 1 query com JOIN
for order in Order.objects.select_related("customer"):
    print(order.customer.name)

# BOM — relação "para muitos": 2 queries no total, não N
for order in Order.objects.prefetch_related("items"):
    print(sum(i.price for i in order.items.all()))
```

> Detecte com `django-debug-toolbar` (conta queries por request) ou `assertNumQueries` no teste ([[testing]]). Se o número de queries cresce com o número de linhas, é N+1.

### Java / Spring — fetch join (JPA/Hibernate)

`LAZY` é o default correto, mas iterar relação lazy fora da sessão = N+1 (ou `LazyInitializationException`). Resolva com **fetch join** na query, não trocando tudo para `EAGER`. Ver [[java-spring]].

```java
// RUIM — N+1: cada order.getCustomer() dispara um SELECT
List<Order> orders = orderRepo.findAll();
orders.forEach(o -> log.info(o.getCustomer().getName()));

// BOM — JPQL com fetch join: uma query só
@Query("SELECT o FROM Order o JOIN FETCH o.customer")
List<Order> findAllWithCustomer();

// BOM alternativa — @EntityGraph declarativo
@EntityGraph(attributePaths = "customer")
List<Order> findAll();
```

> Nunca aplique `JOIN FETCH` em duas coleções na mesma query (produto cartesiano). Para "para muitos", prefira `@BatchSize` ou múltiplos fetch graphs.

### TypeScript / Next — Prisma e o data layer

O N+1 reaparece em ORMs JS e em chamadas dentro de loops de render. Use `include`/`select` no Prisma; em GraphQL, **DataLoader** para batch. Ver [[typescript-next]].

```typescript
// RUIM — N+1: uma query por order dentro do loop
const orders = await prisma.order.findMany();
for (const o of orders) {
  const customer = await prisma.customer.findUnique({ where: { id: o.customerId } });
}

// BOM — uma query com join relacional
const orders = await prisma.order.findMany({
  include: { customer: true },
});
```

> Em Server Components, cada `await` sequencial dentro de `.map` serializa o request. Faça `Promise.all` para paralelizar I/O independente.

---

## Índices

O JOIN/filtro mais elegante é lento sem índice. Crie índice para **colunas usadas em `WHERE`, `JOIN` e `ORDER BY`** de queries quentes — e só essas: índice tem custo de escrita e espaço.

- **Django**: `Meta.indexes = [models.Index(fields=["status", "created_at"])]`, ou `db_index=True` no campo. FK já vem indexada.
- **JPA**: `@Table(indexes = @Index(columnList = "status, created_at"))` — mas trate o índice como decisão de **migração/DDL**, não de mapeamento.
- **Geral**: índice composto respeita a ordem das colunas (leftmost prefix). Confirme uso com `EXPLAIN ANALYZE` — índice criado ≠ índice usado.

---

## Paginação

**Nunca** retorne uma coleção ilimitada de uma tabela que cresce. Sem `LIMIT`, a query que voa com 100 linhas derruba o servidor com 1M.

```python
# RUIM — carrega a tabela inteira na memória e na resposta
return Response(OrderSerializer(Order.objects.all(), many=True).data)

# BOM — DRF pagina por padrão (PageNumberPagination / LimitOffset)
class OrderList(ListAPIView):
    queryset = Order.objects.select_related("customer")
    pagination_class = PageNumberPagination
```

> Para grandes offsets, **keyset/cursor pagination** (`WHERE id > last_id LIMIT n`) supera `OFFSET n` — offset alto faz o banco varrer e descartar tudo antes do offset. Spring: `Pageable` + `Slice`; Prisma: `cursor` + `take`.

---

## Caching — com critério

Cache é a otimização que mais facilmente vira bug. **Só faz sentido para dado caro de computar e relativamente estável.** Antes de cachear, pergunte: a query é lenta mesmo (mediu?) ou falta um índice / sobra um N+1? Resolva a causa antes de mascarar com cache.

Regras:
- **Invalidação é o problema difícil.** Defina TTL e/ou evento de invalidação *antes* de adicionar o cache. Cache sem estratégia de invalidação = dado velho silencioso.
- **Cache o resultado caro, não o request inteiro** quando der — granularidade reduz invalidação.
- **Multi-tenant**: a chave de cache **precisa** incluir o tenant. Vazar cache entre tenants é incidente de segurança ([[security]]), não bug de performance.

```python
# RUIM — chave global em app multi-tenant: tenant A vê dado do tenant B
data = cache.get_or_set("dashboard_stats", compute_stats, 300)

# BOM — chave isola o tenant
key = f"dashboard_stats:{tenant.id}"
data = cache.get_or_set(key, lambda: compute_stats(tenant), 300)
```

> Camadas: HTTP/CDN → cache de aplicação (Redis) → cache de query do ORM → memo em memória. Use a mais alta que resolva. No Next, prefira o caching nativo (`revalidate`, `fetch` cache, `unstable_cache`) antes de subir um Redis.

---

## Checklist

- [ ] Mediu antes de otimizar? Tem antes/depois?
- [ ] Contou queries por request? N+1 morto (`select_related`/`prefetch`, `JOIN FETCH`, `include`)?
- [ ] Coleções paginadas com `LIMIT`? Endpoint de lista não retorna tabela inteira?
- [ ] `WHERE`/`JOIN`/`ORDER BY` quentes têm índice — confirmado por `EXPLAIN`?
- [ ] Cache só onde dói, com TTL/invalidação definidos e chave por tenant?
- [ ] I/O independente paralelizado (`Promise.all`, async) em vez de sequencial?
- [ ] Trade-off de clareza→velocidade documentado ([[comments]])?

---

Relacionado: [[_principles]] · [[code-style]] · [[testing]] · [[security]] · por stack: [[python-django]] · [[java-spring]] · [[typescript-next]].
