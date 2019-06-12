#Removing items from a list

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

#remove the first dogfrom the list

del dogs[0]

print(dogs)

## Removing items by value

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

# Remove 'australian cattle dog' 

dogs.remove('australian cattle dog')

print('\n' + str(dogs))

# '.remove' only works for the first item in the list

