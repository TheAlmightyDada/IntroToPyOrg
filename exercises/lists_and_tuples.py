
#! Ex 01, First List -- Store the values 'python', 'c', and 'java' in a list.
    #!  Print each of these values out, using their position in the list.

print(' Ex 01, First List')

programming_languages = ['python', 'c', 'java']

print(programming_languages[0].title())
print(programming_languages[1].title())
print(programming_languages[2].title())

#! Ex 02, First Neat List -- Store the values 'python', 'c', and 'java' in a 
    #! list. Print a statement about each of these values, using their 
    #! position in the list. Your statement could simply be, 
    #! 'A nice programming language is value.'

print('\n Ex 02, First Neat List')

ex_02_list = ['python', 'c', 'java']

print(ex_02_list[0].title() + ' is a programming language I would like to learn')
print(ex_02_list[1].title() + ' is a programming language I would like to learn')
print(ex_02_list[2].title() + ' is a programming language I would like to learn')

#! Ex 03, Your First List -- Think of something you can store in a list. Make
    #! a list with three or four items, and then print a message that includes 
    #! at least one item from your list. Your sentence could be as simple as, 
    #! "One item in my list is a __."

print('\n Ex 03, Your First List')

ex_03_list_birds = ['robin', 'collared dove', 'great tit', 'goldfinch']

print(ex_03_list_birds[0].title() + ' is a bird in the United Kingdom')
print(ex_03_list_birds[1].title() + ' is a bird in the United Kingdom')
print(ex_03_list_birds[2].title() + ' is a bird in the United Kingdom')
print(ex_03_list_birds[3].title() + ' is a bird in the United Kingdom')

#! Ex 04, First list (loop) -- Repeat First List, but this time use a loop to 
    #! print out each value in the list.

print('\n Ex 04, First list (loop)')

for l in programming_languages:
    print(l.title())

#! Ex 05, First Neat List (loop) -- Repeat First Neat List, but this time use a
    #! loop to print out your statements. Make sure you are writing the same 
    #! sentence for all values in your list. Loops are not effective when you 
    #! are trying to generate different output for each value in your list.

print('\n Ex 05, First Neat List (loop)')

for l in ex_02_list:
    print(l.title())

#! Ex 06, Your First List (loop) -- Repeat Your First List, but this time use 
    #! a loop to print out your message for each item in your list. 
    #! Again, if you came up with different messages for each value in your 
    #! list, decide on one message to repeat for each value in your list.

print('\n Ex 06, Your First List (loop)')

for b in ex_03_list_birds:
    print( 'A ' + b.title() + ' is a bird that is found in the United Kingdom.')

#! Ex 07, Working List -- Make a list that includes four careers, 
    #! such as 'programmer' and 'truck driver'.

print('\n Ex 07, Working List')


careers = ['accountant', 'mechanic', 'pilot', 'artist']

    #! Use the list.index() function to find the index of one career in your list.

print(careers.index('accountant'))
    
    #! Use the in function to show that this career is in your list.

print('mechanic' in careers)

    #! Use the append() function to add a new career to your list.

careers.append('taxi driver')

    #! Use the insert() function to add a new career at the beginning of the list.

careers.insert(2,'actor')

    #! Use a loop to show all the careers in your list.

for c in careers:
    print(c.title())

#! Ex 08, Starting From Empty -- Create the list you ended up with in Working 
    #! List, but this time start your file with an empty list and fill it up 
    #! using append() statements. Print a statement that tells us what the 
    #! first career you thought of was. Print a statement that tells us what 
    #! the last career you thought of was.

print('\n Ex 08, Starting From Empty')

list_of_careers = []

list_of_careers.append('accountant')
list_of_careers.append('mechanic')
list_of_careers.append('actor')
list_of_careers.append('pilot')
list_of_careers.append('taxi driver')

print('The first thing I thought of was an ' + list_of_careers[0].title())
print('The last thing I thought of was an ' + list_of_careers[-1].title())

#! Ex 09, Ordered Working List -- Start with the list you created in Working List.
    #! You are going to print out the list in a number of different orders.
    #! Each time you print the list, use a for loop rather than printing the raw list.
    #! Print a message each time telling us what order we should see the list in.


