---
type: note
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: stable
confidence: high
last_verified: 2026-06-23
token_policy: full
tags: [know, database, sql, stack]
---

# database — padrão de banco (SQL / ORM)

> O **COMO** modelar, consultar e migrar dados em todo o `devSpace` (Postgres, MySQL, via Django ORM / Prisma / JPA). Complementa [[performance]] e as notas de stack. Padrão inviolável — ver [[routing]].

## 1. Schema
- Uma tabela = uma entidade coesa. Normalize até 3FN; **desnormalize só com medida** (perf provada, não palpite).
- Tipos corretos: dinheiro = inteiro em centavos (nunca float), tempo = timestamp **com timezone** (UTC no banco), enum = check/lookup, não string solta.
- Toda FK com índice. `NOT NULL` por padrão; `NULL` é decisão explícita. Defaults no banco quando o domínio exige.
- Chave: PK substituta estável (bigint/uuid). UUID v7/ULID quando precisa ordenar por tempo (ver [[django-uuid-pk-vs-integerfield]]).

## 2. Migrations (seguras, reversíveis)
- **Schema e dados em migrations separadas.** Toda migration reversível.
- **Zero-downtime:** adicionar coluna nullable → backfill em lote → tornar NOT NULL; nunca `ALTER` com lock longo em tabela grande em horário de pico.
- Renomear/remover = processo em 2 deploys (expand → contract). Nunca dropar coluna ainda lida por código vivo.
- Índice em tabela grande: `CREATE INDEX CONCURRENTLY` (Postgres) / online DDL (MySQL 8).

## 3. Query (sem N+1, lê no banco)
- **Mate o N+1:** `select_related`/`prefetch_related` (Django), `include`/`select` (Prisma), `JOIN FETCH` (JPA). Lista que itera relação = suspeito.
- Agrega/filtra/ordena **no banco**, não em memória. `EXISTS` > `COUNT>0`. Pagina sempre (keyset > offset em tabela grande).
- Pegue só as colunas usadas (`only`/`select`). Índice cobre o `WHERE`/`ORDER BY` real — confirme com `EXPLAIN (ANALYZE)`.
- Soft-delete: cuidado com `unique` + manager base (ver [[django-unique-soft-delete-base-manager]]).

## 4. Transação & integridade
- Escrita multi-passo = **uma transação**. `select_for_update()` **dentro** de bloco atômico (fora dele não trava nada — bug comum).
- Invariante de domínio no banco quando possível (constraint/check) **e** no código. Idempotência em operações sensíveis (cobrança) via chave única.
- Multi-tenancy: filtro de tenant em **toda** query (ver isolamento em [[python-django]]). Vazamento de tenant = incidente de segurança ([[security]]).

## 5. Anti-padrões
- ORM gerando query em loop · `SELECT *` em hot path · índice que ninguém usa (custo de escrita) · migration que trava deploy · lógica de negócio em trigger escondida · float pra dinheiro.

Ver também: [[performance]] · [[python-django]] · [[java-spring]] · [[typescript-next]] · [[_principles]].
