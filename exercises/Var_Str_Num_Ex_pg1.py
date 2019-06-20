
# ! Ex 01, Hello World - variable -- "Store your own version of the message "Hello 
 #! World" in a variable, and print it."

print('\n Ex 01, Hello World')

# Defining Variable.
first_variable = 'Hello World!'

# Printing Variable.
print(first_variable)

#* This was done correctly.

# ! Ex 02, One Variable, Two Messages -- Store a new message in the same 
 # ! variable, and then print that new message

print('\n Ex 02, One Variable')

# Changing defined variable. 
first_variable = 'new variable ready for printing'

print(first_variable.capitalize())

# ! Ex 03, Someone Said -- Find a quote that you like. Store the quote in a 
 # ! variable, with an appropriate introduction such as "Ken Thompson once 
 # ! said, 'One of my most productive days was throwing away 1000 lines of 
 # ! code'". Print the quote.

print('\n Ex 03, Someone Said')

# Defining Quote
quote = '''Life is short, and if we enjoy every moment of every day, then we will
be happy no matter what happens or what changes along the way.'''

# Printing Statement #? BTW, three quotation marks allow you to continue a 
                       #? string over multiple lines.
print('Some person once said, \'' + quote + '''. I wish I could think of
something so profound\' ''' ) 

#! Ex 04, First Name Cases -- Store your first name, in lowercase, in a 
    #! variable. Using that one variable, print your name in lowercase, 
    #! Titlecase, and UPPERCASE.

print('\n Ex 04, First Name Cases')

my_name = 'the almighty dada'

print(my_name.title())
print(my_name.lower())
print(my_name.upper())

#! Ex 05, Full Name -- Store your first name and last name in separate 
    #! variables, and then combine them to print out your full name.

print('\n Ex 05, Full Name')

fawlty_first_name = 'basil'
fawlty_last_name = 'fawlty'

print(fawlty_first_name.title() + ' ' + fawlty_last_name.title())

#! Ex 06, About This Person -- Choose a person you look up to. Store their 
    #! first and last names in separate variables. Use concatenation to make a 
    #! sentence about this person, and store that sentence in a variable.

print('\n Ex 06, About This Person')

idol_fn = 'gordon'
idol_ln = 'ramsay'
idol_full_name = idol_fn.title() + ' ' + idol_ln.title()

my_idol = 'My idol is ' + idol_full_name + ''' I like him because he is Honest. 
Straightforward. Doesn\'t pull punches. Worked hard to get where he is.'''

print(my_idol)

#! Ex 07, Name Strip -- Store your first name in a variable, but include at 
    #! least two kinds of whitespace on each side of your name.
    #! Print your name as it is stored.
    #! Print your name with whitespace stripped from the left side, then 
    #! from the right side, then from both sides.


print('\n Ex 07, Name Strip')

ex7_name = '\tingrid '

print(ex7_name.title())

print(ex7_name.title().strip())

#! Ex 08, Arithmetic -- Write a program that prints out the results of at least
    #! one calculation for each of the basic operations: addition, subtraction,
    #! multiplication, division, and exponents.

print('\n Ex 08, Arithmetic')

# Addition
print('Addition')
print(1+1)

# Subtraction
print('\nSubtraction')

print(5-3)

# Multiplication
print('\nMultiplication')

print(8*11)


# Division
print('\nDivision')

print(8/2)

# Exponents (to the power of)
print('\nExponents (to the power of)')

print(5**5)

#! Ex 09, Order of Operations -- Find a calculation whose result depends on
    #! the order of operations. Print the result of this calculation using 
    #! the standard order of operations. Use parentheses to force a nonstandard
    #! order of operations. Print the result of this calculation.

# Order of Operation: BIDMAS - Brackets, Indices, Division, Multiplication etc.

print('\n Ex 09, Order Of Operations')

print('The sum (2+2)+4**2/5*6+8-3 is equal to:')

print((2+2)+4**2/5*6+8-3)

print('''\n This should be worked out as follows, first the brakets ~ 2+2 = 4.
    therefore the new equation is: 4+4**2/5*6+8-3. Then indices ~ 4**2 = 16.
    So the new equation is 4+16/5*6+8-3. Division follows ~ 16/5 = 3.2. 
    New Equation: 4+3.2*6+8-3. Multiplication ~ 3.2*6 = 19.2.
     New Equation: 4+19.2+8-3. Addition & Subtraction ~ 4+19.2+8-3 = 28.2\n''')

print('''If we rearrange the brackets, but otherwise leave the sum the same, we
 we get: 2+(2+4)**2/(5*6)+8-3. The solution to which is: ''')

print(2+(2+4)**2/(5*6)+8-3)

print('''\n This is because it is worked out as follows. First the brackets (2+4)
 and (5*6) which are equal to 6 & 30 respectivley. Therefore the equation 
 becomes 2 + 6**2 / 30 + 8 - 3. Then we do indices 6**2 = 36. 
 Equation = 2 + 36 / 30 + 8 - 3. Next is division ~ 36/30 = 1.2
 Therefore the equation becomes, 2 + 1.2 + 8 - 3. Finally all of the additions
 and subtractions = 8.2)''') 

#! Ex 10, Long Decimals -- On paper, 0.1+0.2=0.3. But you have seen that in 
    #! Python, 0.1+0.2=0.30000000000000004. Find at least one other calculation
    #! that results in a long decimal like this.
print('\nEx 10, Long Decimals')

# I'm not really sure why this works. I'll have to come back to it.

print(4/5*6)