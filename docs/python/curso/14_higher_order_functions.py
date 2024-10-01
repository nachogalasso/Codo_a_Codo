# 30 Days Of Python: Day 14 - Higher Order Functions

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
    
    return wrapper_accepting_params

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