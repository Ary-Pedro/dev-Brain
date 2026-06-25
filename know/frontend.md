---
type: note
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: stable
confidence: high
last_verified: 2026-06-23
token_policy: full
tags: [know, frontend, ui, ux, a11y, stack]
---

# frontend — padrão de UI/UX & front craft

> O **COMO** construir interface de qualidade no `devSpace` (React/Next, e qualquer front). Complementa [[typescript-next]], [[code-style]], [[performance]]. Padrão inviolável — ver [[routing]].

## 1. Componente
- Um componente = uma responsabilidade. Apresentação separada de dados/efeito (container vs view). Props tipadas e mínimas; sem prop booleana que vira N modos (= N componentes).
- Estado o mais **local** possível; subir só quando compartilhado. Server state ≠ UI state (não duplicar dado do servidor em useState).
- Composição > herança/config gigante. Children/slots em vez de mil props.

## 2. Os 4 estados (sempre)
Toda tela que busca dado trata: **loading · erro · vazio · sucesso**. Vazio e erro não são opcionais — são o caminho mais comum no mundo real. Skeleton no loading, mensagem acionável no erro, CTA no vazio.

## 3. Acessibilidade (WCAG — não-negociável)
- HTML semântico primeiro (`button`, `nav`, `label`); ARIA só quando o nativo não cobre.
- Tudo operável por **teclado**; foco visível; ordem de tab lógica; `aria-live` p/ feedback assíncrono.
- Contraste ≥ 4.5:1 (texto). `alt` em imagem com conteúdo, `alt=""` em decorativa. Form: `label` ligado ao input, erro associado por `aria-describedby`.
- Não comunicar só por cor. Respeitar `prefers-reduced-motion`.

## 4. Responsividade & design system
- Mobile-first; breakpoints por conteúdo, não por device. Unidades relativas (`rem`/`%`/`clamp`), `max-width:100%` em mídia.
- Tokens (cor/espaço/tipo) > valores mágicos espalhados. Reusar do design system; não recriar botão.

## 5. Performance percebida
- Bundle: code-split por rota, lazy em pesado, tree-shake. Imagem otimizada (tamanho/format/lazy).
- Evitar re-render desnecessário (memo só com perfil, não preventivo). Otimização prematura é cheiro ([[_principles]]).
- Core Web Vitals: LCP (conteúdo principal cedo), CLS (reserve espaço — sem layout shift), INP (interação responsiva).

## 6. Anti-padrões
- `div` clicável sem role/teclado · só estado de sucesso (sem loading/erro/vazio) · cor como único sinal · estado global pra tudo · `useEffect` pra derivar o que dá pra computar no render · texto fixo sem i18n quando o projeto exige.

Ver também: [[typescript-next]] · [[code-style]] · [[performance]] · [[testing]] · [[_principles]].
