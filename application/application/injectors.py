"""DI定義用のモジュール"""
import boto3
from injector import Binder, Injector, Module

from application.utils.sms import SnsResource, SnsWrapper
from project.settings.environment import aws_settings


class SnsWrapperModule(Module):
    def configure(self, binder):
        binder.bind(SnsWrapper)


class LocalModule(Module):
    """Local環境用のモジュール"""

    def configure(self, binder: Binder) -> None:
        sns_resource = SnsResource(
            boto3.resource(
                "sns",
                region_name=aws_settings.AWS_REGION_NAME,
                endpoint_url=aws_settings.ENDPOINT_URL,
            )
        )
        binder.bind(SnsResource, to=sns_resource)


class DevModule(Module):
    """Dev環境用のモジュール"""

    def configure(self, binder: Binder) -> None:
        sns_resource = SnsResource(
            boto3.resource("sns", region_name=aws_settings.AWS_REGION_NAME)
        )
        binder.bind(SnsResource, to=sns_resource)


injector = Injector([SnsWrapperModule()])
