# Graph Report - .  (2026-06-19)

## Corpus Check
- Corpus is ~29,339 words - fits in a single context window. You may not need a graph.

## Summary
- 1668 nodes · 3113 edges · 89 communities (81 shown, 8 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 159 edges (avg confidence: 0.8)
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
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]
- [[_COMMUNITY_Community 68|Community 68]]
- [[_COMMUNITY_Community 69|Community 69]]
- [[_COMMUNITY_Community 70|Community 70]]
- [[_COMMUNITY_Community 71|Community 71]]
- [[_COMMUNITY_Community 75|Community 75]]
- [[_COMMUNITY_Community 76|Community 76]]
- [[_COMMUNITY_Community 77|Community 77]]
- [[_COMMUNITY_Community 78|Community 78]]
- [[_COMMUNITY_Community 79|Community 79]]
- [[_COMMUNITY_Community 80|Community 80]]
- [[_COMMUNITY_Community 81|Community 81]]
- [[_COMMUNITY_Community 82|Community 82]]
- [[_COMMUNITY_Community 83|Community 83]]
- [[_COMMUNITY_Community 88|Community 88]]

## God Nodes (most connected - your core abstractions)
1. `Consulta` - 50 edges
2. `ResultadoExame` - 30 edges
3. `Usuario` - 29 edges
4. `ConfiguracaoPerfilProfissionalSaude` - 27 edges
5. `RegistroPessoa` - 24 edges
6. `Perfil` - 23 edges
7. `TipoExame` - 23 edges
8. `Endereco` - 21 edges
9. `ItemDisponibilidade` - 21 edges
10. `Medicamento` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Tela Gerenciar Registros de Log` --conceptually_related_to--> `Permissões locais Claude Code (docker/curl/git)`  [AMBIGUOUS]
  src/main/resources/static/RegistroLog.html → .claude/settings.local.json
- `Tela Gerenciar Salas de Atendimento` --semantically_similar_to--> `Tela Gerenciar Reservas`  [INFERRED] [semantically similar]
  src/main/resources/static/SalaAtendimento.html → src/main/resources/static/Reserva.html
- `ConfiguracaoPerfilAdministrativo` --inherits--> `ConfiguracaoPerfil`  [EXTRACTED]
  src/main/java/model/ConfiguracaoPerfilAdministrativo.java → src/main/java/model/ConfiguracaoPerfil.java
- `ConfiguracaoPerfilProfissionalSaude` --inherits--> `ConfiguracaoPerfil`  [EXTRACTED]
  src/main/java/model/ConfiguracaoPerfilProfissionalSaude.java → src/main/java/model/ConfiguracaoPerfil.java
- `Tela Manter Consultas` --shares_data_with--> `Entidade Profissional de Saúde`  [INFERRED]
  src/main/resources/static/consulta.html → src/main/resources/static/profissional.html

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Fluxo de prescrição: Consulta → Medicamento → Posologia** — prontuario_consulta_screen, prontuario_medicamento_screen, prontuario_posologia_screen [INFERRED 0.85]
- **Fluxo de exames: Consulta → Tipo de Exame → Resultado de Exame** — prontuario_consulta_screen, prontuario_tipoexame_screen, prontuario_resultadoexame_screen [INFERRED 0.85]
- **Fluxo de diagnóstico: Consulta → Problema de Saúde → Registro de Doença** — prontuario_consulta_screen, prontuario_problemadesaude_screen, prontuario_registrodoenca_screen [INFERRED 0.85]
- **Fluxo de agendamento: Sala de Atendimento → Profissional → Reserva** — prontuario_salaatendimento_screen, prontuario_profissional_screen, prontuario_reserva_screen [INFERRED 0.85]

## Communities (89 total, 8 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (28): ConsultaResponse, CtrlManterResultadosExame, ReferenciaId, ResultadoExameRequest, ResultadoExameResponse, TipoExameResponse, ResultadoExame, ResultadoExameRepository (+20 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (29): ConfiguracaoPerfilProfissionalSaudeRepository, CtrlManterConfiguracaoPerfilProfissionalSaude, ConfiguracaoPerfilProfissionalSaude, ConfiguracaoPerfilProfissionalSaudeRepository, ServiceManterConfiguracaoPerfilProfissionalSaude, ServiceManterConfiguracaoPerfilProfissionalSaude, ConfiguracaoPerfilProfissionalSaude, DeleteMapping (+21 more)

### Community 2 - "Community 2"
Cohesion: 0.06
Nodes (16): ConsultaResponse, Consulta, Consulta, ConfiguracaoPerfilProfissionalSaude, List, LocalDateTime, Long, Paciente (+8 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (22): RegistroPessoa, RegistroPessoaRepository, RegistroPessoaRepository, Serializable, ServiceManterRegistrosPessoas, Endereco, LocalDate, Override (+14 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (26): CtrlManterMedicamentos, MedicamentoRequest, MedicamentoResponse, MedicamentoRequest, Medicamento, MedicamentoRepository, ServiceManterMedicamentos, ServiceManterMedicamentos (+18 more)

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (26): CtrlManterDepartamentos, DepartamentoRepository, Departamento, PreAuthorize, Query, DepartamentoRepository, ServiceManterDepartamentos, ServiceManterDepartamentos (+18 more)

### Community 6 - "Community 6"
Cohesion: 0.07
Nodes (23): RegistroLog, RegistroLogRepository, RegistroLogRepository, ServiceManterRegistroLog, Funcionalidade, LocalDateTime, Long, Object (+15 more)

### Community 7 - "Community 7"
Cohesion: 0.08
Nodes (15): TipoExame, TipoExameRepository, ServiceManterTiposExame, List, String, TipoExame, ClassificacaoTipoExame, List (+7 more)

### Community 8 - "Community 8"
Cohesion: 0.08
Nodes (22): ConsultaId, CtrlManterPosologias, MedicamentoId, MedicamentoResponse, PosologiaRequest, PosologiaResponse, Posologia, PosologiaRequest (+14 more)

### Community 9 - "Community 9"
Cohesion: 0.10
Nodes (16): Reserva, ReservaRepository, ReservaRepository, ServiceManterReservas, List, LocalDateTime, Reserva, SalaAtendimento (+8 more)

### Community 10 - "Community 10"
Cohesion: 0.13
Nodes (11): Endereco, ServiceManterEnderecos, List, RegistroPessoa, String, Endereco, EnderecoRepository, List (+3 more)

### Community 11 - "Community 11"
Cohesion: 0.11
Nodes (10): Integer, ItemDisponibilidadeRepository, ItemDisponibilidade, ServiceManterItensDisponibilidade, ConfiguracaoPerfilProfissionalSaude, Override, String, ItemDisponibilidade (+2 more)

### Community 12 - "Community 12"
Cohesion: 0.11
Nodes (8): Usuario, ConfiguracaoPerfil, List, Long, Override, Paciente, RegistroLog, String

### Community 13 - "Community 13"
Cohesion: 0.12
Nodes (10): EmpregadoRepository, Empregado, PrePersist, ServiceManterEmpregados, Departamento, Long, String, Empregado (+2 more)

### Community 14 - "Community 14"
Cohesion: 0.10
Nodes (12): SalaAtendimento, SalaAtendimentoRepository, ServiceManterSalasAtendimento, String, List, Long, Reserva, String (+4 more)

### Community 15 - "Community 15"
Cohesion: 0.14
Nodes (6): Perfil, List, Long, String, TipoAcesso, TipoPerfil

### Community 16 - "Community 16"
Cohesion: 0.12
Nodes (12): UserConfig, ConfiguracaoPerfil, UsuarioRepository, Bean, PasswordEncoder, UsuarioRepository, Long, Perfil (+4 more)

### Community 17 - "Community 17"
Cohesion: 0.13
Nodes (13): ConfiguracaoPerfilAdministrativoRepository, ConfiguracaoPerfilAdministrativo, ServiceManterConfiguracaoPerfilAdministrativo, Perfil, String, Usuario, ConfiguracaoPerfilAdministrativo, List (+5 more)

### Community 18 - "Community 18"
Cohesion: 0.16
Nodes (6): AplicacaoDose, LocalDate, Long, Paciente, String, Vacina

### Community 19 - "Community 19"
Cohesion: 0.14
Nodes (9): Paciente, Plano, Consulta, List, Long, Override, RegistroPessoa, String (+1 more)

### Community 20 - "Community 20"
Cohesion: 0.16
Nodes (11): PosologiaRepository, PosologiaRepository, ServiceManterPosologias, List, Posologia, Consulta, ConsultaRepository, List (+3 more)

### Community 21 - "Community 21"
Cohesion: 0.17
Nodes (13): CtrlManterTiposExame, TipoExameId, TipoExamePaiResponse, TipoExameRequest, TipoExameResponse, ServiceManterTiposExame, DeleteMapping, GetMapping (+5 more)

### Community 22 - "Community 22"
Cohesion: 0.17
Nodes (6): ProblemaDeSaude, List, Long, Override, RegistroDoenca, String

### Community 23 - "Community 23"
Cohesion: 0.20
Nodes (12): CtrlManterConfiguracaoPerfilAdministrativo, ServiceManterConfiguracaoPerfilAdministrativo, ConfiguracaoPerfilAdministrativo, DeleteMapping, GetMapping, List, Long, Perfil (+4 more)

### Community 24 - "Community 24"
Cohesion: 0.20
Nodes (12): CtrlManterRegistroLog, ServiceManterRegistroLog, DeleteMapping, Funcionalidade, GetMapping, List, Long, PostMapping (+4 more)

### Community 25 - "Community 25"
Cohesion: 0.19
Nodes (5): RegistroDoenca, Consulta, Long, ProblemaDeSaude, String

### Community 26 - "Community 26"
Cohesion: 0.25
Nodes (11): CtrlManterRegistrosPessoas, ServiceManterRegistrosPessoas, DeleteMapping, GetMapping, List, Map, Object, PostMapping (+3 more)

### Community 27 - "Community 27"
Cohesion: 0.20
Nodes (11): CtrlManterConfiguracoesPerfil, ServiceManterConfiguracoesPerfil, ConfigurarPerfil, DeleteMapping, GetMapping, List, Long, PostMapping (+3 more)

### Community 28 - "Community 28"
Cohesion: 0.20
Nodes (11): CtrlManterEmpregados, ServiceManterEmpregados, DeleteMapping, Empregado, GetMapping, List, Long, PostMapping (+3 more)

### Community 29 - "Community 29"
Cohesion: 0.24
Nodes (11): CtrlManterEnderecos, ServiceManterEnderecos, DeleteMapping, GetMapping, List, Map, Object, PostMapping (+3 more)

### Community 30 - "Community 30"
Cohesion: 0.20
Nodes (11): CtrlManterFuncionalidades, ServiceManterFuncionalidades, DeleteMapping, Funcionalidade, GetMapping, List, Long, PostMapping (+3 more)

### Community 31 - "Community 31"
Cohesion: 0.20
Nodes (11): CtrlManterPerfis, ServiceManterPerfis, DeleteMapping, GetMapping, List, Long, Perfil, PostMapping (+3 more)

### Community 32 - "Community 32"
Cohesion: 0.20
Nodes (11): CtrlManterProblemasDeSaude, ServiceManterProblemasDeSaude, DeleteMapping, GetMapping, List, Long, PostMapping, ProblemaDeSaude (+3 more)

### Community 33 - "Community 33"
Cohesion: 0.27
Nodes (10): CtrlManterReservas, ServiceManterReservas, GetMapping, Long, Model, PostMapping, RedirectAttributes, Reserva (+2 more)

### Community 34 - "Community 34"
Cohesion: 0.20
Nodes (11): CtrlManterTiposAcesso, ServiceManterTiposAcesso, DeleteMapping, GetMapping, List, Long, PostMapping, PutMapping (+3 more)

### Community 35 - "Community 35"
Cohesion: 0.24
Nodes (10): CtrlManterItensDisponibilidade, ServiceManterItensDisponibilidade, DeleteMapping, GetMapping, ItemDisponibilidade, List, Long, PostMapping (+2 more)

### Community 36 - "Community 36"
Cohesion: 0.29
Nodes (9): CtrlManterSalasAtendimento, GetMapping, Long, Model, PostMapping, RedirectAttributes, SalaAtendimento, ServiceManterSalasAtendimento (+1 more)

### Community 37 - "Community 37"
Cohesion: 0.22
Nodes (5): Funcionalidade, List, Long, String, TipoAcesso

### Community 38 - "Community 38"
Cohesion: 0.24
Nodes (4): Plano, Long, Override, String

### Community 39 - "Community 39"
Cohesion: 0.22
Nodes (4): TipoAcesso, Funcionalidade, Long, Perfil

### Community 40 - "Community 40"
Cohesion: 0.21
Nodes (5): AplicacaoDose, Vacina, List, Long, String

### Community 41 - "Community 41"
Cohesion: 0.24
Nodes (12): carregarConsultas(), carregarMedicamentos(), carregarPosologias(), editarPosologia(), escapeHtml(), formatarData(), humanizeEnum(), logout() (+4 more)

### Community 42 - "Community 42"
Cohesion: 0.16
Nodes (15): Tela Manter Consultas, Entidade Consulta, Entidade Medicamento, Entidade Problema de Saúde, Entidade Profissional de Saúde, Entidade Tipo de Exame, Tela Gerenciar Medicamentos, Tela Gerenciar Posologias (+7 more)

### Community 43 - "Community 43"
Cohesion: 0.26
Nodes (4): ConfigurarPerfil, Long, Perfil, Usuario

### Community 44 - "Community 44"
Cohesion: 0.19
Nodes (6): carregarReservas(), excluirReserva(), profissionais, renderizarTabela(), salas, showMessage()

### Community 45 - "Community 45"
Cohesion: 0.28
Nodes (10): atualizarSelectPai(), carregarClassificacoes(), carregarTiposExame(), editarTipoExame(), limparForm(), logout(), mostrarAlerta(), removerTipoExame() (+2 more)

### Community 46 - "Community 46"
Cohesion: 0.29
Nodes (5): ConfigurarPerfilRepository, ServiceManterConfiguracoesPerfil, ConfigurarPerfil, List, Long

### Community 47 - "Community 47"
Cohesion: 0.27
Nodes (7): carregarMedicamentos(), carregarNiveisControle(), editarMedicamento(), logout(), mostrarAlerta(), removerMedicamento(), renderizarTabela()

### Community 48 - "Community 48"
Cohesion: 0.29
Nodes (5): ProblemaDeSaudeRepository, ServiceManterProblemasDeSaude, List, Long, ProblemaDeSaude

### Community 49 - "Community 49"
Cohesion: 0.29
Nodes (5): ServiceManterConsultas, Consulta, ConsultaRepository, List, Long

### Community 50 - "Community 50"
Cohesion: 0.29
Nodes (5): ServiceManterFuncionalidades, Funcionalidade, FuncionalidadeRepository, List, Long

### Community 51 - "Community 51"
Cohesion: 0.29
Nodes (5): ServiceManterPerfis, List, Long, Perfil, PerfilRepository

### Community 52 - "Community 52"
Cohesion: 0.29
Nodes (5): ServiceManterTiposAcesso, List, Long, TipoAcesso, TipoAcessoRepository

### Community 53 - "Community 53"
Cohesion: 0.31
Nodes (8): carregarItens(), carregarProfissionaisSelect(), editarItem(), excluirItem(), logout(), profissionais, renderizarTabela(), showMessage()

### Community 54 - "Community 54"
Cohesion: 0.31
Nodes (7): carregarResultados(), carregarTiposExame(), editarResultado(), logout(), mostrarAlerta(), removerResultado(), renderizarTabela()

### Community 55 - "Community 55"
Cohesion: 0.36
Nodes (7): carregarLista(), carregarSelects(), editar(), excluir(), logout(), mostrarAlerta(), renderizarTabela()

### Community 56 - "Community 56"
Cohesion: 0.36
Nodes (7): carregarLista(), carregarSelects(), editar(), excluir(), logout(), mostrarAlerta(), renderizarTabela()

### Community 57 - "Community 57"
Cohesion: 0.33
Nodes (8): cancelar(), carregar(), funcionalidades, inicializar(), perfis, remover(), salvar(), showMessage()

### Community 58 - "Community 58"
Cohesion: 0.39
Nodes (6): carregarProfissionais(), editarProfissional(), excluirProfissional(), logout(), renderizarTabela(), showMessage()

### Community 59 - "Community 59"
Cohesion: 0.39
Nodes (6): carregarSalas(), editarSala(), excluirSala(), logout(), renderizarTabela(), showMessage()

### Community 60 - "Community 60"
Cohesion: 0.36
Nodes (6): Authentication, CtrlAutenticacaoInfo, GetMapping, Map, Object, String

### Community 61 - "Community 61"
Cohesion: 0.43
Nodes (5): SecurityConfig, HttpSecurity, SecurityFilterChain, Bean, PasswordEncoder

### Community 62 - "Community 62"
Cohesion: 0.46
Nodes (5): ConfigurarPerfilRepository, ConfigurarPerfil, List, Perfil, Usuario

### Community 63 - "Community 63"
Cohesion: 0.39
Nodes (5): PerfilRepository, List, Perfil, String, TipoPerfil

### Community 64 - "Community 64"
Cohesion: 0.46
Nodes (5): TipoAcessoRepository, Funcionalidade, List, Perfil, TipoAcesso

### Community 65 - "Community 65"
Cohesion: 0.52
Nodes (5): cancelar(), carregar(), remover(), salvar(), showMessage()

### Community 66 - "Community 66"
Cohesion: 0.52
Nodes (5): cancelar(), carregar(), remover(), salvar(), showMessage()

### Community 67 - "Community 67"
Cohesion: 0.52
Nodes (3): ResultadoExameRepository, List, ResultadoExame

### Community 68 - "Community 68"
Cohesion: 0.53
Nodes (3): ConsultaRepository, Consulta, List

### Community 69 - "Community 69"
Cohesion: 0.47
Nodes (3): EmpregadoRepository, Empregado, String

### Community 70 - "Community 70"
Cohesion: 0.50
Nodes (3): ConfigurableServletWebServerFactory, CustomWebServerFactory, Override

### Community 71 - "Community 71"
Cohesion: 0.40
Nodes (3): Exception, ModelException, String

### Community 75 - "Community 75"
Cohesion: 0.60
Nodes (4): getProfissional(), TipoProfissional(), toString(), String

### Community 76 - "Community 76"
Cohesion: 0.50
Nodes (3): FuncionalidadeRepository, Funcionalidade, String

## Ambiguous Edges - Review These
- `Permissões locais Claude Code (docker/curl/git)` → `Tela Gerenciar Registros de Log`  [AMBIGUOUS]
  src/main/resources/static/RegistroLog.html · relation: conceptually_related_to

## Knowledge Gaps
- **87 isolated node(s):** `String`, `Object`, `PostMapping`, `PutMapping`, `DeleteMapping` (+82 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Permissões locais Claude Code (docker/curl/git)` and `Tela Gerenciar Registros de Log`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `ConfiguracaoPerfil` connect `Community 16` to `Community 17`, `Community 1`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Why does `ConfiguracaoPerfilProfissionalSaude` connect `Community 1` to `Community 16`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **What connects `String`, `Object`, `PostMapping` to the rest of the system?**
  _87 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.054385964912280704 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.05441400304414003 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.0642243328810493 - nodes in this community are weakly interconnected._