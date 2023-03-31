from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

# Create your views here.
# vamos a tener que importar todos los modelos para poder usarlos en la aplicacion
from .models import *
# traemos nuestro formulario para que se pueda renderizar el template
from .forms import OrderForm
# Tenemos que importar los filtros para poder usarlos en la aplicacion y luego indicarlos dónde queremos que
# se rendericen y es en la function de customers
from .filters import OrderFilter

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
    
    # traemos los filtros para poder usarlos en la aplicacion en las busquedas
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    
    context = {'customers': customers, 'orders': orders, 'orders_count': orders_count, 'myFilter': myFilter}
    return render(request, 'accounts/customers.html', context)


# creamos la function del form para que django nos renderice el template order_form.html
def createOrder(request, pk):
    # Para poder crear varios formularios
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    # Ahora vamos a crear las ordenes desde los clientes
    customers = Customer.objects.get(id=pk)
    # Aqui vamos usar nuestra function de OrderForm para crear un formulario
    # form = OrderForm(initial={'customer': customers}) 
    # Ahora que creamos el OrderFormSet vamos a tener que crear una nueva instancia del formulario
    formset = OrderFormSet(instance=customers)
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('/') 
        formset = OrderFormSet(request.POST, instance=customers)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    # Ahora como context tenemos que pasar el formulario y el formset. En el template de order_form.html 
    # tenemos que pasar tambien el formset.
    # context = {'form': form}
    context = {'formset': formset}
    
    return render(request, 'accounts/order_form.html', context)

# Ahora creamos la function para poder actualizar los datos de nuestras ordenes
def updateOrder(request, pk):
    # vamos a tener que traer nuestro modelo de order
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/') 
    
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)

# Estoy en el video 14 User login and registration