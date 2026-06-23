---
type: project
project: wiks
repo_path: ~/devSpace/mailerWeb/wiks/mailerweb.panel.v2.wiki
scope: mailerweb
stack: [markdown, docs]
brain_policy: read-domain-from-mailerweb-brain
write_policy: dev-brain-only
domain_brain: mailerweb-brain
status: active
token_weight: médio
graph_nodes: 0
graph_edges: 0
source: human
audience: ai
confidence: med
last_verified: 2026-06-19
token_policy: summary-first
tags: [project, mailerweb, docs]
---

# wiks — card vivo

> Camada operacional p/ o agente decidir contexto antes de ler. Estrutura/índice detalhado no mapa [[wiks]].

<!-- @generated:start -->
## Objetivo

**Mirror read-only da wiki do GitLab** do `mailerweb.panel.v2` (`gitlab.com/mailerweb/control-panel/mailerweb.panel.v2.wiki.git`). Doc-as-prose em PT-BR, **sem código executável** — só Markdown. É a fonte de **porquê / intenção / onboarding** do painel; o **o-quê factual** vem de `mailerweb-brain` (gerado do código). Documenta o projeto [[mailerweb-panel-v2]].

## Como consultar

1. **Porquê / intenção / onboarding** → wiks (esta wiki). Entrypoints: `home.md` (índice) e `00-crash-course.md` (atalho de 5 min).
2. **Domínio factual** (onde está, qual app, regra Z) → `mailerweb-brain` via [[mailerweb-bridge]].
3. **Padrão de escrita/engenharia** (ao evoluir a wiki upstream) → `know/`: [[code-style]] · [[naming]] · [[comments]].
4. Não há stack de programação a aplicar aqui ([[python-django]]/[[typescript-next]] valem ao projeto documentado, não à wiki).

## Peso p/ IA

`token_weight=médio` → corpus de prosa amplo (fundamentos, 18 notas de backend, frontend, operações, tutoriais). **Não slurpar a wiki inteira** — ler página dirigida (`home.md` → seção alvo) ou o crash-course. Para relação/factual, preferir o bridge ao varrer Markdown.

> 🔒 **Repo read-only — mirror unidirecional do GitLab.** NUNCA commitar/editar aqui; mudanças vão pra wiki no GitLab. Atualizar só com `git pull`.

## Próxima ação

Sem ação em aberto. Ao precisar de intenção/onboarding do painel: abrir `home.md`, navegar à seção, citar `file:` da página. Não confundir com [[mailerweb-panel-v2]] (o código).
<!-- @generated:end -->

<!-- @user:start -->
(observações manuais do Pedro)
<!-- @user:end -->

---
Relacionados: [[wiks]] (mapa) · [[mailerweb-panel-v2]] (projeto documentado) · [[mailerweb-bridge]] · [[routing]].
