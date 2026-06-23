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
tags: [meta, automation, obsidian]
---

# Plugins Obsidian — Shortlist Curada (AI-first)

## 🟢 Estado real (canônico — atualizado 2026-06-23)

| Status | Plugins | Nota |
|--------|---------|------|
| **Ativos agora** (8) | `dataview` · `obsidian-tasks-plugin` · `templater-obsidian` · `obsidian-kanban` · `obsidian-linter` · `obsidian-day-planner` · `recent-files-obsidian` · `obsidian-icon-folder` | instalados em `.obsidian/`, verificados |
| **Recomendados (próx.)** | `metadata-menu` (frontmatter tipado — sustenta o schema [[_frontmatter]]) · `obsidian-advanced-uri` (deep-link terminal↔Obsidian) · `excalibrain` (navegação humana por relações) | adicionar quando der |
| **Opcionais** | `omnisearch` (+`text-extractor` se PDF/imagem) · `juggl` (só se ExcaliBrain não bastar) | sob demanda |
| **NÃO usar por ora** | `smart-connections` (duplica `vector-map.py` — embeddings/índice/custo) · `obsidian-3d-graph` (decoração) · `obsidian-projects` (descontinuado — Bases+Dataview cobre) | decisão consciente |

> Regra: a verdade do que está **instalado** é `.obsidian/community-plugins.json` + `doctor`. Esta tabela diz o que é **ativo/recomendado/opcional/vetado** — não confundir instalado com planejado. Decisões registradas em [[0003-stack-e-fluxo-2026-06]].

---

> [!info] Escopo deste doc
> Recomendação curada, **não** automação. A instalação é manual (GUI) pelo Pedro.
> Filosofia: **poucos plugins, função clara, IA como camada operacional** — o vault é base de conhecimento para um agente, não decoração visual.

> [!warning] Por que poucos plugins
> Plugin da comunidade executa código de terceiros dentro do vault (risco de supply-chain e de quebra em updates do Obsidian). Quanto menor a superfície, menor o risco. Cada item abaixo justifica seu lugar.

## Decisões do usuário (contexto que molda esta lista)

- **Não usa git por ora** → `Obsidian Git` NÃO é pilar agora. Citado só como **futuro**, quando ele decidir versionar.
- **Não quer expor acesso local/MCP externamente** → a IA consome o vault por **filesystem** (lê os `.md` direto). Logo, **Local REST API / MCP plugin = OPCIONAL/futuro**, não agora.
- **Risco de código de terceiros** → núcleo enxuto, só plugins consolidados e confiáveis.

---

## Núcleo (core) — já ativos, sem instalar nada

Estes vêm com o Obsidian. São a fundação AI-first (estrutura legível por máquina). Apenas garantir que estão **ligados**.

| Core | Função | Prioridade |
|---|---|---|
| Graph | Visão global de conexões entre notas | Agora |
| Backlinks | Mostra quem aponta para a nota atual (contexto reverso) | Agora |
| Properties | Frontmatter YAML editável (metadados que a IA lê) | Agora |
| Daily Notes | Nota diária — base do fluxo de captura/journal | Agora |
| Bases | Tabelas/views nativas sobre as Properties | Agora |

---

## Núcleo mínimo (instalar AGORA) — plugins da comunidade

| Plugin | Função | Prioridade |
|---|---|---|
| `Dataview` | Consulta o vault como banco de dados (queries sobre frontmatter/tasks). Coluna vertebral da camada "dados estruturados que a IA e você consultam". | Agora |
| `Tasks` | Gestão de tarefas embutida nas notas (datas, recorrência, status) — consultável via Dataview. | Agora |
| `QuickAdd` | Captura rápida e criação de notas por template/macro. Reduz fricção de entrada — vault só serve à IA se for alimentado. | Agora |
| `Linter` | Normaliza formatação e frontmatter automaticamente. **Consistência = legibilidade por máquina.** Crítico num vault AI-first. | Agora |
| `Metadata Menu` | Define e edita esquemas de frontmatter (campos tipados) via UI. Garante metadados padronizados que a IA pode confiar. | Agora |
| `Smart Connections` | Busca semântica / notas relacionadas por embeddings, **rodando localmente**. IA "in-vault" sem expor nada externamente. | Agora |
| `Omnisearch` | Busca full-text rápida e fuzzy em todo o vault. | Agora |
| `Text Extractor` | Companheiro do Omnisearch: extrai texto de PDFs/imagens (OCR) para virar pesquisável. | Agora |

> [!note] Smart Connections e privacidade
> Mantém os embeddings/processamento local — alinhado à decisão de **não expor acesso externamente**. Conferir nas configs do plugin se algum modelo remoto está ativado e desligar se não desejado.

---

## Visual — OPCIONAL (instalar só se houver necessidade real)

| Plugin | Função | Prioridade |
|---|---|---|
| `Canvas` (core) | Quadro livre para mapear ideias/relações espacialmente. Já é core — ativar se for usar. | Opcional |
| `Excalidraw` | Diagramas/desenhos à mão dentro do vault. | Opcional |
| `ExcaliBrain` | Grafo hierárquico navegável (pais/filhos/relacionados) sobre o Excalidraw. | Opcional |

> [!tip] Critério para o visual
> Só vale o risco/peso se o desenho **vira artefato reaproveitável** (referenciado por notas/IA). Diagrama decorativo solto = perfumaria, evitar.

---

## Futuro / condicional (NÃO instalar agora)

| Plugin | Função | Quando reconsiderar |
|---|---|---|
| `Obsidian Git` | Versiona o vault via git (histórico, backup, sync). | Quando o usuário **decidir versionar**. Hoje ele não usa git. |
| `Local REST API` | Expõe o vault via API HTTP local (acesso programático/MCP). | Só se a IA precisar **escrever/agir** via API em vez de ler filesystem. Hoje: desnecessário e amplia superfície de exposição. |
| MCP server p/ Obsidian | Conecta o vault a agentes via protocolo MCP. | Mesmo racional do REST API — futuro, não agora. |

---

## Evitar (não recomendados)

- **Projects** — arquivado/sem manutenção. Bases (core) + Dataview cobrem o caso.
- **3D Graph** — efeito visual sem ganho operacional para IA.
- **Perfumaria em geral** — temas pesados, plugins de "produtividade" redundantes, qualquer coisa que adicione código de terceiros sem função clara e única.

---

## Princípio de seleção (resumo)

1. **Função clara e única** — se outro plugin/core já faz, não duplicar.
2. **Legível por máquina antes de bonito** — Linter + Metadata Menu + Properties acima de temas.
3. **Privacidade por padrão** — IA consome por filesystem; nada exposto externamente até decisão explícita.
4. **Superfície mínima** — cada plugin é código de terceiros; menos é mais seguro e mais estável.

Relacionado: [[mcp-obsidian]] — o MCP Obsidian depende do plugin Local REST API listado aqui · vault como `know` base para o agente.
