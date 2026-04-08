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

   # TRY IT YOURSELF
fav_place = ['paris', 'london','tokyo','new york']
print(fav_place) # ['paris', 'london', 'tokyo', 'new york']
print(sorted(fav_place)) # ['london', 'new york', 'paris', 'tokyo']
print(fav_place) # ['paris', 'london', 'tokyo', 'new york'] {still the same order.}
print(sorted(fav_place , reverse=True)) # ['tokyo', 'paris', 'new york', 'london']
print(fav_place) # ['paris', 'london', 'tokyo', 'new york'] {still the same order.}
fav_place.reverse()
print(fav_place) # ['new york', 'tokyo', 'london', 'paris'] {the order is reversed.}
fav_place.reverse()
print(fav_place) # ['paris', 'london', 'tokyo', 'new york'] {the order is back to original.}
fav_place.sort()      
print(fav_place) # ['london', 'new york', 'paris', 'tokyo']{the order is sorted permanently.}
fav_place.sort(reverse=True)
print(fav_place) # ['tokyo', 'paris', 'new york', 'london'] {the order reversed permanently.}

#   Working with dinner guests {done at day 5}
invited_people = ['albert einstein','marie curie','galileo galilei','nikola tesla' ]
print(f"NOTICE: Our dining table would not be deliverd by time.")
print(f"Sorry, We can only invite two people for dinner.")
print(f"Dear, {invited_people[-1].title()} we are sorry not to invite you for dinner.")
print(f"Dear, {invited_people[-2].title()} we are sorry not to invite you for dinner too.")
invited_people.pop()
invited_people.pop(2)
print(f"Dear, {invited_people [0].title()}. you are cordially invited to dinner.")
print(f"Dear, {invited_people[1].title()}. you are cordially invited to dinner.")
print(f"Thus, total {len(invited_people)} people  are invited for dinner.")
del invited_people[0]
del invited_people[1]
print(invited_people) # List is empty now.
print(f"Thus, total {len(invited_people)} are invited for dinner.")
# Output(27_line): 
# Thus, total 2 people are invited for dinner.

                        # TRY IT YOURSELF
cricketer = ['sachin tendulkar', 'virat kohli', 'rohit sharma', 'jasprit bumrah']
print(cricketer[1].title())
message = f"My favourite cricketer is {cricketer[1].title()}."
cricketer.append('ms dhoni')
print(message)
cricketer.insert(0, 'virender sehwag')
print(cricketer)
del cricketer[0]
print(cricketer)
removed_cricketer = cricketer.pop(3)
print(removed_cricketer)
goat_player = cricketer.pop(2)
print(f"goat player is {goat_player.title()}")
cricketer.sort()
print(cricketer)
cricketer.sort(reverse=True)
print(cricketer)
print(sorted(cricketer,reverse=True))
print(cricketer)
cricketer.reverse()
print(cricketer)
print(f"After huge calculations, we got only {len(cricketer)} cricketers left in our list.")
# Output: 
# Virat Kohli
# My favourite cricketer is Virat Kohli.
# ['virender sehwag', 'sachin tendulkar', 'virat kohli', 'rohit sharma', 'jasprit bumrah', 'ms dhoni']
# ['sachin tendulkar', 'virat kohli', 'rohit sharma', 'jasprit bumrah', 'ms dhoni']
# jasprit bumrah
# goat player is rohit sharma
# ['jasprit bumrah', 'ms dhoni', 'sachin tendulkar', 'virat kohli']
# ['virat kohli', 'sachin tendulkar', 'ms dhoni', 'jasprit bumrah']
# ['virat kohli', 'sachin tendulkar', 'ms dhoni, 'jasprit bumrah']
# ['jasprit bumrah', 'ms dhoni', 'sachin tendulkar', 'virat kohli']
# After huge calculations, we got only 3 cricketers left in our list.

                            # TRY IT YOURSELF 
# Trying to get inentional error
# Lets take our previous code and try to  get an error.

                       # Try it Yourself
invited_people = ['albert einstein','marie curie','galileo galilei','nikola tesla' ]
del invited_people[0]
del invited_people[1]
print(f"You are most welcome {invited_people[2]} to the dinner party tonight.")
# Traceback (most recent call last):
#  File "d:\python\hello.py", line 9, in <module>
#   print(f"You are most welcome {invited_people[2]} to the dinner party tonight.")
# IndexError: list index out of range
# We have deleted the first and second element, so the list becomes empty.