#! Print the list in its original order.

for c in careers:
    print(c.title())

#! Print the list in alphabetical order.

print('\n')

for c in sorted(careers):
    print(c.title())

#! Print the list in its original order.

print('\n')

for c in careers:
    print(c.title())

#! Print the list in reverse alphabetical order.

for c in sorted(careers, reverse = True):
    print(c.title())

#! Print the list in its original order.

print('\n')

for c in careers:
    print(c.title())

#! Print the list in the reverse order from what it started.

careers.reverse()

print('\n')
for c in careers:
    print(c.title())


#! Print the list in its original order

careers.reverse()

print('\n')

for c in careers:
    print(c.title())

#! Permanently sort the list in alphabetical order, and then print it out.

print('\n')
careers.sort()

for c in careers:
    print(c.title())



#! Permanently sort the list in reverse alphabetical order, and then print it out.

print('\n')

careers.sort(reverse = True)

for c in careers:
    print(c.title())


#! Ex 10, Ordered Numbers -- Make a list of 5 numbers, in a random order.
    #! You are going to print out the list in a number of different orders.
    #! Each time you print the list, use a for loop rather than printing the raw list.
    #! Print a message each time telling us what order we should see the list in.

number_list = [5, 12, 4, 6, 8]

    #! Print the numbers in the original order.

print('\nNumbers in original order:')

for n in number_list:
    print(n)

    #! Print the numbers in increasing order.

print('\nNumbers in increasing order.')

for n in sorted(number_list):
    print(n)

    #! Print the numbers in the original order.

print('\nNumbers in original order.')

for n in number_list:
    print(n)

    #! Print the numbers in decreasing order.

print('\nNumbers in decreasing order.')

for n in sorted(number_list, reverse = True):
    print(n)

    #! Print the numbers in their original order.
print('\nNumbers in their original order.')

for n in number_list:
    print(n)

    #! Print the numbers in the reverse order from how they started.

print('\nNumbers reversed from original order.')

number_list.reverse

for n in number_list:
    print(n)

    #! Print the numbers in the original order.

print('\nNumbers in their original order.')

number_list.reverse

for n in number_list:
    print(n)

    #! Permanently sort the numbers in increasing order, and then print them out.
print('\nNumbers permanently in increasing order.')

number_list.sort()

for n in number_list:
    print(n)

    #! Permanently sort the numbers in decreasing order, and then print them out

print('\nNumbers permanetly in decreasing order.')

number_list.sort(reverse = True)

for n in number_list:
    print(n)


#! Ex 11, List Lengths -- Copy two or three of the lists you made from the 
    #! previous exercises, or make up two or three new lists.
    #! Print out a series of statements that tell us how long each list is.

# I made a function to print the length of a list.

def list_length(list_name):
    ll = len(list_name)
    print(ll)

print('\n Ex 11, List Length')

print('\nThe length of the list from Ex 01 is:')

list_length(programming_languages)

print('\nThe length of the list from Ex 02 is:')

list_length(ex_02_list)

print('\nThe length of the list from Ex 03 is:')

list_length(ex_03_list_birds)

print('\nThe length of the list from Ex 07 is:')

list_length(careers)

print('\nThe length of the list from Ex 08 is:')

list_length(list_of_careers)

print('\nThe length of the list from Ex 10 is:')

list_length(number_list)


#! Ex 12, Famous People -- Make a list that includes the names of four famous people.
    #! Remove each person from the list, one at a time, using each of the four 
        #! methods we have just seen:
    #! Pop the last item from the list, and pop any item except the last item.
    #! Remove one item by its position, and one item by its value.
    #! Print out a message that there are no famous people left in your list, 
        #! and print your list to prove that it is empty.

print('\n Ex 12, Famous People')

famous_peeps = ['charlie day', 'glenn howerton', 'rob mcelhenney', 
'kaitlin olson']

del famous_peeps[1]

famous_peeps.remove('kaitlin olson')

last_celeb = famous_peeps.pop(0)
last_celeb2 = famous_peeps.pop()

print(last_celeb)
print(famous_peeps)

