def describe_person(first_name, last_name, age=None, favorite_language=None,\
     died=None):

     #Compulsory Information
    print("First name: %s" % first_name.title())
    print("Last name: %s" % last_name.title())
     
     # Optional Information
    if age:
        print('Age: %d' % age)
    if favorite_language:
        print('Favorite language: %s' % favorite_language)
    if died:
        print('died: %s' % died)
    
    print('\n')

describe_person('brian', 'kernighan', favorite_language='C')
describe_person('ken', 'thompson', age=70)
describe_person('adele', 'goldberg', age=68, favorite_language='Smalltalk')
describe_person('dennis', 'ritchie', favorite_language='C', died=2011)
describe_person('guido', 'van rossum', favorite_language='Python')
describe_person('terry', 'Jacobs', age=None)


