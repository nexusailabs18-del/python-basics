          # Using a while loop with Lists and dictionaries
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for current_users in confirmed_users:
    print(current_users.title())

          # Using a while loop with Lists and dictionaries
players = ['charles', 'martina', 'michael', 'florence', 'eli']
registered_players = []
while players:
    current_player = players.pop()
    print(f"Verifying: {current_player.title()}")
    registered_players.append(current_player)

print("\nThe following players have been registered:")
for player in registered_players:
     if player == 'eli':
          continue
     else:
       print(player.title())

if 'eli' not in player:
     print("\nEli is not verified yet...")

          # Removing all Instances of Specific Values from a List:
cricketers = ['Sachin Tendulkar', 'Virat Kohli', 'Rohit Sharma', 'Ravindra Jadeja', 'Rohit Sharma']
print(cricketers)
while 'Rohit Sharma' in cricketers:
    cricketers.remove('Rohit Sharma')
print(cricketers)

                    # Filling a Dictionary with User Input:
responses = {}
polling_active = True
while polling_active:
         name = input("\nWhat is your name?")
         respone = input("Which mountain would you like to climb someday?")
         responses[name] = respone
         repeat = input("Would you like to let another person respond? (yes/no)")
         if repeat == 'no':
             polling_active = False

for name, respone in responses.items():
    print(name + " would like to climb " + respone + ".")

