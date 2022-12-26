from django.urls import path, include
from rest_framework_nested import routers

from application.views import (
    UserViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path(r'', include(router.urls)),
]
