# 30 Days Of Python: Day 4 - Strings

# Now is the turn to work with strings. Let's dig in and start enjoy the knowledge

# We can store a simple letter in a variable or a whole sentence. Remember to do this it's important
# to put the text in between quotes simple or double quotes '' "".

hey_string = 'L'
print(hey_string) # It will print what is stored in the variable
print(len(hey_string)) # It will print the length of the string
full_sentence = 'Hi this a full string sentence, all stored in the variable'
print(full_sentence)
print(len(full_sentence)) # it will count the blank spaces too

# Multiline strings. For this type of strings we a required to use the triple quote ''' ''' or """ """
multiline_string = '''Hi! This is a multiline string.
People do not believe me that I stored a multiline string.
Now, learn how to store a multiline string, same day you will need it.'''
print(multiline_string)

# STRING CONCATENATION (connect strings together)
first_name = 'Claudio'
last_name = "Ramirez"
space = ' ' # This is to add a space between the name and surname
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(first_name) > len(last_name))
print(len(first_name) == len(last_name))
print(len(first_name) != len(last_name))

"""Escape Sequences in Strings
In Python and other programming languages the backlash is followed by a character is an escape sequence. Let us see the most common escape characters:

\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
"""
print("Let's try this new characters and see what we can do \n are you ready?")
# Let's try to draw a table
print("Days\tTopics\tExercises") # Remember that with the \t we add a tab space
print("Day 1\t5\t5")
print("Day 2\t6\t20")
print("Day 3\t7\t15")
print("Day 4\t1\t35")
print('To add a backlash we need to use the symbol (\\)')
print('If we want to use the other quotes \"Hello World!\"')

# FORMATTING a STRING
"""Old Style String Formatting (% Operator)
In Python there are many ways of formatting strings. In this section, we will cover some of them. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision

With this characters what we are doing is indicating the program what type of data is holding the variable. Let's see some examples

"""

# With strings
agent_name = 'James'
agent_surname = 'Castolo'
age = 42
tech_skill = 'Python'
formatted_string = 'This is %s %s. He is %d, and he writes code in %s' %(agent_name, agent_surname, age, tech_skill)
print(formatted_string)

# With intergers
radius = 10
pi = 3.14
area = pi * radius ** 2
area_of_circle = 'The area of a circle with a radius %d is %.2f' %(radius, area) 
# with the expression %.2f we are indicating the number of digits after the .
print(area_of_circle)

# Now using a list
python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
formatted_py = 'The following list are Python libraries:%s ' %(python_libraries)
print(formatted_py)

"""Now we have a new way to use the string formatting is called as a str.format() and to indicate Python where are we putting the string values we are required to use the symbol {}
"""

player_name = 'Oliver'
player_surname = 'Atom'
position = 'Midfielder'
introduction = 'This is {} {}. He plays soccer and he is a {}'.format(player_name, player_surname, position)
print(introduction)

# Now let's use some numbers
a = 6
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
print('{} / {} = {:.2f}'.format(a, b, a / b))

# Strings literals
"""String Interpolation / f-Strings (Python 3.6+)
Another new string formatting is string interpolation, f-strings. Strings start with f and we can inject the data in their corresponding positions. (I like this most)
"""
c = 5
d = 4

print(f'{c} + {d} = {c + d}')
print(f'{c} - {d} = {c - d}')
print(f'{c} * {d} = {c * d}')
print(f'{c} / {d} = {c / d}')
print(f'{c} ** {d} = {c ** d}')
print(f'{c} % {d} = {c % d}')
print(f'{c} // {d} = {c // d}')

"""Python Strings as Sequences of Characters
Python strings are sequences of characters, and share their basic methods of access with other Python ordered sequences of objects – lists and tuples. The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.

Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
Accessing Characters in Strings by Index
In programming counting starts from zero. Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.
We can access to any part of the string by using the index. Remember that programming languages start from 0 index
"""

index_access = 'Python'
a,b,c,d,e,f = index_access
print(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}')
print(len(index_access))

first_letter = index_access[0]
print(first_letter)
two_letters = index_access[0:2] # Here we are slicing our string
print(two_letters)

# we can use negative index
last_letter = index_access[-1]
print(last_letter)

# We can reverse a string and slice it the way we want

greeting = 'Hello World!'
print(greeting[::-1]) # By this command we reverse our string

skip_letters = 'Python'
pto = skip_letters[0:6:2] # we took all the string and slice it every two letters
print(pto)

