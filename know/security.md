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
tags: [know, security]
---

# security — higiene de segurança no dev

> Padrão universal. Aplica em **todo** o devSpace. Cruza com [[_principles]], [[error-handling]] e [[testing]].

**Escopo:** isto **não é pentest**. É higiene de desenvolvedor — o piso que todo código entrega antes de existir. Pentest, threat modeling e red team são outra disciplina; aqui é o que você **não tem desculpa** para errar.

Regra de ouro: **toda entrada é hostil até prova em contrário, todo segredo fica fora do repo, todo processo roda com o mínimo de poder.**

---

## 1. Segredos fora do repo

Nunca commitar credencial, token, chave ou senha. Nem em comentário, nem em "TODO remover depois", nem em teste.

- **Dev:** `.env` (no `.gitignore`) + `.env.example` versionado só com as *chaves*, sem valores.
- **Prod:** secret manager (Vault, AWS Secrets Manager, GCP Secret Manager) ou env do orquestrador. Nunca arquivo no servidor com segredo em texto puro versionado.
- Vazou um segredo no histórico do git? **Rotacione a credencial.** Remover o commit não basta — assuma comprometido.

```python
# RUIM — segredo no código
STRIPE_KEY = "sk_live_51Hx...real"
DATABASE_URL = "postgres://user:senha123@db/app"

# BOM — vem do ambiente, falha cedo se faltar
import os
STRIPE_KEY = os.environ["STRIPE_KEY"]        # KeyError no boot > rodar sem chave
DATABASE_URL = os.environ["DATABASE_URL"]
```

Logs e mensagens de erro também vazam segredo. Ver [[error-handling]]: nunca logar token, senha ou PII.

---

## 2. Validação e sanitização de input

Valide **na borda** (controller/view/handler), com esquema explícito. Confiar no front é confiar no atacante.

- **Allowlist, não blocklist.** Defina o que é válido; rejeite o resto.
- Valide **tipo, faixa, tamanho e formato** — não só "não-nulo".
- Sanitize na **saída** conforme o destino (HTML, SQL, shell, log).

```ts
// RUIM — confia no shape do body
function handler(req) {
  const age = req.body.age;          // string? objeto? undefined?
  db.update({ age });                 // lixo entra direto
}

// BOM — valida com schema antes de tocar em qualquer coisa
const Schema = z.object({ age: z.number().int().min(0).max(150) });
function handler(req) {
  const { age } = Schema.parse(req.body);   // lança em input inválido
  db.update({ age });
}
```

---

## 3. OWASP — o básico inegociável

Não é a lista inteira do OWASP Top 10; são os três que aparecem em quase todo bug de segurança de app:

### Injection (SQL / comando / NoSQL)
Sempre parametrize. **Nunca** concatene input em query ou comando de shell.

```python
# RUIM — SQL injection
cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")

# BOM — query parametrizada
cursor.execute("SELECT * FROM users WHERE email = %s", [email])
```
ORM resolve a maioria dos casos — use `filter()`/repository, evite `raw()`/string SQL. Por stack: [[python-django]] (ORM, evitar `.raw()`/`.extra()`), [[java-spring]] (JPA/`@Query` parametrizado, nunca string), [[typescript-next]] (Prisma/Drizzle, nunca template string em SQL).

### XSS (cross-site scripting)
Escape por padrão na saída; desligar o escape é decisão consciente e rara.

```jsx
// RUIM — injeta HTML cru do usuário
<div dangerouslySetInnerHTML={{ __html: userBio }} />

// BOM — React escapa texto por padrão
<div>{userBio}</div>
// Precisa de HTML rico? Sanitize antes (DOMPurify) — nunca confie no input.
```
Django auto-escapa no template; cuidado com `|safe` e `mark_safe()`. Defina CSP onde der.

### Authorization (authz ≠ authn)
Autenticação responde *quem é você*; **autorização** responde *você pode fazer isso com este recurso*. Cheque **a cada request, no servidor**, sempre amarrando o recurso ao dono.

```python
# RUIM — IDOR: qualquer logado lê qualquer pedido
def get_order(request, order_id):
    return Order.objects.get(id=order_id)

# BOM — escopo pelo dono
def get_order(request, order_id):
    return Order.objects.get(id=order_id, owner=request.user)
```
Esconder o botão no front **não é** controle de acesso. Em multi-tenant, todo query carrega o tenant — ver regras do projeto em [[python-django]] e no CLAUDE.md do app.

---

## 4. Least privilege

Cada componente recebe o **mínimo** de poder para sua função.

- Usuário de DB da app: `SELECT/INSERT/UPDATE/DELETE` nas tabelas que usa — **não** `DROP`, **não** superuser.
- Token de API/CI: escopo restrito, expiração curta, um por finalidade.
- Container/processo: não rodar como `root`; FS read-only onde possível.
- Permissão default = **negar**; abre o que precisa, explicitamente.

---

## 5. Dependências atualizadas

Dependência desatualizada é CVE conhecido esperando exploit.

- Lockfile versionado (`poetry.lock`, `package-lock.json`/`pnpm-lock.yaml`, `pom.xml` com versões fixas).
- Audit no CI: `pip-audit`, `npm audit`/`pnpm audit`, `mvn dependency-check` ou Dependabot/Renovate.
- Atualize **rotineiro e pequeno**, não num big-bang anual. Patch de segurança entra na frente.
- Toda nova dep é superfície de ataque: avalie antes de adicionar (ver [[_principles]] — menos é mais).

---

## Checklist mínimo antes do merge

- [ ] Zero segredo no diff (e nenhum no histórico).
- [ ] Todo input externo validado por schema na borda.
- [ ] Queries parametrizadas; nenhuma string SQL/shell concatenada.
- [ ] Saída escapada por contexto (HTML/template).
- [ ] Authz checada no servidor, recurso amarrado ao dono/tenant.
- [ ] Sem credencial/PII em log ou mensagem de erro.
- [ ] Deps com lockfile e audit limpo.
