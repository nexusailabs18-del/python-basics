                       # Last try it yourself:
cricketers = {                         
    "Virat Kohli": "Batsman",
    "Jasprit Bumrah": "Bowler",
    "MS Dhoni": "Wicket-keeper",
    "Rohit Sharma": "Batsman"
}
cricketers["Suresh Raina"] = "Batsman"
for name, work in cricketers.items():
    print(name + " is a " + work)

           # Revision 
cricketers = {"Virat Kohli": "Batsman",
    "Jasprit Bumrah": "Bowler",
    "MS Dhoni": "Wicket-keeper",
    "Rohit Sharma": "Batsman"
}
cricketers_list = ["Virat Kohli", "Jasprit Bumrah", "Hardik Pandya", "Mohammed Shami"]
for cricketer in cricketers_list:
    if cricketer in cricketers:
        print(f"{cricketer} is in cricketers.")
    else:
        print(f"{cricketer} is not in cricketers.")
for cricketer in cricketers:
    if cricketer not in cricketers_list:
        print(f"{cricketer} is in cricketers.")
                       # or
for cricketer in cricketers:
    if cricketer in cricketers_list:
        print(f"{cricketer} is a {cricketers[cricketer]}.")
    else:
        print(f"{cricketer} is a {cricketers[cricketer]}.")
for cricketer in cricketers_list:
    if cricketer not in cricketers:
        print(f"{cricketer} is not in cricketers.")

                 # Revision
cricketers = []
for cricketer in range(11):
   cricketer_value = {"Virat Kohli": 1,
    "Jasprit Bumrah": 100,
    "MS Dhoni": 264,
    "Rohit Sharma": 235
}
   cricketers.append(cricketer_value)

for dict in cricketers[:10]:
    for cricketer,runs in dict.items():
     if cricketer == "Virat Kohli":
      print(f"{cricketer} scored {runs} run")
     else:
      print(f"{cricketer} scored {runs} runs")

print(".......")
print(f"There are total {len(cricketers)} cricketers in the list")
