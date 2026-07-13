from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="crudapi",
    version="1.0.0",
    author="Mohammed Shameel",
    author_email="your_email@example.com",
    description="Reusable Django CRUD API Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
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
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)