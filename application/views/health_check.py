from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    """ヘルスチェックのテスト

    Args:
        request : リクエスト

    Returns:
        dict: {"msg": "pass"}のjsonレスポンスとステータスコード200
    """
    return JsonResponse(data={"msg": "pass"}, status=200)
