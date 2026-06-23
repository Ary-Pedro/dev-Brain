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
tags: [know, stack, python, django]
---

# Python / Django — padrão de stack

Padrão **opinativo** de engenharia para Python/Django nesta casa. Vale para projetos como [[mailerweb-panel-v2]] (Django 5 multi-tenant + DRF + Celery). Esta nota não repete o universal — herda de [[_principles]], [[code-style]], [[naming]], [[docstrings]], [[testing]], [[error-handling]], [[security]], [[performance]]. Quando bater dúvida de "qual brain", veja [[routing]] e o inventário em [[00-index]].

> Regra-mãe: **Django é framework, não arquitetura.** O framework te dá ORM, views e admin. A organização do domínio é responsabilidade sua.

---

## Layout de app

Um app = um domínio coeso. Quebre o `models.py`/`views.py` monolítico em módulos com responsabilidade única:

```
billing/
├── models.py        # estado + invariantes (fat model, regras locais à instância)
├── selectors.py     # leituras: queries ORM, agregações (read)
├── services.py      # escritas: orquestração, transações, side-effects (write)
├── serializers.py   # fronteira DRF: validação + (de)serialização
├── views.py         # HTTP: roteamento, permissões, status code — fino
├── tasks.py         # Celery
├── permissions.py
└── tests/
```

- **selectors** = ler. **services** = mudar estado. Views chamam services/selectors, nunca o ORM cru para lógica de negócio.
- Sem import circular: `views → services → models`. `services` pode chamar `selectors`. Nunca o inverso.

---

## Fat models vs service layer

Invariante que pertence à instância → **model/method**. Caso de uso que coordena várias entidades, transação ou side-effect (e-mail, fila, pagamento) → **service**.

```python
# RUIM — regra de negócio multi-entidade enfiada na view
def post(self, request):
    invoice = Invoice.objects.get(pk=request.data["id"])
    invoice.status = "paid"
    invoice.paid_at = timezone.now()
    invoice.save()
    Wallet.objects.filter(user=invoice.user).update(balance=F("balance") - invoice.total)
    send_receipt_email(invoice)  # side-effect sem transação; view virou domínio
    return Response(...)
```

```python
# BOM — view fina; caso de uso no service, atômico
# services.py
@transaction.atomic
def pay_invoice(*, invoice: Invoice) -> Invoice:
    invoice.mark_paid()                  # invariante na própria instância (fat model)
    invoice.user.wallet.debit(invoice.total)
    transaction.on_commit(lambda: send_receipt_email.delay(invoice.id))  # side-effect só pós-commit
    return invoice

# models.py
class Invoice(models.Model):
    def mark_paid(self) -> None:
        if self.status == self.Status.PAID:
            raise AlreadyPaidError(self.pk)
        self.status = self.Status.PAID
        self.paid_at = timezone.now()
        self.save(update_fields=["status", "paid_at"])
```

Exceções de domínio (`AlreadyPaidError`) seguem [[error-handling]]: específicas, não `Exception` genérico.

---

## ORM sem N+1

O pecado nº1 de Django. Detalhe e disciplina de medição em [[performance]]; aqui o reflexo:

```python
# RUIM — N+1: uma query por linha ao tocar a FK no loop
for order in Order.objects.all():
    print(order.customer.name)          # +1 query cada iteração
```

```python
# BOM — FK / OneToOne: select_related (JOIN)
orders = Order.objects.select_related("customer")

# BOM — reverse FK / ManyToMany: prefetch_related (query extra + join em memória)
orders = Order.objects.prefetch_related("items")
```

- `.only()`/`.defer()` para colunas pesadas; `.values()`/`.values_list()` quando não precisa de instância.
- Agregação no banco (`Count`, `Sum`, `annotate`), não em loop Python.
- Em testes, prenda regressão com `assertNumQueries` ([[testing]]).

---

## Migrations seguras

Migration é deploy, não enfeite. Em produção com tráfego, schema change não pode travar tabela nem quebrar a versão antiga rodando em paralelo.

- **Coluna nova nullable** ou com `default` no app (não `db_default` que reescreve a tabela inteira em bases grandes).
- **Adicionar e remover em deploys separados** (expand/contract): primeiro adiciona e passa a escrever nos dois; só depois remove o antigo.
- **Backfill de dados** em data migration própria, em lotes — nunca junto da mudança de schema.
- Index em tabela grande: `AddIndexConcurrently` (Postgres) para não bloquear.
- Sempre revise o SQL: `python manage.py sqlmigrate app NNNN`. Migration gerada não é migration revisada.
- Nunca edite migration já aplicada em produção; crie outra.

---

## Settings por ambiente + segredos

