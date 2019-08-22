# Create an empty dictionary.

python_words ={}

# Fill in dictionary, pair by pair. 

python_words['list'] = 'A collection of values that are not connected, but have an order'
python_words['dictionary'] = 'A collection of Key-Value pairs.'
python_words['function'] = 'A named set of instructions that defines a set of actions in Python'

# Print out the items in the dictionary. 

for w, m in python_words.items():
    print('\nWord: %s' % w)
    print('Meaning: %s' % m)


# Modify values in dictionary

print('\ndictionary: ' + python_words['dictionary'])

# Clarifying one of the meanings. 

python_words['dictionary'] = '''A collection of key-value pairs. Each key can be 
used to access its corresponding value'''

print('\ndictionary: ' + python_words['dictionary'])