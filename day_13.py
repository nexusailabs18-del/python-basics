                                      # If statements
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())  # Prints the car with a capital first letter
if car == 'subaru':
            print("\nHii, Subaru")
else:
            print("\nHii, but i am not subaru")
car = "Lamborghini"
if car.lower() == 'lamborghini':
        print(car.upper())
else:
        print("\nFalse")

requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':  # Inequality operator
       print("Hold the anchovies!")

answer = 199
if answer != 200:
       print("Wrong")    #  Wrong

age = 18
print(age == 111)     # False 
print(age == 18)      # True

age = 18
print(age <= 21)   # True   
print(age < 21)    # True
print(age>=21)     # False
print(age>21)      # False

              # Using and to Check Multiple Conditions
age_0 = 22
age_1 =19
print(age_0 >=21 and age_1 >=21)   # False
age_1 = 23
print(age_0 >=21 and age_1 >=21)   # True

age_0 = 22
age_1 = 18
print(age_0 >=21 or age_1 >=21)   # True
age_0 = 18
print(age_0 >=21 or age_1 >=21)   # False

              # Checking whether a value is in a list
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)    # True
print('pepperoni' in requested_toppings)    # False

              # Checking whether a value is not in a list
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")     # Output : Marie, you can post a response if you wish.

              # Boolean Expressions 
game_active = True
can_edit = False
if game_active:
    print("The game is still alive!😎")
else:
    print("The game is over!😭")
if can_edit:
    print("You can edit the game!😗")
else:
    print("You can't edit the game!😰")
# Output : The game is still alive!😎
#          You can't edit the game!😰

