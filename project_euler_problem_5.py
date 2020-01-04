from time import time

def func(lim):
    num = 1

    for i in range(1,lim + 1):
        plus = num
        while num % i != 0:
            num += plus

    return num

start = time()

print(func(21))

end = time()

print("Süre : {:.3f}".format(end - start))