# STRING METHODS
# .capitalize() => only converts the first letter of the string into a capital letter
# .count() => counts ocurrences of substring into a string => .count(substring, start, end)
challenge_count = 'thirty days of python'
print(challenge_count.capitalize())
print(challenge_count.count('y')) # Will count for the 'y' in our string
print(challenge_count.count('y', 7, 14)) # will start counting from index 7 to index 14
print(challenge_count.count('th'))
# .endswith() => will check how our string ends
# .expandtabs() => will replace tabs characters with spaces, we can indicate the size we want
# .find() => returns the index of the FIRST occurrence of the substring we indicated
# .rfind() => returns the index of the LAST occurrence of the substring we indicated
# .format() => gives a nice format to our string remember this use {} and then .format(the variables)
# .index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
# .rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
# .isalnum(): Checks alphanumeric character
# .isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z). Space is excluded
# .isdecimal(): Checks if all characters in a string are decimal (0-9)
# .isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
# .isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
# .isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
# .islower(): Checks if all alphabet characters in the string are lowercase
# .isupper(): Checks if all alphabet characters in the string are uppercase
# .join(): Returns a concatenated string. We can indicate the character we want to use to join the strings
web_tech = ['HTML', 'CSS', 'JAVASCRIPT', 'NODEJS']
result = ' '.join(web_tech)
result_2 = '# '.join(web_tech)
print(result)
print(result_2)
# .strip(): Removes all given characters starting from the beginning and end of the string
# .replace(): Replaces substring with a given string => we need to indicate the word to be replaced
word_replace = 'thirty days of python'
print(word_replace.replace('python', 'coding'))
# .split(): Splits the string, using given string or space as a separator
word_split = 'thirty days of python'
word_split_2 = 'House of dragons'
print(word_split.split()) # We will have a list with each word
print(word_split_2.split(', ')) # a list with the whole sentence
# .title(): Returns a title cased string => capital letter for the first letter of each word
# .swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
# .startswith(): Checks if String Starts with the Specified String

# EXERCISES - Day 4
#1
concat_1 = ['Thirty', 'Days', 'Of', 'Python']
result_concat_1 = ' '.join(concat_1)
print(result_concat_1)

#2
concat_2 = 'Coding'
concat_2a = 'For'
concat_2b = 'All'
result_concat_2 = concat_2 + ' ' + concat_2a + ' ' + concat_2b
print(result_concat_2)

#3
company = 'coding for all'

#4
print(company)

#5
print(len(company))

#6
print(company.upper())

#7
print(company.lower())

#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
print(company[0:6])

#10
print(company.find('coding'))
print(company.index('coding'))
print('coding' in company)

#11
company_replace = company.replace('coding', 'python')
print(company_replace)

#12
print(company.replace('all', 'everyone'))

#13
comp = 'Python, for, Everyone'
print(company.split())
print(comp.split(', '))

#14
tech_comp = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_comp.split(', '))

#15
print(company[0])

#16
print(company[-1])

#17
print(company[10])

#18
acronym_1 = 'Python For Everyone'
acronym_1_split = acronym_1.split()
acro_1 = acronym_1_split[0][0] + acronym_1_split[1][0] + acronym_1_split[2][0]
print(acro_1)
#19
acronym_2 = 'coding for all'
acronym_2_upper = acronym_2.title()
acronym_2_upsp = acronym_2_upper.split()
result_acronym_2 = acronym_2_upsp[0][0] + acronym_2_upsp[1][0] + acronym_2_upsp[2][0]
print(result_acronym_2)



#20 #21
phrase = 'Coding For All'
print(phrase.index('C'))
print(phrase.index('F'))

#22
phrase_2 = 'Coding For All People'
print(phrase_2.rfind('i'))

#23 #24
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rindex('because'))

#25
print(sentence[31:54])

#28  #29
sub_string = 'Coding'
print(phrase.startswith(sub_string))
print(phrase.endswith(sub_string))

#30
phrase_2 = '   Coding For All      '
print(phrase_2.strip())

#31
phrase_identifier = '30DaysOfPython'
phrase_identifier_2 = 'thirty_days_of_python'
print(phrase_identifier.isidentifier())
print(phrase_identifier_2.isidentifier())

#32
py_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
pylib_join = '# '.join(py_libraries)
print(pylib_join)

#33
sentence_newline = 'I am enjoying this challenge.\nI just wonder what is next.'
print(sentence_newline)

#34
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t25\tFinland\tHelsinki')

#35
rad = 10
cir_area = 3.14 * rad ** 2
cir_area_format = 'The area of a circle with radius {} is {} meters square'.format(rad, cir_area)
print(cir_area_format)

#36
f = 8
g= 6

print(f'{f} + {g} = {f + g}')
print(f'{f} - {g} = {f - g}')
print(f'{f} * {g} = {f * g}')
print(f'{f} / {g} = {f / g}')
print(f'{f} % {g} = {f % g}')
print(f'{f} // {g} = {f // g}')
print(f'{f} ** {g} = {f ** g}')