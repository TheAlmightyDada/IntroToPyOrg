dogs  = ['willie', 'hootz', 'peso', 'juno']

if len(dogs) > 3:
    print('Wow, we have a lot of dogs here!')

people = ['dennis', 'charlie', 'cindy', 'dee', 'mac', 'frank']

people_removal = people[-3:]

'''for p in people_removal:
    del i'''


if len(people) > 3:
    del people[-3:]

for p in people:
    print(p.title())