# Vamos a comenzar nuevamente a repasar Python para poder aplicarlo y entender cómo funcionan las cosas
#  Para data analysis

# Comentarios más grandes tipo texto
"""
    This is a comment type text
    Is also know as multiple comment
    
"""

# Let's use the type() method to what type of data we are using
print(type('data'))
print(type(5))
print(type(5.3))
print(type(5.3 + 3j))
print(type(True))
print(type(['Juan','Marta']))
print(type((5, 3, 6)))
print(type({'a':5,'b':6}))
print(type(({3, 4.5, 6,2})))

# Now let's work with the operators
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 ** 3)
print(5 % 3) # modulus
print(5 // 3) # Floor division operator

# Excercises DAY 1
# OPERATORS
print(3 + 4) # addition
print(3 - 4) # subtraction
print(3 * 4) # multiplication
print(3 % 4) # modulus
print(3 / 4) # division
print(3 ** 4) # exponentiation
print(3 // 4) # floor division

# STRINGS
print('My name is Ignacio') # Your name
print('My family name is Galasso') # Family name
print('My country is Argentina') # Country
print('I am starting 30 days of Python')

# CHECK DATA TYPE
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Ignacio'))
print(type('Galasso'))
print(type('Argentina'))


# EUCLIDIAN DISTANCE
# d(p, q)**2 = (q - p)**2 + (q - p)**2
# Between (2, 3) and (10, 8)
print(((2-3)**2 + (10-8)**2)**0.5)