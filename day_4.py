      # Starting new Chapter- Introducing Lists
# Lists are a type of data structure in Python that can hold multiple items. 
# Lists are defined using square brackets [] and can contain items of different types.
bicycels = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycels[0]) # This will print the first item in the list, which is 'trek'
# answer: trek
print(bicycels[0].title())
# answer: Trek
print(bicycels[-1].upper()) # This will print the last item in the list.
# answer: SPECIALIZED
# Using individual values from a list
fruits = ['apple', 'banana', 'cherry']
message = f" I love {fruits[-1].title().removesuffix('y')}ies!"
print(message)
# answer: I love Cherries!

# TRY IT YOURSELF
names = ['aryan', 'aarya', 'suryansh', 'atharva', 'aradhya']
message = f"Hello, {names[0].title()} would you like to learn Python?"
print(message)
message = f"Hello, {names[1].title()} would you like to learn Python?"
print(message)
message = f"Hello, {names[2].title()} would you like to learn Python?"
print(message)
message = f"Hello, {names[3].title()} would you like to learn Python?"
print(message)
message = f"Hello, {names[4].title()} would you like to learn Python?"
print(message)
# ANSWER: Hello, (names) would you like to learn Python?

fav_transport = ['car', 'bike', 'bus', 'train', 'plane']
message = f"I would like to use {fav_transport[1].lower()} for solo travelling."
print(message)
message = f"I would like to have an expensive {fav_transport[0].title()}."
print(message)
# ANSWER: I would like to use (fav_transport) for solo travelling.
# I would like to have an expensive Car. 

  # Question of the day: 
colors = ['red', 'green', 'blue', 'yellow', 'purple']
print(colors[0].upper())
print(colors[-1].upper())
message = f"My favorite colors are {colors[0].upper()}!"
print(message)
message = f"My favorite colors are {colors[-1].upper()}!"
print(message)
# Answer: RED
# PURPLE
# My favorite colors are RED!
# My favorite colors are PURPLE!

# Weekend Final Test Code 😎😎
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
fruits = ['apple', 'banana', 'cherry', 'mango', 'orange']
names = ['aryan', 'aarya', 'suryansh', 'atharva', 'aradhya']
prices = [55000.50, 2000.75, 1200.99, 15000.25, 5000.10]
print(bicycles[3].title())
print(bicycles[2].upper())
print(fruits[0].lower())
print(fruits[1].title())
message = f"I love {fruits[0]}"
print(message)
greeting = f"Hello, {names[0]}! Would you like to learn Python?"
print(greeting)
item = f"This item costs ₹{prices[0]}"
print(item)
print(bicycles[3].removeprefix("s"))
print(fruits[2].removesuffix("y"))
message_1 = f"Hey {names[0]}, do you want a {bicycles[0]} and some {fruits[0]}?"
print(message_1)

message_1 = f"Hey {names}, do you want a {bicycles} and some {fruits}?"
print(message_1)


