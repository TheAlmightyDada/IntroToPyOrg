numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numbers:
    print(n)

# The above method works, but there are better ways. 
# for examplem the range() function.

## Range Function ##

for n in range(1,11):
    print(n)

#adding a step value

for n in range(1,21,2):
    print(n)
print('\n\n')

#The first MILLION numbers in a list
numbers2 = list(range(1,1000001))

print('The lit \'numbers\' has ' + str(len(numbers2)) + ' numbers in it.')

print('These are the last 10 numbers  in the list: ')

for n in numbers2[-10:]:
    print(n)

## min(), max() and sum() functions

ages =[23, 16, 14, 28, 19, 11, 38]

youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)

print('Our youngest reader is ' + str(youngest) + ' years old.')
print('Our oldest reader is ' + str(oldest) + ' years old.')
print('Together, we have ' + str(total_years) + ' years worth of life experience.')
