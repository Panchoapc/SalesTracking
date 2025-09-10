from rest_framework import serializers
from models import Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['rut', 'company_name', 'shipping_address']