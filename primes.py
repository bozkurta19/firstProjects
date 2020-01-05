from time import time
from math import ceil


def primesTill(n):
    print(2)

    check_primes_lim = ceil(n ** (1 / 2))

    # making a list to check the numbers above check_primes_lim faster
    check_primes = list()

    for num in range(3, check_primes_lim, 2):
        is_prime = True

        # shortening the process with not checking numbers above lim
        lim = num ** (1 / 2)

        for i in check_primes:

            if i > lim:
                break

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)

            check_primes.append(num)

    # trying to start with an odd number
    if check_primes_lim % 2 == 0:
        check_primes_lim += 1

    for num in range(check_primes_lim, n, 2):
        is_prime = True

        lim = num ** (1 / 2)

        for i in check_primes:
            if i > lim:
                break

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)


start = time()

primesTill(100000)

finish = time()

print("Time : {:.3f}".format(finish - start))
