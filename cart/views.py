from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def products(request):
    """

    View utilizada para registrar o pedido

    """
    products = Product.objects.all()
    context = {'title':'Menu',
                'products':products}    

    return render(request=request,template_name='cart/products.html',context = context)

@login_required
def middlecart(request):
    """

    View utilizada para registrar o pedido

    """
    customer = request.user
    # Nesse caso o cliente seria o objeto user a linha por assim dizer
    order, created = Order.objects.get_or_create(user_id = customer, status_of_order = False)
    # Aqui estamos verificando se o pedido(Order) já existe, se sim só tamos passando os fields.
    # Se não estamos criando o pedido do user pela primeira vez
    items = order.orderitem_set.all()
    # Nos somos capazes, de obter os "items filhos" do pedido, acessando o filho como um atributo em minusculo e acrescentando a keyword _set
    # E consiguimos fazer oque quisermos com eles, nesse caso estamos pegando todos eles

    context = {'title':'Meio de Carrinho',
            'items':items,
            'order':order}    

    return render(request=request,template_name='cart/middlecart.html',context = context)

@login_required
def checkout(request):
    """

    View utilizada para registrar o pedido

    """

    customer = request.user
    # Nesse caso o cliente seria o objeto user a linha por assim dizer
    order, created = Order.objects.get_or_create(user_id = customer, status_of_order = False)
    # Aqui estamos verificando se o pedido(Order) já existe, se sim só tamos passando os fields.
    # Se não estamos criando o pedido do user pela primeira vez
    items = order.orderitem_set.all()
    # Nos somos capazes, de obter os "items filhos" do pedido, acessando o filho como um atributo em minusculo e acrescentando a keyword _set
    # E consiguimos fazer oque quisermos com eles, nesse caso estamos pegando todos eles

    context = {'title':'Meio de Carrinho',
            'items':items,
            'order':order}  

    return render(request=request,template_name='cart/checkout.html',context = context)
