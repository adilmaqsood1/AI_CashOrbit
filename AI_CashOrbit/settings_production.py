"""Production settings for AI_CashOrbit project.

This file contains production-specific settings that override the base settings.
"""

from .settings import *

# Override base settings for production
DEBUG = False

SECRET_KEY = 'django-insecure-h*ux4_nqet!-^w4!uewv+mw-8c+9pke^zus67(ol)0w!^+tsg9'

ALLOWED_HOSTS = ['*', '.railway.app']

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Configure logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
            'propagate': False,
        },
    },
}

# Ensure static files configuration is correct
STATIC_ROOT = BASE_DIR / 'staticfiles'