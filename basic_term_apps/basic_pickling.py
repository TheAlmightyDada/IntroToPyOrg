import pickle

# This program asks the user for some animals, and stores them. 

# Make an empty list to store new animals in. 
animals = []

# Create a loop that lets users store new animals.
new_animal = ''

while new_animal != 'quit':
    print('\n Please tell me a new animal to remember.')
    new_animal = input('Enter \'quit\' to quit: ')
    if new_animal != 'quit':
        animals.append(new_animal)

# Try to save the animals to the file 'animals.pydata'. 

try:
    file_object = open('animal.pydata', 'wb')
    pickle.dump(animals, file_object)
    file_object.close()

    print('\n I will remember the following animals:')
    for a in animals:
        print(a.title())
except Exception as e:
    print(e)
    print('\n I couldn\'t figure out how to store the animals. Sorry.')