Detalhe de gestão de segredo em [[security]]. Reflexo Django:

```python
# RUIM
SECRET_KEY = "django-insecure-9x...hardcoded"
DEBUG = True
```

```python
# BOM — segredo vem do ambiente, falha cedo se faltar
SECRET_KEY = env("DJANGO_SECRET_KEY")        # KeyError no boot é melhor que vazar default
DEBUG = env.bool("DJANGO_DEBUG", default=False)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
```

- Split: `settings/base.py` + `dev.py`/`prod.py`/`test.py`. `prod` herda de `base` e endurece (HSTS, `SECURE_SSL_REDIRECT`, cookies `Secure`).
- `.env` **fora do repo** e no `.gitignore`. Nada de segredo, DSN ou chave commitado.
- `DEBUG = False` em qualquer ambiente exposto. Sem exceção.

---

## DRF

```python
# views.py — viewset fino; permissão e queryset isolam o tenant
class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, IsTenantMember]

    def get_queryset(self):                       # nunca .all() cru
        return selectors.invoices_for(tenant=self.request.tenant)

    def perform_create(self, serializer):
        services.create_invoice(tenant=self.request.tenant, **serializer.validated_data)
```

- **Serializer** valida e converte; regra de negócio fica no service, não no `validate_*` quando envolve side-effect.
- **Permission** controla acesso; nunca delegue autorização ao front nem ao `if` solto na view.
- Endpoint de escrita ≠ endpoint de leitura: serializer de input pode diferir do de output.
- Paginação ligada por default. `ModelViewSet.queryset = Model.objects.all()` global é armadilha de vazamento entre tenants — sempre via `get_queryset`.

---

## Celery — tasks idempotentes

```python
# RUIM — task que duplica efeito se reentregar (retry, worker morto)
@shared_task
def charge(invoice_id):
    inv = Invoice.objects.get(pk=invoice_id)
    gateway.charge(inv.total)            # cobra de novo a cada retry
```

```python
# BOM — idempotente: chave única + checagem de estado
@shared_task(bind=True, max_retries=3, acks_late=True)
def charge(self, invoice_id):
    inv = Invoice.objects.select_for_update().get(pk=invoice_id)
    if inv.status == Invoice.Status.PAID:
        return                            # já feito; reentrega é no-op
    try:
        gateway.charge(inv.total, idempotency_key=f"inv-{invoice_id}")
        inv.mark_paid()
    except GatewayTimeout as exc:
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)
```

- Passe **ID**, não a instância serializada (evita objeto stale).
- Enfileire side-effect só em `transaction.on_commit` — senão a task roda antes do commit e não acha a linha.
- `acks_late` + retry com backoff. Toda task deve aguentar ser executada duas vezes sem estragar nada.

---

## Docstrings, testes, formatação

- **Docstrings Google style** em services, selectors e funções públicas (`Args:`/`Returns:`/`Raises:`) — ver [[docstrings]]. Model óbvio não precisa; service de negócio precisa.
- **Testes**: `pytest` + `pytest-django` preferido; `TestCase` quando precisar de transação/rollback automático. Teste o service (caso de uso), não o framework. Use `factory_boy`/fixtures, `assertNumQueries` para N+1. Detalhe em [[testing]].
- **Formatação**: `black` (formatação) + `ruff` (lint, ordena import, pega bug) no pre-commit e no CI. Sem discussão de estilo em PR — ver [[code-style]] e [[naming]]. CI bloqueia o que `black --check`/`ruff` reprovam.

---

## Multi-tenancy — isolamento

Em base multi-tenant ([[mailerweb-panel-v2]]) o maior risco é **vazar dado entre tenants**. Trate como invariante de segurança ([[security]]), não como filtro de conveniência.

```python
# RUIM — query global; um id de outro tenant retorna dado alheio
invoice = Invoice.objects.get(pk=pk)
```

```python
# BOM — todo acesso parte do tenant do request
invoice = selectors.invoices_for(tenant=request.tenant).get(pk=pk)
```

- O `tenant` vem do request (middleware), **nunca** de parâmetro controlável pelo cliente.
- Centralize o filtro em selectors/manager (`TenantManager`) — não espalhe `filter(tenant=...)` solto e esquecível.
- Teste explícito de **cross-tenant**: usuário do tenant A não enxerga nem edita recurso do tenant B (espera 404, não 403, para não revelar existência).
- Cuidado com cache, Celery e signals: a chave/contexto tem que carregar o tenant, ou o isolamento vaza fora do ciclo do request.

---

Ver também: [[_principles]] · [[code-style]] · [[performance]] · [[security]] · [[testing]] · [[00-index]]
