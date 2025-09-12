from django.db import models


class Client(models.Model):

    rut = models.CharField(blank=False, unique=True)
    company_name = models.CharField() # Razon Social
    shipping_address = models.CharField()
