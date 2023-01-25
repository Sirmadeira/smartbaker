from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Views de autenticacao de user
from .forms import UserRegisterForm,UserLoginForm


def register(request):
    """

    View utilizada para o cadastro de usuários

    """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Caso falhe a validação isso vai impedir o usuário de perder os dados já cadastrados
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Parabéns conta criada para {username}')
            return redirect('users-login')
        else:
            # Esse else só serve para printar a mensagem de erro se user passar por uma validação não demonstrada
            messages.error(request,'Aparentemente existe um problema!')
            context = {'title':'Cadastre','form':form}
            return render(request = request,template_name ='users/register.html',context = context)

    form = UserRegisterForm()      
    context = {'title':'Cadastre','form':form}
    return render(request = request,template_name ='users/register.html',context = context)

def login(request):
    """
    
    View utilizada para o login de usuários já cadastrados

    """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username = username, password = password)
        if user is not None:
            auth_login(request,user)
            return redirect('users-userspace')
        else:
            messages.error(request,'Usuário inválido!')
            context = {'title':'Login','form':form}
            return render(request=request,template_name='users/login.html',context = context)

    form = UserLoginForm()      
    context = {'title':'Login','form':form}
    return render(request=request,template_name='users/login.html',context = context)

    
@login_required
def logout(request):
    auth_logout(request)
    messages.warning(request,'Usuário deslogado!')
    return redirect('users-login')

@login_required
def userspace(request):
    """

    View utilizada para o espaço do cliente, ele irá ver pedidos já feitos
    e pooderá ser redirecionado para fazer novos pedidos

    """
    context = {'title':'Seus pedidos'}  
    return render(request = request,template_name ='users/userspace.html',context = context)


# Create your views here.
