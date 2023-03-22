from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# vamos a tener que importar todos los modelos para poder usarlos en la aplicacion
from .models import *

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
    # Como aquí tenemos las ordenes y los clientes vamos renderizar ambas bases
    orders = Order.objects.all()
    customers = Customer.objects.all()
    #  como vamos a pasar más de una base de datos, creamos un diccionario externo y allí colocamos las bases
    context = {'orders': orders, 'customers': customers}
    return render(request, 'accounts/dashboard.html', context);

def products(request):
    # Ahora aqui vamos a poder usar los modelos de productos para renderizarlos en los templates. Almacenamos toda
    # la base de datos en una variable 'products', así la podemos pasar en el template
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products});

def customers(request):
    return render(request, 'accounts/customers.html')