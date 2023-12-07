from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Tem como função demonstrar para nós quais produtos temos disponiveis no cart
    Não vai ter que ficar atualizando no frontend diretamente

    """ 
    product_image = models.ImageField(null = True, blank = True)
    # Imagem do produto
    product_name = models.CharField(max_length = 40)
    # Nome do produto
    product_description = models.CharField(max_length = 200)
    # Descrição do produto
    product_date_insertion = models.DateTimeField(auto_now = True)
    # Toda vez que alterar esse field, vai marcar a última data de alteração
    # Essencial para fazer aquela mecanica de última data de alteração do preço
    product_price = models.FloatField()
    # Preço do produto


    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url
    # Faz com que possomos utilizarmos disso como se fosse um atributo, nesse caso
    # Cria-se um atributo imageURL, para se acessar com mais facilidade na class product direto
    # E também para evitar erros 500 caso a imagem não seja renderizada


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

class Order(models.Model):
    """
    Traz as informações dos pedidos ,qual produto foi escolhido, que o usuario fez o pedido
    Data da pedido, se foi finalizado
    
    """
    user_id  = models.ForeignKey(User, on_delete = models.SET_NULL, null = True,blank = True)
    # One to many relationship, um usuario pode fazer múltiplos pedidos
    # Padrão estabelecido se for chave para outro dataset, vai ter a palavra id
    order_date = models.DateField(auto_now_add = True)
    # Marca quando um pedido foi criado
    status_of_order = models.BooleanField(default = False,null = True, blank = False)
    # Marca verdadeira ou falso,  se ele tiver sido finalizado ou não
    transaction_id = models.DateTimeField(auto_now_add=False,null = True)
    # Acho que vou usar isso para observações do cliente

    @property
    def table_total_price(self):
        """
        Isso daki serve para destacar o total de preço que os pedidos tem
        
        """
        orderitem = self.orderitem_set.all()
        table_total_price = sum([item.row_price for item in orderitem])
        if not table_total_price:
            return 0
        return table_total_price

    @property
    def table_total_quantity(self):
        """
        Isso daki serve para destacar a quantidade total de pedidos no carrinho 
        
        """
        orderitems = self.orderitem_set.only('quantity')
        table_total_quantity = sum([item.quantity for item in orderitems])
        if not table_total_quantity:
            return 0
        return table_total_quantity

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = "Orders"

class OrderItem(models.Model):
    """
    Um pedido pode conter múltiplos sub-produtos, logo esse model vai guardar os itens selecionados

    """
    product_id = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
    # One to one relationship - Um item - Um producot
    order_id = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    # One to many relationship - O pedido pode ter múltiplos itens dentro dele
    quantity = models.IntegerField(default = 0,null = True,blank = True)
    # Marca a quantidade de um certo produto
    date_added_order = models.DateTimeField(auto_now_add=True)
    # Marca quando o item foi acrescentado

    @property
    def row_price(self):
        """
        Isso daki serve para destacar o preço do pedido multiplicado pela quantidade de itens pedidos
        Por linha
        
        """
        try:
            row_price = self.product_id.product_price * self.quantity
        except:
            row_price = 0
        return row_price


    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = "OrderItems"

class ShippingInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete =  models.SET_NULL, null = True)
    # One to many relationship, um usuario pode ter múltiplos pedidos em endereços diferentes
    order_id = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    # One to One - Um pedido tem somente um endereço
    postalcode = models.CharField(max_length=14,null = False)
    # CEP - Aviso - Disponibilizar mecanica de consulta de API
    address = models.CharField(max_length = 200,null = False)
    city = models.CharField(max_length = 200,null = False)
    state = models.CharField(max_length = 200,null = False)
    # Informaçoes de endereço
    date_added_shipping = models.DateTimeField(auto_now_add=True)
    # Marca quando o endereço foi acrescentado

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'ShippingInfo'
        verbose_name_plural = "ShippingInfos"


    
# Create your models here.
