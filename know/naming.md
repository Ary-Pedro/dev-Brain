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
tags: [know, naming]
---

# naming — nomenclatura

> Padrão universal de nomes no devSpace. Nome é a primeira documentação. Se o nome precisa de comentário pra ser entendido, o nome está errado.

Lê antes: [[_principles]]. Cruza com [[code-style]], [[git-commits]].

## Regra de ouro

Nome descreve **intenção**, não tipo nem implementação. Prefira clareza a brevidade. O leitor não tem o contexto que você tem agora.

```py
# RUIM
d = get(u)          # d? u?
def proc(l): ...    # proc o quê?
lst2 = filter(lst)  # lst2 não diz nada

# BOM
active_user = get_user(user_id)
def normalize_emails(addresses): ...
verified_users = filter_verified(users)
```

## Convenção por stack

| Elemento | Python | Java | TypeScript |
|----------|--------|------|------------|
| Variável / função | `snake_case` | `camelCase` | `camelCase` |
| Classe / tipo | `PascalCase` | `PascalCase` | `PascalCase` |
| Constante | `UPPER_SNAKE` | `UPPER_SNAKE` | `UPPER_SNAKE` |
| Método | `snake_case` | `camelCase` | `camelCase` |
| Pacote / módulo | `snake_case` | `lowercase` | `camelCase`/`kebab` |

Não misture estilos dentro da mesma linguagem. Siga o idioma da stack, não seu gosto.

```py
# Python — snake_case
def send_welcome_email(user): ...
MAX_RETRY_COUNT = 3
class TenantSubscription: ...
```

```java
// Java — camelCase métodos/vars, PascalCase classes
public void sendWelcomeEmail(User user) { ... }
static final int MAX_RETRY_COUNT = 3;
class TenantSubscription { ... }
```

```ts
// TypeScript — camelCase vars/funcs, PascalCase tipos/componentes
function sendWelcomeEmail(user: User): void { ... }
const MAX_RETRY_COUNT = 3;
type TenantSubscription = { ... };
function UserCard(props: UserCardProps) { ... } // componente React = PascalCase
```

## Arquivos e diretórios

`kebab-case` por padrão para arquivos e pastas — agnóstico de SO, sem ambiguidade de maiúscula.

```
# BOM
user-service.ts
send-welcome-email.test.ts
billing-settings/

# RUIM
UserService.ts        // a não ser que a stack exija (componente React, classe Java)
sendWelcomeEmail.ts
billing_Settings/
```

Exceções legítimas, dite pela stack:
- **Java**: arquivo casa com a classe pública → `TenantSubscription.java`.
- **Python**: módulos em `snake_case` → `user_service.py`.
- **React (TS)**: componente em `PascalCase` → `UserCard.tsx`.

A regra é: siga a convenção da linguagem; `kebab` é o default quando a linguagem não impõe nada.

## Branches

`kebab-case` com prefixo de tipo. Combina com [[git-commits]] (Conventional Commits).

```
# BOM
feat/tenant-billing-webhook
fix/email-double-send
chore/bump-django-5-2

# RUIM
minha_branch
Feature_TenantBilling
fix-bug          // qual bug?
```

Formato: `<tipo>/<descrição-curta>`. Tipos: `feat`, `fix`, `chore`, `refactor`, `docs`, `test`.

## Booleans: sempre `is` / `has` / `can` / `should`

Boolean é uma pergunta sim/não. O nome tem que ler como pergunta.

```py
# RUIM
active = True
admin = user.role == "admin"
delete = False

# BOM
is_active = True
is_admin = user.role == "admin"
has_pending_invoice = invoice.status == "open"
can_edit = user.is_admin or user.owns(resource)
should_retry = attempt < MAX_RETRY_COUNT
```

```ts
// BOM
const isLoading = true;
const hasError = errors.length > 0;
const canSubmit = isValid && !isLoading;
```

## Evite abreviações obscuras

Escreva o nome por extenso. O editor autocompleta; o leitor não adivinha.

```py
# RUIM
usr, btn, cfg, idx, tmp, val, mgr, ctx, resp, qty, amt

# BOM
user, button, config, index, value, manager, response, quantity, amount
```

Abreviações **aceitas** porque são universais e inequívocas: `id`, `url`, `http`, `db`, `api`, `i`/`j` em loops curtos, `e` em callbacks de evento/erro de uma linha.

```ts
items.map((item, i) => ...)        // ok: i em loop trivial
button.onClick = (e) => ...        // ok: e óbvio no escopo
const dbConnection = connect();    // ok: db é universal
```

## Cheiros a evitar

- **Número no nome**: `data2`, `userTemp`, `processV3` → o nome não distingue de fato. Renomeie pela diferença real.
- **Tipo no nome (notação húngara)**: `strName`, `arrUsers`, `userList` → o tipo já está no sistema. Use `name`, `users`.
- **Prefixo redundante de classe**: em `User`, evite `userName`/`userEmail` → use `name`/`email`.
- **Negação dupla**: `isNotInvalid` → use `isValid`.
- **`get` em algo que muda estado**: `getUser()` deve ser puro; se grava, é `fetchUser()`/`loadUser()`/`createUser()`.

## Checklist

- [ ] Estilo da stack respeitado (snake/camel/Pascal)?
- [ ] Boolean lê como pergunta (`is`/`has`/`can`/`should`)?
- [ ] Zero abreviação obscura?
- [ ] Nome diz **o quê/porquê**, não o tipo nem um número de versão?
- [ ] Arquivo/branch em `kebab-case` (salvo exceção da linguagem)?
