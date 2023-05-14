import pytest

from application.serializers.customer import AddressSerializer, CustomerSerializer
from application.tests.factories.customer import AddressFactory


@pytest.fixture
def customer_data():
    """顧客のインプットデータ"""

    return {
        "kana": "オオサカタロウ",
        "name": "大阪太郎",
        "birthday": "1992-01-06",
        "phone_no": "08011112222",
        "address": AddressFactory().id,
    }


@pytest.fixture
def address_data():
    """住所のインプットデータ"""

    return {
        "prefecture": "京都府",
        "municipalities": "京都市東山区",
        "house_no": "清水",
        "other": "1-294",
        "post_no": "6050862",
    }


@pytest.mark.django_db
def test_validate_customer_data(customer_data):
    """customerのデータがバリデーションエラーにならない"""
    serializer = CustomerSerializer(data=customer_data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_phone_no_length_cannot_be_8_or_shorter(customer_data):
    """customerのphone_noが10文字以下のためバリデーションエラーになる"""
    customer_data["phone_no"] = "080" + "1" * 7
    serializer = CustomerSerializer(data=customer_data)
    assert not serializer.is_valid()


@pytest.mark.django_db
def test_validate_address_data(address_data):
    """addressのデータがバリデーションエラーにならない"""
    serializer = AddressSerializer(data=address_data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_post_no_length_cannot_be_6_or_shorter(address_data):
    """addressのpost_noが6文字以下のためバリデーションエラーになる"""
    address_data["post_no"] = "1" * 6
    serializer = AddressSerializer(data=address_data)
    assert not serializer.is_valid()
