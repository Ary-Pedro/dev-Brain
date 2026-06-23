#!/usr/bin/env bash
# install-plugins.sh — restaura os binários dos plugins Obsidian após clone.
# Os main.js/styles.css são gitignored (3º-party, pesados); este script os baixa
# da release oficial p/ cada id ATIVO em .obsidian/community-plugins.json.
#
# Uso: bash scripts/install-plugins.sh
# Depois: reabra o vault no Obsidian.

set -uo pipefail
OBS="$(cd "$(dirname "$0")/.." && pwd)/.obsidian"
PLUGINS="$OBS/plugins"

# id  ->  owner/repo (release com main.js/manifest.json/styles.css)
declare -A REPO=(
  [dataview]=blacksmithgu/obsidian-dataview
  [obsidian-linter]=platers/obsidian-linter
  [obsidian-icon-folder]=FlorianWoelki/obsidian-iconize
  [obsidian-kanban]=mgmeyers/obsidian-kanban
  [obsidian-tasks-plugin]=obsidian-tasks-group/obsidian-tasks
  [templater-obsidian]=SilentVoid13/Templater
  [recent-files-obsidian]=tgrosinger/recent-files-obsidian
  [obsidian-day-planner]=ivan-lednev/obsidian-day-planner
  # recomendados (ADR-0003) — descomente ao adotar:
  # [metadata-menu]=mdelobelle/metadatamenu
  # [obsidian-advanced-uri]=Vinzent03/obsidian-advanced-uri
  # [excalibrain]=zsviczian/excalibrain
)

# lê ids ativos do community-plugins.json (fallback: todos do REPO)
mapfile -t ACTIVE < <(grep -oE '"[a-z0-9-]+"' "$OBS/community-plugins.json" 2>/dev/null | tr -d '"')
[ "${#ACTIVE[@]}" -eq 0 ] && ACTIVE=("${!REPO[@]}")

for id in "${ACTIVE[@]}"; do
  repo="${REPO[$id]:-}"
  [ -z "$repo" ] && { echo "SKIP $id (sem repo mapeado)"; continue; }
  dest="$PLUGINS/$id"; mkdir -p "$dest"
  echo "-- $id ($repo) --"
  for f in manifest.json main.js styles.css; do
    if curl -fsSL "https://github.com/$repo/releases/latest/download/$f" -o "$dest/$f"; then
      echo "   ok $f"
    else
      [ "$f" = "styles.css" ] || echo "   FALHA $f"
      rm -f "$dest/$f" 2>/dev/null
    fi
  done
done
echo "Pronto. Reabra o vault no Obsidian (pode pedir 'trust author')."
