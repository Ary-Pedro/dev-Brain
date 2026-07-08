---
tags: [lesson, react, debug]
keywords: [rota, componente errado, modal, URL, route, debugging]
aliases: [route-antes-de-editar-componente]
---

# Modal/tela errada: trace rota antes de editar componente

**Contexto:** Bug visual — modal ou tela mostra comportamento errado. Há vários candidatos de componentes que poderiam causar isso.

**Sintoma:** Edita arquivo X repetidamente, build passa, comportamento não muda. Arquivo errado.

**Causa:** O componente editado não é o que serve aquela rota. Exemplo real: `/campaigns/template` → `CampaignsPage` (não `TemplatesGalleryPage`). Ambos renderizam templates, mas o router aponta para o primeiro.

**Solução:**
1. Anota a URL exata que o user está vendo
2. Abre `App.jsx` (ou arquivo de rotas) e busca esse path
3. Identifica o componente exato que serve a rota
4. Só então edita

```bash
grep -n "campaigns/template" frontend/src/App.jsx
```

**Evitar futuro:** Nunca assumir qual componente serve uma rota pelo nome do arquivo. Sempre verificar o router antes de qualquer edit em bug visual.

**Visto em:** [[daily/2026-06-26]] · sessão feature/waba-integration
