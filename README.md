# djangoo-crudapi

A reusable Django CRUD API package built with Django REST Framework.

## Features

- Create API
- Read API
- Update API
- Delete API
- Django REST Framework Support
- PostgreSQL Support
- Reusable Django App
- Easy Integration
- Clean Project Structure

---

## Requirements

- Python 3.10+
- Django 5.2+
- Django REST Framework 3.16+

---

## Installation

```bash
pip install djangoo-crudapi
```

---

## Add to INSTALLED_APPS

Open your **settings.py**

```python
INSTALLED_APPS = [
    ...
    "crudapi",
]
```

---

## Configure URLs

Open your project's **urls.py**

```python
from django.urls import path, include

urlpatterns = [
    path("api/", include("crudapi.urls")),
]
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Run Development Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## Project Structure

```
crudapi/
│── admin.py
│── apps.py
│── exceptions.py
│── models.py
│── permissions.py
│── serializers.py
│── services.py
│── tests.py
│── urls.py
│── utils.py
│── validators.py
│── views.py
│── migrations/
```

---

## Example

Install package

```bash
pip install djangoo-crudapi
```

Add to Django

```python
INSTALLED_APPS = [
    ...
    "crudapi",
]
```

Include URLs

```python
urlpatterns = [
    path("api/", include("crudapi.urls")),
]
```

Run

```bash
python manage.py migrate
python manage.py runserver
```

---

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL

---

## Author

**Mohammed Shameel**

GitHub:
https://github.com/shameelputhukkidi-rgb

PyPI:
https://pypi.org/project/djangoo-crudapi/

---

## License

MIT License

---

⭐ If you like this project, please give it a star on GitHub.