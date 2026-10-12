#!/usr/bin/env bash
# Records a lifecycle event, without inferring task success from a stop event.
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
source "$SCRIPT_DIR/hook-lib.sh"
read_hook_input || exit 0
AGENT_NAME=$(json_path "agent_type")
AGENT_ID=$(json_path "agent_id")
[ -z "$AGENT_NAME" ] && AGENT_NAME="unknown"
[ -z "$AGENT_ID" ] && AGENT_ID="unknown"
AGENT_NAME=${AGENT_NAME//$'\n'/ }
AGENT_NAME=${AGENT_NAME//$'\r'/ }
AGENT_ID=${AGENT_ID//$'\n'/ }
AGENT_ID=${AGENT_ID//$'\r'/ }
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
SESSION_LOG_DIR="$(repo_root)/production/session-logs"
if [ "${CGS_HOOK_DRY_RUN:-0}" != "1" ]; then
    mkdir -p "$SESSION_LOG_DIR" || exit 1
    printf '%s | Agent started: %s | id=%s\n' "$TIMESTAMP" "$AGENT_NAME" "$AGENT_ID" >> "$SESSION_LOG_DIR/agent-audit.log" || exit 1
fi
emit_continue_json
exit 0
