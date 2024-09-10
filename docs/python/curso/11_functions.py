# 30 Days Of Python: Day 11 - Functions

"""Functions
So far we have seen many built-in Python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, let us learn what a function is and why we need them?

Defining a Function
A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the def keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.

Declaring and Calling a Function
When we make a function, we call it declaring a function. When we start using the it, we call it calling or invoking a function. Function can be declared with or without parameters.

# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()

"""
"""
Function without Parameters

Function can be declared without parameters. We can create a function without parameters with all the tasks we want to be performed. If we want to pass parameters to the function we need to add them into between the ()

"""


def practice_function():
    name = 'Tito'
    surname = 'Colazzo'
    space = ' '
    full_name = name + space + surname
    print(full_name)
    
# Now we need to call the function to make it work
practice_function()

# We can also perform calculations with the functions
def practice_func_calculation():
    num_one = 4
    num_two = 8
    total_sum = num_one + num_two
    print(total_sum)
    
# Now we call the function
practice_func_calculation()

"""Function Returning a Value - Part 1
Function can also return values, if a function does not have a return statement, the value of the function is None. Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it.

Remember that because the variables are inside the function, they only work in there, so we can create a new function with a different name and use the same variables.

Don't forget the RETURN statement if we want the result of our function
"""
def generate_full_name():
    name = 'Esteban'
    surname = 'Cochi'
    space = ' '
    full_name = name + space + surname
    return full_name

# If we only call the function nothing will happen, so we need to call it into a print()
# generate_full_name()
print(generate_full_name())

def working_with_num():
    num_one = 6
    num_two = 8
    total_sum = num_one + num_two
    return total_sum

# print(working_with_sum())
print(working_with_num())

"""Function with Parameters
In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter

Single Parameter: If our function takes a parameter we should call our function with an argument
  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
  
  That parameter is gonna be used by the function to perform itself
  """

# What we are doing is passing name and whatever value name recieve is going to be
# used by our function
def prac_greetings(name):
    message = 'Hi ' + name + ', I hope you enjoy using Python'
    return message

print(prac_greetings('Jorge'))

def prac_add_number(number):
    # total_sum = 90 + number
    num = 90
    total_sum = num + number
    return total_sum

print(prac_add_number(50))

def prac_square_number(x):
    return x * x

print(prac_square_number(5))

def prac_area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area

print(prac_area_of_circle(6))
""" We are indicating that r is our parameter that later we pass the value of r when we write it at the moment we call the function
"""

# We can aslo use a loop into our function. Let's do one
def prac_sum_loop(n):
    total = 0
    for i in range(n+1):
        total +=i
        print(total)
        
# print(prac_sum_loop(50))
# print(prac_sum_loop(100))
print(prac_sum_loop(10))

"""Two Parameter: A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments. Let us check a function with two parameters:

# syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))

It's important when we call the function to pass both parameters

"""

