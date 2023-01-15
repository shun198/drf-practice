from rest_framework import serializers

from .models import User


class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "employee_number", "username", "email", "role"]
        read_only_fields = ["id", "created_at", "updated_at"]


class LoginSerializer(serializers.ModelSerializer):
    employee_number = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["employee_number", "password"]


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
