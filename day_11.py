                # Revising previous topics
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[2])
bicycles[2] = 'ducati'
print(bicycles)
bicycles.append('honda')
print(bicycles)
bicycles.insert(2,'xyz')
print(bicycles)
popped_bicycle = bicycles.pop(4)  # delets by index and could return the value 
print(popped_bicycle)
del bicycles[3]       # delets by index and doesn't return the value
print(bicycles)    
bicycles.remove('xyz') # delets by value and doesn't return the value
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()   # permanently sort the list
print(cars)
cars.sort(reverse=True)   # permanently sort the list in reverse
print(cars)
print(sorted(cars))   # temporary sort the list
print(sorted(cars, reverse=True))   # temporary sort the list in reverse
cars.reverse()  # reverse the order of the list permanently
cars.reverse()  # you could again retain the list in the original order by doidng same again.
print(len(cars))  # to get the length of the list
  
cats = ['mew', 'purr', 'meow']
dogs = ['woof', 'bark', 'bow-wow']
rabbits =['hop', 'jump', 'skip']
for cat in cats:
    for dog in dogs:
        for rabbit in rabbits:
            print(f"\nA cat can {cat}")
            print(f"\n\tA dog can {dog}")
            print(f"\n\t\tA rabbit can {rabbit}")
print(f"\n\nAll these animals are cute!")

              # Revision of Python Basics
for value in range(1, 12):  # This will print numbers from 1 to 11 🎶
    print(value)
even_numbers = [value for value in range(2, 12, 2)]
print(even_numbers)  # This will print the list of even numbers from 2 to 10
                 # or
even_numbers = list(range(2, 12, 2))
print(even_numbers)  # This will also print the list of even numbers from 2 to 10
squares = []
for value in range(1,11):
               square = value**2
               squares.append(square)
print(squares)
              # or 
squares =[]
for value in range(1,11):
               squares.append(value**2)
print(squares)
                # or
squares  = [value**2 for value in range(1,11)]        # List Comprehension
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])
print(players[1:4])
print(players[3:5])
print(players[-3:])

my_foods = ['pizza', 'falafel', 'carrot cake']      # Copying a list  [Note: my_foods and friends_foods are two different lists]
friends_foods = my_foods[:]                         # friends_foods is a copy of my_foods, not a reference to the same list.
my_foods.append('cannoli')                          # To do so, we had to change this line to {friends_foods = my_foods[:]}:
friends_foods.append('ice-cream')                   # {friends_foods = my_foods}
print(f"My favourite foods are : {my_foods}")
print(f"\tMy friend's favourite foods are : {friends_foods}")

 # Working with remaining Try it yourself:
foods = ['pizza', 'burger', 'pasta', 'salad']
print(f"The most loved food by me is: \n{foods[:4]}")
print(f"\nI found {foods[1:3]} bit spicy 🥵 in my top 4 food list.")
print(f"\nStill I eat {foods[1:4]} monthly.")   

my_pizza = ['pepperoni', 'mushroom', 'onion', 'olives']
friends_pizza = my_pizza[:]
my_pizza.append('extra cheese')
friends_pizza.append('pineapple')
print("My favorite pizza toppings are:\n")
for pizza in my_pizza:
   print(pizza)
print(f"\nMy friends pizza toppings are:\n")
for pizzas in friends_pizza:
        print(pizzas)
        
        # New Topic: Tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
dimensions = (200,50)
print(dimensions)   # Output: (200, 50)
# Let's try to change the value of dimensions[0] to 250
dimensions[0] = 250  # This will raise a TypeError because tuples are immutable

# Looping through a tuple
dimensions = (200, 50)
print(f"The dimensions are:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print(f"\nThe modified dimesnions are:")
for dimension in dimensions:
     print(dimension)
