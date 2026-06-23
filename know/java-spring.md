---
type: note
scope: global
brain_policy: dev-brain
write_policy: dev-brain-only
audience: both
source: human
status: stable
confidence: high
last_verified: 2026-06-19
token_policy: full
tags: [know, stack, java, spring]
---

# java-spring — padrão por stack: Java / Spring Boot

> Padrão **específico** de Java/Spring Boot. Os universais valem antes e vencem em conflito: [[_principles]] · [[code-style]] · [[naming]] · [[docstrings]] · [[testing]] · [[error-handling]] · [[security]] · [[performance]]. Aplica a projetos como [[prontuario]] (Boot 3.3.2) e [[faculdade-alessandro]] (Boot 3.3.5).

## Arquitetura em camadas

Fluxo único de dependência: `Controller → Service → Repository → Entity`. DTO atravessa a borda HTTP; nunca o contrário.

| Camada | Responsabilidade | Não pode |
|--------|------------------|----------|
| **Controller** (`@RestController`) | HTTP, validação de entrada, mapear DTO↔domínio, delegar | conter regra de negócio, tocar `Repository` direto |
| **Service** (`@Service`) | regra de negócio, transação (`@Transactional`) | conhecer `HttpServletRequest` / detalhes web |
| **Repository** (`extends JpaRepository`) | acesso a dados | conter regra de negócio |
| **Entity** (`@Entity`) | mapeamento JPA | sair na resposta HTTP (vira DTO) |
| **DTO** (`record`) | contrato de entrada/saída | ter anotação JPA |

```java
// BOM — controller fino, delega
@RestController
@RequestMapping("/tipo-exame")
class CtrlManterTiposExame {
    private final ServiceManterTiposExame service;
    CtrlManterTiposExame(ServiceManterTiposExame service) { this.service = service; }

    @PostMapping
    TipoExameResponse incluir(@Valid @RequestBody TipoExameRequest req) {
        return service.incluir(req);
    }
}
```

```java
// RUIM — controller com regra + acesso direto a dados
@PostMapping
TipoExame incluir(@RequestBody TipoExame e) {
    if (e.getNome() == null) e.setNome("?");   // regra no controller
    return repository.save(e);                  // pula a service, vaza Entity
}
```

## Pacotes: por feature, com namespace de domínio

Prefira **pacote por feature** (`br.unilasalle.prontuario.exame.{Controller,Service,Repository,Entity}`) a pacote por camada (`controller/`, `service/`, `model/`) — coesão alta, baixo acoplamento entre features.

```
BOM                                    RUIM
br.edu.faculdade.exame/                controller/   (sem namespace de domínio)
  ExameController.java                 service/
  ExameService.java                    model/
  ExameRepository.java                 model/repository/
  Exame.java                           Models/        ← fora do src!
```

- [[prontuario]] e [[faculdade-alessandro]] usam pacotes raiz sem prefixo (`controller`, `service`, `model`). **Corrigir** para `br.<dominio>.*` — ver [[naming]].
- [[faculdade-alessandro]] tem **`Models/` na raiz**, duplicata fora de `src/main/java/` e fora do classpath de build. **Anti-padrão grave**: cópia morta editável por engano. Remover; fonte de verdade é `src/main/java/model/`.

## Injeção por construtor — nunca `@Autowired` em field

```java
// BOM — final + construtor: imutável, testável sem container, dependências explícitas
@Service
class ServiceManterConsultas {
    private final ConsultaRepository repo;
    private final NotificadorService notificador;
    ServiceManterConsultas(ConsultaRepository repo, NotificadorService notificador) {
        this.repo = repo; this.notificador = notificador;
    }
}
```

```java
// RUIM — field injection: campo não-final, dependência oculta, exige Spring p/ testar
@Service
class ServiceManterConsultas {
    @Autowired private ConsultaRepository repo;
}
```

Com um único construtor o Spring injeta sem anotação. Construtor força a dependência a aparecer — se a lista cresce demais, é sinal de classe fazendo coisa demais ([[_principles]]).

## DTO ≠ Entity

Nunca exponha `@Entity` na API. Entity é modelo de persistência (lazy proxies, ciclos, campos internos); DTO é contrato.

```java
// BOM — record imutável como contrato; entity fica interna
record TipoExameRequest(@NotBlank String nome, @NotNull Classificacao classificacao) {}
record TipoExameResponse(Long id, String nome, String classificacao) {}

// RUIM — devolver entity: vaza esquema interno, dispara lazy-loading na serialização,
// e amarra o JSON ao banco
@GetMapping("/{id}") TipoExame buscar(@PathVariable Long id) { return repo.findById(id).orElseThrow(); }
```

## JPA sem N+1

`FetchType.LAZY` + acesso a coleção em loop = uma query por item. Resolva no carregamento, não no loop. Detalhe e métricas em [[performance]].

```java
// RUIM — N+1: 1 query p/ consultas + N p/ resultados
List<Consulta> cs = repo.findAll();
cs.forEach(c -> c.getResultados().size());   // dispara query por consulta

// BOM — JOIN FETCH
@Query("select c from Consulta c join fetch c.resultados")
List<Consulta> findAllComResultados();

// BOM — @EntityGraph (declarativo)
@EntityGraph(attributePaths = "resultados")
List<Consulta> findAll();
```

