from datetime import datetime, timedelta

import factory
from factory import Faker, Sequence, SubFactory

from application.models import Address, Customer


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    prefecture = "京都府"
    municipalities = "京都市東山区"
    house_no = "清水"
    other = "1-294"
    post_no = factory.Sequence(lambda n: "{0:07}".format(n + 100))


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    kana = Sequence(lambda n: "テストコキャク{}".format(n))
    name = Sequence(lambda n: "テスト顧客{}".format(n))
    birthday = Faker(
        "date_between_dates",
        date_start=(datetime.now().date() - timedelta(days=365 * 50)),
        date_end=(datetime.now().date() - timedelta(days=365 * 20)),
    )
    phone_no = Sequence(lambda n: f"080" + "{0:08}".format(n + 100))
    address = SubFactory(AddressFactory)
