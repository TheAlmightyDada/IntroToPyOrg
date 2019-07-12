import pickle

# This program asks the user for some animals, and stores them.

# Make an empty list to store new animals in. 

animals = []

# Create a loop that lets users stor new animals.

new_animal = ''

while new_animal != 'quit':
    print('\nPlease tell me a new animal to remember.')
    new_animal = (input('type \'quit\' to quit: '))
    if new_animal != 'quit':
        animals.append(new_animal)

# Try to save the animals list to the file animals.pydata

try:
    file_object = open('animals.pydata', 'wb')
    pickle.dump(animals, file_object)
    file_object.close()

    print('\n I will try and remember the following animals: ')
    
    for a in animals:
        print(a.title())

except Exception as e:
    print(e)
    print('\nI couldn\'t figure out how to store the animals. Sorry.')


    