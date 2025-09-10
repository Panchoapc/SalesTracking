from rest_framework import serializers
from models import OrderProduct

class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['product', 'sales_order', 'price', 'quantity']