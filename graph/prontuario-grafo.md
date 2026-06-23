---
type: note
scope: prontuario
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: graphify
status: active
confidence: high
last_verified: 2026-06-19
token_policy: summary-first
tags: [graph, code, prontuario]
aliases: [prontuario-graph]
---

# prontuario — grafo de código

> Estrutura real do código (graphify, AST). **1668 nós · 3113 arestas · 89 módulos**.
> Mapa do projeto: [[prontuario]] · relatório bruto: `graph/prontuario/GRAPH_REPORT.md` · grafo: `graph/prontuario/graph.json`.

## Módulos (comunidades, nomeadas pela pasta dominante)

| Módulo | Nós | Pastas | Exemplos |
|--------|-----|--------|----------|
| **model** | 76 | model (36), controller (27), service (13) | `ResultadoExame`, `CtrlManterResultadosExame.java`, `String`, `.ResultadoExame()` |
| **model** | 73 | model (40), controller (19), service (14) | `ConfiguracaoPerfilProfissionalSaude`, `.alterarProfissional()`, `CtrlManterConfiguracaoPerfilProfissionalSaude.java`, `CtrlManterConfiguracaoPerfilProfissionalSaude` |
| **model** | 67 | model (64), controller (3) | `Consulta`, `.Consulta()`, `List`, `LocalDateTime` |
| **model** | 67 | model (36), service (30), (raiz) (1) | `RegistroPessoa`, `.montarJsonRegistroPessoa()`, `ServiceManterRegistrosPessoas`, `.preencherRegistroPessoa()` |
| **model** | 66 | model (30), controller (23), service (13) | `Medicamento`, `CtrlManterMedicamentos.java`, `CtrlManterMedicamentos`, `.from()` |
| **model** | 62 | model (32), controller (17), service (13) | `Departamento`, `CtrlManterDepartamentos.java`, `String`, `ServiceManterDepartamentos` |
| **model** | 54 | model (33), service (21) | `RegistroLog`, `ServiceManterRegistroLog`, `.RegistroLog()`, `ServiceManterRegistroLog.java` |
| **model** | 51 | model (37), service (14) | `TipoExame`, `ServiceManterTiposExame`, `.setClassificacao()`, `.getClassificacao()` |
| **controller** | 50 | controller (26), model (24) | `CtrlManterPosologias.java`, `Posologia`, `.from()`, `CtrlManterPosologias` |
| **model** | 43 | model (28), service (15) | `Reserva`, `.alterar()`, `ServiceManterReservas`, `.validarConflitosDeHorario()` |
| **model** | 42 | model (24), service (18) | `Endereco`, `.montarJsonEndereco()`, `.preencherEndereco()`, `String` |
| **model** | 38 | model (26), service (12) | `ItemDisponibilidade`, `String`, `.alterarItemDisponibilidade()`, `ServiceManterItensDisponibilidade` |
| **model** | 36 | model (36) | `Usuario`, `String`, `.Usuario()`, `.setConta()` |
| **model** | 31 | model (19), service (12) | `Empregado`, `String`, `ServiceManterEmpregados`, `.Empregado()` |
| **model** | 31 | model (19), service (12) | `SalaAtendimento`, `ServiceManterSalasAtendimento`, `SalaAtendimento`, `String` |

## Hubs (god nodes — maior conectividade)

| Símbolo | Grau | Arquivo |
|---------|------|---------|
| `Consulta` | 50 | `src/main/java/model/Consulta.java` |
| `ResultadoExame` | 30 | `src/main/java/model/ResultadoExame.java` |
| `Usuario` | 29 | `src/main/java/model/Usuario.java` |
| `ConfiguracaoPerfilProfissionalSaude` | 27 | `src/main/java/model/ConfiguracaoPerfilProfissionalSaude.java` |
| `RegistroPessoa` | 24 | `src/main/java/model/RegistroPessoa.java` |
| `Perfil` | 23 | `src/main/java/model/Perfil.java` |
| `TipoExame` | 23 | `src/main/java/model/TipoExame.java` |
| `Endereco` | 21 | `src/main/java/model/Endereco.java` |
| `ItemDisponibilidade` | 21 | `src/main/java/model/ItemDisponibilidade.java` |
| `.montarJsonRegistroPessoa()` | 20 | `src/main/java/service/ServiceManterRegistrosPessoas.java` |
| `Medicamento` | 20 | `src/main/java/model/Medicamento.java` |
| `AplicacaoDose` | 19 | `src/main/java/model/AplicacaoDose.java` |

