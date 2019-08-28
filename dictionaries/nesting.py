favorite_numbers = {'eric': [3, 11, 19, 23, 42],
                    'ever': [2, 4, 5],
                    'willie': [5, 35, 120],
                    }

#Looping through the dictionary
for n, nums in favorite_numbers.items():
    print('%s\'s favorite numbers are: %s' % (n, nums))

# Display each persons fav colours individually

for name in favorite_numbers:
    print('\n%s\'s fav numbers are:' % name.title())
    for n in favorite_numbers[name]:
        print(n)

print('\n')
print(favorite_numbers['ever'])

for n in favorite_numbers['ever']:
    print(n)
