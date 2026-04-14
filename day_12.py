                                              # Try it Yourself
buffet = ('eggs','hot dogs', 'spaghetti', 'steak', 'chicken')
print(f"Our restaurant has the following items on the menu:")
for food in buffet:
        print(food.title())

buffet[0] = 'bacon'           # error message: 'tuple' object does not support item assignment
buffet = ('bacon', 'hot dogs', 'spaghetti', 'salad', 'chicken')
print("Sorry, we had made changes to our menu and now we have the following items on the menu:")
for food in buffet:
        print(food.title())

# Master Challenge: Create a list of 10 numbers;
# Do all: # slice first 5 # slice last 5 # copy list # add new number in copied list # loop through original # print squares of each number
no = [1,2,3,4,5,6,7,8,9,10]
print(no[:5])
print(no[5:])
number = no[:]
number.append(11)
print(number)
for nom in no:
    print(nom)
copied_nom = [value**2 for value in number]
print(copied_nom)
squares = [value**2 for value in no]
print(squares)

                             # New chapter: If statements
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())             # bmw is printed in upper case
                                          # Just testing code 😎,now lists practice.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0] = 'honda'
print(bicycles)
bicycles.append('cannodale')
bicycles.insert(2,'suzuki')
del bicycles[0]
popped_bicycle = bicycles.pop(3)
print(f"The first bicycles i owned was{popped_bicycle.title()}.")
bicycles.remove('cannodale')
bicycles.sort()
bicycles.sort(reverse=True)
print(sorted(bicycles))
print(sorted(bicycles, reverse=True))
bicycles.reverse()             # Permanently reverse the list
print(bicycles)

dogs = ['pug', 'corgi', 'rottweiler', 'poodle']
cats = ['siamese', 'persian', 'maine coon', 'bengal']
parrots = ['cockatoo', 'macaw', 'parakeet', 'macaw']
for dog in dogs:
    for cat in cats:
        for parrot in parrots:
            print(f"{dog.title()} loves {cat.title()}!")
            print(f"{dog.title()} loves {parrot.title()}!")
            print(f"{cat.title()} loves {parrot.title()}!")
print("In fact all of them love each other!😂😭\n")
print("For that i wrote the history of the whole world.😗\n")
print("Never mind.")

for value in range(1,25):
    print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)
print(len(squares))
print(min(squares))
print(max(squares))
print(sum(squares))

for i in range(1,10000001):
    print(i)
