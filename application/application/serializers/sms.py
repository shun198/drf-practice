from rest_framework import serializers


class SmsSerializer(serializers.Serializer):
    """SMS用シリアライザ"""

    phone_no = serializers.CharField(max_length=11)
    message = serializers.CharField(max_length=255)
