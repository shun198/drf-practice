from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from application.models import Customer
from application.serializers.customer import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
