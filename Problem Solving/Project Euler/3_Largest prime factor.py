# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the given number?


def largest_prime_factor(num):
    largest_num = num
    if num <= 3:
        return num

    if num % 2 == 0:
        largest_num = 2
        while num % 2 == 0:
            num = num // 2

    ele = 3
    while ele <= num:
        if num % ele == 0:
            num //= ele
            largest_num = ele
        else:
            ele += 2
    return largest_num


print(largest_prime_factor(600851475143))
