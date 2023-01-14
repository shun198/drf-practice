import pytest


def login(client, login_authority):
    """ログイン処理
    Args:
        client: APIClient
        login_authority[dict]:ログイン権限
    """
    client.login(
        username=login_authority["employee_number"],
        password=login_authority["password"],
    )
