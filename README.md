# fast-config

FastConfig is a ready-to-use infrastructure for projects using FastAPI.

## Built with

PostgreSQL

Java 11

- Maven

- Lombok

- Spring Boot

- Spring Boot Starter Data JPA

- Spring Boot Test

- Log4j2

## Installation

1. Clone the repo: https://github.com/einemint/fast-config
2. Install Docker CLI

## Usage
1. Add your code or modules in /app directory
2. Create file .env in the root directory containing variables

DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=

REDIS_HOST=
REDIS_PORT=
REDIS_PASSWORD=

3. Edit Nginx config /app/nginx.conf
4. Edit Celery app /app/celery/celery_app.py
5. Use variables from .env for PostgreSQL and Redis connection
6. Run docker compose up -d in terminal

## Contacts

GitHub:

https://github.com/einemint

Email:

einemint@gmail.com