#! Ex 13, Alphabet Slices -- Store the first ten letters of the alphabet in a list.
#!  Use a slice to print out the first three letters of the alphabet.
#!  Use a slice to print out any three letters from the middle of your list.
#!  Use a slice to print out the letters from any point in the middle of your 
#!    list, to the end.


print('\n Ex 13, Alphabet Slices')

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(alpha_list[:3])
print(alpha_list[4:7])
print(alpha_list[7:])

#! Ex 14, Protected List -- Your goal in this exercise is to prove that copying
#!   a list protects the original list.
#! Make a list with three people's names in it.
#! Use a slice to make a copy of the entire list.
#! Add at least two new names to the new copy of the list.
#! Make a loop that prints out all of the names in the original list, along 
#!   with a message that this is the original list.
#! Make a loop that prints out all of the names in the copied list, along with 
#!   a message that this is the copied list.

print('\n Ex 14, Protected List')

ex14_list = ['miranda', 'shaft', 'stephen']

ex14_copy = ex14_list[:]

ex14_copy.append('anthony')
ex14_copy.append('charlie')

print('These are the names of the original list: ')

for n in ex14_list:
    print(n.title())

print('\nThese are the names of the new \'copied\' list: ')

for n in ex14_copy:
    print(n.title())

#! Ex 15, First Twenty --  Use the range() function to store the first twenty 
#!   numbers (1-20) in a list, and print them out.

print('\n Ex 15, First Twenty')

first_twenty =[list(range(1,21))]

for n in first_twenty:
    print(n)

#! Ex 16, Five Wallets -- Imagine five wallets with different amounts of cash 
#!  in them. Store these five values in a list, and print out the following sentences:
#!  "The fattest wallet has $ value in it."
#!  "The skinniest wallet has $ value in it."
#!  "All together, these wallets have $ value in them."

print('\n Ex 16, Five Wallets')

fivewallets = [15,358,42,10]

fattest_wallet = max(fivewallets)
skinniest_wallet = min(fivewallets)
total_cash = sum(fivewallets)

print('The fattest wallet has £%d in it' % fattest_wallet)
print('The skinniest wallet has £%d in it' % skinniest_wallet)
print('The total cash in all the wallets is £%d' % total_cash)

#! Ex 17, Multiples of Ten -- Make a list of the first ten multiples of ten 
#!  (10, 20, 30... 90, 100). There are a number of ways to do this, but try 
#!   to do it using a list comprehension. Print out your list.

print('\n Ex 17, Multiples of Ten')

mot = [n*10 for n in range(1,11)]

for n in mot:
    print(n)

#! Ex 18, Cubes -- We saw how to make a list of the first ten squares.
#!   Make a list of the first ten cubes (1, 8, 27... 1000) using a list
#!   comprehension, and print them out.

print('\n Ex 18, Cubes')

cubes = [n**3 for n in range(1,11)]

for n in cubes: 
    print(n)

#! Ex 19, Awesomeness --  Store five names in a list. Make a second list 
#!  that adds the phrase "is awesome!" to each name, using a list 
#!  comprehension. Print out the awesome version of the names.

print('\n Ex 19, Awesomeness')

awesome_names_1 = ['derek','james','julie','alisha','toran']

awesome_names_2 = [n.title() + ' is awesome!' for n in awesome_names_1]

for n in awesome_names_2:
    print(n)

#! Ex 20, Working Bakwards -- Write out the following code without using a 
#!  list comprehension:

#!  plus_thirteen = [number + 13 for number in range(1,11)]

print('\n Ex 20, Working Bakwards')

naked_numbers = []

for n in range(1,11):
    naked_numbers.append(n + 13)
    
for n in naked_numbers:
    print(n)

#! Ex 21, Listing a Sentance -- Store a single sentence in a variable. Use a 
#!  for loop to print each character from your sentence on a separate line.

sent_var = 'Store a single sentence in a variable.'

for l in sent_var:
    print('\n %s' % l)

#! Ex 22, Sentance List -- Print your raw list (don't use a loop, 
#!  just print the list).

sent_list = list(sent_var)

print(sent_list)