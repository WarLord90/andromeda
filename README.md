# Calculator API in Django

This project contains a simple Django application exposing API endpoints for basic arithmetic operations.

## Endpoints

All endpoints are prefixed with `/api/` and accept query parameters `a` and `b`.

- `/api/add/` – returns the sum of `a` and `b`.
- `/api/subtract/` – returns the difference between `a` and `b`.
- `/api/multiply/` – returns the product of `a` and `b`.
- `/api/divide/` – returns the quotient of `a` divided by `b` (error if `b` is zero).

Example request:

```
curl "http://localhost:8000/api/add/?a=1&b=2"
```

Response:

```
{"result": 3.0}
```

## Setup

1. Install dependencies:
   ```bash
   pip install django
   ```

2. Run migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Then access the endpoints at `http://localhost:8000/api/`.
