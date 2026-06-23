---
type: note
scope: mailerweb
brain_policy: dev-brain
write_policy: read-only
audience: ai
source: human
status: active
confidence: high
last_verified: 2026-06-19
token_policy: summary-first
tags: [map, mailerweb, docs]
---

# wiks — mirror da wiki do GitLab (MailerWeb panel v2)

> Doc-as-prose, **read-only**. Não é código: é a wiki escrita à mão do time, espelhada do GitLab.
> Para "porquê/intenção/onboarding" → wiks. Para "onde/o quê factual" → `mailerweb-brain` (gerado do código).

## Stack

- **Tipo:** repositório de **documentação Markdown** (sem código executável).
- **Conteúdo:** wiki em **PT-BR** do projeto `mailerweb.panel.v2` (Django 5 + React 19 + Vite + Tailwind 4 + Celery/Redis + MySQL 8, tudo em Docker).
- **Origem:** `git remote origin` → `gitlab.com/mailerweb/control-panel/mailerweb.panel.v2.wiki.git`.
- **Sem manifesto:** não há `package.json`, `pyproject`, `pom.xml`, `Dockerfile` nem `manage.py`. Procurar isso aqui é perda de tempo — o código vive em `mailerweb.panel.v2`.

> Atenção: a stack acima é o que a wiki **descreve**, não o que ela **roda**. wiks só renderiza Markdown.

## Estrutura

Raiz real: `~/devSpace/mailerWeb/wiks/mailerweb.panel.v2.wiki/`

| Dir/arquivo | O que tem |
|-------------|-----------|
| `home.md` | Índice mestre da enciclopédia (entrypoint de navegação) |
| `00-crash-course.md` | Resumo executivo de 5 min: stack, 3 regras de ouro, 29 apps, comandos |
| `01-fundamentos/` | Visão geral V1→V2, multi-tenancy, SOA/EventBus, auditoria, glossário, padrões de código, estrutura de pastas, roadmap SOA |
| `02-backend/` | 18 notas por domínio (mensageria, fila/throttling, IA/RAG, billing/ledger, automações, CRM, campanhas, e-commerce/iGaming, API pública…) |
| `03-frontend/` | Estado/contexto, arquitetura UI, motor do construtor, design system (Tailwind 4, tokens `--gd-*`) |
| `04-operacoes/` | Terraform/AWS, pipeline CI/CD, plano de go-live jul/2026 |
| `tutoriais/` | Onboarding narrativo (primeiros passos, backend, frontend, leis da casa, FAQ, fluxo IA/RAG) |
| `certificacao/` | Casos de negócio para QA/certificação |

## Entrypoints

- **Leitura humana:** `home.md` (índice) → ou `00-crash-course.md` para o atalho.
- **Não há entrypoint de execução** (sem `main`, `index.js`, `manage.py`). É conteúdo, não app.

## Como rodar (comandos)

Não se "roda". Opera-se como repo Git de Markdown:

```bash
# atualizar o mirror (read-only — não fazer commit aqui)
git -C ~/devSpace/mailerWeb/wiks/mailerweb.panel.v2.wiki pull

# renderizar localmente, se quiser preview (opcional)
grip ~/devSpace/mailerWeb/wiks/mailerweb.panel.v2.wiki/home.md
```

> BOM: tratar como referência de leitura e dar `pull`.
> RUIM: editar ou commitar aqui — é mirror unidirecional do GitLab; mudanças vão pra wiki no GitLab, não no Git local.

## Padrões aplicáveis

Para **escrever/editar documentação** (caso evolua a wiki upstream), aplicar de `know/`:

- [[code-style]] — clareza, blocos BOM vs RUIM, exemplos dirigidos
- [[naming]] — nomes de arquivo/seção consistentes (já segue `NN-slug.md`)
- [[comments]] · [[docstrings]] — princípios de prosa técnica concisa
- [[testing]] — só relevante para o código documentado, não para a wiki em si

Não há stack de programação a linkar ([[python-django]]/[[java-spring]]/[[typescript-next]] não se aplicam ao wiks; aplicam-se ao projeto documentado, ver [[mailerweb-panel-v2]]).

## Roteamento

Projeto do **UNIVERSO MailerWeb**. Domínio, fluxos e regras de negócio **NÃO** ficam aqui — ficam no vault `mailerweb-brain` (gerado do código) e na própria wiki. dev-Brain só aplica padrão de engenharia/escrita. Ver [[routing]].

- Padrão de engenharia/escrita → dev-Brain `know/` (vence em conflito).
- Domínio/intenção MailerWeb → wiks (porquê) + `mailerweb-brain` (factual).
- Projeto documentado por esta wiki → [[mailerweb-panel-v2]].

Voltar ao [[00-index]].
