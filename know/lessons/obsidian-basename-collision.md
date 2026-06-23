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
tags: [lesson, obsidian]
keywords: [obsidian, wikilink, basename, colisao, shortest-link, vault]
aliases: [obsidian-basename-collision]
---

# Obsidian: wikilink ambíguo por basename igual em pastas diferentes

## Contexto
Vault com `newLinkFormat: "shortest"`. Dois arquivos com o mesmo basename em pastas distintas, ex: `map/prontuario.md` e `graph/prontuario.md`.

## Sintoma
`[[prontuario]]` resolve para o arquivo "errado" de forma imprevisível — o destino muda dependendo do contexto/índice do vault.

## Causa
Com `shortest`, `[[nome]]` é ambíguo quando existe mais de um `nome.md` no vault. O Obsidian escolhe um dos candidatos sem garantia de qual.

## Solução
- Dar nomes distintos por papel: `graph/<slug>-grafo.md` em vez de `graph/prontuario.md`.
- Ou linkar com caminho explícito: `[[pasta/nome]]` (ex: `[[graph/prontuario]]`).

## Evitar futuro
- Não reusar o mesmo basename em pastas diferentes; deixe o papel no nome.
- Para matar nós fantasma de relatórios com wikilinks placeholder, setar `hideUnresolved: true` em `.obsidian/graph.json`.

Visto em: [[daily/2026-06-19]]
