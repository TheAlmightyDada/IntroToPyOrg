birds = ['ducks', 'geese', 'swans', 'grouse', 'pheasants', 'partridges', 'quail']

# Changing value of item in list

birds[0] = 'pigeon'

for ind, i in enumerate(birds):
    p = str(ind)
    print(p + i.title())

#Finding position on list. 

print(birds.index('geese'))

print('\n\n\n\n')

#Testing whether an item is in a list. 

print('Testing whether an item is in a list\n.')

print('swans' in birds)
print('dog' in birds)

print('\n')

#Adding items to the end of a list

print('Adding items to the end of a list')

birds.append('dove')

for b in birds:
    print(b.title())

#Inserting items into a list

print('\n Inserting items into a list')

birds.insert(1,'ducks')

for i in birds:
    print(i.title())
