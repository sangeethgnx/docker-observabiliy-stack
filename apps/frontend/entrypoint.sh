#!/bin/sh
set -e

ROOT="/workspace"
APP="$ROOT/frontend"

echo "[ENTRYPOINT] Node: $(node -v)"
echo "[ENTRYPOINT] NPM : $(npm -v)"

cd "$APP"

# Install dependencies if needed
if [ ! -d node_modules ]; then
  echo "[ENTRYPOINT] Installing dependencies..."
  npm install
fi

echo "[ENTRYPOINT] Starting Vite dev server..."
exec npm run dev -- --host 0.0.0.0
