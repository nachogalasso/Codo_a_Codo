# 30 Days Of Python: Day 2 - Variables, Builtin Functions
""" Let's work with the different types of variables and the different built-in types of functions in Python. The built-in functions are those that they don't need to be imported, they are included in Python, they are: abs[), delattr() has]() memoryview() set() all() dict() help() min() setattr() any() dir() hex() next() slice() ascii() divmod() id() object() sorted() bin() enumerate() input() oct() staticmethod() bool() eval() int() open() str() breakpoint() exec() isinstance() ord() sum() bytearray() filter() issubclass() pow() super() bytes() float() iter() print() tuple() callable() format() len() property() type() chr() frozenset() list() range() vars() classmethod() getattr() locals() repr() zip() compile() globals() map() reversed() __import__() complex() hasattr() max() round()

https://docs.python.org/3.9/library/functions.html

"""
# Let's work with some built-in functions
print(len('Hello World'))
print(str(5))
print(int('5'))
print(float(5))
print(input('Hi!!, How can I help you?'))

"""If we want to see the keywords that are reserved for Python we only need to insert the following command help('Keywords'). We can use dir(str). Remember we can use these words to declare variables
"""

print(max(10, 25, 36, 8, 7))
print(min(10, 25, 36, 8, 7))
print(min([10, 25, 36, 8, 7]))
print(max([10, 25, 36, 8, 7]))
print(max((10, 25, 36, 8, 7)))
print(sum([10, 25, 36, 8, 7])) # it takes the list as an argument and returns the sum

""" VARIABLES
Remember when we name variables we can't start naming them with a number, special character, ot hyphens. Always try to use descriptive names to distinguish the data they are refering too or the data they storage.
Variables must start with a letter or an underscore, can contain alpha numeric numbers, and they are case-sensitive (don't forget that we can't use the reserved words, if we want to use an "if" we can name it by using "_if")
Python convention for naming variables is using the snake_case, like "last_name", "first_name" and similar. 
Using the equal sign after naming a variable, we declare what data type is going to be stored in that variable.

first_name = 'Asabeneh' => string
last_name = 'Yetayeh' => string
country = 'Finland' => string
city = 'Helsinki' => string
age = 250 => integer
is_married = True => boolean
skills = ['HTML', 'CSS', 'JS', 'React', 'Python'] => list
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   } => dictionary
"""

first_name = 'Juan'
last_name = 'Botero'
age = 36
city = 'Frankfurt'
country = 'Germany'
is_married = False
have_kids = 0
skills = ['Python', 'Power Bi', 'Django', 'Javascript', 'SQL']

# Let's combine the info into a variable
person_info = {
    'first_name': 'Juan',
    'last_name': 'Botero',
    'age': 36,
    'city': 'Frankfurt',
    'country': 'Germany',
    'is_married': False,
    'have_kids': 0,
    'skills': ['Python', 'Power Bi', 'Django', 'Javascript', 'SQL'] 
}

# Let's print our variables
print('First Name: ', first_name)
print('Last Name: ', last_name)
print('Country: ', len(country))
print('Country: ', country)
print('Age: ', str(age))
print('Is Married?', is_married)
print('Skills?', skills)
print('User: ', person_info)
print('User name: ', person_info['first_name'])
print('User country: ', person_info['country'])
print('User age: ', person_info['age'])

# We can declare multiple variables in one line
firstName, lastName, Country, userAge = 'Diego', 'Gomez', 'Argentina', 42
print('First Name: ', firstName)
print('Last Name: ', lastName)
print('Country: ', Country)
print('Age: ', userAge)

# We can use built-in functions to ask the user for their data
user_name = input('Please enter your name:')
user_surname = input('Please enter your surname:')
user_age = int(input('Please tell me your age:'))

print(user_name)
print(user_surname)
print(user_age)


# EXCERCISES 1
# Timming the duration of a light bulb
year = 2024
is_turned_on = False
is_turned_off = True
brand, bulb_type, light_type, watts, price = 'Samsung', 'halogen', 'warm', 40, 2.53
print('The light brand is: ', brand)
print('The bulb type is: ', bulb_type)
print('The light type is: ', light_type)
print('It has: ', watts, ' watts')
print('The price is: ', price)

# EXCERCISES 2
print(type(brand))
print(type(bulb_type))
print(type(light_type))
print(type(watts))
print(type(price))
print(type(person_info))
print(len('Ignacio'))
print(len('Galasso'))

num_one = 5
num_two = 4
add = num_one + num_two
substract = num_two - num_one
multiply = num_two * num_one
divide = num_one / num_two
modulus = num_two % num_one
exponent = num_one ** num_two
floor_division = num_one // num_two
print(add, 
      substract, 
      divide, 
      multiply,
      modulus, 
      exponent, 
      floor_division)

# Working with a circle
radius = 30
pi = 3.14
area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * radius
print(area_of_circle)
print(circum_of_circle)

user_radius = int(input('Please indicate the radius of the circle: '))
area_user_circle = pi * (user_radius ** 2)
print(area_user_circle)