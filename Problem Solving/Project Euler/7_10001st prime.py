# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the nth prime number?


def nthPrime(num):
    counter = num
    i = 2
    x = 0
    while x < counter:
        if isPrime(i):
            prime = i
            x += 1
            i += 1
        else:
            i += 1
    return prime


def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(nthPrime(10001))
