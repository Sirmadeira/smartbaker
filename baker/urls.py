from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'baker-home'),
    path('about/',views.about, name = 'baker-about'),
]