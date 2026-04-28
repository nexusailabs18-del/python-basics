             # Try it yourself  (1)
car = "Enter a car:"
car += "\n We would tell you more about your car."
cars = input(car)
print("Let me see if I can find you a " + cars.title() + ".")
if cars.lower() == "subaru" or cars.lower() == "bmw" or cars.lower() == "audi":
    print("Oh, it's available in Amazon.")
else:
    print("Sorry, we don't have it.")

           # Try it yourslef (2)
dinner = input("Enter the number of people coming for dinner:")
if int(dinner) >= 8 :
    print("You have to wait for a table.")
else:
    print("Your table is ready.")

                    # Try it yourslef (3)
no = ("Enter a number:")
no += "\n We would tell you that your number is multiple of 10 or not."
nom = input(no)
if int(nom) % 10 == 0:
    print("Your number is multiple of 10.")
else:
    print("Your number is not multiple of 10.")

              # Introducing while loops:
current_number = 12
while current_number <= 10000:
    print(current_number)
    current_number += 1            # Device hanged 😎😎

                    # Letting the user choose when to quit:
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message  = ""
while message.lower() != 'quit':
    message = input(prompt)
    if message.lower() != 'quit':
       print(message)
                    # Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message.lower() == 'quit' :
        active = False
    else:
        print(message)

                     # Using a flag
cricketer = "Hii, cricketers enter your name:"
cricketer += "\nA surprise line for Virat Kohli:"
cricketer += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(cricketer)
    if message.lower() == "quit":
            active = False
    elif message.title() == "Virat Kohli":
        print(f"---Hello, {message.title()}! Congratulations for completing 9k runs in IPL.")
    else:
        print(f"---Hello, {message.title()}! Have a great day!")

             # Using break to exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)

    if city.lower() == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")



    
