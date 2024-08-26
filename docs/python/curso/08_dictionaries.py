# 30 Days Of Python: Day 8 - Dictionaries

"""Dictionaries
A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

Creating a Dictionary
To create a dictionary we use curly brackets, {} or the dict() built-in function.

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
Example:

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.

We can check how many items are in the dictionary by using the function len()

Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key
"""

"""Accessing Dictionary Items
We can access Dictionary items by referring to its key name.

Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.

The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
"""

# Accessing by the key name
# We can create a dictionary by using dict = {} or the function dict()
new_dict = dict()
print(type(new_dict))

user = {
    'first_name':'Esteban',
    'last_name':'Quito',
    'age':36,
    'country':'Italy',
    'is_married':False,
    'skills':['Javascript','React','Node','MongoDB','Python'],
    'address':{
        'street':'Caleta street',
        'zipcode':'02264'
    }
}

# Checking how many items are in our dictionary
print('Your dictionary has: ', len(user), 'items')

# Accessing by key name
print('Your user name is: ', user['first_name'])
print('Your user surname is: ', user['last_name'])
print('Your user age is: ', user['age'])

# Can we access by usign the index?
# print('Your user name is: ', user[0]) we can't access by index. The index we can use it when we have
# another dictionary or a list, in our dictionary
print('One of your user skills is: ', user['skills'][2])
print('Your user address is: ', user['address']['street'])

# If the item is not finded in our dictionary we will have an error. To avoid this error we use
# the get() function
print('Your user lives in the city: ', user.get('city'))
# By using get() if the item can't be finded the program will return None, a NoneType object
# Becuase it doesn't exist in our dictionary
print(user.get('skills'))
# print(user.get('skills'[0])) This will return a NoneType object
print(user.get('first_name'))
print(user.get('last_name'))
print(user.values()) # It will return a list called dict_values

"""Adding Items to a Dictionary
We can add new key and value pairs to a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

We can create a new pair of key value. If we need to add an item to a list in our dictionary we can use the list method append()
To add a new pair of key value we are required to call the name of our dictionary and in between [] put the name of the new key and after the = the value assigned to that key
user['job'] = 'Teacher'
"""

# Let's add some items in our dictionary
user['job_title'] = 'Data Analyst' # This new key pair will be added to end of the dictionary
user['skills'].append('Django')
print(user)

"""Modifying Items in a Dictionary
We can modify items in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

This is the same way as we modify a value from a list. We need to call the key and indicate the new value.
"""
user['first_name'] = 'Carlos'
user['age'] = 45
print(user)

"""Checking Keys in a Dictionary
We use the in operator to check if a key exist in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
"""
print('last_name' in user) # True
print('city' in user) # False

"""Removing Key and Value Pairs from a Dictionary
pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
"""

# Let's work removing some keys from our dictionary
person_test = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':32,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print(person_test)

person_test.pop('first_name') # removes first item from dictionary
person_test.popitem() # This will remove the last item, in our case 'address'
del person_test['is_marred']
# Let's check how our dictionary ended up after removing some keys
print(person_test)

"""Changing Dictionary to a List of Items
The items() method changes dictionary to a list of tuples.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

This will change the dictionary to a list of tuples, and then we can change them into a list or change the items.
"""
# I will add again the keys
# person_test['first_name'] = 'Pedro'
# person_test['address'] = {
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# person_test['is_married'] = True - Remember to write True with capital letters
person_test.update({'first_name':'Pedro', 'address':{'street':'Space street','zipcode':'02210'},'is_married':True})

print(person_test)

x = person_test.items()
print(x)
person_test['age'] = 38
print(x)

"""Clearing a Dictionary
If we don't want the items in a dictionary we can clear them using clear() method

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
"""

test_dict = dict(name = 'Juan', age = 28, skills = ['Python', 'Power BI', 'SQL'], is_working = False)
print(test_dict)

# Let's clear our dictionary
test_dict.clear()
print(test_dict) # We can keep the variable but with nothing in it

"""Deleting a Dictionary
If we do not use the dictionary we can delete it completely

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
"""
del test_dict
# print(test_dict) This gives us an error message because the dictionary was deleted

"""Copy a Dictionary
We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
"""

test_dict1 = dict(name = 'Juan', age = 28, skills = ['Python', 'Power BI', 'SQL'], is_working = False)

# Let's create a copy of the dictionary using the copy() method to avoid conflict with the original
test_dict2 = test_dict1.copy()
print(test_dict2)

"""Getting Dictionary Keys as a List
The keys() method gives us all the keys of a a dictionary as a list.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

Getting Dictionary Values as a List
The values method gives us all the values of a a dictionary as a list.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

"""
# Getting the keys of a dictionary
a = test_dict2.keys()
print(a)

# Getting the values of a dictionary
b = test_dict2.values()
print(b)

# EXERCISES - DAY 8

#1
dog = dict()

#2
dog.update({'name':'Toby', 'color':'brown', 'breed':'Shiba Inu', 'legs':4, 'age':8})
print(dog)

#3
student_dict = dict(
    first_name = 'Esteban',
    last_name = 'Quarles',
    gender = 'male',
    age = 26,
    Is_married = False,
    skills = ['Python', 'SQL', 'PowerBi', 'Django', 'Excel'],
    country = 'Spain',
    city = 'Madrid',
    address = {
        'street':'C.Carmen',
        'number': 84,
        'zip_code': '36752'
    }
)

print(student_dict)

#4
print('Student has a total of items: ', len(student_dict))

#5
skills_values = student_dict['skills']
print(skills_values)
print(type(skills_values))

#6
skills_values.append('Javascript')
skills_values.append('R')
student_dict['skills'] = skills_values
print(student_dict['skills'])

#7 #8
keys_dict = student_dict.keys()
values_dict = student_dict.values()

print(keys_dict)
print(values_dict)
print(type(keys_dict))
print(type(values_dict))

#9
student_tuple = student_dict.items()
print(student_tuple)
print(type(student_tuple))

#10
student_dict.popitem()
print(student_dict)

#11
del student_dict
# print(student_dict)