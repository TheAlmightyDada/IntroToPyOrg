# With keyword arguments, we can give the arguements in any order we wand as
#   long as we use the name of the arguments in our calling statment:

def describe_person(first_name, last_name, age):
    # This function takes in a person's first and last name
    #   and their age.
    # It then prints this information our in a simple format.
    print('First name: %s' % first_name.title())
    print('Last name: %s' % last_name.title())
    print('Age: %d\n' % age)

describe_person(age=71, first_name='brian', last_name='kernighan')
describe_person(first_name='ken', age=70, last_name='thompson')
describe_person(last_name='goldberg', first_name='adele', age=68)