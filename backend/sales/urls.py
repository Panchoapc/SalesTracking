from django.urls import include, path
from rest_framework import routers

from sales import views

router = routers.DefaultRouter()
router.register(r'client', views.ClientViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order_product', views.OrderProductViewSet)
router.register(r'sales_order', views.SalesOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]