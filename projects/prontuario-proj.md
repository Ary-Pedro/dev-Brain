---
type: project
project: prontuario
scope: prontuario
repo_path: ~/devSpace/projeto/prontuario
stack: [java, spring-boot, maven, h2]
brain_policy: dev-brain
write_policy: dev-brain-only
domain_brain: (nenhum)
status: active
token_weight: médio
token_policy: summary-first
graph_nodes: 1648
graph_edges: 3094
source: human+graphify
audience: ai
tags: [project]
---

# prontuario — CARD VIVO

> Camada operacional para o agente decidir contexto antes de agir. Mapa estático em [[prontuario]] · Grafo em [[prontuario-grafo]] · Roteamento em [[routing]].

<!-- @generated:start -->
## Objetivo

Sistema de prontuário/saúde acadêmico (UniLaSalle-RJ, 7º período, 2026/1). Backend Spring Boot 3.3.2 REST (Java 17, Maven) + front estático em `static/`, persistência JPA/Hibernate sobre H2 file. Arquitetura clássica em 3 camadas: `controller` (`CtrlManter*`, ~22) → `service` (`ServiceManter*`, ~20) → `model` + `model/repository` (entidades JPA, ~33). Entrypoint `controller.CtrlPrograma` na porta 8081. Domínio núcleo: Consulta, ResultadoExame/TipoExame, Usuario/Perfil, RegistroPessoa, Medicamento/Posologia, Reserva/Disponibilidade.

## Como consultar

1. **Domínio (regra/fluxo do prontuário)** → SOMENTE dev-Brain. Projeto independente, NÃO citar MailerWeb (anti-alucinação).
2. **Padrão (como escrever código)** → `know` (Java/Spring → [[java-spring]]; universais: [[_principles]] [[code-style]] [[naming]] [[error-handling]] [[testing]] [[security]] [[git-commits]]).
3. **Estrutura (onde algo vive / dirs / entrypoints)** → [[prontuario-grafo]] + [[prontuario]] (mapa).
4. **Relação (quem usa quem / impacto / caminho entre nós)** → `graphify query`.

## Peso p/ IA

`token_weight=médio` → NÃO carregar o grafo inteiro. Começar pelo digest (`graph/prontuario.digest.json`: 1648 nós, 3094 arestas, 84 comunidades) e refinar com `graphify query`. God nodes para orientar impacto: `Consulta` (deg 50), `ResultadoExame` (30), `Usuario` (29), `ConfiguracaoPerfilProfissionalSaude` (27), `RegistroPessoa` (24). Tocar nesses = raio de impacto alto.

## Próxima ação

- Endereçar dívida de governança mapeada no recon: ausência de suíte de testes + `mvn -DskipTests` no `Dockerfile` (zero rede de proteção) → [[testing]].
- `ddl-auto=update` e credenciais H2 default / console `/h2-console` exposto → [[security]].
- Pacotes na raiz sem namespace de domínio (`controller`/`service`/`model` em vez de `br.unilasalle.prontuario`) → [[naming]].
<!-- @generated:end -->

<!-- @user:start -->
(observações manuais do Pedro)
<!-- @user:end -->
