# Define that actions for each choice we want do offer.
def ride_bicycle():
    print('\nHere is a bike, have fun!\n')

def go_running():
    print('\nHere are some running shoes. Run fast\n')

def climb_mountain():
    print('\nHere is a map. Can you leave a trip plan for us?\n')

# Give the user some context. 
print('\nWelcome to the nature centre. What would you like to do?')

# Set an initial value for choice. 

choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to take a bicycle ride.")
    print("[2] Enter 2 to go for a run.")
    print("[3] Enter 3 to climb a mountain.")
    print("[q] Enter q to quit.")

    # Ask for the user's choice.
    choice = input('\nWhat would you like to do?')


    # Respond to the user's choice.
    if choice == '1':
        ride_bicycle()
    elif choice == '2':
        go_running()
    elif choice == '3':
        climb_mountain()
    elif choice == 'q':
        print("\nThanks for playing. See you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
    
    