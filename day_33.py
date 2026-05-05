1     # Filling a dictionary with User input
2 response = {}
3 polling_active = True
4 
5 while polling_active:
6     name = input("\nWhat is your name?")
7     mountain = input("Which mountain would you like to climb someday?")
8     response[name] = mountain
9 
10     repeat = input("Would you like to let another person respond? (yes/no)")
11     if repeat == "no":
12         polling_active = False
13     if repeat == "yes":
14         polling_active = True
15     else:
16         print("Please answer with 'yes' or 'no'.")
17 
18 print("\n--- Poll Results ---")
19 for name, mountain in response.items():
20     print(name.title() + " would like to climb " + mountain.title() + ".")

1     # Filling a dictionary with User input
2 cricketer = {}
3 polling_active = True
4 
5 while polling_active:
6     name = input("\nWhich cricketer do you like?")
7     nickname = input("What is his nickname?")
8     cricketer[name] = nickname
9     if name.lower() == 'virat kohli':
10         print("Virat Kohli is one of the greatest cricketers of all time!")
11     else:
12         print(f"{name.title()} is a great cricketer too!")
13     repeat = input("Would you like to let another person respond? (yes/no) ")
14     if nickname.lower() == 'king kohli':
15         print("WARNING: Only Virat Kohli can be called King Kohli!")
16 
17     if repeat.lower() == 'no':
18         polling_active = False
19     elif repeat.lower() == 'yes':
20         polling_active = True
21     else:
22         print("Invalid input. Please enter 'yes' or 'no'.")
23         polling_active = False
24 
25 print("\n--- Poll Results ---")
26 for name, nickname in cricketer.items():
27     print(f"\n{name.title()} is also known as {nickname.title()}.")

1     # Try it yourself (1)
2 sandwich_orders = ['pastrami', 'tuna',  'ham' , 'veggie' , 'chicken']
3 finished_sandwiches = []
4 non_finished_sandwiches = []
5 
6 while sandwich_orders:
7     current_sandwich = sandwich_orders.pop()
8     if current_sandwich == 'pastrami':
9         print("\tSorry, we are out of pastrami.")
10         non_finished_sandwiches.append(current_sandwich)
11         continue
12     print(f"I made your {current_sandwich.title()} sandwich.")
13     finished_sandwiches.append(current_sandwich)
14 
15 print("\n\tYour sandwiches are ready:")
16 for sandwich in finished_sandwiches:
17     print(f"\t\t{sandwich.title()} sandwich.")
18 
19 print("\n\tThe following sandwich(es) are/is not available:")
20 for sandwiches in non_finished_sandwiches:
21     print(f"\t\t{sandwiches.title()} sandwich.")

1     # Try it yourself (2)
2 sandwich_orders = ['pastrami', 'tuna',  'ham' , 'veggie' , 'chicken']
3 finished_sandwiches = []
4 
5 while 'pastrami' in sandwich_orders:
6     sandwich_orders.remove('pastrami')
7 
8 while sandwich_orders:
9     current_sandwich = sandwich_orders.pop()
10 
11     print(f"I made your {current_sandwich.title()} sandwich.")
12     finished_sandwiches.append(current_sandwich)
13 
14 print("\n\tYour sandwiches are ready:")
15 for sandwich in finished_sandwiches:
16     print(f"\t\t{sandwich.title()} sandwich.")

1     # Try it yourself (3)
2 vacation = {}
3 polling_active = True
4 while polling_active:
5     name = input("\nWhat is your name? ")
6     place = input("If you could visit one place in the world, where would you go? ")
7     vacation[name] = place
8 
9     repeat = input("Would you like to let another person respond? (yes/no) ")
10     if repeat == 'no':
11         polling_active = False
12     elif repeat == 'yes':
13         polling_active = True
14     else:
15         print("Invalid input. Please enter 'yes' or 'no'.")
16         polling_active = False
17 
18 print("\n--- Poll Results ---")
19 for name, place in vacation.items():
20     print(f"{name.title()} would like to visit {place.title()}.")
