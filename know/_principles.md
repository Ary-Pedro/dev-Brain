---
type: meta
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: stable
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [know, principles]
---

# Princípios de engenharia — como pensar ANTES de escrever código

> Governa o **COMO** de TODO o devSpace (Python/Django, Java/Spring, TypeScript/Next).
> Esta nota tem precedência. Ver [[routing]] para quando consultá-la.

A maioria dos erros não nasce no código — nasce **antes** dele. Pare. Pense. Depois digite.

## O loop obrigatório (na ordem)

1. **Entenda o problema** — qual é o sintoma, qual é a causa, o que é "pronto". Se não consegue formular em uma frase, ainda não entendeu.
2. **Ache o padrão que já existe no repo** — alguém já resolveu algo parecido aqui. Encontre e **imite**.
3. **Faça o menor diff possível** — toque só no necessário.
4. **Fail-fast** — quebre cedo e alto, não engula erro silencioso.
5. **Revise o diff como se fosse de outra pessoa** antes de entregar.

---

## 1. Entender > codar

Não escreva nada enquanto não souber responder: *o que muda no comportamento?* e *como eu provo que funcionou?*

Investigue antes de editar. Leia o arquivo alvo **e** os vizinhos. Não presuma.

## 2. Imite o padrão existente

A regra de ouro: **código novo deve ler como o código ao redor.** Se um leitor consegue dizer qual linha você adicionou só pelo estilo, você errou.

```python
# RUIM — trouxe estilo de fora, ignora o repo
def GetUserData(id):
    return db.query("select * from users where id="+str(id))

# BOM — segue o padrão que já está no módulo (ORM, snake_case, type hint)
def get_user(user_id: int) -> User:
    return User.objects.get(pk=user_id)
```

Antes de inventar abstração, **procure**: existe um helper, um serializer, um service, um util que já faz isso? Grep primeiro. Reusar > recriar. Ver [[code-style]] e [[naming]].

## 3. Menor diff possível

- Resolva **o** problema, não os cinco adjacentes que você notou de passagem.
- Não reformate linhas que não tocou (polui o diff, esconde a mudança real).
- Refactor oportunista vai em commit separado. Ver [[git-commits]].

```diff
# RUIM — fix de 1 linha escondido em 40 linhas de reformatação
- if user.active:
-     send(user)
+ if user.is_active and user.email_verified:
+     send(user)
+ # ...e reindentou o arquivo inteiro

# BOM — só o que importa
- if user.active:
+ if user.is_active:
      send(user)
```

## 4. Fail-fast

Erro deve aparecer perto da causa, não três camadas depois disfarçado de `None`.

```python
# RUIM — engole e segue, bug viaja longe
try:
    cfg = load_config()
except Exception:
    cfg = {}

# BOM — valida cedo, falha clara
cfg = load_config()
if "api_key" not in cfg:
    raise ValueError("api_key ausente em config")
```

Detalhe de tratamento em [[error-handling]].

## 5. Quando perguntar vs. quando decidir

| Decida sozinho | Pergunte antes |
|---|---|
| Nome de variável, ordem de imports, estilo local | Mudança de contrato/API pública |
| Seguir um padrão já existente no repo | Migração de dados, deleção, algo irreversível |
| Detalhe reversível em 1 commit | Requisito ambíguo onde adivinhar custa caro |
| Como, quando o "o quê" está claro | Trade-off de produto/escopo que o usuário deveria escolher |

Regra prática: **reversível e barato → decide; irreversível ou caro → pergunta.** Não pare o trabalho para perguntar o que você mesmo pode verificar lendo o código.

## 6. YAGNI e DRY com bom senso

- **YAGNI** — não construa para o futuro imaginário. Sem "flag de config para o caso de um dia precisar", sem camada de abstração com uma única implementação.
- **DRY** — elimine duplicação **de conhecimento**, não coincidência de texto. Duas linhas iguais por acaso não são duplicação; forçar abstração entre elas acopla o que devia ser independente.

```python
# RUIM (YAGNI) — generalizou para 1 caso de uso
def render(fmt="html", *, theme=None, plugins=None, cache_strategy=None):
    ...  # só existe render html, hoje e amanhã

# BOM — resolve o que existe
def render_html(content): ...
```

A regra de três: duplicou uma vez, tolere; na terceira, abstraia.

## 7. Código que lê como o código ao redor

Convenção do repo > sua preferência pessoal. Consistência vale mais que "o jeito certo" abstrato. Se o padrão local é ruim, **não copie o vício** — marque para correção e siga o padrão de [[code-style]] (ver precedência em [[routing]]).

---

## Antes de entregar (checklist)

- [ ] Entendi o problema e sei como provar a correção.
- [ ] Imitei o padrão já existente no repo.
- [ ] Diff mínimo, sem reformatação parasita.
- [ ] Falha cedo e clara onde algo der errado.
- [ ] Tem teste cobrindo a mudança. Ver [[testing]].
- [ ] Rotas/contratos consistentes com [[routing]].
- [ ] Não adicionei abstração/flag que ninguém pediu (YAGNI).

## Ver também

[[code-style]] · [[testing]] · [[routing]] · [[naming]] · [[error-handling]] · [[git-commits]]
