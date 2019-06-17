
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
