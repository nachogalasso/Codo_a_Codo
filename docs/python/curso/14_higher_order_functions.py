# 30 Days Of Python: Day 14 - Higher Order Functions


from functools import reduce

"""
Higher Order Functions
In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

A function can take one or more functions as parameters
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable
In this section, we will cover:

Handling functions as parameters
Returning functions as return value from another functions
Using Python closures and decorators

Function as a Parameter
"""

def sum_numb(nums):
    return sum(nums)

def high_order_func(f, lst): # I'm passing first the function and then the list with the values
    sumation = f(lst) # to the variable I will storage the function and the values
    return sumation 
"""
The high order function will recieve another function as parameter and a list for the values, then into a variable i will perform the passed function with the values and will return the result of the function.
So I will use this function into a variable and then print the result
"""
result = high_order_func(sum_numb, [1, 2, 3, 4, 5])
print(result)

"""Function as a Return Value"""

# Let's create some functions to work with. Remember we are passing x as a parameter
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
    
# Now is time to work with the functions into another function, remember that we are going to pass a
# parameter that is going to be passed through all the functions
def higher_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
# Keep in mind that when we call a function into another function we don't have to use the () to call
# the function
result1 = higher_function('square')
print(result1(3))      # 9
result2 = higher_function('cube')
print(result2(3))       # 27
result3 = higher_function('absolute')
print(result3(-3))      # 3

"""
You can see from the above example that the higher order function is returning different functions depending on the passed parameter

When we call the variable result and at the end we add the () and between them we pass a value, we are telling the program that the number is going to be used as the x parameter for the other functions"""

"""
Python Closures
Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.

Example:
"""
def add_ten(): # Our function, we are creating a nested function
    ten = 10 # We declared a variable
    def add(num): # We created another function into our function
        return num + ten # This function takes a parameter and add to it our first variable
    return add # We return the value from our first function that executes the 2nd function

closure_result = add_ten()
# We are printing our variable and passing to it a value as a parameter
print(closure_result(5)) 
print(closure_result(20))

"""
Python Decorators
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

Creating Decorators
To create a decorator function, we need an outer function with an inner wrapper function.

Example:

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON


"""
# Let us implement the example above with a decorator
# This decorator function is a higher order function that takes a function as a parameter
# For this example first I write the decorator function and I call it over the greeting function
def upper_case_decorator(f):
    def wrapper():
        func = f()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@upper_case_decorator # Here we are calling the decorator function. Remember to call it over the func
def greeting():
    return 'welcome to python'

print(greeting())

"""
Applying Multiple Decorators to a Single Function
These decorator functions are higher order functions that take functions as parameters
"""

# Let's create the second decorator
def split_string_decorator(f):
    def wrapper():
        func = f()
        splitting_string = func.split()
        return splitting_string
    
    return wrapper

# It's important to respect the indentation with our functions, if it is necessary leave spaces between
# the functions to identify them and avoid conflicts.

# order with decorators is important in this case - .upper() function does not work with lists
# Decorator will execute in order of precedence
@split_string_decorator
@upper_case_decorator
def greeting1():
    return 'welcome to python'
print(greeting1())
print(type(greeting1())) # Will return a list

"""
Accepting Parameters in Decorator Functions
Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters.
"""

def decorator_with_params(f):
    def wrapper_accepting_params(para1, para2, para3):
        f(para1, para2, para3)
        return ("I live in {}".format(para3)) # I'm indicatin to use only param3
        # return "{}. I live in {}".format(print_full_name, para3)
    return wrapper_accepting_params

"""If we need to return both values from the functions we can do the following changes to the code

def decorator_with_params(f):
    def wrapper_accepting_params(para1, para2, para3):
        full_name = f(para1, para2, para3)
        return ("{}. I live in {}".format(full_name, para3))
    return wrapper_accepting_params

Using the variable full_name to catch the values from the passed function, will help us later to print all the values that were passed when we call the function

"""

# Let's write the function with the decorator and the parameters
@decorator_with_params
def print_full_name(first_name, last_name, country):
    return ("I am {} {}. I love to be an american football oficial".format(first_name, last_name, country))
    
# Now let's call our decorator function with the parameters
print(print_full_name('Carlos', 'Letrin', 'Dinamarca'))

"""
Built-in Higher Order Functions
Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce. Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

Python - Map Function
The map() function is a built-in function that takes a function and iterable as parameters.

    # syntax
    map(function, iterable)
Example:1
"""

# Built-in function => map()
numb1 =[1, 2, 3, 4, 5]

def saqure1(x):
    return x ** 2

numb_squared_map = map(saqure1, numb1)
print(list(numb_squared_map))

# Let's use a lambda function with map()
numb_squared_maplambda = map(lambda x: x ** 2, numb1)
# Don't forget to turn the values into a list because the result will give us a map object
print(list(numb_squared_maplambda))
# print(numb_squared_maplambda) This will return a map object

# With map() we can convert a list of string numbers into a list of int numbers
numb_str = ['1', '2', '3', '4', '5']
numb_int_map = map(int, numb_str)
# print(numb_int_map) This gives us a map object
print(list(numb_int_map))

# Let's use map() to work with strings
names = ['liam', 'robert', 'maria', 'esteban', 'alberto']

# We create the function
def change_to_upper(name):
    return name.upper()

# Now let's pass the function through a map() function
names_upper_map = map(change_to_upper, names)
# Remember this will return an object and we need to convert it into a list
print(list(names_upper_map))

# Now with a lambda function
names_upper_maplambda = map(lambda x: x.upper(), names)
print(list(names_upper_maplambda))

