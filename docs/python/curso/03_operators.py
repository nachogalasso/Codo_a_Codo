# 30 Days Of Python: Day 3 - Operators
# Let's work with some operators to practice with them

# I will use two numbers stored into a variable and then use the print function to work with them
a = 8
b = 4

addition = a + b
diff = a - b
product = a* b
division = a / b
reminder = a % b
floor_division = a // b
exponential = a ** b

# Let's use the print function to work with the numbers stored
print('a + b = ', addition)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', reminder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

num_one, num_two = 6, 3

add = num_one + num_two
sub = num_two - num_one
prod = num_one * num_two
div = num_one / num_two
remainder = num_two % num_one

print('Total: ', add)
print('Substract: ', sub)
print('Product: ', prod)
print('Division: ', div)
print('Modulus: ', remainder)

# Let's put the data to work. Let's use to calculate area, volume, density, and more)

# Area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print('The area of the circle is: ', area_of_circle)

# Area of a rectangule
lenght = 10
width = 15
area_of_rectangle = lenght * width
print('The area of the rectangule is: ', area_of_rectangle)

# Weight of an object
mass = 82
gravity = 9.81
weigth_of_object = mass * gravity
print(weigth_of_object, 'N')

# Density of the liquid
mass = 65
volume = 0.075
density = mass / volume
print(density, 'Kg/m3')


# COMPARASION OPERATORS
"""To work with the comparasion operators we will use the print() function. The result will be TRUE or FALSE. Remember that if we are using the equal to, we need to write after the > or < operator
"""
print(3 > 2) # True
print(3 >= 3) # True
print(3 < 2) # False
print(2 < 3) # True
print(3 <= 2) # False
print(3 == 2) # False
print(2 == 2) # True
print(3 != 2) # True

# Let's compare the len of some words
print(len('Carlota') > len('Chirola'))
print(len('Chorizo') < len('Bondiola'))
print(len('Matambre') == len('Costilla'))
print(len('Matambre') != len('Costilla'))
print(len('Milanesa') == len('Milanesa'))
print(len('Milanesa') != len('Empanada'))

# We can also compare using the following syntax
print('1 is 1', 1 is 1) # True
print('1 is not 2', 1 is not 2) # True
print('A in Asalea', 'A' in 'Asalea') # True
print('S in Asalea', 'S' in 'Asalea') # False
print('coding' in 'conding for all' ) # True
print('a in an:',  'a' in 'an' ) # True
print('4 is 2 ** 2: ', 4 is 2 ** 2 ) # True

# LOGICAL OPERATORS / and or not
print(3 > 2 and 4 > 2) # True
print(3 > 2 and 4 < 3) # False
print(3 < 2 and 4 < 3) # False
print('True and True: ', True and True)
print(3 > 2 or 4 > 3) # True
print(3 > 2 or 4 < 3) # True
print(3 < 2 or 4 < 3) # False
print('True or False: ', True or False)
print(not 3 > 2) # False
print(not True) # False
print(not False) # True
print(not not True) # True
print(not not False) # False

# EXERCISES - DAY 3
my_age = 42
my_height = 1.77
complex_num = 1 + 4j

# Script to calculate the area of a triangle
tri_base = int(input('We are going to calculate the area of a triangle, please insert the value of the base: '))
tri_height = int(input('Now insert the value of the height: '))
area_of_triangule = 0.5 * tri_base * tri_height
print('The area of your triangle is: ', area_of_triangule)

# Triangle perimeter
side_a = int(input('Insert the 1st side of the triangle: '))
side_b = int(input('Insert the 2nd side of the triangle: '))
side_c = int(input('Insert the 3rd side of the triangle: '))
perimeter = side_a + side_b + side_c
print('The perimeter of your triangle is: ', perimeter)

# Rectangle area
rect_length = int(input('Insert the length of the rectangle: '))
rect_width = int(input('Insert the width of the rectangle: '))
rect_perimeter = 2 * (rect_length + rect_width)
print('The area of your rectangle is: ', rect_perimeter)

# Circle area and circumference
circle_radius = int(input('Insert the radius of the circle: '))
pi = 3.14
circle_area = pi * circle_radius ** 2
circle_circumference = 2 * pi * circle_radius

# Calculate the value of y (y = x^2 + 6x + 9)
x_value = 5
y_value = x_value ** 2 + 6 * x_value + 9
print('The value of y = ', y_value)

# Comparations
print(len('Python') != len('Dragon'))
print('jargon' in 'I hope this course is not full of jargon')
print('on' in 'Python' and 'Dragon') # 15

# 16
float_py = len('python')
str_float_py = str(float_py)
print(str_float_py) 

# 18
print(7 // 2 == int(2.7))

# 19
print(type('10') == type(10))

# 20
print(int('9.8') == 10)

# 21 Rate per Hour
hours = int(input('Insert the total working hours: '))
rate_x_hour = int(input('Insert your pay per hour: '))
weekly_earning = hours * rate_x_hour
print('Your weekly earnings are: ', weekly_earning)

# 22 Seconds lived
user_age = int(input('Please insert your age to convert to seconds: '))
year_days = 365
day_hours = 24
hour_minutes = 60
seconds_minutes = 60
seconds_in_a_year = year_days * day_hours * hour_minutes * seconds_minutes
convert_age_to_seconds = user_age * seconds_in_a_year
print('You have lived: ', convert_age_to_seconds)

# 23