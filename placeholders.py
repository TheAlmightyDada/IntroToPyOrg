#A much cleaner way of generating strings that include values.

animal = 'dog'

print('I have a %s' % animal)

#in a list

animals = ['dog', 'cat', 'bear']

for a in animals:
    print('I have a %s' % a)

print('I have a %s, a %s and I have a %s.' % (animals[0], animals[1], animals[2]))

