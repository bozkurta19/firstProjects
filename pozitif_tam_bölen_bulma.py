from time import time


def findDivisors(num):
    divisors = {1, num}

    lim = int(num ** (1 / 2)) + 1

    for i in range(2, lim):
        if num % i == 0:
            divisors.add(i)
            divisors.add(int(num / i))

    divisors = list(divisors)
    divisors.sort()

    return divisors


print("""Pozitif Tam Bölen Bulma

(Çıkmak için \"q\" yazınız.)
""")

while True:

    num = input("Sayı : ")

    if num == "q":
        print("Program Sonlandırılıyor...")
        break

    elif int(num) <= 0:
        print("Geçerli sayı giriniz")

    else:
        start = time()

        print("Pozitif tam bölenleri :", findDivisors(int(num)))

        end = time()

        print("Süre : {:.3f}\n".format(end - start))
