---
type: note
scope: faculdade-alessandro
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: graphify
status: active
confidence: high
last_verified: 2026-06-19
token_policy: summary-first
tags: [graph, code, faculdade-alessandro]
aliases: [faculdade-alessandro-graph]
---

# faculdade-alessandro — grafo de código

> Estrutura real do código (graphify, AST). **379 nós · 793 arestas · 23 módulos**.
> Mapa do projeto: [[faculdade-alessandro]] · relatório bruto: `graph/faculdade-alessandro/GRAPH_REPORT.md` · grafo: `graph/faculdade-alessandro/graph.json`.

## Módulos (comunidades, nomeadas pela pasta dominante)

| Módulo | Nós | Pastas | Exemplos |
|--------|-----|--------|----------|
| **Models** | 36 | Models (36) | `ResultadoExame`, `String`, `.ResultadoExame()`, `TipoExame` |
| **model** | 36 | model (36) | `ResultadoExame`, `String`, `.ResultadoExame()`, `TipoExame` |
| **model** | 33 | model (25), controller (8) | `Consulta`, `String`, `.Consulta()`, `from()` |
| **static** | 33 | static (33) | `app.js`, `exibirErro()`, `carregarConsultas()`, `carregarTiposExame()` |
| **Models** | 32 | Models (32) | `TipoExame`, `ResultadoExame`, `String`, `.TipoExame()` |
| **model** | 32 | model (32) | `TipoExame`, `ResultadoExame`, `String`, `.TipoExame()` |
| **service** | 27 | service (20), model (7) | `ServiceManterResultadosExame`, `Transactional`, `ResultadoExame`, `.consultarResultadoExame()` |
| **controller** | 25 | controller (25) | `CtrlManterTiposExame`, `CtrlManterTiposExame.java`, `ResponseEntity`, `TipoExameResponse` |
| **service** | 25 | service (19), model (6) | `.obterTipoExame()`, `ServiceManterTiposExame`, `Transactional`, `.incluirTipoExame()` |
| **controller** | 23 | controller (23) | `CtrlManterResultadosExame`, `ResponseEntity`, `CtrlManterResultadosExame.java`, `ResultadoExameResponse` |
| **controller** | 19 | controller (19) | `CtrlManterConsultas.java`, `CtrlManterConsultas`, `ResponseEntity`, `.alterarConsulta()` |
| **service** | 15 | service (15) | `.alterarConsulta()`, `ServiceManterConsultas.java`, `ServiceManterConsultas`, `Transactional` |
| **controller** | 10 | controller (10) | `ModelException`, `.tratarErroDeModelo()`, `.tratarArgumentoInvalido()`, `CtrlTratadorErros.java` |
| **Models** | 9 | Models (4), model (4), (raiz) (1) | `ModelException`, `ModelException`, `Exception`, `.ModelException()` |
| **controller** | 9 | controller (9) | `.api()`, `CtrlInicio.java`, `CtrlInicio`, `.inicio()` |

## Hubs (god nodes — maior conectividade)

| Símbolo | Grau | Arquivo |
|---------|------|---------|
| `app.js` | 32 | `src/main/resources/static/js/app.js` |
| `ResultadoExame` | 30 | `Models/ResultadoExame.java` |
| `ResultadoExame` | 30 | `src/main/java/model/ResultadoExame.java` |
| `TipoExame` | 26 | `Models/TipoExame.java` |
| `TipoExame` | 26 | `src/main/java/model/TipoExame.java` |
| `Consulta` | 19 | `src/main/java/model/Consulta.java` |
| `.obterTipoExame()` | 12 | `src/main/java/service/ServiceManterTiposExame.java` |
| `CtrlManterResultadosExame` | 11 | `src/main/java/controller/CtrlManterResultadosExame.java` |
| `CtrlManterTiposExame` | 11 | `src/main/java/controller/CtrlManterTiposExame.java` |
| `ServiceManterResultadosExame` | 11 | `src/main/java/service/ServiceManterResultadosExame.java` |
| `ServiceManterTiposExame` | 11 | `src/main/java/service/ServiceManterTiposExame.java` |
| `exibirErro()` | 11 | `src/main/resources/static/js/app.js` |

> Hub com grau muito alto + nome genérico = candidato a quebrar em peças menores (ver [[_strategy]]).

<!-- @user:start -->
## 🧠 Leitura arquitetural

A distribuição das comunidades confirma uma arquitetura em camadas Spring clássica e bem comportada: os módulos dominantes se organizam por papel (`model`, `service`, `controller`) e por entidade de domínio (`TipoExame`, `Consulta`, `ResultadoExame`). Os maiores módulos são entidades JPA (`ResultadoExame`, `TipoExame` com 36/32 nós), seguidos pelas camadas `service` (`ServiceManterResultadosExame`, `ServiceManterTiposExame`) e `controller` (`CtrlManterTiposExame`, `CtrlManterResultadosExame`, `CtrlManterConsultas`). Há ainda um módulo `static` isolado em torno de `app.js` — todo o front vive num único arquivo JS. O fluxo `controller → service → model/repository` é o esperado para [[java-spring]], e o `CtrlTratadorErros` (`@ControllerAdvice`) como módulo próprio é sinal de tratamento de erro centralizado e saudável.

O ruído mais gritante do grafo é estrutural, não de design: **cada entidade e seu módulo aparecem duplicados** (`Models/ResultadoExame.java` e `src/main/java/model/ResultadoExame.java`, ambos grau 30; idem `TipoExame` grau 26; idem o módulo `ModelException` repartido entre `Models/`, `model/` e `(raiz)`). Isso é o resíduo de pasta `Models/` na raiz já flagrado no mapa — o grafo agora quantifica o custo: inflaciona contagem de nós/comunidades e cria dois pontos de verdade para a mesma entidade. Não é god-object; é cópia morta a apagar (ver [[code-style]]).

Sobre os hubs de maior grau: `ResultadoExame` (30) e `TipoExame` (26) concentram conectividade por serem entidades centrais referenciadas por service, controller, DTOs e repository — é **coesão de domínio saudável**, não god-object; entidades anêmicas com getters/setters naturalmente têm alto fan-in. O caso a vigiar é `app.js` (grau 32, o maior do grafo, com `exibirErro()`, `carregarConsultas()`, `carregarTiposExame()`, `salvarResultadoExame()` todos no mesmo arquivo): aqui sim há acúmulo de responsabilidades num único módulo procedural — candidato a fatiar por recurso. No back-end o acoplamento está sob controle: a presença de `model` dentro dos módulos `service` (7 e 6 nós) é só o service manipulando suas entidades, não vazamento de camada.

Ações concretas:
- **Remover a duplicata `Models/` da raiz** e deixar `src/main/java/model/` como fonte única — elimina os pares de nós espelhados e o módulo `ModelException` fragmentado ([[code-style]], [[java-spring]]).
- **Quebrar `app.js`** em módulos por recurso (tipos de exame / consultas / resultados) + um util de UI para `exibirErro`/`mostrarMensagem`, reduzindo o hub de grau 32 antes que vire dívida real ([[typescript-next]], [[code-style]]).
<!-- @user:end -->

Ver [[00-graph-index]] · padrões em [[routing]].