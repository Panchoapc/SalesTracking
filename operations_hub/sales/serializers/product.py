from rest_framework import serializers
from models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['brand', 'product_type', 'price']