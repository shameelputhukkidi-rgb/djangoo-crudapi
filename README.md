# djangoo-crudapi

A reusable Django CRUD API package built with Django REST Framework.

This package provides reusable CRUD functionality that can be easily integrated into any Django project.

---

# Features

- Create API
- Read API
- Update API
- Delete API
- Django REST Framework Support
- PostgreSQL Support
- Reusable Django App
- Easy Integration
- Clean Project Structure
- Easy to Extend

---

# Requirements

- Python 3.10+
- Django 5.2+
- Django REST Framework 3.16+

---

# Installation

```bash
pip install djangoo-crudapi
```

---

# Quick Start

## Step 1 : Add to INSTALLED_APPS

Open **settings.py**

```python
INSTALLED_APPS = [
    ...
    "crudapi",
]
```

---

## Step 2 : Configure URLs

Open your project's **urls.py**

```python
from django.urls import include, path

urlpatterns = [
    path("api/", include("crudapi.urls")),
]
```

---

## Step 3 : Apply Migrations

```bash
python manage.py migrate
```

---

## Step 4 : Run Development Server

```bash
python manage.py runserver
```

Open your browser

```
http://127.0.0.1:8000/
```

---

# Project Structure

```
crudapi/
│
├── admin.py
├── apps.py
├── exceptions.py
├── migrations/
├── models.py
├── permissions.py
├── serializers.py
├── services.py
├── tests.py
├── urls.py
├── utils.py
├── validators.py
├── views.py
└── __init__.py
```

---

# Example Usage

Install Package

```bash
pip install djangoo-crudapi
```

Add the package to Django

```python
INSTALLED_APPS = [
    ...
    "crudapi",
]
```

Include URLs

```python
from django.urls import include, path

urlpatterns = [
    path("api/", include("crudapi.urls")),
]
```

Run Migrations

```bash
python manage.py migrate
```

Run Server

```bash
python manage.py runserver
```

---

# Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL

---

# Package Information

Package Name

```
djangoo-crudapi
```

Install Command

```bash
pip install djangoo-crudapi
```

PyPI

https://pypi.org/project/djangoo-crudapi/

GitHub

https://github.com/shameelputhukkidi-rgb/djangoo-crudapi

---

# Author

**Mohammed Shameel**

Python Django Full Stack Developer

GitHub

https://github.com/shameelputhukkidi-rgb

---

# License

MIT License

You are free to use, modify and distribute this package under the MIT License.

---

# Support

If you find this package useful,

⭐ Star the GitHub repository

🐞 Report issues on GitHub

💡 Suggest new features

---

# Thank You

Thank you for using **djangoo-crudapi**.

Happy Coding! 🚀