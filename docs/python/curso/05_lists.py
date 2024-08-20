# 30 Days Of Python: Day 5 - Lists
"""Lists
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

"""

# How to Create a List => In Python we can create lists in two ways: Using list built-in function 
# => list() or the empty []

# Using the built-in function list()
from audioop import reverse

from numpy import average


func_list = list()
print(type(func_list))

# Using square brackets []
square_list = []
print(type(square_list))

# Trying something
my_variable = 'Python For Coding'
convert_list = list(my_variable) # This will took every letter and space and store it in an index
print(convert_list)
print(type(convert_list))
print(len(convert_list))

# Let's play with some lists
fruits_1 = ['apple', 'orange', 'banana', 'watermelon', 'grape']
vegetables_1 = ['tomatoe', 'lettuce', 'potatoe', 'onion', 'pumpkin']
grocery_list = ['butter', 'milk', 'meat', 'fish', 'cereal']
techs_1 = ['Python', 'Javascript', 'Java', 'Go', 'PHP']
countries_1 = ['Germany', 'Argentina', 'Spain', 'Italy', 'France']

print('Fruits: ', fruits_1)
print('Number of fruits: ', len(fruits_1))
print('Vegetables: ', vegetables_1)
print('Number of Vegetables: ', len(vegetables_1))
print('Grocery list: ', grocery_list)
print('Number of items in the Grocery list: ', len(grocery_list))
print('Techs: ', techs_1)
print('Number of Techs: ', len(techs_1))
print('Countries to visit: ', countries_1)
print('Number of Countries to visit: ', len(countries_1))

# Let's remember that store different types of data in a list
multi_type_list = ['Robert', 'Paneles', 23, {'city':'Madrid', 'country':'Spain'}, True]
print(multi_type_list)
print(len(multi_type_list))
print(type(multi_type_list))

# It's important to know that each data is into one index, starting from 0. To access to any item
# we need to call our list and then the index of the item we want to work with
# Remember that the index is positive numbers
# Let's use the variable fruits_1
first_fruit = fruits_1[0]
print(first_fruit)
second_fruit = fruits_1[1]
print(second_fruit)
third_fruit = fruits_1[2]
print(third_fruit)
# Also we can do the follow
last_fruit = len(fruits_1) - 1
print(fruits_1[last_fruit])

# When we use negative index, -1 represents the last item in our list, if we increased the value we move to the first
last_fruit = fruits_1[-1]
secondlast_fruit = fruits_1[-2]
first_negative_fruit =fruits_1[-5]
print(last_fruit, secondlast_fruit, first_negative_fruit)

# Now is time unpack our list into single variables
item_list = ['item1', 'item2', 'item3', 'item4', 'item5']
fst_item, snd_item, trd_item, *rest = item_list
# if we want to unpack the last items into one variable before the name we are required to use the *
print(fst_item)
print(snd_item)
print(trd_item)
print(rest)
# We can also do the following thing to unpack the or create a list
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)
# with this type, the last number will be in a simple variable
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

"""Slicing Items from a List
Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
"""

