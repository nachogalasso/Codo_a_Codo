# 30 Days Of Python: Day 12 - Modules

"""What is a Module
A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

Creating a Module
To create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py inside your project folder. Let us write some code in this file.

# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
Create main.py file in your project directory and import the mymodule.py file.

Importing a Module
To import the file we use the import keyword and the name of the file only.

# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
Import Functions from a Module
We can have many functions in a file and we can import all the functions differently.

Now let's import the module from mymodule.py
"""

from hashlib import new
import mymodule # then we will required to indicate the module and function

# Let's use the function inside mymodule.py
print(mymodule.generate_full_name('Tito', 'Carganza'))

"""
To import the function first we need to indicate where the function is located. But we can also indicate when we import the module wich functions we want use from that module. When we do that we don't need to specify the module name of where the function is located

Import Functions from a Module
We can have many functions in a file and we can import all the functions differently.
"""

from mymodule import generate_full_name, sum_two_numbs, get_weight, person_test, get_person

print(generate_full_name('Carlos', 'Escoba'))
print(sum_two_numbs(5, 7))
print(get_weight(110))
# I can also import a variable or a dictionary
print(person_test['first_name'])
print(get_person(person_test))

"""Import Functions from a Module and Renaming
During importing we can rename the name of the module.

We can also import functions and rename them for a more convenient use

from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

Now instead of calling our functions by the name that we declare them in mymodule.py by using the 'as' and indicate the name we want to assign to the functions, later we will call them by using this new name we assign to the function
"""

"""Import Built-in Modules
Like other programming languages we can also import modules by importing the file/function using the key word import. Let's import the common module we will use most of the time. Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re

The built-in modules are those that came with python, we are not required to install them and we can use by importing them into our file. 

REMEMBER to always import the modules at the beginning of our new file.

Also if we want to import all the functions into a module we can use the following command:
from mymodule import *
The * will import all the data contained into our module

Note that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code. However, it is okay to use it to save typing in interactive sessions.

With the built-in modules we can rename their functions if we want to.

"""

"""BUILT-IN MODULES

OS Module
Using python os module it is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.

# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
Sys Module
The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

Example of a script.py file:

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
Now to check how this script works I wrote in command line:

python script.py Asabeneh 30DaysOfPython
The result:

Welcome Asabeneh. Enjoy  30DayOfPython challenge! 
Some useful sys commands:

# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
Statistics Module
The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
Math Module
Module containing many mathematical operations and constants.

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
Now, we have imported the math module which contains lots of function which can help us to perform mathematical calculations. To check what functions the module has got, we can use help(math), or dir(math). This will display the available functions in the module. If we want to import only a specific function from the module we import it as follows:

from math import pi
print(pi)
It is also possible to import multiple functions at once

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2
But if we want to import all the function in math module we can use * .

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
When we import we can also rename the name of the function.

from math import pi as  PI
print(PI) # 3.141592653589793
String Module
A string module is a useful module for many purposes. The example below shows some use of the string module.

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
Random Module
By now you are familiar with importing modules. Let us do one more import to get very familiar with it. Let us import random module which gives us a random number between 0 and 0.9999.... The random module has lots of functions but in this section we will only use random and randint.

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

"""

# EXERCISES DAY 12

#1
import string
from random import randint
import random

print(string.ascii_letters) 
print(string.digits) 

def random_user_id():
    rand_letter = []
    rand_num = []
    
    for i in string.digits:
        rand_num += i
    
    for j in string.ascii_letters:
        rand_letter += j   

    full_list = rand_letter + rand_num
    lst_index = []
    for i in range(0, 6): 
        lst_index.append(randint(0, len(full_list)))
    
    
    user_id = ''.join(full_list[index] for index in lst_index)        
    return user_id      


print(f'Your user id is: {random_user_id()}')

#2
def cht_list():
    rand_letter = []
    rand_num = []
    
    for i in string.digits:
        rand_num += i
    
    for j in string.ascii_letters:
        rand_letter += j   

    full_list = rand_letter + rand_num
    
    return full_list

def total_num_id(lst):
    id_range = int(input('Please indicate the number of characters for your ID:'))
    total_id = int(input("How many id's do you need?"))
    user_ids = []
    
    for i in range(total_id): 
        lst_index = []
        for j in range(id_range):
            lst_index.append(randint(0, len(lst) - 1))
        user_id = ''.join(lst[index] for index in lst_index)
        user_ids.append(user_id)
    
    return user_ids    


# user_ids = total_num_id(cht_list())
# for user_id in user_ids:
#     print(f'Your user id is:', {user_id})

#3
def rgb_color_gen():
    num1= randint(0, 256)
    num2= randint(0, 256)
    num3= randint(0, 256)
    return f'rgb({num1}, {num2}, {num3})'

print('Your random rgb color is: ', rgb_color_gen())

# Exercises 2

#1
def list_of_hexa_colors(num):
    h_lst = []
    hexa_colors = []
    
    for i in string.ascii_letters:
        h_lst += i
        if i == 'f':
            break

    for j in string.digits:
        h_lst.append(j)
    

    for k in range(num):
        hexa = []
        for n in range(0, 6):
            hexa.append(randint(0, len(h_lst) - 1))
        color = ''.join(h_lst[index] for index in hexa)
        h_color = '#' + color
        hexa_colors.append(h_color)
    
    return hexa_colors
   

def list_of_rgb_colors(num):
    rgb_colors = []
    
    for i in range(num):
        num1= randint(0, 256)
        num2= randint(0, 256)
        num3= randint(0, 256)
        rgb_colors.append(f'rgb({num1}, {num2}, {num3})')
        
    return rgb_colors

print(list_of_hexa_colors(3))
print(list_of_rgb_colors(3))


def generate_colors(str, num):
    
    if str == 'hexa':
        return list_of_hexa_colors(num)
    else:
        return list_of_rgb_colors(num)
    

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

# Exercises 3

#1
def shuffled_lst(lst):
    print(lst)
    n = len(lst)
    
    for i in range(n-1, 0, -1):
        q = randint(0, i)
        lst[i], lst[q] = lst[q], lst[i]
    
    return lst
    

lst_to_shuffle = [0, 1, 2, 3, 4, 5]
print(shuffled_lst(lst_to_shuffle))

#2
def unique_random_num():
    unique_num = set()
    
    while len(unique_num) < 7:
        number = random.randint(0, 9)
        unique_num.add(number)
        
    return list(unique_num)

print(unique_random_num())