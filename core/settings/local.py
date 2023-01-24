from .base import *

THIRDY_APPS = [
    'drf_spectacular'
]
[INSTALLED_APPS.append(app) for app in THIRDY_APPS] 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Django DRF E-commerce',
    'DESCRIPTION': 'Django rest framework E-commerce',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}