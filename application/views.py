from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet

from .models import User
from .permissions import IsGeneralUser, IsManagementUser, IsPartTimeUser, IsSuperUser
from .serializers import LoginSerializer, UserSerilaizer, EmailSerializer
from .emails import send_welcome_email


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "send_invite_user_mail":
            return EmailSerializer
        else:
            return UserSerilaizer

    @action(detail=False, methods=["POST"])
    def send_invite_user_mail(self, request):
        """指定したメールアドレス宛へ招待メールを送る

        Args:
            request: リクエスト

        Returns:
            HttpResponse
        """
        serializer = self.get_serializer(data=request.data)
        # バリデーションに失敗したら400を返す
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        email = serializer.validated_data.get("email")
        # メール送信用メソッド
        send_welcome_email(email=email)
        return HttpResponse()

    # get_permissionsメソッドを使えば前述の表に従って権限を付与できる
    def get_permissions(self):
        if self.action in ["update", "partial_update", "send_invite_user_mail"]:
            permission_classes = [IsManagementUser]
        elif self.action == "create":
            permission_classes = [IsGeneralUser]
        elif self.action == "destroy":
            permission_classes = [IsSuperUser]
        elif self.action in ["list", "retrieve"]:
            permission_classes = [IsPartTimeUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["POST"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        employee_number = serializer.validated_data.get("employee_number")
        password = serializer.validated_data.get("password")
        user = authenticate(employee_number=employee_number, password=password)
        if not user:
            return JsonResponse(
                data={"msg": "either employee number or password is incorrect"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            login(request, user)
            return JsonResponse(data={"role": user.Role(user.role).name})

    @action(methods=["POST"], detail=False, permission_classes=[])
    def logout(self, request):
        logout(request)
        return HttpResponse()
