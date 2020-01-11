def isPrime(num):
    # shortening the process
    if num == 2:
        return True

    elif num % 2 == 0:
        return False

    elif num > 1:

        # only checking square root of the number and below to shorten the process
        lim = int(num ** (1 / 2)) + 1

        for i in range(3, lim, 2):
            if num % i == 0:
                return False

        return True

    else:
        return False


if __name__ == '__main__':
    print("Checking the Number If It Is Prime\n")
    while True:
        try:
            num = int(input("The number to check  : "))

            if isPrime(num):
                print("Prime\n")

            else:
                print("Not prime\n")

        except:
            print("Write number")


