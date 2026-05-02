                         # Revision
unconfirmed_users = ['andrew', 'carolina', 'david']
confirmed_users = []
non_verified = []
while unconfirmed_users:

    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been verified:")
for confirmed_user in confirmed_users:
        if confirmed_user == 'carolina':
         non_verified.append(confirmed_user)
         continue
        print(confirmed_user.title())
print("The following users have not been verified:")
for user in non_verified:
    print(user.title())

