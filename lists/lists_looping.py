birds = ['ducks', 'geese', 'swans', 'grouse', 'pheasants', 'partridges', 'quail']

for bird in birds:
    print(bird.title())

#'for' gets python ready to run a loop.
#'bird' is a tempory placeholder as we are going to ask python to print it. It could be anything.
# Then we ask python to print 'bird' which will change
#as the loop goes on to whatever is next in the list.
# the 'for' tells python to run the loop for the lenght of
# the list 'birds'

for bird in birds:
    print('I like'+ ' '+ bird.title())
    print('I really do, it\'s true. ' + 'I just love ' + bird)
print('\nAt the end of the loop, bird = ' + bird)   

bird = 'null'   

print('now, bird =' + bird)