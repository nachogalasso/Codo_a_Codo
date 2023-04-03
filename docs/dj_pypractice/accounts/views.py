from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# django default registration form
from django.contrib.auth.forms import UserCreationForm

# Añadimos mensajes al login
from django.contrib import messages
# Ahora importamos el autentificador de usuario
from django.contrib.auth import authenticate, login, logout
# Unos decorados para que no se vean el login del usuario en otros templates
from django.contrib.auth.decorators import login_required

# Create your views here.
# vamos a tener que importar todos los modelos para poder usarlos en la aplicacion
from .models import *
# traemos nuestro formulario para que se pueda renderizar el template
from .forms import OrderForm, CreateUserForm
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
# Añadimos las web para registro y login
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                # aqui colocamos el mensaje de creacion de usuario, recordar que tenemos que traer el usuario
                # del formulario para poder colocarlo en el mensaje. Luego en el template del login es donde
                # tenemos que colocar nuestro mensaje
                user = form.cleaned_data.get('username')
                messages.success(request, 'Tu usuario: ' + user + ' ha sido creado con éxito')
                return redirect('loginPage')
            
        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password1 = request.POST.get('password')
            
        # ahora usamos el authenticate para validar el usuario y contraseña
            user = authenticate(request, username=username, password=password1)
        # tenemos que chequear que el usuario esté ahí antes de enviarlo
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Usuario o contraseña incorrecta')
                return render(request, 'accounts/login.html')
                
        context = {}
        return render(request, 'accounts/login.html', context)

# Para lograr el logout del usuario tendremos que crear una function
def logoutUser(request):
    logout(request)
    return redirect('loginPage')

# Para los decoradores empieza a tener relevancia el simbolo @ y luego la acción que queremos que se ejecute
# lo tengo que colocar en cada vista que quiera que tenga restricción de usuario
@login_required(login_url='loginPage')
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


@login_required(login_url='loginPage')
def products(request):
    # Ahora aqui vamos a poder usar los modelos de productos para renderizarlos en los templates. Almacenamos toda
    # la base de datos en una variable 'products', así la podemos pasar en el template
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products});


@login_required(login_url='loginPage')
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

@login_required(login_url='loginPage')
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

@login_required(login_url='loginPage')
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


@login_required(login_url='loginPage')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)

# Estoy en el video 15 User Role Based permissions