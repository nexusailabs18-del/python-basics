                      # Organizing a List
# You can organize a list by using the sort() method. [Permanently]
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # Output: ['audi', 'bmw', 'subaru', 'toyota']
# The sort() method sorts the list permanently.
cars.sort(reverse=True)
print(cars) # Output: ['toyota', 'subaru', 'bmw', 'audi']   
# You can also sort a list temporarily by using the sorted() function. [Temporarily]
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Here is the original list :\n\t{cars}") #
print(f"\nHere is the sorted list :\n{sorted(cars)}")
print(f"\nHere is the original list again :\n\t{cars}")
# Output: Here is the original list :
#         ['bmw', 'audi', 'toyota', 'subaru']
# Here is the sorted list :
# ['audi', 'bmw', 'subaru', 'toyota']   
# Here is the original list again :
#         ['bmw', 'audi', 'toyota', 'subaru']
       # Printing a List in Reverse Order
# You can reverse the order of a list by using the reverse() method. [Permanently]
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) # Output: ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars) # Output: ['subaru', 'toyota', 'audi', 'bmw']
# Finiding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # Output: 4 

