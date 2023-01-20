from django.db import models
from django.contrib.auth.models import User
# Django, já tem criado um modelo proprio para usuários


class Address(models.Model):    
    datetime = models.DateTimeField(auto_now_add = True)
    address = models.CharField(max_length = 100)
    number = models.PositiveIntegerField(default = 0)
    complement = models.CharField(max_length = 50)
    author = models.ForeignKey(User,null = True, on_delete = models.SET_NULL)
    class Meta:
        verbose_name_plural = 'Address'
        # Essa classe só serve para garantir que fique bonitinho na admin page



# Create your models here.
