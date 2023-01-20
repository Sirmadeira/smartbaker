from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def products(request):
    """

    View utilizada para registrar o pedido

    """
    context = {'title':'Menu'}    

    return render(request=request,template_name='cart/products.html',context = context)

@login_required
def middlecart(request):
    """

    View utilizada para registrar o pedido

    """
    context = {'title':'Meio de Carrinho'}    

    return render(request=request,template_name='cart/middlecart.html',context = context)

@login_required
def checkout(request):
    """

    View utilizada para registrar o pedido

    """
    context = {'title':'Finalizar Pedido'}    

    return render(request=request,template_name='cart/checkout.html',context = context)
