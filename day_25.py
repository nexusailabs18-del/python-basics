                   # Master Revision
aliens = []

for alien in range(30):
    new_alien =  {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for aliensy in aliens[:6]:
    if aliensy['color'] == 'green':
        aliensy['color'] = 'yellow'
        aliensy['speed'] = 'medium'
        aliensy['points'] = 10

for aliensy in aliens[:8]:
     aliensy['rank'] = 'elite'
     print(aliensy)

print(f"Total number of aliens: {len(aliens)}")

for alien in aliens:
    alienys = f"{alien['color']} {alien['points']} {alien['speed']}"
    print(alienys)
for alien in aliens[:6]:
    alien['rank'] = 'diamond'
    aliensy = f"{alien['color']} {alien['points']} {alien['speed']}"
    alieny = f"{alien['rank']}"
    print("aliensy:")
    print(f"\t{aliensy}")
    print(f"alieny:")
    print(f"\t{alieny}")

print(f"We had {len(aliens)} aliens.")

for alien,info in new_alien.items():
    print(f"{alien}")
    print(f"\t{info}")
    
                    #   Master Revision
cities = {
    'delhi' : { 'country' : 'india' , 'population' : 1000000 , 'fact' : 'capital of india'},
    'london' : { 'country' : 'england' , 'population' : 5000000 , 'fact' : 'capital of england'},
    'paris' : { 'country' : 'france' , 'population' : 2000000 , 'fact' : 'capital of france'},
    'tokyo' : { 'country' : 'japan' , 'population' : 1000000 , 'fact' : 'capital of japan'},
}
for city,info in cities.items():
    print(f"{city.title()}:")
    countri = info['country'] 
    pop = info['population']
    fact = info['fact']
    print(f"\tCountry: {countri.title()}")
    print(f"\tPopulation: {pop}")
    print(f"\tFact: {fact.title()}")

               # New Chapter : User Input and While Loops
message = input("Tell me something, and I will repeat it back to you:")
print(message)

name = input("Please enter your name:")
print(f"Hello,{name.title()}! Welcome to this program.")

prompt = ("If you share your name, we can personlise the messages you see.")
prompt += "\nWhat is your first name ?"
full_name = input(prompt)
first_name = full_name.split()[-1].title()
print(f"Hello, {first_name}! Don't worry, your Dad is here.")
      # Input: Ridhan
      # Output: Hello, Ridhan! Don't worry, your Dad is here.               # 😭😭

age = input("Ridhan, how old are you?")
age = int(age)
if age >= 18:
    print("You are old enough to vote.")
else:
   print("You are not old enough to vote.")

number = input("Enter a number, I would tell it is even or odd:")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

number = input("Enter a number, I would tell the successor of it:")
number = int(number)
print(number+1)

number = input("Enter a number, I would tell the predecessor of it:")
number = int(number)
print(number-1)
