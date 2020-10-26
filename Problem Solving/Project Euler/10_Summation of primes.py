# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below n.


def primeSummation(num):
    sum = 0
    for i in range(2, num):
        if isPrime(i):
            sum = sum + i
    return sum


def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(primeSummation(2000000))
