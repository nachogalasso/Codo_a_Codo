from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# vamos a tener que crear una urls.py dentro de la carpeta de nuestro proyecto.
def home(request):
    return HttpResponse('Aquí tenemos que colocar al url de nuestra web')

def products(request):
    return HttpResponse('Productos')

def customers(request):
    return HttpResponse('Customers')