> Hub com grau muito alto + nome genérico = candidato a quebrar em peças menores (ver [[_strategy]]).

<!-- @user:start -->
## 🧠 Leitura arquitetural

Os módulos dominantes contam uma história clara e repetitiva: quase toda comunidade do grafo é rotulada **model** e tem a mesma assinatura — uma entidade JPA orbitada pelo seu `CtrlManter*` e `ServiceManter*` correspondentes (`ResultadoExame` + `CtrlManterResultadosExame` + `ServiceManterResultadosExame`; `Medicamento` + `CtrlManterMedicamentos` + `ServiceManterMedicamentos`; `Departamento`, `Reserva`, `Empregado`, `TipoExame`...). Isso confirma o que o mapa [[prontuario]] já indica: arquitetura em 3 camadas estritamente **vertical por agregado**, um CRUD por entidade. É previsível e fácil de navegar, mas a comunidade `model`#0 mistura `model`(36)/`controller`(27)/`service`(13) — sinal de que controller e service estão fortemente colados à entidade, sem camada de DTO/contrato isolando o domínio da borda HTTP.

Sobre os hubs de maior grau: a maioria é **coesão saudável de domínio**, não god-object. `Usuario`(29), `Perfil`(23), `Endereco`(21) e `RegistroPessoa`(24) são entidades naturalmente referenciadas por muitas outras — alto grau aqui é esperado. A exceção a vigiar é `Consulta` (grau **50**, `src/main/java/model/Consulta.java`), quase o dobro do segundo colocado: é o agregado central do prontuário (liga `Usuario`, `RegistroDoenca`, exames, datas) e tem real risco de virar entidade-Deus. No lado service, `.montarJsonRegistroPessoa()` (grau 20) e `.montarJsonEndereco()` (grau 16) revelam **serialização JSON feita à mão dentro do service** — acoplamento que cresce com cada campo novo e que um DTO/mapper eliminaria.

Pontos de acoplamento/risco:

- **`Consulta` como hub crítico**: grau 50 concentra dependências do prontuário inteiro — mudança nessa entidade propaga para meio grafo. Candidata nº1 a decompor (extrair `RegistroDoenca`, exames e agendamento para sub-agregados). Ver [[_strategy]].
- **Ausência de camada DTO**: `controller` e `model` aparecem juntos em quase toda comunidade (ex.: comunidade `controller`#9 com controller(26)/model(21)); entidades JPA vazam direto para a borda REST.
- **Serialização manual em service** (`montarJson*`, `preencher*`): lógica repetida e frágil em `ServiceManterRegistrosPessoas` e `ServiceManterEnderecos`.
- **`ConfiguracaoPerfilProfissionalSaude`** (grau 27) + `ConfiguracaoPerfil`/`ConfiguracaoPerfilAdministrativo`: hierarquia de perfis com forte ramificação, vale revisar se a herança está bem modelada.

Ações concretas:

1. **Introduzir DTOs/records de request-response** entre `controller` e `model`, movendo a montagem de JSON para mappers e tirando `montarJson*` dos services — desacopla a borda HTTP da entidade JPA e remove serialização à mão. Ver [[java-spring]] e [[code-style]].
2. **Decompor `Consulta`**: extrair sub-agregados e usar fetch/projeções para o que hoje é carregado em bloco; reduz o grau e o custo de queries do agregado mais quente. Ver [[java-spring]] e [[performance]].
<!-- @user:end -->

Ver [[00-graph-index]] · padrões em [[routing]].