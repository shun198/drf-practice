from pytest_bdd import given, scenarios

scenarios(
    "./features/health_check.feature",
)


@given("ヘルスチェックAPIのURL", target_fixture="url")
def health_check_url():
    return "/api/health/"


@given("ヘルスチェック成功時のJSONを設定", target_fixture="expected")
def health_check_expected():
    return {"msg": "pass"}
