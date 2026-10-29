#!/usr/bin/env bash
# Meteoric Council installer. Built for Moksh Vasant by Fulcrum Labs on FulcrumOS.
#
# Usage: bash install.sh "<workspace>" [--force]
#
# Copies the council's agents, skills and council/ folder into the workspace.
# Safe to re-run: module files are updated in place, Moksh's own data
# (config, memory, games, finance, sessions, reports, his added advisors,
# his roster edits) is never overwritten. A skill or agent with the same
# name that this module didn't install is skipped unless --force, which
# moves it to vault/pre-council-<date>/ first.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WS="${1:-}"
FORCE="${2:-}"
MARK=".meteoric-council"
STAMP="$(date +%Y-%m-%d)"

if [[ -z "$WS" || ! -d "$WS" ]]; then
  echo "Usage: bash install.sh \"<workspace>\" [--force]" >&2
  exit 1
fi
WS="$(cd "$WS" && pwd)"
if [[ "$WS" == "$REPO" ]]; then
  echo "Run this against the OS folder, not the module folder." >&2
  exit 1
fi

installed=() updated=() skipped=() backed_up=() created=() kept=()

backup() {  # move a clashing path into the vault
  local src="$1" dest="$WS/vault/pre-council-$STAMP/${1#$WS/}"
  mkdir -p "$(dirname "$dest")"
  mv "$src" "$dest"
  backed_up+=("${1#$WS/} -> ${dest#$WS/}")
}

# 1. Skills
mkdir -p "$WS/.claude/skills"
for dir in "$REPO"/.claude/skills/*/; do
  name="$(basename "$dir")"
  dest="$WS/.claude/skills/$name"
  if [[ -d "$dest" && ! -f "$dest/$MARK" ]]; then
    if [[ "$FORCE" == "--force" ]]; then backup "$dest"; else skipped+=("skill: $name"); continue; fi
  fi
  [[ -d "$dest" ]] && updated+=("skill: $name") || installed+=("skill: $name")
  rm -rf "$dest"
  cp -R "$dir" "$dest"
  touch "$dest/$MARK"
done

# 2. Agents (marked by the "Meteoric Council" line in their body)
mkdir -p "$WS/.claude/agents"
for f in "$REPO"/.claude/agents/council-*.md; do
  name="$(basename "$f")"
  dest="$WS/.claude/agents/$name"
  if [[ -f "$dest" ]] && ! grep -q "Meteoric Council" "$dest"; then
    if [[ "$FORCE" == "--force" ]]; then backup "$dest"; else skipped+=("agent: $name"); continue; fi
  fi
  [[ -f "$dest" ]] && updated+=("agent: $name") || installed+=("agent: $name")
  cp "$f" "$dest"
done

# 3. council/ — module-owned files are refreshed
C="$WS/council"
mkdir -p "$C"
for item in COUNCIL.md docs scripts examples templates; do
  rm -rf "$C/$item"
  cp -R "$REPO/council/$item" "$C/$item"
done
mkdir -p "$C/advisors"
for brain in alex-hormozi jeremy-haynes nik-setting; do
  if [[ -d "$REPO/council/advisors/$brain" ]]; then
    [[ -d "$C/advisors/$brain" ]] && updated+=("brain: $brain") || installed+=("brain: $brain")
    rm -rf "$C/advisors/$brain"
    cp -R "$REPO/council/advisors/$brain" "$C/advisors/$brain"
  fi
done

# 4. council/ — Moksh's data: create if missing, never overwrite
seed() {  # seed <repo-relative path>
  local rel="$1"
  if [[ -e "$C/$rel" ]]; then kept+=("council/$rel"); return; fi
  mkdir -p "$(dirname "$C/$rel")"
  cp -R "$REPO/council/$rel" "$C/$rel"
  created+=("council/$rel")
}
seed ROSTER.md
seed config.md
seed advisors/mindset-coach
for m in cfo cmo sales fulfilment; do seed "memory/$m.md"; done
for d in sessions reports games/eod games/money finance; do mkdir -p "$C/$d"; done

# 5. Report
section() { local title="$1"; shift; [[ $# -gt 0 ]] && { echo "$title"; printf '  - %s\n' "$@"; }; return 0; }
echo "Meteoric Council → $WS"
section "Installed:" "${installed[@]+"${installed[@]}"}"
section "Updated:" "${updated[@]+"${updated[@]}"}"
section "Created (your data, first install):" "${created[@]+"${created[@]}"}"
section "Kept as-is (your data):" "${kept[@]+"${kept[@]}"}"
section "Backed up before replacing (--force):" "${backed_up[@]+"${backed_up[@]}"}"
section "SKIPPED (name clash, not installed by this module):" "${skipped[@]+"${skipped[@]}"}"
if [[ ${#skipped[@]} -gt 0 ]]; then
  echo "Re-run with --force to back these up to vault/ and install the council's versions."
fi
