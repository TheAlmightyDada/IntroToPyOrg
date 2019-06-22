# Collatz Conjecture

#! The rules are as follows. 

#? If n is even, then n/2. 
#? If n is odd, then 3n + 1. Then divide the result by 2. 

# A Youtube video to watch for more info: https://www.youtube.com/watch?v=5mFpVDpKX70

#!! THE BELOW CURRENTLY DOES NOT WORK.
n = 1

unconfirmed_numbers = []
confirmed_numbers = []

confirmed_numbers.append(n)

#while n == n:
for i in range(1,100001):
    n = n + 1
    if n % 2 == 0:
        print(str(n) + ' - ' + 'even')
        unconfirmed_numbers.append(n)
        working_n = unconfirmed_numbers.pop(0)
        if working_n in confirmed_numbers:
            i = i + 1
        else:
            confirmed_numbers.append(working_n)
            n = working_n / 2
    else:
        print(str(n) + ' - ' + 'odd')
        unconfirmed_numbers.append(n)
        working_n = unconfirmed_numbers.pop(0)
        if working_n in confirmed_numbers:
            i = i + 1
        else:
            n = (3 * working_n) / 2


print('Current Number:' + str(n))
print('Working Number:' + str(working_n))
print('Confirmed Numbers length:' + str(len(confirmed_numbers)))
print('i: ' + str(i))
        

