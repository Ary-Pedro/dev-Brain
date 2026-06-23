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
tags: [know, stack, typescript, nextjs]
---

# TypeScript / Next.js

Padrão de stack para projetos Next.js (App Router) + React + Prisma + Postgres — caso de uso de referência: [[meudinheiro-v2]] (Next.js 16 / React 19 / Prisma / Postgres). Aqui mora o **específico**; o universal continua valendo: [[_principles]], [[code-style]], [[naming]], [[testing]], [[error-handling]], [[security]], [[performance]]. Volta ao [[00-index]] quando se perder.

> Regra-mãe: **o servidor é o padrão.** No App Router tudo é Server Component até você provar que precisa de browser. Cada `"use client"` é uma dívida — JS que vai pro bundle e roda no cliente. Justifique.

---

## App Router — server vs client

Server Component (default) = roda no servidor, pode `await` direto em DB/Prisma, **não** vai pro bundle, **não** tem hooks de estado nem `onClick`. Client Component (`"use client"` no topo) = interatividade, hooks, browser APIs. `"use client"` só quando precisa de **estado, efeito, evento ou API do browser**.

```tsx
// RUIM — página inteira virou client só por causa de um botão
"use client";
import { useState } from "react";
export default async function Page() {  // ❌ async + "use client" nem faz sentido
  const txs = await prisma.transaction.findMany(); // ❌ Prisma no cliente: vaza, não compila
  ...
}

// BOM — server busca os dados; ilha client só onde há interação
// app/transactions/page.tsx  (Server Component)
export default async function Page() {
  const txs = await prisma.transaction.findMany({ select: { id: true, amount: true, payee: true } });
  return <TransactionList items={txs} />; // lista pode ser server; só o filtro é client
}
// app/transactions/filter.tsx
"use client";
export function Filter({ onChange }: { onChange: (q: string) => void }) { /* useState aqui */ }
```

Empurre `"use client"` para as **folhas** da árvore. Não envolva a página; envolva o widget.

---

## Server Actions vs Route Handlers

- **Server Action** (`"use server"`): mutação disparada de um form/componente da própria app. É o default para "salvar/criar/deletar" no fluxo interno. Tipada ponta a ponta, sem inventar endpoint.
- **Route Handler** (`app/api/.../route.ts`): quando precisa de um **HTTP endpoint de verdade** — webhook, consumidor externo, REST público, contrato com terceiro.

```ts
// BOM — mutação interna como Server Action, validada na borda (ver [[security]], [[error-handling]])
"use server";
import { z } from "zod";
const NewTx = z.object({ amount: z.number().positive(), payee: z.string().min(1) });

export async function createTransaction(input: unknown) {
  const data = NewTx.parse(input);            // valida ANTES de tocar no banco
  await prisma.transaction.create({ data });
  revalidatePath("/transactions");
}
```

Não crie um `route.ts` "REST interno" só para o seu próprio front consumir via `fetch` — isso é Server Action com passos a mais e tipo perdido.

---

## Tipos estritos — `strict`, zero `any`

`tsconfig` com `strict: true` (não negociável). `any` é apagar o TypeScript; quando o tipo é genuinamente desconhecido use `unknown` e estreite. Ver [[code-style]], [[naming]].

```jsonc
// tsconfig.json — base
{ "compilerOptions": { "strict": true, "noUncheckedIndexedAccess": true, "noImplicitOverride": true } }
```

```ts
// RUIM
function parse(body: any) { return body.amount * 2; }   // explode em runtime, TS calado

// BOM — entra como unknown, valida, sai tipado
function parse(body: unknown): number {
  return NewTx.parse(body).amount * 2;
}
```

Derive tipos do schema, não duplique: `type NewTx = z.infer<typeof NewTx>`. Single source of truth.

---

## Validação na borda com Zod

**Todo dado que cruza a fronteira** (form, body de request, params, `searchParams`, resposta de API externa, env) é `unknown` até validado. Valide **na entrada**, uma vez, e trabalhe com o tipo já garantido lá dentro. Detalhe de segurança em [[security]]; o que fazer com a falha (mensagem, status, log) em [[error-handling]].

```ts
// BOM — borda valida e converte; o "miolo" recebe dados confiáveis
const result = NewTx.safeParse(formData);
if (!result.success) return { error: result.error.flatten() }; // erro tratado, não throw cru
await createTransaction(result.data);
```

---

## Prisma sem N+1 (`include` / `select`)

