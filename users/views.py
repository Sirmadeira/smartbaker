from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Orders
from .forms import UserRegisterForm

def login(request):
    """
    
    View utilizada para o logi de usuários já cadastrados

    """
    context = {'title':'Login'}
    return render(request=request,template_name='users/login.html',context = context)

def register(request):
    """

    View utilizada para o cadastro de usuários

    """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Caso falhe a validação isso vai impedir o usuário de perder os dados já cadastrados
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Parabéns conta criada para {username}')
            return redirect('users-login')
        else:
            # Esse else só serve para printar a mensagem de erro se user passar por uma validação não demonstrada
            messages.error(request,'Aparentemente existe um problema!')
            context = {'title':'Cadastre','form':form}
            return render(request=request,template_name='users/register.html',context = context)

    form = UserRegisterForm()      
    context = {'title':'Cadastre','form':form}
    return render(request=request,template_name='users/register.html',context = context)

def userspace(request):
    """

    View utilizada para o espaço do cliente, ele irá ver pedidos já feitos
    e pooderá ser redirecionado para fazer novos pedidos

    """
    context = {'title':'Cadastre',
                'pedidos': Orders.objects.all()}
                
    return render(request=request,template_name='users/userspace.html',context = context)

# Create your views here.
