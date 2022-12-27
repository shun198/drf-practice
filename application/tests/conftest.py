import pytest

from django.core.management import call_command


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "fixture.json")


@pytest.fixture
def management_user(db):
    return ("00000001", "test")


@pytest.fixture
def email_data():
    return {
        "email": "test_user_01@test.com",
    }
