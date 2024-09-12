# This file is to practice using python modules

def generate_full_name(name, surname):
    return name + ' ' + surname

# Now we import the module into a new file called 12_modules.py

def sum_two_numbs(a, b):
    return a + b

def get_weight(mass):
    gravity = 9.8
    return mass * gravity


person_test = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':32,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

def get_person(person):
    return person