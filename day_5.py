 # Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)  # Output: ['ducati', 'yamaha', 'suzuki']
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)  # Output: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)  # Output: ['honda', 'yamaha', 'suzuki']
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1,"ducati")
print(motorcycles)  # Output: ['honda', 'ducati', 'yamaha', 'suzuki']
motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles [2]
print(motorcycles)  # Output: ['honda', 'yamaha']
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycleys = motorcycles.pop(1)
print(motorcycles) # Output: ['honda', 'suzuki']
message = f"My first motorcycle was {popped_motorcycleys.title().removesuffix('ys')}."
print(message) # Output: My first motorcycle was Yamaha.
things = ['honda', 'yamaha', 'suzuki','dr.jhatka']
print(things) # Output: ['honda', 'yamaha', 'suzuki', 'dr.jhatka']
too_expensive = 'dr.jhatka'
things.remove(too_expensive)
print(things) # Output: ['honda', 'yamaha', 'suzuki']
print(f"\n{too_expensive.removeprefix('dr.').title()} is goatest scientist in the world")
# Output: Jhatka is goatest scientist in the world

        # Try it Yourself
invited_people = ['albert einstein', 'marie curie', 'isaac newton']
print(f"Dear {invited_people[0].title()} you are coridally invited to our special feast!")
print(f"Dear {invited_people[1].title()} you are coridally invited to our special feast!")
print(f"Dear {invited_people[2].title()} you are coridally invited to our special feast!")

invited_people = ['albert einstein', 'marie curie', 'isaac newton']
invited_people.remove('isaac newton')
print(f"Dear {invited_people[0].title()} you are coridally invited to our special feast!")
print(f"Dear {invited_people[1].title()} you are coridally invited to our special feast!")
print("Sorry Dear Isaac Newton, you are not invited to our special feast anymore.")
invited_people.append('galileo galilei')
print(f"Dear {invited_people[2].title()}, you are herby invited to our special feast!")

invited_people = ['albert einstein', 'marie curie', 'galileo galilei']
print(f"NOTICE:We found a bigger table, so  more people are invited to our special feast!")
invited_people.insert(0, 'nikola tesla')
invited_people.insert(3, 'stephen hawking') 
invited_people.append('ada lovelace')
print(f"Dear {invited_people[0].title()} you are coridally invited to our special feast!")
print(f"Dear {invited_people[1].title()} you are coridally invited to our special feast!")
print(f"Dear {invited_people[2].title()} you are coridally invited to our special feast!")
print(f"Dear {invited_people[3].title()} you are coridally invited to our special feast!")
print(f"Dear {invited_people[4].title()} you are coridally invited to our special feast!")
print(f"Dear {invited_people[5].title()} you are coridally invited to our special feast!")

                       # Try it Yourself
invited_people = ['albert einstein','marie curie','galileo galilei','nikola tesla' ]
print(f"NOTICE: Our dining table would not be deliverd by time.")
print(f"Sorry, We can only invite two people for dinner.")
print(f"Dear, {invited_people[-1].title()} we are sorry not to invite you for dinner.")
print(f"Dear, {invited_people[-2].title()} we are sorry not to invite you for dinner too.")
invited_people.pop()
invited_people.pop(2)
print(f"Dear, {invited_people [0].title()}. you are cordially invited to dinner.")
print(f"Dear, {invited_people[1].title()}. you are cordially invited to dinner.")
del invited_people[0]
del invited_people[1]
print(invited_people) # List is empty now.
# Output:
# NOTICE: Our dining table would not be deliverd by time.
# Sorry, We can only invite two people for dinner.
# Dear, Nikola Tesla we are sorry not to invite you for dinner.
# Dear, Galileo Galilei we are sorry not to invite you for dinner too.
# Dear, Albert Einstein. you are cordially invited to dinner.
# Dear, Marie Curie. you are cordially invited to dinner.
# []  (IndexError: list assignment index out of range)
