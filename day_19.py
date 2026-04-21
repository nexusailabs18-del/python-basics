# Revision

cricketer = {
    'first_name': 'Sachin',
    'last_name': 'Tendulkar',
    'age': 50,
    'country': 'India'
}

print(cricketer)

# Update value
cricketer['first_name'] = 'Arjun'
print(f"Hello {cricketer['first_name']} {cricketer['last_name']}.")

# Delete key
del cricketer['age']
print(cricketer.get('age', 'Not Found'))

# Add again
cricketer['age'] = 30
print(cricketer['age'])

# Conditional logic
if cricketer['age'] > 30:
    age = 0
elif cricketer['age'] < 30:
    age = 0
else:
    age = 1

cricketer['age'] = cricketer['age'] + age

print(f"{cricketer['first_name']} {cricketer['last_name']} is {cricketer['age']} years old.")

# Looping through a dictionary

cricketer = {
    'virat': 'RCB',
    'dhoni': 'CSK',
    'pandya': 'MI',
    'kl rahul': 'DC'
}

for player, team in cricketer.items():
    print(f"\nPlayer: {player.title()}")
    print(f"Team: {team.upper()}")
    print(f"{player.title()} loves ❤️ {team.upper()}")

# Looping through all keys
print("\nAll the popular players in IPL are:")
for player in cricketer.keys():
    print(player.title())

# Favorite players check
my_fav = ['Virat', 'Dhoni']

cricketers = [name.lower() for name in cricketer.keys()]
my_favs = [name.lower() for name in my_fav]

for player in cricketers:
    print(f"Hi {player}")

    if player in my_favs:
        print(f"{player} is in cricketers list.")

# Check missing player
if 'rohit' not in cricketer.keys():
    print("Rohit, where are you?")
else:
    print("Sorry, Rohit is not in our IPL players list.")
# Looping through dictionary keys in sorted order

cricketer = {
    'virat': 'RCB',
    'dhoni': 'CSK',
    'pandya': 'MI',
    'kl rahul': 'DC',
    'rohit': 'MI'
}

# Sorted keys
for player in sorted(cricketer.keys()):
    print(f"{player.title()} plays for {cricketer[player].upper()}")
    print(f"{player.title()}, you are in our cricketers list.")

# All teams (including duplicates)
print("\nThe following teams have been mentioned:")
for team in cricketer.values():
    print(team.upper())

# Unique teams only
print("\nUnique teams mentioned:")
for team in set(cricketer.values()):
    print(team.upper())


# Add new key
cricketer['team'] = 'lsg'
print(f"{cricketer['first_name']} {cricketer['last_name']} is playing for {cricketer['team'].upper()}.")
