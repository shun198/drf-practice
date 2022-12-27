from django.urls import path, include
from rest_framework_nested import routers

from application.views import UserViewSet, LoginViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"", LoginViewSet, basename="login")

urlpatterns = [
    path(r"", include(router.urls)),
]
