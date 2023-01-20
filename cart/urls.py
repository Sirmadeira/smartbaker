from django.urls import path
from . import views


urlpatterns = [
    path('products/',views.products,name = 'cart-products'),
    path('middlecart/',views.middlecart,name = 'cart-middlecart'),
    path('checkout/',views.checkout,name = 'cart-checkout'),

]