# FIRST EXAMPLE

def thank_you(name):
    # This function prints a two-line personalised thank you message.
    print('\nYou are doing good work, %s' % name)
    print('Thank you very much for your efforts on this project')

thank_you('Adriana')
thank_you('Billy')
thank_you('Caroline')

# The above works well but it fails if you do not enter a value for 'name':

# You can give functions a default value: 

def thank_u(name='everyone'):
    print('\nYou are doing good work, %s' % name)
    print('Thank you very much for your efforts on this project')

thank_u('Adriana')
thank_u('Billy')
thank_u('Caroline')
thank_u()

