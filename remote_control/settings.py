from django.conf import settings


# The key to use when signing requests
try:
    SECRET = settings.REMOTE_CONTROL_SECRET
except AttributeError:
    raise ValueError("REMOTE_CONTROL_SECRET is not specified in your settings.")

# The number of seconds until a request is no longer valid
REQUEST_MAX_AGE = getattr(settings, 'REMOTE_CONTROL_REQUEST_MAX_AGE', 60)

# The registered commands which can be called
COMMANDS = getattr(settings, 'REMOTE_CONTROL_COMMANDS', {})
