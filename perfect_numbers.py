from time import time


def isPerfect(num):
    sum_of_divisors = 1

    sqrt = num ** (1 / 2)
    lim = int(sqrt) + 1

    # subtracting the square root if the number is a perfect square not to add the square root 2 times in the for loop
    if sqrt == int(sqrt):
        sum_of_divisors -= sqrt

    for i in range(2, lim):
        if num % i == 0:
            sum_of_divisors += i + num / i

    return sum_of_divisors == num


print("Perfect numbers : ")

start = time()

for i in range(1, 100000):
    if isPerfect(i):
        print(i)

end = time()
print("Süre : {:.3f}".format(end - start))
