from rest_framework.test import APIClient
from rest_framework import status


class TestHealthCheck:
    client = APIClient()
    url = "/api/health/"

    def test_health_check_returns_200(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"msg": "pass"}
