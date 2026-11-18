#!/usr/bin/env bash
# Upload the course app (dist/app) to a web server over SSH.
# Usage: tools/deploy_pilot.sh user@host:/path/to/webroot/fetal-echo-pilot [--dry-run]
# Run `python tools/build.py` first. Nothing in media/ is ever sent: clips are added by hand
# on the server (see docs/09-hosting-pilot.md), so they never pass through this repository.
set -euo pipefail
cd "$(dirname "$0")/.."
DEST="${1:-}"
[ -n "$DEST" ] || { echo "usage: $0 user@host:/path [--dry-run]"; exit 2; }
[ -f dist/app/index.html ] || { echo "dist/app is missing: run python tools/build.py first"; exit 1; }
EXTRA=()
[ "${2:-}" = "--dry-run" ] && EXTRA+=(--dry-run)
# --exclude protects media/ and the password file on the server from being deleted by --delete
rsync -av --delete "${EXTRA[@]}" \
  --exclude 'media/' --exclude '.htaccess' --exclude '.htpasswd' \
  dist/app/ "$DEST/"
echo "Done. Check that the address asks for a password before sharing it."
