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
tags: [know, meta, frontmatter]
aliases: [frontmatter, frontmatter-standard]
---

# _frontmatter — padrão de frontmatter p/ a IA rotear

> Camada **operacional** do vault: estes campos é que dizem ao agente **o que ler, o que entra no contexto da IA e onde pode escrever**.
> Toda nota nova nasce com este frontmatter. Ver [[routing]] (quando consultar o quê) · [[_strategy]] (por que dois brains) · [[_mailerweb-access]] (read-only externo).

A IA não "decora" estas notas — ela **roteia** por elas. O frontmatter é a chave de roteamento; o corpo é o conteúdo. Campo errado = nota invisível ou consumida no lugar errado.

## Campos

| Campo | Obrigatório | O que controla |
|--|--|--|
| `type` | sim | natureza da nota → como o roteador a trata |
| `scope` | sim | alcance: `global`, `cross-repo`, ou um repo (`mailerweb`, `<repo>`) |
| `repo_path` | se aplica | caminho do repo/arquivo de origem (absoluto) — só quando a nota fala de código concreto |
| `brain_policy` | sim | a qual cérebro a nota pertence: `dev-brain` \| `mailerweb-brain-ref` |
| `write_policy` | sim | quem pode gravar: `dev-brain-only` \| `read-only` |
| `audience` | sim | **quem consome**: `ai` \| `human` \| `both` — controla entrada no vetor/contexto IA |
| `source` | sim | origem: `human` \| `ai` \| `graphify` \| `vector` |
| `status` | sim | ciclo de vida: `draft` \| `active` \| `stable` \| `deprecated` |
| `confidence` | recomendado | confiança: `high` \| `med` \| `low` |
| `last_verified` | recomendado | `YYYY-MM-DD` da última checagem contra a realidade |
| `token_policy` | recomendado | como gastar tokens: `summary-first` \| `full` |
| `tags` | sim | tags Obsidian (roteamento + recall) |

## Valores aceitos

### `type`
- `project` — visão/arquitetura de um projeto inteiro.
- `lesson` — problema→solução reaproveitável (`lessons/`). Ver [[lessons]].
- `correction` — vício/erro de domínio registrado, **não** corrigido na fonte (`corrections/`).
- `decision` — registro de decisão arquitetural (ADR) datado e imutável (`decisions/`).
- `note` — nota técnica de padrão (naming, testes, etc.).
- `session` — daily note / log de sessão (`daily/`).
- `agent` — definição/perfil de agente.
- `moc` — Map of Content / índice (hub que aponta, não contém).
- `meta` — nota sobre o próprio vault/processo (_strategy, _frontmatter, _toolbox, routing, flow).

### `scope`
`global` (vale todo o devSpace) · `cross-repo` (mais de um repo) · `<repo>` (ex.: `mailerweb`).

### `brain_policy`
- `dev-brain` — nota nativa deste vault (padrão).
- `mailerweb-brain-ref` — espelha/aponta domínio externo; a verdade vive no mailerweb-brain. Ver [[_mailerweb-access]].
- `read-domain-from-mailerweb-brain` — card de projeto do universo MailerWeb: o padrão é nativo, mas o **domínio** é lido do mailerweb-brain (via [[mailerweb-bridge]]).

> ⚠️ `brain_policy` = a qual cérebro a nota pertence. NÃO confundir com `write_policy` (quem grava). `dev-brain-only` é valor de **write_policy**, nunca de brain_policy.

### Campos extras de card de projeto (`type: project`)
`token_weight` (`baixo|médio|alto|crítico` — tier de custo p/ o [[context-economist]]) · `graph_nodes`/`graph_edges` (do digest graphify) · `domain_brain` · `repo_path` · `stack`. Lessons usam `keywords: [...]` (recall do vetor).

### `write_policy`
- `dev-brain-only` — só a automação/Claude do dev-Brain grava aqui (padrão).
- `read-only` — **nunca** editar/criar/mover/deletar. Vale pra tudo que reflete fonte externa (mailerweb-brain). Saída vai pro dev-Brain, não pra fonte.

### `audience` — controla vetor/contexto IA
- `ai` — **entra** no vector-map e pode ser puxado pro contexto do agente. É memória operacional.
- `human` — **NÃO** entra no vector-map **nem** é consumido pela IA. Existe só pro humano entender/navegar.
- `both` — serve aos dois (entra no vetor **e** é legível pro humano).

### `source`
`human` (escrito por mim) · `ai` (gerado por skill/agent, ex. `/journal`) · `graphify` (derivado do grafo de código) · `vector` (derivado da camada semântica).

### `status`
`draft` → `active` → `stable` · `deprecated` (manter por histórico, fora do roteamento ativo).

### `confidence`
`high` (verificado) · `med` (plausível, não confirmado) · `low` (suspeita/hipótese).

### `token_policy`
- `summary-first` — ler só o topo/resumo primeiro; aprofundar sob demanda (notas longas).
- `full` — ler inteira (notas curtas e densas).

## `audience=human` → fora da IA (regra-chave)

`audience: human` significa: **não vetorizar, não injetar no contexto do agente**. A nota é navegação/leitura humana — entra na pasta, aparece no grafo Obsidian, mas o roteador da IA a ignora.

São `human` por padrão:
- **READMEs de navegação** (índices de pasta, "como usar esta pasta").
- **Daily logs** brutos (`daily/`) — captura crua; a memória reaproveitável já foi destilada em `lessons/` (essas, sim, `ai`/`both`).

São `ai`/`both`: padrões de engenharia, lessons, corrections, project/architecture, MOCs operacionais — tudo que o agente precisa **aplicar**, não só o humano ler.

## Exemplo mínimo

```yaml
---
type: lesson
scope: cross-repo
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: ai
status: active
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [lesson, django, soft-delete]
---
```

Ver também: [[routing]] · [[_strategy]] · [[_mailerweb-access]] · [[_principles]]
