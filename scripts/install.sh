#!/usr/bin/env bash
# install.sh — Enterprise Multi-Agent Protocol v4 bootstrap
# Idempotent (RULE-011) · dry-run supported (RULE-012) · full backups (RULE-010 rollback)
#
# Usage:
#   bash scripts/install.sh [--dry-run] [--target <path>] [--force]
#
# --dry-run  : preview all actions, change nothing
# --target   : override HOME (useful for testing / non-standard layouts)
# --force    : skip confirmation for interactive install

set -euo pipefail

# --- CLI parsing ---------------------------------------------------
DRY_RUN=0
FORCE=0
TARGET="${HOME}"

while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ; shift ;;
    --force)   FORCE=1   ; shift ;;
    --target)  TARGET="$2"; shift 2 ;;
    -h|--help)
      grep '^#' "$0" | head -12
      exit 0 ;;
    *) echo "unknown arg: $1" >&2 ; exit 1 ;;
  esac
done

# --- Structured logging (RULE-004) ---------------------------------
ts()    { date -u +%Y-%m-%dT%H:%M:%SZ; }
log()   { printf '[%s] [%s] %s\n' "$(ts)" "$1" "$2"; }
info()  { log INFO "$1"; }
warn()  { log WARN "$1"; }
error() { log ERROR "$1" >&2; }

do_or_dry() {
  if [ "$DRY_RUN" -eq 1 ]; then
    printf '[DRY-RUN] would run: %s\n' "$*"
  else
    "$@"
  fi
}

# --- Paths ---------------------------------------------------------
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLAUDE_HOME="${TARGET}/.claude"
HOOKS_DIR="${CLAUDE_HOME}/hooks"
TELEMETRY_DIR="${CLAUDE_HOME}/telemetry"
BACKUP_DIR="${CLAUDE_HOME}/backups/install-$(date -u +%Y%m%d-%H%M%SZ)"
CLINERULES="${TARGET}/.clinerules"
SETTINGS="${CLAUDE_HOME}/settings.json"

info "Repo root: ${REPO_ROOT}"
info "Target HOME: ${TARGET}"
info "Dry-run: ${DRY_RUN}"

# --- Preflight -----------------------------------------------------
for cmd in bash python git; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    error "Missing prerequisite: $cmd"
    exit 1
  fi
done
info "Preflight: bash + python + git present"

# --- Confirmation (unless --force or --dry-run) --------------------
if [ "$DRY_RUN" -eq 0 ] && [ "$FORCE" -eq 0 ]; then
  printf 'About to install to %s. Proceed? [y/N] ' "$TARGET"
  read -r reply
  case "$reply" in [yY]|[yY][eE][sS]) : ;; *) info "Aborted by user"; exit 0 ;; esac
fi

# --- Backup existing artefacts (RULE-010 rollback) -----------------
info "Creating backup dir: ${BACKUP_DIR}"
do_or_dry mkdir -p "${BACKUP_DIR}"
for f in "${CLINERULES}" "${SETTINGS}"; do
  if [ -f "$f" ]; then
    do_or_dry cp "$f" "${BACKUP_DIR}/$(basename "$f").bak"
    info "Backed up: $f"
  fi
done

# --- Install rules -------------------------------------------------
SRC_RULES="${REPO_ROOT}/rules/clinerules.template"
if [ -f "${CLINERULES}" ] && cmp -s "${CLINERULES}" "${SRC_RULES}"; then
  info "Rules already up-to-date at ${CLINERULES} (idempotent skip)"
else
  do_or_dry cp "${SRC_RULES}" "${CLINERULES}"
  info "Installed rules to ${CLINERULES}"
fi

# --- Install hooks -------------------------------------------------
do_or_dry mkdir -p "${HOOKS_DIR}"
for hook in policy-freeze.sh destructive-guard.sh; do
  do_or_dry cp "${REPO_ROOT}/hooks/${hook}" "${HOOKS_DIR}/${hook}"
  do_or_dry chmod +x "${HOOKS_DIR}/${hook}"
  info "Installed hook: ${HOOKS_DIR}/${hook}"
