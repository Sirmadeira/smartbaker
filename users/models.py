from django.db import models
from django.contrib.auth.models import User
# Django, já tem criado um modelo proprio para usuários

class Orders(models.Model):
    AVAILABLE_PRODUCTS = (
        (1,'PÃO FRANÇÊS'),
        (2,'BOLO DO CACO'),
        (3,'PÃO ITALIANO')
    )
    
    datetime = models.DateTimeField(auto_now_add = True)
    product = models.CharField(max_length = 20,choices = AVAILABLE_PRODUCTS)
    number = models.PositiveIntegerField(default = 0)
    address = models.CharField(max_length = 100)
    complemento = models.CharField(max_length = 50)
    author = models.ForeignKey(User,null = True, on_delete = models.SET_NULL)
    class Meta:
        verbose_name_plural = 'Orders'
        # Essa classe só serve para garantir que fique bonitinho na admin page
# Create your models here.
