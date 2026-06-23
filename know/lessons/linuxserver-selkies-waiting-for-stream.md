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
tags: [lesson, docker, obsidian]
keywords: [selkies, webrtc, kasmvnc, obsidian, linuxserver, waiting-for-stream, stream]
aliases: [linuxserver-selkies-waiting-for-stream]
---

# linuxserver/obsidian (Selkies) preso em "Waiting for stream"

## Contexto

A imagem nova `lscr.io/linuxserver/obsidian` passou a usar **Selkies/WebRTC** em vez de KasmVNC. Ao abrir no browser, a tela fica travada e nada carrega.

## Sintoma

> Waiting for stream...

O browser fica indefinidamente nessa mensagem.

## Causa

`docker logs` mostrando `Video chunk sender started` indica que o **stream está OK no lado do servidor** — o problema é no lado do cliente/browser. Causas comuns:

1. Um **modal do app** está por cima da tela do stream.
2. Acesso por **http** não é secure-context, e WebRTC exige isso.
3. O Obsidian é instalado **on-demand** e ainda não está presente.

## Solução

1. **Modal por cima** → fechar o modal clicando no `X`.
2. **Secure-context** → acessar via **https** na porta `3001` (ou a mapeada) e **aceitar o certificado self-signed**.
3. **Instalar Obsidian** → clicar no botão **"Instalar obsidian"**. Ele baixa o proot-app (~564M). Os erros `Cannot unlink` durante a instalação são **ruído normal** e podem ser ignorados. O app roda em `/usr/bin/obsidian`.

## Evitar futuro

- Sempre usar **https** (porta mapeada) e aceitar o cert self-signed antes de tentar diagnosticar o stream.
- Confirmar no `docker logs` se o stream está sendo enviado (`Video chunk sender started`) para isolar server vs. client.
- **Alternativa**: usar a **tag antiga com KasmVNC** (http puro), que é mais confiável.

Visto em: [[daily/2026-06-19]]
