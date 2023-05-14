import factory

from application.models import Address


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    prefecture = "京都府"
    municipalities = "京都市東山区"
    house_no = "清水"
    other = "1-294"
    post_no = factory.Sequence(lambda n: "{0:07}".format(n + 100))
