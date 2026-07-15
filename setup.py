from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="djangoo-crudapi",
    version="2.1.1",

    author="Mohammed Shameel",
    author_email="YOUR_EMAIL@gmail.com",

    description="Reusable Django CRUD API app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/shameelputhukkidi-rgb/djangoo-crudapi",

    packages=find_packages(include=["crudapi", "crudapi.*"]),

    include_package_data=True,

    install_requires=[
        "Django>=5.2",
        "djangorestframework>=3.16",
        "psycopg2-binary>=2.9",
    ],

    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires=">=3.10",

    zip_safe=False,
)