birds = ['ducks', 'geese', 'swans', 'grouse', 'pheasants', 'partridges', 'quail']

#Normal print of all of the list.
for n in birds: 
    print(n.title())

print('Results for most common UK birds are as follows:\n')
for ind, i in enumerate(birds):
    place = str(ind + 1)
    print(place + ' ' + i.title())