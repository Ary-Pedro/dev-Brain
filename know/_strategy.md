---
type: meta
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: stable
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [know, strategy, meta]
---

# _strategy — dois cérebros + visão híbrida

> A razão de existirem **dois** brains e três visões de grafo. Leitura única; o resto é [[routing]] e [[hybrid-views]].

## Dois cérebros (divisão de trabalho)

| | **dev-Brain** (este) | **mailerweb-brain** |
|--|--|--|
| Papel | POLICY + ARCHITECTURE memory | TASK memory + DOMAIN retrieval |
| Escopo | geral, cross-projeto | curado por app MailerWeb |
| Tom | prescritivo (o COMO) | operacional (o ONDE/o QUÊ) |
| Otimiza | coerência entre repos | latência + tokens |

Não duplicar. dev-Brain não copia domínio MailerWeb; mailerweb-brain não copia padrão de engenharia.

## Roteamento (resumo — detalhe em [[routing]])

- Dúvida de **domínio MailerWeb** (onde está a regra X, qual app toca Y, fluxo de auth/billing) → **PRIMEIRO** mailerweb-brain, via [[mailerweb-bridge]] (read-only).
- **Padrão / naming / testes / segurança / visão cross-repo** → dev-Brain (`know/`).
- Conflito: padrão de engenharia (dev-Brain) **vence**. Vício no domínio → marcar em [[corrections]], não copiar.

## 3 visões de grafo (complementares — não escolher uma)

| Visão | O que mostra | Fonte |
|--|--|--|
| (a) **Obsidian links** | documentação **explícita** (o que eu escrevi que se relaciona) | `[[wikilinks]]` deste vault |
| (b) **graphify** | estrutura **real** do código (imports, chamadas) | [[00-graph-index]] |
| (c) **vector map** | memória **semântica** / IA (proximidade de sentido) | [[hybrid-views]] |

São camadas, não alternativas. A força do brain vem do **cruzamento** delas.

## Matriz link × vetor × graphify

| Tem link? | Perto no vetor? | Leitura | Ação |
|--|--|--|--|
| sim | perto | relação **forte** (doc + sentido batem) | nada |
| **não** | **perto** | **LINK FALTANDO** | adicionar `Relacionado:` |
| sim | longe | link **genérico/errado** | revisar/remover o link |
| não | longe | relação **fraca** | nada |
| (relação no **graphify**, sem nota) | — | **DOC FALTANDO** | criar nota do que o código já liga |

## Anti-padrões de vault para IA

- **Notas grandes/genéricas** → quebrar em menores e específicas (recall ruim em chunk gigante).
- **Hubs falsos** ("tudo sobre X") → dividir por subtema; um hub deve ser índice, não conteúdo.
- **Títulos ruins** → título = a query que você faria; é o que o vetor e o humano leem primeiro.

Exemplo de quebra:
`MailerWeb (monólito)` → `MailerWeb — Visão Geral` · `… Domínios` · `… Apps` · `… Billing` · `… BYOG`.

## Prática que converge (relatos de campo)

Começar pequeno e expandir — **NÃO** automatizar tudo no dia 1:

1. Vault **pequeno**.
2. **Manual operacional na raiz** (entrada óbvia → [[00-index]]).
3. **Daily note primeiro** (captura antes de organizar).
4. **CLAUDE.md com regras mínimas** (poucas, inquebráveis).
5. **1 MCP server** só.
6. **Expansão gradual** conforme dói — não antes.

Ver também: [[routing]] · [[hybrid-views]] · [[00-graph-index]] · [[_principles]]
