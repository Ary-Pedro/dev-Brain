---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: human
status: active
tags: [meta, moc]
---

# 00-index — Mapa do dev-Brain

> Map of Content. Ponto de entrada do vault. Comece por [[routing]].

## 🧭 Como o Claude usa

1. [[routing]] — qual brain consultar por projeto
2. `know/` — boas práticas a aplicar (o COMO)
3. `map/` — onde fica cada projeto (o ONDE, resumido)
4. `graph/` — grafo de código (graphify)
5. [[flow]] — loop operacional (tasks/kanban/templates/decisions/journal)

## 📐 know/ — Governança (universal)

- [[_principles]] — como pensar antes de codar
- [[code-style]] · [[naming]] · [[docstrings]] · [[comments]]
- [[git-commits]] · [[testing]] · [[error-handling]] · [[security]] · [[performance]]
- [[corrections]] — vícios detectados a corrigir · [[_toolbox]] — skills/agents/plugins (auto)
- [[_mailerweb-access]] — 🔒 mailerweb-brain é SOMENTE LEITURA (regra dura)
- [[lessons]] — memória reutilizável (problema→solução keyworded) · `daily/` — diário de sessões

### Por stack
- [[python-django]] · [[java-spring]] · [[typescript-next]]

## 📦 projects/ — cards vivos (camada operacional)

Estado vivo de cada projeto (stack, repo_path, **token_weight**, brain_policy, próxima ação). O agente consulta ANTES de carregar contexto pesado.
- [[mailerweb-panel-v2-proj|panel-v2]] (crítico) · [[theds-panel-proj|theds]] (crítico) · [[mailerweb-portal-proj|portal]] · [[wiks-proj|wiks]] · [[prontuario-proj|prontuario]] · [[faculdade-alessandro-proj|faculdade]] · [[faculdade-atvdd-proj|atvdd]] · [[meudinheiro-v2-proj|meudinheiro]]

## 🤖 agents/ — sub-agents

- [[mailerweb-bridge]] — ponte read-only pro domínio MailerWeb (lê mailerweb-brain, não duplica)
- [[dev-django]] · [[dev-spring]] · [[dev-next]] — devs sênior por stack
- [[context-economist]] — decide o MENOR contexto p/ a tarefa (economia de token)
- [[brain-architect]] — mantém o vault (frontmatter, links, missing-links, @user)

> Padrão de metadata: [[_frontmatter]] (campo `audience: ai|human` controla o que entra no vetor/IA). Diagramas: [[_diagramas]].

## 📊 dashboards/ — leitura gerencial + operação

- [[projects-board|projetos]] (tabela gerada por `build-dashboards.py`, sem plugin) · [[lessons-board|lições]] · [[pending-board|pendências]] · [[graph-health-board|saúde do grafo]]
- [[tasks-board|board Kanban]] — planejar/mover cards · [[tasks-open|tarefas abertas]] — Tasks query + convenção que a IA segue

## ⚖️ decisions/ — ADRs (decisões arquiteturais)

Escolha estrutural datada e **imutável** (o POR QUÊ). Ver [[decisions/README\|decisions]] · template em [[_template]].
- [[0001-dois-cerebros-mailerweb-readonly|ADR-0001]] dois cérebros / read-only · [[0002-dashboards-plugin-free|ADR-0002]] dashboards sem plugin

## 🗺️ map/ — Inventário do devSpace

### mailerWeb (universo — domínio em `mailerweb-brain`)
- [[mailerweb-panel-v2]] — Django 5 multi-tenant (brain de domínio: `mailerweb-brain`)
- [[mailerweb-portal]] · [[theds-panel]] · [[wiks]]

### projeto (independentes — só dev-Brain)
- [[prontuario]] — Java/Spring
- [[faculdade-alessandro]] — Java/Spring
- [[faculdade-atvdd]] — integradora
- [[meudinheiro-v2]] — Next.js/TS

## 🕸️ graph/ — graphify + camada semântica

- [[00-graph-index]] — visão-texto dos grafos (1 nó-resumo por repo)
- [[hybrid-views]] — 3 visões: links (Obsidian) · estrutura (graphify) · semântica (vector map)
- [[_strategy]] — policy-brain vs task-brain + matriz link×vetor×graphify

Build: `bash graph/build-all.sh` · resumos: `python graph/summarize.py` · merge global: `graphify merge-graphs`.
