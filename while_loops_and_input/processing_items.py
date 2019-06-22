unconfirmed_users = ['ada', 'billy', 'clarence', 'daria']
confirmed_users = []

# Work through the list, and confirm each user.
while len(unconfirmed_users) > 0:

    # Get the latest unconfirmed user, and process them.
    current_user = unconfirmed_users.pop()
    print('Confirming user %s...confirmed!' % current_user.title())

    # Move the current user to the list of confirmed users. 
    confirmed_users.append(current_user)

# Prove that we have finished confirming all users. 

print('\nUnconfirmed users:')
for u in unconfirmed_users:
    print('-' + u.title())

print('\nConfirmed users:')
for u in confirmed_users:
    print('-' + u.title())