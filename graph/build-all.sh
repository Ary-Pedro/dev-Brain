#!/usr/bin/env bash
# build-all.sh — constrói grafo graphify (AST-only, determinístico, sem LLM) por repo
# e mescla tudo num grafo global do devSpace. Reexecutável (idempotente).
#
# Uso:  bash ~/devSpace/dev-Brain/graph/build-all.sh
# Pré:  graphify instalado em venv (~/.local/share/graphify-venv)
#
# AST-only = só estrutura de código (tree-sitter, 36 langs). Docs/PDF (semântico)
# precisam de LLM via `/graphify <path>` — fora deste script de propósito.

set -uo pipefail
PY="$HOME/.local/share/graphify-venv/bin/python"
GRAPHIFY="$HOME/.local/share/graphify-venv/bin/graphify"
OUT="$HOME/devSpace/dev-Brain/graph"

# repo<TAB>slug  — só repos com código real (wiks=docs, atvdd=vazio, theds=nested → fora)
REPOS=(
  "$HOME/devSpace/projeto/prontuario|prontuario"
  "$HOME/devSpace/projeto/faculdade_alessandro|faculdade-alessandro"
  "$HOME/devSpace/projeto/meuDinheiroNaMaoV2|meudinheiro-v2"
  "$HOME/devSpace/mailerWeb/mailerweb-portal|mailerweb-portal"
  "$HOME/devSpace/mailerWeb/mailerweb.panel.v2|mailerweb-panel-v2"
)

build_one() {
  local repo="$1" slug="$2"
  [ -d "$repo" ] || { echo "SKIP $slug — dir ausente"; return 1; }
  echo "=== build $slug ($repo) ==="
  ( cd "$repo" || return 1
    mkdir -p graphify-out
    echo "$PY" > graphify-out/.graphify_python
    "$PY" -c "import sys; open('graphify-out/.graphify_python','w').write(sys.executable)"
    echo "$(pwd)" > graphify-out/.graphify_root

    # 1. detect
    "$PY" -c "
import json; from graphify.detect import detect; from pathlib import Path
r=detect(Path('.')); Path('graphify-out/.graphify_detect.json').write_text(json.dumps(r,ensure_ascii=False))
print('  detect:', r.get('total_files'),'files')" || return 1

    # 2. AST extract (código — determinístico)
    "$PY" -c "
import json; from pathlib import Path
from graphify.extract import collect_files, extract
d=json.loads(Path('graphify-out/.graphify_detect.json').read_text())
cf=[]
for f in d.get('files',{}).get('code',[]):
    p=Path(f); cf += (collect_files(p) if p.is_dir() else [p])
if cf:
    r=extract(cf, cache_root=Path('.'))
    print('  AST:', len(r['nodes']),'nodes', len(r['edges']),'edges')
else:
    r={'nodes':[],'edges':[],'input_tokens':0,'output_tokens':0}; print('  AST: sem código')
Path('graphify-out/.graphify_ast.json').write_text(json.dumps(r,ensure_ascii=False))" || return 1

    # 3. semântico vazio (sem LLM) + merge AST→extract
    "$PY" -c "
import json; from pathlib import Path
ast=json.loads(Path('graphify-out/.graphify_ast.json').read_text())
merged={'nodes':ast['nodes'],'edges':ast['edges'],'hyperedges':[],'input_tokens':0,'output_tokens':0}
Path('graphify-out/.graphify_extract.json').write_text(json.dumps(merged,ensure_ascii=False))" || return 1

    # 4. build + cluster + report + graph.json
    "$PY" -c "
import json; from pathlib import Path
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json
ex=json.loads(Path('graphify-out/.graphify_extract.json').read_text())
dt=json.loads(Path('graphify-out/.graphify_detect.json').read_text())
G=build_from_json(ex)
if G.number_of_nodes()==0:
    print('  GRAFO VAZIO — pulando'); raise SystemExit(2)
com=cluster(G); coh=score_all(G,com)
labels={cid:'Community '+str(cid) for cid in com}
q=suggest_questions(G,com,labels)
rep=generate(G,com,coh,labels,god_nodes(G),surprising_connections(G,com),dt,{'input':0,'output':0},'.',suggested_questions=q)
Path('graphify-out/GRAPH_REPORT.md').write_text(rep)
to_json(G,com,'graphify-out/graph.json')
print('  grafo:',G.number_of_nodes(),'nós',G.number_of_edges(),'arestas',len(com),'comunidades')"
    local rc=$?
    [ $rc -ne 0 ] && { echo "  FALHOU rc=$rc"; return $rc; }

    # 5. copia artefatos pro vault
    mkdir -p "$OUT/$slug"
    cp -f graphify-out/graph.json "$OUT/$slug/graph.json" 2>/dev/null
    cp -f graphify-out/GRAPH_REPORT.md "$OUT/$slug/GRAPH_REPORT.md" 2>/dev/null
    echo "  -> $OUT/$slug/"
  )
}

declare -a GRAPHS
for entry in "${REPOS[@]}"; do
  repo="${entry%|*}"; slug="${entry#*|}"
  if build_one "$repo" "$slug"; then
    [ -f "$OUT/$slug/graph.json" ] && GRAPHS+=("$OUT/$slug/graph.json")
  fi
done

# merge cross-repo → grafo global do devSpace
if [ "${#GRAPHS[@]}" -ge 2 ]; then
  echo "=== merge ${#GRAPHS[@]} grafos -> grafo global ==="
  "$GRAPHIFY" merge-graphs "${GRAPHS[@]}" --out "$OUT/devspace-merged.json" 2>&1 | tail -5
fi

# diagramas HTML interativos (tree viewer) por repo + global
echo "=== tree.html (diagrama interativo) ==="
"$PY" - <<PYEOF
from pathlib import Path
from graphify.tree_html import write_tree_html
OUT=Path("$OUT")
for s in ["prontuario","faculdade-alessandro","meudinheiro-v2","mailerweb-portal","mailerweb-panel-v2"]:
    gp=OUT/s/"graph.json"
    if gp.exists():
        try: write_tree_html(gp, OUT/s/f"{s}_tree.html", project_label=s); print("  tree:",s)
        except Exception as e: print("  FALHA",s,repr(e)[:80])
if (OUT/"devspace-merged.json").exists():
    try: write_tree_html(OUT/"devspace-merged.json", OUT/"devspace_tree.html", project_label="devSpace"); print("  tree: devspace (global)")
    except Exception as e: print("  FALHA global",repr(e)[:80])
PYEOF
echo "=== done ==="
