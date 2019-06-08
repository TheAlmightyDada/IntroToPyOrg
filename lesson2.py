#This lesson is about Variables and Strings.


# A Variable holds a value. If x where to
# equal y (x=y) then in future if I typed
# x I would get y.

message = "Hello Python World!"

print (message)

################################

#strings

# Strings are a type of variable
# They are strings when they are surronded in qoutes.
# So above is also a string

qoute = "This is a string, in a string you can have more qoutation marks 'see, like this'"

    #Changing Case

#This is my string.
first_name = 'kamal'

#Will print the string 'first_name' as is i.e. - kamal
print(first_name)

#will print the string 'first_name' with an upper case first letter i.e. Kamal
print(first_name.title())

#will print the string 'first_name' in ALL CAPS
print(first_name.upper())

# It looks like .capitalize() does the same as .title() - I think title capitalises
# each word in a string. 
print(first_name.capitalize())

# Multi word string .title() test. 

# Defining the variable string

invitcus = "out of the night that covers me"

# .title() test.
print(invitcus.title())

# yes, that's what .title() does.

# .lower() prints all lower case.
print(first_name.lower())

#Where there is a dot with a word and some brakets - these are called 'methods', they do something to a variable. (eg. .lower())

############################################
#Combining Strings (Concatenation)

first_name1 = "eddard"
Last_name1 = "stark"
full_name1 = first_name1 + ' ' + Last_name1
winterfell = full_name1 + ',' + ' ' + "Winter Is Coming"

print(full_name1.title())
print(winterfell)
