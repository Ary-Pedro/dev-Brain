---
type: note
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: active
last_verified: 2026-06-19
token_policy: full
tags: [meta, automation, flow]
---

# flow — loop operacional do dev-Brain

> Como as peças (plugins + scripts + agents) se encaixam no dia-a-dia. A IA segue isto; o humano interage pelo Obsidian.

## O ciclo

```text
capturar → planejar → criar → decidir → registrar → versionar grafo
```

| Passo | Ferramenta | Quem | O quê |
|-------|-----------|------|-------|
| **Capturar** | `daily/` + Day Planner | IA/humano | sessão do dia; blocos de tempo no daily |
| **Planejar** | Tasks + Kanban ([[tasks-board]]) | ambos | tarefa = `- [ ]`; visualiza/move card no board |
| **Listar** | Tasks query ([[tasks-open]]) | IA | checklist viva de tudo aberto |
| **Criar nota** | Templater (`templates/`) | ambos | `project-card` · `lesson` · `session` · `decision` |
| **Decidir** | `decisions/` (ADR) | humano | escolha estrutural, datada, **imutável** |
| **Registrar** | `/journal` (SessionEnd hook) | IA | destila daily → [[lessons]] / [[corrections]] |
| **Grafo** | `build-all.sh` → `summarize.py` → `vector-map.py` → `build-dashboards.py` | script | estrutura + semântica + dashboards regenerados |
| **Navegar** | Recent Files · Iconize · Graph view | humano | últimos tópicos; ícones por categoria |

## Convenção de tarefa (Tasks)

```text
- [ ] Texto #projeto/<slug> 🔼 📅 2026-06-25
```
IA quebra uma tarefa grande em `- [ ]` no daily/sessão; humano marca/edita no [[tasks-board]] (Kanban). Detalhe em [[tasks-open]].

## Regra de aprendizado (destilação — senão o vault vira cemitério de notas)

Toda sessão relevante produz **no máximo**: 1 `lesson` (funcionou) · 1 `correction` (erro recorrente a evitar) · 1 `decision` (ADR) · 1 `skill candidate` (procedimento reutilizável). Não gerar bíblia por bug — só o que **muda comportamento futuro**. Ciclo:

```text
sessão → daily (breadcrumb) → /journal destila → lesson|correction|decision|skill → roteamento futuro usa
```

Sem destilação, nota bonita no Obsidian = inútil pra IA. Toda aprendizagem cai em: lesson · correction · decision · skill · pattern.

## Entrada da IA: context-packet (não o vault)

Antes de chamar a IA numa tarefa, gere o pacote mínimo: `python3 scripts/context-packet.py <slug> "<tarefa>"`. É a **camada 2** (ver abaixo). Nunca "lê tudo aí e vê o que acha".

```text
camada 0: regra curta fixa (CLAUDE.md <200 linhas)
camada 1: skill sob demanda
camada 2: context-packet
camada 3: digest do grafo
camada 4: arquivo real — só se necessário
```
Cache de prompt favorece **prefixo estável** (regra/roteamento) + dinâmico no fim. Saúde do vault: `python3 scripts/doctor.py`.

## Regras que não mudam

- Antes de contexto pesado → [[context-economist]] (lê `token_weight` do card em `projects/`).
- Domínio MailerWeb → [[mailerweb-bridge]] (read-only). Nunca duplicar. ([[0001-dois-cerebros-mailerweb-readonly|ADR-0001]])
- Dashboards têm tabela gerada (sem plugin) — fonte canônica; Dataview é enhancement. ([[0002-dashboards-plugin-free|ADR-0002]])
- Só dev-Brain é escrevível. `mailerweb-brain` read-only.

Ver [[routing]] · [[_strategy]] · [[00-index]].
