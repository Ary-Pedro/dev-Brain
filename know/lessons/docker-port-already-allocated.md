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
tags: [lesson, docker]
keywords: [docker, compose, porta, port-allocated, conflito]
aliases: [docker-port-already-allocated]
---

# docker: Bind for 0.0.0.0:PORT failed: port is already allocated

## Contexto

Ao subir um container (ex. via `docker compose up`), ele falha porque a porta do host que ele tenta mapear já está em uso por outra aplicação.

## Sintoma

```
driver failed programming external connectivity ... Bind for 0.0.0.0:3001 failed: port is already allocated
```

## Causa

Outra aplicação já está usando a porta do host. No mapeamento `HOST:CONTAINER` do compose, a porta do lado HOST está ocupada.

## Solução

1. Descobrir quem ocupa a porta:

```bash
docker ps --format "{{.Names}} {{.Ports}}" | grep PORTA
ss -ltnp | grep PORTA
```

2. Remapear a porta HOST no compose, mantendo a do container. Ex.:

```yaml
ports:
  - "3838:3000"   # troca só o lado HOST; container continua em 3000
```

## Evitar futuro

- Verificar portas livres antes de definir o mapeamento (`ss -ltnp`).
- Padronizar/documentar quais portas HOST cada serviço usa para não colidir.

## Visto em: [[daily/2026-06-19]]

Ex.: o frontend do mailerweb ocupava a porta 3001.
