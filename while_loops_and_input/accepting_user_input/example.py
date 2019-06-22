# Start with a list containning several names.
names = ['dale','guy', 'mothafucka jones']

# Ask the user for a name.
new_name = input('Please tell me someone I should know: ')

# Add the new name to our list. 
names.append(new_name)

# Show that the name has been added to the list. 
for i, n in enumerate(names):
    print(str(i) + ' ' + n.title())