def divisors(number):

    list_of_divisors = []
    test_n = 2
    n = number

    while test_n != n + 1:
        if n % test_n == 0:
            list_of_divisors.append(test_n)
        test_n = test_n + 1

    if len(list_of_divisors) == 1:
        return '%s is prime' % str(n)
    else:
        list_of_divisors.remove(n)
        return list_of_divisors

    test_n = 2