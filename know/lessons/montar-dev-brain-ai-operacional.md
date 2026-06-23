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
tags: [lesson, meta, dev-brain, architecture]
keywords: [dev-brain, second-brain, ai-operational, vault, obsidian, graphify, policy-task, embeddings, claude-code, context-economy]
aliases: [montar-dev-brain-ai-operacional]
---

# Como montar um dev-Brain AI-operacional (não vault decorativo)

**Contexto:** criar uma camada de memória pra agentes (Claude Code) reduzir token e responder melhor sobre múltiplos projetos — não "notas bonitas no Obsidian".

**O que funciona (validado nesta montagem):**
1. **Dois cérebros, papéis separados.** dev-Brain = *policy + architecture memory* (COMO codar, universal, mantido 100% pela IA). Domínio = *task + domain memory* read-only (mailerweb-brain, git da empresa). Roteamento decide qual abrir → não relê o monolito (~200k tokens) pra achar 1 regra.
2. **Roteador, não enciclopédia.** `CLAUDE.md` pequeno aponta pra `routing.md`; `know/` por stack; skills carregam procedimento só quando usadas; subagents isolam contexto.
3. **3 visões complementares de grafo:** links (Obsidian, intenção) + estrutura (graphify AST, realidade do código) + semântica (embeddings, relação não-linkada). Cruzar as 3 acha "link faltando" e "doc faltando".
4. **graphify como fonte consultável**, não enfeite: `graph.json`/digest/`graphify query` economizam token; o HTML é só pro humano.
5. **token_weight por projeto** (`projects/*-proj.md`): agente decide o menor contexto antes de carregar (crítico → nunca abrir repo inteiro).
6. **Loop de aprendizado:** hook SessionEnd (breadcrumb) + skill `/journal` (lição reutilizável). Memória que depende de lembrar morre em dias → automatizar.
7. **audience: ai|human** no frontmatter — nem tudo entra no vetor/IA; navegação/diário é só humano.

**Anti-padrões (evitar):**
- Nota gigante "tudo sobre X" → quebrar em notas pequenas (hub falso confunde IA).
- Confundir **afazer com lição** (TODO vai pra pendência, não pra `lessons/`).
- Clusterizar nas coords 2D do UMAP (artefato) → clusterizar nos **embeddings**; 2D é só desenho.
- Embedar nota inteira → menção incidental polui o vetor; embedar **título+tags+keywords+cabeça**.
- Colisão de basename entre pastas (`map/x.md` vs `graph/x.md`) → sufixo por papel (`-grafo`, `-proj`).
- IA escrever no vault de domínio da empresa → **read-only**, output só no dev-Brain.
- Plugin demais → poucos, confiáveis (plugin roda código de terceiros).

**Baseado em quê (fontes/evidência):**
- **graphify** (safishamsi/graphify) — código→grafo consultável, merge cross-repo, MCP.
- **Embeddings locais** (sentence-transformers MiniLM multilingual) + UMAP + HDBSCAN — mapa semântico + missing-links.
- **Conceitos Claude Code** (CLAUDE.md enxuto, skills load-on-demand, subagents, hooks) — automação e economia de contexto.
- **Relatos de campo + análise do Pedro** — vault pequeno, daily-note-first, expansão gradual, policy vs task/domain memory, não automatizar tudo no dia 1.
- **Prática validada na própria montagem** — diagnósticos reais (cosseno 0.46→0.196 após embedding focado; clobber resolvido com `@user`; drift detectado pelo hook).

**Evitar futuro:** começar pequeno e operacional; cada peça nova justifica redução de token ou aumento de acerto; medir (diagnosticar) antes de aceitar "ficou bom".
**Relacionado:** [[_strategy]] · [[routing]] · [[hybrid-views]] · [[_frontmatter]] · [[_mailerweb-access]]
**Visto em:** [[daily/2026-06-19]]