fruits_2 = ['banana', 'orange', 'mango', 'lemon']
# Now we our list, let's start practicing how to slice the list
all_return_fruits = fruits_2[0:4] # This is like a copy of the list because we include all the items
orange_and_mango = fruits_2[-3:-1] # We can write fruits_2[1:3]
orange_mango_lemon = fruits_2[1:] # If we don't indicate were it ends, it will take al items from one point to the end
orange_lemon = fruits_2[::2] # We are indicating the program to slice every two items
print(all_return_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print(orange_lemon)

"""Modifying Lists
List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.
If we want to modify a item of our list we can do it by indicating the index of the value we want to change, for example, fruits[0] => will change the value for the index 0 in our list
"""
cars = ['BMW', 'Peugeot', 'Toyota', 'Audi', 'Mitsubishi']
cars[4] = 'Mazda' # Here we are changing the value from index 4
cars[1] = 'Acura'
cars_last_index = len(cars) - 1
cars[cars_last_index] = 'Suzuki' # We can also change a value by using a variable
print(cars) 
print(cars_last_index) 

"""Checking Items in a List
Checking an item if it is a member of a list using in operator. See the example below.
Sometimes is important for us to check if a value is in our list and we can do that using the 'in' operator
"""
does_exist = 'Acura' in cars # If we print this variable it will return a True or False value
does_exist2 = 'Fiat' in cars # Is a way to check for values in our list
print(does_exist)
print(does_exist2)

"""Now is time to remove or add items to our list

    To add item to the end of an existing list we use the method append().

    We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.

    The remove method removes a specified item from a list
    
    The pop() method removes the specified index, (or the last item if index is not specified)
    
    The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
    
    The clear() method empties the list
"""

# append() method. It will insert a new item at the end of an existing list
cars.append('Fiat')
cars.append('Renault')
print(cars)

# insert() method. It will insert a new item and we can indicate at the index we want the new item
cars.insert(2, 'Honda') # at index 2 the value Honda will be inserted
cars.insert(4, 'Skoda')
print(cars)

# remove(), with this method we indicate the value we want to remove from out list
# If we don't specify the index, it will remove the last item from our list
cars.remove('Suzuki')
cars.remove('Fiat')
print(cars)

# With the pop() method we can remove a specified index
lst_item = ['item1', 'item2', 'item3']
lst_item.append('item4')
lst_item.pop(1) # if we don't specify the index, it will remove the last item from our list
print(lst_item)

# we can use the del keyword to remove an item from our list
del lst_item[0]
# del lst_item This will delete the whole list of items
# del lst_item[1:3] we can delete a piece of the list using the slicing
print(lst_item)

# The clear() method
cars.clear()
print(cars)
# now our car list is empty of items, we still have the variable to store values into it

"""Copying a List
It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using copy().
"""

# By using lst_item2 = lst_item we well create a copy but both variables will connected, if we modify a value in one list, the other list will be modify too. To avoid this, we use the copy() method
lst_item2 = lst_item
print(lst_item)
# Now both items are connected

lst_item3 = lst_item.copy()
print(lst_item3)
lst_item2.append('item5') # we add an item and we see that both variables changed
lst_item3.append('item6') # only lst_item3 will change because we use the copy() method
print(lst_item)
print(lst_item2)
print(lst_item3)


"""Joining Lists
There are several ways to join, or concatenate, two or more lists in Python.

Plus Operator (+)

Another way to join is using the extend() method The extend() method allows to append list in a list. See the example below.
"""
lst_join1 = ['item1', 'item2', 'item3']
lst_join2 = ['item4', 'item5', 'item6']
lst_joining = lst_join1 + lst_join2
print(lst_joining)

# We can also join numbers
positive_numb = [1, 2, 3, 4, 5]
zero = [0]
negative_numb = [-1, -2, -3, -4, -5]
num_intergers = negative_numb + zero + positive_numb
print(num_intergers)

abc_letters = ['a', 'b', 'c', 'd', 'e']
xyz_letters = ['v', 'w', 'x', 'y', 'z']
whole_letters = abc_letters.extend(xyz_letters) # extend() won't work to store the list in a new variable
abc_letters.extend(xyz_letters)
print('The extended list is: ', abc_letters)

# Can we extend different lists?
numb_2 = [3, 35, 89]
letters_2 = ['a', 'b', 'c']
# numb_2.extend(letters_2)
print(numb_2) # yes we can but is not recommended

"""Counting Items in a List
The count() method returns the number of times an item appears in a list:
"""
print(cars.count('Renault'))
# Because there is no 'Renault' value in our list the result of the count() is 0

lottery = [9, 18, 68, 68, 2, 9, 56, 68, 23, 45, 68, 98, 77, 21, 14, 16]
print(lottery.count(68))
# The result of the count() is 4, 68 appears in our list four times

"""Finding Index of an Item
The index() method returns the index of an item in the list:
It will return the first appearance of the item in our list when it finds it
"""
print(lottery.index(68)) # will indicate the first appearence in our list if the value is repeated

"""Reversing a List
The reverse() method reverses the order of a list.
"""
lottery.reverse()
num_intergers.reverse()
print(lottery)
print(num_intergers)

"""Sorting List Items
To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

sort(): this method modifies the original list

sorted(): returns the ordered list without modifying the original list
"""
lottery.sort()
print(lottery)
# by passing an argument we can reverse the list
num_intergers.sort(reverse=True)
print(num_intergers)

# EXERCISES - DAY 5

#1
exercise_list = list()
print(type(exercise_list))

#2
exercise_list = ['River Plate', 'Real Madrid', 'Barcelona', 'Manchester', 'Juventus']
print(exercise_list)

#3
print(len(exercise_list))

#4
first_item = exercise_list[-5]
second_item = exercise_list[3:4]
last_item = exercise_list[-1]
print(first_item)
print(second_item)
print(last_item)


#5
mixed_data_types = ['Rolando', 26,1.77, {'marital_status':'single', 'address':'Rivera st. 165'} ]

#6 #7
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

#8
print(len(it_companies))

#9
print(it_companies[0])
print(it_companies[2:5])
print(it_companies[-1])

#10
it_companies[6] = 'Linux'
print(it_companies)

#11
it_companies.append('Amazon')

#12
it_companies.insert(4, 'Mozilla')

#13
it_companies[1] = it_companies[1].upper()
print(it_companies) 

#14
it_comp_join = '#; '.join(it_companies)
print(it_comp_join)

#15
print( 'Amazon' in it_companies)

#16
it_companies.sort()
print(it_companies)

#17
it_companies.sort(reverse = True)
print(it_companies)

#18 #19 # 20
first_three_companies = it_companies[0:3]
last_three_companies = it_companies[6:]
middle_companies = it_companies[3:6]
print(first_three_companies)
print(last_three_companies)
print(middle_companies)
 
#21 #22 # 23
it_companies.pop(0)
print(it_companies)

it_companies.pop(4)
print(it_companies)

it_companies.pop(-1)
print(it_companies)

#24 # 25
del it_companies [0:]
print(it_companies)

it_companies.clear()
print(it_companies)

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_stack = front_end + back_end
print(join_stack)

#27
full_stack = join_stack.copy()
full_stack.insert(4, 'Python')
full_stack.insert(5, 'SQL')

print(full_stack)

#Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)
ages.append(min_age)
ages.append(max_age)
print('min age is: ', min(ages))
print('max age is: ', max(ages))
print(ages)

n = len(ages)
get_sum = sum(ages)
print(get_sum)
ages_average = get_sum / n
print('the average age is: ', ages_average)
ages_dif = max_age - min_age
print('The difference between the ages is: ', ages_dif)


#
countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus',  'Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei', 'Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]; 

countries_len = len(countries)
middle_countries = countries_len // 2
print('The total countries is: ', countries_len, '\n', 'The middle of the countries is: ', middle_countries)

first_half_countries = countries[0:96]
second_half_countries = countries[96:]
print(first_half_countries) 
print(second_half_countries)

unpack_country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, rs, us, *scandic = unpack_country
print(ch)
print(rs)
print(us)
print(scandic)

