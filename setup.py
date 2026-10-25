import re

from setuptools import find_packages, setup

docs_require = ["sphinx>=1.8.4"]

tests_require = [
    "coverage[toml]==5.0.3",
    "freezegun==1.5.5",
    "pytest==9.0.3",
    "pytest-django==4.14.0",
    "pytest-cov==2.8.1",\
    # Linting
    "ruff",
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
    python_requires=">=3.11",
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
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.2",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    zip_safe=False,
)
