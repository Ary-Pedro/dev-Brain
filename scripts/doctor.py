#!/usr/bin/env python3
"""
doctor.py — validador de saúde do dev-Brain (sem LLM, determinístico, reexecutável).

Checa: frontmatter obrigatório, enums (type/audience/write_policy/brain_policy),
token_policy em notas ai/both, links quebrados reais, project cards (repo_path + digest),
e DECLARA exceções (artefatos gerados, runtime) em vez de fingir vault limpo.

Uso: python3 ~/devSpace/dev-Brain/scripts/doctor.py [--strict]
Sai 1 se houver erro (não warning). --strict trata warning como erro.
"""
import re, sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
STRICT = "--strict" in sys.argv

REQUIRED = ["type", "scope", "brain_policy", "write_policy", "audience", "source", "status"]
TYPES = {"project", "lesson", "correction", "decision", "note", "session", "agent", "moc", "meta"}
AUDIENCE = {"ai", "human", "both"}
WRITE_POLICY = {"dev-brain-only", "read-only"}
BRAIN_POLICY = {"dev-brain", "mailerweb-brain-ref", "read-domain-from-mailerweb-brain"}
STATUS = {"draft", "active", "stable", "deprecated"}

# EXCEÇÕES DECLARADAS (não são notas curadas — artefatos brutos / runtime / modelos)
def is_exception(rel):
    parts = rel.split("/")
    name = parts[-1]
    if parts[0] in (".obsidian", ".sync", "templates"):
        return "runtime/modelo"
    if name == "GRAPH_REPORT.md":
        return "artefato bruto graphify"
    return None

def parse_fm(text):
    m = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"([a-z_]+):\s*(.*)", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm

def strip_code(t):
    return re.sub(r"```.*?```", " ", t, flags=re.DOTALL)

def main():
    mds = [p for p in ROOT.rglob("*.md")]
    errors, warns, exceptions = [], [], []

    # 1. resolvable set p/ links (stems + aliases de TODAS as notas)
    stems, aliases = set(), set()
    fm_cache = {}
    for p in mds:
        rel = str(p.relative_to(ROOT))
        if any(s in p.parts for s in (".obsidian", ".sync")):
            continue
        stems.add(p.stem.lower())
        t = p.read_text(encoding="utf-8", errors="ignore")
        fm = parse_fm(t)
        fm_cache[p] = (rel, t, fm)
        if fm and fm.get("aliases"):
            for a in re.findall(r"[\w\-./]+", fm["aliases"]):
                aliases.add(a.lower())
    resolvable = stems | aliases

    # placeholders de exemplo em prosa (não são links de navegação)
    PLACEHOLDER = {"b", "nome", "adr-xxxx", "wikilinks", "a", "nota", "x", "y"}

    for p in mds:
        if any(s in p.parts for s in (".obsidian", ".sync")):
            continue
        rel, t, fm = fm_cache[p]
        exc = is_exception(rel)
        if exc:
            exceptions.append(f"{rel}  ({exc})")
            continue

        # 2. frontmatter
        if fm is None:
            errors.append(f"{rel}: SEM frontmatter")
            continue
        for f in REQUIRED:
            if f not in fm:
                errors.append(f"{rel}: falta campo obrigatório '{f}'")
        if fm.get("type") and fm["type"] not in TYPES:
            errors.append(f"{rel}: type inválido '{fm['type']}' (∉ {sorted(TYPES)})")
        if fm.get("audience") and fm["audience"] not in AUDIENCE:
            errors.append(f"{rel}: audience inválido '{fm['audience']}'")
        if fm.get("write_policy") and fm["write_policy"] not in WRITE_POLICY:
            errors.append(f"{rel}: write_policy inválido '{fm['write_policy']}'")
        if fm.get("brain_policy") and fm["brain_policy"] not in BRAIN_POLICY:
            errors.append(f"{rel}: brain_policy inválido '{fm['brain_policy']}'")
        if fm.get("status") and fm["status"] not in STATUS:
            warns.append(f"{rel}: status fora do padrão '{fm['status']}'")
        if fm.get("audience") in ("ai", "both") and "token_policy" not in fm:
            warns.append(f"{rel}: audience={fm.get('audience')} sem token_policy (recomendado)")

        # 3. links quebrados reais (fora de code-fence)
        for m in re.findall(r"\[\[([^\]]+)\]\]", strip_code(t)):
            tgt = m.split("|")[0].split("\\")[0].split("#")[0].split("^")[0].strip()
            if not tgt or "<%" in tgt or "<" in tgt:
                continue
            base = tgt.split("/")[-1].lower()
            if base in PLACEHOLDER or base in resolvable:
                continue
            warns.append(f"{rel}: wikilink possivelmente quebrado [[{tgt}]]")

    # 4. project cards: repo_path existe + digest presente
    for p in (ROOT / "projects").glob("*.md"):
        rel, t, fm = fm_cache.get(p, (str(p), "", None))
        if not fm or fm.get("type") != "project":
            continue
        slug = p.stem.replace("-proj", "")
        rp = (fm.get("repo_path") or "").replace("~", str(pathlib.Path.home()))
        if rp and not pathlib.Path(rp).exists():
            warns.append(f"projects/{p.name}: repo_path não existe no disco ({fm.get('repo_path')})")
        dig = ROOT / "graph" / f"{slug}.digest.json"
        if not dig.exists():
            warns.append(f"projects/{p.name}: sem digest em graph/{slug}.digest.json")

    # 5. mailerweb-brain read-only (informativo)
    mb = pathlib.Path.home() / "devSpace/mailerWeb/mailerweb-brain"
    ro = "OK (não tocado por dev-Brain)" if mb.exists() else "ausente"

    print(f"=== dev-brain doctor ===  notas={len(mds)}  erros={len(errors)}  warnings={len(warns)}  exceções={len(exceptions)}")
    print(f"mailerweb-brain read-only: {ro}")
    if errors:
        print("\n## ERROS")
        for e in errors: print("  ✗", e)
    if warns:
        print("\n## WARNINGS")
        for w in warns: print("  ⚠", w)
    print(f"\n## EXCEÇÕES DECLARADAS ({len(exceptions)}) — artefatos brutos/runtime, não validados de propósito")
    for x in exceptions[:30]: print("  ·", x)

    rc = 1 if errors or (STRICT and warns) else 0
    print(f"\nexit {rc}")
    sys.exit(rc)

if __name__ == "__main__":
    main()
