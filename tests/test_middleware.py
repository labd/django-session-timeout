import pytest
from django.contrib.sessions.middleware import SessionMiddleware
from freezegun import freeze_time

from django_session_timeout.middleware import (
    SESSION_TIMEOUT_KEY,
    SessionTimeoutMiddleware,
)


@pytest.fixture(scope="function")
def r(rf):
    req = rf.get("/")
    middleware = SessionMiddleware()
    middleware.process_request(req)
    req.session["example_key"] = "1"

    req.session.save()
    yield req


def test_session_new(r):
    middleware = SessionTimeoutMiddleware()
    assert middleware.process_request(r) is None
    assert r.session[SESSION_TIMEOUT_KEY]


def test_session_new_empty_session(r):
    r.session.flush()

    middleware = SessionTimeoutMiddleware()
    assert middleware.process_request(r) is None
    assert SESSION_TIMEOUT_KEY not in r.session


def test_session_expire(r, settings):
    settings.SESSION_EXPIRE_SECONDS = 3600
    middleware = SessionTimeoutMiddleware()

    with freeze_time("2017-08-31 21:46:00"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 22:45:00"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 22:46:01"):
        response = middleware.process_request(r)
        assert SESSION_TIMEOUT_KEY not in r.session
        assert response["location"] == "/accounts/login/?next=/"


def test_session_expire_custom_redirect(r, settings):
    settings.SESSION_EXPIRE_SECONDS = 3600
    settings.SESSION_TIMEOUT_REDIRECT = "/foobar/"
    middleware = SessionTimeoutMiddleware()

    with freeze_time("2017-08-31 21:46:00"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 22:46:01"):
        response = middleware.process_request(r)
        assert response["location"] == "/foobar/"


def test_session_expire_no_expire_setting(r, settings):
    settings.SESSION_COOKIE_AGE = 3600
    middleware = SessionTimeoutMiddleware()

    with freeze_time("2017-08-31 21:46:00"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 22:45:00"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 22:46:01"):
        response = middleware.process_request(r)
        assert SESSION_TIMEOUT_KEY not in r.session
        assert response["location"] == "/accounts/login/?next=/"


def test_session_expire_last_activity(r, settings):
    settings.SESSION_COOKIE_AGE = 3600
    settings.SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
    middleware = SessionTimeoutMiddleware()

    with freeze_time("2017-08-31 20:46:00"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 21:45:00"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 21:46:01"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 23:46:02"):
        response = middleware.process_request(r)
        assert SESSION_TIMEOUT_KEY not in r.session
        assert response["location"] == "/accounts/login/?next=/"


def test_session_expire_last_activity_grace_(r, settings):
    settings.SESSION_COOKIE_AGE = 3600
    settings.SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
    settings.SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 90
    middleware = SessionTimeoutMiddleware()

    value = None

    with freeze_time("2017-08-31 20:46:00"):
        assert middleware.process_request(r) is None
        value = r.session[SESSION_TIMEOUT_KEY]

    with freeze_time("2017-08-31 20:47:00"):
        assert middleware.process_request(r) is None
        assert r.session[SESSION_TIMEOUT_KEY] is value

    with freeze_time("2017-08-31 20:47:31"):
        assert middleware.process_request(r) is None
        assert r.session[SESSION_TIMEOUT_KEY] is not value

    with freeze_time("2017-08-31 21:47:32"):
        response = middleware.process_request(r)
        assert SESSION_TIMEOUT_KEY not in r.session
        assert response["location"] == "/accounts/login/?next=/"


def test_session_expire_last_activity_grace_not_update(r, settings):
    settings.SESSION_COOKIE_AGE = 3600
    settings.SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
    settings.SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 90
    middleware = SessionTimeoutMiddleware()

    value = None

    with freeze_time("2017-08-31 20:46:00"):
        assert middleware.process_request(r) is None
        value = r.session[SESSION_TIMEOUT_KEY]

    with freeze_time("2017-08-31 20:47:00"):
        assert middleware.process_request(r) is None
        assert r.session[SESSION_TIMEOUT_KEY] is value

    with freeze_time("2017-08-31 21:46:01"):
        response = middleware.process_request(r)
        assert SESSION_TIMEOUT_KEY not in r.session
        assert response["location"] == "/accounts/login/?next=/"


def test_session_expire_to_redirect(r, settings):
    settings.SESSION_EXPIRE_SECONDS = 3600
    settings.SESSION_TIMEOUT_REDIRECT = "/foobar/"
    settings.SESSION_TIMEOUT_TO_REDIRECT = True
    middleware = SessionTimeoutMiddleware()

    with freeze_time("2017-08-31 21:46:00"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 22:46:01"):
        response = middleware.process_request(r)
        assert response["location"] == "/foobar/"

        settings.SESSION_TIMEOUT_TO_REDIRECT = False
        response = middleware.process_request(r)
        assert response is None

def test_session_expire_to_redirect_login(r, settings):
    settings.SESSION_EXPIRE_SECONDS = 3600
    settings.SESSION_TIMEOUT_TO_REDIRECT = True
    settings.SESSION_TIMEOUT_REDIRECT = None
    middleware = SessionTimeoutMiddleware()

    with freeze_time("2017-08-31 21:46:00"):
        assert middleware.process_request(r) is None

    with freeze_time("2017-08-31 22:46:01"):
        response = middleware.process_request(r)
        assert response["location"] == "/accounts/login/?next=/"

        settings.SESSION_TIMEOUT_TO_REDIRECT = False
        response = middleware.process_request(r)
        assert response is None
