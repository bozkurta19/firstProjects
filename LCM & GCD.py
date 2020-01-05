from time import time


# LCM (EKOK in Turkish) stands for "Least Common Multiple"
# GCD (EBOB in Turkish) stands for "Greatest Common Divisor"

# with trying
def GCD_v1(x, y):
    large = max(x, y)
    small = min(x, y)

    if large % small == 0:
        return small

    lim = small // 2

    # Only checking "small" / 2 and integers below cause higher ones can't divide "small" without any remainder.
    for i in range(lim, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


# with Euclidean algorithm (fastest)
def GCD_v2(x, y):
    dividend = max(x, y)
    divisor = min(x, y)

    # using booleans
    while dividend % divisor:
        dividend, divisor = divisor, (dividend % divisor)

    return divisor


# with LCM - GCD relation
def LCM_v1(x, y):
    return (x * y) / GCD_v1(x, y)


def LCM_v2(x, y):
    return (x * y) / GCD_v2(x, y)


# with trying
def LCM_v3(x, y):
    large = max(x, y)
    small = min(x, y)

    # starting off with larger number
    num = large

    # using booleans again and adding larger number to shorten the process
    while num % small:
        num += large

    return num


print("LCM & GCD Finder")

while True:
    x = int(input("First number : "))
    y = int(input("Second number : "))

    start = time()

    print("Result : {}".format(GCD_v2(x, y)))

    end = time()

    print("Time : {:.3f}\n".format(end - start))
