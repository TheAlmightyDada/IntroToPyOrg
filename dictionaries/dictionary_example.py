python_words = {'list': '''A collection of vallues that are not connected, 
but have an order''',
                'dictionary': '''A collection of key-value pairs.''',
                'function': '''A named set of instructions that defines a set
of actions in Python.''',
                }

# Print out the items in the dictionary.

for w, m in python_words.items():
    print('\nWord: %s' % w)
    print('Meaning: %s' % m)

# Retreving indivdual items.

print('\nWord: %s' % 'list')
print('Meaning: %s' % python_words['list'])


