          # Revision and ending the chapter if statements
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response.")
else:
    print(f"{user.title()}, you can't post a response.")

game_active = True
can_edit = False
if game_active:
    print("The game is active")
else:
    print("The game is not active")
if can_edit:
        print("Editing the game")
else:
        print("You can't edit the game")

age = 14
if age == 13: 
 print("Your age is 13")
elif age == 14:
     print("Your age is 14")
else:
    print("You are not 13 or 14")

                   # Some more:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' not in requested_toppings:
        print("Sorry, we're out of pepperoni.")
else:
      print("Closing the shop.")
   
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
   if requested_topping == 'green peppers':
      print("Sorry, we're out of green peppers right now.")
   else:
     print(f"Adding {requested_topping.title()}.")

print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    print(f"Adding the {requested_toppings}:")
else:
    print("Are you sure you want a plain pizza?")

        # Lastly:
available_toppings = ['mushrooms', 'olives', 'green peppers',
                       'pepperoni', 'pineapple', 'eXtra cheese']
requested_toppings = ['Mushrooms', 'french Fries', 'extra cheese']
available_toppings = [value.lower() for value in available_toppings]
for requested_topping in requested_toppings:
   if requested_topping.lower() in available_toppings:
       print(f"Adding {requested_topping}.")
   else:
       print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

        #   looking at the glimpse of Dictionaries:
alien_0 = {'color': 'green', 'points': 5}
print((alien_0['color']).title())
print((alien_0['points'])**2)
# Output:
# Green
# 25 
