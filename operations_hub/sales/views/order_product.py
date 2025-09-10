from rest_framework import permissions, viewsets
from serializers import OrderProductSerializer
from models import OrderProduct

class OrderProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrderProducts to be viewed or edited.
    """
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    permission_classes = [permissions.IsAuthenticated]