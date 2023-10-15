from django.urls import path
from . import views


urlpatterns = [
    path('products/',views.products,name = 'cart-products'),
    path('middlecart/',views.middlecart,name = 'cart-middlecart'),
    path('checkout/',views.checkout,name = 'cart-checkout'),
    path('updateitem/',views.updateitem,name = 'cart-updateitem'),
    path('processorder/',views.processorder,name='cart-processorder')
]