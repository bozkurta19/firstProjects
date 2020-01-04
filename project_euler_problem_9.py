from time import time

def function():
    for c in range(1,999):
        for b in range(1,c):
            a = 1000 - b - c

            if b > a and a * b + 1000 * c == 500000:
                return a,b,c


baslangic = time()

print(function())

bitis = time()

print("Süre : {}".format(bitis - baslangic))