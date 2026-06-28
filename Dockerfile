FROM python:3.14-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /usr/src/app

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev


FROM python:3.14-slim

RUN apt-get update && apt-get install -y --no-install-recommends gosu \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ./app/ .
COPY --from=builder /usr/src/app/.venv .venv
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

RUN useradd -m -u 1000 appuser && \
    mkdir -p /usr/src/app/log_files && \
    chown -R appuser:appuser /usr/src/app

ENV PATH="/usr/src/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8020

ENTRYPOINT ["docker-entrypoint.sh"]