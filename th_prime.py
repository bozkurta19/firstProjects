from math import log, ceil
from time import time


# the simplest and slowest method
def thPrime1(n):
    # starting off with 1
    num = 1
    prime_order_of_num = 0

    while prime_order_of_num != n:

        num += 1
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_order_of_num += 1

    return num


# with limit and without even numbers
def thPrime2(n):
    if n == 1:
        return 2

    num = 1

    # setting "prime_order_of_num" since we already used 2
    prime_order_of_num = 1

    while prime_order_of_num != n:

        is_prime = True
        num += 2

        # checking the square root of num and number below to shorten the process
        lim = int(num ** (1 / 2)) + 1

        for i in range(3, lim, 2):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_order_of_num += 1

    return num


# cumulative and with limit
def thPrime3(n):
    if n == 1:
        return 2

    num = 1
    primes = list()

    # because we didn't add 2 to primes list
    while len(primes) != n - 1:

        is_prime = True
        num += 2

        for i in primes:

            if i ** 2 > num:
                break

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return num


# Sieve of Erathosthenes (fastest)
def thPrime4(n):
    def isPrime(num):

        # ignored 2 since we're not gonna check it
        if num % 2 == 0:
            return False

        else:
            lim = int(num ** (1 / 2)) + 1

            for i in range(3, lim, 2):
                if num % i == 0:
                    return False

            return True

    def upperBoundFor(n):
        if n < 6:
            return 12

        else:
            return int(n * (log(n) + log(log(n))))

    def findPrimesUnder(num):

        # using a set in case of discarding the same number again
        # ignoring even numbers
        primes = set(range(3, num, 2))
        primes.add(2)

        lim = ceil(num ** (1 / 2))

        for i in range(3, lim, 2):
            if isPrime(i):

                # i * 2 because we don't use any even number in the loop.
                for j in range(i * i, num, i * 2):
                    primes.discard(j)

        return primes

    primes = findPrimesUnder(upperBoundFor(n))

    primes = list(primes)

    primes.sort()

    # because of indexing
    return primes[n - 1]


while True:
    order_of_prime = int(input("Order of the prime : "))

    start = time()

    result = thPrime4(order_of_prime)

    end = time()

    print("\nResult : {}".format(result))
    print("Time : {}\n".format(end - start))
