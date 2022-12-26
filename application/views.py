from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import User
from .permissions import (IsGeneralUser, IsManagementUser, IsPartTimeUser,
                          IsSuperUser)
from .serializers import LoginSerializer, UserSerilaizer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ["login","logout"]:
            return LoginSerializer
        else:
            return UserSerilaizer

    @action(detail=False, methods=["POST"], permission_classes=[])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        employee_number = serializer.validated_data.get("employee_number")
        password = serializer.validated_data.get("password")
        user = authenticate(employee_number=employee_number, password=password)
        if not user:
            return JsonResponse(data={"msg": "either employee number or password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            login(request, user)
            return HttpResponse()

    @action(methods=["POST"], detail=False, permission_classes=[])
    def logout(self, request):
        logout(request)
        return HttpResponse()

    # get_permissionsメソッドを使えば前述の表に従って権限を付与できる
    def get_permissions(self):
        if self.action in ["update", "partial_update"]:
            permission_classes = [IsManagementUser]
        if self.action == "create":
            permission_classes = [IsGeneralUser]
        elif self.action == "destroy":
            permission_classes = [IsSuperUser]
        elif self.action == ["list","retrieve"]:
            permission_classes = [IsPartTimeUser]
        elif self.action in ["login"]:
            # 全てのユーザを許可しないとログインできない
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