"""Remember when we work with a lambda function, first we are required to pass the arguments we are going to use, then what we want the lambda function to do, and for the last the parameters that the function is going to work with."""

"""
Python - Filter Function
The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.

    # syntax
    filter(function, iterable)
"""

# Let's use filter to get only 'even' numbers
numb2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_num_filter(x):
    if x % 2 == 0:
        return True
    return False

even_numbers_filter = filter(even_num_filter, numb2)
# print(even_numbers_filter) THIS WILL ALSO RETURN AN OBJECT
print(list(even_numbers_filter)) # Now we have a list with all the even numbers

# If we want to odd numbers, let's use a lambda function
odd_numb_filterlambda = filter(lambda x: True if x % 2 != 0 else False, numb2)
print(list(odd_numb_filterlambda))

# Now we are going to filter long names more than 7
def names_filter(name):
    if len(name) > 5:
        return True
    return False

long_names = filter(names_filter, names)
print(list(long_names))

# Short names with lambda function
short_names = filter(lambda name: True if len(name) <= 5 else False, names)
print(list(short_names))

"""
Python - Reduce Function
The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value. 

REMEMBER reduce() RETURNS A "SINGLE VALUE"

Example:1
"""

# To work with reduce() we need to import it from the module functools
def add_two_numb(x, y):
    return int(x) + int(y)

total = reduce(add_two_numb, numb_str)
print(total)

# Can we use a lambda?
total_lambda = reduce(lambda x, y: int(x) + int(y), numb_str)
print(total_lambda)

# EXERCISES DAY 14

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises 1

#3
# FILTER
country_filter_lambda = filter(lambda country: True if len(country) >= 7 else False, countries)
print(list(country_filter_lambda))

def short_countries(name):
    if len(name) <= 6:
        return True
    return False

country_filter = filter(short_countries, countries)
print(list(country_filter))

# MAP
def names_upper(name):
    return name.upper()

names_uppermap = map(names_upper, names)
print(list(names_uppermap))

# map with lambda
names_uppermap_lambda = map(lambda name: name.upper(), names)
print(list(names_uppermap_lambda))

# REDUCE
def add_numb_to_reduce(x, y):
    return int(x) + int(y)

numb_red = reduce(add_numb_to_reduce, numbers)
print(numb_red)

numb_red_lambda = reduce(lambda x, y: x + y, numbers)
print(numb_red_lambda)


#4
def print_countries_list(country):
    for i in range(len(country)):
        print(f'The country is: {country[i]}')
    
print(print_countries_list(countries))

#5
def names_list(name):
    for i in range(len(name)):
        print(name[i])
        
print(names_list(names))

#6
def list_of_numbers(numb):
    for i in range(len(numb)):
        print(numb[i])
        
print(list_of_numbers(numbers))

# Exercises 2

#1
def upper_countries(country):
    return country.upper()

upper_countries_map = map(upper_countries, countries)
print(list(upper_countries_map))

#2
square_numb_list = map(lambda x: x ** 2, numbers)
print(list(square_numb_list))

#3
upper_names_map = map(lambda name: name.upper(), names)
print(list(upper_names_map))

#4
def country_with_land(country):
    if 'land' in country:
        return True
    return False

lst_country_with_land = filter(country_with_land, countries)
print(list(lst_country_with_land))

#5
country_with_six = filter(lambda country: True if len(country) == 6 else False, countries)
print(list(country_with_six))

#6
def country_six(country):
    if len(country) >= 6:
        return True
    return False

country_six_or_more = filter(country_six, countries)
print(list(country_six_or_more))

#7
def start_with(country):
    return country.startswith('E')

stt_with = filter(start_with, countries)
print(list(stt_with))

#8
chain_lst_iterator = map(upper_countries, filter(country_with_land, countries))
print(list(chain_lst_iterator))

#9
alst = [1, 'hello', 3.14, 'world', True, 'Python', False, 'here', 2.58, 'to practice']

def get_string_lst(lst):
    string_lst = []
    for item in lst:
        if isinstance(item, str):
            string_lst.append(item)
    return string_lst

print(get_string_lst(alst))

#10
num_sum = reduce(lambda x, y: x + y, numbers)
print(num_sum)

#11
def countries_sentence(accumulated, current):
    # If the accumulated string is empty, just return the current country
    if accumulated == "":
        return current
    # If it's the last country, format it with 'and'
    elif current == countries[-1]:
        return f"{accumulated}, and {current} are north European countries"
    else:
        return f"{accumulated}, {current}"

# Use reduce to create the sentence
new_sentence = reduce(countries_sentence, countries)
print(new_sentence)

#12
countries_lst = [
'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'];

def categorized_countries(type, country):
    
    country_filtered = filter(lambda country: True if type in country else False, country )
    return list(country_filtered)

print(categorized_countries('land', countries_lst))
print(categorized_countries('ia', countries_lst))
print(categorized_countries('island', countries_lst))
print(categorized_countries('stan', countries_lst))

#13
def count_countries_by_letter(countries):
    letter_count = {}
    for country in countries:
        fst_letter = country[0].upper()
        if fst_letter in letter_count:
            letter_count[fst_letter] += 1
        else:
            letter_count[fst_letter] = 1
            
    return letter_count

countries_dict = count_countries_by_letter(countries_lst)
print(countries_dict)

#14
def first_ten_countries(lst):
    return lst[:10]

fst_ten_countries = first_ten_countries(countries_lst)
print(fst_ten_countries)

#15
def last_ten_countries(lst):
    return lst[-10:]

lst_ten_countries = last_ten_countries(countries_lst)
print(lst_ten_countries)

# Exercises 3
