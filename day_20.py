             # Revision 
cricketer = {'virat': 'RCB', 'Dhoni': 'CSK', 'pandya': 'MI', 'kl rahul': 'dc'}
my_fav = ['viRat', 'dHoNi']
cricketers = [value.lower() for value in cricketer.keys()]
my_favs = [value.lower() for value in my_fav]
for player in cricketers:
      print(f"Hi {player} you are my favourite .")
      if player in my_favs:
         print(f"Hi {player} you are my favourite cricketer of all time.")

               # Try it yourself
programming_words = {'Variable': 'Storage','String': 'Text' , 'List': 'Collection','Function': 'Action','Loop': 'Repetition'}
for word,meaning in programming_words.items():
     print(f"{word} means {meaning}")
programming_words["Function"] = "Functionality"
programming_words["Loop"] = "Looping"
programming_words["Tuple"] = "Collection"
for word,meaning in sorted(programming_words.items()):
     print(f"{word} means {meaning}")

rivers_country = {'Nile': 'Egypt', 'Amazon': 'Brazil', 'Yangtze': 'China'}
for river,country in rivers_country.items():
     print(f"The {river} flows throughout {country}.")
for river in rivers_country.keys():
     print(river)
for country in rivers_country.values():
          print(f"{country}")

                 # Try it yourself
fav_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
should_give = ['jen', 'edward','rohit','sarfraz']
for name in fav_languages.keys():
            if name in should_give:
              print(f"Thanks for taking the poll {name}.")
            else:
              print(f"{name} please take the poll.")
for names in should_give:
            if names not in fav_languages.keys():
              print(f"{names} please take the poll.")

                   # Nesting 
RCB = {'virat': 'Batsman', 'phil': 'Batsman', 'bhuvi': 'Bowler', 'hazlegod': 'Bowler'}
MI = {'rohit': 'Batsman', 'rickelton': 'Batsman', 'bumrah': 'Bowler', 'santner': 'Bowler'}
CSK = {'rutu': 'Batsman', 'brevis': 'Batsman', 'khallel': 'Bowler', 'noor': 'Bowler'}
IPL = [RCB, MI, CSK]
for players in IPL:
      print(players)

            # More concise way for Nesting:
cricketers = []
for cricketer in range(36):
    cric =  {'Virat Kohli': 'India', 'Joe Root': 'England', 'Steve Smith': 'Australia'}
    cricketers.append(cric)
for cricketer in cricketers[:6]:
    print(cricketer)
print(".....")
print(f"There are {len(cricketers)} cricketers")
 
       # More practice:
masters = []
for master in range(36):
    bowlers = {"Shane Warne": "Australia", "Muthiah Muralidaran": "Sri Lanka", "James Anderson": "England"}
    masters.append(bowlers)
for master in masters[:6]:
    print(master)
print(".....")
print(f"There are {len(masters)} bowlers.")
