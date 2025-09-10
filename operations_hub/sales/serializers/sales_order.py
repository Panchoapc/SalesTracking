from rest_framework import serializers
from models import SalesOrder

class SalesOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['order_number', 'order_status', 'buyer', 'item', 'total_price', 'additional_info']