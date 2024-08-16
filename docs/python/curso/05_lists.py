# 30 Days Of Python: Day 5 - Lists
"""Lists
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

"""

# How to Create a List => In Python we can create lists in two ways: Using list built-in function 
# => list() or the empty []

# Using the built-in function list()
func_list = list()
print(type(func_list))

# Using square brackets []
square_list = []
print(type(square_list))

# Trying something
my_variable = 'Python For Coding'
convert_list = list(my_variable) # This will took every letter and space and store it in an index
print(convert_list)
print(type(convert_list))
print(len(convert_list))

# Let's play with some lists
fruits_1 = ['apple', 'orange', 'banana', 'watermelon', 'grape']
vegetables_1 = ['tomatoe', 'lettuce', 'potatoe', 'onion', 'pumpkin']
grocery_list = ['butter', 'milk', 'meat', 'fish', 'cereal']
techs_1 = ['Python', 'Javascript', 'Java', 'Go', 'PHP']
countries_1 = ['Germany', 'Argentina', 'Spain', 'Italy', 'France']

print('Fruits: ', fruits_1)
print('Number of fruits: ', len(fruits_1))
print('Vegetables: ', vegetables_1)
print('Number of Vegetables: ', len(vegetables_1))
print('Grocery list: ', grocery_list)
print('Number of items in the Grocery list: ', len(grocery_list))
print('Techs: ', techs_1)
print('Number of Techs: ', len(techs_1))
print('Countries to visit: ', countries_1)
print('Number of Countries to visit: ', len(countries_1))

# Let's remember that store different types of data in a list
multi_type_list = ['Robert', 'Paneles', 23, {'city':'Madrid', 'country':'Spain'}, True]
print(multi_type_list)
print(len(multi_type_list))
print(type(multi_type_list))

# It's important to know that each data is into one index, starting from 0. To access to any item
# we need to call our list and then the index of the item we want to work with
# Remember that the index is positive numbers
# Let's use the variable fruits_1
first_fruit = fruits_1[0]
print(first_fruit)
second_fruit = fruits_1[1]
print(second_fruit)
third_fruit = fruits_1[2]
print(third_fruit)
# Also we can do the follow
last_fruit = len(fruits_1) - 1
print(fruits_1[last_fruit])

# When we use negative index, -1 represents the last item in our list, if we increased the value we move to the first
last_fruit = fruits_1[-1]
secondlast_fruit = fruits_1[-2]
first_negative_fruit =fruits_1[-5]
print(last_fruit, secondlast_fruit, first_negative_fruit)

# Now is time unpack our list into single variables
item_list = ['item1', 'item2', 'item3', 'item4', 'item5']
fst_item, snd_item, trd_item, *rest = item_list
# if we want to unpack the last items into one variable before the name we are required to use the *
print(fst_item)
print(snd_item)
print(trd_item)
print(rest)
# We can also do the following thing to unpack the or create a list
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)
# with this type, the last number will be in a simple variable
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

"""Slicing Items from a List
Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
"""