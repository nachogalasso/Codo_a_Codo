from unicodedata import category
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    # Acá es donde creamos una function para que nuestros datos se visualicen como string y no como obj
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name

    
# Ahora continuamos creando las otras tablas que nos faltan
class Product(models.Model):
    # Acá vamos a hacer lo mismo de agregar una variable para que cambie el valor mediante un select
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # Ahora referenciamos la base a la de Tag
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    # Como Status queremos que se modifique mediante un input de select vamos a crear una variable
    # que nos permita reflejar el cambio en el status de nuestra orden
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered')
    )
    # Así refenciamos a las tablas de Customer y Product
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # Le pasamos los valores de Status para poder modificarlos cuando lo necesitemos.
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    
    def __str__(self):
        return self.product.name
    
    