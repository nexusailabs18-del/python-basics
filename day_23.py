                 # Try it yourself 
people1 = {'first_name': 'John', 'last_name': 'Doe', 'age': 30}
people2 = {'first_name': 'Jane', 'last_name': 'Doe', 'age': 25}
people3 = {'first_name': 'John', 'last_name': 'Smith', 'age': 40}
people = [people1, people2, people3]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    print(f"{full_name} is {age} years old.")

pet1 = {'name': 'Fluffy', 'type': 'cat', 'owner': 'John Doe'}
pet2 = {'name': 'Buddy', 'type': 'dog', 'owner': 'Jane Doe'}
pet3 = {'name': 'Max', 'type': 'dog', 'owner': 'John Smith'}
pet4 = {'name': 'Luna', 'type': 'cat', 'owner': 'Jane Smith'}
pet = [pet1,pet2,pet3,pet4]
for peties in pet:
    pet_name = peties['name']
    pet_type = peties['type']
    pet_owner = peties['owner']
    print(f"{pet_name} is a {pet_type} owned by {pet_owner}.")

favourite_places = {
    'JOHN doe' : {'place1' : 'paris', 'place2' : 'london', 'place3' : 'new york'},
    'Jane Doe' : {'place1' : 'beijing', 'place2' : 'tokyo', 'place3' : 'kazakasthan'},
    'John Smith' : {'place1' : 'paris', 'place2' : 'london', 'place3' : 'bengaluru'},
    'Jane Smith' : {'place1' : 'ahmedabad', 'place2' : 'lahore', 'place3' : 'new york'},
}
for name,place in favourite_places.items():
    print(f"{name.title()} has visited :")
    place = favourite_places[name] 
    for places in place.values():
        print(f"\t{places.title()}")

            # Try it yourself
fav_nom = {
    'virat kohli' : { 'nom 1' : 18 , 'nom 2' : 19 , 'nom 3' : 20},
    'rohit sharma' : { 'nom 1' : 45 , 'nom 2' : 96 , 'nom 3' : 333},
    'sachin tendulkar' : { 'nom 1' : 100 , 'nom 2' : 200 , 'nom 3' : 300},
    'dhonI' : { 'nom 1' : 1000 , 'nom 2' : 2000 , 'nom 3' : 3000},
    
}
for name,nom in fav_nom.items():
    print(f"{name.title()} favourtie number is :")
    number = fav_nom[name]
    for value in number.values():
        print(f"\t{value}")

cities = {
    'delhi' : { 'country' : 'india' , 'population' : 1000000 , 'fact' : 'capital of india'},
    'london' : { 'country' : 'england' , 'population' : 5000000 , 'fact' : 'capital of england'},
    'paris' : { 'country' : 'france' , 'population' : 2000000 , 'fact' : 'capital of france'},
    'tokyo' : { 'country' : 'japan' , 'population' : 1000000 , 'fact' : 'capital of japan'},
}
for city,info in cities.items():
    print(f"{city.title()} :")
    countryi  = info['country']
    population = info['population']
    fact = info['fact']

    print(f"\t Country is {countryi.title()}")
    print(f"\t Population is {population}")
    print(f"\t Fact is {fact.title()}")
