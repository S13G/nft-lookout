from .settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--ojc&jrm^1r94qlu1a*@1pv4x$_8evky+u)xfsm(f$8-0+j)p^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'new_4', 
        'USER': 'postgres', 
        'PASSWORD': '0509',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}

