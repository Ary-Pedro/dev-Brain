---
type: project
project: faculdade-alessandro
scope: faculdade-alessandro
repo_path: ~/devSpace/projeto/faculdade_alessandro
stack: [java, spring-boot, docker]
brain_policy: dev-brain
write_policy: dev-brain-only
domain_brain: (nenhum)
status: active
token_weight: baixo
token_policy: summary-first
graph_nodes: 379
graph_edges: 793
source: human+graphify
audience: ai
tags: [project]
---

# faculdade-alessandro — CARD

<!-- @generated:start -->
## Objetivo

API REST acadêmica de **controle de exames**: CRUD de tipos de exame, consultas e resultados de exame. Projeto **independente** (`groupId=br.edu.faculdade`, `artifactId=controle-exames`). Java 17 + Spring Boot 3.3.5, H2 em arquivo, front estático servido pelo Boot, empacotado via Docker (porta 8081). Camadas controller→service→repository com DTOs `*Request`/`*Response` e `@ControllerAdvice` (`CtrlTratadorErros`). Entrypoint: `controller.CtrlPrograma`.

## Como consultar

1. **Domínio** (regra de negócio, fluxo, entidade) → consultar **só o dev-Brain** (`brain_policy: dev-brain-only`). NÃO citar apps/fluxos/regras de outros domínios.
2. **Padrão** (estilo, naming, error-handling, testes, segurança) → `know/` via [[java-spring]] + bases ([[_principles]], [[code-style]], [[naming]], [[error-handling]], [[security]], [[testing]]).
3. **Estrutura** (onde fica X, papel de dir/arquivo) → [[faculdade-alessandro-grafo]] e o mapa [[faculdade-alessandro]].
4. **Relação** (quem chama quem, dependências, caminho entre nós) → `graphify query` sobre o slug `faculdade-alessandro`.

## Peso p/ IA

`token_weight=baixo` → projeto pequeno e independente. Pode abrir **resumo (mapa) + 2 notas** sem custo relevante. Sequência barata: ler [[faculdade-alessandro]] (mapa) → se precisar de estrutura, abrir [[faculdade-alessandro-grafo]]. Não precisa carregar o grafo inteiro para perguntas de domínio.

## Próxima ação

- Remover a duplicata `Models/` na raiz (cópia morta fora do classpath; fonte de verdade é `src/main/java/model/`). Risco de editar a cópia errada — ver [[code-style]].
- Renomear pacotes raiz (`controller`, `service`, `model`) para `br.edu.faculdade.*`, alinhando ao `groupId` — ver [[naming]].
- `ddl-auto=update` + H2 em arquivo: aceitável para acadêmico, revisar antes de qualquer uso sério — ver [[security]], [[performance]].
<!-- @generated:end -->

<!-- @user:start -->
(observações manuais do Pedro)
<!-- @user:end -->

---

Relacionado: [[faculdade-alessandro]] (mapa) · [[faculdade-alessandro-grafo]] · [[routing]]
