from time import time

def mukemmel_mi(num):
    bolenler_toplami = 1

    sqrt = num ** (1/2)
    lim = int(sqrt) + 1

    if sqrt == int(sqrt):
        bolenler_toplami -= sqrt

    for i in range(2,lim):
        if num % i == 0:
                bolenler_toplami += i + num / i

    return bolenler_toplami == num

print("Mükemmel sayýlar : ")

baslangic = time()

for i in range(1,100000):
    if mukemmel_mi(i):
        print(i)

bitis = time()

print("Süre : {:.3f}".format(bitis - baslangic))