                              # Revision
age = 14
if age >= 18:
    print('You are old enough to vote.😊')
else:
    print('You are not old enough to vote.😔')

                   # The if-elif-else chain
age = 12
if age < 4 :
    print("Your admission cost is $0.😋")
elif age < 18:
    print("Your admission cost is $25.😗")
else:
    print("Your admission cost is $40.🫥")       # Output: Your admission cost is $25.😗

                    # Using multiple elif statements    
age = 56
if age < 4 :
    print("Your admission cost is $0.😋")
elif age < 18:
    print("Your admission cost is $25.😗")
elif age < 65: 
    print("Your admission cost is $15.😉")
else:
    print("Your admission cost is $40.🫥") 
print("\nWelome to our newly opened movie theatre.😎")
# Output: Your admission cost is $15.😉

        #  Welome to our newly opened movie theatre.😎

            # Omitting the else block
age = 82
if age < 4 :
    print("Your admission cost is $0.😋")
elif age < 18:
    print("Your admission cost is $25.😗")
elif age < 65: 
    print("Your admission cost is $15.😉")
elif age >=65:
    print("Your admission cost is $10.🤩")   # Output: Your admission cost is $10.🤩

            # Testing multiple conditions   
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Yakk, I don't like mushrooms!🤮🤢")
if 'pepperoni' not in requested_toppings:
  print("Please, add some pepperoni; I like that!😉")
if 'extra cheese' in requested_toppings:
  print("I want only normal cheese, as cheese not good for health.🥲")
if 'extra cheese' not in requested_toppings:
  print("If not, please add as i won't want to me to regret for that; Never Mind.😗")
                    # Code = 1% ; Emojis = 99%

               # Try it yourself
alien_color = ['green', 'yellow', 'red']
for alien in alien_color:
   if alien == 'green':
     print("Congrats! You have earned 5 points in the game.")
   if alien=='blue':
     print("Wow! You had won the alien game, huge Congrats.")
alien = 'green'
if alien == 'yellow':
     print("Congrats! You have earned 5 points in the game.")
if alien == 'green':
       print("Congrats! You have earned 10 points in the game.")
                  # or
if alien == 'green':
     print("Congrats! You have earned 5 points in the game.")
else:
     print("Congrats! You have earned 10 points in the game.")
if alien == 'yellow':
     print("Congrats! You have earned 5 points in the game.")
else:
     print("Congrats! You have earned 10 points in the game.")

if alien == 'green':
        print("Congrats! You have earned 5 points in the game.")
elif alien == 'yellow':
        print("Congrats! You have earned 10 points in the game.")
else:
     print("Congrats! You have earned 15 points in the game.")

print("Finished the first part of Try it yourself.😎")

            # Try it yourself
person = 35
if person < 2:
    print("You are a baby.")
elif person >=2 and person < 4:
    print("You are a toddler.")
elif person >= 4 and person < 13:
        print("You are a kid.")
elif person >= 13 and person < 20:
        print("You are a teenager.")
elif person >= 20 and person < 65:
        print("You are an adult.")
else :
        print("You are an elder.")        # Who are you amoung them ?

favourite_fruits = ["apple", "banana", "cherry"]
if "apple" in favourite_fruits:
    print(f"I really like {favourite_fruits[0]}!")
if "banana" in favourite_fruits:
    print(f"I really like {favourite_fruits[1]}!")
if "cherry" in favourite_fruits:
    print(f"I really like {favourite_fruits[2]}!")
if "pineapple" in favourite_fruits:
    print(f"I really like {favourite_fruits[3]}!")
if "orange" in favourite_fruits:
    print(f"I really like {favourite_fruits[4]}!")
 # Do you like 🌚........

