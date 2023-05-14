import pytest
from datetime import datetime, timedelta
from django.db.utils import DataError, IntegrityError

from application.models import User, Customer, Address
from application.tests.factories.customer import CustomerFactory, AddressFactory


def get_customer(id):
    return Customer.objects.get(pk=id)


def get_address(id):
    return Address.objects.get(pk=id)


@pytest.mark.django_db
def test_kana_length_can_be_255():
    """カナ氏名の長さの最大値が255文字"""
    kana = "a" * 255
    customer = CustomerFactory(kana=kana)
    assert get_customer(customer.id).kana == kana


@pytest.mark.django_db
def test_name_length_can_be_255():
    """カナ氏名の長さの最大値が255文字"""
    name = "a" * 255
    customer = CustomerFactory(name=name)
    assert get_customer(customer.id).name == name


@pytest.mark.django_db
def test_birthday_can_be_date():
    """カナ氏名の長さの最大値が255文字"""
    birthday = datetime.now().date() - timedelta(days=365 * 20)
    customer = CustomerFactory(birthday=birthday)
    assert get_customer(customer.id).birthday == birthday
