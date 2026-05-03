                       # Revision
unprocessed_users = ['alice', 'brian', 'candace']
verified_user = []
completely_unverified_users = []

while unprocessed_users:
    verified_usersy = unprocessed_users.pop()
    print("Verifying user: " + verified_usersy.title())

    if verified_usersy == 'brian':
        completely_unverified_users.append(verified_usersy)
    else:
        verified_user.append(verified_usersy)
print("The following users have been verified: ")
for verified_usera in verified_user:
    print(verified_usera)
print("The following users still need to be verified: ")
for completely_unverified_usersa in completely_unverified_users:
    print(completely_unverified_usersa)
        
