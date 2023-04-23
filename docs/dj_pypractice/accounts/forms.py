from django.forms import ModelForm
# importamos los forms para poder darle formato a nuestro formulario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class CustomForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
# Ahora creamos nuestro formulario para los usuarios
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']