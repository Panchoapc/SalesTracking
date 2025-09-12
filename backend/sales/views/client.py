from rest_framework import permissions, viewsets
from sales.serializers import ClientSerializer
from sales.models import Client

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Clients to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]