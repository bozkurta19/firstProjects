"""
Problem :
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from time import time


def func(lim):
    # starting off with 1
    num = 1

    for i in range(1, lim + 1):
        plus = num
        while num % i != 0:
            # adding the number to itself to get higher multiples
            num += plus

    return num


start = time()

print(func(20))

end = time()

print("Time : {:.3f}".format(end - start))
