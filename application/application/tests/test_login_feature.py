from pytest_bdd import given, parsers, scenarios, then, when
from rest_framework import status
from rest_framework.test import APIClient

from application.models import User
from application.tests.factories.user import UserFactory

scenarios(
    "features/login.feature",
)


@given("APIClientを生成", target_fixture="client")
def client(db):
    return APIClient()


@given("ログインAPIのURL", target_fixture="url")
def login_url():
    return "/api/login/"


@given(parsers.parse("{permission}権限のユーザ"), target_fixture="user")
def user(permission):
    role = User.Role[permission].value
    return UserFactory(role=role)


@given("ログイン用のJSONを設定", target_fixture="data")
def login_data(user):
    return {
        "employee_number": user.employee_number,
        "password": "test",
    }


@given(
    parsers.parse("{permission}権限でログイン成功時のJSONを設定"), target_fixture="expected"
)
def login_success_expected(permission):
    return {"role": permission}


@when("POST通信を実施", target_fixture="response")
def post(client, url, data):
    return client.post(url, data=data, format="json")


@then("レスポンスのステータスが200")
def response_status_code_200(response):
    assert response.status_code == status.HTTP_200_OK


@then("期待通りのJSONが返却されていること")
def json(response, expected):
    assert response.json() == expected


@given("社員番号またはパスワードが間違っているJSONの設定", target_fixture="data")
def wrong_login_data():
    return {
        "employee_number": "99999999",
        "password": "wrong_password",
    }


@given("ログイン失敗時のJSONを設定", target_fixture="expected")
def login_failure_expected():
    return {"msg": "either employee number or password is incorrect"}


@then("レスポンスのステータスが400")
def response_status_code_400(response):
    assert response.status_code == status.HTTP_400_BAD_REQUEST
