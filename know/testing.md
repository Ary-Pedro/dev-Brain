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
tags: [know, testing]
---

# testing — padrão de testes do devSpace

> Teste não é opcional nem decoração. É a rede que deixa você refatorar sem medo.
> Aplica-se a TODO o devSpace: Python/Django, Java/Spring, TS/Next. Ver [[routing]] e [[_principles]].

## Princípio único

**Teste comportamento, não implementação.** Se você renomeia um método privado e o teste quebra, o teste estava errado. Teste a *interface pública* e os *efeitos observáveis*, não os passos internos.

```python
# RUIM — acopla ao "como" (mock de detalhe interno)
def test_envio(self):
    svc = EmailService()
    svc._build_payload = Mock()           # testando implementação
    svc.send(user)
    svc._build_payload.assert_called_once()

# BOM — testa o "o quê" (efeito observável)
def test_send_marca_email_como_enviado(self):
    user = UserFactory()
    EmailService().send(user)
    self.assertEqual(user.emails.last().status, "sent")
```

## Pirâmide de testes

Muito unitário, alguns de integração, poucos E2E. Pirâmide, não sorvete invertido.

```
        /\      E2E / UI         ← poucos, lentos, frágeis. Só fluxos críticos.
       /--\     Integração       ← DB real, HTTP, fila. Cobrem as costuras.
      /----\    Unitário         ← muitos, rápidos, isolados. A base.
```

- **Unitário**: uma unidade, sem I/O. Roda em milissegundos. É onde mora a lógica de negócio.
- **Integração**: cruza fronteiras reais (banco, ORM, endpoint). Em Django, `TestCase` com DB já é integração de fato.
- **E2E**: caro. Reserve para os 3-5 fluxos que, se quebrarem, derrubam o produto.

Anti-padrão "sorvete invertido": muitos E2E, poucos unitários → suíte lenta, flaky e que ninguém roda.

## O que testar

- Regra de negócio e cálculos. Sempre.
- Branches: caminho feliz **e** os de erro. Ver [[error-handling]].
- Bordas: vazio, nulo, zero, negativo, limite, duplicado.
- Bugs encontrados → primeiro um teste que falha, depois o fix (teste de regressão).

Não teste: getters/setters triviais, framework alheio, mocks testando mocks.

## Nomenclatura

Nome de teste é documentação. Deve descrever **condição → comportamento esperado**, não o método.

```
# RUIM
def test_user(): ...
def test1(): ...

# BOM (Python)
def test_saldo_negativo_bloqueia_saque(): ...
def test_email_invalido_levanta_validation_error(): ...
```

```java
// BOM (JUnit) — padrão metodo_condicao_resultado
@Test void saque_comSaldoInsuficiente_lancaExcecao() { ... }
```

```ts
// BOM (Vitest/Jest) — describe + it legível
describe("calcularJuros", () => {
  it("retorna 0 quando o saldo é zero", () => { ... });
});
```

## Arrange-Act-Assert

Um teste, três blocos visíveis. Uma asserção lógica por teste (pode ser >1 `assert` do mesmo conceito).

```python
def test_desconto_vip_aplica_10_porcento(self):
    # Arrange
    pedido = PedidoFactory(total=100, cliente__vip=True)
    # Act
    total = aplicar_desconto(pedido)
    # Assert
    self.assertEqual(total, 90)
```

Sem ramificação (`if`/`for`/`try`) dentro do teste. Lógica no teste = teste não testado.

## Ferramentas por stack

| Stack | Runner / framework | Notas |
|-------|--------------------|-------|
| Python / Django | **pytest** + `pytest-django`; `django.test.TestCase` p/ DB | Use `factory_boy` p/ fixtures; `TestCase` envolve em transação (rollback automático). Ver [[python-django]]. |
| Java / Spring | **JUnit 5** + AssertJ; `@SpringBootTest` p/ integração; Mockito p/ mocks | Slices (`@WebMvcTest`, `@DataJpaTest`) > subir o contexto inteiro. Ver [[java-spring]]. |
| TypeScript / Next | **Vitest** (preferido) ou Jest; Testing Library p/ componentes; Playwright p/ E2E | Teste o que o usuário vê (`getByRole`), não estado interno. Ver [[typescript-next]]. |

Regra transversal: cada `assert` deve apontar exatamente onde o comportamento divergiu.

## Quando TDD vale a pena

TDD (red-green-refactor) é ferramenta, não religião. Aplique onde paga:

- **Vale**: regra de negócio com bordas claras, bug a corrigir (escreva o teste que reproduz primeiro), API/contrato cujo formato você quer ancorar, refatoração de código legado (caracterize com testes antes de mexer).
- **Não vale (ou pesa pouco)**: spike exploratório, protótipo descartável, UI puramente visual em fluxo, código cuja forma você ainda não conhece.

Heurística: se você não sabe *como* a saída deve ser, é cedo demais para TDD — explore primeiro, depois consolide com teste antes de considerar pronto. Pronto sem teste não é pronto. Ver [[git-commits]]: commit que adiciona comportamento adiciona teste junto.
