<!-- start-no-pypi -->
[![codecov](https://codecov.io/gh/labd/django-session-timeout/branch/master/graph/badge.svg)](https://codecov.io/gh/labd/django-session-timeout)
[![pypi](https://img.shields.io/pypi/v/django-session-timeout.svg)](https://pypi.python.org/pypi/django-session-timeout/)
[![readthedocs](https://readthedocs.org/projects/django-session-timeout/badge/)](https://django-session-timeout.readthedocs.io/en/latest/)
[![tests](https://github.com/labd/django-session-timeout/workflows/Python%20Tests/badge.svg)](https://github.com/labd/django-session-timeout/actions)
<!-- end-no-pypi -->

# django-session-timeout

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

By default, `last activiy` will be grouped per second.
To group by different period use the following setting:

```python
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60 # group by minute
```

To redirect to a custom URL define the following setting:

```python
SESSION_TIMEOUT_REDIRECT = 'your_redirect_url_here/'
```
