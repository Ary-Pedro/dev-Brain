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
tags: [know, style]
---

# code-style — estilo de código

> O **COMO** se escreve código legível em todo o `devSpace` (Python/Django, Java/Spring, TypeScript/Next). Padrão inviolável — ver precedência em [[routing]]. Complementa [[_principles]], [[naming]] e [[comments]].

Regra de ouro: **o formatador decide a estética; você decide a estrutura.** Não gaste revisão de PR discutindo espaço/vírgula — isso é trabalho de máquina. Gaste revisão em estrutura, nomes e fronteiras.

---

## 1. Estrutura de arquivo

Um arquivo conta **uma** história. Ordem de leitura de cima para baixo: o leitor entende o "o quê" antes do "como".

Ordem canônica:

1. Cabeçalho do módulo (docstring/comentário de propósito — ver [[comments]]).
2. Imports (ver §4).
3. Constantes e tipos do módulo.
4. API pública (o que outros importam) **antes** dos helpers privados.
5. Helpers privados por último, na ordem em que são chamados.

Um conceito por arquivo. Se o nome do arquivo precisa de "and"/"util"/"misc", ele faz coisas demais.

```python
# RUIM — helper privado no topo, leitor lê o "como" antes do "o quê"
def _normaliza(raw): ...
def _valida(raw): ...
def processa_pedido(raw):           # a função que importa está enterrada
    return _normaliza(_valida(raw))
```
```python
# BOM — API pública primeiro, helpers descem na ordem de uso
def processa_pedido(raw):
    return _normaliza(_valida(raw))

def _valida(raw): ...
def _normaliza(raw): ...
```

---

## 2. Tamanho de função

Limite **comportamental**, não contador de linhas: uma função faz uma coisa, num nível de abstração. Se você precisa de comentário `# parte 2` ou rolar para ver o `return`, extraia.

Guia prático (sintoma, não lei): ~30 linhas / ~3 níveis de indentação / ~4 parâmetros. Estourou? Provavelmente são duas funções.

```java
// RUIM — busca + filtra + formata + envia, tudo numa função
void relatorio() {
    List<Pedido> p = repo.findAll();
    // filtra
    for (...) { ... }
    // formata
    StringBuilder sb = new StringBuilder(); ...
    // envia
    mailer.send(...);
}
```
```java
// BOM — cada passo nomeado, relatorio() vira o índice
void relatorio() {
    var pedidos = pedidosDoMes();
    var corpo   = formataRelatorio(pedidos);
    enviaPara(financeiro(), corpo);
}
```

---

## 3. Early-return vs aninhamento

**Guard clauses primeiro.** Trate erro/borda no topo e saia. O caminho feliz fica no nível de indentação mais raso, sem `else`.

```typescript
// RUIM — caminho feliz afundado em 3 níveis
function preco(user, item) {
  if (user) {
    if (item.inStock) {
      if (user.isPremium) {
        return item.price * 0.9;
      } else {
        return item.price;
      }
    }
  }
  return null;
}
```
```typescript
// BOM — sai cedo, caminho feliz raso, sem else
function preco(user, item) {
  if (!user) return null;
  if (!item.inStock) return null;
  return user.isPremium ? item.price * 0.9 : item.price;
}
```

`else` depois de `return`/`throw` é ruído — remova. Aninhamento ≥ 3 é cheiro de função faltando (§2).

---

## 4. Imports

Agrupar e ordenar (o formatador faz isso por você — §6): (1) stdlib, (2) terceiros, (3) interno do projeto. Linha em branco entre grupos.

- **Imports absolutos** para o que é do projeto. Relativo só dentro do mesmo pacote/feature e raso (`./x`, não `../../../x`).
- **Nada de wildcard** (`from x import *`, `import static ... .*`): polui o namespace e quebra o "vá até a definição".
- Sem imports não usados — o linter falha o build.
- Ordem alfabética dentro do grupo; deixe a ferramenta ordenar.

```python
# RUIM
from app.services import *
import os
from .a import x
from app.models import User
```
```python
# BOM
import os                      # stdlib

import requests                # terceiros

from app.models import User    # interno
from app.services import cobranca
from .helpers import normaliza
```

---

## 5. Evitar abstração prematura

**WET antes de DRY.** Duplicar **uma** vez é mais barato que a abstração errada. Espere o **terceiro** uso para extrair — só então o eixo de variação é óbvio. Ver [[_principles]].

- Não crie `BaseService`/`AbstractManager`/camada genérica para um único caso.
- Parâmetro booleano que muda o comportamento da função = provavelmente duas funções.
- "Vai que precisa" não é requisito. Resolva o problema de hoje.

```python
# RUIM — generaliza no segundo uso, flag controla o fluxo
def envia(msg, *, sms=False, push=False, retry=3, formatter=None):
    ...  # 1 função, 4 ramos, ninguém entende
```
```python
# BOM — funções concretas; extraia o comum quando o 3º caso provar o padrão
def envia_email(msg): ...
def envia_sms(msg): ...
```

A abstração certa aparece sozinha quando a duplicação dói. Forçá-la cedo trava o código no formato errado.

---

## 6. Formatadores por stack — não negociável

Formatação não entra em PR review: roda no pre-commit/CI e falha o build se diferir. Configuração default da ferramenta, sem "estilo da casa".

| Stack | Formatador | Linter | Onde roda |
|-------|-----------|--------|-----------|
| **Python / Django** | `black` (ou `ruff format`) | `ruff` | pre-commit + CI. Ver [[python-django]] |
| **Java / Spring** | `google-java-format` | (spotless/checkstyle) | build Maven/Gradle. Ver [[java-spring]] |
| **TypeScript / Next** | `prettier` | `eslint` | pre-commit + CI. Ver [[typescript-next]] |

Regras:

- **`ruff` substitui** flake8/isort/pyupgrade — não acumule ferramentas redundantes.
- `prettier` cuida da **estética**; `eslint` cuida de **bugs/regras** (`no-unused-vars`, hooks). Não use eslint para formatar (use `eslint-config-prettier` para desligar conflito).
- Java: `google-java-format` é o árbitro; checkstyle só para regras além de layout.
- CI roda em modo **check** (`black --check`, `prettier --check`, spotless `check`): diferença = build vermelho. Sem exceção manual.

---

## Ver também

- [[_principles]] — como pensar antes de escrever (YAGNI, WET→DRY)
- [[naming]] — como nomear o que esta nota manda estruturar
- [[comments]] — o que comentar (e o que não comentar) no código já estruturado
- [[docstrings]] — o contrato (interface) da unidade de código; complemento de estrutura
