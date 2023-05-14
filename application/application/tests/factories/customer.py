from datetime import datetime, timedelta

import factory
from factory import Faker, Sequence

from application.models import Address, Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    kana = Sequence(lambda n: "テストコキャク{}".format(n))
    name = Sequence(lambda n: "テスト顧客{}".format(n))
    birthday = Faker(
        "date_between_dates",
        date_start=(datetime.now() - timedelta(days=70)).date(),
        date_end=(datetime.now() - timedelta(days=20)).date(),
    )
    phone_no = Sequence(
        lambda n: f"0{7+((n%9+1)%3)}0" + "{0:08}".format(n + 100)
    )


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    prefecture = "京都府"
    municipalities = "京都市東山区"
    house_no = "清水"
    other = "1-294"
    post_no = factory.Sequence(lambda n: "{0:07}".format(n + 100))
