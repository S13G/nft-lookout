from .settings import *
import os
from decouple import config
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['nfts-lookup.herokuapp.com']

DATABASES = {
    "default": dj_database_url.config()
}
