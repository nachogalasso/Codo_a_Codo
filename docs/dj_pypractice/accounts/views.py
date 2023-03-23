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
    
    # traemos el total de los clientes y las ordenes
    total_customers = customers.count()
    total_orders = orders.count()
    
    # Ahora creamos un filtro que nos muestre las ordenes segun sus status
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    #  como vamos a pasar más de una base de datos, creamos un diccionario externo y allí colocamos las bases
    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending, 'total_customers': total_customers}
    return render(request, 'accounts/dashboard.html', context);

def products(request):
    # Ahora aqui vamos a poder usar los modelos de productos para renderizarlos en los templates. Almacenamos toda
    # la base de datos en una variable 'products', así la podemos pasar en el template
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products});

# Aqui tenemos que pasar también el id del cliente que queremos renderizar, lo vamos a indentificar como pk
def customers(request, pk_test):
    customers = Customer.objects.get(id=pk_test)
    
    # traemos las ordenes de los clientes
    orders = customers.order_set.all() 
    # traemos el total de las ordenes
    orders_count = orders.count()
    
    context = {'customers': customers, 'orders': orders, 'orders_count': orders_count}
    return render(request, 'accounts/customers.html', context)