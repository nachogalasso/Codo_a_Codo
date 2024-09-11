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

def calculate_variance(data):
    total_sum = 0
    mean = calculate_mean(data)
    if len(data) == 0:
        return 0
    for i in range(len(data)):
        total_sum += data[i]
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / len(data)
    return variance

print(calculate_variance(numb_to_calculate))

def calculate_std(data):
    variance = calculate_variance(data)
    std_dev = variance ** 0.5
    return std_dev

print(calculate_std(numb_to_calculate))

# Exercises 3

#1
def is_prime(num):
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if (num % i) == 0:
                return f'{num}, is not a prime number'
                break
        else:
            return f'{num}, is a prime number'
    else:
        return f'{num}, is not a prime number'
        
print(is_prime(int(input('Enter a number:'))))

#2
lst1 = [20, 22, 67, 8, 62, 71, 32, 20, 18, 45, 59, 22]
lst2 = [20, 22, 67, 8, 62, 71, 32, 38, 18, 45, 59, 26]
def check_unique_items(data):
    if len(data) == len(set(data)):
        return 'The items are unique'
    else:
        return 'You have duplicated values'
    
print(check_unique_items(lst1))
print(check_unique_items(lst2))

#3
lst3 = [20, 22, 67, 8, 62, 71, 32]
lst4 = [10, 3.5, 18, 62.6, 72.1, 50]
lst5 = [10, 'a', {'name':'Carlos', 'surname':'Gonzalez'}, 3.5, 'Caballo']
def items_are_same_type(data):
    if not data:
        return True
    fst_type = type(data[0])
    return all(isinstance(item, fst_type) for item in data)

print(items_are_same_type(lst3))
print(items_are_same_type(lst4))
print(items_are_same_type(lst5))

#4
def is_valid_variable_name(name):
    if not name:  
        return False
    if not (name[0].isalpha() or name[0] == '_'):  
        return False
    for char in name:  
        if not (char.isalnum() or char == '_'): 
            return False
    # List of Python keywords
    keywords = [
        "False", "None", "True", "and", "as", "assert", "async", "await", "break", 
        "class", "continue", "def", "del", "elif", "else", "except", "finally", 
        "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", 
        "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
    ]
    return name not in keywords

