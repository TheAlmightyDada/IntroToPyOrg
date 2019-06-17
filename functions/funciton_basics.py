# Functions take something that you would otherwise have to repeat and allow 
    # you to come up with a peice of code that is easily defined.

# For example, if I had three employees that I wanted to thank - this would be
    # the long way to do it.

print('You are doing good work, Adriana!')
print('Thank you very much for your efforts on this project.')

print('\nYou are doing good work, Billy!')
print('Thank you very much for your efforts on this project.')

print('\nYou are doing good work, Caroline!')
print('Thank you very much for your efforts on this project.')

def thank_you(name):
    print('\nYou are doing good work %s!' % name)
    print('Thank you very much for your efforts on this project.')

thank_you('Jamie')
thank_you('Oliver')
thank_you('Elliot')
