import pytest
from django.core import mail
from rest_framework.test import APIClient


@pytest.mark.django_db()
class TestInviteUser:
    # 今回は該当するエンドポイントへテストを行いたいのでAPIClientを使用します
    client = APIClient()
    url = "/api/users/send_invite_user_mail/"

    def test_management_user_can_send_invite_user_email(
        self, management_user, email_data
    ):
        """招待メールを送信できたかテスト

        Args:
            management_user (fixture): ログイン用の管理者ユーザ
            email_data (fixture): send_invite_user_mail/へPOSTリクエストを送るためのデータ
        """
        self.client.login(username=management_user[0], password=management_user[1])
        response = self.client.post(self.url, email_data, format="json")
        assert response.status_code == 200
        # メールを一通受信したことを確認
        assert len(mail.outbox) == 1
        # メールの件名が正しいことを確認
        assert mail.outbox[0].subject == "ようこそ"
        # メールの送信元が正しいことを確認
        assert mail.outbox[0].from_email == "example@mail.com"
        # 宛先は複数存在するため、toは配列になります
        # 今回はtest_user_01@test.comのみのため、to[0]と指定します
        # メールの送信先が正しいことを確認
        assert mail.outbox[0].to[0] == email_data["email"]
