from datetime import datetime, timedelta

from factory import Faker, Sequence
from factory.django import DjangoModelFactory
from application.models import Customer
from application.tests.factories.address import AddressFactory


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    name = Sequence(lambda n: "テストコキャク{}".format(n))
    name = Sequence(lambda n: "テスト顧客{}".format(n))
    birthday = Faker(
        "date_between_dates",
        date_start=(datetime.now() - timedelta(days=70)).date(),
        date_end=(datetime.now() - timedelta(days=20)).date(),
    )
    phone_no = Sequence(
        lambda n: f"0{7+((n%9+1)%3)}0" + "{0:08}".format(n + 100)
    )
