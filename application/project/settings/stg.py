"""STG環境用の設定"""
from .base import *

DEBUG = False
ROOT_URLCONF = "project.urls.base"

INSTALLED_APPS += [
    "django_ses",
    "storages",
]


# SESの設定
EMAIL_BACKEND = "django_ses.SESBackend"
AWS_SES_REGION_NAME = os.environ.get("AWS_SES_REGION_NAME")
AWS_SES_REGION_ENDPOINT = os.environ.get("AWS_SES_REGION_ENDPOINT")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
# S3の設定
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
