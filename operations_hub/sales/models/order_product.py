from django.db import models

ORDER_STATUS = ["Pendiente", "Completada", "Cancelada"]
STATUS_CHOICES = [(state, state) for state in ORDER_STATUS]

class OrderProduct(models.Model):
    product = models.ForeignKey('sales.Product', on_delete=models.CASCADE)
    sales_order = models.ForeignKey('sales.SalesOrder', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()