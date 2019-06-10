# Empty list to hold our users
usernames = []

# Add some users
usernames.append('katy')
usernames.append('sarah')
usernames.append('cody')

# Greet our users

for u in usernames:
    print('Welcome to the club ' + u.title())

# Recognise our first user, welcome our newest.

print('\nThank you for being our first user, ' + usernames[0] +' !')
print('and a warm welcome to our newest user, ' + usernames[-1] + '\n')

#Sorting a list

print('sorting a list...\n')

#putting users in aplhabetical order
print('Aplhabeticaly\n')
usernames.sort()

#Displaying list in sorted order

for u in usernames:
    print(u.title())

print('\n'
    )
# Reverse alphabetical order

print('Reversed Aplhabetically\n')

usernames.sort(reverse=True)

for u in usernames:
    print(u.title())

#Restating the list, to test sorted() vs sort()

# Empty list to hold our users
usernames = []

# Add some users
usernames.append('katy')
usernames.append('sarah')
usernames.append('cody')

#sorted keeps list's original order, while sorting - is used in a loop

for u in sorted(usernames):
    print(u.title())

#And then again in original order

print('\n')
for u in usernames:
    print(u.title())

#and then just for fun, as an enumerated list;

for ind, u in enumerate(usernames):
    i = str(ind)
    print(i + u.title())

#and then finally, to reverse the order of the list. 

print('\n To reverse the order of the list:\n')

usernames.reverse()

print(usernames)

