---
type: decision
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: active
confidence: high
last_verified: 2026-06-23
token_policy: full
tags: [decision, adr, stack, flow, token-economy]
aliases: [ADR-0003]
---

# ADR-0003 — Stack de extensões, integração e fluxo (jun/2026)

- **Status:** aceita
- **Data:** 2026-06-23

## Contexto

Pesquisa sobre extensões Obsidian, ponte MCP, hooks, visualização e economia de token. Objetivo: menor contexto + resposta assertiva, sem colecionar plugin/agente por sofisticação. Cérebro irmão mailerweb-brain é read-only.

## Decisão

1. **MCP / Local REST API:** NÃO expor porta Docker agora. Fonte = filesystem local; IA lê/escreve só `dev-Brain` por filesystem; mailerweb-brain read-only. Se um dia usar Local REST API: só `127.0.0.1`, com token, escrita limitada ao dev-Brain.
2. **Hooks:** automação **passiva** no dev-Brain (SessionEnd→journal→destilação lesson/correction; log passivo de arquivos tocados). NÃO instalar `.git/hooks` em todos os repos; graphify pós-commit fica manual/on-demand — sobretudo no panel-v2.
3. **Extensões:** manter os 8 ativos. Adicionar `metadata-menu` (frontmatter tipado) + `obsidian-advanced-uri` (deep-link). **Adiar** `smart-connections` (duplica `vector-map.py`). 3D/Projects vetados. Ver [[obsidian-plugins]].
4. **Visualização:** `excalibrain` primeiro (navegação humana); HTML graphify/vector = artefato técnico; `juggl` só se faltar; 3D não.
5. **Auto-doc:** padrão explícito `<!-- @generated -->`/`<!-- @user -->` por projeto; `summarize.py` já preserva @user. `--wiki` só em repo pequeno, não no panel-v2.
6. **panel-v2 semântico:** pular por ora (crítico/caro). Usar bridge + digest + busca dirigida por app/feature; semântico só por fatia se necessário.
7. **Entrada da IA:** [[flow|context-packet]] (camadas 0-4), não o vault/repo inteiro. Prefixo de prompt estável p/ cache.

## Alternativas descartadas

- **Expor MCP no Docker agora** — superfície/risco sem necessidade real hoje.
- **graphify pós-commit no panel-v2** — custo CPU/IO + ruído de Git em repo gigante.
- **Smart Connections** — embedding/índice duplicado vs `vector-map.py`.

## Consequências

- Menos token (context-packet + digest + roteamento), menos superfície de plugin/risco.
- Aprendizado formalizado (regra de destilação em [[flow]]) evita vault-cemitério.
- Pendências viram TODO no [[pending-board]] em vez de automação prematura.

Ver [[flow]] · [[obsidian-plugins]] · [[context-economist]] · [[0001-dois-cerebros-mailerweb-readonly]].
