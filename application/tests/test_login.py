import pytest

from rest_framework.test import APIClient
from rest_framework import status
from application.tests.common_method import login


@pytest.mark.django_db()
class TestUserSerializer:
    class TestLoginUser:
        client = APIClient()
        url = "/api/login/"

        def test_management_user_login(self, login_management):
            response = self.client.post(self.url, login_management, format='json')
            assert response.status_code == status.HTTP_200_OK
            assert response.json() == {"role": "MANAGEMENT"}

        def test_general_user_login(self, login_general):
            response = self.client.post(self.url, login_general, format='json')
            assert response.status_code == status.HTTP_200_OK
            assert response.json() == {"role": "GENERAL"}

        def test_sales_user_login(self, login_part_time):
            response = self.client.post(self.url, login_part_time, format='json')
            assert response.status_code == status.HTTP_200_OK
            assert response.json() == {"role": "PART_TIME"}

        def test_user_logins_with_incorrect_password(self, login_management):
            login_management["password"] = "test6789"
            response = self.client.post(self.url, login_management, format='json')
            assert response.status_code == status.HTTP_400_BAD_REQUEST
            assert response.json() == {'msg': 'either employee number or password is incorrect'}

        def test_user_logins_without_password(self, login_management):
            login_management["password"] = None
            response = self.client.post(self.url, login_management, format='json')
            assert response.status_code == status.HTTP_400_BAD_REQUEST

        def test_user_logins_without_username(self, login_management):
            login_management["employee_number"] = None
            response = self.client.post(self.url, login_management, format='json')
            assert response.status_code == status.HTTP_400_BAD_REQUEST

        def test_user_logins_with_username_that_does_not_exist(self, login_management):
            login_management["employee_number"] = "12345678"
            response = self.client.post(self.url, login_management, format='json')
            assert response.status_code == status.HTTP_400_BAD_REQUEST


    class TestLogoutUser:
        client = APIClient()
        url = "/api/logout/"
        def test_user_logout(self, login_management):
            login(self.client, login_management)
            response = self.client.post(self.url, login_management, format='json')
            assert response.status_code == status.HTTP_200_OK

        def test_user_logout_without_login(self, login_management):
            response = self.client.post(self.url, login_management, format='json')
            assert response.status_code == status.HTTP_200_OK
