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

"""Packing"""