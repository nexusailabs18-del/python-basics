                  # Revision
prompt = "Please enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
message = ""
while message != 'quit':
    message = input(prompt)
    if message == 'quit':
        print(message)

                    # Revision
prompt = "Please enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city.lower() == 'quit':
        break
    elif city.lower() == 'paris':
        print(f"I'd love to go to {city.title()}, it's my favorite city!")
    else:
        print("I'd love to go to " + city.title() + "!")

                # Revision
prompt = "Please enter a number:"
prompt += "\nCAUTION: Enter a number between 1 and 105!"
prompt += "\n(Enter 'quit' to end the program.)"
while True:
    number = input(prompt)
    if number.lower() == 'quit':
        break  
    number = int(number)  
    if number > 105:
        break  
    elif number >= 100:
        print("That's a big number!")
    elif number == 5:
        print("We skip 5.")
        continue # This still skips everything below it
    else:
        print(f"Success, you entered {number}.")

    print(f"Looping.... :")
    while number <= 105:
         print(number)
         number += 1 

             # Try it yourself (2)
prompt = "Enter your age:"
prompt += "\nYou would be charged according to your age!"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
   agey = input(prompt)
   if agey.lower() == 'quit':
      break
   agey = int(agey)
   if agey == 0:
      print("Please enter a valid age!")
      continue
   elif agey < 3:
      print("Your ticket is free!")
   elif agey <= 3 and agey > 0:
      print("Your ticket is $10!")
   elif agey <= 12:
      print("Your ticket is $15!")
   else:
      print("Your ticket is $20!")

             # Try it yourslef (4)   # (3) already done inside (1) and (2).
       # Writing Infinte loop:
prompt = "\nTell me something, and I will make it in infinite loop:"
prompt += "\nEnter 'Ctrl+C' to end the program."
while True:
    message = input(prompt)
    message = int(message)
    while True:
          print(message)
          message -= 1

