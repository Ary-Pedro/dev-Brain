# Graph Report - .  (2026-06-19)

## Corpus Check
- Corpus is ~7,439 words - fits in a single context window. You may not need a graph.

## Summary
- 379 nodes · 793 edges · 23 communities (21 shown, 2 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]

## God Nodes (most connected - your core abstractions)
1. `ResultadoExame` - 30 edges
2. `ResultadoExame` - 30 edges
3. `TipoExame` - 26 edges
4. `TipoExame` - 26 edges
5. `Consulta` - 19 edges
6. `CtrlManterResultadosExame` - 11 edges
7. `CtrlManterTiposExame` - 11 edges
8. `ServiceManterResultadosExame` - 11 edges
9. `ServiceManterTiposExame` - 11 edges
10. `exibirErro()` - 11 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (23 total, 2 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.12
Nodes (6): ResultadoExame, Consulta, List, Long, String, TipoExame

### Community 1 - "Community 1"
Cohesion: 0.12
Nodes (6): Consulta, List, Long, String, TipoExame, ResultadoExame

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (12): from(), from(), Consulta, Consulta, ConsultaResponse, ResultadoExame, ResultadoExameResponse, List (+4 more)

### Community 3 - "Community 3"
Cohesion: 0.14
Nodes (29): carregarClassificacoes(), carregarConsultas(), carregarResultadosExame(), carregarTiposExame(), carregarTudo(), consultas, editarConsulta(), editarResultadoExame() (+21 more)

### Community 4 - "Community 4"
Cohesion: 0.14
Nodes (6): TipoExame, ClassificacaoTipoExame, List, Long, ResultadoExame, String

### Community 5 - "Community 5"
Cohesion: 0.14
Nodes (6): ClassificacaoTipoExame, List, Long, ResultadoExame, String, TipoExame

### Community 6 - "Community 6"
Cohesion: 0.19
Nodes (13): ResultadoExameRepository, ResultadoExameRepository, ServiceManterResultadosExame, List, Long, ResultadoExame, List, Long (+5 more)

### Community 7 - "Community 7"
Cohesion: 0.19
Nodes (14): CtrlManterTiposExame, ClassificacaoTipoExame, DeleteMapping, GetMapping, List, Long, PostMapping, PutMapping (+6 more)

### Community 8 - "Community 8"
Cohesion: 0.21
Nodes (12): Optional, TipoExameRepository, ServiceManterTiposExame, String, TipoExame, ClassificacaoTipoExame, List, Long (+4 more)

### Community 9 - "Community 9"
Cohesion: 0.23
Nodes (12): CtrlManterResultadosExame, ResultadoExameRequest, ServiceManterResultadosExame, DeleteMapping, GetMapping, List, Long, PostMapping (+4 more)

### Community 10 - "Community 10"
Cohesion: 0.21
Nodes (12): ConsultaRequest, CtrlManterConsultas, ConsultaResponse, DeleteMapping, GetMapping, List, Long, PostMapping (+4 more)

### Community 11 - "Community 11"
Cohesion: 0.30
Nodes (8): ConsultaRepository, ServiceManterConsultas, Consulta, List, LocalDateTime, Long, String, Transactional

### Community 12 - "Community 12"
Cohesion: 0.38
Nodes (7): CtrlTratadorErros, ExceptionHandler, IllegalArgumentException, ModelException, Map, ResponseEntity, String

### Community 13 - "Community 13"
Cohesion: 0.36
Nodes (6): CtrlInicio, Object, ResponseBody, GetMapping, Map, String

### Community 14 - "Community 14"
Cohesion: 0.22
Nodes (5): Exception, ModelException, String, ModelException, String

### Community 16 - "Community 16"
Cohesion: 0.67
Nodes (3): from(), TipoExame, TipoExameResponse

## Knowledge Gaps
- **19 isolated node(s):** `String`, `ConsultaResponse`, `Object`, `Void`, `Void` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ModelException` connect `Community 12` to `Community 6`, `Community 7`, `Community 8`, `Community 9`, `Community 10`, `Community 11`?**
  _High betweenness centrality (0.161) - this node is a cross-community bridge._
- **What connects `String`, `ConsultaResponse`, `Object` to the rest of the system?**
  _19 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.11904761904761904 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.11904761904761904 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.11553030303030302 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.14393939393939395 - nodes in this community are weakly interconnected._
- **Should `Community 4` be split into smaller, more focused modules?**
  _Cohesion score 0.13709677419354838 - nodes in this community are weakly interconnected._