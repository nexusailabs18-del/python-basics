# Revision 1
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city.lower() == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

  # Revision 2
cric = "Enter your full name:"
cric += "\nWe would personalize your name."
cric += "\nSpecial message for legends."
cric += "\t\t\n(Press 'quit' in any case to end the program.)"
message = True
while message :
    name = input(cric)
    if name.lower() == 'quit':
        break
    elif name.lower() == 'virat kohli':
        print(f"Hii {name.title()}, you are the King of cricket.")
    elif name.lower() == 'rohit sharma':
        print(f"Hii {name.title()}, you are the Hitman of cricket.")
    elif name.lower() == 'sachin tendulkar':
        print(f"Hii {name.title()}, you are the God of cricket.")
    elif name.lower() == 'mahendra singh dhoni':
        print(f"Hii {name.title()}, you are the captain cool  of cricket.")
    else:
        print(f"Hii {name.title()}, you are a cricketer.")

  # Using continue in a loop
current_number = 3
while current_number < 10:
    current_number += 1
    if current_number % 2 ==0:
        continue
    print(current_number)

current_number = 14
while current_number < 100:
    current_number += 1
    if current_number % 2 == 1:
        continue
    print(current_number)

                 # Avoiding Infinite Loops
x = 1
while x <= 10:
    print(x)
    x += 1 
           # If
x = 1
while x <= 10:
    print(x)      # Omit : x += 1
                  # Would run till end of universe 😎😎😭😭

                  # Try it yourslef (1)
topping = "Please tell the toppings you want to add in pizza:"
topping += "\nEnter 'quit' to end or 'none' to skip."
while True:
    message = input(topping)
    if message.lower() == 'quit':
     break
    if message.lower() == 'none':
     print("Skipping this entry.")
     continue
    print(f"We are going to add {message.title()} in your pizza.")





  
      