- Default das relações `@OneToMany`/`@ManyToMany` já é LAZY — mantenha. Evite `EAGER`.
- Paginação: `Pageable`, nunca `findAll()` cru numa tabela que cresce.

## Tratamento de erro: `@ControllerAdvice` global

Único ponto com captura ampla; traduz exceção de domínio → resposta HTTP. Regras universais em [[error-handling]].

```java
@RestControllerAdvice
class CtrlTratadorErros {
    @ExceptionHandler(RecursoNaoEncontradoException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    ProblemDetail naoEncontrado(RecursoNaoEncontradoException e) {
        return ProblemDetail.forStatusAndDetail(HttpStatus.NOT_FOUND, e.getMessage());
    }
}
```

- Lance unchecked específica (`RecursoNaoEncontradoException`), não `throws Exception`.
- Nunca `try/catch` vazio na service; deixe subir ao advice.
- Log com SLF4J parametrizado + MDC: `log.error("falha incluir tipo={}", req.nome(), e);` — sem PII ([[security]]).

## Validação com Bean Validation

Valide na borda do controller com `@Valid`; o núcleo confia nos dados.

```java
record ConsultaRequest(
    @NotNull Long pacienteId,
    @NotBlank @Size(max = 200) String motivo,
    @FutureOrPresent LocalDate data
) {}

@PostMapping
ConsultaResponse incluir(@Valid @RequestBody ConsultaRequest req) { ... }  // 400 automático se inválido
```

`@RestControllerAdvice` captura `MethodArgumentNotValidException` para formatar o 400.

## Javadoc

Documente o **porquê** e o contrato (exceções, nulabilidade), não o óbvio. Regras em [[docstrings]].

```java
/**
 * Inclui um tipo de exame.
 * @throws TipoExameDuplicadoException se já existir tipo com o mesmo nome (case-insensitive).
 */
TipoExameResponse incluir(TipoExameRequest req);
```

## Testes: JUnit 5 + Mockito

Disciplina geral em [[testing]]. `mvn -DskipTests` no build (caso de [[prontuario]]) = zero rede de proteção — corrigir.

```java
@ExtendWith(MockitoExtension.class)
class ServiceManterTiposExameTest {
    @Mock TipoExameRepository repo;
    @InjectMocks ServiceManterTiposExame service;

    @Test void incluir_quando_nome_duplicado_entao_lanca() {
        when(repo.existsByNomeIgnoreCase("Sangue")).thenReturn(true);
        assertThrows(TipoExameDuplicadoException.class,
            () -> service.incluir(new TipoExameRequest("Sangue", Classificacao.LAB)));
    }
}
```

- Service: teste unitário com Mockito (sem container).
- Controller: `@WebMvcTest` + `MockMvc`. Repository/integração: `@DataJpaTest` ou `@SpringBootTest` com Testcontainers (não H2 fingindo ser prod).

## Segredos fora do repo

Nada de credencial em `application.properties` versionado. Use env vars / `application-{profile}.properties` ignorado. Regras em [[security]].

```properties
# BOM — placeholder resolvido por env
spring.datasource.url=${SPRING_DATASOURCE_URL}
spring.datasource.password=${DB_PASSWORD}
```

```properties
# RUIM — segredo no commit
spring.datasource.password=postgres123
```

- `ddl-auto=update` + H2 em arquivo (estado de [[prontuario]] e [[faculdade-alessandro]]): ok p/ acadêmico, **proibido** em prod (use Flyway/Liquibase + `validate`).
- Não exponha `/h2-console` nem console com user `sa`/senha vazia fora de dev.

## Formatação: google-java-format

Formatação não se discute em PR — ferramenta resolve. Adote **google-java-format** (plugin Maven `fmt-maven-plugin` ou Spotless) e rode no CI. Ver [[code-style]].

```xml
<plugin>
  <groupId>com.spotify.fmt</groupId>
  <artifactId>fmt-maven-plugin</artifactId>
</plugin>
```

## Checklist de PR (Spring)

- [ ] Controller fino: sem regra de negócio nem acesso direto a `Repository`.
- [ ] Pacote por feature com namespace de domínio (`br.<dominio>.*`); sem código fora de `src/`.
- [ ] Injeção por construtor (`final`), zero `@Autowired` em field.
- [ ] API só com DTO (`record`); nenhuma `@Entity` na resposta.
- [ ] Sem N+1: `JOIN FETCH`/`@EntityGraph`; paginação onde a tabela cresce ([[performance]]).
- [ ] Erros via `@ControllerAdvice`; exceção específica; sem `catch` vazio ([[error-handling]]).
- [ ] `@Valid` + Bean Validation na borda.
- [ ] Testes JUnit 5 + Mockito; build **sem** `-DskipTests` ([[testing]]).
- [ ] Zero segredo versionado; `ddl-auto` não-`update` em prod ([[security]]).
- [ ] `google-java-format` aplicado ([[code-style]]).

Relacionadas: [[_principles]] · [[naming]] · [[docstrings]] · [[error-handling]] · [[testing]] · [[security]] · [[performance]] · [[routing]] · maps [[prontuario]] · [[faculdade-alessandro]] · voltar ao [[00-index]].
