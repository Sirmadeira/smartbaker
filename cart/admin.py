from django.contrib import admin
from .models import Product,Order,OrderItem,ShippingInfo


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingInfo)
# Register your models here.
