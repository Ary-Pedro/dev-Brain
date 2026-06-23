---
type: note
scope: faculdade-atvdd
repo_path: ~/devSpace/projeto/faculdade_ATVDD_INTEGRADORA/atvdd-integradora-vii
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: active
confidence: low
last_verified: 2026-06-19
token_policy: summary-first
tags: [map, projeto, typescript-next]
---

# faculdade-atvdd-integradora-vii — mapa do projeto

> Atividade Integradora VII (faculdade). Projeto **independente** (sem domínio MailerWeb).
> Localização: `~/devSpace/projeto/faculdade_ATVDD_INTEGRADORA/atvdd-integradora-vii`.

> [!warning] Diretório vazio / install oco
> No recon (2026-06-17) a raiz **só tinha `node_modules/`** — **zero arquivos reais** (`find -type f` → 0), apenas **43 symlinks** em `node_modules/.bin` e shells de pacote vazios. **Não há código-fonte, manifesto (`package.json`), lockfile, README nem `CLAUDE.md`.**
> Toda a seção Stack abaixo é **inferida dos binários instalados**, não de fonte verificada. Antes de codar: restaurar o repo (clonar/checkout) e refazer este mapa a partir do `package.json` real.

## Stack

Inferida dos pacotes/symlinks presentes em `node_modules` (`.bin`):

- **Origem provável:** [Lovable.dev](https://lovable.dev) — presença de `lovable-tagger` é a assinatura de um scaffold Vite + React gerado pela Lovable.
- **Build/dev:** **Vite** (`vite` em `.bin`) + `esbuild`/`rolldown`/`rollup`.
- **Linguagem:** **TypeScript** — `tsc`, `tsserver`, `@typescript-eslint/typescript-estree`, `tsconfck`, `sucrase`.
- **Lint/format:** `eslint` + `eslint-config-prettier` + `prettier`.
- **Imagens:** `sharp` (otimização/transformação de imagens).
- **Deploy/edge:** **Cloudflare Workers** — `wrangler`/`wrangler2`, `miniflare`, `workerd`, `nitro`, `h3`, `srvx` (stack Nitro/Cloudflare).
- **Não confirmado:** React, roteador, Tailwind/shadcn — **não há `react`/`tailwind` instalados** no estado atual (install incompleto). Tratar como hipótese até ver o `package.json`.

> [!note] Tag de stack
> Usei `typescript-next` como tag por ser o rótulo TS/web do vault. **Não é Next.js** — é Vite + (provável) React. Reavaliar quando o fonte aparecer.

## Estrutura

Não há diretórios de projeto no estado atual. Tabela = **expectativa** para um scaffold Vite+React/Lovable (validar após restaurar o repo):

| Dir | Papel (esperado) |
|-----|------------------|
| `src/` | Código-fonte da app (componentes, páginas). |
| `src/components/` | Componentes React. |
| `public/` | Assets estáticos. |
| `node_modules/.bin` | **Único conteúdo real hoje** — symlinks de CLIs (vite, eslint, tsc, wrangler…). |
| `index.html` | Entry HTML do Vite (esperado, ausente). |
| `vite.config.ts` | Config do Vite (esperado, ausente). |
| `wrangler.toml`/`.jsonc` | Config Cloudflare Workers (esperado, ausente). |

## Entrypoints

**Nenhum entrypoint presente no disco.** Esperados num scaffold Vite:

- `index.html` → `src/main.tsx` (bootstrap da SPA). **Ausente.**
- `wrangler.toml` + worker handler, se o deploy for via Cloudflare. **Ausente.**

## Como rodar (comandos)

> Não verificável: sem `package.json`, os scripts são desconhecidos. Comandos abaixo são os **defaults da stack** detectada — só funcionam após restaurar o fonte e rodar `npm install`.

```bash
# 1. restaurar o repositório (não está no disco)
git clone <repo> .        # ou: git checkout / git pull

# 2. instalar deps (o node_modules atual está incompleto)
npm install

# 3. dev / build / preview (Vite)
npm run dev               # vite dev server
npm run build             # vite build
npm run preview           # serve o build
npm run lint              # eslint

# 4. deploy edge (se Cloudflare/Wrangler)
npx wrangler dev
npx wrangler deploy
```

> [!tip] BOM vs RUIM ao documentar este projeto
> ```text
> RUIM: "Projeto React + Tailwind com auth JWT."   ← inventado, nada no disco comprova
> BOM:  "Stack inferida de node_modules/.bin (vite, tsc, wrangler).
>        Fonte ausente; confirmar no package.json após restaurar." ← honesto
> ```

## Padrões aplicáveis

Stack TypeScript/web → seguir as notas de governança do vault:

- [[code-style]] · [[naming]] · [[comments]] · [[docstrings]]
- [[testing]] · [[error-handling]] · [[security]] · [[performance]]
- [[git-commits]] · [[_principles]]

## Roteamento

Projeto **independente** — usar **somente** o vault `dev-Brain`. **Não** roteia para conhecimento/convenções do MailerWeb. Ver [[routing]] para as regras de qual base consultar.

---
Voltar ao [[00-index]].
