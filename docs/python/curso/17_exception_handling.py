# 30 Days Of Python: Day 17 - Exception Handling

"""Day 17
Exception Handling
Python uses try and except to handle errors gracefully. A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result. Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our application more robust. The cause of an exception is often external to the program itself. An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. Graceful handling of errors prevents our applications from crashing.

We have covered the different Python error types in the previous section. If we use try and except in our program, then it will not raise errors in those blocks.

Try and Except

try:
    code in this block if things go well
except:
    code in this block run if things go wrong
Example:

try:
    print(10 + '5')
except:
    print('Something went wrong')
In the example above the second operand is a string. We could change it to float or int to add it with the number to make it work. But without any changes, the second block, except, will be executed.

"""

# Example code
# def user_data():
#     try:
#         name = input('Enter your name: ')
#         age = int(input('Enter your age: '))
#         return (f'Name: {name}, Age: {age}')
#     except ValueError:
#         return ('Invalid input. Age should be a number.')
        
# print(user_data())

"""
In the above example, the exception block will run and we do not know exactly the problem. To analyze the problem, we can use the different error types with except.

In the following example, it will handle the error and will also tell us the kind of error raised.
"""

# Example code
# def user_age():
#     try:
#         name = input('Enter your name: ')
#         year = input('Enter the year you were born: ')
#         age = 2024 - year
#         return (f'You are {name}. And your age is {age}')
#     except TypeError:
#         return 'Type error occured'
#     except ValueError:
#         return 'Value error occured'
#     except ZeroDivisionError:
#         return 'Zero division error occured'
    
# print(user_age())
""" With this example we have a TypeError code because when we enter the year we were born, because we don't specified if it is an integer value or a string, later at the age variable we can't perform the operation.
To fix this error we can convert the value into a integer when we ask for the year or at the operation. Let's fix this code by adding the integer convertion
"""
# def user_age1():
#     try:
#         name = input('Enter your name: ')
#         year = input('Enter the year you were born: ')
#         age = 2024 - int(year) # here we convert year to integer
#         return (f'You are {name}. And your age is {age}')
#     except TypeError:
#         return 'Type error occured'
#     except ValueError:
#         return 'Value error occured'
#     except ZeroDivisionError:
#         return 'Zero division error occured'
#     else:
#         print('I usually run with the try block')
#     finally:
#         print('I alway run.')
    
# print(user_age1())

""" 
We can shorten our code usign the following sintax: except Exception as e:. So our code will be
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
"""

"""
Packing and Unpacking Arguments in Python
We use two operators:

* for tuples
** for dictionaries
Let us take as an example below. It takes only arguments but we have list. We can unpack the list and changes to argument.

"""

# Unpacking
# Unpacking Lists

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
"""
print(sum_of_five_nums(lst))

This type of unpacking will return a TypeError:
TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
This function takes numbers, not a list as an argument. That is why we need to unpack or destructure the list.

To fix this error we are required to add the * before the lst
"""
print(sum_of_five_nums(*lst)) # Now the list is unpacked and the function return the result

"""We can also use unpacking in the range built-in function that expects a start and an end."""

numbers = range(2, 7)
print(type(numbers)) 
print(numbers) # This does nothing we have a string, we need to convert numbers into a list to our numbers
print(list(numbers))

# We can also have a list and use it as a range
args = [2, 7]
# numb_args = range(args)
# print(numb_args)
"""
This numb_args = range(args) will give us an error, TypeError: 'list' object cannot be interpreted as an integer. It happens because we didn't unpack the list in our range
"""
# Now we unpack the args in our range
numb_args = range(*args)
print(list(numb_args)) # Don't forget to convert the variable into a list

"""A list or a tuple can also be unpacked like this:"""

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, *rest) # Because I use the * the last arguments also unpack too.
print(fin, sw, nor, rest)
print(type(fin)) # This is a string
print(type(rest)) # This is a list

numbers1 = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers1
print(one, middle, last)
# print(one, *middle, last)
print(type(one)) # This is a integer
print(type(middle)) # This is a list

"""Unpacking Dictionaries"""
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {
    'name':'Asabeneh', 
    'country':'Finland', 
    'city':'Helsinki', 
    'age':23}

"""
print(unpacking_person_info(dct)) This command give us the same error that we have with the list
TypeError: unpacking_person_info() missing 3 required positional arguments: 'country', 'city', and 'age'

If we user the command print(unpacking_person_info(*dct)) the dictionary doesn't unpack correctly. We are required to use the double **

"""
print(unpacking_person_info(**dct))

"""Packing

Sometimes we never know how many arguments need to be passed to a python function. We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.

Packing Lists

"""

def sum_all_args(*args):
    s = 0 # variable to start counting
    for i in args: # loop to pass through all the args we passed
        s += i
    return s

print(sum_all_args(1, 2, 3))             # 6
print(sum_all_args(1, 2, 3, 4, 5, 6, 7)) # 28

"""
Packing Dictionaries

Remember when we pack dictionaries we are required to use the two ** before the args. And we are going to call them kwargs. Also remember to check if the type of the args passed are a dictionary.

"""
def packing_person_name(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    # Again we need to create a loop to pass through all the kwargs we passed to our function
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_name(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

"""
Spreading in Python

Like in JavaScript, spreading is possible in Python. Let us check it in an example below:

By usign the * we can spread list into another list.

"""
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
# We can create a new list spreading the other ones =>
lst_spread = [0, *lst_one, *lst_two]
# Remember to spread a list into another list we need to use the * infront of our var name
print(type(lst_spread))
print(lst_spread)

country_lst_one = ['Brasil', 'Argentina', 'Colombia']
country_lst_two = ['Alemania', 'España', 'Inglaterra', 'Dinamarca']
country_spread_lst = ['Suecia', 'Francia', *country_lst_one, *country_lst_two]
print(type(country_spread_lst))
print(country_spread_lst)
# The list will be spread in the order we put them into the new list.

"""
Enumerate

If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list.

It's like having or displaying the values into a table, were the index is the row and then the value
"""
def index_with_enumerate():
    lst = [20, 30, 40]
    for index, item in enumerate(lst):
        print( index, item )
    
print(index_with_enumerate())

def country_salute(countries):
    for index, i in enumerate(countries):
        print('hi')
        if i == 'Argentina':
            print(f'The country {i} has been found at index {index}')
            
print(country_salute(country_lst_one))

"""
Zip

Sometimes we would like to combine lists when looping through them. See the example below:

"""

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

"""
Exercises: Day 17

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

"""

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
names_inverted = names[::-1]
*nordic_countries, es, ru = names
print(names_inverted)
print(nordic_countries, es, ru)