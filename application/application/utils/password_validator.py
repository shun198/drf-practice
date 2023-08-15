import re

from rest_framework.exceptions import ValidationError


class PasswordValidator:
    def validate(self, password, user=None):
        REX = r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~!@#$%^&*_\-+=`|(){}\[\]:;\"\'<>,.?/]).{8,64}"
        result = re.fullmatch(REX, password)
        if not result:
            raise ValidationError("英大小文字、数字、または特殊文字が含まれていません")
