# Using a fucntion with a while Loop
def cricketers(first_name, last_name):
    """This function takes the first name and last name of a cricketer and returns a formatted string."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me the name of a cricketer:")
    print("(enter 'quit' at any time to quit)")

    first_name = input("First name: ")
    if first_name.lower() == 'quit':
        break
    last_name = input("Last name: ")
    if last_name.lower() == 'quit':
        break

    formatted_name = cricketers(first_name, last_name)
    if formatted_name == "Virat Kohli":
        print(f"\t{formatted_name} is the best cricketer in the world!")
    elif formatted_name == "Sachin Tendulkar":
        print(f"\t{formatted_name} is the greatest cricketer of all time!")
    else:
        print(f"\tAwesome! {formatted_name} is a great cricketer.")

  # Using a fucntion with a while Loop
def get_formatted_name(first, last):
    """Return a full name, neatly formatted."""
    full_name = f"{first} {last}"
    return full_name.title()

while True:
    print("\nPlease tell your name:")
    print("(enter 'q' at any time to quit)")
    first_name = input("First name: ")
    if first_name == 'q':
        break
    
    last_name = input("Last name: ")
    
    formatted_name = get_formatted_name(first_name, last_name)
    print(f"\nHello, {formatted_name}!")

# Returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# Optional arguments
def build_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    return full_name

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# Making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

musician = get_formatted_name('john', 'hooker')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Try it yourself (3)
def describe_city(city, country = "Iceland"):
    """Display a simple sentence about a city."""
    print(f"{city.title()} is in {country.title()}.")

describe_city("Reykjavik")
describe_city("Vestmannaeyjar", "Iceland")
describe_city("Copenhagen", "Denmark")

# Return values
def get_formatted_name(first, last):
    """Return a full name, neatly formatted."""
    full_name = f"{first.title()} {last.title()}"
    return full_name

musician = get_formatted_name("jimi", "hendrix")
print(musician)

# Try it yourself (1)
def make_shirt(size, message):
    """Display a message about the shirt that's going to be made."""
    print(f"\nThe shirt will be {size.title()} in size.")
    print(f'It will say "{message}" on it.')

make_shirt("large", "I love Python!")
make_shirt(size="medium", message="I love Python!")

# Try it yourself (2)
def make_shirt(size = 'large', message = 'I love Python!'):
    """Display a message about the shirt that's going to be made."""
    print(f"\nThe shirt will be {size.title()} in size.")
    print(f'It will say "{message}" on it.\n')

make_shirt()
make_shirt(size="medium")
make_shirt(message="Python is my favorite language!")
make_shirt(size="small", message="Python is the best language!")

# Keyword arguments
def describe_pet(animal_type , animal_name):
    """Display information about the pet."""
    print(f"I have a {animal_type.title()}.")
    print(f"It's name is {animal_name.title()}.\n")

describe_pet(animal_type = 'hamster', animal_name = 'harry')
describe_pet(animal_type = 'dog', animal_name = 'willie')

# Default values
def describe_pet(animal_type, animal_name = 'willie'):
    """Display information about the pet."""
    print(f"I have a {animal_type.title()}.")
    print(f"It's name is {animal_name.title()}.\n")

describe_pet(animal_type = 'hamster')

# Try it yourself (2)
def favourite_book(title):
    """Display a message about someone's favourite book."""
    print(f"One of my favourite books is {title.title()}.")

favourite_book('alice in wonderland')
favourite_book('the great gatsby')

# Passing arguements
def describe_pet(animal_type , pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"It's name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Functions
def greet_user():
    """Display a simple greeting message."""
    print("Hello!")
greet_user()

def greet_user(username):
    """Display a personalised greeting message."""
    print(f"Hello, {username.title()}!")
    print("Welcome to the world of Python programming!")

greet_user("Ridhan")

# Try it yourself (1)
def display_message():
    """Display a message about what I'm learning."""
    print("I'm learning about Functions in Python!")

display_message()

               # Try it yourslef(3)
def make_album(artist,name,songs=None):
    """Return a dictionary of information about an album."""
    album_dict = {'artist': artist, 'name': name}
    if songs:
        album_dict['songs'] = songs
    return album_dict

album = make_album('The Beatles', 'Abbey Road', 17)
print(album)
albumy = make_album('The Beatles', 'Abbey Road')
print(albumy)

for key,value in album.items():
    print(f"\t{key.title()}: {str(value).title()}")
for key,value in albumy.items():
    print(f"\t{key.title()}: {str(value).title()}")

while True:
    print("Please tell me about an album.")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist: ")
    if artist.lower() == 'q':
        break
    name = input("Album Name: ")
    if name.lower() == 'q':
        break
    songs = input("Number of songs: (Optional, Press 'ENTER' to skip..) ")
    if songs.lower() == 'q':
        break
    if songs =="":
        songs = None
    else:
        songs = int(songs)
    album = make_album(artist, name, songs)
    print("Album information:")
    for key, value in album.items():
        print(f"\t{key.title()}: {str(value).title()}")