done

# --- Merge settings.json snippet ------------------------------------
do_or_dry mkdir -p "${CLAUDE_HOME}"
if [ ! -f "${SETTINGS}" ]; then
  info "No existing settings.json — creating minimal file"
  if [ "$DRY_RUN" -eq 0 ]; then
    cat > "${SETTINGS}" <<'EOF'
{
  "hooks": { "PreToolUse": [] }
}
EOF
  fi
fi

# Idempotent merge via Python (portable, no jq dependency)
if [ "$DRY_RUN" -eq 0 ]; then
  SETTINGS_PATH="${SETTINGS}" HOOKS_DIR_ENV="${HOOKS_DIR}" python - <<'PY'
import json, os, sys
p = os.environ["SETTINGS_PATH"]
h = os.environ["HOOKS_DIR_ENV"]
try:
    with open(p, "r", encoding="utf-8") as fh:
        raw = fh.read()
    # Attempt strict parse; if it fails, warn and skip merge
    try:
        cfg = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[WARN] settings.json is not strict JSON ({e}); skipping merge — add hooks manually from templates/settings.hooks.snippet.json", file=sys.stderr)
        sys.exit(0)
    cfg.setdefault("hooks", {}).setdefault("PreToolUse", [])
    pre = cfg["hooks"]["PreToolUse"]
    cmd_pf = f'bash "{h}/policy-freeze.sh"'
    cmd_dg = f'bash "{h}/destructive-guard.sh"'
    have_pf = any("policy-freeze" in json.dumps(e) for e in pre)
    have_dg = any("destructive-guard" in json.dumps(e) for e in pre)
    if not have_pf:
        pre.insert(0, {"matcher": "Write|Edit|NotebookEdit",
                       "hooks":[{"type":"command","command":cmd_pf,"timeout":10}]})
        print("[INFO] Added policy-freeze hook to PreToolUse")
    else:
        print("[INFO] policy-freeze hook already registered (idempotent skip)")
    if not have_dg:
        pre.insert(1 if not have_pf else 1, {"matcher": "Bash|PowerShell",
                       "hooks":[{"type":"command","command":cmd_dg,"timeout":10}]})
        print("[INFO] Added destructive-guard hook to PreToolUse")
    else:
        print("[INFO] destructive-guard hook already registered (idempotent skip)")
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(cfg, fh, indent=2)
except Exception as e:
    print(f"[ERROR] Failed to merge settings.json: {e}", file=sys.stderr)
    sys.exit(1)
PY
else
  info "[DRY-RUN] would merge PreToolUse entries into ${SETTINGS}"
fi

# --- Initialise telemetry ------------------------------------------
do_or_dry mkdir -p "${TELEMETRY_DIR}"
AUDIT="${TELEMETRY_DIR}/audit.jsonl"
if [ "$DRY_RUN" -eq 0 ] && [ ! -f "${AUDIT}" ]; then
  BOOTSTRAP_EVENT=$(printf '{"timestamp":"%s","session_id":"install","correlation_id":"cid-install-%s","protocol_version":"v4","event_type":"protocol_bootstrap","actor":"installer","target":"%s","decision":"installed","summary":"initial install by scripts/install.sh"}\n' \
    "$(ts)" "$(date -u +%s)" "$TARGET")
  echo "$BOOTSTRAP_EVENT" >> "${AUDIT}"
  info "Initialised audit log at ${AUDIT}"
fi

# --- Validate ------------------------------------------------------
info "Running validate.sh ..."
if [ "$DRY_RUN" -eq 1 ]; then
  info "[DRY-RUN] skipping validate.sh"
else
  if bash "${REPO_ROOT}/scripts/validate.sh"; then
    info "Validation passed"
  else
    error "Validation FAILED — check output above. Backup at: ${BACKUP_DIR}"
    exit 1
  fi
fi

info "Install complete. Backup: ${BACKUP_DIR}"
info "Uninstall: bash scripts/uninstall.sh"
exit 0
