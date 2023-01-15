from django.urls import include, path
from rest_framework_nested import routers

from application.views import health_check, login, user

router = routers.DefaultRouter()
router.register(r"users", user.UserViewSet, basename="user")
router.register(r"", login.LoginViewSet, basename="login")

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"health/", health_check.health_check, name="health_check"),
]
