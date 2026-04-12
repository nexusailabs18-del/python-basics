                 # Previous day revision
for value in range(1,11):
    print(value)
number = list(range(1,11))
print(number)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
           # or 
sqaures = []
for value in range(1,11):
    sqaures.append(value**2)
print(sqaures)
square = [value**2 for value in range(1,11)]
print(square)
no = [value for value in range(1, 1000001)]
print(sum(no))        # Python did this in fraction of milli second 🥶
                # Starting Day 9
# Working with the part of a List
players = ['charles','michael','martina','eli','florence']
print(players[:4]) # or  print(players[0:4]) 
print(players[1:])# or print(players[1:4])
print(players[-3:])

players = ['charles','michael','martina','eli','florence']
print("Here are first 2 players of my team:")
for player in players[:2]:
    print(player.title())

           # Copying a list
my_foods = ['pizza ','falafel','carrot cake']
friends_food = my_foods[:]
print(my_foods)
print(friends_food)   # They are separate lists. 
# Proof:
my_foods = ['pizza ','falafel','carrot cake']
friends_food = my_foods[:]
my_foods.append('cannoli')
friends_food.append('ice-cream')
print(my_foods)
print(friends_food)
# Output: ['pizza ', 'falafel', 'carrot cake', 'cannoli']
#         ['pizza ', 'falafel', 'carrot cake', 'ice-cream']
    # What would happen if we use this : friends_food = my_foods
y_foods = ['pizza ','falafel','carrot cake']
friends_food = my_foods
my_foods.append('ice-cream')
friends_food.append('cannoli')
print("My favourite foods are:")
print(f"\t{my_foods}")
print(f"\nMy friends favourtie foods are:")
print(f"\t{friends_food}")
# Output:
# My favourite foods are:
#         ['pizza ', 'falafel', 'carrot cake', 'cannoli', 'ice-cream', 'cannoli']

# My friends favourtie foods are:
#        ['pizza ', 'falafel', 'carrot cake', 'cannoli', 'ice-cream', 'cannoli']
            # These two lists become associated to each other! 😗
            

