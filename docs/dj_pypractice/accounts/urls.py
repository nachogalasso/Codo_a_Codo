# Aquí vamos a colocar el import de las url y los path, con el fin de que al colocar las direcciones web en el
# navegador se utilice esta ruta y no la externa.
from django.urls import path

# importamos nuestra views.py para que pueda utilizar las functions. El . significa que tome de la base del
# proyecto
from . import views

# No olvidar agregar los urlpatterns de nuestros paths
urlpatterns = [
    # Aquí estamos llamando a las functions que se encuentran en views.py
    path('',views.home),
    path('products/',views.products),
    path('customers/',views.customers),
]
