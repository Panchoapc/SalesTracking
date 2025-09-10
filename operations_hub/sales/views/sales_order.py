from rest_framework import permissions, viewsets
from sales.serializers import SalesOrderSerializer
from sales.models import SalesOrder

class SalesOrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SalesOrders to be viewed or edited.
    """
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    permission_classes = [permissions.IsAuthenticated]