import time
import re

from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


SESSION_TIMEOUT_KEY = "_session_init_timestamp_"


class SessionTimeoutMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        self.ignored_paths_regex = None

        regex = getattr(settings, "SESSION_ACTIVITY_IGNORED_PATHS_REGEX", None)
        if regex:
            self.ignored_paths_regex = re.compile(regex)

    def is_path_ignored(self, path):
        ignored = self.ignored_paths_regex and bool(self.ignored_paths_regex.search(path))
        return ignored

    def process_request(self, request):
        if not hasattr(request, "session") or request.session.is_empty():
            return

        init_time = request.session.setdefault(SESSION_TIMEOUT_KEY, time.time())

        expire_seconds = getattr(
            settings, "SESSION_EXPIRE_SECONDS", settings.SESSION_COOKIE_AGE
        )

        session_is_expired = time.time() - init_time > expire_seconds

        if session_is_expired:
            request.session.flush()
            redirect_url = getattr(settings, "SESSION_TIMEOUT_REDIRECT", None)
            if redirect_url:
                return redirect(redirect_url)
            else:
                return redirect_to_login(next=request.path)

        expire_since_last_activity = getattr(
            settings, "SESSION_EXPIRE_AFTER_LAST_ACTIVITY", False
        )
        grace_period = getattr(
            settings, "SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD", 1
        )

        if expire_since_last_activity \
            and time.time() - init_time > grace_period \
            and not self.is_path_ignored(request.path):
            request.session[SESSION_TIMEOUT_KEY] = time.time()
