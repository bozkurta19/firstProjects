"""
Problem :
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from time import time


def func():
    for c in range(1, 999):
        for b in range(1, c):
            a = 1000 - b - c

            """
            (a + b + c)^2 = 1000^2
            a^2 + b^2 + c^2 + 2.a.b + 2.a.c + 2.b.c = 1000000
            2c^2 + 2.a.b + 2.a.c + 2.b.c = 1000000
            c(a + b + c) + ab = 500000
            since a + b + c = 1000
            a.b + 1000c = 500000"""

            if b > a and a * b + 1000 * c == 500000:
                return a, b, c


start = time()

print(func())

end = time()

print("Time : {}".format(end - start))
