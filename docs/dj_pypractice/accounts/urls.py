# Aquí vamos a colocar el import de las url y los path, con el fin de que al colocar las direcciones web en el
# navegador se utilice esta ruta y no la externa.
from django.urls import path

# importamos nuestra views.py para que pueda utilizar las functions. El . significa que tome de la base del
# proyecto
from . import views

# No olvidar agregar los urlpatterns de nuestros paths
urlpatterns = [
    # añadimos las rutas para registro y login
    path('register/', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutPage'),
    # Aquí estamos llamando a las functions que se encuentran en views.py
    path('',views.home, name="home"),
    path('products/',views.products, name="products"),
    path('customers/<str:pk_test>/',views.customers, name="customers"),
    
    path('userpage/',views.userPage, name="user-page"),
    path('account/',views.accountSettings, name="account"),
    
    
    # Creamos el path para nuestro form de order
    # path('create_order/',views.createOrder, name="create_order"),
    # Ahora le vamos a agregar el id del cliente para tener las órdenes no desde los productos, sino desde los clieentes
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    # Creamos el path para el update de un producto
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # Creamos el path para el template del delete de un producto
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