# 5
countries_data = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "languages": [
            "Arabic"
        ],
        "population": 40400000,
        "flag": "https://restcountries.eu/data/dza.svg",
        "currency": "Algerian dinar"
    },
    {
        "name": "American Samoa",
        "capital": "Pago Pago",
        "languages": [
            "English",
            "Samoan"
        ],
        "population": 57100,
        "flag": "https://restcountries.eu/data/asm.svg",
        "currency": "United State Dollar"
    },
    {
        "name": "Andorra",
        "capital": "Andorra la Vella",
        "languages": [
            "Catalan"
        ],
        "population": 78014,
        "flag": "https://restcountries.eu/data/and.svg",
        "currency": "Euro"
    },
    {
        "name": "Angola",
        "capital": "Luanda",
        "languages": [
            "Portuguese"
        ],
        "population": 25868000,
        "flag": "https://restcountries.eu/data/ago.svg",
        "currency": "Angolan kwanza"
    },
    {
        "name": "Anguilla",
        "capital": "The Valley",
        "languages": [
            "English"
        ],
        "population": 13452,
        "flag": "https://restcountries.eu/data/aia.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Antarctica",
        "capital": "",
        "languages": [
            "English",
            "Russian"
        ],
        "population": 1000,
        "flag": "https://restcountries.eu/data/ata.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Antigua and Barbuda",
        "capital": "Saint John's",
        "languages": [
            "English"
        ],
        "population": 86295,
        "flag": "https://restcountries.eu/data/atg.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Argentina",
        "capital": "Buenos Aires",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 43590400,
        "flag": "https://restcountries.eu/data/arg.svg",
        "currency": "Argentine peso"
    },
    {
        "name": "Armenia",
        "capital": "Yerevan",
        "languages": [
            "Armenian",
            "Russian"
        ],
        "population": 2994400,
        "flag": "https://restcountries.eu/data/arm.svg",
        "currency": "Armenian dram"
    },
    {
        "name": "Aruba",
        "capital": "Oranjestad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi"
        ],
        "population": 107394,
        "flag": "https://restcountries.eu/data/abw.svg",
        "currency": "Aruban florin"
    },
    {
        "name": "Australia",
        "capital": "Canberra",
        "languages": [
            "English"
        ],
        "population": 24117360,
        "flag": "https://restcountries.eu/data/aus.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Austria",
        "capital": "Vienna",
        "languages": [
            "German"
        ],
        "population": 8725931,
        "flag": "https://restcountries.eu/data/aut.svg",
        "currency": "Euro"
    },
    {
        "name": "Azerbaijan",
        "capital": "Baku",
        "languages": [
            "Azerbaijani"
        ],
        "population": 9730500,
        "flag": "https://restcountries.eu/data/aze.svg",
        "currency": "Azerbaijani manat"
    },
    {
        "name": "Bahamas",
        "capital": "Nassau",
        "languages": [
            "English"
        ],
        "population": 378040,
        "flag": "https://restcountries.eu/data/bhs.svg",
        "currency": "Bahamian dollar"
    },
    {
        "name": "Bahrain",
        "capital": "Manama",
        "languages": [
            "Arabic"
        ],
        "population": 1404900,
        "flag": "https://restcountries.eu/data/bhr.svg",
        "currency": "Bahraini dinar"
    },
    {
        "name": "Bangladesh",
        "capital": "Dhaka",
        "languages": [
            "Bengali"
        ],
        "population": 161006790,
        "flag": "https://restcountries.eu/data/bgd.svg",
        "currency": "Bangladeshi taka"
    },
    {
        "name": "Barbados",
        "capital": "Bridgetown",
        "languages": [
            "English"
        ],
        "population": 285000,
        "flag": "https://restcountries.eu/data/brb.svg",
        "currency": "Barbadian dollar"
    },
    {
        "name": "Belarus",
        "capital": "Minsk",
        "languages": [
            "Belarusian",
            "Russian"
        ],
        "population": 9498700,
        "flag": "https://restcountries.eu/data/blr.svg",
        "currency": "New Belarusian ruble"
    },
    {
        "name": "Belgium",
        "capital": "Brussels",
        "languages": [
            "Dutch",
            "French",
            "German"
        ],
        "population": 11319511,
        "flag": "https://restcountries.eu/data/bel.svg",
        "currency": "Euro"
    },
    {
        "name": "Belize",
        "capital": "Belmopan",
        "languages": [
            "English",
            "Spanish"
        ],
        "population": 370300,
        "flag": "https://restcountries.eu/data/blz.svg",
        "currency": "Belize dollar"
    },
    {
        "name": "Benin",
        "capital": "Porto-Novo",
        "languages": [
            "French"
        ],
        "population": 10653654,
        "flag": "https://restcountries.eu/data/ben.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Bermuda",
        "capital": "Hamilton",
        "languages": [
            "English"
        ],
        "population": 61954,
        "flag": "https://restcountries.eu/data/bmu.svg",
        "currency": "Bermudian dollar"
    },
    {
        "name": "Bhutan",
        "capital": "Thimphu",
        "languages": [
            "Dzongkha"
        ],
        "population": 775620,
        "flag": "https://restcountries.eu/data/btn.svg",
        "currency": "Bhutanese ngultrum"
    },
    {
        "name": "Bolivia (Plurinational State of)",
        "capital": "Sucre",
        "languages": [
            "Spanish",
            "Aymara",
            "Quechua"
        ],
        "population": 10985059,
        "flag": "https://restcountries.eu/data/bol.svg",
        "currency": "Bolivian boliviano"
    },
    {
        "name": "Bonaire, Sint Eustatius and Saba",
        "capital": "Kralendijk",
        "languages": [
            "Dutch"
        ],
        "population": 17408,
        "flag": "https://restcountries.eu/data/bes.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Bosnia and Herzegovina",
        "capital": "Sarajevo",
        "languages": [
            "Bosnian",
            "Croatian",
            "Serbian"
        ],
        "population": 3531159,
        "flag": "https://restcountries.eu/data/bih.svg",
        "currency": "Bosnia and Herzegovina convertible mark"
    },
    {
        "name": "Botswana",
        "capital": "Gaborone",
        "languages": [
            "English",
            "Tswana"
        ],
        "population": 2141206,
        "flag": "https://restcountries.eu/data/bwa.svg",
        "currency": "Botswana pula"
    },
    {
        "name": "Bouvet Island",
        "capital": "",
        "languages": [
            "Norwegian",
            "Norwegian Bokmål",
            "Norwegian Nynorsk"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/bvt.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Brazil",
        "capital": "Brasília",
        "languages": [
            "Portuguese"
        ],
        "population": 206135893,
        "flag": "https://restcountries.eu/data/bra.svg",
        "currency": "Brazilian real"
    },
    {
        "name": "British Indian Ocean Territory",
        "capital": "Diego Garcia",
        "languages": [
            "English"
        ],
        "population": 3000,
        "flag": "https://restcountries.eu/data/iot.svg",
        "currency": "United States dollar"
    },
    {
        "name": "United States Minor Outlying Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 300,
        "flag": "https://restcountries.eu/data/umi.svg",
        "currency": "United States Dollar"
    },
    {
        "name": "Virgin Islands (British)",
        "capital": "Road Town",
        "languages": [
            "English"
        ],
        "population": 28514,
        "flag": "https://restcountries.eu/data/vgb.svg",
        "currency": "[D]"
    },
    {
        "name": "Virgin Islands (U.S.)",
        "capital": "Charlotte Amalie",
        "languages": [
            "English"
        ],
        "population": 114743,
        "flag": "https://restcountries.eu/data/vir.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Brunei Darussalam",
        "capital": "Bandar Seri Begawan",
        "languages": [
            "Malay"
        ],
        "population": 411900,
        "flag": "https://restcountries.eu/data/brn.svg",
        "currency": "Brunei dollar"
    },
    {
        "name": "Bulgaria",
        "capital": "Sofia",
        "languages": [
            "Bulgarian"
        ],
        "population": 7153784,
        "flag": "https://restcountries.eu/data/bgr.svg",
        "currency": "Bulgarian lev"
    },
    {
        "name": "Burkina Faso",
        "capital": "Ouagadougou",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 19034397,
        "flag": "https://restcountries.eu/data/bfa.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Burundi",
        "capital": "Bujumbura",
        "languages": [
            "French",
            "Kirundi"
        ],
        "population": 10114505,
        "flag": "https://restcountries.eu/data/bdi.svg",
        "currency": "Burundian franc"
    },
    {
        "name": "Cambodia",
        "capital": "Phnom Penh",
        "languages": [
            "Khmer"
        ],
        "population": 15626444,
        "flag": "https://restcountries.eu/data/khm.svg",
        "currency": "Cambodian riel"
    },
    {
        "name": "Cameroon",
        "capital": "Yaoundé",
        "languages": [
            "English",
            "French"
        ],
        "population": 22709892,
        "flag": "https://restcountries.eu/data/cmr.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Canada",
        "capital": "Ottawa",
        "languages": [
            "English",
            "French"
        ],
        "population": 36155487,
        "flag": "https://restcountries.eu/data/can.svg",
        "currency": "Canadian dollar"
    },
    {
        "name": "Cabo Verde",
        "capital": "Praia",
        "languages": [
            "Portuguese"
        ],
        "population": 531239,
        "flag": "https://restcountries.eu/data/cpv.svg",
        "currency": "Cape Verdean escudo"
    },
    {
        "name": "Cayman Islands",
        "capital": "George Town",
        "languages": [
            "English"
        ],
        "population": 58238,
        "flag": "https://restcountries.eu/data/cym.svg",
        "currency": "Cayman Islands dollar"
    },
    {
        "name": "Central African Republic",
        "capital": "Bangui",
        "languages": [
            "French",
            "Sango"
        ],
        "population": 4998000,
        "flag": "https://restcountries.eu/data/caf.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chad",
        "capital": "N'Djamena",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 14497000,
        "flag": "https://restcountries.eu/data/tcd.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chile",
        "capital": "Santiago",
        "languages": [
            "Spanish"
        ],
        "population": 18191900,
        "flag": "https://restcountries.eu/data/chl.svg",
        "currency": "Chilean peso"
    },
    {
        "name": "China",
        "capital": "Beijing",
        "languages": [
            "Chinese"
        ],
        "population": 1377422166,
        "flag": "https://restcountries.eu/data/chn.svg",
        "currency": "Chinese yuan"
    },
    {
        "name": "Christmas Island",
        "capital": "Flying Fish Cove",
        "languages": [
            "English"
        ],
        "population": 2072,
        "flag": "https://restcountries.eu/data/cxr.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Cocos (Keeling) Islands",
        "capital": "West Island",
        "languages": [
            "English"
        ],
        "population": 550,
        "flag": "https://restcountries.eu/data/cck.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Colombia",
        "capital": "Bogotá",
        "languages": [
            "Spanish"
        ],
        "population": 48759958,
        "flag": "https://restcountries.eu/data/col.svg",
        "currency": "Colombian peso"
    },
    {
        "name": "Comoros",
        "capital": "Moroni",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 806153,
        "flag": "https://restcountries.eu/data/com.svg",
        "currency": "Comorian franc"
    },
    {
        "name": "Congo",
        "capital": "Brazzaville",
        "languages": [
            "French",
            "Lingala"
        ],
        "population": 4741000,
        "flag": "https://restcountries.eu/data/cog.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Congo (Democratic Republic of the)",
        "capital": "Kinshasa",
        "languages": [
            "French",
            "Lingala",
            "Kongo",
            "Swahili",
            "Luba-Katanga"
        ],
        "population": 85026000,
        "flag": "https://restcountries.eu/data/cod.svg",
        "currency": "Congolese franc"
    },
    {
        "name": "Cook Islands",
        "capital": "Avarua",
        "languages": [
            "English"
        ],
        "population": 18100,
        "flag": "https://restcountries.eu/data/cok.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Costa Rica",
        "capital": "San José",
        "languages": [
            "Spanish"
        ],
        "population": 4890379,
        "flag": "https://restcountries.eu/data/cri.svg",
        "currency": "Costa Rican colón"
    },
    {
        "name": "Croatia",
        "capital": "Zagreb",
        "languages": [
            "Croatian"
        ],
        "population": 4190669,
        "flag": "https://restcountries.eu/data/hrv.svg",
        "currency": "Croatian kuna"
    },
    {
        "name": "Cuba",
        "capital": "Havana",
        "languages": [
            "Spanish"
        ],
        "population": 11239004,
        "flag": "https://restcountries.eu/data/cub.svg",
        "currency": "Cuban convertible peso"
    },
    {
        "name": "Curaçao",
        "capital": "Willemstad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi",
            "English"
        ],
        "population": 154843,
        "flag": "https://restcountries.eu/data/cuw.svg",
        "currency": "Netherlands Antillean guilder"
    },
    {
        "name": "Cyprus",
        "capital": "Nicosia",
        "languages": [
            "Greek (modern)",
            "Turkish",
            "Armenian"
        ],
        "population": 847000,
        "flag": "https://restcountries.eu/data/cyp.svg",
        "currency": "Euro"
    },
    {
        "name": "Czech Republic",
        "capital": "Prague",
        "languages": [
            "Czech",
            "Slovak"
        ],
        "population": 10558524,
        "flag": "https://restcountries.eu/data/cze.svg",
        "currency": "Czech koruna"
    },
    {
        "name": "Denmark",
        "capital": "Copenhagen",
        "languages": [
            "Danish"
        ],
        "population": 5717014,
        "flag": "https://restcountries.eu/data/dnk.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Djibouti",
        "capital": "Djibouti",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 900000,
        "flag": "https://restcountries.eu/data/dji.svg",
        "currency": "Djiboutian franc"
    },
    {
        "name": "Dominica",
        "capital": "Roseau",
        "languages": [
            "English"
        ],
        "population": 71293,
        "flag": "https://restcountries.eu/data/dma.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Dominican Republic",
        "capital": "Santo Domingo",
        "languages": [
            "Spanish"
        ],
        "population": 10075045,
        "flag": "https://restcountries.eu/data/dom.svg",
        "currency": "Dominican peso"
    },
    {
        "name": "Ecuador",
        "capital": "Quito",
        "languages": [
            "Spanish"
        ],
        "population": 16545799,
        "flag": "https://restcountries.eu/data/ecu.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Egypt",
        "capital": "Cairo",
        "languages": [
            "Arabic"
        ],
        "population": 91290000,
        "flag": "https://restcountries.eu/data/egy.svg",
        "currency": "Egyptian pound"
    },
    {
        "name": "El Salvador",
        "capital": "San Salvador",
        "languages": [
            "Spanish"
        ],
        "population": 6520675,
        "flag": "https://restcountries.eu/data/slv.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Equatorial Guinea",
        "capital": "Malabo",
        "languages": [
            "Spanish",
            "French"
        ],
        "population": 1222442,
        "flag": "https://restcountries.eu/data/gnq.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Eritrea",
        "capital": "Asmara",
        "languages": [
            "Tigrinya",
            "Arabic",
            "English"
        ],
        "population": 5352000,
        "flag": "https://restcountries.eu/data/eri.svg",
        "currency": "Eritrean nakfa"
    },
    {
        "name": "Estonia",
        "capital": "Tallinn",
        "languages": [
            "Estonian"
        ],
        "population": 1315944,
        "flag": "https://restcountries.eu/data/est.svg",
        "currency": "Euro"
    },
    {
        "name": "Ethiopia",
        "capital": "Addis Ababa",
        "languages": [
            "Amharic"
        ],
        "population": 92206005,
        "flag": "https://restcountries.eu/data/eth.svg",
        "currency": "Ethiopian birr"
    },
    {
        "name": "Falkland Islands (Malvinas)",
        "capital": "Stanley",
        "languages": [
            "English"
        ],
        "population": 2563,
        "flag": "https://restcountries.eu/data/flk.svg",
        "currency": "Falkland Islands pound"
    },
    {
        "name": "Faroe Islands",
        "capital": "Tórshavn",
        "languages": [
            "Faroese"
        ],
        "population": 49376,
        "flag": "https://restcountries.eu/data/fro.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Fiji",
        "capital": "Suva",
        "languages": [
            "English",
            "Fijian",
            "Hindi",
            "Urdu"
        ],
        "population": 867000,
        "flag": "https://restcountries.eu/data/fji.svg",
        "currency": "Fijian dollar"
    },
    {
        "name": "Finland",
        "capital": "Helsinki",
        "languages": [
            "Finnish",
            "Swedish"
        ],
        "population": 5491817,
        "flag": "https://restcountries.eu/data/fin.svg",
        "currency": "Euro"
    },
    {
        "name": "France",
        "capital": "Paris",
        "languages": [
            "French"
        ],
        "population": 66710000,
        "flag": "https://restcountries.eu/data/fra.svg",
        "currency": "Euro"
    },
    {
        "name": "French Guiana",
        "capital": "Cayenne",
        "languages": [
            "French"
        ],
        "population": 254541,
        "flag": "https://restcountries.eu/data/guf.svg",
        "currency": "Euro"
    },
    {
        "name": "French Polynesia",
        "capital": "Papeetē",
        "languages": [
            "French"
        ],
        "population": 271800,
        "flag": "https://restcountries.eu/data/pyf.svg",
        "currency": "CFP franc"
    },
    {
        "name": "French Southern Territories",
        "capital": "Port-aux-Français",
        "languages": [
            "French"
        ],
        "population": 140,
        "flag": "https://restcountries.eu/data/atf.svg",
        "currency": "Euro"
    },
    {
        "name": "Gabon",
        "capital": "Libreville",
        "languages": [
            "French"
        ],
        "population": 1802278,
        "flag": "https://restcountries.eu/data/gab.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Gambia",
        "capital": "Banjul",
        "languages": [
            "English"
        ],
        "population": 1882450,
        "flag": "https://restcountries.eu/data/gmb.svg",
        "currency": "Gambian dalasi"
    },
    {
        "name": "Georgia",
        "capital": "Tbilisi",
        "languages": [
            "Georgian"
        ],
        "population": 3720400,
        "flag": "https://restcountries.eu/data/geo.svg",
        "currency": "Georgian Lari"
    },
    {
        "name": "Germany",
        "capital": "Berlin",
        "languages": [
            "German"
        ],
        "population": 81770900,
        "flag": "https://restcountries.eu/data/deu.svg",
        "currency": "Euro"
    },
    {
        "name": "Ghana",
        "capital": "Accra",
        "languages": [
            "English"
        ],
        "population": 27670174,
        "flag": "https://restcountries.eu/data/gha.svg",
        "currency": "Ghanaian cedi"
    },
    {
        "name": "Gibraltar",
        "capital": "Gibraltar",
        "languages": [
            "English"
        ],
        "population": 33140,
        "flag": "https://restcountries.eu/data/gib.svg",
        "currency": "Gibraltar pound"
    },
    {
        "name": "Greece",
        "capital": "Athens",
        "languages": [
            "Greek (modern)"
        ],
        "population": 10858018,
        "flag": "https://restcountries.eu/data/grc.svg",
        "currency": "Euro"
    },
    {
        "name": "Greenland",
        "capital": "Nuuk",
        "languages": [
            "Kalaallisut"
        ],
        "population": 55847,
        "flag": "https://restcountries.eu/data/grl.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Grenada",
        "capital": "St. George's",
        "languages": [
            "English"
        ],
        "population": 103328,
        "flag": "https://restcountries.eu/data/grd.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Guadeloupe",
        "capital": "Basse-Terre",
        "languages": [
            "French"
        ],
        "population": 400132,
        "flag": "https://restcountries.eu/data/glp.svg",
        "currency": "Euro"
    },
    {
        "name": "Guam",
        "capital": "Hagåtña",
        "languages": [
            "English",
            "Chamorro",
            "Spanish"
        ],
        "population": 184200,
        "flag": "https://restcountries.eu/data/gum.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Guatemala",
        "capital": "Guatemala City",
        "languages": [
            "Spanish"
        ],
        "population": 16176133,
        "flag": "https://restcountries.eu/data/gtm.svg",
        "currency": "Guatemalan quetzal"
    },
    {
        "name": "Guernsey",
        "capital": "St. Peter Port",
        "languages": [
            "English",
            "French"
        ],
        "population": 62999,
        "flag": "https://restcountries.eu/data/ggy.svg",
        "currency": "British pound"
    },
    {
        "name": "Guinea",
        "capital": "Conakry",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 12947000,
        "flag": "https://restcountries.eu/data/gin.svg",
        "currency": "Guinean franc"
    },
    {
        "name": "Guinea-Bissau",
        "capital": "Bissau",
        "languages": [
            "Portuguese"
        ],
        "population": 1547777,
        "flag": "https://restcountries.eu/data/gnb.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Guyana",
        "capital": "Georgetown",
        "languages": [
            "English"
        ],
        "population": 746900,
        "flag": "https://restcountries.eu/data/guy.svg",
        "currency": "Guyanese dollar"
    },
    {
        "name": "Haiti",
        "capital": "Port-au-Prince",
        "languages": [
            "French",
            "Haitian"
        ],
        "population": 11078033,
        "flag": "https://restcountries.eu/data/hti.svg",
        "currency": "Haitian gourde"
    },
    {
        "name": "Heard Island and McDonald Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/hmd.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Holy See",
        "capital": "Rome",
        "languages": [
            "Latin",
            "Italian",
            "French",
            "German"
        ],
        "population": 451,
        "flag": "https://restcountries.eu/data/vat.svg",
        "currency": "Euro"
    },
    {
        "name": "Honduras",
        "capital": "Tegucigalpa",
        "languages": [
            "Spanish"
        ],
        "population": 8576532,
        "flag": "https://restcountries.eu/data/hnd.svg",
        "currency": "Honduran lempira"
    },
    {
        "name": "Hong Kong",
        "capital": "City of Victoria",
        "languages": [
            "English",
            "Chinese"
        ],
        "population": 7324300,
        "flag": "https://restcountries.eu/data/hkg.svg",
        "currency": "Hong Kong dollar"
    },
    {
        "name": "Hungary",
        "capital": "Budapest",
        "languages": [
            "Hungarian"
        ],
        "population": 9823000,
        "flag": "https://restcountries.eu/data/hun.svg",
        "currency": "Hungarian forint"
    },
    {
        "name": "Iceland",
        "capital": "Reykjavík",
        "languages": [
            "Icelandic"
        ],
        "population": 334300,
        "flag": "https://restcountries.eu/data/isl.svg",
        "currency": "Icelandic króna"
    },
    {
        "name": "India",
        "capital": "New Delhi",
        "languages": [
            "Hindi",
            "English"
        ],
        "population": 1295210000,
        "flag": "https://restcountries.eu/data/ind.svg",
        "currency": "Indian rupee"
    },
    {
        "name": "Indonesia",
        "capital": "Jakarta",
        "languages": [
            "Indonesian"
        ],
        "population": 258705000,
        "flag": "https://restcountries.eu/data/idn.svg",
        "currency": "Indonesian rupiah"
    },
    {
        "name": "Côte d'Ivoire",
        "capital": "Yamoussoukro",
        "languages": [
            "French"
        ],
        "population": 22671331,
        "flag": "https://restcountries.eu/data/civ.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Iran (Islamic Republic of)",
        "capital": "Tehran",
        "languages": [
            "Persian (Farsi)"
        ],
        "population": 79369900,
        "flag": "https://restcountries.eu/data/irn.svg",
        "currency": "Iranian rial"
    },
    {
        "name": "Iraq",
        "capital": "Baghdad",
        "languages": [
            "Arabic",
            "Kurdish"
        ],
        "population": 37883543,
        "flag": "https://restcountries.eu/data/irq.svg",
        "currency": "Iraqi dinar"
    },
    {
        "name": "Ireland",
        "capital": "Dublin",
        "languages": [
            "Irish",
            "English"
        ],
        "population": 6378000,
        "flag": "https://restcountries.eu/data/irl.svg",
        "currency": "Euro"
    },
    {
        "name": "Isle of Man",
        "capital": "Douglas",
        "languages": [
            "English",
            "Manx"
        ],
        "population": 84497,
        "flag": "https://restcountries.eu/data/imn.svg",
        "currency": "British pound"
    },
    {
        "name": "Israel",
        "capital": "Jerusalem",
        "languages": [
            "Hebrew (modern)",
            "Arabic"
        ],
        "population": 8527400,
        "flag": "https://restcountries.eu/data/isr.svg",
        "currency": "Israeli new shekel"
    },
    {
        "name": "Italy",
        "capital": "Rome",
        "languages": [
            "Italian"
        ],
        "population": 60665551,
        "flag": "https://restcountries.eu/data/ita.svg",
        "currency": "Euro"
    },
    {
        "name": "Jamaica",
        "capital": "Kingston",
        "languages": [
            "English"
        ],
        "population": 2723246,
        "flag": "https://restcountries.eu/data/jam.svg",
        "currency": "Jamaican dollar"
    },
    {
        "name": "Japan",
        "capital": "Tokyo",
        "languages": [
            "Japanese"
        ],
        "population": 126960000,
        "flag": "https://restcountries.eu/data/jpn.svg",
        "currency": "Japanese yen"
    },
    {
        "name": "Jersey",
        "capital": "Saint Helier",
        "languages": [
            "English",
            "French"
        ],
        "population": 100800,
        "flag": "https://restcountries.eu/data/jey.svg",
        "currency": "British pound"
    },
    {
        "name": "Jordan",
        "capital": "Amman",
        "languages": [
            "Arabic"
        ],
        "population": 9531712,
        "flag": "https://restcountries.eu/data/jor.svg",
        "currency": "Jordanian dinar"
    },
    {
        "name": "Kazakhstan",
        "capital": "Astana",
        "languages": [
            "Kazakh",
            "Russian"
        ],
        "population": 17753200,
        "flag": "https://restcountries.eu/data/kaz.svg",
        "currency": "Kazakhstani tenge"
    },
    {
        "name": "Kenya",
        "capital": "Nairobi",
        "languages": [
            "English",
            "Swahili"
        ],
        "population": 47251000,
        "flag": "https://restcountries.eu/data/ken.svg",
        "currency": "Kenyan shilling"
    },
    {
        "name": "Kiribati",
        "capital": "South Tarawa",
        "languages": [
            "English"
        ],
        "population": 113400,
        "flag": "https://restcountries.eu/data/kir.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Kuwait",
        "capital": "Kuwait City",
        "languages": [
            "Arabic"
        ],
        "population": 4183658,
        "flag": "https://restcountries.eu/data/kwt.svg",
        "currency": "Kuwaiti dinar"
    },
    {
        "name": "Kyrgyzstan",
        "capital": "Bishkek",
        "languages": [
            "Kyrgyz",
            "Russian"
        ],
        "population": 6047800,
        "flag": "https://restcountries.eu/data/kgz.svg",
        "currency": "Kyrgyzstani som"
    },
    {
        "name": "Lao People's Democratic Republic",
        "capital": "Vientiane",
        "languages": [
            "Lao"
        ],
        "population": 6492400,
        "flag": "https://restcountries.eu/data/lao.svg",
        "currency": "Lao kip"
    },
    {
        "name": "Latvia",
        "capital": "Riga",
        "languages": [
            "Latvian"
        ],
        "population": 1961600,
        "flag": "https://restcountries.eu/data/lva.svg",
        "currency": "Euro"
    },
    {
        "name": "Lebanon",
        "capital": "Beirut",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 5988000,
        "flag": "https://restcountries.eu/data/lbn.svg",
        "currency": "Lebanese pound"
    },
    {
        "name": "Lesotho",
        "capital": "Maseru",
        "languages": [
            "English",
            "Southern Sotho"
        ],
        "population": 1894194,
        "flag": "https://restcountries.eu/data/lso.svg",
        "currency": "Lesotho loti"
    },
    {
        "name": "Liberia",
        "capital": "Monrovia",
        "languages": [
            "English"
        ],
        "population": 4615000,
        "flag": "https://restcountries.eu/data/lbr.svg",
        "currency": "Liberian dollar"
    },
    {
        "name": "Libya",
        "capital": "Tripoli",
        "languages": [
            "Arabic"
        ],
        "population": 6385000,
        "flag": "https://restcountries.eu/data/lby.svg",
        "currency": "Libyan dinar"
    },
    {
        "name": "Liechtenstein",
        "capital": "Vaduz",
        "languages": [
            "German"
        ],
        "population": 37623,
        "flag": "https://restcountries.eu/data/lie.svg",
        "currency": "Swiss franc"
    },
    {
        "name": "Lithuania",
        "capital": "Vilnius",
        "languages": [
            "Lithuanian"
        ],
        "population": 2872294,
        "flag": "https://restcountries.eu/data/ltu.svg",
        "currency": "Euro"
    },
    {
        "name": "Luxembourg",
        "capital": "Luxembourg",
        "languages": [
            "French",
            "German",
            "Luxembourgish"
        ],
        "population": 576200,
        "flag": "https://restcountries.eu/data/lux.svg",
        "currency": "Euro"
    },
    {
        "name": "Macao",
        "capital": "",
        "languages": [
            "Chinese",
            "Portuguese"
        ],
        "population": 649100,
        "flag": "https://restcountries.eu/data/mac.svg",
        "currency": "Macanese pataca"
    },
    {
        "name": "Macedonia (the former Yugoslav Republic of)",
        "capital": "Skopje",
        "languages": [
            "Macedonian"
        ],
        "population": 2058539,
        "flag": "https://restcountries.eu/data/mkd.svg",
        "currency": "Macedonian denar"
    },
    {
        "name": "Madagascar",
        "capital": "Antananarivo",
        "languages": [
            "French",
            "Malagasy"
        ],
        "population": 22434363,
        "flag": "https://restcountries.eu/data/mdg.svg",
        "currency": "Malagasy ariary"
    },
    {
        "name": "Malawi",
        "capital": "Lilongwe",
        "languages": [
            "English",
            "Chichewa"
        ],
        "population": 16832910,
        "flag": "https://restcountries.eu/data/mwi.svg",
        "currency": "Malawian kwacha"
    },
    {
        "name": "Malaysia",
        "capital": "Kuala Lumpur",
        "languages": [
            "Malaysian"
        ],
        "population": 31405416,
        "flag": "https://restcountries.eu/data/mys.svg",
        "currency": "Malaysian ringgit"
    },
    {
        "name": "Maldives",
        "capital": "Malé",
        "languages": [
            "Divehi"
        ],
        "population": 344023,
        "flag": "https://restcountries.eu/data/mdv.svg",
        "currency": "Maldivian rufiyaa"
    },
    {
        "name": "Mali",
        "capital": "Bamako",
        "languages": [
            "French"
        ],
        "population": 18135000,
        "flag": "https://restcountries.eu/data/mli.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Malta",
        "capital": "Valletta",
        "languages": [
            "Maltese",
            "English"
        ],
        "population": 425384,
        "flag": "https://restcountries.eu/data/mlt.svg",
        "currency": "Euro"
    },
    {
        "name": "Marshall Islands",
        "capital": "Majuro",
        "languages": [
            "English",
            "Marshallese"
        ],
        "population": 54880,
        "flag": "https://restcountries.eu/data/mhl.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Martinique",
        "capital": "Fort-de-France",
        "languages": [
            "French"
        ],
        "population": 378243,
        "flag": "https://restcountries.eu/data/mtq.svg",
        "currency": "Euro"
    },
    {
        "name": "Mauritania",
        "capital": "Nouakchott",
        "languages": [
            "Arabic"
        ],
        "population": 3718678,
        "flag": "https://restcountries.eu/data/mrt.svg",
        "currency": "Mauritanian ouguiya"
    },
    {
        "name": "Mauritius",
        "capital": "Port Louis",
        "languages": [
            "English"
        ],
        "population": 1262879,
        "flag": "https://restcountries.eu/data/mus.svg",
        "currency": "Mauritian rupee"
    },
    {
        "name": "Mayotte",
        "capital": "Mamoudzou",
        "languages": [
            "French"
        ],
        "population": 226915,
        "flag": "https://restcountries.eu/data/myt.svg",
        "currency": "Euro"
    },
    {
        "name": "Mexico",
        "capital": "Mexico City",
        "languages": [
            "Spanish"
        ],
        "population": 122273473,
        "flag": "https://restcountries.eu/data/mex.svg",
        "currency": "Mexican peso"
    },
    {
        "name": "Micronesia (Federated States of)",
        "capital": "Palikir",
        "languages": [
            "English"
        ],
        "population": 102800,
        "flag": "https://restcountries.eu/data/fsm.svg",
        "currency": "[D]"
    },
    {
        "name": "Moldova (Republic of)",
        "capital": "Chișinău",
        "languages": [
            "Romanian"
        ],
        "population": 3553100,
        "flag": "https://restcountries.eu/data/mda.svg",
        "currency": "Moldovan leu"
    },
    {
        "name": "Monaco",
        "capital": "Monaco",
        "languages": [
            "French"
        ],
        "population": 38400,
        "flag": "https://restcountries.eu/data/mco.svg",
        "currency": "Euro"
    },
    {
        "name": "Mongolia",
        "capital": "Ulan Bator",
        "languages": [
            "Mongolian"
        ],
        "population": 3093100,
        "flag": "https://restcountries.eu/data/mng.svg",
        "currency": "Mongolian tögrög"
    },
    {
        "name": "Montenegro",
        "capital": "Podgorica",
        "languages": [
            "Serbian",
            "Bosnian",
            "Albanian",
            "Croatian"
        ],
        "population": 621810,
        "flag": "https://restcountries.eu/data/mne.svg",
        "currency": "Euro"
    },
    {
        "name": "Montserrat",
        "capital": "Plymouth",
        "languages": [
            "English"
        ],
        "population": 4922,
        "flag": "https://restcountries.eu/data/msr.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Morocco",
        "capital": "Rabat",
        "languages": [
            "Arabic"
        ],
        "population": 33337529,
        "flag": "https://restcountries.eu/data/mar.svg",
        "currency": "Moroccan dirham"
    },
    {
        "name": "Mozambique",
        "capital": "Maputo",
        "languages": [
            "Portuguese"
        ],
        "population": 26423700,
        "flag": "https://restcountries.eu/data/moz.svg",
        "currency": "Mozambican metical"
    },
    {
        "name": "Myanmar",
        "capital": "Naypyidaw",
        "languages": [
            "Burmese"
        ],
        "population": 51419420,
        "flag": "https://restcountries.eu/data/mmr.svg",
        "currency": "Burmese kyat"
    },
    {
        "name": "Namibia",
        "capital": "Windhoek",
        "languages": [
            "English",
            "Afrikaans"
        ],
        "population": 2324388,
        "flag": "https://restcountries.eu/data/nam.svg",
        "currency": "Namibian dollar"
    },
    {
        "name": "Nauru",
        "capital": "Yaren",
        "languages": [
            "English",
            "Nauruan"
        ],
        "population": 10084,
        "flag": "https://restcountries.eu/data/nru.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Nepal",
        "capital": "Kathmandu",
        "languages": [
            "Nepali"
        ],
        "population": 28431500,
        "flag": "https://restcountries.eu/data/npl.svg",
        "currency": "Nepalese rupee"
    },
    {
        "name": "Netherlands",
        "capital": "Amsterdam",
        "languages": [
            "Dutch"
        ],
        "population": 17019800,
        "flag": "https://restcountries.eu/data/nld.svg",
        "currency": "Euro"
    },
    {
        "name": "New Caledonia",
        "capital": "Nouméa",
        "languages": [
            "French"
        ],
        "population": 268767,
        "flag": "https://restcountries.eu/data/ncl.svg",
        "currency": "CFP franc"
    },
    {
        "name": "New Zealand",
        "capital": "Wellington",
        "languages": [
            "English",
            "Māori"
        ],
        "population": 4697854,
        "flag": "https://restcountries.eu/data/nzl.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Nicaragua",
        "capital": "Managua",
        "languages": [
            "Spanish"
        ],
        "population": 6262703,
        "flag": "https://restcountries.eu/data/nic.svg",
        "currency": "Nicaraguan córdoba"
    },
    {
        "name": "Niger",
        "capital": "Niamey",
        "languages": [
            "French"
        ],
        "population": 20715000,
        "flag": "https://restcountries.eu/data/ner.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Nigeria",
        "capital": "Abuja",
        "languages": [
            "English"
        ],
        "population": 186988000,
        "flag": "https://restcountries.eu/data/nga.svg",
        "currency": "Nigerian naira"
    },
    {
        "name": "Niue",
        "capital": "Alofi",
        "languages": [
            "English"
        ],
        "population": 1470,
        "flag": "https://restcountries.eu/data/niu.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Norfolk Island",
        "capital": "Kingston",
        "languages": [
            "English"
        ],
        "population": 2302,
        "flag": "https://restcountries.eu/data/nfk.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Korea (Democratic People's Republic of)",
        "capital": "Pyongyang",
        "languages": [
            "Korean"
        ],
        "population": 25281000,
        "flag": "https://restcountries.eu/data/prk.svg",
        "currency": "North Korean won"
    },
    {
        "name": "Northern Mariana Islands",
        "capital": "Saipan",
        "languages": [
            "English",
            "Chamorro"
        ],
        "population": 56940,
        "flag": "https://restcountries.eu/data/mnp.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Norway",
        "capital": "Oslo",
        "languages": [
            "Norwegian",
            "Norwegian Bokmål",
            "Norwegian Nynorsk"
        ],
        "population": 5223256,
        "flag": "https://restcountries.eu/data/nor.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Oman",
        "capital": "Muscat",
        "languages": [
            "Arabic"
        ],
        "population": 4420133,
        "flag": "https://restcountries.eu/data/omn.svg",
        "currency": "Omani rial"
    },
    {
        "name": "Pakistan",
        "capital": "Islamabad",
        "languages": [
            "English",
            "Urdu"
        ],
        "population": 194125062,
        "flag": "https://restcountries.eu/data/pak.svg",
        "currency": "Pakistani rupee"
    },
    {
        "name": "Palau",
        "capital": "Ngerulmud",
        "languages": [
            "English"
        ],
        "population": 17950,
        "flag": "https://restcountries.eu/data/plw.svg",
        "currency": "[E]"
    },
    {
        "name": "Palestine, State of",
        "capital": "Ramallah",
        "languages": [
            "Arabic"
        ],
        "population": 4682467,
        "flag": "https://restcountries.eu/data/pse.svg",
        "currency": "Israeli new sheqel"
    },
    {
        "name": "Panama",
        "capital": "Panama City",
        "languages": [
            "Spanish"
        ],
        "population": 3814672,
        "flag": "https://restcountries.eu/data/pan.svg",
        "currency": "Panamanian balboa"
    },
    {
        "name": "Papua New Guinea",
        "capital": "Port Moresby",
        "languages": [
            "English"
        ],
        "population": 8083700,
        "flag": "https://restcountries.eu/data/png.svg",
        "currency": "Papua New Guinean kina"
    },
    {
        "name": "Paraguay",
        "capital": "Asunción",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 6854536,
        "flag": "https://restcountries.eu/data/pry.svg",
        "currency": "Paraguayan guaraní"
    },
    {
        "name": "Peru",
        "capital": "Lima",
        "languages": [
            "Spanish"
        ],
        "population": 31488700,
        "flag": "https://restcountries.eu/data/per.svg",
        "currency": "Peruvian sol"
    },
    {
        "name": "Philippines",
        "capital": "Manila",
        "languages": [
            "English"
        ],
        "population": 103279800,
        "flag": "https://restcountries.eu/data/phl.svg",
        "currency": "Philippine peso"
    },
    {
        "name": "Pitcairn",
        "capital": "Adamstown",
        "languages": [
            "English"
        ],
        "population": 56,
        "flag": "https://restcountries.eu/data/pcn.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Poland",
        "capital": "Warsaw",
        "languages": [
            "Polish"
        ],
        "population": 38437239,
        "flag": "https://restcountries.eu/data/pol.svg",
        "currency": "Polish złoty"
    },
    {
        "name": "Portugal",
        "capital": "Lisbon",
        "languages": [
            "Portuguese"
        ],
        "population": 10374822,
        "flag": "https://restcountries.eu/data/prt.svg",
        "currency": "Euro"
    },
    {
        "name": "Puerto Rico",
        "capital": "San Juan",
        "languages": [
            "Spanish",
            "English"
        ],
        "population": 3474182,
        "flag": "https://restcountries.eu/data/pri.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Qatar",
        "capital": "Doha",
        "languages": [
            "Arabic"
        ],
        "population": 2587564,
        "flag": "https://restcountries.eu/data/qat.svg",
        "currency": "Qatari riyal"
    },
    {
        "name": "Republic of Kosovo",
        "capital": "Pristina",
        "languages": [
            "Albanian",
            "Serbian"
        ],
        "population": 1733842,
        "flag": "https://restcountries.eu/data/kos.svg",
        "currency": "Euro"
    },
    {
        "name": "Réunion",
        "capital": "Saint-Denis",
        "languages": [
            "French"
        ],
        "population": 840974,
        "flag": "https://restcountries.eu/data/reu.svg",
        "currency": "Euro"
    },
    {
        "name": "Romania",
        "capital": "Bucharest",
        "languages": [
            "Romanian"
        ],
        "population": 19861408,
        "flag": "https://restcountries.eu/data/rou.svg",
        "currency": "Romanian leu"
    },
    {
        "name": "Russian Federation",
        "capital": "Moscow",
        "languages": [
            "Russian"
        ],
        "population": 146599183,
        "flag": "https://restcountries.eu/data/rus.svg",
        "currency": "Russian ruble"
    },
    {
        "name": "Rwanda",
        "capital": "Kigali",
        "languages": [
            "Kinyarwanda",
            "English",
            "French"
        ],
        "population": 11553188,
        "flag": "https://restcountries.eu/data/rwa.svg",
        "currency": "Rwandan franc"
    },
    {
        "name": "Saint Barthélemy",
        "capital": "Gustavia",
        "languages": [
            "French"
        ],
        "population": 9417,
        "flag": "https://restcountries.eu/data/blm.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Helena, Ascension and Tristan da Cunha",
        "capital": "Jamestown",
        "languages": [
            "English"
        ],
        "population": 4255,
        "flag": "https://restcountries.eu/data/shn.svg",
        "currency": "Saint Helena pound"
    },
    {
        "name": "Saint Kitts and Nevis",
        "capital": "Basseterre",
        "languages": [
            "English"
        ],
        "population": 46204,
        "flag": "https://restcountries.eu/data/kna.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Saint Lucia",
        "capital": "Castries",
        "languages": [
            "English"
        ],
        "population": 186000,
        "flag": "https://restcountries.eu/data/lca.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Saint Martin (French part)",
        "capital": "Marigot",
        "languages": [
            "English",
            "French",
            "Dutch"
        ],
        "population": 36979,
        "flag": "https://restcountries.eu/data/maf.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Pierre and Miquelon",
        "capital": "Saint-Pierre",
        "languages": [
            "French"
        ],
        "population": 6069,
        "flag": "https://restcountries.eu/data/spm.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Vincent and the Grenadines",
        "capital": "Kingstown",
        "languages": [
            "English"
        ],
        "population": 109991,
        "flag": "https://restcountries.eu/data/vct.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Samoa",
        "capital": "Apia",
        "languages": [
            "Samoan",
            "English"
        ],
        "population": 194899,
        "flag": "https://restcountries.eu/data/wsm.svg",
        "currency": "Samoan tālā"
    },
    {
        "name": "San Marino",
        "capital": "City of San Marino",
        "languages": [
            "Italian"
        ],
        "population": 33005,
        "flag": "https://restcountries.eu/data/smr.svg",
        "currency": "Euro"
    },
    {
        "name": "Sao Tome and Principe",
        "capital": "São Tomé",
        "languages": [
            "Portuguese"
        ],
        "population": 187356,
        "flag": "https://restcountries.eu/data/stp.svg",
        "currency": "São Tomé and Príncipe dobra"
    },
    {
        "name": "Saudi Arabia",
        "capital": "Riyadh",
        "languages": [
            "Arabic"
        ],
        "population": 32248200,
        "flag": "https://restcountries.eu/data/sau.svg",
        "currency": "Saudi riyal"
    },
    {
        "name": "Senegal",
        "capital": "Dakar",
        "languages": [
            "French"
        ],
        "population": 14799859,
        "flag": "https://restcountries.eu/data/sen.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Serbia",
        "capital": "Belgrade",
        "languages": [
            "Serbian"
        ],
        "population": 7076372,
        "flag": "https://restcountries.eu/data/srb.svg",
        "currency": "Serbian dinar"
    },
    {
        "name": "Seychelles",
        "capital": "Victoria",
        "languages": [
            "French",
            "English"
        ],
        "population": 91400,
        "flag": "https://restcountries.eu/data/syc.svg",
        "currency": "Seychellois rupee"
    },
    {
        "name": "Sierra Leone",
        "capital": "Freetown",
        "languages": [
            "English"
        ],
        "population": 7075641,
        "flag": "https://restcountries.eu/data/sle.svg",
        "currency": "Sierra Leonean leone"
    },
    {
        "name": "Singapore",
        "capital": "Singapore",
        "languages": [
            "English",
            "Malay",
            "Tamil",
            "Chinese"
        ],
        "population": 5535000,
        "flag": "https://restcountries.eu/data/sgp.svg",
        "currency": "Brunei dollar"
    },
    {
        "name": "Sint Maarten (Dutch part)",
        "capital": "Philipsburg",
        "languages": [
            "Dutch",
            "English"
        ],
        "population": 38247,
        "flag": "https://restcountries.eu/data/sxm.svg",
        "currency": "Netherlands Antillean guilder"
    },
    {
        "name": "Slovakia",
        "capital": "Bratislava",
        "languages": [
            "Slovak"
        ],
        "population": 5426252,
        "flag": "https://restcountries.eu/data/svk.svg",
        "currency": "Euro"
    },
    {
        "name": "Slovenia",
        "capital": "Ljubljana",
        "languages": [
            "Slovene"
        ],
        "population": 2064188,
        "flag": "https://restcountries.eu/data/svn.svg",
        "currency": "Euro"
    },
    {
        "name": "Solomon Islands",
        "capital": "Honiara",
        "languages": [
            "English"
        ],
        "population": 642000,
        "flag": "https://restcountries.eu/data/slb.svg",
        "currency": "Solomon Islands dollar"
    },
    {
        "name": "Somalia",
        "capital": "Mogadishu",
        "languages": [
            "Somali",
            "Arabic"
        ],
        "population": 11079000,
        "flag": "https://restcountries.eu/data/som.svg",
        "currency": "Somali shilling"
    },
    {
        "name": "South Africa",
        "capital": "Pretoria",
        "languages": [
            "Afrikaans",
            "English",
            "Southern Ndebele",
            "Southern Sotho",
            "Swati",
            "Tswana",
            "Tsonga",
            "Venda",
            "Xhosa",
            "Zulu"
        ],
        "population": 55653654,
        "flag": "https://restcountries.eu/data/zaf.svg",
        "currency": "South African rand"
    },
    {
        "name": "South Georgia and the South Sandwich Islands",
        "capital": "King Edward Point",
        "languages": [
            "English"
        ],
        "population": 30,
        "flag": "https://restcountries.eu/data/sgs.svg",
        "currency": "British pound"
    },
    {
        "name": "Korea (Republic of)",
        "capital": "Seoul",
        "languages": [
            "Korean"
        ],
        "population": 50801405,
        "flag": "https://restcountries.eu/data/kor.svg",
        "currency": "South Korean won"
    },
    {
        "name": "South Sudan",
        "capital": "Juba",
        "languages": [
            "English"
        ],
        "population": 12131000,
        "flag": "https://restcountries.eu/data/ssd.svg",
        "currency": "South Sudanese pound"
    },
    {
        "name": "Spain",
        "capital": "Madrid",
        "languages": [
            "Spanish"
        ],
        "population": 46438422,
        "flag": "https://restcountries.eu/data/esp.svg",
        "currency": "Euro"
    },
    {
        "name": "Sri Lanka",
        "capital": "Colombo",
        "languages": [
            "Sinhalese",
            "Tamil"
        ],
        "population": 20966000,
        "flag": "https://restcountries.eu/data/lka.svg",
        "currency": "Sri Lankan rupee"
    },
    {
        "name": "Sudan",
        "capital": "Khartoum",
        "languages": [
            "Arabic",
            "English"
        ],
        "population": 39598700,
        "flag": "https://restcountries.eu/data/sdn.svg",
        "currency": "Sudanese pound"
    },
    {
        "name": "Suriname",
        "capital": "Paramaribo",
        "languages": [
            "Dutch"
        ],
        "population": 541638,
        "flag": "https://restcountries.eu/data/sur.svg",
        "currency": "Surinamese dollar"
    },
    {
        "name": "Svalbard and Jan Mayen",
        "capital": "Longyearbyen",
        "languages": [
            "Norwegian"
        ],
        "population": 2562,
        "flag": "https://restcountries.eu/data/sjm.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Swaziland",
        "capital": "Lobamba",
        "languages": [
            "English",
            "Swati"
        ],
        "population": 1132657,
        "flag": "https://restcountries.eu/data/swz.svg",
        "currency": "Swazi lilangeni"
    },
    {
        "name": "Sweden",
        "capital": "Stockholm",
        "languages": [
            "Swedish"
        ],
        "population": 9894888,
        "flag": "https://restcountries.eu/data/swe.svg",
        "currency": "Swedish krona"
    },
    {
        "name": "Switzerland",
        "capital": "Bern",
        "languages": [
            "German",
            "French",
            "Italian"
        ],
        "population": 8341600,
        "flag": "https://restcountries.eu/data/che.svg",
        "currency": "Swiss franc"
    },
    {
        "name": "Syrian Arab Republic",
        "capital": "Damascus",
        "languages": [
            "Arabic"
        ],
        "population": 18564000,
        "flag": "https://restcountries.eu/data/syr.svg",
        "currency": "Syrian pound"
    },
    {
        "name": "Taiwan",
        "capital": "Taipei",
        "languages": [
            "Chinese"
        ],
        "population": 23503349,
        "flag": "https://restcountries.eu/data/twn.svg",
        "currency": "New Taiwan dollar"
    },
    {
        "name": "Tajikistan",
        "capital": "Dushanbe",
        "languages": [
            "Tajik",
            "Russian"
        ],
        "population": 8593600,
        "flag": "https://restcountries.eu/data/tjk.svg",
        "currency": "Tajikistani somoni"
    },
    {
        "name": "Tanzania, United Republic of",
        "capital": "Dodoma",
        "languages": [
            "Swahili",
            "English"
        ],
        "population": 55155000,
        "flag": "https://restcountries.eu/data/tza.svg",
        "currency": "Tanzanian shilling"
    },
    {
        "name": "Thailand",
        "capital": "Bangkok",
        "languages": [
            "Thai"
        ],
        "population": 65327652,
        "flag": "https://restcountries.eu/data/tha.svg",
        "currency": "Thai baht"
    },
    {
        "name": "Timor-Leste",
        "capital": "Dili",
        "languages": [
            "Portuguese"
        ],
        "population": 1167242,
        "flag": "https://restcountries.eu/data/tls.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Togo",
        "capital": "Lomé",
        "languages": [
            "French"
        ],
        "population": 7143000,
        "flag": "https://restcountries.eu/data/tgo.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Tokelau",
        "capital": "Fakaofo",
        "languages": [
            "English"
        ],
        "population": 1411,
        "flag": "https://restcountries.eu/data/tkl.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Tonga",
        "capital": "Nuku'alofa",
        "languages": [
            "English",
            "Tonga (Tonga Islands)"
        ],
        "population": 103252,
        "flag": "https://restcountries.eu/data/ton.svg",
        "currency": "Tongan paʻanga"
    },
    {
        "name": "Trinidad and Tobago",
        "capital": "Port of Spain",
        "languages": [
            "English"
        ],
        "population": 1349667,
        "flag": "https://restcountries.eu/data/tto.svg",
        "currency": "Trinidad and Tobago dollar"
    },
    {
        "name": "Tunisia",
        "capital": "Tunis",
        "languages": [
            "Arabic"
        ],
        "population": 11154400,
        "flag": "https://restcountries.eu/data/tun.svg",
        "currency": "Tunisian dinar"
    },
    {
        "name": "Turkey",
        "capital": "Ankara",
        "languages": [
            "Turkish"
        ],
        "population": 78741053,
        "flag": "https://restcountries.eu/data/tur.svg",
        "currency": "Turkish lira"
    },
    {
        "name": "Turkmenistan",
        "capital": "Ashgabat",
        "languages": [
            "Turkmen",
            "Russian"
        ],
        "population": 4751120,
        "flag": "https://restcountries.eu/data/tkm.svg",
        "currency": "Turkmenistan manat"
    },
    {
        "name": "Turks and Caicos Islands",
        "capital": "Cockburn Town",
        "languages": [
            "English"
        ],
        "population": 31458,
        "flag": "https://restcountries.eu/data/tca.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Tuvalu",
        "capital": "Funafuti",
        "languages": [
            "English"
        ],
        "population": 10640,
        "flag": "https://restcountries.eu/data/tuv.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Uganda",
        "capital": "Kampala",
        "languages": [
            "English",
            "Swahili"
        ],
        "population": 33860700,
        "flag": "https://restcountries.eu/data/uga.svg",
        "currency": "Ugandan shilling"
    },
    {
        "name": "Ukraine",
        "capital": "Kiev",
        "languages": [
            "Ukrainian"
        ],
        "population": 42692393,
        "flag": "https://restcountries.eu/data/ukr.svg",
        "currency": "Ukrainian hryvnia"
    },
    {
        "name": "United Arab Emirates",
        "capital": "Abu Dhabi",
        "languages": [
            "Arabic"
        ],
        "population": 9856000,
        "flag": "https://restcountries.eu/data/are.svg",
        "currency": "United Arab Emirates dirham"
    },
    {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "capital": "London",
        "languages": [
            "English"
        ],
        "population": 65110000,
        "flag": "https://restcountries.eu/data/gbr.svg",
        "currency": "British pound"
    },
    {
        "name": "United States of America",
        "capital": "Washington, D.C.",
        "languages": [
            "English"
        ],
        "population": 323947000,
        "flag": "https://restcountries.eu/data/usa.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Uruguay",
        "capital": "Montevideo",
        "languages": [
            "Spanish"
        ],
        "population": 3480222,
        "flag": "https://restcountries.eu/data/ury.svg",
        "currency": "Uruguayan peso"
    },
    {
        "name": "Uzbekistan",
        "capital": "Tashkent",
        "languages": [
            "Uzbek",
            "Russian"
        ],
        "population": 31576400,
        "flag": "https://restcountries.eu/data/uzb.svg",
        "currency": "Uzbekistani so'm"
    },
    {
        "name": "Vanuatu",
        "capital": "Port Vila",
        "languages": [
            "Bislama",
            "English",
            "French"
        ],
        "population": 277500,
        "flag": "https://restcountries.eu/data/vut.svg",
        "currency": "Vanuatu vatu"
    },
    {
        "name": "Venezuela (Bolivarian Republic of)",
        "capital": "Caracas",
        "languages": [
            "Spanish"
        ],
        "population": 31028700,
        "flag": "https://restcountries.eu/data/ven.svg",
        "currency": "Venezuelan bolívar"
    },
    {
        "name": "Viet Nam",
        "capital": "Hanoi",
        "languages": [
            "Vietnamese"
        ],
        "population": 92700000,
        "flag": "https://restcountries.eu/data/vnm.svg",
        "currency": "Vietnamese đồng"
    },
    {
        "name": "Wallis and Futuna",
        "capital": "Mata-Utu",
        "languages": [
            "French"
        ],
        "population": 11750,
        "flag": "https://restcountries.eu/data/wlf.svg",
        "currency": "CFP franc"
    },
    {
        "name": "Western Sahara",
        "capital": "El Aaiún",
        "languages": [
            "Spanish"
        ],
        "population": 510713,
        "flag": "https://restcountries.eu/data/esh.svg",
        "currency": "Moroccan dirham"
    },
    {
        "name": "Yemen",
        "capital": "Sana'a",
        "languages": [
            "Arabic"
        ],
        "population": 27478000,
        "flag": "https://restcountries.eu/data/yem.svg",
        "currency": "Yemeni rial"
    },
    {
        "name": "Zambia",
        "capital": "Lusaka",
        "languages": [
            "English"
        ],
        "population": 15933883,
        "flag": "https://restcountries.eu/data/zmb.svg",
        "currency": "Zambian kwacha"
    },
    {
        "name": "Zimbabwe",
        "capital": "Harare",
        "languages": [
            "English",
            "Shona",
            "Northern Ndebele"
        ],
        "population": 14240168,
        "flag": "https://restcountries.eu/data/zwe.svg",
        "currency": "Botswana pula"
    }
]


def most_spoken_languages(countries):
    all_languages = []
    
    for key in countries:
        if 'languages' in key:
            for i in key['languages']:
                all_languages.append(i)

    # Let's find the most popular languages
    lang_counts = {}
    for item in all_languages:
        if item in lang_counts:
            lang_counts[item] += 1
        else:
            lang_counts[item] = 1

    sorted_langs = sorted(lang_counts.keys(), key=lang_counts.get, reverse=True)    
    
    top_languages = sorted_langs[:10]  # Change to 20 if needed
    return top_languages

print(most_spoken_languages(countries_data))

def most_populated_countries(countries):
    most_populated = list()

    for item in countries:
        new_data = {
            'name': item['name'],
            'population': item['population']
        }
        if new_data['population'] >= 100000000:
            most_populated.append(new_data)
    
    return most_populated[:10]    
            
print(most_populated_countries(countries_data))