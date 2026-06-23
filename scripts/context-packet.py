#!/usr/bin/env python3
"""
context-packet.py — monta o PACOTE DE CONTEXTO mínimo p/ uma tarefa, a partir do
card do projeto + digest + lessons/decisions relevantes. NÃO despeja o vault.

Esse pacote é a ENTRADA da IA (Claude/Codex). Camadas (ver [[flow]]):
  0 regra fixa · 1 skill · 2 ESTE pacote · 3 digest do grafo · 4 arquivo real só se preciso.

Uso: python3 scripts/context-packet.py <slug> "<descrição da tarefa>"
     (slug = nome do card sem -proj, ex: meudinheiro-v2, mailerweb-panel-v2)
Saída: markdown no stdout (redirecione p/ um arquivo se quiser).
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
if len(sys.argv) < 2:
    print("uso: context-packet.py <slug> \"<tarefa>\""); sys.exit(2)
slug = sys.argv[1].replace("-proj", "")
task = sys.argv[2] if len(sys.argv) > 2 else "(descreva a tarefa)"

def fm(text):
    m = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    d = {}
    if m:
        for ln in m.group(1).splitlines():
            mm = re.match(r"([a-z_]+):\s*(.*)", ln)
            if mm: d[mm.group(1)] = mm.group(2).strip()
    return d

card_p = ROOT / "projects" / f"{slug}-proj.md"
if not card_p.exists():
    print(f"# Context Packet\n\n⚠️ Sem card projects/{slug}-proj.md. Crie via templates/project-card.md."); sys.exit(1)
card = fm(card_p.read_text(encoding="utf-8"))

stack = card.get("stack", "").strip("[]")
weight = card.get("token_weight", "?")
domain = card.get("domain_brain", "(nenhum)")
is_mw = "mailerweb" in (card.get("scope", "") + domain)

# regras de stack
stack_note = {"django": "python-django", "python": "python-django", "spring": "java-spring",
              "java": "java-spring", "next": "typescript-next", "typescript": "typescript-next",
              "react": "typescript-next", "vite": "typescript-next"}
rules = set()
for k, v in stack_note.items():
    if k in stack.lower(): rules.add(v)

# lessons relevantes (scope = mailerweb se projeto MW, senão cross-repo + scope==slug)
lessons = []
for p in (ROOT / "know" / "lessons").glob("*.md"):
    if p.name == "README.md": continue
    d = fm(p.read_text(encoding="utf-8"))
    sc = d.get("scope", "")
    if (is_mw and sc == "mailerweb") or sc == "cross-repo" or sc == slug:
        lessons.append(p.stem)

decisions = [p.stem for p in sorted((ROOT / "decisions").glob("[0-9]*.md"))]

print(f"""# Context Packet — {slug}

## Tarefa
{task}

## Projeto / domínio
- Projeto: [[{slug}-proj|{slug}]] · stack: {stack} · token_weight: **{weight}**
- Domínio: {"mailerweb-brain via [[mailerweb-bridge]] (READ-ONLY)" if is_mw else "independente — só dev-Brain, NÃO citar MailerWeb"}
- Mapa/estrutura: [[{slug}]] · grafo: [[{slug}-grafo]] · digest: graph/{slug}.digest.json

## Regras aplicáveis (know/)
{chr(10).join(f"- [[{r}]]" for r in sorted(rules)) or "- (genéricas)"}
- universais: [[_principles]] [[code-style]] [[naming]] [[testing]] [[error-handling]] [[security]]

## Arquivos prováveis
- (preencher após digest/graphify query — NÃO abrir repo inteiro)

## Lições relacionadas
{chr(10).join(f"- [[{l}]]" for l in lessons) or "- (nenhuma)"}

## Decisões relacionadas
{chr(10).join(f"- [[{d}]]" for d in decisions) or "- (nenhuma)"}

## Não fazer
- NÃO abrir repo inteiro nem graph.json cru (use digest + graphify query).
{"- NÃO escrever no mailerweb-brain (read-only). NÃO duplicar domínio aqui." if is_mw else "- NÃO citar apps/fluxos/regras MailerWeb (anti-alucinação)."}

## Orçamento de contexto
**{weight}** — {"crítico: exigir plano antes de ler mais; bridge+digest+query, nunca repo inteiro" if weight in ("crítico","critico") else "alto: delegar/digest" if weight=="alto" else "médio: digest + graphify query dirigida" if weight in ("médio","medio") else "baixo: resumo + ~2 notas"}
""")
