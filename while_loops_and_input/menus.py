# Give the user some context. 
print('\nWelcome to the nature center. What would you like to do?')

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enteres the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print('\n[1] Enter 1 to take a bicycle ride.')
    print('\n[2] Enter 2 to go for a run.')
    print('\n[3] Enter 3 to climb a mountain.')
    print('\n[q] Enter q to quit.')

    # Ask for the user's choice.
    choice = input('\nWhat would you like to do? ')
    
    # Respond to the user's choice.
    if choice == '1':
        print('Here\'s a bike, have fun! \n')
    elif choice == '2':
        print('\nHere are some running shoes. Run Fast!\n')
    elif choice == '3':
        print('\nHere is a map. Can you leave a trip plan for us?\n')
    elif choice == 'q':
        print('\nThanks for playing. See you later. \n')
    else:
        print('\n I don\'t understand that choice, please try again. \n')

# Print a message that we are all finished.
print('Thanks agian, bye now.')