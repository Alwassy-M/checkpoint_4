import math
from decimal import Decimal

#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

list = ['wali', 'one', 'hello']
tuple = ('Item_1',123, False, 0.0001,[1, 'two'])
my_float = 100.222
my_int = 1993

def my_deci(x,y): # I ceated this func to see results
  print(Decimal(x) + Decimal(y))
  
my_deci(9.5, 10)

dictionary = {
  'first_name': 'Angel',
  'last_name': 'Kindel',
  'age': '1000'
}

#Exercise 2: Round your float up.
print(math.ceil(my_float))

#Exercise 3: Get the square root of your float.
print(math.sqrt(my_float))

#Exercise 4: Select the first element from your dictionary.
print(dictionary['first_name'])

#Exercise 5: Select the second element from your tuple.
print(tuple[0])

#Exercise 6: Add an element to the end of your list.
list.append('added_element')
print(list)

#Exercise 7: Replace the first element in your list.
list[0]= 'replaced_element'
print(list)

#Exercise 8: Sort your list alphabetically.
print(sorted(list))

#Exercise 9: Use reassignment to add an element to your tuple.

tuple += ('new element',)
print(tuple)

