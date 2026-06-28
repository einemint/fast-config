#!/bin/sh
set -e
mkdir -p /usr/src/app/log_files
chown -R appuser:appuser /usr/src/app/log_files

cd /usr/src/app
exec gosu appuser gunicorn main:app \
  --bind 0.0.0.0:8020 \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --forwarded-allow-ips='*'