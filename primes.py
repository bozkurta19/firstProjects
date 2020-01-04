from time import time
from math import ceil


def primes(rng):
    print(2)

    check_primes = list()

    rng_lim = ceil(rng ** (1 / 2))

    for num in range(3, rng_lim, 2):
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

            check_primes.append(num)

    if rng_lim % 2 == 0:
        rng_lim += 1

    for num in range(rng_lim, rng, 2):
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

primes(10000)

finish = time()

print("Time : {:.3f}".format(finish - start))
