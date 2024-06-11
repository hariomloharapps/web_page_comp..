from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import App2User

class App2UserCreationForm(UserCreationForm):
    class Meta:
        model = App2User
        fields = ('username', 'email', 'password1', 'password2')
