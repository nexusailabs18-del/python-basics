               #  Final stage of list chapter
#  Checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
     print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!") 

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are outof green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#  Checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adiinng {requested_topping}.")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")

runs = []
if runs:
    for run in runs:
        print(f"Kohli had scored {run} runs.")
else:
        print("Kohli has not played any match.")

          # Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry we don't have {requested_topping}.")

print("\nFinished making your pizza.") 

my_fav = ['kohli', 'rohit','dhoni', 'jadeja',
          'rahul','sachin','bumrah','hazlegod']
friend_fav = ['kohli', 'starc','rayudu','pant','sachin','bumrah']
for my_fa in friend_fav:
    if my_fa in my_fav:
        print(f"My friend likes {my_fa.title()} and me also.")
    else:
        print(f"My friend likes {my_fa.title()} but me not much.")

print("\nJust for fun, we like all of them. 😊")

                                   # Try it yourself
username = ['admin','Bharat','Aryavarta','Hindustan','Tenjiku','Jambudweep'] 
for user in username:
    if user ==  'admin':
        print(f"Hello {user.title()}, would you like a status report ?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")  # Minor mistake done here that i leaved f😗, Now corrected.
username.clear()
if username:
    for user in username:
        print(f"Hello, to all of our {user.title()}s")
else:                                                              # Mistake: I not algined else with if, so nothing in otuput! Keep in mind .😎
        print("We need to find some users!")

current_users = ['admin','Bharat','Aryavarta','Hindustan','Tenjiku','Jambudweep']
new_users = ['admin','Bharat','Tenjiku','ArYan','sURYAnsh']
for new_user in new_users:
     current_users_lowered = [u.lower() for u in current_users]             # Hardest point ever till.🤯
     if new_user.lower() in current_users_lowered:
         print(f"Sorry, the username {new_user.title()} is already taken. Please enter a new username.")
     else:
         print(f"The username {new_user.title()} is available.")

                       # Try it yourself
ordinal_no = list(range(1,10))
for ordinals in ordinal_no:
    if ordinals == 1:
        print(f"{ordinals}st")
    elif ordinals == 2:
            print(f"{ordinals}nd")
    elif ordinals == 3:
         print(f"{ordinals}rd")
    else:
         print(f"{ordinals}th")
# Output:
# 1st
# 2nd
# 3rd
# 4th
# 5th
# 6th
# 7th
# 8th
# 9th

                     # END OF CHAPTER IF STATEMENTS 🥳 🎉
        # Tommorow we will learn revise the whole chapter.
