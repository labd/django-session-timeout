.. start-no-pypi

.. image:: https://dev.azure.com/lab-digital-opensource/django-session-timeout/_apis/build/status/labd.django-session-timeout?branchName=master
    :target: https://dev.azure.com/lab-digital-opensource/django-session-timeout/_build/latest?definitionId=2&branchName=master

.. image:: http://codecov.io/github/LabD/django-session-timeout/coverage.svg?branch=master
    :target: http://codecov.io/github/LabD/django-session-timeout?branch=master

.. image:: https://img.shields.io/pypi/v/django-session-timeout.svg
    :target: https://pypi.python.org/pypi/django-session-timeout/

.. image:: https://readthedocs.org/projects/django-session-timeout/badge/?version=stable
    :target: https://django-session-timeout.readthedocs.io/en/stable/?badge=stable
    :alt: Documentation Status

.. image:: https://img.shields.io/github/stars/labd/django-session-timeout.svg?style=social&logo=github
    :target: https://github.com/Labd/django-session-timeout/stargazers

.. end-no-pypi

======================
django-session-timeout
======================

Add timestamp to sessions to expire them independently

Installation
============

.. code-block:: shell

   pip install django-session-timeout


Usage
=====

Update your settings to add the SessionTimeoutMiddleware:

.. code-block:: python

    MIDDLEWARE_CLASSES = [
        # ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django_session_timeout.middleware.SessionTimeoutMiddleware',
        # ...
    ]


And also add the ``SESSION_EXPIRE_SECONDS``:


.. code-block:: python

    SESSION_EXPIRE_SECONDS = 3600  # 1 hour


By default, the session will expire X seconds after the start of the session.
To expire the session X seconds after the `last activity`, use the following setting:

.. code-block:: python

    SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True


By default, `last activiy` will be grouped per second.
To group by different period use the following setting:

.. code-block:: python

    SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60 # group by minute
