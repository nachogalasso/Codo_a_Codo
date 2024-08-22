# 30 Days Of Python: Day 7 - Sets

"""Sets
Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

Creating a Set
We use the set() built-in function.

Creating an empty set
# syntax
st = set()
Creating a set with initial items
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
Example:

# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}

Remember they are used to store UNIQUE items. They are UNORDERED and UN-INDEXED

Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Duplicates Not Allowed
Sets cannot have two items with the same value. Duplicates values will be ignored. For the sets TRUE or 1 and FALSE or 0, will be the same value, so because they are duplicate, it will be ignored
"""

import stat


st = set() # creating a set
st = {'item1', 'item2', 'item3', 'item4'}
print(st)
print(type(st))

# length of our set
print('The length of our set is: ', len(st))

"""Accessing Items in a Set
We use loops to access items. We will see this in loop section

Checking an Item
To check if an item exist in a list we use in membership operator.

We can loop through out set to find items
"""
print('Is item3 in our set? ', 'item3' in st)


"""Adding Items to a Set
Once a set is created we cannot change any items and we can also add additional items.

By using the add() built-in function, we can add items to our set. This will be added at the end of our set

To Add multiple items we use the update() function. The update() allows to add multiple items to a set. The update() takes a list argument. We are required to add a list of items saved into a variable. We are required to add iterable items.
"""

st.add('item5')
print(st)
# Notice that our values change positions. It doesn't matter where the value is added because there
# are no indexes so the items will be in a different position every time we call the set.

# Adding multiple items
# Let's create a new set
fruits = {'Apple', 'Orange', 'Lemon', 'Banana'}
vegetables = {'Tomato', 'Potato', 'Lettuce', 'Onion'}
fruits.update(vegetables)
print(fruits)
# This is similar to doing a join

# Updating another set
st2 = {'item6', 'item7', 'item8'}
st.update(st2)
print(st)

"""Removing Items from a Set
We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.

The pop() methods remove a random item from a list and it returns the removed item.

Clearing Items in a Set
If we want to clear or empty the set we use clear method. clear()

Deleting a Set
If we want to delete the set itself we use del operator.
"""

# REMEMBER BEFORE REMOVING AN ITEM, FIRST CHECK IF THE ITEM IS IN THE SET
# st.remove('item9') This will show an error because item9 is not in the set
st.remove('item4')
print(st)

st.discard('item10') # Won't show any errors
print(st)

# With pop() we will remove a random item from our set
removed_item = st.pop()
print('The removed item is: ', removed_item)
print(st)

# Let's use the clear() method to clean a set
cars = {'Audi', 'Toyota', 'Renault', 'Fiat'}
print(cars)
cars.clear()
print(cars)

# With the del operator we delete the whole set
del st
# print(st) We will have an error because the set doesn't exist anymore
del fruits

"""Converting List to Set
We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
"""
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
print(type(lst))
# Lets convert the list into a set
st = set(lst)
# Remember that once we have a set the items are unordered and unchangeable
print(type(st))

"""Joining Sets
We can join two sets using the union() or update() method.

Union This method returns a new set
"""
# We use union() to join both sets, and we can use update() too. The first method returns a new set.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

# With update
fruits1 = {'banana', 'orange', 'mango', 'lemon'}
vegetables1 = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits1.update(vegetables1)
print(fruits1)

"""Finding Intersection Items
Intersection returns a set of items which are in both the sets. This is a good option to find similar values into different sets
"""

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(whole_numbers)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
print(python)

"""Checking Subset and Super Set
A set can be a subset or super set of other sets:

Subset: issubset()
Super set: issuperset

In return we will have a True or False value
"""

whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python.issubset(dragon)     # False

"""Checking the Difference Between Two Sets
It returns the difference between two sets.

This will return to us those values that are not intersected
"""

print(whole_numbers.difference(even_numbers)) # {1, 3, 5, 7, 9}

print(python.difference(dragon))     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
print(dragon.difference(python))     # {'d', 'r', 'a', 'g'}

"""Finding Symmetric Difference Between Two Sets
It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
"""
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}

print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

"""Joining Sets
If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
"""

odd_numbers1 = {0, 2, 4 ,6, 8}
even_numbers1 = {1, 3, 5, 7, 9}
even_numbers1.isdisjoint(odd_numbers1) # True, because no common item

# EXERCISES - DAY 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print('The set contains: ',  len(it_companies), 'items')

#2
it_companies.add('Twitter')
print(it_companies)

#3
more_it_companies = {'Reddit', 'Twitch', 'Tik Tok'}
it_companies.update(more_it_companies)
print(it_companies)

#4
it_companies.remove('Reddit')
print(it_companies)

#5
# The difference between remove and discard is that the first one will give us an error if they can't
# find the item that we want to remove

# Exercises 2
#1
print(A.union(B))

#2
print(A.intersection(B))

#3
print(A.issubset(B)) # True

#4
print(A.isdisjoint(B)) # False

#5
# print(A.union(B))
# print(B.union(A))

#6
print(A.symmetric_difference(B))

#7
del A
del B

# Exercises 3
age_st = set(age)
print(type(age_st))

print('The length of the age list is: ',len(age))
print('The length of the age set is: ', len(age_st))
# There is difference between boths because the set ignores the duplicated values

sentence = 'I am a teacher and I love to inspire and teach people'
sentence_lst = sentence.split()
print(sentence_lst)

print('The length of the sentence list is: ',len(sentence_lst))
middle = len(sentence_lst) // 2
first_line = sentence_lst[:5]
second_line = sentence_lst[5:]
print(first_line)
print(second_line)

first_line_set = set(first_line)
second_line_set = set(second_line)
print(type(first_line_set))
print(type(second_line_set))
print('The length of the first set is: ', len(first_line_set))
print('The length of the second set is: ', len(second_line_set))

print(first_line_set.symmetric_difference(second_line_set))