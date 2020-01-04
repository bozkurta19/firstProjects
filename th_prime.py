#Kümülatif ve limitli
def inci_asal3(asal_sirasi):

    if asal_sirasi == 1:
        return 2

    sayi = 1
    asallar = list()

    while  len(asallar) != asal_sirasi - 1:

        asal_mi = True
        sayi += 2

        for i in asallar:

            if i**2 > sayi:
                break

            if sayi % i == 0:
                asal_mi = False
                break

        if asal_mi:
            asallar.append(sayi)

    return sayi

#En hýzlýsý (Sieve of Erathosthenes)
def inci_asal4(asal_sirasi):
    def is_prime(sayi):
        if sayi % 2 == 0:
            return False

        else:
            limit = int(sayi ** (1/2)) + 1

            for i in range(3,limit,2):
                if sayi % i == 0:
                    return False

            return True


    def upper_bound_for_p_n(n):
        if n < 6:
            return 12

        else:
            return int(n * (log(n) + log(log(n))))


    def find_primes_under(num):
        primes = set(range(3,num,2))
        primes.add(2)

        lim = ceil(num ** (1 / 2))

        for i in range(3,lim,2):
            if is_prime(i):
                for delete in range(i * i,num,i * 2):
                    primes.discard(delete)

        return primes


    primes = find_primes_under(upper_bound_for_p_n(asal_sirasi))

    primes = list(primes)

    primes.sort()

    return primes[asal_sirasi - 1]


start = time()

result = inci_asal4(10001)

end = time()

print("Sonuç : {}".format(result))
print("Süre : {}".format(end - start))