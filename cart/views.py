from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
import orjson
# Biblioteca para descarregamento de json


def products(request):
    """

    View utilizada para demonstrar os produtos

    """
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(user_id = customer, status_of_order = False)
        items = order.orderitem_set.all()
        cartitems = order.table_total_quantity
    else:
        cartitems = 0
    # Repassando para css do carrinho

    products = Product.objects.all()
    context = {'title':'Menu',
                'products':products,
                'cartitems':cartitems}    

    return render(request=request,template_name='cart/products.html',context = context)

@login_required
def middlecart(request):
    """

    View utilizada para meio de funil

    """
    customer = request.user
    # Nesse caso o cliente seria o objeto user a linha por assim dizer
    order, created = Order.objects.get_or_create(user_id = customer, status_of_order = False)
    # Aqui estamos verificando se o pedido(Order) já existe, se sim só tamos passando os fields.
    # Se não estamos criando o pedido do user pela primeira vez
    items = order.orderitem_set.all()
    # Nos somos capazes, de obter os "items filhos" do pedido, acessando o filho como um atributo em minusculo e acrescentando a keyword _set
    # E consiguimos fazer oque quisermos com eles, nesse caso estamos pegando todos eles
    cartitems = order.table_total_quantity

    context = {'title':'Meio de Carrinho',
            'items':items,
            'order':order,
            'cartitems':cartitems}    
        
    return render(request=request,template_name='cart/middlecart.html',context = context)

@login_required
def checkout(request):
    """

    View utilizada para obter endereço e finalizar o pedido

    """

    customer = request.user
    # Nesse caso o cliente seria o objeto user a linha por assim dizer
    order, created = Order.objects.get_or_create(user_id = customer, status_of_order = False)
    # Aqui estamos verificando se o pedido(Order) já existe, se sim só tamos passando os fields.
    # Se não estamos criando o pedido do user pela primeira vez
    items = order.orderitem_set.all()
    # Nos somos capazes, de obter os "items filhos" do pedido, acessando o filho como um atributo em minusculo e acrescentando a keyword _set
    # E consiguimos fazer oque quisermos com eles, nesse caso estamos pegando todos eles
    cartitems = order.table_total_quantity
    # Essa varivave esta sendo chaamda no contexto múltiplas vezes depois fazer rest api

    context = {'title':'Meio de Carrinho',
            'items':items,
            'order':order,
            'cartitems':cartitems}  

    return render(request=request,template_name='cart/checkout.html',context = context)

@login_required
def updateitem(request):
    """
    Função utilizada para passar os dados obtido pelo cart.js
    para o backend esse carinha que vai receber os dados dos items

    """
    if request.method == 'POST':
        data = orjson.loads(request.body)
        # Recebendo POST request do frontend
        print(data)
        productId = data['productId']
        # Id do produto selecionado
        action = data['action']
        # Action = Ação que o user fez
        print('Produto clicado', productId)
        print('Ação feita', action)
        # Variaveis importontes a serem carregadas

        customer = request.user
        # Obtendo o usuario
        product = Product.objects.get(id = productId)
        # Obtendo informações gerais do produto 
        order, created = Order.objects.get_or_create(user_id = customer, status_of_order = False)
        # Verificando o pedido dele ou criando um pedido para o user
        orderitem, created = OrderItem.objects.get_or_create(order_id = order, product_id = product )
        # Verificando os items dele ou criando
        
        if action  == 'add':
            orderitem.quantity = (orderitem.quantity + 1)
        elif action  == 'remove':
            orderitem.quantity = (orderitem.quantity - 1)
        
        orderitem.save()
        # Salvando o valor repassado no item de acordo com o botao do front end
        if orderitem.quantity <= 0:
            orderitem.delete()
        # Deletando quando um pedido está vazio ou meno do que 0
        
    return JsonResponse('Item foi adicionado', safe = False)
    # Aviso não mexer nesse retorno

@login_required
def processorder(request):
    return JsonResponse('Pagamento concluido', safe = False)
