# Lesson 2a

# Whitespace

# Spaces = ' '
# Tabs = '\t'
# Newlines = '\n'

#Examples of Tabs

print("I'm getting fed up of typing 'Hello World!'") # Nothing
print("\tI'm getting fed up of typing 'Hello World!'") #Tab at the front of the string
print("I'm getting fed up of typing\t 'Hello World!'") #Tab after 'typing'

#Examples of newlines

print('\n')#Just a new line to seperate newlines from tabs

print("I'm getting fed up of typing 'Hello World!'") #Nothing
print("\nI'm getting fed up of typing 'Hello World!'") #Newline at the beginning
print("I'm getting fed up of typing \n'Hello World!'") #Newline before 'Hello World'
print("\n\n\nI'm getting fed up of typing 'Hello World!'")#Three new lines before the string.

# To strip whitespace from strings, which is useful if it is user provided information.
# the following action is needed

# Lets say someone defines there name and DOB;

name = 'Kamal ' # As you can see, there is an un-needed space there.
DOB = '14.08.1973' 
#Because of this space if I print the following;

print(name + DOB) # There is a space between the Name and the DOB

#To get rid of this space we need to use the stip 'method'

print(name.strip()+DOB)

# You can also stip just from the left with .lstrip or just from the right with .rstrip

## Numbers

print(3+2)#addition
print(3-2)#subtraction
print(3*2)#multiplication
print(3/2)#division
print(3**2)#to the power

# Floating-Point Numbers

print(0.1+0.2)