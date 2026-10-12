"""
Django settings for Mahin Travels.

Secrets and database credentials are loaded from a local .env file.
Never commit real passwords or API keys.
"""
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def env(name, default=""):
    return os.getenv(name, default)


SECRET_KEY = env("SECRET_KEY", "unsafe-dev-key-change-me")
# Prefer the project-specific name to avoid collisions with host environment
# variables that may use DEBUG for an unrelated purpose.
DEBUG = env("DJANGO_DEBUG", env("DEBUG", "True")).lower() in ("1", "true", "yes")
ALLOWED_HOSTS = [
    host.strip()
    for host in env("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
    if host.strip()
]
vercel_hosts = []
for variable in ("VERCEL_URL", "VERCEL_BRANCH_URL", "VERCEL_PROJECT_PRODUCTION_URL"):
    host = env(variable).strip()
    if host and host not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(host)
        vercel_hosts.append(host)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "tours",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "tours.context_processors.site_defaults",
            ],
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASE_URL = (
    env("DATABASE_URL").strip()
    or env("POSTGRES_URL_NON_POOLING").strip()
    or env("POSTGRES_URL").strip()
    or env("POSTGRES_PRISMA_URL").strip()
)
DATABASE_ENGINE = env("DATABASE_ENGINE", "sqlite").lower()
if DATABASE_URL:
    import dj_database_url

    database_config = dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=True,
    )
    # Supabase's transaction pooler can route each transaction to a different
    # database connection, so Django must not keep server-side cursors open.
    database_config["DISABLE_SERVER_SIDE_CURSORS"] = True
    DATABASES = {
        "default": database_config
    }
elif env("VERCEL") == "1" or env("VERCEL_URL") or env("VERCEL_ENV"):
    raise ImproperlyConfigured(
        "Vercel requires a hosted PostgreSQL connection. Set DATABASE_URL, "
        "POSTGRES_URL_NON_POOLING, or POSTGRES_URL in Project Environment Variables."
    )
elif DATABASE_ENGINE == "postgresql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("POSTGRES_DB", "mahin_travels"),
            "USER": env("POSTGRES_USER", "postgres"),
            "PASSWORD": env("POSTGRES_PASSWORD"),
            "HOST": env("POSTGRES_HOST", "localhost"),
            "PORT": env("POSTGRES_PORT", "5432"),
            "CONN_MAX_AGE": 60,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-in"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

GEMINI_API_KEY = env("GEMINI_API_KEY")
GEMINI_MODEL = env("GEMINI_MODEL", "gemini-2.0-flash")

# Override these values through .env before deploying the site.
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in env("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]
CSRF_TRUSTED_ORIGINS.extend(
    f"https://{host}"
    for host in vercel_hosts
    if f"https://{host}" not in CSRF_TRUSTED_ORIGINS
)

SITE_NAME = "Mahin Travels"
SITE_TAGLINE = "Discover India, one journey at a time"
SITE_PHONE = "+91 98765 43210"
SITE_EMAIL = "hello@mahintravels.com"
SITE_ADDRESS = "MG Road, Bengaluru, Karnataka, India"
