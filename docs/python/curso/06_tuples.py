# 30 Days Of Python: Day 6 - Tuples
"""Tuples
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
operator: to join two or more tuples and to create a new tuple

Creating a Tuple
Empty tuple: Creating an empty tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

A tuple is like a list but no can't change its values
"""
# Creating a Tuple
tpl = ('item1', 'item2', 'item3', 'item4', 'item5', 'item6')

# Another way to create a tuple
empty_tuple = ()
empty_tpl = tuple()
print(type(tpl))
print(type(empty_tuple))
print(type(empty_tpl))

# A tuple of fruits
fruits = ('Banana', 'Apple', 'Orange', 'Mango', 'Lemon')

# We can create a tuple with different data types
comb_tuple = ('Casa', 'house', 35, 42.5, {'age':48,'surname':'Ramirez'})
print(type(comb_tuple))
print(comb_tuple[4])

"""Tuple length
We use the len() method to get the length of a tuple.
"""
print(len(fruits))

"""Accessing Tuple Items
The tuples have the same index of the lists. Positive Indexing Similar to the list data type we use positive or negative indexing to access tuple items.

We can use tpl[n] to acces to any value of our tuple
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list/tuple length refers to the first item. 
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4] this will be item1
second_item = tpl[-3] this will be item2
"""

first_fruit = fruits[0]
second_fruit = fruits[1]
last_fruit = fruits[-1]
print(first_fruit)
print(second_fruit)
print(last_fruit)


"""Slicing tuples
We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.
"""

# Positive index
middle_values = tpl[1:3]
print(middle_values)
from_index_to_rest = tpl[2:]
print(from_index_to_rest)

# Negative index
neg_index = tpl[-6:]
print(neg_index)
neg_middle_items = tpl[-3:-1]
print(neg_middle_items)

"""Changing Tuples to Lists
=> We can change tuples to lists and lists to tuples. 

=> Tuple is immutable if we want to modify a tuple we should change it to a list.

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl) Now we have a list, and we can change the values by using the lists methods

"""

cars = ('BMV', 'Audi', 'Porsche', 'Ferrari', 'Lamborghini')
print(type(cars))
# Now we can change and replace the tuple into a list or store the new list in a variable
cars_list = list(cars)
cars_list_copy = list(cars).copy()
cars = list(cars)
print(type(cars_list))
print(type(cars_list_copy))
print(type(cars))

# Now that our tuple is a list, let's change some values
cars[0] = 'Acura'
cars[2] ='Tesla'
print(cars)
print(type(cars))

# Now let's go back to the tuple
cars = tuple(cars)
print(type(cars))

"""Checking an Item in a Tuple
We can check if an item exists or not in a tuple using in, it returns a boolean.

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
"""

print('orange' in fruits) # True
print('apple' in fruits) # False
# fruits[0] = 'apple'  TypeError: 'tuple' object does not support item assignment

"""Joining Tuples
We can join two or more tuples using + operator

# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
"""

vegetables = ('Tomato', 'Potatoe', 'Cabbage', 'Onion', 'Carrot')

# Let's use the operator to join two tuples
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
print(type(fruits_and_vegetables))

""" Can we join a list with a tuple?
tpl1 = [51, 13, 42]
tpl2 = (12, 85, 72)
tpl_join = tpl1 + tpl2
print(tpl_join)

No we can't. This is the error we got TypeError: can only concatenate list (not "tuple") to list
"""

# If we convert the value?
tpl1 = [51, 13, 42]
tpl2 = (12, 85, 72)
tpl1 = tuple(tpl1)
tpl_join = tpl1 + tpl2
print(tpl_join)
# Yes converting the list into a tuple allow us to join both of them

"""Deleting Tuples
It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.

# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
"""

# Let's delete the fruits and vegetables variable
del fruits_and_vegetables
# print(fruits_and_vegetables) => NameError: name 'fruits_and_vegetables' is not defined
# this happens because previously we have deleted the variable

# EXERCISES - DAY 6

#1
empty_tuple2 = tuple()
empty_tuple3 = ()
print(empty_tuple2)
print(type(empty_tuple3))

#2
brothers = ('Juan', 'Rodrigo', 'Carlos', 'Marcos')
sisters = ('Cecilia', 'Luciana', 'Florencia', 'Dolores')
siblings = brothers + sisters
print(type(brothers))
print(type(sisters))
print(siblings)

#3
print('The total of siblings you have is: ', len(siblings))

#4
siblings = list(siblings)
siblings.append('Roberto')
siblings.append('Estela')
print(siblings)
print(type(siblings))

family_members = siblings.copy()
print(type(family_members))
print(family_members)

family_members = tuple(family_members)
print(type(family_members))
print(family_members)

# Exercises: Level 2