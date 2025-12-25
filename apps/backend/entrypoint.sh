#!/bin/sh
set -e

echo "[ENTRYPOINT] Python: $(python --version)"

if [ ! -d /app/venv ]; then
  echo "[ENTRYPOINT] Installing dependencies..."
  pip install --no-cache-dir flask psycopg2-binary prometheus-flask-exporter requests
fi

echo "[ENTRYPOINT] Starting Flask backend..."
exec python /app/app.py
