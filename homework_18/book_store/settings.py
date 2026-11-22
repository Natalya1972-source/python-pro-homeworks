"""
Django settings for book_store project.
"""

import os
from pathlib import Path


# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# SECURITY
# --------------------------------------------------

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-homework18-local-development-key",
)

DEBUG = os.getenv(
    "DJANGO_DEBUG",
    "True",
).lower() == "true"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------

INSTALLED_APPS = [
    # Django applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Debug Toolbar
    "debug_toolbar",

    # Our applications
    "books",
    "accounts",
]


# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    "debug_toolbar.middleware.DebugToolbarMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    # Custom middleware
    "books.middleware.RequestLoggingMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------------------------------------
# URL CONFIGURATION
# --------------------------------------------------

ROOT_URLCONF = "book_store.urls"


# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# --------------------------------------------------
# WSGI
# --------------------------------------------------

WSGI_APPLICATION = "book_store.wsgi.application"


# --------------------------------------------------
# DATABASE - POSTGRESQL
# --------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",

        "NAME": os.getenv(
            "POSTGRES_DB",
            "bookstore",
        ),

        "USER": os.getenv(
            "POSTGRES_USER",
            "bookuser",
        ),

        "PASSWORD": os.getenv(
            "POSTGRES_PASSWORD",
            "bookpass",
        ),

        "HOST": os.getenv(
            "POSTGRES_HOST",
            "db",
        ),

        "PORT": os.getenv(
            "POSTGRES_PORT",
            "5432",
        ),
    }
}


# --------------------------------------------------
# REDIS CACHE
# --------------------------------------------------

REDIS_HOST = os.getenv(
    "REDIS_HOST",
    "redis",
)

REDIS_PORT = os.getenv(
    "REDIS_PORT",
    "6379",
)

CACHES = {
    "default": {
        "BACKEND": (
            "django.core.cache.backends.redis.RedisCache"
        ),
        "LOCATION": (
            f"redis://{REDIS_HOST}:{REDIS_PORT}/1"
        ),
    }
}


# --------------------------------------------------
# CUSTOM USER MODEL
# --------------------------------------------------

AUTH_USER_MODEL = "accounts.CustomUser"


# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = "uk"

TIME_ZONE = "Europe/Kyiv"

USE_I18N = True

USE_TZ = True


# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# --------------------------------------------------
# EMAIL
# --------------------------------------------------

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)


# --------------------------------------------------
# AUTHENTICATION
# --------------------------------------------------

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "books:home"

LOGOUT_REDIRECT_URL = "books:home"


# --------------------------------------------------
# DJANGO DEBUG TOOLBAR
# --------------------------------------------------

INTERNAL_IPS = [
    "127.0.0.1",
]


# --------------------------------------------------
# LOGGING
# --------------------------------------------------

LOGGING = {
    "version": 1,

    "disable_existing_loggers": False,

    "formatters": {
        "simple": {
            "format": (
                "{levelname} "
                "{asctime} "
                "{name}: "
                "{message}"
            ),
            "style": "{",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },

    "loggers": {
        "books": {
            "handlers": [
                "console",
            ],
            "level": "INFO",
            "propagate": False,
        },
    },
}


# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
