from pytest_bdd import given, scenarios, then, when
from rest_framework import status
from rest_framework.test import APIClient


scenarios(
    "features/health_check.feature",
)


@given("APIClientを生成", target_fixture="client")
def client(db):
    return APIClient()


@given("ヘルスチェックAPIのURL", target_fixture="url")
def health_check_url():
    return "/api/health/"


@given("ヘルスチェック成功時のJSONを設定", target_fixture="expected")
def health_check_expected():
    return {"msg": "pass"}


@when("GET通信を実施", target_fixture="response")
def get(client, url):
    return client.get(url, format="json")


@then("レスポンスのステータスが200")
def response_status_code_200(response):
    assert response.status_code == status.HTTP_200_OK


@then("期待通りのJSONが返却されていること")
def json(response, expected):
    assert response.json() == expected
