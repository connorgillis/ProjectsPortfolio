from .base import *

import os

from google.oauth2 import service_account

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_HOST = ''
EMAIL_PORT = 465

EMAIL_HOST_USER = ''

EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

EMAIL_USE_SSL = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    ""
)

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

GS_PROJECT_ID = ''
GS_BUCKET_NAME = ''

MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)

try:
    from .local import *
except ImportError:
    pass

django_heroku.settings(locals())
