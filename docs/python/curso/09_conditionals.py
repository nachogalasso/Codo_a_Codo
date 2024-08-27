# 30 Days Of Python: Day 9 - Conditionals

"""Conditionals
By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

Conditional execution: a block of one or more statements will be executed if a certain expression is true
Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.
If Condition
In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.

# syntax
if condition:
    this part of code runs for truthy conditions

Example: 1

a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

"""

# Conditional with one condition
"""
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
As you can see in the example above, 3 is greater than 0. The condition was true and the block code was executed. However, if the condition is false, we do not see the result. In order to see the result of the falsy condition, we should have another block, which is going to be else.
"""
# x = int(input('Enter a number:'))
x = 6

if x > 0:
    # First condition is FOR TRUE statements
    print('Yes is a positive number')
    
# Let's add and else condition
""" If Else
If condition is true the first block will be executed, if not the else condition will run.

# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
**Example: **

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
The condition above proves false, therefore the else block was executed. How about if our condition is more than two? We could use _ elif_.


a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
Short Hand
# syntax
code if condition else code
**Example: **
"""
# a = int(input('Enter a number: '))
a = 6
if a > 0:
    print('Is a positive number')
else:
    print('Is a negative number')
    
# We use elif when we have more than two conditions
"""If Elif Else
In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.

# syntax
if condition:
    code
elif condition:
    code
else:
    code
**Example: **
"""
# b = int(input('Enter a number: '))
b = 6
if b > 0:
    print('Is a positive number')
elif b == 0:
    print('Your number is Zero')
else:
    print('Is a negative number')
    
"""Short Hand
# syntax
code if condition else code
**Example: **

a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

We can write the whole condition in one line of code
"""
# c = int(input('Enter a number: '))
c = 2
print('Is a positive number') if c > 0 else print('Is a negative number')

"""Nested Conditions
Conditions can be nested

# syntax
if condition:
    code
    if condition:
    code
**Example: **

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

We can nest some conditions in order to create more especific guidelines to our program. This will help us to be more presice on what we want the program to execute
"""

# d = int(input('Enter a number: '))
d = 0
if d > 0:
    if d % 2 == 0:
        print('Your number is positive and int')
    else:
        print('Is only a positive number')
elif d == 0:
    print('Your number is equal to Zero')
else:
    print('Is a negative number')

"""We can avoid writing nested condition by using logical operator and.

If Condition and Logical Operators
# syntax
if condition and condition:
    code
**Example: **

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
"""
# Instead of using nested we can use the AND to write our conditionals
# e = int(input('Enter a number: '))
e = 0
if e > 0 and e % 2 == 0:
    print('Your number is positive and int')
elif e > 0 and e % 2 != 0:
    print('Is only a positive number')
elif e == 0:
    print('Your number is equal to Zero')
else:
    print('Is a negative number')

"""If and Or Logical Operators
# syntax
if condition or condition:
    code
**Example: **

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
"""

# Now is time to use the OR operator
# user = 'John'
# access_level = 3
user = 'admin'
access_level = 6
# user = input('Are you user or admin?').lower()
# access_level = int(input('Please what is your access level?'))

if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')


# EXERCISES - DAY 9

#1
age = int(input('Please enter your age: '))

if age > 18:
    print('You are old enough to drive')
else:
    dif = 18 - age
    print(f'You need {dif} years to drive')
    
#2
your_age = int(input('Please enter your age?'))
my_age = 32

dif = abs(my_age - your_age)

if my_age > your_age:
    print(f'I am {dif} years older than you')
elif my_age == your_age:
    print('We are the same age')
else:
    print(f'You are {dif} years older than me')
    
#3
numb_1 = int(input('Please enter a number to compare: '))
numb_2 = int(input('Please enter a second number: '))

if numb_1 > numb_2:
    print(f'{numb_1} is greater than {numb_2}')
elif numb_1 == numb_2:
    print(f'{numb_1} is equal to {numb_2}')
else:
    print(f'{numb_1} is lower than {numb_2}')
    

# Exercises Level 2

#1
grade = int(input('Please enter your grade to know your note: '))

if grade > 80 and grade <= 100:
    print('Your note is an A')
elif grade > 70 and grade <= 89:
    print('Your note is a B')
elif grade > 60 and grade <= 69:
    print('Your note is a C')
elif grade > 50 and grade <= 59:
    print('Your note is a D')
else:
    print('Your note is a F')
    
#2
season = input('To know the season enter the month we are now: ').lower()

if season == 'september' or season == 'october' or season == 'november':
    print('We are in Autumn')
elif season == 'december' or season == 'january' or season == 'february':
    print('We are in Winter')
elif season == 'march' or season == 'april' or season == 'may':
    print('We are in Spring')
else:
    print('We are in Summer')

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Please enter a fruit: ').lower()

if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(f'{new_fruit} is now added to the list')
    print(fruits)

# Exercises: Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 25,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


if 'skills' in person:
    psn_skills = person.get('skills')
    print(psn_skills[2:3])
    
if 'Python' in person.get('skills'):
    print('Yes, he has Python skills')
    
if 'JavasScript' and 'React' in person.get('skills'):
    print('He is a front end developer')
elif 'Node' and 'Python' and 'MongoDB' in person.get('skills'):
    print('He is a fullstack developer')
else:
    print('unknown title')
    
if person['is_marred'] == True and person['country']  == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married')
    
