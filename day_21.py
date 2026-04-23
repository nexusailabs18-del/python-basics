               # Revision
cricketers = {                          # I was experimenting with my school computer and this: 😉😎
    "Virat Kohli": "Batsman",
    "Jasprit Bumrah": "Bowler",
    "MS Dhoni": "Wicket-keeper",
    "Rohit Sharma": "Batsman"
}
cricketers_list = ["Virat Kohli", "Jasprit Bumrah", "Hardik Pandya", "Mohammed Shami"]
for cricketer in cricketers_list:
    if cricketer not in cricketers:
      print(f" {cricketer.title()} is not in the cricketers dictionary.")

for cricketer in cricketers_list:
   if cricketer in cricketers_list:
      print(f"Hii {cricketer.title()}")

# OUTPUT:
#  Hardik Pandya is not in the cricketers dictionary.
#  Mohammed Shami is not in the cricketers dictionary.
# Hii Virat Kohli
# Hii Jasprit Bumrah
# Hii Hardik Pandya
# Hii Mohammed Shami

                       # REVISION
      # Another way to write the previous code:
cricketers = {                                            
    "Virat Kohli": "Batsman",
    "Jasprit Bumrah": "Bowler",
    "MS Dhoni": "Wicket-keeper",
    "Rohit Sharma": "Batsman"
}
cricketers_list = ["Virat Kohli", "Jasprit Bumrah", "Hardik Pandya", "Mohammed Shami"]
for cricketer in cricketers_list:
    if cricketer in cricketers:
        print(f"{cricketer} you are in our dictionary.")
    else:
        print(f"{cricketer} you are not in our dictionary.")

for cricketer in cricketers:
    if cricketer not in cricketers_list:
        print(f"{cricketer} you are in our dictionary.")

                # REVISION
cricketers = []
for cricketer in range(36):
    cricketer_value =  {"Virat Kohli": "Batsman",
    "Jasprit Bumrah": "Bowler",
    "MS Dhoni": "Wicket-keeper",
    "Rohit Sharma": "Batsman"
}
    cricketers.append(cricketer_value)

for cricketer in cricketers[:6]:
    print(cricketer)
print("................")
print(f"We have {len(cricketers)} cricketers.")

                       # Today's Topic:
# Make an empty list for string aliens.
aliens = []

# Make 30 green aliens:
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")
# OUTPUT:
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
 # ...
 # Total number of aliens: 30

                  #  A list in dictionary:
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings':['mushrooms','extra cheese']
}
print(f"You have ordered a {pizza['crust']}--crust pizza with the following toppings:")
for topping in pizza['toppings']:
   print(f"\t{topping}")

cricketers = {                                            
    "Virat Kohli": ["Batsman", "Captain"],
    "Jasprit Bumrah": ["Bowler", "Fast"],
    "MS Dhoni": ["Wicket-keeper", "Finisher", "Captain"],
    "Rohit Sharma": ["Batsman"]
}
for name,role in cricketers.items():
   if len(role) == 1:
      print(f"{name} role is :") 
   else:
      print(f"{name} roles are :")
   for role in role:
      print(f"\t{role}")
# Output:
# Virat Kohli role is :
#     Batsman
#     Captain
# Jasprit Bumrah roles are :
#     Bowler
#     Fast
# MS Dhoni roles are :
#     Wicket-keeper
#     Finisher
#     Captain
# Rohit Sharma role is :
#     Batsman

                # A Dictionary in a Dictionary:
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username,user_info in users.items():
    print(f"\nUsername : {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation : {location.title()}")
# Output:
# Username : aeinstein
#    Full name: Albert Einstein
#    Location : Princeton
# Username : mcurie
#    Full name: Marie Curie
#    Location : Paris


