import pytest
from django.db.utils import DataError, IntegrityError

from application.models import User
from application.tests.factories.user import UserFactory


@pytest.mark.django_db
def test_username_length_can_be_150():
    """usernameの長さの最大値が150文字"""


@pytest.mark.django_db
def test_username_length_cannot_be_151_or_more():
    """usernameの長さの最大値が150文字"""

    with pytest.raises(DataError):
        UserFactory(username="a" * 151)
