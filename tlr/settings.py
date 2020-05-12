import os
import sys
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

STORAGE_DIR = os.path.join(BASE_DIR, 'storage')
LOG_DIR = os.path.join(STORAGE_DIR, 'logs')

DEBUG = config('DEBUG', default=False, cast=bool)
DATABASE_ENGINE = config('DATABASE_ENGINE')
REDIS_URL = config('REDIS_URL')
MIGRATED = config('MIGRATED', default=True, cast=bool)
TELNET_HOST = config('TELNET_HOST')
TELNET_PORT = config('TELNET_PORT')
TELNET_TIMEOUT = config('TELNET_TIMEOUT', default=300, cast=int)

TIMEZONE = config('TIMEZONE', default='Asia/Jakarta')

LOGGING_ROOT = config(
    'LOGGING_ROOT', default=os.path.join(STORAGE_DIR, 'logs'))
LOG_LEVEL = config('LOG_LEVEL', default='info').upper()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '{asctime} {levelname} {name} {message}',
            'style': '{',
        },
        'verbose': {
            'format': '{asctime} {levelname} {name} {process:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'production': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'tlr.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 7,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'production'],
            'level': LOG_LEVEL
        },
        '__main__': {
            'handlers': ['console', 'production'],
            'level': LOG_LEVEL,
            'propagate': False,
        }
    }
}
