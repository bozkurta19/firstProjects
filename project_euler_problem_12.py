from time import time


def bolen_sayisi(num):
    bolen_sayisi = 2

    sqrt = num ** (1/2)
    lim = int(sqrt) + 1

    if sqrt == int(sqrt):
        bolen_sayisi -= 1

    for i in range(2,lim):
        if num % i == 0:
            bolen_sayisi += 2

    return bolen_sayisi


start = time()

n = 0
number_of_factors = 0
while not number_of_factors > 500:
    n += 1

    if n % 2 == 0:
        number_of_factors = bolen_sayisi(n/2) * bolen_sayisi(n+1)

    else:
        number_of_factors = bolen_sayisi(n) * bolen_sayisi((n+1)/2)

end = time()

print(int((n * (n + 1)) / 2))
print("Süre : {:.3f}".format(end - start))