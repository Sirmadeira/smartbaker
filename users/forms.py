from django import  forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    #https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username/
    # Como depois substituir ele
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']



class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password1']
