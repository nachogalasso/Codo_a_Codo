# Return all custmers from a customer table
customers = Customer.objects.all()

# Return first customer in a table
customers = Customer.objects.first()

# Return last customer in a table
customers = Customer.objects.last()

# Returin single customer by name
customers = Customer.objects.get(name= 'John Doe')

# Returin single customer by id
customerById = Customer.objects.get(id=1)

# Returns all orders related to a customer (firstCustomer variable set above)
firstCustomer.order_set.all()

# Returns orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

# Returns products from products table with value of "Out Door" in category attribute
products = Product.objects.filter(category='Out Door')

# Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# Returns all products with the tag of "Sports": (Query Many to Many Fields)
productsFiltered = Product.objects.filter(tags__name='Sports')

# Returns the total count for number of time "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name='Ball').count()

# Returns total count for each product ordered
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1
        
# Returns: allOrders: { 'Ball': 1, 'Sports': 1 }


# RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    
class ChildModel(models.Model):
    parent = models.ForeingKey(ParentModel)
    name = models.CharField(max_length=100, null=True)
    
parent = ParentModel.objects.first()
#Returns all child models related to the parent
parent.childmodel_set.all()