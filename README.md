# django-session-timeout

[![PyPI](https://img.shields.io/pypi/v/django-session-timeout)](https://pypi.org/project/django-session-timeout/)
[![tests](https://github.com/labd/django-session-timeout/actions/workflows/python-test.yml/badge.svg)](https://github.com/labd/django-session-timeout/actions/workflows/python-test.yml)
[![readthedocs](https://readthedocs.org/projects/django-session-timeout/badge/)](https://django-session-timeout.readthedocs.io/en/latest/)

Add timestamp to sessions to expire them independently

## Installation

```shell
pip install django-session-timeout
```

## Usage

Update your settings to add the SessionTimeoutMiddleware:

```python
MIDDLEWARE_CLASSES = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    # ...
]
```

And also add the ``SESSION_EXPIRE_SECONDS``:


```python
SESSION_EXPIRE_SECONDS = 3600  # 1 hour
```

By default, the session will expire X seconds after the start of the session.
To expire the session X seconds after the `last activity`, use the following setting:

```python
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
```

By default, `last activity` will be grouped per second.
To group by different period use the following setting:

```python
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60 # group by minute
```

To redirect to a custom URL define the following setting:

```python
SESSION_TIMEOUT_REDIRECT = 'your_redirect_url_here/'
```

## Releasing

Changes are tracked with [changie](https://changie.dev/). Add a changelog
entry to every pull request with a user-facing change:

```shell
changie new
```

When entries are merged to the default branch, a release pull request is
opened (or updated) automatically. Merging that pull request tags the release,
creates the GitHub release and publishes the package to PyPI.
