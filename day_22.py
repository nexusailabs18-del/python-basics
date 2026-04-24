                    # Revision 
cricketers = {"Virat Kohli": "Batsman",
    "Jasprit Bumrah": "Bowler",
    "MS Dhoni": "Wicket-keeper",
    "Rohit Sharma": "Batsman"
}
cricketers_list = ["Virat Kohli", "Jasprit Bumrah", "Hardik Pandya", "Mohammed Shami"]
for cricketer in cricketers_list:
    if cricketer not in cricketers:
        print(f"{cricketer} is not in cricketers.")
    else:
        print(f"{cricketer} is in cricketers.")
for cricketer in cricketers:
    if cricketer not in cricketers_list:
      print(f"{cricketer} is in cricketers.")
                           # OR
for cricketer in cricketers_list:
    if cricketer in cricketers:
        print(f"{cricketer} is in cricketers.")
    else:
        print(f"{cricketer} is not in cricketers.")
for cricketer in cricketers:
    if cricketer not in cricketers_list:
        print(f"{cricketer} is in cricketers.")

                 # Revision:
cricketers = []

for cricketer in range(12):
    cricketer_value = {"Virat Kohli": 1,
    "Jasprit Bumrah": 100,
    "MS Dhoni": 264,
    "Rohit Sharma": 235
}
    cricketers.append(cricketer_value)

for cricketersy in cricketers[:6]:
    if cricketersy["Jasprit Bumrah"] == 100:
        cricketersy["Jasprit Bumrah"] = 35
    if cricketersy["Rohit Sharma"] == 235:
        cricketersy["Rohit Sharma"] = 264
for name,runs in cricketersy.items():
    if runs == 1:
        print(f"{name} has scored {runs} run.")
    else:
        print(f"{name} has scored {runs} runs.")
    
print(f"\t\nWe had {len(cricketers)} cricketers.")
for cricketersy in cricketers[:13]:           # It will print only max 12 times,not 13 
  print(cricketersy)                          # After 6 prints, all would be normal (unchanged)

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
    full_name = f"{user_info['first']}{user_info['last']}"
    locations = f"{user_info['location']}"
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {locations.title()}")




