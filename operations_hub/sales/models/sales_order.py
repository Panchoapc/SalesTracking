from django.db import models

ORDER_STATUS = ["Pendiente", "Completada", "Cancelada"]
STATUS_CHOICES = [(state, state) for state in ORDER_STATUS]

class SalesOrder(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order_number = models.PositiveIntegerField()
    order_status = models.CharField(choices=STATUS_CHOICES)
    buyer = models.ForeignKey('sales.Client', on_delete=models.CASCADE)
    item = models.ManyToManyField(
        'sales.Product',
        through="OrderProduct"
    )
    total_price = models.PositiveIntegerField(default=0, null=False)
    additional_info = models.TextField()
