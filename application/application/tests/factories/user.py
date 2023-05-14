"""ユーザー生成用モジュール"""
from datetime import datetime, timedelta

from factory import Faker, PostGenerationMethodCall, Sequence
from factory.django import DjangoModelFactory

from application.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Sequence(lambda n: "テスト利用者{}".format(n))
    employee_number = Sequence(lambda n: "{0:08}".format(n + 100))
    password = PostGenerationMethodCall("set_password", "test")
    email = "test@com"
    role = User.Role.GENERAL
    created_at = Faker(
        "date_between_dates",
        date_start=(datetime.now() - timedelta(days=20)).date(),
        date_end=datetime.now(),
    )
    updated_at = Faker(
        "date_between_dates",
        date_start=(datetime.now() - timedelta(days=20)).date(),
        date_end=datetime.now(),
    )
