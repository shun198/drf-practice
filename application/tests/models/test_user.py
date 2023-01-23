from django.db import DataError, IntegrityError
from django.test import TransactionTestCase

from application.models import User


class TestUser(TransactionTestCase):
    fixtures = ["fixture.json"]
    model = User
