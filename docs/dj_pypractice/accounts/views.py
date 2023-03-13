from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# vamos a tener que crear una urls.py dentro de la carpeta de nuestro proyecto.
# def home(request):
#     return HttpResponse('Aquí tenemos que colocar al url de nuestra web')

# def products(request):
#     return HttpResponse('Productos')

# def customers(request):
#     return HttpResponse('Customers')

""" Ahora que tenemos los templates tendremos que modificar las functions para que ahora linkeen a nuestros templates. Por lo tanto la def pasa a ser la siguiente

def home(request):
    return render(request, 'accounts/dashboard.html')
    Aqui lo que estamos pasando es el comando request y le estamos indicando la ruta donde se encuentra nuestro template
    
"""

def home(request):
    return render(request, 'accounts/dashboard.html');

def products(request):
    return render(request, 'accounts/products.html');

def customers(request):
    return render(request, 'accounts/customers.html')