from django.shortcuts import render


def home(request):
    context  = {'title': 'Home'}
    return render(request=request,template_name='baker/home.html',context = context)

def about(request):
    context = {'title':'Sobre'}
    return render(request=request,template_name='baker/about.html',context = context)

# Create your views here.
