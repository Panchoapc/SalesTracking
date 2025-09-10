from django.db import models

BRANDS = ["Pepito",
          "Cornet",
          "Cuneta"]

PRODUCT_TYPE = ["Pepito",
                "Cornet",
                "Cuneta"]

BRAND_CHOICES = [(marca, marca) for marca in BRANDS]
PRODUCT_CHOICES = [(marca, marca) for marca in BRANDS]

class Product(models.Model):
    brand = models.CharField(choices = BRAND_CHOICES, default=BRANDS[0])
    product_type = models.CharField(choices = PRODUCT_CHOICES, default=PRODUCT_TYPE[0])
    price = models.IntegerField(default=0, null=False)
