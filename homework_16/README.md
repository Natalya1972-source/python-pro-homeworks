# Homework 16 — Авторизація та безпека в Django

Навчальний проєкт книжкового магазину на Django.

## Реалізовано

У домашньому завданні додано:

- Custom User Model на основі `AbstractUser`
- реєстрацію нового користувача
- login
- logout
- захист сторінок для авторизованих користувачів
- Django permissions
- Django groups
- групу `Managers`
- права на додавання, редагування, видалення та перегляд книг
- Django Debug Toolbar
- logging
- custom middleware для логування HTTP-запитів
- відображення користувача в навігації

## Права доступу

Користувачі групи `Managers` мають права:

- `add_book`
- `change_book`
- `delete_book`
- `view_book`

Звичайний користувач може переглядати сайт, але не має прав на додавання, редагування та видалення книг.

## Custom Middleware

Middleware фіксує:

- HTTP-метод
- URL запиту
- користувача
- HTTP status response
- час виконання запиту

Приклад логування:

```text
INFO books.middleware: Request: GET / | User: Nataly
INFO books.views: Користувач відкрив головну сторінку
INFO books.middleware: Response: 200 | Path: / | Time: 0.021 sec
```

## Django Debug Toolbar

Для аналізу роботи застосунку підключено `django-debug-toolbar`.

Toolbar дозволяє переглядати:

- SQL-запити
- templates
- request
- settings
- час виконання запитів

## Запуск проєкту

Встановити залежності:

```bash
pip install -r requirements.txt
```

Виконати міграції:

```bash
python manage.py migrate
```

Завантажити тестові дані книжкового магазину:

```bash
python manage.py loaddata books_data.json
```

Запустити сервер:

```bash
python manage.py runserver
```

Проєкт буде доступний за адресою:

```text
http://127.0.0.1:8000/
```

## Використані технології

- Python
- Django
- SQLite
- HTML
- CSS
- Django Templates
- Django Authentication
- Django Permissions and Groups
- Django Debug Toolbar
- Logging
- Custom Middleware