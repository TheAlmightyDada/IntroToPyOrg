
#Ex 1 (First List)- First List.

print('\n Ex 1 (First List)')

p_l = ['python', 'c', 'java']

print(p_l[0])
print(p_l[1])
print(p_l[-1])

#Ex 2 (First Neat List) - Store the values 'python', 'c', and 'java' in a list. Print a statement about each of these values, using their position in the list.

print('\n Ex 2 (First Neat List)')

print('I am learning ' + p_l[0].title())
print('I wish to learn ' + p_l[1].title())
print('I think I will learn ' + p_l[2].title() + ' next')

#Ex 3 (Your First List) - Think of something you can store in a list. Make a list with three or four items, and then print a message that includes at least one item from your list. Your sentence could be as simple as, "One item in my list is a __."

print('\n Ex 3 (Your First List)')
birds = ['ducks', 'geese', 'swans', 'grouse', 'pheasants', 'partridges', 'quail']

print('In my list is a bird with the name ' + '\'' + birds[2] + '\'')

#Ex 4 (First List - Loop) - Repeat First List, but this time use a loop to print out each value in the list.

print('\n Ex 4 (First List - Loop)')

for p in p_l:
    print(p.title())

#Ex 5 (First Neat List - Loop) - Repeat First Neat List, but this time use a loop to print out your statements. Make sure you are writing the same sentence for all values in your list. Loops are not effective when you are trying to generate different output for each value in your list.

print('\n Ex 5 (First Neat List - Loop)')

for p in p_l:
    print('\'' + p.title() +'\''+ ' is a programming laungage')

#Ex 6 (Your First List - Loop) - Repeat Your First List, but this time use a loop to print out your message for each item in your list. Again, if you came up with different messages for each value in your list, decide on one message to repeat for each value in your list.

print('\n Ex 6 (Your First List - Loop)')
for b in birds:
    print(b.title())





