# 30 Days Of Python: Day 13 - List Comprehension

"""List Comprehension
List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.

# syntax
[i for i in iterable if expression]
Example:1

For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:

# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']
Example:2

For instance if you want to generate a list of numbers

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
Example:2

List comprehension can be combined with if expression

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# One way without list comprehension
language = "Python"
lst = list(language)
print(type(lst))
print(lst)

# Using list comprehension
lst_c = [i for i in language]
print(type(lst_c))
print(lst_c)

# Create a list of numbers
numbers = [i for i in range(11)]
print(type(numbers))
print(numbers)

# We can create tuples and also use operations
tpl_num = [(i, i * i) for i in range(11)]
print(type(tpl_num))
print(tpl_num)

# Also combine them with expressions
even_num = [i for i in range(21) if i % 2 == 0]
print(type(even_num))
print(even_num)

odd_num = [i for i in range(21) if i % 2 != 0]
print(type(odd_num))
print(odd_num)

"""Lambda Function
Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another function.

Creating a Lambda Function
To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression. See the syntax and the example below. Lambda function does not use return but it explicitly returns the expression.

# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
"""

# Let's say we have the following function
def add_num(a, b):
    return a + b

print(add_num(5, 9))

# With a Lambda function we can write it into a variable
add_two_num_lambda = lambda a, b: a + b
# After we use the lambda word, we need to specify the arguments we are going to pass
# then we use the dot notation : and then the expression a + b
# Let's call our lambda function
print(add_two_num_lambda(5, 12))

# self invoke lambda
invoke_lambda = (lambda a, b: a * b)(2, 3)
print(invoke_lambda)
# When we finish writing the lambda function we pass the arguments, remember to put both into ()

square = lambda a: a ** 2
cube = lambda b: b ** 3
print(square(2))
print(f'The square of 2 is {square(2)}')
print(cube(3))
print(f'The cube of 3 is {cube(3)}')

# Lambda with multiple variables
multi_var_lambda = lambda a, b, c: (a ** 2) - (3 * b) + (4 * c)
print(multi_var_lambda(3, 5, 2))

"""Lambda Function Inside Another Function
Using a lambda function inside another function.

Example:

def power(x):
    return lambda n : x ** n
    
"""

def power(x):
    return lambda n: x ** n

func_lambda = power(2)(3) # Our function will need two arguments to work, we pass them separate
print(func_lambda)
two_power_five = power(2)(5)
print(two_power_five)

# EXERCISES DAY 13

#1
numbers1 = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_num = [i for i in numbers1 if i < 0]
positive_num = [i for i in numbers1 if i >= 0]
print(negative_num)
print(positive_num)

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flttd_list = [number for row in list_of_lists for number in row]
flattened_list = [number for row in flttd_list for number in row]
print(flattened_list)

#3
lst_of_tuples = [(i, 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
for tup in lst_of_tuples:
    print(f'{tup}')
    

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

upper_countries = [
    (country[0].upper(), country[0][:3].upper(), country[1].upper()) 
    for country_lst in countries
    for country in country_lst]
    
print(upper_countries)

#5
country_dict = [
    {'country':country[0].upper(), 'city':country[1].upper()} 
    for country_lst in countries 
    for country in country_lst]
print(country_dict)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

con_strings = [' '.join(name) 
               for name_list in names 
               for name in name_list]

print(con_strings)

#7
