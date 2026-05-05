# Try it yourself (1)
sandwich_orders = ['pastrami', 'tuna',  'ham' , 'veggie' , 'chicken']
finished_sandwiches = []
non_finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        print("\tSorry, we are out of pastrami.")
        non_finished_sandwiches.append(current_sandwich)
        continue
    print(f"I made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n\tYour sandwiches are ready:")
for sandwich in finished_sandwiches:
    print(f"\t\t{sandwich.title()} sandwich.")

print("\n\tThe following sandwich(es) are/is not available:")
for sandwiches in non_finished_sandwiches:
    print(f"\t\t{sandwiches.title()} sandwich.")

# Try it yourself (2)
sandwich_orders = ['pastrami', 'tuna',  'ham' , 'veggie' , 'chicken']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n\tYour sandwiches are ready:")
for sandwich in finished_sandwiches:
    print(f"\t\t{sandwich.title()} sandwich.")

# Try it yourself (3)
vacation = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    vacation[name] = place
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    elif repeat == 'yes':
        polling_active = True
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        polling_active = False

print("\n--- Poll Results ---")
for name,place in vacation.items():
    print(f"{name.title()} would like to visit {place.title()}.")

# Filling a dictionary with User input
cricketer = {}
polling_active = True

while polling_active:
    name = input("\nWhich cricketer do you like?")
    nickname = input("What is his nickname?")
    cricketer[name] = nickname
    if name.lower() == 'virat kohli':
        print("Virat Kohli is one of the greatest cricketers of all time!")
    else:
        print(f"{name.title()} is a great cricketer too!")
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if nickname.lower() == 'king kohli':
        print("WARNING: Only Virat Kohli can be called King Kohli!")
        
    if repeat.lower() == 'no':
        polling_active = False
    elif repeat.lower() == 'yes':
        polling_active = True
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        polling_active = False

print("\n--- Poll Results ---")
for name, nickname in cricketer.items():
    print(f"\n{name.title()} is also known as {nickname.title()}.")

# Filling a dictionary with User input
response = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    mountain = input("Which mountain would you like to climb someday?")
    response[name] = mountain
    
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active = False
    if repeat == "yes":
        polling_active = True
    else:
        print("Please answer with 'yes' or 'no'.")

print("\n--- Poll Results ---")
for name,mountain in response.items():
    print(name.title() + " would like to climb " + mountain.title() + ".")
