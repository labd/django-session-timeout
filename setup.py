import re

from setuptools import find_packages, setup

docs_require = ["sphinx>=1.8.4"]

tests_require = [
    "coverage[toml]==5.0.3",
    "freezegun==0.3.15",
    "pytest==5.3.5",
    "pytest-django==3.8.0",
    "pytest-cov==2.8.1",\
    # Linting
    "isort[pyproject]==4.3.21",
    "flake8==3.7.9",
    "flake8-blind-except==0.1.1",
    "flake8-debugger==3.1.0",
]

with open("README.md") as fh:
    long_description = re.sub(
        "<!-- start-no-pypi -->.*<!-- end-no-pypi -->\n",
        "",
        fh.read(),
        flags=re.M | re.S,
    )

setup(
    name="django-session-timeout",
    version="0.1.0",
    description="Middleware to expire sessions after specific amount of time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LabD/django-session-timeout",
    author="Lab Digital",
    author_email="opensource@labdigital.nl",
    install_requires=["Django>=1.11", "six>=1.12"],
    tests_require=tests_require,
    extras_require={"docs": docs_require, "test": tests_require},
    use_scm_version=True,
    entry_points={},
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
)
