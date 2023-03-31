# No olvidar que antes de hacer el filter tenemos que instalar pip install django-filter y luego colocarlo en
# el archivo settings.py dentro de installed apps el comando 'django_filters',
# Vamos a usar ORDER (de models.py) para poder crear nuestro modelo de filtro para la busqueda de los datos.
import django_filters
# Para hacer nuestro filtro más personalizado importamos algunas variables
from django_filters import DateFilter, CharFilter

from .models import *
# importamos todo para no tener inconvenientes.
# Vamos a crear una nueva clase para nuestro filtro
class OrderFilter(django_filters.FilterSet):
    #Ahora creamos nuestros filtros de busqueda
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    # Ahora que agregamos el CharFilter podemos hacer la busqueda o filtro a traves del note
    note = CharFilter(field_name='note', lookup_expr='icontains')
    #creamos otra clase Meta, que va a necesitar minimamente 2 atributos
    class Meta:
        model = Order
        # Ahora le indicamos los campos que queremos utilizar
        fields = '__all__'
        # Creamos una variable exclude en la cual le indicamos los variables que no queremos utilizar
        exclude = ['customer', 'date_created']