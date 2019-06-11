numbers = [1,3,4,2,5]

#sort() puts numbers in increasing order.

numbers.sort()
n = str(numbers)
print(n + '\n')

#sort(reverse=True) puts numbers in decreasing order.
numbers.sort(reverse=True)
print(numbers)

#sorted() still works too. 
print('\n')

print(sorted(numbers))
print(numbers)

#reverse() works for numbers too. 

print('\n')

numbers.reverse()
print(numbers)

