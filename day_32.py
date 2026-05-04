                       # Revision
cricketer = ['virat', 'rohit', 'rahul', 'sachin','ronaldo']
hundred_cricketer = []
non_hundred_cricketer = []
non_cricketer = []
while cricketer:
  player = cricketer.pop()
  print("Verifying cricketer: " + player.title())

  if player == 'ronaldo':
    non_cricketer.append(player.title())
  elif player == 'sachin':
    hundred_cricketer.append(player.title())
  else:
    non_hundred_cricketer.append(player.title())
   
print("Player(s) with 100 centuries:")
for cricketer in hundred_cricketer:
  print(cricketer.title())
  if len(hundred_cricketer) == 1:
    print("Only one player with 100 centuries!")
  else:
   print("More than one player with 100 centuries!")

print("Player(s) with less than 100 centuries:")
for cricketer in non_hundred_cricketer:
  print(cricketer.title())
  if len(non_hundred_cricketer) == 1:
    print("Only one player with less than 100 centuries!")
else:
    print("More than one player with less than 100 centuries!")

print("Player(s) not a cricketer:")
for cricketer in non_cricketer:
  print(cricketer.title())

prompt = "\nPlease enter the name of a cricketer [from the list]: "
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
  name = input(prompt)
  if name.lower() == 'quit':
    break
  if name.lower() == 'ronaldo':
    print(name.title() + " is not a cricketer.")
  if name.lower() == 'sachin':
    print(f"Only 1 player with 100 centuries: {name.title()}.")
  if name.lower() == 'virat':
    print(f"The king : {name.title()} Kohli.")
  else:
    print(name.title() + " is a cricketer.")

          # Revision
unconfirmed_user = ['alice', 'brian', 'candace']
confirmed_user = []
denied_user = []
while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print("Verifying user: " + current_user.title())
    if current_user == 'candace':
        denied_user.append(current_user)
    else:
        confirmed_user.append(current_user)
        if confirmed_user:
          print("Adding user: " + current_user.title())
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_user: 
  print(confirmed_user)
print("\nThe following users have been denied:")
for denied_user in denied_user:
 print(denied_user)

message = "\n[For 'candace']:"
message += "\nCandance enter your password to confirm: "
message += "\nI'm sorry, your request has been denied because of legal issues."
message += "\nIf you are verified please enter 'quit' and exit."
while message:
    prompt = input(message)
    if prompt == 'quit':
        break
    if prompt != 'candace':
        print("Your request has been confirmed.")
        print("Quitting the program.")
        break

    if prompt == 'candace':
     print("Candace enter your password to confirm: ")
     pwd = int(input("Password: "))
     if pwd == 1234:
      print("Your request has been confirmed.")
      break
     else:
      print("I'm sorry, your request has been denied because of legal issues.")
      print("If you are verified please enter 'quit' and exit.")
      continue
     
   
    
