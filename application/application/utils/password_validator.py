import re

from rest_framework.exceptions import ValidationError


class PasswordValidator:
    def validate(self, password, user=None):
        REX = r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~!@#$%^&*_\-+=`|(){}\[\]:;\"\'<>,.?/]).{8,64}"
        result = re.fullmatch(REX, password)
        if not result:
            raise ValidationError(
                "パスワードは次の4種類全てを含めた上で8文字以上、64文字以下にしてください。半角英数字・記号(!@#$%+-=)"
            )
