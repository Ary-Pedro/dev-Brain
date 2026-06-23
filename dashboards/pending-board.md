---
type: moc
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: human
source: ai
status: active
tags: [meta, dashboard]
---
# ⏳ Pendências & correções — dashboard

> Requer **Dataview** p/ a tabela. Correções abertas:

```dataview
TABLE status
FROM "know/corrections"
WHERE contains(tags, "corrections")
```

## Pendências conhecidas (manuais)
- [x] Restart p/ ativar `context-economist` + `brain-architect` — verificado (6 agents no registry, boot ok)
- [ ] P2 Obsidian browser (stream Selkies) — cosmético (pendente)
- [x] P3 graphify semântico — rodado em `meudinheiro-v2` (34 nós semânticos, 3 hyperedges). Próximos sugeridos: `prontuario`, `mailerweb-portal`. **NÃO** panel-v2 (crítico, caro) sem plano do [[context-economist]].
- [x] M2 vector map cor por tag-domínio — `graph/mailerweb_vector_map_domain.html` (flag `--domain`, 5 buckets; mapa por-pasta preservado)
- [x] Triar `graph/*_missing-links.md` — 10 links de alta confiança aplicados (8 notas); pares espúrios e os 46 do mailerweb (read-only) rejeitados

## Follow-ups novos (descobertos 2026-06-19)
- [x] Gap #1 — 3 proj cards faltantes (theds-panel/wiks/faculdade-atvdd) criados com `token_weight`
- [x] Gap #2/#3 — frontmatter normalizado ao schema [[_frontmatter]] em 69 notas (64 via workflow multiagente + 5 proj cards `scope`)
- [x] Geradores emitem frontmatter canônico — `summarize.py`/`vector-map.py`/hooks `dev-brain-journal`+`dev-brain-sync` patchados; `doctor` confirma 0 erros
- [x] Grafo **semântico** propagado — meudinheiro + prontuario + portal (3/5). panel-v2/faculdade pulados ([[0003-stack-e-fluxo-2026-06|ADR-0003]])
- [ ] Re-triar `dev-brain_missing-links.md` (73 pares) via [[brain-architect]]

## Sessão 2026-06-23 — doctor + context-packet + stack/fluxo

Entregue: `scripts/doctor.py` (saúde do vault, 0 erros) · `scripts/context-packet.py` + template (entrada mínima da IA) · status real de plugins ([[obsidian-plugins]]) · regra de destilação + camadas de contexto ([[flow]]) · [[0003-stack-e-fluxo-2026-06|ADR-0003]] · fix bug `brain_policy` (4 cards) + stack panel-v2 (postgres→mysql) + schema `_frontmatter` (meta/brain_policy/token_weight/keywords).

TODO abertos:
- [ ] Instalar (GUI) plugins recomendados: `metadata-menu`, `obsidian-advanced-uri`, `excalibrain`
- [ ] **Notas de stack desatualizadas** (audit): `typescript-next` (Next 15/16 caching/Turbopack) · `java-spring` (3.3 EOL → 3.5/4.x) · `python-django` (async + 5.2 LTS) · exemplo Celery `select_for_update` fora de atomic
- [ ] WABA trio: links recíprocos + reavaliar `scope` (genérico Meta = cross-repo?) ([[brain-architect]])
- [ ] context-packet: filtrar lessons cross-repo por stack (hoje puxa Django em projeto Next)
- [ ] **Codex→Claude equivalentes** (regra: ignorar Codex, usar ~/.claude): faltam `dba`, `uiux`, `monitor` — criar skill/agent se a demanda aparecer (hoje: doctor cobre monitor-de-vault; security-auditor/code-architect/code-reviewer já existem em plugins)
- [ ] Prioridade 5 (fatiar mailerweb por domínios): **bloqueado** — mailerweb-brain é read-only; só dá p/ instruir [[mailerweb-bridge]] a retornar escopo-domínio, não criar `domains/` lá