def func_with_two_param(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name;

print('The client name is: ', func_with_two_param('Carlos', 'Costas'))

# Now with numbers
def func_with_numbers(num_one, num_two):
    total_sum = num_one + num_two
    return total_sum;

print('The total sum is: ', func_with_numbers(5, 14))

def calc_current_age(current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Carlos current age is: ', calc_current_age(2024, 1982))

def calc_object_weight(mass, gravity):
    weight = str(mass * gravity) + ' N' # After the calculation we convert the value into a string
    return weight;

print('The weight of our client is: ', calc_object_weight(82, 9.81)) # It is expresed in newtons

"""Passing Arguments with Key and Value
If we pass the arguments with key and value, the order of the arguments does not matter.

# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here

We can pass the key-value pair from the dictionaries as arguments in our functions
"""

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name

print(print_full_name(firstname= 'Raul', lastname= 'Estevez'))

def print_twonumb_add(num1, num2):
    total_sum = num1 + num2
    return total_sum

print(print_twonumb_add(num1= 4, num2 = 8))

"""Function Returning a Value - Part 2
If we do not return a value with a function, then our function is returning None by default. To return a value with a function we use the keyword return followed by the variable we are returning. We can return any kind of data types from a function.

Returning a string: Example:
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

"""

# Returning a boolean: Example:
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False


# Returning a list: Example:
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

"""
Function with Default Parameters

Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.

# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)

The default value is the one that we pass with the params => def afunction(param = default_value)

"""

def param_greettings(name = 'Pedro'):
    message = name + ', welcome to this program'
    return message

print(param_greettings())
print(param_greettings('Gonzalo'))

def param_greettings_fullname(name = 'Ramiro', surname = 'Colacho'):
    space = ' '
    full_name = name + space + surname
    return full_name

print(param_greettings_fullname())
print(param_greettings_fullname(name = 'Juan', surname = 'Mosquito'))

def param_calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;

print('Age: ', param_calculate_age(1821))

def param_weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight

print('Weight of an object in Newtons: ', param_weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', param_weight_of_object(100, 1.62)) # gravity on the surface of the Moon

"""Arbitrary Number of Arguments
If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)

We use the * when we don't know how many params we are going to pass. We can use the args
"""

def various_params(*args):
    total = 0
    for n in args:
        total += n # It will take all the values passed to the function
    return total

print(various_params(10, 3, 5))

# Default and Arbitrary Number of Parameters in Functions
def param_generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
        
print(param_generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

# Function as a Parameter of Another Function
#You can pass functions around as parameters

def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)

print(do_something(square_number, 3)) # 27

# EXERCISES - DAY 11

#1
def add_two_numbers(num1, num2):
    total_sum = num1 + num2
    return total_sum

add_two_numbers(2, 6)

#2
def area_of_circle(r):
    PI = 3.14
    circle_area = PI * r ** 2
    return circle_area

area_of_circle(6)

#3
def add_all_nums(*args):
    total_sum = 0
    for i in args:
            if not isinstance(i, (int, float)):
                return 'Please insert a number'
    else:
        for n in args:
            total_sum += n # Don't forget to declare before the variable
        
    return total_sum
print(add_all_nums('house'))
print(add_all_nums(3, 6, 7))

#4
def cel_to_fah(c):
    
    if not isinstance(c, (int, float)):
        return 'Please insert a celcius number'
    else:
        f = (c * 9 / 5) + 32
        return print(f'Your {c}ºC temperature to fahrenheit is {f}ºF')
    
cel_to_fah(32)

#5
def check_season(x):
    x = str(x)
    if x == 'december' or x == 'january' or x == 'febrary' or x == 'march':
        return 'Your season is Winter'
    elif x == 'april' or x == 'may' or x == 'june':
        return 'Your season is Spring'
    elif x == 'july' or x == 'august' or x == 'september':
        return 'Your season is Summer'
    else:
        return 'Your season is Autumn'
        
# check_season(input('Enter your month:'))

#7
def solve_quadratic_eqn():
    a = float(input('Enter the value of a:'))
    b = float(input('Enter the value of b:'))
    c = float(input('Enter the value of c:'))
    d = b**2-4*a*c
    
    if d < 0:
        return 'This equation has no real solution'
    elif d == 0:
        x = -b +- (b ** 2 - 4 * a * c) ** 0.5 / 2 * a
        return f'The solution to this equation is {x}'
    
# solve_quadratic_eqn()

#8
def print_list(x):
    for i in range(len(x)):
        print(x[i])
        
print_list(x = ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'])

#9
def reverse_list(x):
    return x[::-1]

def reverse_list1(lst):
    reversed_list = []
    for i in range(len(lst) -1, -1, -1):
        reversed_list.append(lst[i])
        
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

#10
cars = ['bmw', 'toyota', 'audi', 'porsche', 'ferrari']

def capitalize_items(lst):
    capitalize_list = ' '.join(lst)
    x = capitalize_list.upper()
    s = x.split(' ')
    return s

capitalize_items(cars)

#11

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

def add_item(lst, item):
    if type(item) == str:
        
        lst.append(item)
        return lst
    else:
        lst.append(item)
        return lst
        
print(add_item(food_staff, 'Meat')) # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
print(add_item(numbers, 5)) # [2, 3, 7, 9, 5]

#12
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
        return lst
    
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
print(remove_item(numbers, 3))  # [2, 7, 9]

#13
def sum_all_range_num(num):
    total_sum = 0
    for i in range(num + 1):
        total_sum += i
        
    return total_sum

print(sum_all_range_num(5))  # 15
print(sum_all_range_num(10)) # 55
print(sum_all_range_num(100)) # 5050

#14
def sum_all_odds(num):
    odds = []
    for i in range(num + 1):
        if i % 2 != 0:
            odds.append(i)
            
    return odds

print(sum_all_odds(100))

#15
def sum_all_evens(num):
    evens = []
    for i in range(num + 1):
        if i % 2 == 0:
            evens.append(i)
            
    return evens

print(sum_all_evens(80))

# Exercises level 2

#1
def evens_and_odds(num):
    evens = []
    odds = []
    for i in range(num + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return f'The number off evens is: {len(evens)}, the number of odds is: {len(odds)}'

print(evens_and_odds(100))
print(evens_and_odds(75))

#2
# A example using a recursive function
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    
print(factorial(8))

#3
def is_empty(param):
    if param is None:
        return True
    elif isinstance(param, str) and len(param) == 0:
        return True
    elif isinstance(param, (list, tuple, dict)) and len(param) == 0:
        return True
    
    return False

print(is_empty(""))          # True (empty string)
print(is_empty([]))          # True (empty list)
print(is_empty({}))          # True (empty dictionary)
print(is_empty(None))        # True (None)
print(is_empty("Hello"))     # False (non-empty string)
print(is_empty([1, 2, 3]))   # False (non-empty list)

#4
# They should calculate_mean, calculate_median, calculate_mode, 
# calculate_range, calculate_variance, calculate_std (standard deviation).
numb_to_calculate = [10, 26, 68, 23 , 45, 32, 85, 11, 9, 5]

def calculate_mean(data):
    total_sum = 0
    for i in range(len(data)):
        total_sum += data[i]
    
    return total_sum / len(data)

print(calculate_mean(numb_to_calculate))

def calculate_median(data):
    x = data.copy()
    sorted_data = x.sort()
    n = len(x)
    mid = n // 2
    if n % 2 == 0:
        return (x[mid - 1] + x[mid]) / 2
    else:
        return x[mid]
    
print(calculate_median(numb_to_calculate))

def calculate_mode(data):
    mode = {}
    for n in data:
        mode[n] = mode.get(n, 0) + 1
    
    max_freq = max(mode.values())
    modes = [key for key, value in mode.items() if value == max_freq]
    return modes

print(calculate_mode(numb_to_calculate))

def calculate_range(data):
    sort_min_data = sorted(data)
    sort_max_data = sorted(data, reverse = True)
    min = sort_min_data[0]
    max = sort_max_data[0]
    
    return max - min

print(calculate_range(numb_to_calculate))