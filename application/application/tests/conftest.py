import pytest
from django.core.management import call_command
from pytest_bdd import given, parsers, then, when
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "fixture.json")


@pytest.fixture
def login_management():
    return {
        "employee_number": "00000001",
        "password": "test",
    }


@pytest.fixture
def login_general():
    return {
        "employee_number": "00000002",
        "password": "test",
    }


@pytest.fixture
def login_part_time():
    return {
        "employee_number": "00000003",
        "password": "test",
    }


@pytest.fixture
def email_data():
    return {
        "email": "test_user_01@test.com",
    }


@pytest.fixture
def client(scope="session"):
    return APIClient()


# @given("APIClientを生成", target_fixture="client")
# def client(db):
#     return APIClient()


# @then("レスポンスのステータスが200")
# def response_status_code_200(response):
#     assert response.status_code == status.HTTP_200_OK


# @when("GET通信を実施", target_fixture="response")
# def get(client, url):
#     return client.get(url, format="json")


@when("POST通信を実施", target_fixture="response")
def patch(client, url, data):
    return client.post(url, data=data, format="json")


@when("PATCH通信を実施", target_fixture="response")
def patch(client, url, data):
    return client.patch(url, data=data, format="json")


@when("DELETE通信を実施", target_fixture="response")
def delete(client, url, data):
    return client.delete(url, data=data, format="json")


# @then("期待通りのJSONが返却されていること")
# def json(response, expected):
#     assert response.json() == expected
