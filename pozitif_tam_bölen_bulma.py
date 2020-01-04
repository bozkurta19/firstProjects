from time import time


def bolenleri_bul(num):
    bolenler = {1,num}

    lim = int(num ** (1 / 2)) + 1

    for i in range(2,lim):
        if num % i == 0:
            bolenler.add(i)
            bolenler.add(int(num / i))

    bolenler = list(bolenler)
    bolenler.sort()

    return bolenler


print("""Pozitif Tam Bölen Bulma

(Çýkmak için \"q\" yazýnýz.)
""")

while True:

    sayi = input("Sayý : ")

    if sayi == "q":
        print("Program Sonlandýrýlýyor...")
        break

    elif int(sayi) <= 0:
        print("Geçerli sayý giriniz")

    else:
        baslangic = time()

        print("Pozitif tam bölenleri :",bolenleri_bul(int(sayi)))

        bitis = time()

        print("Süre : {:.3f}\n".format(bitis - baslangic))