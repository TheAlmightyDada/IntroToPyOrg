# This function takes a number and prints, in an array, all of its divisors.
#   If the number given is a prime - this function tell you that. 

def divisors(number):
    # Create an empty list -- this will be the array that holds the answer.
    list_of_divisors = []

    # Create a test number, this is the starting number the 'divisors()' 
    #   argument will be tested against. (starting at 2 to ignore 1)
    test_n = 2

    # Create a variable for the argument given
    n = number

    # The below 'while loop' tests if there is a remainder when dividing the number
    #   given in the argument number by the current test number.

    # It continues until the 'test_n' is equal to the given argument number.
    while test_n != n + 1:

        # If there is no remainder, the number is added to the 'list_of_divisors'
        #   list.
        if n % test_n == 0:
            list_of_divisors.append(test_n)

        # The test number is then increased by 1 and the loop is run again.
        test_n = test_n + 1

    # The following 'if statement' pulls out prime numbers, based on the length
    #   of the 'list_of_divisors' list.
    if len(list_of_divisors) == 1:
        print('%s is prime' % str(n))
    
    # If the number is not a prime number, the following removes the original
    #   argument number from the list and then prints the list as an array.
    else:
        list_of_divisors.remove(n)
        print(list_of_divisors)

    # Resets 'test_n' to 2

    test_n = 2



divisors(8654474)