# user entered list

# When the below variable has quit as the value, the program quits.
quit_var = ''

# Other Variables

user_name = ''

# The list. 

number_in_list = []


print('\nWelcome to my program!')

user_name = input('\nWhat is your name? ')

print('\nHi %s, let\'s get started.' % user_name.title())

print('-------------------------------------------------')
print('\nLet\'s build a list of numbers.To leave the program, just type \'quit\'.')

while quit_var != 'quit':
    quit_var = input('Enter number:')

    if quit_var != 'quit':
        number_in_list.append(quit_var)

for n in number_in_list:
    print(n)



