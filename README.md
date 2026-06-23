---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: human
status: active
tags: [meta, moc, readme]
---

# dev-Brain

Cérebro de **engenharia** do `devSpace`. Vault Obsidian que governa **COMO** se programa neste workspace — não *onde está* o código.

Separação de responsabilidades:

| Vault | Pergunta que responde | Escopo |
|-------|----------------------|--------|
| **dev-Brain** (este) | *Como pensar, como escrever, qual padrão, qual docstring, qual boa prática* | Todo o `devSpace` — universal |
| **mailerweb-brain** | *Onde está o arquivo, o que é esse fluxo, qual a regra de negócio* | Só o universo MailerWeb |

> dev-Brain **enxerga tudo**. Aplica boas práticas e aponta/corrige os grupos de dados do `mailerweb-brain` para o Claude respeitar o padrão do dev.
>
> - Projeto **MailerWeb** → dev-Brain **consome** `mailerweb-brain` (padrão + domínio).
> - Projeto/serviço **fora** → **só** dev-Brain. Sem alucinar MailerWeb.

A regra de roteamento está em [[routing]].

---

## Estrutura

```
dev-Brain/
├── 00-index.md      ← mapa de conteúdo (MOC) — comece aqui
├── routing.md       ← quando consultar cada brain
├── know/            ← BOAS PRÁTICAS (o COMO) — governança · lessons/ · corrections/
├── map/             ← mapa de alto nível do devSpace (o ONDE, resumido)
├── projects/        ← cards vivos por projeto (token_weight, brain_policy, próxima ação)
├── agents/          ← specs dos sub-agents especializados (stack + meta)
├── graph/           ← saída do graphify (graph.json, GRAPH_REPORT.md) + vector maps + missing-links
├── decisions/       ← ADRs — decisões arquiteturais datadas e imutáveis
├── dashboards/      ← leitura gerencial + operação (projects, tasks/Kanban, pending)
├── daily/           ← diário de sessões (breadcrumb automático + /journal)
├── templates/       ← templates Templater (project-card, lesson, session, decision)
├── automation/      ← flow operacional, plugins, MCP
└── docker/          ← infra do vault (compose, MCP Obsidian)
```

Padrão de metadata em [[_frontmatter]]; loop operacional em [[flow]].

## Uso com Claude Code

1. Antes de codar, Claude lê [[routing]] → decide quais notas de `know/` aplicar.
2. `know/` define docstring, naming, estilo, testes, segurança — **por stack**.
3. `map/` localiza o projeto e aponta para o brain de domínio (ex.: mailerweb-brain).
4. `graph/` dá a visão grafo do código (gerado por [graphify](https://github.com/safishamsi/graphify)).

## Abrir no Obsidian

Open folder as vault → selecione `dev-Brain/`. O graph view colore por domínio (ver `.obsidian/graph.json`).

## Setup após `git clone`

Artefatos pesados e binários de plugin são **gitignored** (regeneráveis — ver `.gitignore` e [[0002-dashboards-plugin-free|ADR-0002]]). Para reconstituir:

```bash
# 1. binários dos plugins Obsidian (main.js etc — config já vem versionada)
bash scripts/install-plugins.sh

# 2. grafos de código (graphify AST) + resumos + mapas vetoriais
bash graph/build-all.sh
~/.local/share/graphify-venv/bin/python graph/summarize.py
~/.local/share/vecmap-venv/bin/python graph/vector-map.py ~/devSpace/dev-Brain dev-brain

# 3. dashboards gerados (sem plugin)
python3 dashboards/build-dashboards.py
```

## Saúde + uso pela IA

```bash
python3 scripts/doctor.py                       # valida frontmatter/links/cards (CI gate)
python3 scripts/context-packet.py <slug> "tarefa"   # entrada MÍNIMA da IA (não o vault inteiro)
```

Loop operacional completo em [[flow]]. Decisões em `decisions/`. O que está pendente em [[pending-board]].
