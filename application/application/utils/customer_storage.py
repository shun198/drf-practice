import boto3
from botocore.exceptions import ClientError
from project.settings.environment import aws_settings
from storages.backends.s3boto3 import S3Boto3Storage


class CustomerStorage(S3Boto3Storage):
    pass
