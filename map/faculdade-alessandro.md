---
type: note
scope: faculdade-alessandro
repo_path: ~/devSpace/projeto/controle-exames
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: active
confidence: med
last_verified: 2026-06-19
token_policy: summary-first
tags: [map, projeto, java-spring]
---

# faculdade_alessandro — MAPA

> API REST de controle de exames (CRUD de tipos de exame, consultas e resultados de exame). Projeto acadêmico, **independente**. `groupId=br.edu.faculdade`, `artifactId=controle-exames`.

## Stack

- **Linguagem:** Java 17
- **Framework:** Spring Boot 3.3.5 (`spring-boot-starter-parent`)
- **Web:** Spring MVC + Tomcat embutido (`starter-web`) — `starter-jersey` também presente, mas os controllers usam `@RestController` (MVC), não JAX-RS.
- **Persistência:** Spring Data JPA + Hibernate; banco **H2** em arquivo (`jdbc:h2:file:...`), `ddl-auto=update`.
- **Build:** Maven (`spring-boot-maven-plugin`, `finalName=controle-exames`).
- **Infra:** Docker multi-stage (Maven build → JRE Alpine) + Docker Compose com volume `h2-data`.
- **Front:** estático servido pelo Boot (`static/index.html` + `css/app.css` + `js/app.js`).

## Estrutura

| Dir / arquivo | Papel |
|---|---|
| `pom.xml` | Manifesto Maven; deps e Java 17. |
| `Dockerfile` / `docker-compose.yml` | Build multi-stage e orquestração (porta 8081, volume H2). |
| `src/main/java/controller/` | Camada web. `CtrlPrograma` = entrypoint `@SpringBootApplication`; `CtrlManter*` = endpoints REST; `*Request`/`*Response` = DTOs; `CtrlTratadorErros` = `@ControllerAdvice`. |
| `src/main/java/service/` | Regras de negócio (`ServiceManterTiposExame`, `ServiceManterConsultas`, `ServiceManterResultadosExame`). |
| `src/main/java/model/` | Entidades JPA (`TipoExame`, `Consulta`, `ResultadoExame`, enum `ClassificacaoTipoExame`, `ModelException`). |
| `src/main/java/model/repository/` | Repositórios Spring Data (`*Repository`). |
| `src/main/resources/application.properties` | Config (port 8081, datasource H2, h2-console, show-sql). |
| `src/main/resources/static/` | Front estático (HTML/CSS/JS). |
| `Models/` (raiz) | **Duplicata fora do `src`** de TipoExame/ResultadoExame/Classificacao/ModelException. Não está no classpath de build — provável resíduo. Verificar antes de usar; a fonte de verdade é `src/main/java/model/`. |

> RUIM (estado atual): entidades existem em dois lugares (`Models/` raiz e `src/main/java/model/`). Risco de editar a cópia morta. BOM: manter só `src/main/java/model/` e remover `Models/`.

## Entrypoints

- **Classe main:** `controller.CtrlPrograma` (`@SpringBootApplication(scanBasePackages={"controller","service","model"})`, `@EnableJpaRepositories("model.repository")`, `@EntityScan("model")`).
- **HTTP:** `http://localhost:8081` — UI estática em `/`, console H2 em `/h2-console`.
- **Endpoints REST** (ver `README-Docker.md`): `/tipo-exame/*`, `/consulta/*`, `/resultado-exame/*` (listar/incluir/registrar/alterar/remover).

## Como rodar

Via Docker (caminho recomendado pelo projeto):

```bash
docker compose up --build      # sobe em http://localhost:8081
docker compose down            # para
docker compose down -v         # para + apaga dados do H2
```

Local com Maven:

```bash
./mvnw spring-boot:run         # se houver wrapper; senão: mvn spring-boot:run
mvn clean package -DskipTests  # gera target/controle-exames.jar
mvn test                       # roda testes (starter-test presente)
```

> Defaults configuráveis por env: `SERVER_PORT`, `SPRING_DATASOURCE_URL/USERNAME/PASSWORD`. H2 console: JDBC `jdbc:h2:file:/app/data/testdb`, user `sa`, senha vazia.

## Padrões aplicáveis

Sempre (de `know/`): [[_principles]] · [[code-style]] · [[naming]] · [[docstrings]] · [[comments]] · [[error-handling]] · [[security]] · [[testing]] · [[git-commits]] · [[performance]].

Por stack: [[java-spring]] (Spring Boot, camadas controller→service→repository, DTOs Request/Response, `@ControllerAdvice`).

Pontos de atenção de governança neste repo:
- Pacotes raiz sem prefixo (`controller`, `service`, `model`) em vez de `br.edu.faculdade.*` — fora da convenção de pacote; ver [[naming]].
- `ddl-auto=update` + H2 em arquivo: ok para acadêmico, **não** para produção; ver [[security]] e [[performance]].
- Limpar duplicata `Models/` na raiz (ver [[code-style]]).

## Roteamento

Projeto **independente** — consultar **somente** o dev-Brain. Não citar apps, fluxos ou regras de outros domínios. Stack detectada: Java/Spring → aplicar [[java-spring]] + bases de `know/`. Regra completa em [[routing]].

Voltar ao [[00-index]].
