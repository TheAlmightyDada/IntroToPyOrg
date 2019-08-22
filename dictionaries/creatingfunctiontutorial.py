def show_words_meanings(python_words):
    # This function takes in a dictionary of python words and meanings,
    #   and prints out eace word with its meanings.

    print('\n\nThese are the Python words I know:')
    for w, m in python_words.items():
        print('\nWord: %s' % w)
        print('Meaning: %s' % m)

def show_words_meanings_clean(python_words):
    print('\n\nThese are the Python words I know:')
    for w, m in python_words.items():
        print('\n%s: %s' % (w,m))

python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }
show_words_meanings(python_words)

# Remove the word 'list' and its meaning. 

del python_words['list']

show_words_meanings(python_words)

print('\n')

show_words_meanings_clean(python_words)