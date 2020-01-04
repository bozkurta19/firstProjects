from time import time


# LCM (EKOK in Turkish) stands for "Least Common Multiple"
# GCD (EBOB in Turkish) stands for "Greatest Common Divisor"

# Deneme ile
def EBOB_v1(x, y):
    buyuk = max(x, y)
    kucuk = min(x, y)

    if buyuk % kucuk == 0:
        return kucuk

    limit = kucuk // 2

    for i in range(limit, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


# EBOB algoritmasý ile (en hýzlýsý)
def EBOB_v2(x, y):
    bolunen = max(x, y)
    bolen = min(x, y)

    while bolunen % bolen:
        bolunen, bolen = bolen, (bolunen % bolen)

    return bolen


# EKOK - EBOB baðýntýsýný kullanarak
def EKOK_v1(x, y):
    return (x * y) / EBOB_v1(x, y)


def EKOK_v2(x, y):
    return (x * y) / EBOB_v2(x, y)


# Deneme ile
def EKOK_v3(x, y):
    buyuk = max(x, y)
    kucuk = min(x, y)

    sayi = buyuk

    while sayi % kucuk:
        sayi += buyuk

    return sayi


while True:
    x = int(input("1. Sayý : "))
    y = int(input("2. Sayý : "))

    baslangic = time()

    print("Sonuç : {}".format(EKOK_v2(x, y)))

    bitis = time()

    print("Süre : {:.3f}\n".format(bitis - baslangic))
