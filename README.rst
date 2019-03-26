======================
django-session-timeout
======================


Status
======
.. image:: https://travis-ci.org/labd/django-session-timeout.svg?branch=master
    :target: https://travis-ci.org/labd/django-session-timeout

.. image:: http://codecov.io/github/LabD/django-session-timeout/coverage.svg?branch=master
    :target: http://codecov.io/github/LabD/django-session-timeout?branch=master

.. image:: https://img.shields.io/pypi/v/django-session-timeout.svg
    :target: https://pypi.python.org/pypi/django-session-timeout/


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
