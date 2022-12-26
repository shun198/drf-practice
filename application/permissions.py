from rest_framework.permissions import BasePermission
from .models import User


# アルバイトユーザー
# アルバイトユーザができることは一般ユーザ、管理ユーザ、スーバーユーザ共にできるためTrueを返す
# それ以外はFalseを返す
class IsPartTimeUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.user and request.user.is_authenticated:
            # アルバイトユーザーにできて一般ユーザーと管理ユーザーにできないことはないので管理ユーザーもTrue
            if (
                request.user.role == User.Role.PART_TIME
                or request.user.role == User.Role.GENERAL
                or request.user.role == User.Role.MANAGEMENT
            ):
                return True
        return False

# 一般ユーザー
# 一般ユーザができることは管理ユーザ、スーバーユーザ共にできるためTrueを返す
# それ以外はFalseを返す
class IsGeneralUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.user and request.user.is_authenticated:
            # 一般ユーザー、管理ユーザーともにTrueになるよう設定
            if (
                request.user.role == User.Role.GENERAL
                or request.user.role == User.Role.MANAGEMENT
            ):
                return True
        return False


# 管理ユーザー
# 管理ユーザができることはスーパーユーザ共にできるためTrueを返す
# それ以外はFalseを返す
class IsManagementUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.user and request.user.is_authenticated:
            if request.user.role == User.Role.MANAGEMENT:
                return True
        return False

# スーパーユーザー
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
