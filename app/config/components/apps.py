DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "debug_toolbar",
]

INTERNAL_APPS = [
    "movies.apps.MoviesConfig",
]

INSTALLED_APPS = [*DJANGO_APPS, *THIRD_PARTY_APPS, *INTERNAL_APPS]
