"""
Django settings for eventease_project project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Load local .env if it exists
if (BASE_DIR / ".env.local").exists():
    load_dotenv(BASE_DIR / ".env.local")
else:
    load_dotenv(BASE_DIR / ".env")  # Render uses environment vars anyway

# SECURITY
SECRET_KEY = os.getenv("SECRET_KEY", "insecure-default-key")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']
CSRF_TRUSTED_ORIGINS = ['http://localhost', 'https://*.onrender.com']

# APPLICATIONS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main_app",
]

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Whitenoise for static files
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

ROOT_URLCONF = "eventease_project.urls"

# TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "eventease_project.wsgi.application"

# DATABASE
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    # Production / Render
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL, conn_max_age=600, ssl_require=True
        )
    }
else:
    # Local development
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME", "events"),
            "USER": os.getenv("DB_USER", "postgres"),
            "PASSWORD": os.getenv("DB_PASSWORD", "H0612z"),
            "HOST": os.getenv("DB_HOST", "localhost"),
            "PORT": os.getenv("DB_PORT", "5432"),
        }
    }

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# AUTH
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
