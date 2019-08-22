# I would like to try and create a function that looks for a given word. Here goes.


python_words = {'list': '''A collection of vallues that are not connected, 
but have an order''',
                'dictionary': '''A collection of key-value pairs.''',
                'function': '''A named set of instructions that defines a set
of actions in Python.''',
                }

def inputlookup():
    return input('Define Word: ')
def listlookup():
    listchoice = return input('Define Dictionary: ')

def lookup(list,word):
    print('Word: %s' % word)
    print('Meaning: %s' % list[word])

def autolookup():
    lookup(listchoice,wordchoice)

wordchoice = ''
listchoice = {}

lookup(python_words,'list')









