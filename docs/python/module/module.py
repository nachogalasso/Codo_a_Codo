# print('I like to be a module')
# print(__name__)

#!/usr/bin/env python3

__counter = 0

# if __name__ == "__main__":
#    print('I prefer to be a module')
# else:
#    print('I like to be a module')
   
def suml(the_list):
   global __counter
   __counter += 1
   the_sum = 0
   for e in the_list:
      the_sum += e
   return the_sum

def prodl(the_list):
   global __counter
   __counter += 1
   prod = 1
   for e in the_list:
      prod *= e
   return prod

if __name__ == '__main__':
   print('I prefer to be a module, but I can do some tests for you')
   my_list = [i+1 for i in range(5)]
   print(suml(my_list) == 15)
   print(prodl(my_list) == 120)