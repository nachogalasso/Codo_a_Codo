from django.contrib import admin

# from .models import Customer
# para importar todas las tablas podemos utilizar el siguiente comando
from .models import *
# Register your models here.

admin.site.register(Customer)
# Ahora aquí tenemos que agregar un comando por cada tabla
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)