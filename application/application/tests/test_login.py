import pytest
from rest_framework import status
from rest_framework.test import APIClient

from application.tests.common_method import login


@pytest.mark.django_db()
class TestUserSerializer:
    class TestLoginUser:
        """ログイン処理のテスト"""

        client = APIClient()
        url = "/api/login/"

        def test_management_user_login(self, login_management):
            """管理者ユーザで正常にログインできることをテスト"""
            response = self.client.post(
                self.url, login_management, format="json"
            )
            assert response.status_code == status.HTTP_200_OK
            assert response.json() == {"role": "MANAGEMENT"}

        def test_general_user_login(self, login_general):
            """一般ユーザで正常にログインできることをテスト"""
            response = self.client.post(self.url, login_general, format="json")
            assert response.status_code == status.HTTP_200_OK
            assert response.json() == {"role": "GENERAL"}

        def test_part_time_user_login(self, login_part_time):
            """アルバイトユーザで正常にログインできることをテスト"""
            response = self.client.post(
                self.url, login_part_time, format="json"
            )
            assert response.status_code == status.HTTP_200_OK
            assert response.json() == {"role": "PART_TIME"}

        def test_user_logins_with_incorrect_password(self, login_management):
            """間違ったパスワードでログインできないことをテスト"""
            login_management["password"] = "test6789"
            response = self.client.post(
                self.url, login_management, format="json"
            )
            assert response.status_code == status.HTTP_400_BAD_REQUEST
            assert response.json() == {
                "msg": "either employee number or password is incorrect"
            }

        def test_user_logins_without_password(self, login_management):
            """パスワードなしでログインできないことをテスト"""
            login_management["password"] = None
            response = self.client.post(
                self.url, login_management, format="json"
            )
            assert response.status_code == status.HTTP_400_BAD_REQUEST

        def test_user_logins_without_employee_number(self, login_management):
            """社員番号なしでログインできないことをテスト"""
            login_management["employee_number"] = None
            response = self.client.post(
                self.url, login_management, format="json"
            )
            assert response.status_code == status.HTTP_400_BAD_REQUEST

        def test_user_logins_with_employee_number_that_does_not_exist(
            self, login_management
        ):
            """存在しない社員番号でログインできないことをテスト"""
            login_management["employee_number"] = "12345678"
            response = self.client.post(
                self.url, login_management, format="json"
            )
            assert response.status_code == status.HTTP_400_BAD_REQUEST

    class TestLogoutUser:
        """ログアウト処理のテスト"""

        client = APIClient()
        url = "/api/logout/"

        def test_user_logout(self, login_management):
            """正常にログアウトできることをテスト"""
            login(self.client, login_management)
            response = self.client.post(
                self.url, login_management, format="json"
            )
            assert response.status_code == status.HTTP_200_OK

        def test_user_logout_without_login(self, login_management):
            """ログインしていなくても200を返すことをテスト"""
            response = self.client.post(
                self.url, login_management, format="json"
            )
            assert response.status_code == status.HTTP_200_OK
