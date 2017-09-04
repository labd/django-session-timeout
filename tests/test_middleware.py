import pytest
from freezegun import freeze_time
from django_session_timeout.middleware import SESSION_TIMEOUT_KEY
from django.contrib.sessions.middleware import SessionMiddleware

from django_session_timeout.middleware import SessionTimeoutMiddleware


@pytest.fixture(scope='function')
def r(rf):
    req = rf.get('/')
    middleware = SessionMiddleware()
    middleware.process_request(req)
    req.session['example_key'] = '1'

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

    with freeze_time('2017-08-31 21:46:00'):
        assert middleware.process_request(r) is None

    with freeze_time('2017-08-31 22:45:00'):
        assert middleware.process_request(r) is None

    with freeze_time('2017-08-31 22:46:01'):
        response = middleware.process_request(r)
        assert SESSION_TIMEOUT_KEY not in r.session
        assert response['location'] == '/'


def test_session_expire_no_expire_setting(r, settings):
    settings.SESSION_COOKIE_AGE = 3600
    middleware = SessionTimeoutMiddleware()

    with freeze_time('2017-08-31 21:46:00'):
        assert middleware.process_request(r) is None

    with freeze_time('2017-08-31 22:45:00'):
        assert middleware.process_request(r) is None

    with freeze_time('2017-08-31 22:46:01'):
        response = middleware.process_request(r)
        assert SESSION_TIMEOUT_KEY not in r.session
        assert response['location'] == '/'
