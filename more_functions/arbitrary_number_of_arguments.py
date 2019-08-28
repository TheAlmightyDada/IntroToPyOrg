def example_function(arg_1, arg_2, *arg_3):
    # Let's look at the argument values.
    print('\narg_1:', arg_1)
    print('arg_2:', arg_2)
    print('arg_3:', arg_3)

example_function(1,2)
example_function(1,2,3)
example_function(1,2,3,4)
example_function(1,2,3,4,5)

def example_function2(arg_1, arg_2, *arg_3):
    print('\narg_1:', arg_1)
    print('arg_2:', arg_2)
    for a in arg_3:
        print('arg_3 value:', a)

example_function2(1,2)
example_function2(1,2,3)
example_function2(1,2,3,4)
example_function2(1,2,3,4,5)

# Adder Function

def adder(n_1, n_2, *nums):
    # This function adds the given numbers together,
    #   and prints the sum.

    # Start by adding the first two numbers, which will always be present.
    sum = n_1 + n_2

    # Then add any other numbers that were sent.
    for num in nums:
        sum = sum + num

    print('The sum of your numbers is %d' % sum)

adder(1,2,3,4,5,6,7,8,9,10,11,12)
        