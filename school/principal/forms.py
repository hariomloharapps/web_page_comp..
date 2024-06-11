from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PrincipalUser

class PrincipalCreationForm(UserCreationForm):
    class Meta:
        model = PrincipalUser
        fields = ('username', 'email', 'password1', 'password2')



from django import forms
from .models import Principal

class PrincipalLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Principal
        fields = ['username', 'password']
