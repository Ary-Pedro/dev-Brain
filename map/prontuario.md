---
type: note
scope: prontuario
repo_path: ~/devSpace/projeto/prontuario
brain_policy: dev-brain
write_policy: dev-brain-only
audience: ai
source: human
status: active
confidence: high
last_verified: 2026-06-19
token_policy: summary-first
tags: [map, projeto, java-spring]
---

# prontuario — MAPA

> Projeto **independente** (não-MailerWeb). Sistema de prontuário/saúde acadêmico do UniLaSalle-RJ (7º período, 2026/1). Backend Spring Boot REST + páginas estáticas. Recon read-only em `~/devSpace/projeto/prontuario`.

## Stack

| Item | Valor | Fonte |
|------|-------|-------|
| Linguagem | Java 17 | `pom.xml` (`<java.version>17`) |
| Framework | Spring Boot 3.3.2 (parent) | `pom.xml` |
| Build | Maven (`spring-boot-maven-plugin`) | `pom.xml` |
| Web | spring-boot-starter-web (`@RestController`) | `pom.xml` + controllers |
| Persistência | Spring Data JPA + Hibernate | `pom.xml`, `application.properties` |
| Banco | H2 (file `./data/testdb`, `ddl-auto=update`) | `application.properties`, `docker-compose.yml` |
| View | Thymeleaf (dep) + HTML estático em `static/` | `pom.xml`, `resources/static` |
| Segurança | Spring Security + BCrypt, `formLogin` | `SecurityConfig.java`, `CtrlPrograma.java` |
| Validação | spring-boot-starter-validation | `pom.xml` |
| Docs API | springdoc-openapi (Swagger UI) | `pom.xml` |
| Container | Docker multi-stage (Maven→JRE 17 alpine), porta 8081 | `Dockerfile`, `docker-compose.yml` |

> Opinião: arquitetura clássica em 3 camadas (controller/service/model+repository) — coerente, mas pacotes na raiz (`controller`, `service`, `model`) **sem prefixo de domínio** (ex.: `br.unilasalle.prontuario`). Anti-padrão de nomeação de pacote; ver [[naming]].

## Estrutura (dirs-chave)

| Caminho | Papel |
|---------|-------|
| `src/main/java/controller/` | REST controllers `CtrlManter*` (~22), 1 por agregado |
| `src/main/java/service/` | Regras de negócio `ServiceManter*` (~20) |
| `src/main/java/model/` | Entidades JPA + enums + `ModelException` (~33) |
| `src/main/java/model/repository/` | Repositórios Spring Data JPA |
| `src/main/java/controller/filter/` | `SecurityConfig`, `UserConfig` (segurança/auth) |
| `src/main/resources/static/` | Front estático: 13 HTML (CRUD por entidade) |
| `application.properties` (raiz **e** resources?) | Config H2/JPA; há cópia na raiz do projeto |
| `data/` | Arquivo do banco H2 (volume Docker) |
| `Dockerfile` / `docker-compose.yml` | Build/run containerizado |
| `target/` | Artefatos de build (ignorável) |

## Entrypoints

- **Main:** `controller.CtrlPrograma` — `@SpringBootApplication(scanBasePackages={"controller","service","model"})`, `@EnableJpaRepositories("model.repository")`, `@EntityScan("model")`.
- **HTTP:** porta `8081`. REST sob caminhos por recurso, ex. `@RequestMapping("/medicamento")`.
- **H2 console:** `/h2-console` (user `sa`, senha vazia).
- **Swagger UI:** servido pelo springdoc (`/swagger-ui.html`).

## Como rodar (comandos)

```bash
# Docker (recomendado — sobe na 8081)
docker compose up --build
docker compose down       # parar
docker compose down -v    # parar + limpar volume H2

# Maven local
mvn -B -DskipTests package   # gera target/*.jar
java -jar target/*.jar
mvn spring-boot:run          # dev
mvn test                     # testes (nenhuma suíte detectada no recon)
```

> Atenção (governança): `mvn -DskipTests` no `Dockerfile` + ausência de suíte de testes = zero rede de proteção. `ddl-auto=update` em prod é arriscado. Ver [[testing]] e [[security]].

## Padrões aplicáveis

Stack Java/Spring → seguir [[java-spring]].
Universais (sempre): [[_principles]] · [[code-style]] · [[naming]] · [[error-handling]] · [[testing]] · [[security]] · [[git-commits]].

Pontos de atenção mapeados no recon:
- Pacotes sem namespace de domínio → [[naming]].
- Credenciais H2 default e console exposto → [[security]].
- Sem testes + `skipTests` no build → [[testing]].

## Roteamento

Projeto **independente** — consultar **somente** o dev-Brain. Não citar apps, fluxos ou regras do MailerWeb (anti-alucinação). Detalhe da árvore de decisão em [[routing]].

---
Voltar a [[00-index]].
