
dogs = ['willie','hootz']

if 'willie' in dogs:
    print('Hello, Willie!')
if 'hootz' in dogs:
    print('Hello, Hootz')
if 'peso' in dogs:
    print('Hello, Peso')
if 'monty' in dogs:
    print('Hello, Monty') 

# This could be written much better with a loop. 

dogs_we_know = ['willie', 'hootz', 'peso', 'monty', 'juno', 'turkey']
dogs_present = ['willie', 'hootz','freddie']

# Go through all the dogs we know and greet the ones that are present.
print('\n')

for d in dogs_present:
    if d in dogs_we_know:
        print('Hello, %s' % d.title())
    else:
        print('Nice to meet you %s' % d.title())
        dogs_we_know.append(d)

print('\n')

for d in dogs_present:
    if d in dogs_we_know:
        print('Hello, %s' % d.title())

    


