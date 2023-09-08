

import os
from .base import *

ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(" ")
SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = os.environ["DEBUG"].lower() == "true"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + os.environ["DB_ENGINE"],
        'NAME': os.environ["DB_NAME"],
        'HOST': os.environ["DB_HOST"],
        'PORT': os.environ["DB_PORT"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
    }
}

CORS_ALLOWED_ORIGINS = [
    os.environ["FRONTEND_ORIGIN"],
]