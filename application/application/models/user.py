import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    """システムユーザ"""

    username_validator = UnicodeUsernameValidator()

    class Role(models.IntegerChoices):
        """システムユーザのロール

        Args:
            MANAGEMENT(0): 管理者
            GENERAL(1):    一般
            PART_TIME(2):  アルバイト
        """

        MANAGEMENT = 0
        GENERAL = 1
        PART_TIME = 2

    # 不要なフィールドはNoneにすることができる
    first_name = None
    last_name = None
    date_joined = None
    groups = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_number = models.CharField(
        unique=True,
        validators=[RegexValidator(r"^[0-9]{8}$")],
        max_length=8,
        # 管理者のログイン画面で社員番号と表示される
        verbose_name="社員番号",
    )
    """社員番号"""
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    """ユーザ名"""
    email = models.EmailField(max_length=254, unique=True)
    """メールアドレス"""
    role = models.PositiveIntegerField(
        choices=Role.choices, default=Role.PART_TIME
    )
    """ロール"""
    created_at = models.DateTimeField(auto_now_add=True)
    """作成日"""
    updated_at = models.DateTimeField(auto_now=True)
    """更新日"""

    # デフォルトはusernameだが今回は社員番号を指定
    USERNAME_FIELD = "employee_number"
    # uniqueのemailとusernameを指定
    REQUIRED_FIELDS = ["email", "username"]

    class Meta:
        ordering = ["employee_number"]
        db_table = "User"

    def __str__(self):
        return self.username
