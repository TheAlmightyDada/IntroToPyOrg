# Creating a function to test the length of a list and return a value.

def amount_check (list, subject):
    if len(list) > 3:
        print('Wow, there are a lot of ' + subject + '\'s here!')
    else:
        print('Okay, there are a reasonable amount of '+ subject+ '\'s here.')

dogs = ['willie', 'hootz', 'peso', 'juno']
actors = ['charlie', 'mac']

amount_check(dogs,'dog')
amount_check(actors,'actor')


