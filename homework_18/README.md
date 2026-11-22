# Homework 18.1 — Docker: контейнеризація Python-додатків

Навчальний Django-проєкт книжкового магазину, контейнеризований за допомогою Docker Compose.

## Реалізовано

У проєкті налаштовано три Docker-сервіси:

- `web` — Django;
- `db` — PostgreSQL;
- `redis` — Redis.

Також реалізовано:

- Dockerfile для Django-проєкту;
- Docker Compose;
- PostgreSQL volume для збереження даних;
- volume для static files;
- healthcheck для PostgreSQL;
- healthcheck для Redis;
- `docker-entrypoint.sh`;
- автоматичне виконання Django migrations;
- автоматичний `collectstatic`;
- `.env` для змінних оточення;
- `.env.example`;
- перенесення даних з SQLite до PostgreSQL;
- Redis як Django cache.

## Запуск проєкту

Створити файл `.env` на основі `.env.example`.

Потім виконати:

```bash
docker compose up --build
```

Після запуску сайт доступний:

```text
http://127.0.0.1:8000/
```

## Перевірка контейнерів

```bash
docker compose ps
```

Очікуються три сервіси:

```text
web
db
redis
```

PostgreSQL та Redis повинні мати статус `healthy`.

## Завантаження тестових даних

```bash
docker compose exec web python manage.py loaddata books/fixtures/books_data.json
```

## Перевірка PostgreSQL

```bash
docker compose exec web python manage.py shell -c "from django.db import connection; print(connection.vendor)"
```

Очікуваний результат:

```text
postgresql
```

## Перевірка Redis

```bash
docker compose exec web python manage.py shell -c "from django.core.cache import cache; cache.set('test_key', 'Redis працює', 60); print(cache.get('test_key'))"
```

Очікуваний результат:

```text
Redis працює
```

## Docker volumes

Використовуються:

- `postgres_data` — дані PostgreSQL;
- `static_data` — статичні файли Django.

## Docker entrypoint

`docker-entrypoint.sh`:

1. очікує готовності PostgreSQL;
2. запускає migrations;
3. виконує `collectstatic`;
4. запускає Django.

## Основні технології

- Python 3.13
- Django 6.1
- PostgreSQL
- Redis
- Docker
- Docker Compose
- WSL
- 