O Prisma esconde o custo igual a qualquer ORM. Loop que acessa relação dispara N queries. Use `include`/`select` para trazer o necessário numa query só — e `select` para **não** trazer o que não usa (colunas e relações). Aprofunde em [[performance]].

```ts
// RUIM — N+1: 1 query nas contas + 1 por conta para buscar transações
const accounts = await prisma.account.findMany();
for (const a of accounts) {
  const txs = await prisma.transaction.findMany({ where: { accountId: a.id } }); // ❌
}

// BOM — uma query, só os campos usados
const accounts = await prisma.account.findMany({
  select: {
    id: true,
    name: true,
    transactions: { select: { id: true, amount: true }, take: 20 },
  },
});
```

`select` > `include` quando você sabe os campos: menos dados na rede, payload menor, sem vazar coluna sensível.

---

## Data fetching & caching do Next

Busque dados **no Server Component**, perto de onde renderiza. Entenda o cache: por padrão o Next memoiza/cacheia `fetch`; controle com `cache`/`revalidate` e invalide mutações com `revalidatePath` / `revalidateTag`. Dado que precisa estar sempre fresco (saldo, dashboard financeiro) deve ser explicitamente dinâmico — não confie em cache silencioso para dado de dinheiro.

```ts
// dado que muda toda hora: opte por dinâmico explícito
export const dynamic = "force-dynamic"; // ou fetch(url, { cache: "no-store" })
// dado estável: revalida a cada N
fetch(url, { next: { revalidate: 3600 } });
```

---

## Error & Loading boundaries

Use os arquivos especiais do App Router em vez de espalhar `try/catch` de UI: `loading.tsx` (fallback de Suspense durante o fetch do segmento) e `error.tsx` (`"use client"`, captura erro de render e oferece `reset()`). `not-found.tsx` para 404 de recurso. A política de erro (o que logar, o que mostrar ao usuário) é a de [[error-handling]] — boundary é só onde ela acontece.

```tsx
// app/transactions/error.tsx
"use client";
export default function Error({ error, reset }: { error: Error; reset: () => void }) {
  return <button onClick={reset}>Tentar de novo</button>; // não exponha stack ao usuário
}
```

---

## TSDoc

Documente o **porquê** e o contrato, não o óbvio. TSDoc (`/** ... */`) em funções exportadas, server actions e tipos públicos — o resto a assinatura tipada já conta. Regra geral em [[docstrings]].

```ts
/**
 * Cria uma transação para a conta do usuário logado.
 * @throws ZodError se o input não casar com o schema.
 */
export async function createTransaction(input: unknown) { /* ... */ }
```

---

## Testes — Vitest/Jest + Testing Library

Vitest (ou Jest) para lógica e Testing Library para componentes — **teste comportamento, não implementação** (queries por papel/texto, não por classe CSS). Server Actions e validação Zod testam-se como funções puras: dado de entrada → efeito esperado. Filosofia e cobertura em [[testing]].

```ts
// BOM — testa o contrato da borda, não o detalhe interno
it("rejeita amount negativo", () => {
  expect(NewTx.safeParse({ amount: -1, payee: "x" }).success).toBe(false);
});
```

---

## ESLint + Prettier

ESLint para **regras** (bugs, `no-explicit-any`, hooks rules), Prettier para **formatação** — não brigue por estilo em PR, deixe a ferramenta decidir (ver [[code-style]]). Rode no CI e em pre-commit; lint quebrado não faz merge.

---

## Segredos: env server-side

Variáveis sem `NEXT_PUBLIC_` ficam **só no servidor**. Tudo com prefixo `NEXT_PUBLIC_` é **embutido no bundle do cliente** — qualquer um lê. Logo: `DATABASE_URL`, chaves de API, segredos **nunca** levam o prefixo. Detalhe em [[security]].

```ts
// RUIM — vaza o banco pro browser
NEXT_PUBLIC_DATABASE_URL=postgres://...   // ❌ exposto no JS do cliente

// BOM
DATABASE_URL=postgres://...               // server-only
NEXT_PUBLIC_APP_URL=https://app.exemplo   // ok: público de propósito
```

Valide o env no boot (Zod) para falhar cedo se faltar segredo, em vez de quebrar em runtime no meio de uma request.

---

## Ver também

[[_principles]] · [[code-style]] · [[naming]] · [[docstrings]] · [[testing]] · [[error-handling]] · [[security]] · [[performance]] · [[routing]] · [[meudinheiro-v2]] · [[00-index]]
